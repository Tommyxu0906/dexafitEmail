"""
segment.py: clean, classify, score, dedupe, and flag the raw lead list.

Reads data/leads_raw.csv and config/campaign.yaml, writes data/leads_segmented.csv.
No row is ever dropped. Exclusion is a flag, not a delete, so the whole list stays
auditable in the committed CSV. Runs with no arguments: python src/segment.py
"""

import re
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "leads_raw.csv"
OUT = ROOT / "data" / "leads_segmented.csv"
CONFIG = ROOT / "config" / "campaign.yaml"

# The 8 fields counted for dedupe completeness. Highest completeness wins a tie.
DEDUPE_FIELDS = ["full_name", "email", "job_title", "practice_name",
                 "city", "state", "website", "notes"]
# The core fields that make a lead sendable. Notes is optional, so it is not here.
CORE_FIELDS = ["full_name", "email", "job_title", "practice_name",
               "city", "state", "website"]

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Practice names that read as a clinic or medical group. Used both as a fallback
# clinical signal and as the multi provider signal for scoring.
CLINICAL_PRACTICE_WORDS = ["medical", "internal medicine", "family medicine",
                           "primary care", "clinic", "bariatric", "sports medicine"]
MULTI_PROVIDER_WORDS = ["group", "partners", "associates", "collective",
                        "center", "institute", "clinic", "medicine", "practice"]


def classify(job_title, practice_name):
    """Return (profession, confidence). Categories are routing buckets, not job
    titles: a Physician Assistant is not a physician but gets the clinical value
    prop, so it lands in `clinical`. Checked in order, so nutrition and fitness
    title signals win before the clinical practice name fallback (a dietitian at a
    medical group stays nutrition).
    """
    title = (job_title or "").strip().lower()
    practice = (practice_name or "").strip().lower()
    tokens = set(re.findall(r"[a-z]+", title))

    nutrition_high = (
        tokens & {"rd", "rdn"}
        or any(p in title for p in
               ["registered dietitian", "dietitian", "nutritionist", "nutrition coach"])
    )
    fitness_high = (
        "cpt" in tokens
        or any(p in title for p in
               ["personal trainer", "strength coach", "performance coach", "trainer"])
    )
    clinical_high_title = (
        tokens & {"md", "do", "np"}
        or "physician assistant" in title
        or "nurse practitioner" in title
    )

    if nutrition_high:
        return "nutrition", "high"
    if fitness_high:
        return "fitness", "high"
    if clinical_high_title:
        return "clinical", "high"
    if any(w in practice for w in CLINICAL_PRACTICE_WORDS):
        return "clinical", "high"
    if "health coach" in title:
        # Ambiguous by nature. A health coach may or may not do nutrition work,
        # so it sends with a generic opener rather than a nutrition specific one.
        return "nutrition", "low"
    if "director of performance" in title:
        supports_fitness = any(w in practice for w in
                               ["perform", "strength", "athletic", "sport", "fitness"])
        if supports_fitness:
            return "fitness", "low"
        return "unclassified", "n/a"
    # Founder, Owner, Wellness Director, or anything else with no other signal.
    return "unclassified", "n/a"


def valid_email(email):
    return bool(EMAIL_RE.match((email or "").strip().lower()))


def completeness(row, fields):
    return sum(1 for f in fields if str(row.get(f, "")).strip() != "")


def dedupe(df):
    """Return {lead_id: canonical_lead_id} for every duplicate loser. Group valid
    email rows by normalized email. Highest completeness wins, ties break to the
    lowest lead_id. Losers are flagged, never removed.
    """
    losers = {}
    df = df.copy()
    df["_email_norm"] = df["email"].str.strip().str.lower()
    df["_valid"] = df["email"].apply(valid_email)
    for email_norm, group in df[df["_valid"]].groupby("_email_norm"):
        if len(group) < 2:
            continue
        ranked = sorted(
            group.itertuples(index=False),
            key=lambda r: (-completeness(r._asdict(), DEDUPE_FIELDS), r.lead_id),
        )
        canonical = ranked[0].lead_id
        for r in ranked[1:]:
            losers[r.lead_id] = canonical
    return losers


def score(row, weights):
    """Raw additive intent score, capped at 100. Driven by relationship and intent,
    never by provider type. Raw weights sum to 125, so the cap bites the top leads.
    """
    raw = 0
    if str(row["notes"]).strip():
        raw += weights["existing_relationship"]
    if row["source"] == "inbound_form":
        raw += weights["inbound_form"]
    if row["source"] == "partner_referral":
        raw += weights["partner_referral"]
    if row["market_tier"] == "launch":
        raw += weights["launch_market"]
    if any(w in str(row["practice_name"]).lower() for w in MULTI_PROVIDER_WORDS):
        raw += weights["multi_provider_signal"]
    if completeness(row, CORE_FIELDS) == len(CORE_FIELDS):
        raw += weights["complete_profile"]
    if row["profession_confidence"] == "high":
        raw += weights["high_classification_confidence"]
    return min(raw, 100)


def main():
    with open(CONFIG) as f:
        config = yaml.safe_load(f)

    markets = {(m["city"].lower(), m["state"].lower()) for m in config["launch_markets"]}
    weights = config["scoring_weights"]
    exclude_waitlist = config["pilot"]["exclude_waitlist_markets"]

    # keep_default_na=False so blank cells stay "" strings, not NaN.
    df = pd.read_csv(RAW, dtype=str, keep_default_na=False)

    professions, confidences = [], []
    for _, row in df.iterrows():
        prof, conf = classify(row["job_title"], row["practice_name"])
        professions.append(prof)
        confidences.append(conf)
    df["profession"] = professions
    df["profession_confidence"] = confidences

    # temperature. inbound_form is deliberately not warm: an inbound enquiry about
    # scans says nothing about interest in a provider marketplace.
    df["temperature"] = df.apply(
        lambda r: "warm" if (str(r["notes"]).strip()
                             or r["source"] in ("partner_referral", "event_signup"))
        else "cold",
        axis=1,
    )
    df["market_tier"] = df.apply(
        lambda r: "launch" if (r["city"].strip().lower(), r["state"].strip().lower()) in markets
        else "waitlist",
        axis=1,
    )
    df["priority_score"] = df.apply(lambda r: score(r, weights), axis=1)
    df["template_key"] = df["profession"]
    df["campaign_track"] = df["temperature"] + "_" + df["market_tier"]

    losers = dedupe(df)

    def exclusion(row):
        # Precedence: data validity, then dedupe, then classification, then market.
        if not valid_email(row["email"]):
            return "missing_email"
        if row["lead_id"] in losers:
            return "duplicate_of:" + losers[row["lead_id"]]
        if row["profession"] == "unclassified":
            return "unclassified_profession"
        if row["market_tier"] == "waitlist" and exclude_waitlist:
            return "outside_launch_market"
        return ""

    df["excluded_reason"] = df.apply(exclusion, axis=1)

    ordered = ["lead_id"] + [c for c in df.columns if c != "lead_id"]
    df[ordered].to_csv(OUT, index=False)

    print_summary(df)


def print_summary(df):
    def block(title, series):
        print(title)
        # Sort by count descending, then label ascending. value_counts leaves the
        # order of tied counts unspecified, which made this summary vary between
        # runs. The README quotes this output verbatim, so it has to be stable.
        for k, v in sorted(series.items(), key=lambda kv: (-kv[1], str(kv[0]))):
            label = k if str(k).strip() else "(blank)"
            print("  {:<28} {}".format(label, v))
        print()

    sendable = df[df["excluded_reason"] == ""]
    print("=" * 52)
    print("SEGMENTATION SUMMARY")
    print("=" * 52)
    print("Total leads in: {}".format(len(df)))
    print("Sendable this campaign: {}".format(len(sendable)))
    print("Excluded: {}".format(len(df) - len(sendable)))
    print()
    block("By profession (all rows):", df["profession"].value_counts())
    block("By classification confidence:", df["profession_confidence"].value_counts())
    block("By temperature:", df["temperature"].value_counts())
    block("By market tier:", df["market_tier"].value_counts())

    reasons = df[df["excluded_reason"] != ""]["excluded_reason"]
    # Collapse duplicate_of:<id> into one bucket for the summary count.
    collapsed = reasons.apply(lambda r: "duplicate_of" if r.startswith("duplicate_of") else r)
    block("Exclusions by reason:", collapsed.value_counts())


if __name__ == "__main__":
    main()
