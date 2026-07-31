# DexaFit Provider Marketplace: Structure, Pricing, and Provider Acquisition

Tommy Xu | Prepared for Hamza Masaeed and Adam | July 2026

**Working repo:** github.com/Tommyxu0906/dexafitEmail

---

## 1. What DexaFit is actually selling

The asset is not a directory. It is the ninety seconds after a client sees their body composition results and asks "okay, now what?"

That moment is rare and expensive to manufacture. A nutritionist running paid ads is buying attention from someone who might want to change their body. DexaFit can hand that same nutritionist a person who has already paid to measure their body, already sat through the results conversation, and is actively asking what to do next.

So the product is not a listing. It is **one provider at a time, non auctioned routing of a qualified, data attached, high intent referral at the moment of decision.** Every decision below follows from that.

The practical consequence, and the theme of this memo: **our binding constraint is referral supply, not provider demand.** There are far more providers who want clients than there are scans producing referrals.

**Assumptions.** I did not have DexaFit's scan volume, opt in rate, or existing referral behavior, so I parameterized those. Everything else comes from public benchmarks and is named. Give me the real numbers and I will rerun the model.

---

## 2. Pricing: what a referral is worth

**What a provider earns from one client.** Private practice nutrition sessions run $75 to $175, with industry data putting average treatment value near $155. Engagements last three to six months. Six sessions at $150 is a lifetime value near **$900**, with a realistic band of $600 to $1,500. Trainers and physicians sit elsewhere, but the method is the same.

**What they can pay to get one.** Service businesses stay healthy at a customer acquisition cost of 20 to 30 percent of lifetime value. At $900, that is **$180 to $270 per acquired client.**

**What competing channels charge.**

| Channel | Model | Price | Structural weakness |
|---|---|---|---|
| Thumbtack | Pay per lead | $15 to $80, dynamic | Same lead sold to three to five pros. Everyone pays, one books. |
| Zocdoc | Subscription plus per booking | $35 to $110 per new patient | Quoted individually, not public. Unpredictable budgeting. |
| Opencare (dental) | Per matched patient | $200 to $400 | Narrow category |

**Where a DexaFit referral lands.** It is a better unit than a pay per lead introduction on three counts. Routing is one provider at a time and non auctioned, rather than the same lead sold to five. With the client's permission it arrives with a secure scan summary, so the provider opens holding a baseline instead of asking intake questions. And the timing is precise, because the person is asking the question right now.

If the first provider declines or does not respond within the acceptance window, the referral may be routed to the next qualified match. The commitment is that a referral is never auctioned to several providers at once, not that a provider holds a permanent territory.

Using a one in three conversion rate as a working assumption, a provider who can spend $180 to $270 per acquired client can pay **$60 to $90 per referral** and stay well inside a healthy CAC. Treat that as an initial test range rather than a settled price. It sits above Thumbtack, inside Zocdoc's band, and is defensible in a sales conversation because the provider can do the arithmetic themselves.

---

## 3. The model: performance first, subscription second

A $99 per month listing is easy to justify on paper. At $900 lifetime value a provider needs slightly more than one new client a year to break even. The arithmetic is not the obstacle. **Belief is.** No provider has seen a DexaFit referral yet, so a monthly fee asks them to pay for volume we cannot prove. Charging subscription before we have conversion data is the most common way early marketplaces stall: supply signs up, sees nothing, and churns loudly.

**Phase 1, first 90 days.** No listing fee. $60 per accepted referral, invoiced monthly. The provider carries zero risk and pays only for something real. DexaFit gets what it actually needs, which is conversion data by category and market.

**Phase 2, after 90 days.** Convert the cohort with their own numbers in hand. "Last quarter you accepted nine referrals and paid $540." Featured combines a monthly platform fee with direct routing eligibility and preferred referral pricing. The final packaging should be based on pilot conversion and capacity data. They are not being sold a promise, they are being offered better terms on something they already buy.

Phase 1 generates the evidence needed for Phase 2. It is sales sequencing, not a pricing concession.

**The tiers we convert them to:**

| Tier | Price | What it buys | Who it is for |
|---|---|---|---|
| **Verified** | Free | Vetted profile, appears in relevant match results, credential badge | Supply base. Keeps the directory dense enough to be useful. |
| **Featured** | $99 / mo or $999 / yr, plus per referral | Priority placement, expanded profile, booking link, direct routing eligibility, preferred referral pricing, performance dashboard | The core paid product. Post pilot, most revenue sits here. |
| **Partner** | From $249 / mo | Multi provider or multi location, first look routing in a defined category and market, co marketing | Clinics and larger practices. The natural home for category and market priority agreements. |

Two boundaries matter. **Free does not include routing.** Verified providers appear in results but receive no routed referrals, because the paid product is the routing, not the visibility. If free providers get referrals, nobody upgrades. **Paid placement never overrides fit.** Matching ranks on relevance first, meaning specialty, goal, geography, and credentials. Paid tiers break ties and boost position within the relevant set. They cannot surface an irrelevant provider. DexaFit's brand is why clients trust the recommendation, and a bad match damages the scan business, not just the marketplace.

---

## 4. Launch scope: cap the supply side deliberately

This is the point I would push hardest on.

Referral supply is set by scan volume. If we sell 200 Featured subscriptions in Boston while producing a few dozen routable referrals a month, most providers receive nothing and churn while telling other providers it did not work. Provider demand is easy to fill. **Filling it is the failure mode.**

So cap provider density per market per category, and use the cap as the pitch. "We are accepting eight metabolic health providers in Boston" is both operationally correct and the strongest line available in a cold email. The scarcity is real rather than manufactured, which is why it holds up under questioning.

Launch narrow: fat loss nutrition, metabolic health, sports performance, and post scan strength programming, in one or two markets with the highest scan volume. Recruit 50 to 100 applicants, approve a qualified provider pool, and activate only the number supported by current referral volume. **The initial active cohort may be closer to 15 to 25 providers.** Recruiting and activation are separate numbers on purpose: an approved pool that exceeds live capacity is a queue we can draw from as scan volume grows, not a promise we have already broken.

---

## 5. Provider acquisition: working the 1,000 leads

**Segmentation, applied in this order.** Profession first, since the value proposition differs: nutritionists want clients who arrive with data, trainers want measurable goals and rescan driven retention, physicians and clinics want continuity of care, meaning a client they already hold data on routed back for follow up. The clinical track also uses a different call to action, since a physician referral decision is not made by booking a fifteen minute call. Then relationship temperature, warm versus cold. Warm leads receive a relationship specific opener and higher manual review priority. Then market priority, since leads outside launch markets go into a waitlist sequence that also reinforces the density cap.

Sending one campaign to all 1,000 would waste the list and, more importantly, generate demand we cannot fulfill.

**Sequence: three emails, not five.** The offer is good enough that it does not need six weeks of nurture, and a short sequence lets us work the list and learn faster.

| Email | Timing | Job |
|---|---|---|
| E1 | Day 0 | The offer in five lines. One provider at a time referrals, no listing fee, $60 per accepted referral, capped cohort. |
| E2 | Day 3 | Make it concrete. What one referral actually looks like. |
| E3 | Day 8 | Short close with a low friction out. |

**The call to action is not "pay now."** It is "apply to the founding cohort." We are collecting interest, objections, and willingness to pay, and we cannot optimize checkout for a product whose volume we have not yet proven.

**What "accepted referral" means**, since the $60 attaches to it: the client has opted in, the provider has reviewed the referral summary and agreed to the introduction, and DexaFit has released the contact information through the approved workflow. A provider is never billed for a referral they declined or never saw.

**Personalization.** Merge fields drive the copy: profession, city, specialty, nearest DexaFit location, and existing relationship. Low confidence personalization and the highest priority accounts receive manual review. No lead receives more than three touches. The repo implements this end to end.

---

## 6. Measurement

**Acquisition:** positive reply rate by segment, application rate, meetings booked, approved provider rate meaning applications that clear vetting, and paid conversion at day 90. I would not report open rate. Since mail privacy protection it mostly measures image proxy prefetching, and optimizing subject lines against it produces false winners.

**Marketplace health:** referrals routed per provider per month, provider response time to a routed referral, referral to booked appointment rate, referral to paying client rate, and client satisfaction with the match.

The single most important early number is **referrals per provider per month.** Below roughly two, the paid tier stops making sense to the provider and churn follows regardless of how good the product is.

**What the 1,000 leads are worth.** Planning assumptions, not forecasts. Every rate below is a guess until we have sent the first two hundred emails.

| Stage | Conservative | Base | Upside |
|---|---|---|---|
| Total leads | 1,000 | 1,000 | 1,000 |
| Valid and classified | 850 | 850 | 850 |
| In launch markets, sent this campaign | 600 | 600 | 600 |
| Positive reply rate | 6% | 12% | 20% |
| Interested providers | 36 | 72 | 120 |
| Clear vetting and fit | 25 | 50 | 80 |
| Paying at day 90 | 8 | 20 | 35 |
| First cohort ARR at $99 | ~$9.5k | ~$23.8k | ~$41.6k |

**The first 1,000 leads are a validation cohort, not the full revenue opportunity.** Even the upside case is under $50k ARR. These leads are worth working because they produce the first cohort and the objection data that tells us whether the model works, not because they are a revenue event.

**The base case already sits at the capacity ceiling.** Twenty paying providers each needing at least two referrals a month is forty routed referrals a month. Whether DexaFit can produce that is a function of scan volume and post scan opt in rate, not of how well the outreach performs. **The funnel tells us how many providers we can sign, and scan volume tells us how many we can keep.** If those two numbers disagree, the outreach should be throttled, not accelerated. This is the first thing I would check against real data.

---

## 7. Recommendation

Do not build the full marketplace before launch. Recruit 50 to 100 applicants in one or two markets, approve a qualified pool, and activate only what current referral volume supports, likely 15 to 25 providers to start. Price at no listing fee plus $60 per accepted referral for 90 days, and use the outreach conversations themselves as the pricing research.

Three questions the pilot should answer before anything scales:

1. Which provider types do clients actually choose when given a real recommendation?
2. What will providers pay for, specifically: placement, priority routing, non auctioned referrals, or data?
3. Can DexaFit generate enough referral volume per provider to retain a paid tier at all?

Question three decides the right scale and monetization model for the marketplace. Everything in this plan is built to answer it in ninety days rather than nine months.

---

## Appendix. Sample email and repo

E1 below is the cold nutritionist version. E2 and E3, the trainer and physician variants, and fifteen fully rendered examples are in the repo. Braces are merge fields.

*Subject A:* Referrals from {location} clients who already have their body comp data
*Subject B:* Eight nutritionist slots in {city}

Testing specific mechanism versus scarcity.

> Hi {first_name},
>
> I work with DexaFit, the body composition and metabolic testing clinics. {location} runs DEXA, RMR, and VO2 max scans, and after every one of them the client asks some version of "okay, so what do I do now?"
>
> Right now we mostly say "find a good nutritionist." We are changing that. We are building a small vetted group we route those clients to directly. With the client's permission, you receive their stated goal and a secure scan summary before the first conversation.
>
> No listing fee during the pilot. You pay only when you accept a referral, and each one goes to one provider at a time rather than to five people at once.
>
> We are taking eight nutritionists in {city}. Worth fifteen minutes?
>
> Tommy

**The repo** contains segmentation and prioritization rules, personalization field generation, templates for all three provider categories, and a sample run over fifty mock leads with output committed so it reads without running anything. I built it on mock data because I do not have the real list. That list will have a different schema and its own quality issues, but mapping it in is a short exercise and the segmentation and personalization logic carries over unchanged.

**Deliberately out of scope**, to be decided with data and specialist input rather than guessed at now: client consent design, secure health data sharing, and privacy and compliance review, all of which gate any real referral; provider vetting and credential verification; payment and invoicing infrastructure; the client facing matching interface; full pricing by profession, since trainer and physician economics need their own derivation; and deliverability setup such as domain warming and list validation, which is execution rather than strategy.
