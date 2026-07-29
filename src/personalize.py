"""
personalize.py: generate the merge field values each email needs.

Reads data/leads_segmented.csv and config/campaign.yaml, writes
data/leads_personalized.csv. The opener is the one genuinely personalized line. A
deterministic rules engine produces it here so the workflow runs with no API key,
but the exact model prompt payload is built by build_opener_prompt() (shown in the
README). Runs with no arguments: python src/personalize.py
"""

from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
SEG = ROOT / "data" / "leads_segmented.csv"
OUT = ROOT / "data" / "leads_personalized.csv"
CONFIG = ROOT / "config" / "campaign.yaml"

SPECIALTY_HINTS = [
    ("sports nutrition", "sports nutrition"),
    ("sports medicine", "sports medicine"),
    ("metabolic", "metabolic health"),
    ("bariatric", "metabolic and weight work"),
    ("performance", "performance work"),
    ("strength", "strength work"),
]

CATEGORY_NOUN = {
    "nutrition": "nutrition providers",
    "fitness": "coaches",
    "clinical": "clinics",
}


def first_name(full_name):
    parts = (full_name or "").strip().split()
    return parts[0] if parts else "there"


def nearest_location(row, markets):
    key = (row["city"].strip().lower(), row["state"].strip().lower())
    return markets.get(key, {}).get("location_name", "Future market")


def slots_remaining(row, markets):
    key = (row["city"].strip().lower(), row["state"].strip().lower())
    m = markets.get(key)
    return str(m["slots_remaining"]) if m else ""


def specialty_of(practice_name):
    practice = (practice_name or "").lower()
    for hint, label in SPECIALTY_HINTS:
        if hint in practice:
            return label
    return ""


def build_opener_prompt(lead):
    """Return the exact prompt payload that would go to a model in production. It
    builds and returns the string, it does not call anything. Prompt design is part
    of what is being demonstrated, so this is the real payload, not a sketch.
    """
    return (
        "You write the first line of a cold outreach email to a healthcare "
        "provider for DexaFit, a body composition testing company launching a "
        "referral marketplace.\n\n"
        "Rules:\n"
        "- One sentence, under 25 words.\n"
        "- Plain and specific. No adjectives, no flattery, no exclamation marks.\n"
        "- If a relationship note is present, reference it naturally.\n"
        "- Otherwise reference the practice specialty if one is given.\n"
        "- Otherwise reference their city and profession only.\n"
        "- Never invent facts not present in the fields below.\n\n"
        "Provider fields:\n"
        "  first_name: {first_name}\n"
        "  profession: {profession}\n"
        "  practice_name: {practice_name}\n"
        "  city: {city}\n"
        "  relationship_note: {notes}\n"
    ).format(
        first_name=first_name(lead["full_name"]),
        profession=lead["profession"],
        practice_name=lead["practice_name"],
        city=lead["city"],
        notes=lead["notes"] if str(lead["notes"]).strip() else "(none)",
    )


def generate_opener_rules(lead):
    """Deterministic opener generator that populates the CSV. Returns (opener,
    confidence), where confidence is the branch that fired. Low confidence rows are
    the human in the loop boundary: in production those lines get written by hand.
    """
    note = str(lead["notes"]).strip()
    if lead["temperature"] == "warm" and note:
        return ("Picking this back up since we first connected (" + note + ").", "high")

    specialty = specialty_of(lead["practice_name"])
    if specialty:
        return ("Came across " + lead["practice_name"].strip()
                + " and your focus on " + specialty + ".", "medium")

    city = lead["city"].strip() or "your area"
    noun = CATEGORY_NOUN.get(lead["profession"], "providers")
    return ("Reaching out to a few " + noun + " in " + city + ".", "low")


def main():
    with open(CONFIG) as f:
        config = yaml.safe_load(f)
    markets = {(m["city"].lower(), m["state"].lower()): m
               for m in config["launch_markets"]}

    df = pd.read_csv(SEG, dtype=str, keep_default_na=False)

    df["first_name"] = df["full_name"].apply(first_name)
    df["nearest_location"] = df.apply(lambda r: nearest_location(r, markets), axis=1)
    df["slots_remaining"] = df.apply(lambda r: slots_remaining(r, markets), axis=1)

    openers, confidences = [], []
    for _, row in df.iterrows():
        # Only sendable rows get an opener. Excluded rows are retained with blanks
        # so the file stays a complete, auditable record of the whole list.
        if row["excluded_reason"] == "":
            opener, conf = generate_opener_rules(row)
        else:
            opener, conf = "", ""
        openers.append(opener)
        confidences.append(conf)
    df["opener"] = openers
    df["personalization_confidence"] = confidences

    df.to_csv(OUT, index=False)

    sendable = df[df["excluded_reason"] == ""]
    print("Personalized {} sendable leads.".format(len(sendable)))
    print("Personalization confidence on sendable leads:")
    for k, v in sendable["personalization_confidence"].value_counts().items():
        print("  {:<8} {}".format(k, v))
    hand = (sendable["personalization_confidence"] == "low").sum()
    print("{} low confidence openers would be hand written before send.".format(hand))


if __name__ == "__main__":
    main()
