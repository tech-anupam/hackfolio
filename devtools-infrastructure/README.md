# DevTools and Infrastructure

![Projects](https://img.shields.io/badge/Projects-169-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### AutoAudit Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bbbb-5be1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Akkshita06/AutoAudit-Agent) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mp2liy5a3rvyntyc.buildwithlocus.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/24e43090f21c436c839fe93bfcf13a5b) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-29-FF6B6B?style=flat-square)

> Your Last Audit Missed Something. We Won't.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Google Cloud API](https://img.shields.io/badge/Google%20Cloud%20API-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square) ![Allorigins.win](https://img.shields.io/badge/Allorigins.win-333333?style=flat-square)

**The problem it solves**

Most website owners have no idea why their site isn't ranking on Google. 
Traditional SEO audits cost $200–$500+, take days, and come back as 50-page PDFs that require an expert to interpret.

AutoAudit Agent  makes SEO visibility instant and accessible:

- **Pay $5, get a full audit in 30 seconds** — no waiting, no back-and-forth
- **Plain-English recommendations** ranked by impact, not alphabetically
- **Non-devs can act on it** — every fix comes with copy-paste-ready code
- **No account required** — one-time payment, report appears on screen immediately

It's built for indie hackers, small business owners, and freelancers who 
need real SEO signal without the agency price tag. Instead of a static report, the always-on tier deploys fixes directly to WordPress, Webflow, and Shopify via official APIs — turning audit findings into shipped changes automatically.

**Challenges we ran into**

**1. Stripe Connect Express not supported in India**
Ran into a hard blocker: Stripe Connect Express isn't available for 
Indian accounts, which meant I couldn't complete the payment onboarding 
to go live. Rather than drop the payment flow entirely, I built a 
**fully functional mock checkout** that mirrors the real Stripe UI — 
card fields, processing state, SSL badge — so judges can experience 
the complete user journey end-to-end.

> Hey judges — if there's a workaround for India-based Stripe onboarding,
> I'd love to know! Happy to go live immediately. For now, the demo mode
> shows the full intended flow faithfully.

**2. CORS & real-time page fetching in the browser**
Fetching arbitrary user URLs client-side hits CORS walls immediately.
Routed through a proxy with a 9-second abort timeout and a graceful fallback to estimated data — so the product never shows a blank screen regardless of the target site's headers.

**3. Meaningful scoring without a backend**
Building an SEO score that feels trustworthy using only DOM parsing (no Lighthouse, no PageSpeed API) required a weighted model across known ranking signals — title length, H1 structure, HTTPS, alt text coverage, word count — calibrated so scores correlate with real patterns.

**4. Demo UX that doesn't feel fake**
Used `Promise.all` to race the terminal animation against the live fetch so the loading screen always feels purposeful. The report appears the moment both are ready — never padded, never blocking.

**Using LocusFounder to Build a Business!**

**AutoAudit Agent is a direct application of LocusFounder's core vision:**
an AI agent that builds and runs a business end-to-end, making money 
while you sleep.

**Here's exactly how it maps:**

LocusFounder promises to take a one-line idea ("I want to sell candles")
and build a full business from it — site, payments, copy, customers.
AutoAudit Agent does the same thing, but for SEO services:

- **The product builds itself**: URL in → AI crawls, scores, and generates 
  an impact-ranked audit — zero human involvement per transaction
- **Payments are autonomous**: $5 collected per audit via Locus Checkout, 
  deposited directly into a Locus wallet — no manual invoicing, no chasing 
  customers
- **The upsell runs itself**: after seeing real issues, users are shown the 
  $29/month always-on tier — the agent converts, charges, and delivers 
  without founder intervention
- **Unit economics that work at scale**: ~$0.02 Claude API cost per audit 
  against a $5 price — the business makes money on transaction #1

This is LocusFounder's thesis made concrete: a solo founder can describe 
a business idea ("instant AI SEO audits for $5") and have an agent 
infrastructure run it profitably from day one, with no employees, 
no support queue, and no manual fulfillment.

[Akkshita Isa](https://github.com/Akkshita06)

`2026-05-12`

---

### cohortfit
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cohortfit-4c8b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abm32/cohortfit) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cohortfit.anukritiai.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/44d93cf80bbc4214bc37fb42adfe3569) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-14-FF6B6B?style=flat-square)

> Genomic feasibility auditing for trial protocols

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Azure](https://img.shields.io/badge/Azure-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square)

**How you are solving it?**

cohortfit reads a clinical trial protocol and computes the pharmacogenomic phenotype distribution of the cohort that protocol will *actually* recruit, given the ancestry mix of its planned sites.

```
protocol ──▶ Claude (extraction only) ──▶ {drugs, dose, criteria, sites, target N}
                                                    │
                            deterministic engine (no LLM past this line)
                            ├─ drug ──▶ PGx-actionable gene (CPIC)
                            ├─ site ancestry mix ──▶ pinned allele frequencies
                            ├─ Hardy–Weinberg ──▶ diplotype frequencies
                            └─ CPIC table ──▶ diplotype → phenotype
                                                    │
                      expected cohort phenotype distribution + screening gaps
                      + per-site metabolic burden
```

### The one structural idea

**The model converts unstructured text into typed claims. Deterministic code does everything after that.** `models.py` encodes this as types — an *extraction side* (`Protocol`, `Site`, `DoseRegimen`, Claude's only allowed output surface) and a *verdict side* (`AuditReport`, `GeneDrugFinding`, `Verdict`) produced only by pinned arithmetic. It is enforceable rather than aspirational.

### What the engine does

1. **Enrolment-weighted ancestry mix** across sites, weighted by `planned_n`.
2. **Blend pinned allele frequencies** — gnomAD v4.0, stored with raw counts (`HapB3` in South Asians is literally 1,538 copies in 91,072 alleles). The loader **rejects any entry without `source` and `rsid` provenance**, so a hand-written number cannot load.
3. **Hardy–Weinberg expansion** to diplotypes (`p²`, `2pq`), sum-to-one asserted in tests.
4. **CPIC lookup** against tables pinned at `v2024.01` inside `anukriti-pgx-core`. Unmapped diplotypes become `Indeterminate`, never dropped.
5. **Screening-gap rule** → `ACTIONABLE` when a CPIC Level A pair has no genotype criterion.
6. **Per-site burden** → the CRO-legible output: Munich 6.40% at-risk vs Mumbai 3.55%.

### Findings are tiered, and it refuses to overclaim

**Tier 0** is arithmetic on pinned tables. **Tier 1** requires a cited literature multiplier. **Tier 2** is labelled scenario, never prediction.

`CONTESTED` is a verdict the engine can actually *reach*. On the demo cohort it fires because HapB3 carries **79.3%** of the actionable burden and CPIC's own guideline flags that HapB3 carriers dosed at the standard 25% reduction showed reduced effectiveness *and* increased toxicity (PMID 37639651). The tool declines to resolve a dispute CPIC has not resolved — and it derived that from the arithmetic, not from a hand-written string.

It also reports **what it cannot compute**: a US cohort prints a coverage warning naming the 35% of enrolment (AFR, AMR) with no pinned data, instead of quietly returning European numbers. The one value we distrust — SAS `*2A` from the exome callset — carries a runtime warning with the *direction* of the error, and Poor Metabolizer ships as a range rather than a point estimate.

### A derived result we have not seen published

In a pure South Asian cohort, **94.2% of the CPIC-panel actionable burden sits on one allele, HapB3** — effective allele count 1.12, versus 2.10 in Europeans, with `*13` never firing at all. And HapB3 is precisely the allele whose dosing CPIC contests. Set it aside and number-needed-to-screen goes **28 → 487**. The population with the most concentrated risk is concentrated on the weakest evidence. Reproducible from `docs/FINDINGS.md` with no new data.

### Built during the hackathon

All code in this repository was written today, 2026-08-08, from an empty repo. The one pre-existing component is our own open-source library `anukriti-pgx-core` (pinned CPIC tables), used as a dependency and cited as such. **236 tests, ruff clean, offline by default**, deployed to Azure Container Apps.

**How Did You Use Claude?**

Claude is used in two distinct roles, and the boundary between them is the product.

### 1. In the product — extraction, and only extraction

`cohortfit extract` / `POST /extract` sends unstructured protocol prose to Claude (Sonnet 4) and gets back structured JSON: drugs, dose regimen, inclusion/exclusion criteria, sites, target enrolment. That output is immediately run through `Protocol.model_validate()` — malformed output raises `ExtractionError` rather than propagating into the math.

**Claude never estimates a frequency, a phenotype, or a verdict.** Every number in the report comes from pinned gnomAD fixtures and CPIC tables. This is not a policy we ask reviewers to trust — `models.py` splits the type system into an extraction side and a verdict side so a model-generated number has no type it could inhabit.

This is a deliberate architectural claim: **the deterministic layer decides, the model explains, never the reverse.** In a domain where a wrong number gets someone a chemotherapy dose their enzyme cannot clear, an LLM belongs on the parsing side of the boundary and nowhere else. Claude's job is bridging *legacy prose protocols* into structured form during the industry's transition to CDISC USDM / ICH M11 — a real and large job, and one it is genuinely good at.

### 2. In the build — Claude Code as the primary engineering surface

The entire repository was built today with Claude Code: the Tier 0 engine, the Hardy–Weinberg expansion, the FastAPI layer with full OpenAPI annotations, the React workbench, 236 tests, and every document in `docs/`.

More interestingly, Claude Code was used **adversarially against our own output**. It found and fixed a set of provenance defects that are exactly the failure class this project exists to catch:

- A frequency module declaring values as "gnomAD v2.1.1" that had never been queried — deleted, because nothing imported it.
- Three docs describing an auto-load behaviour a commit had deliberately removed.
- A `detection_floor()` function that was tested but never reached a report, so the output quoted a Wilson bound of 0.0042% while every provenance table documented the rule-of-three 0.0033%. Two numbers for one claim.

That last one is the whole thesis in miniature: an unverifiable number drifts, silently, unless something structural stops it. Each fix is a separate commit with the reasoning in the body.

**What is the deployed URL for this project?**

https://cohortfit.anukritiai.com/

**What is the problem your project solves?**

**Every trial protocol has an implicit genome it was written for. Nobody checks whether the patients being enrolled actually have it.**

A protocol's dose regimen is typically calibrated on a largely European reference population. Run the same protocol at Indian sites and a *computable* fraction of enrollees are metabolically mismatched to that dose. They have adverse events, they drop out, the safety signal muddies, and the trial slips — or fails.

### Why it matters

- Anthropic's own clinical-trial partner **ICON** says enrolment delays hold up **up to 80% of trials**, and that *"the barrier to getting medicines to patients faster is operational, not scientific."*
- **$2.1B** went to Isomorphic Labs in May 2026 for AI-first drug *design*. Almost nothing is chasing the eighteen months a trial loses waiting for the right patients.
- A substantial protocol amendment costs **$141,000 (Phase II) to $535,000 (Phase III)**, 76% of protocols need at least one, and an oncology delay day is worth **~$840,000** in unrealised sales plus **$55,716** in direct Phase III cost (Tufts CSDD 2024).

### The mismatch is invisible after the fact

In FAERS adverse-event data, South Asia reports at roughly **1% of its population-proportional rate** (representation ratio 0.010, measured over 1,311,022 deduplicated cases). If the dose is wrong for a population, postmarket surveillance will not tell you.

Meanwhile the requirement is hardening. Japan and China mandate local testing or foreign-data ethnic-sensitivity analysis, and India's waiver of local trials is actively contested on exactly these grounds. *"Does this dose hold in a South Asian cohort"* is becoming a regulatory deliverable, not a nice-to-have.

### The failure mode we are actually preventing

A prior system on our platform shipped a rule blocking clinical synthesis for South Asian patients on a *"27% carrier frequency"* claim citing a real paper. The paper was real. **The number was hand-written and never came from the cited data.** It ran live for 52 days before a manual audit caught it.

The lesson was not "check harder." It was that **a number with no traceable provenance is indistinguishable from a correct one** until someone audits it. That is the class of error cohortfit exists to make structurally impossible.

Team **Wearebatman** -- [Abhimanyu R B](https://github.com/Abm32), [Aagneye S](https://github.com/aagneye-syam)

`2026-08-08`

---

### FundX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fundx-6c89) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Kobi1003/FundX) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/IeVFKISaN3M) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/IeVFKISaN3M) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-12-FF6B6B?style=flat-square)

> Bid. Invest. Negotiate.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square)

Team **AltF4** -- [Pratik GuhaRoy](https://github.com/PratikPorc), [URSHASHI MAJUMDER](https://github.com/urshashi09), [Srinjani RoyChowdhury](https://github.com/SrinjaniRoyChowdhury), [Swapnil Kobi](https://github.com/Kobi1003)

`2026-09-12`

---

### Humsafar
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/humsafar-1aee) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Preethesh16/Humsafar) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://humsafar-fgu6.onrender.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/oaui_xdnsfI) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-12-FF6B6B?style=flat-square)

> #multiagents #travel #bookings #prava #visa

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Travel planning is not a search problem. It is a coordination problem—and today the traveller is still the coordinator.
Ask an AI to plan Goa and it can generate a beautiful list. But the moment reality enters—one fixed budget, competing flight and hotel prices, different group preferences, places spread across a map, changing weather, and payment responsibility—the “assistant” hands the work back to you. You reopen ten tabs, compare incompatible options, rebuild the budget after every change, connect nearby stops manually, and trust one opaque agent with too much money.
Humsafar removes that coordination burden. A conversational concierge first understands how you want to travel, who is coming, what matters, what can be skipped, and the maximum you will spend. It then creates a small economy of specialist agents—Journey, Stay, Food and Things to Do—that discover options and negotiate over the same finite budget. If Stay wants more, another specialist must make a real concession. A neutral mediator guarantees the final allocation fits; the user chooses only among options already affordable.
Humsafar then transforms those choices into a practical, proximity-aware day plan with timings, route order, weather context, nearby food suggestions and a guided trip quest—without pretending every suggestion was booked.
Most importantly, delegation is bounded. The approved plan is run-scoped and one-shot. Each purchasing agent receives a merchant-scoped Prava credential capped to only its own slice, so a buggy or compromised agent cannot reach another agent’s allocation—or the rest of the traveller’s money. Visa’s sandbox enforcement has already refused an over-cap attempt.
Humsafar moves AI travel from “Here are some recommendations” to “Your specialists coordinated the trade-offs, proved the budget, and can act only inside the permission you gave them.”

**Challenges we ran into**

The hardest part was not making four agents talk. It was making every rupee and "success" mean something.
1. Our first negotiation was theatre. The preferred options already fit, so every agent agreed immediately. We rebuilt it around actual prices: every ask maps to something buyable and every concession selects a real cheaper alternative. A deterministic mediator, not an LLM, allocates integer paise; largest remainder splitting makes the slices exact, and a minimums first fallback guarantees termination without overspending.
2. Providers do not behave like one clean product. Duffel returned foreign currency flights while accommodation access varied; maps, weather and venue APIs all failed differently. We normalized provenance, conservative conversion and destination aware fallbacks. Every row says whether it is provider backed, reference priced, fixture or advisory, never turning a suggestion into a booking.
3. Prava forced real systems debugging. Linux could not complete passkeys, so we built a phone QR handoff that keeps card, OTP and biometrics on Prava. Node also timed out while curl worked: unreachable NAT64 addresses plus a short Happy Eyeballs window were the cause. Raising its timeout made 12 out of 12 requests stable. When the assigned test card later failed credential minting even in Prava's flow, we reproduced it across amounts, currencies and paths, stopped wasteful retries, preserved support evidence and failed closed instead of fabricating success.
4. Dynamic routes broke the map. Returning to the same stay each night stacked markers and tangled multi day paths. We made each day a quest level, separated nearby markers deterministically, preserved real visit order and handed actual navigation to Google Maps.

**Best Visa Intelligent Commerce Implementation**

Visa's rails are what actually make Humsafar's budget promise true, not just a payment button we added at the end.
Journey, Stay, Food and Things to Do agents compete for one fixed budget while a deterministic mediator (not an LLM) settles the exact integer paise split, so the model can argue but never round or create money.
After the user approves once, each agent gets its own Prava mandate and single use Visa credential, locked to one merchant and capped at its slice. We tested this for real on Visa's sandbox: five mandates approved through an actual phone passkey ceremony, one run that produced four merchant scoped credentials for ₹9,800, ₹11,200, ₹4,200 and ₹3,600, adding up exactly to the ₹28,800 we'd negotiated. We also tried to break it on purpose: a ₹160 request against a ₹100 mandate got refused by Visa itself, not by a check in our own code.
Card numbers and session secrets never touch our prompts, logs, or storage. If one agent's purchase fails, only its own slice gets renegotiated, the rest of the plan stays intact.

**Most Startup-Ready Product**

We scoped Humsafar from day one as something with a life after this weekend, not a demo meant to disappear on Monday. The problem it solves, having one fixed amount of money and several things you need to buy across categories, doesn't go away when the hackathon ends. It's every trip, every apartment move, every event budget, for anyone who's ever had to choose between a nicer flight and a nicer hotel.

The architecture reflects that on purpose. The core mechanic, specialists negotiating over a shared pot, a mediator settling the split, each one executing on its own scoped Prava card, isn't hardcoded to travel. Swap the specialist set and the same negotiation engine handles furnishing an apartment or planning an event just as well. That was a platform decision, not a shortcut we took because we ran out of time.

We also built it the way a real product has to be built under pressure. Every external integration sits behind a live or fixture adapter, so a dead API key degrades gracefully instead of taking the whole thing down. And we were upfront in this submission about what's actually live (Prava, Duffel in test mode) versus what's a realistic fixture standing in for a partner API we haven't set up a business relationship with yet (Viator, OpenTable), because that felt more honest than faking it for a demo.

What we'd build next is concrete, not filler: more specialist categories, budget priors learned from past trips, and the most natural next step, letting a group of people split one shared budget the same way our specialists already split one, so a friend group gets the same safety guarantees a single traveller gets today.

This is a product we'd keep building the day after results are announced, prize or no prize. The team, the roadmap, and the willingness to do the unglamorous parts (KYB, real partner APIs, production Prava access) are all already in motion.

**Participation Credits (Already Claimed)**

We used the OpenAI participation credits to build and actually test Humsafar's reasoning layer, not to generate decorative copy.

The Agents SDK runs a Budget Strategy Agent that interprets each traveller's goal, four specialists (Journey, Stay, Food, Things to Do) that pick grounded options and negotiate at the same time, and a separate Mediator that explains the final compromise. The model's decisions genuinely change which specialists get involved, what each one prioritizes, and which real option it defends, it's not the same output every run.

Where the credits actually went was testing the paths that make this safe enough to touch real commerce: structured output validation, parallel agent turns, malformed responses, timeouts, rate limits, and the deterministic fallbacks for when any of that goes wrong. None of the model facing schemas contain a budget, price, allocation, or payment field. OpenAI chooses strategy and which options to defend, audited integer paise code owns every rupee, and Prava is completely outside what the agents can call directly.

That's what the credits bought us: a reusable architecture where the model's reasoning actually matters, but a model failure can never overspend the budget or touch payment data.

**OpenAI**

OpenAI models are what make the negotiation real instead of theater, and we know that because our first attempt wasn't real.

We built the orchestrator and four specialists (Journey, Stay, Food, Things to Do) as separate Agents SDK agents with real handoffs, not one prompt playing four roles. The first time we ran it, every specialist agreed to the initial split immediately, because the preferred options already fit inside the budget. It looked like a negotiation and was actually nothing. We rebuilt it so every ask is tied to an actual buyable price from that run, so a specialist can only concede by genuinely switching to a cheaper real alternative it found. Only then did the agents start actually disagreeing, pushing back, and changing their asks round to round based on what the others just argued, which is the part that needed a model, since a rules engine can't decide "is this a fair concession" against prices that are different every single run.

We kept the model out of one place on purpose. The actual allocation, how many rupees each agent gets, is decided by plain deterministic code after the agents finish arguing, integer paise, largest remainder splitting, so it's exact every time. We didn't want a model rounding or inventing a number where real money is involved. The model argues, the code allocates.

So the split is deliberate and specific: OpenAI reasoning where a judgment call is genuinely needed round over round, plain code the moment money actually moves. Pull the Agents SDK handoffs out and there's no negotiation left, just one agent making sequential tool calls with nobody to push back.

**Best Prava Adapter for the NANDA Town**

Our whole Prava integration reduces to one function: mintScopedCard(mandateId, merchant, amountCap). It issues a merchant locked, amount capped, one time credential, and it doesn't know anything about our negotiation logic or our specific agents, which is on purpose, since we wanted it usable outside Humsafar entirely.

That's what NANDA Town actually needs: several independent agents each getting their own scoped spending authority, without one agent's failure taking down the rest. Ours already works that way. Each agent gets its own capped credential, and if a purchase attempt exceeds its cap or tries a merchant outside its scope, it gets rejected at the card level rather than caught after the fact by our own code. We also built a live or fixture fallback into the adapter itself, so a missing key or a flaky sandbox call degrades instead of crashing the run, which matters just as much inside a shared simulation as it does in our own demo.

We registered our agent team with a NANDA AgentFacts card and a basic agent to agent ping, so the adapter is actually discoverable the way NANDA expects, not something you'd have to dig into our repo to find.

The reason we'd call this an adapter rather than a one off integration: it never assumes our specialists or our budget splitting exist. Any agent in any framework that needs a bounded, revocable way to spend money can call the same function. Humsafar is just the first place we proved it holds up with multiple agents drawing against real spending limits at the same time.

**Agentic Commerce Hackathon**

Humsafar answers what this hackathon actually asked: what happens when an agent doesn't just recommend something, but finishes the job, safely.

Give it a goal and one total budget, say "plan my Goa trip under ₹30k", and it spins up specialist agents (Journey, Stay, Food, Things to Do) that don't just split the work, they negotiate over the same fixed pot. Each argues its case and pushes back on the others, and a mediator settles the split so it fits the budget. That's the actual point: one agent can't reason about giving up more here to get more there. A team can.

Once the split is locked, the user approves once with a single Prava passkey mandate. Humsafar then mints a merchant scoped, one time Prava card per agent, sized to its agreed slice. Each agent completes a real transaction on its own credential. No agent ever sees a raw card number, and none can reach another agent's slice or the rest of the money, because the cap is enforced by the card network itself, not a policy check a bug or bad merchant link could talk its way around.

We show two of these live: an agent nudged toward an over slice purchase gets blocked at the card level on screen, and when one agent's booking is deliberately failed, the orchestrator renegotiates only that agent's slice instead of the whole plan collapsing.

That's Prava used the way this hackathon asked for, not a payment button at the end, but the thing that makes the core promise (a team of agents can be trusted with your money) actually true.

Team **Humsafar** -- [Jeswin Jacob lobo](https://github.com/jeswin2003lobo), [Preethesh Carvalho](https://github.com/Preethesh16), [Deepthi C J](https://github.com/deepthii26)

`2026-08-02`

---

### tinkerers[dot]space
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tinkerers-space-321e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/qKitNp/tinker-cli) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tinkerers.space) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/1819ea3a828f424fb39a2896c75182d3) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-10-FF6B6B?style=flat-square)

> cloud platform for non-technical vibe-coders

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**What is the problem your project solves?**

There will be more than **a billion software engineers by next year**, and most of them will be non-technical people using Claude Code.

I have already met people building amazing applications with no technical background. I have met a sociology professor who built a complete pipeline to translate books from English to local languages. But the biggest hurdle for them is no longer creating software; it is deploying it. That includes deploying ML models, web apps, load balancers, and databases.

The bottleneck has now moved from development to deployment, and none of the cloud providers are catching up fast enough. It is still very difficult for non-technical vibe-coders to get their products out there.

**What is the deployed URL for this project?**

https://tinkerers.space

**How you are solving it?**

I have been homelabbing since my teens. A few months ago, I created an agentic loop that analyzes a repo or project, writes a Dockerfile based on the requirements, and deploys it.

Many of my friends who are Product Managers started using it to deploy their personal projects.

I realized we needed to build a new cloud platform for Agentic Engineering—one designed by people whose introduction to software engineering was through vibe-coding.

This new cloud, Tinkerers.Space, is agent-first: users (or their agents) do not need to install a CLI. Instead, they can provision GPUs, servers, and serverless instances through natural interaction. The best part is that it is cheaper and more convenient than AWS, GCP, or Azure; because we own and operate our own infrastructure.

Links that are deployed on Tinkerers.Space:
https://lucky-lynx-7438.tinkerers.space/
https://itstimeline.tinkerers.space/

PS: Attached my old laptop that is the server rn:

![image](https://assets.devfolio.co/content/ed5e9aba96554bdebc739e215063724a/636edcbb-e83e-405b-bfc5-2185f1bc6ecc.png)

**How Did You Use Claude?**

I tried to productionize it today by updating the CLI and adding Anthropic models along with OpenAI models.

I found Claude Managed Agents intriguing and was tempted to use them since they were solving a lot of my problems, especially those related to security. But I decided not to, due to two major concerns: a 5-hour hackathon is not ideal for testing out new technologies that require major rewrites and subsequent testing, and the concern of vendor-locking myself to Anthropic. Even though it seems they are winning the model wars, one can never be too sure.

However, one must say that using Claude Opus with Langchain DeepAgents did give a slightly better result than using the GPT model.

Pranjal Pranjal

`2026-08-08`

---

### ExoDex
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/exodex-55cc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aarush-paul/exodex-wrapper) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ssa-frontend-ojpu.onrender.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ATVfUBPThG4) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> To Infinity & Beyond

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![WebGL](https://img.shields.io/badge/WebGL-333333?style=flat-square) ![3D Mapping](https://img.shields.io/badge/3D%20Mapping-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square)

Team **Ctrl+Shift+Esc** -- [Aarush Paul](https://github.com/aarush-paul), [Mayank Pradhan](https://github.com/skillissueguykagit), [Jayeeta Bhanja](https://github.com/jayeetabhanja-arch)

`2026-09-12`

---

### Meter
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/meter-e51a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ammarjiruwala/meter) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://meter-three-beta.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/r7qmY5sIkpc) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> AI manages your work, we manage your AI

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**Challenges we ran into**

Only if we had a token for every challenge we faced.

In all honesty, we started thinking we had something to work with. Spoiler alert, we (really really) didn't. 
We found the leading repository in the field of token prediction. But guess what, it was just a linear hollow template that gave out random guesses in the name of token prediction. Wrong metrics, wrong formulas, wrong results.

So we did what all sane rising sophomores, complete beginners in AI/ML, heuristics and umm.. Hierarchical backoff with geometric shrinkage do. Which is of course using the power of 100dollars in OpenAI credits, to make everything - all prediction logic, all frontend, every metric - from scratch, on our own.

Our testing credit cards got exhausted after too many runs, so we spent hours on calls with the Prava team getting everything sorted. Shoutout to Shubham and Sushant for testing an unreasonable number of credit cards.

Shivam had to switch database setups multiple times before finally settling on the good old Supabase, and running like a 1000 tests (quite literally) . Tanay had to completely change the dashboard to be dynamic (update logs every 3 seconds), and homepage to be 3D. Shubh had to explain his screen time to his parents. Ammar had to figure out why the error margin of the autonomous feedback loop was rising from 49% to 200% before it finally started decreasing to within 10% in the final model.

All things considered, the worst challenge was still without a doubt running out of caffeine. BUT finallyyy seeing the 0% error rate on some of the runs reignited our will to sacrifice our sleep schedules.

**The problem it solves**

Companies spend thousands a month on LLM calls and can't tell you how quickly it went by, and when balance hits zero at mid project, production stops.

Meter is a drop-in proxy.
As soon as you use our integration, every call, attribute, feature is tracked. 
We predict your input and output tokens, something that no one else can do. Or at least not using the painstaking heuristics and self improving feedback loops we have in place (you really should go through the “how prediction works” section on the website)
When you're about to run out of tokens, we predict  how many you need within a really improved error margin (6.5x better), and then buy them for you, through our dearest Prava. 

They say the devil will burn all your credits, but guess what, now the devil wears prava. 

In the future, we plan to expand the type of prompts, which we define as feature-tags, that the prediction model can conquer. We also wish to expand to AI providers other than OpenAI. Further we wish to decrease the latency of the proxy and database. All this will help us progress to a point where we are ready to flawlessly ship to users and businesses.

**Best Visa Intelligent Commerce Implementation**

We built a dedicated agent called the Treasurer agent that autonomously holds a human-approved Visa mandate and spends against it with nobody present. VIC is what allows the automatic budget top ups to run.

**Most Startup-Ready Product**

*We are not just startup ready, but also ready for startups to use.*
Meter ships as managed infrastructure or inside your own perimeter. The hosted stack runs the proxy on Render, the dashboard on Vercel and the ledger on Supabase against a single shared Postgres, while docker compose up deploys that same stack single-tenant inside your VPC, where your provider keys never leave your environment. And the product appreciates in place. Prediction accuracy is derived from your own accumulated per-feature history, so forecast quality improves the longer you run it - so not only can it handle users, but users make it better.

**OpenAI**

Firstly, Meter is a drop in proxy for live OpenAI traffic, the predictions our engine makes is for OpenAI, specifically the GPT 4o Mini model. Our entire prediction model is trained on actual token information from 1756 OpenAI requests for output token estimation, and uses OpenAI's own tiktoken for input token estimations.

**iMessage Agent**

We don’t only know when to use Prava, but also when not to because we have a circuit breaker that automatically blocks suspicious prompting activity to avoid your bank account from being empty due to leaked API keys. When that happens we immediately alert the user with iMessages via Linq. This keeps them always notified and their bank accounts always safe.

**Best Agentic User Experience**

The dashboard is live. The status ramp is colourblind safe and contrast was measured for this exact reason. The top-up renders as "dry run, no money moved”. We don't invent any payments or log lines, we only show states that exist in the ledger. And the dashboard shows user friendly live analytics and the entire site has clear navigation with creative 3D UI.

**Agentic Commerce Hackathon**

We predict the cost before the call, not after the bill. We did deep analysis, check every research paper and repo we could find - but nothing exists for inspirations that can pass even remotely close benchmarks. Everyone else reports what you spent; we forecast it pre-flight and cut it off mid-flight - 70% error down to 11%, measured across 1,300 real calls, not asserted.
A real Visa settlement with no human present. Most agentic-commerce demos stop one step before the money moves. Ours has a transaction id. It's deployed, you can drive it yourself in ten minutes, and we publish what we haven't proven.

Team **Devil Wears Prava** -- Ammar Jiruwala, Shubh Jain, Shivam Kapadia, [Tanay Desai](https://github.com/tanaydesai-dev)

`2026-08-03`

---

### RideLink
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ridelink-776c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/suryak2025cse-sys/RideLinkAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ride-link-ai.vercel.app/passenger) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/aD_SUAtO4s4?si=IDbJ-qc-gsPAkHHC) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Connected Community Rides, Powered by Intelligence

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

***Problem statement:***

Daily commuters often face expensive and unreliable daily transportation, with limited connectivity to public transport. Many people travel along the same routes every day, yet there is no trusted platform that enables them to safely share rides.

 Existing ride-hailing services are designed primarily for commercial drivers and individual trips, leaving empty seats in private vehicles unused while others struggle to find affordable transportation. This inefficient use of vehicles contributes to increased traffic congestion, higher fuel consumption, and greater carbon emissions
 
**Solution:**

**RideLink AI** enables daily commuters travelling in the same direction to share rides with one another.

 By connecting verified drivers with passengers whose destinations are along the same route, the platform makes commuting more affordable and convenient.

Drivers can also earn by sharing their unused vehicle seats, while passengers enjoy safe and cost-effective transportation.

**Key Features:**

**Demand Hotspots:**
Suggests the main hotspot areas.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/7798618a-c37d-42ac-9290-ee5814c7b115.png)

 **Emergency SOS:**
Activating SOS will immediately broadcast your live GPS location, notify your emergency contacts, and dispatch an urgent alert to platform safety leads.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/06fa5e25-b84b-4ebe-a2fe-1d9f75e56909.png)

**Ride Suggestions:**
Recommends the most suitable ride.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/226356a9-6123-4737-9168-9ac4bfb58f64.png)

**Trust Score:**
Shows driver and passenger reliability.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/6d22799d-1da4-4aa1-9838-d005f0be3238.png)

**Women Safety:**
Verified drivers with SOS support.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/ffd29941-6beb-44ff-a649-ab725d84d159.png)

**Campus & Corporate Mode:**
Private ride-sharing for colleges and companies.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/7e08f15f-1e6b-43de-a9fb-129b412178a9.png)

**CarbonTracker:**
Shows fuel and CO₂ savings through ride sharing.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/2bdee726-07e0-489b-9d28-3cfd3e683a77.png)

**Safe & Secure**
Driver can only offer a Ride after they verify their Aadhar and liscence

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/9ebddc00-e2fc-4075-913f-a93edda01262.png)

**Challenges we ran into**

Building **RideLink AI** involved solving several complex full-stack engineering challenges:

**Real-Time Multi-Client Synchronization:** Initially, ride data was stored in local React component state, causing data loss on browser refresh and preventing passengers from seeing new rides. We resolved this by re-architecting our Express backend to persist ride offers directly to MongoDB Atlas while emitting real-time WebSocket events via Socket.IO. This ensures every connected client receives instant UI updates across browsers without page refreshes.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/be7e9c1b-8375-4b36-8344-813c6bf02535.png)


**Firebase OAuth Domain Authorization:** Deploying Google OAuth via Firebase triggered domain authorization errors due to cross-origin security policies. We resolved this by registering production domain origins in the Firebase Console and configuring custom provider parameters to explicitly force the Google account selection window every time.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/7f9ab361-7167-4dc2-bf39-d865deafbc9c.png)


**Strict Document-Based Driver Authorization:** Early prototypes allowed drivers to gain verified status without submitting real identity documents. We hardened our Express validation middleware and MongoDB schemas to strictly verify Aadhaar Card and Driver’s License fields, locking ride creation endpoints until identity verification is completed.

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/1047c547-0041-4893-bccf-1190f7b7ea36.png)

**Atomic Inventory Control for Concurrent Bookings:** Simultaneous booking requests created race conditions where seats could be oversold. We implemented atomic MongoDB document updates and validation logic in our Express controllers to verify remaining seat capacity before confirming any booking

![image](https://assets.devfolio.co/content/e222800fb6ea4528b1a8ea44eee1d520/35ba27e0-f0e3-4a77-bbb0-3c379c4a45d3.png)

Team **Code Shift** -- [SURYA K](https://github.com/suryak2025cse-sys), [Udhayan L](https://github.com/udhayanl), [Vithull M](https://github.com/vithull-m), Shobika S, [SETHUKAMAL PG](https://github.com/sethukamalpg), Vaanathi J

`2026-07-30`

---

### Tiny color
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tiny-color-a178) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/s-abdullah12/tinycolor) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1215187375?share=copy) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> A faithful Go port of the TinyColor JS library

![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Testing](https://img.shields.io/badge/Testing-333333?style=flat-square) ![Color](https://img.shields.io/badge/Color-333333?style=flat-square) ![fuzzing](https://img.shields.io/badge/fuzzing-333333?style=flat-square) ![Porting](https://img.shields.io/badge/Porting-333333?style=flat-square)

**The problem it solves**

TinyColor is one of those small JavaScript libraries that shows up everywhere. Angular Material, Chart.js, and Bootstrap all use it to parse, format, and adjust colors. When I started working in Go, I found I wanted the same thing and could not find a drop-in replacement that behaved the same, so I built it: a tiny Go library that mirrors TinyColor's API and matches its output.

### What it does

Take almost any color string and normalize it: named colors, hex in a few widths, rgb, hsl, hsv, even the messy input people paste in such as missing commas, stray spaces, or percent signs. Convert between formats, including 8-digit hex. Adjust colors with Lighten, Darken, Saturate, Desaturate, Grayscale, Tint, Shade, Spin, Complement, or Invert. Mix two colors with weight and alpha, generate schemes like analogous, monochromatic, and triadic, and check contrast for WCAG AA and AAA so you can pick readable text for a given background.

### Who it's for

Go developers who need color handling in CLI tools, theming engines, image work, or design systems, and who want behavior they already know from the JavaScript library.

**Challenges we ran into**

The hard part was behavioral equivalence, not just getting the code to run. TinyColor is small but it relies on JavaScript-specific behavior: tolerant string parsing, float rounding in each color space, and the exact clamping it does. Go does not provide any of that for free, and output that is close was never good enough.

So I did not trust my eyes and built a differential test harness early on. It runs the real TinyColor in Node, feeds the same inputs to both implementations, and compares the results side by side. This caught real HSL and HSV rounding mismatches I would never have reasoned about from reading code alone.

Fuzzing did the rest. Go's fuzzer feeds mutated inputs back in to keep the port honest. One practical snag was that Go fuzzing does not run cleanly across multiple packages, so I pinned the Makefile targets to a single package, documented it, and made the fuzz and validate targets work out of the box.

I trust the port not because I reviewed every line, but because every differential run and fuzz round agrees with the original. I also translated the upstream test suite into Go table tests. The results are verified by running, not argued.

Syed Abdullah

`2026-08-03`

---

### TATVA-Forensic Intelligence Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tatvaforensic-intelligence-platform-39e2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rio-ARC/TATVA-Forensic-Investigation) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/Rpbh-g6_wUA) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Rpbh-g6_wUA) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> From fragmented evidence to explainable truth

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![OCR](https://img.shields.io/badge/OCR-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

## The Problem Tatva Solves

**Tatva is designed to assist and augment investigators, not replace them. Human investigators remain at the center of every decision, while Tatva helps them process and analyze complex evidence faster and more effectively.**

Modern investigations often involve massive amounts of fragmented digital evidence spread across multiple sources—call records, transaction logs, GPS traces, chat exports, reports, audio transcripts, and other datasets. While the information exists, the connections between them are difficult, time-consuming, and error-prone to uncover manually.

Investigators frequently spend days or even weeks correlating data from different formats and sources to answer fundamental questions:

- Who is connected to whom?
- What sequence of events occurred?
- Which entities are genuinely suspicious?
- Which leads can be safely eliminated?
- What evidence supports a particular conclusion?

Tatva addresses this challenge by transforming heterogeneous evidence into a unified investigative knowledge graph.

### What Tatva Enables

- **Automated Evidence Correlation** – Connects people, accounts, locations, devices, communications, and events across multiple evidence sources.
- **Dynamic Data Ingestion** – Supports structured and unstructured evidence through adaptive schema mapping and intelligent preprocessing.
- **Knowledge Graph Reconstruction** – Converts fragmented information into an interactive graph of entities and relationships.
- **Timeline Reconstruction** – Rebuilds chronological sequences of events from distributed evidence.
- **Investigator-in-the-Loop Analysis** – Allows investigators to validate, prioritize, or clear entities while preserving evidence provenance.
- **Explainable Intelligence** – Every insight can be traced back to the original supporting evidence.

### Impact

Instead of manually stitching together disconnected files and records, investigators can focus on reasoning, decision-making, and field work while Tatva handles large-scale evidence correlation and graph-based analysis.

In short, **Tatva turns fragmented evidence into explainable investigative intelligence**, helping reduce analysis time, surface hidden connections, and support faster, more informed investigations.

**Challenges we ran into**

# Challenges We Ran Into

### 1. Heterogeneous Evidence Formats

**Problem:**  
Investigative data rarely arrives in a standardized format. Different CSVs used different column names for the same concepts, reports came in PDFs and text files, and evidence sources varied significantly in structure. Our initial preprocessing pipeline relied on hardcoded schemas, making it brittle when new datasets were introduced.

**Solution:**  
We introduced a hybrid preprocessing architecture with an LLM-powered Dynamic Schema Mapping layer. The LLM identifies dataset types and maps arbitrary column names to canonical schemas, allowing our deterministic preprocessors to continue operating without modification. This made the system adaptable while maintaining extraction accuracy.

---

### 2. Stale Graph Generation

**Problem:**  
Even after uploading completely new evidence, the system kept generating the same graph, risk scores, and insights. New files were successfully uploaded but were not being consumed by the downstream intelligence pipeline.

**Solution:**  
We traced the complete data flow and discovered that parts of the pipeline were still referencing static development datasets. We refactored the processing workflow so that uploaded files become the single source of truth, ensuring that every upload triggers schema mapping, preprocessing, graph integration, Neo4j updates, and analytics regeneration.

---

### 3. Building an Explainable Knowledge Graph

**Problem:**  
Many AI systems can generate insights, but investigators need to understand *why* an insight was generated. A black-box recommendation system would not be useful in a forensic environment.

**Solution:**  
We designed the graph architecture around explainability. Every relationship, event, alert, and risk score is linked back to supporting evidence and provenance information, allowing investigators to verify the reasoning behind system-generated intelligence.

---

### 4. Dynamic Investigation Workflows

**Problem:**  
Investigations evolve over time. During testing, we realized that investigators often discover information outside the system, such as verified alibis or cleared suspects. A static graph could not incorporate this feedback.

**Solution:**  
We introduced a Human-in-the-Loop workflow where investigators can mark entities as Cleared, Person of Interest, or Priority Target. These assessments are stored separately from evidence, preserving factual data while allowing the graph to visually adapt to ongoing investigation decisions.

---

### 5. Large Graph Visualization and Usability

**Problem:**  
Raw knowledge graphs quickly become cluttered and difficult to interpret, especially when multiple entity types and relationships are displayed simultaneously.

**Solution:**  
We migrated to an interactive 3D graph visualization workflow with entity-centric filtering, contextual views, timeline integration, and visual risk indicators. This helped investigators focus on relevant parts of the graph without losing access to the complete investigation context.

---

### 6. Balancing AI and Deterministic Processing

**Problem:**  
Early on, we considered using LLMs for the entire extraction pipeline. While flexible, this introduced concerns around consistency, cost, reproducibility, and hallucinations.

**Solution:**  
We adopted a hybrid architecture. Deterministic preprocessors handle structured forensic datasets for reliability, while LLMs are used selectively for schema understanding and unstructured document extraction. This provided the flexibility of AI without sacrificing trustworthiness.

**AI/ML**

## Why Tatva Fits the AI/ML Track

Tatva leverages Artificial Intelligence and Machine Learning to transform fragmented forensic evidence into actionable investigative intelligence.

The platform combines LLM-powered schema understanding, intelligent entity extraction, entity resolution, graph analytics, risk scoring, and timeline reconstruction to automatically correlate heterogeneous evidence sources into a unified knowledge graph.

Rather than relying on rigid data formats, Tatva uses AI to understand and normalize diverse datasets, enabling investigators to work with real-world evidence that often arrives in inconsistent structures.

The system further augments investigations through graph-based intelligence generation, explainable risk assessment, and investigator feedback loops, creating a Human-in-the-Loop AI workflow where machine intelligence accelerates analysis while human investigators retain decision-making authority.

AI is not an auxiliary feature in Tatva—it is fundamental to how evidence is processed, correlated, analyzed, and transformed into investigative insights.

**Open Innovation**

## Why Tatva Fits the Open Innovation Track

Tatva addresses a real-world challenge that extends across law enforcement, cybercrime investigation, financial fraud analysis, digital forensics, and intelligence operations: transforming fragmented evidence into actionable investigative intelligence.

Modern investigations involve vast amounts of heterogeneous data including call records, transaction logs, GPS traces, reports, communication records, and other digital artifacts. These datasets are often disconnected, inconsistent, and difficult to correlate manually, resulting in significant time spent on evidence analysis rather than investigation itself.

Tatva introduces an investigator-centric intelligence platform that ingests diverse evidence sources, automatically correlates entities and events, reconstructs timelines, generates explainable knowledge graphs, and surfaces actionable insights while keeping human investigators in control of all critical decisions.

The platform combines multiple technologies including knowledge graphs, graph analytics, dynamic data ingestion, timeline reconstruction, investigator feedback loops, and explainable intelligence generation to create a unified investigative workspace.

As part of this innovation, Tatva also incorporates AI/ML components such as:
- LLM-powered Dynamic Schema Mapping for handling heterogeneous datasets.
- Intelligent extraction from unstructured reports and documents.
- Risk scoring and entity prioritization.
- Graph-based intelligence generation and analytics.

Rather than replacing investigators, Tatva augments their capabilities by reducing manual correlation effort, improving visibility into complex relationships, and enabling faster, evidence-backed decision making.

By combining AI, graph intelligence, and human expertise into a single workflow, Tatva represents an innovative approach to modern investigative analysis, making it a strong fit for the Open Innovation track.

Team **XCRYPT** -- [Subhajit Das](https://github.com/Subhajit-Das-1), [Subarno Chakraborty](https://github.com/kutan-fuiton), [Biraj Acherjee](https://github.com/Biraj021), [Aritra Roy Choudhury](https://github.com/rio-ARC)

`2026-05-31`

---

### CivicClick
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/civicclick-b3a1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jacky0898/Civicclick) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://civicclick-frontend.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Where clicks make changes

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Google Location services](https://img.shields.io/badge/Google%20Location%20services-333333?style=flat-square)

**The problem it solves**

🌍 The Problem It Solves

In popular tourist destinations like Goa, visitors often face real-world safety and infrastructure issues that are not visible online — such as poorly lit roads, broken walkways, unsafe public areas, or sanitation problems near crowded spots.

Today, there is no simple, unified system where:

- Tourists can quickly report unsafe or inconvenient conditions
- Other visitors can be aware of risks before reaching a location
- Local volunteers or communities can track and resolve these issues transparently

As a result:

- Tourists unknowingly enter unsafe areas  
- Civic issues remain unreported or ignored  
- There is a clear gap between problem visibility and action  

---

⚠️ Challenges in Existing Systems

- Fragmented reporting: Issues are scattered across social media or ignored entirely  
- No real-time awareness: Visitors lack live insights about safety in specific locations  
- Low accountability: Even if reported, there is no clear tracking or resolution flow  
- Not tourist-focused: Most civic platforms are designed for locals, not travelers  

---

💡 Our Solution — CivicClick

CivicClick is a Civic & Tourism Safety Platform that enables users to:

- Report local issues with location and context  
- View and track nearby problems in real time  
- Enable volunteers to take action and update status  
- Navigate directly to issue locations via map integration  

The platform follows a clear lifecycle:

Report → Track → Resolve  

This ensures that issues are not just reported, but actively followed up and addressed.

---

🚀 Why It’s Better

- Safety-first approach — highlights risks for tourists and locals  
- Real-time visibility — users can avoid unsafe areas proactively  
- Action-oriented flow — volunteers can directly participate in resolution  
- Lightweight and accessible — no complex setup, immediate usability  

CivicClick acts as a live awareness and response system that improves both safety and accountability in public environments.

---

🎯 Real-World Impact

- Helps tourists make safer navigation decisions  
- Encourages community-driven problem solving  
- Improves transparency in civic issue handling  
- Creates a more trustworthy and informed environment  

---

“Safer places aren’t built by chance — they’re built by awareness, action, and accountability.”           

-  “When people can see problems clearly, they can solve them faster — CivicClick makes that possible.”

**Challenges we ran into**

🚧 Challenges I Ran Into

While building CivicClick, most of the challenges weren’t about adding features — they were about making everything actually work smoothly in real-world usage, especially during testing and demo prep.


⚠️ 1. Users Getting Logged Out on Refresh

One of the first issues I faced was users getting logged out every time the page refreshed. It made the app feel unreliable.

Fix:

* Stored the JWT token in localStorage
* Created a central auth hook to manage session state
* Added simple expiry checks and route protection

After this, the app finally felt consistent and usable.



⚠️ 2. SSR Crashes (Next.js Issue)

Since the app uses Next.js, accessing things like localStorage during server-side rendering caused crashes.

Fix:

* Wrapped browser-only code with `typeof window !== 'undefined'`

A small change, but it fixed a major stability issue.


⚠️ 3. Broken Map Links

Some issue cards were opening invalid Google Maps links due to missing or incorrect coordinates.

Fix:

* Validated coordinates before using them
* Converted `[lng, lat]` properly to `lat,lng`
* Disabled the map button if location wasn’t available

This made the map feature reliable during demo.



⚠️ 4. UI Breaking with Unexpected Data

At times, the API returned incomplete data, which caused the UI to crash.

Fix:

* Used safe defaults while destructuring
* Added optional chaining
* Handled empty states properly

Now the UI stays stable even with imperfect data.



⚠️ 5. Inconsistent Keyword Logic

The keyword-based logic for priority and issue type was initially giving inconsistent results.

Fix:

* Normalized text (lowercase)
* Used simple first-match rules
* Added safe fallback (Medium + Civic)

Keeping it simple made the behavior more predictable.


⚠️ 6. Network Errors During Authentication

During integration, login and signup stopped working due to API URL and config issues.

**Fix:**

* Standardized API base URL using environment variables
* Verified request payloads
* Added basic logging to debug quickly

This helped restore stable communication between frontend and backend.


💡 Key Takeaway

The biggest learning was that building features is only half the job. Making them stable, predictable, and demo-ready is what really matters.

A lot of effort went into fixing edge cases and ensuring nothing breaks during actual usage — which made the final product feel reliable and complete.

**The Render Deployment Bounty ($850 Pool)**

🚀 How Our Project Fits the Render Deployment Track

CivicClick is designed to be a fully deployable, real-world application, and using Render made it easy to move from local development to a live, accessible product.

---

💡 Why Render

We used Render to deploy both the backend and make the application publicly accessible. It allowed us to:

* Deploy quickly without complex setup
* Manage environment variables securely
* Ensure the app is available online for real-time usage and demo

This was important because our project is not just a prototype — it is meant to be used in real scenarios.

---

⚙️ What We Deployed

* Backend (Node.js + Express API) deployed on Render
* Handles authentication, issue reporting, and data management
* Connected to MongoDB for persistent storage

The deployed backend powers all core features like reporting, tracking, and volunteer updates.

---

🌐 Real-World Accessibility

By deploying on Render, CivicClick is:

* Accessible from anywhere (not limited to localhost)
* Demo-ready for judges and users
* Capable of handling real interactions in real time

This aligns with the goal of building solutions that go beyond development and actually work in practical environments.

---

📈 Why This Matters

A key part of our project is not just building features, but ensuring they are usable and accessible in real-world conditions.

Using Render helped us:

* Validate the full system in a live environment
* Test real user flows (login, reporting, resolving issues)
* Deliver a stable and reliable demo experience

---

💬 Summary

CivicClick fits the Render deployment track by being a fully functional, deployed application that demonstrates how a real-world civic and tourism safety platform can be built, hosted, and used effectively.

It shows not just what the system can do — but that it is already ready to be used.

Akash G

`2026-05-15`

---

### Mandamus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mandamus-ai-judicial-infrastructure-platform-a842) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KISHORE0709-LEO/Mandamus) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mandamus-judicial.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/F_B0MsafY58) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> AI Judicial Infrastructure Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Data Mining](https://img.shields.io/badge/Data%20Mining-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square)

**The problem it solves**

India's judiciary is currently facing a catastrophic crisis: over 50 million pending cases, a shortage of judges, and a massive barrier to entry for ordinary citizens who lack the financial means or connections to navigate the legal system. Mandamus is an AI-driven judicial infrastructure platform built to decentralize and accelerate justice at every layer.

1. Solving the Administrative Backlog
Manual scheduling, physical document filing, and precedent lookup take days of a judge's time. Mandamus utilizes Google Cloud and Vultr for a high-performance, distributed backend that automates the entire judicial pipeline. With Snowflake's powerful data warehousing, we can process millions of historical judicial records to provide real-time precedent analysis, turning days of research into seconds of AI-driven insights.

2. Breaking the Silence (Victim Protection)
Victims of sensitive crimes often fear reporting due to potential identity exposure. Our "Silent Justice" module provides a secure, anonymous vault for reporting. To ensure absolute transparency and trust, we utilize the Solana blockchain to create immutable, tamper-proof logs of report submissions. This ensures that once a report is filed, it cannot be deleted or altered by any authority, providing a "Decentralized Chain of Custody" for justice.

3. Intelligent Evidence Reading
Evidence processing is the primary bottleneck in modern courts. Mandamus uses Gemini (Multimodal) to instantly "read" and analyze evidence (images, CCTV logs, medical reports, and documents) the moment they are uploaded to Google Cloud Storage (GCS). Instead of waiting weeks for manual verification, authorities receive AI-generated strength assessments and summaries, allowing for immediate action in critical cases.

4. Humanizing Legal Guidance
Legal jargon is a barrier to human rights. Our AI Legal Assistant uses ElevenLabs to provide high-fidelity, empathetic voice guidance, explaining complex laws in plain language. By integrating Backboard.io for real-time state management and collaborative signaling, we ensure that citizens can interact with the legal system seamlessly, even on low-bandwidth connections.

5. Virtual Infrastructure for Everyone
By moving the courtroom to a Virtual Hearing Pipeline, Mandamus removes the need for expensive physical travel. Lawyers and judges collaborate through real-time dashboards synchronized via MongoDB, ensuring that justice is served wherever there is an internet connection.

Summary of Why it Matters:
Mandamus makes the existing judicial task safer through blockchain immutability, faster through multimodal AI intelligence, and accessible through voice-enabled regional language support. It transforms a slow, centralized bottleneck into a fast, decentralized service for 1.4 billion people.

**Challenges we ran into**

Real-Time Signaling Stability: Our WebRTC signaling initially lived in server memory—any Render or Vultr deployment restart would crash active court sessions mid-hearing. We solved this by integrating Managed Redis as a persistent signaling layer, making judicial sessions survive restarts and allowing the platform to scale horizontally across cloud clusters.

Cross-Browser Audio Compatibility: Standard audio streaming for our AI Legal Assistant kept throwing ERR_REQUEST_RANGE_NOT_SATISFIABLE errors across browsers. We re-engineered the entire TTS pipeline into a Base64-encoded JSON architecture—voice is now delivered as encoded payloads and decoded client-side using ElevenLabs, working seamlessly everywhere from mobile to desktop.

Multi-Cloud Database Handshakes (Vultr + GCP): Connecting our Vultr-hosted backend to MongoDB Atlas across different cloud providers triggered persistent SSL/TLS handshake failures (Internal Alert 1081). We overcame this by re-engineering the MongoDB client with custom TLS parameters, relaxed hostname validation, and optimized server-selection timeouts to ensure stable connectivity in a multi-cloud environment.

Multimodal Evidence Interpretation: Getting one system to "read" a harassment screenshot, a medical report, and a handwritten complaint required complex grounding. We built a background analysis engine powered by Gemini (Multimodal) that triggers automatically on Google Cloud Storage (GCS) upload and returns structured intelligence directly to the judicial dashboard.

Synchronized Justice Workspace (Backboard.io): Keeping a judge and multiple lawyers in a cohesive "Virtual Courtroom" without lag or state drift was a major hurdle. We implemented Backboard.io for real-time collaborative state management, ensuring that when a judge sends an invite or starts a session, the courtroom state updates instantly for all participants without manual polling.

Automated Judicial Workflows (n8n): Orchestrating the complex logic between victim reports, authority notifications, and legal analysis was too heavy for a standard monolithic backend. We utilized n8n to build a robust workflow engine that handles asynchronous triggers, ensuring that when a report is filed, it is routed, analyzed, and logged through the correct authority channels without blocking the main judicial pipeline.

**AI & ML**

Mandamus fits into the AI & ML Track by transforming the static judicial process into a reactive, intelligent ecosystem. Here’s how:

Multimodal Evidence Intelligence: We utilize Gemini (Multimodal) to solve the biggest bottleneck in justice: evidence reading. Our system automatically "reads" harassment screenshots, medical reports, and handwritten documents uploaded to Google Cloud Storage (GCS), extracting key entities and providing authorities with instant, objective summaries and strength assessments.

Voice-Enabled Legal Guidance: We’ve integrated ElevenLabs to power an empathetic, high-fidelity AI Legal Assistant. This allows citizens to receive real-time legal guidance through natural voice interaction, breaking down the barrier of complex legal jargon and making the law accessible to everyone.

Neural Judicial Summarization: Mandamus uses Large Language Models (LLMs) to parallelize the analysis of massive judicial filings. It distills multi-hundred-page documents into concise "TL;DR" summaries for judges, highlighting the most critical precedents and legal arguments in seconds.

Intelligent Workflow Orchestration: By using n8n, we’ve built an AI-driven routing engine that evaluates report severity and location in real-time, intelligently "connecting" victims to the most relevant local authorities or NGOs without manual intervention.

By combining Multimodal Vision, Natural Language Processing, and AI-driven Automation, Mandamus demonstrates how machine intelligence can directly solve the 50-million-case backlog and make the judicial system truly proactive.

**ElevenLabs**

ElevenLabs Integration in Mandamus :
Mandamus uses ElevenLabs to solve one of the biggest hurdles in the Indian legal system: the linguistic divide. While law is often locked in complex English jargon, our platform uses ElevenLabs to bring justice directly to the people in their native tongue.

6-Language Regional Expansion: We have implemented high-fidelity judicial guidance in 6 major languages—English, Hindi, Telugu, Kannada, Tamil, and Malayalam. This ensures that citizens from across India can understand their legal rights and navigate the "Silent Justice" module without needing a translator or expensive legal counsel.

Voice-Driven Judicial Accessibility: For many citizens, reading long legal texts is a barrier. We use ElevenLabs' human-like voices to read out case summaries and legal advice, transforming Mandamus from a static website into an interactive AI Legal Advisor that anyone can listen to and understand.

Engineered for Reliability: To handle the unique challenges of rural connectivity, we developed a custom Base64-encoded audio payload architecture. By encoding ElevenLabs' synthesis on the server and decoding it client-side, we’ve ensured that the "Voice of Law" remains stable and high-quality even on low-bandwidth mobile networks, bypassing all standard browser streaming limitations.

By leveraging ElevenLabs Multilingual v2, Mandamus ensures that every Indian citizen—regardless of their language or location—has a vocal, empathetic, and expert legal advisor in their pocket.

**Google Gemini**

Mandamus utilizes Gemini 1.5 Flash as the multimodal intelligence engine of the judicial platform, solving the critical bottleneck of evidence processing and legal research.

Multimodal Evidence Interpretation: We use Gemini’s native multimodal capabilities to "read" and analyze disparate evidence types—from blurry harassment screenshots to complex medical reports and handwritten complaints. It automatically extracts key entities, dates, and locations, providing authorities with instant, structured intelligence.

High-Speed Precedent Search: Gemini powers our Neural Precedent Finder, performing contextual ranking across millions of judicial records. It identifies not just matching keywords, but the "intent" and "legal reasoning" of past judgments, surfacing the most relevant precedents for any given case in seconds.

Automated Judicial Drafting: We utilize Gemini 1.5 to automate the generation of formal legal drafts, issues presented, and judicial summaries. Its large context window allows us to feed in hours of virtual hearing transcripts and hundreds of pages of evidence to produce precise, high-fidelity legal documents that are ready for court review.

By leveraging Gemini 1.5, Mandamus transforms a slow, manual judicial system into a high-speed, AI-driven infrastructure that can handle the 50-million-case backlog with professional-grade precision.

**MongoDB Atlas**

1. Secure One-Time-Password (OTP) Repository: We implemented this in otp_repository.py. It’s a specialized storage system for the temporary codes you get when you log in. It ensures that your login is secure and that the code automatically "expires" and disappears after a few minutes so no one can reuse it.
A secure way to log you in that automatically throws away your password after you use it so it's always safe.

2. Judicial Case Context System: This is implemented across our backend/main.py. It stores everything about a case in one place—including the summaries made by the AI and the notes from virtual hearings. This allows the "Draft Generator" and the "Judge Dashboard" to instantly see the full history of any case without searching through different files.
A digital folder that keeps all the AI notes and hearing details together so the judge has everything they need on one screen.

3. Silent Justice Evidence Metadata Store: In our Silent Justice module, we use MongoDB to store the "descriptions" of evidence (like photos or reports) that victims upload. It keeps a record of the evidence’s severity and type, which our Gemini AI then uses to automatically sort and route the case to the right authority.
A smart list that keeps track of all the evidence victims upload, helping the AI quickly decide which police team or NGO needs to see it first.

4. High-Availability SSL-Optimized Infrastructure We specifically configured this in client.py to handle the unique challenges of connecting from the cloud (Render/Vercel). We built a connection that is resilient to SSL handshake errors, ensuring the database is "always on" and never disconnects during a live hearing.
A super-stable connection that ensures the platform never crashes or goes offline while a judge or lawyer is using it.

**Backboard**

Backboard Integration in Mandamus
In most legal apps, you have to refresh the page to see updates—but justice can’t wait for a "Refresh" button. We integrated Backboard.io to transform Mandamus into a living, breathing judicial workspace where everything happens instantly.

Live Chatbot Memory: Our AI Legal Assistant isn’t just a simple window; it’s a shared intelligence. Using Backboard, we synchronized the Chat History and AI State in real-time. Whether a citizen is chatting on their phone or a lawyer is reviewing the same case on a desktop, the conversation stays perfectly in sync across every device, ensuring no legal detail is ever lost.

The "Shared Eyes" Feature (Unified State): During a high-stakes hearing, the Judge and Lawyers need to be on the same page—literally. We used Backboard to build a Unified Courtroom State. When a Judge selects a specific piece of evidence or highlights a case precedent, it instantly updates on the Lawyer’s dashboard. It’s like having "shared eyes" on the evidence, making the virtual courtroom feel like a single, cohesive room.

Zero-Latency Judicial Triggers: We’ve replaced slow database polling with Backboard’s Instant Signaling. Whether it’s an urgent hearing invite, a new evidence upload alert, or a real-time status change in the "Silent Justice" vault, the notification hits the relevant authority’s dashboard the millisecond it happens.

By integrating Backboard, we’ve moved away from static web pages and built a Reactive Judicial Infrastructure. From real-time chatbot persistence to collaborative courtroom dashboards, Mandamus ensures that justice moves at the speed of thought, not the speed of the browser.

Team **Kalki** -- [M. KISHORE](https://github.com/KISHORE0709-LEO), [CH V Sneha](https://github.com/chv-sneha)

`2026-05-10`

---

### Tutelaris
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tutelaris-5d08) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bshreyakamath/Tutelaris) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Tutelaris is an AI-powered womem saftey platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Google Maps API](https://img.shields.io/badge/Google%20Maps%20API-333333?style=flat-square) ![gTTS](https://img.shields.io/badge/gTTS-333333?style=flat-square)

**The problem it solves**

Women and individuals travelling alone in taxis, auto-rickshaws, or vans may encounter unsafe situations where openly calling for help or activating an SOS feature could escalate the situation.During such incidents, fear or panic may make it difficult to interact with a safety application
manually. Existing solutions often depend on active user intervention, while the absence of readily available evidence and location information can make incident reporting more difficult. With the growing use of ride-sharing and public transportation, advances in artificial intelligence, smartphones, GPS, and location-based technologies provide an opportunity to develop discreet and proactive safety solutions without requiring additional hardware.
Tutelaris combines discreet AI assistance, incident evidence collection, location-based safety support, and emergency navigation within a single platform. Instead of relying exclusively on a conventional SOS interaction, the system provides multiple forms of assistance that can be used
at different stages of a potential safety incident, reducing dependence on continuous manual interaction.

**Challenges we ran into**

Real-time Emergency Alerts: Ensuring alerts and recorded evidence reach the [](url)correct emergency contacts quickly.
• Accurate Location Tracking:  Maintaining reliable GPS tracking,
especially in areas with weak signals.
• Safe Route Selection: Providing routes that prioritize safety and
accessibility, not just the shortest distance.
• Audio Recording: Starting and saving the recording quickly during a stressful emergency situation.
• Privacy & Security: Protecting users' personal information, location data, and recorded evidence from unauthorized access.
• Network Issues: Ensuring critical features work as reliably as possible when internet connectivity is poor.
• False/Accidental Alerts: Preventing accidental SOS activation while still keeping the emergency process fast.
• Integration: Connecting the mobile app, database, maps/location services, and emergency notification system into one reliable workflow.

**Women Safety**

Women and individuals travelling alone in taxis, auto-rickshaws, or vans may encounter unsafe situations where openly calling for help or activating an SOS feature could escalate the situation.During such incidents, fear or panic may make it difficult to interact with a safety application manually. Existing solutions often depend on active user intervention, while the absence of readily available evidence and location information can make incident reporting more difficult. With the growing use of ride-sharing and public transportation, advances in artificial intelligence, smartphones, GPS, and location-based technologies provide an opportunity to develop discreet
and proactive safety solutions without requiring additional hardware.

Team **Out of box thinkers** -- Srusti Shetty, Melisha Lewis, Shreya Kamath, Srishti P, [Bhumika C.S](https://github.com/BhumikaCS)

`2026-08-16`

---

### Semver-cli
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/semvercli-ece2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Divyanshi88/Server_CLI-) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Hriqi82TRb0) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Fast Semantic Versioning from the command line

![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![vs code](https://img.shields.io/badge/vs%20code-333333?style=flat-square) ![Cargo](https://img.shields.io/badge/Cargo-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square) ![Proptest](https://img.shields.io/badge/Proptest-333333?style=flat-square)

**The problem it solves**

The problem it solves
Managing software versions looks simple until prerelease tags, build metadata, sorting rules, and compatibility ranges become involved. Basic string comparison can produce incorrect results—for example, treating 1.0.0-beta.11 as lower than 1.0.0-beta.2.
SemVer CLI provides a fast and reliable way to work with Semantic Versioning 2.0 directly from the terminal. Developers can use it to:
Parse versions into major, minor, patch, prerelease, and build components.
Compare versions using correct semantic precedence instead of unsafe string comparison.
Sort stable and prerelease versions accurately.
Check whether a version satisfies npm-compatible caret and tilde ranges.
Validate version input before publishing packages or creating releases.
Automate version checks in scripts, release pipelines, and CI/CD workflows.
Built in Rust, it is lightweight, predictable, and resistant to malformed input. Its behavior is verified through 47 unit, integration, property-based differential, and range tests.
SemVer CLI makes release automation easier and safer by replacing custom version-handling logic with one tested command-line tool.

**Challenges we ran into**

Challenges I ran into
One of the biggest challenges was implementing Semantic Versioning precedence correctly. Versions cannot be compared as ordinary strings—for example, beta.11 must rank higher than beta.2, while build metadata must not affect precedence. I solved this by representing numeric and alphanumeric identifiers separately and testing the official SemVer ordering examples.
Prerelease range behavior was another difficult area. A range such as ^1.2.3 must reject prerelease versions by default, while ^1.2.3-alpha.1 may accept later prereleases only for the same major, minor, and patch version. I aligned the implementation with npm’s node-semver behavior and added dedicated caret, tilde, and prerelease tests.
I also encountered a missing Python semver dependency while running differential tests. This caused property tests to repeatedly reject cases instead of finishing normally. After installing the required module, I reran the complete optimized suite successfully.
To increase confidence beyond hand-written examples, I added property-based differential tests that compare the Rust implementation against Python SemVer across generated inputs. The final result passes all 47 unit, integration, differential, and range tests.

[Divyanshi Sharma](https://github.com/Divyanshi88)

`2026-08-03`

---

### croniter-rs
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/croniterrs-ed98) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/moneytosms/croniter-rs) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/Y0Zg8jbhxg8) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Y0Zg8jbhxg8) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> A Rust port of Python's croniter

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![pytest](https://img.shields.io/badge/pytest-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Github Action](https://img.shields.io/badge/Github%20Action-333333?style=flat-square) ![Serde](https://img.shields.io/badge/Serde-333333?style=flat-square) ![Proptest](https://img.shields.io/badge/Proptest-333333?style=flat-square) ![Chrono](https://img.shields.io/badge/Chrono-333333?style=flat-square)

**Challenges we ran into**

The one that took the longest to find was three orders of magnitude smaller than anything
we thought we were looking for.

`get_prev` was occasionally returning a fire time a whole day early. Not slightly wrong, a
whole day. Python's `datetime` stores whole microseconds. chrono, the Rust date library,
keeps nanoseconds. A start time one microsecond past the second lands about 954
nanoseconds past it once it goes through a float. The backward search subtracts one
microsecond to look just before that instant, which in Python lands exactly on the second
and in Rust landed 46 nanoseconds below it. Zeroing the seconds field then rounded that
into the previous minute, and the whole search fell through to the day before.

You cannot find that by reading the code. Both versions look correct. We only found it
because we were diffing against a real reference implementation at full precision.

The more uncomfortable lesson was why it took so long. Our corpus extractor had a bug of
its own: it recorded the constructor keyword arguments onto one record type and rebuilt
everything else from scratch, so zero of 3,128 `next` records carried a single keyword.
Around 1,538 calls made against non-default croniters were being replayed as defaults. Our
evidence was making the port look more correct than it was, which is worse than the port
being wrong, because you do not go looking. Fixing the extractor is what made the
microsecond bug visible at all.

Two other things worth mentioning.

Differential fuzzing found a case in Sydney in the year 2100 where our port and Python
disagreed by exactly one hour. Same local time, different UTC offset. That one was not
ours. chrono-tz compiles a fixed table of DST transitions and holds the last offset
forever once it runs past the end, while Python keeps evaluating the rule indefinitely.
They agree through 2099. There was nothing to fix, so we pinned the boundary with a test
that will fail if chrono-tz ever extends its table, and capped the fuzzer at 2099 so it
stops comparing two timezone databases and goes back to comparing two croniters.

And late on, while checking our work, we found three open bug reports against the original
Python library filed by other people. We tested all three against our port. We reproduce
all three exactly. That was the right outcome rather than a disappointing one, since the
whole goal is behavioural equivalence, and fixing a bug that callers may already have
worked around would quietly break them. They are pinned by tests now, so if upstream ever
fixes one, our test fails and tells us to go and look.

**The problem it solves**

croniter is the library that answers one deceptively simple question: given a cron
expression like `*/30 1-3 * * *` and a point in time, when does it fire next, and when did
it last fire. A lot of Python schedulers lean on it to decide when work actually runs.

The problem with rewriting something like this in a faster language is that cron is not
simple. It is fifteen years of accumulated edge cases. Daylight saving time creates local
times that happen twice and local times that never happen at all. There is a
day-of-month/day-of-week rule inherited from vixie-cron that looks like a bug and is
deliberate. There is `L` for last day of month, `W` for nearest weekday, `#` for nth
weekday, and hash-scheduled expressions that spread load deterministically across a fleet.

A rewrite that gets any of those subtly wrong does not crash. It just runs your job at the
wrong time, quietly, maybe once a year when the clocks change. That is the failure mode we
cared about.

So we did not set out to write a cron library. We set out to write a cron library that we
could prove behaves the same as the one people already depend on. What you get is a single
Rust binary with no Python runtime needed, a good deal faster, that we can show returns
the same answers as the original on 15,827 recorded calls and passes the original
project's own 248-test suite without us editing a single line of it.

The verification is honestly the part we would want someone to look at. The hackathon rule
was that the port cannot link into the Python runtime, no PyO3, no embedded interpreter.
So we ran the original test suite once under instrumentation and recorded every call it
made, what was asked and what Python answered, into a golden corpus that pure Rust replays
with no Python present. Then, separately, we wrote a small Python shim that satisfies
`import croniter` and forwards every call to the Rust binary over a pipe, which lets the
untouched original test suite run live against our port. Python calls out to Rust as an
external program, which is the legal direction. Either layer would stand on its own.

Team **Sanctum** -- [Srimoneyshankar Ajith](https://github.com/moneytosms), [Nidhi Rakesh](https://github.com/nidheerakesh)

`2026-08-03`

---

### Rustify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rustify-92ba) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jamshed-Ahmad/Rustify.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uYQvvJVhtyk) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Rustify: 100% parity, 14x faster performance.

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square)

**The problem it solves**

The problem Rustify solves
While python-slugify is the industry standard for generating SEO-friendly, Unicode-aware URLs in the Python ecosystem, it relies on a full Python runtime and external dependencies like text-unidecode
. For high-performance web gateways, lightweight CLI tools, or cloud-native environments requiring predictable latency, spinning up a Python interpreter introduces significant overhead in cold startup times and memory consumption.
Our project, Rustify, is a pure-Rust port that completely eliminates the Python runtime dependency. It provides a standalone, native implementation that is mathematically proven to be 100% behaviorally equivalent to the original, even when handling complex Unicode transliterations
.
How it makes existing tasks better:
By moving this slugification engine to 100% safe Rust, we solved the inherent performance bloat of interpreted runtimes. Our port allows developers to run robust URL generation in systems programming and high-performance backends with massive efficiency gains:
32x Faster Startup: Cold invocations dropped from 38.5ms (Python) to just 1.2ms (Rust).
91.5% Memory Reduction: Peak memory footprint (RSS) was slashed from 24.8 MB to a mere 2.1 MB.
14.2x Throughput Increase: Processing speed jumped from 42.5k ops/sec to 603.5k ops/sec on identical workloads.
Furthermore, we achieved this with Zero Unsafe Code, enforcing #![forbid(unsafe_code)] at the crate root to ensure memory safety without the risky "escape hatches" often seen in AI-assisted migrations
.
Challenges we ran into
The 'Untouched Test Suite' Constraint One of the strictest rules of the Port Mortem hackathon is preserving test parity without modifying the original test suite files
. We needed a way to force a Python pytest suite to validate a compiled Rust binary.
How we got over it: We engineered a highly innovative thin adapter bridge (tests/test_adapter.py). By using Python's subprocess module, we intercepted original module calls and routed all slugification requests to our Rust binary (target/release/rustify). This allowed us to achieve 100% test parity (82/82 tests) without touching a single file in the original repository
.
Windows Linker and Sanitizer Blockers During final compilation on Windows, we encountered a persistent error: linker link.exe not found and discovered that Address Sanitizer (ASan)—a requirement for cargo-fuzz—is not supported on standard Windows targets. This threatened our "Differential Fuzz Survivor" bonus.
How we got over it: To satisfy Rule 03 (Standalone & Runnable), we bypassed local host limitations by implementing a multi-stage Dockerfile
. By moving the build process to a Linux-based container (rust:1.80-slim), we gained access to stable sanitizers and native linkers, ensuring the project remains portable and buildable with a single command.
Differential Fuzzer Divergences To claim the +5 Bonus, our fuzzer needed to run continuously for 60 seconds with zero divergences
. Initially, our Rust port diverged from Python when handling specific Unicode edge cases and word-boundary truncation logic.
How we got over it: We re-engineered our internal regex engine to mirror Python's specific Unicode boundaries and programmatically matched python-slugify's "smart truncation" behavior. We successfully ran the final loop for 65 continuous seconds, evaluating thousands of randomized cases with zero divergences, securing our status as a "Differential Fuzz Survivor."

**Challenges we ran into**

Test Parity: Achieved 100% parity using a thin adapter bridge to run the original, unmodified Python test suite against the Rust binary

Environment Blockers: Bypassed Windows linker errors (link.exe) and limited sanitizer support by pivoting to a multi-stage Dockerfile for a portable build

Unicode Parity: Re-engineered internal regex logic to mirror Python’s NFKD normalization and specific word-boundary behaviors.
Fuzzing Divergences: Resolved edge-case discrepancies to survive a 65-second differential fuzzing run with zero failures

Team **The Last Commit** -- Vicky Patil, Jamshed Ahmad, Sairaj Deshpande, Alex Sawant

`2026-08-03`

---

### MakeMyShow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/makemyshow-1c45) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Pratheek555/makemyshow) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://makemyshow-nine.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Performances that reach the right fans!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

***THE PROBLEM:***
Fans struggle to bring artists to their city.
Artists cannot easily measure local demand.
Traditional booking involves uncertainty and financial risk.

*****HOW WE SOLVE IT*****
MakeMyShow creates demand-backed city drops.
Fans make capped commitments for potential shows.
Artists can review demand before confirming.

*****Why is it useful today?*****
It connects artists with genuine local audiences.
It reduces risk before venues and tickets are booked.
It helps fans turn interest into real events.

***What you plan to build next?***

We plan to add smart venue matching.
Artists will get richer analytics and campaign tools.
We will improve ticketing and automated settlement.
Mainly adding a agentic layer to help ai agents book mandates and discover them better.

**Challenges we ran into**

- Prava sometimes had "internal server errors" which was sometimes was adding a overhead to the project completion time

other than that not many, everything went smooth

**Most Startup-Ready Product**

MakeMyShow is a startup ready product and is perfect to get started in our Country India because of how diverse the country is.

For example my college is random village out of nowhere has 20,000 students who are easily willing to pay for good performances. 

Good events are not only for the Big cities, with the right crowd (which artist discovers through MakeMyShow) and artist the possibilities are endless.

Currently the platform aggregates demand and eventually will open up for students to run campaigns to get their favorite artist to their locality.

This is a problem that's dear to me, felt like I have been running through my whole university life without good events to go to and I feel that's the same problem everywhere too. 

We will eventually also be solving the on ground venue quality and other important things.

[Pratheek Ravikumar](https://github.com/Pratheek555/Stack-development)

`2026-08-03`

---

### Warden
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/warden-d9cb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abhyuday404/Warden) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://warden-guarded-deploy.geekyabhi6387.chatgpt.site/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SB48ewRbHGI) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Deploy Easily

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square)

**The problem it solves**

Ever had issues trying to deploy your application/projects? We solve that right in your CLI without needing to go anywhere with proper payment integration done through Prava.
Just launch `ward` and tell it all you need to do, because along with helpful commands for all your needs, its agentic and will understand and tend to all your deployment needs.

**Challenges we ran into**

->Making this platform agnostic because different cloud providers perform differently and have different requirements on how they process things.
How we solved this is have a plug and play system for all kinds of providers so you can just write a plugin yourself for a cloud provider you need to be integrated in this.

->Cloud providers usually don't just work on a pay once basis, so we had to get around the limitations of that and instead work on a budget gate basis to handle payments

Team **minions** -- Priyank Garg, [Advay Vivek](https://github.com/AdvayV), [Abhyuday Rai](https://github.com/abhyuday404), Kaavish Gogia

`2026-08-03`

---

### RAVEN
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/raven-e4cf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HimanshuM685/RAVEN) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://raven.007575.xyz/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/pAMIiey4wiM) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> RENT YOUR COMPUTE POWER, MAKE YOUR AGENT PROUD

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![DigitalOcean](https://img.shields.io/badge/DigitalOcean-333333?style=flat-square) ![SolanaSDK](https://img.shields.io/badge/SolanaSDK-333333?style=flat-square)

**Challenges we ran into**

### The reaper was eating live leases

Renters kept getting `Connection closed` seconds after a lease went active. The
daemon log had the answer, once we read it carefully:

    lease 2509060c-e5e2-4f3e-8b8b-144a474ee57f up: ssh root@bore.pub -p 48372
    reaped 2 orphan sandbox(es): 2509060c, contributor-1

Two bugs in one line. Containers were named `raven-<first 8 chars of lease id>`, and
the orphan reaper *reconstructed* the lease id from that name — so it compared
`2509060c` against the full UUID the daemon held, never matched, and destroyed every
live lease one tick after it started. Worse, the `name=raven-` filter also matched
`raven-contributor-1`: the daemon was reaping **itself**, and would have taken
`raven-backend-1` and `raven-web-1` with it on a shared host.

The fix was to stop deriving identity from a human-readable name. Containers now
carry `raven.lease=<full uuid>` and `raven.role=sandbox` labels, and the reaper
filters on the label. Names became cosmetic. The original test used a fake backend
and never exercised the name parsing, so we added a regression test that asserts the
full id survives, that an unlabelled `raven-contributor-1` row is ignored, and that a
running lease is never reaped.

### "Connection closed" that was four different bugs wearing a trenchcoat

The same symptom kept coming back for unrelated reasons, and each one looked
identical from the renter's side — TCP connects, then dies before the SSH banner.

1. **Over-hardening.** We had shipped `--read-only` and `--cap-drop=ALL`. But the
   sandbox writes SSH host keys and the root password at boot, and sshd's privilege
   separation needs `SYS_CHROOT`. Under `set -e` the entrypoint died instantly — yet
   the *tunnel* container stayed up, so the relay happily accepted connections to
   nothing. We dropped `--read-only` and re-added exactly the seven capabilities sshd
   needs, no more.
2. **A firewall hop nobody could see.** The tunnel forwarded to the sandbox's
   published port via `host.docker.internal` — traffic from the Docker bridge back
   into a host port, which Ubuntu's default `ufw` rules silently drop.
3. **No readiness gate.** The daemon advertised the lease the instant the relay
   printed a port, so renters could connect before `ssh-keygen -A` finished.
4. **A 60-second TTL floor** meant a thin balance self-destructed the box mid-session.

The structural fix collapsed the whole design: the tunnel client now runs *inside* the
sandbox container as its main process, so there is one container per lease, no bridge
hop, no host port published at all, and the container's lifetime **is** the tunnel's
lifetime. On top of that, the daemon refuses to advertise a lease until it has dialed
the public address itself and seen a real `SSH-2.0` banner come back — so a relay that
accepts a port and drops the traffic fails loudly on our side instead of silently on
the renter's.

### A deposit that took the money and credited nothing

A wallet returns a transaction signature the moment it *sends*, not when it confirms.
Our top-up endpoint did a single `getTransaction` at `confirmed`, which almost always
ran ahead of the chain and returned null — so the SOL had left the user's wallet and
their balance still read zero, with the signature gone forever once they closed the
tab.

We fixed it on both sides: the registry polls for confirmation and returns a
**retryable 409** rather than a generic error, and the browser parks the signature in
`localStorage` before calling, clears it only on success, and retries on next load.
Crediting is idempotent by transaction id, so retrying is free and can never
double-credit. A permanently bad signature is dropped instead of retried forever.

### Static bundles bake their config at build time

The UI would load perfectly and then fail every API call with `Failed to fetch`.
`NEXT_PUBLIC_REGISTRY_URL` is inlined at build time, `.dockerignore` kept `web/.env`
out of the build context, and Compose interpolates build args from the *shell* — not
from `env_file`. So the "correct" URL in `web/.env` was never read by anything, and
the default (`localhost:4000`) got baked in, pointing every visitor at their own
machine. We made the image proxy `/api` to the backend on its own origin so the
default is correct with zero configuration, and made fetch failures name the exact
URL that failed instead of the browser's useless generic message.

**The problem it solves**

# The problem it solves

Renting a GPU or a spare box today means a cloud account, a credit card, a minimum
billing increment, and a signup flow — and on the other side, a machine that sits
idle 90% of the day earning nothing. RAVEN is a marketplace that removes both.

**For the renter.** Connect a Solana wallet, top up, click Rent. You get an `ssh`
command, a per-lease root password, and the box's host-key fingerprint. You are
billed **per second** at the node's advertised rate, and the moment you click
Release — or your balance hits zero — the sandbox is destroyed and you stop paying.
No account, no card, no minimum, no idle charges. The autonomous path is the same
API: an agent signs in, tops up, rents the cheapest node, SSHes in, runs a job, and
releases, with no human in the loop.

**For the contributor.** One command shares a machine:
`docker compose up -d --build contributor`. No wallet or private key ever touches
that box — the daemon holds only an opaque bearer key, and the registry signs
payouts server-side. **No inbound ports and no port forwarding:** each lease dials
*out* through a reverse tunnel, so a laptop behind NAT can earn without touching a
router. Earnings settle on-chain automatically at the end of every lease.

**What makes it safer than "here's SSH to my box."** Every lease is a throwaway
container with no bind mounts, bridge networking, every Linux capability dropped
except the handful sshd needs, `no-new-privileges`, no swap, and capped CPU/RAM/PIDs.
Credentials are generated per lease, passed as env and unset before anything can read
them via `docker inspect`, and never logged. A hard TTL inside the guest plus a
reaper on the host guarantee a sandbox never outlives its lease — even if the
registry dies. And because renters get the host-key fingerprint up front, they can
verify the machine instead of trusting it on first connect.

**Best Use of Solana**

Solana isn't a payment button bolted on the side it's the identity layer, the
funding rail, and the settlement rail for a per-second compute market.

**Wallet is the only account system.** There is no email, no password, no user table.
Both roles authenticate the same way: `GET /auth/nonce` issues a single-use nonce,
the wallet signs `Sign in to RAVEN: <nonce>` via wallet-standard (Phantom / Solflare /
Backpack), and the server verifies the ed25519 signature against the claimed pubkey
with tweetnacl before minting a 24h JWT. One session serves both the renter and the
contributor dashboard — the same wallet is a buyer when it rents and a contributor
when it hosts.

**Top-ups are real transfers, verified on-chain — not trusted from the client.** The
browser builds and signs a `getTransferSolInstruction` transfer with `@solana/kit`,
and hands the registry only the resulting signature. The server then re-derives the
truth from the chain: fetch the transaction, reject it if `meta.err` is set, require
the depositor to appear as a **signer** in `accountKeys`, and compute the credit as
`postBalances[platform] - preBalances[platform]` the actual lamport delta on the
platform account. A client claiming "I sent 10 SOL" is worth nothing.

**Payouts settle on-chain automatically, per lease.** When a lease ends, the registry
bills the exact seconds used and immediately signs a SOL transfer to the contributor's
payout address, confirmed over `sendAndConfirmTransactionFactory`. The contributor's
machine never holds a wallet, a keypair, or a payout address — it authenticates with
an opaque bearer key, and the registry resolves that key to an address server-side.
`PLATFORM_PRIVATE_KEY` is read in exactly one function, server-side, at payout time.

**Money is lamports as `bigint`, end to end.** Rates, balances, charges and payouts are
BigInt in TypeScript and BSON Long in MongoDB (`useBigInt64`), so there is no float
anywhere in the billing path. Prorated cost is integer math:
`rate * ceil(seconds) / 3600n`.

**Honest scope:** balances are a custodial off-chain ledger, not an on-chain program.
That's deliberate — per-second billing with an on-chain debit per tick would cost more
in fees than the compute. Deposits and payouts are on-chain and verifiable; the metering
in between is not. `MAINNET=true` flips the whole stack from devnet to mainnet-beta.

**Best Use of DigitalOcean**

A Droplet plays a role here that no contributor machine can: it is the one host with a
**stable public address**, and the entire NAT-traversal design depends on that.

**The Droplet is the rendezvous point that makes home hardware rentable.** Contributors
run on laptops and boxes behind NAT with no port forwarding and no public IP. Each
lease's sandbox dials *out* to a `bore` relay running on the Droplet (`network_mode:
host`, control port 7835, a configurable range like 49152-49215 for live leases), and
the renter SSHes to a port on the Droplet. Without a fixed public host in the middle,
a marketplace of consumer machines simply doesn't work — the Droplet turns a laptop on
home Wi-Fi into a rentable node with zero router configuration.

**One `docker compose up -d` brings up the whole operator side.** Registry (Express),
the static web app behind nginx, and the tunnel relay are three services in one file.
Contributor and buyer sit behind Compose *profiles*, so a bare `up` on the Droplet
never accidentally starts a contributor daemon — while `docker compose up -d
contributor` on a shared machine enables its profile automatically. Two commands, two
roles, no extra steps.

**nginx on the Droplet solves a real cross-origin problem.** The web app is a Next.js
static export, so `NEXT_PUBLIC_*` values are baked in at build time — an absolute
`http://` API URL is blocked as mixed content behind HTTPS, and `localhost` in a static
bundle means the *visitor's* machine. The web image proxies `/api/` to the backend
service on the same origin, so the default configuration is correct with no build args,
no CORS, and no second TLS certificate.

**The Droplet also shaped the security architecture — by what it can't do.** Standard
Droplets don't expose `/dev/kvm`, so a Firecracker microVM tier was prototyped and then
removed in favour of hardened containers that run anywhere Docker does. The README says
plainly what that costs: the sandbox shares the contributor's kernel. Choosing the
boundary the hardware can actually deliver, and documenting it, beat advertising an
isolation tier we couldn't honour.

**Best Use of MongoDB Atlas**

MongoDB holds **only the money** balances, deposits, charges, payouts, sign-in nonces
and contributor keys. Nodes and live leases stay in memory on purpose, so heartbeats and
the billing watchdog never touch the database. That split keeps the write path tiny and
makes every collection a financial record.

**Idempotency comes from the schema, not from application locking.** `deposits._id` is
the Solana transaction signature. Crediting a top-up inserts that document first: a
duplicate signature throws `E11000` and the `$inc` is skipped. A confirmed deposit
therefore **cannot** credit twice, no matter how many times a flaky client retries —
which is exactly what let us make the browser retry a pending deposit on every page
load until it lands, instead of losing the user's SOL when a tab closed.

**Balances can't go negative, atomically.** Charging a finished lease uses an
aggregation-pipeline update:
`$max: [{ $subtract: ['$balance', lamports] }, 0]` Mongo's equivalent of
`greatest(x, 0)`, applied in a single atomic operation rather than a read-modify-write
race across concurrent leases.

**Money never becomes a float.** The driver runs with `useBigInt64: true`, so lamports
round-trip as BSON Long ↔ JS `bigint` with no precision loss anywhere in the ledger.

**A TTL index does the session-security housekeeping.** Sign-in nonces are stored with
`_id = wallet address` (so a wallet has at most one live nonce, and a new request
invalidates the old), read via `findOneAndDelete` (single use, atomically), and swept by
a TTL index on `expiresAt` with `expireAfterSeconds: 0`. Expired nonces clean themselves
up — no cron, no sweeper job.

**Both dashboards are aggregation pipelines, not N+1 loops.** The buyer roll-up
(`$group` over `charges`) returns lease count, total seconds and total spent in one
round trip. The contributor roll-up joins `payouts` to `charges` with `$lookup` on
`leaseId` to report earnings, seconds served, and via
`$sum: { $cond: [{ $eq: ['$txid', null] }, '$lamports', 0] }` the amount *earned but
not yet settled on-chain*, distinguishing "we owe you" from "we paid you" in a single
query. Indexes match the access patterns exactly: `{address, createdAt}` on charges,
`{payto, createdAt}` on payouts, `{address}` on contributor keys.

**Known limitation, documented in the code:** crediting a deposit is two writes without
a multi-document transaction (Atlas needs a replica set for that), so a crash between
them drops one credit. It's marked in-source with the fix wrap in
`session.withTransaction` rather than left as a silent hazard.

**Best Use of DigitalOcean**

How does this project fit within the track?

A Droplet plays a role here that no contributor machine can: it is the one host with a
stable public address, and the entire NAT-traversal design depends on that.

The Droplet is the rendezvous point that makes home hardware rentable. Contributors
run on laptops and boxes behind NAT with no port forwarding and no public IP. Each
lease's sandbox dials out to a
bore

relay running on the Droplet (
network_mode: host

, control port 7835, a configurable range like 49152-49215 for live leases), and
the renter SSHes to a port on the Droplet. Without a fixed public host in the middle,
a marketplace of consumer machines simply doesn't work — the Droplet turns a laptop on
home Wi-Fi into a rentable node with zero router configuration.

One
docker compose up -d

brings up the whole operator side. Registry (Express),
the static web app behind nginx, and the tunnel relay are three services in one file.
Contributor and buyer sit behind Compose profiles, so a bare
up

on the Droplet
never accidentally starts a contributor daemon — while
docker compose up -d contributor

on a shared machine enables its profile automatically. Two commands, two
roles, no extra steps.

nginx on the Droplet solves a real cross-origin problem. The web app is a Next.js
static export, so
NEXT_PUBLIC_*

values are baked in at build time — an absolute
http://

API URL is blocked as mixed content behind HTTPS, and
localhost

in a static
bundle means the visitor's machine. The web image proxies
/api/

to the backend
service on the same origin, so the default configuration is correct with no build args,
no CORS, and no second TLS certificate.

The Droplet also shaped the security architecture — by what it can't do. Standard
Droplets don't expose
/dev/kvm

, so a Firecracker microVM tier was prototyped and then
removed in favour of hardened containers that run anywhere Docker does. The README says
plainly what that costs: the sandbox shares the contributor's kernel. Choosing the
boundary the hardware can actually deliver, and documenting it, beat advertising an
isolation tier we couldn't honour.

Team **PiedPiper** -- [Himanshu Malik](https://github.com/HimanshuM685), [Ratnadwip Sarkar](https://github.com/RealRatnadwip), [Koushik Mondal](https://github.com/Koushikmondal06)

`2026-07-26`

---

### ARGUS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/argus-8eac) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/100376-govind/ARGUS) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/CWmactP0iLU?feature=shared) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/CWmactP0iLU?feature=shared) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> From information chaos to optimal crisis response

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Google Maps API](https://img.shields.io/badge/Google%20Maps%20API-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Geocoding](https://img.shields.io/badge/Geocoding-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Direction API](https://img.shields.io/badge/Google%20Direction%20API-333333?style=flat-square) ![nest.js](https://img.shields.io/badge/nest.js-333333?style=flat-square)

**The problem it solves**

ARGUS is built to solve:

- Information Overload: During large-scale disasters such as floods, earthquakes, fires, and industrial accidents, emergency command centers receive thousands of distress reports from multiple sources within a short period. Processing this volume of information manually becomes extremely difficult.

- Delayed Emergency Response: Emergency personnel spend valuable time verifying reports, assessing their severity, and coordinating response efforts. These delays can significantly impact rescue operations during the critical "Golden Hour."

- Duplicate and Unverified Reports: Multiple citizens often report the same incident using different descriptions, while some reports may be incomplete, inaccurate, or misleading. This increases the risk of duplicate dispatches and inefficient resource utilization.

- Lack of Automated Incident Validation: Most existing emergency response systems rely heavily on manual verification, making it difficult to quickly distinguish genuine incidents from duplicate or low-confidence reports.

- Inefficient Incident Prioritization: Determining which emergencies require immediate attention is challenging when hundreds of incidents arrive simultaneously. Critical cases may be delayed while less severe incidents consume valuable operational resources.

- Suboptimal Resource Allocation: Emergency resources such as ambulances, fire brigades, police units, and disaster response teams are limited. Without intelligent prioritization and validation, these resources may not be deployed in the most effective manner.

- Limited Decision Support: Traditional systems primarily collect and display information but provide limited assistance in analyzing reports, identifying patterns, or supporting operational decision-making.

- Lack of Unified Situational Awareness: Emergency operators often have to interpret information from multiple disconnected sources, making it difficult to obtain a comprehensive real-time understanding of the overall situation.

- Limited Transparency and Accountability: Manual decision-making processes often lack detailed reasoning and audit trails, making post-incident analysis, reporting, and operational review more challenging.

How ARGUS Addresses These Challenges

- Automatically ingests and structures emergency reports from multiple data sources.
- Prioritizes incidents using AI based on severity, contextual understanding, and potential impact.
- Validates incidents by correlating common keywords, locations, timestamps, and supporting reports from multiple independent sources.
- Reduces duplicate incidents and minimizes false positives before emergency resources are deployed.
- Assists emergency responders by recommending optimal resource allocation based on validated incident priority.
- Provides a real-time tactical command dashboard with explainable AI-generated insights to support informed decision-making.
- Maintains comprehensive audit logs, reasoning traces, and incident timelines to improve transparency and post-incident analysis.
- Enables emergency management agencies to respond more quickly, accurately, and efficiently during high-volume disaster scenarios.

**Challenges we ran into**

1. Validating Emergency Reports Without Reliable Ground Truth

One of the biggest challenges was determining whether an incoming distress report was genuine. During large-scale disasters, command centers receive hundreds or thousands of reports describing the same event in different ways. Some reports are incomplete, duplicated, exaggerated, or even false. Simply trusting every report would lead to unnecessary deployment of emergency resources, while rejecting genuine reports could delay life-saving operations.

Our Solution: AI-Powered Evidence Correlation

Instead of relying on a single report, we implemented a Caller Triangulation and Evidence Correlation Engine.

The Field Validator automatically compares each incoming incident with all previously received reports and looks for supporting evidence by analyzing:

Common Keywords: Identifies recurring terms such as flood, fire, collapsed building, smoke, or explosion across independent reports.
Location Clustering: Groups reports originating from the same locality or nearby geographic coordinates, even when different users describe the location differently.
Call Pattern Analysis: Detects clusters of reports arriving within a short time window, indicating that multiple independent sources are witnessing the same incident.
Incident Similarity: Compares disaster type, affected area, timestamps, and contextual descriptions to calculate an overall similarity score.

The AI combines these signals to produce a Validation Confidence Score. If several independent reports consistently point to the same event, ARGUS automatically increases confidence and marks the incident as verified. This approach significantly reduces false positives while improving trust in the system's recommendations.

2. Reducing Operational Runtime Without Sacrificing Accuracy

Another major challenge was maintaining fast response times. The Field Validator was designed to use multiple validation techniques, including evidence correlation and AI-based Wi-Fi Environment Intelligence. Running every validation method sequentially for every incident increased processing time and unnecessary computational cost.

Our Solution: Priority-Based Validation Pipeline

To optimize execution, we redesigned the validation workflow into a priority-driven pipeline.

Every incident first undergoes Evidence Correlation, which is computationally lightweight and quickly checks whether multiple independent reports already confirm the event.

If the resulting confidence score exceeds a predefined threshold, the incident is immediately marked as sufficiently validated, and additional validation steps are skipped.

Only when the confidence is below the threshold does ARGUS invoke the secondary validation layer, such as AI-based Wi-Fi Environment Intelligence, to gather additional supporting evidence.

This conditional execution strategy provides two major benefits:

Lower average processing time, because expensive validation modules are executed only when necessary.
Improved scalability, allowing ARGUS to process a much larger number of concurrent incidents during mass casualty events.

By intelligently bypassing unnecessary computations, the platform maintains both speed and validation accuracy, ensuring that emergency responders receive reliable information as quickly as possible.

3. Making AI Decisions Transparent and Trustworthy

Emergency response systems cannot rely on opaque AI decisions. Operators need to understand why an incident received a particular priority or validation score before committing valuable rescue resources.

Our Solution: Explainable AI

Instead of exposing complex model reasoning, ARGUS generates concise, human-readable explanations for every important decision.

For each validated incident, the system presents:

Number of supporting reports
Common keywords detected
Matching locations
Similarity scores
Validation confidence
Short reasoning bullets explaining why the incident was verified

This enables emergency commanders to quickly audit the AI's recommendations while maintaining confidence in the decision-making process.

4. Handling High Volumes of Concurrent Emergency Reports

Mass casualty events often generate thousands of reports within minutes. Sequential processing quickly becomes a bottleneck, increasing latency precisely when rapid response is most critical.

Our Solution: Modular Multi-Agent Architecture

We designed ARGUS as a chain of specialized AI agents, each responsible for a single task:

Data Dispatcher structures incoming reports.
Risk Evaluator assigns priority based on severity and context.
Field Validator verifies incidents through evidence correlation and additional validation when needed.
Resource Allocator recommends optimal deployment strategies.
Compliance Auditor records every decision for transparency and accountability.

Each agent operates independently and passes structured outputs to the next stage, enabling parallel processing, easier debugging, and be

Team **Team Brahmastra** -- [Govind Raj Gupta](https://github.com/100376-govind), [Archita Chakraborty](https://github.com/Architachak2005), [Pankaj Kumar Gupta](https://github.com/PankajGupta-dev), [Rupanjan Saha](https://github.com/RupanjanSaha123)

`2026-07-12`

---

### NeuroForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neuroforge-0a0a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saurabhksatya/NeuroForge) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-training-orcin.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Train • Visualize • Compare • Predict

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Integrating machine learning workflows into a web-based environment while keeping the interface simple and intuitive.

Managing model training and evaluation efficiently while maintaining responsive user interactions.

Providing customization options for neural networks and reinforcement learning without overwhelming users with complexity.

Ensuring compatibility between frontend interactions and backend training processes.

**The problem it solves**

Machine learning tools are often fragmented, requiring users to switch between multiple platforms for data preprocessing, model training, evaluation, visualization, and experimentation. This creates a steep learning curve for students, beginners, and researchers.

NeuroForge solves this by providing a unified platform where users can upload datasets, train and compare machine learning models, build neural networks, experiment with reinforcement learning, visualize results, and export models—all from a single browser-based interface.

Team **Barely Functional** -- Ishan S Bhat, Om Patel, Utkarsh Raj, Saurabh Satya

`2026-06-14`

---

### ShadowMesh AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shadowmesh-ai-cc00) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/souma9830/ShadowMess-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/7_Mg54j9A6U?si=IWxYYHVe0v0T4P3W) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/7_Mg54j9A6U?si=IWxYYHVe0v0T4P3W) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Turning Cyber Attacks into Actionable Intelligence

![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

# The Problem ShadowMesh Solves

## Background

Modern organizations invest heavily in firewalls, endpoint protection, intrusion detection systems, and security monitoring tools. While these solutions help detect or block attacks, they often fail to answer critical questions after an attacker enters the network:

* Who is the attacker?
* What are they trying to achieve?
* How skilled are they?
* Which systems are they targeting?
* What techniques and tools are they using?
* What will they do next?

Traditional security solutions are primarily focused on prevention and detection. They generate alerts but provide limited insight into attacker behavior and intent.

---

## The Challenge

Security teams face several challenges:

* Large volumes of security alerts leading to analyst fatigue.
* Limited visibility into attacker objectives.
* Difficulty distinguishing between low-skill attackers and advanced threats.
* Lack of realistic environments to safely observe attacker behavior.
* High costs associated with commercial deception platforms.
* Limited integration between threat intelligence, attacker profiling, and deception technologies.

As a result, organizations often remain reactive instead of proactive.

---

## Our Solution: ShadowMesh

ShadowMesh is an AI-powered cyber deception and threat intelligence platform that creates realistic, adaptive enterprise environments designed to attract, engage, and analyze attackers.

Instead of immediately blocking attackers, ShadowMesh safely redirects them into a controlled deception environment where their actions can be observed, profiled, and converted into actionable intelligence.

---

## How ShadowMesh Helps

### Attacker Profiling

ShadowMesh automatically analyzes attacker behavior and generates:

* Skill level assessment
* Attack objectives
* Tool identification
* Confidence scores
* MITRE ATT&CK mappings

This helps security teams understand the nature of the threat much faster.

---

### Adaptive Deception

The platform dynamically creates realistic enterprise assets such as:

* Web servers
* Databases
* API gateways
* Active Directory environments
* File servers
* Cloud resources

The environment adapts based on attacker behavior, increasing engagement and intelligence collection.

---

### Threat Intelligence Generation

Every attacker interaction is transformed into structured intelligence including:

* MITRE ATT&CK techniques
* Threat actor profiles
* Behavioral patterns
* Cloud activity
* Credential theft attempts
* Lateral movement indicators

This intelligence can be exported and shared with security teams.

---

### Early Threat Detection

ShadowMesh detects:

* Port scanning
* Service enumeration
* Credential harvesting
* Active Directory reconnaissance
* Cloud credential abuse
* Canary token triggers

allowing organizations to identify malicious activity before real assets are targeted.

---

## Who Can Use ShadowMesh?

### Security Operations Centers (SOC)

Monitor attacker behavior in real time and reduce investigation time.

### Enterprises

Deploy deception networks to identify intrusions before attackers reach critical systems.

### Government Organizations

Collect intelligence on advanced persistent threats (APTs) and suspicious activity.

### Educational Institutions

Provide realistic cybersecurity training environments.

### Research Teams

Study attacker behavior, tactics, techniques, and procedures (TTPs).

### Managed Security Service Providers (MSSPs)

Offer deception-based monitoring and threat intelligence services to clients.

---

## Benefits

* Improves threat visibility
* Reduces analyst workload
* Increases attacker engagement time
* Provides actionable intelligence
* Enhances incident response
* Supports proactive defense strategies
* Integrates with existing security tools
* Generates industry-standard threat intelligence reports

---

## Impact

ShadowMesh transforms cybersecurity from a reactive process into an intelligence-driven defense strategy.

Instead of simply detecting attacks, organizations gain the ability to understand attackers, learn from their behavior, and continuously improve their security posture.

**Challenges we ran into**

# Challenges We Ran Into

Building ShadowMesh involved integrating multiple technologies including AI profiling, deception infrastructure, container orchestration, threat intelligence, real-time visualization, and cloud deception. Throughout development, we encountered several technical challenges that required careful debugging and architectural improvements.

---

## 1. Dynamic Topology Mutation Breaking Existing Sessions

### Problem

One of the core features of ShadowMesh is the ability to mutate the deception network topology to confuse attackers. Initially, when the topology mutated, all existing nodes were replaced with completely new ones.

This caused:

* Existing attacker sessions to break unexpectedly
* Loss of context for ongoing interactions
* Sudden disappearance of previously discovered systems

### Solution

We redesigned the mutation engine to retain a portion of existing nodes while introducing new ones.

This allowed:

* Existing attacker interactions to continue naturally
* Network evolution without disrupting engagement
* More realistic enterprise behavior

---

## 2. MITRE ATT&CK Mapping Consistency

### Problem

Different detection modules occasionally mapped the same attacker behavior to different MITRE ATT&CK techniques.

This created:

* Inconsistent threat reports
* Duplicate intelligence records
* Incorrect dashboard analytics

### Solution

We centralized MITRE ATT&CK mappings into a unified mapping layer and validated all detection outputs against a single source of truth.

---

## 3. Container Management and Resource Isolation

### Problem

The deception environment relies heavily on Docker containers representing fake services.

During testing we observed:

* Orphaned containers after crashes
* Resource consumption increasing over time
* Inconsistent cleanup behavior

### Solution

We implemented a dedicated container management layer with:

* Automatic cleanup routines
* Resource limits
* Container tracking
* Graceful failure handling

This significantly improved system stability.

---

## 4. Realistic Deception vs Performance

### Problem

Making deception environments realistic often required generating:

* Large numbers of users
* Fake documents
* Active Directory objects
* Credentials
* Cloud artifacts

However, generating everything dynamically increased startup time.

### Solution

We optimized generation logic by:

* Caching reusable datasets
* Pre-generating common artifacts
* Using lightweight templates
* Loading only required assets when needed

This improved responsiveness without sacrificing realism.

---

## 5. AI Profiling Reliability

### Problem

LLM-generated attacker profiles occasionally returned inconsistent formats or unexpected values.

This caused:

* Parsing failures
* Invalid confidence scores
* Incorrect attacker classifications

### Solution

We added:

* Strict schema validation
* Confidence score normalization
* Input sanitization
* Fallback heuristic profiling

This ensured stable behavior even when AI responses were imperfect.

---

## 6. Detecting Attacker Intent Accurately

### Problem

Simply recording attacker actions did not provide enough information to understand attacker objectives.

For example:

* Port scans alone reveal little intent.
* Credential access may indicate privilege escalation or data theft.

### Solution

We developed behavioral correlation mechanisms that combine:

* MITRE ATT&CK techniques
* Credential access events
* Cloud activity
* Active Directory enumeration
* Canary triggers

This produces much more accurate attacker profiling.

---

## 7. Integrating Multiple Components

### Problem

ShadowMesh contains many interconnected subsystems:

* FastAPI backend
* React frontend
* Neo4j
* Redis
* Docker containers
* Socket.IO
* AI services
* Alerting systems

A failure in one component could impact the entire platform.

### Solution

We introduced:

* Health checks
* Retry mechanisms
* Graceful degradation
* Smoke testing
* Integration testing

This improved reliability and made debugging significantly easier.

---

## 8. Making the Platform Demo-Friendly

### Problem

Hackathon judges and evaluators have limited time. Complex setup procedures would reduce usability and demonstration quality.

### Solution

We focused on:

* Automated deployment
* One-command startup
* Real-time dashboards
* Visual attack graphs
* Automated simulations

This made the platform much easier to showcase and evaluate.

---

## Key Takeaway

The biggest challenge was not building individual features, but making many advanced cybersecurity components work together as a cohesive system.

By combining deception technology, artificial intelligence, threat intelligence, container orchestration, and real-time analytics into a single platform, we created a system that not only detects attackers but also learns from them and transforms their behavior into actionable intelligence.

**Open Innovation**

## Open Innovation

ShadowMesh falls under the **Open Innovation** track because it addresses a broad and critical cybersecurity challenge faced by organizations across multiple industries. Rather than solving a niche problem, ShadowMesh introduces an AI-powered cyber deception and threat intelligence platform that can be adapted for enterprises, government agencies, educational institutions, research organizations, and security operations centers.

The project combines deception technology, attacker profiling, threat intelligence, cloud deception, Active Directory deception, and real-time analytics to help defenders better understand attacker behavior and respond proactively. Its flexible architecture and wide applicability make it a strong fit for the Open Innovation track.

Team **ASTRAX** -- [Subhranil Mondal](https://github.com/extremecoder-rgb), [Soumadeep Shee](https://github.com/souma9830), [subha Prasana Parida](https://github.com/debarpanjasu07-hub), [Dhrubojyoti Chakraborty](https://github.com/Dhrubojyot)

`2026-05-31`

---

### SilverHands-  A senior-first digital platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/silverhands-a-seniorfirst-digital-livelihood-platform-turning-lifelong-skills-into-dignified-safe-alsupported-income-012a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MohamedSuhailN/silver-hands) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ewulp27yObA?si=UI4A1LvBP3KcERhg) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Every Skill Deserves An Income

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Millions of senior citizens and homemakers possess valuable skills such as cooking, tutoring, tailoring, handicrafts and traditional arts, but these skills often remain economically untapped.

Existing employment platforms are mainly designed for conventional jobs and younger professionals, making them difficult to use for flexible, home-based or part-time livelihoods.

SilverHands solves this by creating an AI-powered livelihood ecosystem where seniors and homemakers can turn their experience into trusted digital profiles, discover opportunities, connect with customers and build sustainable income.

Its voice-first AI assistant reduces the need for complicated forms and navigation, making digital participation more accessible for older users.

**Challenges we ran into**

One of our biggest challenges was making the AI genuinely useful rather than building another chatbot. We had to design a system where AI understands natural language, collects missing information, asks for confirmation and then performs real backend actions without fabricating data.

We also faced integration challenges between the AI layer, Django APIs and the frontend, particularly around API failures, environment configuration and reliable AI responses.

Voice interaction was another challenge because browser speech recognition can stop unexpectedly or behave differently across browsers. We addressed this with explicit listening states, error handling and text fallback.

Finally, we had to ensure that AI-generated actions remain secure: the AI can suggest an action, but authentication, authorization, validation and database updates remain controlled by the backend.

Team **Black Clovers** -- Manikandan S, [Yugandran D](https://github.com/YugandranD), Lekasvarr S, Nithish M, MOHAMED SUHAIL

`2026-09-02`

---

### Anti-Narcos Graph Intel
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/antinarcos-graph-intel-a371) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Kamal-Kumar123/Anti-Narcos-Graph-Intel) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://anti-narcos-graph-intel-fh2j-dmb8siz6k.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tEvVKIYqxZY) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Ask the narcotics graph.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square)

**Challenges we ran into**

**Building a Graph-RAG pipeline on free-tier cloud was harder than we expected. These were the main hurdles:**

**Challenge 1 - Wrong evidence from vector search**

When we first asked questions like “Dharavi,” the system did return an answer - but the sources were pulling from unrelated Mumbai cases. Vector search was picking the nearest chunks by similarity, even when they weren’t about the place in the question. That showed us embeddings alone weren’t enough. We added query-focus filtering, entity matching, and keyword recall. After that, answers actually came from reporting that matched the question.


**Challenge 2 - When to answer from the graph vs. when to crawl the web**

The core idea was: if the graph doesn’t have enough evidence, the system should go fetch new data from the public web. The hard part was defining “enough.” Without a clear rule, it would either crawl on every query or almost never. We set a threshold: we need a minimum number of high-confidence chunks before answering from the graph alone. If that bar isn’t met, the OSINT pipeline runs - 
search, crawl, ingest, then ask again. That made the system genuinely adaptive instead of crawling blindly every time.

![image](https://assets.devfolio.co/content/0ce77a60d06349238539b64b45b75c73/66d1418a-d44b-4f32-ac0d-4a6fa38b4dc2.png)

**Challenge 3 - The OSINT pipeline kept breaking mid-flow**

One question triggers a long chain: web search, page crawl, article cleaning, entity extraction, saving to Neo4j, generating embeddings, then answering again. If any step failed, it looked like the app had frozen. We added background jobs, step-by-step progress in the UI, and a crawler fallback - if Scrapy fails, httpx takes over. Users can now see whether the system is searching, crawling, or updating the graph.

**Challenge 4 - LLM extraction wasn’t trustworthy at first**

The graph depends on extracting people, drugs, locations, and cases from articles. Smaller models sometimes echoed the JSON schema back instead of filling it in, or left entities blank. Irrelevant news was getting ingested too. We moved to a stronger model and added a lexicon check first - if an article has no narcotics signal, don’t extract it at all. That kept the graph cleaner and made answers much more useful.

**Challenge 5 - Split-host deploy looked fine until the browser hit the API**

The frontend is on Vercel and the API is on Render, so a green GitHub deploy still meant a broken product. Every Vercel preview minted a new *.vercel.app origin, and Render CORS rejected it — localhost worked, live previews did not. OTP over Gmail then died because Render cannot open SMTP on port 587; Resend over HTTPS still would not mail judges without a verified domain. We allowed Vercel preview origins by regex, dropped JWT/OTP rather than demo a login that could not verify anyone, and fixed a TypeScript HeadingLevel mismatch that was failing the Vercel build even when the API was healthy. After that, the console and the graph actually talked to each other in production.

![image](https://assets.devfolio.co/content/0ce77a60d06349238539b64b45b75c73/0e85b838-8e5d-4149-b648-a05981bb0ac4.png)

**The problem it solves**

**Narcotics intelligence is scattered and hard to connect.**

Seizures, arrests, and trafficking reports sit in separate news articles, press notes, and portals. Keyword search finds documents, not relationships - who is linked to whom, which drugs move through which routes, and which cases share the same people or locations.

Anti-Narcos Graph Intel turns public reporting into a Neo4j knowledge graph and lets analysts ask questions in plain language. The system:

Retrieves evidence with vector search + graph traversal (not guesswork)
Shows sources, entities, and network links for every answer
Auto-expands when the graph is thin - it searches the web, crawls relevant pages, extracts entities, and re-answers from updated data
Surfaces risk patterns (repeat offenders, hub locations, cross-case links) as analyst aids - not verdicts
Who it helps: law-enforcement analysts, researchers, and investigators who need faster situational awareness without manually reading hundreds of articles.

Impact: hours of manual link analysis -> one question, cited answer, and an explorable network graph.
[](url)

![image](https://assets.devfolio.co/content/0ce77a60d06349238539b64b45b75c73/4dd629fd-10a2-4be2-a79a-74d09a393e36.png)

**Anti Narcotics**

**Narco-Graph Intel** is an anti-narcotics graph, not a generic news bot: it turns public NDPS-style reporting into Neo4j nodes for people, drugs, places, agencies, cases and seizures, then answers questions from those links. A lexicon gate (**heroin, MD, cocaine, tramadol, NCB, DRI, ANC, BSF**) drops anything without a narcotics signal before extraction, so the graph stays clean. Cross-article MERGE is what surfaces the actual intel — the same accused in Mumbai and Pune, a city tied to more than one drug type — and six Cypher rules flag multi-city actors, co-accused pairs, repeat names, ≥1 kg seizures and cross-substance networks for a human analyst, never as a finding of guilt. If evidence is thin, it crawls public sources (NCB/PIB/national press) and writes them back; it does not touch classified systems.

![image](https://assets.devfolio.co/content/0ce77a60d06349238539b64b45b75c73/542c1fd6-c5ef-40fc-aa2b-ccfe89bf01a0.png)

![image](https://assets.devfolio.co/content/0ce77a60d06349238539b64b45b75c73/92e00513-e522-452d-bda2-7e5758fc7a66.png)

Team **The Conflicters** -- Deepika Bhagat, Abhishek Kumar, Ikramul Hasan, Waseem Akram, [Kamal Kumar](https://github.com/Kamal-Kumar123)

`2026-08-16`

---

### Levenshtein-go
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/levenshteingo-2ca2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MuhammadUmar7195/levenshtein-go) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://muhammadumar7195.github.io/levenshtein-go) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1215231627?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> 100% verified Go port of fastest-levenshtein

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![HTML5](https://img.shields.io/badge/HTML5-333333?style=flat-square) ![Markdown](https://img.shields.io/badge/Markdown-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

# Levenshtein Distance

Levenshtein distance is simply the number of edits (**insertions, deletions, or substitutions**) needed to turn one word into another.

For example, turning **"fast"** into **"faster"** takes **two edits**.

In daily life, this is the exact math behind features we use every day:

- Autocorrect on your phone
- Search engine **"Did you mean...?"** suggestions
- Spam filtering
- DNA sequence matching

## The Problem

The problem is that the traditional way of calculating this distance is incredibly slow and eats up a lot of memory, especially when a server has to check thousands of words per second.

## The Solution

This project solves that bottleneck for the Go ecosystem.

I took the fastest known algorithm from the JavaScript world and ported it into Go.

By packing the matrix calculations into **64-bit integers** and removing **all memory allocations**, developers can now build high-performance search features, spell checkers, and fuzzy-matching tools in Go without crashing their servers or wasting CPU power.

**Challenges we ran into**

# Challenges Faced

The biggest hurdle I faced was forcing Go to behave exactly like JavaScript's V8 engine when doing bitwise math.

JavaScript is very forgiving if you try to bit-shift a number too far; it automatically wraps it around a **31-bit mask**.

Go is strict; if you shift out of bounds, it either panics or zeros out the number.

This completely broke my algorithm for strings longer than **32 characters**.

I had to manually trace the math and add explicit bit masks (`1 << uint(k&31)`) in Go to perfectly match the original logic.

## The Most Surprising Challenge

The most surprising challenge, however, came during testing.

I built a differential fuzzer to test my code directly against the original Node.js code across **29,000 randomised strings**.

While doing this, I actually discovered a bug in the original repository!

The original code calculates emoji distances incorrectly because it blindly counts UTF-16 surrogate pairs rather than actual characters.

Because my goal was **"100% behavioural parity,"** I had to make a tough design decision:

> I chose to optimise my Go port for maximum speed using a byte-level table, and documented the original emoji bug honestly in my architecture decisions rather than intentionally writing bad math just to match it.

Umar Asif

`2026-08-03`

---

### Edict
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edict-9c96) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/furyfist/edict) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://edict-iota.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a7SGo1K1HKQ) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Authority infrastructure for autonomous agents.

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Companies pay for a lot of software every month. Most subscriptions renew automatically, and nobody has time to check every price increase or every unused seat. Over time, money slowly gets wasted.

Giving this job to an AI agent sounds like a good idea, until you ask one question: what happens if the AI gets fooled?

Imagine a vendor sends an email saying, "Your plan changed. Please pay $48,000 today." If the AI is the only thing deciding whether to pay or not, one convincing email is enough to lose money.

Edict solves the problem underneath that.

The question is not, "Can an AI renew my subscriptions?"

The real question is, "Can I give an AI permission to spend money with a hard limit, watch everything it does, stop it anytime, and prove it never went beyond that limit?"

A human writes the spending rules in plain English. Those rules become real payment limits enforced by the payment network, not by our code. The AI only suggests what to do. A separate policy engine checks every action against the rules before any payment happens. Even if the AI gets fooled, the payment cannot go through.

**Challenges we ran into**

**1. Proving nothing was hidden, not just that nothing changed**

This was the biggest challenge.

At first, I thought an append-only ledger solved everything. Every record was signed and linked to the previous one, so nobody could edit history.

But then I realized something.

That only proves nobody changed a record after it was written. It does not prove that every record was written in the first place.

Someone could charge the card and simply skip writing the ledger entry. The ledger would still look completely clean because there is nothing missing from its point of view.

The fix was two-sided reconciliation.

Instead of only checking that every ledger entry had a matching payment, I also checked that every real payment had a matching ledger entry.

That second check is what catches money that quietly disappears.

**2. Fake domains broke real passkey logins**

This bug wasted more time than I expected.

I used placeholder domains like figma.example while setting up vendor payments.

That is completely normal in documentation, but the real payment network refused to start the passkey flow because those domains do not actually exist.

The error looked like a broken passkey, so I spent time checking browsers and devices instead of the real problem.

As soon as I replaced the placeholder domains with the vendors' real domains, everything worked.

It reminded me that third-party services often validate things you do not expect, so it is better to test them with realistic data as early as possible.

**3. The charge history API wasn't there**

I planned the reconciliation feature around fetching past charges from the payment network.

I tried several different API endpoints.

Every one of them returned a 404.

Instead of pretending everything was working, I made the app honest.

If the system cannot fetch the payment history, it tells the user directly instead of showing a false "everything looks good."

A verification system should never hide uncertainty. If it cannot verify something, it should simply say, "I couldn't verify this."

**Best Visa Intelligent Commerce Implementation**

The spending limit is not enforced by our code. It lives inside the payment credential itself.

If the AI gets fooled and tries to make a payment above the limit, the payment network rejects it directly, just like your card gets declined at checkout.

Increasing the limit always needs a real passkey approval from the owner. Nothing inside our application can increase it on its own.

Before a policy becomes active, we replay it against real payment history so the user can see exactly what it would have approved or blocked before they accept it.

**Most Startup-Ready Product**

This project is our answer to one simple question: how do you let an AI agent do real work without letting it go rogue?

Every safety feature in the project has a real attack trying to break it. We do not just say the system is safe. We try to break it on camera.

And nothing depends on "trust us."

Every action, every refusal, and every verification is signed and can be checked independently, even if our application is completely turned off.

**OpenAI**

An OpenAI model suggests what to do, like renewing a subscription or cancelling one. It also turns plain English spending rules into structured policies.

But it never makes the final decision.

It only makes suggestions. A separate policy engine checks every action, and that engine has no way to call the payment system directly.

We also use another OpenAI model as the attacker. It tries to trick the assistant into approving payments it should never approve.

Every attack and every result is recorded and signed, so safety is not just something we claim. It is something we can measure and show.

**Agentic Commerce Hackathon**

Prava is the only part of the system that can actually move money. Everything else has to go through it.

We also use Prava's transaction history as a second, independent source of truth.

In the demo, we purposely send a payment without writing it to our own ledger. Then we compare our records with Prava's records and immediately find the missing transaction.

Prava helps prove that our own application should never be trusted blindly, and that is exactly the point.

[furyfist .](https://github.com/furyfist)

`2026-08-03`

---

### GitHub oracle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stormaboba-ebbe) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://github-oracle.space-z.ai/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Turn your GitHub profile into magic cards!

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GraphQL](https://img.shields.io/badge/GraphQL-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

**1. GitHub API rate limits on a shared infrastructure**
The single hardest constraint. The public GitHub API allows only 60 requests per hour per IP without authentication — and the hackathon's shared preview environment meant a single IP was shared across all visitors and judges. The first end-to-end test exhausted the quota instantly, returning 429 before any card could render.

How I solved it elegantly — a four-layer defense:

Tiered in-memory caching. Profiles/repos cache for 30 min, commit events
for 3 min, and fully-generated destiny cards for 1 hour. Repeat reads of the same user drop from ~5s to 46ms, bypassing GitHub entirely.
GraphQL consolidation. When a token is available, I fetch profile + 100
repos + primary languages in one GraphQL query instead of two REST calls — cutting quota usage by a third. Graceful degradation. The commit-events fetch is skipped entirely when the remaining quota drops below 3, so the next visitor always gets a card (just without commit-based achievements). The events API is also wrapped in a soft-fail: any error returns an empty analysis instead of crashing the pipeline.
A guided rate-limit dialog. When the limit is truly hit, the UI shows a
themed modal — "The Oracle's Sight Is Dimmed" — with a live countdown to reset and two paths: Log in with GitHub (OAuth, unlocks a personal 5,000/hour quota) or Wait & retry. After login, the pending generation auto-retries. This turned a hard failure into a polished, on-brand moment.

**2. Getting structured JSON out of an LLM — reliably**
The oracle needs the AI to return strict JSON (description, abilities,
fortune, prediction). In practice the model would sometimes wrap output in markdown fences, add preamble text, or omit a field.

The fix: a defensive extractJson() that strips code fences, isolates the first { … } block, validates each field's type, and — on any failure — falls back to a deterministic lore generator that branches on commit cadence (e.g. high momentum → "a roaring river… great works shall flow"). The card always renders, even if the AI oracle goes silent.

**3. Commit-pattern analysis from a noisy events API**
GitHub's public events endpoint returns up to 100 recent events of mixed types (push, star, fork, comment…), with commit counts nested inside PushEvent payloads. Deriving meaningful signals — commits/week, peak hour, weekend ratio — required careful aggregation and language attribution via a repo-name → language map built from the repos fetch. Timezone handling was especially fiddly: getHours() uses the server's locale, so I standardized on UTC-normalized parsing and documented the assumption.

**4. 3D card physics without a 3D library**
I wanted a premium, mouse-tilt-and-flip card using only Framer Motion — no Three.js weight. The challenges: keeping the glare overlay's useTransform at the top level of the component (calling hooks inside JSX props breaks React's rules-of-hooks lint), managing backface-visibility across the flip, and ensuring the inner flip layer's rotateY didn't fight the outer tilt's rotateX/rotateY. Solved with nested preserve-3d containers and a single spring-driven motion-value pipeline.

**5. Organizations aren't users**
The GraphQL user(login:) query returns null for organization accounts, which would falsely report "user not found." I added a REST fallback — if GraphQL returns no user, the code transparently retries via the REST /users/{login} endpoint before declaring a 404, so orgs like companies still get a reading.

**6. Keeping 60+ animated background elements performant**
The living background combines ~50 twinkling stars, breathing glow orbs, drifting runes, a hue-shifting nebula, and a Ken Burns image zoom. To stay smooth I used only GPU-composited properties (transform, opacity, filter), deterministic pseudo-random positions (so React doesn't thrash on re-render), and a prefers-reduced motion media query that disables every animation for accessibility — verified at a steady 60fps with zero jank.

**The problem it solves**

**The Cold Data Dilemma in Developer Profiles**
Traditional developer profiles — resumes, portfolios, and raw GitHub statistics — are highly transactional and sterile. A row of repositories, a simple star counter, and a list of languages tell us *what* someone built, but never *who* they are as a builder. Existing visualizers (like contribution graphs or stat cards) are informative but lifeless, flat, and hard to distinguish from one another. This sterile approach to developer identity makes onboarding, community-building, and peer recognition feel impersonal.

**Humanizing Technical Footprints**
**GitHub Oracle** reframes a developer’s public footprint into a living, personalized mythology. By entering a username, the application reads their "aura" — analyzing repositories, languages, stars, followers, account age, and commit rhythms. It then conjures a unique 3D destiny card stamped with:
*   A deterministic developer archetype.
*   An AI-authored character lore and signature abilities.
*   Unlockable community achievements.
*   A predictive analysis of future coding habits.

By transforming a spreadsheet of metrics into an interactive narrative, GitHub Oracle demonstrates that developer-tooling UX can be emotional, aesthetic, and playful without sacrificing real engineering depth.

Anton Denisov

`2026-06-26`

---

### GitPlus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gitplus-8c3d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arpan7sarkar/GitPlus.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1mw7O_v6DSS4jGTYYRb8kGoqIxlwP6Zvm?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=5RGONrTmCv4&feature=youtu.be) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> One stop platform for managing codebases

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Github Actions](https://img.shields.io/badge/Github%20Actions-333333?style=flat-square) ![CI/CD](https://img.shields.io/badge/CI/CD-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

### 🧠 Understanding a codebase shouldn't take weeks.

Every developer has faced the frustration of staring at a massive, unfamiliar repository — whether it's a new hire joining a team, an open-source contributor navigating a 100k-line project, or a security auditor hunting for vulnerabilities buried across hundreds of files. **The traditional approach is painfully manual**: read file after file, trace imports, grep for function names, and hope you don't miss anything critical.

**GitPlus eliminates this friction entirely.**

---

### What People Can Use It For

**🔍 Instant Codebase Understanding (For Developers & New Hires)**
- Paste any GitHub repository URL and get an **AI-generated architectural overview** in seconds — framework detection, key files, complexity analysis, and a narrative summary of what the project does.
- Ask natural-language questions like *"How does authentication work?"* or *"Where is the payment logic?"* and receive **streaming AI answers with exact file and line-number citations**, powered by hybrid vector search through **Actian Vector AI DB**.

**🛡️ Automated Security Auditing (For DevSecOps & Tech Leads)**
- Run a **12-category security vulnerability scan** on any repository — detecting hardcoded API keys, SQL injection risks, insecure CORS configurations, weak cryptography, broken access controls, and more.
- Get actionable findings **before code hits production**, replacing hours of manual security review with a single click.

**📐 Architecture & Documentation Generation (For Architects & Team Leads)**
- Auto-generate a **10-section system design document** complete with data flow descriptions, component breakdowns, and architectural patterns — solving the universal problem of outdated or non-existent documentation.
- Generate **developer onboarding guides** that new team members can follow from day one, cutting onboarding time from weeks to hours.

**🕸️ Interactive Dependency Visualization (For Debugging & Refactoring)**
- Explore a **2D force-directed dependency graph** that maps every module relationship in the codebase. Drag nodes, hover over imports, and instantly understand how files connect — making refactoring and circular dependency detection visual and intuitive.

**🐙 Native GitHub Workflow Integration (For Engineering Teams)**
- Browse **GitHub Issues**, **Pull Request diffs**, and **commit timelines** directly inside GitPlus without context-switching between tools.
- **VexReview** (our GitHub Action component) automatically reviews every pull request with AI-powered code analysis, giving teams production-grade reviews on every merge.

**🤝 Collaboration & Sharing (For Teams & Open Source)**
- Generate **shareable permalink URLs** for any AI chat session or security audit — enabling seamless knowledge sharing across distributed teams.
- Launch any indexed repository directly in a **StackBlitz Cloud IDE** with one click for instant hands-on exploration.

---

### How It Makes Existing Tasks Easier & Safer

| Traditional Approach | With GitPlus |
|:---|:---|
| Spend **2-3 weeks** reading code to understand a new project | Get a complete architectural overview in **30 seconds** |
| Manually grep through files to find relevant code | **Hybrid RAG search** (Actian Vector AI + BM25) retrieves the exact code chunks you need |
| Security reviews are manual checklists prone to human error | **Automated 12-category scans** catch vulnerabilities humans miss |
| Architecture docs are outdated the moment they're written | **AI-generated system design docs** reflect the actual current codebase |
| Context-switch between GitHub, IDE, docs, and chat tools | **Unified workspace** with Issues, PRs, Commits, Chat, and Cloud IDE in one place |
| LLMs hallucinate when given large codebases | **Reciprocal Rank Fusion (RRF)** ensures only the most relevant code chunks reach the LLM — eliminating hallucinations |

---

> **In short:** GitPlus turns any GitHub repository from an opaque wall of code into an interactive, searchable, audited, and visualized AI workspace — making codebases **understandable in minutes, not months**.

**Challenges we ran into**

Since this was our first time working with Actian Vector, there was a significant learning curve. We first had to understand the fundamentals of chunking, embeddings, and how vector databases store and retrieve information. After setting up Actian Vector in Docker, we encountered hardware limitations, as one of our teammates' laptops couldn't handle the workload, so we distributed the development across two laptops.

One of the biggest challenges was optimizing our chunking strategy. Initially, we used a fixed chunk size of around 40 characters, but the retrieval quality was poor. We experimented with three to four different chunking algorithms and strategies before finding an approach that significantly improved embedding quality and search accuracy.

We also implemented a Retrieval-Augmented Generation (RAG) pipeline so the AI could understand and answer questions about the entire codebase. Since it was our first time building a RAG system, integrating it was challenging. We used Actian's AI SDK with LangChain support to create the complete pipeline, and after several iterations, we successfully got it working.

Fetching repositories from GitHub was relatively straightforward. However, integrating GitHub, the vector database, embeddings, chunking, and the RAG pipeline into one complete system required considerable debugging and experimentation. Despite these challenges, we were able to successfully build and integrate the entire solution.

**Accio Relevance - Build with Actian VectorAI Database**

github : https://github.com/arpan7sarkar/GitPlus
video : https://drive.google.com/drive/u/1/folders/1mw7O_v6DSS4jGTYYRb8kGoqIxlwP6Zvm

## What we built

GitPlus turns a GitHub repository into an AI that understands its own codebase. Every user query retrieves fresh, line-accurate context instead of relying on a one-time summary. The same retrieval pipeline powers onboarding guides, security audits, architecture documentation, and AI pull-request reviews through **VexReview**.

This is only possible because of **Actian VectorAI Database**, which serves as the foundation of our semantic retrieval system.

---

## Why Actian

We chose Actian because it solved the problems that mattered during development:

* **Quick self-hosted setup** with Docker for fast local development.
* **Actian Console** for inspecting collections, payloads, and indexing while debugging.
* **Powerful payload filtering**, allowing multiple code granularities to live in a single collection.
* **Flexible gRPC/REST APIs** supporting dense search, batch upserts, filtered queries, and deletes.

---

## Hierarchical Semantic Search

Instead of storing one flat list of code chunks, GitPlus builds a **4-level hierarchy**:

| Tier   | Content                                            |
| ------ | -------------------------------------------------- |
| Repo   | Entire repository summary                          |
| Module | Directory-level summary                            |
| File   | File summary + raw file content                    |
| Symbol | Functions, classes, and methods (AST-based chunks) |

All four levels are stored inside **one Actian collection** (`gitplus_nodes_v3`) with a filterable `level` field. Broad questions search higher-level summaries, while specific questions search symbol-level embeddings—all without maintaining separate indexes.

---

## Hybrid Retrieval

Every query performs two searches simultaneously:

1. **Actian dense vector search** for semantic similarity.
2. **Postgres BM25 keyword search** for exact matches.

The results are merged using **Reciprocal Rank Fusion (RRF)** and refined with **Maximal Marginal Relevance (MMR)** to produce diverse, highly relevant context. This retrieval runs **fresh on every chat turn**.

---

## Real-world Integration

Building against the actual Actian server uncovered important implementation details:

* We generate deterministic UUIDs for vector IDs while keeping our own repository IDs in the payload, making re-indexing idempotent.
* We build queries using Actian's typed `Field` and `Filter` objects, enabling reliable filtered search.

These primitives gave us precise control over indexing and retrieval rather than hiding the database behind a simplified API.

---

## Impact

Actian enabled us to:

* Store the entire hierarchy in **one collection** instead of multiple indexes.
* Build efficient hybrid search with semantic + keyword retrieval.
* Safely re-index repositories using deterministic IDs and filtered deletes.
* Inspect and debug the full ingestion pipeline through the Console.
* Focus engineering effort on AST-aware chunking, hierarchy, and retrieval quality instead of vector database infrastructure.

**Best Use of Gemini API**

GitPlus & VexReviewer leverage Google Gemini (Gemini 2.0 Flash) as the core AI engine powering deep codebase intelligence and autonomous PR code reviews.

Rather than treating code as raw text, our architecture parses repositories into a 4-tier AST hierarchy (Symbol → Block → File → Directory) using WASM Tree-Sitter. We feed these structured code nodes along with dense/sparse vector retrieval context from Actian VectorAI directly into Gemini 2.0 Flash.

Key Gemini Integrations:

Codebase Q&A & Architecture Synthesis: Gemini synthesizes multi-file code context to answer complex questions, generate system architecture docs, and perform onboarding audits with line-accurate citations.
VexReviewer (Automated PR Reviews): Gemini analyzes raw git diffs against indexed repository context to perform automated code reviews, flag security vulnerabilities, and suggest inline optimizations before merging.
Production Resilience: Built a primary-fallback pipeline (llm.ts) prioritizing Gemini 2.0 Flash for low-latency inference and high-context code reasoning.
By combining structural AST parsing with Gemini's high-speed long-context window, we turn static GitHub repositories into an interactive, self-explaining codebase graph.

**Open Innovation**

GitPlus falls under the **Open Innovation** track because it doesn't fit into any of the domain-specific categories provided in the hackathon. Instead of solving a problem in healthcare, finance, education, or another specific industry, GitPlus is a **developer productivity platform** that helps software engineers understand, analyze, secure, and collaborate on codebases more efficiently.

By combining AI, semantic code search, automated security analysis, documentation generation, and GitHub workflow integration, GitPlus addresses a universal challenge faced by development teams across every industry. Its impact is cross-domain, making software development faster, safer, and more accessible regardless of the application being built. That broad applicability is exactly why GitPlus is best suited for the **Open Innovation** track.

Team **WeDev** -- [Souvik Kundu](https://github.com/Souvik-kundu-off), [BARSHAN MAJUMDAR](https://github.com/Barshan-Majumdar), [Sagar Bhadra](http://github.com/SagarBhadra01), [Arpan Sarkar](https://github.com/arpan7sarkar)

`2026-07-26`

---

### PhishXMule
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/phishxmule-c1ec) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajnil9/PhishXMule) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1jTSsa_eYeK0C5GiEffOCjFHWw9wt_6bl) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/rSeBShMCFTE) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> ML Cybersecurity Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Support Vector Machine (SVM)](https://img.shields.io/badge/Support%20Vector%20Machine%20(SVM)-333333?style=flat-square)

**The problem it solves**

Phishing and fraud attacks have splintered across channels — a scam might arrive as a malicious URL, a phishing email, an SMS smishing text, a screenshot shared in a chat app, or show up as a synthetic identity mule account during bank onboarding. Most detection tools only cover one of these surfaces, forcing security teams to stitch together disconnected point solutions.

PhishXMule solves this by unifying detection across all five attack surfaces in a single platform:

• Who it's for: Banks and fintechs (fraud & onboarding risk), SOC/security teams (phishing triage), and everyday users (screenshot/link/SMS checks).

• How it helps: Each module runs a dedicated, purpose-built ML model tuned to its channel — a lightweight LightGBM classifier for URLs, calibrated NLP models for emails/SMS, a stacking ensemble with SHAP explainability for fraud onboarding, and a hybrid vision + OCR + QR pipeline for screenshots — so detection stays fast, accurate, and explainable instead of relying on one generic model for everything.

**Challenges we ran into**

•Class imbalance in fraud data: The Bank Account Fraud dataset has only ~1.1% fraud cases. We addressed this with a custom Focal Loss in LightGBM, scale_pos_weight tuning in XGBoost, and evaluated on Recall @ 5% FPR rather than raw accuracy, which is misleading on imbalanced data.

•False positives on legitimate emails/screenshots: Early versions over-flagged benign urgency language and generic login pages. We fixed this with the 3-layer Email safeguard pipeline (link scanning → urgency detection → false-positive overlay) and the "Unknown" vision guard (base_risk = 0.5) in ImageX to avoid classifying uncertain images as 100% phishing.

• PyTorch/Hugging Face integration bugs: Encountered KeyError crashes from mismatched label2id/id2label types, and DataLoader 5D tensor errors caused by return_tensors="pt" in the transform pipeline — both fixed during refactoring (see ImageX's refactoring history).

• Model size vs. accuracy trade-offs: Keeping the URL classifier lightweight (~2.8 MB) while maintaining 84%+ generalization accuracy required careful feature selection (33 lexical/structural features) instead of a larger deep model.

• Explainability requirements: Fraud decisions need to be auditable for AML compliance, so we integrated SHAP TreeExplainer into MuleX to generate human-readable Red Flag / Green Flag justifications alongside every risk score.

**Open Innovation**

• Cross-Paradigm AI Orchestration: Pioneering a unified threat-detection engine that seamlessly integrates three distinct machine learning disciplines—Natural Language Processing (text), Computer Vision (images), and Tabular ML (financial data)—into a single, cohesive architecture.

• Breaking Traditional Security Silos: Challenging the industry standard of heavily segregated, multi-vendor point solutions by proving that disparate AI modalities can be converged to eliminate blind spots and reduce operational friction.

• Full Kill-Chain Visibility: Shifting from isolated attack detection to a holistic, lifecycle approach that tracks a threat from the initial semantic lure (PhishX), through the visual deception of spoofed interfaces (ImageX), down to the mathematical anomalies of money laundering (MuleX).

• Contextual Threat Synthesis: Leveraging multi-modal intelligence to understand how different vectors interact, allowing the system to accurately score complex attacks where a seemingly benign SMS and a visually manipulated login screen combine to create a critical threat.

• Extensible Defense Framework: Establishing a highly modular, open-architecture foundation that is designed to easily ingest new data streams and AI models, ensuring the platform can rapidly adapt to future, AI-generated cyber threats.

Team **Priest Kings** -- [Rajnil Saha](https://github.com/rajnil9), [Sayantan Roy](https://github.com/Sayantan176), [Bikramjit Pakhira](https://github.com/CodewithBikram2025), [Debmallar Dasgupta](https://github.com/debmallardasgupta)

`2026-07-26`

---

### AEGIS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegis-4760) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/madhesh935/AEGIS-OS) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4Y_W4AIet9I) [![Built at](https://img.shields.io/badge/Built%20at-Tech%20Genesis%20'26-0052CC?style=flat-square)](https://tech-genesis.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> One Platform. One Truth. One Mission

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem It Solves
Criminal investigations drown in data. A single case generates terabytes of CCTV footage, GPS logs, call records, autopsy reports, and witness statements — all sitting in disconnected systems with no shared context. Investigators manually correlate everything, reconstruct timelines by hand, and still miss contradictions hidden across sources. The average investigation takes 28 days to close. The human error rate is 18.7%. Justice gets delayed. Sometimes it fails entirely.
AEGIS-OS fixes this.
Forensic investigators can upload every evidence source into a single platform and immediately get a unified, AI-reasoned view of the entire case. The system automatically detects timeline contradictions between a witness statement and a CCTV timestamp, flags unusual movement patterns in GPS trails, maps relationships between suspects, locations, devices, and events, and generates a courtroom-ready narrative with full evidence citations.
Law enforcement agencies can cut investigation time from 28 days to 3.5 days and reduce human error from 18.7% to 2.1%.
Forensic analysts no longer need to manually cross-reference six isolated systems. Every insight is traceable, every anomaly is explained, and every output meets legal admissibility standards.
Smart policing units can use the real-time anomaly detection and geographic heatmaps for proactive hotspot monitoring, not just reactive case work.
In short: AEGIS-OS turns fragmented evidence into actionable intelligence, and turns investigators into better detectives.

**Challenges we ran into**

Making the Knowledge Graph Actually Reason, Not Just Store
The hardest problem was not ingesting evidence. It was making Neo4j do meaningful cross-source reasoning under time pressure. Early on, our graph queries returned correct results but missed temporal context entirely. A witness statement placing a suspect outside at 09:15 and a CCTV timestamp showing them inside at 09:12 were both in the graph but the contradiction detection engine did not surface the conflict because the edges lacked consistent temporal metadata schemas across source types.
We fixed this by enforcing a unified temporal edge model at ingestion time. Every relationship in the graph, regardless of source, carries timestamp, confidence, and source_type properties. Once that was consistent, contradiction detection became a straightforward Cypher traversal rather than application-layer logic.

NLP Pipeline Choking on Unstructured Forensic Documents
Autopsy reports, witness transcripts, and forensic lab documents do not follow a standard format. Our initial spaCy pipeline was trained on general text and consistently misclassified forensic terminology. "Blunt force trauma to the occipital region" was not being extracted as a cause-of-death entity. Time of death estimates buried in paragraph three were being ignored entirely.
We solved this by layering Hugging Face Transformers on top of spaCy for document-level understanding, using Gemini API for structured extraction with a forensic-specific prompt schema. That combination brought NLP autopsy analysis accuracy from around 61% up to 94%.

Real-Time Canvas Performance with 5+ Evidence Streams
Pushing simultaneous updates from CCTV analysis, GPS reconstruction, anomaly alerts, and graph updates to the Living Evidence Canvas over WebSockets caused the frontend to thrash. React was re-rendering the entire canvas on every incoming event.
We restructured the state management to use stream-specific slices with selective subscription, so a GPS ping update only re-renders the map component, not the full canvas. Response time on anomaly alerts dropped to 2.3 seconds average after that change.

Team **Rising Devs** -- [MADHESH B](https://github.com/madhesh935), Athina Karthikeyan, [Lokith S](https://github.com/Lokith007), SHIREEN HAIRUNEESHA

`2026-06-27`

---

### AEGIS-OS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegisos-185e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Lokith007/AEGIS-OS) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fQFb1LrYnYo) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> One Platform. One Truth. One Mission

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

The Problem It Solves
Criminal investigations drown in data. A single case generates terabytes of CCTV footage, GPS logs, call records, autopsy reports, and witness statements — all sitting in disconnected systems with no shared context. Investigators manually correlate everything, reconstruct timelines by hand, and still miss contradictions hidden across sources. The average investigation takes 28 days to close. The human error rate is 18.7%. Justice gets delayed. Sometimes it fails entirely.
AEGIS-OS fixes this.
Forensic investigators can upload every evidence source into a single platform and immediately get a unified, AI-reasoned view of the entire case. The system automatically detects timeline contradictions between a witness statement and a CCTV timestamp, flags unusual movement patterns in GPS trails, maps relationships between suspects, locations, devices, and events, and generates a courtroom-ready narrative with full evidence citations.
Law enforcement agencies can cut investigation time from 28 days to 3.5 days and reduce human error from 18.7% to 2.1%.
Forensic analysts no longer need to manually cross-reference six isolated systems. Every insight is traceable, every anomaly is explained, and every output meets legal admissibility standards.
Smart policing units can use the real-time anomaly detection and geographic heatmaps for proactive hotspot monitoring, not just reactive case work.
In short: AEGIS-OS turns fragmented evidence into actionable intelligence, and turns investigators into better detectives.

**Challenges we ran into**

Making the Knowledge Graph Actually Reason, Not Just Store
The hardest problem was not ingesting evidence. It was making Neo4j do meaningful cross-source reasoning under time pressure. Early on, our graph queries returned correct results but missed temporal context entirely. A witness statement placing a suspect outside at 09:15 and a CCTV timestamp showing them inside at 09:12 were both in the graph but the contradiction detection engine did not surface the conflict because the edges lacked consistent temporal metadata schemas across source types.
We fixed this by enforcing a unified temporal edge model at ingestion time. Every relationship in the graph, regardless of source, carries timestamp, confidence, and source_type properties. Once that was consistent, contradiction detection became a straightforward Cypher traversal rather than application-layer logic.

NLP Pipeline Choking on Unstructured Forensic Documents
Autopsy reports, witness transcripts, and forensic lab documents do not follow a standard format. Our initial spaCy pipeline was trained on general text and consistently misclassified forensic terminology. "Blunt force trauma to the occipital region" was not being extracted as a cause-of-death entity. Time of death estimates buried in paragraph three were being ignored entirely.
We solved this by layering Hugging Face Transformers on top of spaCy for document-level understanding, using Gemini API for structured extraction with a forensic-specific prompt schema. That combination brought NLP autopsy analysis accuracy from around 61% up to 94%.

Real-Time Canvas Performance with 5+ Evidence Streams
Pushing simultaneous updates from CCTV analysis, GPS reconstruction, anomaly alerts, and graph updates to the Living Evidence Canvas over WebSockets caused the frontend to thrash. React was re-rendering the entire canvas on every incoming event.
We restructured the state management to use stream-specific slices with selective subscription, so a GPS ping update only re-renders the map component, not the full canvas. Response time on anomaly alerts dropped to 2.3 seconds average after that change.

Team **Babakunnn** -- [Lokith S](https://github.com/Lokith007), [Abdullah Mustafa](https://github.com/AbdullahMustafa7), [Sanjay Kumar S](https://github.com/Sanjay-Kumar-S-GitHub)

`2026-06-14`

---

### Finder
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finder-0da7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cheerful-gaufre-1bdd5a.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Find cheapest products across platforms

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

People waste time searching across multiple sites (like Amazon and Flipkart) to find the best price and genuine reviews.

**Challenges we ran into**

Getting real-time price data (APIs are limited)
Handling fake or biased reviews
Affiliate approval and commissions
Competing with big players
Keeping data updated constantly

Team **pookie** -- [Rose Seby](https://github.com/rosesebyk)

`2026-04-28`

---

### DriftWatch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/driftwatch-1291) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tripathi-Nishant/CloudWatch) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1GS914PA8tHIO1s4G5Uo5HyUGPT54t1bl/view) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/62229e530c1f40b5839b048ff6958e2e) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Turning ML Monitoring into Decision Intelligence.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square)

**The problem it solves**

Machine learning models in production often fail silently.
Unlike traditional software, they don’t crash they continue running while gradually making incorrect predictions as the underlying data changes over time (data drift).

This creates serious issues:

▪️Decreasing model accuracy
▪️Hidden financial losses
▪️Poor business decisions
▪️No alerts or visibility into what went wrong

Most existing solutions either:

Focus only on model performance (not data changes), or Provide complex metrics without clear actions

How DriftWatch solves it

DriftWatch continuously monitors training vs production data to detect drift in real time.

It goes beyond detection by:

▪️Identifying the type and cause of drift
▪️Recommending actionable steps (retrain, fix schema)
▪️Estimating business impact (accuracy drop & financial loss)
▪️Providing clear decisions: ACT / IGNORE / MONITOR
Impact

DriftWatch makes ML systems:

▪️More reliable
▪️Transparent
▪️Business-aware

It transforms ML monitoring from passive dashboards into active decision-making systems.

**Challenges we ran into**

One of the biggest challenges was reliably detecting drift across different types of data distributions without generating too many false positives.

Initially, when I implemented statistical tests like PSI and KL Divergence, I noticed that:

Small natural variations in data were being flagged as drift
Different features behaved very differently (numerical vs categorical)
Threshold tuning was inconsistent across datasets

This made the system noisy and less practical for real-world use.

How I solved it

▪️ Combined multiple statistical methods (PSI, KL, KS Test) instead of relying on a single metric
▪️ Designed adaptive thresholds based on feature type and distribution
▪️ Separated handling for numerical and categorical drift
▪️ Added a classification layer to identify the root cause before triggering alerts

Another Challenge

▪️Building the system as a complete decision pipeline (not just detection) was also tricky.
▪️Mapping drift → action → business impact required designing multiple layers
▪️Estimating accuracy drop and financial loss in a generic way was non-trivial

I solved this by creating a modular pipeline:
▪️Detect → Classify → Recommend → Evaluate → Decide

Outcome
These improvements made DriftWatch:
▪️More accurate and reliable
▪️Less noisy (fewer false alerts)
▪️More practical for real-world ML pipelines

Team **Outliers** -- [Divya DS](https://github.com/divyads5), [Nishant tripathi](https://github.com/Tripathi-Nishant)

`2026-05-04`

---

### AarogyaX Cure
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aarogyax-cure-40b8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/animesh2008-projects/AarogyaX-Cure) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aarogyax-cure-936f95.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> One Platform. Faster Help. Better Care.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Vanilla JS](https://img.shields.io/badge/Vanilla%20JS-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**

In an emergency, people often don't know where to go, who to contact, or how to quickly share their location and medical information. They may have to use different apps or make several calls, which can take valuable time.

**AarogyaX** Cure brings these things together in one place. It helps users quickly send an SOS, share their location, find nearby hospitals and labs, connect with blood donors, access their emergency medical information, and get basic AI-powered health guidance.

The idea is simple: make it easier for people to get the right help at the right time, without having to manage everything separately.

**Challenges we ran into**

**Challenges We Ran Into**

One of our biggest challenges was getting different parts of the project to work together smoothly. We were integrating Firebase, Geoapify, GPS location, the Flask backend, and the Gemini AI assistant, so a small issue in one service could affect the overall workflow.

We also had to handle things like location permissions, real-time Firestore updates, API responses, and different user roles. We solved these issues by testing each feature separately, checking the API responses carefully, and then connecting everything step by step.

Another challenge was making the AI assistant useful without making it sound like a doctor. We added clear safety guidance so that it provides basic health information and first-aid guidance rather than claiming to give a final diagnosis.

Overall, the biggest lesson was that integrating multiple services is much harder than building each feature individually, but testing everything in smaller parts helped us get the system working reliably.

Team **AARS NexGen** -- [Animesh Karmakar](https://github.com/animesh2008-projects), [RAJ PATRA](https://github.com/raj21092006), [Atanu Mondal](https://github.com/0Atanu0), [JITEN MAHATO](https://github.com/jiten2007)

`2026-08-27`

---

### CodeSensei
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codesensei-26f9) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://code-sensei-8hro.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Debug loud. Learn fast. Get roasted.

![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![API](https://img.shields.io/badge/API-333333?style=flat-square)

**Challenges we ran into**

### 1. Inconsistent output between Groq and Gemini

Running two different models side by side was looking cool until I tried to merge their responses into one UI. Groq Llama 3.3 and Gemini 3.7 don't format their responses the same way, they each have their own style of describing the problem. That meant the same bug could show up looking completely different depending on which model caught it first, which broke the one clean feed I was going for.

### 2. Socket.io connections dropping mid-session

The real-time sync (Battle mode, live opponent feed, Socket Live status) relied on persistent connections staying alive but sockets would randomly drop mid session, which meant a player's code would freeze on the opponent's screen or the live feed would just go stale without any obvious error. The connection kept disconnecting for no clear reason.

**The problem it solves**

## The Problem

Learning to actually debug not just copy-paste from Stack Overflow is one of the hardest and loneliest parts of becoming a developer. Most coding practice platforms either:
- Throw test cases at you and go silent until you pass or fail, with zero insight into why your logic actually broke
- Give you AI help that's totally disconnected from the moment you need it you have to stop, copy your code, paste it into a chatbot, and lose your whole flow
- Turn debugging into something that feels like homework instead of something fun,so people burn out before the skill even sticks

And on top of all that, most practice happens alone, in silence. No pressure, no one watching, no real feedback. But that's not how debugging actually feels in the real world a teammate catching your bug in a PR, everyone on a live incident call staring at the same broken function that energy is nothing like grinding problems by yourself at 1am.

CodeSensei turns debugging into something live and social, with an AI actually narrating what's going on instead of you staring alone at a red squiggly line wondering what you did wrong.

- **Real-time AI diagnostics** (Groq Llama 3.3 + Gemini 3.7) watch your code as you type and call out logic bugs while you're still writing them you don't need to run anything or wait for a failed submission to find out something's broken
- **Roast Mode** gives you blunt, funny feedback on bad patterns leftover `// BUG` comments, unhandled edge cases, sloppy boundary checks and honestly it sticks better precisely because it's entertaining instead of another wall of dry text
- **1v1 Battle mode** turns fixing bugs into a live race against another player, with a synced read-only feed of their code so you can see how they're doing without touching it — basically the pressure of real debugging under a deadline, minus the real consequences
- **Solo Dojo** and **Pair Sandbox** let people go at their own pace or team up, so it works whether you're grinding solo or practicing with a friend/mentor
- **AI Tutor** actually explains why a bug happened instead of just handing you the fix closing that annoying gap between "the AI told me the answer" and "I actually understand what went wrong"

[Subham Sutardhar](https://github.com/SubhamFlow)

`2026-08-21`

---

### SafeX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safex-f936) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/suhanimaurya05/women-safety.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://suhanimaurya05.github.io/women-safety/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/56e3f0598b044a87af3be9e168815808) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> One Stop women's safety Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

SafeX combines critical safety features into a single, intuitive platform with:

- **Emergency SOS**: providing One-touch activation for rapid emergency response
- **Trusted Contacts Feature**: you can Manage and notify emergency contacts instantly
- **Live Location Sharing**: you can Share your real-time location with trusted people
- **Nearby Help Finder**: Locate police stations, hospitals, and emergency services
- **Safe Route Guidance**: Get safety-rated route recommendations
- **Fake Call Feature**: Discreet escape option for unsafe situations
- **Incident Reporting**: Document and report safety incidents
- **Status Tracking**: Communicate your current safety status

All of this us Built using robust yet simple techstack.

| **Frontend**   | React                |
| **Build Tool** | Vite                 |
| **Styling**    | Tailwind CSS         |
| **Language**   | JavaScript           |
| **Storage**    | Browser local Storage|
| **Deployment** | GitHub Pages         |

judges , Even a seconds delay costs big time if the right measures are not taken at the right moment . So to reduce this gap of panic and fear we decided to use technology . We want to build a community where people don't just care , but also do something about women safety . Our idea is also highly feasible with future plans of launching it as a downloadable playstore app and also integration in smart watches for maximal functionality . Also we plan to use AI stress detection to auto initiate SOS response . And we hope to make our society a safer better space for all of us.

**The problem it solves**

help , help , someone pls help me . imagine being in a state of crisis and shouting for help unsuccessfully . Good morning judges , i think it is not much of a secret how is the state of crime against women in india , about 66.2 cases are reported per lakh women in india and what's surprising is that most of the cases are never reported . women always have to be on high alert while travelling and even then on the face of real danger they are barely able to do anything . There are measures but what good are they if you can't think properly due to panic and fear . Taking this problem as the base of our project we team codeSherlox built Safex . A women safety platform built to provide quick emergency response , trusted contact management, and intelligent route guidance.

**Women Safety**

Even a seconds delay costs big time if the right measures are not taken at the right moment . So to reduce this gap of panic and fear we decided to use technology . We want to build a community where people don't just care , but also do something about women safety . Our idea is also highly feasible with future plans of launching it as a downloadable playstore app and also integration in smart watches for maximal functionality . Also we plan to use AI stress detection to auto initiate SOS response . And we hope to make our society a safer better space for all of us.

Team **codeSherlox** -- [Janvi Agrawal](https://github.com/janvi123-boop), [Suhani Maurya](https://github.com/suhanimaurya05), Mansi Singh

`2026-08-16`

---

### Bellwether
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bellwether-10fb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/navyabijoy/push-to-prod/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0u6XGytHFVw) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> APIs should fix your code, not announce breakage.

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Slack API](https://img.shields.io/badge/Slack%20API-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square)

**What is the deployed URL for this project?**

bellwether-hazel.vercel.app

**How Did You Use Claude?**

Claude runs three separate jobs inside the pipeline, each deliberately narrow.

The first is reading prose. When a field's description changes, we ask Claude a single factual question with only three allowed answers: did the unit or meaning of this field change, yes, no, or unclear. We never ask whether something is breaking. Claude answers the question, and our own rules decide what that answer means. This split is the whole design. It's why the same spec change always produces the same verdict, and it's why a wrong answer can't quietly become a severe finding.

The second is writing the test that proves a problem exists. Claude writes a test describing how the code should behave under the new contract, and we run it against the customer's untouched code. If it fails, the problem is real. If it passes, we drop the finding.

The third is writing the fix itself.

Everything Claude produces gets checked by something that isn't Claude. The test has to fail on the original code, the fix has to make it pass, the patched code has to compile, and the customer's existing tests have to still pass. If any of that fails, nothing gets sent. We also record which parts came from a model and which came from our own logic, and it shows up in the pull request, so nobody mistakes one for the other.

Claude also wrote most of the code, through Claude Code. The more useful thing was using it to audit work rather than produce it. We had it read the existing codebase and report only what it could verify by actually running, which is how we found that our verification step was passing every single finding because it couldn't run the tests at all, and that every finding was pointing at the same wrong line. Later we had it generate synthetic code with known problems and check whether we found exactly those. That turned up six cases we were silently missing, including one where our own logic invented a problem that didn't exist. Six real defects came out of writing tests rather than reading code.

**How you are solving it?**

When a vendor's API spec changes, we start by comparing the old and new versions to see what actually changed. Some of those changes are structural, like a field being removed. Others only exist in the written description, where a field's meaning shifts while its type stays the same. Those are the ones nothing else catches, so we use a model to read the prose and answer narrow factual questions about it. The model never decides how serious something is. It answers questions, and fixed rules decide what the answers mean, so the same input always produces the same result.

Next we look at the customer's code and find the places that depend on what changed. Not just where a field is read, but where the code makes an assumption about it, like comparing against a value that no longer exists.

Then comes the part that matters most. For every possible problem, we write a test and run it against the customer's unmodified code. It has to fail. If it passes, the code doesn't actually depend on the change, so we drop the finding and say nothing. Only if the test fails do we write a fix, apply it, confirm the test now passes, and confirm the customer's existing tests still pass. Everything runs in an isolated container. Anything that can't get through all five steps never becomes a pull request.

That last part is why this can be trusted with repository access. A wrong guess can't reach a developer, because it can't produce a test that fails on real code. In our runs, ten changes to a spec produced four pull requests.

What we built is a GitHub App. You install it, it watches the vendor's spec, and when something changes it opens a pull request explaining what broke, showing the exact line, and including the test output from before and after the fix. It posts to Slack when it does.

**What is the problem your project solves?**

Every piece of software depends on APIs it doesn't control. When one of those APIs changes, the code calling it can break, and often it breaks quietly. Nothing crashes, nothing fails to build, no test goes red. The code keeps running and starts doing the wrong thing, sometimes for months before anyone notices.

Vendors do announce these changes. Nobody reads changelogs. The person who wrote the affected code has usually moved on, and even a careful team can't audit every line against every release note from every provider they use. Some of the worst changes never make it into a changelog at all, because the vendor didn't consider them breaking.

This mattered less when there was nothing better to do about it. That's no longer the case. Developers already let tools work directly inside their repositories, and the hard part of changing code automatically is solved. What's missing is the layer that connects an API provider to the code their customers actually wrote.

We watch third-party APIs for changes, find the exact lines in your code that break, and prove it by writing a test that fails against your real code before we touch anything. Then we fix it, confirm the test passes and nothing else broke, open a pull request, and post it to your Slack. If we can't prove a problem, you never hear about it.

The impact is a shift in who does the work. Right now the burden sits on every customer to notice, understand, and repair a change they didn't make. It should sit with the provider who made it. If this works, an API provider stops announcing breaking changes and starts shipping the fix, and the developer never reads the changelog because there's nothing left to do about it.

Team **Blue Cheese** -- [Swayam Mishra](https://github.com/swayam-mishra), [Navya Bijoy](https://github.com/navyabijoy)

`2026-08-08`

---

### Nines
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nines-fc85) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kkrishguptaa/nines) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_DVCk4C6zvw) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Reliability compiler for Claude

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![Agents](https://img.shields.io/badge/Agents-333333?style=flat-square) ![Wilson](https://img.shields.io/badge/Wilson-333333?style=flat-square) ![Reliability](https://img.shields.io/badge/Reliability-333333?style=flat-square)

**What is the deployed URL for this project?**

https://github.com/kkrishguptaa/nines

**What is the problem your project solves?**

## The problem

Agents are right *most* of the time. That is not a shipping bar.

Per-step errors **compound**. Twenty steps at 95% each finish around **36%** end-to-end (PRD compounding math). High-stakes work stays manual because teams cannot *declare* a reliability target and know whether it cleared.

Today you pick a model and hope. Nothing lets you name a bar, spend compute until the math clears it, or stop honestly when it does not.

## Why it matters

Without a measured gate, demos ship silent best-guesses. Judges and operators need a **receipt**: green ship or red escalate — never a fake 100% after a lucky streak.

## Impact

Nines is embeddable **infrastructure around Claude** (Apache 2.0): other products call one public seam and get budgeted evidence, not vibes.

**How you are solving it?**

## Approach

Nines is a **reliability compiler**. One public Python seam:

```python
from nines import run, Task, Budget

receipt = run(
    Task(prompt="..."),
    target=0.8,
    budget=Budget(max_cost_usd=2.0, max_attempts=25),
)
# target_met → ship; else → human
```

### What we built (hackathon)

1. **Independent verifier** synthesized from the task alone (not copied from the solver).
2. **Canary / known-bad check** — discard checkers that accept garbage.
3. **Diverse fan-out** across model × effort × framing (Claude Opus / Sonnet / Haiku).
4. Every candidate **gated** by the checker; escalate until budget or bar.
5. **`target_met` only if the Wilson lower bound ≥ target** (z≈1.96) — not Wald, which collapses at 0/n and n/n.
6. **Zero passes ⇒ no silent best-guess** (`best_output` stays empty).
7. Live demos: `examples/demo_arc.py` (easy clear → hard refuse), comparison harness, Remotion pitch reel.

### Product moment

- Easy task (`is_palindrome`): 15/15 clears 0.7 — you gained *knowing*, not a “better” answer.
- Hard task (`parse_money`): pool splits (e.g. opus 5/8 · sonnet 7/8 · haiku 1/9) → **`target_met: false`**. We refuse to lie.

### Honesty bounds

We measure **checker-pass rate**, not ground truth (Stroebl-style caveat). Canary reduces risk; it does not erase it. Not a novel model; not a production multi-tenant SLA.

**Prior art disclosure:** built for Push to Prod / this repo; claims map to code in `docs/claims.md`.

**How Did You Use Claude?**

## Claude is the core intelligence layer

Nines is built **on Anthropic Claude**, not beside it.

| Role | How Claude is used |
| --- | --- |
| **Synthesizer** | Claude writes an independent checker from the task prompt alone |
| **Solvers** | Diverse fan-out across Opus / Sonnet / Haiku × effort × framing |
| **Defaults** | Bare `nines.run` uses the Anthropic adapter when `ANTHROPIC_API_KEY` is set |
| **Canary loop** | Regenerates a checker with Claude if known-bad passes |

Orchestration, Wilson gating, budgets, and Receipts are our code. **Generation and verification judgment run through Claude.**

Hackathon demos (`demo_arc`, `demo.compare`) hit live Claude with real spend (~cents for evidence). Cursor Cloud agents + Claude also accelerated implementation and pitch assets — the product itself is Claude-backed agent infrastructure.

[Krish Gupta](https://github.com/kkrishguptaa)

`2026-08-08`

---

### Agent Runtime Core (ARC-SDK)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agent-runtime-core-arcsdk-88c6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Vishallakshmikanthan/agent-runtime-core) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agent-runtime-core.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/jyNUsRmYxCo) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Don’t just run AI. Run Smarter and Reliable AI

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Adaptive Planning](https://img.shields.io/badge/Adaptive%20Planning-333333?style=flat-square) ![Agent Based Execution](https://img.shields.io/badge/Agent%20Based%20Execution-333333?style=flat-square) ![LLM Based Verification](https://img.shields.io/badge/LLM%20Based%20Verification-333333?style=flat-square) ![Agent Execution](https://img.shields.io/badge/Agent%20Execution-333333?style=flat-square) ![Middleware architecture](https://img.shields.io/badge/Middleware%20architecture-333333?style=flat-square) ![Event-driven architecture](https://img.shields.io/badge/Event--driven%20architecture-333333?style=flat-square)

**What is the deployed URL for this project?**

https://agent-runtime-core.vercel.app/

**What is the problem your project solves?**

As AI agents move from prototypes to production systems, organizations face a fundamental challenge: there is no runtime infrastructure that guarantees their reliability, observability, and recoverability.

Today, developers can build powerful AI agents using Claude, OpenAI, LangGraph, CrewAI, AutoGen, and similar frameworks. However, once these agents are deployed, they execute as opaque black boxes. If an agent hallucinates, loses context, selects the wrong tool, produces an inconsistent response, or fails midway through execution, there is no standardized runtime that can detect, verify, recover, and explain these failures.

As a result, every company independently builds its own logging, tracing, recovery logic, verification pipelines, and debugging tools—leading to duplicated engineering effort, inconsistent reliability, and systems that are difficult to trust in production.

This lack of a production-grade AI runtime is becoming one of the biggest barriers to deploying autonomous AI systems in enterprise environments.

ARC solves this problem by introducing a runtime reliability layer for AI agents. Instead of replacing existing AI frameworks, ARC sits transparently between the application and the AI model, automatically planning execution, protecting context, verifying outputs, recovering from failures, recording every execution step, and exporting production-grade telemetry.

Our goal is to make deploying AI agents as reliable and observable as deploying modern cloud applications.

![image](https://assets.devfolio.co/content/2c6eecbf82af466da53cf07e1ae82ca9/db6d1cd8-ddb9-41fa-91d5-b9b034f8e7a8.png)

**How Did You Use Claude?**

Claude is the core intelligence and execution engine inside ARC. Rather than building another AI application on top of Claude, we built a runtime layer around Claude that controls, protects, verifies, and observes how Claude-powered agents execute.

ARC intercepts Claude requests and routes them through its Adaptive AI Runtime. Before execution, ARC's planner determines the appropriate execution strategy based on the task's complexity, context, tools, verification requirements, and recovery policy. The resulting execution plan governs how the Claude request should be handled.

Claude then performs the actual reasoning and tool-driven execution, while ARC provides the surrounding runtime capabilities:

Application → ARC Planner → Context Firewall → Claude → Verification → Recovery → Flight Recorder → Telemetry

Claude is therefore not an optional feature or a chatbot inside ARC — Claude is the reasoning engine that ARC is designed to make production-ready.

We also designed ARC to remain provider-agnostic, so the same runtime architecture can eventually support other foundation models. However, Claude is our primary model and the core demonstration of ARC's capabilities.

![image](https://assets.devfolio.co/content/2c6eecbf82af466da53cf07e1ae82ca9/1d8c5a3f-b78d-4e0b-8b68-8e02fdf54ee3.png)

**How you are solving it?**

We are solving this problem by building ARC (Adaptive Runtime Core) — a production-grade AI runtime that sits transparently between AI applications and foundation models like Claude.

Instead of requiring developers to redesign their existing AI agents, ARC works as a lightweight SDK. Developers simply wrap their existing Claude application or AI agent with ARC, and every request is automatically routed through an intelligent runtime pipeline before reaching the model.

The runtime performs six core functions:

Adaptive Execution Planner – Analyzes every request and dynamically determines the optimal execution strategy, reasoning depth, context budget, verification policy, and recovery policy.
Context Firewall – Protects against prompt injection, context poisoning, duplicate context, and unnecessary context expansion before requests reach the model.
Verification Engine – Validates AI outputs using configurable verification strategies such as schema validation, execution validation, and policy checks to improve reliability.
Recovery Engine – Detects execution failures, creates checkpoints, retries recoverable failures, and enables controlled recovery without requiring application-level logic.
Flight Recorder & Replay Engine – Records every execution event, tool invocation, reasoning step, and runtime decision, enabling complete replay and root-cause analysis.
Event-Driven Runtime & Telemetry – Every component communicates through an event bus and exports telemetry, allowing seamless integration with enterprise observability platforms.

Unlike existing agent frameworks that focus primarily on workflow orchestration, ARC focuses on runtime intelligence and reliability. It actively plans, protects, verifies, records, and recovers AI execution while remaining provider-agnostic and compatible with existing AI ecosystems.

Our vision is to make AI systems as reliable, observable, and maintainable as modern cloud applications by providing the missing runtime infrastructure for production AI.

![image](https://assets.devfolio.co/content/2c6eecbf82af466da53cf07e1ae82ca9/5fc9eb74-e4f2-4e3e-af54-ed3985838276.png)

Team **VibeSync** -- [SNEHA C](https://github.com/CSNEHA20), Vishal Lakshmikanthan

`2026-08-08`

---

### Title X
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/title-x-b174) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/IshaanShettigar/title-x) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://title-x-web.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GGtbTpJkJW8) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI junior associate for Indian property title law

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![OCR](https://img.shields.io/badge/OCR-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**What is the deployed URL for this project?**

https://title-x-web.vercel.app/

**What is the problem your project solves?**

A property title search in India takes a lawyer **3–5 days per file**. The work is almost entirely manual: reading decades of deeds, Encumbrance Certificates, RTCs and mutation records — often in Hale Kannada or handwritten revenue script — and then cross-referencing them by hand to reconstruct who owned what, when, and whether anything is missing.

Two things make this brutal.

**Economics.** Bank empanelment work pays ₹1,500–5,000 per file, so days of senior-lawyer time destroys the margin. Firms also rely on expensive specialist translators simply to read the source material.

**Liability.** A suppressed mortgage or a single broken link in a 30-year chain of title is a professional-negligence event. These misses aren't caused by incompetence — they're caused by fatigue, on page 180 of 240, at the end of a long day.

And the costly failure usually isn't misreading a document. It's the document that was never in the file at all. An Encumbrance Certificate lists every transaction ever registered against a property; if it records a mortgage in 2011 and the corresponding deed is absent from the case file, that gap is invisible unless someone manually reconciles the ledger against the folder, line by line.

That reconciliation is exactly the work no human does reliably — and exactly what a machine should never get tired of doing.

**How you are solving it?**

**Title X turns the lawyer from a searcher into a reviewer.**

## Reading the file

A lawyer drops in the property's documents and walks away. Title X reads every page — including old Kannada and handwritten revenue records — works out what each document actually is, and pulls out what matters: the parties, the property, the dates, the survey numbers, the encumbrances.

It knows the difference between a Partition Deed and a Power of Attorney, and reads each on its own terms the way a lawyer would, rather than applying one generic template to everything.

Critically, nothing it tells you is unverifiable. Every extracted fact is attached to the exact sentence and page it came from — click a name, land on the pixel. Lawyers are professionally paranoid, and rightly so. We never ask them to take our word for anything.

## What we built today: catching what isn't there

Reading documents well is table stakes. The expensive mistakes in title work aren't misread documents — they're **missing** ones. A mortgage registered in 2011 that nobody ever obtained the deed for. A release that was never filed. These gaps are invisible precisely because there is nothing in the folder to notice.

But there is a way to see them. An Encumbrance Certificate is the government's own ledger of every transaction ever registered against a property. So you audit the file against the ledger: for every transaction on record, is the underlying document actually here?

That is a genuinely tedious reconciliation — across decades of records, names spelled four different ways, and document numbers written in three different formats. It is precisely the work a human does badly at 6pm.

Title X now does it automatically. Open a case and you see, in plain terms, which registered transactions have no supporting document on file, which of those actually threaten the title, and which are harmless noise. And because pointing at a problem isn't much use on its own, it drafts the email to the client requesting exactly those missing documents.

That's the shift we're after. Not *"here's a summary of your documents"* — but *"here are the four documents missing from this file, here's the one that matters, and here's the email asking for it."*

**How Did You Use Claude?**

Claude is the intelligence layer of the product, not an add-on. Every AI call in production runs on **`claude-opus-5`** via the Anthropic API, across four distinct jobs.

**1. Document classification.** A fast, low-effort pass reads the OCR text and identifies what the document actually is, from a taxonomy of 50+ Indian legal instrument types — plus a flag for compound documents that are several instruments stapled together. This routes everything downstream.

**2. Type-specialised extraction.** A high-effort pass then runs a prompt and response schema specific to that document type, returning structured legal data where every field carries its source quote and page number. We map our internal thinking level onto Anthropic's effort control, so cheap routing work and hard extraction work get proportionate reasoning budgets through the same interface.

**3. Cross-document reconciliation.** The EC gap check is where Claude does genuinely hard work. We deliberately narrowed its job: deterministic code handles the mechanical normalisation of document numbers, and Claude adjudicates only what code cannot — whether "Krishnappa S/o Ramaiah" in a 2011 ledger entry is the same person as "K. Krishnappa" on a deed, whether a date discrepancy is registration lag or a genuinely different transaction, and whether a given gap is material to the title. It returns a structured verdict with reasoning for every row.

**4. Drafting the next action.** Claude reads the completed gap check and drafts the client email requesting the specific missing documents.

We also used **Claude Code** as our primary development environment for this build — the workflow substrate, the gap-check logic, and its frontend were designed and implemented with it.

Team **Juris Machina** -- Rapaka Vivek, [Ishaan Shettigar](https://github.com/IshaanShettigar)

`2026-08-08`

---

### IndustrialSafetyAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/industrialsafetyai-8af1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/keshav123126/IndustrialSafetyAI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1FfQ425o_rs?si=xReWCINGRQafZUyC) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Industrial Safety Monitoring

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Arificial Intelligence](https://img.shields.io/badge/Arificial%20Intelligence-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

The problem it solves

Industrial workplaces are exposed to many safety risks such as workers not wearing proper Personal Protective Equipment (PPE) and unsafe environmental conditions like high gas levels, smoke, or temperature. Manual monitoring is time-consuming and may miss important safety violations.

Industrial Safety AI helps solve this problem by combining Machine Learning and Computer Vision. It predicts workplace risk from sensor data and automatically detects PPE compliance from images using YOLOv8. The system also provides safety recommendations, keeps a history of predictions, generates PDF reports, and includes an AI assistant to answer safety-related questions. This helps industries improve worker safety, reduce accidents, and make safety monitoring faster and more reliable.

**Challenges we ran into**

Challenges we ran into

During development, we faced several challenges. Setting up the project structure and managing dependencies between FastAPI, Streamlit, YOLOv8, and the Machine Learning model required careful debugging. We also encountered module import errors, empty CSV issues in the statistics page, PDF generation problems, and deployment limitations because YOLO models required more memory than free hosting services allowed. Another challenge was integrating different modules into a single application while keeping the project organized. We solved these issues by restructuring the project, improving error handling, optimizing the code, separating modules, testing each feature individually, and using Git for version control throughout development.

Team **shdj** -- Naina Garg, Keshav Mittal, Kumar Aryan

`2026-08-02`

---

### InflectRS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/inflectionrs-4b70) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jnaitik/inflection-rs) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GQgB29L4RLc) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> 1:1 safe Rust port of Python's inflection library.

![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Regex](https://img.shields.io/badge/Regex-333333?style=flat-square) ![Cargo](https://img.shields.io/badge/Cargo-333333?style=flat-square) ![CLI](https://img.shields.io/badge/CLI-333333?style=flat-square) ![open source](https://img.shields.io/badge/open%20source-333333?style=flat-square) ![Unicode](https://img.shields.io/badge/Unicode-333333?style=flat-square)

**Challenges we ran into**

Porting a dynamically typed Python library into a strictly typed, zero-allocation Rust codebase presented several non-trivial engineering challenges. Here is how we tackled them:

---

### 1. Reconciling Python vs. Rust Regex Engines
* **The Challenge:** Python's re module supports backreferences (\1) inside replacement strings and arbitrary regex features. Rust’s high-performance regex crate uses finite automata with linear-time search guarantees, which explicitly disallows backreferences within match patterns and expects $1 notation in substitutions.
* **How We Solved It:** We systematically audited every singularization, pluralization, and casing rule from the Python source, rewriting backreferences into Rust-compatible $1 string interpolation syntax without breaking edge-case match logic.

---

### 2. Zero-Allocation Cow<'a, str> Architecture
* **The Challenge:** Standard string manipulation usually allocates fresh String instances on every call. Our goal was to eliminate heap allocations whenever a string doesn't actually change (e.g., calling pluralize("people") should return "people" without allocating new memory).
* **How We Solved It:** We refactored key transformation APIs (pluralize, singularize, transliterate) to return Cow<'a, str> (Clone-on-Write). Combined with an .is_ascii() fast-path check, strings that require no modifications borrowing directly from the input string slice, completely bypassing heap allocation.

---

### 3. Fixing Upstream Edge-Case Bugs & Panics
* **The Challenge:** To guarantee 1:1 behavioral equivalence, we ran original Python edge cases against our Rust implementation. This exposed hidden bugs present in the original Python code:
  - camelize("", false) caused an unhandled index out-of-bounds error on empty strings.
  - The singularization rule for "oxen" lacked a terminal $ anchor, causing accidental regex collisions with unrelated terms.
* **How We Solved It:** We added guard clauses for empty/malformed inputs and tightened all regex rule anchors across our entire rule dictionary, validating the fixes with a comprehensive 93-test behavioral suite.

---

### 4. Thread-Safe Global State in Safe Rust
* **The Challenge:** Python compiles module-level regex patterns lazily into global list objects. In Rust, sharing global mutable state across threads requires careful synchronization to avoid data races or lock contention.
* **How We Solved It:** We leveraged std::sync::LazyLock to initialize regex rules lazily on first access. This guarantees compile-once execution and safe, immutable, multi-threaded access without writing a single line of unsafe code.

**The problem it solves**

### 1. Eliminating Python's String-Handling Bottlenecks
Python is a go-to language for text processing and web services, but libraries like Python’s inflection rely on dynamic execution and interpreted string processing. When scaling high-throughput APIs, microservices, or data pipelines that transform millions of strings (e.g., ORMs mapping snake_case database columns to CamelCase JSON schemas), string manipulation becomes an unexpected performance bottleneck. 

inflection-rs provides a **1:1 behaviorally equivalent, high-performance Rust port** that delivers sub-microsecond transformations while guaranteeing zero memory leaks and thread safety.

---

### 2. Zero-Allocation Memory Efficiency
Standard string inflection libraries frequently allocate new heap memory on every single function invocation, creating heavy garbage collection overhead or memory fragmentation.

* **How inflection-rs fixes this:** By utilizing Rust's Cow<'a, str> (Clone-on-Write) smart pointer along with .is_ascii() fast-path checks, inflection-rs avoids heap allocation entirely when processing strings that do not require modification. 
* **The Result:** Massive throughput gains in resource-constrained CLI utilities and concurrent server applications.

---

### 3. Absolute Memory Safety & Concurrency Guarantee
In dynamic or C/C++ string processing tools, multi-threaded text transformation runs the risk of race conditions, buffer overflows, or unexpected runtime panics.

* **100% Safe Rust:** Written with zero unsafe blocks and enforced with strict cargo clippy lint checks.
* **Thread-Safe Rule Compilations:** Replaced Python’s runtime-compiled regular expression lists with static, thread-safe std::sync::LazyLock regex instances. Regexes compile exactly once per application lifecycle and can be safely shared across thousands of concurrent OS threads without lock contention or re-parsing overhead.

---

### 4. Patching Unhandled Edge-Case Bugs
During the porting process, we audited Python’s original implementation and discovered critical edge-case bugs that could cause silent failures or runtime panics. inflection-rs fixes these outright:

* **Panic Prevention:** Python’s camelize("", false) crashes on empty inputs due to unhandled index lookups. inflection-rs handles empty inputs cleanly and predictably.
* **Incorrect Matches:** Python’s singularization rule for "oxen" lacked a terminal $ regex anchor, leading to accidental partial matches on unrelated words. inflection-rs ensures precise anchor boundaries across all 93 passing behavioral tests.

---

### 5. Dual-Crate Utility: Embedded Library & Standalone CLI
inflection-rs isn't just a backend library; it serves two distinct developer workflows out of the box:

1. **Rust Library (inflection):** Drop-in dependency for Rust microservices, web frameworks (Axum, Actix), code generators, and ORMs needing fast, reliable text casing and pluralization.
2. **Terminal CLI (inflection-cli):** A lightweight binary powered by clap for DevOps engineers, shell scripting, and CI/CD pipelines needing fast, cross-platform batch text transformation directly in bash or zsh scripts.

Team **Panic! At the Compiler** -- Prashant Chandra, [Naitik Jain](https://github.com/jnaitik)

`2026-08-03`

---

### Aegis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegis-autonomous-infrastructure-renewal-agent-1118) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Venkat-Kolasani/aegis-renew) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aegis-renew-sigma.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/klwkgypoI0c) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Autonomous Infrastructure Renewal Agent

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square)

**The problem it solves**

Domains, TLS certs, and DNS records expire quietly. Small teams almost never notice until something breaks or a subdomain gets hijacked, because when you're two people running side projects, nobody's actual job is watching for renewals. You find out from a broken link, not a calendar reminder.

Aegis keeps an eye on a portfolio of domains, checking RDAP for expiry, crt.sh (with a live TLS handshake as a fallback) for certs, and DNS for dangling CNAMEs that match known takeover patterns. An LLM ranks what actually needs attention, and if a renewal is genuinely covered by a mandate you already approved, locked to one merchant, one price cap, one year, Aegis renews it and shows you the completed checkout.

Most monitoring tools stop at the warning email. We wanted this one to actually finish the job, but only inside limits you set ahead of time, never past them.

**Challenges we ran into**

Honestly, the failure mode we were most scared of wasn't a normal bug, it was the agent spending money it shouldn't. Most of our real engineering time went into making sure the ranking step could never trigger a charge by itself. POST /api/agent/rank is completely side-effect-free, it only writes a recommendation. A separate policy re-checks everything right before money moves, merchant name, URL, country, currency, exact price, against an actively approved mandate, and checks it all again immediately before the charge fires. Writing two checks for the same thing felt excessive at first. Then a test caught a stale mandate that the first check missed and the second one didn't, and it stopped feeling excessive.

Finding a real merchant to renew against was its own headache. We spent an hour going through actual registrars, Namecheap, Porkbun, GoDaddy, Hover, name.com, looking for anything with a working agent checkout path, and came up empty. Turns out Prava's UCP integration is built around Shopify storefronts, not domain registrars, which we hadn't expected going in. Rather than fake a real integration to look more polished, we built our own small demo registrar and disclosed it plainly, in the code and the README.

The bug that actually broke our sandbox test: we minted real Prava payment credentials, the network confirmed the charge as SUCCESS, and the merchant reported it back as DECLINED. Two systems disagreeing about whether money moved is not something we wanted to quietly paper over, so the API now distinguishes "the merchant confirmed checkout" from "the payment provider confirmed that outcome." When they disagree, it reports reconciliation_required instead of pretending everything succeeded.

One smaller, dumber one: the shared schema had a column literally named provider_mandate_id, and our own security rule says we're never allowed to store a raw Prava mandate ID anywhere. We didn't want to quietly break our own rule, and didn't want to rename a column the other person owned without checking first, so for now the ORM maps it to a one-way digest instead of the real value, with a note to rename it properly once we'd actually talked it through.

**Best Visa Intelligent Commerce Implementation**

Aegis uses Visa Intelligent Commerce through Prava, not a raw card form in the browser.

The user approves a yearly, merchant-locked Prava mandate once with a passkey. For covered renewals, the server mints ephemeral Visa network-token credentials (single-use token + dynamic CVV) and completes checkout, then reports the outcome back to Prava.

Security boundaries we kept:
- Browser never sends amount, mandate id, network token, or CVV (only `domain_id`)
- Ranking with OpenAI never charges
- Execution only proceeds when an active matching mandate, merchant lock, quote under the cap, and final `auto_renew` all align

Evidence is real Prava sandbox end-to-end (mandate approval through completed DEMO checkout), with the DEMO merchant disclosed. That is a Visa-tokenized agent payment path for infrastructure renewal, with standing mandate authority after one passkey.

**Most Startup-Ready Product**

Aegis is a deployable product slice, not a notebook demo.

What ships today:
- Live operations UI: https://aegis-renew-sigma.vercel.app/dashboard
- Live API + Postgres: https://aegis-api-imf0.onrender.com
- Cold-start path without on-camera DB seeding
- Real Prava sandbox mandate + completed checkout evidence in `docs/evidence/`
- Honest README scorecard (DEMO registrar disclosed; production keys out of scope)

The console has a clear four-step pipeline (scan → mandate → OpenAI rank → covered renew), safety gates that block charge on `flag_for_review`, and host-dashboard secrets only. A two-person team can demo from a cold load: scan an authorized host, approve a yearly mandate once, rank, and execute only when coverage allows.

That is startup-ready in the hackathon sense: working software, deployed URLs, real payment proof, and clear limits instead of a half-working larger claim.

**Participation Credits (Already Claimed)**

Aegis uses OpenAI as a core product step, not a bolt-on demo.

After scanning authorized hostnames for domain expiry, TLS expiry, and DNS takeover risk, we call OpenAI `gpt-4o` through the official SDK with strict structured outputs. The model returns explainable `criticality_score`, `decision` (`auto_renew` | `flag_for_review` | `ignore`), and `reason` for each domain.

Ranking is side-effect-free: it never mints a Prava credential or charges a mandate. A separate deterministic policy may keep or downgrade `auto_renew` when coverage is missing or the quote does not fit. Autonomous renewal only runs when a user-approved yearly Prava mandate, merchant lock, quote, and final `auto_renew` all align.

That makes OpenAI the judgment layer in a real agentic commerce loop: detect risk, decide with gpt-4o, pay only under standing mandate authority. Live demo and sandbox payment evidence are linked in the project.

**Best Agentic User Experience**

Aegis treats autonomous payment UX as a trust problem, not a dashboard skin. The console walks operators through one clear path: Scan → Approve mandate → Rank with OpenAI → Renew only when policy allows. Inventory risk signals and OpenAI decisions are labeled separately so people never confuse a scan score with an authorization to spend. Execute stays disabled until the final decision is auto_renew, so the UI itself blocks unauthorized charges. Callouts disclose the demo merchant and mandate caps so every high-stakes step is legible before money moves.

Team **FutureBoX** -- [Venkat Kolasani](https://github.com/WhiteDeViLOp0), [vivek vattem](https://github.com/vivekvattem)

`2026-08-02`

---

### John CEO Pay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/john-ceo-payments-ad15) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/John-CEO-HQ/prava-rnd) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://john.ceo) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Pay from Telegram via Prava

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Webauthn](https://img.shields.io/badge/Webauthn-333333?style=flat-square) ![Hono](https://img.shields.io/badge/Hono-333333?style=flat-square) ![MCP](https://img.shields.io/badge/MCP-333333?style=flat-square)

**The problem it solves**

AI chats can suggest a purchase, but someone still has to leave and pay - or paste a card into the bot. John CEO Pay lets you confirm a buy in Telegram and approve on Prava's hosted page, so the agent never sees the card. Useful today for founders who already talk to John and need a safe checkout handoff. Next: finish the return path once Prava/Visa unblocks post-OTP, then live MCP shopping when EU cards work.

Before: John CEO (john.ceo + Telegram). This weekend: Prava pay path (prava-sdk sandbox checkout, prava-pay MCP kept for later, skills, feature-flagged mounts).

**Challenges we ran into**

Two blockers.

1) Prava Pay MCP is production-only (no sandbox host). Our EU cards are rejected on live pay.prava.space, so we could not finish MCP checkout. Prava recommended the SDK/API sandbox. We built prava-sdk (Telegram -> payment_url -> hosted card/OTP) and kept MCP for later.

2) SDK sandbox E2E: full integration works through create session from John, open Prava, enter card, submit OTP. We debugged this live with the Prava team. After OTP the Prava page freezes and never returns to John CEO, so we do not get an order id. Prava said the hang is on Visa's side; no fix before the deadline. Our callback/poll path is wired; we are waiting on that upstream fix.

Worked: Telegram confirm, real Prava sandbox session, card + OTP, secrets stay on the control plane.
Did not: order id back in chat; EU live MCP checkout.
Learned: SDK/API was the right demo path for us; we will not claim a completed order until the return works.

**Best Visa Intelligent Commerce Implementation**

We run the commercial action through Prava (Visa Intelligent Commerce partner): sandbox Visa test card, OTP, and hosted collect. The agent only creates the Prava session and waits for status; Visa credentials never enter Telegram. We reached OTP end-to-end, including a live debug call with Prava. After OTP the Prava page freezes; Prava said the hang is on Visa's side. We are not claiming a completed order until that returns - the Visa path is integrated and demonstrated through OTP.

**Most Startup-Ready Product**

John CEO is already a live product (john.ceo, Telegram coworker). This weekend we added a real Prava pay workflow on that product - not a throwaway demo shell - behind feature flags, with secrets kept on the control plane. Clear user (founder/ops buying from chat), working handoff through Prava card/OTP, and a path to keep using it after the event once the post-OTP return is unblocked.

**Best Agentic User Experience**

John confirms merchant and amount in Telegram, then sends the user to Prava's hosted page for card + Face ID / OTP. The agent never sees card data. The UX is short and trust-clear through OTP. Return to chat with an order id is blocked today by a Prava-hosted freeze after OTP (Prava attributed to Visa); the confirm -> approve handoff still shows the product experience we are judging for.

**Agentic Commerce Hackathon**

Agent discovers/decides in Telegram; Prava enables the payment (sandbox session + hosted approve). Meaningful Prava use is the core commercial step. We disclose John CEO existed before; Prava pay path was built this weekend. Completion after OTP is blocked upstream; we do not fake an order id.

Team **John CEO** -- [Marcin Zduniak](https://github.com/mz7mz7mz7)

`2026-08-02`

---

### otto
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/otto-8e87) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DarshanHarihar1/otto) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://otto-plum-iota.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/9JZbyu7eUpI) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> a photo is the whole checkout

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square)

**Challenges we ran into**

prava sandbox needs a real passkey / face id step. worked fine in chrome on my laptop. inside imessage’s in-app browser it kept dying with “verification failed.”

same session, same card, same otp. the webview just couldn’t do webauthn.

fix was simple once i found it: start checkout in messages, finish the link in safari or chrome, then otto gets the callback and texts ordered back. annoying to hit mid build, but after that the flow was solid.

**The problem it solves**

you’re holding the thing you want and still end up searching amazon or the brand site just to buy it.

otto is an imessage agent: text a photo, get a live price, shop around if the same brand is cheaper, checkout in chat via prava. it also remembers past buys so refills don’t start from zero.

useful today because the whole flow stays in messages. no app, no cart, no tab hell.

next: tighter refill prompts from memory and smoother checkout so you don’t have to bounce out of imessage for passkey.

**Best Visa Intelligent Commerce Implementation**

otto is an imessage shopping agent that discovers, decides, and pays. photo comes in, we id the product and quote a live price, optionally shop around for a cheaper same brand option, then on yes we open a prava approval session.

prava is our visa intelligent commerce path. user binds a card once with passkey, prava issues a virtual card for the buy, otto gets the result back in chat as ordered. after the first purchase we set up a mandate for later refills (with a spend cap) so nobody re enters card details every time.

agent doesn’t just recommend. it completes a real sandbox visa backed checkout in the conversation.

**OpenAI**

openai is the brain of the flow, not a chat wrapper.

photo comes in, we use openai vision to pull brand, product, size, category off the label. that structured id is what we hit shopify with for a real price. we also use it for matching when we shop around or offer a substitute, so we’re not just string matching titles.

without that, otto is a webhook that can’t see the photo. that’s the openai track.

**iMessage Agent**

otto is an imessage agent end to end. you text a product photo to our linq number, we get message.received, run vision + shopify, and reply in the same chat with a live quote. say yes or tapback, get a prava link, ordered comes back in the thread.

not a side bot that dumps a link and bails. id, price, shop around, pay, memory for refills… all inside messages. that’s the track.

**Agentic Commerce Hackathon**

agentic commerce in the literal sense. otto doesn’t stop at “here’s a product.” it ids what you photographed, finds a live shopify price, shop arounds for a cheaper same brand option, takes yes or a tapback as intent, and checks out through prava.

payments and state live with the agent too. after a buy it keeps shelf memory and can do mandate style refills later. not a one time lookup bot. photo in, decision in chat, money out. that’s the track.

[darshan harihar](https://github.com/DarshanHarihar1)

`2026-08-02`

---

### PramanAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pramanai-f57d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/debaa98/PramanAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://praman-ai-one.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Watch your agent spend. Watch the line hold.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square) ![Observability](https://img.shields.io/badge/Observability-333333?style=flat-square)

**Challenges we ran into**

In dev, events emitted from the API route showed up, but events emitted
inside server actions randomly didn't — the trace would gaslight us. Root
cause: Next.js can load the same module more than once in development, so
the server-action bundle and the route-handler bundle each got their *own*
in-memory event array, and the poller only ever saw one of them. A proof
layer that drops evidence is worse than none. Fix: backed the store with a
`globalThis` singleton (`globalThis.__pramanTrace ??= …`) so every bundle
writes to one shared array, and documented that a production deploy swaps
this for KV/SQLite — in-memory is demo-scoped by design.

Observability is the easiest place to leak what you're protecting

Early on, we dumped whole session/response objects into the console's `meta`
field for debugging — convenient, and exactly wrong for a payments product:
an audit feed that echoes raw payloads is a credential leak with a UI.
[If true for you: what you actually caught in the feed goes here.] We
inverted the rule: `emitTrace()` never receives raw objects, only
hand-picked masked fields — amounts, merchant names, last4, truncated IDs
via a `mask()` helper. The trail proves what happened without ever
containing what must stay secret, which is also a hard hackathon rule
(no payment credentials in repos or demos).

**The problem it solves**

- The problem
AI agents can now spend real money. Payment rails like Prava (with Visa Intelligent Commerce) make agent-initiated transactions *technically* safe — scoped mandates, passkey approval, one-time credentials. But for the human, it's still a black box: you hand software your card, it says "done," and you're left trusting a claim.

Three things are broken:

1. **Opacity.** Between your "yes" and the receipt, you can't see what the agent actually did — which merchant, what amount, under which permission, whether the credential was really single-use.
2. **Unverifiable safety.** Every agentic commerce product *says* "your limits are enforced." None *show* it. Users can't tell real enforcement from a promise — and when an agent goes wrong (bug, prompt injection, hallucinated purchase), they find out from their bank statement.
3. **No accountability trail.** When something fails, there's no attributed record of who did what: did the user approve it? Did the agent overstep? Did the network refuse it? Disputes, debugging, and audits all need exactly this.

## What PramanAI does

**For users** — a live proof console beside the agent's checkout. The mandate you granted (merchant, cap, expiry), your passkey approval, the masked one-time credential, and the final network result stream in real time, each row attributed to **USER / AGENT / PRAVA / NETWORK**. Green means money moved as permitted. Red means the line held.

**For builders** — a drop-in observability layer for the Prava SDK: 4 files, zero new dependencies, one `emitTrace()` call per lifecycle step. Your compliance becomes your demo.

**Red-team mode** — one button fires four deliberately out-of-bounds attempts (over-cap, wrong merchant, expired mandate, prompt-injected "ignore all limits") through the **same real purchase path** — and shows each one refused, live. Safety demonstrated, not asserted.

## Why it makes things easier and safer

- **Converts trust into verification** — the biggest adoption blocker for agentic commerce is "I don't trust an AI with my card." Watching enforcement happen beats being told about it.
- **Faster debugging** — builders see exactly where a flow stopped: mandate check, session, approval, or checkout.
- **Built-in evidence** — the console is a shareable audit trail for disputes and support, fully masked (never PAN/CVV — last4 and truncated IDs only).
- **Defense-in-depth, made visible** — server-side mandate checks as the first line, network-level token scoping as the second, both observable.

**Prava moves the money. PramanAI proves it.**

**Best Visa Intelligent Commerce Implementation**

Visa Intelligent Commerce & Prava Integration: Demonstrates Tokenization (PAN/CVV masking), User Authentication (Passkey/WebAuthn simulation), Mandate Scope Enforcement (Cap, Merchant, Time Window), and Immutable Audit Trail.

**iMessage Agent**

Helpfull for Group-chat agent

**Agentic Commerce Hackathon**

The docs organize around four "what do you want to do" entry points, which is the closest thing to an official use-case map: letting an agent pay with your card via MCP or CLI, adding payments to your own app via SDK or API, selling to AI shoppers as a merchant or marketplace, and controlling what your agent spends through a no-code wallet dashboard. The "who benefits" section fills that in with named personas

[Debabrata Pattnayak](https://github.com/debaa98)

`2026-08-02`

---

### router.taxi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/routertaxi-9621) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pkyanam/router-taxi-hackathon) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://router.taxi/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/4IIFTOIX4Us) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> router.taxi is OpenRouter for rides.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Android](https://img.shields.io/badge/Android-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Linux](https://img.shields.io/badge/Linux-333333?style=flat-square)

**Challenges we ran into**

Our biggest hurdle was making stateful Android VMs reliably preserve Uber sessions while supporting Google Play Services and secure app streaming. We solved it with isolated snapshots, deterministic device automation, health checks, and durable session restoration. We also designed graceful payment failure handling because Prava currently supports only a limited selection of popular US banking cards.

**The problem it solves**

router.taxi is OpenRouter for rides. Ask naturally in iMessage; OpenAI structures the trip, Router compares live connected Uber and Lyft prices, Linq keeps the flow conversational, and Prava authorizes a bounded one-time payment before an isolated Android device attempts checkout. The same account-scoped pricing is available through web, REST API, and MCP. Next we plan to integrate Lyft and other providers while also speeding up response / device automation times while improving UX/usage flow.

**Best Visa Intelligent Commerce Implementation**

We integrated Prava Pay into our application which builds upon VISA agentic eCommerce platform. Final verification / Passkey goes through VISA network.

**Most Startup-Ready Product**

We're currently working with another Indian startup for distribution (https://justbobit.com) and have talks with major agent platform (https://folk.com) and sandbox provider to expand functionality. Looking to raise funding soon. We've already booked several rides with router.taxi in a test environment of our own (without Prava, still working to move from Prava sandbox -> production).

**OpenAI**

We utilize OpenAI API with GPT-5.6-Luna to process natural language queries in our Linq agent and support vague address entry.

**iMessage Agent**

You can text our iMessage Linq agent to book your entire ride! A simple "I’m at Union Station and need to get to The Wharf for less than 45 bucks." results in live rideshare pricing in chat with screenshot proof and ability to generate Prava Pay link. Then ride booking status is relaying via Linq along with final "reciept" of success/failure.

**Best Agentic User Experience**

We have a simple sign-up (one-time) process that lets you create router.taxi account, link your rideshare accounts like Uber/Lyft and then text a Linq powered number to request a ride. Once account is setup, it's a few clicks to approve payment/ride!

**Agentic Commerce Hackathon**

We utilize Prava and Linq to enable an easy-to use agent that lets you message router.taxi for a ride and book the ride end-to-end. We support REST API / MCP for any other agent to use!

Preetham Kyanam

`2026-08-03`

---

### ai-email-assistant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aiemailassistant-ca81) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/logiclayer0/ai-email-assistant) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-email-assistant-y6m87ssg5f5u5j2vscd3nk.streamlit.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Transform email chaos into clarity

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![Groq API](https://img.shields.io/badge/Groq%20API-333333?style=flat-square) ![Llama 3.3 (70B Versatile)](https://img.shields.io/badge/Llama%203.3%20(70B%20Versatile)-333333?style=flat-square)

**Challenges we ran into**

* **API Key Exposure & Security:** Storing the Groq API key directly in the codebase triggered automated security warnings on GitHub. We resolved this by implementing **Streamlit Secrets** (`st.secrets`), allowing us to securely inject API credentials at runtime without exposing them publicly.
* **Streamlit Cloud Dependency Management:** Initially encountered `ModuleNotFoundError` during deployment because cloud environments didn't recognize external dependencies. We resolved this by configuring a precise `requirements.txt` file containing `streamlit` and `groq`.
* **State & Key Management:** Ensuring smooth tab switching between the Summarizer and Draft Generator without losing input data or raising `KeyError` exceptions when handling missing secrets locally.
****

**The problem it solves**

### 📧 AI Email Assistant

In today's fast-paced environment, individuals and professionals struggle with email overload, spending hours reading long email threads and drafting polite, professional responses. **AI Email Assistant** solves this by leveraging high-speed LLMs to automate summarization and response generation in seconds.

### 🚀 Key Solutions & Features:
* **Instant Email Summarization:** Extracts core takeaways, highlights, and urgent action items from lengthy emails without requiring the user to read through dense text.
* **Smart Draft Generator:** Converts simple bullet points or quick prompts (e.g., *"Say yes to meeting tomorrow at 3 PM"*) into well-structured, professional email replies.
* **Reduces Cognitive Fatigue:** Eliminates writer's block and ensures business communications maintain a clear, polite, and effective tone.
* **Saves Hours Every Week:** Cuts down email handling time from 10–15 minutes per email thread to under 10 seconds.

Team **TECH-MAKERS** -- [Jaspreet Kaur](https://github.com/JASPREET0909), [Mahek Bajpai](https://github.com/logiclayer0)

`2026-07-30`

---

### AutoLayout.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cloak-7229) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/casualGamer-dev/autolayout.ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/14tjteouI98n2k5p34VqaihSA0F56VSsp?usp=drive_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/ViNuwDbLvnc) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Sketch. Capture. Generate.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**Challenges we ran into**

## Building Reliable On-Device AI Detection

Our biggest challenge was making the entire sketch recognition pipeline work completely offline. The TensorFlow Lite model had to run directly on mobile devices with limited resources while maintaining high detection accuracy across different drawing styles.

**How we solved it:** We trained an EfficientDet-Lite0 model, optimized it for TensorFlow Lite, verified the exported model's tensor ordering manually, and built a lightweight preprocessing pipeline that converts captured images into the exact format expected by the model. This allows fast, offline inference without relying on cloud APIs.

---

## TensorFlow Lite Output Didn't Follow Standard SSD Format

Most TensorFlow Lite object detection examples assume outputs are returned in the order:

```
boxes
classes
scores
count
```

Our exported Model Maker model instead returned:

```
scores
boxes
count
classes
```

The application initially interpreted detections incorrectly, causing misplaced UI elements and invalid layouts.

**How we solved it:** Instead of assuming the standard SSD output format, we inspected the raw tensors produced by the model, confirmed the actual output order, and updated the inference pipeline accordingly. We also added verification scripts so future model retraining automatically validates tensor layouts before deployment.

---

## Generating Real UI Layouts from Detection Boxes

Detecting interface components is only half the problem. The detected elements arrive as unordered bounding boxes, while React Native requires a structured hierarchy of rows, columns, containers, and components.

**How we solved it:** We developed a custom layout reconstruction algorithm that groups detected components by their vertical positions, sorts elements horizontally, and rebuilds the intended interface hierarchy before generating React Native code. This creates readable layouts instead of simply placing components with absolute positioning.

---

## Supporting Offline-First Code Generation

We wanted users to generate UI code even without an internet connection, while still offering AI-powered enhancements whenever connectivity is available.

**How we solved it:** Detection, layout reconstruction, and React Native code generation run entirely on-device. When internet is available, an optional enhancement pipeline uses the Gemini API together with Actian Vector AI to generate meaningful labels, improve placeholder content, and apply design themes. If offline, the core experience remains fully functional.

---

## Deploying Multiple AI Services Together

Our application combines mobile AI inference, cloud storage, semantic search, and generative AI, making deployment more complex than a traditional mobile application.

**How we solved it:** We separated the architecture into independent components. The mobile app performs all core detection locally, while the backend handles authentication, Cloudflare R2 uploads, Gemini enhancement, MongoDB persistence, and Actian Vector AI semantic retrieval. This modular design keeps the offline experience fast while allowing cloud features to scale independently.

**The problem it solves**

AutoLayout.ai eliminates the repetitive process of converting hand-drawn UI wireframes into working application code. Designers, developers, students, and startup founders often spend hours recreating paper sketches inside design tools before writing frontend code from scratch.

With AutoLayout.ai, users simply draw a UI on paper, capture it using their phone, and instantly receive clean React Native code. The app performs object detection entirely on-device, allowing sketch recognition and code generation even without an internet connection. Users can review and correct detected components before code generation, ensuring accurate layouts while dramatically reducing prototyping time.

For teams working in hackathons, product discovery, education, or rapid MVP development, AutoLayout.ai bridges the gap between imagination and implementation, transforming ideas into working interfaces within minutes instead of hours.

**Accio Relevance - Build with Actian VectorAI Database**

AutoLayout.ai uses Actian VectorAI as the semantic retrieval engine behind its AI-powered Enhance workflow. After a sketch is detected and converted into a React Native layout, the backend generates a natural-language description of the interface and performs hybrid vector retrieval over a library of UI patterns.

Rather than relying on a single nearest-neighbor search, AutoLayout.ai combines two searches: one ranks layouts by semantic similarity of the generated description, while the other filters and ranks patterns using the detected UI element types (Text, Button, Image, Switch, etc.). The two ranked lists are merged using Reciprocal Rank Fusion (RRF), ensuring patterns that are both structurally and semantically similar receive the highest priority.

The retrieved pattern is then supplied to the AI enhancement pipeline to generate more context-aware labels, themes, and UI improvements. If Actian VectorAI is unavailable, the application automatically falls back to an in-Mongo cosine similarity implementation, ensuring the feature remains available without interrupting the user experience.

**Best Use of Gemini API**

Gemini powers AutoLayout.ai's optional Enhance pipeline, adding intelligence on top of the fully offline sketch-to-code workflow.

While object detection, layout reconstruction, and React Native code generation all happen locally on the user's device, Gemini is responsible for transforming placeholder UI elements into meaningful application content. It generates realistic button labels, screen copy, and design themes while preserving the original layout detected by the on-device AI.

To maximize reliability during demos and real-world usage, AutoLayout.ai automatically falls back to OpenRouter whenever Gemini is unavailable due to missing credentials, rate limits, or service outages. This ensures AI enhancement remains available without compromising the core offline experience.

**Best Use of MongoDB Atlas**

MongoDB Atlas serves as the application's persistent backend for user accounts, authentication, sketch metadata, generated React Native code, AI enhancement results, and correction history.

AutoLayout.ai follows a local-first architecture. Every sketch is first saved locally and placed into a persistent synchronization queue that works even without internet connectivity. When connectivity becomes available, the queue safely synchronizes metadata to MongoDB Atlas and uploads sketch images directly to Cloudflare R2 using pre-signed URLs. A mutex-protected sync mechanism guarantees that concurrent uploads, edits, and deletions cannot overwrite one another, providing reliable synchronization across offline and online sessions.

This architecture enables users to continue designing and generating code anywhere while MongoDB Atlas transparently maintains long-term persistence and synchronization once the device reconnects.

Team **pnpm build** -- [Koustav Singh](https://github.com/koustavx08), [Swarnabha Datta](https://github.com/Swarnabha-Datta), [Tamanash Das](https://github.com/casualGamer-dev)

`2026-07-26`

---

### deployit
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/deployit-c319) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abhishekumar2x/deployit) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=oI8WfRX2qks) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=oI8WfRX2qks) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> One Command. Instant Deployment

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![cloudflare](https://img.shields.io/badge/cloudflare-333333?style=flat-square) ![ink](https://img.shields.io/badge/ink-333333?style=flat-square) ![bun](https://img.shields.io/badge/bun-333333?style=flat-square)

**The problem it solves**

Deploying modern web applications is still fragmented, time-consuming, and requires developers to manually choose hosting platforms, configure deployment settings, and manage provider-specific workflows.

**Challenges we ran into**

One of the biggest challenges was building a unified deployment workflow for multiple hosting providers. Each platform—such as Vercel, Netlify, and Render—has its own APIs, authentication methods, deployment endpoints, and build requirements. There was no common standard, making it difficult to create a single command that worked consistently across all providers.

Another hurdle was accurately detecting different project frameworks and build configurations. Projects can use different package managers, custom build scripts, and output directories, so relying on simple file detection often produced incorrect deployment settings.

We overcame these challenges by designing Deployit with a modular provider architecture, where each hosting platform has its own deployment adapter while exposing a common interface to the CLI. We also implemented a robust project scanner that analyzes the project structure, dependencies, and configuration files to determine the correct framework and deployment settings. This approach made the deployment process reliable, scalable, and easy to extend with support for additional hosting providers in the future.

**Open Innovation**

DeployIt embodies the principles of Open Innovation by integrating existing technologies, APIs, and open-source tools to create a unified and more efficient deployment experience. Rather than building a new hosting platform, it connects with multiple cloud providers such as Vercel, Netlify, and Render, allowing developers to choose the best platform without being locked into a single ecosystem.

The project leverages open-source libraries for framework detection and project analysis while utilizing publicly available deployment APIs to automate hosting. Its modular architecture also enables developers to contribute support for additional cloud providers, frameworks, and deployment strategies, making the platform extensible and community-driven.

By reducing the complexity of deploying applications, DeployIt lowers the barrier for students, startups, freelancers, and open-source contributors to bring their projects online. This encourages collaboration, faster innovation, and wider adoption of modern cloud technologies—key objectives of the Open Innovation model.

Team **Soanpapdi** -- [Abhishek Kumar](https://github.com/abhishekumar-dev), [Sanchit Gupta](https://github.com/sanchit0-1)

`2026-07-26`

---

### OpsForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/opsforge-4fc3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PankajGupta-dev/Ops_Forge) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/BnBVd1FOT70?si=USA5LbSsL5dMYpyU) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BnBVd1FOT70?si=USA5LbSsL5dMYpyU) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Where AI Builds, Deploys & Heals.

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![railway](https://img.shields.io/badge/railway-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square) ![pydantic](https://img.shields.io/badge/pydantic-333333?style=flat-square)

**Challenges we ran into**

# Challenges We Ran Into

Building **OpsForge** required balancing ambitious ideas with practical engineering. Throughout development, we encountered several technical and architectural challenges that shaped the final product.

---

## 1. Balancing Vision with Hackathon Constraints

**Challenge:** Our original goal was to build a fully autonomous AI Platform Engineer, but implementing every feature within a hackathon timeline was unrealistic.

**Solution:** We prioritized building an end-to-end **AI Incident Commander**, delivering a polished workflow while keeping the architecture modular for future expansion.

---

## 2. Integrating Live Telemetry

**Challenge:** Different applications expose monitoring data in different formats, making universal monitoring difficult.

**Solution:** We standardized monitoring around a **Base URL**, allowing Agent 3 to collect health, metrics, and logs from any compatible application.

---

## 3. Generating Meaningful Root Cause Analysis

**Challenge:** Raw logs and metrics alone don't provide actionable insights.

**Solution:** We integrated the **Gemini API** to analyze telemetry and generate root cause analysis, recovery recommendations, supporting evidence, and confidence scores.

---

## 4. Leveraging Historical Knowledge

**Challenge:** Similar incidents were treated independently, ignoring valuable past resolutions.

**Solution:** We introduced **Agent 5**, which retrieves similar historical incidents from MongoDB Atlas to provide context-aware recovery recommendations.

---

## 5. Improving Historical Retrieval

**Challenge:** A fixed number of retrieved incidents either missed useful context or introduced unnecessary noise.

**Solution:** We implemented a **dynamic retrieval strategy** that selects incidents based on confidence scores while maintaining an upper retrieval limit.

---

## 6. Maintaining a Modular Architecture

**Challenge:** As features grew, tightly coupling agents would reduce maintainability.

**Solution:** Each agent was assigned a dedicated responsibility with well-defined interfaces, allowing independent development and future scalability.

---

## 7. Demonstrating the Complete Workflow

**Challenge:** Showing the platform's capabilities within a short hackathon demo.

**Solution:** We designed a concise end-to-end scenario—from deployment and monitoring to AI-powered root cause analysis, historical retrieval, and knowledge base updates.

---

# Lessons Learned

- Prioritizing a polished workflow is more valuable than implementing every planned feature.
- AI is most effective when combined with structured telemetry and historical knowledge.
- Modular architectures enable rapid development and easier scalability.
- Dynamic retrieval improves recommendation quality over fixed retrieval methods.
- Reusable abstractions make the platform adaptable across diverse applications.

> **OpsForge taught us that effective AI isn't just about intelligent reasoning—it's about combining real-time telemetry, historical knowledge, and modular automation into a workflow engineers can trust.**

**The problem it solves**

> **"CI/CD gets your application into production. OpsForge keeps it running."**

## 🚨 The Problem OpsForge Solves

Modern software teams can deploy applications in minutes—but **recovering from failures still takes far too long**.

When a deployment fails, engineers are forced to switch between multiple tools to identify the issue, analyze logs, investigate metrics, search past incidents, decide on a recovery strategy, and manually execute fixes. This fragmented workflow delays recovery, increases downtime, and puts critical production systems at risk.

Existing CI/CD platforms primarily focus on **building and deploying applications**, but they stop short when something goes wrong. They don't autonomously diagnose failures, learn from historical incidents, recommend the best recovery actions, or safely orchestrate remediation with human approval.

As infrastructure grows more complex, this manual and reactive approach leads to:

- ⏱️ **Increased Mean Time to Recovery (MTTR)**
- 💰 **Higher operational costs**
- 🔁 **Repeated incidents due to limited organizational memory**
- 🚀 **Slower software delivery caused by fear of production failures**

## 💡 Our Solution

**OpsForge** addresses this gap by transforming deployment into an **intelligent, end-to-end operational workflow**.

Instead of stopping at deployment, OpsForge:

- 🤖 **Autonomously analyzes deployment failures**
- 📊 **Correlates logs, metrics, and runtime telemetry**
- 🧠 **Learns from historical incidents using semantic retrieval**
- 🎯 **Recommends the most effective recovery strategy**
- 🔊 **Generates AI-powered recovery explanations with voice approval**
- 🚀 **Safely orchestrates infrastructure recovery with human oversight**

OpsForge reduces operational complexity, accelerates incident resolution, and enables engineering teams to ship software with greater confidence.

---

## ⭐ Key Takeaway

> **Traditional CI/CD automates deployments. OpsForge automates operational decision-making.**

> **CI/CD gets your application into production. OpsForge keeps it running.**

**Best Use of ElevenLabs**

ElevenLabs is integrated into Agent 4 (Recovery & Voice Approval Agent) to convert AI-generated recovery plans into clear, natural-language voice narrations, enabling operators to quickly understand incidents and recommended actions. This enhances accessibility and improves the human approval workflow before any recovery action is executed. Currently, the platform requires explicit human approval to ensure operational safety. As future work, OpsForge aims to support policy-driven automated recovery execution for low-risk incidents, while preserving human oversight for critical production operations.

**Best Use of MongoDB Atlas**

MongoDB Atlas powers Agent 5 (Knowledge Memory Agent) by serving as the centralized knowledge repository for historical incidents, root cause analyses, recovery actions, and deployment outcomes. It enables the agent to retrieve semantically similar past incidents, preserve organizational knowledge, and provide context-aware recommendations with confidence scoring. By continuously storing verified operational data, MongoDB Atlas allows OpsForge to improve future decision-making and reduce incident resolution time through intelligent historical learning.

**Best Use of Gemini API**

Agent 1 – Deployment Planning & Infrastructure Intelligence (Gemini API)

Gemini API powers Agent 1 by intelligently analyzing the selected GitHub repository to understand its structure, detect the application framework, identify dependencies, and validate deployment readiness. Based on this analysis, it recommends the optimal deployment configuration, highlights potential issues before deployment, and generates deployment insights that help reduce configuration errors and improve deployment success rates.

Agent 3 – Telemetry & Root Cause Analysis (Gemini API)

Gemini API is the reasoning engine behind Agent 3, where it analyzes deployment logs, runtime metrics, and telemetry data to identify the most probable root cause of production failures. It correlates multiple signals, explains the failure in natural language, assesses its impact, and generates structured recovery recommendations. This enables OpsForge to transform raw operational data into actionable insights, significantly accelerating incident diagnosis and reducing Mean Time to Recovery (MTTR).

**Open Innovation**

🌍How OpsForge Fits the Open Innovation Category

Open Innovation Approach

OpsForge is designed as an **open, extensible, and platform-agnostic AI-powered DevOps orchestration platform** that addresses a universal challenge faced by software teams worldwide: reducing deployment failures and accelerating incident recovery.

Rather than being built for a single organization or cloud provider, OpsForge is designed to integrate with existing developer ecosystems and cloud platforms, enabling organizations of any size to adopt intelligent operational workflows without replacing their current infrastructure.
Why OpsForge is an Open Innovation Solution

 🌐 Solves a Universal Industry Problem

Every organization deploying software faces similar operational challenges:

- Failed deployments
- Production downtime
- Slow incident response
- Fragmented monitoring tools
- Manual recovery procedures
- Loss of organizational knowledge

OpsForge addresses these challenges irrespective of industry, technology stack, or cloud provider.

---

🔗 Integrates with Existing Ecosystems

Instead of replacing existing DevOps tools, OpsForge works alongside them by integrating with services such as:

- GitHub
- GitHub Container Registry (GHCR)
- Railway
- MongoDB Atlas
- Gemini AI
- ElevenLabs
- Docker

Its modular architecture also allows future integration with platforms such as Kubernetes, Render, Fly.io, AWS, Azure, and Google Cloud.

---

🤖 AI-Powered Collaborative Intelligence

OpsForge combines multiple specialized AI agents that collaborate throughout the software deployment lifecycle:

- Deployment & Infrastructure Agent
- Telemetry & Root Cause Analysis Agent
- Recovery & Voice Approval Agent
- Knowledge Memory Agent

Each agent contributes specialized intelligence while sharing structured information with the others, enabling faster and more reliable operational decisions.

---

🧠 Continuous Organizational Learning

Unlike traditional deployment tools, OpsForge continuously learns from previous incidents.

The Knowledge Memory Agent stores deployment outcomes, root causes, recovery actions, and verification results to improve future recommendations. This transforms operational experience into reusable organizational knowledge rather than allowing it to remain isolated within individual engineers.

---

🔄 Extensible and Future-Ready

OpsForge follows a modular, provider-agnostic architecture.

Its deployment layer can support multiple infrastructure providers by implementing provider-specific adapters without changing the core orchestration logic. This makes the platform adaptable to evolving technologies and organizational needs.

---

## Innovation Impact

OpsForge moves beyond traditional CI/CD by introducing **AI-assisted operational intelligence**.

Instead of only automating deployments, it helps engineering teams:

- Detect failures faster
- Diagnose root causes intelligently
- Learn from historical incidents
- Recommend recovery strategies
- Execute verified recovery workflows with human approval
- Continuously improve future operational decisions

This creates a more resilient, explainable, and collaborative software delivery process.

Team **Voldemort.exe** -- [Pankaj Kumar Gupta](https://github.com/PankajGupta-dev), [Govind Raj Gupta](https://github.com/100376-govind), [Aritra Roy Choudhury](https://github.com/rio-ARC)

`2026-07-26`

---

### Akasha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/akasha-56ed) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ltsRoy/Akasha) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://akasha-emergencyweb.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/xw50IabaGB0) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Offline SOS Mesh Network with VectorDB and Gemma.

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Bluetooth Module](https://img.shields.io/badge/Bluetooth%20Module-333333?style=flat-square) ![ONNX](https://img.shields.io/badge/ONNX-333333?style=flat-square) ![Embedded Systems](https://img.shields.io/badge/Embedded%20Systems-333333?style=flat-square) ![Room Database](https://img.shields.io/badge/Room%20Database-333333?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-333333?style=flat-square) ![Google Direction API](https://img.shields.io/badge/Google%20Direction%20API-333333?style=flat-square)

**The problem it solves**

AKASHA addresses the critical communication gap during disasters and emergencies. When cellular networks and the internet fail, people in distress are left without reliable access to communication, emergency guidance, or nearby rescue resources. AKASHA enables offline communication and life-saving assistance in disaster zones, remote regions, and no-network environments through a resilient mesh network.

**Challenges we ran into**

Integrating Actian VectorAI Database – Setting up the vector database, designing the embedding pipeline, ensuring consistent similarity scores between the Android device and the Ground Station, and optimizing semantic search performance.

Reliable Calling Feature – Building a stable peer-to-peer calling system over Bluetooth mesh while dealing with bandwidth limitations, connection stability, and maintaining low latency in offline environments
.
Image Sharing over Mesh Network – Transferring images efficiently over Bluetooth LE mesh required chunking large files, handling packet loss, implementing reliable reassembly, and ensuring successful multi-hop delivery.

Offline-First Architecture – Making the app fully functional without internet by coordinating local AI models, BLE mesh networking, and seamless fallback between different operating modes.

Maintaining Performance on Mobile Devices – Balancing AI inference, networking, encryption, and battery usage while keeping the application responsive on Android devices.

**Accio Relevance - Build with Actian VectorAI Database**

Our solution uses Actian VectorAI Database to power semantic search over emergency knowledge and intelligently rank nearby hospitals, rescue centers, police stations, and other facilities based on both the user's situation and location. This enables accurate, context-aware recommendations even in disaster scenarios.

**Open Innovation**

AKASHA addresses a real-world problem that affects everyone—disaster response and emergency communication—rather than solving a challenge for a single organization. It combines offline AI, Bluetooth mesh networking, and vector search to create a resilient communication platform that can be adapted for governments, NGOs, rescue teams, and remote communities.

Team **DontStop** -- [Arkajit Chowdhury](https://github.com/aj69op), [Tamal Kumar Khan](https://github.com/tamal006), [Debasish Das](https://github.com/debasish-60099), [Soumyajit Roy](https://github.com/ltsroy)

`2026-07-26`

---

### Mavi-Linking
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mavilinking-ce47) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mayur51015/Mavi-Linking) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mavi-linking-mq7d.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Ibnem0mGs3g) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> One Profile. Unlimited Opportunities.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![mongoose](https://img.shields.io/badge/mongoose-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

MAVI Linking solves the problem of fragmented developer identities. Students and freshers often have skills, projects, coding profiles, certificates, and achievements spread across multiple platforms, making it difficult for recruiters and colleges to evaluate them effectively. The platform provides a unified developer profile where users can showcase their technical skills, projects, achievements, and professional growth. It simplifies recruitment, placement tracking, portfolio sharing, and skill assessment through a single intelligent and shareable profile with QR-based access.

**Challenges we ran into**

One of the biggest challenges was integrating multiple profile systems and creating a scalable role-based architecture for Users, Recruiters, and College/Teacher dashboards. Another challenge was managing secure authentication using JWT and connecting the frontend, backend, and MongoDB Atlas across different deployment platforms. During deployment, issues such as expired GitHub tokens, environment variable configuration, MongoDB connection setup, CORS restrictions, and Render deployment errors were encountered. These challenges were resolved through proper API configuration, secure environment management, database optimization, and deployment debugging.

[Mayur Khandare](https://github.com/Mayur51015)

`2026-06-13`

---

### InfraPilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/infrapilot-71e5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ishaan-jindal/InfraPilot) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://infrapilot.ishaanjindal.tech) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Own Your Infrastructure. Verify Its Security.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square)

**The problem it solves**

InfraPilot solves the critical gap between managed ease-of-use and self-hosted control by treating security as the foundation of the deployment pipeline rather than an afterthought.

### The Problem

1. Managed Platforms (e.g. Vercel, Netlify, Railway): They make shipping code incredibly simple, but keep developers in the dark regarding their application's security posture. They also lock projects into expensive, proprietary hosting ecosystems.
2. Self-Hosted Infrastructure (e.g. VPS, EC2, Home Labs): Deploying to your own servers grants full ownership and significantly lowers costs, but leaves complex security configuration entirely up to the developer. It is incredibly easy to accidentally expose default database ports, run containers with dangerous root privileges, or leave SSH authentication misconfigured.

### The Solution

InfraPilot integrates automated security intelligence directly into the build and deploy workflow. It simplifies and secures infrastructure management in three ways:

* Automatic Security Auditing: Developers connect a GitHub repository, and before any code is built or run, the system scans for leaked secrets (AWS, OpenAI, Stripe, Slack keys), committed env files, and Dockerfile misconfigurations. It computes a Security Score (0-100) to give immediate visibility into the build risk.
* Non-Root Isolation by Default: It generates secure Docker templates that run applications under unprivileged system accounts (such as a restricted node user or an appuser group), mitigating the risk of host-takeover exploits.
* Full Asset Cleanups: When deleting a deployment, the system leaves no trace behind. It stops and removes the container, deletes the dynamic Caddy proxy routes, wipes the built Docker image, and deletes the local repository files from the host to prevent VPS disk bloat.

By auditing configurations and exposing vulnerabilities before the code goes live, InfraPilot makes deploying to personal servers as simple as a PaaS, and far safer than manual scripting.

**Challenges we ran into**

While building InfraPilot, we encountered several challenging technical hurdles across container orchestration, reverse proxy management, and pipeline state synchronization:

### 1. Docker-in-Docker Constraints for User Builds
Initially, we attempted to package the entire backend system inside a Docker container. However, because InfraPilot builds and runs user application containers dynamically, this required a complex Docker-in-Docker (DinD) or socket-sharing setup. This introduced permission issues, slow build times, and instability on low-resource ARM64 VPS instances.
* **The Solution**: We re-architected the platform so that the FastAPI backend runs natively on the host VPS using PM2. This allowed the backend direct, native access to the host's Docker CLI and host resources, while keeping postgres, Caddy, and the Next.js frontend isolated in their own docker containers.

### 2. Caddy Reverse Proxy Dynamic Routing Conflicts
We integrated Caddy's admin API to dynamically add and remove subdomain reverse proxy routes as containers spun up and down. However, we ran into configuration conflicts when Caddy refused to permit duplicate route definitions or overlapping port 80/443 listener scopes across separate server blocks.
* **The Solution**: We shifted from creating independent servers to querying and appending route rules directly into Caddy's default HTTP server router instance (`srv0`). We also built database-backed checks to verify that subdomains are clean and fully removed before applying new routes.

### 3. Subdomain Unique Database Collisions
Because the database model enforces a unique constraint on subdomains, assigning the subdomain to the project name when the deployment was first queued caused immediate database blockages when running concurrent builds or redeploying the same project.
* **The Solution**: We implemented a two-step subdomain mapping system. When a build is initially queued, it receives a temporary, guaranteed-unique ID. Once the repository is cloned and the pipeline extracts the commit SHA, the system updates the subdomain to the final `[project-name]-[5-letter-commit-sha]` format, handling collisions by appending unique incrementing suffixes.

Team **Char Tabahi** -- Narayanan S, [Karan Gandhi](https://github.com/karangandhi-1712), Viral Patni, [Ishaan Jindal](https://github.com/SacredNightmare99)

`2026-06-14`

---

### GPU Vault
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gpu-vault-17ab) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DevDebpriyo/GPU-Vault) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1KWphzHE63A) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Institutional DePIN & Compute Settlement Layer

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square)

**The problem it solves**

# The Problem GPUVault Solves

The rapid growth of AI has created an unprecedented demand for GPU compute resources. At the same time, universities, enterprises, research institutions, and data centers own large fleets of expensive GPUs that often remain underutilized for significant periods of time.

Current compute marketplaces face several critical challenges:

* **Idle Infrastructure:** Millions of dollars worth of enterprise-grade GPUs remain unused, resulting in poor asset utilization and lost revenue opportunities.
* **Lack of Trustworthy Settlement:** Existing platforms often rely on centralized intermediaries, creating payment disputes and settlement risks between providers and consumers.
* **Compliance Limitations:** Most decentralized compute networks are designed for permissionless participation and lack institutional requirements such as KYC, access controls, geofencing, and workload restrictions.
* **Poor Auditability:** Organizations require transparent records for financial reporting, governance, and compliance, but many compute marketplaces lack immutable audit trails.
* **Complex Resource Discovery:** Finding the right compute provider based on cost, location, performance, and compliance requirements is often inefficient and time-consuming.

# What People Can Use GPUVault For

GPUVault creates a secure and compliant marketplace where compute resources become tradable digital assets.

## For Universities & Research Institutions

* Monetize unused GPU clusters during off-peak periods.
* Restrict access to approved researchers or academic partners.
* Generate additional revenue from existing infrastructure investments.
* Maintain full visibility into resource usage and earnings.

## For Enterprises

* Rent out idle AI infrastructure instead of leaving hardware unused.
* Create private or consortium-based compute marketplaces.
* Enforce internal security, compliance, and workload policies.
* Track utilization, uptime, and revenue across GPU fleets.

## For AI Teams & Startups

* Access institutional-grade GPU resources on demand.
* Secure compute through transparent blockchain-based settlement.
* Avoid long procurement cycles and expensive infrastructure purchases.
* Automatically discover the best compute providers based on cost, latency, and compliance requirements.

## For Consortiums & Organizations

* Launch branded internal compute exchanges.
* Share infrastructure across departments or partner organizations.
* Define role-based permissions for administrators, operators, and users.
* Maintain a verifiable audit trail for governance and reporting.

# How GPUVault Makes Existing Processes Easier and Safer

### Safer Payments

Smart contract escrow ensures that funds are only released after compute services have been successfully delivered, reducing counterparty risk for both providers and consumers.

### Transparent Operations

Every job request, pricing agreement, policy requirement, and settlement event is recorded on-chain, creating a permanent and tamper-resistant audit trail.

### Compliance by Design

Organizations can enforce KYC requirements, workload restrictions, geofencing rules, and access controls without sacrificing the benefits of decentralized infrastructure.

### Better Resource Utilization

Instead of allowing expensive GPUs to sit idle, organizations can continuously generate value from existing hardware investments.

### Intelligent Resource Matching

AI-driven routing automatically selects the most suitable compute provider based on factors such as price, availability, performance, compliance requirements, and latency.

# Impact

GPUVault transforms compute infrastructure from a static operational expense into a liquid, revenue-generating real-world asset. By combining institutional-grade controls with blockchain-based settlement on ADI Chain, it enables organizations to participate in the decentralized compute economy securely, transparently, and at scale.

**Challenges we ran into**

# Challenges We Ran Into

Building GPUVault involved combining decentralized infrastructure, institutional compliance requirements, AI-powered orchestration, and blockchain settlement into a single platform. Several technical and architectural challenges emerged during development.

## 1. Designing for Both DePIN and Institutional Compliance

Most DePIN platforms are designed around permissionless participation, while our target users (universities, enterprises, and research organizations) require strict access controls and compliance guarantees.

The challenge was finding a balance between decentralization and institutional requirements such as:

* KYC-gated access
* Role-based permissions
* Workload restrictions
* Geographic compliance requirements

We addressed this by introducing a policy-driven architecture where providers can define access rules and workload restrictions as metadata attached to compute resources. This allowed us to preserve marketplace flexibility while supporting enterprise-grade governance.

## 2. Modeling Compute as a Tradable Asset

Traditional cloud platforms treat compute as a service, but GPUVault needed to represent compute capacity as a measurable and settleable asset.

The difficulty was designing a system that could:

* Track available GPU capacity
* Record utilization over time
* Associate usage with financial settlement
* Maintain an immutable audit trail

We solved this by making ADI Chain the source of truth for settlement events while keeping operational workload data off-chain. This hybrid approach reduced blockchain overhead while preserving transparency and verifiability.

## 3. AI-Based Resource Matching

A key goal was enabling intelligent routing between compute consumers and providers.

The challenge was that matching decisions are rarely based on a single factor. A request may require balancing:

* Price
* Latency
* Availability
* Compliance requirements
* Provider restrictions

To overcome this, we implemented an AI-assisted brokerage layer that evaluates multiple constraints simultaneously and recommends the most suitable provider rather than simply choosing the cheapest option.

## 4. Workflow Builder Complexity

The visual automation system was inspired by tools like Zapier, but adapting that concept to decentralized compute infrastructure introduced additional complexity.

Users needed to create workflows such as:

> "If GPU prices fall below a threshold, automatically deploy a training cluster."

Building a flexible workflow engine while keeping the user experience intuitive required several iterations of the node structure, state management, and execution flow before arriving at a design that felt both powerful and approachable.

## 5. Integrating Multiple Technologies

GPUVault combines:

* Next.js
* TypeScript
* ADI Chain
* Vercel AI SDK
* React Flow
* 0G Storage

Each component solved a different problem, but integrating them into a cohesive architecture required careful coordination between data flow, blockchain interactions, AI reasoning, and frontend state management.

We overcame this by clearly separating responsibilities between the settlement layer, orchestration layer, AI layer, and storage layer, which reduced coupling and simplified debugging.

# Key Takeaway

The biggest challenge was not a single bug, but designing a system that could simultaneously satisfy the requirements of decentralized infrastructure, institutional compliance, and intelligent automation. Solving this required multiple architectural iterations and a strong separation of concerns between blockchain settlement, AI orchestration, and compute resource management.

**Blockchain**

## How GPUVault Fits the Blockchain Category

GPUVault is not simply a cloud-computing marketplace with crypto payments. Blockchain serves as the core trust, settlement, and audit layer of the platform.

### Blockchain-Powered Settlement

Every compute transaction is settled on ADI Chain through smart contracts. Payments are locked in escrow and automatically released once compute services are successfully delivered and verified, removing the need for centralized intermediaries.

### Real-World Asset (RWA) Integration

GPUVault transforms underutilized institutional GPU infrastructure into productive digital assets. Enterprise and university GPUs become tradable compute resources whose availability, utilization, and revenue generation can be transparently tracked.

### Decentralized Physical Infrastructure Network (DePIN)

The platform connects real-world hardware providers with global compute demand through a decentralized marketplace. ADI Chain provides the trust layer that coordinates resource allocation, service agreements, and economic incentives between participants.

### Immutable Audit Trail

Job requests, pricing agreements, workload policies, SLA records, and settlement events are recorded on-chain, creating a transparent and tamper-proof history suitable for institutional compliance and reporting requirements.

### Smart Contract Automation

Smart contracts automate key marketplace functions, including:
- Escrow and payment settlement
- Service verification
- SLA enforcement
- Provider reputation tracking
- Marketplace governance logic

### Why It Belongs in the Blockchain Track

GPUVault combines multiple blockchain-native concepts:

- **DePIN** – Monetizing real-world GPU infrastructure through decentralized coordination.
- **RWA** – Treating enterprise compute capacity as a real-world asset class.
- **Smart Contracts** – Automating trust, settlement, and compliance workflows.
- **On-Chain Transparency** – Creating verifiable records of compute usage and payments.

By using ADI Chain as the settlement and verification layer, GPUVault enables institutions to participate in decentralized infrastructure markets while maintaining the transparency, security, and auditability required for enterprise adoption.

**Web Development**

## How GPUVault Fits the Web Development Category

GPUVault is a full-stack web application that enables institutions to manage, monetize, and automate GPU infrastructure through a modern browser-based platform.

### Key Web Development Features

* Interactive dashboards for monitoring GPU utilization, workloads, and revenue.
* Visual workflow builder for automating compute operations.
* Role-based access control for administrators, operators, and users.
* AI-powered resource matching and deployment recommendations.
* Real-time management of compute assets through an intuitive web interface.

### Why It Belongs in the Web Development Track

GPUVault combines modern frontend development, backend orchestration, AI integration, and enterprise-grade user experiences into a single full-stack web platform, making complex infrastructure management accessible through the browser.

**Open Innovation**

## How GPUVault Fits the Open Innovation Category

GPUVault addresses a growing global challenge: the underutilization of institutional GPU infrastructure amid rapidly increasing demand for AI compute.

By combining DePIN, blockchain-based settlement, AI-driven resource allocation, and enterprise compliance controls, GPUVault creates a new model for connecting idle compute resources with organizations that need them.

The platform is designed to serve a wide range of stakeholders—including universities, enterprises, researchers, startups, and AI developers—making advanced compute infrastructure more accessible while generating value from existing assets.

Through its innovative combination of web technologies, AI, and blockchain, GPUVault demonstrates a novel approach to solving real-world infrastructure and resource allocation challenges.

Team **AVENGERS** -- [Nilarpan Jana](https://github.com/nilarpan7), [Subhajeet Gorai](https://github.com/Subho4531), [Samrat Natta](https://github.com/Samrat25), [Debpriyo Ghosal](https://github.com/DevDebpriyo)

`2026-05-31`

---

### vajra
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vajra-ec81) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/swaraj-shubh/nmit) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=7ghpbMepHdw) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> A Secure LLM Proxy Gateway Against PromptInjection

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MERN stack](https://img.shields.io/badge/MERN%20stack-333333?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

The problem:-
Prompt injection is now one of the most critical vulnerabilities in AI systems and is recognized in the OWASP LLM Top 10. Real-world challenges such as Pangea’s AI Escape Room and Microsoft’s LLMail-Inject competition have shown that even well-configured models can be compromised through adversarial prompt engineering.
These incidents expose a fundamental weakness: most production AI deployments rely on single-layer defenses like static system prompts or basic filtering, approaches that fail against evolving attack strategies.


The usage:-
1.Enterprise->Deploy LLMs in regulated environments (finance, healthcare, legal) with audit-ready security controls baked in, not bolted on.

2.AI Agents->Protect autonomous agents from adversarial instruction hijacking ,the exact attack class highlighted in OWASP LLM Top 10 and Microsoft's LLMail-Inject competition.

3.Zero Friction Adoption->Any team calling an LLM API gets full-stack injection defense by simply routing through VAJRA. No prompt rewrites. No model fine-tuning. No infrastructure redesign.

**Challenges we ran into**

Challenges we ran into:-
1. Detecting prompt injection beyond simple keywords.
2. Handling continuously evolving jailbreak techniques.
3. Integrating RAG chatbot with our proxy server.

How did we solve?:-
1. Solved by using semantic embeddings + similarity search instead of only regex filtering.
2. Solved by logging blocked prompts and updating the attack corpus using vector similarity clustering.
3. Solved by routing both user queries and the prompt goes to VAJRA before sending it to LLM.

**Blockchain / Cybersecurity**

1. Our project directly addresses one of the biggest modern AI security threats : "Prompt Injection" which is listed in OWASP LLM top 10 vulnerabilities.

2. It acts as a security gateway/firewall for AI systems.

3. It applies core cybersec principles such as zero trust architecture, threat detection, secure sandboxing etc.

**Google Gemini**

Our project uses Gemini in multiple critical stages of the pipeline. After every client request passes through VAJRA’s sanitization and semantic filtering layers, Gemini is used as an intent-aware classifier to analyze ambiguous or adversarial prompts that traditional rule-based systems cannot reliably detect.
VAJRA then securely forwards validated prompts to the Gemini API for final response generation, making Gemini the primary reasoning engine behind the application while VAJRA provides the surrounding security and governance infrastructure.

How Gemini is used:
1.Core LLM Backend — all AI inference goes through Gemini
2.Intent Classifier (L2) — Gemini classifies user intent as safe/risky/review-needed


Why it matters:
1.Adds enterprise-grade security without changing client code
2.Detects jailbreaks, PII leaks, secrets in outputs before returning to user
3.Real-time audit logging + live dashboard


Instead of creating another standalone chatbot, we are solving one of the biggest adoption barriers for advanced LLMs like Gemini: prompt injection, unsafe tool execution, and sensitive data leakage.
This directly aligns with the Gemini track because we are building a real-world system that enhances the safe deployment of Gemini-powered applications in enterprise environments.

Team **git-push-win** -- [Tanmay Srivastava](https://github.com/tanmay-srivastav4), [Shubham Verma](https://github.com/swaraj-shubh), [Devansh Pateriya](https://github.com/dvshpat), [Keshav Lath](https://github.com/Klath123)

`2026-05-10`

---

### echo_
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/echo-9177) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/siddhi1229/echo-nitte) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1SxrhEnXqydtAG1iP0BrE5qXF8OhOWUNK/view) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Predict the worst.Ship the fix.Protect the uptime.

![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Slack API](https://img.shields.io/badge/Slack%20API-333333?style=flat-square) ![Kubernetes](https://img.shields.io/badge/Kubernetes-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Jaeger](https://img.shields.io/badge/Jaeger-333333?style=flat-square)

**The problem it solves**

# What is Echo?

Echo is an **autonomous Site Reliability Engineering (SRE) agent** that predicts microservice failures *before* they occur  and resolves them automatically, without waking up your on-call engineer at 3 AM.

---

## The Problem with Traditional SRE

Modern distributed systems don’t fail in isolation  they fail in cascades. A single degraded service  high latency can silently ripple through the dependency graph until the entire platform collapses. By the time alerts trigger, the damage is already done.

Traditional observability tools tell you **what broke**.  
Echo tells you **what’s about to break**.

---

## What Echo Makes Possible

| Task | Without Echo | With Echo |
|------|-------------|-----------|
| Detecting cascade failures | Post-incident analysis | Predicted 2–5 minutes in advance |
| Alert response | On-call engineer woken at 3 AM | Fully autonomous remediation |
| Root cause tracing | Manual log-diving | Instant cascade path visibility |
| Incident documentation | Manual Notion/Slack updates | Automatic cross-channel updates |
| Chaos engineering | Requires separate tooling | Built-in fault injection lab |

---

## Who Uses It

- **Platform/SRE teams** that require sub-2-second failure prediction across complex microservice graphs  
- **Startups** without dedicated NOC teams, needing autonomous reliability coverage  
- **Hackathon teams** deploying on Kubernetes who want zero-downtime demos  
- **Engineering managers** seeking MTTR visibility without constant dashboard monitoring  

---

## The Full Loop

1. **Ingest** : Every 2 seconds, collect latency, error rates, CPU usage, and RPS per service node  
2. **Predict** : A GNN encodes system topology while an LSTM models temporal patterns → outputs calibrated failure probability + cascade path  
3. **Plan** : A policy engine maps severity levels to concrete actions (scale up, circuit break, alert)  
4. **Execute** : The action executor applies decisions (or logs them in DRY-RUN mode) and broadcasts updates to all dashboard clients via WebSocket  
5. **Notify** : Slack, Notion, and GitHub Issues are updated automatically

**Challenges we ran into**

**Challenges & Engineering Hurdles**

1.**Solving Circular Import Deadlocks**

**Problem:** The Orchestrator singleton shared dependencies with the policy_engine and action_executor, creating a classic circular import crash on server startup.
**The Fix:** I restructured the module boundaries by moving type annotations behind TYPE_CHECKING guards and implemented dependency injection. The action_executor now receives a callback hook instead of importing the orchestrator directly, decoupling the architecture.

2. **Maintaining the Strict 2s Inference Tick**

**Problem**:The ML pipeline (GCN + LSTM) occasionally exceeded the 2-second tick window due to PyTorch’s JIT overhead, leading to "drifting" timestamps and stale telemetry.
**The Fix:** I developed a dedicated inference_wrapper.py using thread-safe tensor cloning. By offloading inference to an asyncio.run_in_executor thread pool, the main loop remains non-blocking. If a tick is missed, the system intelligently uses the previous prediction and marks confidence as degraded.

3.**Optimizing WebSocket Fan-out**

**Problem**: Broadcasting the full graph state to 20+ simultaneous clients caused JSON serialization lag, slowing down the live dashboard.
**The Fix**: I implemented pre-serialization. The tick payload is serialized exactly once using orjson, and the resulting bytes are broadcast via asyncio.gather. This reduced per-client overhead by ~85%.


4.**Resolving Vite HMR Conflicts**

**Problem**: Vite’s Hot Module Replacement (HMR) and our API used the same port, causing the frontend to accidentally try and parse HMR signals as Echo telemetry data.
**The Fix**: I isolated the communication channels by explicitly defining a VITE_WS_URL and adding URL validation guards in the useWebSocket hook to silently drop any traffic not originating from our /ws endpoint.

**AI & ML**

## AI/ML at the Core, Not a Wrapper

Echo doesn't call an LLM and display its response. The AI **is** the product.
Every remediation decision Echo takes is driven by a custom-trained ML pipeline
running on live infrastructure telemetry, end-to-end.

---

### The ML Architecture

#### 1. Graph Neural Network (GNN) : Structural Reasoning
- Models the **microservice dependency graph** as a graph data structure
- Each node = a service (auth, orders, payments, ledger)
- Each edge = a live call relationship with metrics (error rate, latency, RPS)
- The GNN learns **which topological patterns precede failures**
  e.g. "when auth latency spikes AND orders error rate crosses 5%, payments will fail within 3 minutes"

#### 2. LSTM (Long Short-Term Memory) : Temporal Reasoning  
- Sequences the last N graph snapshots (2-second intervals) into a time window
- Captures **drift patterns** that a single snapshot can't detect
  e.g. a slowly climbing CPU that looks fine at T=0 but is catastrophic at T=20
- Prevents false positives from transient spikes

#### 3. Ensemble Output
- GNN + LSTM outputs are combined into a **single calibrated failure probability** (0–1)
- Includes a **cascade path** : the predicted propagation order through the graph
- Includes a **time-to-failure estimate** in minutes
- Confidence score degrades automatically when telemetry is stale (honest uncertainty)

#### 4. Groq LLM Integration : Incident Summarization
- After the model fires an action plan, Groq LLM generates a **plain-English incident summary**
- Uses **rolling memory** (last 5 ticks) for contextual, non-repetitive summaries
- Sent to Slack / Notion so on-call engineers understand *why* the system acted

---

### Why This is Real ML (not a chatbot with a dashboard)

| Criterion | Echo |
|-----------|------|
| Custom model trained on domain data | ✅ Trained on 1,000 synthetic fault scenarios |
| Model runs inference at production frequency | ✅ Every 2 seconds, <50ms latency |
| Model output drives autonomous decisions | ✅ Directly controls scale-up and circuit-breaker actions |
| Uncertainty quantification | ✅ Confidence degradation when telemetry is stale |
| LLM for human-in-the-loop explanation | ✅ Groq rolling-memory summaries |
| Novel application of GNN to SRE | ✅ Applying graph ML to microservice observability |

---

### The Novel ML Contribution

Most SRE tooling uses **threshold alerts** (if latency > 500ms, page someone).
Echo uses **learned structural + temporal patterns** to predict failures that
*haven't crossed any threshold yet* : the quiet precursors that experienced
SREs recognize but monitoring tools miss entirely.

This is the core ML hypothesis: **graph topology encodes failure propagation
paths, and temporal sequences of graph states are predictive of cascade events.**

Team **Lil Kids** -- [Sarva Dubey](https://github.com/HESleagacy), [siddhi agarwal](https://github.com/siddhi1229), [Ananya Gupta](https://github.com/Ananya44444), [Abhijeet Yadav](https://github.com/abjt01)

`2026-05-10`

---

### CodeSpotlight
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codespotlight-7df0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hmcommits/CodeSpotlight) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://codespotlight-hm.web.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BZO2LhEN5AU) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The Developer Proof-Of-Work Platform

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square)

**Challenges we ran into**

### 🧩 The Challenge: AI Non-Determinism & Frontend Crashes

One of the most complex hurdles we faced was reliably rendering the AI-generated architecture diagrams without crashing the frontend. 

We integrated **Gemini 2.5 Flash** to analyze repositories and output `Mermaid.js` flowchart syntax. However, Large Language Models are inherently non-deterministic. Even with strict prompt engineering, the AI would occasionally return slightly invalid syntax, such as:
*   Injecting unexpected Markdown code fences (e.g., ` ```mermaid `).
*   Using parentheses inside node definitions.

When our Flutter frontend attempted to parse these edge cases inside the iframe, the Mermaid renderer would throw a fatal syntax error, causing the UI component to crash completely.

### 🛠️ The Solution: A Robust Middleware Sanitizer

We quickly realized that prompt engineering alone wasn't enough to guarantee stability. To solve this, we built a **regex-based middleware sanitizer** directly into our Node.js backend. 

Before saving any AI output to MongoDB, this custom data pipeline intercepts the response and performs aggressive cleaning:
1.  **Strips rogue markdown fences** to ensure raw text execution.
2.  **Enforces correct graph directives** (e.g., defaulting to `graph TD`).
3.  **Automatically converts invalid characters** (like nested parentheses) into safe, quoted string labels using Regex.

**The Impact:** By implementing this middle-layer sanitizer, we transformed an unpredictable AI output into a **100% deterministic, crash-proof data source**, allowing our UI to render complex architecture diagrams flawlessly every single time.

**The problem it solves**

# CodeSpotlight ✨

**The Developer Proof-of-Work Platform**
*Transform any public GitHub repository into a beautifully rendered, AI-powered case study.*

**Live Application / Deployment Link:** https://codespotlight-hm.web.app

**Watch Demo:** https://youtu.be/BZO2LhEN5AU



---

## 📖 Overview

Many developers build great projects but lose them in scattered GitHub repositories. **CodeSpotlight** is a centralized showcase directory where developers can host their deployed projects, generate AI-powered technical deep-dives, and present their work to recruiters through a polished, read-only portfolio interface.

Paste a GitHub URL, and CodeSpotlight's integration with Gemini AI and the GitHub API instantly generates architecture diagrams, commit heatmaps, language visualizations, and a fully formatted Markdown README.

---

## ✨ Features

- **🤖 AI Technical Deep Dive:** Gemini 2.5 Flash generates a comprehensive case study explaining the project's purpose, the hardest problems solved, and the architectural decisions made.
- **📄 Auto-Generated READMEs:** Export your AI-generated project analysis to beautiful, fully-formatted Markdown, ready to be pushed directly to your GitHub repository.
- **🏗️ Architecture Diagrams:** Auto-generated Mermaid.js flowcharts visualize components, data flow, and system interactions in a secure sandboxed iframe.
- **🔥 Commit Heatmap:** A real 52-week × 7-day contribution grid pulled live from GitHub to showcase consistent effort.
- **🌍 Public Discoverability:** A global "Discover" feed where developers can browse top projects filtered by tech stack (MERN, Web3, AI, etc.).
- **🔐 Secure Portfolio Sharing:** Share a read-only link to your portfolio with recruiters without exposing edit/delete controls. Includes customizable social links (LinkedIn, Twitter, Portfolio).

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** Flutter Web (Canvas Kit)
- **Routing:** `go_router` for shareable deep links
- **Markdown:** `flutter_markdown`
- **Hosting:** Firebase Hosting

### Backend
- **Framework:** Node.js + Express
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** MongoDB Atlas (Mongoose)
- **AI Integration:** `@google/generative-ai` (Gemini 2.5 Flash)
- **Hosting:** Render.com

---

## 🌐 Deployment Information

This project is fully deployed and accessible live for the hackathon judging process:
- **Frontend (Flutter Web):** Deployed on **Firebase Hosting**
- **Backend (Node.js/Express):** Deployed on **Render.com**
- **Database (MongoDB):** Hosted on **MongoDB Atlas**
- **Live URL:** https://codespotlight-hm.web.app

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.
### Prerequisites

- [Node.js](https://nodejs.org/en/) (v18 or higher)
- [Flutter SDK](https://docs.flutter.dev/get-started/install) (3.x with Web target enabled)
- A [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) cluster URI
- A Google [Gemini API Key](https://aistudio.google.com/)
- A [GitHub Personal Access Token (PAT)](https://github.com/settings/tokens)

### 1. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Copy the environment template
cp .env.example .env
```

**Configure Environment Variables (`backend/.env`):**
| Variable | Description |
|---|---|
| `PORT` | API port (default: `3000`) |
| `MONGODB_URI` | MongoDB Atlas connection string |
| `JWT_SECRET` | Secret key for signing authentication tokens |
| `GITHUB_PAT` | GitHub Personal Access Token (public repo scope) |
| `GEMINI_API_KEY` | Google AI Studio key |
| `CLIENT_URL` | Frontend URL for CORS (e.g., `http://localhost:52870`) |

```bash
# Install dependencies
npm install

# Start the development server
npm run dev
```

### 2. Frontend Setup

```bash
# Open a new terminal and navigate to the frontend directory
cd frontend

# Get dependencies
flutter pub get

# Run the Flutter web app (Chrome)
flutter run -d chrome
```
*Note: The frontend is configured to communicate with `http://localhost:3000/api` by default.*

---

## 📂 Project Structure
```text
CodeSpotlight/
├── backend/
│   ├── src/
│   │   ├── controllers/      # Route logic
│   │   ├── models/           # Mongoose schemas (User, Project)
│   │   ├── routes/           # Express routes (auth.js, projects.js)
│   │   └── services/         # Integrations (geminiService.js, githubService.js)
│   └── index.js              # Server entry point
│
├── frontend/
│   ├── lib/
│   │   ├── models/           # Dart data models
│   │   ├── pages/            # UI Screens (Dashboard, Discover, Detail)
│   │   ├── services/         # API & Auth clients
│   │   ├── theme/            # Global AppTheme and styling
│   │   └── widgets/          # Reusable UI (Cards, Heatmap, Mermaid)
│   └── web/                  # Web-specific assets (index.html)
│
└── deploy.sh                 # Deployment automation script
```

Harsh Mayekar

`2026-05-05`

---

### Orvex
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/orvex-ee43) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIRACULOUS65/Orvex) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/dnqY6lMGYPQ) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Autonomous Intelligent AI Payment Agent SDK

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square) ![Qwen + Groq + NVIDIA + Gemini](https://img.shields.io/badge/Qwen%20+%20Groq%20+%20NVIDIA%20+%20Gemini-333333?style=flat-square) ![Pydantic + RAG + Embeddings](https://img.shields.io/badge/Pydantic%20+%20RAG%20+%20Embeddings-333333?style=flat-square) ![Node.js + TypeScript + Fastify](https://img.shields.io/badge/Node.js%20+%20TypeScript%20+%20Fastify-333333?style=flat-square) ![PostgreSQL + Supabase + ChromaDB/Pinecone](https://img.shields.io/badge/PostgreSQL%20+%20Supabase%20+%20ChromaDB/Pinecone-333333?style=flat-square) ![Deterministic Policy Engine](https://img.shields.io/badge/Deterministic%20Policy%20Engine-333333?style=flat-square)

Team **Team Quantum Glitch** -- [Devargho Chakraborty](https://github.com/Boredooms), [Sushovan Ghosh](https://github.com/MIRACULOUS65), [Suman Ghosh](https://github.com/Suman-Ghosh-2005), [Suparna Panda](https://github.com/suparna39)

`2026-09-12`

---

### Spydra
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spydra-ee03) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SRIKRISH-S/Spydra) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://spydra-hackathon.onrender.com/ui) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/5Id70xjKigg) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The runtime security web that watch your AI agent

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**Challenges we ran into**

Building a universal interception layer for AI agents came with several intense technical hurdles:

1. **Transparent Interception:** We needed to intercept underlying Python subprocesses and HTTP requests without requiring developers to completely rewrite their existing agent code. We had to build a robust hooking mechanism that works seamlessly with standard libraries like `requests`, `httpx`, and `subprocess`.
2. **Provenance-Aware Authority:** The hardest challenge was tracing the *origin* of data. We had to build a system that could accurately differentiate between a trusted, hardcoded command and an untrusted string fetched from a malicious web search, and then evaluate that context against our policy engine in milliseconds.
3. **Low-Latency Dashboarding:** Agents generate a massive amount of telemetry. We had to ensure that streaming this data to our React dashboard (for the live Sankey flows and event streams) did not create a bottleneck or slow down the agent's actual execution time.

**The problem it solves**

### The Blind Spot in AI Agents
Right now, developers are rapidly integrating AI agents—like custom LangChain workflows, Cursor, and Model Context Protocol (MCP) servers—into their infrastructure. We give these agents the power to make tool calls, execute shell commands, and send HTTP requests. 

However, this creates a massive security blind spot:
1. **Zero Visibility:** There is no centralized inventory of what an agent can touch or see.
2. **No Guardrails:** There is no enforcement mechanism when a new capability is quietly added.
3. **The Ghostjacking Threat:** Untrusted content (like a malicious webpage or a prompt injection) can hijack an agent, tricking it into exercising its legitimate privileges maliciously.

### The Solution: Spydra
**Spydra is a Runtime Governance Engine for AI agents.** 
Think of it as a security mesh. Every tool call, HTTP request, or shell command is a strand. Spydra sits at the center, intercepting every action *before* execution. 

Instead of just asking, *"Is this agent allowed to use this tool?"* 
Spydra asks, *"Was the information that **caused** this action actually authorized to exercise that power?"*

It evaluates actions against a 4-tier policy engine (**Block, Warn, Monitor, Allow**), tracks token budgets, and provides security teams with a real-time visual dashboard of every agent's actions, ensuring that rogue AI actions never reach production.

Team **GloInnov** -- [Akshaya I](https://github.com/akshayaindirasekar), [SRIKRISHNA S](https://github.com/SRIKRISH-S), [Vetha Narayanan G](https://github.com/GVethaNarayanan)

`2026-09-02`

---

### Hot Seat
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hot-seat-092e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hotseatai.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI that grills you before they do.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![OAuth](https://img.shields.io/badge/OAuth-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square)

**The problem it solves**

The problem it solves

Job seekers preparing for interviews get generic mock questions with no real feedback on how they answered — and no easy way to know if their resume actually matches a specific job description before applying. Hot Seat solves both:

- AI-generated mock interviews tailored to the specific role and domain (software engineering — including VLSI/embedded sub-tracks — finance, consulting, sales, marketing), not generic question banks.
- Answer evaluation with adaptive follow-ups — when an answer scores low, the system automatically asks a targeted follow-up instead of just moving on, mimicking a real interviewer probing a weak spot.
- Resume-vs-Job-Description gap analysis — parses a JD into structured requirements, matches them against the resume with evidence-backed scoring, and gives specific, actionable rewrite recommendations instead of a vague "add more keywords."
- In-browser code execution (C/C++/Java/Python/JavaScript/Verilog) for technical interview rounds, so candidates can solve and run code without leaving the platform.

**Challenges we ran into**

One subtle bug took real digging: users who improved their resume based on our recommendations and re-uploaded it against the same job description would sometimes get a lower match score than before — even though the resume had objectively gotten better. Traced it to LLM sampling non-determinism: the job-description-parsing step re-ran through Gemini on every analysis with no temperature control, so the same JD text could get parsed into a different number of requirements each time, and that noise leaked into the final score. Fixed it two ways — pinned temperature=0.0 across every structuring/evaluation call for reproducibility, and added a hash-based cache so re-analyzing the exact same JD reuses the previously-parsed result instead of re-deriving it with fresh sampling variance.

Also had to design around a real security risk: the code-execution feature runs submitted code as a subprocess directly in the backend container. A naive implementation would let user-submitted code read back GEMINI_API_KEYS, database credentials, and other secrets from the process environment — solved with an explicit environment-variable allowlist so subprocesses only see what they strictly need to run.

Harshal Shah

`2026-08-20`

---

### Anori
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anori-763b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sreenathmmenon/anori) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://anori-studio-production.up.railway.app) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> From a web of pages to a web of capabilities

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square)

**What is the deployed URL for this project?**

https://anori-studio-production.up.railway.app

**How you are solving it?**

We approached Anori as an application-architecture problem, not an automation problem.

At its core is a small model:

**Resource + Capability Contract + Policy → Affordance**

A Resource represents something meaningful such as an Order, Room, Product, Trip or Character.

A Capability Contract describes a meaningful action, including its inputs, preconditions, effects, state changes, guarantees, approval requirements and verification.

A Policy defines who may perform that action, under what authority, delegation, limits and context.

An Affordance is the live result:

**What can this specific human or agent actually do right now?**

For example:

`reserve_plan` → available
`purchase_plan` → human approval required above $500
`schedule_assembly` → unavailable until an order exists
`cancel_order` → disappears after dispatch

When state, identity, delegation or policy changes, the human interface and WebMCP tool surface change together because both come from the same application truth.

This is how Anori differs from simply exposing tools through WebMCP.

**WebMCP gives agents a structured way to call website capabilities. Anori defines what those capabilities mean, when they are valid, who may use them, what they change and whether they succeeded.**

Execution follows one authoritative path:

**derive → propose → revalidate → authorize → approve → execute → verify → receipt → notify**

The AI can reason about what to do, but it cannot declare itself authorized, bypass policy, mutate protected state or claim success. Anori owns those decisions.

We also built an **AI Application Compiler** for existing products.

Instead of forcing a company to rewrite its application, the compiler analyzes existing pages, APIs, OpenAPI definitions, workflows and business rules. AI proposes Resources, Capability Contracts, Policies, state transitions and effects, while retaining evidence and uncertainty.

Ambiguous rules require review. High-consequence actions cannot silently become publishable because a model inferred them.

We then proved the platform across very different products.

**Mysa Living** turns “design my room under this budget” into a geometry-valid, inventory-aware, approval-aware outcome. We deliberately make the selected desk go out of stock; the agent receives new affordances, replans, chooses an alternative, preserves the budget and continues.

**FlowShop** demonstrates buyer and seller agents negotiating under price-band and approval policies.

**Roamly** treats a trip as a living outcome that can heal after cancellations, weather or price changes.

**Inkling Worlds** turns a sketch and description into a playable semantic world, proving Anori is not just a commerce or workflow framework.

The same foundation powers all of them, while each remains a completely different customer experience.

The system we built includes the semantic kernel, authoritative runtime, dynamic WebMCP projection, AI Application Compiler, Anori Studio, SDK, delegated authority, resumable approvals, verification, semantic receipts, observability and evaluation infrastructure.

**The goal is not to make AI better at operating websites. It is to make applications themselves natively understandable and operable by humans and intelligence.**

Prior work disclosure: Inkling originated from an earlier creative experiment around turning drawings into playable experiences. Anori’s platform architecture, runtime, compiler, Studio, WebMCP integration and the implementation connecting these products were built for this project.

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/4fa184df-0826-43c7-b99b-a08f27338f18.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/4a4062c6-dc1e-43f7-883d-c5e470efc0b4.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/a30d6f1b-79aa-4ba0-bf61-644064188917.png)

**How Did You Use Claude?**

Claude is central to Anori in two ways:

**Claude helped build Anori, and Claude can operate applications built with Anori.**

During development, we used Claude Code as a multi-agent engineering environment rather than simple autocomplete.

We created specialist agents for architecture, the semantic runtime, AI Application Compiler, WebMCP, Studio, product experiences, QA, visual review and adversarial testing. Independent work ran in isolated worktrees, while a principal agent remained responsible for integration and architectural coherence.

This process found real problems rather than simply generating code.

Claude agents discovered an approval bug that could have turned a denied action into an approvable one, an exported runtime helper that could have bypassed the normal authorization lifecycle, tests that were passing for the wrong semantic reason, Compiler/Studio integration drift, unreachable product journeys and misleading UI states.

Those issues were fixed at the architectural layer and protected with regression tests.

Claude is also the runtime intelligence.

We verified the real Anthropic path end-to-end.

Claude interpreted natural-language intent, received only the current affordances exposed by Anori, selected a valid capability and attempted it through Anori’s normal runtime.

When a $1,590 purchase crossed a $500 approval threshold, Claude could not simply proceed. Anori suspended execution until a human approved it, then executed the action and verified the resulting state.

We then changed the world underneath the agent by exhausting inventory for the selected product.

The original plan became invalid.

Anori recalculated the available affordances. Claude received the new possibilities, rejected an option that violated the budget, selected a different valid product and replanned toward the outcome.

**This was not a scripted AI demo. The application state changed, the available capabilities changed, Claude changed its plan, and Anori continued to enforce the rules.**

The live Claude run also exposed a real issue in our structured model adapter: the model was being asked for a “required shape” without receiving the full schema. Claude returned semantically correct data in a near-miss structure and validation failed. We fixed the shared adapter to provide the schema explicitly, after which the real Anthropic path succeeded.

That separation is fundamental:

**Claude understands intent, reasons, plans and replans.**

**Anori owns state, authority, policy, approvals, effects, execution and verification.**

AI is becoming both a **software builder** and a **software user**.

Claude Code represents one side of that shift. Claude operating Anori applications represents the other.

**Anori is the application layer between those two worlds: something intelligence can build with, and something intelligence can safely act on.**

**What is the problem your project solves?**

The web was built for humans to operate software through pages, buttons, forms and navigation. AI agents are now becoming capable enough to act on our behalf, but most applications were never designed for them.

Computer-use agents can inspect screens and click through existing websites. That is useful, but it still adapts AI to software designed for humans.

We are asking a more fundamental question:

**What should applications become when AI is a first-class user of software?**

This shift is already beginning. WebMCP is exploring a web where sites expose structured capabilities directly to agents instead of forcing them to infer every action from the interface.

But exposing a tool is not enough. If an agent sees `purchase`, `bookStay` or `cancelOrder`, it still needs authoritative answers:

Who may perform it?
In what state is it valid?
What will change?
How much may the agent spend?
Does a human need to approve?
Can it be reversed?
How is success verified?

That is what we are building with **Anori**.

**Anori is an open application platform for the Agentic Web.**

Our thesis:

**From a web of pages to a web of capabilities.**

Anori gives applications an explicit model of:

**Resources** — what exists
**Capability Contracts** — what can happen and what it changes
**Policies** — who may do it and under what limits
**Affordances** — what this particular human or agent can actually do right now

Websites do not disappear. Humans still get beautiful, branded experiences. But underneath them is one application truth that can also power mobile experiences, WebMCP tools, AI agents, approvals and future interfaces.

Instead of manually operating a furniture site, a user can say:

**“Design a two-person home office under my budget. Everything must fit, arrive this weekend, and ask me before purchasing.”**

The AI reasons about how to achieve the goal. Anori decides what is actually possible and authorized.

The same model can support commerce, travel, SaaS, support and even creative software.

We do not think the future of the web is simply AI clicking faster.

We think applications themselves will become legible to intelligence.

Search helped create an **information graph** of the web: what exists and what we know.

Agents will increasingly need a **Possibility Graph**: what can actually be done, by whom, under what constraints, right now.

**The web learned how to publish information. We believe its next layer will publish trustworthy possibilities. Anori is infrastructure for that future.**

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/ccc36b3b-a0db-416f-9949-676d4c41d736.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/54e7eab5-f2cc-48bf-b83c-daaef11a6078.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/298ef413-1373-4191-80a1-af87e3da820a.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/a382f83d-9874-449b-ac94-bd78cee3de14.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/7046f383-a3b5-4eb8-b5c9-408aa3021b78.png)

![image](https://assets.devfolio.co/content/83eea038367744b69205e3c1d67ed3af/89653282-0e9d-4573-b18d-8d7ad9accfe6.png)

[Sreenath Menon](https://github.com/sreenathmmenon)

`2026-08-08`

---

### new
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/new-ab8d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AMMANKUMARD100/new) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Quite OK Image Format"

![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Cargo](https://img.shields.io/badge/Cargo-333333?style=flat-square) ![Png crate](https://img.shields.io/badge/Png%20crate-333333?style=flat-square) ![Libfuzzer-sys](https://img.shields.io/badge/Libfuzzer--sys-333333?style=flat-square) ![Cargo-fuzz](https://img.shields.io/badge/Cargo--fuzz-333333?style=flat-square)

**The problem it solves**

PNG is the standard lossless image format, but its encoder/decoder (via zlib/DEFLATE) is relatively slow — especially encoding. QOI trades a small amount of compression ratio for a huge gain in speed: it's typically 20–50x faster to encode and 3–4x faster to decode than PNG, while landing in a similar compression-ratio ballpark, because it uses a simple byte-stream of small ops (run-length encoding, small pixel-to-pixel diffs, a tiny recently-seen-color cache) instead of DEFLATE's general-purpose compression.

**Challenges we ran into**

Here's a summary of the challenges you ran into while porting this project to Rust, based on our conversation:

1. Missing external dependencies (stb_image)

The original C qoiconv.c/qoibench.c rely on stb_image.h/stb_image_write.h (single-header PNG libraries) that aren't included in the repo and had to be substituted — the Rust port uses the png crate instead for PNG I/O, since there's no direct single-header equivalent in Rust's ecosystem.

2. Misreading a correct result as a bug

Your main.rs test on a 2×2 image reported "encoded 26 bytes" and looked broken at first glance. It turned out to be correct — a 2×2 image with 4 completely different colors has almost nothing to compress, so the 14-byte header + 8-byte padding dominates the tiny output. This wasn't a logic bug in qoi.rs at all; it just needed verifying against a manual simulation of the encode algorithm to confirm.

3. Cargo project structure mismatches

The single-file/loose-file mental model from C (gcc file.c -o binary) doesn't map directly onto Cargo:

mod qoi; (used when qoi.rs sits next to a file as a local submodule) kept failing with E0583: file not found for module once qoi.rs was moved into the shared library (src/lib.rs → src/qoi.rs) and referenced from src/bin/*.rs binaries instead.
Needed pub mod qoi; and pub use qoi::{...}; in lib.rs together — one exposes the qoi:: path itself (for qoi::qoi_encode(...) call sites), the other exposes flat names at the crate root (for qoi_rs::QoiDesc style imports). Missing either one caused E0432: unresolved import errors.
src/main.rs being present alongside src/bin/*.rs silently added a third binary (named after the package) that also needed fixing, which wasn't obvious until the compiler error list included it unexpectedly.
4. Sandbox/environment limitations during debugging

No rustc/cargo was available in this chat's sandbox to compile-check anything directly, and outbound network access was disabled (no git clone, no fetching stb_image.h). Verification had to be done by hand-translating the Rust encode logic into Python and running that simulation instead of compiling the real Rust code.

Team **Core gods** -- AMMAN KUMAR D

`2026-08-01`

---

### py-ulid-r
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pyulidr-9d8e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/barshamishra19/py-ulid-rust) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/W7caBCGxXUc) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A high-performance, behaviorally verified Rust imp

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square)

**The problem it solves**

**py-ulid-rs** is a high-performance Rust port of the popular `py-ulid` Python library, designed to generate **ULIDs (Universally Unique Lexicographically Sortable Identifiers)** efficiently and safely.

ULIDs are 128-bit, UUID-compatible identifiers that are naturally sortable by time, making them useful for database primary keys, distributed systems, and high-throughput applications.

The project addresses four key problems:

**1. Performance Bottlenecks**
ID generation is often on the hot path of applications. Python's interpreter overhead can limit throughput. `py-ulid-rs` achieves **sub-300ns generation times**, delivering approximately **40–65× faster performance** than the original Python implementation, verified using Criterion benchmarks.

**2. Safety & Correctness**
Rust's strong type system eliminates entire classes of invalid states. For example, unsigned integer types make negative values unrepresentable, reducing runtime validation overhead while maintaining predictable behavior.

**3. Verifiable Behavioral Equivalence**
Instead of assuming the port behaves like the original, we built a **differential testing pipeline**. The original Python library acts as an oracle, generating **10,000+ test vectors** that are compared against the Rust implementation for deterministic operations.

**4. Improved Specification Compliance**
During the port, we identified a logic issue in the original library's Monotonic implementation involving sub-second remainder handling. The Rust implementation corrects this behavior while maintaining compatibility across deterministic functionality.

**Challenges we ran into**

**1. Rust Dependency Compatibility**
The project targets an older Rust toolchain (1.75), while newer versions of development dependencies such as Criterion and Proptest introduced transitive dependencies requiring newer Rust features. I resolved this through dependency auditing and carefully pinning compatible versions.

**2. Python's Dynamic Types vs Rust's Type Safety**
Python performs runtime validation for invalid inputs, while Rust's type system can prevent some invalid states at compile time. The challenge was ensuring that stronger typing did not unintentionally change expected behavior. These decisions were documented in `DECISIONS.md`.

**3. Fixing Bugs vs Maintaining Parity**
While porting the Monotonic generator, I discovered an issue in the original implementation's same-millisecond detection. Rather than blindly reproducing the behavior, I chose to fix it and document the change while preserving deterministic behavioral compatibility.

**4. Building a Reliable Differential Testing Pipeline**
128-bit integers cannot safely be represented as standard JSON numbers across all environments without risking precision loss. To avoid this, the testing pipeline represents large integer values as **decimal strings**, ensuring exact comparisons between Python and Rust.

[Barsha Mishra](https://github.com/barshamishra19)

`2026-08-02`

---

### TalentLens AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/talentlens-ai-15e9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pankhudiglitch/TalentLens-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://talent-lens-ai-three.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4tfM9MERpHo?si=S48LowxErNuV4CXu) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI- Powered Resume Intelligence Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges while building TalentLens AI was creating an accurate candidate ranking system instead of simple keyword-based filtering. Many resumes use different formats, wording styles, and skill descriptions, which made consistent AI evaluation difficult.

Another challenge was extracting meaningful information from resumes and identifying relevant skills, experience, and candidate strengths in a structured way. Some resumes had inconsistent layouts, making parsing and analysis unreliable initially.

We also faced difficulties while designing the ranking logic and explainability system. The goal was not only to rank candidates but also to clearly explain why a candidate was shortlisted. Building transparent AI reasoning required multiple iterations and testing.

On the frontend side, maintaining a clean and responsive UI while displaying candidate scores, detected skills, ranking insights, and analysis cards was another hurdle.

These issues were solved by:

Improving the resume parsing workflow

Refining the AI scoring and ranking logic

Structuring candidate data more effectively

Optimizing frontend components for better responsiveness and readability

Testing with multiple resume samples to improve consistency and accuracy


Through continuous debugging, testing, and UI improvements, the platform became more reliable, scalable, and user-friendly.

**The problem it solves**

Hiring teams and recruiters often spend hours manually reviewing resumes, comparing candidates, and identifying the best fit for a role. Traditional ATS systems mostly rely on keyword matching and fail to explain why a candidate is suitable.

TalentLens AI solves this problem by using AI-powered candidate analysis to automatically rank resumes based on skills, experience, and job relevance. The platform helps recruiters quickly identify top candidates while also providing transparent reasoning behind each ranking.

The system detects candidate skills, evaluates experience, calculates an AI suitability score, and highlights why a candidate is shortlisted — such as strong technical fit, relevant experience, and positive candidate signals.

This makes the hiring process:

Faster

More accurate

More transparent

Less biased

Easier for recruiters and HR teams


TalentLens AI can be used by:

Recruiters

HR teams

Startups

Companies handling large-scale hiring

Placement cells and career platforms


By automating resume screening and providing explainable AI-based rankings, TalentLens AI reduces manual effort and improves hiring efficiency.

[Pankhudi Singh](https://github.com/pankhudiglitch)

`2026-07-03`

---

### CodeVerse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codeverse-5d55) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://best-codeverse.pages.dev/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=6CQB52WAL9c) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> All in One Code Learning Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Building CodeVerse involved several challenges.

One of the biggest challenges was organizing a large amount of programming content in a way that remained simple and easy to navigate. Creating a clean interface while keeping the website responsive across different screen sizes also required multiple design iterations.

Another challenge was integrating AI-assisted development into the workflow while ensuring that the final website was customized, visually appealing, and functional. Testing layouts, improving navigation, and refining the user experience required continuous experimentation and feedback.

These challenges were solved through iterative development, careful UI improvements, extensive testing, and version control using GitHub.

**The problem it solves**

# CodeVerse

**Redeem Code-(CODEVERSE123!)

Learning programming often requires students to switch between multiple websites for tutorials, notes, roadmaps, coding challenges, and learning resources. This makes the learning process confusing and time-consuming, especially for beginners.

CodeVerse solves this by bringing everything together in one place. It provides a clean and organized platform where students can explore programming languages, access structured learning roadmaps, watch recommended tutorials, and discover useful development resources without constantly searching across the internet.

The platform is designed to help beginners start their coding journey more easily while also serving as a central hub for continuous learning.

[Yuvraj Khera](https://github.com/WebsiteCoder07)

`2026-07-08`

---

### UniEvents HQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/unievents-hq-a34d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/talha5978/uni-events-hq) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1K8IC3PxUZBoSyZaQXRsaqK01EECO92FE/view) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Transforming Campus Event Management

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

- Handling complex role system (Admin, President, Treasurer, Member, Student)
- Making payment verification flow smooth and secure
- Implementing reliable QR code scanning and verification
- Managing multiple time slots per event
- Balancing simplicity for students with powerful tools for societies

**The problem it solves**

**UniEvent HQ** is a complete event management platform for universities.

- Students can browse events, register easily, and receive a personal QR code for entry.
- Society Presidents can create events, manage members, and track registrations.
- Treasurers can verify payments and manage society bank accounts.
- Admin (Student Affairs) can approve student accounts and oversee everything.

[Muhammad Talha](https://github.com/talha5978/)

`2026-07-23`

---

### MailShield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mailshield-89f1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://diiyyaar.github.io/MailShield/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Think Before you click

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![CodeIgniter](https://img.shields.io/badge/CodeIgniter-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Phishing emails are one of the most common cybersecurity threats. Many users struggle to distinguish between genuine and fraudulent emails, which can lead to stolen passwords, financial loss, and identity theft.

MailShield helps users identify potentially dangerous emails by analyzing their content for common phishing indicators such as urgent language, password requests, OTP requests, suspicious links, and account verification prompts.

The application classifies emails into **Low**, **Medium**, or **High Risk** and provides safety recommendations, making it easier for users to recognize phishing attempts before interacting with suspicious emails.

MailShield is designed as an educational and awareness tool that promotes safer online behavior and helps users make informed decisions when handling emails.

**Challenges we ran into**

## Challenges I Ran Into

As this was my first hackathon project, one of the biggest challenges was designing a responsive and user-friendly interface while keeping the project simple and easy to understand.

Another challenge was implementing the phishing detection logic. I had to decide which keywords commonly appear in phishing emails and create a JavaScript-based analyzer that could classify emails into Low, Medium, and High Risk based on the detected indicators.

I also faced issues while deploying the project using GitHub Pages. Initially, the website was not appearing after deployment, but I resolved it by configuring the correct branch and waiting for GitHub Pages to finish building the site.

Throughout the development process, I tested the application with different sample emails and refined the detection logic to improve the accuracy of the results.

Diya R

`2026-07-24`

---

### NovaStart: Startup Portfolio & Intake
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/novastart-startup-portfolio-and-client-intake-platform-c559) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/singhaman2353-ux/startup-portfolio) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://startup-portfolio.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A full-stack platform where founders can showcase.

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![Gunicorn](https://img.shields.io/badge/Gunicorn-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square) ![Fetch API](https://img.shields.io/badge/Fetch%20API-333333?style=flat-square) ![flask-cors](https://img.shields.io/badge/flask--cors-333333?style=flat-square)

**The problem it solves**

Many early-stage startups and freelancers rely on email or messaging apps to collect project inquiries, which makes it difficult to organize client requests. **NovaStart** provides a professional web presence with a structured intake process and an admin dashboard to manage submissions efficiently.

![image](https://assets.devfolio.co/content/03868079359e4cea999e2e1017d9e6dc/6c6f4810-c443-472e-b803-9026cfddd1aa.png)

![image](https://assets.devfolio.co/content/03868079359e4cea999e2e1017d9e6dc/5fd0c4c5-e8c9-443f-b9aa-d6f452c81fdd.png)

It's built to be a real, working funnel — from *visitor lands on the page* to *founder has a structured lead in hand* — not just a pretty landing page with **no backend behind it.**

**Challenges we ran into**

Building and deploying a split frontend/backend app surfaced a few real hurdles:

**CORS blocking the first request**
Since the frontend (Vercel) and backend (Render) live on completely different origins, the browser blocked the very first `fetch()` call by default. I got past it by explicitly configuring Flask-CORS to allow only the deployed frontend's origin, rather than opening the API up entirely.

**Free-tier cold starts**
Render's free backend spins down when idle, so the first request after inactivity can take 30–50 seconds. I handled this on the frontend by disabling the submit button and showing a "Submitting…" state, so the delay reads as "working" instead of "broken."

**Keeping the API URL environment-aware**
The JavaScript needed to call `http://127.0.0.1:5000` during local development but the live Render URL once deployed. Instead of hardcoding the URL in multiple places, I pulled it into a single config variable so switching environments meant changing one line, not hunting through the codebase.

Aman Singh

`2026-07-25`

---

### Imagscanner
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/imagscanner-2eb1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aimagscan.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Transforming Images into Intelligent Insights..

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**Challenges we ran into**

# Challenges I Ran Into

Building ImageScanner involved several technical challenges that helped me improve both my problem-solving and development skills.

### 1. Accurate OCR on Different Images
One of the biggest challenges was extracting text accurately from images with poor lighting, low resolution, handwritten content, or complex backgrounds. Different OCR models performed differently depending on the image quality. I addressed this by preprocessing images (resizing, noise reduction, and contrast enhancement) before passing them to the OCR engine, which significantly improved accuracy.

### 2. Understanding Image Context
Extracting text alone wasn't enough—the real challenge was enabling the AI to understand the overall context of the image. I combined OCR output with computer vision and an LLM so the application could generate meaningful explanations instead of simply returning raw text.

### 3. Handling Large Images
Large image files increased processing time and memory usage. To solve this, I optimized image resizing and compression before processing while preserving enough quality for accurate analysis.

### 4. API Integration and Error Handling
Integrating multiple AI services introduced challenges such as API latency, failed requests, and inconsistent responses. I implemented proper exception handling, request validation, retries, and user-friendly error messages to make the application more reliable.

### 5. Creating a Smooth User Experience
Displaying AI-generated responses in a clean and interactive way required several UI improvements. I focused on making the workflow simple: upload an image, wait for analysis, and receive structured results including extracted text, summaries, and AI-generated insights.

These challenges taught me the importance of optimizing AI pipelines, handling edge cases, and designing applications that are both technically robust and easy for users to interact with.

**The problem it solves**

# The Problem ImageScanner Solves

Every day, people interact with images that contain valuable information—documents, receipts, handwritten notes, medical reports, product labels, educational diagrams, and real-world scenes. However, extracting and understanding this information often requires multiple tools such as OCR software, translators, search engines, and AI chatbots, making the process slow, fragmented, and inefficient.

**ImageScanner** solves this problem by transforming any image into actionable knowledge. Users simply upload an image, and the platform automatically extracts text, identifies visual elements, understands the context, and generates meaningful insights using AI.

## What can people use it for?

- 📄 **Document Analysis:** Extract and summarize information from reports, invoices, forms, and handwritten notes.
- 🎓 **Education:** Explain diagrams, charts, mathematical problems, and study materials in simple language.
- 🛒 **Shopping:** Scan product labels to understand ingredients, nutritional information, and product details.
- 🌍 **Travel:** Translate signboards, menus, and documents in different languages.
- 🏥 **Healthcare:** Read and summarize medical reports or prescriptions for easier understanding.
- ♿ **Accessibility:** Help visually impaired users by describing images and reading text aloud.
- 📊 **Business:** Automate data extraction from receipts, bills, and business documents to reduce manual work.

## How it makes tasks easier

Instead of switching between multiple applications, users get everything in one place:
- Accurate OCR for text extraction
- AI-powered image understanding
- Automatic summaries and explanations
- Interactive Q&A about the uploaded image
- Fast, real-time results through a simple interface

ImageScanner saves time, reduces manual effort, improves accessibility, and enables users to interact with visual information more intelligently. It turns static images into searchable, understandable, and actionable knowledge, making AI-powered image analysis accessible to everyone.

[AKASH S](https://github.com/Akashsenthilkumar08)

`2026-07-26`

---

### Mission2K38
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/missionk-524e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/iamKrishnendu11/Mission-2038) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mission-2038.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Gali se ग्लोबल tak .

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

# The Problem It Solves

Football is one of the world's most popular sports, yet discovering talented players remains a difficult, expensive, and subjective process. Many aspiring footballers, especially from rural and underrepresented regions, never get the opportunity to showcase their skills because they lack access to professional scouts, academies, or trial events.

Traditional scouting relies heavily on manual observation, making it time-consuming, inconsistent, and prone to human bias. Coaches often have to review hours of match footage without any objective performance metrics, while players receive little to no analytical feedback to improve their game.

## Mission2K38 solves these challenges by:

- ⚽ Using **AI-powered computer vision** to automatically analyze football training and match videos.
- 📊 Generating objective performance metrics such as movement, ball control, speed, passing, and overall performance.
- 🎯 Helping coaches and scouts identify talented players using data-driven insights instead of subjective judgment.
- 🌍 Providing a digital platform where players from any location can upload videos and participate in scouting opportunities.
- 📈 Offering personalized analytics that help players understand their strengths and improve their weaknesses.
- 🤝 Connecting players, coaches, scouts, and football academies through a unified ecosystem.

## Impact

Mission2K38 democratizes football scouting by making talent identification more **accessible, transparent, affordable, and scalable**. Our vision is to ensure that every talented footballer gets a fair opportunity to be discovered, regardless of their background or location.

**Challenges we ran into**

# Challenges We Ran Into

Building Mission2K38 within a hackathon timeline came with several technical and engineering challenges.

## AI Model Integration

Integrating **YOLO** and **MediaPipe** into a seamless player analysis pipeline was one of our biggest hurdles. Synchronizing object detection, pose estimation, and frame processing while maintaining real-time performance required extensive optimization.

## Real-Time Video Processing

Processing football videos efficiently without significant latency was challenging. We optimized frame extraction, reduced unnecessary computations, and improved the inference pipeline to deliver faster analysis.

## Performance vs Accuracy

Finding the right balance between inference speed and detection accuracy was critical. We experimented with different YOLO models, confidence thresholds, and frame sampling strategies to achieve reliable results while keeping processing time low.

## Full-Stack Integration

Connecting the AI backend with our Next.js frontend required careful API design and asynchronous processing. We implemented a clean communication pipeline to ensure smooth video uploads, analysis, and result visualization.

## Scalability

Designing the architecture to support multiple users and large video uploads was another challenge. We structured the backend to be modular and deployment-ready for future cloud scaling.

## Team Collaboration

Since multiple developers were working simultaneously on the frontend, backend, AI models, and UI, maintaining code consistency and avoiding merge conflicts required effective Git workflows and continuous communication.

## What We Learned

These challenges helped us gain hands-on experience in computer vision, AI deployment, API integration, performance optimization, and collaborative software development. Overcoming them enabled us to build a functional end-to-end AI football scouting platform within the limited hackathon timeframe.

**Best Use of Gemini API**

# Why Mission2K38 fits the "Best Use of Gemini API" Track

Mission2K38 leverages the **Google Gemini API** to transform raw football performance data into meaningful, personalized insights for players, coaches, and scouts.

After our computer vision pipeline analyzes uploaded videos using **YOLO** and **MediaPipe**, Gemini interprets the extracted metrics and generates easy-to-understand performance summaries, strengths, weaknesses, and actionable improvement recommendations.

Instead of presenting users with only numerical statistics, Gemini converts complex analytical data into natural language, making professional-level feedback accessible to players of all skill levels.

## How Gemini powers our platform

- 🤖 Generates personalized player performance reports.
- 📊 Explains AI analysis in simple, human-readable language.
- 💡 Recommends training plans based on detected strengths and weaknesses.
- ⚽ Assists coaches and scouts with intelligent player evaluation summaries.
- 🧠 Helps players understand how to improve through AI-driven recommendations.

## Impact

By combining **Computer Vision** with the **Gemini API**, Mission2K38 delivers an intelligent football scouting experience that is not only accurate but also understandable and actionable. This enables data-driven talent identification while providing every player with personalized AI coaching and performance insights.
![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/0653e52c-ac1b-4c23-89e0-453baf14524f.jpeg)

![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/2e2bac5c-d323-4cde-a364-733587aa2e4c.jpeg)

![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/b6f29b65-c071-452e-9de1-1248e48605b3.jpeg)

**Best Use of MongoDB Atlas**

# Why Mission2K38 fits the "Best Use of MongoDB Atlas" Track

Mission2K38 uses **MongoDB Atlas** as the primary database to power our AI-driven football scouting platform. Atlas enables us to efficiently manage player data, scouting information, AI-generated performance reports, and user interactions in a scalable and secure cloud environment.

Our application stores structured and semi-structured data, making MongoDB's flexible document model an ideal choice for handling evolving player profiles and performance analytics.

## How MongoDB Atlas powers our platform

- ⚽ Stores player profiles, coach accounts, and scout information.
- 📊 Maintains AI-generated performance reports and match analytics.
- 🎥 Manages metadata for uploaded football training and match videos.
- 🏆 Stores trial registrations, scouting events, and academy information.
- 🔐 Provides secure authentication and user management.
- ☁️ Delivers a scalable cloud database that supports future growth and high availability.

## Why MongoDB Atlas

MongoDB Atlas allowed us to rapidly develop and deploy our application without worrying about database infrastructure. Its scalability, reliability, and flexible schema helped us build a robust backend capable of handling large volumes of football scouting data.

By combining **MongoDB Atlas**, **Next.js**, **Node.js**, **Express.js**, and our **AI computer vision pipeline**, Mission2K38 delivers a modern, scalable platform for digital football talent identification.
![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/2dc23336-3b5d-4ae0-bd46-db6703e4446c.jpeg)

![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/1423b9df-f963-4625-af9b-a677505e4cf9.jpeg)

**Open Innovation**

# Why Mission2K38 fits the Open Innovation Track

Mission2K38 is an AI-powered football scouting platform that addresses a real-world challenge: making talent discovery more accessible, objective, and data-driven.

Traditional football scouting is often limited by geography, cost, and human bias, preventing many talented players from being discovered. Our platform leverages **Computer Vision, YOLO, MediaPipe, and AI analytics** to evaluate player performance from uploaded videos and generate meaningful insights for coaches, scouts, and academies.

The solution is designed as a scalable digital platform that can be adopted by football academies, clubs, schools, tournaments, and independent scouts. By combining AI with sports technology, Mission2K38 democratizes football scouting and creates equal opportunities for aspiring players regardless of their location or background.

### Innovation Highlights

- 🤖 AI-powered player performance analysis
- ⚽ Automated football scouting using computer vision
- 📊 Objective performance metrics and analytics
- 🌍 Accessible to players from any location
- 📈 Scalable platform for academies, clubs, and scouts
- 🚀 Potential for expansion into other sports and talent identification systems

Mission2K38 demonstrates how AI can solve a real-world problem with measurable social and technological impact, making it an ideal fit for the **Open Innovation** track.
![image](https://assets.devfolio.co/content/e49d261c858f4c07ada62f8eafeb5d08/9bc7f3ce-b5e0-41c6-aa47-521201206ebd.png)

Team **Algo Rhythm** -- [Krishnendu Mandal](https://github.com/iamKrishnendu11), [Sucharita Das](https://github.com/iamSucharita), [Prithvi Raj Thakur](https://github.com/prithvi-raj-thakur), [Sukhendu Chakraborty](https://github.com/sukhendu-chakraborty)

`2026-07-26`

---

### Nova AutoML & AI data platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nova-automl-and-ai-data-platform-ace3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://openhub-platform.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JmG5PiKDwGM?si=a3o_uHs7KKkwjQ0S) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Machine learning for everyone — no code required.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Data Science](https://img.shields.io/badge/Data%20Science-333333?style=flat-square) ![Data Visualization](https://img.shields.io/badge/Data%20Visualization-333333?style=flat-square)

**Challenges we ran into**

Deployment on Render:- The default Python version (3.14) broke installs for ML dependencies. We pinned Python 3.11.11, split production vs. local requirements, and fixed the WSGI entrypoint so Gunicorn could find the app reliably.

Excel uploads crashing :- .xlsx files failed during upload/parsing. We added proper Excel handling (openpyxl) and tightened backend validation so bad files fail with clear errors instead of crashing the server.

Messy real-world CSVs :- Many uploads weren’t plain UTF-8. We built a multi-encoding fallback (UTF-8, Latin-1, CP1252, etc.) so common exports from Excel and regional tools still load.

AutoML timeouts :- Training several models on one request was too slow for a web server. We optimized the AutoML pipeline and tuned Gunicorn (timeout: 120s, limited workers) so runs could finish without the process being killed mid-training.

Frontend error visibility :- Early on, failed uploads or training runs looked like “nothing happened.” We improved error handling in the UI and added Run ID debugging so users could inspect logs, status, and re-runs when something went wrong.

Optional heavy dependencies :- Not every environment has XGBoost installed. We made it gracefully optional so the platform still runs with scikit-learn models when XGBoost isn’t available.

**The problem it solves**

Nova Dominators — AutoML Data Intelligence Platform :-
Nova Dominators is a web-based platform that turns raw CSV/Excel data into trained machine learning models and actionable insights without writing code.

The problem it solves:-
Building useful ML models usually means juggling Python notebooks, manual data cleaning, model selection, and separate reporting tools. That barrier keeps many people from using machine learning on their own data.
Nova Dominators bundles that workflow into one place upload a dataset, and the platform handles preprocessing, model training, comparison, and reporting.

What you can use it for :-
i) Quick ML prototypes:-
Drag & drop a dataset, optionally set a target column, and AutoML trains several models (Logistic Regression, Random Forest, XGBoost, etc.) and picks the best one.
ii) Data exploration:-
The Smart Dataset Analyzer surfaces stats, column types, and distributions before you commit to modeling.
iii) Safer data cleaning:-
Auto Clean suggests fixes (missing values, duplicates, outliers, etc.) with a risk meter and impact preview so you can apply changes with more confidence.
iv) Synthetic data:-
The Dataset Creator generates configurable test datasets (numeric, categorical, date) for demos, learning, or pipeline testing.
v) Visual reporting:-
Nova Power BI Report builds interactive charts and relationship dashboards from your data similar to a lightweight BI tool.
vi) Model handoff:-
Download the trained model, view the leaderboard, and inspect training logs for reuse or further work.

How it makes existing tasks easier :-
i) No coding required — classification and regression pipelines run automatically (imputation, encoding, scaling, feature selection, cross-validation).
ii)One upload, full pipeline — from raw file to best model, metrics, and downloadable artifact in a single flow.
iii)Guided cleaning — cleaning recommendations are ranked and labeled by risk instead of guessing which transformations are safe.
iv)All-in-one toolkit — analysis, cleaning, training, and visualization live in one UI instead of switching between Jupyter, Excel, and Power BI.

**Open Innovation**

Open Innovation is about making advanced technology accessible, reusable, and extensible — not locked inside expert-only tools or closed ecosystems. Nova Dominators fits that track because it opens up machine learning to people who don’t write code, while staying built on open standards and open-source tools.

1. Democratizes ML :-
Most ML work still lives in Python notebooks and requires data-science skills. Nova Dominators lets anyone with a CSV or Excel file upload data and get a trained model, metrics, and insights — no coding required.
That aligns with open innovation’s core idea more people can participate in building solutions, not just ML engineers.

2. Built entirely on open-source technology:-
The platform is powered by widely used open tools:
Flask, pandas, scikit-learn, XGBoost, Joblib
Instead of a black-box proprietary AutoML product, it’s a transparent, community-backed stack that others can inspect, fork, and extend.

3. Open data in, open artifacts out :-
Input:- standard open formats (CSV, Excel) — no vendor       lock-in.
Output:- downloadable models, leaderboards, training logs, and cleaned datasets.
Users keep ownership of their data and can reuse models elsewhere — supporting interoperability instead of trapping users in one platform.

4. Transparent, explainable workflow :-
Open innovation favors trust and visibility, not opaque AI:-
i) Model leaderboard (compare algorithms side by side).
ii) Run logs and metadata for every training job.
iii)Risk-rated data cleaning so users see what changed and why.
This makes the pipeline auditable — important for education, research, and small businesses.

5. Enables experimentation without proprietary datasets:- 
The Dataset Creator generates synthetic datasets for learning, demos, and testing. That supports open innovation in education and prototyping: people can experiment freely before working with real or sensitive data.

6. Extensible by design (API-first):-
The backend exposes REST endpoints (/api/upload, /api/analyze, /api/models/..., etc.), so others can:
i)Integrate AutoML into their own apps.
ii)Add new model types or data connectors.
iii)Build plugins on top of the platform.

Team **Nova Dominators** -- [SAYAN GHOSH](https://github.com/sayan-ghosh8124), [SUVA GHOSH](https://github.com/Suvaghosh), [Spandan Karfa](https://github.com/Spandan-24), [Shayan Ghosh](https://github.com/Shayanghosh03)

`2026-07-26`

---

### SITEMIND
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sitemind-1b00) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AwkJay/sitemind-hexafalls2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1vX2ele6wy-RC1-foVLY5FybCP5Duj-qp/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI Intelligence Platform for Data Centre EPC Proje

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

India is witnessing an unprecedented data centre construction boom, driven by AI, cloud computing, digital services, and emerging quantum computing infrastructure. According to the JLL 2025 India Data Centre Report, India's operational capacity is expected to grow from 900 MW in 2024 to over 2,700 MW by 2027, representing more than $15 billion in investments. A single hyperscale facility involves 15,000–40,000 equipment line items, up to 200 contractors, and thousands of commissioning tests, where even minor errors can compromise Tier III/IV certification.
While tools like Jira, Bitrix24, Primavera, Microsoft Project, and Autodesk Construction Cloud manage tasks, schedules, and documents effectively, they do not understand engineering standards or connect compliance, procurement, quality, and commissioning data. As a result, critical project information remains fragmented, leading to costly rework, procurement delays, commissioning failures, and schedule overruns. Industry reports show that 67% of Asia-Pacific data centre EPC projects exceeded planned schedules by more than 10%, largely due to these issues.

SiteMind solves this by providing an AI-powered engineering intelligence layer over existing project management systems. It unifies project documents, engineering standards, schedules, procurement records, quality inspections, and commissioning data into a single platform. SiteMind automatically detects specification deviations, grounds every compliance finding with cited engineering standards, predicts schedule and supply chain risks, assists engineers during commissioning, and provides instant, citation-backed answers from project documents.

By transforming fragmented project information into actionable engineering intelligence, SiteMind helps EPC teams reduce rework, improve compliance, accelerate decision-making, and deliver critical infrastructure faster, more safely, and with greater confidence.

**Challenges we ran into**

Challenges We Ran Into

- Scoping the problem statement — Generalizing from a narrower data-centre EPC compliance tool to a platform applicable to any hyperscale or public-infrastructure megaproject, without losing precision in the process.
- Market research shaping the core thesis — Existing AI compliance tools we evaluated either fabricated citations or embedded the decision inside an opaque model score with no audit trail. This gap defined the product thesis: the LLM never computes the verdict — it only extracts and explains, while a deterministic rule engine decides.
- Avoiding over-reliance on agent frameworks — We decided against wrapping the core compliance logic in an agent-orchestration framework, since it introduces control flow that is difficult to audit for pass/fail decisions on safety-critical clauses. The decision layer remained plain Python; the one agent framework used (LangGraph) is scoped strictly to the conversational Copilot interface, separate from the verdict path.
- LLM provider reliability — Rate limits on free-tier LLM access posed a risk to demo stability, so we implemented a provider fallback chain for prose generation, while ensuring no provider is ever involved in the pass/fail decision itself.
- Building genuine vector search, not a fallback disguised as one — We selected a self-hosted vector database over a cloud API to preserve the offline, on-site operating model. Dense embedding search alone missed exact clause matches, and keyword search alone missed paraphrased queries, so we implemented hybrid retrieval (dense + BM25, fused via reciprocal rank fusion) with an acceptance gate to prevent confidently citing an incorrect clause.
- Defining "tamper-evident" precisely — On-chain notarization proves a record was not silently altered after the fact; it does not verify that the original entry was accurate. This distinction required a three-state verification result rather than a binary one, so that "unreachable" is never conflated with "tampered."
- Sourcing verified standards data — Every citation had to resolve to actual digitized regulatory text rather than content recalled from model training. This required sourcing and structuring real IS/CEA standards documents before any retrieval or compliance logic could be considered reliable.

**Accio Relevance - Build with Actian VectorAI Database**

SiteMind is an AI-powered EPC Project Intelligence platform that helps engineers make faster and more reliable decisions by unifying engineering documents, standards, schedules, procurement, and quality records. To enable accurate, explainable, and citation-backed retrieval of engineering standards, SiteMind integrates Actian VectorAI DB as its semantic search engine, ensuring every compliance check and Copilot response is grounded in real engineering clauses rather than LLM memory. 
One of the biggest challenges in engineering AI is ensuring that responses are based on real engineering standards, not on what an LLM "remembers." That's why we integrated Actian VectorAI DB as the retrieval engine behind SiteMind.
We deployed Actian VectorAI DB locally in Docker, making the entire solution offline, secure, and enterprise-ready, without relying on external APIs or cloud vector databases.
We indexed over 6,200 vectorized chunks from digitized Indian Standards (IS/BIS), along with SiteMind's internal engineering standards repository. Every compliance check and Copilot query searches this knowledge base before presenting a citation.
Here's how the retrieval pipeline works:
When an engineer asks a question or a compliance rule is executed, the query is first converted into a MiniLM embedding. That query is then processed in two parallel searches:
A dense semantic search using Actian VectorAI DB, which finds clauses based on meaning.
A BM25 keyword search, which finds exact lexical matches.
Instead of choosing one over the other, we combine both using Reciprocal Rank Fusion (RRF), ensuring that results strong in either semantic similarity or keyword relevance are surfaced.
To guarantee reliability, we apply an additional acceptance gate. A retrieved clause is accepted only if its clause number or text matches the expected engineering rule; otherwise, SiteMind falls back to a verified local copy. This prevents incorrect citations from ever reaching the engineer.
Most importantly, Actian VectorAI DB never decides whether a design passes or fails. It is used solely to retrieve the correct engineering clause. The actual compliance decision is always performed by our deterministic Python rule engine, ensuring every verdict is explainable, auditable, and reproducible.
To demonstrate that this is a real integration and not a mock-up, our system exposes retrieval provenance for every result, including the retrieval method, similarity score, rank, and the fact that the search was performed across 6,206 indexed engineering vectors. This gives engineers complete transparency into how every compliance citation was obtained.
In short, Actian VectorAI DB gives SiteMind the speed and intelligence of semantic search, while our deterministic rule engine guarantees the accuracy and trustworthiness required for mission-critical infrastructure projects.

**Best Use of Gemini API**

SiteMind uses the Gemini API as an engineering reasoning and explanation layer rather than a decision engine. Gemini extracts engineering parameters from complex Design Basis Reports, generates natural-language compliance summaries, powers a multi-turn Engineering Copilot, and converts engineering findings into clear, actionable insights. Every response is grounded using retrieval from Actian VectorAI Database, while the final compliance verdict is always computed by a deterministic Python rule engine. This separation enables explainable AI that combines Gemini's reasoning capabilities with verifiable engineering standards, eliminating hallucinated compliance decisions and making the system suitable for mission-critical infrastructure projects.

What makes the Gemini usage novel?
Gemini never decides PASS/FAIL—it extracts, reasons, and explains, while deterministic code computes every engineering verdict.
Multi-turn Engineering Copilot that answers questions across project documents, schedules, supply chain, and engineering standards with citation-backed responses.
Grounded Generation—every response is based on retrieved engineering clauses rather than Gemini's internal knowledge, reducing hallucinations.
Offline-first architecture—if Gemini is unavailable, the platform gracefully falls back to deterministic templates, ensuring compliance workflows continue uninterrupted.

**Best Use of ElevenLabs**

SiteMind integrates ElevenLabs to make engineering intelligence accessible to field engineers through a multilingual voice assistant. Engineers can ask questions or submit voice notes in Hindi, English, or regional languages, and SiteMind responds with citation-backed answers in both text and natural speech. ElevenLabs powers speech-to-text (STT) and text-to-speech (TTS), enabling hands-free interaction on construction sites where typing is impractical. The voice assistant is integrated with SiteMind's Engineering Copilot, allowing engineers to retrieve compliance clauses, project information, schedule risks, and supply chain updates while keeping their hands free for on-site work. By combining ElevenLabs with grounded retrieval and deterministic engineering validation, SiteMind delivers natural voice interactions without compromising the accuracy or explainability of engineering decisions.

Why ElevenLabs?
Multilingual voice interface for engineers working in diverse linguistic environments.
Hands-free access to engineering knowledge on construction sites.
Natural speech responses for compliance, standards, schedules, and project queries.
Integrated with the AI Copilot, ensuring every spoken answer is grounded in retrieved engineering standards rather than model memory.

**Best Use of Solana**

About the Integration

SiteMind integrates Solana to create a tamper-evident audit trail for critical engineering compliance decisions. Every finalized compliance report is converted into a cryptographic hash and recorded in SiteMind's append-only audit ledger. When enabled, this hash is anchored on the Solana blockchain, creating an immutable timestamped proof that the record existed in that exact form.

Why Solana?

In large EPC projects, compliance reports, NCRs, inspections, and approvals often determine project acceptance, contractual claims, and regulatory audits. Any unauthorized modification of these records can lead to disputes and financial loss.

By leveraging Solana's high throughput, low transaction cost, and immutable ledger, SiteMind enables engineers, contractors, clients, and auditors to independently verify that a compliance record has not been altered after approval, without relying solely on SiteMind's own database. This provides transparency, accountability, and trust across multiple stakeholders.

How it Works
A compliance report is finalized by SiteMind's deterministic rule engine.
A cryptographic hash of the report is generated.
The hash is stored in SiteMind's append-only audit ledger.
With SOLANA_ENABLED=1, the same hash is anchored on the Solana Devnet.
During verification, SiteMind recomputes the document hash and compares it against the on-chain record. Any modification immediately results in a mismatch, proving the record has been changed.
Why this is innovative

Unlike traditional construction management systems that rely on centralized databases, SiteMind uses Solana to provide independent, tamper-evident verification of engineering decisions. This makes compliance records transparent, auditable, and trustworthy throughout the lifecycle of mission-critical infrastructure projects.

"Solana doesn't decide compliance—it proves that the compliance decision recorded by SiteMind has not been silently altered after it was approved."

This distinction aligns with your project's philosophy: AI retrieves, deterministic code decides, and Solana guarantees the integrity of the recorded decision.

**Best Use of DigitalOcean**

The novelty of SiteMind lies in transforming DigitalOcean from a traditional hosting platform into an AI-powered engineering intelligence infrastructure. Instead of merely serving a web application, DigitalOcean orchestrates document ingestion, AI-powered analysis, deterministic compliance validation, schedule intelligence, procurement analytics, and real-time collaboration within a unified cloud-native platform. Engineers upload complex EPC documents, and SiteMind automatically extracts engineering parameters, retrieves relevant standards from a knowledge base of over 6,200 digitized engineering vectors, performs deterministic compliance checks, generates citation-backed insights, and maintains an auditable project history—all from a single scalable deployment. This shifts construction management from passive document storage to an intelligent decision-support system capable of proactively identifying risks before they become costly site failures, making DigitalOcean the backbone of an always-available, production-ready AI platform for critical infrastructure.

**Best Use of MongoDB Atlas**

Best Use of MongoDB Atlas

SiteMind leverages MongoDB Atlas as the persistent backbone for its engineering intelligence platform. Every finalized compliance decision, audit event, project timeline update, NCR, and AI-generated insight is stored as structured documents, enabling real-time access, historical traceability, and scalable management of complex infrastructure data. The platform's Audit Ledger records every finalized compliance decision as an append-only document with a cryptographic content hash, ensuring that engineering decisions remain traceable and independently verifiable throughout the project lifecycle. MongoDB Atlas provides the flexibility and scalability needed to manage thousands of engineering records generated across large EPC projects involving 15,000–40,000 equipment line items and up to 200 concurrent contractors.

Why MongoDB Atlas?
Flexible document model for engineering documents, compliance reports, NCRs, RFIs, schedules, and audit records.
Append-only Audit Ledger ensures finalized compliance decisions remain traceable and tamper-evident.
Scalable cloud architecture capable of handling thousands of project records across multiple infrastructure projects.
Seamless integration with AI services, Actian VectorAI DB, and deterministic compliance workflows.

**Best Use of Gemini API**

SiteMind integrates the Gemini API as its intelligent engineering reasoning and conversational layer, enabling engineers to interact naturally with complex project data through an AI-powered Copilot. Gemini analyzes engineering documents, understands technical queries, generates compliance explanations, summarizes specifications, and assists with RFIs, schedules, procurement, and quality records using grounded, citation-backed retrieval rather than relying on model memory. Every response is enriched with engineering context retrieved from over 6,200 digitized engineering standard vectors, while the final compliance verdict is always computed by SiteMind's deterministic Python rule engine, ensuring that AI explains engineering decisions but never determines them. This combination of Gemini's multimodal reasoning capabilities with grounded retrieval and deterministic validation delivers accurate, explainable, and trustworthy AI assistance for mission-critical infrastructure projects.

**Best Use of Solana**

SiteMind leverages Solana to create a tamper-evident, cryptographically verifiable audit trail for engineering compliance in large infrastructure projects. Every finalized compliance report, Non-Conformance Report (NCR), approval, and quality milestone is securely stored off-chain, while its SHA-256 cryptographic hash is anchored on the Solana blockchain. This enables engineers, clients, contractors, and auditors to independently verify that approved engineering records have not been altered after sign-off without exposing confidential project data. By combining deterministic engineering validation with Solana's fast, low-cost, and immutable blockchain infrastructure, SiteMind brings transparency, accountability, and trust to mission-critical EPC projects involving 15,000–40,000 equipment line items, up to 200 concurrent contractors, and thousands of quality inspections, ensuring every compliance decision remains permanently verifiable throughout the project lifecycle.

**Best Use of MongoDB Atlas**

SiteMind leverages MongoDB Atlas as the persistent backbone for its engineering intelligence platform. Every finalized compliance decision, audit event, project timeline update, NCR, and AI-generated insight is stored as structured documents, enabling real-time access, historical traceability, and scalable management of complex infrastructure data. The platform's Audit Ledger records every finalized compliance decision as an append-only document with a cryptographic content hash, ensuring that engineering decisions remain traceable and independently verifiable throughout the project lifecycle. MongoDB Atlas provides the flexibility and scalability needed to manage thousands of engineering records generated across large EPC projects involving 15,000–40,000 equipment line items and up to 200 concurrent contractors.

Why MongoDB Atlas?
Flexible document model for engineering documents, compliance reports, NCRs, RFIs, schedules, and audit records.
Append-only Audit Ledger ensures finalized compliance decisions remain traceable and tamper-evident.
Scalable cloud architecture capable of handling thousands of project records across multiple infrastructure projects.
Seamless integration with AI services, Actian VectorAI DB, and deterministic compliance workflows.

**Open Innovation**

SiteMind is an AI-powered engineering intelligence platform that augments existing EPC tools instead of replacing them. It unifies project documents, engineering standards, schedules, procurement, quality, and commissioning data to support projects involving 15,000–40,000 equipment items and up to 200 contractors. Using AI agents, deterministic rule evaluation, and citation-backed RAG, it enables automated compliance checks, predictive risk analysis, and explainable decision support. Built with a modular, offline-first architecture, SiteMind is scalable beyond data centres to any large infrastructure project.

**Sustainability**

SiteMind improves sustainability by preventing construction errors before they reach the site, reducing material waste, rework, and project delays. A single hyperscale data centre typically involves 15,000–40,000 equipment line items, up to 200 concurrent contractors, and thousands of commissioning activities, making even small compliance errors costly. By detecting non-conformances during design review instead of after construction, SiteMind can significantly reduce unnecessary demolition, concrete and steel wastage, and schedule overruns. Internal ROI estimates indicate that preventing a single major compliance issue can save approximately 20 engineering hours and around ₹15 lakh in rework costs. The platform runs offline using a locally deployed Actian VectorAI DB and deterministic rule engine, reducing dependence on cloud infrastructure while remaining scalable across data centres, industrial plants, smart cities, transportation, and other large public infrastructure projects.

Team **TechNerdies** -- [Sarbajit Kumar De](https://github.com/Sarbajit-2004), [Saksham Jaiswal](github.com/Saksham-Jaiswal-2004), [Awnikant Ajay](https://github.com/AwkJay)

`2026-07-26`

---

### RouterOps
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/routerops-246f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/asgofficial/RouterOps) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GxUdydzDiBg) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Ai orchestration Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

The api tokens keep running away and we have to re create api keys

**The problem it solves**

RouterOps is a smart AI model orchestration platform that acts as an intelligent gateway between users and multiple large language models. Instead of sending every request to a single model, RouterOps evaluates each prompt for complexity, reasoning depth, coding requirements, context size, speed, and cost before dynamically selecting the most suitable AI model.

The platform continuously monitors model availability, latency, token limits, and API health, automatically switching to alternative models whenever failures occur. This ensures uninterrupted responses, lower operational costs, and improved performance. RouterOps enables businesses and developers to integrate multiple AI providers through a single intelligent interface while maximizing response quality and minimizing infrastructure expenses.

**Open Innovation**

Because we are trying to solve a real world problem which is basically faced by students

Team **Gaut-A-Bug** -- [Asmita Mahato](https://github.com/asmoGlitch), [Ayush Singh Gautam](https://github.com/asgofficial)

`2026-07-26`

---

### AuditGemma
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/auditgemma-06c3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chethankotian2005/auditgemma) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/pge-SHbAcCw?si=iAICurqMUeVfsmWA) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI Powered SME Compliance & Risk Triage Copilot

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square)

**Challenges we ran into**

1. **Ollama Model Loading Timeouts (The 502 Bad Gateway Cascade)**
   We initially tried to load the heavy `gemma3:4b` model dynamically for document extraction. However, the laptop's hardware took more than 30 seconds to load it into memory. The backend had a hardcoded 30-second timeout, which would trigger a "fallback" to `gemma:2b`. Because Ollama processes one model at a time, this queued a *second* cold-load behind the first one, guaranteeing a complete timeout cascade and a 502 Bad Gateway error on every single file upload from the Flutter app. We fixed this by prioritizing `gemma:2b`, removing the silent fallback, and bumping the FastAPI timeouts.

2. **Container vs. Host Clock Skew (The 401 Unauthorized)**
   The Flutter app was correctly generating Firebase Auth tokens to submit the final application. However, because the Docker container running the backend had an internal clock that was exactly 1 second behind the host laptop/phone, the Firebase Admin SDK rejected the token for being "used in the future" (`Token used too early`). We resolved this by explicitly adding a 60-second clock skew tolerance to the token verification logic.

3. **Data Contract Mismatches (The `KeyError`)**
   The Flutter frontend serialized the document type in the JSON payload as `"document_type"`, but the backend's deterministic Stage 2 layer (the Entity Consistency Check) was strictly expecting `"doc_type"`. This caused the backend to instantly crash right as it tried to evaluate the documents. We patched the backend to safely accept the correct key.

4. **LLM Hallucinations Crashing Deterministic Code (The 500 Error)**
   Because Gemma was extracting data directly from messy, unstructured images (like GST filings), it occasionally hallucinated invalid dates (like `2023-09-31`). When our strict Python signal layer tried to convert those strings into native `datetime` objects to calculate transaction velocity bursts, it threw a `ValueError` (day out of range), crashing the entire scoring pipeline. We made the code resilient by wrapping the date parsers in `try/except` blocks to gracefully skip unparseable dates.

5. **Silent Database Failures**
   The backend was designed to save scored cases to Firebase Firestore. However, because the cloud credentials weren't fully configured yet for local testing, the backend silently threw the scored cases away after processing them. This resulted in the mobile app showing "Pending", but the Next.js Officer Dashboard showing an empty queue. We solved this by building a resilient local in-memory fallback store so the pipeline could function flawlessly without cloud infrastructure.

**The problem it solves**

**AuditGemma** solves the problem of slow, manual, and error-prone financial compliance reviews.

Traditionally, when a Small or Medium Enterprise (SME) applies for a loan or undergoes an audit, a human compliance officer has to manually read through unstructured images and PDFs (KYC documents, bank statements, invoices), manually cross-reference data across those files to catch discrepancies, and hunt for subtle fraud patterns like money laundering via rapid transaction bursts.

AuditGemma automates this entire bottleneck. It uses Gemma's native vision capabilities to instantly extract structured data from messy images, runs deterministic code to catch exact-match discrepancies (e.g., mismatched tax IDs) and transaction velocity fraud, and then uses Gemma's reasoning to generate a final risk score and a human-readable narrative. This turns hours of manual auditing into a near-instant, AI-assisted workflow, allowing human officers to simply review the final narrative and make the final "Approve" or "Escalate" decision.

Team **Team ACE** -- [Chethan V Kotian](https://github.com/chethankotian2005), [ANSHIKA ANSHIKA](https://github.com/Anshika-17a), [Ashley Fernandes](https://github.com/ashley549), [Ananya Salian](https://github.com/Ananya-Salian)

`2026-07-20`

---

### ZeroOps
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zeroops-a735) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Megh2005/ZeroOps) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1neChKUdhEQWxTCFRaP8PAQQn51zGDYis_T9OiNJujP8/edit?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=2w_NyeOLt2w) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Architect. Automate. Accelerate.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Terraform](https://img.shields.io/badge/Terraform-333333?style=flat-square)

**The problem it solves**

Modern software deployment and cloud infrastructure management often involve multiple disconnected tools, manual configurations, and repetitive operational tasks. Developers and DevOps engineers must configure CI/CD pipelines, provision cloud resources, manage secrets, containerize applications, monitor deployments, troubleshoot failures, and perform rollbacks using different platforms. This fragmented workflow increases deployment complexity, slows software delivery, introduces configuration errors, and requires significant operational expertise.

**ZeroOps** addresses these challenges by providing an **AI-powered autonomous DevOps orchestration platform** that automates the complete software delivery lifecycle—from source code to production deployment—while minimizing manual intervention.

With **ZeroOps**, users can:

- **Automatically trigger deployments from GitHub** whenever new code is pushed, eliminating manual deployment processes.
- **Build and containerize applications automatically** by detecting project frameworks, validating existing Docker configurations, or generating optimized Dockerfiles when required.
- **Deploy applications seamlessly to cloud platforms** such as **Google Cloud Platform (GCP)** using services like **Cloud Run** or **Google Kubernetes Engine (GKE)** without manually configuring infrastructure.
- **Securely manage sensitive credentials** through integrated secret management services, ensuring API keys, service accounts, and environment variables are never exposed within source code or deployment pipelines.
- **Continuously validate deployments** by monitoring application health, container readiness, service availability, and deployment status before marking releases as successful.
- **Automatically recover from deployment failures** by detecting runtime issues, analyzing deployment errors, and rolling back to the last stable version whenever necessary.
- **Monitor deployment history and operational metrics** through centralized logging, deployment tracking, and real-time execution status, providing complete visibility across the deployment lifecycle.
- **Leverage AI-assisted deployment intelligence** to identify configuration issues, recommend corrective actions, and automate operational decisions that traditionally require experienced DevOps engineers.
- **Extend deployment workflows across multiple cloud providers**, enabling future support for hybrid and multi-cloud deployment strategies from a unified platform.

**ZeroOps** significantly reduces manual operational effort, shortens deployment cycles, improves deployment consistency, enhances infrastructure security, minimizes human error, and increases application reliability through intelligent automation and self-healing capabilities.

Whether deploying a small web application, managing enterprise-scale microservices, or building cloud-native platforms, **ZeroOps** provides a unified solution to **build, deploy, monitor, secure, recover, and automate modern DevOps workflows with confidence**, enabling organizations to move closer to a truly **Zero Operations** environment.

**Challenges we ran into**

Building **ZeroOps** involved overcoming several complex challenges across **DevOps automation, cloud deployment, AI-powered orchestration, and secure infrastructure management**. Our objective was not only to automate deployments but also to create a platform capable of making intelligent operational decisions while ensuring reliability, security, and scalability.

---

## 1. Intelligent Deployment Automation

One of the primary challenges was creating a deployment pipeline that could operate autonomously after every code push. Applications differ in structure, dependencies, build processes, and deployment requirements, making it difficult to design a universal workflow. We addressed this by implementing an intelligent orchestration engine capable of analyzing project configurations, identifying application frameworks, generating deployment workflows, and executing them with minimal manual intervention.

---

## 2. Automated Containerization

Supporting multiple programming languages and application frameworks required a flexible containerization process. While some repositories already contained optimized Docker configurations, many did not. The challenge was ensuring every application could be packaged consistently without requiring developers to manually create Dockerfiles. We solved this by validating existing configurations and automatically generating optimized Dockerfiles whenever required.

---

## 3. Secure Credential Management

Cloud deployments require access to sensitive credentials such as service account keys, API tokens, and environment variables. Managing these securely while preventing accidental exposure during builds and deployments was a critical challenge. We implemented secure secret management that retrieves credentials dynamically during deployment, ensuring sensitive information is never embedded in source code, repositories, or deployment logs.

---

## 4. Reliable Cloud Deployment

Automating deployment to **Google Cloud Platform (GCP)** required handling infrastructure provisioning, authentication, container image management, deployment execution, and service updates without manual intervention. We streamlined this workflow by integrating automated deployment mechanisms that build, validate, and deploy applications directly to cloud environments while minimizing configuration complexity for developers.

---

## 5. Deployment Validation and Self-Healing

Successfully deploying an application does not always guarantee that it is functioning correctly. Detecting runtime failures such as startup errors, unhealthy containers, failed health checks, or unavailable services was a significant challenge. To improve deployment reliability, we implemented continuous deployment validation combined with automated rollback mechanisms that restore the most recent stable release whenever deployment failures are detected.

---

## 6. AI-Assisted Error Detection and Recovery

Traditional deployment pipelines simply report failures, leaving developers responsible for identifying and resolving issues manually. Our goal was to make ZeroOps capable of assisting with operational troubleshooting. This required building AI-driven mechanisms that analyze deployment logs, identify probable root causes, recommend corrective actions, and support automated recovery workflows whenever possible.

---

## 7. Continuous Monitoring and Observability

Providing complete visibility into deployment status, execution history, and operational health required integrating centralized monitoring and logging across the deployment lifecycle. We developed a monitoring system that continuously tracks deployments, records execution logs, captures deployment metrics, and enables developers to quickly diagnose issues while maintaining a complete deployment history.

---

## 8. Scalability and Future Multi-Cloud Support

Designing ZeroOps exclusively for a single cloud provider would limit its long-term usability. One of the architectural challenges was building the deployment engine in a modular way so that support for additional cloud providers such as **AWS** and **Microsoft Azure** could be integrated without redesigning the core orchestration workflow. This approach ensures future extensibility while preserving a consistent deployment experience across multiple cloud environments.

---

## Conclusion

Each of these challenges contributed to the development of **ZeroOps** as an **AI-powered autonomous DevOps platform** capable of securely automating the complete software deployment lifecycle. By combining intelligent workflow orchestration, automated containerization, secure credential management, cloud deployment, deployment validation, AI-assisted troubleshooting, continuous monitoring, and self-healing capabilities, ZeroOps significantly reduces manual operational effort while delivering faster, safer, and more reliable application deployments.

Team **DataNexus** -- [Atyasha Bhattacharyya](https://github.com/atyasha2054), [Megh Deb](https://github.com/Megh2005), [Sandeep Sarkar](https://github.com/Sandeep-Sarkar-13)

`2026-07-12`

---

### Tendril
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tendril-1e0f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HimanshuM685/Tendril) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tendril.007575.xyz/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/S6kS0GuMbOM) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Pay only what your used. Get Paid for Your Compute

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square)

**The problem it solves**

## 🚨 The Problem It Solves

Renting compute today means going through a data center. You create an account, pass KYC, opt into billing, and pay per-action for capacity you often can't even get on demand. At the same time, millions of personal CPUs, GPUs, and RAM sit idle most of the day. And the fastest-growing class of compute consumers **autonomous agents** can't just show up and rent a machine, because every existing path assumes a human clicking through wallet popups and sign-ups. This fragmentation leaves two problems unsolved:

- **Gatekept, high-friction compute:** Builders queue for scarce, expensive cloud GPUs behind accounts, opt-ins, and per-call billing.
- **Idle hardware with no easy way to monetize it:** Ordinary people have spare capacity but no safe, simple way to rent it out without exposing their machine.

**Tendril** closes that gap: a prepaid marketplace where anyone can rent out their own PC's CPU/RAM/GPU, and anyone, a person *or* an agent, can rent it by the hour, **prepaid in native ALGO**, with a sandboxed SSH box in seconds and billing down to the exact second used.

## 💡 What Can People Use It For?

- **Burst Compute Without the Cloud Paperwork:** Spin up a real, sandboxed Linux box over SSH in seconds for a build, batch job, model run, or anything you'd normally provision a VM for no signup, no KYC, no opt-in.
- **Earning From Idle Hardware:** Run the contributor daemon on a spare machine and rent out the compute you weren't using. You're paid **on-chain, by the second**, the moment the lease ends minus a small platform fee.
- **Agent-Native Compute Rental:** The part nothing else does well. An autonomous agent hits `GET /explorer` (free) to survey live nodes and pick one itself, then `POST /rent/:id` to start a metered session no human, no clicks, no per-action signing.
- **Quick Throwaway Environments:** Need a clean, isolated box to test something risky or run untrusted code? Every lease is a fresh hardened container that's destroyed on release; nothing persists.

## 🛡️ How It Makes Tasks Easier, Faster, and Safer

- **One Signature, Not Many (Prepaid + Metered):** You top up once; after that, renting just spends your prepaid balance. No per-action wallet popups, no x402 usage is metered continuously but charged **once at release**, prorated to the exact seconds used.
- **You Give Compute, Never Access:** A contributor never hands over their filesystem or account. The renter only ever touches an ephemeral, hardened Docker container **no host mounts, no host network, nearly all Linux capabilities dropped, `--no-new-privileges`**, plus hard CPU/memory/PID caps — destroyed the instant the lease ends.
- **Nothing To Expose At Home:** The renter reaches the box through a `bore` tunnel that runs *inside* the sandbox, so a contributor never opens a port on their own machine. When the container dies, the tunnel dies with it.
- **No Runaway Bills:** If your balance can't cover the running time, the session stops automatically; worst case, you overrun by a single meter tick.
- **Double-Spend-Proof Ledger:** Deposits are credited idempotently per Algorand transaction ID, so a confirm can never be counted twice, and settlement bills are exactly once on release.

**Challenges we ran into**

**Hardening the sandbox without breaking SSH.** The whole pitch rests on the container being locked down drop nearly every Linux capability, `--no-new-privileges`, no host mounts, no host network. The problem: the moment I actually applied that, `sshd` refused to start. Dropping `setuid`/`setgid` means sshd can't fork a session and demote to the logged-in user, and `no-new-privileges` blocks the privilege transition outright. So I had the choice every "secure sandbox" hits a box nobody can log into, or a box that isn't really sandboxed. I worked through it by treating capabilities as an allowlist instead of "drop all": add back only `CAP_SETUID`, `CAP_SETGID`, and `CAP_CHOWN` (the minimum sshd needs to set up a session), keep everything else dropped, and keep the hard CPU/memory/PID caps. The renter gets a real shell; the container still can't touch the host.

**Getting the renter to the box without the contributor opening a port.** A contributor sharing their PC should never have to port-forward or expose anything on their home network that kills adoption and it's a security footgun. My first version tunnelled from the *host*, which meant the daemon was the thing listening, and that's exactly what I didn't want. The fix was to move `bore` *inside* the sandbox: the tunnel client runs in the ephemeral container, dials out, and the public `host:port` it gets back is what the renter SSHes into. Nothing is ever opened on the contributor's machine, and when the lease ends and the container dies, the tunnel dies with it no dangling exposure.

**Making sure a deposit could never be credited twice.** Balances live off-chain in Neon, credited when the registry confirms an on-chain deposit. Early on a confirm could fire more than once (poll + retry), and that double-credited the balance free money, which is the worst possible bug for a payments system. I made crediting idempotent on the Algorand transaction id: the credit is an upsert keyed on `txid` with a unique constraint, so a repeated confirm is a no-op. Same principle carried into billing usage is metered continuously but charged exactly once at release, prorated to the second, so there's no path to double-charge either.

---

[Himanshu Malik](https://github.com/HimanshuM685)

`2026-06-30`

---

### EurekaAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eurekaai-fb02) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/srini-was-taken/eureka) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://eureka-jee.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Q4O3NZtCsg4) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> EdTech platform to reinforce and test your concept

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-333333?style=flat-square)

**The problem it solves**

## What it does

EurekaAI is an anti-cheat, active-learning AI tutor that refuses to give students the answer. Instead of handing out solutions on demand, it uses four research-backed tools to force genuine understanding:

**Socratic Solver** — Upload any problem and EurekaAI responds with targeted questions, not solutions. Hints escalate only after 3 stuck turns. Hard problems automatically route to a deeper reasoning model. The AI is explicitly prompted to delay answers and track where your reasoning breaks down, session by session.

**Feynman Explainer** — Explain a concept in your own words (text or voice). EurekaAI returns a structured 0–100 score, identifies the exact gaps in your reasoning, and fires a sharp follow-up question to address them. The scoring pipeline outputs structured JSON (score + specific gaps + targeted follow-up), which is a novel implementation with no direct equivalent in existing ed-tech.

**Focus Mode** — A full distraction-free study environment: PDF rendered on canvas with a custom page range selector, drag-to-highlight, drop note pins, built-in Pomodoro timer (25 min sessions), flashcard creator, and quiz generator; all in one screen without switching tabs.

**Mistake Journal** — Every wrong attempt is logged, tagged by concept, and gets an AI-generated root-cause diagnosis. The system tracks resolved vs. unresolved error patterns over time, surfacing your blind spots before exam day.

**Challenges we ran into**

## Challenges I ran into

**Socratic enforcement is prompt-level only.** A sufficiently persistent user can jailbreak the "never give the answer" constraint through multi-turn pressure. I mitigated this with session-scoped context that tracks reasoning progress and re-anchors the prompt at each turn, but it's not airtight.

**LLM hallucination in hints.** Models are more likely to generate a plausible-sounding hint than admit uncertainty — especially in niche JEE chemistry problems. I addressed this by prompting the model to cite which concept the hint is anchored in, making hallucinated hints easier to spot.

**Focus Mode annotation persistence.** Highlights and note pins are session-local until Supabase storage is fully wired. This was the hardest feature to ship at hackathon pace because PDF canvas coordinates need to be serialised and re-mapped on page re-rende, so I prioritised getting the experience right and deferred the persistence layer.

**Groq free-tier rate limits** under concurrent use required debouncing Feynman submissions and adding a queue indicator in the UI so users know their request is processing, not dropped.

Sriniketh Natarajan

`2026-06-30`

---

### RepCoach
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/repcoach-2b76) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gamerboyadarsh-dot/rep-coach) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/lerQb_Ts0NM?si=tw4jcZ6IAZnDXLxg) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/lerQb_Ts0NM?si=tw4jcZ6IAZnDXLxghttps://youtu.be/lerQb_Ts0NM?si=tw4jcZ6IAZnDXLxg) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Real-time AI form coaching — 33 body landmarks, ze

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Sites API](https://img.shields.io/badge/Google%20Sites%20API-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

## The problem

Home fitness has two broken options today:

- **Hiring a trainer** costs $50–150/hour, pricing out most people from getting real, personalized feedback on their movement.
- **Fitness apps** (Nike Training Club, generic workout trackers) just play you a demo video and hope you copy it correctly. They count reps from a phone's accelerometer or manual logging — they have no idea if your actual form is safe.

The result: people train with bad form for months without knowing it, plateau, or get hurt. Research on fitness-related injuries found that **73% happen during unsupervised training** — precisely the moment nobody is there to catch a mistake before it becomes an injury.

## What RepCoach does

RepCoach is a real-time AI form coach that runs entirely in your browser using a standard webcam — no wearables, no app install, no subscription.

- **Live pose tracking** — Google MediaPipe's PoseLandmarker tracks 33 body landmarks at 25–30 fps, running client-side via WebAssembly/GPU. No video is ever uploaded; everything is processed and discarded locally.
- **Real biomechanical grading, not just rep counting** — joint angles are calculated every frame to detect specific form errors: knee valgus (caving in) on squats, hip sag on push-ups and planks, incomplete range of motion on jumping jacks. Errors are flagged on the exact rep they happen, not in a summary afterward.
- **Four supported exercises** — squats, push-ups, jumping jacks (rep-based), and plank holds (time-based isometric tracking).
- **AI Coach chatbot** — answers form questions and can read an uploaded workout-plan PDF to answer questions about it.
- **Progress system** — 7-day activity chart, workout streaks, calorie estimates, personal records per exercise, full workout history.
- **Body metrics** — weight/height input with automatic BMI calculation.
- **Gamification** — unlockable achievement badges, daily streaks, confetti on milestones, voice feedback with selectable coach personality (Supportive / Drill Sergeant), light/dark themes.
- **Accounts** — Firebase Authentication (Google + GitHub sign-in) with Firestore sync across devices, plus a fully offline Guest Mode for trying it instantly with zero signup.
- **Installable PWA** — works like a native app on mobile with no app store required.

## Tech stack

**Frontend:** React 19, TypeScript, Vite, Tailwind CSS, Framer Motion
**Computer vision:** `@mediapipe/tasks-vision` (PoseLandmarker, GPU-delegated, client-side only)
**Backend/data:** Firebase Authentication (Google & GitHub OAuth), Cloud Firestore, `localStorage` for Guest Mode
**Other:** Web Speech API (voice feedback), `react-body-highlighter` (muscle engagement diagrams), `canvas-confetti`, `vite-plugin-pwa`

**Challenges we ran into**

## 1. Rep counting silently failing on one side of the body

**The bug:** Push-up rep counting was hardcoded to only track the user's left elbow/shoulder/wrist. If the camera angle or the user's position meant the left side wasn't clearly visible, the model's confidence dropped and reps simply stopped incrementing — with no error shown, so it looked like the app was just broken.

**Root cause:** A single boolean flag (`isLeftSide = true`) was passed into the rep-detection function instead of dynamically choosing a side.

**The fix:** We now read MediaPipe's per-landmark `visibility` confidence score (which was previously being discarded before it reached the rep-counting logic) and have the app automatically track whichever side — left or right — has higher confidence on a given frame. This made the squat logic, which already evaluated both sides, the template for fixing push-ups too.

## 2. Camera "switching" that wasn't actually switching cameras

**The bug:** The front/rear camera toggle button changed the UI's mirror state, but on several devices the actual video feed never changed — it just flipped the same camera horizontally with CSS.

**Root cause:** Camera selection relied solely on the `facingMode` constraint in `getUserMedia()`. Many browsers and most laptops/desktops with a single webcam silently ignore this constraint and return whatever camera they were already using.

**The fix:** We switched to enumerating actual physical devices with `navigator.mediaDevices.enumerateDevices()` and requesting a specific camera by its `deviceId`, with `facingMode` kept only as a fallback hint. We also properly stop all tracks on the previous `MediaStream` before requesting a new one to avoid "camera already in use" errors, and persist the user's last-selected camera so it's remembered next session.

## 3. Noisy single-frame pose data causing false or missed reps

**The challenge:** Raw per-frame joint angles are noisy — a single bad frame near a rep's threshold angle could trigger a false rep or cause a real rep to be missed entirely, especially right at the top/bottom of a movement.

**The fix:** We added an exponential moving average (EMA) smoothing pass on joint angles before they reach the rep state machine, plus a minimum-visibility confidence gate so frames where a required joint is occluded or off-screen don't get counted toward a state transition at all.

## 4. Building real auth and sync with zero backend server

**The challenge:** This is a fully static, serverless app (hosted on Surge) — there's no backend to handle authentication or store user data conventionally.

**The fix:** We used Firebase Authentication (Google + GitHub OAuth) and Cloud Firestore entirely from the client, with a parallel `localStorage`-backed Guest Mode so the app is fully usable instantly with zero signup friction — useful both for first-time users and for judges trying the live demo without creating an account.

## 5. Mobile responsiveness and last-minute regression testing

**The challenge:** With most development and testing happening on a desktop browser, the dashboard layout in particular wasn't originally built with small viewports in mind, and a few rapid late-stage feature additions (theme toggle, activity chart, muscle diagram) introduced fresh regressions right before submission.

**The fix:** We ran a dedicated mobile-viewport pass (375px/414px) to fix overflow and tap-target issues, and did a full regression sweep across the recently-touched features — including verifying the muscle-engagement diagram renders correctly for all four exercise types, not just the one most recently edited — before final submission.

Adarsh Agrawal

`2026-06-30`

---

### CareerOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/careeros-4abd) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1QmGPNymJSZwnFkeszT9jWgTBd3J3bhjl/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JT_Kz0WbHCc) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Career Intelligence Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

Students today have access to thousands of courses, internships, certifications, and career opportunities, but lack a structured system to understand where they stand and what they should do next.

Career guidance is often fragmented across multiple platforms, making it difficult for students to identify skill gaps, measure readiness, and create actionable career plans.

As a result, many students spend significant time learning without a clear roadmap, leading to inefficient preparation and uncertainty about career progression.

CareerOS addresses this challenge by providing a unified AI-powered platform that evaluates career readiness, identifies growth opportunities, and generates personalized roadmaps tailored to each student's goals.

What It Does:

CareerOS is an AI-powered career intelligence platform designed to help students make informed career decisions and accelerate their professional growth.

Key Features:

• Career Readiness Assessment
• Personalized Skill Gap Analysis
• AI-Generated Career Roadmaps
• Goal-Based Learning Recommendations
• Resume and Portfolio Insights
• Progress Tracking Dashboard
• AI Career Assistant
• Internship and Placement Preparation Support

The platform transforms career planning from guesswork into a structured and measurable process.

**Challenges we ran into**

One of the biggest challenges was designing a meaningful career readiness framework that could provide actionable insights instead of generic scores.

Different career domains require different skill sets, making it difficult to create a flexible evaluation system that remains relevant for software engineering, AI/ML, data science, and other technical fields.

Another challenge was generating personalized recommendations that adapt to individual goals while maintaining consistency and relevance.

We also had to carefully balance AI-generated guidance with structured rule-based logic to ensure recommendations remained practical, transparent, and useful for students.

Building an intuitive user experience while managing complex personalization workflows was another key challenge throughout development.

[Anumeha Paul](https://github.com/Anumeha600)

`2026-06-13`

---

### Signal-API Playground
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/apiplayground-c772) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/marrupushya01-hub/signal-api-playground) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://signal-api-playgrounds.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3EY3cpNSiCY) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A lightweight browser-based API testing tool

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**Challenges we ran into**

**CORS restrictions**-Since Signal runs entirely in the browser, APIs that don't set CORS headers block requests. We documented this as a known limitation and framed it honestly rather than hiding it behind an unstable proxy.

**Coordinating a 3-person Git workflow**-Two teammates pushed to forks instead of cloning directly, which caused merge conflicts. We resolved this by fetching their branches manually and merging with `--allow-unrelated-histories`.

**Splitting components cleanly**-Designing the architecture so three people could work on separate files (UrlBar, RequestPanel, Sidebar, Modals) without stepping on each other required careful planning upfront.

**The problem it solves**

During fast-paced hackathons, developers waste time downloading and configuring heavy desktop tools like Postman just to test a simple API endpoint.

Signal solves this by being a **zero-install, browser-based API playground**. Open the link and start testing instantly-no setup, no account, no backend required.

- Test GET, POST, PUT, PATCH, DELETE requests with headers, auth, and body
- Mock mode lets you fake responses when your backend isn't ready yet
- History and collections saved automatically to localStorage-no login needed
- Generate ready-to-use code in cURL, Fetch, Axios, or Python in one click
- Share any request with a teammate via a single link

Team **The Byte Alchemists** -- [Pusya Maru](https://github.com/marrupushya01-hub), [Mousumi Behera](https://github.com/mousumi442), [Mahesh Kumar Sahu](https://github.com/Mahesh-forcode)

`2026-06-15`

---

### Syntax Saga
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/buildandgame-c27d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://syntaxsaga-arena.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GVvfabu3AtE?si=_67DZBXUGzt23aNn) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Start as a Rookie. End as a Legend.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Pymongo](https://img.shields.io/badge/Pymongo-333333?style=flat-square)

**Challenges we ran into**

Building a live Remote Code Execution (RCE) engine in 24 hours is incredibly difficult. Here are the major hurdles we cleared:

1. The 64-Bit Database Explosion (MongoDB Overflow)
To scale our platform to 100 unique questions without hardcoding, we built a Python procedural generator (seed.py). However, during the generation of the "Hard Tier," our exponential math paradigms calculated massive numbers (e.g., 1000  100). While Python handled this instantly, it triggered a fatal OverflowError when inserting into MongoDB, as BSON is strictly capped at 64-bit (8-byte) integers.

How we got over it: We refactored the generator to use mathematically complex but overflow-safe operations (like modulo, bitwise shifts, and floor division) to maintain the difficulty without breaking the database architecture.

2. Safely Compiling 5 Languages on the Fly
Executing raw, untrusted user code in C, C++, Java, Node, and Python on a single server is a massive security and resource risk. We had to ensure a user's infinite loop wouldn't crash the entire platform.

How we got over it: We utilized Python's subprocess module with strict temporal timeouts, automatically terminating any execution that exceeded 4 seconds. Furthermore, we containerized the entire backend using Docker, installing the native compilers (GCC, G++, OpenJDK) directly into a Linux image to ensure isolation and cross-platform reliability.

3. The Production Deployment Bridge
Bridging a serverless frontend (Vercel) to a heavy, stateful compiler backend (Render) created immediate deployment friction. We faced strict TypeScript build errors (TS6133), live CORS blocking, and 500 Internal Server Errors when the Render container tried to access our MongoDB Atlas cluster.

How we got over it: We implemented dynamic environment variables (API_URL) to easily swap between local and production states, resolved the TypeScript strictness flags, and properly configured MongoDB Atlas IP whitelisting (0.0.0.0/0) so our dynamic Render container could securely persist user XP and solved statuses.

**The problem it solves**

Standard coding platforms and technical screening tools suffer from a major flaw: they only test a developer's ability to write code from a blank slate. In the real world, engineers spend just as much time reading, debugging, and patching legacy code as they do writing new functions.

Syntax Saga solves this by offering an immersive, gamified coding environment that tests both sides of the engineering coin through two distinct tracks:

Builder Labs: Traditional logic construction where developers build scalable solutions from scratch to pass strict memory bounds and hidden test cases.

Breaker Labs: Real-world bug hunting. Users are presented with pre-written algorithms containing subtle logic flaws or syntax errors. They must read, diagnose, and patch the code.

By combining an enterprise-grade UI (powered by the Monaco Editor) with live multi-language execution (Python, JS, C, C++, Java) and an XP-based progression system, Syntax Saga makes technical learning and candidate screening far more engaging, realistic, and comprehensive.

Team **TripleThreat** -- [Bhoomi Koli](https://github.com/bhoooomi05), [Jibin Joseph](https://github.com/Jibin-7), [Ananya Kotian](https://github.com/ananyakotian264)

`2026-06-15`

---

### FA-PQWC
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fapqwc-9685) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tanaymitra54/Finality-Aware-Post-Quantum-Witness-Compaction) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1201125501?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Run post-quantum signatures on-chain without blow

![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Networking](https://img.shields.io/badge/Networking-333333?style=flat-square) ![CLI](https://img.shields.io/badge/CLI-333333?style=flat-square) ![Erasure coding](https://img.shields.io/badge/Erasure%20coding-333333?style=flat-square) ![Post-quantum crypto](https://img.shields.io/badge/Post--quantum%20crypto-333333?style=flat-square)

**Challenges we ran into**

Getting Falcon and SLH-DSA to play nice under a unified trait was surprisingly painful. Each PQ crate exposes a different API different key types, different signing conventions, different error handling. We ended up writing a thin wrapper layer that normalizes everything to a common KeyPair + AuthenticationWitness interface, but the type gymnastics took several iterations to get right.
The canonical codec was another rabbit hole. Post-quantum signatures are variable-length (SLH-DSA signatures range wildly depending on the message), and our encoder originally rejected any payload over a hardcoded limit. Switched to length-prefixed bounded vectors with a configurable MAX_WITNESS_BYTES  cleaner, safer, and future-proof.
And then there was the migration automaton. Allowing accounts to transition classical → hybrid → PQ-only while guaranteeing no downgrade attacks (e.g., a compromised validator convincing an old node to accept a classical signature on a PQ account) required encoding the policy state directly into the state root. Once we committed policy to the hash, everything clicked  you can't lie about what scheme an account accepts.

**The problem it solves**

FA-PQWC: Finality-Aware Post-Quantum Witness Compaction
The Problem It Solves
Post-quantum signatures (ML-DSA, Falcon, SLH-DSA) are 10–270x larger than ECDSA signatures. Naively dropping them into an Ethereum-account blockchain means every full node stores every signature forever — storage costs explode, and the network becomes impractical.
FA-PQWC provides a reference architecture for PQ-safe blockchains without the storage nightmare. The core insight: separate transaction data from authentication witnesses, verify PQ signatures on the consensus path (before finality), then prune witnesses from compact nodes after finality. Archive nodes retain erasure-coded shares for auditability.
What you can use it for:
Blockchain researchers — study a working prototype of witness compaction with 5 signature schemes
Protocol designers — benchmark real PQ signature performance (keygen, sign, verify, block build/verify at scale) to make informed tradeoffs
Layer-1 engineers — evaluate the monotonic account migration automaton that prevents quantum-downgrade attacks when transitioning from classical → hybrid → PQ-only
Cryptography engineers — inspect the canonical binary codec, domain-separated hashing, and erasure-coded archival design
Key benchmark results with Falcon-512:
3× faster verification than ECDSA (22.5 μs)
Smallest PQ signature at just 659 bytes
Full PQ security on the consensus path
Built with: Rust + libp2p + Tokio + Axum
GitHub: https://github.com/tanaymitra54/Finality-Aware-Post-Quantum-Witness-Compaction

Team **LaLaWorld** -- [Tanay Mitra](https://github.com/tanaymitra54), [Adithyan .K.R](https://github.com/Arekes101), [SOUMYA GOEL](https://github.com/soumyagoel11)

`2026-06-14`

---

### BugOps Arena — AI Debugging Game
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bugops-arena-aipowered-realtime-debugging-game-b245) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AnuragSanyal7439/bugops-arena) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://bugops-arena.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Fix bugs. Beat the clock. Learn faster with AI.

![Next.js, React.js, Tailwind CSS, JavaScript, Framer Motion, LocalStorage, Gemini API, Firebase/Supabase-ready Leaderboard, Vercel, Git, GitHub](https://img.shields.io/badge/Next.js,%20React.js,%20Tailwind%20CSS,%20JavaScript,%20Framer%20Motion,%20LocalStorage,%20Gemini%20API,%20Firebase/Supabase--ready%20Leaderboard,%20Vercel,%20Git,%20GitHub-333333?style=flat-square)

**The problem it solves**

Many beginners learn programming syntax, but they struggle to debug code confidently. Traditional practice platforms often feel repetitive and less engaging, and learners do not always get instant guidance when they make mistakes.

BugOps Arena solves this by turning debugging practice into an interactive browser-based game. Users fix buggy code under time pressure, earn XP, use hints, track progress, and improve their problem-solving skills through a fun and competitive web experience.

The project combines learning, productivity, gameplay, real-time competition, and AI-powered assistance into one modern platform.

**Challenges we ran into**

One of the biggest challenges was combining many different ideas into one smooth experience: an interactive website, debugging game, productivity dashboard, leaderboard, creative UI, and AI-powered hints. I had to make sure the project did not feel like separate sections, but like one complete platform.

Another challenge was building the game logic properly, including timer, score, lives, XP, difficulty levels, and result tracking. Managing user progress with localStorage also required careful handling so that dashboard stats, accuracy, streaks, and leaderboard data stayed consistent.

The AI hint system was also challenging because the hints had to be useful without directly revealing the full answer. To solve this, I added fallback predefined hints and explanations so the app can still work even if the AI API is unavailable.

I also focused a lot on frontend polish. Creating a futuristic cyberpunk interface with animations, glowing cards, responsive layout, and game-like interactions took time, but it helped make BugOps Arena feel like a next-generation web experience rather than a basic coding quiz.

[Anurag Sanyal](https://github.com/dashboard)

`2026-05-28`

---

### ShopEase - Full Stack E-Commerce Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shopease-full-stack-ecommerce-platform-d6df) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shopease-iucm.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Shop Smarter, Faster.

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Postman](https://img.shields.io/badge/Postman-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square)

**The problem it solves**

ShopEase solves the problem of managing online shopping and store administration in one platform. It helps customers easily browse products, search and filter items, add products to cart, choose payment methods, place orders, and view order confirmation.
For store admins, it provides a dashboard to manage products, categories, users, orders, payments, revenue, and reports. This reduces manual work and makes e-commerce management faster, simpler, and more organized.

**Challenges we ran into**

While building ShopEase, I faced several technical and design challenges.

One of the major challenges was implementing a complete e-commerce workflow that included product management, shopping cart functionality, checkout, payment processing, and order management while maintaining a smooth user experience.

Another challenge was managing communication between the frontend, backend, and MySQL database. Ensuring data consistency for products, users, carts, and orders required careful API design and testing.

Building the admin dashboard was also challenging because it involved handling multiple modules such as products, categories, orders, users, coupons, reports, returns, and replacements within a single interface.

I also faced UI and responsiveness issues while designing pages for different screen sizes and ensuring a consistent user experience throughout the platform.

These challenges were addressed through continuous testing, debugging, database optimization, API validation, and iterative UI improvements. The experience helped improve problem-solving skills, full-stack development knowledge, and understanding of real-world e-commerce systems.

Dhanush R

`2026-05-29`

---

### HACKANIZER
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hackanizer-a0bc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SharmisthaHalder57/Hackanizer) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/m50WrhSq60I) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> One Platform. Seamless Events. Everyone Connected.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Large-scale events often struggle with attendee management, meal distribution, and real-time coordination. Traditional methods such as paper coupons, manual verification, and spreadsheets are prone to delays, duplication, misuse, and lack of visibility for organizers. Our platform digitizes these processes through role-based management, QR-powered meal verification, and a live dashboard, enabling secure, efficient, and transparent event operations.

**Challenges we ran into**

1. Preventing Duplicate Meal Claims: Since the same meal QR code is shared among all attendees, ensuring that a user could not claim the same meal multiple times required robust backend validation and database checks.

2. Real-Time Status Synchronization: One of the biggest challenges was updating the user's meal status and the organizer dashboard instantly after a QR scan. We implemented real-time communication to ensure data consistency across all interfaces.

3. Managing Multiple User Roles: The platform supports Participants, Judges, Mentors, Volunteers, and Organizers. Designing a scalable role-based access system while maintaining a smooth user experience was challenging.

4. QR Verification Workflow: Creating a seamless flow where QR codes appear instantly upon meal claim requests and are verified efficiently at food counters required careful API and state-management design.

5. Concurrency Handling: During peak meal hours, multiple users may attempt to claim meals simultaneously. Handling concurrent requests without creating duplicate records or race conditions was an important technical challenge.

6. Dashboard Data Accuracy: Ensuring that organizers always see the latest meal claim statistics and attendee information required efficient database querying and synchronization mechanisms.

7. Hackathon Time Constraints: Building authentication, role management, QR workflows, database integration, and a live organizer dashboard within a limited hackathon timeframe required rapid prototyping and prioritization of core features.

**Open Innovation**

Our solution addresses a common challenge faced across hackathons, conferences, festivals, workshops, and other large-scale events. It is not limited to a specific industry or domain and can be adapted to various use cases involving attendee management, resource distribution, and real-time monitoring. Since the platform has broad applicability and can create value across multiple sectors, it aligns well with the Open Innovation track.

Team **Hojoborolo** -- [Sharmistha Halder](https://github.com/SharmisthaHalder57), [Soumyadeb Nandy](https://github.com/Soumdeb), [Soham Mazumder](https://github.com/devbysoham), [Divya Mondal](https://github.com/Divya-Mondal-14), [Srineeja Bhowmick](https://github.com/srineeja)

`2026-05-31`

---

### LogwatchAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/logwatchai-9899) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kumariluckyraj/logwatchai_ju) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/12HXYow4CoRRgvEjF7KXY5r7fP_tpnCMy/view?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Self-healing reliability platform for deployments

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Canary deployments are dangerous without intelligence when you push a new backend version and route real user traffic to it, failures are invisible until damage is already done. Engineers find out through user complaints, not systems. LogWatchAI detects failure spikes in real time and acts before users notice.

Manual rollback is too slow and too human-dependent traditional incident response requires someone to be awake, read alerts, understand the logs, make a decision, and manually execute a rollback. At 3am this takes 20-40 minutes minimum. LogWatchAI does the entire cycle in under 2 seconds with zero human involvement.

Log analysis is a manual, expertise-heavy task reading hundreds of log lines, identifying patterns, clustering similar failures, and forming a root cause hypothesis requires senior engineering experience. LogWatchAI automates this entirely  it clusters failures, identifies root causes, estimates business impact, and suggests exact fixes using RAG-powered AI analysis.

Code bugs cause downtime even after rollback rolling back traffic to stable stops the bleeding but doesn't fix the broken code. The same deployment will fail again next time. LogWatchAI's Patch Agent reads the actual broken file, generates a corrected version using an LLM, validates it, creates a git checkpoint, and writes the fix to disk autonomously.

Network failures look identical to code bugs in logs  a closed port and a database error both produce 502/500 responses. Without network visibility, engineers waste time debugging code when the real issue is a service simply not running. LogWatchAI integrates real Nmap scanning to distinguish network failures from application failures before attempting any code patch.

**Challenges we ran into**

Trigger Agent rolling back in an infinite loop after the first successful rollback, the error tracker's in-memory sliding window still contained all the pre-rollback bad requests. Error rate showed 35% even though traffic had already switched to stable. The agent kept firing the rollback action every second. Fixed with a 60-second cooldown and a minimum request threshold the agent cannot act again until the window has had time to flush stale data and reflect the actual current state.


 A key security challenge we addressed was ensuring logs never reach external APIs in raw form since production logs regularly contain passwords, Bearer tokens, JWT signatures, database connection strings, and PII, we built a sanitization layer that pattern-matches and redacts all sensitive data before any log entry is embedded into Pinecone or included in a Groq prompt, ensuring that even if a third-party service were breached, no credentials or user data would be exposed.

**Open Innovation**

LogWatchAI fits the Open Innovation track because it takes an unsolved problem in infrastructure engineering and approaches it in a way that has never been done before not by improving an existing tool, but by combining technologies from completely different domains into one autonomous system. We took vector databases from the AI search space, LLM inference from generative AI, network scanning from cybersecurity, and canary deployment management from DevOps and connected them into a single self-healing pipeline that no existing product offers. Open Innovation means solving real problems without being constrained to a specific domain or predefined solution and that is exactly what this is. Every engineering team on the planet deals with production failures, rollbacks, and incident response, yet no tool today detects, diagnoses, rolls back, patches code, and scans the network autonomously in one unified flow. We identified that gap and built the solution from scratch by innovating across discipline boundaries AI, security, DevOps, and systems engineering simultaneously which is the definition of open innovation.

Team **Syntax Squad** -- [Kashish Roy](https://github.com/KASHISHROY), [Kumari Lucky Raj](https://github.com/kumariluckyraj), [Enaitul Hoque](https://github.com/enaitul), [Ritwika Dey](https://github.com/Ritwika-dey)

`2026-05-31`

---

### Nexinspect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexinspect-4618) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AishikMondal/Nexinspect2) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> See Beyond Chrome DevTools

![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

Nexinspect is fragmented and overly technical. Developers constantly switch between Chrome DevTools, Lighthouse, accessibility scanners, security analyzers, and performance profilers just to understand why a website feels slow or broken.
Even after collecting all the metrics, developers still need to manually identify:
i)what caused the issue
ii)how severe it is
iii)and how to fix it.


Our extension solves this by combining:
i) performance diagnostics
ii) accessibility analysis
iii) security auditing
iv) network inspection
v) AI-powered root cause analysis

into a single real-time sidebar interface.

**Challenges we ran into**

One major challenge was collecting low-level browser diagnostics directly inside a Chrome extension without relying entirely on Chrome DevTools.

Chrome extensions have API limitations, especially around:
i) performance profiling,
ii) memory inspection,
iii) network interception.

To overcome this, I combined multiple browser APIs such as:
i) PerformanceObserver,
ii) MutationObserver,
iii) Chrome WebRequest APIs,
iv) runtime instrumentation techniques.

Another challenge was organizing large amounts of runtime data into a clean and usable UI. Since performance, accessibility, security, and network data update continuously, maintaining real-time synchronization without making the extension laggy required careful state management and optimization.

I also faced difficulties in converting raw technical metrics into meaningful insights. Instead of only showing numbers like CLS or TTFB, I had to design an AI-assisted interpretation layer that explains:
i) why an issue happens,
ii) its impact on user experience,
iii) and possible fixes.

Team **Hackbuzz** -- [Aishik Mondal](https://github.com/AishikMondal), [Hiya Sarkar](https://github.com/hiyasarkar), [Aishika Chakra](https://github.com/AISHIKA-CHAKRA)

`2026-05-31`

---

### Client flow_ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/client-flowai-daba) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://preview-chat-7045c1f3-81aa-4b6d-bfe8-cf7c940401f1.space-z.ai/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fDymrE6s8bs?si=2iY0wnyZJ0CLMFCY) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-powered client workflow automation for smarter

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square)

**The problem it solves**

This project solves the problem of inefficient and fragmented client workflow management by providing an AI-powered platform that streamlines communication, task handling, and workflow automation in one place.

Many users and teams struggle with managing repetitive tasks, coordinating client interactions, and maintaining productivity across multiple tools. Our solution simplifies this by offering an intelligent web-based system that automates workflows, improves response efficiency, reduces manual effort, and creates a smoother user experience.

By combining AI assistance with an intuitive interface, the platform helps users save time, improve organization, and make workflow management faster and more reliable.

**Challenges we ran into**

During development, we faced challenges with deployment configuration, dependency management, and integrating AI-driven workflow logic smoothly across the frontend and backend. Since the project uses multiple technologies including Next.js, React, Prisma, and Tailwind CSS, ensuring compatibility between packages and resolving build/runtime errors was a key hurdle.

Another challenge was optimizing the user flow and making the interface intuitive while maintaining performance. We solved these issues through iterative debugging, testing different configurations, refining the architecture, and improving the UI/UX based on repeated testing.

**Using LocusFounder to Build a Business!**

This project fits this track because we used the Locus ecosystem to rapidly build and validate a business-focused AI solution. The platform helped us accelerate development, prototype quickly, and focus on solving a real workflow problem for users and businesses. Our project is designed as a practical SaaS-style solution that improves client workflow management through automation and AI assistance.

Team **Zynk studio** -- Mohammed Khan, Hammad Khan

`2026-05-16`

---

### Leetdell
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/leetdell-3171) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/acharnikhil72-commits/LEETHNUTH.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://leetdeil.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Delivery Intelligence System

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square) ![Hibernate](https://img.shields.io/badge/Hibernate-333333?style=flat-square)

**The problem it solves**

In India's last-mile delivery ecosystem, delivery boys are paid a fixed daily wage to complete 25+ deliveries — but up to 40% of attempts fail due to unreachable customers, cash-on-delivery fraud, and wrong-time deliveries. These failed attempts waste fuel, time, and money, with companies absorbing the cost silently.

Leetdell solves this by predicting delivery failure before the boy even leaves.

By taking inputs like delivery area, time slot, weather, and payment type, Leetdell uses logistic regression trained on real feedback data to calculate a risk score for each delivery. If the risk crosses 60–70%, the app alerts the manager to confirm the order first — preventing wasted trips entirely.

The result: fewer returns, better delivery completion rates, and an estimated 5% reduction in daily operational losses — all without changing how delivery companies already work.

**Challenges we ran into**

**Technical Challenges:**

We built Leetdell as a Java Spring Boot backend with HTML frontend, but Render doesn't natively support Java deployment. We solved this by learning Docker, containerising our application, and deploying via Docker images — which taught us valuable lessons in DevOps and cloud infrastructure.

Database connectivity was another hurdle. We used Render's free PostgreSQL tier, which had initial connection latency issues, but persistence paid off and it stabilised.

**Strategic Challenge — Cost vs. Impact:**

We initially considered using advanced AI models, but realised that if the operational savings are only five percent whilst AI running costs consume ten percent of revenue, the business case collapses. So we chose logistic regression instead — a lightweight, interpretable model that delivers real value without burning resources. Sometimes the smartest solution isn't the fanciest one.

**Using LocusFounder to Build a Business!**

Leetdell is built directly on the LocusFounder vision — turning a real-world logistics problem into a scalable business solution. Delivery companies in India lose significant revenue daily due to failed deliveries caused by unreachable customers, fraud cash-on-delivery orders, and poor route planning. Leetdell addresses this by using logistic regression to predict delivery failure risk based on area, time slot, weather, and order type — helping managers confirm high-risk deliveries before dispatch.
The business model is clear: delivery companies save at least 5% of operational costs by eliminating wasted trips, fuel, and misallocated daily wages. Instead of paying a delivery boy ₹500 for 15 successful deliveries, they now get closer to the full 25 — maximising output per rupee spent.

This is not just a tech project — it is a deployable, cost-effective SaaS tool built for logistics startups and delivery companies ready to optimise their last-mile operations.

Team **Leethnut** -- [Nikhil S Achar](https://github.com/acharnikhil72-commits), Kusuma M

`2026-05-17`

---

### Swarm KeyDB
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/swarm-keydb-6071) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/scholtz/swarm-keydb/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.nuget.org/packages/SwarmKeyDb.SwarmConsistency) [![Built at](https://img.shields.io/badge/Built%20at-ETHPrague%202026-0052CC?style=flat-square)](https://ethprague2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Redis with decentralized storage

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kubernetes](https://img.shields.io/badge/Kubernetes-333333?style=flat-square) ![C#](https://img.shields.io/badge/C#-333333?style=flat-square)

**The problem it solves**

We created new redis implementation which is more resilient to concurrent drive failures as it is using the decentralized storage Swarm for each instance. Supports all redis interface commands to put, delete, batch operations, pubsub, and lua scripting.

We also created nuget library for resiliancy check of the incomming data from a storage server.

The app is published to the docker hub, and provides helm charts for easy installation to kubernetes.

We also created more tools such as the migration tool from other redis database and many examples in c#, react, node, go and python.

Many use cases are heavily documented such as the deployment, local docker run, or kubernetes deply.

CICD checks for more than 300 tests passing on windows, unbuntu and mac builds and also checks the sdk tests passing in c#, js, go and python.

**Challenges we ran into**

We enjoyed building and did not struggle with anything. Goal was clear.

**Network Economy**

We created redis implementation which is using Swarm as the data storage. This increases the high availabilty and resiliancy of the redis stored data. We created tools which migrate existing persistant redis databases to swarm-keydb database. Many examples in c#, node, python and go, and documented everything properly.

**Verified Fetch — Trust No Gateway**

We created .NET library for verification of data received from bee and created CICD pipelines which updates the nuget package with the current implementation

**A Simple Key-Value Store on Swarm**

We created redis implementation which stores data to swarm

Team **Swarm KedDB** -- [Ludovit Scholtz](https://github.com/scholtz/), Petr Pavlis

`2026-05-10`

---

### Traffic Priority Smart Monitoring Controller
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/traffic-priority-and-smart-monitoring-controller-tpsmc-d978) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/akhil053/TPSMC) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LpA9YjrIMjU) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Traffic that thinks. Roads that react.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

**The problem it solves**

Emergency Green Corridor — siren detected → signals auto-clear the route to hospital
 Auto Accident Dispatch — crash sensors trigger a countdown, picks best hospital, sends victim info ahead
 Real-Time Congestion Scoring — fuses PIR, mic, gas & vibration into a live 0–100 score per junction
ML Route Suggester — shows fastest vs. safest path using a custom neural net
Remote Signal Override — force RED/GREEN or clear a corridor from the dashboard instantly
Live City Map — all junctions, hospital markers, congestion rings, and alert feed in one view
Air Quality & Noise Alerts — hyperlocal AQI + dB tracking at each junction
Offline Fallback — switches to SMS dispatch and cached data when internet is down

**Challenges we ran into**

FPGA IIR Filter Scaling — siren thresholds that passed in simulation failed on real hardware due to fixed-point scaling mismatch; fixed constants in the Verilog and corrected the testbench siren/accident priority conflict

Congestion Scores — frontend was fabricating sensor values for offline junctions (score * 1.7 for AQI etc.); replaced entire client-side scoring with a deterministic backend model with a data_source badge

ML Panel vs. Toolbar Button Overlap — floating panel sat exactly on top of the TRAFFIC LAYER button at certain widths; moved panel to right-center, locked toolbar to flex-wrap: nowrap

Route Lines Invisible Under Traffic Layer — ML and hospital routes blended into Mapbox road tiles; fixed with line-offset staggering + glow halo layers + traffic layer opacity dimming when routes are active

ESP32 UART2 / USB Serial Conflict — debug logs mixed into sensor packets the PYNQ was reading; moved sensor stream to GPIO17/16 (UART2), kept USB for debug only

Dispatch Sending to a Busy Hospital — distance-only logic picked the nearest hospital even if it had 2 beds and was BUSY; replaced with priority ranking (TRAUMA_READY > AVAILABLE > BUSY) then ETA

**Internet of Things**

Layer 1 — Sense (ESP32)

PIR, microphone, MQ-135 gas & vibration sensors read the physical world
Sends raw DATA, PIR, MIC_AVG, MIC_PEAK, GAS, VIB over UART every 2s
Layer 2 — Edge Process (PYNQ-Z2 FPGA)

FPGA runs IIR filters + threshold logic in hardware — no cloud round-trip
Classifies alerts (CLEAR / SIREN / ACCIDENT etc.) in microseconds
Hardware watchdog resets the system if it freezes (every 150ms)
Layer 3 — Communicate (MQTT)

FPGA bridge publishes processed JSON to traffic/edge topic
Server sends commands back to junctions via traffic/command (e.g. FORCE_GREEN)
Bidirectional, lightweight — standard IoT protocol
Layer 4 — Act & Visualise (Flask + Dashboard)

Flask consumes MQTT, runs ML routing, triggers emergency dispatch
Dashboard shows live map, congestion scores, alerts — all from real sensor data
Actions loop back to hardware: siren detected → MQTT command → junction turns green
In short: Physical sensors → Edge FPGA → MQTT → Cloud logic → Real-world actuation. That's a complete IoT feedback loop.

Team **Super_Nova** -- [Sachin Kumar](https://github.com/Sachin22mishra), [Gyan Prakash](https://github.com/gyanprakash53), [Kumar Akhil](https://github.com/akhil053)

`2026-05-10`

---

### Business platform for Women Artisans
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/business-platform-for-women-artisans-36a5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tejaswini-Mallikarjun-Patil/kalaasetu) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_qia-fIIiEY?si=nBbz764JYS8Dcoe8) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Empowering Women Artisans

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![scikit-learn library](https://img.shields.io/badge/scikit--learn%20library-333333?style=flat-square)

**The problem it solves**

This platform is designed especially to support women artisans and small handicraft businesses by helping them make informed business decisions using AI-powered recommendations. Many women-led artisan businesses struggle with pricing products, identifying the right selling platforms, understanding market demand, and accessing digital business tools. Existing solutions are often generic and not tailored to their specific needs.

Our system simplifies this process by allowing users to describe their handmade products in simple language. The platform analyzes the product, asks follow-up questions if details are missing, predicts suitable pricing and demand, estimates profit, and recommends the best marketplaces such as Etsy or Instagram. By combining machine learning, explainable AI, and live market insights, the platform reduces manual market research, improves decision-making, and makes digital business guidance more accessible, especially for women entrepreneurs and artisans.

**Challenges we ran into**

1.Organizing the backend architecture into modular folders and services
2.Understanding how trained .pkl models, TF-IDF vectorizers, and label encoders connect together
3.Testing API endpoints using Swagger/OpenAPI for the first time
4.Deciding between static ML predictions and live market data integration

**AI & ML**

Our project fits this track because it directly solves real operational and growth problems faced by local artisans and small handmade product businesses using AI-powered automation, multilingual communication, and accessible digital tools.
1.It uses AI to simplify business operations such as product recommendations, pricing suggestions, customer support, inventory understanding, and sales assistance.
2.It supports multilingual communication, making the platform accessible to regional-language users who are usually excluded from advanced digital platforms.It helps artisans expand market reach by generating product descriptions, marketing content.

Team **HackNova** -- [Nidhishree N](https://github.com/nidhi-shree), [Harshitha S](https://github.com/Harshitha-44S), [Afifa Taskeen](https://github.com/AfifaTaskeen), [Tejaswini Patil](https://github.com/Tejaswini-Mallikarjun-Patil)

`2026-05-10`

---

### AgentShield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentshield-469c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Akash-lamani/agentshield18) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=ycXzaozSISI) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Cybersecurity Platform for AI Agent Auditing

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![CI/CD](https://img.shields.io/badge/CI/CD-333333?style=flat-square) ![Commander.js](https://img.shields.io/badge/Commander.js-333333?style=flat-square)

**The problem it solves**

AgentShield solves the emerging cybersecurity risks of autonomous AI agents used in coding, automation, and enterprise workflows. Modern AI agents can access filesystems, execute shell commands, connect to APIs, browse the web, and interact with external MCP tools — creating a completely new attack surface that traditional security tools cannot properly protect.

Our platform specifically detects AI-native threats such as prompt injections, malicious MCP servers, exposed API keys, unsafe hooks, dangerous tool execution, and autonomous workflow exploitation.

AgentShield combines static analysis, taint analysis, secret scanning, prompt injection detection, MCP auditing, and an adversarial AI pipeline with attacker, defender, and auditor agents to proactively identify vulnerabilities and secure AI agents before deployment.

**Challenges we ran into**

# Challenges I Ran Into

1. Building the CLI Security Engine
Creating a modular CLI scanner capable of scanning multiple configuration formats was difficult. The project needed to analyze files such as `CLAUDE.md`, `settings.json`, `mcp.json`, `.env`, and agent skill files while supporting multiple AI-agent frameworks.

I solved this by designing the backend in a modular structure where each security feature was separated into independent rule modules. This made the scanner easier to maintain, scale, and extend with new security checks.

---

2. Detecting Prompt Injection Vulnerabilities
One major challenge was identifying prompt injection patterns inside AI configuration files and skill definitions. Traditional security scanners are not designed to understand AI-specific attacks such as hidden instructions or jailbreak prompts.

I solved this by creating custom scanning rules and injection test cases based on OWASP LLM Top 10 attack patterns.

---

 3. Taint Analysis for Unsafe Data Flow
Tracking how untrusted input flows into dangerous operations such as shell execution or network requests was technically challenging.

To solve this, I built a taint-analysis engine that tracks data from sources like user input and environment variables to dangerous sinks like `curl`, `exec`, and shell commands.

---

4. Managing False Positives in Security Scanning
During development, many safe configurations were incorrectly flagged as vulnerabilities, which reduced scan accuracy.

I improved this by adding severity scoring, confidence weighting, and context-aware validation to reduce unnecessary alerts and improve the reliability of scan results.

**Open Innovation**

AgentShield fits the Open Innovation track because it addresses a real and emerging industry problem in AI security using an open, extensible, and developer-focused approach.

As AI agents become more autonomous and widely used, there is a growing need for tools that can secure them against prompt injection attacks, unsafe tool execution, exposed secrets, malicious MCP servers, and runtime misuse. Existing cybersecurity tools are not specifically designed for AI-agent ecosystems.

AgentShield contributes to open innovation by providing:
- an extensible CLI-based AI security platform
- modular security rule architecture
- OWASP LLM Top 10 aligned security analysis
- runtime monitoring and policy enforcement
- support for multiple AI-agent frameworks such as Claude Code, LangChain, CrewAI, and OpenAI SDK

The project is designed to be easily extendable, allowing developers and researchers to add new security rules, analysis modules, and framework integrations as AI technologies evolve.

By combining AI security research, cybersecurity practices, and developer tooling into an accessible platform, AgentShield encourages collaborative innovation and helps improve the safety of future autonomous AI systems.

Team **AgentX** -- [Akash Lamani](https://github.com/Akash-lamani), [Prajwal R_T](https://github.com/PrajRT19), [AP Likhith Ponnappa](https://github.com/ap-likhith), [Balaji Durgasa Katwe](https://github.com/BALAJIDKATWE)

`2026-05-10`

---

### CamSense AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aotians-5e98) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CamSense-AI) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Transforming traditional CCTV into an intelligent

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# CamSense AI - Smart CCTV Intelligence Platform

## Overview

CamSense AI is an AI-powered smart surveillance and automation platform that transforms traditional CCTV systems into intelligent real-time monitoring systems.

The platform combines:

* Weapon detection
* Human detection
* Attendance monitoring
* Unknown person detection
* Energy optimization
* Smart surveillance analytics

using a single AI-powered CCTV infrastructure.

---

# What Problems Does It Solve?

Traditional CCTV systems only record footage and require constant manual monitoring. Security teams must spend hours reviewing video recordings to detect incidents.

CamSense AI automates this process using Computer Vision and Artificial Intelligence.

The system can:

* detect dangerous objects in real time,
* identify authorized and unauthorized individuals,
* automate attendance,
* optimize electricity usage,
* and generate instant alerts during suspicious activities.

---

# Key Features

## 🔫 Weapon Detection

The system detects:

* knives
* guns
* dangerous weapons

in real-time CCTV footage using a trained YOLO-based AI model.

If a weapon is detected:

* an alert is generated,
* snapshots are saved,
* and administrators are notified instantly.

This helps improve safety in:

* schools
* colleges
* offices
* public places
* restricted zones

---

## 👤 Human Detection & Occupancy Monitoring

The platform detects whether humans are present inside a room.

Using real-time occupancy analysis:

* lights and fans are automatically turned OFF when rooms become empty,
* reducing unnecessary power consumption.

This creates an intelligent energy-efficient environment.

---

## 🧠 Attendance Monitoring

The system uses AI-based face recognition for automated attendance.

Workflow:

1. Verified students/staff are registered.
2. Face embeddings are stored securely.
3. Live CCTV feed performs real-time face recognition.
4. Attendance is marked automatically.

This removes:

* manual attendance systems,
* proxy attendance,
* and unnecessary paperwork.

---

## 🚨 Unknown Person Detection

If an unregistered or unauthorized person enters:

* the system detects the unknown face,
* saves a snapshot,
* logs the event,
* and generates an admin alert.

This adds an extra security layer to institutions and workplaces.

---

## ⚡ Smart Energy Optimization

The system intelligently controls:

* lights
* fans
* room occupancy automation

based on real-time human presence detection.

Benefits:

* reduced electricity waste
* lower operational costs
* sustainable energy management

---

# Real-World Applications

CamSense AI can be used in:

* Schools & Colleges
* Smart Classrooms
* Offices
* Laboratories
* Libraries
* Hostels
* Government Buildings
* Restricted Security Areas
* Smart Campuses

---

# Why Is It Useful?

## ✅ Improves Safety

Real-time weapon detection and unauthorized person alerts improve security response time.

## ✅ Saves Energy

Automatic device control reduces electricity wastage significantly.

## ✅ Reduces Manual Monitoring

AI automates surveillance tasks that usually require human operators.

## ✅ Faster Incident Detection

Security incidents can be identified instantly instead of reviewing hours of footage manually.

## ✅ Scalable Architecture

The same CCTV infrastructure can support multiple intelligent AI modules.

---

# Technologies Used

* YOLOv11 / YOLOv8
* OpenCV
* Python
* MongoDB
* FastAPI
* Face Recognition
* Computer Vision
* Real-Time CCTV Streaming

---

# Future Scope

Future versions may include:

* Violence detection
* Suspicious activity recognition
* Lost & found AI search
* Crowd analytics
* Emergency alert systems
* Multi-camera centralized monitoring

---

# Conclusion

VisionGuard AI transforms passive CCTV cameras into active intelligent surveillance systems.

By combining AI, automation, and real-time analytics, the platform improves:

* safety,
* operational efficiency,
* attendance management,
* and energy optimization

using a single scalable CCTV ecosystem.

**Challenges we ran into**

# Challenges & Bugs Faced During Development

Building CamSense AI involved integrating multiple AI and real-time surveillance components into a single CCTV-based platform. During development, we faced several technical and practical challenges.

---

# 1. Real-Time CCTV Processing Lag

## Problem

One of the biggest challenges was maintaining real-time performance while running multiple AI tasks simultaneously on live CCTV streams.

Initially:

* frame processing became slow,
* detection latency increased,
* and live video started lagging when multiple detections were active.

This happened because:

* object detection,
* face recognition,
* and continuous frame processing

were consuming high computational resources.

## Solution

We optimized the pipeline by:

* using lightweight YOLO models (YOLOv8/YOLOv11 Nano),
* reducing frame resolution,
* processing selected frames instead of every frame,
* and separating modules into independent services.

This significantly improved real-time performance and reduced latency.

---

# 2. False Human Detection in Energy Optimization

## Problem

During occupancy-based automation testing, the system occasionally failed to switch OFF lights and fans correctly because:

* shadows,
* posters,
* and partial human visibility

sometimes caused false detections.

This led to incorrect occupancy counts.

## Solution

We improved detection reliability by:

* adding confidence threshold filtering,
* using continuous frame verification,
* and validating human presence across multiple frames before triggering automation.

This reduced false triggers and stabilized the energy optimization system.

---

# 3. Attendance Duplication Issue

## Problem

While implementing face-recognition-based attendance, the same student was being marked multiple times because the camera continuously detected the same face.

## Solution

We implemented:

* session-based attendance logging,
* timestamp validation,
* and duplicate prevention logic.

Now attendance is marked only once within a defined time interval.

---

# 4. Unknown Person Detection Accuracy

## Problem

The system initially struggled to distinguish between:

* verified users,
* partially visible faces,
* and low-light camera feeds.

This sometimes caused verified users to be classified as unknown.

## Solution

We solved this by:

* storing face embeddings instead of raw images,
* improving lighting conditions during registration,
* capturing multiple face angles,
* and applying confidence-based matching thresholds.

This improved recognition stability significantly.

---

# 5. Weapon Detection Dataset Quality

## Problem

Finding a reliable CCTV-style weapon dataset was difficult because many public datasets:

* contained low-quality images,
* inconsistent annotations,
* or unrealistic images not matching real surveillance scenarios.

Training on such datasets reduced model accuracy.

## Solution

We:

* filtered irrelevant samples,
* selected CCTV-oriented datasets,
* used Roboflow preprocessing and augmentation,
* and trained lightweight YOLO models for faster iteration and testing.

This improved detection performance while maintaining real-time speed.

---

# 6. Cloud Training & Runtime Issues

## Problem

While training models on Google Colab, we faced:

* runtime disconnections,
* GPU unavailability,
* and interrupted sessions during long training runs.

## Solution

We optimized training by:

* using lightweight Nano models,
* reducing unnecessary epochs,
* using smaller curated datasets,
* and frequently saving checkpoints.

This allowed us to continue development without requiring paid GPU infrastructure.

---

# 7. Integrating Multiple AI Modules Together

## Problem

Initially, separate AI modules were difficult to coordinate because:

* energy optimization,
* attendance monitoring,
* and surveillance detection

all required independent camera logic and backend handling.

## Solution

We redesigned the architecture into modular services where:

* each feature has separate processing pipelines,
* but all modules share the same MongoDB backend and centralized dashboard.

This made the platform more scalable and maintainable.

---

# Key Learning

One of the biggest lessons from this project was understanding that building real-world AI systems is not only about training models.

A major part of development involved:

* optimization,
* system integration,
* real-time processing,
* event handling,
* and scalable architecture design.

---

# Conclusion

Despite multiple technical hurdles, VisionGuard AI evolved into a scalable intelligent surveillance platform by combining:

* AI detection,
* real-time monitoring,
* automation,
* and modular system design.

These challenges helped us improve both the technical robustness and practical usability of the project.

Team **Infinite Loopers** -- [Subham Ray](https://github.com/Subham777-max), [Subhajit Jati](https://github.com/Danger525), [Anubhab Roy](https://github.com/Anubhab1606), [Soumadeep Shee](https://github.com/souma9830)

`2026-05-09`

---

### AI-NMS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ainms-eb58) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shivam-kumar-emf-portrait/Agent_Mart) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agent-mart-weld.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/EXvfUlA6LkE) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> NETWORK MONITORING SYSTEM

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square)

**The problem it solves**

**The Problem**
In the current AI landscape, two major issues exist:

1. Subscription Fatigue: Most powerful AI tools are locked behind expensive monthly subscriptions. Users often need a one-time task done (like a single code review or a document summary) but don't want to commit to a $20/month plan.
2. The "Machine Payment" Barrier: Autonomous AI agents are rising, but they cannot easily navigate traditional credit card checkouts. There is no standardized way for one AI agent to "hire" and "pay" another AI agent to complete a specialized task.
3. 

**The Solution: AgentMart**
AgentMart is a Pay-per-task AI Marketplace that solves these problems by creating a bridge between humans, AI agents, and on-chain payments.

1. Pay-Only-For-What-You-Use: Humans can browse a marketplace of 15+ specialized agents and pay a few cents (in USDC) for a single execution. No subscriptions, no hidden fees—just instant micro-services.
2. Enabling Machine-to-Machine Commerce: AgentMart is built with a machine-readable service registry. This means other AI agents can programmatically discover services, understand their input/output requirements via JSON schemas, and settle payments autonomously using the Locus Checkout protocol.
3. Instant On-Chain Settlement: By using USDC on-chain, we eliminate the 3-5 day waiting period of traditional banking. Service providers get paid instantly for their compute, and users get their results the moment the transaction is confirmed.
4. Standardized AI Tasks: Whether it's a "Smart Contract Auditor" or a "Podcast-to-Thread Agent," AgentMart provides a unified interface and checkout experience for diverse AI capabilities, making it the "Amazon for AI Agents."
5. AgentMart transforms AI from a subscription-based software into a live, liquid economy where humans and machines can trade value seamlessly.

**Challenges we ran into**

Building AgentMart was an exciting challenge, especially while trying to merge high-end 3D aesthetics with complex on-chain payment logic. Here are the main hurdles I faced and how I overcame them:

1. The "Spline" Runtime Crash
One of the most frustrating bugs was a TypeError: w.substring is not a function that crashed the entire application on startup. After deep debugging, I traced it back to the Spline 3D runtime failing to parse certain scene data.

**The Fix:** I implemented a custom SplineErrorBoundary and used React.lazy for the 3D hero section. This ensures that even if the 3D scene fails to load, the rest of the marketplace remains fully functional.

2. API Proxy & Deployment Mismatches
During local development, my frontend was proxying requests to the wrong backend port, leading to confusing JSON parsing errors. This got even more complex when deploying to Vercel (frontend) and Render (backend).

**The Fix**: I refactored the network layer to use environment-aware base URLs. I also configured vercel.json rewrites and aligned the Vite proxy settings to ensure seamless communication between the services in both development and production environments.

3. Database Schema Consistency
Moving to a wallet-based architecture required a fresh SQLite schema. At one point, the orders table was missing in production, which caused every checkout attempt to fail.

**The Fix** : I rebuilt the database initialization logic to include Auto-Migration and Auto-Seeding. Now, the backend automatically detects if the services table is empty and seeds 15 specialized agents on startup, ensuring the marketplace is always "ready to use" for new users.

4. Dynamic Data Null-Safety
Handling machine-readable JSON schemas from AI agents often resulted in runtime crashes when fields were unexpectedly null or numeric instead of strings.

**The Fix** :  I performed a rigorous null-safety audit across the codebase, implementing safe string processing for critical UI elements like the Navbar, Activity logs, and Checkout forms (using patterns like String(val || '').substring()).
These challenges taught me the importance of Graceful Degradation—ensuring that a single failing component (like a 3D robot or a missing database record) doesn't break the entire user experience.

**Track: Checkout with Locus**

AgentMart is a decentralized marketplace for AI micro-services where every transaction is powered and settled on-chain using Locus Checkout. Our project is a core fit for this track because it demonstrates a real-world use case for autonomous "Agent-to-Agent" payments and instant on-chain settlement.

How AgentMart fits into the Locus Track:
Integrated On-Chain Payments: We have fully integrated the Locus Checkout API to handle USDC payments for over 15 specialized AI agents. Every task—from AI Code Reviews to Smart Contract Audits—is secured by a Locus payment session.
Machine-Readable Economy: The defining feature of AgentMart is its machine-readable service registry. By using Locus, we enable autonomous AI agents to discover a service, parse its JSON schema, and trigger a checkout session to pay for tasks without any human intervention.
Seamless User Experience: We utilize the Locus frontend components to provide a premium, trustless checkout flow. It handles wallet connections and transaction state perfectly, allowing users to pay-per-task with professional-grade security.
Automated Fulfillment: Our backend listens to Locus Webhooks to instantly trigger AI agent execution once the on-chain payment is confirmed, creating a complete end-to-end loop of "Payment → Execution → Result."
By leveraging Locus, AgentMart moves beyond simple APIs to create a functional Agent Economy where AI services are traded securely and autonomously using USDC.

4:29 AM

Team **HackEarth** -- Priyam Kumar, Rahul Kumar, Shivam Kumar

`2026-04-29`

---

### 1ClickAgent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/oneclickagent-e9fb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Officialhomie/inpay) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://1clickagent.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Agents pay any site. One script tag.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Drizzle](https://img.shields.io/badge/Drizzle-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![USDC](https://img.shields.io/badge/USDC-333333?style=flat-square) ![Ai Agents](https://img.shields.io/badge/Ai%20Agents-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square) ![neon](https://img.shields.io/badge/neon-333333?style=flat-square)

**The problem it solves**

OneClickAgent is payment infrastructure for the agent economy. It solves the discovery and payment problem for autonomous AI agents: any website with a Locus checkout session becomes agent-payable in 30 seconds, with zero custom integration beyond a single `<script>` tag.

The core: a **four-layer session discovery protocol** (HTTP HEAD → meta tag scan → `/.well-known/agent-checkout.json` manifest → database fallback) backed by a **real-time spending controls engine** that enforces five policy dimensions before every payment — maxSingleTransaction, maxDailySpend, maxPerMerchantDaily, allowedCategories, blockedMerchants. Every decision, approved or rejected, is logged in an immutable audit trail.

**For merchants:** paste one script tag. The `agentrelay.js` SDK injects machine-readable metadata, registers the session as discoverable, and renders a "Pay with Agent" button. Any Locus session becomes agent-payable in 30 seconds.

**For agents:** `POST /api/agent/pay` with any URL. The runtime discovers the session, validates it, enforces spending policy, executes payment via Locus USDC on Base, polls for confirmation, and returns a signed receipt with the on-chain transaction hash.

**Locus APIs used:**
- `POST /checkout/sessions` — creates checkout sessions
- `GET /checkout/sessions/{id}` — validates session before payment
- `POST /checkout/agent/pay/{id}` — executes autonomous agent payment
- `GET /checkout/agent/payments/{id}` — polls payment status
- `GET /pay/balance` — agent wallet balance + dashboard display
- Webhook `checkout.session.paid` — fast-path receipt confirmation

**Challenges we ran into**

The hardest problem was **universal session discovery** — making any arbitrary website discoverable without requiring any custom backend integration. We solved this with a four-layer fallback protocol that works even on sites that have never heard of OneClickAgent.

The second challenge was **spending policy enforcement** without blocking legitimate payments. We built a policy engine that evaluates five dimensions in under 10ms and logs every decision with a reason code, so operators can audit why any payment was approved or rejected.

The third challenge was **webhook-less confirmation** — Locus webhooks may not always arrive in time during a demo. We built a polling fallback with exponential backoff so the agent always gets a definitive confirmation, then enriches the receipt if the webhook arrives later.

**Track: Checkout with Locus**

OneClickAgent is built entirely on the CheckoutWithLocus stack. Merchants integrate via a single script tag that creates a Locus checkout session and registers it as agent-discoverable. Agents call POST /checkout/agent/pay/{sessionId} to execute USDC payments on Base. The platform uses /pay/balance for real-time wallet checks, polls /checkout/agent/payments/{id} for confirmation, and processes checkout.session.paid webhooks for fast-path receipts. The spending controls engine evaluates every payment against merchant-specific and agent-specific policies before any Locus call is made. This is a complete, production-deployed implementation of agent-native checkout — not a prototype.

[Victor Igwilo](https://github.com/Officialhomie)

`2026-04-29`

---

### LowKey Private
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lowkey-private-362c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/asgofficial/lowkey-private) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/-glQxvq-Ogk) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Universal Consent Manager

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Electron](https://img.shields.io/badge/Electron-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square)

**The problem it solves**

LowKey Private* (powered by the *CookieShield engine*) is an advanced, professional-grade local networking and privacy tool designed to provide comprehensive tracking defense without breaking website functionality. Its core value proposition revolves around graduating from basic cookie blocking to intelligent, multi-layered privacy management.

**Challenges we ran into**

1. Connecting the UI to the backend
2. Managing the pipelines
3. Dealing with the zero-day trackers
4. Selecting outbound stripper as a segregation tool.

Team **Cipherers** -- [Alex Raj](https://github.com/Py-Cipherer), [Sanchita Rani Saha](https://github.com/Sanchita-200), [Ayush Singh Gautam](https://github.com/asgofficial)

`2026-04-19`

---

### Citifix
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cityfix-0c37) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/techyguy7863/citifix/tree/main/frontend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://citifix.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/gb0tmY2i950?si=PmtLjDqSGYfKSpjg) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> CitiFix is a community-driven platform that empowe

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Twilio](https://img.shields.io/badge/Twilio-333333?style=flat-square)

**The problem it solves**

CitiFix solves the problem of inefficient and unstructured civic issue reporting, where citizens often struggle to report problems like potholes, waste, water leakage, or streetlight failures, and rarely receive timely updates or resolution.

It provides a simple and centralized platform where users can easily report issues, track their status in real-time, and gain community support through voting. This makes the process more transparent, faster, and accountable, while also helping authorities prioritize critical problems.

By introducing automated escalation and structured workflows, CitiFix ensures that unresolved issues don’t get ignored and receive the attention they need.

**Challenges we ran into**

Built reliable escalation logic with multiple conditions, handled OTP authentication issues, managed role-based access, and optimized real-time complaint tracking through structured APIs, validation, and efficient backend design.

Team **Horizon** -- [ARNAB DAS](https://github.com/Mr-binarymonk), [Mrittika Sarkar](https://github.com/msarkar1927moon-svg), [SHUVAM DUTTA](https://github.com/shuvamdutta2004), [Arya Chakraborty](https://github.com/aryachackraborty-spec)

`2026-04-19`

---

### VERIFAI-DIGITAL EVIDENCE VERIFICATION PLATFORM
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/verifaidigital-evidence-verification-platform-e131) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Void-git-uc5/VERIFAI.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://verifai-psg7.onrender.com/frontend/index.html) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sTLT0T4hCGw) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co)

> See More. Verify More.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![SHA-256 Hashes](https://img.shields.io/badge/SHA--256%20Hashes-333333?style=flat-square)

Team **Quad Core** -- [Asif Amin](https://github.com/Void-git-uc5), [Shubham Naskar](https://github.com/shubhamnaskar10), [Khushi Kumari](https://github.com/Khushi5-js)

`2026-09-12`

---

### WebSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/websense-7f3a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vishaal-08/WebSense) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/c758c58e684a4ea7b3cac18f8b1a8456) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Understand before you agree.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![manifest V3](https://img.shields.io/badge/manifest%20V3-333333?style=flat-square)

**The problem it solves**

**WebSense** helps people understand **Terms & Conditions **and other legal agreements before they **accept** them.

It detects risky clauses directly on webpages, analyzes them, and highlights things that could affect the user—such as hidden fees, automatic renewals, data-sharing, cancellation restrictions, or unfair terms. This saves users from having to read through long, complicated legal documents and helps them make safer, more informed decisions before clicking **“I Agree.”**

**Challenges we ran into**

One challenge we ran into was making the extension work reliably across different websites, since Terms & Conditions can be structured very differently from one page to another. We also had to handle cases where the page content changes dynamically.

We solved this by improving the DOM detection and clause extraction logic, adding keyword-based filtering before sending text for analysis, and making the backend handle errors and missing API keys gracefully. We also added automated tests to make sure the risk detection and API endpoints keep working correctly.

Team **Tech Titans** -- Niteesh Karvendhan, Adityan S, Vishaal O H, Siva Harish K, Dharaneeswaran K

`2026-09-02`

---

### FINORA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finora-9eb8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rhk2845-dot/FINORA.git) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> payment platform semilar to Gpay and navi

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Goal: Build an all-in-one healthcare streaming and services platform.

Target users: Patients and families, including elderly and non-technical users.

Core features:

Healthcare video streaming
Doctor appointment booking
Health insurance application
Medicine/product shopping
Personalized health recommendations
Premium subscription for priority appointments

UI/UX: Use a Netflix-inspired content layout with horizontal category rows, large hero sections and personalized recommendations. Use Amazon/Myntra-inspired shopping functionality, but maintain one consistent healthcare brand identity.

Usability: The interface must be extremely simple and understandable for first-time users.

Technical: Build a responsive web application suitable for desktop, tablet and mobile.

Output: Provide the complete UI structure, page list, feature descriptions, user flow and implementation code.

**Challenges we ran into**

Difficulty expressing my ideas clearly – I had many ideas but found it difficult to explain all of them in one clear prompt.
Managing multiple requirements – I wanted to combine features from different platforms like Netflix, Amazon, and Myntra, along with healthcare services.
Getting the expected UI design – The AI sometimes produced a design that was different from what I imagined, so I had to refine my prompt repeatedly.
Maintaining consistency – Adding new features during the prompting process sometimes affected the existing design or functionality.
Choosing the right words – I sometimes struggled to describe exactly how I wanted the website to look and work.
Refining the output – I needed several follow-up prompts such as “also add this” or “make it more user-friendly” to achieve the desired result.
Balancing simplicity and features – I wanted the website to have many advanced features while still being easy enough for a first-time or non-technical user to understand.
Understanding AI limitations – The AI does not always interpret an idea exactly as intended, so I had to clarify and restructure my requirements.

Team **Black feathers** -- Bharathi priyan, Bevin Kumar, Hemnath M, HEMANTHKUMARAN R

`2026-09-02`

---

### Spider-Sense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spidersense-5691) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Qypher365/Spider-Sense) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/FQyv6aSiC1s?si=dlWB2_yqw5zjdFI0) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> The tingle for your information

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Everyday we fill numerous amounts of forms for logins, signups etc. But have we ever thought that do they really need it?
Well, we made Spider-Sense exactly for that! It allows you to scan and check any site about the information that they are asking is actually needed or not.
It also explains and tells you what they actually need and why do they need it, so you know where your information is going. 
It allows users to validate the sites on the basis of how is it going to use their information, and safeguard themselves.

**Challenges we ran into**

First big challenge was integrating three different systems simultaneously. UI/UX, Backend and chrome filling took too much time and intellect. We solved it using cloudflare integration and api_url integration. The other problem was ui builiding for three different environments, we solved it by dividing work on the basis of environment. We also faced issues with ghost environments

Team **TEAM QUBIT** -- Sameer Soni, Himanshu Chaudhari, Shlok Vyas, Divyansh Kapale, Swastik Patidar

`2026-09-02`

---

### MUTEKI-EVOLVE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mutekievolve-5a10) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shamitha311/MUTeki-Evolve-Foundation) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/qA_f0NUxh_Q?si=JNC2qVdM2gaO4xEC) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Generate. Execute. Learn. Evolve.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was integrating two fundamentally different systems without tightly coupling their internal implementations.

Muteki is responsible for autonomous investigation, worker lifecycle, tool execution, events, and isolation, while MTASA provided the inspiration for the iterative **Generate → Execute → Evaluate → Remember → Improve** learning pattern. We had to determine which concepts from MTASA were reusable without unnecessarily porting its delivery-specific solver and execution environment.

Another major challenge was defining a clean integration boundary. Instead of allowing the strategy engine to execute commands directly, we designed it to produce only high-level investigation strategies. These strategies pass through schema and safety validation before being handed to a dedicated Muteki adapter.

We also needed a normalized representation for investigation events, evidence, results, and scores so that the strategy engine and UI would not depend directly on Muteki internals.

Finally, we designed the system to handle stagnation. When multiple iterations fail to make meaningful progress, the Teacher/review layer analyzes previous attempts, identifies unexplored directions, and produces a revised strategy while preventing near-duplicate strategies from being repeatedly generated.

The result is a modular architecture where the strategy engine, Muteki adapter, evaluation engine, orchestration layer, and UI can be developed and tested independently before being connected into the final closed loop.

**The problem it solves**

Modern autonomous security-testing systems can investigate targets, but they often follow relatively fixed strategies. When an investigation fails or reaches a dead end, the system may repeat similar approaches instead of learning from previous attempts.

**MUTeki-Evolve** addresses this by combining Muteki's autonomous security investigation capabilities with an MTASA-inspired strategy evolution loop:

**Generate → Execute → Evaluate → Remember → Improve**

The system starts with a high-level investigation strategy, executes it through Muteki's existing sandboxed architecture, collects investigation events and evidence, evaluates the progress made, stores the result in strategy memory, and generates an improved strategy for the next iteration.

This allows the system to progressively adapt its investigation approach rather than simply repeating the same process.

The architecture is designed around trusted, isolated hackathon targets. The AI generates only high-level investigation strategies and cannot select targets, modify runtime references, execute arbitrary host commands, or bypass the sandbox. This keeps the learning loop separated from the underlying execution and isolation mechanisms.

The result is an autonomous security-testing framework that can demonstrate measurable strategy improvement across multiple investigation rounds.

Team **Only - Semi's** -- Shamitha S A, [Srinath A](https://github.com/srinath-712), [Kudimi Rohith](https://github.com/kudimirohith-bit)

`2026-09-02`

---

### Legalease AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/legalease-ai-37f3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://legalease-ai-buddy.lovable.app/) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co)

> Legal AI is very good platform

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Solution:
An AI-powered legal awareness platform that provides citizens with accurate, government-authorized legal information — not random internet search results. Users can upload images of legal notices/documents and receive AI-generated explanations of what the notice means, what their rights are, and what steps they can take, sourced strictly from verified government legal databases. The platform also includes a "Know Your Benefits" section where users can ask about entitlements relevant to their situation (student ID discounts, category-based scholarships, fee waivers, public amenity rights, etc.), helping them access benefits they're often unaware of — reducing unnecessary legal fees and empowering informed decision-making.

**Challenges we ran into**

Target Clients/Users:
General citizens (especially first-time recipients of legal notices) who feel intimidated by legal or police interactions
Students who are unaware of discounts, scholarships, and category-based benefits
Economically weaker sections and SC/ST/OBC category individuals eligible for government schemes but unaware of them
Small business owners and individuals facing minor legal/administrative notices who currently overspend on lawyers for basic issues
Rural and semi-urban populations with limited access to legal literacy resources

Uday Tyagi

`2026-08-20`

---

### Apex fitz
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/apex-fitz-e845) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaswanth1823/fitness-tracker/tree/main) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co)

> AI coaching, GPS tracking,form analysis

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

Development Challenge

One of the biggest hurdles I faced was implementing real-time GPS tracking and AI-based exercise form analysis in the same application.

GPS tracking required continuously collecting location data while calculating distance, pace, speed, and route without making the app consume excessive battery. The camera-based form checker was also challenging because exercise movements need to be analyzed from video while providing useful feedback.

I solved this by separating these features into dedicated modules: using location services for GPS tracking, CameraX and pose-analysis technologies for movement detection, and Gemini for AI-powered coaching and feedback. I also designed the app so that sensitive AI operations and API keys are handled through a secure backend instead of being exposed in the Android application.

This experience taught me how to break a complex AI fitness application into smaller, manageable systems and integrate them into one platform.

**The problem it solves**

Apex Fitz fits the Overall track by combining multiple technologies into one practical platform that solves real problems faced by athletes and fitness users.
The project uses AI to provide personalized fitness coaching, computer vision to analyze exercise form, and GPS technology to track running and cycling activities. It also provides workout tracking, progress analytics, goal management, and an integrated fitness marketplace.
Instead of requiring users to switch between multiple applications for running, gym workouts, progress tracking, and fitness guidance, Apex Fitz brings these capabilities together in one platform.
The project demonstrates how modern AI and mobile technologies can be applied to a real-world problem: helping people track their performance, train more effectively, understand their progress, and improve exercise technique.
The focus is on building a useful, technology-driven product with practical applications rather than limiting the solution to a single technology or ecosystem.

Team **Codestars** -- [Jaswant policharla](https://github.com/jaswanth1823)

`2026-08-20`

---

### DCFLens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dcflens-0309) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Aarush-x/DCFLens) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://dcflens.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> One ticker. One valuation.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square)

**The problem it solves**

DCFLens is built to make company valuation accessible to people who are interested in investing but may not have a strong background in finance. Traditional valuation models are often filled with financial jargon, complicated spreadsheets, and assumptions that can make it difficult for an everyday investor to understand how a company is actually being valued.

DCFLens simplifies this process by presenting the most important insights in plain English first. Users can understand what the valuation is saying without needing to know every financial term. If they want to dig deeper, they can explore the calculations, assumptions, financial metrics, and reasoning behind the result.

Trust is also a major part of the platform. Instead of asking users to blindly accept an AI-generated explanation or valuation, DCFLens connects its findings back to primary sources such as the company's SEC filings and annual reports. Users can directly inspect the evidence behind important claims and numbers.

Alongside the DCF valuation, DCFLens runs a 10-point financial audit checklist that adapts its analysis to the company and its sector. It looks at factors such as margins, growth, debt, cash flow, dilution, return on equity, and business complexity to help users identify strengths, weaknesses, and areas that deserve further attention.

The goal is not to tell someone what stock to buy. It is to give everyday investors a clearer starting point for researching a company, understanding what it may be worth, and seeing the evidence behind the analysis before making their own decisions.

**Challenges we ran into**

One of our main challenges was integrating Gemini with JavaScript Object Notation (JSON) while ensuring that the generated responses consistently followed the required schema. At first, Gemini occasionally returned JSON with missing fields, incorrect data types, or formatting that did not match our expected schema, which caused errors in the application.

We solved this by defining a strict JSON schema, validating Gemini's output before processing it, and adding error-handling and fallback logic to safely handle invalid responses.

**Best Use of Render**

![image](https://assets.devfolio.co/content/cfaae55d2f0e433d9bc96eab7157ad12/3ecbfe9f-286a-40bc-a3ba-861eaaad093d.jpeg)

DCFLens turns SEC filings into evidence-backed stock valuations, with transparent assumptions and bounded Gemini analysis. Render powers both our Dockerized FastAPI backend and a dedicated Render Workflow.
Our analyze_company workflow takes a ticker, retrieves and normalizes SEC financial data, calculates a deterministic DCF valuation, evaluates the original ten-point checklist, and applies validated AI adjustments. It returns structured results containing the valuation, assumptions, and supporting evidence. If Gemini fails, the deterministic valuation is preserved.
The workflow runs independently of the webapp’s request cycle, letting us execute and inspect an analysis directly through Render. Each run exposes its status, logs, duration, and output. Our live Apple demo completed successfully in approximately 31 seconds with AI analysis applied.
Render therefore supports two distinct experiences: an interactive API for the website and a separately executable research task. The workflow currently runs from the Render dashboard, with frontend integration planned next.

**Best Use of Gemini API**

DCFLens uses the Gemini API to add evidence-grounded qualitative analysis to stock valuation. It connects financial calculations with an explanation of the business behind them.
We first calculate a deterministic DCF baseline using normalized SEC financial data and sector-aware assumptions. Gemini then evaluates the supplied evidence and proposes bounded adjustments to growth and discount rates, alongside qualitative findings for our ten-point business checklist.
Every AI claim must cite an evidence ID supplied in the input. Python validation rejects nonexistent references and enforces adjustment limits. Gemini cannot change historical facts, shares, net debt, valuation formulas, or checklist wording. Each accepted adjustment records its baseline, final value, rationale, evidence, and valuation impact.
Our interface presents plain-English explanations with a deeper “Know why” layer. If Gemini is unavailable or its response fails validation, DCFLens preserves the deterministic valuation instead of inventing a result.
We demonstrated a successful live Apple analysis through Render Workflows with Gemini analysis applied. Our differentiation is auditable AI: users can inspect what Gemini changed, why it changed, and how it affected the valuation.

Team **GOAT** -- [Aarush Muralinathan](https://github.com/Aarush-x), [sai niranjan](https://github.com/sainiranjan2006), [Abinav Prasath](https://github.com/abinav19002), [Sanjeev Raja](https://github.com/Sanjeev2007)

`2026-08-30`

---

### Multiverse 3D
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/multiverse-d-6195) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://multiverse3d.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> An AI-Assisted XR Learning Platform with Voice Gui

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![ASP.NET](https://img.shields.io/badge/ASP.NET-333333?style=flat-square) ![C#](https://img.shields.io/badge/C#-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem: XR Development is Intimidating and Inaccessible

Learning Spatial Computing and 3D programming (like Unity and C#) is notoriously difficult. Historically, it has suffered from three major bottlenecks:

The Setup Barrier: Beginners must download massive, heavy game engines, configure complex SDKs, and often buy expensive VR/AR headsets just to write their first line of code.

The Feedback Loop: In traditional XR development, checking if your code works means compiling the project, putting a headset on, taking it off to fix a bug, and repeating. This slow loop shatters focus.

Cognitive & Reading Fatigue: 3D mathematics (vectors, coordinate spaces, scene graphs) is dense. EdTech platforms typically force students to read walls of text and documentation to figure it out, which causes rapid burnout and drop-offs.

---

🌌 The Solution: Multiverse 3D

Multiverse 3D shatters these barriers by providing a zero-setup, fully browser-based XR learning platform. We bring the 3D engine directly to the student, wrapping it in an intelligent, AI-guided educational layer.

Here is how people can use it and how it makes learning XR significantly easier:

Zero-Setup Browser IDE (Live Visualizer): Users write actual C# code in our Monaco-powered editor, which is securely compiled on our .NET backend. The results are immediately projected onto an interactive 3D WebGL Canvas. No downloads, no headsets, and instant visual feedback.

Sylvie, The Real-Time AI Voice Tutor: Because reading dense technical documentation is exhausting, we built Sylvie. Powered by Gemini 2.5 Flash and ElevenLabs TTS, Sylvie is an interactive voice assistant who watches your code. If you get stuck on a spatial concept or write a bug, she speaks to you in real-time to guide you out of it, providing a 1-on-1 mentorship experience that drastically reduces reading fatigue.

RAG-Grounded Explanations: Sylvie isn't just a wrapper around an LLM; she is connected to a Vector Database containing our proprietary XR curriculum. When she explains a concept, it is contextually grounded in real coursework, preventing AI hallucinations.

Dynamic, AI-Graded Personalization: Education shouldn't be one-size-fits-all. When users sign up, they take a short-answer diagnostic. The Gemini API intelligently grades their open-ended answers and outputs strict JSON to generate a highly personalized curriculum dashboard—hiding what they already know and focusing only on their weak points.

Three Pillars of Mastery: Users don't just read; they act. They can learn through Modules (guided theory), Training (building scenes from scratch to pass unit tests), and Debugging (fixing broken simulated XR environments like a software engineer would in the real world).

**Challenges we ran into**

One of the biggest technical challenges was designing the pipeline to convert student-written C# code into a 3D result rendered with Three.js.

We initially considered directly converting C# into JavaScript/Three.js code, but this would become difficult for complex code and Unity-specific operations. We solved this by introducing an intermediate XR representation.

The final pipeline became:

C# Code
   ↓
Roslyn Parser
   ↓
AST
   ↓
Semantic Layer
   ↓
XR Commands
   ↓
Custom XR Interpreter
   ↓
XR Runtime State
   ↓
Three.js
   ↓
3D Output

Instead of trying to translate every C# statement directly into Three.js, the semantic layer identifies the intent of the code, such as creating, moving, scaling, or rotating an object. The interpreter then executes these XR commands in a controlled runtime, while Three.js is responsible only for rendering the resulting 3D state.

This separation made the architecture more manageable, safer, and easier to validate for student coding challenges.

**Best Use of Gemini API**

Multiverse 3D leverages the Gemini API as the core intelligence engine across our entire platform. We use Gemini 2.5 Flash to power 'Sylvie', our interactive voice tutor, who provides real-time, context-aware debugging and guidance as users write C# code. Additionally, we use Gemini's structured JSON output capabilities to evaluate our open-ended onboarding diagnostic, automatically grading user knowledge to dynamically personalize their learning dashboard. Finally, we utilize Gemini's embedding models to implement a RAG pipeline, ensuring all of the AI tutor's explanations are firmly grounded in our custom XR curriculum rather than hallucinated.

**Best Use of ElevenLabs**

Multiverse 3D uses ElevenLabs to breathe life into our interactive AI tutor, Sylvie. Because this is an EdTech platform navigating complex spatial computing and programming concepts, many students struggle to read and parse long blocks of dense technical text on their own. When users get stuck on C# code or XR theory in our browser-based IDE, Sylvie doesn't just provide dry text feedback—she speaks to them in real-time.

By integrating ElevenLabs' ultra-realistic Text-to-Speech API, we transform raw AI code analysis and RAG-retrieved curriculum data into a natural, conversational voice assistant. This voice integration drastically reduces cognitive load, significantly improving students' understanding and retention of the material while turning an intimidating coding interface into a highly personalized, 1-on-1 mentorship experience.

Team **CodeCrew** -- [Venkatachalam S](https://github.com/Venkat7123), [Ameen Basha](https://github.com/Ameen-Nawaz), [Pranav Bhargav_M](https://github.com/zapgeek), [Sharan I](https://github.com/sharan052006), [Vasu Vigneshwaran P](https://github.com/vasu28git)

`2026-08-30`

---

### Kavasam
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/kavasam-54c7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Don-Gabriel/kavasam-pechacks) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/shorts/1_9LibE4teI) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> PEC HACKS 4.0

![Android](https://img.shields.io/badge/Android-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![elasticsearch](https://img.shields.io/badge/elasticsearch-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square)

**The problem it solves**

Phone scams are one of the fastest-growing forms of fraud in India, and they most often target the people least able to defend against them — elderly parents, new smartphone users, and anyone caught off guard. A caller pressures the victim for an OTP, a UPI payment, or asks them to install a remote-access app, and by the time family realises what happened, the money is gone. Ordinary dialers do nothing during a call, spam apps only label numbers, and most tools stop working the moment there is no internet.

**Kavasam is an Android phone app (a full default dialer) that adds scam protection without interfering with normal calling.**

People can use it to:

- **Make and receive normal calls that always work.** Caller ID, spam scoring, and blocking run on the device, so safety never depends on the network.
- **Detect scams during a live call.** The user marks red flags such as an OTP request or a remote-access request, and Kavasam produces an explainable risk score, supported by an optional, consent-based cloud check. No phone numbers, contacts, or call audio ever leave the device.
- **Hear a spoken warning in English or Tamil.** A one-tap voice alert reads out clear advice for users who cannot read a screen quickly enough.
- **Let a family member help.** The protected phone shows a 6-character code; a guardian links their own phone using it, and any dangerous call sends the guardian an instant alert and a report.
- **Check suspicious content.** Users can paste a message, scan a QR code with the camera, or upload an email PDF, and Kavasam analyses it — and every link inside it — for phishing, fake login pages, and impersonation.

The guiding rule is simple: cloud intelligence can improve safety, but it must never be required to place, answer, or reject a call. Kavasam makes the risky moment slower, clearer, and shared.

**Challenges we ran into**

- **Android blocks microphone access during calls.** Our original plan to transcribe a live call for analysis was not possible, because Android silences the microphone for normal apps during a cellular call. We confirmed this with device logs and redesigned the feature as an in-app call between two Kavasam phones, where the app controls the audio and can transcribe both sides.

- **Staying the default dialer.** Calls kept falling back to the system dialer. Crash logs showed our in-call service failing on a missing call endpoint at the start of each call, which ended the process. Fixing the null handling kept the call inside our own screen.

- **A QR scanner that only failed in release builds.** Live scanning worked while testing but crashed in the release build, because code shrinking removed camera and barcode classes that are loaded indirectly. We corrected the build configuration so the scanner works reliably.

- **SMS to Indian numbers requires regulatory approval.** Sending real SMS to +91 numbers needs DLT registration, which takes days. Instead of waiting, we changed the guardian feature to a device-code pairing model stored in a database, and moved alerts to a messaging workflow that needs no such approval.

- **Text-to-speech access limits.** Voice warnings initially failed even with available credits, because only certain voices are allowed on the free plan. We added an automatic fallback voice so warnings always play, and translate the message for the second language.

- **Keeping the system genuinely private.** The hardest part was ensuring that raw numbers, contacts, audio, and transcripts never leave the phone. Every request to the cloud is limited to a small set of redacted signals, and sensitive details such as codes and card numbers are masked before anything is sent.

- **Making every integration optional and reliable.** Each connected service was built to fail safely, so the app keeps working normally even if a service is unavailable during a demo.

**Best Use of Render**

Render hosts Kavasam's consent gateway — the FastAPI service that every cloud feature runs through. Using the included `render.yaml` blueprint, a single deploy brings up the API that handles AI scam analysis, Actian vector lookups, guardian pairing, and the n8n webhook target, with health and audit endpoints and all secrets kept server-side. It gives the app one reliable, reproducible backend without any provider-specific setup, while calling, caller ID, and local safety keep working even if the gateway is offline.

**Best Use of n8n**

n8n powers Kavasam's guardian alerting as a provider-neutral automation layer, so the app never holds messaging credentials. A secured webhook receives danger events from the gateway, a Switch node routes them by type (alert, report, approval, enrollment), and a Telegram node delivers a real-time warning to the guardian. A second webhook handles inbound replies, forwarding a guardian's ACCEPT or REJECT back to the gateway. This makes the guardian flow a genuine two-way, human-in-the-loop workflow that can swap delivery channels without touching the app.

**Best Use of Gemini API**

Gemini is the reasoning core across Kavasam's safety features. It gives a calm, explainable "second opinion" on tracked calls, analyses pasted messages, links, QR payloads, screenshots, and email PDFs for phishing and fraud, powers live two-sided transcription in the in-app guardian call, and translates spoken scam warnings into Tamil. Every request is limited to redacted signals or user-supplied content, and the app always falls back to deterministic checks if the AI is unavailable, so guidance is smart when possible and safe by default.

**Best Use of ElevenLabs**

ElevenLabs turns a scam warning into speech for users who can't read a screen fast enough during a stressful call. On a high-risk result, one tap plays a clear spoken alert in English or in Gemini-translated Tamil, only the warning text and language are ever sent, and if the cloud voice is unavailable the app falls back to the device's own text-to-speech so an alert is always heard. This makes safety accessible to elderly and low-literacy users, not just those watching the display.

**Best Use of MongoDB Atlas**

MongoDB is the backbone of Kavasam's guardian pairing. The protected phone generates a 6-character code stored in MongoDB, and when a guardian links their phone, the database binds the two devices exclusively — a code can be claimed once, and danger reports are scoped to that pair, so no device can ever read another pair's data. Reports are written and served from MongoDB with short retention, giving the guardian a private, reliable inbox that never contains call audio or transcripts.

**Best Use of Snowflake API**

Snowflake is Kavasam's privacy-safe analytics sink. Each analysis writes a metadata-only event — type, risk level, source, and timestamp — with no numbers, contacts, content, or audio, letting the team understand adoption and risk distributions without compromising user privacy. Writes are asynchronous and fail-open, so warehouse availability never affects calling or safety on the phone.

**Best Use of Actian Vector Database**

Actian VectorAI serves as Kavasam's scam-pattern memory for live calls. Known scam behaviours are stored as vectors and, during a tracked call, the caller's behaviour signals are matched against them with nearest-neighbour search to surface the closest known pattern and its similarity. This grounds the on-device risk score with real vector evidence — shown to the user as an explainable "matches a known scam pattern" result — while only a small, redacted signal vector is ever sent, never numbers, contacts, or audio.

Team **Volente Dynamics** -- [Don Gabriel](https://github.com/Don-Gabriel), [Nirubama A](https://github.com/Nirubama01), [Mary Vivitha](https://github.com/vivi-2111), [Poonkundran R](https://github.com/poonkundran021), [VIJAYALAKSHMI G](https://github.com/vg07-sys)

`2026-08-30`

---

### Gameverse-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gameverseai-e7c3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/maitreyeekulkarni02/GameVerse-AI) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Gamified Learning Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

GameVerse AI transforms traditional learning into personalized, interactive gameplay.

Most educational platforms provide the same content to every learner, even when students have different strengths, weaknesses, and learning patterns. GameVerse AI continuously learns from student interactions such as quiz attempts, mistakes, progress, and completed challenges.

These learning events are converted into semantic vector memories using a local embedding model and stored in Actian VectorAI DB. When generating the next learning experience, GameVerse retrieves the most relevant historical memories through semantic search and provides that context to the AI content generation system.

This allows the platform to adapt gameplay difficulty, explanations, challenges, and remediation to each learner instead of relying only on static profiles or keyword matching.

The result is an AI-powered learning experience that becomes increasingly personalized as the student plays.

**Challenges we ran into**

One of our biggest challenges was integrating Actian VectorAI DB as a genuinely load-bearing component rather than simply listing it as a technology.

We designed a semantic-memory pipeline where learning events are converted into 384-dimensional embeddings using Sentence Transformers and stored in Actian VectorAI DB. Relevant memories are retrieved through vector similarity search and passed into the AI content-generation pipeline to influence future gameplay.

Another challenge was local infrastructure. Running Actian VectorAI DB required Docker and virtualization support, while our development machine initially had virtualization disabled. We implemented a resilient SQLite fallback using the same embeddings and cosine-similarity approach so the application could continue functioning during local development.

We also had to handle dependency compatibility, embedding-model loading, connection failures, and automated testing. We added dedicated Actian integration and fallback tests and verified the complete backend test suite with 82 passing tests.

Finally, we designed the deployment architecture so the FastAPI backend can be deployed through Render while keeping configuration and secrets environment-based.

**Best Use of Render**

We use Render to deploy the GameVerse AI FastAPI backend as a production-ready cloud service. The backend handles authentication, game generation, learning events, progress tracking, AI content generation, and API requests from the React frontend.

Render gives us a simple CI/CD workflow connected directly to our GitHub repository, allowing every committed update to be deployed without managing our own server infrastructure.

**Best Use of Actian Vector Database**

Actian VectorAI DB powers the semantic memory layer of GameVerse AI.

Every important learning interaction, such as quiz mistakes, successful attempts, topic struggles, and progress, is converted into a 384-dimensional embedding using Sentence Transformers and stored as a vector in the learning_memories collection.

When generating a new gameplay experience, GameVerse performs semantic vector search to retrieve the student's most relevant past learning experiences. This context is then provided to the AI so it can adapt the next chapter, challenge difficulty, explanations, and remediation to the learner.

This makes Actian VectorAI a load-bearing component of our personalization engine rather than simply a database listed in the technology stack.

Team **Gamified Coders** -- [Impreet Khanijo](https://github.com/impreetsingh427), [Aditya Bawche](https://github.com/adityabawche), [Nipun Chaudhari](https://github.com/NipunChaudhari), [Samarth Pawar](https://github.com/Samarthpawar), [Maitreyee Kulkarni](https://github.com/maitreyeekulkarni02)

`2026-08-30`

---

### AgentPay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentpay-autonomous-financial-infrastructure-for-an-agenttoagent-economy-cc18) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/01d7ef3463934a86a8007a4e891ea3d4) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Autonomous Financial Infrastructure for an Agent

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![SHA-256 Hashes](https://img.shields.io/badge/SHA--256%20Hashes-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Autonomous AI agents are becoming capable of performing tasks independently, but there is still no simple way for agents to safely discover work, establish trust, verify outcomes, and exchange value without constant human intervention.

AgentPay solves this by providing trust and financial coordination infrastructure for an agent-to-agent economy.

In AgentPay, tasks are matched with suitable AI agents based on capability, reputation, historical quality, success rate, and availability. Eligible agents can compete through bidding, while the task reward is secured using simulated AP Credits.

After completing a task, the worker's result is locked with a SHA-256 integrity fingerprint and evaluated by an independent verifier. The worker becomes eligible for settlement only when the required verification conditions are satisfied.

AgentPay also provides reputation-based trust, Canary testing for newly introduced agents, provisional access, security monitoring, human review, disputes, and arbitration.

This creates a safer autonomous workflow:

Task Discovery → Matching → Bidding → Escrow → Execution → Verification → Conditional Settlement → Reputation

AgentPay demonstrates how autonomous AI agents can safely collaborate and participate in future digital economies without blindly trusting each other.

**Challenges we ran into**

One of our biggest challenges was maintaining consistency across the complete AgentPay lifecycle.

Task assignment, bidding, escrow, execution, submission, verification, settlement, reputation, disputes, and security are interconnected. A failure in one stage could create an incorrect state elsewhere.

For example, we needed to prevent duplicate settlements, double payment, self-verification, settlement after failed verification, negative balances, and modification of submitted results.

We addressed these problems by enforcing important rules in backend services, adding transactional state changes, duplicate-action protection, immutable submission snapshots, SHA-256 integrity verification, ledger-based AP tracking, and complete activity/audit history.

Another challenge was deciding how to trust newly introduced AI agents. Instead of immediately allowing an unknown agent to handle valuable tasks, we introduced Canary testing and provisional access. New agents first prove their capability in a controlled test and then build trust through lower-value, independently verified tasks.

Finally, because AgentPay contains many interconnected systems, keeping the interface understandable was challenging. We simplified the UI around the main agent lifecycle so users can understand what is happening without being overwhelmed by the underlying infrastructure.

Team **code bros** -- HARIHARAN G, KIRAN E, Allen Christopher, Akshaya Karthik

`2026-08-29`

---

### Axiom
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/axiom-7646) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prakash-M-27/Fintech) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Don't predict the market instead adapt it

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**Challenges we ran into**

Data processing gets time but the Market price changes continuosly. We have make the agent decide and trade before the market change. The prediction is impossible.

**The problem it solves**

Axiom : Autonomous AI Agents for Real-Time Financial Markets

CSI ORIGIN 2026 | Problem Statement 3
Solution — Simple Explanation

Your product is a real-time AI decision system for markets, not a future-prediction system.

It continuously watches NIFTY, Gold, and USD using:

Price & volume

Liquidity

Technical signals

News/articles

Market conditions

Cross-asset relationships


Then multiple AI agents work together:

1. Observe → Collect what is happening now.
2. Interpret → Understand the current market condition.
3. Reason → Decide what action makes sense now.
4. Evaluate Risk → Check stop-loss, exposure and risk limits.
5. Allocate Capital → Decide how much capital is allowed.
6. Execute → Take the approved action (MVP: paper trading).
7. Observe Outcome → See what actually happened.
8. Adapt → Update the decision when conditions change.

The key idea

The AI doesn't say:

> “NIFTY will go up.”



Instead, it says:

> “Based on the current evidence, BUY is the best decision right now. If liquidity falls, volatility increases, or major negative news appears, this decision becomes invalid and the system will immediately reassess.”



So while Decision A is active, the system is already watching for possible conditions B, C, and D.

If one of those conditions occurs:

Market changes → Scenario triggers → Current decision is reassessed → Risk checked → New decision immediately generated.

Technology

Frontend: React
Backend: FastAPI
AI orchestration: LangGraph + LangChain
Database: PostgreSQL/TimescaleDB + pgvector
Real-time: WebSockets + Redis
Analytics: Python, Pandas, NumPy
MVP execution: Paper trading

The real value is therefore continuous adaptive decision-making under changing market conditions, rather than market prediction.

Team **Team Error 503** -- Mohammed Faheem, K S Dharshan, Gurumoorthi A, Prakash M

`2026-08-29`

---

### Helm
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/helm-b7da) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShyamKumar29/Helm) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> An agent at the helm of your company's cash flow

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Uvicorn](https://img.shields.io/badge/Uvicorn-333333?style=flat-square)

**Challenges we ran into**

![image](https://assets.devfolio.co/content/a0a844f95b4c48568c17cb0319d0a0f3/9672c8f4-e2c7-462f-9a17-188034652c7f.png)

**Knowing when the optimizer should give up**
The engine runs a scenario-based MILP over Monte Carlo forecasts, which can in theory hang on a bad scenario set. We hard-capped every solve at 2 seconds with a greedy fallback (`solver.fallback_used = true`, surfaced straight to the UI) — a demo where the "brain" freezes mid-decision is worse than a slightly worse decision made on time.

**Keeping the LLM honest**
The explainer narrates decisions the optimizer already made, but LLMs invent numbers when they're uncertain. We built a numeric-grounding check that verifies every figure the model states against the actual `DecisionObject` before trusting the output, and fall back to a fully deterministic template narrator (`templates.py`) on anything ungrounded or if [Groq / Claude] is unreachable. No exceptions, no silently hallucinated rupee amounts in a financial demo.

**A silent serialization bug that corrupted our own contract**
`by_alias=True` on one Pydantic model in `whatif.py` was quietly mangling `diff_from_previous.flipped[].from` — the exact field judges would see when a decision flips under a chaos event. Caught it during integration, fixed it, and added a regression test so it can't come back unnoticed.

**Three people building against frozen contracts — and the contracts still drifted**
`contracts/fixtures/forecast.sample.json` only had 2 points (day 0, day 30) against a spec that required 91 buckets, which silently rendered our fan chart as a flat line instead of confidence bands. Fixed the fixture, logged it in `contracts/CHANGELOG.md` — and it's the reason we now sanity-check every fixture against its own spec before building UI on top of it.

**Live replay stalls on long runs**
`sim_loop.py`'s explanation-attach step makes a self-referential HTTP call back into the same async server while the original request is still in flight, stalling roughly 3 seconds per decision. Doesn't break correctness, does hurt long-run playback feel. Root-caused and scoped (run day-advance in a thread, or make the self-call properly async) but left flagged rather than patched — the fix touches `api/`, outside the diagnosing dev's ownership lane, and we chose to respect the "stay in your folder" rule under time pressure rather than risk a merge conflict at hour 20.

**The problem it solves**

![image](https://assets.devfolio.co/content/a0a844f95b4c48568c17cb0319d0a0f3/778bef21-ea38-449c-bf73-1b276b80c4b4.png)

**In one line:** a company's treasurer decides every morning where its limited cash goes — we replaced him with an agent that never sleeps on the job.

### The problem

A business has one person juggling all of this, every single day:
- Which supplier invoices to pay now, and which to delay
- Which early-payment discounts are worth taking
- Whether to borrow from a credit line to cover a gap
- How much cash to keep untouched for payroll, GST, and other fixed obligations

The catch: money customers owe the business almost never arrives on time. So the treasurer is deciding today's cash allocation against a *guess* about tomorrow's cash position — and when that guess is wrong, the company either runs short on payroll or pays unnecessary interest cleaning up the mess.

Today this is handled with static rules ("always pay on the due date") or plain gut feel. Neither adapts. Neither sees the shortfall coming until it's already happening.

### What HELM does

HELM is an autonomous working-capital agent that takes over this decision entirely:

- **Forecasts 90 days of cash**, treating customer payment dates as *uncertain* — not a fixed promise — using each customer's real payment history
- **Calculates exactly how much cash is safe to spend today**, holding back only what's needed to protect upcoming obligations
- **Decides, for every invoice**, whether to pay now, pay early for a discount, delay, or borrow — balancing discount value, financing cost, penalty risk, and supplier relationships all at once, not optimising for one number
- **Re-optimises automatically** the moment something material changes — a payment slips, a rate moves, a new bill lands
- **Explains every decision** in plain language: what it chose, what it rejected, and what would have to change for it to decide differently

### Why it matters

Manual, rule-based cash management costs businesses real money — missed discounts, avoidable interest, late supplier payments, and liquidity scares that were visible in the data days before they became a crisis. HELM turns that into a continuous, explainable, automated decision loop, so no one finds out about a cash shortfall the same day it happens.

Team **Xyrus** -- [Yaswanth K B](https://github.com/noobme007), [Sheshakanth Ra](https://github.com/sheshakanthra), Suganth K, [Shyam Kumar J](https://github.com/ShyamKumar29)

`2026-08-29`

---

### TranXit Haryana
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tranxit-edb3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ankurtaneja14/Tranxit) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://expo.dev/accounts/theankurtaneja/projects/bus_tracker/builds/a7edd960-b518-4eb3-90c9-e655879c61c2) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co)

> Transforming Haryana's New Electric Bus Network

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

![image](https://assets.devfolio.co/content/f7ee99e7595b4901a91d6dcd277ee203/4ee8a074-11ec-4ee0-bc5a-1b692ec8b38f.png)

**The Unpredictability Trap**
*Haryana deployed 375+ electric buses (HCBSL & GMCBL across Gurugram, Panipat, Ambala, Karnal, Hisar, Rohtak, Rewari). However, commuters face unpredictable waiting times, confusing route stops, and zero visibility into bus crowding, causing many to revert to auto-rickshaws or private vehicles*.

**Lack of Metro Efficiency**
*Buses exist physically, but lack the digital infrastructure commuters expect from modern metro systems—such as live countdown timers, tap-and-go digital ticketing, real-time seat availability, and multi-modal transfer guidance.*

**Challenges we ran into**

![image](https://assets.devfolio.co/content/f7ee99e7595b4901a91d6dcd277ee203/5dc7c128-46bf-4988-b4be-b3ba177361ae.png)

*Implementing the payments part was such a hassle for us. Coz it was not the skill issue but rather we tried some wrong approaches just for the sake of trying.

Which eventually led us to crash the 40% of the architecture. Then we gave up on our trials and used the approach we were familiar with and eventually leading to creating a perfect app for the perfect Market Gap.*

Team **Beta Males** -- [Ankur Taneja](https://github.com/ankurtaneja14), [rudr kumar](github.com/Rudr124)

`2026-08-22`

---

### WaveSafe
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wavesafe-9469) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arvindkumar-ship-it/WaveSafe) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/AKZOnFFqXSo?si=qWU510kadG31v9Xd) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co)

> Platform for Smarter Coastal Travel and Safety

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![POSTGIS](https://img.shields.io/badge/POSTGIS-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square)

**The problem it solves**

# 🌊 Wave-Safe

> **A Unified Platform for Smarter Coastal Travel and Safety**

Wave-Safe is a unified web-based coastal safety and intelligence platform that combines real-time ocean and weather intelligence, trip planning, emergency coordination, and rescue tracking into one coastal travel experience.

## 👥 Team

**Team Name:** LazyCoders

- **Arvind Kumar** — Team Leader
- **Om Kushwaha**
- **Rishabh Pal**

---

## 🚨 Problem Statement

India has over **7,500 km of coastline**, but there is no unified digital platform that provides tourists with real-time beach safety intelligence and coordinated emergency response.

### Current Challenges

- No simple real-time **Safe / Caution / Unsafe** signal for beaches.
- Visitors may lack current information about ocean conditions, rip-current risks, and official hazard advisories.
- Emergency assistance can depend on a chain of separate phone calls.
- Hospitals, lifeguards, police, coast guard, rescue posts, and jurisdictions operate through disconnected records.
- There is no single system to automatically identify and coordinate the appropriate responder for an incident.
- Existing ocean and weather data is available, but it is not converted into one simple decision for a beach visitor.

---

## 💡 Solution

**Wave-Safe** bridges the gap between **real-time risk awareness and emergency response**.

The platform is designed as a travel website first, with safety intelligence integrated throughout the user's journey.

### Predict → Plan → Protect → Track

- **Predict:** Calculate a live beach safety verdict from ocean and weather data.
- **Plan:** Identify risky travel windows and suggest safer alternatives.
- **Protect:** Provide one-tap SOS with location sharing and coordinated emergency dispatch.
- **Track:** Provide live rescue tracking, acknowledgements, and ETAs.

---

## ✨ Features

### 🟢 Live Beach Safety

Provides a live:

- **SAFE**
- **CAUTION**
- **UNSAFE**

verdict for beaches using real ocean and weather data.

### 🗓️ Smart Trip Planning

- Evaluates risk across planned time windows.
- Flags potentially dangerous slots.
- Suggests safer alternative beaches.

### 🆘 One-Tap SOS

A single SOS trigger can share the user's exact location with:

- 112 / emergency response
- Nearest hospital
- Coast guard / marine police
- Lifeguard post

### 🚑 Emergency Dispatch & Tracking

Tracks an incident through:

```text
Created → Dispatched → Acknowledged → En Route → Arrived → Resolved
```

### 🗺️ Hospital & Authority Routing

- Capability-filtered hospital matching.
- Jurisdiction-matched authority routing.
- Defined response roles.
- Parallel emergency dispatch.

### 📍 Live Rescue Tracking

- Location pings.
- ETA tracking.
- Stale-session detection.
- Rescue progress visibility.

### 🔔 Notifications

- SMS notifications.
- Web Push notifications.
- Localized templates.
- English fallback.

### 📴 Offline Support

- Offline-capable Progressive Web App.
- Local action queue.
- Automatic synchronization after reconnect.

### 🔐 Authentication

- Phone + OTP login.
- Defined OTP expiry.

### 🏢 Admin & Operations

- Beach management.
- Jurisdiction management.
- Hospital management.
- Incident dashboards.
- Acknowledgement dashboards.
- Risk-rule tuning.
- Log export.

### 🌊 Data Ingestion & Risk Engine

- INCOIS + SACHET connectors.
- Manual beach closures.
- Data normalization and unit conversion.
- Redis-based deduplication.
- Risk scoring.
- Time-series hazard outlook.

---

## 🧠 Risk Engine

The Risk Engine combines multiple inputs into an explainable risk score.

### Inputs

- Wave height
- Current speed
- Wind
- Tide
- Water quality
- Forecast trend
- Lifeguard coverage

### Risk Formula

```text
R = σ( Σ wᵢzᵢ + Σ wᵢⱼzᵢzⱼ + λ₁Δtrend + λ₂Δtide )
```

### Risk Classification

| Risk Score | Verdict |
|---:|---|
| `R < 0.33` | 🟢 SAFE |
| `0.33 – 0.66` | 🟡 CAUTION |
| `R ≥ 0.66` | 🔴 UNSAFE |

Active **tsunami, storm surge, or evacuation** conditions override normal scoring and force:

```text
R = 1 → UNSAFE
```

---

## 🛠️ Tech Stack

### Frontend

- **React**
- **Next.js (SSR)**
- **Mapbox GL JS / Google Maps API**
- **Progressive Web App (PWA)**

### Backend

- **Python**
- **FastAPI**
- **REST APIs**
- **WebSockets**
- **Celery**

### Database & Storage

- **PostgreSQL 16**
- **PostGIS**
- **Redis 7**
- **S3-compatible object storage**

### Infrastructure & DevOps

- **Docker**
- **Kubernetes**
- **Kafka / RabbitMQ**
- **GitHub Actions CI/CD**
- **AWS / GCP**

### External APIs & Data Sources

- **INCOIS** — Ocean & advisory data
- **SACHET** — CAP / RSS alerts
- **112 ERSS** — Emergency di

**Challenges we ran into**

# The Bug That Almost Slipped Into Production

**Project:** WaveSafe — Coastal Safety Platform
**Where it hit:** `POST /v1/admin/beaches`
**Found during:** Final Swagger E2E testing, hours before deployment

## The Crash

```
psycopg2.errors.InvalidParameterValue:
Geometry type (Point) does not match column type (Polygon)
```

A clean 500. Not a validation error — a raw database exception leaking straight
to the client.

## Why It Happened

Swagger's auto-generated example payload showed a generic GeoJSON `Point`.
Following it felt natural — but the `beaches` table stores each beach as a
**Polygon** (a boundary, not a pin drop). The API had no validation layer
checking the GeoJSON `type` before handing it to PostGIS. The request sailed
straight through FastAPI → SQLAlchemy → Postgres, where the *database*
finally said no — the hard way.

## The Fix

**Immediate:** Rebuilt the payload as a proper closed-ring Polygon
(5 coordinate pairs, first == last). Confirmed the endpoint logic itself was
fine — it was purely an input-shape problem.

**Real fix (queued, non-blocking):** Add a Pydantic validator on the GeoJSON
`type` field so bad input returns a clean `422` before it ever touches the DB.

## The Pattern

This wasn't a one-off. The same root cause — **the database was the only
validation layer** — surfaced twice more in the same session:

| Endpoint | Expected | Got |
|---|---|---|
| `admin/beaches` | 422 (wrong geometry) | 500 crash |
| `admin/activity-thresholds` | 409 (duplicate key) | 500 crash |
| `safezone/guidance` | 422 (empty-string UUID) | 500 crash |

All three: the app layer trusted the input and let Postgres be the bouncer.
Postgres did its job perfectly — data integrity held. But the *caller*
got a stack trace instead of a sentence.

## The Takeaway

> A database constraint enforcing correctness is not the same as an API
> validating input. One protects your data. The other protects your users
> from a 500 page.

None of the three were blockers — all admin/internal-only, zero impact on
the core user flow (SOS trigger → dispatch → tracking), which stayed clean
through every test. But they're first on the list for the next patch.

Team **LazyCoders** -- [Rishabh Pal](https://github.com/risbh19), [Om Kushwaha](https://github.com/omkushwaha2812), [Arvind Kumar](https://github.com/arvindkumar-ship-it)

`2026-08-22`

---

### SecAgent Hub
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/secagent-hub-16b6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pranavk-7117/SecAgentHub) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://secagent-hub-delta.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co)

> A Security Digital Twin for Cloud Infrastructure

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**Challenges we ran into**

Building meaningful infrastructure relationships: Converting Terraform resources into a security-aware model required understanding networking, IAM, dependencies, and resource access.

Keeping the analysis deterministic: Attack paths needed to be based on actual infrastructure relationships rather than AI assumptions.

Controlling AI hallucinations: Ensuring the AI only reasons from verified security findings and infrastructure relationships, instead of inventing resources, attack paths, or vulnerabilities.

Simulating changes safely: The What-If engine needed to modify a virtual copy without affecting the original infrastructure, then recalculate and compare attack paths.

Integrating multiple components: Connecting Terraform parsing, security scanning, Digital Twin, attack analysis, AI remediation, and verification while preserving the existing prototype.

Verifying AI-generated fixes: AI-generated Terraform changes cannot simply be trusted; they need to be validated, rescanned, and re-evaluated against the attack paths.

**The problem it solves**

Modern cloud infrastructure generates hundreds of unprioritized security findings every day, yet most existing tools treat each vulnerability in isolation — leaving developers buried under a relentless flood of alerts with no clear sense of what truly matters. SecAgentHub was built to solve exactly this problem. Rather than simply cataloging disconnected findings, SecAgentHub understands how individual vulnerabilities interact and chain together to form real, exploitable attack paths across your infrastructure. It cuts through the noise by intelligently prioritizing critical risks based on actual exploitability and business impact, not just severity scores. But discovery is only half the battle — SecAgentHub goes further by empowering developers to apply AI-guided remediations and then verify, through a live Digital Twin simulation of their infrastructure, that the fix genuinely closes the attack path before a single line of code ever reaches production. The result is a security platform that doesn't just tell you what's broken — it shows you the path an attacker would take, guides you to the most impactful fix, and proves the door is locked before you deploy.

Team **PC_Cookerz** -- [Pranav Khandelwal](https://github.com/pranavk-7117), [Pranjal Singh](https://github.com/LEGEND7006), [Piyush Sohanda](https://github.com/Shylad2007), [Shubham Patil](https://github.com/ShubhamPatil200507)

`2026-08-22`

---

### Aegis Command
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegis-command-80fd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TanmayJain-dev/Aegis-Command) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/18nVRUMhZMJ-18spOLxxeTVd9RZkLXl6L/edit?usp=drive_link&ouid=111248514812270628490&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co)

> Unified Threat Intelligence Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Building a complete autonomous intelligence pipeline required solving multiple engineering challenges:

• Synchronizing real-time UAV detection streams with a responsive tactical dashboard.
• Converting computer vision detections into meaningful geospatial intelligence.
• Integrating AI reasoning with retrieved intelligence while maintaining low latency.
• Designing a stable WebSocket-based communication pipeline for live threat updates.
• Creating realistic intelligence datasets and evidence retrieval workflows for prototype evaluation.

We overcame these challenges through modular architecture, optimized backend pipelines, and continuous testing between the AI engine and frontend command interface.

**The problem it solves**

Modern security operations generate massive amounts of unstructured data from UAV feeds, intelligence reports, and field sensors. Human operators must manually correlate these sources under time pressure, causing delayed threat identification and decision-making.

Aegis Command addresses this by creating an autonomous threat intelligence system that combines computer vision, geospatial tracking, AI-powered reasoning, and intelligence retrieval into a single operational dashboard.

The platform detects objects from live aerial feeds, analyzes movement patterns, correlates detections with historical intelligence, and generates actionable threat assessments in real time.

**Defence**

AEGIS fits the Defence track because we are solving a battlefield situational-awareness problem: how do you turn fragmented sensor observations into verified operational context when bandwidth, connectivity and human attention are constrained?

Team **Aegis-AI** -- Aryan garg, [Rishabh Bansal](https://github.com/rishabh230707-afk), [Tanmay Jain](https://github.com/TanmayJain-dev)

`2026-08-16`

---

### Tuffy CLI: Memory-Native AI Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tuffy-cli-4af1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CodebyKumar/tuffy-cli) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/k7OaUmzACUY) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> With a memory framework built for local AI agents

![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![CLI](https://img.shields.io/badge/CLI-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![voice-ai](https://img.shields.io/badge/voice--ai-333333?style=flat-square) ![anthropic-api](https://img.shields.io/badge/anthropic--api-333333?style=flat-square) ![llm-agent](https://img.shields.io/badge/llm--agent-333333?style=flat-square) ![memory-graph](https://img.shields.io/badge/memory--graph-333333?style=flat-square) ![elastimem](https://img.shields.io/badge/elastimem-333333?style=flat-square)

**What is the problem your project solves?**

Typical agent memory is a vector database bolted onto a chatbot: no sense of time, no sense of relationships between facts, and no graceful behavior on weak hardware or no network.

Tuffy CLI's bet is that memory deserves its own architecture, and that "local-first" should be provable, not just claimed. **Elastimem** is that architecture, built as layers: versioned facts, hybrid recall, a background consolidation worker, and, its newest layer, a graph, all scaled by a Memory Governor across three hardware tiers. This event proved that whole layered framework works end to end through a real model, and proved local-first and Claude-is-core can both be true at once.

**What is the deployed URL for this project?**

No live deployment by design (local-first CLI tool) - repo: https://github.com/CodebyKumar/tuffy-cli

**How you are solving it?**

**Elastimem is the key solution here**: a self-built memory framework for local AI agents, backed entirely by one embedded SQLite database, not a separate vector database, not a hosted service, no external dependency to run offline. It's built as four layers:

- **Versioned facts.** Plain SQLite rows; a correction creates a new version, nothing is silently overwritten.
- **Hybrid recall.** SQLite's own FTS5 full-text search plus semantic/vector search over past conversation chunks, no external index or service.
- **A background consolidation worker.** Extracts and merges memory off the reply path, so it never blocks a turn.
- **A knowledge graph.** Entity and relationship recall via multi-hop SQL traversal against that same SQLite file, no graph library, its newest layer.

All four are scaled by a **Memory Governor** across three hardware tiers, not just "on" or "off":

- **LITE**: the hard floor - no LLM call and no embedder call, ever. Keyword-only recall, rule-based fact capture, and (as of this event's upstream update) real read-only 1-hop graph traversal against whatever graph already exists, though nothing new is written to it at this tier.
- **STANDARD**: embedder and LLM extraction on, batched every 2 turns; 1-hop graph expansion; dedupe-and-decay-level consolidation.
- **FULL**: per-turn background extraction; 2-hop graph expansion with clustering; full LLM-assisted consolidation, including merges.

The same code runs correctly whether the host has 2 GiB or 32 GiB free - one architecture that degrades predictably, not three different code paths.

Tuffy CLI is the terminal AI agent built around Elastimem: a ReAct-style tool-calling loop that works identically across model providers, a tool registry plus skills and MCP support, and voice mode. It runs on a local model or on Claude, switching live, with the same tools and the same Elastimem memory either way.

**What was built during this event's window**, not before it:

- **Brought Tuffy CLI current with Elastimem's complete feature set, including its graph layer, and verified the whole framework end to end inside a real agent**, not just that it imports. Verification found and fixed two real gaps: the system prompt was never reading the graph data Elastimem computed, and the background extraction worker's token budget was too small once graph extraction was added, silently truncating and discarding entire extractions. Both confirmed fixed with real stored data, not just passing tests. Later in the same event, pulled a further upstream Elastimem fix that raises LITE tier's graph floor from no traversal at all to real 1-hop read traversal, re-verified directly against this machine's real LITE tier.
- **Built a native Anthropic Messages API provider**, not a config entry pointing at an existing OpenAI-compatible path, so Claude drives the agent loop and the memory pipeline itself as a first-class model. Verified live against the real API, including a genuine bug only live testing caught. Claude Haiku 4.5 is now the default model.
- **Built an enforced online/offline network mode**, live-switchable, that is mechanical rather than cosmetic: offline blocks API models from loading or being switched to, and strips network-dependent tools from what the agent is even told it can call.
- **Added Maya Research's cloud text-to-speech as the online voice engine**, alongside the existing local Whisper/Piper voice path offline, with the model's own reply style aware of which one is active.

**Existing before this event (not built at this hackathon):**

- **Tuffy CLI's core**: the ReAct-style tool-calling loop, local model loading via llama.cpp, the OpenAI-compatible API provider, the tool registry, the skills system, and the MCP client.
- **Voice mode's local path**: Whisper speech-to-text and Piper text-to-speech, offline.
- **An earlier Elastimem integration**: facts, episodic recall, and lessons wired into Tuffy CLI, but without the graph layer, without online/offline mode, without the Claude provider, and without Maya Research's cloud TTS - all four of those are new this event.
- **Elastimem itself**, as a framework, including its graph layer: a separate standalone project (`CodebyKumar/elastimem`) that predates this event entirely and already backs more than one product. What's new this event is bringing Tuffy CLI current with it and verifying it end to end, not writing Elastimem's own graph-layer code.

**How Did You Use Claude?**

Claude is the model actually driving the agent: a native Anthropic Messages API provider built for this event speaks Anthropic's real wire format directly, not an OpenAI-compatible shim, and Claude Haiku 4.5 is the default model so both the tool-calling loop and Elastimem's background memory-extraction pipeline run on Claude out of the box. Specifically, Claude is what "online" mode means in Tuffy CLI: the enforced online/offline toggle puts Claude in the driver's seat whenever the agent is online, reasoning, calling tools, and driving memory extraction itself, and only falls back to a local model when offline.

Verified live against the real API:

- Streaming, a full tool-use loop with self-correction, and code execution rather than asserted answers.
- Elastimem's memory pipeline (remembering, recalling, building context) all confirmed working end to end with Claude generating the completions.

Claude is also the reasoning engine behind the graph-memory capability that is this submission's centerpiece, extracting entities and relationships into Elastimem's knowledge graph and grounding replies in what the graph surfaces back.

[Kumarswami Kallimath](https://github.com/CodebyKumar)

`2026-08-08`

---

### Codesearch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codesearch-d799) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shivamg5080/codesearch) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://das.boats/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/abc4469749d64a7c8fcbffb77a06d039) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> DSA platform for the AI era: Socratic hints

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**What is the problem your project solves?**

The problem

Competitive programming is the gateway to software jobs in India, but the tooling around it fails the majority of the people trying to walk through it — in two compounding ways.

It's English-only. Codeforces, CodeChef, CSES, LeetCode, and every tutorial layered on top assume fluent technical English. A student in a Tier-2 or Tier-3 town who thinks, reasons, and asks questions in Hindi, Tamil, Telugu, Bengali, or Marathi has to first translate the problem, then translate their own confusion, then translate the explanation back. The language barrier taxes every single step, and it hits hardest exactly when the student is already stuck.

It's solution-first. When that student finally asks for help, the internet hands them a finished solution — an editorial, a GitHub answer, or an AI assistant that dumps working code on the first ask. They unblock and learn nothing. The pattern behind the problem, the part that transfers to the next problem, never lands. This is how people grind hundreds of problems and still freeze in an interview.

Why it matters

The students most excluded by both barriers are the ones with the least access to a human mentor. English-medium, metro students have coaching, seniors, and peer groups. Everyone else has a search bar. That gap isn't about ability — it's about who gets a patient tutor and who gets a copy-pasteable answer.

Our solution and its impact

CodeSearch is an AI tutor that refuses to give away the answer, and speaks your language out loud.

- Vernacular-first, by voice. Ask "मुझे इसमें hint दो" into the mic and hear the reply in Hindi. Sarvam AI powers speech-to-text (saaras:v3, with automatic language detection), text-to-speech (bulbul:v2), and the tutoring brain (sarvam-30b) across 11 Indian languages — while code, variable names, and math stay intact in English, the way real engineers actually speak.
- Hints, not spoilers. A strict five-level hint ladder walks the learner from a nudge toward the right idea to a full explanation, and the tutor pushes back on "just give me the code." This is our core guarantee, so we measure it rather than assume it: an eval harness plays an escalating learner against the real system prompt across 20 classic problems, and CI fails the build if casual hint requests ever leak a solution.
- One bank, four judges. Codeforces, CodeChef, CSES, and LeetCode problems, searchable in one place, with an in-browser C++ runner.
- Learning that sticks. Spaced-repetition reviews and a progress dashboard turn one solved problem into a retained pattern.

The impact we're after is simple: give a student without a mentor, and without English, the thing a good senior would have given them — a patient voice in their own language that asks the next right question instead of handing over the answer.
Github link - https://github.com/shivamg5080/codesearch

**What is the deployed URL for this project?**

https://das.boats/

**How you are solving it?**

Our approach

We treated the tutor's restraint as the product. Anyone can wire an LLM to a problem statement; the hard part is building something that consistently refuses to hand over the answer, in a language the learner actually thinks in. So we made two architectural commitments: pedagogy lives in versioned prompt files, not scattered through application code, and that pedagogy is measured in CI rather than assumed.

What we built

CodeSearch is a Next.js 16 (App Router, React 19, TypeScript) application with four working surfaces:

1. A problem bank — Codeforces, CodeChef, CSES, and LeetCode ingested into one searchable Postgres table with normalized 1–10 difficulty and per-judge tag vocabularies. Statements are fetched and cached lazily on first open.
2. A voice tutor workspace — the problem, the learner's code, and a live chat panel side by side, with a mic bar.
3. An in-browser C++ runner — write, compile, and run against sample input without leaving the page.
4. A progress dashboard — real per-user analytics over solved/attempting/bookmarked status, topic breakdowns, and spaced-repetition reviews.

How it works

The tutoring loop. The workspace streams to /api/copilotkit, an in-process CopilotKit runtime — no second service to deploy. The route auth-gates the request and enforces a per-user daily message cap (incrementing before checking, so concurrent requests can't slip past it), then builds a chat adapter pointed at Sarvam.

Each turn, the model receives structured context: problem metadata, the statement, the learner's current code, the active tutor mode, and their current hint level. The system prompt is assembled as PEDAGOGY + MODE + GATE_REMINDER — and the hint-gate reminder is appended last, deliberately, because models weight trailing instructions most heavily. Every prompt string in the product lives in src/prompts/ and is imported from exactly one place, so a single edit propagates to all three consumers: the live runtime, an alternative LangGraph agent backend, and the eval harness. Application code never inlines prompt text.

The voice loop. The mic records → /api/voice/stt sends audio to Sarvam saaras:v3, which transcribes and auto-detects the Indian language → the UI switches the tutor into that language and sends the transcript as a chat turn → the reply is read back through /api/voice/tts (Sarvam bulbul:v2). Vernacular output is injected as additional instructions only when the language isn't English, so English learners pay no prompt overhead.

The hint ladder. Five escalating levels, from "here's the shape of the idea" to a full walkthrough, with the tutor pushing back on demands for finished code. Hint level is per-user, per-problem, and persisted.

Retention. Solving a problem schedules its first review; remembered advances a fixed interval ladder of [1, 3, 7, 16, 35, 90] days, forgotten resets to stage 0. A solved problem is never silently downgraded.

**How Did You Use Claude?**

We used Claude Code as the primary development environment for CodeSearch — not as a code-completion sidekick, but as the tool we built the architecture through. Claude is not a runtime dependency of the product (the tutor brain is Sarvam sarvam-30b, with OpenAI as an optional switch); it's how the product got built and kept honest.sidekick, but as the tool we built the architecture through. Claude is not a runtime dependency of the product (the tutor brain is Sarvam sarvam-30b, with OpenAI as an optional switch); it's how the product got built and kept honest.

Encoding the constraints instead of re-explaining them. The repo carries a CLAUDE.md and an AGENTS.md that act as durable project memory. AGENTS.md opens with a warning that this is Next.js 16 — a version with
breaking changes that postdate most modcts the agent to read the bundled docsin node_modules/next/dist/docs/ before writing a line of code. CLAUDE.md records the things that only become
obvious after reading several files: thbackends is live, that prompts live inexactly one directory and application code never inlines them, that GATE_REMINDER is appended last on
purpose, that Sarvam needs reasoning_efty content. Every session started withthat context instead of rediscovering it.

Where it did the heavy lifting. The work that benefited most was the structural refactoring, not the greenfield typing — consolidating every scattered prompt string into src/prompts/ with a single import site
so one edit propagates to the live runt the evals simultaneously; building thehint-leakage eval harness and wiring it into CI; hardening the hint gate and correcting the eval baselines when the first numbers turned out to be optimistic; and writing the EC2 + Caddy + pm2 deployment recipe that put the app on its own domain.

A convention we actually enforced. One rule in CLAUDE.md shaped the codebase more than any other: comments
explain why, and usually name a measured around an API quirk, we recorded thesymptom. That's why the Sarvam adapter carries a comment explaining that removing reasoning_effort: "low"
breaks the tutor "in ways that look lik — a note that will save whoever touches it next an afternoon.

And for the submission itself. We connected Devfolio's MCP server to Claude Code and drafted this submission through it, with Claude reading the repo to ground each answer in what the code actually does rather than what we remembered building.

Team **UP93** -- Shivam Gupta, [Shivansh Gupta](https://github.com/shivanshgupta365)

`2026-08-08`

---

### BugForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bugforge-f259) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mohitpaddhariya/bugforge) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/6b25a1b49c4c4d42952e22ffb71c77a4) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/6b25a1b49c4c4d42952e22ffb71c77a4) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> Ticket in, verified pull request out.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Playwright](https://img.shields.io/badge/Playwright-333333?style=flat-square)

**How you are solving it?**

Two halves that need each other.

## ShopForge — the test track

A small e-commerce app (login → cart → coupon → checkout → orders) running in Docker across 6 services: `web` (Next.js 15, ships the browser telemetry tracker), `api` (FastAPI + SQLAlchemy), `collector` (ingest + query, deliberately separate), `db` (Postgres, schemas `shop` and `telemetry`), `supportdesk` (tickets, with no dependency on the store so it stays up when the store breaks), and `gitea` (sandboxed git host).

**Trace correlation is the piece everything depends on.** A trace ID is minted per *user interaction*, not per HTTP request, so one click that fires three API calls produces one trace. It rides an `X-Trace-Id` header into the API and is written onto every log line, SQL statement, business event and stack frame. One query returns both sides on one clock:

```
t_5fade 43.194  WEB   click #place-order
t_5fade 43.219  API   coupon_applied  SAVE20 uses=4
t_5fade 43.231  API   ERROR  CheckViolation           checkout.py:71
t_5fade 43.242  WEB   POST /api/checkout → 500
t_5fade 45.400  WEB   click #place-order   ← retried
t_5fade 48.900  WEB   click #place-order   ← retried
```

Those last two lines are the whole argument for doing this: the customer got no feedback, which is why the ticket says "spinning" and not "error".

**Five planted bugs**, each switchable at runtime, each with a written answer key giving file, cause and expected symptom:

- **Coupon race (TOCTOU)** — backend concurrency. Can the agent deliberately induce a race?
- **Invisible click**, an overlay eating the mobile button — frontend only, **zero backend logs**. Diagnosable only from the click's real hit target.
- **`total_cents` → `total` rename** — contract drift. Requires reading both sides of the boundary.
- **Order IDOR** — authorization. Recognising a security issue from an innocent-sounding ticket.
- **Expired coupon** — **not a bug**. Must be closed with no patch.

**Historical telemetry is generated, never faked.** For the agent to investigate "the customer's session from Tuesday," that session has to exist first. Rather than hand-writing telemetry rows, seeding *drives the broken app* as the customer — including the human parts, like clicking the button three times and giving up. The telemetry is real because it was really produced. Each seeded run asserts its own symptom appeared and fails loudly otherwise: **31/31 confirmed across four consecutive resets.**

## The bug-triage skill — the agent

1. Searches telemetry for the customer's session and reads the merged timeline
2. Reads the implicated source and states a root cause naming a file and a line
3. Reproduces the bug in a real browser, recording video and a Playwright trace
4. Writes a test that fails
5. Fixes the root cause
6. Verifies three ways: new test passes, full suite passes, and the original browser reproduction re-runs clean
7. Opens a PR with the root cause, the evidence timeline, and the before/after video

"Cannot reproduce" and "working as intended" are first-class successful outcomes. One of the five tickets is not a bug at all, and the correct behaviour is to close it without touching code.

Run state lives on disk at `.bugforge/runs/<ticket>/`, not in context, so a run survives a restart and any harness can resume one it did not start.

## Ticket #1042, end to end

The agent reached the root cause from telemetry alone, in five commands, before opening a browser. Graded against the answer key written in the design doc:

- **File** — key: `api/app/routers/checkout.py`. Agent: `checkout.py:71` ✅
- **Cause** — key: read-modify-write on `coupons.uses` without row locking. Agent: the same, and it also named the time-of-check site the key omits ✅
- **Secondary** — key: `web/app/checkout/page.tsx`, loading state never cleared. Agent: found at `page.tsx:99` ✅

```
✓ new_test    test_coupon_race — FAILED before, PASSED after
✓ full_suite  4 passed, 0 failed
✓ repro       symptom present before, absent after (same script, hash-pinned)
verdict: VERIFIED
```

`bf pr open` refuses to run on an unverified ticket. Result: https://github.com/mohitpaddhariya/bugforge/pull/1

## Not deployed publicly, deliberately

The store contains planted vulnerabilities — including an IDOR that exposes other users' orders — so hosting it on the open internet would be irresponsible. It's a one-command local stack instead: `docker compose up -d --wait` brings all six services up healthy in about 26 seconds.

## Challenges we ran into

**My own tooling faked a pass three times.** The most useful thing that went wrong. The reproduction helper sent a JSON body without a content-type header, so every authenticated call 401'd — and the reproduction reported **ABSENT**, i.e. "no bug here", while the bug was live and firing. A green result from a broken harness is worse than a red one. Two more of the same shape: `/api/debug/reset` wipes the sessions table and killed the browser's cookie mid-run; and Playwright names videos per page, so re-runs accumulated files and the GIF step picked an arbitrary old one. This is why every seeded run now asserts its own symptom and fails loudly. Silent degradation is the failure mode that matters in agent tooling, because everything downstream still looks fine.

**The race could not be filmed.** The 500 needs two checkouts to interleave. The browser's connection is already warm, so the customer's request won that race in every single recorded run — the camera kept ending up pointed at a success. I stopped trying to force it and split the evidence instead. The video shows the customer-visible half, which is deterministic: a rejected checkout the page never surfaces, the spinning button. The race itself is evidenced by the timeline and by `test_coupon_race`. The PR says exactly that in a sentence rather than implying the video shows something it does not.

**Making a race a reliable regression test.** A barrier alone was not enough — the first request usually finished before the second was dispatched, and the test passed while the bug was live. It now fires three concurrent checkouts, retries up to six collisions, and re-primes the coupon to `uses = max_uses − 1` between attempts. Verified in both directions: red with the bug on, green with it off.

## Key decisions

**The collector is a separate service.** The agent edits `api` code. If telemetry lived inside `api`, a bad patch could blind the agent mid-investigation. The observability plane has to survive the data plane. Verified by killing `api` and confirming the collector still served past telemetry.

**Trace ID per intent, not per request.** Per-request tracing answers "what happened during this HTTP call." Per-interaction tracing answers "what happened when the user clicked this" — which is the question a ticket actually asks.

**Exploration compiles to a deterministic script.** An LLM navigating a browser is the right tool for finding a path from a vague ticket and the wrong tool for proving a fix — if it re-navigates differently, "it worked the second time" proves very little. So the reproduction is a Playwright script run three times: to confirm, to verify, and by the reviewer. `bf verify` hashes it, so editing the script to make the "after" run pass voids the verification.

**"No patch" is a success state.** An agent that always produces a patch will confidently fix working code, and nobody will notice. Ticket 1046 exists to test the refusal.

## Honest status — what is and is not done

- Store, telemetry, seeded runs — complete, all acceptance criteria passing
- Skill + `bf` CLI — complete
- Ticket 1042 — **full loop, PR opened**
- Tickets 1043–1046 — bugs planted, tickets written, telemetry seeded, but **not yet run through the agent**
- browser-use exploration — **not wired up**; reproductions are plain Playwright, written against the CLI's scaffold
- Gitea — running, but the PR went to GitHub
- Scoring harness across all 5 bugs — **not built**

So: one of five tickets has been run end to end. The other four are staged, not demonstrated.

## Disclosure: pre-existing work, reused code, and AI assistance

**Pre-existing work: none.** The repository was created empty at the start of the event. Every line of application code, telemetry, skill instruction and design document in it was written during Push to Prod. This project has not been presented at another hackathon. Full history is public: 3 commits on `main` plus the fix branch, 141 tracked files.

**Third-party code**, used as ordinary dependencies, unmodified: Next.js 15, React, Tailwind, FastAPI, SQLAlchemy 2.0, Pydantic, psycopg2, Postgres 16, Playwright, httpx, PyYAML, Docker Compose, Gitea, ffmpeg. No code was copied from tutorials, templates, starters, or another project.

**AI assistance.** Built with Claude Code (Opus) — details in the Claude question, including a phase that used an 11-agent parallel workflow.

**Note on the "answer key written first" claim.** The bug catalogue — file, cause, expected symptom for all five bugs — was specified in `docs/01-store-spec.md` §7 before any implementation code existed. The per-bug YAML manifests were written in the same phase as the code, from that spec. So the claim is that the *specification* predates the implementation, which the commit history supports; it is not a claim that each manifest file predates its corresponding source file.

**Prior art this builds on, none of it reused as code:** SWE-bench (repo-only, no runtime), WebArena (task completion, not debugging), and commercial session-replay and error-monitoring tools, whose trace-correlation idea is the thing this project takes seriously and builds the rest on top of.

**What is the deployed URL for this project?**

https://github.com/mohitpaddhariya/bugforge

**What is the problem your project solves?**

Ticket in, verified pull request out — it reproduces the bug in a real browser, fixes the root cause, and re-runs the customer's exact path to prove it's gone.

Support tickets and stack traces live in different worlds. A customer writes "checkout just spins." An engineer has a 500 in a log somewhere. Connecting those two costs the first hour of every bug, and it's almost entirely mechanical: find the session, find the request, find the line, work out which of the customer's clicks caused it.

Meanwhile the AI tooling around this is pointed at the wrong half. Generating a plausible patch from a stack trace is close to solved. What isn't solved is **proof** — did it reproduce the bug or imagine one, did it fix the cause or silence the symptom, is the customer's symptom actually gone on the path the customer took, did it break something else.

Underneath that sits a measurement problem nobody talks about: **you cannot tell whether a bug-fixing agent was right.** A patch that looks reasonable and one that's correct read identically in a diff. SWE-bench is repo-only — no running UI, no telemetry. WebArena measures task completion, not debugging. So there is no public way to answer "is this agent any good at triage?"

## Why it matters

Every team now has an agent that will confidently hand them a patch. Nobody has a way to know whether to trust it. Review capacity, not patch generation, is the bottleneck — and review capacity is exactly what an unverifiable patch consumes.

## The impact

So bugforge builds the missing layer first: a running full-stack app, instrumented end to end, with five bugs whose causes were written down before any code existed. Once that exists, an agent's diagnosis can be graded instead of admired, and the interesting classes of bug become testable — races, mobile-only layout faults, contract drift across the frontend/backend boundary, authorization holes, and tickets that turn out not to be bugs at all.

The agent is the demo. The gym is the contribution — the thing other people's triage agents get measured against.

**How Did You Use Claude?**

Claude is the product's runtime, not just its build tool.

bugforge ships as a skill — `SKILL.md` plus a `bf` CLI. The split rule is explicit: if two competent engineers would produce the same output, it's a script; if they might disagree, it's Claude's call. Claude decides which session matches a vague ticket, what the root cause is, whether a reproduction confirms the symptom, and — critically — whether it's a bug at all. The CLI does telemetry queries, browser driving, test runs and git. Claude never hand-writes an HTTP request or parses a log format.

That split is what makes it harness-agnostic. Claude Code, Cursor, Codex, OpenHands and Aider agree on exactly three capabilities: read a file, write a file, run a shell command. The skill assumes only those. No MCP server, no subagents, no harness-specific tool calls.

On ticket #1042 Claude reached the correct root cause from telemetry alone, in five commands, before opening a browser — naming `checkout.py:71` and the read-modify-write on `coupons.uses`, plus a secondary frontend fault at `page.tsx:99` that the answer key did not even list.

**Claude Code built it, from an empty directory.** I wrote the specs and made the architecture calls — separating the collector from the API, tracing per user-interaction rather than per request, generating rather than faking historical telemetry, compiling browser exploration into a deterministic script. One phase ran a parallel multi-agent workflow: 11 agents on disjoint directories building the store from `docs/01-store-spec.md`, then integrating and adversarially verifying against the spec's acceptance criteria.

**The most useful thing that went wrong was in my own tooling.** The reproduction helper sent a JSON body without a content-type header, so every authenticated call 401'd — and the reproduction reported "no bug here" while the bug was live and firing. A green result from a broken harness is worse than a red one. That's why every seeded run now asserts its own symptom and fails loudly: silent degradation is the failure mode that matters in agent tooling, because everything downstream still looks fine.

[Mohit Paddhariya](https://github.com/mohitpaddhariya)

`2026-08-08`

---

### Watchman
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/watchman-179c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Syedowais312/watchman) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> Live pixel topology for your Kubernetes cluster

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![Kubernetes](https://img.shields.io/badge/Kubernetes-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![eBPF](https://img.shields.io/badge/eBPF-333333?style=flat-square) ![Hubble](https://img.shields.io/badge/Hubble-333333?style=flat-square) ![Cilium](https://img.shields.io/badge/Cilium-333333?style=flat-square)

**How you are solving it?**

## A live pixel canvas over three real data sources, with Claude as the query layer

Services render as pixel blocks. Real request traffic is drawn as moving dots along **observed** edges. A service turns red when it crosses a measured overload threshold. Every number on screen comes from a live source — there is no simulated or mocked data anywhere in the wired path.

### Architecture

```
Kubernetes API (watch)  ──┐
metrics-server API      ──┼──▶  Go aggregator (in-memory)  ──▶  WebSocket ──▶  pixel canvas
Hubble Relay (GetFlows) ──┘                │
                                           └──▶  Claude (Haiku 4.5)  ──▶  chat panel
```

A Go aggregator merges a client-go shared informer (pod state), metrics-server polling (CPU), and a Cilium/Hubble `GetFlows` gRPC subscription (eBPF-traced network flows) into one in-memory model, then pushes snapshot-on-connect + diffs over a WebSocket at 4Hz.

### Engineering decisions that were measured, not guessed

**The overload signal is CPU as a percentage of the pod's CPU request, threshold 200%.** I measured both candidate signals against the real app under real load:

| service | idle | under load | % of request |
|---|---|---|---|
| product-catalog | 2m | 1699m | **3398%** |
| frontend | 8m | 865m | **1730%** |
| astronomy-db | 3m | 677m | **1354%** |
| shipping / quote / email | 1–3m | 1–3m | ~6% (off this path) |

Idle tops out at 30% of request; loaded services land at 428–3398%. The 200% threshold sits in a wide empty gap, so it never flaps.

**I rejected request-rate as the primary signal after measuring it.** Flow-count sampling was non-monotonic — `product-catalog` measured 1289 flows/5s *idle* but blank *under load*, because the Hubble CLI drops events at high volume. Flow data is excellent for *drawing* traffic and useless for *gating* a blink.

**Edges are earned.** A line is drawn between two services only after Hubble has actually observed a flow for that pair. `payment` and `email` stay visibly edgeless because they are only reachable via `checkout`, which is disabled here — that is real, not a bug.

**React owns the shell only.** The canvas is driven by a plain `requestAnimationFrame` loop reading a mutable store the WebSocket mutates directly. Live pod state never enters React state — that would re-render every 500ms tick and visibly stutter.

**Colour is not the only cue.** Overload adds a heavier border, corner bolts, a `!` badge, a shake, and steam particles. Palette validated for colour-blind separation (worst all-pairs CVD ΔE 11.5).

**Load is real.** k6 runs as an in-cluster pod generating real HTTP traffic against the real app — it never injects events into the WebSocket. Driving load through `kubectl port-forward` dropped 18% of requests at 60 VUs, so `run-load.sh` runs k6 in-cluster instead.

### Disclosure

The visualization and aggregator were built before this hackathon. **The work completed during this hackathon is the Claude integration** — `aggregator/claude.go`, the `POST /api/chat` endpoint, and the frontend wiring (see the `Claude Haiku 4.5 as the chat reasoning layer` commit).

**How Did You Use Claude?**

## Claude is the query layer over measured telemetry — and is constrained so it cannot hallucinate

**Claude Haiku 4.5** turns the dashboard into something you can ask questions of. Instead of picking a panel and a time range, you ask *"did product-catalog overload?"* and get the peak value, wall-clock time, and incident duration.

### How it is wired

The Go aggregator maintains an **overload event log** — every threshold crossing it actually measured, with `service`, `metric`, `peak_value`, `start_time`, `end_time`, `duration`, `active`. `POST /api/chat` hands Claude that log as JSON alongside a system prompt that forbids invention:

```go
// aggregator/claude.go
resp, err := client.Messages.New(ctx, anthropic.MessageNewParams{
    Model:     "claude-haiku-4-5",
    MaxTokens: 256,
    System:    []anthropic.TextBlockParam{{Text: claudeSystemPrompt}},
    Messages:  []anthropic.MessageParam{
        anthropic.NewUserMessage(anthropic.NewTextBlock(userContent)),
    },
})
```

The prompt states: *"You may ONLY use the JSON event log provided... Never invent a service, a number, or an incident that isn't in the log. If the log doesn't answer the question, say so plainly instead of guessing."*

### Three deliberate engineering choices

**1. Grounding is verified, not assumed.** I tested the failure case explicitly. With an empty event log:

> **Q:** did product-catalog overload?
> **A:** "The event log is empty, so I cannot determine whether product-catalog overloaded. There are no incidents recorded."

It refuses rather than producing a plausible fabrication. For an observability tool this is the property that matters most — a monitoring system that invents incidents is worse than no monitoring system.

**2. Haiku 4.5, chosen deliberately.** The task is grounded fact-lookup over a small JSON payload, not open-ended reasoning. Haiku ($1/$5 per MTok) is the right tier; spending Opus-tier tokens on templated fact retrieval would be waste, and the latency matters in an incident.

**3. The key never reaches the browser.** Claude is called server-side from Go via the official `anthropic-sdk-go`, with `ANTHROPIC_API_KEY` read from the aggregator's environment. The frontend only ever talks to `POST /api/chat` on localhost. A rule-based matcher over the same event log remains as a fallback, so the demo still answers if the key is absent — but Claude is the primary path and the only one that handles paraphrased questions.

### Claude Code as the build tool

Claude Code did the integration work in this repo, including catching that the pre-existing chat module's docstring still claimed it was "deliberately NOT an LLM" and that a stale `GROQ_API_KEY` reference needed replacing — leftovers that would have made the submission's own documentation wrong.

**What is the deployed URL for this project?**

https://github.com/Syedowais312/watchman

**What is the problem your project solves?**

## Cluster observability makes you read graphs instead of seeing your system

When a Kubernetes service starts failing, the standard tooling hands you a wall of time-series dashboards. You are asked to reconstruct a **live, moving system** from a dozen static line charts — correlating CPU panels against request-rate panels against a service map that was drawn from a config file rather than from observed traffic.

Three specific things go wrong:

- **The topology is fiction.** Most service maps are generated from declared config, so they show edges that never carry traffic and miss the ones that do. You cannot tell what is actually talking to what.
- **Overload is buried in a number.** "CPU: 1699m" means nothing without the request as a denominator. Whether that is fine or on fire depends on context the dashboard does not show you.
- **Answering a question takes minutes.** "Did product-catalog overload in the last hour, and for how long?" requires picking the right panel, the right time range, and eyeballing a threshold crossing.

**Impact:** during an incident, the time spent translating dashboards into a mental model is time the outage continues. The information is all present — it is just not in a form a human can absorb at a glance or ask a question of.

Watchman's bet is that a cluster should be **seen and interrogated**, not decoded.

[Syed Owais](https://github.com/Syedowais312)

`2026-08-08`

---

### Croniter-port
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/croniterport-5deb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Aksh2758/croniter-java.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/841626b0bcf14cb187b8355691e573c2) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co)

> croniter, ported to Java. Same battle-tested cron

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

**Scoping a genuinely complex library under time pressure.** *croniter.py*
is ~1,335 lines of actual code, and a lot of that complexity is exactly
the stuff that's hard to get right even within the same language: DST
transitions (ambiguous/nonexistent local times during spring-forward and
fall-back), leap years, nearest-weekday (*W*) and nth-weekday-of-month
(*#, L*) logic, and hash-based (Jenkins-style) scheduling. We had to be
deliberate about what to port fully vs. treat as a documented gap, rather
than rushing a "complete" port that silently broke on edge cases.

**Verifying correctness without just trusting our own Java code.** Rather
than eyeballing behavioral equivalence, we built a differential fuzz
harness that runs the same random cron expression + timestamp through
both the real Python *croniter* and our Java port and compares the actual
*get_next()*/*get_prev()* output.

**Reproducibility across machines.** Our original test entrypoint
(*make test*) depended on whatever local JDK/Python versions happened to
be installed, which gave inconsistent fuzz/bench results across our own
machines. We moved the whole build → test → fuzz → bench pipeline into
*docker compose up --build* as a single pinned entrypoint, so results are
reproducible for anyone running that one command.

**Keeping our own documentation honest.** Partway through, we caught our
own README/decisions doc describing API methods that didn't actually
exist in the shipped code (leftover from an earlier draft). We went back
and corrected the docs to match the real, verified API surface rather
than the more feature-complete-sounding version we'd originally sketched.

![image](https://assets.devfolio.co/content/3abfcb1af50941bbb9399c6458f7f895/c47e8f45-4530-4f92-a37a-b2e3c49ce5cd.jpeg)

**The problem it solves**

Java backend teams that need cron-style scheduling usually end up either
adopting Quartz's full scheduling framework (heavy, for a lot of teams
overkill) or hand-rolling their own cron parser (error-prone — DST, leap
years, and nth-weekday logic are easy to get subtly wrong).

Python's *croniter* already solves this well — it's a small, focused
library with a simple *get_next()/get_prev()* API, and it's genuinely
load-bearing infrastructure: 1.2B+ cumulative PyPI downloads, embedded in
tools like Prefect and Celery-based schedulers.

**croniter-java** ports that same simple API to the JVM, so Java teams get
the same battle-tested cron-parsing behavior without pulling in Quartz.
It's not a bridge or wrapper around the Python library — it's a from-
scratch Java reimplementation, validated against the original through
differential fuzz testing (random cron expression + random timestamp,
comparing output directly against real Python *croniter*

![image](https://assets.devfolio.co/content/3abfcb1af50941bbb9399c6458f7f895/3e3b0943-5a4d-4a6d-9107-fb503e7f964c.jpeg)).

Latest fuzz run: 19,600 cases in 60 seconds, 0 divergences.

Team **Dukes Exodus** -- Akshatha K S, Dnyandip Vadane

`2026-08-03`

---

### JSBI for Go
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/jsbi-for-go-a748) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sarthak-vats-cse/JSBI-Go) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/xqUuwPft_3M) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/xqUuwPft_3M) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co)

> A high-performance Go implementation of the JSBI B

![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square)

**The problem it solves**

JavaScript applications often rely on JSBI to perform arbitrary-precision integer arithmetic, especially in environments where native BigInt support is unavailable or where consistent BigInt behavior is required across platforms. However, developers migrating JavaScript projects to Go face the challenge of rewriting or replacing this functionality while preserving identical behavior.

JSBI-Go solves this problem by providing a Go implementation that preserves the semantics and developer experience of the original JSBI API. It enables developers to migrate applications from TypeScript/JavaScript to Go without redesigning their BigInt logic or changing application behavior.

This project supports essential BigInt operations such as arithmetic, bitwise operations, shifts, string parsing, radix conversions, integer conversions, and DataView-compatible functionality, making the migration process faster, safer, and more reliable.

**Benefits**
1. Simplifies migration from TypeScript/JavaScript to Go.
2. Preserves BigInt behavior across languages.
3. Reduces redevelopment effort during language migration.
4. Provides a familiar API for developers already using JSBI.
5. Includes automated tests to verify correctness and compatibility.

**Challenges we ran into**

One of the biggest challenges was preserving the behavior of the original JSBI library while adapting it to Go's programming model. JavaScript and Go differ significantly in their type systems, error handling, and support for arbitrary-precision integers, making a direct line-by-line translation impractical.

Another challenge was ensuring that JavaScript BigInt semantics—such as truncating integer division, bitwise operations on signed values, radix-based parsing, and integer conversion behavior (asIntN/asUintN)—were preserved after migration.

We also encountered project setup challenges while configuring the Go module, organizing the migrated source, and validating the implementation. These were resolved by setting up a proper Go project structure, running automated unit tests, verifying coverage, and continuously testing the migrated implementation against expected behavior.

To ensure reliability, we adopted an iterative migration approach: migrate functionality, compile, run tests, and verify behavior before proceeding to the next stage. This helped us identify issues early and maintain compatibility with the original JSBI API throughout the migration process.

**Key Challenges**
1. Preserving JavaScript BigInt behavior in Go.
2. Adapting language-specific features between TypeScript and Go.
3. Maintaining API compatibility while following Go best practices.
4. Validating correctness through comprehensive automated testing.
5. Ensuring the migrated implementation remained maintainable and easy to extend.

Team **Null_Pointers** -- [SARTHAK VATS](https://github.com/Sarthak-vats-cse), Ritesh Nayak, [Garv Rajput](https://github.com/garrygarry-arch), Mayank Srivastava

`2026-08-02`

---

### Mavi-Linking
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mavilinking-ce01) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mayur51015/Mavi-Linking) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mavi-linking-mq7d.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Ibnem0mGs3g) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co)

> From Learning to Hiring — All in One Platform.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Building MAVI Linking involved several technical and architectural challenges. One of the biggest challenges was designing a scalable role-based system for Students, Recruiters, Teachers, and Administrators while ensuring secure access through JWT authentication and role-based authorization. Integrating the frontend, backend, and MongoDB Atlas across cloud platforms such as Vercel and Render introduced issues like CORS configuration, environment variable management, API endpoint mismatches, deployment failures, and intermittent 503 Service Unavailable errors, which required systematic debugging and server configuration improvements.

Another major challenge was designing a unified data model that allows different roles to collaborate without duplicating information. Building features such as placement workflows, real-time notifications, secure messaging, and synchronized status updates across dashboards required careful planning of database relationships and APIs.

As the project evolved, it became clear that a simple portfolio platform was not enough. The architecture had to be redesigned to support a long-term vision of a Developer Career Ecosystem, incorporating mentorship, career guidance, recruitment management, analytics, and AI-ready modules. These challenges were addressed by refactoring the project into modular components, improving API design, optimizing database schemas, strengthening authentication and validation, and planning scalable communication and workflow systems that can support future growth.

**The problem it solves**

Today's students, freshers, recruiters, and educational institutions rely on multiple disconnected platforms for career development and recruitment. Students use GitHub for code, LinkedIn for networking, coding platforms for practice, email and messaging apps for communication, and separate placement portals for job applications. This fragmented workflow makes it difficult to showcase skills, track progress, receive mentorship, and manage recruitment efficiently.

MAVI Linking solves this problem by bringing the entire career and recruitment journey into one unified platform. Students can create verified developer profiles, showcase projects, certifications, coding achievements, and track their placement readiness. Teachers can monitor student progress, provide career guidance, verify projects and certificates, conduct mentoring sessions, and communicate directly with students. Recruiters can discover verified talent, post job opportunities, manage hiring pipelines, schedule interviews, evaluate candidates, and collaborate with teachers throughout the recruitment process.

The platform also provides role-based dashboards, secure messaging, real-time notifications, document verification, placement management, analytics, QR-based profile sharing, and AI-ready modules for candidate ranking, resume analysis, skill-gap assessment, and career recommendations.

By replacing fragmented tools with a single collaborative ecosystem, MAVI Linking simplifies career development, improves communication, increases trust through profile verification, streamlines campus placements, and enables faster, more informed hiring decisions for both educational institutions and recruiters. It empowers students to grow professionally while helping colleges and companies build a more efficient and transparent recruitment process.

[Mayur Khandare](https://github.com/Mayur51015)

`2026-08-03`

---

### EdgeLence
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edgelence-ed82) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/debaa98/EdgeLence) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://edge-lence.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co)

> an eBPF-based auto-capture agent — observability

![GraphQL](https://img.shields.io/badge/GraphQL-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**Challenges we ran into**

as a single Rust binary that ingests and queries logs, metrics, and traces by storing everything as Parquet files and querying them with the DataFusion engine, instead of standing up a separate database server

**The problem it solves**

The genuinely hard, more interesting problem is capturing HTTP/gRPC traffic straight off the wire, from the kernel, without touching the app's code at all — the trick Pixie and Odigos use at the platform level. Rust isn't a stylistic choice here, it's close to load-bearing: Aya, the Rust eBPF library, is built from the ground up without relying on libbpf or bcc — it makes raw syscalls itself through the libc crate, so you get a real eBPF toolchain without ever touching C

[Debabrata Pattnayak](https://github.com/debaa98)

`2026-08-03`

---

### robfig-cron-rs
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/robfigcronrs-6eb8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/f-ei8ht/robfig-cron-rs) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cron-rs-site.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tW3ivQR0WmE) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co)

> Same cron. No GC. Zero unsafe.

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Golang](https://img.shields.io/badge/Golang-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square)

**Challenges we ran into**

1. The StepAboveMax Silent Bug (Upstream Issue #543)
Differential fuzzing revealed that Go's parser silently accepts */90 * * * * -- a step value of 90 on a minute field whose maximum is 59. It produces a wrong schedule instead of rejecting the expression. This wasn't a translation bug; it was a pre-existing upstream Go bug that the port initially inherited by faithfully mirroring Go's get_range logic.
How I got over it: Added a StepAboveMax { step, max, expr } error variant to CronError and inserted the validation check in get_range immediately after the existing step == 0 check. A regression test with four cases was added. Re-running the 204,425-case fuzz suite confirmed zero unintended divergences (30,663 intentional StepAboveMax rejections tracked separately).

2. chrono DateTime<Tz> Overhead Killing Next() Throughput
The Rust port's Next() throughput (schedule computation) was ~500K ops/sec versus Go's ~1M ops/sec. The root cause was that chrono::DateTime<Tz> carries a full timezone offset and performs heavier arithmetic than Go's lightweight 24-byte time.Time. The paranoid corollary was that a naive-arithmetic rewrite (dropping timezone-aware DateTime in favor of plain integer math) could silently introduce DST-correctness regressions.
How I got over it: Documented the tradeoff honestly in DECISIONS.md and bench/methodology.md. Parser throughput was improved from ~700K to ~2.5M ops/sec by replacing per-parse HashMap rebuilds with const static lookup tables. Deferred the DateTime rewrite to a follow-up because DST correctness matters more than a microbenchmark number in a scheduler.

3. The Stop Handler Deadlock During Job Await
Go's Stop() returns after jobWaiter.Wait() -- all in-flight jobs finish. The naive Rust translation would spawn a watcher task that awaits the atomic job counter to hit zero, then resolves the oneshot sender. But run_loop runs inside Runtime::block_on, which returns the moment run_loop returns -- aborting any just-spawned job tasks before they complete.
How I got over it: The Stop handler waits for in-flight jobs inline inside the run loop before resolving the oneshot, so the worker thread's block_on keeps the runtime alive until every queued job task is done. The running_jobs counter uses lock-free AtomicUsize + tokio::sync::Notify instead of spawning a separate watcher.

4. FastDelay Schedule Producing Catch-Up Spin, Not Lateness
An early version of the benchmark's FastDelay schedule subtracted the nanosecond fraction from now before computing next, which landed next in the past ~95% of the time. The tick lateness metric became a catch-up spin loop measuring re-dispatch cost rather than actual scheduling lateness.
How I got over it: Rewrote FastDelay::next to always return from + period (never in the past) in both the Rust harness and the Go bench-helper. Now the lateness numbers reflect real scheduling accuracy.

5. Dedicated OS Thread vs Run-of-the-Mill tokio::spawn
Using tokio::spawn on the caller's runtime would cause stop()'s blocking_recv to deadlock when called from the same runtime. Using a shared multi-task runtime would let long-running user jobs starve the schedule-wake timer through cooperative fair-share scheduling.
How I got over it: Every Cron::start() spawns a dedicated OS thread that owns its own single-threaded tokio runtime. This keeps scheduling latency off the shared fair-share queue and makes stop() callable from any context (including #[test] functions without an async runtime entry).

**The problem it solves**

**robfig-cron-rs** is a faithful Rust port of robfig/cron (the Go library with 14,000+ stars that powers cron scheduling in thousands of Go applications). 

The port addresses the core limitation of Go for latency-critical scheduling workloads: Go's garbage collector (GC) introduces unpredictable pause times into the cron loop (sleep → wake → run job). 

Those stop-the-world pauses can cause scheduled jobs to fire late, a multi-second spike buried in the tail.

What people can use it for: Exactly what the original Go library is used for, scheduling recurring tasks in any Rust application. 

Install a job to run every 5 minutes, every hour at half-past, on the first Monday of every month, or at any cron expression. Ship a background task, a periodic cleanup, a heartbeat probe, a data pipeline trigger, without GC jitter.

How it makes tasks easier and safer:
- Zero unsafe blocks -- every concurrency primitive, timezone math, and panic recovery path is implemented in safe Rust.
- Architecturally immune to upstream bugs: The port discovered and fixed a silent bug in the Go original where */90 * * * * would parse without error and produce a fundamentally wrong schedule. The Rust port rejects this cleanly with Step above field maximum. It is also immune to issue #568 (stale timer values after Windows Fast Startup resume) because it always reads the live wall clock instead of trusting the timer channel.
- Predictable tail latency proven under sustained load: A 4-hour soak test with 64.5 million ticks across 461 progressively-added jobs held p99 lateness flat at 2.27 ms -- no GC spikes.
- One-command verification: docker run --rm -it robfig-cron-rs launches an interactive TUI dashboard with integrated test runner, differential fuzz, benchmark suite, and interactive sandbox.

[Saif Ali Khan](https://github.com/zzorgg)

`2026-08-03`

---

### Testy-Claw
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/testyclaw-3e49) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tesyclaw.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> #cliagent #agenticworkflow

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square)

**Challenges we ran into**

While building the CLI agent, one of the biggest hurdles I faced was managing the interaction between the AI model and local system tools.

Initially, the agent could generate commands correctly, but executing those commands safely and handling unexpected outputs was challenging. For example, a command might fail because of a missing dependency, incorrect directory context, or an environment-specific issue, and the agent did not have enough context to recover.

I solved this by introducing a structured tool execution layer between the agent and the operating system. Instead of allowing the model to directly execute commands, I created predefined tools with clear inputs and outputs. Each tool returned structured responses containing the command status, error messages, and execution results, which were then sent back to the agent for reasoning.

I also added better error handling, logging, and validation around tool calls. This made the agent more reliable because it could understand failures, adjust its approach, and retry with better context.

This experience taught me the importance of designing AI agents with controlled tool access, observability, and predictable interfaces rather than relying only on the model's generated output.

**The problem it solves**

Developers often need to repeatedly perform tasks like understanding codebases, running commands, generating files, debugging issues, and automating workflows. Existing CLI tools require manual commands and deep knowledge of different tools. A CLI agent provides a natural language interface where developers can ask an AI agent to perform tasks on their behalf.

https://tesyclaw.vercel.app/

https://github.com/pritamscodee/tesyclaw

![image](https://assets.devfolio.co/content/fcc174f46e2a41dfbc07db9385ff9490/f943e704-c8f2-43ef-a768-1158033e652e.jpeg)

![image](https://assets.devfolio.co/content/fcc174f46e2a41dfbc07db9385ff9490/cf86a2d8-25d4-4b0b-a823-891719051cfe.jpeg)

[Pritam mondal](https://github.com/pritamscodee)

`2026-06-21`

---

### Artifex
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/artifex-a-productiongrade-multiagent-ai-platform-for-foster-care-intelligence-6303) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://artifex-woad-beta.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> AI platform for smarter foster care decisions

![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Reactstrap](https://img.shields.io/badge/Reactstrap-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Microservice Architecture](https://img.shields.io/badge/Microservice%20Architecture-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![DigitalOcean](https://img.shields.io/badge/DigitalOcean-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**Challenges we ran into**

Building Artifex involved several technical and architectural challenges.

### Multi-Agent Coordination

One of the biggest challenges was designing a reliable multi-agent system where specialized agents (Planner, Risk, Matching, Fairness, Approval, and Monitoring) could collaborate without creating race conditions, duplicated work, or inconsistent workflow states.

We solved this by introducing workflow orchestration with Temporal and event-driven communication through NATS, allowing agents to operate independently while maintaining a consistent source of truth.

### Long-Running Workflow Reliability

Foster care processes can span days, weeks, or even months. Traditional request-response architectures were not suitable for workflows that needed to survive service restarts, failures, and extended periods of inactivity.

To address this, we implemented durable workflows that automatically recover from failures and preserve execution state across the entire placement lifecycle.

### Explainability and Trust

Generating recommendations was relatively straightforward; making those recommendations understandable and trustworthy was significantly harder.

We built explainable decision pipelines that provide confidence scores, reasoning traces, workflow histories, and agent-level explanations so caseworkers can understand why a recommendation was produced rather than treating the system as a black box.

### Fairness and Bias Monitoring

Because foster care decisions directly impact vulnerable children, fairness was a critical requirement. Designing fairness audits that continuously monitor demographic parity, bias drift, and decision disparities while remaining interpretable required extensive experimentation.

We developed dedicated fairness monitoring workflows and dashboards that surface potential disparities and allow human reviewers to investigate them before action is taken.

### Digital Twin Simulation

Creating realistic "what-if" simulations for foster care interventions was another significant challenge. Predicting how interventions such as increased therapy, school changes, or additional family visits could influence future outcomes required balancing predictive modeling with uncertainty estimation.

We addressed this by building a Digital Twin framework that evaluates alternative intervention scenarios and presents confidence-aware projections rather than deterministic predictions.

### Full-Stack Integration

Artifex combines AI orchestration, machine learning models, workflow engines, real-time event streaming, fairness auditing, monitoring systems, and interactive dashboards. Integrating these components into a unified platform while maintaining performance and usability required substantial engineering effort.

Through iterative testing, workflow tracing, and continuous debugging, we successfully built a cohesive platform that demonstrates how production-grade Agentic AI systems can support complex social-impact decision making.

**The problem it solves**

# Artifex

## Problem Statement

Foster care agencies face complex challenges when evaluating referrals, matching children with suitable foster families, monitoring placements, and identifying risks before crises occur. These processes are often fragmented across multiple systems, rely heavily on manual coordination, and provide limited visibility into ongoing cases.

As a result, agencies frequently encounter:

* Suboptimal placement decisions
* Delayed identification of placement risks
* Limited real-time case visibility
* Fairness and bias concerns in AI-assisted decisions
* Lack of transparency and accountability
* Operational inefficiencies caused by disconnected workflows

These challenges directly impact placement stability, child well-being, and long-term outcomes.

---

## Solution

Artifex is an AI-powered foster care intelligence platform that combines Agentic AI, workflow orchestration, machine learning, and responsible AI governance to support social workers throughout the foster care lifecycle.

Rather than replacing human decision-makers, Artifex acts as an intelligent decision-support system that helps agencies make faster, fairer, and more informed decisions.

Key capabilities include:

* AI-powered foster family matching
* Placement risk prediction and early intervention
* Multi-agent workflow orchestration
* Real-time monitoring and event streaming
* Human-in-the-loop approvals
* Fairness auditing and bias detection
* Explainable AI recommendations
* Digital Twin simulation for intervention planning
* Tamper-evident AI audit trails

---

## How It Works

### Multi-Agent AI Orchestration

Artifex uses specialized AI agents that collaborate to process referrals, assess risk, generate recommendations, validate decisions, and monitor ongoing placements.

The platform includes:

* Planner Agents
* Risk Assessment Agents
* Matching Agents
* Validator Agents
* Monitoring Agents
* Supervisor Agents

Agents dynamically coordinate through durable workflows and event-driven communication.

### Placement Matching

The matching engine evaluates:

* Age compatibility
* Geographic proximity
* Language preferences
* Medical and behavioral needs
* Family capacity
* Historical placement outcomes

Recommendations include confidence scores and clear explanations.

### Risk Prediction

Artifex continuously analyzes placement data to identify potential disruptions before they occur.

The system monitors:

* Placement history
* Family characteristics
* Child needs
* Behavioral trends
* Weekly check-ins

High-risk cases trigger alerts and intervention recommendations.

### Responsible AI

Every recommendation is:

* Explainable
* Auditable
* Human-reviewable

The platform continuously measures fairness using demographic parity, equalized odds, calibration metrics, and bias drift detection.

---

## Technical Architecture

Artifex is built using:

* FastAPI
* LangGraph
* Temporal Workflows
* NATS Event Bus
* PostgreSQL
* Qdrant Vector Database
* Redis
* Machine Learning Models
* WebSocket Real-Time Streaming

The system follows an event-driven, fault-tolerant architecture designed for long-running workflows and production-scale deployment.

---

## Innovation

Artifex introduces several novel capabilities:

* Self-healing multi-agent AI orchestration
* Multi-model consensus validation
* Real-time workflow intelligence
* Human-centered AI governance
* Automated fairness auditing
* Explainable placement recommendations
* Digital Twin simulation for child welfare planning
* Tamper-evident AI decision logging

The project demonstrates how Agentic AI can operate as a reliable decision-support partner in mission-critical social impact domains.

---

## Impact

Artifex aims to:

* Improve placement stability
* Reduce placement disruptions
* Detect risks earlier
* Support social workers with actionable insights
* Increase operational efficiency
* Improve fairness and transparency
* Build trust in AI-assisted decision-making

By combining Agentic AI, workflow orchestration, machine learning, and human oversight, Artifex provides a scalable blueprint for the future of intelligent child welfare systems.

Team **How's Life** -- Saatvika Reddy, [Adwika Vishal](https://github.com/AdwikaVishal), Shantanu Singh

`2026-06-07`

---

### AI-Powered Career Guidance and Resume Intelligence Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-career-guidance-and-resume-intelligence-platform-4f4d) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Empowering students with AI-driven resume analysis

Team **Zenmaster** -- Tanush R

`2026-07-30`

---

### Racecraft AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/racecraft-ai-04c8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CzPhantom10/F1-AgenticAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://f1-agentic-ai.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_QOfYiclPxk) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> An Agentic AI Engine for Formula 1

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square)

**Challenges we ran into**

Building Racecraft AI required solving several challenges beyond simply connecting an LLM to Formula 1 data.

### 1. Hallucinated Analysis
Early versions allowed the language model to perform calculations and rankings directly. This frequently produced confident but incorrect conclusions, especially for comparisons and race predictions.

**Solution:**  
I moved all statistical computation into dedicated analysis agents and restricted the LLM to explanation and reasoning. The model now explains results instead of generating raw calculations.

### 2. Historical Data Integration
Formula 1 data spans decades and comes from multiple sources with different structures and naming conventions.

**Solution:**  
I created a preprocessing pipeline that normalizes drivers, constructors, circuits, race results, and standings into a unified format that can be queried consistently.

### 3. Context-Aware Conversations
Follow-up questions often depended on previous queries, requiring the system to remember entities, circuits, and comparisons.

**Solution:**  
Implemented a memory layer that stores conversation context and passes relevant information to the orchestrator agent for subsequent queries.

### 4. Race Prediction Reliability
Naive prediction models simply favored championship leaders regardless of track characteristics.

**Solution:**  
Built a dedicated prediction engine that incorporates recent form, track history, constructor strength, podium frequency, average finishing position, and circuit-specific performance.

### 5. Performance Optimization
Real-time analysis across large historical datasets created noticeable latency.

**Solution:**  
Precomputed driver intelligence, constructor intelligence, and circuit intelligence datasets that can be retrieved instantly by agents during execution.

**The problem it solves**

Formula 1 data is scattered across race results, standings, historical records, and circuit statistics. While fans can access raw information, extracting meaningful insights often requires manually analyzing multiple sources and comparing large amounts of data.

Racecraft AI solves this by combining historical race intelligence, championship data, circuit-specific performance metrics, and AI-powered reasoning into a single platform.

Instead of simply displaying statistics, the system uses an agentic AI architecture where specialized agents retrieve, analyze, compare, and predict outcomes before generating natural-language explanations.

Users can:

- Compare drivers, constructors, and seasons
- Analyze performance at specific circuits
- Explore historical Formula 1 data
- Generate race predictions using historical and current season trends
- Ask follow-up questions through a conversational AI interface
- Retrieve context-aware insights instantly

The platform transforms complex motorsport datasets into actionable intelligence, making Formula 1 analysis accessible to both casual fans and data-driven enthusiasts.

[Prateek Sinha](https://github.com/CzPhantom10)

`2026-06-14`

---

### Mavi-Linking
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mavilinking-dc1c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mayur51015/Mavi-Linking) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Ibnem0mGs3g) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> One Profile. Unlimited Opportunities.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React Router](https://img.shields.io/badge/React%20Router-333333?style=flat-square) ![bycryptjs](https://img.shields.io/badge/bycryptjs-333333?style=flat-square)

**The problem it solves**

MAVI Linking solves the problem of fragmented developer identities. Students and freshers often have skills, projects, coding profiles, certificates, and achievements spread across multiple platforms, making it difficult for recruiters and colleges to evaluate them effectively. The platform provides a unified developer profile where users can showcase their technical skills, projects, achievements, and professional growth. It simplifies recruitment, placement tracking, portfolio sharing, and skill assessment through a single intelligent and shareable profile with QR-based access.

**Challenges we ran into**

One of the biggest challenges was integrating multiple profile systems and creating a scalable role-based architecture for Users, Recruiters, and College/Teacher dashboards. Another challenge was managing secure authentication using JWT and connecting the frontend, backend, and MongoDB Atlas across different deployment platforms. During deployment, issues such as expired GitHub tokens, environment variable configuration, MongoDB connection setup, CORS restrictions, and Render deployment errors were encountered. These challenges were resolved through proper API configuration, secure environment management, database optimization, and deployment debugging.

[Mayur Khandare](https://github.com/Mayur51015)

`2026-06-15`

---

### Neural style transfer (NST)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neural-style-transfer-nst-0ea8) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> It's convert your normal image into any style image

[Yash singh](https://github.com/yashsingh-tech99)

`2026-07-30`

---

### KnowDoc AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/knowdoc-ai-ca06) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Yashank024/KnowDoc) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://knowdoc.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/rT09NK0a9Ng) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Transform PDFs into an intelligent conversational

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GeminiAPI](https://img.shields.io/badge/GeminiAPI-333333?style=flat-square)

**The problem it solves**

**KnowDoc AI** is an enterprise-grade document intelligence platform that **combines OCR, Retrieval-Augmented Generation (RAG)**, semantic search, vector databases, and Google Gemini to transform unstructured documents into an intelligent conversational knowledge base.

Every organization stores critical information inside PDFs, invoices, contracts, reports, and scanned documents. Finding specific information requires manually reading hundreds of pages, making document retrieval slow, expensive, and error-prone.

KnowDoc AI eliminates this problem by converting unstructured documents into an intelligent knowledge base. Users can upload documents and ask questions in natural language. Instead of searching manually, the system retrieves relevant information using semantic search and Retrieval-Augmented Generation (RAG), delivering fast, accurate, context-aware answers.

**Inspiration**

Modern businesses generate thousands of documents every month, but most of this information remains locked inside PDFs. Traditional keyword search cannot understand document context.

The project was inspired by the idea of combining OCR, Vector Databases, RAG, and Large Language Models to build an AI assistant capable of understanding enterprise documents just like a human researcher.

**What it does**

KnowDoc AI is an AI-powered document intelligence platform that transforms PDFs and scanned documents into a searchable conversational knowledge base.

**The system:**

Uploads PDFs and scanned documents
Extracts text using PaddleOCR
Splits documents into semantic chunks
Generates vector embeddings
Stores embeddings inside ChromaDB
Retrieves relevant context using semantic search
Uses Google Gemini to generate grounded answers
Provides citation-based AI responses
Supports enterprise-scale document search
How we built it

The frontend was developed using Next.js, React, and Tailwind CSS, providing a responsive and modern user experience.

The backend was built with FastAPI, exposing REST APIs for document upload, OCR processing, indexing, retrieval, and AI chat.

The AI pipeline follows a Retrieval-Augmented Generation (RAG) architecture. Uploaded PDFs are processed with PaddleOCR to extract text from scanned documents. The extracted text is divided into semantic chunks, converted into embeddings using HuggingFace Sentence Transformers, and stored inside ChromaDB. When a user submits a question, the system retrieves the most relevant document chunks through semantic vector search and sends only this context to Google's Gemini model, enabling accurate and grounded responses while minimizing hallucinations.

The application is deployed using Vercel (frontend) and Railway (backend).

**Challenges we ran into**

**Challenges we ran into**

Handling scanned PDFs with inconsistent image quality
Building an efficient RAG pipeline for accurate retrieval
Optimizing semantic chunking for better context preservation
Integrating OCR with vector indexing
Deploying frontend and backend across Vercel and Railway
Managing environment variables and Gemini API securely
Reducing hallucinations by grounding responses in retrieved context
Accomplishments we're proud of
Built a complete AI-powered document intelligence platform from scratch
Successfully integrated OCR, RAG, ChromaDB, and Gemini AI
Developed a conversational interface for enterprise documents
Implemented semantic search instead of traditional keyword search
Deployed a production-ready full-stack AI application
Created a scalable architecture suitable for future enterprise expansion
What we learned

**During this project we gained practical experience in:**

Retrieval-Augmented Generation (RAG)
Large Language Model integration
OCR pipelines
Semantic Search
Vector Databases
Embedding generation
Prompt Engineering
FastAPI backend development
Cloud deployment using Railway and Vercel
Full-stack AI application architecture
What's next for KnowDoc AI

**Future versions of KnowDoc AI will include:**

Multi-user workspaces
Authentication and role-based access
Support for millions of documents
Distributed vector databases
Hybrid search (Vector + Keyword)
Document summarization
Knowledge Graph integration
Multi-modal document understanding
Team collaboration
Enterprise dashboard and analytics
Agentic AI workflows
Fine-tuned enterprise document assistants
Built With (Technologies)
Next.js
React.js
JavaScript
Tailwind CSS
FastAPI
Python
Google Gemini API
PaddleOCR
RAG
ChromaDB
Sentence Transformers
HuggingFace Embeddings
Semantic Search
Vector Database
REST API
Git
GitHub
Railway
Vercel

Yashank Gupta

`2026-06-25`

---

### Production-Ready E-Commerce Backend Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/productionready-ecommerce-backend-platform-38ea) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/k95578516-oss/E-Commerce-System) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> E-Commerce with Scalable Backend Architecture

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Apache Maven](https://img.shields.io/badge/Apache%20Maven-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square) ![SwaggerUI](https://img.shields.io/badge/SwaggerUI-333333?style=flat-square)

**Challenges we ran into**

Building a production-ready backend involved several engineering challenges beyond implementing standard CRUD operations.

One of the biggest challenges was implementing secure JWT-based authentication and role-based authorization using Spring Security while ensuring protected endpoints remained accessible only to authorized users.

Another challenge was maintaining transactional consistency in the order workflow. During order creation and cancellation, inventory needed to be updated accurately, and cancelled orders had to restore product stock without leaving inconsistent data.

I also implemented soft delete to preserve historical records while ensuring deleted entities were automatically excluded from API responses. Integrating audit logging required capturing important user actions transparently without affecting application performance.

During development, I encountered Swagger configuration issues where some endpoints were not visible because of an incorrect server configuration. After debugging the application configuration and validating endpoint mappings, I resolved the issue successfully.

This project significantly improved my understanding of Spring Boot architecture, REST API design, security, transaction management, Docker, and production-oriented backend development.

**The problem it solves**

# CommerceCore – Production-Ready E-Commerce Backend Platform

## The Problem It Solves

Many small and medium-sized e-commerce businesses struggle with backend systems that are secure, scalable, and maintainable. Basic CRUD applications often lack proper authentication, role-based access control, inventory management, auditing, and administrative insights, making them unsuitable for real-world deployment.

CommerceCore addresses these challenges by providing a production-inspired backend platform built with modern software engineering practices.

The platform enables secure user authentication using JWT, role-based authorization for administrators and customers, complete product and category management, shopping cart functionality, order processing, inventory updates, audit logging, and administrative analytics through a centralized dashboard.

To improve reliability and maintainability, the project also incorporates features such as soft delete, optimistic locking, Docker containerization, Swagger API documentation, pagination, search, and the Outbox Pattern for future event-driven scalability.

This project demonstrates how a modern e-commerce backend can be designed using clean architecture and enterprise development principles while remaining easy to extend with a frontend or additional microservices.

[_khushi _](https://github.com/k95578516-oss)

`2026-06-27`

---

### Agent Observability
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agent-observability-f344) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/icohangar-ops/agent-observability) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agent-observability-bay.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/VO85I2in0-o) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> AI agent observability dashboard for finance

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

AgentOps gives finance and engineering leaders a single place to understand how much AI agents cost, who is using them, and whether usage matches policy — without digging through provider invoices or raw logs.

As teams deploy more LLM-powered agents, spend becomes invisible: tokens pile up across departments, frontier models get used for routine tasks, and nobody can answer “what did we spend last month, and on what?” AgentOps fixes that by rolling up token usage × live model pricing into CFO-ready views — costs are computed, not stored, so numbers always reflect current rates.

What people use it for:

CFO / finance — org-wide spend, trends, department budgets, and tier-level rollups (Routine / Research / Frontier)
Engineering / platform — which agents, models, and employees drive the most usage
Governance — tiered model access so expensive frontier models stay reserved for high-stakes work
How it makes work easier and safer:

One dashboard instead of spreadsheets + scattered API bills
Tiered access aligns model choice with job type and budget
Datadog LLM Observability integration — live traces (latency, tokens, errors) sit next to cost data; credentials stay server-side only, read-only pull from Datadog
Budget visibility per department so overspend is caught early
Live demo: https://agent-observability-bay.vercel.app

**Challenges we ran into**

1. Deploying a long-running Express app on Vercel serverless
The app was built as a traditional Express server (app.listen()), but Vercel runs APIs as serverless functions. I split the build so app.ts bundles separately from the server entrypoint, added api/index.mjs as the Vercel handler, and used rewrites so /api/* hits the function while the React SPA serves everything else.

2. Production API returned 500 — missing DATABASE_URL
The frontend deployed fine, but every API call failed. Vercel logs showed DATABASE_URL must be set. The @workspace/db package throws at import time, so even /api/healthz crashed before handling requests. Fix: provision Neon Postgres via Vercel Marketplace (--plan free_v3, not free), push the Drizzle schema, seed sample data, and redeploy.

3. pino-pretty worker threads on serverless
The API build bundled pino-pretty with worker threads, which break in Vercel’s serverless runtime. I skipped the pino esbuild plugin when VERCEL=1 so production logging uses plain JSON instead of pretty-print workers.

4. Neon env var naming
Neon injects POSTGRES_URL and DATABASE_URL, not always the same name. I added fallbacks in lib/db so either works without manual remapping.

5. Git push to a personal mirror
Pushing to Cubiczan/agent-observability failed with 403 because macOS reused cached icohangar-ops credentials. Fix: clear credential helpers and push with an isolated inline credential helper for the Cubiczan account.

[Shyam Desigan](https://github.com/icohangar-ops)

`2026-06-27`

---

### CODESTORM
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codestorm-52cd) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://code-storm-xi.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3TKJ0suuoGI) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Create Websites That Feel Alive.

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Modern web applications often feel static, slow, and disconnected from user intent. Most websites still rely on traditional page loads and basic interactions, which limits engagement and reduces efficiency in completing tasks. Users are frequently forced to switch between multiple tools for simple workflows, and most interfaces do not adapt to user behavior or provide real-time feedback.

This project addresses these limitations by transforming static websites into dynamic, responsive, and intelligent experiences. It enables real-time interaction, smoother workflows, and more intuitive interfaces that respond instantly to user input. By integrating modern frontend techniques and optional AI-powered features, it reduces friction in everyday tasks and improves overall usability.

It can be used to build productivity tools, real-time dashboards, interactive learning platforms, browser-based utilities, and experimental web experiences where responsiveness and engagement are essential. The goal is to make web applications feel alive, adaptive, and more aligned with how users actually interact with digital systems today.

**Challenges we ran into**

One of the major challenges during development was handling real-time AI API integration securely. While integrating the Gemini API for dynamic responses, the API key was accidentally exposed in the frontend during early testing. This led to the key being flagged and blocked, which caused the application to stop working and switch to fallback mode.

To resolve this, I had to revoke the leaked API key and generate a new one. After that, I refactored the project structure to ensure proper security by moving sensitive keys into environment variables instead of hardcoding them in the frontend. I also restructured the API calls so that requests are handled more safely without exposing credentials to the client side.

Another challenge was managing inconsistent responses and fallback behavior when the API was unavailable. I solved this by implementing a fallback system that ensures the UI remains functional even when external services fail, improving overall stability.

Through this process, I learned the importance of secure API handling, proper environment configuration, and building resilient applications that can gracefully handle external failures.

Kani Jayachandran

`2026-06-28`

---

### SteadyStride
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/steadystride-a18a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deba2k5/cognexus) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> just a normal hackathon

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

did not face any problem it was easy to implement

**The problem it solves**

Agentic web scraper

[Debangshu Chatterjee](https://github.com/deba2k5)

`2026-07-11`

---

### Sales_Forecasting
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/salesforecasting-5857) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rishabhg46-bot/Sales_Forecasting_System) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/obeOqL924M4) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Transforming Sales Data into Smart Business Decisi

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Plotly](https://img.shields.io/badge/Plotly-333333?style=flat-square) ![Statsmodels](https://img.shields.io/badge/Statsmodels-333333?style=flat-square)

**Challenges we ran into**

Cleaning and preprocessing time-series sales data.
Creating effective lag and rolling features for forecasting.
Comparing and tuning multiple forecasting models (Baseline, ARIMA, XGBoost).
Detecting anomalies and selecting suitable clustering parameters.
Managing file paths, model saving, and integrating everything into a Streamlit dashboard.

**The problem it solves**

Every retail and e-commerce company — from Walmart and Amazon to D-Mart and Flipkart — lives and dies by one question: "How much of each product will we sell next month, and will we have enough stock to meet that demand?" Getting this wrong in either direction costs crores — overstock wastes storage and capital, understock loses sales and customers.
This is not a beginner classification problem. This is a multi-layered, real industry problem that requires you to work with time-series data (data ordered by date, not rows of independent customers), build and compare multiple forecasting models, detect anomalies in sales patterns, segment products by demand behavior, and deliver a working interactive dashboard that a business manager could open on Monday morning and make stocking decisions from.

[Rishabh Gupta](https://github.com/rishabhg46-bot)

`2026-07-12`

---

### SafeNet AI – Cyber Fraud Detection Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safenet-ai-intelligent-cyber-fraud-detection-and-digital-safety-platform-0eca) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Protecting Every Click with AI.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

## The Problem

Cyber fraud has become one of the fastest-growing digital threats worldwide. Every day, people receive phishing emails, scam messages, fake job offers, fraudulent shopping links, malicious QR codes, and deceptive websites. Unfortunately, many users cannot distinguish legitimate content from cyber threats, resulting in financial loss, identity theft, and compromised personal information.

Existing cybersecurity tools are often designed for technical users and require multiple applications to perform different security checks. This makes digital protection difficult for students, professionals, senior citizens, and everyday internet users.

## Our Solution

**SafeNet AI** is an AI-powered digital safety platform that helps users detect and understand online threats before they become victims.

The platform enables users to analyze suspicious emails, SMS messages, WhatsApp chats, website URLs, QR codes, and screenshots using Artificial Intelligence. Instead of simply labeling content as "safe" or "unsafe," SafeNet AI explains *why* something appears suspicious and provides practical recommendations to help users make informed decisions.

The platform also includes password strength analysis, an AI cybersecurity assistant, and an interactive cyber awareness hub that educates users about phishing, ransomware, social engineering, and other common online threats.

By combining intelligent threat detection with cybersecurity education in a single modern web application, SafeNet AI makes online safety simple, accessible, and practical for everyone.

**Challenges we ran into**

As the project evolves, one of the key challenges has been designing an architecture that balances usability with accurate AI-powered threat analysis. We are also working on integrating multiple components, such as URL analysis, screenshot processing, and AI-based explanations, into a seamless user experience. Our approach is to build the application in modular components, thoroughly test each feature individually, and then integrate them incrementally to ensure reliability and maintainability.

Team **Byte Builders** -- [Aastha Gupta](https://github.com/Aastha-Gupta-123)

`2026-07-20`

---

### Campus Connect AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-connect-ai-98d2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/medisaidulu) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> One Smart Platform for Every College Student

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

During development, we faced challenges in designing a simple and user-friendly interface while integrating multiple campus services into one platform. We also worked on organizing the application structure and planning the AI assistant integration. By dividing the work between team members, researching documentation, and testing each module step by step, we were able to overcome these challenges and improve the overall project.

**The problem it solves**

College students often use multiple apps and notice boards to check events, class schedules, placement updates, study materials, and lost & found information. This wastes time and important announcements are often missed.

Campus Connect AI solves this problem by bringing everything into one platform. Students can access notes, receive event notifications, report or search lost items, view timetables, check placement updates, and get instant answers through an AI assistant. This makes campus life easier, faster, and more organized.

Team **CodeWarriors** -- [Saidulu Medi](https://github.com/medisaidulu), [Charan Teja](https://github.com/charantejarathlavath-dotcom)

`2026-07-24`

---

### Aegisops AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegisops-ai-autonomous-multiagent-security-investigation-platform-3a15) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rigur-Calypso/aegisops-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aegisops-ai.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Autonomous Multi-Agent Security Investigation

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square)

**The problem it solves**

## The Real-World Problem

Security Operations Centers (SOCs) are in crisis. The average enterprise SOC receives **over 10,000 alerts per day**, and analysts can only investigate a fraction of them. Each investigation requires manually correlating logs across firewalls, endpoint agents, authentication systems, and network monitors — a process that takes **4-8 hours per incident**. Meanwhile, attackers complete their kill chain in under 30 minutes.

Existing AI tools make this worse, not better. They produce "black-box" conclusions with no traceability — hallucinating IP addresses, fabricating indicators of compromise, and citing evidence that doesn't exist. Analysts end up spending more time fact-checking the AI than doing actual investigation.

## What AegisOps AI Does

AegisOps AI is an **autonomous SOC copilot** that takes raw, messy security telemetry (Sysmon process logs, Suricata network alerts, authentication events) and automatically reconstructs the full attack story — end to end.

**Key differentiator: Explainable AI with zero hallucinations.** Every single AI-derived conclusion traces back to a real telemetry event ID. If the AI says "credential dumping occurred at 14:32 UTC," you can click the citation and see the exact LSASS memory access event that triggered that claim.

### How it works:
1. **Ingest & Parse** — Raw logs are normalized into a unified event schema (supports Sysmon, Suricata, auth logs)
2. **Correlate** — 4 deterministic correlation rules detect multi-stage attack patterns across event boundaries
3. **Knowledge Graph** — Events are materialized as a Neo4j graph (Host → Process → IP → User relationships), enabling structural reasoning
4. **Multi-Agent AI Pipeline** — Three specialized agents collaborate sequentially:
   - **Triage Agent** classifies severity and maps to MITRE ATT&CK tactics
   - **Investigation Agent** generates hypotheses, correlates evidence, reconstructs the attack chain
   - **Reporting Agent** produces an executive-ready incident report with narrative prose
5. **Executive Report** — Professional incident report with MITRE ATT&CK mapping, evidence citations, confidence scores, and recommended remediation actions

### Who benefits:
- **SOC Analysts** — Reduce investigation time from hours to seconds
- **Security Teams** — Get explainable AI findings they can actually trust
- **CISOs & Executives** — Receive professional incident reports ready for board-level communication
- **Small businesses** — Access enterprise-grade security investigation capabilities without a dedicated SOC team

The platform ships with 5 real-world attack scenarios (ransomware, credential dumping, SSH brute-force, PowerShell download cradles, C2 beaconing) with cinematic frame-by-frame replay, making it both a powerful investigation tool and an educational platform for security training.

**Challenges we ran into**

## 1. AI Hallucination — The Core Problem We Had to Solve

The biggest challenge was preventing the AI from hallucinating evidence. Early in development, the LLM would confidently cite event IDs that didn't exist in the telemetry data — a catastrophic failure for a security tool where trust is everything.

**How I solved it:** I built a "hallucination guardrail" into the architecture itself. The AI agents can only cite event IDs that actually exist in the replay timeline. Every `AIInvestigationResult` includes a `citations` tuple, and those citations are validated against the real `source_event_id` fields from the normalized events. Additionally, I implemented a deterministic `HeuristicLLM` fallback that uses pattern-matching instead of generative AI — so even when the LLM is unavailable or untrustworthy, the pipeline still produces accurate, evidence-backed findings.

## 2. Clean Architecture Enforcement

Maintaining strict architectural boundaries (domain layer has zero framework imports) across a fast-moving one-month hackathon was extremely difficult. It's tempting to just import FastAPI or SQLAlchemy directly in domain entities to "move fast."

**How I solved it:** I wrote AST-based architecture tests that parse the Python source files in the domain layer and assert that they contain zero imports from FastAPI, SQLAlchemy, or any infrastructure framework. These tests run on every `make test` invocation, so any violation is caught instantly. This gave me the confidence to move fast without breaking the architecture.

## 3. Multi-Agent Context Passing

Getting three independent AI agents to collaborate in a meaningful pipeline — where each agent builds on the previous agent's analysis without repeating work — was a significant design challenge. The naive approach (just concatenating outputs) produced redundant, bloated results.

**How I solved it:** I designed an `AgentContext` object that flows through the pipeline. Each agent reads prior results from the context, contributes its own analysis, and appends its `AgentResult` back. The Investigation Agent reads the Triage Agent's severity classification before generating hypotheses. The Reporting Agent reads both prior agents' outputs to produce a coherent executive summary. This accumulative context pattern ensures each agent adds unique value.

## 4. Graph RAG Integration

Connecting Neo4j's knowledge graph to the AI pipeline required careful prompt engineering. Simply dumping the raw graph data into the LLM prompt produced worse results than no graph context at all.

**How I solved it:** I built a `build_graph_context_prompt()` method that formats the attack subgraph as structured, human-readable text — listing nodes by type (Host, User, Process, IP) and relationships with their properties. This compact representation fits within context windows while preserving the structural relationships that make graph context valuable for reasoning.

## 5. Production Deployment on Free Tier

Deploying a complex stack (FastAPI + Next.js + PostgreSQL + Neo4j + Redis) to the live internet for $0 was a puzzle. Free-tier services have tight memory limits (512MB RAM), and the Docker Compose approach that works locally doesn't fit on free platforms.

**How I solved it:** I decomposed the monolithic Docker Compose deployment into a split architecture: Vercel for the Next.js frontend (with API proxy rewrites), Render for the Python backend (Docker deployment), Neon for managed PostgreSQL, Neo4j AuraDB Free for the graph database, and Upstash for serverless Redis. Each service fits within its provider's free tier, and they communicate over the public internet with proper security configurations.

Team **mima** -- Bhagyesh Kamal, Garima Narula

`2026-07-29`

---

### driver risk monitoring system
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/driver-risk-monitoring-system-2bc7) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

[meera meera](https://github.com/meerapola05-lab)

`2026-07-30`

---

### KAVACH AI-Kolkata Police Intelligence Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/kavach-aikolkata-police-intelligence-platform-bd57) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sohamghosh1762-max/kavach-ai-platform) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/11F8oCZnk0QuxtvoFMq09WJh9oYFNpq8N) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Safe City. Secure Future.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

KAVACH AI addresses several critical challenges faced by modern law enforcement agencies during criminal investigations.

**Key Problems**

1. Fragmented Police Data
Police information is distributed across multiple independent systems.
FIRs, criminal records, evidence, CCTV logs, emergency calls, and investigation notes are not centrally connected.
Officers spend significant time manually searching different databases.

2. Time-Consuming Investigations
Investigators manually collect information from multiple sources before making decisions.
Cross-referencing suspects, vehicles, phone numbers, and evidence is slow and resource-intensive.
Critical response time increases during active investigations.

3. Lack of Criminal Relationship Discovery
Traditional systems cannot automatically identify relationships between criminals.
Hidden connections involving shared vehicles, addresses, phone numbers, gangs, and repeat offenders often remain undiscovered.
Detecting organized criminal networks requires extensive manual analysis.

4. Limited Intelligence from Existing Crime Systems
Existing police software primarily acts as a record management system.
Officers receive raw records instead of actionable intelligence.
The responsibility for identifying patterns and making connections falls entirely on investigators.

5. Language Barriers During Investigations
Officers often prefer speaking in regional languages.
Most investigation systems support only text-based English queries.
This limits accessibility and slows down information retrieval.

6. Difficulty Searching Large Investigation Records
Thousands of FIRs, evidence documents, witness statements, and investigation notes cannot be efficiently searched using conventional keyword-based systems.
Similar historical cases are difficult to locate quickly.

7. No Predictive Crime Intelligence
Traditional systems focus only on historical records. They do not provide forecasts of crime hotspots, repeat offenders, or emerging crime trends.Police cannot proactively allocate patrol resources.

8. Manual FIR Analysis
Investigators manually review lengthy FIR documents. Extracting crime details, suspects, locations, evidence, and timelines consumes valuable time.
Scanned documents require additional manual processing.

9. Slow Operational Decision Making
Officers must manually gather information before deciding:
Which patrol unit should respond
Which route is safest
Which suspects are connected
Which previous cases are relevant

10. Lack of Explainable AI
Many AI systems generate answers without showing supporting evidence.
Investigators need transparent, evidence-backed recommendations that can be verified using official records.


**How KAVACH AI Solves These Problems**

**AI Investigation Assistant**
Enables investigators to query police databases using natural language.
Retrieves evidence-backed results within seconds.

**Multilingual Voice Investigation**
Supports voice-based investigation in multiple Indian languages.
Automatically detects language, translates, understands intent, and retrieves relevant records.

**Graph-Based Criminal Intelligence**
Uses Neo4j to identify hidden criminal relationships.
Discovers shared vehicles, addresses, phone numbers, gangs, and repeat offenders.

**Retrieval-Augmented Generation (RAG)**
Searches investigation documents, witness statements, forensic reports, and evidence.
Generates responses based only on retrieved police records.

**Predictive Crime Analytics**
Uses machine learning to identify:
Future crime hotspots
High-risk locations
Repeat offenders
Crime trends
Patrol deployment priorities

**AI-Assisted FIR Analysis**
Automatically processes uploaded FIRs.
Extracts structured information using OCR and AI.
Generates concise investigation summaries.

**Crime Hotspot Intelligence**
Visualizes crime density and risk levels on interactive maps.
Provides patrol recommendations and tactical insights.

**Automated Investigation Reports**
Generates professional investigation summaries, operational briefings, and case reports directly from retrieved evidence.

**Evidence-Driven AI**
Every AI-generated insight is supported by official investigation records.
Ensures transparency, explainability, and traceability throughout the investigation process.

**Challenges we ran into**

**1. Integrating Multiple Databases**
Integrating PostgreSQL, Neo4j, and RAG Vector Database into a unified investigation workflow was one of the biggest challenges.
We designed an intelligent query routing mechanism to ensure that only the required backend service is executed for each investigation query.

**2. Retrieval-First AI Architecture**
Initially, the AI generated generic responses before retrieving evidence from the databases.
We redesigned the pipeline to follow a Retrieval → Evidence Aggregation → AI Reasoning workflow, ensuring every AI response is based on retrieved records.

**3. Multilingual Voice Investigation**
Supporting voice-based investigations across multiple Indian languages introduced challenges in speech recognition, translation, and intent detection.
We implemented a structured pipeline with Speech Recognition → Language Detection → Translation → Intent Detection → Entity Extraction before database retrieval.

**4. Criminal Relationship Analysis**
Representing complex criminal relationships such as shared vehicles, phone numbers, addresses, and gang associations using traditional relational databases was difficult.
We integrated Neo4j Graph Database to model and visualize criminal networks efficiently.

**5. RAG Integration**
Building an evidence-backed Retrieval-Augmented Generation (RAG) pipeline required proper document chunking, embedding generation, semantic indexing, and similarity search.
We optimized document retrieval to ensure AI-generated summaries are grounded in retrieved investigation records.

**6. FIR Document Processing**
Extracting structured information from uploaded FIR PDFs and scanned documents was challenging.
We integrated an OCR pipeline to convert documents into searchable text before AI analysis.

**7. Predictive Crime Analytics**
Designing prediction models for crime hotspots and repeat offenders required careful feature engineering and realistic datasets.
We selected machine learning algorithms suitable for crime forecasting while keeping the architecture extensible.

**8. Real-Time Dashboard Synchronization**
Keeping dashboards, hotspot maps, alerts, and investigation status synchronized without manual refresh was a challenge.
We introduced real-time backend update mechanisms to ensure data consistency across the platform.

**9. Voice Query Understanding**
Distinguishing between different investigation intents (crime search, FIR lookup, criminal relationship analysis, prediction, report generation) from natural speech required a robust intent classification pipeline.
We improved intent detection by separating translation, entity extraction, and backend execution planning.

**10. Explainable AI**
One of the major goals was ensuring that AI recommendations remain transparent and verifiable.
We designed the system so that every AI-generated insight is traceable to retrieved evidence rather than relying solely on language model reasoning.

**Open Innovation**

**How KAVACH AI Fits the Open Innovation Track**

KAVACH AI is an AI-powered Police Intelligence and Investigation Platform that brings together multiple advanced technologies to solve one of the most challenging problems in modern law enforcement—transforming fragmented police records into actionable, evidence-backed intelligence.

**Why It Fits the Open Innovation Track**
Introduces an AI-first investigation workflow by combining natural language understanding, graph intelligence, Retrieval-Augmented Generation (RAG), machine learning, and geospatial analytics into a unified platform.
Integrates multiple disconnected police data sources including FIRs, criminal records, investigation notes, emergency calls, patrol information, and digital evidence to provide investigators with a single intelligent search experience.

Supports multilingual voice-based investigations, allowing officers to ask questions in their preferred language while the system automatically performs speech recognition, translation, intent detection, and evidence retrieval.
Uses graph intelligence (Neo4j) to uncover hidden relationships between suspects, vehicles, phone numbers, addresses, gangs, and repeat offenders that are difficult to identify through conventional databases.
Implements Retrieval-Augmented Generation (RAG) to ensure AI responses are generated from retrieved investigation records and official documents instead of relying on generic AI knowledge, improving transparency and explainability.
Provides predictive crime analytics using machine learning models to identify potential crime hotspots, repeat offenders, and emerging crime trends, supporting proactive policing and better resource allocation.
Automates FIR analysis and document intelligence through OCR and AI, reducing the time required to process investigation documents and extract critical information.
Generates explainable operational recommendations, enabling investigators to make informed decisions based on verified evidence while keeping humans responsible for all final operational actions.

Team **aNioNs** -- [ROHIT MISTRY](https://github.com/rohitmistry176-beep), [Abir Khan](https://github.com/scout6774-66667), [SOHAM GHOSH](https://github.com/sohamghosh1762-max)

`2026-07-26`

---

### ClickSafe
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/clicksafe-b781) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/The-Batman-gang/ClickSafe-Backend) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uS36Jcd3qDc) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Be Safe by ClickSafe

![MERN stack](https://img.shields.io/badge/MERN%20stack-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

### **Problem Statement: The Rise of Web Scams and Fake Job Advertisements**

In the modern digital landscape, the internet has become the primary medium for commerce, communication, and employment. However, this convenience has also led to an unprecedented rise in sophisticated cyber threats, specifically phishing websites, fraudulent services, and job scams. Job seekers and casual internet users are increasingly targeted by highly convincing copycat domains and fake employment postings. 

A particularly damaging and growing trend is **employment fraud**. Scammers set up spoofed company websites or write highly attractive, fake job listings on popular social platforms. To execute these scams, fraudsters often pose as HR professionals or recruiters, utilizing generic personal emails (like Gmail or Yahoo) while claiming affiliation with prestigious corporations. Unsuspecting applicants share sensitive personal information (such as government IDs, bank details, and home addresses) during fake hiring processes.

Traditional security measures like simple antivirus software or basic DNS blocklists are reactive and often fail to detect these dynamic threats. They lack the context-aware intelligence needed to identify:
1. Mismatches between a recruiter's email domain and the official website of the company they claim to represent.
2. "Too-good-to-be-true" compensation offers compared to standard market rates.
3. Sophisticated, freshly-registered domains that look legitimate but lack an established social or corporate footprint.

---

### **The Solution: ClickSafe (VeriWeb) Security Suite**

**ClickSafe** is an AI-powered, multi-agent trust and safety analysis backend that dynamically evaluates the legitimacy of websites and job postings in real time. Rather than relying on simple database blacklists, ClickSafe inspects security threats by combining deterministic technical scans, content extraction, and Large Language Model (LLM) reasoning.

ClickSafe resolves these challenges through two primary pipelines:

#### **1. Website Safety & Technical Audit**
When a user visits a suspicious link, ClickSafe orchestrates a parallel inspection:
*   **Technical Scanning:** Inspects SSL/TLS certificates, domain registrar data (detecting newly registered domains commonly used in short-lived scams), and hosting configurations.
*   **Reputation Mining:** Cross-references the domain against online databases and history records.
*   **Scraper-Based Content AI:** Uses Playwright to crawl the site, extracts text, and feeds it to a Gemini-powered agent to assess whether the page structure and claims resemble typical phishing or scam templates.
*   **Final Synthesis:** Combines these insights into an easy-to-read Trust Score and Risk Level (Safe, Suspicious, or Dangerous).

#### **2. Job Scam Inspection & Verification**
For career pages and job ads, ClickSafe provides a specialized micro-service pipeline:
*   **Domain Alignment Check:** Deterministically verifies recruiter identity by matching their email domain against the official company website and flagging personal webmail providers.
*   **Automated Extractor:** Extracts critical components of a job post—including salary details, requirements, and recruiter profiles.
*   **Gemini Background Verification:** Leverages Google's Gemini models to check public discussion records for fraud alerts, and verifies whether the HR professional has an established digital presence associated with the firm.

### **Key Innovations**
*   **On-Demand Processing (Toggle Feature):** By offering a client-controlled toggle, the system preserves user privacy and server resources. It only runs expensive AI analyses when explicitly requested by the user.
*   **Client HTML Forwarding:** The backend allows clients (like a Chrome extension) to pass the raw HTML they have already loaded. This eliminates redundant crawler requests, prevents anti-bot blocks on job boards, and guarantees instant response times.

**Challenges we ran into**

Challenges Faced
Dynamic Websites: Many job portals (such as LinkedIn and TCS iBegin) load content using JavaScript, making traditional HTML scraping unreliable.
Inconsistent Page Structures: Every job website uses different HTML layouts, so building a universal extractor required handling multiple selector patterns.
False Positive Extraction: Generic page content (footers, related jobs, legal notices, navigation menus) often interfered with extracting accurate skills, employment types, salaries, and company information.
Data Normalization: Similar information appeared in different formats (e.g., "Full Time", "Full-time", "FULL_TIME"), requiring normalization into a consistent schema.
Token Optimization: Raw job descriptions were often several thousand words long, so we had to intelligently reduce the content while preserving the information needed for AI analysis.
Balancing Accuracy and Performance: The system needed to extract comprehensive information without significantly increasing scan time, requiring careful optimization of scraping and parsing logic.

Team **BatMan** -- [Shaswat Pathak](https://github.com/ethyashpathak), [Aditya Shaw](https://github.com/Aditya82005), [Md Arieeb Ali](https://github.com/arieeb), [Shagun Shaw](https://github.com/ShagunShaw)

`2026-07-26`

---

### NeuroAccess
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neuroaccess-fcd3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pratham27-pro/NeuroExcess) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/5gXvd6tPtl0) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co)

> Accessibility support, one click away.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![HuggingFace](https://img.shields.io/badge/HuggingFace-333333?style=flat-square) ![Plasmo](https://img.shields.io/badge/Plasmo-333333?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-333333?style=flat-square)

**Challenges we ran into**

* Balancing automation with accuracy: Automatically fixing accessibility issues without breaking a website’s layout or functionality required careful testing.
* Generating meaningful AI image descriptions: Ensuring that AI-generated alt text was accurate and useful across a wide variety of images was a significant challenge.
* Maintaining compatibility across websites: Every website has a different structure, so making our extension work reliably on modern, dynamic web pages required handling many edge cases.
* One of the biggest challenges was implementing OCR that worked reliably across all websites. Web pages contain text in many different formats—images, scanned PDFs, icons, low-resolution graphics, and complex layouts.

**The problem it solves**

The Problem: Millions of people struggle to use websites because many are not designed with accessibility in mind. Missing image descriptions, poor contrast, difficult navigation, and hard-to-read content make everyday tasks like studying, banking, shopping, or applying for jobs frustrating or even impossible.

Our Solution: NeuroAccess is a Chrome extension that makes websites more accessible with a single click. It automatically improves readability, enhances keyboard navigation, generates AI image descriptions, provides text-to-speech and voice controls, and applies personalized accessibility profiles based on each user’s needs. Instead of users adapting to inaccessible websites, NeuroAccess adapts websites to the user.

Team **Cofi.exe** -- [Pratishtha Mehra](https://github.com/PRATISHTHA-MEHRA), [Simrat Oberoi](https://github.com/simratoberoi), [Vaibhav Chaturvedi](https://github.com/VaibhavChaturvedi03), [Pratham Jain](https://github.com/pratham27-pro)

`2026-07-25`

---

### ZeusX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zeusx-455c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pratik0144/gemma-msrit) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a6ZuQrPq4Ms?si=4wNJ3YRe6PI_3b1I) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> AI-powered cashflow intelligence platform.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

The biggest hurdle was getting the forecast to feel trustworthy rather than generic. Feeding messy, real-world SME data (irregular payment cycles, inconsistent invoice formats) into the model initially produced forecasts that were too smooth and didn't reflect actual cash flow volatility. We fixed this by tightening the data preprocessing step before it hit the model, so seasonal dips and late payments actually showed up in the risk alerts.

The second challenge was time. Building the forecast engine, the liquidity alerts, and a bank-ready report generator all in a single day meant we had to cut scope aggressively — for example, prioritizing accurate alerts over a polished UI, since judges (and real users) would care more about correct numbers than visuals.

**The problem it solves**

Indian SMEs rarely see cash shortfalls coming. Most run their finances on spreadsheets, with no forecasting and no early warning when a big customer pays late or a seasonal dip hits. By the time the problem is visible, it's already a crisis.

**Gemma SME Cashflow Copilot** fixes this by:
- Generating a **3-6 month cash forecast** from existing financial data
- Flagging **liquidity risk early**, with the specific customer/invoice names behind the risk — not just a generic warning
- Drafting **follow-up messages** to chase overdue payments
- Producing **tax notes** and a **bank-ready report**, so owners walk into a loan meeting prepared instead of scrambling

It turns raw numbers into decisions a small business owner can actually act on — days or weeks before the cash crunch hits, not after.

Team **ZeusX** -- [Pratik Potadar](https://github.com/pratik0144), siddarth takale

`2026-07-18`

---

### Drishti
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/drishti-de6d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/soumyachk101/Drishti) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://web-one-virid-58.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co)

> Drishti: See your network the way an attacker does

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![NetworkX](https://img.shields.io/badge/NetworkX-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![nmap](https://img.shields.io/badge/nmap-333333?style=flat-square)

**The problem it solves**

Security teams are drowning in vulnerability scans. A single scan returns **hundreds of CVEs sorted by CVSS score** — but CVSS rates each flaw *in isolation*. It never asks the only question that matters: **can an attacker actually reach this?**

The result is dangerous mis-prioritization:

- Teams burn hours patching a scary **"9.8"** buried three firewalls deep — unreachable from the internet.
- Meanwhile an exposed **"5.3"** on the internet-facing load balancer — the real front door — stays open.
- A real breach is almost never one bug; it's a **chain** of small hops from the edge to the crown-jewel database. Scanners score the links, never the chain.

**Drishti** fixes this by modeling your network the way an attacker actually reads it:

- **Maps the real attack path** — builds a live directed graph and traces every route from the internet to your most valuable assets (Yen's k-shortest-paths on NetworkX).
- **Prices risk in dollars** — every attack path gets a **deterministic** dollar-exposure figure a CISO can take to the board, not a vague CVSS number.
- **Drafts the fix** — one click generates a defensive Ansible/shell/CLI remediation, grounded in the real finding, reviewed by a human before it runs.
- **Proves the fix worked** — resolve a finding and total exposure **recomputes live** (e.g. $902,900 → $702,900), because the math is real, not a mock-up.

Who it's for: security analysts and blue teams who need to answer **"what do I fix first?"** — with reachability, dollars, and a ready fix, instead of a spreadsheet of thousands of CVEs.

**Defensive by design:** Drishti maps and prices risk — it never attacks. Real scanning (Nmap + NVD) is consent-gated to private networks only, and every finding is honestly reported (an unavailable check is never shown as "safe").

**Challenges we ran into**

**1. Attack-path enumeration exploded on dense graphs.**
Naively finding "every path from the internet to every asset" is a combinatorial nightmare — on a well-connected network it hangs forever. We solved it with **Yen's k-shortest-paths**, bounded hard: a max hop-length, top-K paths per target, and a global cap. This keeps the engine fast and the output focused on the paths that actually matter.

**2. Making the risk number trustworthy — and un-fakeable.**
For judges (and real users), a dollar figure is worthless if an AI could hallucinate it. We split the system cleanly: the **engine computes** every dollar figure deterministically from the graph, and the **AI only explains** it — the `/impact` endpoint overwrites the model's output with the engine's value after it returns. Same inputs always produce the same number, and `make smoke` asserts the exact live drop ($902,900 → $702,900) on every run.

**3. Keeping the AI strictly defensive.**
An AI that writes "fixes" could be coaxed into writing exploits. We prepend a hard guardrail to **every** prompt, analyze the CVE context without ever using it to justify offensive output, and treat every generated script as a review-first suggestion. An `AI_MOCK` fallback also means a flaky network never breaks a live demo.

**4. Real device scanning — without becoming an attack tool.**
We wanted to detect real vulnerabilities on a live network, not just seeded data. The hard part was doing it *ethically*. So scanning is **consent-gated**: it runs on the host by default, and on the wider subnet only after an explicit "I'm authorized" toggle; it accepts **private RFC1918 targets only and refuses public IPs**; and it uses direct Nmap on the local subnet — **never MITM or another device's traffic.** Deep Scan matches detected service versions against the **NVD** database via CPE, then feeds results into the same risk engine.

**5. The honesty problem: "unknown" is not "safe".**
Most tools show "0 vulnerabilities" for a device they never actually scanned — which is a lie. We built three distinct states end-to-end: **"not scanned"** (grey), **"0 CVEs — scanned, clean"** (green, with the note that absence of a match isn't proof of safety), and **"N CVEs found"** (red). Unscanned nodes never masquerade as clean, and empty scans create no findings.

**6. Autonomous scanning at scale.**
Manually re-scanning each device doesn't scale. We added a background scheduler that round-robins deep-scans across discovered devices on a configurable interval, with concurrency and port caps and polite rate-limiting — surfacing a live per-device vulnerability count that rolls up to each parent node.

**7. Shipping something that isn't a "works-on-my-laptop" hack.**
We kept the whole thing **typed end-to-end** (Pydantic schemas mirrored in the TypeScript client), backed by **180+ backend tests (~195 cases passing)** across the engine, AI, ingest, deep-scan, netconfig, and auth, and enforced green CI gates before every feature — then deployed it live (Railway + Vercel + real Groq).

Team **Rosomalai** -- [Soumya Chatterjee](https://github.com/soumya28022005), [Snigdha Mondal](https://github.com/Snigdha-Mondal), [Subhadip Paul](https://github.com/Subhadip-Paul2006), [Soumya Chakraborty](https://github.com/soumyachk101)

`2026-07-12`

---

### DebugMind-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/debugmindai-8c3b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nkour5308/debugmind-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://debugmind-ai.onrender.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/e5400adb55784a5490c2a47098ecc182) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co)

> AI That Teaches, Not Just Solves.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Monaco Editor](https://img.shields.io/badge/Monaco%20Editor-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square) ![Groq API](https://img.shields.io/badge/Groq%20API-333333?style=flat-square)

**Challenges we ran into**

1. Integrating the AI model and configuring the Groq API securely.
2. Designing an AI that guides users through debugging instead of immediately generating the correct code.
3. Managing the interaction between the Monaco code editor, AI backend and real-time chat interface.
4. Creating a smooth and responsive split-screen UI for code editing and AI mentoring.
5. Handling deployment issues on Render.
6. Balancing helpful AI guidance with an educational approach that encourages users to think and learn rather than copy solutions.

**The problem it solves**

Many AI coding assistants provide complete solutions, instantly encouraging developers and students to copy and paste the code without understanding the root cause of bugs limiting learning and weakening debugging skills.

DebugMind AI solves this by acting as an AI debugging mentor rather than a code generator. It analyzes the user's code, identifies potential issues, asks guiding questions and provides progressive hints instead of immediately revealing the answer. This helps users develop logical thinking, improve problem-solving abilities and become more confident programmers.

It makes debugging easier by offering step-by-step guidance, helping users understand why the error occurs and how to fix it themselves, making the learning process more effective and engaging.

Navneet Kour

`2026-06-29`

---

### API Playground
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/api-playground-34db) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Naradhrishi/devlynix-api-playground) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://api-playground-v1.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/L2PdXCOoaoM) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> Browser-based API testing -- no login.l, no setup.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square)

**Challenges we ran into**

## Challenge 1: CORS Errors
When sending requests to external APIs from the browser, 
CORS (Cross-Origin Resource Sharing) blocked many requests.

**How I solved it:** Implemented a proxy configuration in 
Vite to route requests and handled CORS errors gracefully 
in the UI with clear error messages explaining the issue 
to users.

## Challenge 2: Displaying Complex JSON
Nested JSON responses with hundreds of lines were hard to 
read in a plain textarea.

**How I solved it:** Integrated React Syntax Highlighter 
to render JSON with color coding, collapsible nodes, and 
proper indentation — making responses instantly readable.

## Challenge 3: State Management Across Components
Sharing request/response data between the request panel, 
response panel, and history sidebar became complex.

**How I solved it:** Implemented Zustand for centralized 
state management, giving all components access to a single 
source of truth without prop drilling.

**The problem it solves**

## The Problem
Every developer needs to test APIs while building projects. 
Current tools like Postman require:
- Heavy desktop installation
- Account creation and login
- Complex setup and configuration

This slows down developers during fast-paced hackathons and 
quick debugging sessions.

## The Solution
API Playground runs entirely in the browser. Open the link 
and start testing immediately. No installation. No login. 
No friction.

## Who Is It For?
- Developers testing their own APIs during development
- Hackathon participants who need quick API verification
- Students learning how REST APIs work
- Anyone who finds Postman overkill for simple tasks

## Key Benefits
- **Instant access** — just open the URL and go
- **Request history** — saved locally, no account needed
- **Request History Reload** — reloads the history request data like url, body, header etc. everything.
- **Clean UI** — distraction-free, focused on the task
- **Completely free** — no plans, no limits, no login

[Naradhrishi Kumar](https://github.com/Naradhrishi)

`2026-06-15`

---

### Racecraft AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/racecraft-ai-c612) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CzPhantom10/F1-AgenticAI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_QOfYiclPxk) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> An Agentic AI Engine for Formula 1

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square)

**Challenges we ran into**

Building Racecraft AI required solving several challenges beyond simply connecting an LLM to Formula 1 data.

### 1. Hallucinated Analysis
Early versions allowed the language model to perform calculations and rankings directly. This frequently produced confident but incorrect conclusions, especially for comparisons and race predictions.

**Solution:**  
I moved all statistical computation into dedicated analysis agents and restricted the LLM to explanation and reasoning. The model now explains results instead of generating raw calculations.

### 2. Historical Data Integration
Formula 1 data spans decades and comes from multiple sources with different structures and naming conventions.

**Solution:**  
I created a preprocessing pipeline that normalizes drivers, constructors, circuits, race results, and standings into a unified format that can be queried consistently.

### 3. Context-Aware Conversations
Follow-up questions often depended on previous queries, requiring the system to remember entities, circuits, and comparisons.

**Solution:**  
Implemented a memory layer that stores conversation context and passes relevant information to the orchestrator agent for subsequent queries.

### 4. Race Prediction Reliability
Naive prediction models simply favored championship leaders regardless of track characteristics.

**Solution:**  
Built a dedicated prediction engine that incorporates recent form, track history, constructor strength, podium frequency, average finishing position, and circuit-specific performance.

### 5. Performance Optimization
Real-time analysis across large historical datasets created noticeable latency.

**Solution:**  
Precomputed driver intelligence, constructor intelligence, and circuit intelligence datasets that can be retrieved instantly by agents during execution.

**The problem it solves**

Formula 1 data is scattered across race results, standings, historical records, and circuit statistics. While fans can access raw information, extracting meaningful insights often requires manually analyzing multiple sources and comparing large amounts of data.

Racecraft AI solves this by combining historical race intelligence, championship data, circuit-specific performance metrics, and AI-powered reasoning into a single platform.

Instead of simply displaying statistics, the system uses an agentic AI architecture where specialized agents retrieve, analyze, compare, and predict outcomes before generating natural-language explanations.

Users can:

- Compare drivers, constructors, and seasons
- Analyze performance at specific circuits
- Explore historical Formula 1 data
- Generate race predictions using historical and current season trends
- Ask follow-up questions through a conversational AI interface
- Retrieve context-aware insights instantly

The platform transforms complex motorsport datasets into actionable intelligence, making Formula 1 analysis accessible to both casual fans and data-driven enthusiasts.

[Prateek Sinha](https://github.com/CzPhantom10)

`2026-06-14`

---

### DevLynix API Studio
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/devlynix-api-studio-94d0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyanshukumar008/devlynix-api-playground) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://devlynix-api-playground.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nKWG8I8kljQ) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> CORS-free playground for testing REST APIs.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

### ⚠️ Key Hurdles & Technical Challenges

Building a serverless proxy interface within Next.js 15 presented a few critical challenges that required strict debugging:

1. **Dynamic Content-Type Crashing:** 
   * *The Problem:* Initially, the proxy router blindly assumed all destination targets would return standard `application/json` data. When hitting endpoints that returned clean HTML page matrices or raw text streams, `response.json()` failed instantly and crashed the serverless function instance.
   * *The Solution:* Implemented a validation layer that checks the incoming `content-type` header from the remote response object. It dynamically routes the data through `.json()` parsing or falls back safely to `.text()` resolution.

2. **HTTP Payload Handling Errors:**
   * *The Problem:* Passing incoming payload data bodies seamlessly inside non-GET methods (POST/PUT) often led to formatting issues where target APIs rejected the request structures as bad payloads.
   * *The Solution:* Configured a dynamic data type parsing checker inside the handler configuration block that accurately converts object elements into strings via `JSON.stringify(body)` only when necessary.

**The problem it solves**

### 🚀 The Problem It Solves

When frontend developers build web applications, testing third-party REST APIs directly from the local browser (`localhost`) almost always triggers frustrating **CORS (Cross-Origin Resource Sharing) errors**. Traditional workarounds require changing browser flags or setting up heavy local backend systems just for basic validation.

### 🛠️ How DevLynix API Studio Fixes This

DevLynix API Studio provides a lightweight **Server-Side Reverse Proxy Architecture** built on Next.js 15 Serverless Routes. 

* **Seamless CORS Bypassing:** Routes client requests through a central serverless API handler (`/api/proxy`) to make server-to-server calls, completely bypassing browser CORS restrictions.
* **Full CRUD Testing:** Enables developers to immediately test GET, POST, PUT, and DELETE workflows on live mock providers like DummyJSON and JSONPlaceholder.
* **Smart Stream Parsing:** Automatically detects network `content-type` to parse raw JSON payloads or text/html matrices dynamically without crashing the system instance.
* **Local Session Auditing:** Features an integrated request history ledger that saves previous logs in the browser's LocalStorage workspace for rapid session tracking.

[Priyanshu Kumar](https://github.com/priyanshukumar008)

`2026-06-15`

---

### EduTech twin AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edutech-twin-ai-51b7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aradhanaa28-remo/pacemate-backend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://code-vert-eight.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1201110868#t=0) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> From information to imagination

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

The Challenge: When testing our live deployment link inside the hackathon portal’s iframe and linking out to external resources, the app broke. Browser security blocked us with a wall of X-Frame-Options restrictions and Cross-Origin (CORS) errors. Because our app relies on tracking a student's live session data, the browser viewed the cross-website behavior as a security threat and completely blocked our telemetry tracking.

How We Overcame It: We quickly refactored our security headers and navigation logic:

Header Optimization: We updated our backend server's Content-Security-Policy (CSP) and adjusted X-Frame-Options to explicitly allow trusted iframe embedding.

Secure Window Isolation: We routed external links to open in a secure, isolated browser tab using target="_blank" paired with rel="noopener noreferrer".

PostMessage API: To keep our Telemetry Engine Matrix from losing track of the student's progress across windows, we implemented safe window.postMessage communication to sync state data without violating browser security protocols.

**The problem it solves**

The Problem We Solve

Today's students spend hours reading textbooks, notes, and PDFs, yet many struggle to understand and retain what they learn. Traditional learning methods often present information as plain text, making complex concepts feel boring, overwhelming, and difficult to remember.

As a result, students lose interest, rely on memorization, and forget concepts soon after exams.

PaceMate AI solves this problem by humanizing educational content. Instead of presenting information as static text, our platform transforms study materials into engaging stories, quests, and interactive learning experiences.

By adding context, emotions, characters, and challenges, PaceMate AI makes learning feel natural, memorable, and enjoyable—just like listening to a great story.

We don't just digitize education.
We humanize it.

Team **AI Avengers** -- Navina M, Nimmala Vyshnavi, Aradhanaa K, Jeevika RS

`2026-06-14`

---

### AEGIS QR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegis-qr-fa2b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/raghavgaur-pixel/Alt-F4-Project) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/6cb24lzO0Ec?si=kztB51pwxxADyXnL) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> See beyond the QR

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

QR codes have become a convenient way to access websites, make payments, download applications, and share information. However, this convenience comes with a significant security risk: users often scan QR codes without knowing where they lead. Cybercriminals increasingly use malicious QR codes to redirect victims to phishing websites, fake payment portals, malware downloads, and other harmful destinations.

Most people have no practical way to inspect a QR code before opening it. Existing QR scanners typically redirect users immediately to the destination URL, providing little or no information about potential threats. This creates an opportunity for phishing attacks, credential theft, financial fraud, and malware distribution.

AEGIS QR solves this problem by allowing users to analyze a QR code before interacting with it. Instead of simply decoding the embedded URL, the platform performs advanced security checks, including URL analysis, redirect tracking, browser-based page inspection, screenshot capture, and AI-powered threat assessment. Users receive a detailed security report that explains what the QR code does, where it redirects, what risks were detected, and how confident the system is in its assessment.

This makes QR code usage safer for individuals, businesses, educational institutions, and organizations by helping users identify potentially dangerous QR codes before they become victims of scams, phishing campaigns, or malware attacks.

**Challenges we ran into**

One of the biggest challenges was building a reliable browser-inspection engine for QR codes. Static analysis alone was not enough, since many malicious QR codes redirect users through multiple URLs before reaching their final destination. To solve this, we integrated Playwright to launch a real browser, follow redirects, inspect page content, capture screenshots, and analyze potentially dangerous behaviors such as credential-harvesting forms, hidden iframes, suspicious JavaScript, and social-engineering tactics.

A major hurdle was managing the complexity of browser automation while keeping the system stable. During development, we encountered several issues, including redirect-chain handling bugs, Playwright compatibility problems, and false positives where legitimate websites such as YouTube were incorrectly classified as suspicious. We addressed these issues by improving our detection logic, refining risk-scoring heuristics, introducing trusted-domain handling, and adding extensive debugging and testing to understand exactly why specific sites were being flagged.

Another challenge was integrating the browser-inspection results across the full stack. The backend needed to generate screenshots and detailed analysis reports, while the frontend had to display redirects, findings, screenshots, confidence scores, and recommendations in a clear and user-friendly way. This required careful coordination between the database schema, API responses, and frontend components.

Despite these obstacles, overcoming them allowed us to create a much more powerful QR security platform that goes beyond simple URL checks and provides users with a real-world view of what happens when a QR code is opened.

Team **Alt F4** -- Gouransh Pahwa, Raghav Gaur, Lavya gupta, Anurag Gaur

`2026-06-14`

---

### FlashMind
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/flashmind-f512) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://effulgent-blancmange-6e63d0.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

> Transforming topics into smart vocabulary cards

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![vs code](https://img.shields.io/badge/vs%20code-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was integrating AI APIs directly into the frontend project. While testing the application, API requests failed due to browser security and API restrictions. I learned about frontend limitations, debugging JavaScript errors, and improving project structure.

Another challenge was designing a responsive and attractive user interface using HTML, CSS, and JavaScript while keeping the project beginner-friendly and functional.

**The problem it solves**

FlashMind helps students improve vocabulary learning in a more interactive and engaging way. Traditional memorization methods can feel boring and difficult to remember. This project generates smart flashcards based on different topics like cooking, space, and cricket, helping users learn new words along with definitions and example sentences.

The project provides a clean and beginner-friendly interface where users can instantly generate vocabulary cards. It makes learning faster, easier, and more enjoyable for students and language learners.

[Hashini S](https://github.com/hashini47)

`2026-05-28`

---

### A cli agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/a-cli-agent-a27c) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

[Pritam mondal](https://github.com/pritamscodee)

`2026-05-31`

---

### Xero-Editor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/xeroeditor-6bba) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://xero-editor.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

> A multi-llm integrated platform to automate tasks

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

While creating the sound effect and meme engine we faced many hurdles like binary data to sound interpretation sometimes the code editors crashes and server issues

**The problem it solves**

It is a ai tool which help creators and video editors in many ways. For eg:- many video editors 

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/8d4552d5-3aa0-4b65-a123-3574ba38441c.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/64ee07ff-81bb-4b1b-99f8-d0556783df31.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/f490603f-14e0-4d39-8b7c-613957290249.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/303860d3-16ad-433b-a923-a7fee1d0e62e.jpeg)waste hours to find a sound effect for their video but still not found a relevant one,xero says "why don't create one yourself by just typing text". Same goes for xero meme engine 2.0 it let you create custom memes for you. More ai tools like prompt enhancer and color grader let you make your video or image more eye-catching and awesome

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/bbcd06ab-27c2-4dad-a314-5e13ddd7e32f.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/bc01243e-dbb0-41a7-82bf-d8185392f3b8.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/1df28327-7af0-4c9d-893f-eefcc5b54b8e.jpeg)

![image](https://assets.devfolio.co/content/199d983c29d745adae7563b51a7d8cab/33f54090-86e4-41a4-8af5-073f2a6e8619.jpeg)

Team **TeensAreBuilders** -- Vinayak Raghav

`2026-05-30`

---

### Eventify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eventify-33f2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Debasmita012/Eventify) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://eventify-frontend-t5k9.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/9ud4Oe7n4_8?si=sEvaYm1IxDA6a6bA) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co)

> One Platform. Every Opportunity.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![bycryptjs](https://img.shields.io/badge/bycryptjs-333333?style=flat-square)

**The problem it solves**

College event management today is fragmented. Important announcements get lost in WhatsApp groups, organizers rely on spreadsheets, and students struggle to discover opportunities beyond their immediate circles.

This results in:

* Missed opportunities for both campus events and external hackathons.
* Manual and inefficient event logistics.
* Limited visibility into student achievements, skills, and mentorship opportunities.

Eventify solves this by creating a unified, AI-powered student engagement platform.

Smart Event Discovery: Aggregates internal college events and external opportunities from platforms like Devfolio and Unstop into a personalized feed.
Secure Event Management: Digital check-ins, verified meal coupons, real-time crowd monitoring, and instant help-desk support.
Automated Achievement Tracking: Verified certificates automatically contribute to student portfolios, badges, and MAR points.
Campus Networking: Students can discover peers with similar interests, achievements, or hackathon experience, making mentorship and collaboration effortless.

Eventify transforms scattered campus activities into a connected ecosystem where students can discover, participate, achieve, and grow.

**Challenges we ran into**

Challenges Faced & Solutions
 1. CORS Redirect Issue

After deploying the frontend and backend separately, API requests failed due to CORS errors caused by trailing slashes in the API URL, which triggered unwanted redirects.

Solution: Sanitized backend URLs in the frontend configuration by automatically removing trailing slashes before making requests.
2. MongoDB Data Type Mismatch

Quiz creation requests failed because organizer IDs were sent as strings from the frontend while MongoDB stored some IDs as integers, causing query mismatches.

Solution: Implemented backend validation to handle and compare both string and integer ID formats.

3. Peer Graph Performance Optimization

Computing student similarity graphs dynamically was challenging under the memory and CPU limits of free-tier hosting.

Solution: Built a lightweight Jaccard similarity engine in Python using MongoDB aggregations, achieving fast response times without external graph databases.

 4. Asset Rendering Issues

Several design assets contained unwanted checkerboard backgrounds that appeared poorly on gradient interfaces.

Solution: Replaced them with clean assets and used CSS blend modes to ensure seamless integration with the UI.

**Web Development**

Eventify is a showcase of modern full-stack web engineering, combining high-speed user interfaces, robust database design, and real-time operations:

Modern Full-Stack Architecture: Built using a decoupled architecture with React (Vite + TailwindCSS) for a highly responsive, interactive frontend, backed by a high-performance FastAPI (Python) REST API and MongoDB Atlas for flexible document storing.
Real-Time Interactive Elements: Implements live poll voting, real-time quiz arenas, instant announcement broadcasts, and digital meal ticket verification—demonstrating real-time state synchronization between student and organizer sessions.
Advanced Web API Integrations: Integrates the Google Gemini API for an intelligent, contextual campus chatbot, exports active fests to calendar platforms via dynamically generated ICS files, and performs secure password hashing via bcrypt.
Complex Data Modeling (Opportunity Graph): Rather than just static CRUD pages, the project computes complex Jaccard similarity matrices directly in the backend routes to generate real-time social/skill recommendation graphs, proving that complex data pipelines can be run efficiently on light web stacks

Team **RealX** -- [Rishi Poddar](https://github.com/RishiP20041512), [Debasmita Banerjee](https://github.com/Debasmita012), [Adrija Roy](https://github.com/Adrijaa-06)

`2026-05-31`

---

### Adverto
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/adverto-ff30) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tahahussayn/Adverto---SynchronicityS2.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=zE1eI8ZItMY) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=zE1eI8ZItMY) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co)

> Transform Ideas into Winning Ads!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-333333?style=flat-square)

**The problem it solves**

ADVERTO - an AI system that generates, tests, and optimizes ad creatives automatically. It turns ideas into attention-grabbing ads, identifies top performers, and scales them-helping brands reduce wasted spend, improve conversions, and grow faster without manual trial and error.

**Challenges we ran into**

1.Deployment & Build Pipeline : Repeated TypeScript strict-mode failures on Netlify — the local dev server was lenient (Turbopack skips type-checking), but the Netlify production build runs tsc in strict mode, surfacing errors that were invisible locally. Required multiple fix-and-push cycles.
Incorrect netlify.toml base directory — a teammate added base = "adverto-hackathon/app" which broke the build path entirely.
Git history conflicts — needed to revert to a specific commit mid-deploy while teammates were still pushing changes. 2.TypeScript Strict Mode Errors : JSX namespace not found — JSX.Element[] broke under React 19's new JSX transform where the global JSX namespace is no longer auto-injected.
Implicit any on Supabase callbacks — onAuthStateChange parameters required explicit AuthChangeEvent and Session | null types.
Variable used before assignment — timeoutId in the typewriter component was declared without initialization, caught only by the production build.
Invalid Framer Motion Transition property — once: true was placed inside a transition object instead of viewport.
React.cloneElement prop typing — passing an index prop via cloneElement required ReactElement<any> instead of ReactElement<unknown>. 
3.Meta Ads API Integration : Sandbox account limitations — Meta's Marketing API sandbox doesn't support all endpoints available in production, making publish/creative flows hard to test end-to-end.
OAuth token management — securely passing and refreshing Meta access tokens through n8n webhooks required custom proxy handling. 
4.Real-time & Data Sync : Supabase Realtime race conditions — local optimistic skeletons (for generating creatives) had to be carefully matched against DB rows arriving via Realtime to prevent flickering or duplicate cards.
CSS-only chart overflow — pure CSS percentage-height bars overflowed their container when mock data values exceeded 100%, requiring data normalization.

**Open Innovation**

It is an innovative idea revolving around real world problems based on marketing which is the backbone of any business looking to improve their online image.

Team **Tech Titans** -- ENAAKSHI SEN, [Taha Hussain](https://github.com/tahahussayn), [Rajdeep Das](https://github.com/rajdeep-das-2007), Shreyaan Dey, Soumyakanta Mukherjee

`2026-05-31`

---

### Spike 🎯
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spike-aa09) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lloyd-c137/spike) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Autonomous multi-LLM bounty-hunting agent

![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square) ![AI](https://img.shields.io/badge/AI-333333?style=flat-square) ![CLI](https://img.shields.io/badge/CLI-333333?style=flat-square) ![Automation](https://img.shields.io/badge/Automation-333333?style=flat-square) ![security](https://img.shields.io/badge/security-333333?style=flat-square) ![Semgrep](https://img.shields.io/badge/Semgrep-333333?style=flat-square) ![bounty](https://img.shields.io/badge/bounty-333333?style=flat-square)

**The problem it solves**

Security bounties are scattered across GitHub issues, Algora, and advisory databases — finding, auditing, fixing, and claiming them is a manual process that most developers don't have time for. Spike automates this end-to-end with a multi-LLM agent that discovers, plans, audits, fixes, validates, and submits security bounties autonomously.

**Challenges we ran into**

The biggest challenge was building a truly self-contained agent with cascading LLM architecture (Claude → DeepSeek → GLM-4.1V) for resilience. Another challenge: balancing scan speed vs depth — solved with targeted CI/CD pattern matching that catches critical GitHub Actions vulnerabilities in seconds without a full Semgrep scan.

**Using LocusFounder to Build a Business!**

Spike is an autonomous multi-LLM agent that **is the business** — not just a tool that helps one. It independently generates revenue by discovering, auditing, fixing, and claiming security bounties across open-source ecosystems.

## How Spike embodies LocusFounder's vision

- **Autonomous revenue generation**: Spike finds bounties on GitHub Issues, Algora, and GHSA advisories, audits the repos, generates AI fixes, and submits PRs — end-to-end without human intervention
- **Multi-LLM orchestration**: Uses 3 cascading LLM providers (Claude Sonnet, DeepSeek, GLM-4.1V) for planning, fix generation, and validation — resilient to any single provider outage
- **Proven results**: Already generated value — 5 critical + 10 high-severity vulnerabilities found in SolFoundry (PR submitted), 800+ findings on nodejs/node
- **Agent-as-business**: Spike doesn't assist a founder — Spike IS the bounty hunter, operating autonomously 24/7 across the open-source economy

## Tech Stack
- TypeScript + Node.js (self-contained, zero system deps)
- Semgrep (1200+ security rules) + custom CI/CD pattern matching
- Anthropic Claude, DeepSeek V4, SiliconFlow GLM-4.1V for AI orchestration
- GitHub API for discovery and PR submission

## Public Repo
https://github.com/lloyd-c137/spike

anran zhao

`2026-05-12`

---

### TradeSimx
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tradesimx-5362) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Platform for No-Code Algorithmic Trade & Backtest.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

TradeSimx solves the problem of accessibility in algorithmic trading and quantitative finance. Most existing trading platforms require coding knowledge, complex setup, and expensive tools, making them difficult for students, beginners, and non-technical users.

TradeSimx provides a no-code platform where users can create, test, and analyze trading strategies using a simple visual interface and historical market data. Users can build strategies with indicators like RSI, MACD, Moving Averages, and Bollinger Bands without writing code.

The platform makes trading strategy development easier, safer, and more accessible by enabling:

* Risk-free backtesting on historical data
* Automated performance analysis
* Interactive visualizations and reports
* Faster strategy experimentation without manual coding

TradeSimx helps bridge the gap between theoretical financial learning and practical real-world implementation while promoting financial literacy and data-driven decision-making.

**Challenges we ran into**

* Building an accurate backtesting engine for real-world trading simulation was challenging due to large historical datasets and trade execution logic. We optimized data handling and debugging to improve accuracy and performance.

* Converting no-code user inputs and chatbot instructions into executable trading strategies was complex. We solved this by developing a modular strategy parser.

* Financial data from APIs sometimes contained missing or inconsistent values. We implemented preprocessing techniques like cleaning, validation, and normalization to ensure reliable results.

* Integrating analytics, visualization, and automated report generation while maintaining system performance required careful modular architecture design and component separation.

**Using LocusFounder to Build a Business!**

TradeSimx fits perfectly into the FinTech and AI/ML track by making quantitative finance and algorithmic trading more accessible through automation and intelligent strategy testing.

Our platform allows users to create, backtest, and analyze trading strategies using a no-code interface powered by technical indicators, historical market data, and automated performance analytics. By combining AI-assisted strategy generation, financial data processing, and visualization, TradeSimx helps students, researchers, and beginner traders explore algorithmic trading without requiring programming expertise.

The project promotes financial literacy, risk-free experimentation, and data-driven decision-making while leveraging modern FinTech and AI technologies to simplify quantitative finance.

Team **Code Crusaders** -- [Sharath K M](https://github.com/SHARATHKM2004), [LubnaKausar Halageri](https://github.com/LUBNAKAUSAR2006)

`2026-05-17`

---

### Student Skill Matching Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/student-skill-matching-platform-9e67) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Connect students with opportunities through skills

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Many students struggle to find opportunities, teammates, internships, and projects that match their actual skills and interests. Existing platforms often focus only on resumes or academic scores, making it difficult for students to showcase practical abilities.

The Student Skill Matching Platform helps students create profiles based on their skills, technologies, and interests. The platform can connect students with suitable teammates, project collaborations, learning communities, and opportunities based on skill compatibility.

This makes networking, collaboration, and discovering opportunities easier and more accessible for students.

**Challenges we ran into**

One of the main challenges was designing a system that could effectively match students based on different skills and interests. Managing user data and ensuring proper filtering and matching logic was initially difficult.

I also faced challenges while working on the frontend-backend integration and handling form data correctly. Debugging API connections and fixing data flow issues took time, but I overcame them by testing components step by step and improving the project structure.

Through this project, I improved my problem-solving skills, debugging techniques, and understanding of full stack development.

**Using LocusFounder to Build a Business!**

• AI
• Community Building
• Student Innovation
• Web Development

Sreeja sreeja

`2026-05-14`

---

### Scrolltale
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scrolltale-6111) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/robin11110000/scrolltale) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/-vbiiN3GPPI) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> comics, unchained.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Webtoon's creator economy is broken — artists are paid flat rates regardless of panels produced, expected to churn out **40–60 panels every single week**, and have zero visibility into how platform revenue translates to their paycheck. With **64% of Webtoon's readership under 24** and the romance genre alone valued at **$1.8 billion**, the platform is clearly printing money while creators report being ghosted on contracts, stripped of creative control, and burned out. I've seen this firsthand — I know creators who've lived this cycle and are already backing Scrolltale as the platform they actually want to exist.

Scrolltale puts transparent on-chain payouts at the center of the creator relationship, so there's no more guessing where the money went. Readers unlock episodes using coins and those episodes are theirs permanently **as on-chain assets** — not locked to a platform that can revoke access tomorrow. Creators get a **real-time payout** dashboard with **verifiable transaction hashes** instead of a flat rate and a prayer. It's a decentralized publishing layer built for the readers who scroll past midnight and the indie artists who are done compromising their art for an algorithm.

**Challenges we ran into**

The most concrete technical blocker was payment infrastructure — Stripe checkout isn't available in my country, so building out the real coin purchase flow required working around that limitation for now. On the product side, convincing artists to migrate away from a platform they already have an audience on is a harder sell than it looks; the creator acquisition problem is as much about trust and network effects as it is about having a better product. Expanding the right connections — artists, Web3 communities, webtoon readers — is something I'm actively working on but takes time to build authentically. The UI is in a good place but still needs polish and a more distinctive visual identity to truly stand out in a space where aesthetic is everything to the audience.

**Using LocusFounder to Build a Business!**

Scrolltale was built end-to-end using Locus Founder as an AI cofounder — starting from a raw idea ("decentralized webtoon platform with on-chain payouts") and letting it drive the business and technical architecture from the ground up. The full-stack structure — React + Vite frontend, Express backend, Postgres waitlist persistence, and a multi-stage Docker deployment — was scaffolded and iterated on through Locus, cutting down what would have been weeks of solo founder work into a focused hackathon build.

[Robin Scherbatsky](https://github.com/robin11110000)

`2026-05-26`

---

### Pipeo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pipeo-3cf1) [![Built at](https://img.shields.io/badge/Built%20at-ETHPrague%202026-0052CC?style=flat-square)](https://ethprague2026.devfolio.co)

> Channels that never sleep

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Swarm](https://img.shields.io/badge/Swarm-333333?style=flat-square)

**The problem it solves**

Enable users and their agents to talk to each other via Swarm network. Imagine like Reddit style posts and replies to them. Each user ("participant") is creating their own feed and the "aggregator" is composing them to a single data structure. Messages are sent to a different channels/topics.

Team **Pipeo** -- [Ondřej Raška](github.com/ondratra), [Agoston Szoke](https://github.com/agoston0x), [Dawid Szlachta](https://github.com/dszlachta)

`2026-05-10`

---

### MalSight
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/malsight-9414) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/samiranpal2004/Malsight) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MaFDlbgeMFQ) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co)

> Not Just Detection — Investigation

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Google Gemini 2.5 Flash](https://img.shields.io/badge/Google%20Gemini%202.5%20Flash-333333?style=flat-square)

**The problem it solves**

### The Malware Detection Problem

**Traditional antivirus is failing.** Signature-based detection is useless against zero-day malware, AI-generated polymorphic threats, and packed/obfuscated payloads that mutate on every deployment. 91% of cyberattacks start with a phishing email, and most companies — especially SMBs — have no dedicated malware analyst to investigate suspicious files.

### What MalSight Does

MalSight is an **AI-powered malware analysis platform** where a Gemini 2.5 Flash agent acts as a senior security researcher. Instead of matching signatures, it *thinks* — forming hypotheses, calling analysis tools strategically, reasoning about results, and adapting its investigation based on what it finds.

**Three ways people use it:**

1. **Upload a suspicious file** — drag-and-drop any `.exe`, `.dll`, `.pdf`, `.py`, `.sh`, or `.zip`. Within 60 seconds, get a full threat report in plain English with MITRE ATT&CK technique mapping, IOC extraction, and a confidence-scored verdict.

2. **Connect your Gmail** — MalSight automatically scans every email attachment that arrives. Malicious files are quarantined and labeled before you ever open them. Zero configuration, zero human action required.

3. **Send via SMTP** — organizations route their mail server through MalSight's SMTP gateway. Attachments are held, analyzed in a GKE gVisor sandbox, and only delivered if clean.

### What makes it different from existing tools

- **Explainable verdicts** — not just "malicious" but *why*. The full agent reasoning chain is visible: every tool call, every conclusion, every decision. Analysts can audit exactly how the verdict was reached.
- **Adaptive investigation** — a fixed pipeline runs the same steps on every file. MalSight's agent adapts: a known-hash file resolves in 3 seconds with 1 tool call; an unknown packed binary gets a full 10-step investigation with sandbox execution, memory forensics, and IOC enrichment.
- **Real-time reasoning stream** — watch the agent think live via Server-Sent Events. AGENT_THOUGHT, TOOL_CALL, TOOL_RESULT events stream to the browser as the investigation happens.
- **Memory forensics** — packed malware hides its real payload in memory. MalSight dumps process memory at runtime, scans for injected PEs, extracts decrypted strings, and detects shellcode patterns invisible on disk.
- **Gmail integration** — connect any Gmail account with one click. Attachments are scanned automatically, emails are labeled (MALSIGHT_CLEAN / MALSIGHT_MALICIOUS), and threats are moved to a quarantine folder.

**Challenges we ran into**

### 1. Cross-process SSE streaming
The RQ worker (running the Gemini agent) and the FastAPI server (serving the SSE endpoint) are separate processes — they don't share memory. Our initial `STREAM_EVENTS` in-memory dict was always empty on the API side. **Fix:** switched to Redis as a shared event bus. Agent emits events to a Redis list, SSE endpoint reads from it with 300ms polling.

### 2. GKE sandbox can't execute Windows PE binaries
Our sandbox runs on Linux with gVisor. When we submitted a real `.exe`, it failed with `ENOEXEC (Exec format error)` — Linux can't natively execute PE32 binaries. **Fix:** added smart file-type detection in the sandbox command. Windows PEs get static string analysis inside the container; Python/shell scripts get full strace execution. The agent's system prompt was updated to understand this limitation and pivot to static analysis tools for PE files.

### 3. Gemini FunctionResponse requires dict, not list
`get_pe_sections()` returns a list of section objects, but the Gemini SDK's `FunctionResponse` only accepts dicts. Every call to this tool crashed the agent loop with a Pydantic validation error. **Fix:** wrapped all non-dict tool results in `{"items": result, "count": len(result)}` before passing to `FunctionResponse`.

### 4. MalwareBazaar false positives
The `check_malwarebazaar()` function was returning `found: True` for every file because it wasn't checking for API error responses. The API returned `{"error": "Unauthorized"}` (missing auth header), and our parser treated any non-"hash_not_found" response as a hit. **Fix:** added explicit error key checking + the correct `Auth-Key` header (not `API-KEY` — the docs were misleading).

### 5. PostgreSQL generated column conflict
Dev 1's database schema had `elapsed_seconds` as a PostgreSQL generated column (auto-computed from timestamps). Our `UPDATE` statements tried to write to it directly, crashing every job. **Fix:** removed `elapsed_seconds` from all UPDATE queries and let the DB compute it.

### 6. Redis tunnel vs environment variables
GCP Memorystore Redis is VPC-internal — unreachable from a dev laptop. We SSH-tunnel through a GKE node to `127.0.0.1:6379`, but the `.env` file had the direct Memorystore IP. Worse, stale shell environment variables silently overrode `.env` values. **Fix:** used `load_dotenv(override=True)` everywhere, and added `unset REDIS_URL DATABASE_URL` to the startup checklist.

### 7. MalwareBazaar ZIP extraction
Downloaded malware samples use compression level 5.1 which standard `unzip` can't handle. Extracting real samples for testing required `7zip` — a small but frustrating blocker during rapid iteration.

Team **Rossogolla** -- [Tiasha Biswas](https://github.com/Tiasha08), [Piyush Paul](https://github.com/Piyush800x), [Samiran Pal](https://github.com/samiranpal2004), [Sudipta Ghorami](https://github.com/Sudipta57)

`2026-05-09`

---

### CodeRescue
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-agent-0d47) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sumit989bishnoi-crypto/ai-frontend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sumit989bishnoi-crypto.github.io/ai-frontend/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/rLoX1jGxs8g) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co)

> AI Debugger

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Before CodeRescue	With CodeRescue
Copy error → open StackOverflow → search → read multiple threads → try solutions	Paste code → get fix in seconds
Manually compare buggy vs fixed code	Side-by-side explanation with corrected code
Wonder if the fix is reliable	Confidence score tells you how certain the AI is (high/medium/low)
Switch between IDE and browser constantly	Single web interface, works on any device
Makes Code Safer By
Catching null pointer exceptions before they crash production

Identifying off-by-one errors that cause silent data corruption

Spotting memory leaks (C++) that degrade performance over time

Fixing async/await mistakes (JavaScript) that lead to race conditions

Flagging truncated code when input exceeds 1500 characters, preventing incomplete analysis

Key Differentiators
Auto language detection — No dropdown menus, just paste and go

Human-readable explanations — Describes bugs like you're explaining to a non-coder

Copy-to-clipboard — Fixed code is one click away from your IDE

No account required — Completely free and open access

Model choice — Switch between Gemma 3 12B (faster) and 27B (more accurate) based on your needs

Challenges I ran into
Challenge 1: Gemini API Returning Inconsistent JSON Formats
The Problem:
The Gemini API kept wrapping JSON responses in markdown code blocks (```json ... ```) or adding explanatory text before/after the JSON object. This broke the JSON parser completely, causing the app to fail silently.

How I Fixed It:
I implemented a multi-strategy JSON extraction system with 4 fallback layers:

python
def extract_json(raw: str) -> dict | None:
    # Strategy 1: Direct parse
    # Strategy 2: Strip markdown code blocks with regex
    # Strategy 3: Regex extract JSON object pattern
    # Strategy 4: Bracket-matching to find complete JSON block
This brute-force approach ensures that even if the AI misbehaves, the system still extracts valid JSON. I also set temperature=0 and top_k=1 to make the model as deterministic as possible.

 Challenge 2: Handling Multiple AI Models Gracefully
The Problem:
When I added model switching between Gemma 3 12B and 27B, some models would fail to load while others succeeded. The app needed to handle partial model availability without crashing.

How I Fixed It:
I wrapped each model initialization in individual try-catch blocks and stored available models in a dictionary:

python
models = {}
for model_key, model_name in AVAILABLE_MODELS.items():
    try:
        models[model_key] = genai.GenerativeModel(model_name)
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
The API now dynamically falls back to any available model if the requested one isn't loaded, and the frontend shows only working models.

🏃 Challenge 3: Rate Limiting Without Blocking Legitimate Users
The Problem:
Without rate limiting, a single user could spam the API and exhaust quota. But overly aggressive limits would hurt the user experience.

How I Fixed It:
I implemented a 2-second cooldown per IP using an in-memory dictionary with timestamps. The 429 Too Many Requests response still returns a 200-like JSON body so the frontend can display a friendly message instead of crashing:

python
def is_rate_limited(ip: str) -> bool:
    now = time()
    if ip in _last_request and now - _last_request[ip] < 2:
        return True
    _last_request[ip] = now
    return False
🌐 Challenge 4: CORS Issues Between GitHub Pages and Hugging Face
The Problem:
The frontend on GitHub Pages and backend on Hugging Face Spaces have different origins, causing CORS (Cross-Origin Resource Sharing) errors. Browsers blocked all API calls.

How I Fixed It:
I configured Flask-CORS to only allow the specific GitHub Pages domain, not wildcard origins:

python
allowed_origins = os.getenv("ALLOWED_ORIGINS", "https://sumit989bishnoi-crypto.github.io")
CORS(app, origins=allowed_origins.split(","))
On the frontend, I detect whether the app is running on GitHub Pages and dynamically switch between

**The problem it solves**

Instant Code Debugging Without Context Switching
Developers waste 30-50% of their debugging time just identifying what's wrong with broken code. CodeRescue eliminates this by providing instant, AI-powered code analysis and fixes without leaving the browser.

 What People Can Use It For
Students learning to code — When error messages are confusing, CodeRescue explains bugs in plain English and shows the corrected code side-by-side

Junior developers — Get instant feedback on syntax errors, logic bugs, and anti-patterns before submitting code reviews

Interview preparation — Paste broken code examples and understand why they fail, learning debugging patterns

Quick code reviews — Rapidly validate small code snippets for common issues without setting up a full development environment

Cross-language debugging — CodeRescue auto-detects programming languages (Python, JavaScript, Java, C++, and more), so you don't need to specify what language you're working in

[sumit kumar](https://github.com/sumit989bishnoi-crypto)

`2026-05-05`

---

### CostHunter
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/costhunter-f851) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/immansha/aideas-cost-hunter) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](http://cost-hunter-models-359289023438.s3-website-us-east-1.amazonaws.com/dashboard.html) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=s7dKyvWoJeE&t=16s) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> RL-Powered AWS Cost Optimizer

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Amazon Web Services (AWS)](https://img.shields.io/badge/Amazon%20Web%20Services%20(AWS)-333333?style=flat-square) ![DynamoDB](https://img.shields.io/badge/DynamoDB-333333?style=flat-square)

**The problem it solves**

Most teams don’t realize they’re wasting cloud money until the bill arrives by then, the damage is already done.

Tools exist, but they’re passive: dashboards, alerts, spreadsheets. They require engineers to remember to check them. In reality, they don’t.

CostHunter flips this model.

Instead of humans looking for waste, an RL agent continuously scans infrastructure, identifies inefficiencies, and brings actionable recommendations directly into the developer workflow.

What people can actually do with it:

Detect idle or underutilized EC2 instances in real time, not weeks later
Get context-aware recommendations (not just metrics, but reasoning)
Approve/reject actions inside their IDE  no dashboard hopping
Continuously improve decisions via human feedback → RL retraining loop

This makes cloud cost optimization:

Proactive instead of reactive
Integrated instead of fragmented
Learning instead of static

The result is simple:
→ less wasted spend
→ faster decisions
→ zero context switching

And critically  a system that gets smarter every time it’s used, instead of stale the moment it’s deployed.

**Challenges we ran into**

The hardest problems weren’t in the model  they were in making the system actually work in the real world.

1. RL model breaking on real AWS data

The agent trained cleanly on synthetic data. The moment I connected it to live EC2 scans, everything broke  feature dimensions didn’t match, distributions were skewed, and the policy collapsed.

Fix:
I introduced a strict data contract between the scanner and the RL environment:

standardized feature schema
normalization pipeline aligned with training
fallback handling for missing/edge-case metrics

This turned “works in notebook” into “works in production.”

2. DQN instability under real-world drift

Initially tested DQN  it performed well early, then diverged around ~30K timesteps when cost patterns shifted.

Fix:
Switched to PPO with a clipped surrogate objective, which stabilized updates under non-stationary reward distributions.

This wasn’t just a model swap it changed how I think about RL:

algorithm choice = assumption about environment stability

3. Deploying ML inside AWS Lambda

This was unexpectedly painful:

PyTorch exceeded Lambda’s 250MB limit
Windows/Linux binary mismatches broke deployments
Cold starts were too slow for real-time use

Fix:

Used Lambda Layers with manylinux2014_x86_64 builds
Stripped unnecessary dependencies
Optimized packaging to stay within limits
4. Designing a reliable feedback loop

Initially, feedback (approve/reject) was passed directly between services → brittle and hard to scale.

Fix:
Moved to DynamoDB as the source of truth:

all actions logged centrally
retraining triggered asynchronously
components decoupled and retry-safe

This made the system scalable from a few resources to thousands without redesign.

5. Trust vs automation tradeoff

I started with a fully autonomous system. It failed the moment I thought about real production risk.

Fix:
Introduced human-in-the-loop as a core design principle, not a fallback:

every action requires approval
feedback becomes training signal
trust compounds over time
Big takeaway

The hardest part wasn’t building an RL agent.

It was building a system that:

survives real data
handles shifting environments
and earns enough trust to actually be used

That’s where most “AI projects” fail  and where this one became real.

[mansha singh](https://github.com/immansha)

`2026-04-26`

---

### Neural Nodes – AI Deployment with Locus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neural-nodes-ai-infrastructure-deployment-with-locus-checkout-79fd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ankittrip/NeuralNodes---AI-Infrastructure-as-Chat) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/uiY4oci79aw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uiY4oci79aw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Instant AI-powered deployment for any GitHub repo

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Webhook](https://img.shields.io/badge/Webhook-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Deploying applications from GitHub is still a complex, manual, and time-consuming process. Developers need to understand infrastructure, configure environments, handle scaling, and manage deployments separately.

More importantly, infrastructure today is not easily monetized in real-time, especially for the emerging agent economy where AI systems need to autonomously purchase and execute tasks.

Neural Nodes solves this by turning infrastructure deployment into an instant, on-demand, and monetized service.

Users (and even AI agents) can simply provide a GitHub repository, and the system automatically:
- Analyzes the project structure
- Detects architecture (frontend, backend, fullstack)
- Calculates infrastructure cost dynamically
- Enables payment via Locus Checkout (USDC)

Once payment is confirmed, deployment is triggered automatically, and a live URL is generated.

This removes complexity, reduces friction, and enables programmable infrastructure powered by real-time payments.

This system supports both human users and AI agents, aligning directly with the agent economy vision enabled by Locus.

**Challenges we ran into**

One of the biggest challenges was ensuring reliable and accurate system behavior while working with AI-based analysis.

Initially, relying fully on AI for architecture detection led to inconsistent results. To solve this, I implemented a deterministic override system that ensures correct classification (frontend, backend, fullstack) regardless of AI ambiguity.

Another major challenge was integrating Locus Checkout in a way that works without a sandbox environment. Since real payments were not feasible for testing, I built a controlled "simulation flow" that mimics webhook-triggered deployment while keeping the backend fully compatible with real payment events.

Handling real-time deployment feedback was also challenging. To improve user experience, I implemented a staged status flow (Awaiting Payment → Payment Confirmed → Deploying → Live), making the system feel production-ready and transparent.

Additionally, ensuring smooth communication between frontend, backend, and webhook events required careful handling of asynchronous flows and error states.

Team **Neural Nodes** -- Ankit Tripathi, Yashasvi Gupta

`2026-04-30`

---

### TollBooth - The Paywall for AI Agents
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tollbooth-the-paywall-for-ai-agents-4314) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tonyromero15-1/Tollbooth-locus-https://github.com/tonyromero15-1/Tollbooth-locus-) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tollbooth-locus.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/91653f5b621f4df293d415a0214336bc) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Payment infrastructure enabling autonomously

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

AI agents can't access premium APIs because they lack payment infrastructure. Traditional paywalls require human credit cards and authentication. TollBooth implements HTTP 402 protocol with Locus USDC payments, enabling agents to autonomously discover, pay for, and access APIs with zero human interaction - unlocking the agent economy.

**Challenges we ran into**

1. Implementing programmatic USDC payments without human wallet signing
2. Building machine-readable discovery via agent.json manifest
3. Handling session management across 402 redirects and payment confirmations
4. Ensuring sub-15 second payment settlement for real-time agent workflows
5. Creating responsive UI that works across mobile and desktop

**Track: Checkout with Locus**

TollBooth is built entirely around the Locus Checkout SDK. Every API call payment flows through Locus:

1. API providers set USDC prices per call
2. When agents/users access paywalled endpoints, TollBooth creates Locus checkout sessions programmatically
3. Payments settle in USDC on Base blockchain via Locus
4. Providers receive funds directly to their wallets through Locus settlement

Core Locus Integration:
- Uses Locus Checkout SDK for session creation
- Programmatic USDC payments via Locus API
- Real-time payment validation through Locus webhooks
- Base blockchain settlement powered by Locus infrastructure

TollBooth demonstrates Locus's value proposition for machine-to-machine micropayments - enabling autonomous agents to pay for API access without human intervention. The entire payment infrastructure is Locus-powered, making it impossible to build this project without CheckoutWithLocus.

Every transaction = Locus checkout. Every settlement = Locus on Base. TollBooth IS a Locus application.

Tony Romero

`2026-04-30`

---

### H-A-Qmarg
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/haqmarg-f5d9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shamsinghbhavi19/H-A-QMarg) [![Built at](https://img.shields.io/badge/Built%20at-Hack&Chill3.0-0052CC?style=flat-square)](https://hackandchill--3.devfolio.co)

> **H-A-Q Marg** is a web platform designed to help

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square)

**The problem it solves**

****H-A-QMarg****

A web platform that is dealing with the gap found in legal family welfare cases in teir - 3 and teir-2 cities. This platform provides a way to educate the women in rural background regarding family welfare cases. Women can get to know their rights, ask any family welfare case from AI chatbot and even genrate petition.

**Challenges we ran into**

The major challange was the data collection regarding the family welfare cases. The next chalaange was a AI chatbot instead of using condidtional statement we have used LLM .

Team **Team_TechTalk** -- Arpita Tayal, SHAMBHAVI SINGH

`2026-04-28`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
