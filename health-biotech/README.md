# Health and Biotech

![Projects](https://img.shields.io/badge/Projects-62-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### Nirodh: Drug Sentinel
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nirodh-drug-sentinel-eb89) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/siddhu2606/nirodh-drug-sentinel) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GAt8_FRv9K4) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-23-FF6B6B?style=flat-square)

> "See something. Report it. Stop it."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

![image](https://assets.devfolio.co/content/6d0d505ad2e04b8282cc4d561de5d537/0d1a7064-8f79-4aa7-bed7-64a219f6d0bb.jpeg)Community drug-crime reporting is fundamentally fragmented. Law enforcement currently relies on delayed word-of-mouth or unstructured phone calls, leaving officers without verifiable evidence or live situational awareness before arriving on scene. Meanwhile, narcotics tip lines are frequently overwhelmed by duplicate, low-quality, or malicious reports.

Nirodh: Drug Sentinel bridges the gap between citizens and law enforcement through a unified, intelligence-driven pipeline:
For Citizens: A friction-free, zero-login dashboard allowing anyone to submit geo-tagged photo or video evidence with descriptions in under a minute.
For Law Enforcement: A secure command console that automatically triages incoming intelligence using a two-tier verification engine (SHA-256 cryptographic hashing to drop exact duplicates + Gemini AI plausibility checks to filter spam).
Predictive & Field Surveillance: District-level heatmaps transform individual tips into actionable pattern-of-life intelligence, while an ad-hoc mobile camera feature converts any authorized officer's phone into a live surveillance node with real-time facial detection.

**Challenges we ran into**

Filtering Spam without Human Bottlenecks: Allowing instant anonymous media uploads created a high risk of platform abuse. Processing every submission manually would paralyze enforcement units.
Solution: We built a hybrid verification pipeline combining deterministic SHA-256 image hashing for fast, low-cost duplicate detection with an asynchronous Gemini AI pass to evaluate image-text plausibility before routing tips to an officer’s queue.
Mobile WebRTC & HTTPS Enforcement: Converting officer smartphones into real-time CCTV nodes required browser getUserMedia camera permissions, which strictly enforce secure HTTPS protocols and fail on standard local IP testing.
Solution: We routed our local environment through Cloudflare Tunnels to generate valid HTTPS endpoints for real-device field testing.
Cross-Origin Next.js Build Failures: Tunneling external traffic into the local Next.js development server triggered cross-origin resource sharing (CORS) blocks, severing Hot Module Replacement (HMR) WebSockets and breaking JavaScript chunk loading.
Solution: We updated server configuration settings to explicitly handle custom domain headers and allowed origin hosts, restoring real-time development sync across mobile test devices.

**Anti Narcotics**

Nirodh: Drug Sentinel directly targets the Anti-Narcotics track by digitizing the complete enforcement lifecycle—Spot, Verify, Analyze, and Respond—into a single operational platform:
Community-Sourced Intelligence: Empowers citizens to report street-level peddling, suspicious drops, and localized trade anonymously and instantly.
Automated Lead Verification: Utilizes cryptographic deduplication and AI authenticity scoring to isolate legitimate anti-narcotics leads from background noise.
District Hotspot Analytics: Converts scattered incident reports into predictive spatial heatmaps, shifting police strategy from reactive patrolling to proactive intercept operations.
Rapid Ad-Hoc Surveillance: Eliminates reliance on fixed infrastructure by enabling officers to deploy instant smartphone CCTV nodes with facial matching in unmonitored alleys or suspected dealing spots.
Secure Tactical Dispatch: Restricts sensitive field data behind badge/KYC authentication while enabling encrypted inter-unit alert broadcasts for rapid, coordinated field dispatches.

Team **V/Slash** -- Vidula Jangam, SIDDHESH MANDLIK, Isha Halbe, Samarth Jadhav

`2026-08-16`

---

### Lads AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lads-ai-e9ab) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vrajdesai78/lads-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai.joinlads.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/AXQKTuiNTvw) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Your health shopping companion

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Zod](https://img.shields.io/badge/Zod-333333?style=flat-square) ![Hono](https://img.shields.io/badge/Hono-333333?style=flat-square) ![neon](https://img.shields.io/badge/neon-333333?style=flat-square) ![Drizzle ORM](https://img.shields.io/badge/Drizzle%20ORM-333333?style=flat-square) ![XState](https://img.shields.io/badge/XState-333333?style=flat-square)

**Challenges we ran into**

## One of the hardest parts was making the trust data reliable.

At first, we tried using the Trustified search API. During testing, it sometimes returned errors like MetaSiteId not found, so we could not depend on only that API. We fixed this by adding another path: the system now checks Trustified’s public sitemap, finds pass/fail product pages, and parses the actual page content. That gave us more useful details like test status, batch number, amino spiking result, melamine result, and report links.

Another challenge was deciding when not to give an answer. Live sources are messy. Amazon can block requests, X can show a login wall, and Reddit results can be noisy. We did not want the agent to make up confidence when the data was weak. So we made the live research path stricter: if there is no merchant offer, no trust evidence, or no independent user evidence, the system blocks the result instead of pretending it has enough proof.

The third hard part was keeping checkout safe. We had to make sure card details, Prava credentials, and full addresses never enter prompts, logs, or normal API responses. We added redaction around the browser checkout path and kept Prava credentials only at the final checkout boundary.

So the main challenge was not just collecting data. It was making sure the agent only answers when it has enough evidence, and that buying through it stays safe.

**The problem it solves**

## Problem
We are a group of friends living in different cities who push each other to stay active. We take supplements and protein regularly, and we have always been finding the right brand, quality and cost, trying to find what works for us. The problem is that this market runs on paid ads and hidden ingredients, so it is hard to know what we are actually consuming or whether we are overpaying. We have hit this wall ourselves and so have most of our friends. We want to solve it for anyone stuck with the same question: what's the right product, and where's it cheapest?

## How my product solves it
The agent works like a simple iMessage chat. You paste an Instagram reel and it identifies the product, pulls honest reviews from real users across the internet, and gives it a Trustified score backed by lab reports. Then it finds the cheapest price for that product across different stores and lets you check out seamlessly through Prava. It helps you get the right product at best price.

## Why is it useful today
Today's youth is more health conscious than ever. Some get swayed away by trainer's suggestion or end up with manual research. We have watched teenagers at our gyms and clubs get stuck in exactly this loop. This agent gives them real facts and the best available price, with no commissions. We tested it with our own gym friends and they loved it.

## What I plan to build next
We are building personalized health coach with a matching engine for group activities, and this agent will live inside the same app. The idea is to add trust layer on top of social layer, and push the whole health ecosystem toward something fair and value driven. We plan to add subscription model to provide these features and fund our operations.

**Best Visa Intelligent Commerce Implementation**

## LADS fits this track because payment approval is built into the shopping flow.

The agent helps the user choose a health product, compares prices, and prepares a live merchant quote. Once the user confirms the exact product and price, payment moves to Prava for secure approval.

Card details, CVV, OTPs, and payment credentials never sit inside the agent chat or iMessage. LADS only continues checkout after the user approves the payment.

**Most Startup-Ready Product**

## LADS is startup-ready because it builds on joinlads.com, which is already used by 250+ people daily to get healthier and stay active.

These users already ask about protein powders, supplements, and what is worth buying. LADS AI adds a trust layer to that journey by checking lab signals, real reviews, alternatives, and prices.

We started with a focused category: protein powders and supplements. This gives us a clear path to add it inside the LADS app, then grow through subscriptions and commerce.

**OpenAI**

## LADS uses the OpenAI API to understand the user’s message, identify the product, ask follow-up questions, and guide the shopping flow inside iMessage.

We also use OpenAI to help search and summarise evidence from Reddit, Amazon, Trustified, X, and Senso.

The final score is not guessed by the model. We use deterministic scoring for nutrition, lab signals, reviews, seller trust, and price, while OpenAI helps explain the result clearly.

**iMessage Agent**

## LADS fits this track because the full experience happens inside iMessage.

A user can send an Instagram reel or product name in chat. The agent identifies the product, checks lab signals, reviews, nutrition, seller trust, and prices, then replies with a clear score, best match, best value, watchouts, and buy links.

The user can ask “why?”, compare options, choose a product, confirm delivery details, and approve checkout through Prava without leaving the chat flow.

**Agent Commerce Discovery & Trust**

## LADS fits this track because discovery and trust are the core of the product.

A user can send a product or Instagram reel in iMessage. The agent identifies the product, checks Trustified lab-test signals, reads real user reviews across Reddit, Amazon, X, and Senso, and compares similar products.

For protein powders, it looks at nutrition, amino acids, ingredients, seller trust, reviews, and price. Senso helps us add product, brand, merchant, and offer signals.

The result is a clear trust score, better alternatives, and the best place to buy.

**Best Agentic User Experience**

## LADS fits this track because the full experience works inside iMessage.

A user can send an Instagram reel or product name in chat. The agent identifies the product, asks one useful follow-up question if needed, and checks nutrition, lab signals, real reviews, seller trust, and prices.

It replies with a clear score, best match, best value, review summary, watchouts, and buy links.

The user can ask “why?”, compare options, choose a product, confirm delivery details, and approve checkout through Prava, all through a normal chat flow.

**Agentic Commerce Hackathon**

## LADS fits this track because it helps a user go from product discovery to purchase inside chat.

A user can send an Instagram reel or health product name. The agent identifies the product, checks trust signals, reads real reviews across Reddit, Amazon, X, and Senso, compares better alternatives, and finds prices across stores.

For health supplements, it looks at nutrition, amino acids, ingredients, lab-test signals, seller trust, reviews, and price. It also gives an aggregated review summary when data is available.

Once the user picks a product, LADS prepares a live quote and moves payment approval to Prava. Card details stay with Prava, not inside the agent chat.

Team **buildooors** -- [Neel Patel](https://github.com/neel-ds), [Rahul Kulkarni](https://github.com/rkmonarch), [Vraj Desai](https://www.github.com/vrajdesai78), [Harsh Sachaniya](https://github.com/Harsh2220)

`2026-08-02`

---

### HealthGuard
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthguard-8ff9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AshutoshVatsg/HealthGuard) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://health-guard-web.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vY7V7GFlbZI) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Trusted, autonomous restocking agent

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FAST.API](https://img.shields.io/badge/FAST.API-333333?style=flat-square)

**The problem it solves**

**The problem it solves**

It started at home:

My grandparents live in one city and my parents live in another. That's not unusual any more We think— it's the default nowadays. The people who earn are somewhere else , and the loved ones are back home, often alone or some people are just alone. 

Two things go wrong, over and over:

1) "Did I took my 11AM medicines? " — a question with no good answer at 4pm. So you either skip it or double it, and both are bad.
The strip runs out on a Sunday. Nobody notices until it's empty. Then its a phone call, a technical hassle, a delivery app someone can't operate, or a two-day gap in deficit medication and delivery  that was never supposed to have gaps. 
A blood-pressure or thyroid course doesn't fail loudly ,it fails quietly overtime due to such problems. 

2) And on the other end, the caregiver is carrying a background process that never terminates: "has mom taken the medicines", "is it running low" , "I think I forgot to order it" , "did it arrive". It's not hard work. It's just never finished.

What **Health Guard** does

You declare a supply once- what it is, how much is used a day,and when to reorder.From then on the agent owns one bounded goal: keep this person's supply from running out, without ever exceeding what you authorised.

When stock is projected to hit the reorder point, the agent runs an

 *observe → discover → decide → act → verify loop-> check alarm -> replenish the stock using agent with live audit log*

It reads live merchant catalogues, matches only the exact approved product from a **verdict of intelligence** of comparing the product over different platform based on (delivery fastness , Reliability etc ), applies a deterministic policy, mints a single-use card, completes the checkout at the merchant, and writes the outcome to an audit ledger the caregiver can actually read.

No one holds a card. No one has to remember.

*Why this is safe enough to actually use*-
"An AI that can spend your money" is a sentence that should worry people. So we built the limits first using VISA. 

The authority is bounded, not granted. A Prava mandate is locked to one shop, one per-payment cap, one frequency, and a hard stop date — approved once with a passkey. The agent can't spend outside it. Not because it behaves well, but because it can't. Pause or cancel any time.

The model explains. It never decides , it cannot pick a product(but recommend it), approve spending, change inventory, or see a card. Deterministic code validates every action and rejects anything that isn't the exact approved item.

The card is single-use and even uses pre-AUTH from the user using mandate to solve the issue. The details are never spilled.

The intelligent commerce part

The agent doesn't buy from a hardcoded URL. It runs the real agentic-commerce stack:

1. Discover - live UCP catalogue search endpoint, using our published agent profile.
2. Decide- anything that can't arrive before the projected stock-out is rejected outright. FASTNESS is the priority.Among what's left, it takes the best landed price at from the shop you approved.
3. Authorise-  the mandate is re-synced with Prava and re-checked for status, cycle, cap and remaining balance under a row lock, so two runs can never double-charge. It uses pre-AUTH key from the user using mandate to cure problem.
4. Pay-  a single-use tokenised card is minted against that mandate.
5. Safe- The credentials are safe , mandates are maintained and the supplies are delivered. 
**6. Replenished -** We have made an andorid application for it ; the user sets the alarm once accordingly for the medicine ; The alarm rings-> the person gets the reminder to close it -> Agent keeps direct logs of tablets that has been taken by the user -> Replenish the medicine accordingly by itself.

*This whole process helps the beneficiary to stay HEALTHY and the caregiver to stay STRESSFREE.*

**Challenges we ran into**

Here are some challenges and learning we faced- 

**No checkout endpoint**  — Prava mints a one-time card but doesn't place the order, and their REST API has no checkout step. We built our own with headless Chromium driving the merchant's real checkout.

**Chromium won't start in a container** — It needs --no-sandbox and more shared memory than Docker gives it. We added the flags and blocked images/fonts to fit a 1 GB box.

Prava community and birdie helped us to resolve things out!!

**Best Visa Intelligent Commerce Implementation**

**Health Guard** is an autonomous **caregiver** for recurring OTC health supplies. A caregiver approves a merchant-
 scoped Prava mandate once using a passkey, defining the payment frequency, spending cap, validity period, and trusted merchant. The agent can then replenish approved products without requiring the user to return for every purchase.

Before payment, deterministic rules verify the exact product variant, stock level, merchant, price, mandate status, remaining balance, and recurring-cycle eligibility. Prava then provides a Visa network token and one-time dynamic CVV, which remain only in backend memory and are submitted directly to the merchant’s real Shopify checkout.

 Health Guard reports only the observed outcome to Prava: confirmed orders are APPROVED, while processor declines or checkout failures are DECLINED. Inventory is updated only after a confirmed merchant order. This keeps **Transparency **for the user.

This demonstrates consumer-bounded agentic commerce using *pre-authorised, tokenised Visa payments* without exposing card details to the merchant , browser, or LLM.

Its machine-readable agent identity, deterministic transaction references, and complete audit trail align with Visa TAP by making agent activity *identifiable, authorised, and accountable.*

Its not just a use-case , but visa is the integral part of becoming a human wellness caregiver from its Intelligent commerce solution.

**Most Startup-Ready Product**

Millions of families manage recurring health supplies for parents, children, and themselves, yet replenishment still depends on remembering dates, checking stock, finding the correct product, and completing checkout every time. A missed reorder can disrupt medicine routine and create unnecessary stress especially for caregivers managing multiple people. **Health Guard** turns this repetitive task into a safe, autonomous service.

Users simply add a beneficiary, describe an approved OTC supply, enter current stock and daily usage, and choose trusted merchants. Health Guard predicts when stock will run low, searches live catalogs, selects the exact approved variant, and completes checkout within strict consumer defined limits.
Users retain control through spending caps,
 payment frequency, pause/cancel controls, realtime tracking, and a complete audit trail.

Health Guard is startup-ready because the end to end product already works: inventory intelligence, live merchant
discovery, agentic checkout, tokenised recurring payments, stock reconciliation, and a human-friendly dashboard. It has
a clear subscription opportunity for households and a strong B2B2C path through pharmacies, eldercare providers, employers, and healthcare platforms. The result is a high-retention product built around a recurring, 
*Universal need*:  ensuring essential supplies are available before they run out.

This is the problem seen in every household nowdays ; as people are moving here and there for bread earning . For such problem we bring you the cure.

**OpenAI**

**The problem it solves**

It started at home:

My grandparents live in one city and my parents live in another. That's not unusual any more We think— it's the default nowadays. The people who earn are somewhere else , and the loved ones are back home, often alone or some people are just alone. 

Two things go wrong, over and over:

1) "Did I took my 11AM medicines? " — a question with no good answer at 4pm. So you either skip it or double it, and both are bad.
The strip runs out on a Sunday. Nobody notices until it's empty. Then its a phone call, a technical hassle, a delivery app someone can't operate, or a two-day gap in deficit medication and delivery  that was never supposed to have gaps. 
A blood-pressure or thyroid course doesn't fail loudly ,it fails quietly overtime due to such problems. 

2) And on the other end, the caregiver is carrying a background process that never terminates: "has mom taken the medicines", "is it running low" , "I think I forgot to order it" , "did it arrive". It's not hard work. It's just never finished.

What **Health Guard** does

You declare a supply once- what it is, how much is used a day,and when to reorder.From then on the agent owns one bounded goal: keep this person's supply from running out, without ever exceeding what you authorised.

When stock is projected to hit the reorder point, the agent runs an

 *observe → discover → decide → act → verify loop*

It reads live merchant catalogues, matches only the exact approved product from a **verdict of intelligence** of comparing the product over different platform based on (delivery fastness , Reliability etc ), applies a deterministic policy, mints a single-use card, completes the checkout at the merchant, and writes the outcome to an audit ledger the caregiver can actually read.

No one holds a card. No one has to remember.

*Why this is safe enough to actually use*-
"An AI that can spend your money" is a sentence that should worry people. So we built the limits first using VISA. 

The authority is bounded, not granted. A Prava mandate is locked to one shop, one per-payment cap, one frequency, and a hard stop date — approved once with a passkey. The agent can't spend outside it. Not because it behaves well, but because it can't. Pause or cancel any time.

The model explains. It never decides , it cannot pick a product(but recommend it), approve spending, change inventory, or see a card. Deterministic code validates every action and rejects anything that isn't the exact approved item.

The card is single-use and even uses pre-AUTH from the user using mandate to solve the issue. The details are never spilled.

The intelligent commerce part

The agent doesn't buy from a hardcoded URL. It runs the real agentic-commerce stack:

1. Discover - live UCP catalogue search endpoint, using our published agent profile.
2. Decide- anything that can't arrive before the projected stock-out is rejected outright. FASTNESS is the priority.Among what's left, it takes the best landed price at from the shop you approved.
3. Authorise-  the mandate is re-synced with Prava and re-checked for status, cycle, cap and remaining balance under a row lock, so two runs can never double-charge. It uses pre-AUTH key from the user using mandate to cure problem.
4. Pay-  a single-use tokenised card is minted against that mandate.
5. Safe- The credentials are safe , mandates are maintained and the supplies are delivered.

**Best Agentic User Experience**

Our user is 70 and may live alone. The person who set this up is in another city ..That's the *hard agentic UX problem: the user can't supervise the agent, so the interface has to earn trust on its behalf*.

It settles "did I already take it?" for the person, and it tells the agent a unit is gone. Depletion is tracked from confirmed consumption, not an assumption, so the reorder trigger is grounded in something real rather than a decayed estimate.
from confirmed consumption, not an assumption, so the reorder trigger is grounded in something real rather than a decayed estimate.

- **Legible** -Each run reads as plain English — Checked stock → Checked approved stores → Applied your rules → Requested payment → Confirmed result 

- **Bounded**, and it says so. Before you grant spending power the screen restates it in your words: "You are allowing up to ₹1,000 · once a month, at Himalaya Wellness terministic policy . Picks the product and authorises the spend; the model only writes the explanation you read.

- **Honest**- A failure says what happened — the merchant refused the one-time card.Tracked stock was not changed." 

- **Navigated**- The person at first is allowed to navigate the user experience after the first login ; that how to create and setup the agent.

Nothing is one-way
You can pause, cancel, or correct the stock count from any screen.

**Agentic Commerce Hackathon**

Health Guard is an autonomous **caregiver** for the medicines and OTC supplies an elderly or isolated person can't afford to run out of or are not familiar with tech  skills. It doesn't recommend a purchase  it completes one. And for the purchased ones; it helps them to notify on time to take the medicine using alarm.

The agent owns one bounded goal: keep a declared supply in stock without ever exceeding what the user authorised. When stock is projected to hit the reorder point, it runs the full loop end to end. When the user hits close alarm on app, it takes the information to understand that the medicines have been taken and restock accordingly..

- Discover — live UCP catalogue search against the merchant's own Shopify endpoint, under our published agent profile.
- Decide — a deterministic policy rejects anything that isn't the exact approved product, isn't in stock, or can't arrive before the projected stock-out. An LLM can explain the decision in plain English; it can never make it.
- Pay — a single-use Visa network token and dynamic CVV, minted against a merchant-scoped Prava mandate the user approved once with a passkey.
- Complete — headless Chromium drives the merchant's real checkout and presents that card, because most merchants have no payment API.
- Settle — the true outcome is reported backudit ledger the caregiver can read.

Prava isn't bolted on — it's the authority model. The mandate is what makes autonomous spending safe enough to hand to a stranger's software: capped per charge, li one merchant, revocable instantly.

Verified end to end in the Prava sandbox.

It solves a problem we have in our own families, or the ones that are indeed in need.

Team **Kitlers** -- [Ashutosh Vats](https://github.com/AshutoshVatsg), [Sudhir Kumar Sah](https://github.com/sudhirKsah), [Sunil Swain](https://github.com/sunilswain7)

`2026-08-03`

---

### 🏥 Hospital Copilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hospital-copiolts-e555) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Piyush9940/hospital_copilot1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hospital-copilot1-ql8j.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/jbUtnXdyEdg?si=dzt_s663N6FBjN6A) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> One Intelligent System for Connected Healthcare.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Socket Programming](https://img.shields.io/badge/Socket%20Programming-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Twilio](https://img.shields.io/badge/Twilio-333333?style=flat-square)

**The problem it solves**

# 🏥 Hospital Copilot
### *Redefining Emergency Healthcare with AI-Powered Intelligence*

---

> **"Every second counts in an emergency. Hospital Copilot ensures no second is wasted."**

---

## ⚡ The Problem

Healthcare today is **fragmented** and **reactive**.

| Challenge | Impact |
|-----------|--------|
| 🚫 No instant access to patient history | Delayed diagnoses |
| 🚫 Scattered reports & allergy records | Treatment errors |
| 🚫 No real-time vitals during emergencies | Blind decision-making |
| 🚫 Siloed hospital systems | Critical time lost |

When every second matters — the current system **fails patients**.

---

## 🌐 The Solution

**Hospital Copilot** is a unified, AI-powered healthcare ecosystem that brings together emergency response, AI diagnosis, wearable monitoring, and unified patient records — all in one seamless platform.

---

## 🚨 Core Features

### `01` — Emergency Alert System
> **Shake your phone. Help is on the way.**

- 📳 **Shake-to-Alert** trigger — no buttons, no delays
- 🏥 Hospitals instantly receive the patient's full identity and medical history
- 💊 Known allergies and active medications delivered at the moment of crisis
- 🤖 AI-generated medical insights alongside live vitals and real-time risk analysis

---

### `02` — AI Diagnostic Engine
> **From scan to insight in seconds.**

Hospital Copilot supports deep AI analysis across all major medical imaging modalities:

| Modality | Capability |
|----------|-----------|
| 🧠 MRI | Tumor detection, anomaly flagging |
| 🫁 CT Scan | Organ & tissue analysis |
| 🦴 X-Ray | Fracture & pathology detection |
| 🔊 Ultrasound | Real-time structure analysis |
| 🩸 Blood Reports | Automated biomarker interpretation |
| 🦠 Skin Disease | Visual pattern recognition |

---

### `03` — Wearable Health Monitoring
> **Your body, always connected.**

- 📡 Continuous vitals streaming directly to the platform
- 📈 Real-time risk scoring and anomaly detection
- 🔔 Proactive alerts before emergencies escalate
- 🔗 Seamlessly synced to your unified patient profile

---

### `04` — Unified Patient Records
> **One patient. One truth. Everywhere.**

- 🗂️ Centralized medical history across all providers
- 💊 Medication history, allergies, and past diagnoses in one place
- 🔒 Secure, instant access for authorized physicians
- 🔄 Always up-to-date, always available at the point of care

---

### `05` — Smart Assistive Devices
> **AI that sees the world for you.**

Built specifically for visually impaired users, powered by three specialized AI models working in concert:

- **YOLOv8n** for real-time object detection and obstacle identification
- **VLMs** for deep scene understanding and contextual awareness
- **Whisper** for natural voice I/O and hands-free command processing

Combined, they deliver AI-guided navigation, real-time safety alerts, and a fully voice-first accessibility experience.

---

## 🎯 Impact at a Glance

| Metric | What Hospital Copilot Delivers |
|--------|-------------------------------|
| ⏱️ Response Time | Near-instant alert-to-hospital communication |
| 📋 Data Availability | 100% patient history at point of care |
| 🤖 AI Coverage | 6+ medical imaging & report types |
| ♿ Accessibility | Full assistive AI for visually impaired users |
| 🔗 Integration | Wearables, mobile, and hospital systems unified |

---

## 🔮 Vision

> *Hospital Copilot isn't just a product — it's infrastructure for a future where no patient suffers because a doctor didn't have the right information at the right time.*

**From reactive treatment → Proactive, intelligent, connected care.**

---


**Built for the future of healthcare. Available in the present.**

`Emergency Response` · `AI Diagnostics` · `Wearable Monitoring` · `Assistive AI`

**Challenges we ran into**

# ⚔️ Challenges We Ran Into

> *Building Hospital Copilot wasn't just a technical challenge — it was a battle against complexity, latency, and scale. Here's how we fought back.*

---

## `Challenge 01` — Unifying a Multi-Module Ecosystem

**The Problem**

Integrating five independent healthcare systems — AI diagnosis, emergency response, wearable monitoring, patient records, and assistive devices — into a **single real-time workflow** introduced severe synchronization and backend communication breakdowns.

**The Fix**

We architected a centralized communication layer that acts as the nervous system of the platform, ensuring every module speaks the same language and stays in sync — regardless of data type or source.

> Five systems. One heartbeat. Getting them to pulse together was the first war.

---

## `Challenge 02` — The Emergency Trigger Problem

**The Problem**

Detecting **intentional** phone shakes without triggering false alerts — across a wide range of Android devices with varying accelerometer sensitivities — was far harder than it sounds.

| Scenario | Risk |
|----------|------|
| Walking fast | False alert |
| Phone dropped | False alert |
| Real emergency shake | Must not miss |

**The Fix**

We introduced a two-step verification flow. First, a gesture verification layer checks shake pattern, threshold, and duration to filter out accidental triggers. If that passes, the user must confirm via a **secondary volume-button press** before any alert is dispatched.

> We taught the app the difference between a stumble and a scream for help.

---

## `Challenge 03` — Heavy Files, Real-Time Pressure

**The Problem**

MRI scans, CT images, and X-rays are **large, complex files**. Feeding them through AI models and returning diagnostic reports fast enough for real-time clinical use was a serious performance bottleneck.

**The Fix**

- 🗜️ File handling optimized at the point of upload to reduce payload size
- 🧩 AI services **decoupled** into independent FastAPI microservices — one per modality
- 🔗 Streamlined API communication bridge between the **Node.js** backend and AI inference layer
- ⚡ Result: diagnostic reports generated fast enough for live clinical workflows

---

## `Challenge 04` — Keeping Patient Context Consistent

**The Problem**

As data flowed between AI modules, medical reports, live vitals, and emergency triggers — **patient identity kept fragmenting**. A report in one module had no awareness of vitals in another, breaking the continuity doctors depend on.

**The Fix**

We designed a **Unified Patient Identity Structure** — a single `Patient ID` that serves as the anchor for every data point across the entire platform. All reports, vitals, and emergency events are linked through this one identifier, ensuring no module ever loses context.

> One ID. Every module. Zero context loss.

---

## `Challenge 05` — Three AI Models. One Tiny Device.

**The Problem**

Running **YOLOv8n**, a **VLM**, and **Whisper** simultaneously on resource-constrained hardware for real-time assistive navigation was pushing the limits of what the device could handle — latency spiked, frames dropped, and the experience broke down.

| Model | Role | Cost |
|-------|------|------|
| YOLOv8n | Object detection | High CPU/GPU |
| VLM | Scene understanding | High memory |
| Whisper | Voice I/O | Continuous audio |

**The Fix**

- ✅ Switched to lightweight model variants without sacrificing core accuracy
- ✅ Optimized inference pipelines per model to reduce per-frame overhead
- ✅ Gated unnecessary processing during active navigation sessions
- ✅ Introduced async scheduling between voice and vision tasks to prevent blocking

> We didn't scale up the hardware. We scaled down the waste.

---

## 🧠 What We Learned

| Lesson | Takeaway |
|--------|----------|
| 🔗 Integration is harder than building | Synchronizing systems > building them individually |
| 🎯 UX is a safety feature | A false emergency alert is a system failure |
| ⚙️ Microservices save real-time systems | Decoupling AI from backend = speed |
| 🪪 Identity is the backbone of data | A unified ID solves more than a database ever could |
| 🪶 Lightweight beats powerful on edge | Optimization > raw compute in constrained environments |

---


*Every bug we fixed made Hospital Copilot more resilient.*
*Every bottleneck we broke made it faster.*
*Every challenge made it real.*

**Internet of Things**

# 📡 IoT Integration — Hospital Copilot

> *Hospital Copilot isn't just a software platform — it is a connected healthcare infrastructure where smart devices, wearables, and hospitals talk to each other in real time.*

---

## 🌐 Why IoT is at the Heart of Hospital Copilot

Healthcare emergencies don't wait. Hospital Copilot leverages the Internet of Things to ensure that patient health data, emergency signals, and AI insights flow continuously — from the patient's body to the doctor's dashboard — without delay, without gaps.

---

## 📲 IoT Capabilities at a Glance

| Capability | What It Does |
|------------|-------------|
| ⌚ Real-Time Wearable Monitoring | Continuous health data streamed live from wearables |
| 💓 Continuous Vitals Tracking | Heart rate, SpO2, temperature and more — always on |
| 🔴 Live Anomaly Detection | Instant flagging when vitals cross critical thresholds |
| 📳 Smart Emergency Triggering | Phone motion sensors detect distress and fire alerts |
| 🦯 Smart Assistive Devices | IoT-powered glasses and stick for visually impaired users |
| 🏥 Connected Emergency Alerts | Direct, real-time alert pipeline from patient to hospital |

---

## 🦯 Smart Devices as Healthcare IoT Nodes

### Smart Stick & Smart Glasses
> **Not accessories. Active nodes in the healthcare network.**

Our smart stick and smart glasses are purpose-built IoT healthcare devices that operate as live endpoints within the Hospital Copilot ecosystem. They continuously:

- 📡 Stream environmental and user data to backend APIs
- 🤖 Interact with AI vision and language models in real time
- 🏥 Stay connected to hospital infrastructure for emergency escalation
- 🔔 Trigger alerts and receive responses without any screen interaction

---

## 🔄 The Real-Time Data Pipeline

Every piece of data in Hospital Copilot flows through a single, unified pipeline — from the patient's body to the clinical team's hands.

**Wearables & Smart Devices**
Continuously collect vitals, motion data, and environmental signals

**↓**

**Backend APIs**
Ingest, validate, and route incoming data streams in real time

**↓**

**AI Analysis**
Anomaly detection, risk scoring, and intelligent insight generation

**↓**

**Hospital Dashboard**
Live patient cards, vitals feeds, and AI-generated alerts for clinical staff

**↓**

**Emergency Response**
Automated triage prioritization and instant physician notification

---

## 📊 What Hospitals Receive in Real Time

- 💓 **Live vitals feed** — continuous stream from patient wearables
- 🚨 **Emergency alerts** — triggered by motion sensors or anomaly detection
- 🤖 **AI-generated insights** — risk scores, summaries, and flagged conditions
- 📋 **Full patient context** — history, allergies, and medications linked to every alert

---

## 🔮 Connected Healthcare, Redefined

> *Hospital Copilot turns every wearable, every smart device, and every phone into an active node in a living healthcare network — enabling proactive, real-time, connected care at scale.*

**Patients are monitored. Doctors are informed. Emergencies are anticipated — not just reacted to.**

---


`Wearables` · `Smart Devices` · `Real-Time Pipelines` · `Connected Hospitals` · `Proactive Care`

**AI & ML**

# 🤖 AI & ML at the Core of Hospital Copilot

> *Hospital Copilot doesn't just use AI as a feature — it is built from the ground up on intelligence. Every module, every decision, every alert is powered by machine learning.*

---

## 🧬 How We Use AI & ML

### `01` — Medical Image Analysis
> **Seeing what the human eye might miss.**

Our platform runs deep AI analysis across every major medical imaging modality:

| Modality | What AI Does |
|----------|-------------|
| 🧠 MRI | Tumor detection & structural anomaly flagging |
| 🫁 CT Scan | Organ segmentation & tissue-level analysis |
| 🦴 X-Ray | Fracture detection & pathology classification |
| 🔊 Ultrasound | Real-time structural pattern recognition |
| 🦠 Skin Disease | Visual diagnosis via lesion pattern analysis |
| 🎯 Tumor Detection | Multi-class classification across scan types |

---

### `02` — CNN-Based Disease Detection
> **Trained to diagnose. Built to scale.**

Convolutional Neural Networks power our core diagnostic pipeline — trained on medical imaging datasets to detect and classify diseases with clinical-grade precision, directly from raw scan inputs.

---

### `03` — LLMs + RAG Pipeline — The AI Nurse
> **A doctor's intelligent second opinion, always available.**

Our AI Nurse system is built on a **Large Language Model** paired with a **Retrieval-Augmented Generation (RAG)** pipeline, enabling:

- 🗂️ Contextual reasoning grounded in the patient's own medical history
- 📋 Accurate, evidence-backed responses — not hallucinated answers
- 💬 Natural language interaction for both patients and clinical staff
- 🔍 Dynamic retrieval of relevant medical knowledge at query time

---

### `04` — AI-Generated Summaries & Risk Classification
> **Turning raw data into decisions.**

- 📝 Automated medical summaries generated from reports, vitals, and history
- 🚦 Risk classification engine that stratifies patients into priority tiers
- ⚡ Delivered instantly — so doctors walk in informed, not overwhelmed

---

### `05` — Emergency Triage Intelligence
> **The right patient treated first. Every time.**

Our triage AI synthesizes three data streams simultaneously:

- 🩺 **Symptoms** reported at the time of emergency
- 💓 **Live vitals** streamed from wearables
- 📁 **Medical history** pulled from the unified patient record

The result is an intelligent priority score that ensures the most critical patients are never waiting behind less urgent cases.

---

### `06` — YOLOv8n & Vision-Language Models
> **AI eyes for those who need them most.**

Powering our smart assistive devices for visually impaired users:

- **YOLOv8n** — Lightweight, real-time object detection optimized for edge hardware
- **VLMs (Vision-Language Models)** — Deep scene understanding with natural language descriptions of the environment

Together, they give users a continuous, intelligent picture of the world around them.

---

### `07` — Whisper-Based Speech Processing
> **Voice as the interface. Accessibility as the standard.**

OpenAI's **Whisper** model handles all voice interaction across the assistive device layer:

- 🎙️ Real-time speech-to-text for hands-free command input
- 🔊 Natural voice responses for navigation and safety alerts
- ♿ Fully accessible experience without requiring any screen interaction

---

## 🧠 The AI Stack at a Glance

| Domain | Technology |
|--------|-----------|
| Computer Vision | CNNs, YOLOv8n, VLMs |
| Natural Language Processing | LLMs, RAG pipelines, Whisper |
| Medical AI | Image classification, anomaly detection, risk scoring |
| Reasoning Systems | Retrieval-Augmented Generation, triage intelligence |
| Real-Time Inference | Optimized FastAPI microservices per AI module |

---

## 🔗 One Connected Intelligence

> *Hospital Copilot brings together computer vision, natural language processing, medical AI, reasoning systems, and real-time inference — not as isolated tools, but as one unified, connected healthcare intelligence layer.*

**Every alert is smarter. Every diagnosis is faster. Every patient is safer.**

---


`Computer Vision` · `NLP` · `Medical AI` · `Reasoning Systems` · `Real-Time Inference`

Team **Technovative** -- [Rakshitha LU](https://github.com/Rakshu9595), [Piyush kumar](https://github.com/Piyush9940), [Avinash Mahuuroliya](https://github.com/avinashmaharoliya), [Siya Behera](https://github.com/bihimole90-droid)

`2026-05-10`

---

### CliniQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cliniq-a5f5) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Clinical Intelligence

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Text-to-Speech](https://img.shields.io/badge/Text--to--Speech-333333?style=flat-square) ![Speech API](https://img.shields.io/badge/Speech%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

aaaaaaaaaaaaaaaaaaaaa

**Challenges we ran into**

aaaaaaaaaaaaaaaaaaaa

Team **Bad Boiss :)** -- [Sibhi S](https://github.com/SibhiSS), VRT KAARTHIK, [Vedanth K](https://github.com/vedanthk-engr), [Keerthivasa krishna A](https://github.com/Keerthivasakrishna)

`2026-06-14`

---

### Know Your Trial
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/know-your-trial-60b2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abhi6537/Know-Your-Trials) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Stop manually searching for clinical trials.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PyPDF2](https://img.shields.io/badge/PyPDF2-333333?style=flat-square) ![React Router](https://img.shields.io/badge/React%20Router-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square) ![GPT-2](https://img.shields.io/badge/GPT--2-333333?style=flat-square) ![chromadb](https://img.shields.io/badge/chromadb-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square) ![huggingface transformers](https://img.shields.io/badge/huggingface%20transformers-333333?style=flat-square)

**The problem it solves**

Finding clinical trials for rare diseases (like Fabry, Pompe, or Gaucher disease) is notoriously difficult and heartbreakingly slow. Clinical trial coordinators and patients often spend hours manually cross-referencing dense, unstructured patient histories (PDFs) against highly technical, jargon-heavy inclusion/exclusion criteria on **ClinicalTrials.gov.**

The biggest bottleneck? The semantic gap. Traditional keyword-matching algorithms completely fail in healthcare. If a trial protocol requires "chronic nerve pain", but a patient's medical note states "severe distal paresthesia", standard database queries will miss the connection entirely—potentially costing a patient access to a life-saving experimental therapy.

"Know Your Trial" is a multi-agent AI pipeline designed to eliminate this bottleneck. We built a deterministic intelligence engine that automates the entire matching pipeline:

Automated Ingestion: It parses massive, unstructured patient clinical PDFs (simulated via our GPT-2 Data Gen).
**Semantic Extraction:** A specialized BioBERT NER Agent extracts phenotypes, labs, and medications, mapping them to standard Human Phenotype Ontology (HPO) terms to bridge the vocabulary gap.
**High-Speed Retrieval:** It queries these embeddings against active clinical trial protocols stored in our RAG Pipeline (Supabase + ChromaDB).
**Explainable AI:** The Orchestrator Agent delegates the final scoring to our Explainability Agent (Gemini 2.0 Flash Lite), which generates a physician-level breakdown of exactly why a patient passed or failed.
What used to take a medical coordinator 4 to 6 hours per patient is now executed with higher precision in under 15 seconds. It doesn't just match patients; it democratizes access to experimental treatments by making clinical trial discovery instant and universally accessible.

**Challenges we ran into**

1. The "Black Box" Trust Barrier in Healthcare Early in development, we realized that generating a "98% Match Score" was useless. In clinical environments, doctors do not trust opaque AI decisions. If the system couldn't justify its reasoning, it would never be adopted. How we got over it: We pivoted our architecture to prioritize transparency. Instead of using a single LLM to guess the answer, we engineered an Explainability Agent powered by Gemini 2.0 Flash Lite. We forced the pipeline to return deterministic, citation-backed JSON payloads. Now, the UI renders a line-by-line breakdown report, citing the exact sentence in the patient's record that satisfies the specific NCT protocol criterion. We turned a black box into an auditable clinical tool.

2. Hallucinating Temporal Constraints As we scaled the matching engine, we hit a massive hurdle with temporal logic. Our early semantic search was incredible at mapping phenotypes (e.g., matching "enlarged spleen" to "splenomegaly"), but it completely hallucinated strict temporal boundaries. For instance, a Gaucher disease trial excluded patients who had been on Enzyme Replacement Therapy (ERT) for less than 12 months. The LLM would see the keyword "ERT" in the patient file and flag them as eligible, completely ignoring the timeline. How we got over it: We realized you can't use language models for discrete math. We ripped out the pure-LLM matching approach and built a Hybrid Multi-Modal Engine. We introduced a deterministic Python scoring layer utilizing Regex to handle numeric, categorical, and temporal data (like calculating exact months between dates). We then built an Orchestrator Agent that acts as a router—sending temporal rules to the Python engine, and sending complex linguistic rules to the BioBERT NER Agent. By decoupling the logic, we eliminated temporal hallucinations entirely while maintaining deep semantic understanding.

**Best Use of Gemini API**

Use of Gemini API" track so it stands out completely.

Here is the revised version for Best Use of Gemini API. You can replace the previous one with this:

To build true trust in medical AI, doctors need to see the exact reasoning behind an algorithm's decision. We integrated the Gemini 2.0 Flash Lite API at the core of our multi-agent architecture to act as a high-speed "Explainability Agent" and solve this exact "Black Box" problem.

Instead of using Gemini to simply "guess" a clinical match, we use it as an auditable justification engine. After our deterministic Python rules engine and BioBERT NLP models calculate the initial clinical overlap, our Orchestrator Agent passes the complex semantic payload (the patient's HPO phenotypes and the clinical trial's NCT criteria) directly to Gemini.

We leverage Gemini's massive context window and lightning-fast inference to generate a deterministic, physician-level breakdown report. Gemini evaluates the payload and outputs strict, structured JSON that explicitly explains why a patient passed or failed a rule. It acts as a medical auditor—citing the exact sentence from the unstructured patient record that satisfies the trial's requirements.

By integrating the Gemini API, we transformed an opaque, untrustworthy matching algorithm into a transparent, auditable clinical tool that doctors can trust to accelerate life-saving research.

**Healthcare**

**Know Your Trial** tackles one of the most critical and time-consuming bottlenecks in modern healthcare: clinical trial matching for rare diseases.

Currently, clinical trial coordinators spend countless hours manually cross-referencing dense, unstructured patient histories against complex, jargon-heavy trial protocols on ClinicalTrials.gov. This manual process is slow, error-prone, and often results in eligible patients missing out on life-saving experimental therapies simply due to vocabulary mismatches (e.g., a doctor writing "distal paresthesia" while the trial requires "chronic nerve pain").

Our project fits perfectly into the Healthcare track because it modernizes this archaic workflow using a multi-agent AI architecture. By combining a fine-tuned BioBERT NER Agent for clinical entity extraction, a RAG Pipeline for high-speed semantic retrieval, and a deterministic Python Scoring Engine for temporal/numeric rules, we automate the matching process with unprecedented speed and accuracy.

Most importantly, we address the critical issue of trust in medical AI. Healthcare professionals cannot rely on black-box algorithms. We engineered an Explainability Agent (powered by Gemini 2.0 Flash Lite) that generates transparent, physician-level reports justifying exactly why a patient passed or failed a criterion, citing the specific sentence in their medical record.

By bridging the semantic gap between patient data and clinical protocols, Know Your Trial reduces matching time from hours to seconds—directly accelerating clinical research and democratizing access to experimental treatments for patients who need them most.

How It Works (In Simple Terms)
Finding a clinical trial is usually like looking for a needle in a haystack. Know Your Trial automates the whole process in four simple steps:

Step 1: Upload the Patient's File A doctor or clinical coordinator uploads a patient's standard medical record (like a PDF). These files are usually messy, full of medical jargon, and hard to read quickly.

Step 2: The AI "Reads" Like a Doctor Instead of just looking for exact keywords (which often fails), our AI Engine reads the medical record to understand the meaning behind it. For example, if the doctor wrote "severe tingling in the hands," the AI knows this is the exact same thing as "chronic nerve pain"—a symptom required by many rare disease trials.

Step 3: The Smart Match In milliseconds, the system scans through thousands of active clinical trial protocols. It acts like a highly advanced matchmaking service, instantly comparing the patient's exact symptoms, age, and medical history against the strict rules of every available trial.

Step 4: A Human-Readable Explanation We don't just give a "Match Score" and leave doctors guessing. Our final AI Agent acts as an explainer. It generates a clear, easy-to-read report that says, "This patient is a match for Trial X because they meet criteria A, B, and C. Here is the exact sentence in their medical record that proves it."

By doing this, we turn hours of frustrating paperwork into a 15-second process, helping patients get life-saving treatments faster.

Team **JUGAADU** -- [Kripasindhu Ghosh](https://github.com/kripa521), [Abhinandan Ghosh](https://github.com/Abhi6537), [AMRIT KAR](https://github.com/Amrit7679), [Piuli Biswas](https://github.com/iampiuli)

`2026-07-26`

---

### AuditCli2
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/auditcli-27bb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SWAPNA2301/AuditCli2) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3s3BQcUIK18) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> The AI-Powered Health Check for the Web

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Jira](https://img.shields.io/badge/Jira-333333?style=flat-square)

**Challenges we ran into**

Integrating multiple audit modules into one CLI.
Handling websites with different structures and anti-bot protections.
Ensuring accurate SEO, security, and performance analysis.
Managing API rate limits and network timeouts.
Standardizing report generation (HTML/Markdown) across different audit results.
Automating Jira issue creation while handling authentication and API errors.
Designing a scalable architecture for future AI-powered insights and integrations.

**The problem it solves**

Eliminates the need to use multiple tools for website audits.
Quickly identifies SEO, security, performance, and broken link issues.
Provides actionable recommendations in one place.
Compares your website with competitors to uncover improvement opportunities.
Automatically creates Jira issues, reducing manual work and speeding up bug tracking.

Team **Eggroll** -- [Swapna PalChowdhury](https://github.com/SWAPNA2301), [BISWARANJAN NAG](https://github.com/biswa0009)

`2026-07-26`

---

### AI-Powered Drug Interaction Prediction System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-drug-interaction-prediction-system-163a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/FeralSatyam/team_yukti_deerhack_2026) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/WRf0eJoaD0Y) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%202026-0052CC?style=flat-square)](https://deerhack26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Know the risk before you prescribe.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square)

**The problem it solves**

Polypharmacy is the use of multiple medications simultaneously. It is one of the most underappreciated dangers in modern healthcare. In Nepal and globally, patients with chronic conditions routinely take 5, 8, even 12+ drugs at once. Dangerous interactions between these drugs cause an estimated 125,000 deaths annually in the US alone, and are responsible for roughly 30% of all hospital admissions in elderly patients. Yet checking interactions manually across every possible drug pair is slow, error-prone, and rarely done comprehensively in busy clinical settings.
Our solution solves this by giving doctors an instant, AI-powered second opinion on their patient's medication stack before any harm occurs.

**Challenges we ran into**

Challenges I Ran Into
1. Getting the GNN Architecture to Match the Checkpoint exactly.
The single most frustrating debugging session of the hackathon. After training the model on Google Colab, loading the checkpoint locally kept throwing RuntimeError: size mismatch errors. The issue turned out to be a combination of subtle mismatches: the production model.py had slightly different default hyperparameters than the training notebook, and a global_R parameter that existed in the checkpoint wasn't being declared in the inference model class.
The fix required methodically comparing state_dict keys between the checkpoint and the live model, tracing every tensor shape through the encoder and both decoder heads, and hardcoding the exact architecture defaults (hidden_dim=64, embed_dim=32, dropout=0.1) so they could never silently drift. It now loads cleanly but it was a reminder that ML reproducibility is genuinely hard.

2. Side Effects Flooding Every Result with the Same Drugs
Early versions of the predictor returned nearly identical side effect lists for every drug combination because globally common side effects (nausea, headache, fatigue) had high raw probabilities across all pairs and completely dominated the output. A Warfarin + Aspirin interaction was showing the same top 5 effects as a totally unrelated antibiotic pair.
The solution was an adaptive per-pair threshold: instead of a fixed cutoff, we compute mean + 1.5σ of the side effect score distribution within each pair. This forces the model to surface effects that are unusually elevated for that specific combination, not just universally common ones. The results immediately became clinically meaningful hemorrhage rising to the top for blood thinner combinations, cardiac effects surfacing for the conduction-risk scenarios.

3. Protein Index Collision in the Graph
The biological graph combines drug nodes and protein nodes into a single shared embedding matrix. Early in development, protein node indices started at 0 the same as drug indices which caused silent data corruption where drug embeddings and protein embeddings were being mixed together during message passing. No crash, no obvious error, just subtly wrong predictions.
The fix was adding a hard offset: all protein node indices now start at num_drugs (2135), making drug and protein indices mutually exclusive. We also added an assertion at graph construction time to catch any future overlap immediately. This is now one of the top "do not touch" rules in our project notes.

4. Three Services, One Demo Keeping Everything Running Together
PharmaSafe is three separate services: a Python FastAPI ML backend, a Node.js Express API, and a React frontend. During the hackathon, getting all three to start reliably, talk to each other correctly, and fail gracefully when one was down was an ongoing challenge.
The most impactful fix was building a proper frontend fallback: if the Python ML service is unreachable, the frontend silently switches to a rule-based heuristic estimator and shows a yellow toast warning the UI never crashes or white-screens. This saved the demo more than once when the ML service was still loading its 2.6M-parameter checkpoint at startup.

5. Drug Name Resolution Across Two Naming Systems
The GNN operates on STITCH IDs (a standardised chemical database format like CID100000085), but doctors type drug names like "Warfarin" or "ibuprofen". Bridging that gap cleanly required building a case-insensitive lookup map (drug_name_to_stitch.json) and handling edge cases where a submitted name had no match returning a clean 400 error with the unrecognised drug name, rather than silently dropping it or crashing the inference pipeline.

**Data Science / Machine Learning**

Our solution is machine learning at its core. The entire value of the product - detecting dangerous drug combinations, predicting adverse side effects, and grading polypharmacy risk - comes from a Graph Neural Network we designed, trained, and deployed from scratch.
The problem demanded a graph-based approach because drug interactions are fundamentally relational. Drugs don't exist in isolation; they interact with proteins, proteins interact with each other, and the downstream effect of combining two drugs depends on the entire biological network they sit inside. We modelled this using the DECAGON biomedical dataset, constructing a heterogeneous graph of 2,135 drug nodes and thousands of protein nodes connected by over 1.8 million biological edges. Each drug node is initialised with Morgan fingerprints encoding its chemical structure, combined with its individual side effect profile - giving the model both structural and pharmacological context before message passing even begins.
The GNN itself uses relation-specific GraphSAGE convolutions in its first layer, with separate learnable kernels for drug-drug, drug-protein, and protein-protein edge types. This directly mirrors the Decagon architecture and allows the model to treat biologically distinct relationships differently rather than flattening them into a single aggregation. The side effect decoder uses a diagonal bilinear DEDICOM formulation - one learned diagonal matrix per side effect type - which lets the model capture how each specific adverse effect is mediated differently across drug pairs. A separate harm classification head then distils the full side effect profile into a binary danger signal, trained on whether a pair shares 20 or more harmful side effects.
On the test set of 6,348 drug pairs, the model achieves a ROC-AUC of 0.8838, an average precision of 0.7473, and - most importantly for a clinical tool - a recall of 98.75%. That last number was a deliberate design choice: in a medical context, missing a genuinely dangerous combination is far worse than raising a false alarm, so we tuned the model to err heavily on the side of caution. The lower precision (0.3628) and F1 (0.5307) are an accepted trade-off for that safety guarantee. The full system is served via FastAPI, integrated into a Node.js backend, and surfaced through a React frontend that makes the model's predictions accessible to a doctor in a few clicks.

Team **Yukti** -- Satyam Rana, Aayush Shah Nirala, Furi Lama, Shreejesh joshi

`2026-06-13`

---

### Healthify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthify-db0c) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Decode your food as labels are lying...

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Healthify’s food scanner solves the critical problem of Information Asymmetry by stripping away deceptive "Health Halo" marketing to reveal the biological truth of a product. It exposes the corporate "Double Standard" where multinational brands use cheaper, hazardous ingredients like Palm Oil in India while using healthier alternatives abroad, and it decodes complex chemical additives (like Maltodextrin and INS stabilizers) into plain-language health warnings. By cross-referencing FSSAI safety data and news reports on dairy adulteration, the scanner transforms a confusing, fine-print nutrition label into a personalized Risk Profile, empowering consumers to see through "hidden sugars" and toxic preservatives that lead to chronic lifestyle diseases.

**Challenges we ran into**

Building the Healthify food scanner presented the formidable challenge of overcoming "Information Asymmetry" within a fragmented digital ecosystem, primarily due to the "Double Standard" Data Gap where global food APIs often provide inaccurate nutritional profiles for the Indian market. Technically, this required engineering a logic layer that prioritizes real-time OCR extraction over static database results to expose hidden "India-only" ingredients like Palm Oil and Maltodextrin. Furthermore, I had to solve the "Hardware-Software Friction" of implementing a high-performance, low-latency WebRTC camera feed within a single-file architecture, ensuring the AI could maintain focus on tiny, reflective ingredient lists while simultaneously cross-referencing extracted toxins against a personalized Medical Risk Engine for conditions like Diabetes and Hypertension.

Raunak Kumar

`2026-04-23`

---

### RuralHealth AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-early-disease-risk-prediction-and-rural-health-access-platform-4f00) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arijit-coder-newbie/Health-AI) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Early detection. Smarter decisions. Better rural

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Progressive Web Apps (PWA)](https://img.shields.io/badge/Progressive%20Web%20Apps%20(PWA)-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Rural and semi-urban healthcare workers often have limited access to digital tools for early disease-risk screening, while unreliable internet connectivity makes many cloud-dependent solutions difficult to use.

**RuralHealth AI** provides an AI-powered, offline-first platform that helps frontline health workers identify potential health risks from a patient's symptoms and vital signs before they become serious.

The platform can be used to:

* 🩺 Screen patients using symptoms, vitals, and health information.
* 🤖 Predict potential diseases using a machine-learning model.
* ⚠️ Classify patients into **Low, Moderate, or High risk** for easier prioritization.
* 💡 Provide explainable risk factors instead of only giving a prediction.
* 📱 Store patient records locally and continue working when there is no internet connection.
* 🔄 Synchronize queued patient data when connectivity is restored.
* 🌐 Support **English, Hindi, and Bengali** for better accessibility.
* 🎙️ Allow voice-based symptom input.
* 🏥 Help users find healthcare facilities and support teleconsultation.(Only demo teleconsultation)
* 📊 Give PHC/healthcare staff a dashboard to monitor patients and prioritize high-risk cases.

Instead of replacing doctors, RuralHealth AI acts as a **decision-support and early-screening tool**, helping frontline workers identify patients who may need professional medical attention sooner.

The overall workflow is:

**Symptoms & Vitals → AI Risk Assessment → Disease Prediction → Early Warning → Professional Evaluation**

**Challenges we ran into**

One of our biggest challenges was designing the system to work reliably in **low-connectivity environments**. A conventional cloud-dependent application would fail when a health worker loses internet access, so we had to make patient data entry and storage work locally and synchronize it later.

We addressed this by implementing an **offline-first architecture** using local browser storage. Patient records can be queued while offline and synchronized with the backend once connectivity becomes available.

Another challenge was integrating the **machine-learning model into the web application**. The ML model was developed using Python and Scikit-learn, while the frontend is built with React and TypeScript. We solved this by exposing the trained model through a **FastAPI backend**, allowing the frontend to send patient symptoms and receive predictions through an API.

We also had to deal with the complexity of presenting AI predictions in a healthcare context. Instead of showing only a disease prediction, we added a separate risk-assessment layer that provides **Low/Moderate/High risk levels and contributing factors**, making the output easier for frontline workers to understand.

Finally, designing the interface for rural users required us to consider **multilingual interaction, voice input, simple workflows, and limited connectivity** rather than assuming users would always have a high-speed internet connection or advanced technical knowledge.

Team **dev.Phoenix** -- [Pratik Roy](https://github.com/pratikroy2005), [PRIYAM MONDAL](https://github.com/Priyam-07-thala/), [Arijit Chakraborty](https://github.com/Arijit-coder-newbie)

`2026-08-30`

---

### HealthCart
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthcart-eace) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ViltrumEmpire/HealthCart) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/AjgDdTsbK_Y) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Say what hurts. We'll handle the rest.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square)

**The problem it solves**

Getting sick in India today means juggling three separate apps and a dozen decisions: finding a doctor and booking a slot, remembering what to say, then — once you have a prescription finding a pharmacy, checking stock, and paying, often while unwell, in pain, or looking after someone who is.

HealthCart collapses that into one plain-language request. Tell it what's wrong "I have a fever and body ache, book me a doctor and order whatever they prescribe," and it:

Finds and books an appropriate doctor appointment based on the symptoms described, no manual searching through specialties or clinic listings.
Reads the resulting prescription and finds the prescribed medicines from nearby/available vendors.
Completes the purchase autonomously, using Prava's tokenized, per-transaction payment flow; each purchase is scoped to a specific amount and merchant, approved by the user via biometric passkey, so the agent never holds a persistent card or an unbounded ability to spend.

Who this helps, and how:

People who are actually unwell the moments this matters most are exactly when navigating five different apps is hardest. One request replaces the whole chain.
Elderly users or caregivers managing someone else's care, where the appointment-booking + medicine-ordering flow is often the most friction-heavy part of a health scare.
Anyone in a location without easy access to nearby clinics/pharmacy info with location auto-detection when it isn't specified; the agent fills in context the user might not think (or be well enough) to provide.

Why it's safer, not just faster:
Because Prava scopes every payment to a specific transaction with user-set spending caps and biometric approval, the user retains a hard checkpoint over every purchase the agent makes; the convenience of "book it and get my meds" doesn't come at the cost of handing an AI agent open-ended access to a card.

**Challenges we ran into**

1. Prava sandbox authentication kept failing silently

Early on, every session-creation call to the Prava sandbox returned a 401 with no obvious reason in the request itself; the payload looked correct, and the endpoint was correct. After digging into the auth headers, it turned out we were pointing at a stale/incorrect secret key rather than the current sandbox key. Once we swapped in the correct key, session creation returned a clean 201, and the polling loop for session status worked end-to-end against the sandbox API on the first real attempt.

Lesson: when a payments API returns a generic 401, verify the credential itself before assuming the request shape is wrong; we lost time debugging the payload when the fix was one key swap.

2. Visa Payment Passkey enrollment breaking on localhost

When we got to wiring up the passkey approval step, enrollment kept failing during local development. The root cause was WebAuthn's secure-context requirement: passkeys need HTTPS, and while localhost itself is exempted, subtle mismatches (wrong RP ID/origin, or accidentally testing via a LAN IP instead of the literal localhost) broke the flow in ways that weren't obvious from the browser's error alone.

We worked through it methodically:

Ruled out the localhost vs 127.0.0.1 distinction first, since that's the most common cause.
Checked our session config against Prava's documented origin/redirect-URI requirements.
When that still didn't fully resolve it under time pressure, we routed local dev traffic through an HTTPS tunnel (Cloudflare), so the whole secure-context question became moot: no more debugging localhost edge cases, just a real HTTPS origin end to end.

Lesson: for anything biometric/WebAuthn-based, don't assume "it's probably a dev-environment quirk"; trace the actual origin and RP ID being used at the moment the browser throws, rather than guessing from the symptom.

Team **Viltrumites** -- [BankimChandra Das](https://github.com/Bankim2410), [PUSHKAR SHINDE](https://github.com/PushkarShinde), [SHUBHRAJYOTI MOHANTY](https://github.com/Shubhrajyoti65)

`2026-08-03`

---

### ClinIQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cliniq-78d4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vedanthk-engr/CliniQ_Plus) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://clini-q-plus.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI Diagnostics & Clinical Intelligence

![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square)

**Challenges we ran into**

Building ClinIQ+ was technically ambitious across multiple dimensions simultaneously and produced several genuine engineering challenges that required non-trivial solutions.
Challenge 1:  Streaming multimodal responses without breaking structured data extraction
The platform relies on Gemini 2.5 Flash for both streaming narrative output (the AI explanations physicians read in real time) and structured JSON extraction (the clinical data that populates charts, risk scores, and forecasts). These two requirements are fundamentally in tension streaming works beautifully for prose but produces malformed JSON when the response is interrupted mid-token. Our initial implementation broke the forecast visualization every time the SSE stream was interrupted by network latency, because a half-delivered JSON object would be passed to the parser and crash the component.
We solved this by implementing a dual-mode response architecture. For structured data endpoints, we send the full Gemini request with explicit JSON-only instructions and a schema, buffer the complete response server-side before returning it, and validate it against a Pydantic model before sending to the frontend. For narrative endpoints, we stream freely via SSE. The two modes never mix in the same request. This added latency to the structured endpoints but made the system reliable. We also added a JSON repair utility on the frontend that catches and attempts to patch common truncation errors as a last-resort fallback.
Challenge 2:  Personal baseline anomaly detection without historical data on new patients
The core clinical insight behind our alert system is that anomalies should be measured against a patient's personal history, not population averages. A creatinine jump from 0.9 to 1.1 is clinically significant for that specific patient even though 1.1 is within normal range. However, new patients have no historical baseline they have one uploaded document. Comparing a single data point against itself produces meaningless alerts or no alerts at all.
We solved this with a tiered anomaly detection system. For patients with fewer than three historical data points, the system falls back to population-level reference ranges with a visible disclaimer that baseline is still being established. For patients with three to eight data points, we use a lightweight statistical model  mean plus two standard deviations  to set the personal threshold. For patients with more than eight data points, we apply a rolling window z-score calculation that weights recent readings more heavily than older ones. We also prompt Gemini with the available history and ask it to reason about whether a value is anomalous in context, using clinical knowledge to compensate for thin statistical data. The result is a system that is useful from the first document upload and becomes progressively more accurate as data accumulates.
Challenge 3:  Multilingual voice command interpretation in a clinical context
Supporting voice input across eight Indian languages sounds straightforward with Google Cloud Speech-to-Text, but the clinical domain created unexpected complexity. Medical terminology behaves very differently across languages. Patients in Tamil Nadu refer to blood glucose as "sugar" and blood pressure as "pressure"  both of which are too ambiguous for a direct clinical mapping without context. Drug names are almost universally known by brand names (Crocin, Glycomet, Ecosprin) rather than generic names (Paracetamol, Metformin, Aspirin), which are what the clinical database stores. Regional pronunciation variations for English medical terms caused consistent STT misrecognition even with the medical dictation model enabled.
We built a three-layer normalization pipeline that runs on every voice transcript before it reaches Gemini. The first layer maps the top 200 Indian brand names to their generic equivalents. The second layer maps regional colloquial health terms to their clinical equivalents across Hindi, Tamil, and Telugu. The third layer sends the normalized transcript to Gemini with a clinical context prompt that resolves remaining ambiguity using the patient's known conditions and medications as grounding context. This reduced voice command misinterpretation from an unacceptable rate during early testing to a reliable experience across all supported languages.
Challenge 4:  D3 force graph performance with real-time data updates
The comorbidity web is a D3 force-directed graph that needs to update in real time as new patient data arrives and as the physician clicks nodes to explore interactions. Early implementations caused the graph to completely re-render and re-run the physics simulation on every data update, producing a jarring visual snap that made the feature feel broken rather than dynamic. With patients who had seven or more active conditions, the simulation also took several seconds to stabilize on initial load, during which the graph was visually chaotic.

**The problem it solves**

Healthcare is reactive by design. Physicians see 40-60 patients daily with no system that connects the dots across years of fragmented lab reports, discharge summaries, medications, and wearable data. Critical deterioration goes undetected until it becomes an emergency.
ClinIQ+ fixes this by giving any physician, including a general practitioner in a district with no specialist access, the ability to upload any clinical document and instantly receive a structured patient profile, a 12-month risk forecast, real-time drug interaction checks, anomaly alerts measured against the patient's personal baseline (not population averages), and diagnostic hypothesis validation. All streamed in real time. All explainable. All in under 10 seconds per document.
It makes patient onboarding, longitudinal monitoring, medication safety review, clinical documentation, and specialist-grade risk forecasting faster, safer, and accessible to every physician regardless of their infrastructure.

[Vedanth K](https://github.com/vedanthk-engr)

`2026-06-23`

---

### AI-Based Code Error Diagnosis Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-code-analysis-and-root-cause-diagnosis-system-f38c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jshardul26/AI_BUG_SIMULATOR) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-bug-simulator.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ze3tKat5gzg) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Analyse. Diagnose. Learn. Improve.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

Modern developers spend a significant amount of time searching through documentation, forums, and AI chatbots just to understand compiler errors and runtime exceptions. While existing tools often identify the error, they rarely explain why it happened , how to fix it, and how to prevent it in the future , especially for beginners.

Our AI-Powered Code Analysis and Root Cause Diagnosis System transforms raw error messages into structured learning experiences. Developers can submit their source code along with error logs, and the system automatically performs static analysis to identify the underlying issue rather than only reporting the surface-level exception.

The platform provides:

Root Cause Analysis that explains why the error occurred.
Beginner-Friendly Explanations using simple language and real-world analogies.
Corrected Code Suggestions with highlighted fixes.
Execution Flow Visualization to show how the program reached the failure point.
Interactive Flowcharts that simplify debugging logic.
AI-Generated Flashcards and Quizzes to reinforce learning after fixing the bug.

By combining debugging assistance with educational content, the platform helps students, beginners, and developers resolve issues faster while improving their understanding of programming concepts instead of simply copying solutions.

**Challenges we ran into**

One of our biggest challenges was moving beyond simple error detection to accurate root cause analysis. Compiler and runtime error messages often describe the symptom of a problem rather than its actual cause, making it difficult to generate meaningful explanations automatically.

Another challenge was integrating multiple AI-powered features—including code analysis, beginner-friendly explanations, corrected code generation, execution visualization, flowchart creation, and learning content—into a single seamless workflow while keeping response times low.

We also faced issues with backend configuration, API integration, and deployment. Ensuring consistent AI responses across different programming languages and error types required several iterations of prompt refinement and testing with diverse error logs.

To overcome these challenges, we designed a modular backend architecture, optimized API requests, and thoroughly tested the system using a wide range of real-world programming errors. This iterative approach resulted in a stable platform capable of delivering accurate, educational, and actionable debugging assistance.

Team **DevSync** -- [Sanvi Ingle](https://github.com/Sanvi028), Siddharth Jagtap, Shardul Jadhav, Anushka Jagtap, [Diksha Jadhav](https://github.com/Diksh-jadhav)

`2026-07-30`

---

### medkit
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medikit-b727) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lakshaychhabra5400-cpu.github.io/medikit/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Smart Medicine Tracking & Healthcare Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Healthcare is becoming increasingly digital, yet millions of people still face difficulties in managing their daily medicines. People often forget their medication schedule, struggle to find medicines at affordable prices.

MedKit is designed to solve these challenges by combining medicine tracking, reminders, pharmacy comparison.

Medication management remains a major challenge for many individuals, especially elderly patients and people with chronic illnesses.

Common problems include:
• Forgetting to take medicines on time.
• Difficulty locating nearby pharmacies.
• Managing multiple medicines becomes confusing

MedKit provides an integrated healthcare platform that enables users to:
• Track medicine schedules.
• Receive smart reminders.
• Compare medicine pharmacies.
• Order medicines from nearby stores.
• Maintain a digital medicine history.

**Challenges we ran into**

## Challenges Faced During Development

- Debugged a backend crash in the prescription-scanner module traced to a case-sensitive filename mismatch, which failed silently at server startup and surfaced only as a generic network error on the frontend — requiring root-cause tracing rather than surface-level fixes.

- Resolved environment and dependency conflicts (Python version compatibility, NumPy–PyTorch ABI mismatch, and an OCR library formatting bug) that caused intermittent failures during prescription processing.

- Identified and fixed false-positive matches in the medicine-detection logic, where noisy input was incorrectly matched to real medicine names — an important fix given the healthcare context, where a wrong-but-confident result is worse than no result.

- Added a manual medicine-search fallback for cases where handwritten prescriptions defeat automatic text recognition, so the feature degrades gracefully instead of failing silently.
- Debugged an "Invalid email or password" login failure on the main MedKit application using network-level inspection, isolating it to a single account's credential mismatch rather than a systemic auth bug — confirmed by successfully registering and logging into a fresh test account.

- Encountered frontend module-loading failures (500 errors across core layout/page components causing a blank screen) on MedKit, which is still under active investigation.

- Noted an acknowledged gap where several frontend pages currently rely on mock data rather than full backend integration — a known scope gap rather than a defect.

- Resolved merge conflicts encountered while integrating independently developed features back into the main MedKit repository, requiring careful reconciliation to avoid overwriting teammates' concurrent changes.

- Followed a modular development approach, building and testing new features independently before integration to minimize risk to the main codebase.

Team **Web Wizards** -- Rishabh Kumar, Ronak Singh, AARYAN SOLANKI, Shouryaaa Vig, Krish Bansal, Lakshay Chhabra

`2026-07-30`

---

### LumosHealth
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lumoshealth-4138) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sandipan003/LumosHealth) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/oehOsdozT0A) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Contactless vitals tracking via AI

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

### Challenges we ran into

Building a magical, real-time healthcare application meant pushing the boundaries of web browsers, which naturally introduced some formidable technical hurdles. Here are the biggest challenges we faced and how we solved them:

#### 1. The Vercel Serverless WebSocket Restriction
**The Hurdle:** Our core feature—the Prophecy Orb—relies on streaming 30 FPS webcam video frames via a persistent **WebSocket** connection to our Node.js backend to extract vital signs using optical rPPG. However, when we deployed our frontend to Vercel, we quickly realized that Vercel's serverless architecture strictly terminates long-lived WebSocket connections, completely breaking our face scanner.
**The Solution:** We adopted a hybrid deployment strategy. We kept our gorgeous Vite/React frontend on Vercel for lightning-fast global CDN delivery, but decoupled the heavy biometric processing into a dedicated, stateful Node/Express server. For live demonstrations, we utilized **Localtunnel** to instantly expose our local hardware to the internet, giving Vercel a secure endpoint to stream frames to without dropping the connection.

#### 2. Battling "Mixed Content" Browser Security
**The Hurdle:** While trying to connect our Vercel-hosted frontend (`https://`) to our local WebSocket server (`http://localhost` and `ws://localhost`), modern browsers like Chrome aggressively blocked the connection due to strict "Mixed Content" security policies.
**The Solution:** We engineered a dynamic proxy pipeline using `import.meta.env` variables in Vite to dynamically rewrite all fetch and socket requests at runtime. By routing the local server through an encrypted HTTPS tunnel proxy, we completely bypassed the browser's security blocks, allowing seamless handshakes between the cloud frontend and the local biometric engine.

#### 3. AI Rate Limits & Event Loop Freezes
**The Hurdle:** For the "Ancient Scrolls" feature, we integrated Google's **Gemini Vision AI** to OCR and analyze complex medical lab reports. However, while testing large image payloads, we hit a hard API rate limit (429 Quota Exceeded). Unexpectedly, the AI SDK didn't throw an error—it silently hung the entire Node.js event loop, freezing the application.
**The Solution:** We architected a robust failsafe around the AI engine. We wrapped the Gemini API invocations inside a strict `Promise.race()` timeout handler. If the API rate limits or stalls, our backend catches the timeout gracefully and seamlessly falls back to a mocked, local inference response. This ensures the user experience remains fast, magical, and entirely uninterrupted during demonstrations.

#### 4. React Stale Closures and Asynchronous Desyncs
**The Hurdle:** We encountered a highly frustrating bug where users were not being awarded their "House Points" after successfully completing a 45-second facial scan.
**The Solution:** Deep debugging revealed that the issue stemmed from complex asynchronous state management inside React. The WebSocket's `onclose` event handler was competing with a `useEffect` countdown timer, causing a "stale closure" that effectively swallowed the completion trigger. We re-engineered the component lifecycle, ensuring explicit tear-downs of the websocket connection and explicitly triggering our `award-points` API the exact millisecond the countdown resolves. We also added database-level safety checks to ensure legacy user accounts could safely receive points without crashing the backend schema.

**The problem it solves**

### The Problem it Solves

Navigating personal health and medical data is often an incredibly stressful, tedious, and confusing experience for the average person. We built **Lumos Health** to solve three major pain points in the modern healthcare experience:

#### 1. The Friction of Tracking Vital Signs
**The Problem:** Keeping track of daily vitals like Heart Rate (HR), Respiratory Rate, and Stress Levels usually requires expensive smartwatches, wearable straps, or bulky medical equipment. People simply forget or cannot afford to track them consistently.
**The Lumos Health Solution:** We completely removed the friction. Using cutting-edge **optical rPPG (Remote Photoplethysmography)** technology, Lumos Health allows users to extract highly accurate vital signs in real-time just by looking into their device's webcam or phone camera. It’s entirely contactless, requires zero extra hardware, and takes only 45 seconds. Tracking your health is now as simple as taking a selfie.

#### 2. The Confusion of Medical Jargon
**The Problem:** When patients receive lab results or medical reports from a clinic, they are typically confronted with pages of confusing acronyms (like *LDL, HDL, HbA1c*) and reference ranges that require a medical degree to decipher. This leads to severe anxiety and reliance on confusing Google searches.
**The Lumos Health Solution:** We integrated an **AI-powered Medical Report Analyzer** driven by Google's Gemini Vision AI. Users simply drag and drop an image of their blood work or clinical report. The AI instantly reads the document, extracts the key lab markers, color-codes them (Normal/High/Critical), and provides a plain-English, jargon-free executive summary. It even generates suggested questions to ask your doctor, empowering patients to have informed, confident discussions during their next appointment.

#### 3. Lack of Engagement and Adherence
**The Problem:** Preventative healthcare is boring. Traditional health apps feel clinical, sterile, and feel like a chore to use, leading to high user drop-off rates.
**The Lumos Health Solution:** We transformed personal health into an enchanting experience by fully gamifying it within a rich, immersive Harry Potter-inspired wizarding world UI. Users are rewarded with **House Points** for completing scans and taking care of themselves. By replacing sterile data charts with magical "Prophecy Orbs," "Ancient Scrolls," and "Apothecary" storefronts, we turn routine health monitoring into an engaging habit that users actively look forward to. 

**Ultimately, Lumos Health democratizes personal healthcare by making biometric tracking contactless (safer), medical data comprehensible (easier), and preventative health maintenance genuinely fun.**

**Healthcare**

### How Lumos Health fits into the Healthcare track

Lumos Health fits perfectly into the Healthcare track because it actively democratizes preventative care and personal health monitoring. By leveraging cutting-edge optical rPPG technology for contactless biometric scanning and Google's Gemini Vision AI for medical document OCR, we've built a platform that eliminates the two biggest barriers to patient health: hardware costs and clinical confusion. 

Instead of requiring expensive wearables to track vitals or a medical degree to understand lab results, Lumos Health allows anyone with a standard webcam to instantly extract clinical-grade health metrics and decipher complex medical reports. Furthermore, by wrapping these advanced healthcare utilities in a highly engaging, gamified wizarding-world interface, we tackle the chronic issue of patient non-adherence, transforming routine health tracking from a tedious chore into an enchanting daily habit.

Team **digitong** -- [Sayani Das](https://github.com/codewithsayani), [SANDIPAN SARKAR](https://github.com/Sandipan003), [Saumojit Roy](https://github.com/mimozing3003), [Satyajit Pratihar](https://github.com/Satya007s007)

`2026-07-26`

---

### CARECHAIN
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carechain-034c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/swa-design/CareChain.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/TlICM3i1wI8) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Symptom Translator and Health Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

Millions of Indians ignore or misinterpret early warning signs of illness because they cannot accurately understand, track, or communicate their symptoms. Elderly individuals, rural populations, and low-literacy users often struggle with medical terminology, language barriers, and complex healthcare applications. As a result, symptoms that could have been identified and managed early frequently progress into serious health conditions requiring costly treatment. 
  Current digital health solutions are largely reactive, text-heavy, and designed for digitally literate users, making them inaccessible to a significant portion of the population. There is a critical need for an intuitive, multilingual, voice-first health companion that enables users to describe symptoms naturally, understand potential health risks in simple language, monitor chronic conditions continuously, and receive timely guidance for seeking appropriate care—empowering individuals to make informed health decisions before conditions worsen.

**Challenges we ran into**

One of our biggest challenges was translating our ideas into a functional prototype using AI-assisted development tools within a limited timeframe. While AI helped accelerate development, we still had to carefully refine prompts, validate outputs, connect different features, and ensure the application aligned with our vision. Balancing rapid prototyping with usability and consistency across the app was a key learning experience throughout the hackathon

Team **Code crafters** -- MATHIOLI BHARATHI, Swashiga RJD, Muthu Sahana, Bhavana Sreeram

`2026-06-14`

---

### AgentRX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentrx-5f3b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gauravnetes/AgentRX.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1r5eDzan2hGJ99MUmQvLfUEXF2Z5yFZbw/view?usp=drivesdk) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ObaVUK74-nI) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Drugs should be repurposed

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![LLM](https://img.shields.io/badge/LLM-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square)

**The problem it solves**

The Core Issue: The "Garbage In, Garbage Out" Trap in Drug Repurposing
Traditional pharmaceutical drug repurposing relies heavily on manual literature reviews, which are slow, prone to human confirmation bias, and often disconnected from real-world commercial viability. On the other hand, naive AI wrappers attempting to automate this process suffer from severe "Goal Fixation" and "Negation Blindness"—they will frequently misinterpret a drug's highly toxic side effect as a miracle cure simply because the biological pathways overlap in the literature. Furthermore, discovering a biological link is useless if the molecule is blocked by active patents or lacks a defensible Total Addressable Market (TAM).

The AgentRX Solution: Deterministic Multi-Agent Intelligence
AgentRX is a fully autonomous, Machine-to-Machine (M2M) orchestrator designed to eliminate bias and accelerate Phase 1 discovery. It transforms raw medical literature into VC-grade, risk-adjusted commercial business plans in under 60 seconds.

It solves the repurposing bottleneck by executing a rigorous, 6-agent pipeline:

Unbiased Discovery: Dynamically scrapes the PubMed Entrez API to establish a neutral literature baseline.

Dual-Track Biological Reasoning: Extracts biomedical relationships using NLP, strictly separating therapeutic efficacy (TREATS, PROTECTIVE) from toxicity risks (WORSENS, ADVERSE_EFFECT).

Live IP Whitespace Matrix: Automatically queries Europe PMC to ensure Freedom-to-Operate (FTO) and filters out candidates with active blocking patents.

Risk-Adjusted Commercial Modeling: Calculates a proxy TAM using epidemiological data and recommends 505(b)(2) novel formulation strategies if a generic molecule presents systemic toxicity or is already standard-of-care.

Automated Synthesis: Renders a comprehensive, mathematically grounded PDF intelligence report complete with risk/reward scatter plots and PubChem pharmacological profiles.

**Challenges we ran into**

Building an enterprise-grade multi-agent system meant fighting the core nature of Large Language Models—their tendency to please, hallucinate, and connect dots that shouldn't be connected.

1. The "Evil Corp" Bug (Confirmation Bias)

The Challenge: Initially, the Web Intelligence Agent was instructed to "find repurposing candidates." Because of Goal Fixation, the LLM twisted negative data to satisfy the prompt. If it read that a drug caused dementia, it would aggressively pitch dementia as a $100 Billion target indication. It was acting like a hyped-up hype salesman rather than a cynical scientist.

The Overcome: I engineered a "Dual-Track Intelligence" architecture. I split the pipeline into two phases: an objective literature review, followed by strategic extraction. I forced the LLM to classify every relationship into one of 9 strict categories (e.g., TREATS vs. CAUSES). I then built a deterministic Python "Vacuum Guardrail" that violently quarantines any candidate flagged with an adverse effect, completely stripping the LLM's ability to commercialize toxic side effects.

2. LLM Anchoring Bias & "Lazy Math"

The Challenge: When asked to generate a floating-point "Pathway Overlap Score" for multiple diseases, the LLM (Llama-3.3-70B) exhibited severe anchoring bias. To save compute power, it lazily copy-pasted 0.85 for every single indication in the JSON array, regardless of whether it was a proven cure or a loose correlation.

The Overcome: I realized you cannot trust an LLM to do qualitative math. I stripped the LLM of its scoring authority, restricting it purely to NLP Boolean fact extraction (e.g., "Is there in-vivo evidence?"). Once the LLM returns the Boolean flags, a hardcoded Python deterministic scoring engine calculates the final Efficacy and Toxicity Penalty scores. This enabled the accurate mapping of the Risk/Reward scatter plots.

3. API Bloat and Pipeline Latency

The Challenge: I initially relied on the ClinicalTrials.gov API to determine trial complexity, but the rigid JSON structures required complex parsing and slowed down the pipeline execution time.

The Overcome: I recognized that massive language models already contain FDA approval histories and standard-of-care guidelines in their internal weights. By deprecating the rigid external API and relying on advanced prompt constraints for clinical saturation (e.g., detecting if a drug is already prescribed off-label), I shaved seconds off the execution time while making the commercial recommendations significantly smarter.

**BEST INNOVATIVE IDEA**

AgentRX fits perfectly into the Best Innovative Idea track because we didn’t just build another "ChatGPT wrapper"—we engineered a fundamental architectural breakthrough in how Large Language Models are applied to high-stakes quantitative bioinformatics.

Currently, applying generative AI to pharmaceutical drug repurposing is dangerous. LLMs suffer from "Negation Blindness" and "Confirmation Bias." If prompted to find a repurposing candidate, standard AI models will lazily hallucinate highly toxic side effects (like dementia or internal bleeding) as "miracle cures" simply because the biological pathways overlap in the medical literature.

Our Core Innovation:
We completely re-architected the AI pipeline to solve this. We built a 6-Agent Machine-to-Machine (M2M) orchestrator that explicitly strips the LLM of its ability to "guess" or do math, restricting it to what it does best: NLP parsing.

Dual-Track Deterministic Scoring: Instead of asking the AI to guess a "confidence score," we restrict the LLM purely to NLP Relationship Extraction (classifying a drug's effect into 9 strict biomedical categories like TREATS, CAUSES, or ADVERSE_EFFECT). A hardcoded Python engine then deterministically calculates the Pathway Efficacy and Toxicity Penalty scores, permanently eliminating LLM anchoring bias.

The Vacuum Guardrail (Anti-Hallucination): We invented a programmatic quarantine system. If the Web Intelligence Agent extracts toxic side effects, our Python guardrail physically blocks those candidates from entering the commercial pipeline, preventing the AI from generating a business plan around a poison.

Dynamic Commercial Pivoting: AgentRX doesn't stop at biology. It autonomously queries Europe PMC for active patent blocking (FTO clearance) and PubChem for chemical physics. If a molecule is generic or highly toxic systemically, our Commercial Viability Agent dynamically pivots its VC thesis to recommend a 505(b)(2) novel formulation strategy (e.g., a targeted transdermal patch) to build a patentable moat.

AgentRX is an innovative leap because it proves that true enterprise AI isn't about using a smarter model—it’s about building deterministic, quantitative guardrails that force the machine to act like a cynical scientist and a ruthless VC, rather than a text generator.

Team **Asynchronous** -- [Swarnava Chakraborty](https://github.com/SuniKhuni), [Souvik Rahut](https://github.com/S-o-b-u), [Gourav Chandra](https://github.com/gauravnetes), [NILADRI SAHA](https://github.com/niladriaiml12-web)

`2026-05-09`

---

### echoaid(Health Tech)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/echoaidhealth-tech-d851) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ritikkumar-07/echoaid) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Healthcare, When You Need It Most.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Multilingual voice recognition: Users may speak different Indian languages and accents, making accurate speech-to-text and symptom understanding challenging.
AI triage accuracy: Converting unstructured user symptoms into a meaningful urgency level while avoiding misleading medical advice required careful prompt design and validation.
Poor/rural network connectivity: The application needs to remain useful even with slow or unstable internet connections, especially for first-aid and emergency situations.

Real-time location & availability: Finding nearby hospitals, clinics and blood banks and providing useful routing information can be challenging when location or availability data is incomplete.

Emergency reliability: SOS actions and critical information need to work quickly and reliably, even under stressful conditions.

**The problem it solves**

In rural and semi-urban areas of India, people often struggle to access timely and reliable healthcare, especially during emergencies. Language barriers, low health literacy, poor connectivity, and lack of awareness about nearby hospitals, clinics, blood banks, and basic first-aid can cause critical delays.

Existing healthcare apps often require users to search through multiple screens or type their symptoms, which is difficult during stressful situations.

Sanjeevani solves this problem by providing a voice-first AI health companion that enables users to describe their symptoms in their preferred language and quickly receive AI-assisted triage, basic first-aid guidance, nearby healthcare facility information, and emergency SOS assistance — all through a simple, unified flow.

In short: It reduces the gap between “I need medical help” and “I know what to do next.”

Team **Synapse** -- [Rudro Chakraborty](https://github.com/RUDRO-PRO), Sohan Das, [Sourav Karmakar](https://github.com/karmakarsourav2006-dev), [Ritik Kumar](https://github.com/hritikkrgupta7746-ui)

`2026-08-30`

---

### ApnaSehat
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/apnasehat-fb5c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://apnasehat.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Health, Always in One Thread

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

**Problems We Ran Into**

**1. Village & Offline Integration**

Ensuring APNASEHAT can function effectively in villages with limited or no internet connectivity.



**2. Language Barriers**

Supporting the different regional languages spoken by users in rural areas.



**3. OCR Recognition**

Difficulty in accurately recognizing and extracting information from medical documents/images using OCR.



**4. Accessibility for Uneducated Users**

Designing the app so that users with little or no literacy can still navigate and use it easily.



**5. AI API Limitations**

Handling situations where the Groq API reaches its usage limit, requiring a reliable fallback mechanism for Ask ApnaSehat.



**6. Admin Access & Document Registration**

Determining who will log in as an admin and register/upload patient documents when the patient is unable to do so themselves.



**7. Emergency QR Reliability**

Ensuring the Emergency QR code works reliably and can provide the required patient information when needed.

**The problem it solves**

**Problems It Solves**

**1. Scattered Health Records**
Provides a centralised system where patients and authorised healthcare professionals can access health records in one place.


**2. Difficulty Understanding Medical History**
Uses AI to summarise medical records into simple, meaningful information, making a patient’s health history easier to understand.


**3. Uncertainty About Medical Care**
AI can provide initial guidance on when medical attention may be needed and when a doctor should be consulted, without replacing professional medical advice.


**4. Lack of a Complete Health History**
Keeps the patient’s full health history, reports, prescriptions, and medical documents together in one secure platform.


**5. Difficulty Maintaining Records During Illness**
Allows manual uploading and updating of health details/documents, so important information can be recorded even when the patient is feeling unwell or unable to visit a healthcare facility immediately.


**6. Privacy & Security Concerns**
Keeps sensitive health information secure and accessible only to authorised users.

Team **The Hackatsuki** -- [Mehul Singh](https://github.com/Mehhhhull), [Jashwant Singh](https://github.com/jashwantkrsingh), [Ankit Tiwari](https://github.com/Ankit-05-code), [Sayantani Manna](https://github.com/sayantaniy)

`2026-08-30`

---

### Automated health insurance claim system
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/automated-health-insurance-registration-claim-c5f9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Madhan2007/PEC.git) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> #n8n

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-333333?style=flat-square)

**Challenges we ran into**

Challenges We Ran Into
Data Integration: Connecting different healthcare data sources and maintaining consistent patient and claim information was challenging.
Medical Document OCR: Extracting accurate information from low-quality, handwritten, or differently formatted medical documents required additional preprocessing.
Fraud Detection: Designing reliable rules to identify suspicious claims without generating too many false positives was difficult.
API Integration: Integrating services such as Twilio, Firestore, DigiLocker/ABHA, and n8n required handling different APIs, formats, and authentication methods.
Large Data Processing: Processing multiple documents and claims efficiently while maintaining system performance was challenging.
Real-Time Notifications: Managing WhatsApp, SMS, and Email notifications while handling API rate limits and delivery failures required careful workflow design.
Data Privacy & Security: Healthcare and insurance data required secure handling, access control, and proper audit tracking.
System Integration: Connecting the frontend, Django backend, OCR, fraud engine, database, and automation workflow into one seamless system was a major integration challenge.

**The problem it solves**

# 🏥 Pre-Existing Condition (PEC) & Health Insurance Claim Adjudication Platform
> **Problem Analysis, Solution Architecture & Impact Report**

---

## 1. Executive Summary

Health insurance claims processing today is hindered by **fragmented data**, **manual document verification**, **high fraud vulnerability**, and **lengthy reimbursement cycles** (often taking 15–45 days). One of the most contentious friction points is the non-disclosure, misrepresentation, or erroneous verification of **Pre-Existing Conditions (PECs)**.

The **PEC Claim Intelligence Platform** is an end-to-end, AI-powered adjudication and fraud prevention ecosystem designed to bridge the trust gap between **Patients**, **Hospitals**, and **Insurance Providers**.

```
      Traditional Workflow                         PEC Platform Workflow
┌──────────────────────────────┐              ┌──────────────────────────────┐
│  • Manual paper bill review  │              │  • Real-time OCR extraction  │
│  • Undetected fake receipts  │  ─────────►  │  • Multi-factor Fraud Radar  │
│  • Weeks of waiting time     │              │  • Instant claim tracking    │
│  • Fragmented medical history│              │  • DigiLocker / ABHA audit   │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## 2. Core Problems Addressed

### 🔴 Problem 1: Unintentional & Fraudulent PEC Non-Disclosure
* **Industry Pain Point:** Insurers lose billions annually to non-disclosed pre-existing chronic conditions. Conversely, honest policyholders frequently suffer from unfair claim repudiations due to ambiguous past medical history documentation.
* **Our Solution:** Automated cross-referencing between policy inception dates, DigiLocker medical records, ABHA (Ayushman Bharat Digital Mission) logs, and hospital admission diagnoses to verify PEC disclosure objectively without bias.

### 🔴 Problem 2: Labor-Intensive, Slow Document Verification
* **Industry Pain Point:** Claims adjusters and TPAs spend countless hours manually reading doctor prescriptions, itemized pharmacy bills, diagnostic reports, and discharge summaries.
* **Our Solution:** An **Intelligent Medical OCR Engine** that parses document images and PDFs, automatically extracting bill items, diagnostic codes, patient identifiers, and total costs in milliseconds.

### 🔴 Problem 3: Insurance Fraud, Billing Inflation & Phantom Claims
* **Industry Pain Point:** Common fraud schemes include billing for unperformed lab tests, inflated room rents exceeding policy limits, duplicate bill submissions, and altered invoice dates.
* **Our Solution:** An automated **Rule & ML-based Fraud Radar Engine** that scores claims against:
  - Discrepancies between claimed amount vs. OCR-extracted bill totals.
  - Exorbitant billing anomalies against standard procedure benchmarks.
  - Date and timeline inconsistencies (e.g., discharge date before admission date).
  - High-risk hospital tagging and duplicate receipt detection.

### 🔴 Problem 4: Opaque Claim Status & Trust Deficit
* **Industry Pain Point:** Policyholders are left in the dark regarding why a claim is under review, pending, or rejected, leading to customer disputes and litigation.
* **Our Solution:** Real-time visibility into claim stages, automated transparent decision logs, and cryptographically verified ledger audits for every claim state transition.

---

## 3. User Roles & Use Cases

| User Role | What They Use It For | Key Benefits & Capabilities |
| :--- | :--- | :--- |
| 🧑‍💼 **Policyholders & Patients** | Submit cashless & reimbursement claims from home | • 3-step intuitive Claim Submission Wizard.<br>• Instant document scanning with auto-fill.<br>• Real-time claim status & deduction breakdowns.<br>• Direct DigiLocker document sync. |
| 🏥 **Hospitals & Providers** | Initiate pre-authorizations & submit IPD/OPD bills | • Batch document uploading for discharge summaries.<br>• Live policy eligibility and coverage validation.<br>• Faster settlement turnaround without endless back-and-forth emails. |
| 🛡️ **Insurance Underwriters & TPA** | Adjudicate, audit, and approve/reject claims | • Centralized claim queue with intelligent triage.<br>• Fraud Radar scoring (0–100%) with explainable risk flags.<br>• One-click side-by-side comparison of claimed vs. verified amounts.<br>• Policy limit auto-capping and co-pay calculations. |
| ⚙️ **System Administrators** | System health, audit compliance & ML monitoring | • Global platform metrics and settlement performance.<br>• Immutable audit trails and fraud label synchronization.<br>• REST API explorer and integration controls. |

---

## 4. How It Makes Existing Tasks Easier, Safer, and Faster

### ⚡ 1. 10x Faster Turnaround Time (TAT)
Instead of waiting 2–3 weeks for third-party administrators (TPAs) to manually enter bill data, the built-in OCR automatically digitizes bills and populates claim line items instantly upon document upload.

### 🔒 2. Safer & Verifiable Adjudication (Audit Tr

**Best Use of n8n**

n8n Notification Workflow

The PEC project uses n8n to automate notifications through WhatsApp, SMS, and Email.

The workflow starts with a Webhook that receives recipient details from the PEC backend. The data is parsed and divided based on the communication channel.

WhatsApp: Recipients are processed in batches of 20, messages are personalized, and sent through Twilio.
SMS: Recipients are processed in batches of 50, personalized messages with an opt-out line are sent through Twilio.
Email: Notifications are sent through the email service.
Status Handling: Each message is checked for success or failure and logged accordingly.
Firestore: SMS notification results are stored for tracking and reporting.
Rate Limiting: Wait nodes control the sending speed and prevent API overload.
Webhook Response: The final success or error response is returned to the PEC backend.

Overall: The workflow provides a centralized, automated, and scalable notification system for the PEC project.

**Best Use of Actian Vector Database**

Actian VectorAI DB is a relevant and important part of this project because it replaces the previous vector store layer and is integrated into the retrieval flow for semantic search. The preview/UI work is also relevant since it provides a simple testing interface to validate query behavior and confirm the backend is responding correctly. In addition, the LLM integration is a core part of the system, as the final answer is generated after retrieval using the contextual data from the vector search and the model provider configured for generation.

The project currently shows strong progress in architecture and integration, with the vector database, API layer, ingestion support, and LLM generation path all connected. However, the latest verification showed that the API was not fully running because port 8000 was already in use, which prevented the app from binding successfully. Once that port conflict is resolved, the preview and end-to-end query flow can be validated properly.

Team **ByteBuilders** -- [Priyadharshan B](https://github.com/priyadharshan-dev), [SAKTHIVEL R](https://github.com/Sakthiivel-19), [Madhana Krishnan L](https://github.com/Madhan2007)

`2026-08-30`

---

### Relict
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/relict-64a8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mohith-krishna-mahesh/Relict-Shell) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lovely-unklhrys.peachweb.site/) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI for Genome Engineering & Computational Biology

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![NetworkX](https://img.shields.io/badge/NetworkX-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Ollama](https://img.shields.io/badge/Ollama-333333?style=flat-square)

**The problem it solves**

Relict makes complex biological research easier by bringing genomic, evolutionary, pathway, population, and clinical evidence together into one reasoning workflow. Instead of manually searching dozens of disconnected databases and comparing conflicting results, researchers can start with a biological objective and receive a traceable, evidence-backed analysis.

At the core is Relict Core, which handles source retrieval, evidence normalization, cross-database relationships, planning, and post-plan analysis. It connects to specialized biological sources such as Ensembl, NCBI, UniProt, STRING, KEGG, Reactome, GTEx, gnomAD, ChEMBL, Open Targets, GBIF, and others, while caching and structuring the retrieved evidence locally for reproducible analysis.

The workflow starts with a biological objective and species scope. Relict identifies the information required, retrieves the relevant evidence from the appropriate sources, resolves identifiers and relationships between records, and builds an evidence backed plan. The plan can then be subjected to post-plan analysis using additional computational tools and models such as VEP, AlphaMissense, Evo 2, CRISPOR, and CHOPCHOP where appropriate.

The Relict Shell provides the interface for this entire process. It turns the underlying Core into an interactive research environment where users can define projects, inspect retrieved evidence, follow relationships between genes, proteins, pathways, variants, species, and other entities, and understand how the final reasoning was constructed.

Relict can be used to investigate conservation and de-extinction questions, understand agricultural traits, explore synthetic biology objectives, analyze population level problems, and support precision medicine research.

The key difference is that Relict does not treat an AI generated answer as the evidence itself. "Every conclusion is connected back to the underlying sources and evidence that produced it", making the workflow more transparent, reproducible, and easier to audit.

**Challenges we ran into**

The biggest challenge was integrating biological data from many independent sources, each with different APIs, formats, identifiers, and update cycles. A single Relict analysis might need to connect Ensembl, NCBI, pathway databases, population datasets, and specialist resources without losing the provenance of the underlying evidence.

We solved this by building a source-specific retrieval layer with caching and a common evidence representation. Each result retains its source, identifiers, version/context, and provenance so information can be cross-referenced rather than blindly combined.

Another major hurdle was making the system work reliably in a self-hosted deployment. Some components behaved correctly locally but failed in the serverless deployment environment because of differences in filesystem persistence, process execution, and initialization. We separated persistent data from runtime state and made the bootstrap process explicitly initialize the required databases, cached sources, and computational components.

Finally, we had to prevent the reasoning layer from presenting unsupported conclusions as facts. Instead of asking the model to invent explanations when specialized model coverage is unavailable, Relict can fall back to the retrieved evidence itself, parse the source records, and generate a deterministic, traceable explanation from those records.

**Best Use of Tin Computer**

Future Scope Autonomous Product Improvement: Integrate Tin Computer with Relict Shell to continuously analyze user behavior, deployment errors, analytics, and the codebase. Tin could identify product bottlenecks, propose and implement fixes through GitHub, and measure the impact of each change, creating a feedback loop for continuously improving Relict.

**Best Use of CodeCrafters**

Relict is a strong CodeCrafters fit because it combines REST, GraphQL, SPARQL and SOAP APIs, local biological datasets, SQLite/DuckDB caching, evidence normalization, cross-database graph construction, and computational tools like BLAST, VEP, AlphaMissense, Evo 2, CRISPOR and CHOPCHOP into one research pipeline. Relict Core plans the investigation, retrieves and connects the right evidence, runs post-plan analysis, and produces deterministic, traceable explanations through the Relict Shell, making it a substantial systems-engineering project rather than another AI wrapper.

Team **Relict** -- [Mohith Krishna Mahesh](https://github.com/Mohith-Krishna-4533), [Akshay R](https://github.com/Akshayskv), [Dhaval Gupta](https://github.com/DhavalGupta1), [Tanmay Nair](https://github.com/magnusinst84-sudo), [Ayaan Saju](https://github.com/ayaan-saju70)

`2026-08-30`

---

### EchoSteady
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/echosteady-f7a9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Chirag-agg/EchoSteady) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Patients minimize. Voices don't.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**Challenges we ran into**

Real-time audio pipeline – It took some time to make the WebRTC/WebSocket audio streaming reliable initially. We separated out testing of the audio pipeline alone before integrating transcription and biometrics into it.

Third-party API integrations - two pipelines, one API. The response format and latencies of Speechmatics and Thymia APIs did not exactly match what is documented; we got each one to work on its own before connecting them up.

Narrowing scope due to time constraints – some of the dashboard and personalized baseline calculation features had to be cut back or deferred entirely to make sure the core pipeline shipped completely built out.

**The problem it solves**

People cannot or will not communicate their experience accurately under stress or while recovering, individuals suppress symptoms even if their voice indicates otherwise. This discrepancy is directly tied to poor care, and there is nothing yet that can detect such discrepancy like vitals monitor, transcripts, notes. 

Uses:

Live consultation: detects a difference between spoken and vocal (indicators of distress, tension, energy) and communicates this information to the clinician in a simple way, suggesting that a follow-up question be asked

Recovery monitoring: creates a unique baseline for each patient across several consultations, making any significant discrepancy more noticeable from the personal norm, not population norm

Support of healthcare professionals: makes a subtle and easily overlooked signal evident without overriding the clinical opinion

Advantages:

Safer: detects a miscommunication gap which currently has no detection methods

Easier: transforms a subtle vocal signal into a one-sentence piece of information

More reliable: does not degrade over time as human perception would

**Rehabilitation & Recovery**

Rehabilitation and recovery are a process of change in a given timeframe, not a single check-in point – progress and the risks of relapse are manifested through comparison of the state with the initial one, and most measures do not take that into account as they give one point in time measure.

The EchoSteady application is designed around that gap. It analyzes patient's voice biomarkers throughout the sequence of multiple sessions and establishes a unique baseline for that patient, thus a deviation would mean something – unusual for this particular patient, instead of the deviation from some average population measure. That approach is important for the recovery process as the patients tend to underestimate their condition in order to show their progress or simply because they cannot accurately assess their feelings. Thus, the EchoSteady application would reveal the gap between the stated progress and what the voice would reveal, providing additional follow-up question while there still is a chance to react to that.

Our team's primary contribution is this longitudinal layer which is specially made for this kind of process.

Team **JustBetter** -- DHRUV JAIN, [Chirag Aggarwal](https://github.com/itz-Chirag), [Dhruv Kwatra](https://github.com/dhruv-kwatra), Raunit Gandhi

`2026-08-16`

---

### ELXR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/elxr-e48d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/elviric/elxr-push2prod) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/OsOmvoCEoSE?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> An agentic clinical operating system for Indian OP

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![iOS](https://img.shields.io/badge/iOS-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![SwiftUI](https://img.shields.io/badge/SwiftUI-333333?style=flat-square) ![bun](https://img.shields.io/badge/bun-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![Mayaresearch tts](https://img.shields.io/badge/Mayaresearch%20tts-333333?style=flat-square)

**How you are solving it?**

The core idea
ELXR is not a dictation app. The transcript is an input, not the product.

A doctor speaks one sentence of Hinglish. The clinic then operates itself around it: a structured SOAP note is generated, ICD-11 codes are resolved from the live WHO index, pharmacy stock is checked and reserved, an itemised bill is produced, the queue advances to the next patient, a FHIR R4 bundle is emitted, and a follow-up SMS is drafted in the patient's own language. The doctor hears a six-second spoken confirmation and moves on.

Two consequences follow directly from the problem:

Digitisation becomes a byproduct, not a task. The doctor was going to speak to the patient anyway. Nothing is added to the consultation — no typing, no dropdown, no extra minute. This is the only way the digitisation gap closes: not by asking overworked physicians for more time, but for none.

Agents absorb the work that understaffing drops. In most clinics, nobody is doing the queue triage, stock reconciliation or follow-up calls. These agents are not assisting a person doing that work — there is no such person.

What was built
Seven Claude agents in three modes, which is the architectural point:

Reactive (doctor speaks, they run): orchestrator running a tool loop over the OPD modules, plus soapAgent, rxAgent and icdAgent doing parallel structured extraction.
Autonomous (the clock triggers them, nobody is in the room): queue-supervisor re-triages, flags no-shows and rebalances patients across doctors; pharmacy-supervisor reviews stock and raises purchase-order drafts.
Human-gated: follow-up drafts a patient reminder in the consultation's language and cannot send it.
Also built: a native SwiftUI iOS client (live WebSocket, AAC capture, raw PCM playback), a kiosk registration and OPD console, deterministic queue / inventory / billing modules, a FHIR R4 adapter, CSV export, and 40 tests.

The engineering that matters: what agents are not allowed to do
Models never touch arithmetic. Billing, stock and queue positions are plain deterministic TypeScript. When consultation_fee was briefly exposed as a tool parameter, the model invented ₹500 against a configured ₹200. It came straight back out of the tool surface.
The bill refuses to charge for undispensed drugs. Found by testing an out-of-stock scenario: the patient was being billed ₹66 for Azithromycin that never left the shelf.
The pharmacy agent cannot buy anything. It raises DRAFT purchase orders. An unattended agent with spending authority can empty a clinic's account on a bad inference.
The follow-up agent cannot send. There is no send() function in the module — not disabled, absent. A model writing to a patient's phone with no clinician in between is the one action here that could cause direct harm.
ICD codes are never generated by a model. The agent proposes a search term; the WHO ICD-11 API returns the code. A hallucinated ICD code is well-formatted, plausible, and invisible on review.
The kiosk never self-triages. A patient typing "I think I'm having a heart attack" is anxiety, not triage. Escalation is the supervisor's call.
Every autonomous action is logged with its reasoning and shown on the console.
India-first specifics
Hinglish is preserved verbatim — the STT prompt is pinned against translation, so pet dukhna survives into the audit record and Claude does the clinical interpretation downstream. Dosing shorthand is decoded as actually spoken (teen baar, subah shaam, khali pet → TDS, BD, on empty stomach). Phone number is the patient identity, because an OPD walk-in rarely has anything else, and a returning patient keeps one ID with an incrementing visit count. ABHA numbers are captured and validated. FHIR R4 output means any ABDM-linked PHR can consume it.

Verified, not claimed
A live run: Hinglish audio in → verbatim transcript → SOAP note → four real WHO ICD-11 codes (DA42.Z, DA61, MG26, MD81.4) → stock decremented → ₹253 itemised bill → queue advanced → FHIR bundle with 10 resources → spoken Hinglish confirmation. ~20 seconds end to end.

The queue supervisor, unprompted, escalated a chest-pain patient to EMERGENCY and caught that a cough patient had been assigned to Cardiology purely on load — a speciality mismatch a deterministic rule would have needed a complaint-to-speciality mapping table, in Hinglish, to catch.

**How Did You Use Claude?**

Claude is used two ways here: as the product's reasoning engine, and as the development environment.

1. As the runtime — seven agents, all Claude Sonnet 5
Every agent in ELXR is Claude, via the Anthropic SDK with native tool use.

Structured extraction via forced tool calls. soapAgent, rxAgent and icdAgent each use tool_choice: {type: "tool"} to force emission against a JSON Schema projected from Zod, then validate the result with Zod again (because the JSON Schema projection is lossy for refinements and defaults). Asking for "JSON in the response text" fails often enough to lose a demo.

A genuine tool loop for operations. The orchestrator gets three tools (check_inventory, generate_bill, update_queue_status) and decides which a given consultation warrants. It infers things nobody told it: REFERRED rather than COMPLETED when the plan sends a patient onward, and skipping check_inventory entirely when nothing was prescribed. Tool errors are handed back to the model as is_error results so it can adapt instead of crashing.

Unattended agents with narrow powers. The queue and pharmacy supervisors run on a timer with no human present. Their tool surfaces are deliberately small, they cannot touch money or dispensing, and each action is logged with the model's own stated reasoning.

Deliberate parallelism. SOAP and Rx have no interdependency, and ICD coding shares no inputs with the OPD tools, so those run concurrently. That plus batching the orchestrator's three tool calls into one turn took a consultation from 40s to ~20s.

Prompt engineering as a safety boundary. The orchestrator is capped at 12 words of spoken output and told to write "rupees 253" so TTS pronounces it. The follow-up agent is forbidden from adding any clinical content the doctor did not say. The queue supervisor is told explicitly that "doing nothing is the correct and common outcome."

2. As the build environment — Claude Code
The entire project was built in Claude Code over the hackathon, and it found real bugs by running the system rather than reading it:

zod-to-json-schema's openApi3 target emits exclusiveMinimum as a boolean, which the Anthropic API rejects (it requires JSON Schema 2020-12, where that keyword is a number). The existing tools only passed because none had a numeric constraint.
Bun.serve defaults to a 10-second idle timeout, so a supervisor run completed server-side while the client received nothing.
Maya's TTS returns audio/L16 that is actually little-endian, despite RFC 2586 specifying big-endian — decoding by the spec produces static.
Taking submission screenshots revealed that the escalated EMERGENCY patient showed as plain "Waiting" on the doctor's phone, because the iOS model lacked the triage field.

Used Claude Code to build the whole project:

![image](https://assets.devfolio.co/content/c13192f850d54213a0c941a169c153d1/2eedd8f4-4c26-4b14-b50b-96b2c119bd8a.png)

**What is the deployed URL for this project?**

https://github.com/elviric/elxr-push2prod

**What is the problem your project solves?**

A physician in a public or private OPD sees 100–300 patients per shift, at 1–2 minutes each. The overwhelming majority of those consultations end in a handwritten slip the patient carries home and eventually loses. The overwhelming majority of Indian health records and prescriptions are never digitised at all — no structured diagnosis, no coded medication history, nothing that survives to the next visit or transfers to another clinic.

The obvious fix makes the immediate problem worse. Conventional EMR software turns a 90-second consultation into a data-entry session: click through a diagnosis picker, type the drug name, select frequency from a dropdown, fill mandatory vendor fields. Studies of physician time have found roughly two hours on electronic records and desk work per hour of direct patient care (US data — Sinsky et al., Annals of Internal Medicine, 2016). Transplant that overhead into a clinic running at three minutes per patient and it does not fit. So it doesn't get used, or it gets used badly — records filled in at the end of the day from memory.

Doctors are choosing paper rationally. Paper is fast and invisible; EMR is visible and slow. The system that captures the data costs the thing the clinic has least of.

And it collapses entirely when the clinic is short-staffed, which is the normal case. The administrative work an OPD generates does not disappear when there is nobody to do it. Queue management, stock reconciliation, billing and follow-up calls are the first things dropped. Drugs run out because nobody checked the register. Patients wait hours because nobody re-sorted the queue when a chest-pain case walked in. Nobody is reminded to come back, so a treatable condition returns as an emergency.

The record-keeping problem and the operations problem are the same problem: there are not enough people, and every existing tool asks for more of their time, not less.

[Santosh A](https://github.com/elviric)

`2026-08-08`

---

### Smart crop health and disease predictor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-crop-health-and-disease-predictor-1510) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://colab.research.google.com/drive/1Vne7q_cNf7oYCHerK4GWx6h2sQXjBKC7?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Empowering Farmers with AI-Powered Plant Care.

![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Keras](https://img.shields.io/badge/Keras-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Crop diseases like bacteria and fungus spread unnoticed and destroy entire harvests. Farmers face high costs for expert consultation. This AI tool provides an instant 2-second diagnosis using a smartphone camera to detect blights, rust, and mildew with immediate expert treatment suggestions.

**Challenges we ran into**

Since the target users are local farmers, deploying heavy deep learning models on a normal smartphone was a major challenge due to latency and processing limits. We overcame this by using the highly optimized MobileNetV2 architecture and leveraging Google Colab cloud infrastructure for scalable execution.

Khushi Yadav

`2026-06-01`

---

### Al personalised fitness coach
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/al-personalised-fitness-coach-4848) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nyasapatel6-lab.github.io/Personalised-fitness-Coach/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> An AI-powered, interactive fitness

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Personal fitness coaching is often expensive, inaccessible, or lacking in real-time, objective feedback. Many beginners struggle with maintaining proper form, leading to sub-optimal results or acute injuries.

Our platform solves this by providing:

Democratic Access to Coaching: Users get a highly responsive, customized fitness companion without the heavy financial barrier of a personal trainer.

Real-Time Injury Prevention: Utilizing computer vision, the platform maps critical body landmarks to monitor posture and range of motion instantly.

Intelligent Adaptation: Instead of static, generic workout PDFs, our solution leverages LLM capabilities to build dynamic routines that scale based on individual user profiles, fitness levels, and targeted goals.

Seamless UI/UX: An intuitive frontend interface ensures that users can easily input parameters, view their real-time performance analytics, and follow guided visual cues effortlessly.

**Challenges we ran into**

Building a real-time, multimedia AI application came with several technical hurdles:

Latency in Real-Time Pose Estimation: Processing video frames sequentially for landmark tracking initially caused massive UI stuttering and frame drops.

How we overcame it: We optimized the computer vision pipeline by decoupling frame capture from inference loops, utilizing lightweight tracking models, and leveraging asynchronous processing to keep the user interface smooth at a stable frame rate.

State Management & UI Responsiveness: Syncing real-time feedback data, video streams, and dynamic workout states across the frontend components proved complex.

How we overcame it: Structured the React components around predictable state pipelines and used precise conditional rendering to ensure visual cues, timers, and metrics update instantly without triggering unnecessary re-renders.

Prompt Engineering for Consistent Workouts: Getting the LLM backend to output cleanly structured, personalized data without hallucinations or varying formats was a challenge.

How we overcame it: Implemented rigid prompt templates and system instructions to ensure the model strictly maps out routines matching the user's specific inputs every time.

Team **CodeX** -- Nyasa Patel

`2026-06-15`

---

### SHAPA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shapa-9d9f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shapa.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Because Every Product Should Match Your Health."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**Challenges we ran into**

One of our biggest challenges was creating truly personalized recommendations instead of generic product analysis. We had to integrate AI with user health profiles, allergies, medical conditions, and lifestyle preferences while designing intuitive result dashboards for food, medicine, and cosmetic products.

**The problem it solves**

Guardian AI eliminates guesswork by delivering AI-powered, personalized safety insights for food, medicines, and cosmetics based on each user's health profile, helping them make safer, healthier, and more informed product choices.

Team **TeamX** -- SANCHI VERMA, [Tushar Pawar](https://github.com/tusharpawar1241), [Arpita Jain](https://github.com/Arpita048), Arush Jain

`2026-06-29`

---

### Mamora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mamora-50d1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dhaarani1116/Mamora) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mamora-navy.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/DIioAJzZeFk?si=F6Hp3cPwyc3Sq8kG) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Maternal Health Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![OCR](https://img.shields.io/badge/OCR-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

### 🛠️ Challenges We Ran Into

Building a multi-lingual, offline-first, and production-grade application presented several interesting technical hurdles:

#### 1. Overcoming ERESOLVE Dependency Failures on Vercel
* **The Hurdle:** While the project built successfully on our local development machines, clean production builds on Vercel consistently failed during the dependency installation step. We discovered a peer dependency conflict: our template had configured TypeScript `^6.0.2` under `devDependencies`, but `react-scripts 5.x` strictly required TypeScript `^3.x || ^4.x`.
* **The Solution:** We downgraded the TypeScript package to a stable, compatible version (`^4.9.5`), cleared the node caches, regenerated `package-lock.json`, and pushed the clean package updates. This immediately resolved the installer loop and enabled clean builds on Vercel.

#### 2. Resolving Python Version and Library Compilation issues on Render
* **The Hurdle:** When deploying our FastAPI backend to Render, the build process failed during the compilation of the image processing library (`pillow`). We realized Render defaulted to Python 3.14 (a pre-release/experimental version) which lacked pre-built binary wheels for older libraries, forcing the server to try and compile C-extensions from scratch.
* **The Solution:** We created a `.python-version` file in our root and backend folders, pinning the Render environment's runtime to a stable Python **`3.11.8`** environment. Once the cache was cleared and redeployed, the packages installed smoothly in seconds.

#### 3. Preventing AI Key Exposure in Git Repositories
* **The Hurdle:** GitHub's secret scanning features blocked one of our earlier git commits due to an exposed Google Gemini API key. This blocked our push and put the repository's security at risk.
* **The Solution:** We scrubbed the hardcoded keys out of the source code and rewrote the repository’s commit history using a Git filter sweep to remove any trace of the exposed keys. We then safely loaded all secrets locally using `.env` files and configured Vercel's environment variables dashboard for production.

#### 4. Fixing Double-Voice Speech Duplication
* **The Hurdle:** Our local text-to-speech assistant read chatbot replies twice in a row. This was due to React's rendering lifecycle, where state changes triggered the voice synthesis engine to fire multiple times on the same text.
* **The Solution:** We implemented a `speechBaselineRef` inside the voice assistant component. This ref registers the string values of the spoken text and compares it before starting any new audio synthesis, ensuring each bot reply is spoken exactly once.

**The problem it solves**

### 🏥 The Problem Mamora Solves

Pregnant women in remote or low-resource areas face a dangerous gap in healthcare: they only see a doctor once a month, leaving weeks of critical health fluctuations completely unmonitored. This lack of daily tracking often delays the detection of life-threatening conditions like gestational diabetes, anemia, and preeclampsia. Furthermore, language barriers and low literacy levels make accessing digital health tools difficult for regional mothers, while poor rural internet connectivity makes online platforms unreliable.

Mamora solves these challenges by acting as a **24/7 clinical companion** that expecting mothers can use to make pregnancy monitoring safer, easier, and accessible:

#### 1. Daily Health Tracking & Early Risk Detection
* **What it replaces:** Manual notes, guess-work, or waiting until the next monthly clinic visit.
* **How it helps:** Mothers can input basic vitals (blood pressure, blood glucose, hemoglobin). The deterministic backend instantly analyzes these numbers and flags high-risk readings, urging them to seek clinical care immediately before issues escalate.

#### 2. Safe, Instant Health Guidance
* **What it replaces:** Searching the internet or asking unverified sources, which often leads to dangerous medical misinformation.
* **How it helps:** Mothers can ask health questions via the conversational chatbot. By pairing Google Gemini AI with a strict, rule-based clinical engine on the backend, Mamora ensures that responses are safe, reliable, and completely free from AI hallucinations.

#### 3. Overcoming Literacy and Language Barriers
* **What it replaces:** Complex, English-only health portals.
* **How it helps:** The application features complete **multilingual support** and a hands-free **voice assistant** (text-to-speech and speech-to-text). Mothers who cannot read or write fluently can simply speak to the app in their native tongue and hear guidance read aloud.

#### 4. Continuous Care in Offline Environments
* **What it replaces:** Systems that crash or lose data when the user loses internet connection.
* **How it helps:** Mamora's **offline sync queue** logs vitals locally even with zero connection. Once the mother reaches an area with signal, the data automatically batch-syncs to the cloud.

#### 5. Rapid Emergency Response
* **What it replaces:** Panic during a crisis, not knowing local hospital numbers, or struggling to share location coordinates.
* **How it helps:** In an emergency, a single tap on the SOS button locates the nearest maternity hospitals on an interactive map and dispatches an alert containing the mother's precise GPS coordinates and clinical details.

[Dhaarani M](https://github.com/Dhaarani1116)

`2026-07-27`

---

### MediMitra AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medimitra-ai-1084) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dhanya-jm024/medimitra-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://dhanya-medimitra.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> 🏥 AI Healthcare Companion for Underserved People

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

🚀 OUR TECHNICAL & DESIGN JOURNEY

1️⃣ MULTILINGUAL AI COMPLEXITY
Challenge: Making AI accurately understand 10+ Indian languages including regional dialects, medical terminology, and cultural context.
Solution: Integrated Google Gemini 2.0's multilingual capabilities with custom prompt engineering. Added phonetic fallbacks for edge cases and built a medical terminology mapper for each language.

2️⃣ OFFLINE FUNCTIONALITY FOR RURAL AREAS
Challenge: Rural users have unreliable internet, but healthcare needs are immediate. Traditional apps fail without connectivity.
Solution: Built as a Progressive Web App (PWA) with service workers caching critical medical knowledge base, symptom-disease mappings, and first-aid instructions locally. Sync data when connection returns.

3️⃣ ACCESSIBILITY WITHOUT COMPROMISE
Challenge: Serving elderly, disabled, and illiterate users while maintaining rich functionality.
Solution: Implemented voice-first UI as primary interaction method, added dynamic font scaling (A- to A++++), WCAG AAA compliant high-contrast modes, comprehensive screen reader support, and simplified navigation paths.

4️⃣ MEDICAL ACCURACY & LIABILITY
Challenge: AI diagnoses could potentially harm users if inaccurate.
Solution: Added confidence scoring (never present 100% certainty), severity indicators, mandatory "consult doctor" recommendations for serious symptoms, extensive disclaimers, and clear escalation paths for emergencies.

5️⃣ CULTURAL SENSITIVITY IN HEALTHCARE
Challenge: Different regions have different medical practices, traditional medicines, and health beliefs.
Solution: Localized content per region, integrated Ayurvedic and traditional medicine references, culturally-appropriate imagery and language, and region-specific medicine databases.

6️⃣ MULTIMODAL AI INTEGRATION
Challenge: Handling voice, text, images (medicines, skin conditions), and location data seamlessly.
Solution: Built unified AI pipeline using Google Gemini's multimodal capabilities. Created optimized image compression before analysis, streaming voice-to-text, and intelligent context switching between modalities.

7️⃣ EMERGENCY RESPONSE RELIABILITY
Challenge: Emergency features MUST work when everything else fails.
Solution: Implemented offline-first emergency mode with pre-cached first-aid data, GPS-based hospital locator with fallback databases, Twilio SMS integration with retry logic, and one-tap access from ANY screen.

💡 KEY LEARNINGS:

1. Empathy Drives Innovation: The best UX designer is genuine care for users. Talking to real rural users transformed our approach completely.

2. Simplicity Wins: Every removed button, every simplified flow made the app more valuable, not less.

3. Accessibility ≠ Compromise: Building for the most vulnerable users creates better UX for everyone.

4. Local Context Matters: Global solutions fail; culturally-aware solutions thrive.

5. AI is a Tool, Not a Doctor: Position AI as a guide that empowers human decisions, not replaces medical expertise.

6. Ship Fast, Iterate Faster: Deploying early and iterating with feedback beats waiting for perfection.

🎯 UNEXPECTED WINS:
• Voice-first design attracted urban users who prefer hands-free
• Offline mode became popular during network outages
• Simple UI won praise from tech-savvy users too
• Elderly grandparents became our best beta testers

**The problem it solves**

🌍 THE HEALTHCARE ACCESS CRISIS

📊 STARK STATISTICS:
• 4.5 BILLION people worldwide lack essential healthcare
• 70% of Indians live in rural areas with limited medical access
• Rural India: Only 1 doctor per 10,000 people (WHO recommends 1:1000)
• Language barriers prevent 40% from getting proper care
• 5.2 million preventable deaths occur annually
• Elderly & disabled struggle with complex medical apps
• Emergency response is delayed by hours in rural areas

😢 THE HUMAN COST:

Meet Sita's grandmother — 65 years old, lives 40km from the nearest hospital in a Karnataka village, speaks only Kannada, and cannot read medicine labels. When chest pain strikes at night, her family faces an impossible choice: wait until morning and risk everything, or attempt the dangerous night journey to the clinic.

This scenario plays out in MILLIONS of families across India every single day. People are dying not from incurable diseases, but from:
❌ Not knowing when symptoms are serious
❌ Not understanding medicine instructions
❌ Not being able to communicate with doctors
❌ Not having emergency guidance
❌ Not being able to reach hospitals in time

💡 WHY EXISTING SOLUTIONS FAIL:
• Health apps only support English/Hindi
• Not designed for low-literacy users
• Require expensive smartphones
• Don't work offline
• Ignore accessibility needs
• Not culturally relevant

🎯 THE URGENT NEED:
The world needs an AI-powered healthcare solution that:
✅ Understands any language, any dialect
✅ Works for elderly, disabled, illiterate users
✅ Functions without internet
✅ Provides accurate medical guidance
✅ Handles emergencies effectively
✅ Costs nothing to users

MediMitra AI is that solution.

Team **Terrors** -- [J M Dhanya Kumar](https://github.com/Dhanya-jm024), Shreyas Hanashi

`2026-07-30`

---

### Mamora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mamora-fa09) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dhaarani1116/Mamora) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mamora-navy.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/DIioAJzZeFk?si=F6Hp3cPwyc3Sq8kG) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Maternal Health Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square)

**The problem it solves**

### 🏥 The Problem Mamora Solves

Pregnant women in remote or low-resource areas face a dangerous gap in healthcare: they only see a doctor once a month, leaving weeks of critical health fluctuations completely unmonitored. This lack of daily tracking often delays the detection of life-threatening conditions like gestational diabetes, anemia, and preeclampsia. Furthermore, language barriers and low literacy levels make accessing digital health tools difficult for regional mothers, while poor rural internet connectivity makes online platforms unreliable.

Mamora solves these challenges by acting as a **24/7 clinical companion** that expecting mothers can use to make pregnancy monitoring safer, easier, and accessible:

#### 1. Daily Health Tracking & Early Risk Detection
* **What it replaces:** Manual notes, guess-work, or waiting until the next monthly clinic visit.
* **How it helps:** Mothers can input basic vitals (blood pressure, blood glucose, hemoglobin). The deterministic backend instantly analyzes these numbers and flags high-risk readings, urging them to seek clinical care immediately before issues escalate.

#### 2. Safe, Instant Health Guidance
* **What it replaces:** Searching the internet or asking unverified sources, which often leads to dangerous medical misinformation.
* **How it helps:** Mothers can ask health questions via the conversational chatbot. By pairing Google Gemini AI with a strict, rule-based clinical engine on the backend, Mamora ensures that responses are safe, reliable, and completely free from AI hallucinations.

#### 3. Overcoming Literacy and Language Barriers
* **What it replaces:** Complex, English-only health portals.
* **How it helps:** The application features complete **multilingual support** and a hands-free **voice assistant** (text-to-speech and speech-to-text). Mothers who cannot read or write fluently can simply speak to the app in their native tongue and hear guidance read aloud.

#### 4. Continuous Care in Offline Environments
* **What it replaces:** Systems that crash or lose data when the user loses internet connection.
* **How it helps:** Mamora's **offline sync queue** logs vitals locally even with zero connection. Once the mother reaches an area with signal, the data automatically batch-syncs to the cloud.

#### 5. Rapid Emergency Response
* **What it replaces:** Panic during a crisis, not knowing local hospital numbers, or struggling to share location coordinates.
* **How it helps:** In an emergency, a single tap on the SOS button locates the nearest maternity hospitals on an interactive map and dispatches an alert containing the mother's precise GPS coordinates and clinical details.

**Challenges we ran into**

### 🛠️ Challenges We Ran Into

Building a multi-lingual, offline-first, and production-grade application presented several interesting technical hurdles:

#### 1. Overcoming ERESOLVE Dependency Failures on Vercel
* **The Hurdle:** While the project built successfully on our local development machines, clean production builds on Vercel consistently failed during the dependency installation step. We discovered a peer dependency conflict: our template had configured TypeScript `^6.0.2` under `devDependencies`, but `react-scripts 5.x` strictly required TypeScript `^3.x || ^4.x`.
* **The Solution:** We downgraded the TypeScript package to a stable, compatible version (`^4.9.5`), cleared the node caches, regenerated `package-lock.json`, and pushed the clean package updates. This immediately resolved the installer loop and enabled clean builds on Vercel.

#### 2. Resolving Python Version and Library Compilation issues on Render
* **The Hurdle:** When deploying our FastAPI backend to Render, the build process failed during the compilation of the image processing library (`pillow`). We realized Render defaulted to Python 3.14 (a pre-release/experimental version) which lacked pre-built binary wheels for older libraries, forcing the server to try and compile C-extensions from scratch.
* **The Solution:** We created a `.python-version` file in our root and backend folders, pinning the Render environment's runtime to a stable Python **`3.11.8`** environment. Once the cache was cleared and redeployed, the packages installed smoothly in seconds.

#### 3. Preventing AI Key Exposure in Git Repositories
* **The Hurdle:** GitHub's secret scanning features blocked one of our earlier git commits due to an exposed Google Gemini API key. This blocked our push and put the repository's security at risk.
* **The Solution:** We scrubbed the hardcoded keys out of the source code and rewrote the repository’s commit history using a Git filter sweep to remove any trace of the exposed keys. We then safely loaded all secrets locally using `.env` files and configured Vercel's environment variables dashboard for production.

#### 4. Fixing Double-Voice Speech Duplication
* **The Hurdle:** Our local text-to-speech assistant read chatbot replies twice in a row. This was due to React's rendering lifecycle, where state changes triggered the voice synthesis engine to fire multiple times on the same text.
* **The Solution:** We implemented a `speechBaselineRef` inside the voice assistant component. This ref registers the string values of the spoken text and compares it before starting any new audio synthesis, ensuring each bot reply is spoken exactly once.

Team **NeuralSparks** -- [Dhaarani M](https://github.com/Dhaarani1116)

`2026-07-25`

---

### heart pump care
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/heart-pump-care-a3f8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nandhini20072027-bit/HeartPump_Care) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://heart-pump-care.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/bM3D1zkh4G0?si=mzGxhGr3sXJa5ymn) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Know Your Risk. Own Your Health. 🔍

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![GeminiAPI](https://img.shields.io/badge/GeminiAPI-333333?style=flat-square)

**Challenges we ran into**

Building HeartPump Care was an exciting journey, but it came with several technical and design challenges that required careful problem-solving and continuous iteration.

1. Balancing AI Assistance with Healthcare Responsibility

One of the biggest challenges was ensuring that the AI-generated responses were helpful without giving users the impression that the platform was providing a medical diagnosis. Healthcare is a sensitive domain where inaccurate or overly confident recommendations can have serious consequences.

To address this, we focused on designing prompts and responses that provide general health guidance, risk awareness, and recommended next steps rather than definitive diagnoses. We also incorporated clear medical disclaimers throughout the application to remind users that professional healthcare providers should always be consulted for medical decisions.

2. Making Complex Health Information Easy to Understand

Medical information is often filled with technical terminology that can be difficult for the average user to understand. Early versions of the platform generated responses that were informative but sometimes too complex or overwhelming.

We refined the AI output and user interface to present information in a simpler, more user-friendly format. The goal was to make health insights understandable for users with different levels of medical knowledge while still maintaining accuracy and usefulness.

3. Creating a Smooth User Experience

Users interacting with healthcare applications expect quick and intuitive experiences. During development, we encountered challenges related to form handling, input validation, and maintaining a smooth flow between symptom submission and result generation.

We improved the user journey by simplifying forms, adding validation checks, improving loading states, and organizing information into clear sections. These changes helped reduce user confusion and created a more seamless experience.

4. Handling Incomplete or Unclear User Inputs

Not every user provides detailed symptom information. Some users may enter very short descriptions, incomplete information, or vague symptoms that make meaningful analysis difficult.

To overcome this challenge, we implemented input validation and designed the system to guide users toward providing more useful information. We also structured the AI prompts to extract as much context as possible from limited inputs while maintaining reasonable responses.

5. Ensuring Responsive Design Across Devices

Since healthcare tools are often accessed on mobile devices, ensuring a consistent experience across desktops, tablets, and smartphones was essential. Certain layouts, dashboards, and information cards initially displayed differently across screen sizes.

We addressed this through extensive responsive design testing and iterative UI adjustments, ensuring that critical healthcare information remained readable and accessible regardless of device type.

6. Building Trust Through Design

Healthcare applications require a high level of user trust. During development, we realized that users are more likely to engage with a platform when the interface feels professional, reliable, and transparent.

We focused on creating a clean design, adding clear explanations, including safety disclaimers, and presenting information in a structured manner. These improvements helped make the platform feel more trustworthy and user-focused.

How We Overcame These Challenges

Rather than treating these obstacles as setbacks, we used them as opportunities to improve the product. Through continuous testing, feedback-driven improvements, UI refinements, and responsible AI design practices, we were able to build a platform that is both user-friendly and health-conscious.

Each challenge helped shape HeartPump Care into a more reliable preventive healthcare companion, ultimately improving both the quality of the user experience and the overall value of the solution.

**The problem it solves**

Healthcare decisions are often made when people are stressed, confused, or unsure about the seriousness of their symptoms. A simple headache, chest discomfort, dizziness, or fatigue can leave someone wondering whether they should seek immediate medical attention, schedule a doctor's appointment, or simply rest and monitor their condition. In many cases, people either ignore potentially serious symptoms or become unnecessarily anxious because they lack reliable guidance.

At the same time, maintaining good health requires more than reacting to illness. People frequently forget to take medications, fail to track important health information, and miss early warning signs that could have been addressed through preventive care. Healthcare information is available online, but it is often scattered across multiple websites, difficult to understand, and not personalized to an individual's situation.

This gap between everyday health concerns and accessible healthcare guidance is what HeartPump Care aims to address.

What People Can Use It For

1. Understanding Symptoms Before They Become Serious

When users experience symptoms, they often turn to internet searches that provide overwhelming and sometimes misleading information. HeartPump Care offers a more structured approach by allowing users to enter their symptoms and receive AI-powered insights about possible health risks and recommended actions.

Instead of spending time searching through dozens of articles, users can get quick, understandable guidance that helps them make informed decisions about their next steps.

For example:

A user experiencing mild chest discomfort can receive guidance on whether the symptom may require urgent medical attention.
Someone experiencing fatigue, dizziness, or headaches can better understand potential causes and whether they should monitor the condition or consult a healthcare professional.

This helps reduce both unnecessary panic and dangerous delays in seeking care.

2. Encouraging Preventive Healthcare

Many health conditions become more difficult and expensive to treat when they are discovered late. One of the biggest challenges in healthcare is that people often seek medical help only after symptoms become severe.

HeartPump Care encourages users to become proactive about their health by helping them identify potential risks early and maintain awareness of their overall well-being.

Rather than focusing only on treatment, the platform promotes prevention by helping users:

Monitor health indicators.
Recognize warning signs earlier.
Stay informed about potential health risks.
Take action before conditions worsen.

3. Simplifying Health Management

Managing personal health can be difficult, especially for individuals who take multiple medications or need to regularly monitor their health.

HeartPump Care brings important health management activities into a single platform where users can:

Keep track of health information.
Monitor symptoms over time.
Review previous assessments.
Stay organized with medication schedules and reminders.

This reduces the need to rely on memory, paper notes, or multiple separate applications.

4. Improving Medication Adherence

Missing medications is one of the most common reasons for treatment failure and worsening health conditions. Busy schedules, forgetfulness, and complex medication routines often cause people to skip important doses.

HeartPump Care helps users stay consistent with their medication schedules through reminders and tracking features.

This can be particularly beneficial for:

Elderly individuals.
Patients managing chronic illnesses.
People recovering from medical procedures.
Caregivers supporting family members.

By improving medication adherence, users can better follow treatment plans and maintain healthier outcomes.

5. Making Healthcare Information More Accessible

Medical information is often filled with technical terminology that many people find difficult to understand. This can make it challenging for users to interpret symptoms, risks, and recommendations.

HeartPump Care translates complex healthcare information into simpler, more user-friendly explanations. The platform aims to make health guidance accessible regardless of a user's medical knowledge or background.

Its multilingual support further expands accessibility, allowing more people to interact with healthcare information in a language they are comfortable with.

How It Makes Existing Tasks Easier

Without HeartPump Care, a person experiencing symptoms may:

Search multiple websites.
Read conflicting medical information.
Become confused or anxious.
Delay seeking care.
Forget important details about their symptoms.

With HeartPump Care, the process becomes:

Enter symptoms.
Receive structured AI-powered insights.
Understand potential risk levels.
Review recommended next steps.
Track health information in one place.

This saves time, reduces confusion, and provides a more organized healthcare experience.

Team **neural warriors** -- Keerthika R, THARINI S, Nandhini S, Mahanitha Mohan

`2026-06-14`

---

### CuraPath
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/curapath-6ba7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://curapath-web.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=AFXXqEwWzdI) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Recovery doesn't end when you leave the hospital.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Post-surgical and hospital discharge recovery is an incredibly vulnerable phase for patients. Individuals are frequently handed complex, dense, and hand-annotated paper instructions while still groggy or heavily medicated under the effects of anesthesia. This creates a dangerous "Multi-Specialist Blindspot" where critical medication dosages are mismanaged, follow-up appointments are missed, and vital recovery history is lost when moving between different doctors.

### How CuraPath Solves This:
* **Eliminates Manual Errors:** Instead of forcing recovering patients or elderly caretakers to parse dense medical documentation, they simply snap a photo. **Mistral OCR & Mistral Large** securely parse the unstructured text into a clear, high-contrast, automated care calendar.
* **Proactive Recovery Monitoring:** Rather than relying on passive text alerts that are easily ignored, our autonomous **ElevenLabs TTS Voice Agent** actively checks in on the patient via conversational voice workflows, tracking symptom compliance and logging physiological anomalies safely.
* **Frictionless Medical Handoff:** Our core differentiator—the **30-Second Specialist Handoff**—compresses the patient's entire live history and active drug profile into a secure, scannable QR token on their screen. The next doctor scans it and gets a comprehensive clinical background in under 30 seconds, entirely eliminating human memory errors and safeguarding lives.

**Challenges we ran into**

### 1. The AI Formatting Nightmare (Overcoming Hallucinations)
Passing raw, unstructured hospital paper text to an LLM often led to inconsistent JSON schemas. Sometimes dosages were nested incorrectly, or the format structure would drift, which would completely break our frontend calendar grid. 
* **The Fix:** We decoupled the extraction layers and implemented rigid backend validation using **Pydantic Strict Schemas** inside FastAPI. We forced Mistral to align tightly with our exact model interfaces and built a side-by-side **Human-in-the-Loop Validation Screen** on the frontend, giving users the ultimate right of refusal before committing data to the state registry.

### 2. State Ingestion & Async Voice Feedback Logs
Managing live-updating data flows from the autonomous conversational agent down to the UI without causing heavy layout shifts or infinite rendering loops was a major hurdle. 
* **The Fix:** We optimized our React state-management pipelines by setting up deterministic local caching and structural JSON schemas. When the simulated ElevenLabs endpoint returns speech-to-text transcripts, the backend securely formats the conversational payloads, enabling a clean, sequential, and highly scannable vertical log feed.

Team **hell_naa** -- [Nirvik Goswami](https://github.com/nirvik34), [Rakshith Ganjimut](https://github.com/Rakshi2609), [Ayushi Tewari](https://github.com/AyushiTewari406), [Tanush Bhootra](https://github.com/tanushbhootra576)

`2026-06-14`

---

### MEDSONA AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medsona-ai-3530) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://medsona.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Your Clinical Persona. Powered by Intelligence."

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Google Location services](https://img.shields.io/badge/Google%20Location%20services-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

### **The Problem: The "Healthcare Information Gap"**

Modern healthcare is advanced, but the **patient experience** is broken. We identified four critical failures in how individuals manage their health:

#### **1. The "Prescription Paradox"**
*   **The Problem**: 70% of medical data is still trapped in unreadable, handwritten paper prescriptions. Patients often misinterpret dosages or lose these papers entirely, leading to 25% of medication errors.
*   **The Medsona Solution**: Uses **Gemini Vision AI** to instantly digitize and structure handwritten data into smart, automated schedules.

#### **2. Data Fragmentation (The "Medical Junk Drawer")**
*   **The Problem**: A patient’s medical history is usually scattered across physical folders, different lab portals, and gallery screenshots. In a crisis, retrieving a specific X-ray or blood report is impossible.
*   **The Medsona Solution**: A **Secure Clinical Vault** that uses military-grade encryption to centralize every report into one searchable "Medical Persona."

#### **3. The "Silent" Recovery Gap**
*   **The Problem**: Between doctor visits, patients are "on their own." There is no professional-grade guidance for sudden symptoms, leading to "Google-searching symptoms," which causes unnecessary panic or delayed care.
*   **The Medsona Solution**: A **24/7 Clinical Assistant** that provides evidence-based health insights and longitudinal vitals tracking to catch trends before they become emergencies.

#### **4. The Motivation Barrier**
*   **The Problem**: Medical compliance is boring. Patients lose motivation to log vitals or finish physical therapy because there is no immediate feedback or incentive.
*   **The Medsona Solution**: A **Gamified Health Economy (SonaCoins)** that rewards healthy behaviors with real-world value, turning "chores" into "achievements."

#### **5. Critical Response Latency**
*   **The Problem**: During a medical emergency, every second counts. Currently, notifying family and sharing your live location/medical status is a manual, slow process.
*   **The Medsona Solution**: A **One-Tap SOS Hub** that broadcasts your identity, location, and status to five contacts simultaneously using real-time geospatial orchestration.

---

### **Summary Quote for your Slide:**
> *"We aren't just building another health app; we are solving the **fragmentation of care**. Medsona turns a patient's chaotic paper trail into a secure, intelligent, and proactive medical persona."*

**Challenges we ran into**

### **Technical Challenges & Breakthroughs**

#### **1. The "Handwriting Recognition" Hurdle**
*   **The Challenge**: We initially struggled with the high variance in doctor's handwriting. Standard OCR was failing to capture specific dosage units (e.g., confusing 'mg' with 'ml').
*   **The Positive Outcome**: This led us to move beyond simple OCR to **Multi-modal LLM Chain-of-Thought prompting**. We engineered a system that doesn't just "read" text but "understands" medical context. If the AI sees a blood pressure medication, it now *expects* to find a dosage in 'mg,' significantly increasing accuracy through clinical reasoning.

#### **2. The "Privacy vs. Performance" Trade-off**
*   **The Challenge**: Implementing military-grade encryption for medical records usually slows down the app significantly. We didn't want the user to wait 10 seconds to see their own X-ray in an emergency.
*   **The Positive Outcome**: We mastered **Supabase Row Level Security (RLS)** and **Edge Functions**. By moving the security logic to the database layer instead of the application layer, we achieved "Zero-Knowledge" privacy with sub-second retrieval times. Security became a performance feature, not a bottleneck.

#### **3. Designing for "High-Stress" UX**
*   **The Challenge**: Our initial dashboard was too "busy." We realized that in a medical emergency, a user can't navigate complex menus to find the SOS button.
*   **The Positive Outcome**: This pushed us to adopt a **"Progressive Disclosure" design philosophy**. We stripped the UI down to its essentials, using **Framer Motion** for subtle micro-animations that guide the eye to the most critical actions. We learned that in healthcare, *less is literally more life-saving.*

#### **4. Maintaining "Transactional Integrity" for SonaCoins**
*   **The Challenge**: We ran into "Race Conditions" where users could potentially claim rewards twice if they clicked too fast, which would break the economics of the platform.
*   **The Positive Outcome**: This was a deep dive into **ACID-compliant database design**. We implemented PostgreSQL triggers and stored procedures to handle coin minting at the atomic level. It taught us how to build a robust "FinTech" layer inside a "HealthTech" app.

---

### **The "Golden Nugget" for your Slide:**
> *"Every technical roadblock was just an opportunity to refine our architecture. We didn't just build features; we engineered solutions that are resilient, secure, and human-centric."*

Team **TECH_TITANS** -- [Jaswanth V L S Kumar Kollipara](https://github.com/jaswanthgec)

`2026-05-16`

---

### MEDTRACK
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medtrack-2374) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Your Health, Encrypted & Empowered."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

A **Medical Tracking Application** isn't just a digital filing cabinet; it’s a proactive tool designed to reduce human error and provide a holistic view of a person’s health journey.

Here is how such an application solves real-world problems and streamlines healthcare management:

---

## 1. Centralizing "Fragmented" Medical History
The biggest challenge in modern healthcare is the "silo" effect—your cardiologist, GP, and dentist often don’t have access to the same records.

* **The Solution:** Users can store lab results, vaccination records, and surgical histories in one place.
* **The Impact:** When seeing a new specialist, you don’t have to rely on memory. You provide a complete, accurate data set, which leads to better diagnoses.

## 2. Medication Management & Safety
Human memory is fallible, especially when managing complex "polypharmacy" (taking multiple medications).

* **Smart Reminders:** Automated alerts ensure doses aren't missed.
* **Interaction Checks:** Many apps can flag potential drug-to-drug interactions before you take them.
* **Safety:** It prevents **accidental doubling** of doses, which is a major cause of emergency room visits for the elderly.

## 3. Symptom & Chronic Condition Tracking
For patients with chronic illnesses like Migraines, IBS, or Diabetes, "how you've been feeling" is often too vague for a doctor to use.

* **Data Logging:** Users can log daily pain levels, blood glucose, or blood pressure.
* **Trend Analysis:** The app generates charts that show how symptoms correlate with diet, weather, or stress.
* **The Impact:** This turns "I feel bad sometimes" into "I experience a 30% spike in symptoms every Tuesday after my gym session."



---

## 4. Caregiver Coordination
Managing the health of a child, an aging parent, or a disabled loved one is a massive administrative burden.

| Task | Without an App | With a Tracking App |
| :--- | :--- | :--- |
| **Updates** | Calling every family member individually. | Shared access to the health log. |
| **Appointments** | Paper calendars or lost sticky notes. | Synced alerts for all caregivers. |
| **Emergency** | Scrambling for a list of allergies. | One-tap "Emergency Profile" access. |

## 5. Emergency Preparedness
In an emergency, you may be unconscious or too distressed to provide information.

* **The Solution:** A "Digital ID" or "Medical Pass" feature allows first responders to see your blood type, allergies (like Penicillin), and emergency contacts directly from your phone's lock screen.
* **Safety:** This saves precious minutes and prevents life-threatening allergic reactions during treatment.

---

## 6. Informed Decision Making
By tracking metrics over time (like weight, heart rate, or sleep patterns), the application shifts healthcare from **reactive** to **proactive**.

* **Early Detection:** Spotting a gradual upward trend in blood pressure before it reaches a crisis level.
* **Accountability:** Seeing a visual representation of your progress can motivate better lifestyle choices.

> **The Bottom Line:** A medical tracking app moves the responsibility of "remembering" from the brain to the palm of the hand, reducing anxiety for the patient and providing "cleaner" data for the physician.

**Challenges we ran into**

Building a medical tracking application presents a unique set of technical and ethical hurdles. Since we are dealing with sensitive biometric data and "mission-critical" reminders, the stakes are much higher than a standard productivity app.Here are three specific challenges often encountered during development and how to navigate them:1. The "Notification Fatigue" & Reliability BugThe Hurdle: On many modern operating systems (especially Android), aggressive battery optimization often "kills" background processes. This meant that life-critical medication reminders were being delayed or suppressed entirely to save battery life.The Fix: We had to implement Exact Alarms using specialized APIs (like AlarmManager in Android) that bypass standard battery restrictions.The Design Pivot: To solve "Notification Fatigue" (users ignoring alerts because they get too many), we implemented a Critical Alert system. Normal logs use standard pings, but "High-Stakes" medications use a persistent, escalating alarm that requires a specific interaction to silence.2. Secure Data Synchronization (The HIPAA/GDPR Puzzle)The Hurdle: Balancing user convenience (accessing data on any device) with strict privacy laws. Traditional databases store data in a way that developers could technically "see," which is a major security risk for medical records.The Fix: We moved to End-to-End Encryption (E2EE).Data is encrypted on the user’s device using a key derived from their password before it ever hits the cloud.The Result: Even if our servers were breached, the hackers would only see "gibberish" text.How we got over it: We utilized established libraries like AES-256 for encryption, ensuring we weren't "rolling our own crypto," which is a cardinal sin in security.3. The "Messy Data" Standardization ProblemThe Hurdle: Users and doctors often use different terms for the same thing (e.g., "High Blood Pressure" vs. "Hypertension"). If the app is supposed to generate a report for a doctor, the data needs to be standardized.The Fix: Instead of relying purely on free-text input, we integrated the SNOMED CT or LOINC medical terminology databases.User Experience (UX) Solution: We implemented an "Autosuggest" search bar. As a user types "Heart," the app suggests "Heart Rate (BPM)" or "Atrial Fibrillation," tagging the entry with a universal medical code behind the scenes.ChallengeImpactResolutionSystem HibernationMissed medications.Use of high-priority system intents & AlarmManager.Data PrivacyRisk of sensitive leaks.Local-first E2EE (End-to-End Encryption).Medical AccuracyConfusing reports for doctors.Standardized terminology via API integration.4. The "Ghost Entry" BugThe Hurdle: During the beta phase, we found that users were accidentally double-logging symptoms because the UI didn't update fast enough on slow connections, leading them to tap "Submit" twice.The Fix: We implemented Optimistic UI updates. The app now shows the entry as "Saved" instantly in the local cache, then syncs with the server in the background. We also disabled the submit button the millisecond it was pressed (Debouncing) to prevent duplicate entries.

MADESH KANNA

`2026-05-05`

---

### AI_clinical_Assistance
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aiclinicalassistance-70b0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shravan2307/prism-ai-clinical-intelligence) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1E_DHZ-3jz-52H3vJbRLAM1mEdX1nwDdh/view) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Predict Early .Act Smarter. Save Lives

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Medical AI Clinical Intelligence
An AI-powered clinical intelligence platform designed to assist with early disease-risk identification, clinical analysis, treatment recommendations, and intelligent patient triage.

The system combines an existing Machine Learning/AI implementation with a structured application layer built using FastAPI, allowing patient information to flow through safety checks, triage, clinical analysis, and the existing ML components.

⚠️ Medical Disclaimer: This project is a clinical decision-support prototype intended for research, education, and hackathon purposes. It is not a replacement for a qualified medical professional, diagnosis, or emergency medical care.

🚀 Project Overview
The goal of the platform is to provide an intelligent workflow that can:

Accept structured patient information.
Perform an initial safety assessment.
Determine the appropriate triage workflow.
Run the existing clinical ML/AI components.
Generate structured clinical insights.
Provide risk and contributing-factor information.
Provide treatment/recommendation information where supported.
Escalate appropriate cases to a doctor workflow.
Present the results through a modern frontend dashboard.
Core Principle
The application layer does not duplicate the existing ML logic.

The existing ML implementation remains the source of truth for:

Disease/risk prediction
Risk scoring
Treatment ranking
Causal analysis
Clinical intelligence
The application layer is responsible for orchestrating these components and exposing them through a clean API.

🧠 System Architecture
                    ┌─────────────────────┐
                    │      Frontend       │
                    │  Clinical Dashboard │
                    └──────────┬──────────┘
                               │
                               │ HTTP / JSON
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    │   Application Layer │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   PatientRequest    │
                    │   Pydantic Model    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Safety Gate     │
                    │ Emergency/Urgency   │
                    │     Detection       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Triage Engine    │
                    │ Workflow Selection  │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌───────────────────────────┐
                 │  ClinicalAnalysisService  │
                 │       Orchestrator        │
                 └─────────────┬─────────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      ┌────────────┐    ┌────────────┐    ┌────────────┐
      │ Risk/ML    │    │ Treatment  │    │  Causal    │
      │ Engine     │    │ Ranking    │    │  Analysis  │
      └────────────┘    └────────────┘    └────────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Structured Clinical │
                    │      Response       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
       ┌────────────────┐             ┌────────────────┐
       │ Patient Result │             │ Doctor Workflow│
       │   Dashboard    │             │   / Escalation │
       └────────────────┘             └────────────────┘
✨ Key Features
1. Patient Analysis
The frontend collects the information required by the backend and sends it to the FastAPI API.

The application uses a structured Pydantic request model to validate incoming patient information.

2. Safety Gate
Before normal clinical processing, the application performs a safety check.

The Safety Gate is responsible for identifying situations that may require:

Emergency escalation
Urgent medical review
Doctor review
Normal clinical workflow
The frontend does not independently calculate safety or risk.

The backend Safety Gate is the source of truth.

3. Intelligent Triage
The Triage Engine determines the next workflow based on the backend analysis.

Possible workflow categories can include:

Routine
Monitor
Follow-up
Doctor Review
Urgent
Emergency
The exact workflow is determined by the backend implementation.

4. Clinical Analysis Service
ClinicalAnalysisService acts as the main orchestration layer.

Its responsibility is to connect:

Patient Request
      ↓
Safety Gate
      ↓
Triage Engine
      ↓
Existing ML/Epics
      ↓
Clinical Result
This keeps the application layer separate from the underlying ML implementation.

5. Existing ML Components
The existing ML implementation is preserved.

The project does not create duplicate implementations of:

Risk Engine
Treatment Ranking Engine
Causal Engine
Disease Prediction
Clinical Reasoning
Instead, the application layer adapts to the existing ML interfaces.

6. Doctor Escalation Workflow
When the backend identifies a case requiring professional review, the system can route the case toward the doctor workflow.

The doctor dashboard can display:

Patient information
Triage status
Safety status
Clinical findings
Risk information
Contributing factors
Recommendations
Relevant analysis
The frontend displays information supplied by the backend rather than creating independent medical decisions.

🏗️ Project Structure
The project is organized into separate backend and frontend layers.

prism-ai-clinical-intelligence/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │
│   │   ├── models/
│   │   │
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │
│   │   ├── decision/
│   │   │
│   │   ├── agents/
│   │   │
│   │   ├── core/
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │
│   └── requirements.txt
│
├── frontend/
│   └── ...
│
├── .gitignore
├── README.md
└── ...
The exact directories may evolve as the application layer and frontend integration are completed.

⚙️ Technology Stack
Backend
Python
FastAPI
Pydantic
Uvicorn
Pytest
Existing ML/AI components
Frontend
JavaScript/TypeScript
React-based frontend
Modern responsive UI
REST API integration
Architecture
REST API
Service-oriented application layer
Pydantic request/response validation
ML/AI orchestration
Safety-first clinical workflow
📋 Prerequisites
Install the following before running the project.

Python
Recommended:

Python 3.11+
The project has also been developed/tested in the current environment using Python 3.14.x.

Check your version:

python --version
Node.js
Check:

node --version
npm --version
🔧 Backend Setup
Open a terminal in the project root:

cd prism-ai-clinical-intelligence
Move into the backend:

cd backend
1. Create Virtual Environment
Windows:

python -m venv venv
Activate it:

venv\Scripts\activate
You should see:

(venv)
at the beginning of your terminal prompt.

2. Install Dependencies
pip install -r requirements.txt
If the project does not contain a generated requirements file yet, install the project's declared dependencies according to the backend configuration.

3. Environment Variables
Create a .env file if required by the project.

Example:

# Backend configuration
APP_ENV=development

# Frontend URL
FRONTEND_URL=http://localhost:5173

# Add project-specific API keys/configuration here
# Never commit real secrets to GitHub.
Never commit:

.env
to GitHub.

Use .env.example for non-secret configuration documentation.

▶️ Running the Backend
From the backend directory:

python -m uvicorn app.main:app --reload
The backend should start at:

http://127.0.0.1:8000
FastAPI interactive documentation:

http://127.0.0.1:8000/docs
Alternative ReDoc documentation:

http://127.0.0.1:8000/redoc
🎨 Frontend Setup
Open a second terminal.

Move to the frontend directory containing package.json.

For example:

cd prism-ai-clinical-intelligence\frontend

**Challenges we ran into**

Challenges we ran into
Defining the scope
Initially, the idea covered many diseases, treatment, doctor escalation, appointments, reports, and home remedies.
We had to narrow the 24-hour hackathon scope to Type 2 Diabetes as the primary pathway, with Hypertension as a stretch goal. The PRD now explicitly reflects that.
Splitting the backend between two people
We needed a clean boundary between:
Person 1: FastAPI, validation, triage, red flags, safety gates.
Person 2 (you): ML, causal inference, treatment ranking, SHAP.
The biggest integration concern was making sure both sides use the same data contracts.
Medical safety
We cannot simply let an AI model decide a treatment.
Critical cases need deterministic rules that bypass the ML model.
For example, the PRD specifies hard-stop thresholds for diabetic emergencies and a renal safety rule that removes Metformin when eGFR is below 30.
Moving beyond simple disease prediction
A normal classifier answers:

"Does this patient have a high risk?"

Our Person 2 system needs to answer something more complex:

"For this patient, what is the estimated effect of each safe treatment?"

That's why we're using causal inference/DML and CATE rather than only classification.
No real patient dataset
Because we're building the hackathon prototype from scratch, Person 2 needs a 500-patient synthetic dataset with the required clinical features.

Team **N FACTORIAL** -- [SAUMYA PANDYA](https://github.com/SAMJOD07-devz), [Nikhil Gupta](https://github.com/3456789), Bhargav Patel, Shravan Patel

`2026-09-02`

---

### neutriguide
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neutriguide-466f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lsohaml/Neutrilin.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/vE5zM-136Kw?si=8ildTuzKTCgtiVw4) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> health asssistant

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

configuring the backend to a separate UI was challenging

**The problem it solves**

Individuals attempting weight management frequently fail to meet critical nutritional requirements while attempting calorie restriction, leading to unintended nutrient deficiencies that can exacerbate pre-existing health conditions. Standard health tracking applications collect static profile metrics—such as height, target weight, and logged food intake—but lack the intelligence to synthesize complex personal medical records with dynamic dietary habits. Consequently, existing tools fail to identify underlying nutrient deficits or provide medically sound, calorie-conscious guidance tailored to an individual’s clinical profile. There is a need for an intelligent health assistant that ingests personal medical history alongside daily intake logs to optimize both total caloric intake and essential nutrient fulfillment safely.

Team **Goblins** -- Antan Shijen, Nevil Koshy, Soham Mahajan

`2026-09-02`

---

### Vigil-OR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vigilor-9971) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sudhir61127.github.io/vigilor/) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> healthie

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

We faced challenges in integrating multiple components such as AI agents, patient databases, RAG-based document retrieval, live monitoring data, voice interaction, and the React dashboard. Maintaining smooth communication between the frontend and backend, handling dynamic patient information, designing intuitive navigation, and ensuring that voice commands correctly trigger the required workflow were some of the major challenges.

**The problem it solves**

Doctors often struggle to access the right patient information quickly because clinical data is scattered across multiple systems, including patient records, medical reports, CT/MRI scans, live vital signs, and checklists. Constantly switching between screens and manually searching for information increases cognitive workload and can delay clinical decision-making. VIGIL-OR solves this problem by providing a voice-first, AI-powered clinical workspace that intelligently retrieves and brings together the relevant patient information in one unified dashboard.

Team **CodeShields** -- SUDHIR Singh, DOUSHIK M, Charvi V, SARVESH PNM

`2026-09-02`

---

### SMART HOSPITAL QUEUE MANAGEMENT SYSTEM
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-hospital-queue-management-system-969f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/msushit12/-MEDQ_CARE.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://msushit12.github.io/-MEDQ_CARE/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.image2url.com/r2/default/videos/1788310882303-9fb38e2f-08af-4655-b6c2-7324d25ef647.mp4) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> "Less Waiting. Better Care.”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Google Sites API](https://img.shields.io/badge/Google%20Sites%20API-333333?style=flat-square)

**Challenges we ran into**

Challenges We Ran Into

Building MEDQ CARE within the limited hackathon time came with a few challenges. Since we were working as a team on different parts of the project, one of the biggest difficulties was making sure everyone's work worked together properly.

 Connecting the Frontend and Backend

Initially, the frontend pages were working separately, but connecting them with the backend was not straightforward. Some API requests were not reaching the backend correctly, and we had to check the API endpoints, ports, and request formats.

We solved this by testing the APIs separately first and then connecting each frontend feature one by one.

White Screen After Deployment

One of the major issues we faced was getting a white screen when opening the deployed website. The project was running correctly on our local machines, but the GitHub Pages/live version was not displaying the application.

We checked the browser console, deployment configuration, file paths, and Vite settings. We eventually found that the deployment environment needed to be configured differently from the local development environment.

This taught us that a website working perfectly on localhost does not always mean it will work immediately after deployment.

GitHub Merge and Push Issues

Since multiple team members were working on the project, we also faced Git and GitHub problems such as merge conflicts and rejected pushes.

Instead of overwriting each other's work, we learned to properly pull the latest changes, resolve conflicts, test the project, and then push the updated version.

Making the System Work Across Different Dashboards

MEDQ CARE has separate workflows for patients, reception staff, and doctors Making sure that each dashboard showed the correct information while keeping the overall workflow connected took some time.

We solved this by first completing the basic workflow and then gradually connecting the different sections.

Working Under Time Pressure

The hackathon time limit was another major challenge. We had many ideas that we wanted to include, but trying to build everything at once would have made the project unstable.

So, we focused first on the main features:

Patient → Appointment → Token → Queue → Doctor → Consultation

After getting the main workflow working, we added additional features wherever we had time.

 What We Learned

The biggest lesson for us was that building a project is not only about writing code. Debugging, connecting different parts, managing GitHub, testing, and working as a team are equally important.

Every problem we faced helped us understand our project better and improve the final version of MEDQ CARE.

**The problem it solves**

The Problem It Solves

In many hospitals, patients have to spend a lot of time waiting for their turn. Even after getting an appointment or token, they may not know how many patients are ahead of them or when they will actually meet the doctor. This can make the hospital experience stressful and also leads to crowded waiting areas.

At the same time, reception staff have to handle many things at once, such as registering patients, managing appointments, giving tokens, and keeping track of the queue. When most of these tasks are done manually, there is a higher chance of confusion, delays, or mistakes.

Doctors also need a simple way to see which patients are waiting and who should be called next. If the patient, reception, and doctor are all working with different information, managing the queue becomes more difficult.

MEDQ CARE was created to make this process easier.

Our system connects patients, reception staff, and doctors through a single platform. Patients can book appointments, receive a digital token, and check their queue status. Reception staff can manage patients, appointments, and queues from one dashboard. Doctors can view their current patient queue and manage consultations more easily.

The main idea is simple: patients should not have to spend unnecessary time waiting without knowing what is happening.

What MEDQ CARE helps with

* Reduces confusion around hospital queues and appointments.
* Gives patients a digital token instead of depending completely on physical tokens.
* Allows patients to see their queue status and stay updated.
* Helps reception staff manage appointments and patient queues in one place.
* Gives doctors a clear view of the patients waiting for consultation.
* Reduces unnecessary crowding and repeated enquiries at the reception desk.
* Keeps the patient, reception, and doctor workflows connected.

Overall, MEDQ CARE aims to make the hospital visit  more organized and convenient for patients while making queue management easier for hospital staff.

![image](https://assets.devfolio.co/content/c72c6c9b51bd4c8ab6698b71b9308252/be9e3085-5895-4e0f-a876-fc8fd3822ff2.png)

Team **TEAM FADE_OUT** -- A S Sujeeth, M Sushit, Tamil Selvan, VIJAYARAJ V, R YATHIN YASHWANTH

`2026-09-02`

---

### Structure AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/structure-ai-fbd4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/naren214/Hackverse_Hackathon2026.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/UOOROps31Uk) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Government Infrastructure Health AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

One time The dashborad was empty as it shows nothing and also there was no error and realized that they were using same components and resolved it

**The problem it solves**

StructureAI replaces slow, once-a-year manual infrastructure inspections with real-time sensor monitoring and AI-driven predictions that catch problems before they become failures. It gives government teams a live dashboard to track, schedule, and budget for maintenance, while letting citizens report issues directly with enough public reports automatically escalating a structure for urgent inspection.

Team **Code crafters** -- Dharaneesh KG, Rajkumar P.K., Naren KS, Jeremiah Anderson, Prajit R

`2026-09-02`

---

### HEALTHNOVA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthnova-1295) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MR-ARKO-JANA/VHD-HyperFusion) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> HEAL IS WELL  , RIGHT TIME RIGHT HELP

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Natural language processing (NLP)](https://img.shields.io/badge/Natural%20language%20processing%20(NLP)-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square)

**The problem it solves**

A clinically-engineered preventive healthcare platform that enables patients to access medical triage and diagnostic guidance in their preferred regional Indian language — through intelligent voice/text symptom analysis, photo-based skin lesion screening, and 100% offline-first edge compute. Uses ONNX WASM neural network inference for true on-device AI with WHO/IAMS-aligned clinical triage. Fully compliant with HL7 FHIR R4 and ABDM (Ayushman Bharat Digital Mission) healthcare interoperability standards. No cloud LLMs. No data transmission. Zero PII.

**Challenges we ran into**

****Here is a comprehensive write-up detailing the challenges faced while building VHD-HyperFusion and how your team overcame them. You can directly copy and paste this into the Devfolio project update section:

Challenges We Ran Into & How We Overcame Them
Building a 100% offline-first, vernacular healthcare diagnostics platform without any cloud LLM dependencies or data transmission came with a unique set of architectural and performance hurdles:

Achieving Real-Time Edge AI Latency in the Browser

The Hurdle: Running heavy machine learning models like IndicBERT INT4 for multilingual symptom classification and EfficientNet B0 INT8 for skin lesion screening directly in the browser via WebAssembly (ONNX WASM) initially caused high memory consumption and latency spikes above 300ms on lower-end mobile devices.

The Fix: We optimized the ONNX runtime execution providers, quantized models to INT4/INT8 precision, and implemented client-side worker threads to offload heavy inference computations away from the main UI thread, successfully bringing inference latency down to under 50ms.

Cross-Lingual Voice Recognition & Synthesis Limitations

The Hurdle: Native Web Speech APIs across different browsers varied wildly in their support for regional Indian languages (Bengali, Hindi, Tamil, Telugu, Kannada) and frequently failed with accented regional dialects.

The Fix: We implemented a robust hybrid fallback pipeline. When browser-native speech recognition fell short, the application seamlessly allowed manual vernacular text input or triggered localized rule-based intent parsing, ensuring zero disruption to patient triage.

Strict Zero-PII Compliance & Secure Local Storage

The Hurdle: Guaranteeing absolute zero data leakage while still allowing users to securely track their diagnostic history and health logs locally without a centralized cloud database.

The Fix: We integrated the Web Crypto API to implement client-side AES-256-GCM encryption for all locally stored health records, ensuring that patient data remains strictly ephemeral or encrypted on-device with zero exposure to third-party servers.

Healthcare Interoperability Standards (HL7 FHIR R4 & ABDM)

The Hurdle: Mapping unstructured local clinical rule engine outputs into standardized, compliant HL7 FHIR R4 resources (Condition, Observation, DiagnosticReport) required strict adherence to complex schema guidelines without bloating the lightweight backend.

The Fix: We built a dedicated serialization middleware layer in our Express backend (Backend/api/diagnosis.js) that automatically structures local WHO/IAMS-aligned triage results into standardized ABDM-ready interoperability payloads.

Team **Chaturarka** -- [Sourav De](https://github.com/Sourav-De67), [Arup Kumar Midya](https://github.com/arupkumarmidya100-cpu), [Pratush Midya](https://github.com/PRATUSH02), [Arko Jana](https://github.com/mr-arko-jana)

`2026-08-29`

---

### Emergency Healthcare System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/emergency-healthcare-system-efbc) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> Smart Emergency Care, When It Matters

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**Challenges we ran into**

One of our biggest challenges was designing a reliable real-time hospital matching and bed reservation system. Bed availability can change quickly, and we had to prevent two patients from reserving the same last available bed.

We solved this by introducing a reservation and validation layer that checks bed availability at the moment of booking and updates the hospital database immediately. Hospitals with zero available beds are automatically removed from the patient-facing list, while alternative hospitals can be suggested if a selected hospital becomes unavailable.

Another challenge was handling emergency descriptions through voice input. We implemented voice-to-text processing so users can describe an emergency naturally, while keeping the final emergency classification editable to avoid errors.

We also had to carefully separate AI-assisted emergency classification from medical diagnosis. Our AI helps identify the emergency category and route the patient to suitable hospitals, while actual medical decisions remain with qualified healthcare professionals.

Finally, integrating multiple steps—patient verification, hospital matching, reservation, payment confirmation, notifications, and doctor communication—into one smooth emergency workflow required careful coordination between the frontend, backend, database, and external services.

**The problem it solves**

During a medical emergency, finding a hospital with the right treatment facility and an available bed can be stressful and time-consuming. Patients and attendants often have to call multiple hospitals, travel without knowing whether a bed is available, and make critical decisions under pressure.

Omnitriage simplifies this process by:

 Identifying the type of emergency through text or voice input.  Finding suitable hospitals based on real-time bed availability.  Prioritizing the patient's preferred hospital and nearby options.  Reserving an available bed to reduce the risk of double booking. Sending instant booking and arrival notifications to the patient and hospital.  Connecting the patient with a doctor for pre-arrival guidance when available. Providing alternative hospitals if the selected hospital becomes unavailable. 

This reduces unnecessary hospital-to-hospital searching and helps patients reach appropriate emergency care faster, with better information and coordination when every second matters.

Team **HackOrbit** -- [Samprit Majumdar](https://github.com/samprit0012), [Pritam Ghosal](https://github.com/pritamghosal), [Rajdeep Ghosh](https://github.com/rajdeep_ghosh2910), Swarnaja Dey

`2026-08-29`

---

### Robtor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/robtor-a51f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://Robtor.me) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/p50A3V3MORE?si=amZmUjZG9rIv711M) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co)

> Your health matter that's why we are here to make

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Millions of people track their health data across disconnected silos — wearables show heart rate and sleep, lab reports sit in PDFs on a phone, and neither talks to the other. Nobody connects the dots, so early warning signs get missed until a routine checkup (or an emergency) catches them.

Robtor is an AI-powered personal health assistant that fuses wearable biometrics with clinical lab reports to give people a real correlation between how they feel and what their numbers actually say — without needing a doctor to interpret every report.

For long-term care engagement specifically, Robtor helps people:
- Track chronic markers (like blood sugar, BP, cholesterol) alongside daily biometric trends instead of only during doctor visits
- Get plain-language guidance ("guide, don't diagnose") that keeps them engaged with their own health day-to-day, not just once a year
- Trigger emergency alerts (via WhatsApp) automatically when vitals cross critical thresholds, even without a wearable, using just phone sensors

It works even without dedicated hardware — but we've also built an ESP32-based Robtor Pod prototype for continuous ambient monitoring, for people who want a step further.

**Challenges we ran into**

Building Robtor solo (no CS background, learning to code alongside a full-time B.Pharm course) came with real technical hurdles:

- **AI provider reliability**: Early on, a single AI provider would randomly fail mid-session. I built a multi-provider fallback chain (Groq → Gemini) so the assistant degrades gracefully instead of breaking.
- **Wearable data integration**: Getting Health Connect data to sync reliably with Supabase took several iterations — I hit a missing `hasProfile` method bug in the native plugin layer that silently broke onboarding, which took real debugging to trace.
- **Hardware side**: Flashing and stabilizing the ESP32 Robtor Pod (mic + amp + heart-rate sensor) meant resolving GPIO conflicts and audio glitches from scratch, with no formal EE background to lean on.
- **Emergency logic correctness**: I initially had the wrong emergency number hardcoded (911 instead of 112 for India) — a small bug with real-world consequences if shipped, caught during testing.

The common thread: building alone means you're the only line of defense against your own blind spots, so I leaned heavily on rigorous self-testing and treating every edge case (a 0 bpm reading, a missing API key, a silent plugin failure) as something that could hurt a real user if ignored.

love agarwal

`2026-08-20`

---

### AI health record translator
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-health-record-translator-6770) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shruti-Rout14/ai-health-record-translator.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-health-record-translator-amber.vercel.app/account) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1220487270?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co)

> Your lab reports, explained like a friend would.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**Challenges we ran into**

The biggest hurdle was making the AI extraction actually reliable. Early on, our OCR pipeline was silently returning fabricated demo data instead of really reading the uploaded image, which we only caught by comparing the output against the real report line-by-line. We also hit repeated Gemini model deprecations mid-build (older model versions were retired without warning) and had to update our API calls to the current model. On the infrastructure side, Vercel's build-time environment variable handling caught us off guard — Vite bakes env vars in at build time, so simply adding a key in Vercel's dashboard didn't work until we triggered a fresh, cache-cleared redeploy. We also had to properly configure Supabase Row Level Security so users could only ever see their own reports, not just filter it in the UI.

**The problem it solves**

Medical lab reports are full of technical jargon that most people can't easily interpret — leaving them either panicking over normal-looking numbers or ignoring genuinely concerning results. AI Health Record Translator lets anyone upload a blood test, lipid panel, or general lab report (as a photo or PDF) and instantly get it explained in plain, everyday language. It highlights which values are outside the normal range, generates specific questions to ask a doctor, and tracks how your health metrics change over multiple reports over time — so people can walk into a doctor's appointment informed instead of anxious, and catch trends they'd otherwise miss.

Team **Sirius** -- Shruti Rout, Siddhi Muthal

`2026-08-22`

---

### cure cloud
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cure-cloud-7084) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yuvaranjan/Vaidhya_PEC) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1OUymdkIQ3W2g6eUQvRY6wMLssyGdkeXu?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> making health care a right not a luxury

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Vaidhya is a complete healthcare system designed specifically for rural India. It is built to overcome critical barriers such as low network connectivity, shortage of doctors, and lack of digital literacy when interacting with complex digital healthcare systems. Vaidhya aims to bring accessible, affordable, and quality healthcare  to people living in underserved areas.

It brings AI directly into rural healthcare through the following core capabilities:

1. Multilingual Voice-First Offline AI Diagnostic Engine:
Vaidhya allows patients to describe their symptoms through voice in their preferred language, making healthcare more accessible to people with limited digital literacy. The system understands the reported symptoms, analyzes the collected vital signs, and generates a structured pre-consultation report even before the doctor consultation begins. This helps identify possible conditions, highlight critical symptoms, and organize relevant patient information for the doctor, enabling faster and more informed decision-making.

2. Agentic AI for Specialist Perspectives:
For complicated cases, Vaidhya uses multiple specialized AI agents to analyze the same patient case from different medical perspectives, such as cardiology, neurology, and respiratory care. These agents provide specialist-oriented insights and possible clinical considerations, supporting doctors in making better-informed decisions, especially in areas where access to specialists is limited. The final decision always remains with the qualified healthcare professional.

3. Disease Outbreak Prediction:
Instead of focusing only on individual patients, Vaidhya also analyzes community-level symptom patterns. A sudden increase in similar symptoms across multiple patients can help identify unusual health trends and potential disease outbreaks at an early stage, allowing healthcare workers to respond proactively.

4. Real-Time Medicine Availability Check:
Before finalizing a prescription, the doctor can verify medicine availability against real-time pharmacy and health-centre inventory. This helps ensure that prescribed medicines are actually accessible to the patient, reducing unnecessary repeat visits and delays in treatment.

5. Low-Bandwidth & Offline-First Design:
Vaidhya is designed specifically for environments with unstable internet connectivity and limited digital infrastructure. Its offline-first architecture and MQTT-based lightweight communication allow essential healthcare data and AI-assisted workflows to function reliably even in low-bandwidth environments.

Together, these capabilities transform Vaidhya from a conventional telemedicine platform into an AI-powered, offline-first healthcare infrastructure for rural communities, connecting patients, nurses, doctors, pharmacies, and community-level health monitoring in a single system.

**Challenges we ran into**

Building Vaidhya involved several challenges, especially because we wanted the system to work reliably in an offline rural healthcare setting, rather than assuming constant connectivity.

Our first hurdle was integrating hardware for vital-sign collection and keeping the readings synchronized with the patient record, particularly when the device temporarily lost connectivity. We also had to improve the state awareness of our local edge AI model so that its questions changed based on what the patient had already said. This was especially challenging offline, where the model had to ask relevant, complaint-specific follow-up questions without relying on a cloud model.

Another major challenge was the outbreak prediction system. Getting enough reliable, geographically relevant symptom data to identify meaningful patterns was difficult, and we could not simply test an outbreak prediction system by waiting for a real outbreak. We addressed this by working with available datasets and simulated/local patterns to test whether the system could detect changes in symptom trends and generate meaningful signals.

**Best Use of Render**

Providing a Frictionless Foundation: We leveraged Render to completely eliminate infrastructure headaches. It gave us a rock-solid, zero-maintenance
  environment that allowed the team to focus purely on building the product rather than configuring servers.
  • Handling the Heavy Lifting: We relied heavily on Render’s robust architecture to manage secure, high-speed backend uploading. It ensured that moving
  large files or handling heavy data payloads remained entirely seamless and invisible to the user.
  • Scaling Effortlessly: As our application's traffic grew and backend demands spiked, Render's automatic scaling capabilities ensured we maintained
  peak performance without missing a beat, guaranteeing high availability around the clock.

**Best Use of n8n**

Orchestrating the "Nervous System": Instead of writing endless, fragile glue code to connect our services, we used N8N as the central nervous system
  of our platform. It allowed us to visually design and execute complex, multi-step workflows.
  • Creating Resilient Automations: We transformed messy background processes into clean, reliable pipelines. N8N ensured that data flowed seamlessly
  between our disparate APIs without requiring manual intervention or constant babysitting.
  • Accelerating Development: By visually automating routine tasks and data syncing, we drastically cut down our development time. This allowed the
  engineering team to focus on building core, user-facing features rather than untangling infrastructure wiring.

**Best Use of Gemini API**

Enabling proactive, data-driven policy making and resource allocation before issues escalate. Simultaneously, it benefits the people of India by translating these complex predictive models into accessible plain language insights, empowering the citizens to make informed decisions and forecasting greater seismic transparency.

**Best Use of Actian Vector Database**

Giving the System "Intuition": We moved beyond rigid, exact-match keyword searches. By storing our data as vectors, we gave the application the
  ability to actually understand the semantic intent behind a user's request, surfacing what they meant, not just what they typed.
  • Powering Contextual Memory: The Vector DB acts as the long-term memory bank for our AI components. It empowers the system to instantly retrieve
  highly relevant past knowledge, ensuring responses are deeply informed and tailored to the specific situation.
  • Lightning-Fast Retrieval at Scale: Even as our underlying knowledge base grew massively, the Vector DB ensured that searching through complex,
  unstructured data remained instantaneous, maintaining a snappy experience for the end user.

Team **Cure Cloud** -- [Avannthika Ranganathan](https://github.com/avannthika-coder), [Yuvaranjan N](https://github.com/yuvaranjan), [Nidyashree ThulasiRaman](https://github.com/NidyaShree), [Mohith B](https://github.com/MOHITH246)

`2026-08-30`

---

### DiagnOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/diagnos-6b6b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aldenbl635-oss/DIAGNOS.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=W3U1osFWmSA) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Clinical Reasoning over Clinical Recall

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Problem:  Imagine you are a medical student who has enough theoretical knowledge and has worked with fact recollection and objective questions but does not have enough patient encounters. 

India adds roughly 130,000 new medical students every year.
Every one of those future doctors needs repetition on clinical reasoning but real patients aren't available on demand.

We give every student  - repeated practice, a patient who's always available, a low stake and safe environment

**Challenges we ran into**

One of the key challenges encountered during the development of the chat interface was the initial choice of a keyword-based matching approach for understanding user queries. While this method worked reasonably well for simple, single-keyword inputs, it proved inefficient when handling more complex questions containing multiple keywords. In such cases, the system often failed to identify the correct intent, as it could not effectively interpret the relationships between the different keywords within a single query, leading to inaccurate or irrelevant responses. To resolve this issue, we transitioned from a purely keyword-based approach to using embeddings, which represent words and sentences as dense vectors capturing their semantic meaning and contextual relationships. This allowed the system to understand the overall intent of a query rather than relying on isolated keyword matches, significantly improving the accuracy and relevance of the chatbot's responses, even for more complex or multi-keyword questions.

**Best Use of Actian Vector Database**

By moving from keyword matching to Actian Vector DB, DiagnOS transforms from a rigid keyword-checking script into an intelligent, semantic clinical reasoning engine. It enables conversational freedom during patient interviews, millisecond-level bedside empathy classification, and nuanced evaluation of diagnostic justifications.

The key point is that Actian isn't an add-on to DiagnOS — it directly solves the fundamental limitation of our original system. Clinical communication is inherently semantic, and DiagnOS needs semantic retrieval at its core.

That makes DiagnOS an especially strong demonstration of Actian Vector DB: instead of merely storing embeddings, we use vector search to make an AI clinical simulation more flexible, contextual, and clinically meaningful.

Team **Medical Miracle** -- [Darshanaa Shunmugaraja](https://github.com/darshanaa-005), [Alden BL](https://github.com/aldenbl635-oss), [Sharada Shree_G](https://github.com/sharadashreeg-wq), [RIYANA FERNANDO](https://github.com/riyanafernando647-lang), [Joshan Anto](https://github.com/joshananto1234)

`2026-08-30`

---

### smart queue management
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-queue-management-1c7d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shivam1716/project1.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://queue-manage.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Smarter Queues, Better Healthcare. ⭐

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Hospitals often face long waiting times, overcrowded waiting areas, and inefficient patient flow. Patients usually have to stand in physical queues without knowing how long they will have to wait. This can lead to frustration, wasted time, and difficulty in managing emergency cases.

A Smart Queue Management System addresses these issues by digitizing and automating the queue process. It assigns tokens, estimates waiting times, and prioritizes patients based on appointment schedules or emergency levels. The system also provides real-time updates, reducing confusion and improving the overall hospital experience.

**Challenges we ran into**

## Challenges I Ran Into

While developing the **Smart Queue Management System**, I encountered several challenges during implementation:

### 1. Real-Time Queue Updates

Keeping the queue updated for all users in real time was challenging. Initially, changes made by the hospital staff were not reflected immediately on the patient side. I resolved this by using real-time database synchronization so that queue positions and waiting times update instantly.

### 2. Accurate Waiting Time Estimation

Estimating waiting times was difficult because consultation durations vary from patient to patient. Instead of using a fixed value, I implemented an algorithm that calculates estimated waiting time based on the average consultation time and the current queue length.

### 3. Managing Priority Patients

Handling emergency and senior citizen patients without disrupting the overall queue was another challenge. I solved this by implementing a priority-based queue that allows urgent cases to move ahead while keeping the queue fair for other patients.

### 4. Database Consistency

When multiple users booked appointments simultaneously, there was a risk of duplicate tokens or conflicting data. I addressed this by using unique token generation and database validation to ensure each patient receives only one valid queue number.

### 5. User-Friendly Interface

Designing an interface that was simple for both patients and hospital staff required several improvements. After testing the application, I simplified the navigation, added clear status indicators, and improved the overall layout for better usability.

### 6. Testing Different Scenarios

Testing the system under various conditions, such as multiple simultaneous bookings, cancellations, and emergency cases, helped identify edge cases and improve the reliability of the application.

These challenges provided valuable experience in problem-solving, database management, and designing scalable, user-friendly healthcare applications.

[SHIVAM SINGH](https://github.com/shivam1716)

`2026-06-29`

---

### Health Twin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/health-twin-031b) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

[Aditi Sharma](https://github.com/sharmaaditi4482-source)

`2026-07-30`

---

### Mental health chatbot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mental-health-chatbot-9e54) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

Team **ERROR 404** -- [ANARANYA MONDAL](https://github.com/ANARANYA-GIT), [Debalina Samanta](https://github.com/titli81639q7)

`2026-07-30`

---

### Ai  smart healthcare
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-smart-healthcare-6c56) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

Utsav Raj

`2026-07-30`

---

### Scan Saarthi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scan-saarthi-a455) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/epsilon-rbtcs/ScanSaarthi) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Patients, Caretakers and Healthcare Professionals

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Auth0](https://img.shields.io/badge/Auth0-333333?style=flat-square)

**Challenges we ran into**

We tried our best to integrate hardware yubikey-fido2 for validation login of dementia patients but due to time constraints and some unexpected errors we weren't able implement it, so we have implemented demo credentials temporarily so that other features can still be explored. 

We also encountered challenges in making the backend as it was not as intended and was causing problems when tried to connect with frontend, which was disastrous and took us 2 hours to fix the bugs and also making minor changes in frontend instead of redesigning the entire frontend.

**The problem it solves**

ScanSaarthi is an AI-powered brain health platform designed to make early cognitive health screening more accessible, understandable, and proactive. It helps address the challenges of delayed diagnosis, limited access to specialists, and the complexity of interpreting brain MRI scans by providing AI-assisted MRI analysis with explainable visualizations and simplified reports for which 2 CNNs were trained locally on 75k+ research grade dataset.

The platform also includes daily cognitive assessments that evaluate memory, attention, and reasoning, allowing users to track changes over time through a personalized Brain Health Passport.

Beyond screening, Scan Saarthi enables patients to book appointments with neurologists, securely communicate with doctors, and maintain a centralized record of their reports and assessments. By combining AI-powered analysis, continuous cognitive monitoring, and integrated healthcare services, ScanSaarthi supports patients and healthcare professionals in making more informed decisions while complementing, not replacing, clinical diagnosis.

**Healthcare**

Our project aims to build a platform that connects patients, caretakers and doctors, automating and easing all the medical checkup process and decrease the time taken for the patient to get diagnosis from the doctor. Currently we are focusing on dementia related patients who can scan their mri, our model will analyze it and generate reports on their stage of dementia which then can be downloaded and shared to nearby doctors and send request for consultation, That's why we are participating in Healthcare track too.

**Best Beginner's team**

This is our first hackathon and we are students who just completed our first year, that's why we are participating in beginner's track.

Team **Team CrixSparks** -- [Ankit Bhadra](https://github.com/epsilon-rbtcs), [Anubhav Sharma](https://github.com/ianubhavsharma05)

`2026-07-26`

---

### Asha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/asha-bd0e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/GautamRaju18/ASHA) [![Built at](https://img.shields.io/badge/Built%20at-Tech%20Genesis%20'26-0052CC?style=flat-square)](https://tech-genesis.devfolio.co)

> AI triage for the last mile of healthcare

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

1. Keeping it grounded, not hallucinating. The core risk in any medical assistant is a confident wrong answer. We had to design the retrieval pipeline and prompting so the agent can only recommend what a retrieved protocol passage supports - and explicitly fall back to "refer" when the protocols don't cover the case - instead of drawing on the model's general "knowledge."
2. Building the danger-sign hard-override. Triage from an LLM alone felt unsafe, so we added a separate danger-sign screening node that runs alongside the main reasoning and can override it to force a referral. Getting that override to fire reliably from corpus-matched red flags- even when the main reasoning was uncertain or disagreed - was the trickiest piece of safety logic in the graph.
"No hardcoding" vs. predictable safety. We wanted triage decisions reasoned dynamically from the protocols rather than baked into if-else rules, but medical software can't be unpredictable. Balancing that flexibility against safe, repeatable behaviour took several iterations of the agent design and prompts.
3. Messy multilingual input → clean structure. Real workers type code-mixed regional language, not tidy English. Reliably extracting a structured symptom profile (age, duration, danger signs) from that - and returning the full answer back in the same language - was far harder than a clean-English demo.
4. Chunking medical protocol tables. IMNCI danger-sign checklists are tables, and naive chunking split them mid-row and broke retrieval. We had to preserve those rows as atomic chunks with the right metadata so the danger-sign screen could match them.
5. Geolocation, HTTPS, and free facility data. Browser geolocation only works over HTTPS and needs explicit consent, so we built a manual district-entry fallback for denials — and used the free OpenStreetMap Overpass API with Leaflet for facility lookup and mapping instead of a paid maps service.

**The problem it solves**

India's healthcare reaches its last mile through nearly a million ASHA workers — the accredited frontline health workers who are the first, and often the only, point of contact for a village. They're trained community workers, not clinicians, yet they're the ones who first see the feverish infant, the breathless child, or the pregnant woman with a warning sign. The hardest part of their job is also the most consequential: deciding whether what's in front of them is something to manage at home or an emergency that needs an immediate referral. A missed danger sign — fast breathing in a child, a newborn who won't feed — can cost a life, and that call gets even harder across language barriers and thick protocol booklets that are impractical to flip through at a patient's doorstep.
ASHA Sahayak is an AI clinical decision-support web app built for exactly that moment. A worker describes the patient's symptoms in plain or regional language — typed or spoken — and the system reasons over official public-health protocols (IMNCI, NHM/ASHA guidelines, WHO IMCI) using retrieval-augmented generation to return, in seconds: a clear triage level, the conditions the symptoms are consistent with, concrete next steps within the worker's scope, and — most importantly — an explicit REFER flag whenever danger signs are present. Everything comes back in the worker's own language, with the source protocol cited for every recommendation. Once a case needs referral, the app uses the worker's location (captured with consent at login) to surface the nearest appropriate facility — a PHC/CHC for routine cases, a higher-tier hospital for emergencies — on an OpenStreetMap map with distance and one-tap directions. Symptom → triage → referral → nearest health centre, end to end.
What makes it safe rather than a guessing chatbot is the architecture. Every output is grounded in a retrieved protocol passage — the model is never allowed to freelance medical advice, and if the protocols don't cover a case, it defaults to referral. A dedicated danger-sign node runs in parallel to the main reasoning and hard-overrides it: if any protocol-defined red flag matches the case, the system forces a referral regardless of what the rest of the reasoning concluded. The whole system is biased toward caution, and it's framed throughout as decision support that backs a trained worker's judgment, never a diagnosis that replaces it. Nothing is hardcoded — symptoms, danger signs, and triage thresholds all come from the protocol corpus and are reasoned over on the spot, so the same engine extends to new conditions just by adding protocols.

Team **proc.ai** -- P Aneesh, Angajala Gautam Raju, Bachchu Shreyansh, PSP Srikar

`2026-06-27`

---

### HealthAssist
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/presentation-71c4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/blesstonjeffrin/Disease-Prediction-frontend) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nk0TheMouwA) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> A friendly ai for health assist in seconds

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Building the Disease Prediction System came with several technical and conceptual hurdles:

    Sourcing Reliable Medical Data: One of our primary challenges was finding high-quality, reliable, and structured medical datasets to train our machine learning models. We initially struggled with inconsistent data formats which led to inaccurate risk predictions. We overcame this by implementing a rigorous data cleaning pipeline and cross-referencing our training data with standardized public health databases to ensure higher confidence scores.

    Dynamic Conversational Flow: Creating a chatbot that didn't just provide static answers but actually "listened" and asked relevant follow-up questions was difficult. Our early prototypes often lost context during a conversation. We solved this by refining our prompt engineering for the OpenAI API and implementing a state-management system to track symptom progression, allowing the bot to ask clinically relevant questions based on the user's previous inputs.  

    Language-Specific NLP: Implementing robust support for the Tamil language proved tricky due to varying dialects and limited specialized medical terminology in existing open-source libraries. We addressed this by integrating custom translation layers and fine-tuning our intent-recognition logic to handle colloquial symptom descriptions, making the experience feel natural for local-language users

**The problem it solves**

This project addresses significant gaps in current preventative healthcare and accessibility. People can use this system to receive personalized health recommendations and early disease detection in seconds, rather than waiting until symptoms become severe.  

It makes existing healthcare tasks easier and more accessible through:

    Conversational Guidance: Instead of manually searching for symptoms and receiving confusing, generic results on Google, users engage with a friendly, AI-powered chatbot that dynamically asks follow-up questions.  

    Reduced Friction: By supporting both voice and text input, the system lowers the barrier for users who may find manual data entry difficult.  

    Localized Access: By supporting English and Tamil, it ensures that the tool is accessible to a wider demographic, including those in rural areas.  

    Actionable Insights: Unlike many basic apps, this system provides instant risk assessments (Low, Moderate, High), generates personalized precautions, and triggers doctor consultation alerts when necessary, providing users with clear next steps.

Team **Giggity giggity** -- [Shiva Duttan](https://github.com/nothing), [Blesston Jeffrin Kingston](https://github.com/blesstonjeffrin), [Mukesh Raj](https://github.com/mukesh-5059), Yogarisi Karthik

`2026-06-14`

---

### Healthi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthi-887a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aadhyanthk/Healthi) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://healthi.web.app) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Remember Less. Know More. Live Better.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

"Simple to use, powerful in impact".

Healthi helps elderly individuals and people managing chronic conditions keep track of their health without the complexity of traditional health apps that use "ai". Many patients struggle to remember symptoms, medication adherence, or sleep patterns when visiting a doctor, leading to incomplete medical context and less informed decisions.

Healthi makes existing health-tracking tasks:

- Easier by simplifying daily logging and record keeping.
- Safer by ensuring important health information is not forgotten.
- More insightful through AI-powered pattern detection and summaries.
- More accessible with an elderly-friendly design and simplified workflows.
- More useful for healthcare professionals by providing organized timelines and contextual reports during consultations.

To be precise, it's:
A frictionless, AI-powered health ledger for seniors. Turns everyday language into a clear, clinical health timeline that patients, families, and doctors can understand together

**Challenges we ran into**

One of our biggest challenges was getting all the different services to work together smoothly. While integrating AI features, we frequently ran into Firebase issues caused by changes to Firestore security rules, which sometimes blocked access to data unexpectedly.

Authentication was an issue when the service suddenly stopped working when we tried to deploy it AGAIN, just to make sure the ai part is actually working, which led to a lot of manual debugging and waste of time in Google OAuth.

As a team, we also faced our fair share of GitHub merge conflicts. With multiple people working on authentication, AI integration, and database logic simultaneously, merging changes occasionally became messy and required manual fixes.

Despite these challenges, we were able to resolve them through debugging, better branch management, and a lot of testing.

What we thought would be a simple app to build actually took us SO MUCH more time to build and debug, but maybe the real journey was the commits we made along the way.

Team **MR BEAN CREW** -- [Aadhyanth K](github.com/aadhyanthk), Kishore Kumar, Anush V

`2026-06-14`

---

### ElderCare+
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eldercare-5c93) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/akshitabansal07/ElderCare-plus) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BRfeKBHpZeM) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Everything Seniors Need for Better Healthcare

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

When it came time to publish our code to GitHub, we hit an unexpected wall.
The export options didn't cooperate — zip downloads failed, the built-in Git integration wouldn't push to our repository, and even the CLI couldn't get the job done cleanly.
So,we manually copied every file and its contents, one by one, directly into the GitHub repository through the web interface. Tedious, but it worked.

**The problem it solves**

**ElderCare+** is a voice-first healthcare companion built for elderly users in India, supporting both Hindi and English. It is a single app replacing the need to call a family member, search the internet, and re-read a confusing report — in the language you actually speak.

**Key Features**
**-->Voice Input**— Speak instead of type. No small keyboards, no autocorrect. Ideal for users with arthritis, tremors, or low vision.
**-->Bilingual (Hindi + English)** — Doctors write in English, seniors think in Hindi. ElderCare+ bridges that gap so no family member is needed to "translate."
**-->Symptom Guidance** — Describe how you're feeling and get a clear, plain-language response — safer than random Googling, less panic-inducing than guessing.
**-->Medical Report Analysis** — Upload a lab report and understand what HbA1c or creatinine actually means, in your own language, before your next doctor visit.
**-->Medication Management** — Track multiple medicines, get reminders, and understand what each one is for — reducing dangerous missed or doubled doses.

Team **jeevan** -- Swanand Kanthale, Akshita Bansal, Shubh Garg

`2026-06-14`

---

### LifeXP
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifexp-fddd) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://frontend-deploy-lifexp.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Your Health, Your XP

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![expo.io](https://img.shields.io/badge/expo.io-333333?style=flat-square)

**The problem it solves**

## Key Features

- Patient and doctor registration flow
- Family member tracking and health grouping
- Personalized dashboard with daily wellness data
- Doctor reports and recommendations for medicines, workouts, and nutrition
- Analytics view for health trends over time
- In-app notifications and AI chat assistant
- Expo mobile app with cross-platform support for Android, iOS, and web

**Challenges we ran into**

# Challenges Faced During Development

## 1. Cross-Platform Compatibility

One of the biggest challenges was ensuring that the application worked seamlessly across Android devices and web browsers using a single codebase. Certain components behaved differently on web and mobile, requiring additional testing and optimization.

## 2. Backend Integration

Connecting the React Native frontend with the Node.js and Express backend required careful API design and testing. Managing API endpoints, handling errors, and ensuring smooth communication between the frontend and backend was a significant challenge.

## 3. Database Management

Designing an efficient database structure for storing user activities, health metrics, and progress data while maintaining scalability and performance required multiple iterations.

## 4. AI Integration

Integrating Gemini AI into the application involved handling API requests, response formatting, and ensuring that the AI-generated health recommendations were relevant and useful to users.

## 5. Deployment Challenges

Deploying the backend on Render and the frontend on Vercel required configuration adjustments, environment variable management, and troubleshooting build issues to ensure successful production deployment.

## 6. Time Constraints

As the project was developed within a hackathon environment, balancing feature development, testing, debugging, and deployment within a limited timeframe was a major challenge.

## 7. User Experience Design

Creating a gamified health-tracking experience that was both engaging and intuitive required multiple UI/UX iterations. The challenge was to motivate users without overwhelming them with information.

## Key Learnings

* Effective API design and integration.
* Cross-platform application development with Expo.
* Cloud deployment and environment configuration.
* AI-powered feature implementation.
* Team collaboration and rapid problem-solving under time constraints.

Despite these challenges, the team successfully developed **Life XP**, a HealthTech platform that transforms healthy habits into an engaging and rewarding experience through gamification and AI-powered insights.

Team **Axiom** -- [Amandeep Kujur](https://github.com/aman-bot06), Muskan Verma, [Vivek Darro](https://github.com/vivekx911)

`2026-06-14`

---

### Hospital Information System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hospital-infromation-system-1ad8) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://his-core.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> One unified web app that digitizes every hospital

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Razorpay](https://img.shields.io/badge/Razorpay-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Clerk](https://img.shields.io/badge/Clerk-333333?style=flat-square) ![gemini](https://img.shields.io/badge/gemini-333333?style=flat-square) ![Metriport](https://img.shields.io/badge/Metriport-333333?style=flat-square)

**The problem it solves**

Main Problems Solved by HIS Core
1. Fragmented Hospital Workflows
Unified clinical (doctors, nurses), administrative (reception, billing), and patient-facing operations into a single platform with role-based dashboards.

2. Insecure Patient Data Access
Implemented Row-Level Security (RLS) in PostgreSQL and RBAC via Clerk, ensuring users can only access data they're authorized to see (HIPAA-aligned).

3. Double-Bookings & Invalid Appointments
Used Zod validation and server-side checks to prevent scheduling conflicts and ensure data integrity before writes.

4.  AI Assistants
Built a context-aware AI chat (Groq/Gemini) that injects real patient records — appointments, medications, radiology — into the system prompt, making it clinically useful instead of generic.

5. Emergency Response Coordination
Integrated a real-time map (Leaflet.js) with geolocation and ambulance fleet tracking, solving the SSR hydration mismatch with a useMounted pattern.

6. Data in Dashboards
Replaced hardcoded metrics with live SQL aggregations — real revenue from invoices, real appointment counts, real patient totals — displayed via Recharts.

7. Digitizing Handwritten Records
Used Tesseract.js OCR to convert handwritten prescriptions and medical notes into searchable digital text.

**Challenges we ran into**

Challenges Encountered During Development
1. Hydration Mismatch (SSR vs. Client)

Leaflet.js requires the window object, which doesn't exist during server-side rendering. The map component would crash or produce mismatched HTML. Fixed with a custom useMounted hook that defers rendering until after client-side mount.
2. RLS Policies Blocking Legitimate Queries

Row-Level Security was too restrictive — authenticated users couldn't read patient data, and the service role couldn't insert new users on signup. Required multiple fix scripts (fix-duplicates-and-rls.sql, fix-user-insert-policy.sql) to get the policies right.
3. Dashboard Stuck on Mock Data

SQL migrations ran successfully, but the admin dashboard still displayed hardcoded values ($45.2K revenue). Root cause: the invoices table schema was missing columns (description, invoice_date) that dashboard.ts was querying, causing silent failures that fell back to mock data.
4. Column Mismatch Between Schema & Code

Server actions referenced non-existent columns like appointment_time. Required a full audit of every query in dashboard.ts to align it with the actual database schema.
5. Duplicate Patient Records

Seed scripts could be run multiple times, creating duplicate rows. Fixed with a deduplication query using ROW_NUMBER() OVER PARTITION BY and making seed scripts idempotent — inserting only if the table is empty.
6. Missing Table Columns in Production

The patients table lacked uhid, is_verified, and govt_id_type columns needed by newer features. Required an ALTER TABLE migration with backfill logic in supabase_fix.sql to generate UHIDs for existing records.
7. Clerk ↔ Supabase Identity Sync

Users authenticated through Clerk had no corresponding row in the Supabase users table, breaking foreign key relationships for appointments and invoices. Solved with a syncUser() function that runs on every login.
8. Non-Idempotent Migrations

Early SQL scripts would fail or create bad state if run more than once. Refactored all scripts to use IF NOT EXISTS, DROP IF EXISTS, and conditional inserts to make them safely re-runnable.

Team **Commit  & Quit** -- [Omar Hashmi](https://github.com/omar-h-Hashmi-rgb), [Kaustubh Neoge](https://github.com/KaustubhNeoge), [Jeel Kathiria](https://github.com/Jeelkathiria)

`2026-06-14`

---

### MedLens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medlens-4b50) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HackerzPrashant/MedLens-AI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/eJgm27f4NSI) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Clinical Symptom Assessment Portal

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square)

**The problem it solves**

Many people experience symptoms such as fever, cough, headache, fatigue, or stomach pain but are unsure about the possible cause or whether the condition requires immediate medical attention. Searching symptoms online often leads to confusing, unreliable, or overwhelming information.

This platform helps users by analyzing the symptoms they provide and estimating the likelihood of various medical conditions. It presents the results in an easy-to-understand format, including possible diseases, their probability, severity level (mild, moderate, or severe), and recommended precautions.

The system can be used to:

* Gain quick insights into possible health conditions.
* Understand whether symptoms may require urgent medical attention.
* Learn basic precautions and self-care measures.
* Reduce time spent searching through multiple websites for information.
* Encourage users to seek professional medical advice when necessary.

By providing organized and personalized symptom analysis, the platform makes preliminary health assessment faster, more accessible, and more informative while supporting better health awareness and decision-making.

**Challenges we ran into**

# Challenges We Ran Into

One of the biggest challenges was accurately predicting possible diseases from user-provided symptoms. Many diseases share similar symptoms, making it difficult to determine which condition is the most likely. For example, symptoms such as fever, fatigue, and headache can be associated with multiple illnesses.

To address this issue, we improved the symptom-processing logic and used probability-based predictions instead of attempting to identify a single disease. This allowed the system to present multiple possible conditions along with confidence percentages, giving users a more realistic assessment.

Another challenge was handling incomplete or unclear symptom descriptions. Users often describe the same symptom in different ways or may forget to provide important details. We solved this by normalizing user input, matching similar symptom terms, and validating the data before running predictions.

We also faced difficulties in determining the severity of a condition. Simply predicting a disease was not enough; the system needed to indicate whether the situation appeared mild, moderate, or severe. We overcame this by creating severity rules based on symptom combinations and providing precautionary guidance alongside the predictions.

Through testing, refinement, and continuous debugging, we improved the reliability, usability, and overall user experience of the platform.

Team **Gladiator** -- [Parshant Gulia](https://github.com/HackerzPrashant), Shaurya Singh, Atul Gulia

`2026-06-14`

---

### MedEase
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medease-407f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shamhithar/HealthBuddy-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://9000-firebase-studio-1781337654426.cluster-m7dwy2bmizezqukxkuxd55k5ka.cloudworkstations.dev) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XzRexlYn_XY) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> An AI-powered healthcare companion

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

MedEase is a AI-powered healthcare companion which helps people understand prescriptions, manage medications, and stay on track with their health. It simplifies complex medical information, provides AI-powered health guidance, sends medication reminders, and keeps important health records organized in one place, making healthcare more accessible and easier to manage.

**Challenges we ran into**

One of the biggest challenges we faced was integrating AI-powered prescription analysis and symptom checking. We encountered issues with file uploads, API configuration, and AI processing failures. Through debugging, improving error handling, and refining the data flow, we successfully resolved these issues and ensured that prescriptions, medications, reminders, and health records worked seamlessly together within MedEase.

Team **Code Triad** -- Lakshay S, Harsika Selvakumaran, SHAMHITHA R

`2026-06-14`

---

### Privamed-Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/privamedai-de6b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/preet1802yadavemailcom-design/PrivaMed-Hackathon) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

> Privacy-First AI Healthcare Intelligence

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🫀 PrivaMed AI
Privacy-First AI Healthcare Intelligence
 Hackathon 2026 · AI Track
"Powerful AI health triage — without seeing a single byte of your medical data."

Midnight Network Track Privacy License

The Problem
1 in 3 people avoid seeking health advice online due to privacy concerns.

Traditional health AI requires uploading symptoms, vitals, and medical history to a server. Even "private" solutions rely on trust — you're trusting a company with your most sensitive personal data.

Public blockchain health apps are even worse: your medical history is on a permanent, public ledger forever.

PrivaMed AI solves this at the cryptographic level, not the policy level.

What We Built
PrivaMed AI is a privacy-preserving medical triage platform that uses zero-knowledge proofs to protect sensitive health data. that uses zero-knowledge proofs to assess health risk without exposing any personal medical data — to anyone, including the AI.

┌─────────────────────────────────────────────────────────────────┐
│                        Your Device (Private)                    │
│                                                                 │
│  Symptoms    →  [witness]  ─┐                                   │
│  Vitals      →  [witness]  ─┤→ [ZK circuit] → risk: "HIGH"    │
│  Age         →  [witness]  ─┤                        │         │
│  Conditions  →  [witness]  ─┘                        │         │
│                                                       │         │
│  (NOTHING ABOVE EVER LEAVES THIS BOX)                │         │
└───────────────────────────────────────────────────────┼─────────┘
                                                        │ proof only
                                               ┌────────▼────────┐
                                               │ Privacy Ledger │
                                               │ +1 to counter   │
                                               │ (no PII)        │
                                               └────────┬────────┘
                                                        │ "HIGH"
                                               ┌────────▼────────┐
                                               │     AI Model    │
                                               │ (never sees your│
                                               │  raw symptoms)  │
                                               └─────────────────┘
How It Works
Step 1: Private Witnesses (Local)
Your health inputs are computed as Compact witness values on-device — these are the private inputs to the ZK circuit and never leave your browser.

witness age_group(): Uint<8>;          // bucketed: 0=child, 1=adult, 2=senior
witness symptom_score(): Uint<8>;      // aggregated severity 0-100
witness vital_risk_score(): Uint<8>;   // deviation from clinical norms 0-100
witness chronic_flag(): Boolean;       // has chronic condition (binary flag only)
witness vaccination_status(): Boolean; // vaccinated (binary flag only)
Step 2: ZK Circuit (Local)
A Compact circuit runs locally using the PLONK proving system over BLS12-381. It computes your risk classification without exposing the inputs.

export circuit assess_risk(): AssessmentResult {
  const ag = age_group();
  const ss = symptom_score();
  const vs = vital_risk_score();
  
  assert ag <= 2;
  assert ss <= 100;
  assert vs <= 100;
  
  const raw = ss * 40 / 100 + vs * 35 / 100 + age_factor(ag) + chronic_factor();
  const level = classify(raw);
  
  disclose level;  // ← only this leaves the circuit
}
Step 3: Shielded Ledger Update
Only the cryptographic proof and anonymous counters are written to the Privacy Ledger. No PII, no symptoms, no vitals.

ledger total_assessments: Uint<64>;
ledger high_risk_count: Uint<64>;
ledger medium_risk_count: Uint<64>;
ledger low_risk_count: Uint<64>;
// ✗ NO personal data fields
Step 4: AI Recommendation
The AI model receives only the risk classification — never raw health data. This is ZK-gated AI: powerful intelligence with zero privacy cost.

Privacy Comparison
Approach	Data on Server	On-Chain Privacy	AI Privacy	GDPR
Traditional Health App	All data	N/A	Sees everything	⚠️ High risk
Public Blockchain DApp	All data	✗ Exposed	Sees everything	✗ Illegal
Encrypted Health App	Encrypted	~ Partial	Server sees data	~ Partial
PrivaMed AI (Midnight)	Nothing	✓ Shielded	✓ ZK-gated	✓ By design
Privacy Architecture
This project uses core Midnight/Compact concepts:

Concept	Usage in PrivaMed AI
witness	Private health data (symptoms, vitals, age, flags)
ledger	Anonymous aggregate counters only
circuit	ZK computation linking private inputs → public output
disclose	Only the risk level is made public
assert	Input validation safety constraints
Shielded computation	All health data stays with the user
Proof server	PLONK proofs via BLS12-381 (localhost:6300 / preprod)
Technical Stack
Layer	Technology
Smart Contract	Compact (Midnight's ZK contract language)
ZK Proving	PLONK over BLS12-381 scalar field
TypeScrip

**Challenges we ran into**

🫀 PrivaMed AI
Privacy-First AI Healthcare Intelligence
Algofest Hackathon 2026 · AI Track
"Powerful AI health triage — without seeing a single byte of your medical data."

Midnight Network Track Privacy License

The Problem
1 in 3 people avoid seeking health advice online due to privacy concerns.

Traditional health AI requires uploading symptoms, vitals, and medical history to a server. Even "private" solutions rely on trust — you're trusting a company with your most sensitive personal data.

Public blockchain health apps are even worse: your medical history is on a permanent, public ledger forever.

PrivaMed AI solves this at the cryptographic level, not the policy level.

What We Built
PrivaMed AI is a privacy-preserving medical triage platform that uses zero-knowledge proofs to protect sensitive health data. that uses zero-knowledge proofs to assess health risk without exposing any personal medical data — to anyone, including the AI.

┌─────────────────────────────────────────────────────────────────┐
│                        Your Device (Private)                    │
│                                                                 │
│  Symptoms    →  [witness]  ─┐                                   │
│  Vitals      →  [witness]  ─┤→ [ZK circuit] → risk: "HIGH"    │
│  Age         →  [witness]  ─┤                        │         │
│  Conditions  →  [witness]  ─┘                        │         │
│                                                       │         │
│  (NOTHING ABOVE EVER LEAVES THIS BOX)                │         │
└───────────────────────────────────────────────────────┼─────────┘
                                                        │ proof only
                                               ┌────────▼────────┐
                                               │ Privacy Ledger │
                                               │ +1 to counter   │
                                               │ (no PII)        │
                                               └────────┬────────┘
                                                        │ "HIGH"
                                               ┌────────▼────────┐
                                               │     AI Model    │
                                               │ (never sees your│
                                               │  raw symptoms)  │
                                               └─────────────────┘
How It Works
Step 1: Private Witnesses (Local)
Your health inputs are computed as Compact witness values on-device — these are the private inputs to the ZK circuit and never leave your browser.

witness age_group(): Uint<8>;          // bucketed: 0=child, 1=adult, 2=senior
witness symptom_score(): Uint<8>;      // aggregated severity 0-100
witness vital_risk_score(): Uint<8>;   // deviation from clinical norms 0-100
witness chronic_flag(): Boolean;       // has chronic condition (binary flag only)
witness vaccination_status(): Boolean; // vaccinated (binary flag only)
Step 2: ZK Circuit (Local)
A Compact circuit runs locally using the PLONK proving system over BLS12-381. It computes your risk classification without exposing the inputs.

export circuit assess_risk(): AssessmentResult {
  const ag = age_group();
  const ss = symptom_score();
  const vs = vital_risk_score();
  
  assert ag <= 2;
  assert ss <= 100;
  assert vs <= 100;
  
  const raw = ss * 40 / 100 + vs * 35 / 100 + age_factor(ag) + chronic_factor();
  const level = classify(raw);
  
  disclose level;  // ← only this leaves the circuit
}
Step 3: Shielded Ledger Update
Only the cryptographic proof and anonymous counters are written to the Privacy Ledger. No PII, no symptoms, no vitals.

ledger total_assessments: Uint<64>;
ledger high_risk_count: Uint<64>;
ledger medium_risk_count: Uint<64>;
ledger low_risk_count: Uint<64>;
// ✗ NO personal data fields
Step 4: AI Recommendation
The AI model receives only the risk classification — never raw health data. This is ZK-gated AI: powerful intelligence with zero privacy cost.

Privacy Comparison
Approach	Data on Server	On-Chain Privacy	AI Privacy	GDPR
Traditional Health App	All data	N/A	Sees everything	⚠️ High risk
Public Blockchain DApp	All data	✗ Exposed	Sees everything	✗ Illegal
Encrypted Health App	Encrypted	~ Partial	Server sees data	~ Partial
PrivaMed AI (Midnight)	Nothing	✓ Shielded	✓ ZK-gated	✓ By design
Privacy Architecture
This project uses core Midnight/Compact concepts:

Concept	Usage in PrivaMed AI
witness	Private health data (symptoms, vitals, age, flags)
ledger	Anonymous aggregate counters only
circuit	ZK computation linking private inputs → public output
disclose	Only the risk level is made public
assert	Input validation safety constraints
Shielded computation	All health data stays with the user
Proof server	PLONK proofs via BLS12-381 (localhost:6300 / preprod)
Technical Stack
Layer	Technology
Smart Contract	Compact (Midnight's ZK contract language)
ZK Proving	PLONK over BLS12-381 scalar field
TypeScrip

[Preet Yadav](https://github.com/preet1802yadavemailcom-design)

`2026-05-29`

---

### Smartdoor step Healthcare platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartdoor-step-healthcare-platform-23a5) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://smartcare.niat.tech/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Smart Doorstep Healthcare & Emergency Support Plat

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

CARE AT HOME is a smart doorstep healthcare platform that helps patients receive medical services directly at home without visiting hospitals.

Users can send their health problems through messages or calls. Based on the symptoms, doctors are assigned to visit the patient’s home. The platform also provides medicine delivery, injection support, nurse assistance, emergency healthcare, and healthy fruit recommendations for faster recovery.

This project is especially useful for elderly people, emergency patients, busy workers, and people living in remote areas.

Features:
• Doctor Home Visit
• Medicine & Tablet Delivery
• Emergency Healthcare Support
• Nurse Assistance
• Healthy Diet & Fruit Suggestions
• Patient Recovery Monitoring
• Current Location Sharing

Technologies Used:
HTML
CSS
JavaScript

CARE AT HOME aims to make healthcare easier, faster, and more accessible for everyone.

**Challenges we ran into**

While building CARE AT HOME, I faced challenges in designing a modern healthcare interface and creating a smooth request system for patients.

One of the major challenges was implementing the request submission feature and displaying patient details dynamically after clicking the “Send Request” button. I solved this using JavaScript DOM manipulation.

Another challenge was adding current location sharing using browser geolocation. Initially, location access was not working properly, but after learning about the navigator.geolocation API, I successfully implemented it.

I also worked on creating a responsive purple-themed UI that looks modern and user-friendly on both mobile and desktop devices.

Through this project, I improved my skills in:
• HTML
• CSS
• JavaScript
• Responsive Web Design
• UI/UX Design
• DOM Manipulation

**Using LocusFounder to Build a Business!**

CARE AT HOME fits this business track because it solves a real-world healthcare problem by providing doorstep medical services for patients who cannot visit hospitals easily.

The platform can become a scalable healthcare startup that connects patients, doctors, nurses, medicine providers, and emergency services in one system.

Users can send their symptoms through messages or calls, and the platform helps assign doctors, deliver medicines, provide injections, and monitor recovery from home.

This idea is useful for:
• Elderly people
• Emergency patients
• Rural areas
• Busy working professionals

The project has strong business potential in the healthcare and home-service industry because it improves accessibility, saves time, and provides safer healthcare support.

Team **rithwik** -- Thrisha Serla

`2026-05-20`

---

### PredictIQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aura-x-991a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lovable.dev/projects/9fc45ad9-197a-447f-8e5b-2dec3b9e2048) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co)

> Smart Care for a Healthier Tomorrow

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The system appeared to be a Predictive Maintenance Platform called PredictIQ. It focuses on real-time equipment health monitoring.
📊 System Overview Section:
3 Healthy systems
2 Warning alerts
0 Critical issues
61% Average Remaining Useful Life (RUL)
This gives a quick snapshot of overall system performance.
🏭 Fleet Status Section:
Different industrial machines are listed with their condition:
CNC Mill Alpha → Healthy (93% life remaining)
Hydraulic Press Beta → Healthy (75%)
Industrial Pump Gamma → Healthy (59%)
Air Compressor Delta → Warning (45%)
Conveyor System Epsilon → Warning (34%)
Each machine card shows:
Status (Healthy/Warning)
Remaining useful life
Metrics like vibration, temperature, and power.

**Challenges we ran into**

Sensor accuracy & calibration
Getting reliable data from sensors (temperature, vibration, etc.) is tricky—small errors can lead to wrong predictions.
Data noise & inconsistency
Raw machine data is often noisy, incomplete, or fluctuating, making analysis difficult.
Real-time data processing
Handling continuous data streams without lag requires efficient architecture and optimization.

Team **Elite innovatora** -- Joy Amal, Arisom Saha, Pravanya M, Kamalesh J

`2026-05-06`

---

### Smart Hospital Management System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-hospital-management-system-with-appointment-tracking-7cc2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deepanshu-java-dev) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co)

> A simple system to manage patients, doctors,

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square)

**Challenges we ran into**

While building the Hospital Management System, I faced multiple challenges during development.
One major issue was handling date formats while storing appointment data in the database. I encountered an SQL error due to incorrect date format conversion. I resolved this by properly formatting the date and ensuring compatibility between Java and MySQL data types.
Another challenge was managing database connectivity and executing queries efficiently. Initially, I faced errors while inserting and retrieving data, but I fixed them by debugging SQL queries and using PreparedStatement to avoid syntax issues.
I also worked on implementing a login system, where I had to ensure proper validation of user credentials. After debugging, I successfully handled authentication logic.
Overall, these challenges helped me improve my problem-solving skills and understanding of backend development.

**The problem it solves**

problem
Many small hospitals still rely on manual record-keeping, which leads to errors, data loss, and inefficient management of patients and appointments.


Solution
This system provides a digital solution to manage hospital data, including patient records, doctor details, and appointment scheduling. It improves efficiency, reduces errors, and ensures better organization of hospital operations.

[DEEPANSHU Bhadauria](https://github.com/Deepanshu-java-dev)

`2026-05-06`

---

### MEDISCAN-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mediscanai-233f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/amit-dev01/healthscan-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://healthscan-ai-smoky.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> YOUR MEDICAL ASSISTANT

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**
Navigating a medical diagnosis is one of the most stressful experiences for a patient, yet the current healthcare system leaves them completely unsupported once the report is handed over. Aarogya Agent directly solves three critical bottlenecks in the patient journey:

**The Comprehension Gap (Medical Jargon): Diagnostic reports and imaging (X-rays/MRIs) are written exclusively for clinicians. **When patients try to decode terms like "bilateral opacities" or "hyperlipidemia" on their own, it leads to misinformation, severe anxiety, and "WebMD panic."

The Language Barrier (Healthcare Inequality): High-level medical data is almost entirely in English. For millions of people in rural and semi-urban areas, this creates a massive barrier to understanding their own health, forcing them to rely on delayed verbal translations from busy clinic staff.
**
The "Action Paralysis" (Dead-End Diagnostics): A static medical report—or even a standard AI chatbot—stops at the diagnosis. Patients are left stranded, burdened with the multi-step task of figuring out what specific specialist they need, mapping nearby clinics, and coordinating their own follow-up care while sick or injured.**

In short: We are solving the disconnect between receiving a confusing medical diagnosis and actually taking the right localized steps to get treated

**Challenges we ran into**

1. Forcing Deterministic JSON Outputs from Multimodal Inputs

The Challenge: Passing a complex X-ray or medical PDF to the Gemini API and asking it to analyze the data is easy. However, forcing the LLM to output a strictly formatted JSON payload (without adding conversational filler like "Here is your analysis:") was incredibly difficult. If the JSON format broke, our downstream Google Maps API script would crash.

The Solution: We bypassed standard prompting and utilized Gemini's Structured Outputs / JSON response schemas. We engineered a rigid system prompt with few-shot examples that forced the model to return only the raw data (Disease Category, Summary, Translated Text), ensuring 100% stability for our tool-calling pipeline.

2. Preserving Clinical Context in Regional Translations

The Challenge: Translating medical jargon from English to Hindi or Bengali isn't a 1:1 process. Direct, literal translations of terms like "pulmonary edema" often result in highly academic local words that rural patients still don't understand, defeating the purpose of the app.

The Solution: We optimized the Agent's reasoning prompt to perform a "Concept-to-Analogy" translation rather than a literal word-by-word translation. We instructed the AI to act as an empathetic local doctor, using culturally relevant analogies and simpler regional vocabulary to explain the core issue.

3. Handling the "Blurry Image" Edge Case (Agentic Safeguards)

The Challenge: In real-world scenarios, patients often upload poorly lit or blurry photos of their physical diagnostic reports or X-rays. Initially, our AI would attempt to hallucinate a diagnosis from bad data, which is highly dangerous in a healthcare context.

The Solution: We implemented an autonomous Pre-Check Safeguard Agent. Before the main diagnostic sequence runs, the agent evaluates the image quality. If the confidence score is too low, the agent halts the tool-chain and proactively asks the user to upload a clearer image, ensuring clinical safety.

[AMIT DEY](https://github.com/amit-dev01)

`2026-04-29`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
