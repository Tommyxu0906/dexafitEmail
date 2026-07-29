# DexaFit Provider Marketplace: Structure, Pricing, and Provider Acquisition

Tommy Xu | Prepared for Hamza Masaeed and Adam | July 2026

**Working repo:** github.com/Tommyxu0906/dexafitEmail

---

## 1. What DexaFit is actually selling

The asset here is not a directory. It is the ninety seconds after a client sees their body composition results and asks "okay, now what?"

That moment is rare and expensive to manufacture. A nutritionist running paid ads is buying attention from someone who might be interested in changing their body. DexaFit can hand that same nutritionist a person who has already paid money to measure their body, already sat through the results conversation, and is actively asking to be told what to do next.

So the product we are selling providers is not a listing. It is **exclusive access to a qualified, data-attached, high-intent referral at the exact moment of decision.** Every pricing and structural decision below follows from that.

The practical consequence: our binding constraint is referral supply, not provider demand. There are far more nutritionists and trainers who want clients than there are scans producing referrals. I will come back to why this should shape the entire launch.

**Assumptions used below.** I did not have DexaFit's scan volume, opt-in rate, or existing referral behavior, so I have parameterized those. Everything else is drawn from public benchmarks and named. Give me the real numbers and I will rerun the model.

---

## 2. Pricing: what a referral is actually worth

### Step 1. What a provider earns from one client

Private practice nutrition sessions run roughly $75 to $175, with industry data putting the average treatment value near $155. Typical client engagements last three to six months. A conservative six sessions at $150 gives a lifetime value of about **$900** per client, with a realistic band of $600 to $1,500. Trainers and physician practices sit at different points but the method is the same.

### Step 2. What they can afford to pay to get one

Service businesses stay healthy at a customer acquisition cost around 20 to 30 percent of lifetime value. At $900 LTV, that is **$180 to $270 per acquired client.**

### Step 3. What competing channels charge

| Channel | Model | Price | Structural weakness |
|---|---|---|---|
| Thumbtack | Pay per lead | $15 to $80, dynamically priced | Same lead sold to three to five pros simultaneously. Everyone pays, one books. |
| Zocdoc | Subscription plus per booking | $35 to $110 per new patient | Pricing quoted individually, not public. Unpredictable budgeting. |
| Opencare (dental) | Per matched patient | $200 to $400 | Narrow category |

### Step 4. Where a DexaFit referral lands

A DexaFit referral is a materially better unit than a Thumbtack lead for three reasons:

1. **It is exclusive.** Routed to one provider, not auctioned to five.
2. **It arrives with objective data.** The provider opens the conversation holding a body composition baseline instead of asking intake questions. Sales cycle shortens, and the first session is more valuable to the client.
3. **The timing is precise.** The person is asking the question right now, not idly browsing.

If we assume roughly one in three referrals converts to a paying client, which is conservative for a warm exclusive introduction, then a provider who can spend $180 to $270 per acquired client can pay **$60 to $90 per referral** and still be well inside a healthy CAC.

That is the number. It sits above Thumbtack, inside Zocdoc's band, and is defensible in a sales conversation because the provider can do the arithmetic themselves.

---

## 3. The model: performance first, subscription second

A $99 per month listing is easy to justify on paper. At $900 LTV, a provider needs slightly more than one new client per year to break even on it. The arithmetic is not the obstacle.

The obstacle is belief. No provider has seen a DexaFit referral yet, so a monthly fee asks them to pay for volume we cannot prove. Charging subscription before we have conversion data is the most common way early marketplaces stall: supply signs up, sees nothing, and churns loudly.

**Recommended structure:**

**Phase 1, first 90 days.** No listing fee. $60 per accepted referral, invoiced monthly. The provider carries zero risk and pays only for something real. DexaFit gets the thing it actually needs, which is conversion data by category and market.

**Phase 2, after 90 days.** Convert the cohort to subscription with their own numbers in hand. "Last quarter you accepted nine referrals and paid $540. The Featured plan is $99 per month with unlimited routing and priority placement." At that point the provider is not being sold on a promise, they are being offered a discount on something they have already bought.

Phase 1 exists to manufacture the proof that makes Phase 2 an easy conversation. It is a sales sequencing decision, not a pricing concession.

---

## 4. Tiers

These are the post pilot prices. The founding cohort receives the Featured workflow with the listing fee waived for 90 days, so the prices below are what we convert them to once they have seen referral volume, not what we open the conversation with.

| Tier | Price | What it buys | Who it is for |
|---|---|---|---|
| **Verified** | Free | Vetted profile, appears in relevant match results, credential badge | Supply base. Keeps the directory dense enough to be useful. |
| **Featured** | $99 / mo or $999 / yr | Priority placement in matched results, expanded profile, booking link, direct routing of inbound referrals, performance dashboard | The core paid product. Post pilot, this is where most revenue sits. |
| **Partner** | From $249 / mo | Multi provider or multi location, first look routing in a defined category and market, co marketing and educational content with DexaFit | Clinics and larger practices. Also the natural home for exclusivity deals. |

Two boundaries that matter:

**What free does not include.** Verified providers appear in results but do not receive routed referrals. The paid product is the routing, not the visibility. If free providers get referrals, nobody upgrades.

**Paid placement never overrides fit.** Matching is ranked on relevance first: specialty, goal alignment, geography, remote availability, credentials. Paid tiers break ties and boost position within the relevant set. They cannot surface an irrelevant provider. DexaFit's brand is the reason clients trust the recommendation, and a client sent to a bad match damages the scan business, not just the marketplace.

---

## 5. Launch scope: cap the supply side deliberately

This is the point I would push hardest on.

Referral supply is finite and set by scan volume. If we sell 200 Featured subscriptions in Boston while producing a few dozen routable referrals per month, most providers receive nothing, and they churn while telling other providers it did not work. Provider demand is easy to fill. Filling it is the failure mode.

**So cap provider density per market per category, and use the cap as the pitch.** "We are accepting eight metabolic health providers in Boston" is both operationally correct and the strongest thing we can say in a cold email. Scarcity here is real, not manufactured, which is why it will hold up under questioning.

**Launch narrow:**
- Categories: fat loss nutrition, metabolic health, sports performance, post scan strength programming
- Geography: start where scan volume is highest, one or two markets
- Cohort: 50 to 100 vetted providers total, not 1,000

---

## 6. Provider acquisition: working the 1,000 leads

### Segmentation

Three cuts, applied in this order:

1. **Profession.** Nutritionist / RD, trainer, physician or clinic. Different value proposition each. Nutritionists want clients who arrive with data. Trainers want measurable goals and repeat scan driven retention. Physicians and clinics want to extend the patient journey without adding staff.
2. **Relationship temperature.** Already connected to a DexaFit location versus cold. Warm leads get a different first line and a much shorter sequence.
3. **Market priority.** Leads inside launch markets go first. Everyone else goes into a waitlist sequence, which also reinforces the density cap.

Sending one campaign to all 1,000 would waste the list and, more importantly, would generate demand we cannot fulfill.

### Sequence design

Three emails, not five. The offer here is genuinely good and does not need six weeks of nurture. A short sequence also lets us get through the list faster and learn faster.

| Email | Timing | Job |
|---|---|---|
| E1 | Day 0 | The offer in five lines. Exclusive referrals, no fee, limited slots. |
| E2 | Day 3 | Make it concrete. Walk through what one referral actually looks like. |
| E3 | Day 8 | Short close with a low friction out. |

Two subject line variants per email, each testing one hypothesis. Full copy in the appendix.

**The call to action is not "pay now."** It is "apply to the founding cohort." We are collecting interest, objections, and willingness to pay, and we cannot optimize checkout for a product whose volume we have not yet proven.

### Personalization

Merge fields drive the copy: profession, city, specialty, practice type, nearest DexaFit location, and whether they have an existing relationship. High value leads, meaning multi provider clinics and anyone in a priority category, get a manually written first line rather than a generated one. Everything else is automated.

---

## 7. Measurement

**Provider acquisition:**
- Positive reply rate, by segment
- Application rate
- Meeting booked rate
- Approved provider rate, meaning applications that clear vetting
- Paid conversion at day 90

I would not report open rate. Since mail privacy protection it mostly measures image proxy prefetching, and optimizing subject lines against it produces false winners.

**Marketplace health, post launch:**
- Referrals routed per provider per month, which is the churn predictor to watch
- Provider response time to a routed referral
- Referral to booked appointment rate
- Referral to paying client rate, self reported at first, then verified
- Client satisfaction with the match

The single most important early number is **referrals per provider per month.** If that falls below roughly two, the paid tier stops making sense to the provider and churn follows regardless of how good the product is.

### What the 1,000 leads are worth

Planning assumptions, not forecasts. Every conversion rate below is a guess until we have sent the first two hundred emails, and the point of the pilot is to replace them with real numbers.

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

Two things this table makes clear.

**First, the list alone is not a business.** Even the upside case is under $50k ARR. The 1,000 leads are worth working because they produce the first cohort and, more importantly, the conversion and objection data that tells us whether the model works. Treating this campaign as a revenue event rather than a learning exercise would be the wrong frame.

**Second, the base case is already at the capacity ceiling.** Twenty paying providers each need at least two referrals per month to stay, which is forty routed referrals per month. Whether DexaFit can produce that is a function of scan volume and post scan opt in rate, not of how well the outreach performs. This is the same constraint from section 5 showing up in the numbers: **the funnel tells us how many providers we can sign, and scan volume tells us how many we can keep.** If those two numbers disagree, the outreach should be throttled, not accelerated.

This is the first thing I would want to check against real data.

---

## 8. Recommendation

Do not build the full marketplace before launch. Run a founding cohort of 50 to 100 vetted providers in one or two markets, priced at $0 plus $60 per accepted referral for 90 days, and use the outreach conversations themselves as the pricing research.

Three questions the pilot should answer before anything scales:

1. Which provider types do clients actually choose when given a real recommendation?
2. What will providers pay for, specifically: placement, exclusivity, routing, or data?
3. Can DexaFit generate enough referral volume per provider to retain a paid tier at all?

Question three is the one that decides whether this is a business or a feature. Everything in this plan is built to answer it in ninety days rather than nine months.

---

## Appendix A. Email sequence, nutritionist and cold

Variables in braces are merge fields. Full templates for trainer and physician segments are in the repo.

---

**E1, Day 0**

*Subject A:* Referrals from {location} clients who already have their body comp data
*Subject B:* Eight nutritionist slots in {city}

Testing: specific mechanism versus scarcity.

> Hi {first_name},
>
> I work with DexaFit, the body composition and metabolic testing clinics. {location} runs DEXA, RMR, and VO2 max scans, and after every one of them the client asks some version of "okay, so what do I do now?"
>
> Right now we mostly say "find a good nutritionist." We are changing that. We are building a small vetted group we route those clients to directly, with their scan data attached.
>
> No listing fee during the pilot. You pay only when you accept a referral, and each one goes to you alone rather than to five people at once.
>
> We are taking eight nutritionists in {city}. Worth fifteen minutes?
>
> Tommy

---

**E2, Day 3**

*Subject A:* What one of these referrals actually looks like
*Subject B:* Re: {city} nutritionist slots

Testing: value demonstration versus thread continuation.

> Hi {first_name},
>
> Quick follow up with something concrete, since "referral" means very little on its own.
>
> A client comes in for a DEXA scan. We measure body fat percentage, lean mass by region, visceral fat, and resting metabolic rate. They sit down for a results consultation, find out their RMR is lower than they assumed and that they have lost lean mass over the past year, and they ask what to do about it.
>
> That is the point we would route them to you. You get their name, their goal, and the scan data before the first conversation. No intake guesswork, and no convincing them the problem is real, because they just paid to measure it.
>
> If that is the kind of client you want more of, here is the application: {link}. Two minutes, and I will personally review it.
>
> Tommy

---

**E3, Day 8**

*Subject A:* Closing the {city} group this week
*Subject B:* Should I close your file?

Testing: deadline versus permission to say no.

> Hi {first_name},
>
> We are finalizing the {city} founding group this week, so this is my last note about it.
>
> If the timing is wrong, no problem at all. Reply "later" and I will check back when we open the next round.
>
> If you want in: {link}
>
> Tommy

---

## Appendix B. What is in the repo

The repo contains the working version of the outreach system: segmentation and prioritization rules, personalization field generation, message templates for all three provider categories, and a sample run over fifty mock leads with the output committed so it can be read without running anything. This memo also lives in the repo under `strategy/`.

I built it against mock data because I do not have the real list. The real list will have a different schema and its own data quality issues. Mapping it into this pipeline is a short exercise. The segmentation and personalization logic carries over unchanged.

## Appendix C. Deliberately out of scope

Held back to stay inside the time budget, and because they should be decided with data rather than guessed at now:

- Provider vetting workflow and credential verification process
- Payment and invoicing infrastructure
- The client facing matching interface
- Full pricing by profession. Trainer and physician economics differ from the nutritionist model above and need their own derivation.
- Deliverability setup: domain warming, sending infrastructure, list validation. Necessary before any real send, but it is execution rather than strategy.
