# Finance and Fintech

![Projects](https://img.shields.io/badge/Projects-203-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### MyMiniEpic
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/myminiepic-8f22) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mpk1vfvzu4k4kt6x.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-11-FF6B6B?style=flat-square)

> Some memories deserve more than a swipe.

![Locus Founder](https://img.shields.io/badge/Locus%20Founder-333333?style=flat-square)

**The problem it solves**

**Every parent and pet owner wants a gift that feels one-of-a-kind — but personalized books today are expensive, slow, and require design skills.**

Walk into any bookstore and you'll find thousands of children's books. None of them feature your child. None of them star your dog. Generic stories get read once and forgotten. But a story where your 4-year-old daughter defeats a dragon using her actual personality traits, or where your golden retriever named Biscuit saves the neighborhood — that gets read a hundred times and kept forever.

The problem is that custom illustrated books have historically been a luxury. Traditional personalized book services charge $60–$120, take 2–4 weeks to deliver, and still use rigid templates where you're just swapping a name into pre-written text. That's not personalization — that's a mail merge.

**MyMiniEpic fixes this entirely.**

A customer takes a short quiz — name, personality traits, favorite genre, breed (for pets) — and our AI generates a fully unique 10-page illustrated storybook starring their child or pet as the hero. Not template-swapped. Actually unique — the plot, the dialogue, the humor, the illustrations are all generated around *that specific character.*

What people use it for:

- A birthday gift for a child that no one else on earth has — their name, their personality, their adventure

- A keepsake for pet owners who want to immortalize their dog or cat in a real, printed storybook

- A thoughtful, personal gift for baby showers, holidays, or "just because" — the kind of gift that makes someone say "*how did you even find this?*"

- A memorial book for a pet that has passed — turning memories into a story that lasts

**Three tiers, every budget covered:**

- **Digital PDF** ($14.99) — instant download, readable on any device, shareable with family

- **Softcover print** ($29.99) — a real book, shipped to your door

- **Hardcover print** ($49.99) — premium quality, built to survive years of bedtime readings

**The charity angle: **Every purchase donates $1–$3 to animal shelters. Customers aren't just buying a book — they're helping a real animal while celebrating their own. We surface this as a surprise charity receipt included with the order, turning a purchase into a feel-good moment.

**Why this matters beyond gifts:** We've observed that stories create stronger emotional memories than photographs. A photo captures a moment. A story captures a personality. Parents and pet owners don't just want to remember what their child or pet looked like — they want to remember who they were. MyMiniEpic turns that instinct into a product.

**The marketplace layer:** Beyond direct-to-consumer sales, MyMiniEpic actively onboards pet shops, gift stores, and local boutiques as resellers on our platform. These shops(I have included Etsy and Shopify) can offer personalized gifts and items for the loved ones. This turns every local pet shop into a distribution channel. For these distribution channels, we find leads in CRM section. 

**Marketing through Google Ads Layer:**  We are using Google Ads to sponsor our pages and the platform we are running to reach to audience.

**Challenges we ran into**

**Port mismatch between Vite and LocusBuild**

The Vite dev server defaults to port 5173, but the *.locusbuild* configuration expected port 3000. The build verifier checks the port declared in *.locusbuild*, so even a perfectly working server on 5173 would fail verification every time — the health check would hit port 3000 and get nothing. This was frustrating because the app worked fine locally but kept failing in the Locus pipeline. The fix was hardcoding *port: 3000* in both *vite.config.ts* and *.locusbuild* simultaneously so both systems agreed on where the server lives.

**Backend process silently exiting during build verification**

The build verifier kept reporting that the backend (*tsx src/server.ts*) would start and then immediately exit, failing the health check. The logs showed no obvious error. After digging in, the root cause was dependency isolation — *dotenv* and several other packages were installed at the project root but not inside the *backend/subfolder*. Since the backend runs from its own directory, it couldn't find its dependencies and crashed on import. Fixed by adding an explicit *cd backend && npm install* step to the build pipeline so the backend has its own complete *node_modules*.

**AI story generation consistency and quality control**

Getting the AI to generate stories that were genuinely funny, age-appropriate, and consistent across 10 pages required significant prompt engineering. Early outputs were either too generic ("Biscuit went on an adventure and had fun") or tonally inconsistent (page 3 would be whimsical, page 7 would read like a Wikipedia article). We solved this by structuring the generation into a two-pass system: first pass generates a story outline with character arc and tone guidelines, second pass writes each page while referencing the outline. This kept the narrative coherent and the humor consistent throughout.

**Quiz-to-story pipeline latency**

The full generation pipeline (quiz intake → story generation → illustration generation → PDF assembly) initially took 45+ seconds, which felt like an eternity for a user staring at a loading screen. We broke this into a streaming experience: the story text generates first and displays page-by-page while illustrations render in the background. Users start reading immediately while the full book assembles. Perceived wait time dropped from 45 seconds to under 10.

**Print-ready PDF formatting**

Digital PDFs and print-ready PDFs have completely different requirements — bleed margins, CMYK color space, spine width calculations for hardcover, DPI requirements for illustrations. A PDF that looks perfect on screen can print with clipped edges and washed-out colors. We built a separate export pipeline that re-renders the entire book at 300 DPI with proper bleed margins and print-safe color profiles, triggered only when a customer selects the softcover or hardcover tier.

**Using LocusFounder to Build a Business!**

MyMiniEpic isn't a project that happens to use Locus. It's a project that **couldn't exist without Locus**. The entire business — from concept to first customer — was built, launched, and operated inside a single Locus workspace.

**What LocusFounder built:**

**Market research and idea validation** — Locus pressure-tested the personalized storybook concept, identified the pet owner + parent intersection as the highest-intent market, and validated pricing tiers ($14.99 / $29.99 / $49.99) against competitor analysis

**Brand identity** — Locus generated the MyMiniEpic brand, including the coral/navy color palette, logo, and brand voice. These decisions persisted across sessions through Locus's business memory — nothing had to be repeated or re-explained

**Full-stack storefront** — The React + Vite storefront was built and deployed by the Locus build agent to a live URL, including the quiz flow, story preview, and checkout

**Product and checkout** — Three product tiers (Digital PDF, Softcover, Hardcover) were created directly in Locus with Locus Checkout buttons embedded in the purchase flow, handling real USDC transactions end-to-end

**Cold email outreach** — Locus's CRM and outreach tools ran cold email campaigns targeting pet shop owners and gift boutique operators, pitching them on becoming resellers. This is the distribution flywheel — every shop that signs up becomes a new sales channel without us lifting a finger

**Lead generation **— Locus found and qualified leads for both B2C (pet owners and parents) and B2B (pet shops and dropshippers), running separate outreach sequences for each audience

**What makes this a true LocusFounder Track submission:**

The hackathon track asks: "*What happens when the agent is the founder?*" MyMiniEpic answers that directly. Locus didn't just build a website — it made product decisions, brand decisions, pricing decisions, and distribution decisions. It identified the market, built the storefront, found the customers, and ran the sales motion.

The cold email engine isn't an afterthought — it's the growth loop. While most hackathon submissions will show a website the agent built once, MyMiniEpic shows a business the agent operates daily — finding new reseller leads, emailing them, following up, managing the CRM, and expanding distribution autonomously.

Locus is the co-founder that handles everything the solo builder can't: design, deployment, distribution, and daily operations. The human brings the vision. Locus brings the execution. That's exactly what this track is about.

Team **kitlers** -- [Sathvik Pasuvula](https://github.com/sathvik9105), [Sunil Swain](https://github.com/sunilswain7), [Ashutosh Vats](https://github.com/AshutoshVatsg)

`2026-05-26`

---

### Invoice Now
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/invoice-matchmaking-5333) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vatsalm30/ETHDenverProject) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/047c445c0a394716abbfa0f1a5ded12f) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-11-FF6B6B?style=flat-square)

> Don't Settle for Less

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![DAML](https://img.shields.io/badge/DAML-333333?style=flat-square)

**The problem it solves**

Invoice financing represents a $3+ trillion global market built on a fundamental structural inefficiency: suppliers who have completed legitimate work and hold confirmed invoices are forced to wait 30, 60, or even 90 days for payment while their capital sits frozen in receivables. This liquidity gap creates cascading operational risk;  suppliers cannot pay their own vendors, fund new production, or invest in growth while waiting on buyers to fulfill payment terms. The existing solutions to this problem are fragmented and opaque: traditional factoring companies offer take-it-or-leave-it rates with no competitive transparency, and suppliers have no mechanism to verify whether the terms they receive reflect fair market pricing. Invoice Now addresses this directly by creating a competitive auction marketplace where invoicees can sell confirmed invoices immediately, financiers bid in real time for the right to fund those invoices, and the resulting market dynamics produce rates anchored to genuine supply and demand rather than a single intermediary's margin requirements.

**Challenges we ran into**

One of the biggest hurdles our team faced was verifying the legitimacy of financiers and invoicees without compromising user privacy. Because our platform handles financial transactions, trust is essential, but traditional verification methods like KYC require collecting and storing sensitive data, which conflicted with our goal of building a privacy-preserving system. After researching alternative approaches, we determined that Zero-Knowledge (ZK) proofs offered the best solution, allowing users to prove they meet verification requirements without revealing their underlying information. Although integrating ZK proofs required us to rethink our validation logic and overcome a technical learning curve, it ultimately enabled us to strengthen platform security, preserve user privacy, and enhance overall trust in the system.

**Use of AI tools and agents**

In Invoice Now, we use AI to streamline the invoice submission process and reduce friction for users. Specifically, we implemented an AI-powered invoice parser that automatically extracts structured data from uploaded documents. Instead of requiring users to enter every field manually, the system processes PDFs or images using document-understanding models that identify key text regions, classify fields, and normalize the data into a standardized format for our platform.

**New France Village**

Our project, Invoice Now, directly aligns with the Future of Finance focus of the New France Village track by bridging real-world financial infrastructure with blockchain-native systems. At its core, we are bringing Real-World Assets (RWA) on-chain by tokenizing invoices, enabling them to be financed in a more transparent, efficient, and accessible way. From a DeFi and RealFi perspective, we transform traditionally illiquid receivables into digitally verifiable financial instruments that can integrate with decentralized liquidity. At the same time, we incorporate compliance-aware architecture to align with AML, regulatory, and institutional standards, making the system viable not just for crypto-native users but also for traditional financial participants. This positions Invoice Now at the intersection of TradFi and DeFi, creating infrastructure that could support treasury companies, institutional capital, and eventually broader Main Street adoption. By modernizing invoice financing through blockchain rails while preserving privacy and compliance, our project reflects the evolution of finance that New France Village aims to highlight.

**Best Privacy-Focused dApp Using Daml**

Invoice Now is a privacy-first invoice financing dApp built natively on Canton L1 using Daml, directly aligning with the Best Privacy-Focused dApp track. Invoice financing involves highly sensitive commercial data — supplier identities, pricing terms, payment schedules, and credit exposure — making confidentiality essential. Our smart contracts are written entirely in Daml and model invoices as agreements between clearly defined parties: Supplier, Debtor, and Financier. Leveraging Canton’s granular party-based data visibility, only relevant stakeholders can view specific contract details. For example, financiers can evaluate financing terms without seeing unrelated supplier information, debtors see only their obligations, and competing financiers cannot access each other’s bids. This demonstrates meaningful use of Daml’s native privacy model rather than relying on external chains or superficial implementations.

Beyond technical correctness, Invoice Now showcases real-world utility in confidential DeFi and RealFi infrastructure. The application’s UI clearly indicates which party the user is acting as and visibly demonstrates how contract visibility changes across roles, making Canton’s privacy guarantees tangible in a live deployment. By combining programmable invoice tokenization, role-based confidentiality, and controlled data disclosure, the project highlights how enterprise-grade supply chain finance can operate on-chain without exposing sensitive business information. This makes Invoice Now a strong demonstration of Canton Network’s privacy-first architecture and its potential for institutional adoption.

Team **Boiler Blockchain** -- [Jacob Gutwein](https://github.com/jgutw), [Manasvi Meka](https://github.com/mmeka24), [Alzahraa Ahmed](https://github.com/Zara-commits), [Vatsal Maheshwari](https://github.com/vatsalm30)

`2026-02-21`

---

### Agent Heist
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agent-heist-ec85) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/projnanda/nandatown/pull/214) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/af14dd1a3ccc41b3b81e0138d87e9355) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/af14dd1a3ccc41b3b81e0138d87e9355) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-8-FF6B6B?style=flat-square)

> How to Scam Agents and Influence Their Payments

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

**After 20 years of internet, humans still get scammed online. What do you think happens when agentic commerce takes off?** 
 
Agent Heist answers that question by making it a game. Buyer agents (each with a real $100 Prava mandate, some with deterministic logic and some with LLM brains) shop across honest and adversarial merchants (some with deterministic logid and some with LLM brain) that fight back with prompt injection, price manipulation, fake urgency, and bait-and-switch. Every overpayment, decline, and blocked attack is a **real Prava sandbox transaction**, not a simulation, till we hit our limit. 
 
What you can use it for:
 
- **Developers** can stress-test their user shopping agents against live social-engineering attacks before shipping them.
- **AI safety researchers** get real agent-to-agent adversarial payment data, a gap that's barely been tested.
- **The ecosystem** sees which attacks succeed, which defences hold, and how well network-level spending caps stop a compromised agent from overpaying.
It makes agentic commerce **safer** by turning an untested attack surface into measurable, reproducible, gamified data and proves that Prava's mandate caps enforce a spending limit even when the buyer agent itself gets fooled.

This is a small sample of what we are building at RMI Agentic (www.rmiagentic.com), do take a look.

**Challenges we ran into**

## Challenges I Ran Into
 
This is a mix of hurdles and some stem my lack of understanding of the documentation.

Wiring a **live payment API into a deterministic multi-agent game** meant most hurdles were about reverse-engineering how Prava actually behaves.
 
**Passkey auth kept failing.** WebAuthn approval threw Authentication Failed in every browser, until I noticed the Prava team mail which confirmed the test card expiry in the docs was wrong (12/27 should be 12/30).
 
**Mandate cap semantics were ambiguous, so we tested them.** Charging $200 on a $100 mandate with $13.50 already spent returned Total 213.50 exceeds threshold 100.00, confirming the cap is **cumulative** and enforced at the network level. That's our whole thesis: Prava blocks the overcharge even when the buyer agent is fooled.
 
**Making a live API deterministic.** Built a mock mode mirroring Prava's error codes (THRESHOLD_EXCEEDED, MANDATE_NOT_FOUND) for reproducible runs, live mode opt-in. Fixed 409 Conflict on re-runs by prefixing payment references with a timestamped _RUN_ID.

**Best Visa Intelligent Commerce Implementation**

Most entries will show VIC processing a payment; Agent Heist shows VIC defending an agent under attack, a deeper, more convincing implementation.
 
Agent Heist runs entirely on Prava (the sanctioned way to implement VIC), so it's eligible by default and wins on integration depth:
 
- **VIC used as designed:** passkey-approved mandates, cumulative network-level caps, and single-use scoped tokens on live Visa-network settlement (our cap test returned Visa's own Total 213.50 exceeds threshold 100.00).
- **Beyond the happy path:** we deliberately handle THRESHOLD_EXCEEDED, declines, and conflicts, VIC controls working under stress.
- **The proof point:** the game exists to show VIC's cap holds even when the buyer agent is socially engineered into overpaying, the strongest evidence Visa's controls do their job.
- **Reusable:** a drop-in adapter and adversarial harness for anyone building a VIC agent.

**OpenAI**

In Agent Heist, OpenAI reasoning is working in real world scenarios and it is the core.
 
- **OpenAI is the brain of every agent:** buyer and merchant agents reason, negotiate, and decide with OpenAI LLMs, the honest merchants price fairly, the adversarial ones craft prompt-injection and social-engineering attacks, and buyers defend, all via model reasoning rather than hard-coded rules.
- **A real, hard agentic problem:** we test whether an OpenAI-driven shopping agent can be scammed by another OpenAI-driven agent, an open, under-explored AI-safety question, answered with real payment data.
- **Model reasoning under pressure:** the game measures which prompts and defenses hold when one LLM agent actively tries to manipulate another, genuine adversarial evaluation, not a scripted demo.
- **Complete and reproducible:** live payments on real rails, deterministic mock mode for scored runs, a working leaderboard, a finished product, not a prototype.

**Best Prava Adapter for the NANDA Town**

The track asks for a dependable, reusable Prava payments adapter and a scenario that proves it. 

Agent Heist delivers both, mapped straight to the rubric:
 
- **Quality & reliability of the adapter:** a PravaPayments plugin implementing NANDA Town's payments-layer interface (quote / pay / verify / refund), with a mock mode for reproducible runs and opt-in live mode.

- **Security, authorization & failure handling:** passkey-approved mandates, cumulative network-level caps, single-use scoped tokens, idempotent references  and deliberate handling of THRESHOLD_EXCEEDED, MANDATE_NOT_FOUND, 409 conflicts, and declines.

- **Successful Prava sandbox transactions:** every purchase is a real mandate charge on Prava's sandbox (our cap test returned Total 213.50 exceeds threshold 100.00), not a simulation.

- **Ease of installation & reuse:** drop into any scenario via payments: prava, with a provisioning script and a README covering install and reuse.

- **Quality of the scenario on top:** Agent Heist: a buyer-vs-merchant marketplace with honest and adversarial agents, stress-tests the adapter and generates real agent-to-agent attack data.

**Meets the success standard:** the adapter makes it trivial for future NANDA Town builders to plug in Prava as a payment layer and the adversarial game is a ready-made harness to verify their own agents.

**Agentic Commerce Hackathon**

The track wants a reliable Prava adapter for NANDA Town, proven by real sandbox transactions with failure handling. Agent Heist is exactly that, and the adversarial game doubles as the adapter's stress test:
 
- **Adapter quality:** PravaPayments plugin implementing nest's Payments interface, with mock mode (reproducible) and opt-in live mode.
- **Real transactions + failures:** Every purchase is a live mandate charge; we deliberately handle THRESHOLD_EXCEEDED, MANDATE_NOT_FOUND, 409s, and declines, not just the happy path.
- **Security/authorization:** Passkey-approved mandates, cumulative network-level caps, single-use scoped tokens,  proven to hold even when the agent is socially engineered.
- **Ease of reuse:** Drop into any scenario via payments: prava.
- **Scenario quality:** A real buyer-vs-merchant marketplace generating agent-to-agent attack data, the "agentic commerce" the track is about.

[Mitesh Tank](https://www.github.com/inquisitivetank)

`2026-08-02`

---

### TrustDrop
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trustdrop-81fc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sunilswain7/TrustDrop) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-moij1jmns40adzkv.beta.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-8-FF6B6B?style=flat-square)

> Sell files. Get paid on-chain. Zero trust required

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

**The Problem**

For the past few months, I got into making digital assets in Blender. What started as a hobby quickly turned into freelance opportunities — but the experience was brutal:

1. **Buyers steal work.** You send the file, they ghost. Your hours of work, used for free.
2. **Sellers scam buyers.** Pay first? The seller disappears or delivers garbage.
3. **Previews lie.** What you saw isn't what you got. No way to verify.

***TrustDrop Fix***-

1) Every uploaded file is **AES-256-CBC encrypted** before it's stored. The raw file doesn't exist in a downloadable form anywhere — not on the server, not in the preview, not in the browser. The decrypted file is only generated **after** the Locus Checkout payment is verified on-chain. No payment means no file. No screenshots of the real thing either — buyers only see Agent generated cinematic previews, not the actual asset.
2) Seller cannot sell garbage-> TrustDrop agent makes the preview of the file uploaded for the buyer to confirm first.(No room of cheating)=> Agent does verification for you.


As a new creator on Discord or Twitter, **trust is nonexistent.** Buyers won't risk money on an unknown seller. Sellers won't risk their work on an unknown buyer. Both sides lose — the buyer misses a talented creator, the seller never gets their shot.

***TrustDrop Fix***-

The Improvement Room solves this too. A buyer who commits funds is putting skin in the game — the seller knows the buyer is serious. And if the buyer ghosts after seller delivers? The commitment fee is **released to the seller** as compensation. Both sides have something to lose, so both sides act in good faith.

Fake portfolios, stolen assets, and fabricated reputation have become a nightmare across online creator communities.

Existing platforms don't fix this:
- **Gumroad** takes up to 23% in fees
- **Etsy** requires KYC, card details, and bank accounts — excluding young creators globally
somehow they create subscription plans.

- **Neither** offers cryptographic proof that the delivered file matches the preview

***TrustDrop Fix***-

**Minimal platform fees** on purchases — 100% of the payment goes to the seller via Locus Pay. No KYC, no bank account, no credit card required. Sellers just need a Locus wallet address to start selling. Buyers can even tip creators via email — the recipient gets a **claim link** from Locus to collect USDC without needing a crypto wallet at all. And on-chain USDC payments can't be reversed or clawed back like PayPal chargebacks.      

No verification. No protection. No access for emerging talent.

**TrustDrop** provides all three: dual on-chain verification (webhook + session status polling), automatic escrow protection with deadline-based resolution, and a zero-barrier entry for any creator anywhere in the world i.e a **PAYOUT WORLD**. This solves one of the most hinged payout session problem over the internet using Locuscheckout architecture. Millions of designers(Roblox , Minecraft , blender builds) , coders , assets builder does transaction on daily basis can now easily **Sell and Pay** with **TrustDrop** securely.

**Challenges we ran into**

## 1. Production vs Beta API — Checkout Failing on Day One

The very first time we tried to run a Locus Checkout session, it failed immediately. The checkout iframe wouldn't load, and API calls returned errors. We were pointing at 'api.paywithlocus.com' (the production endpoint) — but our 'claw_dev_' API key only works against the beta environment.

**Fix:** Changed the API base URL from 'https://api.paywithlocus.com/api' to 'https://beta-api.paywithlocus.com/api' and the checkout URL to 'https://beta.paywithlocus.com'. Environment and API key have to match — dev keys only work against beta, production keys only work against prod. A small misconfiguration, but it blocked the entire payment flow until we caught it.

## 2. Locus Pay API Field Names — The Silent Payout Failure

The first major blocker hit when seller payouts silently failed with 400 errors. After a buyer purchased a listing and payment landed in the platform wallet, the server tried to forward funds to the seller — but every call to '/pay/send' failed.

**Root cause:** The Locus API uses 'to_address' (not 'to'), expects 'amount' as a number (not a string), uses 'memo' (not 'reason'), and returns 'transaction_id' (not 'txHash'). Every single field name was wrong.

**Fix:** Corrected all field names and response parsing in 'lib/locus.ts'. Confirmed with a live test showing funds forwarded to the seller wallet. This taught us to never assume API field names — always test with real calls first.

## 3. BWL Upload Size Limit — The 5KB Wall

Sellers couldn't upload files larger than ~5KB. The upload would silently fail with no error message. After extensive debugging, we discovered that BWL's reverse proxy blocks large request bodies.

**Fix:** Moved file uploads entirely to Supabase Storage with client-side direct uploads via signed URLs. The server generates a signed upload URL ('/api/upload/signed-url'), the client uploads directly to Supabase (bypassing the BWL proxy), and the server downloads from Supabase server-to-server for encryption. This pattern works for files of any size.

## 4. The Checkout Popup That Kept Dying

The commitment fee payment in the Improvement Room used Locus Checkout in 'popup' mode, which opened a new browser tab. But browser popup blockers immediately killed the tab — the buyer had no chance to pay. On some browsers it would flash open and close within a second.

**Fix:** Switched to 'mode="embedded"' which renders the checkout inline as an iframe. But this introduced a new problem — the embedded iframe locked scroll on the entire chat area. Fixed by wrapping the checkout in a 'max-h-[350px] overflow-y-auto' container, keeping the chat scrollable while the checkout renders inline.

## 5. The Invisible 409 — Commitment Payments That Vanished

This was the hardest bug to find. After switching to embedded checkout, buyers could pay the commitment fee successfully — the checkout showed a success screen — but *nothing happened*. No commitment message appeared in chat, no timer started, no deadline was set. The money left the buyer's wallet and went to the platform, but the commitment was never created in the database.

**Root cause:** After checkout success, the frontend called '/api/room/[id]/commit/confirm' which called 'verifyPaymentOnChain()'. But the on-chain verification returned false because Locus hadn't propagated the transaction yet (takes a few seconds). The endpoint returned a 409 error — but the embedded checkout iframe was covering the error UI, so the failure was completely invisible. The commitment row was never inserted, which meant no chat message, no timer, no refund path.

**Fix:** Added retry logic — up to 5 attempts with 3-second intervals. The UI shows "Verifying payment... attempt 2/6" so the buyer knows something is happening. The checkout iframe auto-dismisses after success, revealing the retry progress. This alone fixed the entire commitment flow.

**Track: Checkout with Locus**

# TrustDrop & Locus: Checkout Stack Architecture

TrustDrop is built **entirely** on the Locus payment stack. Every dollar that moves through the platform—whether for purchases, commitment escrows, refunds, seller payouts, creator tips, or email claims—flows through Locus APIs. 

Beyond a standard payment button, we have engineered an **escrow-backed negotiation system, a multi-webhook payout pipeline, and an email-based tipping flow** on top of Locus.

---

### 1. Locus Checkout SDK ('@withlocus/checkout-react')
We utilize the 'LocusCheckout' React component in **embedded mode** across three distinct payment flows. Each flow triggers a unique 'createCheckoutSession()' call with custom 'webhookUrl' and 'metadata' parameters for precise routing.

* **Product Purchases:** Embedded directly inline on the listing page. Upon success, a webhook triggers file decryption and generates a download token.
* **Commitment Fees:** In the Improvement Room, buyers pay a 20% commitment fee to request changes. This spawns an independent checkout session. The fee is held in escrow until seller delivery or buyer response resolves it.
* **Creator Tips:** Buyers can tip creators (custom amounts or preset $1, $3, $5 tiers). A session is created per tip, routing the payout to the seller's wallet or email via the webhook.

### 2. Checkout Sessions API ('POST /api/checkout/sessions')
We generate checkout sessions server-side using the 'CreateCheckoutSessionRequest' type. When prices change in the Improvement Room, we use 'cancelCheckoutSession()' to kill the old session and create a new one.

**Session Payload Configuration:**
* 'amount': Dynamically set (listing price, commitment fee, or tip).
* 'description': Context-aware (e.g., *"Purchase: Neon Cat"*, *"Commitment fee"*).
* 'webhookUrl': Flow-specific routes ('/api/checkout/webhook', '/api/room/[id]/commit/confirm', '/api/tip/webhook').
* 'successUrl': Redirects the user back to the correct post-payment view.
* 'metadata': Encodes the flow type, listing ID, seller wallet, delivery method, and buyer ID.
* 'receiptConfig': Set to '{ enabled: true, merchantName: "TrustDrop" }' for branded receipts.
* 'expiresInMinutes': Set to '30'.

### 3. Session Status Polling ('GET /api/checkout/sessions/:id')
After a webhook fires, we utilize a **dual verification** system. The webhook notifies us of the payment, and we confirm it on-chain by polling the session status. 
* We call 'getCheckoutSession()' to securely read the session's 'status', 'amount', and 'metadata' to process the payout routing.

### 4. Webhook Verification & Security
Both of our webhook endpoints verify the 'x-locus-signature' header to ensure data integrity. 
* **Encryption:** We use HMAC-SHA256 with our webhook secret.
* **Validation:** We implemented 'verifyWebhookSignature()' using 'crypto.timingSafeEqual' to prevent timing attacks.

**Handled Events:**
* 'checkout.session.paid': Triggers the payout, file decryption, or escrow resolution.
* 'checkout.session.expired': Logged and acknowledged by the system.

### 5. Locus Email Escrow ('POST /api/pay/send-email')
For our "Send via Email" tipping flow, the webhook bypasses standard wallet delivery and initiates an escrow via '/pay/send-email'. 

* **Routing Logic:** The delivery method is read from 'metadata.deliveryMethod', directing the webhook to fire either 'sendPayment()' (wallet) or 'sendEmailPayment()' (email).
* **Claim System:** The creator receives an email with a secure **claim link** to collect their USDC. No crypto wallet is required upfront.
* **Auto-Refund:** Unclaimed funds are automatically returned to the platform wallet after 30 days.

---

## Why This Goes Beyond a Simple Checkout Integration

Most checkout integrations are linear (Pay → Webhook → Done). TrustDrop leverages Locus as the foundation for a complex **multi-party escrow system**:

1.  **Three Independent Flows:** Separate webhooks handle entirely different business logic (purchases, escrows, tips).
2.  **Metadata Routing:** 'type', 'deliveryMethod', 'sellerWallet', and 'recipientEmail' turn a single webhook handler into a dynamic payout router.
3.  **Lifecycle Management:** We actively manage sessions, utilizing 'cancelCheckoutSession()' when dynamic pricing updates occur.
4.  **Dual Verification:** Webhook notifications paired with 'getCheckoutSession()' polling ensures high reliability against on-chain propagation delays.
5.  **Email Escrow:** Utilizing '/pay/send-email' extends the platform's reach beyond native Web3 users.
6.  **AI Pipeline:** Even preview generations run through Locus Wrapped APIs.
7.  **Professional Polish:** Utilizing 'receiptConfig' for branded, professional buyer experiences.

Team **Kitlers** -- [Sathvik Pasuvula](https://github.com/sathvik9105), [Ashutosh Vats](https://github.com/AshutoshVatsg), [Sunil Swain](https://github.com/sunilswain7)

`2026-04-30`

---

### PopUpStore
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/popupstore-2aa5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sunilswain7/Popupstore) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-moc3kzq33gi5oz8o.beta.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Pay for URL -> Get URL -> MakeMoney via drops

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**
In Indian social commerce, thousands of independent creators and boutique retailers operate through Instagram DMs and WhatsApp groups. While these platforms are great for discovery, they create a "Technical Tax" the moment a merchant wants to scale. Even 

We identified three critical bottlenecks that prevent these creators from becoming professional digital businesses:

1. **Developer Tax & Complexity Gap**: Creating a professional storefront for a "Limited Drop" currently requires hiring a developer or wrestling with complex, expensive platforms like Shopify. Most creators don't have weeks to wait; they have a drop happening now.

2) **The "Bot Sniper" Problem** :Limited-edition drops are often ruined by automated bot-nets that drain inventory in seconds to resell on third-party sites. Traditional storefronts are "sitting ducks" without expensive Web Application Firewalls (WAF).

3) **The Blind-Flight Analytics** :Merchants know who bought (because they received a DM), but they have zero insight into Visitor Intent. They don't know how many people clicked the link , or if their site crashed under heavy load.

**Challenges we ran into**

1. **Wrong .locusbuild format** — services was an array (old format), API expects an    
  object keyed by name. Fixed the schema.  

2. **The “Black Box” Deployment Gap**
Locus Build takes ~3–5 minutes to provision a container, and a static loading screen created uncertainty for merchants.

Fix: We integrated the SSE log stream (/logs?follow=true) into a live "Chatbox" to see the Transparency and where the project has reached.

 3. We hit a critical ECS/Locus conflict where platform-injected HOSTNAME variables overrode Next.js defaults, causing silent health-check failures.

Fix- We resolved this by force-binding the server to 0.0.0.0 during boot to bypass the runtime variable precedence and ensure service accessibility -LOCUS community helped me

4. **Service discovery failures** — Multiple deploys showed "failed" due to no service    
  arn:aws:servicediscovery... errors on the platform side. Resolved by deleting       
  everything and creating fresh projects.                                               
5. **Stale projects/services** — Had 2 duplicate projects with 5 services total, all stuck in "queued". Cleaned up to a single project.

We solved these at last with help and support!!

**Track: Using BuildWithLocus to leverage our suite.**

PopWithLocus utilizes seven Locus Build endpoints plus the native SSE streaming architecture — every integration is load-bearing and essential to the "agentic" workflow. 

1)**Autonomous Service Orchestration**(POST /v1/services). Agent 2 (Builder) programmatically provisions isolated ECS/Fargate containers on the fly. We don't just host a site; we dynamically create a brand-new cloud environment for every creator drop based on a single natural language sentence.

2)**Dynamic Variable Injection** (PATCH /v1/variables). Before a container boots, we securely inject the AI-parsed product data and Locus Pay checkout links into the service environment. This ensures that the storefront is completely stateless and ephemeral — the code stays the same, but the "business" changes per deployment.

3)*Infrastructure-Level Observability* (/logs?follow=true). We treat the Locus SSE Log Stream as the "nervous system" of our agents.

4)**Frontend UX(uses SSE LOGS)**: We pipe raw Docker logs directly to a "Hacker Terminal" in the UI so merchants can watch their store being born.

5)**Self-Healing Recovery (POST /.../rollback)**. To ensure High Availability, Agent 3 (Lifecycle) monitors the log stream for CrashLoop signals. If an AI-generated UI update causes a failure, the agent autonomously triggers a Locus Rollback to the last stable deployment.

6)**Economic Kill-Switch (PATCH /services/:id - Scale-to-Zero)** - To protect creators from credit-draining EDoS (Economic Denial of Sustainability) attacks, the agent cross-references log traffic against successful Locus Pay webhooks.

7)**Event-Driven Sync (POST /webhooks)**. We register background callbacks to handle the "Deployment Gap." If a user closes their browser during the 5-minute build, Locus pings our backend via webhook upon success to update our global database and notify the merchant.

8)**Credit Guard** (GET /billing/balance). Before initiating any cloud compute, Agent 2 performs a safety check on the Locus credit balance. This prevents failed deployments and ensures the platform always has enough "fuel" to run the creator's store.

Without Locus Build, I would have needed a full DevOps team to manage container orchestration, a cybersecurity team for bot mitigation, and an SRE team for incident recovery.

Team **Kitlers** -- [Sunil Swain](https://github.com/sunilswain7), [Sathvik Pasuvula](https://github.com/sathvik9105), [Ashutosh Vats](https://github.com/AshutoshVatsg)

`2026-04-24`

---

### AlphaOracle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/alphaoracle-e1eb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/namanguptagit/AlphaOracle) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://alphaoracle.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Turning breaking news into decentralized profits.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![CSS3​](https://img.shields.io/badge/CSS3​-333333?style=flat-square) ![Locus Api Gateway](https://img.shields.io/badge/Locus%20Api%20Gateway-333333?style=flat-square) ![FireCrawl Api](https://img.shields.io/badge/FireCrawl%20Api-333333?style=flat-square) ![Server-Sent Events](https://img.shields.io/badge/Server--Sent%20Events-333333?style=flat-square)

**The problem it solves**

Navigating decentralized finance and prediction markets (like Polymarket) requires exhaustive human vigilance. Traders are forced to constantly monitor geopolitical events, macroeconomic news, and crypto legislation to catch market-moving information before the odds adjust. This is manually exhausting, prone to human bias, and strictly limits the volume of opportunities a single person can capitalize on. 

**AlphaOracle** solves this by establishing a fully autonomous, tireless "Prediction Market Agent" built specifically for the Machine Economy. 

It completely removes the human from the active loop by automating the three hardest parts of predictive trading:
1. **Live Data Ingestion:** It uses wrapped proxies to scrape the internet in real-time, focusing specifically on dynamic, high-stakes market questions.
2. **Contextual Reasoning:** It routes the scraped data unconditionally to an LLM (GPT-4o) that acts as an expert analyst, stripping away emotional bias and generating a strict probabilistic confidence score. 
3. **Cryptographic Execution:** Once confidence thresholds are met, the agent autonomously signs and broadcasts a real, on-chain smart contract transaction to the Polygon blockchain. 

**How it makes existing tasks safer:**
Giving an AI agent direct access to your wallet is historically dangerous. AlphaOracle solves this by utilizing the **Locus API Gateway**. Rather than exposing private API keys or giving the bot direct control over an unbounded Web3 wallet, AlphaOracle operates inside a sandboxed Agent Wallet. Financial guardrails prevent the AI from ever executing trades that exceed its predefined `allowance`. If the bot begins to overspend, the Locus API natively intercepts the `POST /pay` calls and halts execution, drastically reducing downside risk.

**Use Cases:**
- Automatically capitalizing on breaking regulatory news (e.g., *SEC ETF Approvals*).
- Macroeconomic predictive trading (e.g., *Federal Reserve Interest Rate cuts*).
- General automated portfolio hedging against global news events while the user sleeps.

**Challenges we ran into**

**Unbounded Autonomous Drain & Loop Control**
One of the most dangerous aspects of building a continuously running backend (setInterval based EventEngine) is that if the AI logic glitches, it can blindly drain Web3 wallets or rack up astronomical API usage trying to execute trades thousands of times an hour. 

We ran into this hurdle early on when the agent's LLM confidence was consistently crossing the execution bounds. The execution engine was running away and exhausting its sandboxed API allowances within minutes, causing silent `403 Forbidden` crashes in the background that we were completely blind to until we manually checked the system logs.

**How We Overcame It:**
We completely decoupled the infinite execution loop into a strictly gated, stateful REST architecture, and we weaponized the Locus Payment API's native safety features to act as our **circuit breaker**. 
Instead of letting the bot crash silently, we explicitly refactored `executor.ts` to trap Axios `403` API Allowance errors. If the Locus proxy tells us we have exceeded our safety bounds, the AgentEngine securely halts itself and emits a custom `{ event: 'alert' }` payload up through our Server-Sent Events network! 
The Frontend Dashboard instantly catches this specific alert, natively clicks the "Stop Agent" button to pause the recurring loop, and injects a flashing red glassmorphism warning banner at the top of the UI so developers know instantly that the safety limit was reached.

**Using PayWithLocus.com to leverage our suite.**

AlphaOracle is the perfect embodiment of the **Machine Economy** because it is a completely autonomous, financially-enabled M2M (Machine-to-Machine) entity. It goes far beyond simply parsing text; it natively orchestrates its own supply chain of intelligence without a human ever pressing a button or signing a credential.

**How it fits the track:**
1. **Inter-Agent Commerce:** Rather than relying on a developer to hardcode expensive OpenAI or Firecrawl API keys directly into the backend, AlphaOracle utilizes the **Locus Network's Wrapped APIs**. The agent uses its own Locus Wallet balance to dynamically route micro-payments to fund its own data scraping (Firecrawl) and logical inference (GPT-4) cycles. It is a machine hiring other machines.
2. **Autonomous Execution:** Traditional Web3 applications require humans to physically click "Approve" on a MetaMask pop-up. AlphaOracle operates as a sovereign entity; the exact moment it establishes statistical confidence in a macroeconomic event, it uses the Locus `api/pay` endpoints to independently broadcast and sign cryptographic bets onto the Polygon network. 
3. **Programmable Guardrails:** By utilizing Locus's backend policy checks, AlphaOracle operates within a strict and enforceable safety allowance. It proves that we can build AI agents that handle real money and place genuine financial bets while completely mitigating the risk of unbounded LLM logic loops blindly draining primary accounts.

[Naman Gupta](https://github.com/namanguptagit)

`2026-04-14`

---

### Opex AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/opex-ai-b72b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/_7sS60Xu_hQ) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_7sS60Xu_hQ) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> AI Agent for monetization businesses for YouTubers

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Webhook](https://img.shields.io/badge/Webhook-333333?style=flat-square) ![YouTube Data API](https://img.shields.io/badge/YouTube%20Data%20API-333333?style=flat-square) ![Stripe API](https://img.shields.io/badge/Stripe%20API-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

**OPEX AI** solves one of the biggest problems in the creator economy: creators have audiences, but most struggle to build scalable monetization systems beyond ads and sponsorships.

Today, **YouTubers** and  **Digital creators** spend countless hours trying to:

- Design digital products
- Analyze audience trends
- Build storefronts
- Write marketing copy
- Handle payment systems
- Track sales and revenue

Most creators are forced to become designers, marketers, analysts, and business operators — which takes time away from what they do best: creating content.

**OPEX AI** changes this completely.

**OPEX AI** acts like a team of autonomous AI employees that run a creator’s monetization business automatically. A creator simply connects their YouTube channel, and the platform:

**Working**
1. Analyzes audience trends using AI
2. Detects monetization opportunities
3. Generates digital products like wallpapers, posters, thumbnails, and social kits
4. Creates marketing content automatically
5. Launches branded storefronts
6. Handles payments through Locus
7. Tracks revenue and wallet analytics in real time

This allows creators to launch AI-powered digital businesses in minutes instead of weeks.

The platform also demonstrates how AI agents can become operational business workers — not just chatbots. Instead of assisting with one task, OPEX AI creates a fully connected autonomous workflow where multiple AI agents collaborate together to generate revenue.

For  **Creators**, this means:

Faster monetization
Passive income opportunities
Zero inventory or shipping
Reduced manual work
AI-driven business automation

For the hackathon vision, **OPEX AI** showcases how Locus can become the financial infrastructure powering autonomous AI businesses.

**Challenges we ran into**

One of the biggest challenges while building **OPEX AI** was designing a believable autonomous AI workflow instead of making the platform feel like a simple chatbot or AI tool.

Since the project uses multiple AI agents working together, coordinating the flow between:

- Trend Analysis
- Product Generation
- Marketing Automation
- Payment Handling
- Revenue Tracking

was initially difficult. The system needed to feel like real AI employees collaborating in real time.

Another major challenge was integrating the payment workflow with the AI automation layer. We wanted the payment experience to feel seamless, where purchasing a product immediately triggered backend AI workflows, updated dashboards, and generated live activity logs. Managing webhook handling and synchronizing real-time revenue updates required careful backend orchestration.

Creating the live AI activity feed was also challenging. The dashboard needed to visually communicate that AI agents were continuously working behind the scenes. To solve this, we implemented animated live logs, real-time updates, and agent status indicators that simulate autonomous operations happening in production.

**Using LocusFounder to Build a Business!**

**OPEX AI** directly aligns with the hackathon’s Week 4 theme by using Locus as the financial infrastructure powering autonomous AI-run creator businesses.

- Additional Focus Areas
- AI Agents & Automation
- Creator Economy
- AI Monetization Systems
- Digital Commerce Infrastructure
- Autonomous Workflows
- AI-Powered Business Operations

![image](https://assets.devfolio.co/content/4245387cfc314537b56fd847d3202496/2f36626d-b3ea-4614-81fc-f93d1da51214.png)

Team **CodeCrafters** -- [Om Baviskar](https://github.com/ombaviskar18)

`2026-05-17`

---

### ForkFlow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/revivalosai-f79d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JanhviJathot03/ForkFlow-) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/K3KzORHLP-g) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/K3KzORHLP-g) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Build. Fork. Scale Intelligence.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Today, AI agents are mostly locked inside centralized platforms with limited ownership, monetization, and customization options. Developers and creators can build powerful AI tools, but there is no open ecosystem where agents can be shared, forked, rented, or monetized transparently.

ForkFlow solves this by creating a decentralized marketplace for AI agents powered by Locus payments.

Users can:

create AI agents using prompts
deploy them instantly
rent or sell them to others
fork and improve existing agents
earn royalties automatically through payments

The platform makes AI agent creation and monetization accessible even to non-technical users .

ForkFlow transforms AI agents from isolated tools into tradable, collaborative digital assets.

**Challenges we ran into**

One of the biggest challenges while building ForkFlow was designing a system that combined AI workflows, decentralized ownership,payments into a seamless user experience.

Initially, integrating agent monetization with the Locus payment flow was difficult because the platform needed to support multiple actions like renting, purchasing, and forking agents while automatically handling creator royalties. Managing these interactions in a scalable and user-friendly way required restructuring the payment architecture multiple times.

Another major hurdle was handling dynamic AI agent generation from prompts. Since users could create completely different types of agents, we needed a flexible workflow system that could adapt to multiple agent behaviors without requiring hardcoded logic for every use case.

We also faced issues with secure API key management during development. GitHub push protection blocked deployments after detecting exposed API keys inside environment files. To solve this, we restructured the project using proper .env handling, added .gitignore protection, and regenerated compromised keys to improve project security.

These challenges helped us improve both the architecture and security of the platform, making ForkFlow more scalable and production-ready.

Janhvi Jathot

`2026-05-25`

---

### Draykon AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/draykon-ai-ed3d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://draykon-ai.pages.dev/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0iDPtBNGI-M?si=vqjiS83JCzd0ytz5) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Draykon AI - Built to Break Limits

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Natural Language Processing](https://img.shields.io/badge/Natural%20Language%20Processing-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square) ![UI/UX Design](https://img.shields.io/badge/UI/UX%20Design-333333?style=flat-square) ![Very Large Language Model](https://img.shields.io/badge/Very%20Large%20Language%20Model-333333?style=flat-square)

**The problem it solves**

**The Problem Draykon AI Solves**

Draykon AI is a comprehensive intelligent system designed to help users execute their ideas more quickly and efficiently.

**Problem**

Many people struggle to complete tasks effectively because they rely on multiple tools for different purposes, such as writing, coding, researching, and problem-solving. This often results in wasted time, decreased focus, and lower productivity.

**Solution**

Draykon AI offers a solution by providing a unified system powered by a large language model that understands user input and assists with various tasks within a single platform. Instead of switching between tools, users can interact with a single system to accomplish their work more effectively.

**Features**
- Multi-purpose task handling (writing, coding, and problem-solving)
- Fast and context-aware responses
- Simple and clean user interface
- Reduced dependency on multiple applications

**Implementation**

A working prototype has been developed to demonstrate how users can engage with Draykon AI. The project includes a functional interface, core system logic, and a demonstration of task execution.

**Impact**

Draykon AI helps users save time, maintain focus, and improve productivity by simplifying the task execution process. It makes advanced technology more accessible and practical for everyday use.

**Challenges**

Currently, the user interface is optimised for desktop use but does not perform as well on mobile devices.

**Links**
- Main Website: [https://draykon-ai.pages.dev/](https://draykon-ai.pages.dev/)
- Demo: [Draykon AI - Guest Page](https://draykon-ai.pages.dev/pages/guest)
- Login: [Login to Draykon](https://draykon-ai.pages.dev/pages/login)
- Feedback: [Give Feedback](https://draykon-ai.pages.dev/pages/feedback)
- Support Me: [Support the Developer](https://draykon-ai.pages.dev/pages/support)
- Presentation: [Draykon AI PPT](https://gamma.app/docs/From-Thought-to-Execution-q93te1lhfgxf3p1)

![image](https://assets.devfolio.co/content/5364220cdd924caf8f4e6a1e1510744a/60bda489-43bc-42dc-9a4f-c1524372ac28.png)

![image](https://assets.devfolio.co/content/5364220cdd924caf8f4e6a1e1510744a/5fa52871-e4c1-409f-828b-66efea8c47ba.png)

**Challenges we ran into**

### Overcoming Key Challenges in System Development

In our journey to create a robust system, we identified several primary challenges that demanded our attention and expertise. 

#### Ensuring Reliability Across Input Types

The first major challenge was guaranteeing that the system operates reliably across a diverse range of input types. This required us to:

- **Conduct Comprehensive Testing:** We implemented extensive testing protocols to understand how the system responds to various inputs, ensuring that it performs consistently under different scenarios.
- **Iterate Strategically:** Our approach involved multiple iterations of the design and functionality, allowing us to gather valuable insights from each version and refine our processes effectively.

#### Achieving Consistency and Relevance

To deliver consistent and relevant outputs, we concentrated on the following strategies:

- **Structured Processing:** We established a well-organised framework for how the system processes requests, enabling it to generate accurate responses based on user input.
- **Feedback Loops:** By incorporating user feedback at every stage, we ensured that our outputs resonated with the intended audience and met their expectations.

#### Maintaining Speed Amid Complexity

Another significant challenge was maintaining speed while managing intricate tasks. We approached this by:

- **Performance Optimisation:** Our team dedicated time and resources to optimise the system's performance, enhancing speed without compromising the quality of the outcomes.
- **Balancing Complexity and Efficiency:** We devised methods to simplify complex processes, allowing the system to perform efficiently even under heavy computational loads.

#### Prioritising Design

We recognised that design plays a crucial role in user experience. Our priorities included:

- **User-Centric Design Philosophy:** We aimed to create an interface that is both intuitive and aesthetically pleasing, allowing users to navigate effortlessly while accessing advanced functionalities.
- **Simplicity in Functionality:** Despite the complexity of the tasks being handled, we ensured that the system felt simple and user-friendly.

#### Continuous Improvement

To tackle these challenges effectively, we implemented a cycle of continuous improvement:

- **Rigorous Testing and Refinement:** We embraced a culture of testing and refinement, regularly updating the system based on performance metrics and user feedback.
- **Focused Interface Development:** Our commitment to a clean and focused interface ensured that users could engage with the system without distractions, leading to enhanced productivity.

Through these proactive measures and a determined mindset, we have successfully addressed the key challenges in developing a reliable and efficient system, setting the stage for ongoing success and innovation.

**Track: Checkout with Locus**

**Artificial Intelligence / Machine Learning**  
- **Deep Learning**: Exploring neural networks and their applications in various fields.  
- **Natural Language Processing**: Enhancements in understanding and generating human language.  
- **Computer Vision**: Advancements in image processing and visual recognition.  

---

**Innovation / Future Tech**  
- **Blockchain Technology**: Examining decentralised systems and their implications.  
- **Quantum Computing**: Understanding the potential of quantum mechanics in processing.  
- **Smart Cities**: Innovations aimed at improving urban living through technology.  

---

**Productivity Tools**  
- **Project Management Software**: Tools that enhance collaboration and organisation.  
- **Time Management Apps**: Solutions designed to optimise personal and professional schedules.  
- **Automation Tools**: Utilising technology to streamline repetitive tasks.

Team **Draykon AI** -- Himanshu Kumar Singh

`2026-04-26`

---

### Give With Locus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/give-with-locus-e75d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/GPT-64590/givewithlocus-paygentic-1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://givewithlocus.web.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Let AI find the cause, let Locus move the money.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Paywithlocus](https://img.shields.io/badge/Paywithlocus-333333?style=flat-square)

**The problem it solves**

**Live:** https://givewithlocus.web.app — click "Explore with demo account" on the login page to try it with a real USDC wallet (pre-funded on Base).

## Why this exists

Most people want to help. The hard part isn't wanting — it's trusting that your $20 actually reached the family it was meant for, finding a charity that works, and doing it without burning a Saturday on research.

Giving has always had two coupled problems: a **trust problem** (opaque payment rails, stale charity data, annual reports that lag a year behind) and a **rails problem** (slow cross-border payments, banking infrastructure that excludes the regions that need help most, and payment stacks that can't be composed with AI agents). Fixing either one has traditionally come at the cost of the other.

Locus is the first stack that collapses both problems into one integration. GiveWithLocus is what happens when you build for a world where those trade-offs are gone.

## What Locus makes possible — for donors, and for charities

**Trust you can see, not just receive.**

- A donor can watch their gift arrive on-chain, in **seconds** — every donation carries a BaseScan transaction hash. No waiting for an annual report.
- A charity can show its community, board, or regulator exactly where every dollar went — without a six-month PDF reconciliation project. Accountability becomes a public query, not a batch job.

**Rails built for the world, and for agents.**

- **Speed.** A drought-relief org gets the money in minutes, not 2 to 5 business days. When a family is waiting for water, minutes matter.
- **Reach.** A charity in rural Kenya doesn't need a US bank account or a SWIFT correspondent. They need a wallet, and Locus provisions one at signup, for free. No banking infrastructure required.
- **Cost.** A $5 donation from Jakarta to that Kenyan clinic arrives as $5, not $1.50 after wire fees. Gas is sponsored. Small generosity survives.
- **Composability.** An AI agent can actually do the work — find the cause via Locus-wrapped Brave search, verify the charity by reading its mission page through Locus-wrapped Firecrawl, execute the donation on Base, and receipt the donor with an on-chain link — all in one conversation.

## Who this serves

- **An individual donor** who wants to help with malaria nets in West Africa — types it in plain language, gets three verified options with impact scores, donates $5 with one click, receives an on-chain receipt in seconds.
- **A small charity** in a region where USD banking is hard to access — gets listed for free, accepts USDC from anywhere in the world, and grows through my email-escrow recruitment loop.
- **A CSR or foundation team** (on the vision roadmap) — operating a corporate giving budget as a programmable Locus wallet with sub-allowances per cause, and turning the annual ESG report into a BaseScan query instead of a six-month reconciliation.

## Why I built this

Giving should be easy to do, easy to verify, and easy to scale — whether you're giving $5 or $5 million. It should carry the donor's good intent all the way to the person who needed help, with nothing lost to fees, latency, or opacity on the way. Locus is what finally makes all three possible in the same stack. GiveWithLocus is my demonstration — built for people, not paperwork.

**Challenges we ran into**

### 1. Locus wallets have two addresses, and I was storing the wrong one

When you call Locus's registration endpoint, you get back an ownerAddress — an externally-owned account. But the on-chain **smart wallet** that donations should actually settle into doesn't exist yet at registration time. It takes about 30 seconds to deploy, and only appears on a subsequent call to the status endpoint.

I didn't realize this at first and stored the ownerAddress as each charity's deposit address. The result was a silent failure: every donation appeared to settle on-chain (because the ownerAddress is a valid 20-byte address and USDC transfers to it are perfectly legal), but the charity's Locus API would forever report a zero balance — because /pay/balance queries the smart wallet, not the owner.

I caught this during a live test when $0.50 had clearly left the donor's wallet but the charity couldn't see it. The fix was a backfill script that polls the status endpoint for every charity, updates the stored address to the deployed smart wallet, and preserves the old owner address under a previousOwnerAddress field. Two charities whose API keys had gone stale needed full re-registration. I also patched the registration helper to always poll-and-store correctly for any future wallet.

### 2. Direct USDC transfers don't emit webhooks

Only the checkout-sessions endpoint does. I learned this when agent-executed donations stayed stuck as "QUEUED" in my database forever, even though BaseScan showed they had confirmed within seconds. There was no callback path telling me to flip the status.

I solved this in three layers:

1. **Inline poll** — the donation tool now polls Locus's transaction history for up to ten seconds after sending, so the agent can announce confirmation in the same chat turn.
2. **Page-mount reconcile** — a reconciliation endpoint fires fire-and-forget on every dashboard and donations-page load, syncing stale statuses against live Locus state.
3. **Chat-page reconcile** — after discovering users who stayed on the chat page after donating still saw stuck statuses, I added a reconcile call on chat mount **and** after every assistant turn completes.

Now no matter where a user lands after donating, the status catches up within seconds.

**Using PayWithLocus.com to leverage our suite.**

GiveWithLocus uses **six Locus API endpoints plus the checkout SDK** — every one load-bearing, none decorative. The entire app is a demonstration of what becomes possible when payments, email escrow, pay-per-use web APIs, and smart-wallet provisioning all live behind one suite.

**Wallet provisioning.** Every donor and every charity gets a Locus smart wallet at signup via Locus's registration endpoint, with automatic polling of the status endpoint to capture the deployed smart-wallet address (not the EOA). Encrypted keys are stored server-side.

**Direct USDC transfers (pay/send).** When a user confirms a donation in the chat agent, the donor's wallet transfers USDC to the charity's wallet on Base mainnet. Gas-sponsored — the dollar amount the donor enters is exactly what the charity receives.

**Email escrow (pay/send-email).** The agent's recruit-charity tool invites off-platform nonprofits by sending USDC in escrow with a claim link. This is my growth flywheel: donors bring charities onto the platform without any admin touching a spreadsheet.

**Embedded checkout (@withlocus/checkout-react + checkout/sessions).** For users who prefer a classic flow over the chat, the donation page renders Locus's embedded checkout against a session created server-side with the charity's API key. A webhook verifies the HMAC signature with the session's stored secret and flips the donation to confirmed.

**Brave web search** (Locus-wrapped, $0.035 per call). When the agent can't find a matching charity in my verified database, it searches the web. Metered per call, so research spend scales with actual agent usage — not a monthly subscription.

**Firecrawl scraping** (Locus-wrapped, $0.003 per call). The agent reads mission pages and impact reports directly from charity websites, giving the donor live evidence rather than a ten-year-old review page.

**Transaction history (pay/transactions).** Used by my donation-status reconciler — since pay/send does not emit webhooks, I poll this endpoint to sync stale database statuses against live Locus state, in three places (on chat mount, on dashboard mount, after every agent turn).

Without Locus I would have needed to build a custom payments stack, a wallet system, a web-search integration, a scraper billing layer, and a checkout UI — plus the escrow and gas-sponsorship logic. With Locus, all of that is one composable suite, and the hackathon project works end-to-end: **real money, real blockchain, real charities.**

Team **athena19** -- Samuel Mulia

`2026-04-13`

---

### Buildr
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/buildr-1f2e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://buildr-ashen.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/VP-88nZh8Qg) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Agents hire agents. USDC settles it.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square) ![Server-Sent Events (SSE)](https://img.shields.io/badge/Server--Sent%20Events%20(SSE)-333333?style=flat-square) ![Claude (Anthropic)](https://img.shields.io/badge/Claude%20(Anthropic)-333333?style=flat-square)

**The problem it solves**

**Today, AI agents can't pay each other.**                  
                                                                              
  If you want to build an agent that scrapes a website, summarizes the        
  content, translates it, and generates a marketing image — you need five     
  separate API subscriptions, five billing dashboards, five credit cards, and 
  a ton of glue code. There's no primitive for one agent to *hire* another.   

  buildr fixes this by creating an autonomous economy where AI agents         
  discover, negotiate with, and pay specialist agents in **real USDC on Base, 
  settled through Locus**. Zero humans in the loop for transactions.          
                                                            
  ### What people can use buildr for                                          
  
  - **Compound workflows** — submit a natural-language task ("research AI     
  payments, summarize, translate to Japanese, generate a blog image") and
  watch 4+ specialist agents get hired in real-time, each doing one thing well
  - **One wallet, many APIs** — a single Locus-funded wallet transparently
  pays for Firecrawl, Exa, OpenAI, Anthropic, Stability AI, DeepL, Deepgram,  
  Brave Search, and Perplexity — no upstream accounts needed
  - **New revenue for agent builders** — register your AI agent, set a USDC   
  price-per-call, earn directly to your wallet or email                       
  - **Programmable spend guardrails** — Locus policy limits (per-tx caps,
  allowances, approval thresholds) let orchestrators spend safely without     
  human approval for every action                           
                                                                              
  ### Why it's safer than existing workflows                                  
  
  - **Auditable on-chain** — every agent payment is a real Base USDC          
  transaction with a clickable Basescan link. No opaque credit card
  statements.                                                                 
  - **Price discovery, not price gouging** — 2-round negotiation auction
  settles at ~80% of asking price                                             
  - **Escrow-backed email payments** — recipient agents can use emails instead
   of wallets; funds sit in escrow until claimed                              
  - **Transparent execution trail** — every sub-task, agent hire, payment, and
   tx hash is logged and replayable in the Playground                         
                                                            
  ### The end state we're building toward                                     
                                                            
  An internet where any AI agent can transact with any other AI agent,        
  autonomously, without humans wiring money or maintaining API keys. buildr is
   the proof that the primitive already works — today, on Base, via Locus.

**Challenges we ran into**

### 1. "Hex key ≠ API key" — the auth rabbit hole
                                                                              
  Locus gives you two things when you sign up: a **wallet recovery key**      
  (`0x...`) and an **API key** (`claw_dev_...`). I spent an hour trying to    
  Bearer-auth with the hex key before reading the docs carefully. Fix: use    
  `claw_dev_*` for Bearer, never send the hex key anywhere. 

  ### 2. Wrong base URL in early integration                                  
  
  Started with `https://api.paywithlocus.com/api` — all calls 404'd. Turns out
   the beta environment lives at `beta-api.paywithlocus.com/api`. The API key
  type determines the environment. Added the correct URL as a constant at the 
  top of `lib/locus.ts`.                                    

  ### 3. Transaction hashes aren't returned synchronously                     
  
  A Locus `POST /pay/send` returns `{ transaction_id, status: "QUEUED" }` —   
  the actual on-chain `tx_hash` only appears after 10–30 seconds when Base
  confirms the block. For the demo to show real Basescan links in the         
  execution timeline, I had to **poll** `/pay/transactions/:id` up to 5 times
  at 2s intervals right after each transfer, then persist the `tx_hash` to
  SQLite and include it in the SSE event stream.

  ### 4. Background tasks dying on navigation

  Initially the orchestration ran inside the React `useEffect` hook of the    
  orchestrate page. The moment a user clicked "Marketplace" to browse agents
  while a task was running, the SSE reader got garbage-collected and the whole
   pipeline vanished. Moved the entire run logic out of React into a **Zustand
   store with an async runner** that lives in the module, not the component.
  Now tasks survive navigation and a new topbar badge shows "N running" so you
   can jump back to the live view.

  ### 5. Keyword-based decomposition was too brittle

  My first `decomposeTask` was a wall of `if (input.includes("translate"))`.  
  It failed hilariously on "help me launch my SaaS" (just routes to
  summarization). Replaced it with a **Claude structured-output call** that   
  returns `{subTasks: [{category, description}]}` JSON constrained to a
  whitelist of 17 categories. Kept the keyword version as a graceful fallback
  when the API key isn't set.

  ### 6. Next.js server/client component minefield                            
  
  Passing `onMouseEnter` handlers from a server component into a client       
  component throws a stringify error in Next.js 16. Hit it three separate
  times across the redesign. Solution: any component with JS event handlers   
  gets `"use client"` at the top, and purely decorative hover effects use CSS
  `:hover` selectors instead.

  ### 7. Port mismatch killed internal agent calls                            
  
  The orchestrator fetches specialist endpoints via                           
  `${NEXT_PUBLIC_APP_URL}${agent.endpoint}`. My `.env.local` said port 3000
  but my dev server auto-shifted to 3002 because 3000 was occupied. Every     
  specialist call timed out silently and fell back to `[Demo]` text. Fixed by
  always aligning env var to actual runtime port and adding a log line when
  the fetch fails.

**Using PayWithLocus.com to leverage our suite.**

- Best Use of Locus Payments — primary track (we use pay/send,              
  pay/send-email, pay/balance, pay/transactions, gift-code-requests, and 9
  wrapped APIs)                                                               
  - Best Paygentic Agent / Best AI Agent — agent-to-agent economy
  - Best Developer Tool / Infrastructure — buildr is a primitive for agent    
  composition                                                                 
  - Grand Prize / Main Track                                                  
  - Best UI/UX (if available)

Team **lumo** -- [Shinjan Patra](https://github.com/flaminshinjan), Tanish Vadel

`2026-04-16`

---

### SignFlow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/signflow-a1cb) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=KDsyd7BzeiA) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=aVUMpGVybJw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Translating hands into voices

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Mediapipe](https://img.shields.io/badge/Mediapipe-333333?style=flat-square)

**The problem it solves**

Millions of deaf and non-verbal individuals face communication barriers every day because most people do not understand sign language. This affects their education, job opportunities, confidence, and ability to communicate freely in daily life.

Sign Flow solves this problem by acting as a real-time communication bridge between deaf and hearing individuals.


**What people can use it for:**
1. Communicating easily with deaf or non-verbal people without knowing sign language
2. Helping deaf students understand teachers in classrooms
3. Assisting conversations in hospitals, offices, banks, and public places
4. Improving accessibility and inclusion in workplaces and education
5. Enabling deaf individuals to express themselves confidently and independently

**How it works:**

Speech/Text → Sign Language
- Spoken or typed words are converted into Indian Sign Language.

Sign Language → Text
- Hand gestures in sign language are converted into readable text.


**Why it matters**
Sign Flow reduces communication gaps, promotes inclusion, and helps deaf individuals become more independent in everyday life. Because apparently in 2026 humans can talk to satellites but still struggle to talk to each other face-to-face. Incredible species honestly.

**Challenges we ran into**

One of the biggest challenges was making the sign language recognition accurate in real time. Hand gestures can look very similar, and small changes in finger position or camera angle sometimes caused incorrect detections. To improve this, I spent a lot of time training and testing different gesture inputs and refining the detection logic using Python.

Another challenge was creating smooth and understandable sign language animations for the text-to-sign feature. Since Indian Sign Language resources are limited online, I had to manually work on animations using Blender and integrate them properly into Unity. Synchronizing animations with translated text without delays was also difficult initially.

I also faced performance issues while trying to make everything work smoothly on mobile devices. Some processes were slow or laggy during real-time translation. I optimized the workflow and reduced unnecessary processing to improve responsiveness.

The biggest non-technical challenge was understanding the real problems faced by deaf individuals. To solve this, I visited and tested the project with deaf students at Sanjay School in Porvorim. Their feedback helped me improve the usability and overall communication experience of the app.

Turns out building inclusive technology is harder than making another food delivery app. Shocking revelation for the tech industry honestly.

**Using LocusFounder to Build a Business!**

Sign Flow has the potential to grow beyond a student project into a scalable accessibility startup focused on inclusive communication.

Millions of deaf and non-verbal individuals still face communication barriers in schools, workplaces, hospitals, and public services because sign language support is limited. Sign Flow solves this through real-time speech/text ↔ Indian Sign Language translation.

This project can evolve into a business by:

- Partnering with schools and colleges for accessibility support
- Integrating with hospitals, customer service, and government services
- Offering API or SDK access for apps and platforms
- Collaborating with companies like Google, Apple, or Microsoft for accessibility integration
- Providing enterprise accessibility solutions for workplaces

The goal is not just to build an app, but to create technology that makes communication inclusive for millions while building a sustainable accessibility-focused platform.

[Harsh Marathe](https://github.com/HarshMarathe0505)

`2026-05-08`

---

### Credeasy
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/credeasy-869b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dasouvik122005/Credeasy) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Your digital footprint is your new credit score.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Joblib](https://img.shields.io/badge/Joblib-333333?style=flat-square) ![LightGBM](https://img.shields.io/badge/LightGBM-333333?style=flat-square)

**The problem it solves**

Millions of individuals - such as gig workers, young professionals, and the unbanked - are considered **New To Credit (NTC)** or have "thin credit files". Because they lack a traditional credit history, legacy scoring models automatically reject them, creating a frustrating Catch-22: *you need credit to get credit*.
**Credeasy** bridges this gap by analyzing **alternative behavioral data** to generate accurate credit scores. Instead of relying on past bank loans, our AI engine evaluates a user's digital footprint and daily financial habits:
- 💸 **Wallet Inflow Consistency** (e.g., Daily/Weekly UPI transactions)
- 📱 **SIM Card Tenure** (Proving long-term stability)
- 📶 **Airtime Recharge Regularity** (Consistent monthly plans vs. irregular emergency micro-topups)
- ⚡ **Utility Payment Discipline** (Paying electricity or broadband bills on time)
### Why it Matters
* **For Lenders & Fintechs:** Provides a safe, data-driven way to underwrite loans for a massive untapped market without taking on blind risk.
* **For Borrowers:** Provides a fair, accessible, and transparent way to prove financial responsibility and secure capital for businesses, education, or emergencies.

**Challenges we ran into**

Building a platform that bridges complex machine learning with a seamless user experience brought several hurdles:
1. **Quantifying "Messy" Alternative Data**  
   Translating non-traditional data points into a mathematical risk signal was difficult. We had to carefully engineer features and assign weights to ensure that behaviors like `Irregular Emergency Topups` correctly correlated with financial volatility, while `Consistent Monthly Plans` signaled stability.
2. **Explainable AI (XAI) over Black-Box Models**  
   > **Note:** Lenders and users don't trust a random number. 
   
   A major challenge was taking our model's probability outputs and translating them into human-readable **SHAP decision attributions**. We built logic that clearly explains exactly *why* a score was given (e.g., `+35 pts: 3+ Years SIM Tenure` vs `-40 pts: Frequent Missed Utility Payments`).

Team **ThetaZen** -- [Souvik Das](https://github.com/dasouvik122005), [Tridib Biswas](https://github.com/GITtridib22), [Locket Chattaraj](https://github.com/Locket51), [Rashmi Pyne](https://github.com/rashmi-crypto)

`2026-08-27`

---

### Saheli Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saheli-ai-d69b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://saheliai.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Your Virtual Safety Companion.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

### The Problem It Solves

Women often face safety concerns while traveling alone, especially during late hours or in unfamiliar locations. Most existing safety applications are reactive and depend on users manually triggering an SOS after an emergency has already occurred.

**Saheli AI** addresses this challenge by providing a proactive safety ecosystem that focuses on prevention, protection, and preparedness.

The platform helps users:

* Find safer travel routes instead of only the fastest routes.
* Share live locations with trusted contacts.
* Access emergency support through SOS, emergency calling, and safety alerts.
* Locate nearby police stations, hospitals, and medical stores.
* Learn self-defense and situational awareness through dedicated training resources.
* Enhance personal safety through features such as Safety Siren and Virtual Companion Mode.

By combining AI-powered safety intelligence, emergency response tools, safe navigation, and self-defense education, Saheli AI empowers women to travel with greater confidence and security.

**Challenges we ran into**

### Challenges We Ran Into

One of the biggest challenges we faced was working under severe time and connectivity constraints during the offline hackathon. Although the event was scheduled as an 8-hour hackathon, the effective development time was significantly reduced due to delays in the event schedule. Additionally, unstable Wi-Fi, slow internet speeds, and occasional device performance issues made development and testing difficult.

Since several core features of Saheli AI, such as maps, live location services, and AI-powered functionalities, depended on internet connectivity, these issues impacted our ability to rapidly iterate and test the application. To overcome this, we prioritized the most critical features, divided responsibilities efficiently among team members, and focused on building a stable proof of concept rather than attempting to implement every planned feature.

Another challenge was integrating multiple functionalities—including safe route planning, emergency response mechanisms, community safety intelligence, and self-defense resources—into a single cohesive user experience within a limited timeframe. We addressed this by simplifying the workflow, reducing unnecessary complexity, and concentrating on the core user journey.

Despite these obstacles, our team successfully developed and demonstrated the concept, gaining valuable experience in rapid problem-solving, teamwork, and building under pressure.

Team **Syntax League** -- [Snehasish Saha](https://github.com/snehasishlabs), [Rana Pratap Roy](https://github.com/RP-Roy), Niranjana Karmakar, [Shilajit Paul](https://github.com/shilajitpaul2005-ui)

`2026-08-30`

---

### VeriPay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/veripay-ai-verifies-before-paying-430c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyansh-narang2308/veripay) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://veripay.priyanshnarang.in/) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> AI agents that act. Payments you can trust.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

**The Problem**: AI agents can authorize payments, but they blindly trust that physical-world services were actually completed.

**The Solution**: I engineered VeriPay to solve this "trust after spending" gap by introducing an autonomous escrow guardrail that uses a Vision AI model to cryptographically compare before/after photos, only settling Prava funds if the work is visually verified.

**Why it's useful today**: As agentic commerce scales rapidly, my architecture proves that agents can safely operate as fiduciary proxies by possessing the capability to say "No" to fraudulent contractor claims.

**What's next**: I plan to scale my Tri-Agent architecture to include real-time video verification and an automated, zero-knowledge dispute resolution protocol.

**Challenges we ran into**

1. Prava Escrow State Management:
My biggest integration hurdle was preventing payments from settling immediately. 
I had to dive deep into the Prava documentation to implement the **awaiting_result** holding state. I resolved this by explicitly creating scoped sessions and delaying the final settlement until the backend fired the **POST /v1/sessions/report-status** webhook with the AI's final **APPROVED** or **DECLINED** judgment.

2. Vision AI **False Positives** (Prompt Engineering):
Initially, the Vision Verification Agent was too lenient, approving "After" photos even if they were blurry or irrelevant. I debugged this by replacing simple prompts with a strict mathematical delta-analysis protocol. The agent is now forced to cryptographically compare the specific damage in the "Before" photo with the exact same spatial coordinates in the "After" photo before outputting a strict boolean decision.

3. Serverless DB Cold Starts (Neon & Prisma):
During deployment to Vercel, the Prisma client kept throwing 500 errors (**PrismaClientInitializationError**) on the dashboard because our Neon Serverless Postgres database would scale to zero and timeout during cold starts. I debugged the Vercel logs, customized the **vercel.json** build commands to strictly enforce Prisma generation, and adjusted the connection pooling limits to handle the cold start latency seamlessly.

**Best Visa Intelligent Commerce Implementation**

VeriPay represents the future of Visa Intelligent Commerce by moving beyond static payments into dynamic, AI-gated financial routing. By natively integrating Prava's Agentic Payments Sandbox, we built a closed-loop escrow system. We use Prava's POST /v1/sessions to generate time-locked, merchant-scoped virtual credentials. The transaction is then held in an awaiting_result state until our Vision AI verifies the physical work is completed, at which point the AI automatically hits Prava's report-status endpoint to authorize the final settlement.

**Most Startup-Ready Product**

VeriPay isn't just a hackathon script; it is a fully engineered, production-ready SaaS platform. We built a robust architecture using Next.js 15 (App Router), a Neon serverless PostgreSQL database, and Prisma ORM to handle complex relational state machines between users, properties, and agent runs. The frontend utilizes Shadcn UI and custom Framer Motion routing for a premium, zero-latency user experience. The product solves a massive real-world problem, contractor fraud and invoice chasing in property management, making it highly viable for immediate customer onboarding and VC pitching.

**Participation Credits (Already Claimed)**

VeriPay is heavily powered by OpenAI's latest models via OpenRouter to orchestrate our autonomous escrow pipeline. We utilize gpt-4o-mini for our Vendor Discovery Agent to rapidly parse property maintenance issues, evaluate urgency, and generate localized quotes. More importantly, we use the flagship gpt-4o multimodal model for our Vision Verification Agent. When a contractor uploads a photo of a completed repair, gpt-4o mathematically compares the "Before" and "After" images to verify the physical work, acting as the final cryptographic judge that releases the Prava escrow funds.

**Best Prava Adapter for the NANDA Town**

We built the exact, reusable Prava payments adapter required for physical-world agentic commerce. Our architecture handles the entire transaction lifecycle: negotiating with mock contractors, securing the budget in a Prava session, and—most importantly, handling failure conditions using Prava’s Agentic Payments Sandbox. If our Vision AI detects that a contractor's work is incomplete or faked, our adapter automatically reports DECLINED to the Prava API, safely blocking the payment and proving that AI agents can act with true fiduciary responsibility.

**Agent Commerce Discovery & Trust**

VeriPay solves the "merchant discovery" problem by engineering a dedicated Vendor Discovery Agent. Because autonomous agents must never route payments to fraudulent vendors, our database architecture natively implements a TrustScore model designed specifically to consume Senso as our primary trust and discovery signal. When a tenant requests a repair, our Discovery Agent leverages Senso's verified merchant data to filter local contractors. It ensures that it only generates quotes and spins up Prava payment sessions for highly reputable, Senso-verified merchants, completely mitigating vendor fraud in the autonomous commerce loop.

**Best Agentic User Experience**

Most agentic commerce projects rely on clunky, text-heavy chatbot interfaces that confuse users. VeriPay reinvents the agentic UX by embedding the AI directly into a premium, native-feeling SaaS dashboard.

We achieved this by utilizing a Next.js 15 App Router foundation paired with Framer Motion to create buttery-smooth, zero-latency transitions. Our custom MotionLink architecture ensures that navigating the dashboard feels like a native macOS application rather than a web app.

Furthermore, we abstracted the intense complexity of multi-agent orchestration and Prava's escrow API into a beautiful, human-readable UI Stepper. Instead of reading through terminal logs or chat histories, landlords simply see visual state changes (Analyzing ➔ Payment Authorized ➔ Verification Passed). By masking the complex financial rails behind a stunning, intuitive interface, VeriPay makes autonomous agentic commerce accessible to everyday consumers.

[Priyansh Narang](https://github.com/priyansh-narang2308)

`2026-08-01`

---

### Vouch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vouch-ac67) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rocker1166/vouch) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vouch-prava.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8izb4I5Hw2g) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Approve a budget once. The agent does the buying.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Prisma](https://img.shields.io/badge/Prisma-333333?style=flat-square) ![Vercel AI SDK](https://img.shields.io/badge/Vercel%20AI%20SDK-333333?style=flat-square) ![Neon Postgres](https://img.shields.io/badge/Neon%20Postgres-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square) ![visa](https://img.shields.io/badge/visa-333333?style=flat-square) ![senso](https://img.shields.io/badge/senso-333333?style=flat-square)

**Challenges we ran into**

- Our first Prava integration didn't actually enforce anything — session-per-order authorized a $400 order against a $242 budget, because the cap is only checked when a charge is attempted. Our own acceptance test caught it. Rebuilt on standing mandates, so now Visa itself declines: `DECLINED — Total amount 400.00 exceeds threshold 242.00`.

- Three mandates couldn't mint payment credentials and we almost filed a bug with Prava. Turned out the generic published test card just can't mint cryptograms in the sandbox — a different card worked first try. Withdrew the report, felt a bit stupid, moved on.

- Every real Linq webhook 400'd, and from our side it looked like Linq never called us at all. A dashboard screenshot showed them calling us every time. Our subscription had silently negotiated a newer webhook version with a different payload shape, so every real text parsed to "no message". Fixed it against their documented example, verified with a real text from a real phone moving real stock.

- Shopify's UCP gateway wants a Shopify-Buyer-IP header that's in neither the UCP spec nor Shopify's docs. Only presence matters — found it by throwing headers at a real store until one stuck.

- Smaller ones: real merchants send checkout totals as an array not an object, so every real purchase silently read total=null and died before authorize; and our webhook dedupe was an in-process Set, which buys twice on serverless — moved idempotency into Postgres before it could fire.

**The problem it solves**

Keeping a business stocked and paid-up is tiring, manual work — someone has to notice what's running out, remember what's due, compare prices, and place the orders. It eats hours small teams don't have. And money slips away too: subscriptions quietly get more expensive, and some invoices come from fakers pretending to be a real company. Vouch does this whole chore for you: set a budget once, and it watches what's running low or due, checks the seller is real, and buys it — and the spending limit sits with Visa, so if the agent ever tries to spend too much, the card itself says no. Your team just texts it ("we drank 5 cokes"). Today it handles subscriptions and restocks; next, everything else a business pays for.

**Best Visa Intelligent Commerce Implementation**

The whole product is built on Prava mandates: one standing mandate per merchant, capped at that merchant's ceiling, registered at the card network. The over-budget block is Visa's decision, not our code — there is no `if (total > cap)` on the money path. Proven with a real $400-vs-$242 decline (correlation id in the repo) and a real completed sandbox order on a real merchant.

**Most Startup-Ready Product**

Judge it like a startup: the loop (detect → verify → cap → buy → ledger) is the product, renewals and restock are just the first two rails. Deployed and public (vouch-prava.vercel.app), no demo-ware — sandbox is a key, not a code path; going live is an env var. Clear ICP (cafés, clinics, small offices), a real wedge (network-enforced spending authority for agents), and honest limits stated in the repo.

**OpenAI**

Two agents on the OpenAI API (gpt-5): an autonomous procurement cycle built on the OpenAI Agents SDK with five guardrails and a deterministic oracle test (`npm run agent:check` asserts the agent reproduces every outcome — money, supplier pick, vendor check, decline, and the silence on a blocked order), plus an interactive chat/SMS agent driving the same money core. Real tool loops, not a ChatGPT wrapper.

**iMessage Agent**

The Linq surface is real and two-way: Partner API v3, Standard Webhooks HMAC verification, replay protection, DB-backed `webhook-id` idempotency so a retry can't buy twice. Named team members text the agent and get replies attributed by name on the ledger; strangers can join by texting a PIN, or get refused — verified live both ways with real texts moving real stock. The agent also decides on its own when to text a product photo (a real tool call, not a post-process).

**Agent Commerce Discovery & Trust**

Senso is our WHO guard: before any payment, the vendor's billing domain is verified against a grounded Senso knowledge base. A spoofed Adobe invoice from `adobe-billing.co` is dropped by name — "not Adobe's billing domain on file" — before money moves. It fails closed: a vendor Senso can't verify is a vendor we don't pay. Trust decides which merchant the agent engages, which is exactly this track's brief.

**Best Agentic User Experience**

The UX thesis is that the best agent interaction is often silence: a blocked order never interrupts you, and the reason lives on the ledger. What does reach you is one chat (web) or one text thread (SMS) — the same agent on both. Purchases pause on a real confirm-before-spending card, receipts carry a one-tap revoke link, first run is a guided tour that ends by talking to the agent, and the whole team shares the surface with per-person attribution.

**Agentic Commerce Hackathon**

Prava is the core of the product, not an add-on. Every merchant gets a standing mandate capped at its ceiling; the agent charges within it and Visa declines anything outside it — we relay the network's own `DECLINED — exceeds threshold` verbatim, with correlation id. Real sandbox settles including a live checkout on a real UCP merchant (restaurantware.com, verified against Prava's own mandate record). Going live is flipping an env var, not a rewrite.

Team **Innovisionaries** -- [Suman Jana](https://github.com/rocker1166), [Arnab Mondal](https://github.com/codewarnab)

`2026-08-03`

---

### viGEMMAlya
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vigemmalya-528d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gauravmishraokok/GemmaHack2026) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/KBatGV2byss) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/KBatGV2byss) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Trust, Trace , Explain Money Laundering Detection

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

# Challenges We Ran Into







---



## 🧠 Training an Effective Risk Model



Our biggest challenge was building a risk model that could distinguish genuinely suspicious activity from the huge number of legitimate transactions.



- Cleaned and engineered features from a banking transaction dataset containing millions of records.

- Built an XGBoost-based risk model instead of relying purely on rule-based detection.

- Iteratively tuned features, thresholds, and hyperparameters to reduce false positives while maintaining high recall.

- Designed the pipeline so updated transaction data can continuously improve the model through periodic weight retraining instead of requiring a complete rebuild.



---



## 📊 Preparing the Dataset



Real financial datasets are messy.



Some records lacked KYC details, customer relationships, or consistent formatting.



To make the reasoning pipeline reliable we had to:



- Normalize currencies, timestamps and identifiers.

- Engineer graph-friendly relationship features.

- Manually enrich missing KYC metadata.

- Validate every generated feature before model training.



Without a clean dataset, even the best model produced unreliable results.



---



## 🔗 Discovering Hidden Relationships



Money laundering rarely appears as isolated transactions.



The difficult part was discovering hidden networks between customers.



To solve this we:



- Constructed transaction graphs.

- Connected customers using shared PANs, addresses, devices and transaction behaviour.

- Used the **Louvain Community Detection Algorithm** to automatically identify suspicious communities instead of analysing accounts individually.



This dramatically improved case generation quality.



---



## 📚 Research Concepts We Incorporated



Instead of building a simple LLM wrapper, we incorporated multiple research-backed techniques into the pipeline.



### 1. Activation Probing



Rather than using only Gemma's generated text, we experimented with reading intermediate neural activations to estimate risk directly from the model's internal representations.



### 2. GBNF Constrained Generation



Compliance reports cannot invent legal terminology.



Using **GBNF (Grammar-Based Normal Form)** constrained decoding forces the model to generate only valid report structures and approved legal categories.



### 3. Evidence-First Reasoning



The model is never allowed to "reason first."



Instead it must:



1. Gather evidence

2. Verify supporting facts

3. Decide whether sufficient evidence exists

4. Generate the report



If evidence is insufficient, the pipeline refuses to generate conclusions.



### 4. Concept Drift Detection & Incremental Learning



Financial behaviour changes over time.



Instead of treating the model as static, the system is designed to detect dataset drift and periodically retrain the XGBoost model using newly available transaction data, ensuring risk predictions remain accurate.



### 5. Graph-based Community Detection



We integrated graph analytics using the **Louvain Algorithm** to identify coordinated transaction communities, significantly improving the quality of suspicious case detection.



---



## 🤖 Making Gemma Reliable



Running Gemma locally introduced several engineering challenges.



- Larger models exceeded available memory on our hardware.

- Smaller models required careful prompt engineering to preserve report quality.

- Internal reasoning consumed the response budget, causing incomplete outputs until context limits were adjusted.

- Response verification was added to ensure every numerical value generated by the model exactly matched the original transaction data.



---



## ⚖️ Balancing Explainability and Accuracy



Unlike traditional LLM applications, every statement in an STR must be legally defensible.



We therefore built multiple verification layers:



- Every monetary value is cross-checked against source transactions.

- Every conclusion must reference supporting evidence.

- Confidence scores are generated for every section of the report.

- Reports cannot be produced when sufficient evidence is unavailable.



This guarantees the compliance officer always understands **why** the model reached a particular conclusion instead of receiving a black-box prediction.



---



## 🔬 Research Papers That Guided Our Design



Our implementation draws inspiration from multiple research directions rather than a single model:



- **Activation Probing / Linear Probes** — understanding model internal representations.

- **Louvain Community Detection** — graph-based fraud and relationship discovery.

- **GBNF Grammar-Constrained Decoding** — structured and deterministic LLM outputs.

- **Evidence-First / Retrieval-Augmented Reasoning** — preventing hallucinations by grounding every conclusion in evidence.

- **Concept Drift Detection & Incremental Learning** — maintaining model performance as financial behaviour evolves.

**The problem it solves**

# The problem it solves

## In one line

Small banks can't afford enterprise-grade AML compliance, while cloud AI solutions cannot legally process sensitive financial data. **viGEMMAlya** solves both problems by running entirely on the bank's own infrastructure and automating the most time-consuming parts of AML investigations.

---

## The problem, broken down

Every bank in India—whether a large commercial bank, NBFC, or co-operative bank—is required to monitor transactions for suspicious activity and submit a **Suspicious Transaction Report (STR)** within **7 working days** whenever money laundering is suspected. Missing this deadline can lead to significant regulatory penalties.

The challenge is that:

- **Small banks cannot afford large compliance teams.** Large institutions employ dedicated AML departments, whereas many smaller banks have only one or two compliance officers responsible for the entire process.

- **Rule-based alert systems generate overwhelming false positives.** Simple rules such as *"Transaction amount > ₹10 lakh"* often flag thousands of legitimate transactions. Every alert still requires manual investigation—reviewing transaction history, identifying linked accounts, checking KYC information, determining applicable regulations, and preparing documentation.

- **Cloud AI is not a viable solution.** Banking regulations and India's DPDP Act require sensitive customer financial data to remain within the bank's infrastructure. This prevents institutions from sending transaction data to external AI services, regardless of their capabilities.

---

## What we built

### Stage 1 — Batch Engine (:8001)

Processes millions of transactions and narrows them down into a small number of genuinely suspicious cases.

**Responsibilities**
- Rule-based transaction screening
- Machine Learning risk scoring
- Transaction clustering
- Gemma-based internal risk representation
- High-risk case generation

↓

### Stage 2 — Reasoning Engine (:8002)

Investigates each suspicious case before generating a compliance report.

**Responsibilities**
- Collect supporting evidence
- Build investigation timeline
- Discover linked accounts
- Check KYC and risk indicators
- Verify whether sufficient evidence exists
- Generate Suspicious Transaction Report (STR)
- Verify every numerical value against source data
- Produce sentence-level confidence scores

↓

### Stage 3 — Human Review

The compliance officer reviews the AI-generated report and either approves or rejects it.

After approval, the system automatically:

- Sends Email notification
- Sends WhatsApp notification
- Exports the official filing
- Updates the immutable audit log

---

**Most importantly, the entire pipeline runs completely offline on the bank's own infrastructure. No customer financial data ever leaves the organization.**

---

## Who this helps and how

| Stakeholder | Benefit |
|--------------|---------|
| **Compliance Officers** | Spend minutes instead of hours investigating each case. The AI prepares the first draft while the officer focuses on verification and approval. |
| **SME Customers** | Faster investigations reduce unnecessary account freezes, allowing businesses to continue payroll, supplier payments, and daily operations. |
| **Loan Applicants** | AML verification becomes significantly faster, reducing delays in loan approvals. |
| **Businesses with complex transaction patterns** | Lower investigation costs enable banks to onboard legitimate customers that would otherwise require expensive manual reviews. |
| **Banks** | Receive automated report generation, complete audit trails, instant notifications, and compliance-ready documentation while keeping all sensitive data on-premise. |

**2nd Runner Up**

# Why this fits Track 2 — Gemma Financial Compliance & Risk Triage

> "Develop an intelligent compliance assistant that analyzes transactions, onboarding documents, and financial records to detect anomalies, assess risk, summarize findings, and generate compliance-ready reports for review teams."

---

## Mapping to the judging criteria

| Track Requirement | Our Implementation |
|-------------------|--------------------|
| **Analyze transactions & financial records** | Processes a real 5-million-row banking transaction dataset using rules, ML scoring, and clustering. |
| **Detect anomalies** | Gemma-based risk model analyzes each case using internal model representations instead of prompt-only reasoning. |
| **Assess risk** | Produces risk scores, confidence values, and Out-of-Distribution detection with Red/Yellow/Green classification. |
| **Summarize findings** | Generates plain-English summaries linked directly to supporting evidence. |
| **Generate compliance-ready reports** | Produces structured STR reports using official regulatory terminology with confidence highlighting. |
| **Onboarding documents** | Already incorporates KYC status, jurisdiction risk, and shell-company indicators. The architecture supports future document ingestion. |

---

## What makes it more than "just an LLM wrapper"

- 🧠 **Uses Gemma's internal representations** for risk scoring rather than prompt engineering alone.
- 🔒 **Restricts legal classifications** to valid predefined categories at generation time.
- 🎯 **Provides sentence-level confidence** backed by evidence verification.
- 🔐 **Runs completely offline**, satisfying regulatory data residency requirements.
- ✅ **Maintains a complete audit trail**, including report generation, verification, attestation, notifications, and filing.

Team **Cute Potatoes** -- [Mishka Tiwari](https://github.com/mishhkaaa), [Kamal Karteek U](https://github.com/Kamalllx), [khushi dubey](https://github.com/khushidubeyokok), [Gaurav Mishra](https://github.com/gauravmishraokok/gauravmishraokok)

`2026-07-20`

---

### Shield With Locus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shield-with-locus-e7e7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/GPT-64590/shieldwithlocus-paygentic-2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shieldwithlocus.v1c.dev/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Runtime security for every BuildWithLocus service.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-333333?style=flat-square) ![BuildWithLocus](https://img.shields.io/badge/BuildWithLocus-333333?style=flat-square)

**The problem it solves**

# The problem ShieldWithLocus solves

A few weeks ago I deployed a Next.js app to an AWS instance in Singapore. Twelve days later a commodity botnet had found it, exploited the runtime, and used the box to pump 1.15 TB of traffic at a Brazilian Minecraft server for three days. I didn't notice the attack, AWS emailed me about the bill. The attacker had no idea who I was. Their botnet just scans the public internet looking for anything reachable and vulnerable. I was both. That was enough.

The whole story was already in my container logs: nineteen documented probe sessions, the name **innocentzero** hard-coded into their payloads, shell commands failing with attacker URLs right there in the error text. Twelve days of evidence sitting in stdout. Nobody was reading them.

The ugly part isn't that I got hit. It's how ordinary it was.

AI is pulling more people into shipping software right now than at any point in twenty years; students, solo founders, career-changers. The first version of anything you ship is the version you don't know how to secure yet. The tools that helped you ship it in a weekend don't come with a security team bundled in. Meanwhile commodity botnets are industrialized, scanning every IPv4 constantly, recruiting cheap cloud instances as free bandwidth for whoever paid them that week. The gap between "I shipped" and "I'm in a botnet" is measured in days.

**ShieldWithLocus** is for that gap. It's the runtime watchdog that would have caught my incident the same day instead of three days later, and it can be small because **BuildWithLocus** already ships everything it needs: a live log SSE stream on every service, and a deploy API that can scale to zero, roll back, or restart with one call.

## What it does

**Detect.** A 25-rule IOC engine reads every log line as Locus emits it — scanner probes, RCE payloads, brute-force, SQL injection, malware handles, entropy-guarded secret leaks. No LLM in the baseline path; severity compounds over a rolling window.

**Explain.** When an incident opens, LLM streams a Zod-validated report — classification, timeline, remediation, executive summary. Capped at 60 reports/hour so a log storm can't turn into an AI bill.

**Contain.** Scale to zero, roll back to last healthy, or restart — all through the same claw_… key you used to deploy. Every action is audit-logged and reversible.

## Why I built it

Getting attacked because you started learning is a tax on curiosity, and every hour of silence between the first probe and the first person who notices is an hour the attacker gets for free. Runtime security shouldn't be a paid feature that only teams with budgets and SOC analysts get. It should run quietly on the platform your code already runs on, within reach of anyone who can **git push**. If one person shipping their first real app on **BuildWithLocus** this month never has to read the log of their own compromise after the fact, that's the week worth building for.

**Challenges we ran into**

# Challenges I ran into

The hardest bug in this build was a BuildWithLocus deploy failure that kept insisting my Next.js dashboard was not ready, even though the container was starting cleanly.

Every deploy flipped to failed after exactly 5m20s with the error message ECS service did not become ready before timeout. The runtime logs showed Next.js 16.x booting and reporting Ready in 0ms. Curling the URL externally returned 200 — sometimes. Between successes I was getting 503s, and the logs showed tasks being replaced every 2–3 minutes, each printing a fresh Ready in 0ms on a different ip-x-x-x-x.ec2.internal host. Meanwhile my Hono agent (plain Node HTTP) in the same project deployed fine. Something was Next-specific.

The smoking gun was buried in the startup log:

```
- Local:         http://ip-10-0-0-94.ec2.internal:8080
- Network:       http://ip-10-0-0-94.ec2.internal:8080
```

Local and Network should both read 0.0.0.0. They did not. I had set ENV HOSTNAME=0.0.0.0 in my Dockerfile, but ECS Fargate overrides HOSTNAME at runtime with the ENI DNS name of the task — and that override beats any ENV directive baked into the image. The server.js inside Next standalone reads process.env.HOSTNAME and calls server.listen(port, hostname), so it was binding only to that specific IP. Anything on the loopback interface of the container (including the HEALTHCHECK) got ECONNREFUSED. Task unhealthy → ECS replaces → new task, same binding, same failure → loop forever, until the 5m20s patience window of the platform ran out and the deploy got marked failed.

The fix is one line, but it is only obvious after you understand the override order: set HOSTNAME=0.0.0.0 at the Locus service-variable layer (PATCH /v1/variables/service/:id), not in the Dockerfile. Locus-level env vars are injected into the ECS task definition after the runtime HOSTNAME resolution in Docker, so yours wins. After that, Next binds to 0.0.0.0, the HEALTHCHECK passes, ECS reaches steady state, the deploy goes green.

Hono, Express, the net/http package in Go — anything whose default listen(port) binds to 0.0.0.0 without consulting HOSTNAME — never hits this. It is Next-standalone-specific (and probably catches a few other self-hosted SSR frameworks that read HOSTNAME). Once I understood the override order I wrote it up as a note for other hackathon participants on BuildWithLocus so nobody else loses a day to it.

**Track: Using BuildWithLocus to leverage our suite.**

**ShieldWithLocus** is both a **BuildWithLocus** consumer and a **BuildWithLocus** watchdog. The entire detect-report-contain loop is built on primitives the platform already exposes, accessed through the same claw key used to ship the service itself. No second identity, no second agent, no bolt-on stack.

Detection rides the live SSE log stream (GET /v1/services/:id/logs?follow=true) — every log line flows through a 25-rule regex IOC engine on the agent the moment Locus emits it. Authentication is workspace JWT via POST /v1/auth/exchange, refreshed every 24 hours so monitoring never drops. Services are looked up per incident via GET /v1/services/:id.

**Containment is three reversible actions, each a single Locus API call:**

- Scale to zero via PATCH /v1/services/:id with runtime min:0 max:0 — traffic halts in under two seconds
- Rollback to last healthy via POST /v1/deployments/:id/rollback
- Restart in place via POST /v1/services/:id/restart
- Paranoid autonomy also disables auto-deploy via PATCH /v1/services/:id with autoDeploy:false, so an attacker with git write cannot redeploy their payload back into place

**Every action is authorized with the operator claw key, audit-logged with actor attribution (agent or user), and reversible without SSH or manual production surgery.**

The fit for this track is that ShieldWithLocus demonstrates the BuildWithLocus suite already contains everything a production-grade runtime security layer needs. The SSE log firehose, the reversible deploy API, the per-service variable surface, the addon system, the BYOD domain flow — all load-bearing, all used for their native purpose, none decorative. **The same platform that ships your code can also watch it, classify attacks against it, and contain them through the API you already know.**

Team **athena19** -- Samuel Mulia

`2026-04-22`

---

### CREDITDNA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/creditdna-86fc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/varsharanir07/CreditDNA) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://credit-dna.vercel.app/#landing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/c17dd63df63a4fdfa9bdd69ff4ae9036) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> CreditDNA- Credit for every Indian

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

CreditDNA is a modern web application that provides accessible credit scoring for Indians by leveraging their existing UPI transaction history. Rather than relying on traditional credit bureaus, CreditDNA analyzes UPI patterns to generate a credit score, making financial inclusion possible for millions.

**Challenges we ran into**

Feature Engineering Complexity:-

Converting raw transactions into meaningful behavioural signals was challenging Needed to design:
Transaction frequency , Merchant diversity ,Spending consistency.
We converted raw transactions into structured behavioural features using domain-driven metrics like frequency, diversity, and consistency, and validated them with simulated user scenarios.

Building Trust Without CIBIL:-
Banks rely heavily on traditional scores
Convincing them to trust alternative scoring is challenging.
We built trust by adding explainable AI, confidence scores, and positioning our model as a complementary system, allowing banks to test it gradually with real behavioural data

Team **BOTSQUAD** -- Simon Paul, [Mayank Bansal](https://github.com/mayankbansal4381ssgn6-dotcom), Varsha Rani, Devanandha Sajith

`2026-03-17`

---

### RoomMate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/roommate-89a1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sparshagarwal0411/roommate) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://roommate-lemon.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=qLGNigZR2bI) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Split expenses, Not friendships!

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

RoomMate **simplifies hostel expense management** by providing a single platform to budget, split shared bills, track payments, and view balances in real time. It **replaces manual calculations** and alert-based coordination with **automated splitting, clear payer assignments, and polite reminders**, reducing confusion and conflicts among roommates. Designed for students, it makes daily financial tasks **faster, transparent, and stress-free.**

**Challenges we ran into**

One major challenge was **maintaining accurate expense splits and balances** when multiple users get added or updation of expenses at the same time, which initially caused **inconsistencies in dues calculation**. I resolved this by **restructuring the Supabase database tables** and enforcing the server-side validations in the backend to ensure reliable calculations.

Another challenge was **integrating authentication smoothly** with the React frontend. This was addressed using **Supabase Auth** along with proper session and state management. Overcoming these challenges improved the **stability, reliability, and scalability** of the application.

Team **Broken Table** -- [Sparsh Agarwal](https://github.com/sparshagarwal0411), [Siya Yadav](https://github.com/skylover02), [Harsh Bhardwaj](https://github.com/Harshb7406), [Akash Niranjan](https://github.com/shenmok)

`2026-02-02`

---

### AntiDeepfake
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/antideepfake-e1ee) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rohit-ghosh-01/Noisify) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> "A tool for safe social media"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

In modern digital world, especially in social media, bots scrap public pictures and train face recognition models and then use them for creating deepfake images and harass people.
We tried to solve this issue by creating a three layer tool that injects noise into the image at pixel level that is invisible to human eye but it is enough to distract a AI model that is under training and forces it to learn wrong.
It also included a local facial recognition module that could check the final version and give the score as output for analysis.
If user wants, in exchange of quality, the image can be passed through face swap guard module that also adds another layer and the picture is safe when facing Face swapping models.

**Challenges we ran into**

'Fawkes' - the cloaking module we used, is under development and it performs well under low setting but as the cloaking level increases, the visual distortion increases, this decreases the image quality.
Local Face recognition model we used was good but there are many sophisticated models that can bypass the cloaking and still recognize the facial features.
And also the processing time it took was too high, especially in low end systems.
There is a need a do more research and testing to improve the project (tool).

Team **TechTokers** -- [Abhijit Dutta](https://github.com/abhiduttaa), [Samrat Saha](https://github.com/Samrat-ops-hue), [Rohit Ghosh](https://github.com/rohit-ghosh-01)

`2026-08-30`

---

### Cam
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cam-00ff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ombhojane/cam) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cam.omisaur.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ge2va08IeME) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> iPhone-level photos for budget Android phones

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![google cloud](https://img.shields.io/badge/google%20cloud-333333?style=flat-square) ![Sharp](https://img.shields.io/badge/Sharp-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square)

**What is the deployed URL for this project?**

https://cam.omisaur.app/

**What is the problem your project solves?**

more than 60% of india owns a budget smartphone

pics from these smartphones are dull, overexposed, blurryy & the glare is just cherry on the top: makes you regret buying the phone.

so people spend a lot of time to enhance it on gemini/ai enhnacer apps, one by one, adds on friction!

**How Did You Use Claude?**

i used Claude to review high-risk enhancements, especially photos with faces, text, glare, and small details.

it compares the original and enhanced photo and rejects the result if identity, text, objects, or scene geometry changed. during testing, it caught changes like altered hair, changed faces, missing rainbows, and invented skyline details.

i integrated it as an optional safety layer that rejects uncertain results instead of showing them. a smaller improvement is better than changing someone’s memory.

**How you are solving it?**

the idea is simple:
click a photo → the app instantly enhances it while preserving the original nuances.

it uses image regeneration method that removes anamolies, keeps the subject nuances and makes it better quality!

cam save hours to iterate editin in gemini & money in unused random ai enehnacer subscriptions (it's as low as 1000rs/week!)

cost: 2rs/image
letancy: 30secs

subscription model:
99/199rs per month based on usage
so most of the people could affoard it and it'll be the best lifestyle spend!

[Om Bhojane](https://github.com/ombhojane)

`2026-08-08`

---

### StockPot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stockpot-9d3c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0xSamrat/stockpot) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://getstockpot.shop/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Yn1AWKZG674) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI agents trade surplus food between restaurants

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square) ![Linq](https://img.shields.io/badge/Linq-333333?style=flat-square)

**Challenges we ran into**

# 1. "Challenges I ran into" 

**Square kept returning 403 FORBIDDEN, which looks exactly like a bad token.** I spent an evening rotating credentials. The token was fine — the `account_id` field actually wants Square's *location id*, and a wrong location gives the identical error to a wrong key. Two different mistakes, one message. Found it by curling the API directly instead of trusting my own client.

**My live market screen worked in curl and was blank in every browser.** The server sends *named* server-sent events, and a browser ignores those unless you subscribe to each name by hand. My test was two curl streams, which prints everything regardless of name — so it could never catch it. I found it by finally opening the page like a user would.

**Prava's own support told me a card mandate dies after one charge. They were wrong.** Instead of designing around it, I tested it live: one ₹1,400 approval took ₹1,120, then ₹200, and stayed usable. The catch is a `max_charges` field that silently defaults to 1 — almost certainly why their own team believed it didn't work. One approval now covers many trades.

**My test suite was sending real texts to a real phone.** Dozens, every time it ran. The messaging client is real whenever an API key is set, the test database is the dev database, and that database had a real phone in it. It hid because tests roll back — the records vanished, the messages stayed sent. I wasted an hour hunting a runaway loop in the market that never existed. Tests now physically cannot reach the network.

**A screen read "₹0.00 settled" while money was genuinely moving.** Three delivery events were defined in the code and published by nothing, so the live feed went silent at exactly the moment the product does its one job. The browser was also listening for three event names the server never used. Both halves had to be broken for it to hide that long. The total now comes from the ledger, not from whatever a browser tab happened to see.

**A phone could never be linked to a second kitchen.** The code asked "do I know this number?" *before* reading the message, so a phone belonged forever to whichever kitchen claimed it first. Later attempts weren't refused — just ignored, while the screen waited. I found it in the data, not the logs: a code issued, texted 16 seconds later, still unused, and no failed-attempt record either. Nothing accepted *and* nothing refused only happens if the code was never read.

**The problem it solves**

Restaurants throw away 4–10% of everything they buy. In India, food services
bin about 22 million tonnes a year. The maddening part: the café two streets
away is paying full price for the same ingredient, on the same day. Nobody
connects the two, because no owner has time to ring around every evening.

**Stockpot gives each kitchen an AI agent that does the ringing around.**

It reads your order management POS (Now only Square, Petpuja and others in future), then estimate the wastage from it'swaste management brain then works out what will spoil before you get through
it, and puts it up for auction to kitchens near you. When you are short of
something, it bids for it instead. You do not watch a screen — you get a text
when something needs your say-so.

### What it makes easier

- You stop guessing what is about to go off. It is worked out from what you
  have actually sold.
- You find a buyer without phoning anyone.
- Short of paneer at 6pm? Ask for it in plain English and nearby kitchens bid
  to supply you.
- Every decision your agent makes is written down, including the ones where it
  refused — so you can see *why* it did not buy.

### What it makes safer

This is the part that matters, because it is other people's money.

- **The money only moves after the food arrives.** The buyer reads a
  six-character code to the driver at the door. No code, no payment.
- **You pay for what actually turned up.** Ordered 15kg and only 12kg was
  usable? You are charged for 12.
- **Your spending limit is enforced by the card network, not by us.** You
  approve a ceiling once with your fingerprint, and Visa itself refuses
  anything above it. Even a bug in our code cannot overspend.
- **Anything over your limit asks you first**, by text. Reply YES or NO.
- **Kitchens too far away are kept out of your auctions entirely.** Somebody
  has to drive it.
- **We take 2.8%**, shown on its own line. Never hidden inside a rounded-down
  figure.

Every one of these rules is published in plain English on the site — including
the things we have not built yet.

---

**Best Visa Intelligent Commerce Implementation**

# "Best Visa Intelligent Commerce Implementation" 

**We never touch a card number.** Not stored, not logged, not held in memory. The card stays with Visa. What our app holds is a mandate — a credential that says "this agent may spend up to this much, on this trade" — and that is the only thing an agent ever gets near. That is the whole point of Intelligent Commerce, and it is why an owner can let software spend without handing software their card.

**The human consents once, with a fingerprint.** One passkey approval on their own phone sets a ceiling. No card typed into our site, no card on our server, nothing for us to leak.

**The ceiling exists before any bidding starts.** The mandate is created the moment a shortage is posted — not at checkout. So an agent can never bid into a limit that does not exist yet, and there is no window where it is negotiating without a cap already in force.

**The refusal comes from Visa, not from us.** When settlement is attempted above the cap, `THRESHOLD_EXCEEDED` comes back from the network. Our code is not the thing saying no. That matters: a bug of ours, or an agent that has been talked into something stupid, still physically cannot overspend. Every other safety rail in this product is ours and could be wrong. This one isn't.

**One credential, many trades, partial amounts.** Ordered 15kg, only 12kg usable — settle 12. One ₹1,400 approval took ₹1,120, then ₹200 later, and stayed live throughout. We had to prove that last part ourselves: Prava's support told us a mandate dies after one charge, and it doesn't — `max_charges` silently defaults to 1.

**And settlement is idempotent.** Charges are keyed on the listing and the delivery confirmation, enforced by a database constraint. Retry a timed-out call and it goes back with the same Prava key, so it's safe at their end too. Press the button twice and the second press moves nothing and says so.

The app also always reports which client actually ran — real network or recorded fixture. A demo that narrates a real payment while quietly faking one is the worst thing we could ship.

**Most Startup-Ready Product**

# Most Startup-Ready Product

**The business model isn't a slide. It's in the ledger.**

We take 2.8% of every trade, deducted at settlement and shown on its own line — never buried in a rounded-down figure. Seller payouts are built, with the can't-pay-twice rule enforced by a database constraint. A trade that completes today produces a real fee, a real payable, and a real transfer record. Nothing about the revenue model is waiting to be implemented.

**We have an answer to the cold-start problem, which is the thing that kills marketplaces.**

A two-sided market is worthless on day one because nobody is on it. Ours isn't. A kitchen connects its Square account and immediately sees a number it has never seen before: *"₹18,012 went in the bin over the last 45 days."* That's their own money, worked out from their own sales, with no other kitchen involved. Single-player value in a multiplayer product — and it's also the pitch. You don't sell a restaurant on a marketplace. You show them what they threw away last month.

**The network effect is local, which makes it winnable.**

Food has to be driven, so what matters isn't how many kitchens we have globally — it's how many are within a few kilometres of each other. That means we don't need scale, we need density in one neighbourhood at a time. Every kitchen that joins makes the market better for everyone already in its radius and worse for a competitor trying to start there. It's the city-by-city playbook, but with a smaller unit than a city.

**Readiness: it runs.** Live on a public domain, real Square sales in, real card rails out, 753 tests. A restaurant owner who has never seen it can sign up with their own Square account and get to a first trade unaided — we rebuilt onboarding until that was true.

**And the honest part: we have no paying customers yet.** Forty-eight hours old. What we have is a working product, a fee that already collects itself, and a first conversation that starts with a number the owner didn't know. What we'd need next is one neighbourhood — six to ten kitchens close enough to trade — and the willingness to knock on doors.

**OpenAI**

# OpenAI 

**Every trading decision in this product is made by a model, and no model can move money.** That line is the whole design.

When an auction opens, each kitchen's agent runs a `deliberate` step on gpt-4o-mini with tool-calling. It decides one thing: bid or don't, and at what price. What happens next — clearing the auction, verifying the delivery, charging the card — is ordinary deterministic code with no model call anywhere in it. A model that hallucinates costs us a bad bid. It cannot cost anyone a payment.

**Tool-calling means it checks instead of guessing.** The agent doesn't get handed a paragraph of context and asked to imagine. It calls for what it needs: how much of this do I have, how many days of cover, what does this normally cost, how far away is the seller. So "we'd be three days short" is a number it looked up, not a sentence it produced because it sounded plausible.

**Every decision is written down in the agent's own words — including the refusals.** That audit trail is a product feature, not debug logging. On the live market screen you watch kitchens turn trades down and say why: *"We can't sell 10kg when we only have 7.68kg in stock."* Most agent demos only show you the yes. The refusals are the more interesting half, because they're where you find out whether the thing is actually reasoning or just agreeing.

**And the model is never the last line of defence.** Above the owner's spending limit, a human is asked by text. Above the card's ceiling, Visa itself refuses. So the model is trusted with judgement and nothing else — which is, we think, the honest place to put an LLM in a system that spends real money.

Live in production, deciding real auctions, right now.

**iMessage Agent**

# Linq / iMessage Agent 

**iMessage isn't a notification channel here. It's the control surface.**

Kitchen owners don't sit at a dashboard — they're on a line at 7pm. So when an agent wants to spend more than its owner allowed, it doesn't queue a notification. It texts them: *"Your agent wants to buy 5kg of Paneer for ₹1,321. That's above your ₹1,000 limit, so it needs you."* They press and hold, tap 👍, and the trade goes through. They never open the app.

**We wrote for the medium, not just to it.**

- **Tapbacks where they exist, words where they don't.** iMessage gets "press and hold, tap 👍". RCS and SMS get "reply YES or NO" — because telling an Android owner to tap a reaction their phone can't send is telling them to do nothing. The wording narrows to the transport; what we *accept* stays wide: a tapback, a typed YES, or a 👍 sent as an ordinary message all work.
- **One question at a time.** This one cost us. A bare "YES" has no subject — if two approvals are outstanding, the owner cannot say which they meant, and we can only guess. So an agent now holds one open question per owner and the rest wait. We shipped the wrong version first and a real phone got the same question four times in one second.
- **A replayed tapback approves exactly once.** Linq retries for 25 minutes, so idempotency isn't optional.

**Consent is inbound-first.** We can only ever text a handle that has texted us. A phone is bound to a kitchen by a six-character code the owner reads off their own screen — so we know *which* kitchen, rather than guessing. A wrong code binds nothing, three wrong guesses lock it, and STOP works.

**And messaging can never break a trade.** Every send is wrapped: if Linq is down, rate-limited, or nobody has texted us, the auction still clears and the food still moves. The screen just misses a line.

Delivery codes, "sold", "on its way", and "paid" all arrive the same way — on the one app a restaurant owner already has open.

**Best Prava Adapter for the NANDA Town**

# Best Prava Adapter for NANDA Town

**We haven't packaged a NANDA Town adapter yet — but the payment layer this asks for already exists, and it's the part that's hard.**

Stockpot's Prava integration lives behind a typed `PravaClient` protocol with two implementations: the real HTTP client, and a recorded-fixture fake used by every test. Nothing in the business logic knows which one is running, and the API response always says which one did — a demo that narrates a real payment while quietly faking one is the worst thing we could ship.

**Quote, pay, verify, fail — all four are built.**

- **Quote.** A mandate is created when a shortage is posted, before any bidding. The ceiling exists before an agent can negotiate into it.
- **Pay.** Partial capture against that mandate: ordered 15kg, only 12kg usable, settle 12. One ₹1,400 approval took ₹1,120 then ₹200 and stayed live.
- **Verify.** Settlement is gated on physical delivery — a six-character code read aloud at the door — then reconciled against `get_payment_result`.
- **Fail.** Charges branch on `pending` / `succeeded` / `failed` rather than assuming success, because a call that times out *after* the row is written means the row exists and no money moved. Retries reuse the same Prava idempotency key, so they're safe at their end too. Uniqueness is enforced by a database constraint, not by our code remembering.

**The commerce simulation is already running.** Six autonomous kitchens negotiate continuously — quoting, bidding, refusing on their own reasoning, settling under per-agent budgets, and asking a human by text above a limit. Refusals are recorded in the agent's own words. That's the scenario layer this track asks teams to build "on top", and it's what the adapter was extracted from.

**What we found that a future builder would otherwise lose a day to:** `max_charges` silently defaults to 1, so a mandate appears to die after one charge — Prava's own support believed this. And the sandbox asks for an OTP "sent to your phone" that is never sent; it's a fixed value in the docs.

**What's left is packaging, not plumbing.** The protocol boundary was built so a NANDA Town adapter is a wrapper over an interface that already exists, rather than a rewrite. That's the next step, and we'd rather say so than claim a deliverable that isn't in your repo yet.

**Best Agentic User Experience**

# "Best Agentic User Experience"  

**The hard part of an agent isn't making it act. It's making a person comfortable letting it.** So every screen answers the three questions an owner actually has: what did it do, why, and how do I stop it.

**You can see why it said no.** Every decision an agent makes is written down in its own words — refusals included. "Selling would leave us three days short" is a real line from a real agent turning down a real trade. Most demos only show you the yes.

**You control it with one number.** Set a spending limit. Under it, trades happen on their own. Over it you get a text: reply YES or NO, or just tap 👍. The wording changes to match your phone, because telling an Android owner to tap a reaction their phone doesn't have is telling them to do nothing.

**It watches before it acts.** A new agent starts in shadow mode — it decides and records, and spends nothing. You read what it would have done, then hand it the keys when you're ready. Trust earned rather than asked for.

**Nothing is silently greyed out.** Every disabled button says what it's waiting for: "the driver has to type your code in first — that's what proves the food arrived." Setup is one step at a time, with the next thing always named.

**We publish our own rules in plain English**, on a page anyone can read — including a section for what we haven't built yet.

And the unglamorous parts, which are most of it: empty screens say what to do next instead of showing three zeros, errors are written for a cook rather than a developer ("this demo's keys have gone stale" beats "401 X-API-Key required"), and every screen works in light and dark, on a phone.

The test we held ourselves to: could someone who has never seen this finish a delivery without being told how?

**Agentic Commerce Hackathon**

# 2. "How your project fits into this track" 

**Prava isn't a checkout button bolted on the end. It's the safety mechanism the whole product rests on.**

Every kitchen's agent can spend money without asking. What stops that being reckless is a Prava mandate: the owner approves a ceiling once with a passkey, and the card network itself refuses anything above it. When our agent tries to settle over the cap, `THRESHOLD_EXCEEDED` comes back — and that isn't our code declining, it's Visa. A hijacked agent, or a bug of ours, physically cannot overspend.

**We used the hard parts, not the happy path.**

- **Partial capture.** Ordered 15kg, only 12kg usable — charged for 12. One ₹1,400 approval settled ₹1,120, then ₹200, and stayed live.
- **Idempotency.** Charges are keyed on the listing and the delivery confirmation, enforced by a database constraint rather than our code remembering. Press charge twice and the second press moves nothing and says so. A timed-out call retries with the *same* Prava key, so it's safe at their end too.
- **Delivery-gated settlement.** The charge only fires after the buyer reads a six-character code to the driver at the door.

**We found something Prava's own support had wrong.** They told us a mandate dies after one charge. We tested it against the live sandbox and proved otherwise — `max_charges` silently defaults to 1. One approval now covers many trades, which is the difference between a demo and something an owner would leave running.

**And we were honest about where Prava stops.** We needed to pay sellers out. Discord said Prava can't. Rather than trust that, we probed every plausible payout route against the live API alongside a nonsense control path — all 404, identically. A real answer instead of a rumour. So we built our own payout rail, with the can't-pay-twice rule enforced by a database column.

Throughout, the app reports **which** client actually ran — real or fixture. A demo that narrates a real payment while quietly faking one is the worst thing we could ship.

Team **Claude Dude** -- [Samrat Mukherjee](https://github.com/Samrat-Mukherjee)

`2026-08-03`

---

### SnapFit AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/snapfit-ai-149f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sandman-sh/snapfitAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://snapfit-ai-ten.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=Bt8PmDQDqXY) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI Fashion Discovery Meets Biometric Payments

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**Challenges we ran into**

### 🛠️ Challenges We Ran Into & How We Solved Them

#### 1. HTML5 Canvas CORS Taint & Virtual Try-On Freezes
* **The Hurdle**: When rendering try-on overlays, loading product photos directly into an HTML5 canvas threw browser CORS security errors (`SecurityError: Tainted canvas`), which caused `toDataURL()` to fail silently and stuck the UI on a loading spinner.
* **How We Solved It**: We built a pre-loader service (`loadImageAsDataURL`) that converts all clothing and model images into safe base64 data-URLs with cache-busting (`?_cors=1`) before performing background removal keying and compositing.

---

#### 2. Anatomical Alignment Across Different Clothing Types
* **The Hurdle**: Overlaying dresses, leather jackets, or sneakers using static pixel offsets resulted in floating clothes or mismatched body proportions.
* **How We Solved It**: We created category-aware anchor math (`dresses`, `outerwear`, `tops`, `footwear`) that dynamically detects garment types, calculates full-body model proportions, and positions transparent outfit cutouts accurately over shoulders, waist, or feet.

---

#### 3. Making the Conversational AI Execute Real App Actions
* **The Hurdle**: Standard chatbot assistants only return text answers and cannot interact with web page buttons or modals.
* **How We Solved It**: We configured our KIRO AI assistant (`gpt-5.6-sol`) to output structured `[ACTION]` intent payloads alongside text responses. The React controller reads these payloads and automatically opens Virtual Try-On sessions, triggers Prava 1-click checkouts, or filters categories based on natural chat prompts.

---

#### 4. Asynchronous Virtual Card Token Polling & Payment Telemetry
* **The Hurdle**: Handling the multi-step payment session flow (`POST /v1/sessions` $\rightarrow$ Passkey verification $\rightarrow$ Token generation $\rightarrow$ Outcome reporting) without blocking the user interface.
* **How We Solved It**: Built an asynchronous payment pipeline that initializes Prava session context, polls for 16-digit Visa network tokens and single-use CVVs, and immediately reports `APPROVED` transaction execution telemetry back to Prava's network.

**The problem it solves**

### 🚨 The Problem

Have you ever seen a cool outfit on Instagram, Pinterest, or on a friend, but had **no idea where to buy it**? 

Shopping for clothes online today is frustrating:
* You have to open 10 different tabs to search for matching clothes.
* You can't tell if an outfit will actually look good on you until it arrives in the mail.
* You have to type your secret credit card details into online stores you don't fully trust.

---

### ⚡ What People Use SnapFit AI For

1. **Snap & Match**: Upload any photo or take a picture of an outfit. Our AI isolates the clothes and finds the exact item + cheaper budget lookalikes in seconds.
2. **Virtual Try-On**: See how the clothes look on a full-body model or your selfie before spending a single rupee.
3. **AI Shopping Copilot (KIRO)**: Ask the AI assistant to *"try on the leather jacket"* or *"buy the floral dress"*, and it handles the shopping for you.
4. **1-Click Safe Payments**: Tap **Pay with Prava** and approve with your fingerprint or Face ID.

---

### 🔒 How It Makes Shopping Safer & Easier

* **Zero Card Risk**: Prava automatically creates a **single-use virtual card** for every purchase. Online stores never see your real credit card numbers.
* **No Bad Fits or Wasted Returns**: Virtual try-on lets you preview how clothing drapes on a full-body model before buying.
* **Fast 1-Click Checkout**: No filling out address forms or entering OTPs — just instant biometric passkey approval.
* **Budget Limits**: Set spending rules (e.g. *"Never spend more than ₹4,000 on jackets"*), and the AI automatically keeps you within budget.

**Best Agentic User Experience**

SnapFit AI delivers a top-tier agentic user experience by eliminating all traditional shopping friction.

Instead of searching through endless catalog pages or filling out long checkout forms, the user simply uploads a photo. The UI provides real-time feedback as the AI removes the person, isolates the dress, and displays the matched product.

From there, the user gets an interactive 3D virtual try-on studio and a seamless 1-tap biometric Prava Passkey checkout—no annoying window popups, redirects, or manual card entries. It feels effortless, fast, and modern from start to finish.

**Agentic Commerce Hackathon**

SnapFit AI fits the Agentic Commerce track by turning visual outfit inspiration into an instant 1-click buy.

When a user snaps or uploads a photo of anyone wearing a dress, our AI uses GPT 5.6 SOL and GPT-IMAGE-1 to strip away the person and background, generate a clean studio dress product shot, and match the exact item online.

Users can then immediately try on the dress in 3D and buy it on our site in one tap using Prava’s tokenized Passkey payments (Touch ID / Face ID) without typing any card details or leaving the app.

Rohit Yadav

`2026-08-02`

---

### Zoosh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zoosh-ai-7f54) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://zoosh-pay.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_L8mqOnT41E) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Your one stop payment settlement

![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square)

**Challenges we ran into**

First of all the math behind debt calculations. Just trying to explain my coding agent what my intention and thinking is behind the debt calculation is was head breaking. Then comes Prava. Love the app, love the seamless integration but there were many instances where my sandbox payments were failing and I couldn't figure out why I was getting 4xx error codes even when I wasn't doing anything wrong. Loved the founders of prava, they helped me fix it ASAP. 
Zoosh uses prava as the payment auth layer, Zoosh-pay as the compute layer and Cashfree(sandbox) as distribution layer for the money mandates. Just applying modularity cleanly in the zoosh ecosystem so that there is no clutter of backend routes was a very big task. To think of efficient backend rules while preserving the meaning of my app, phew that took some good chunk of time.
Also frontend. It broke so many times. There were times a simple fix I prompted my agent to do(I have good prompts alright) sometimes changed components of my project completely (hehe). But it was fun, designing simple websites so that user can navigate through the website is a fun task in prod development. 
NOW THE DB PART. Trust me, I changed my DB schema more than twice just because it wasn't consistent with my backend routes. Lord, that was one part I kind of hated doing but Codex helped me a lot here (thank you OpenAI for the 100usd creds). RLS policies, migrations etc etc...phew thank god that is done and dusted.
Oh and also choosing a good model for voice agent also was a challenge, I tried three models and then finalized on whisper-1 by openai. 
Zoosh also contains of a Linq as a sms service and a fallback mailing system as well. There were times where Linq bugged(which I thought), but it was me and my problem with apis. well you learn something new everyday and im still new to this stuff so yay.
Thankfully everything sat well properly without any friction. I will like to give a good shout out to 5.6 Luna (my dear model). She spent a lot of brainstorming sessions discussing tradeoffs for designs and routes. Loved the build experience, learned a lot and mostly I enjoyed this. I solved a problem that I deemed fit to solve rather than asking AI to give me 'problems for hackathons'. So loved making Zoosh. I will still work on Zoosh after the hackathon cuz I think it solves a problem and I can make a startup on this. 
So thank you if you read till here, and enjoy Zoosh :)

**The problem it solves**

Imagine this, you are out with your friends, constantly paying for each other, not keeping track of your payments. At the end of the day, you are tire and you don't wanna pay up right away. Those delays turn from hours to days to weeks! And these delays become a grudge between friends. 
Now what if you have Zoosh? A platform where you have your own zoosh agent using which you can log your payments throughout the day. And at the end of the day, you press 'Settle Up' and you just get one payment request rather than many small ones. Just one payment and your debt gets redistributed among all your other friends. One button, All debt settled. No hassle. All safe, and your information never stays with us. That is what Zoosh is. Removing your headache of payments and keeping your friendships intact while you enjoy :)

**Best Visa Intelligent Commerce Implementation**

Nowadays who doesnt own a Visa card? Prava helps Zoosh to create and authenticate a single payment mandate to clear multiple dues in a group. Zoosh agent takes your words and converts them to money, what you spent, what others spent - keep track of it without losing a paisa.

**Most Startup-Ready Product**

I strongly believe that we can fund my project into creating a big product, something that will have a high churn rate on customers, not just because its good, because it is required - required by friends, small businesses and what not. An agent easing out the pain of calculating everything for you to split money. Prava to create a single mandate to pay once and then split it among the creditors. Zoosh eases life for you!

**OpenAI**

I have implemented Whisper-1 and used codex throughout the build journey to perfect Zoosh to the core. OpenAI has enabled me to solve a very evident existing problem of splitting money in a group of friends in a fun, interactive manner that not just friends, but people with different uses can use Zoosh too!

**iMessage Agent**

Linq allows Zoosh to be powerful and interactive to the core user level. Zoosh-v2 will include a message agent using Linq which will directly use Zoosh from iMessages without ever interacting with any other app. Think about it - an app you use everyday used to integrate with a app you need everyday!

**Best Agentic User Experience**

My Zoosh agent can easily understand communication in English and parse it to normal English and splitting math!
It parses to Linq, prava and my ledger math easily without any hassle. the smooth integration of Zoosh agent allows it to become something that no other group payments apps have nowadays!

**Agentic Commerce Hackathon**

I have solved a problem that I have faced in my friend group. And I believe using a voice agent to handle and parse everyday group expenses, easy to use and very accurate!
Using Zoosh we can remove the sour conversations of asking our friends to return our money back or forgetting about it, zoosh reminds them of what they owe. One payment, and every due to every friend in the group is settled!
Its that easy.

[Umang Sharma](https://github.com/zolo-z1west)

`2026-08-02`

---

### Accord
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/accord-82dc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KaranSinghBisht/accord) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://accord-prava.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tODFGd_jDtc) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> The intent firewall for AI agent payments

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Drizzle](https://img.shields.io/badge/Drizzle-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square) ![Visa Intelligent Commerce](https://img.shields.io/badge/Visa%20Intelligent%20Commerce-333333?style=flat-square)

**Challenges we ran into**

* Prava's sandbox went down a few times mid-build, so I made the core guarantee independently provable. A blocked cart never requests a charge, and the public `/replay` page recomputes every rule verdict live with no login required.

* My biggest bug was in the quote hash that binds a decision to what was judged. I initially hashed only the price and product ID. I then realized that the rules and the LLM judge also read the item's category and description. This meant a merchant could change the label the decision was based on while the hash still verified. I now bind every field the decision touches, with escaping to prevent a value from forging the layout.

* Another silent issue was that the default OpenAI model rejects `temperature: 0`. This caused the judge to fail closed and escalate every cart. I fixed it by sending the temperature parameter only to models that support it. Once Prava's sandbox recovered, I also captured Prava's own over-cap refusal as supporting evidence.

**The problem it solves**

An AI shopping agent can pass every check, including verified identity, an approved merchant, and a valid spending limit, and still buy the wrong thing. A hidden instruction on a product page can quietly add an item to its cart, and identity checks or spend limits cannot detect that.

Accord compares the agent's real cart against your plain-English mandate and only mints a one-time Visa card through Prava when they match. When they do not match, no card is created, so there is nothing to misuse.

Accord is the layer between an agent being allowed to pay and ensuring that it pays for the right thing.

**Best Visa Intelligent Commerce Implementation**

Accord adds the layer above Visa Intelligent Commerce's agent identity and spend controls: line-item intent enforcement at the moment of credential issuance. Permissions are a passkey-authorized Prava mandate scoped to amount, merchant, category and quantity — the agent holds no card and no key. Every decision is bound to a hash of the exact quote it judged, and a blocked cart never triggers a charge, so no credential ever exists to misuse. When a cart matches, a real one-time Visa credential is minted via Prava, capped to the exact total, and the settled charges are verifiable against Prava's own mandate record. Transaction completion, permissions, trust and controls — all enforced on Visa rails.

**OpenAI**

Accord's second enforcement layer is an OpenAI model acting as a semantic intent judge. It compares the agent's real cart against the mandate's plain-language intent and catches what deterministic rules can't — a same-price substitution, or an item added by a prompt injection — while treating all cart text as data, never instructions. Run at temperature 0 with strict JSON output, it can only lower trust, never override the rules, so even a fully compromised judge can't approve a purchase on its own.

**Best Agentic User Experience**

Accord makes an invisible security decision legible. You write a mandate in plain English; every agent run streams into a live console; a blocked attack becomes a human-readable incident report showing the exact cart, the mandate, and the hidden text the agent was tricked by; ambiguous calls escalate to a one-tap human inbox; and a kill switch pauses the mandate at Prava. A person can see, in seconds, why a purchase was allowed or refused.

**Agentic Commerce Hackathon**

Accord is the safety layer for agentic commerce — what lets an autonomous agent be trusted with money. The agent shops and proposes a cart; Accord checks it against the human's plain-English mandate and only then mints a one-time payment credential via Prava. It turns "an agent that can spend" into "an agent you can safely let spend."

[Karan Bisht](https://github.com/KaranSinghBisht)

`2026-08-02`

---

### PromptAi.credit
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/promptaicredit-9c30) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Vib-UX/promptai/tree/integration/prava) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://pravamcp.promptai.credit) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/pu5YfgtCr-4) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> frontier models. zero bill. approve once, ship.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Browserify](https://img.shields.io/badge/Browserify-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSX](https://img.shields.io/badge/JSX-333333?style=flat-square) ![Playwright](https://img.shields.io/badge/Playwright-333333?style=flat-square)

**Challenges we ran into**

> passkey broke in the ide browser → use chrome/safari; rotate PRAVA_USER_ID on fido 409
> namecheap card field is a stripe iframe → couldn’t type in; used their paymentmethod + stripeResponseHandler
> sandbox charge declined (expected) → report DECLINED, register on sandbox balance
> porkbun was a dead end → switched to namecheap sandbox; ip whitelist kept rotating

**The problem it solves**

> agents build the app, then stall at human checkout
> gooogle maps billing, domain reg, email/cloud credits all need a card mid-prompt
> you approve once (passkey) → prava one-time visa → agent pays and keeps shipping
> real card never hits the model; merchant + amount are locked
> use it whenever a vibecode task needs a production url or a funded api to finish

**Best Visa Intelligent Commerce Implementation**

prava issues a one-time visa network token (not the real pan) for each buy
passkey approve → merchant + amount locked at the network
agent drives checkout with that credential (namecheap / maps / paid apis)
report approve/decline so the token is closed, no dangling card

**Agentic Commerce Hackathon**

agent hits a real checkout mid-task (domain, maps billing, paid apis)
prava one-time visa + passkey → agent pays without seeing the real card
merchant + amount scoped; report approve/decline; keep shipping

[Vibhav Sharma](https://github.com/Vib-UX)

`2026-08-03`

---

### Snag
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/snag-f1ce) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/swpnldubey/snag) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://use-snag.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BXU8cxecwtU) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Pay supplier invoices only when they match.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**Challenges we ran into**

The main challenge was completing the Prava Sandbox flow end to end. I audited the request payload for a real email domain, a valid bare HTTPS merchant origin, and a persistent browser profile for passkey checkout.

A sandbox test card later failed after identity verification. With the Prava team, I isolated it to the card, used a fresh test card, and completed the public deployed flow successfully.

I learned that for agentic payments, an LLM should explain evidence, but deterministic policy should control whether money can move. User approval and payment scope are necessary trust boundaries.

**The problem it solves**

Growing physical-goods and DTC brands often pay supplier invoices by manually comparing what they ordered, what arrived, and what the supplier billed. That slows down lean ops teams and can lead to overpayment, duplicate payment, or paying for goods that were not received.

Snag performs a three-way match between a purchase order, delivery note, and supplier invoice. OpenAI explains the document evidence, while deterministic controls decide PAY or HOLD. When everything matches, Snag unlocks one user-approved, amount- and merchant-scoped Prava Sandbox payment session.

Built as a deployed Next.js and React app with Next.js API routes on Vercel. OpenAI handles evidence explanation; Prava Sandbox handles hosted passkey approval and the constrained supplier payment flow.

Next: connect live purchasing, warehouse, and accounting systems; add duplicate-invoice checks, tolerance rules, vendor policies, and exception review for HOLD invoices.

**Best Visa Intelligent Commerce Implementation**

Snag uses Prava Sandbox to turn a matched supplier invoice into a user-approved, amount- and merchant-scoped payment session. The implementation shows how agentic commerce can stay useful and safe: the agent checks invoice evidence, but payment only moves after clear policy checks and human approval.

**OpenAI**

Snag uses OpenAI to explain the evidence across a purchase order, delivery note, and supplier invoice in plain language. The model helps the user understand why an invoice should be paid or held, while deterministic matching logic controls the actual PAY/HOLD decision.

**Best Agentic User Experience**

Snag keeps the workflow simple: show the invoice evidence, return PAY or HOLD, and require the user to approve a tightly scoped Prava Sandbox payment session.

**Agentic Commerce Hackathon**

Snag uses an agent to explain purchase order, delivery note, and invoice evidence, then lets deterministic policy decide whether a scoped Prava Sandbox payment session can be approved.

[Swapnil Dubey](https://github.com/swpnldubey)

`2026-08-03`

---

### Dhandha.com
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dhandhacom-62c2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/LAKSHYA2517/dhandha.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=kM7t9vrz7QY) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Compliance First. Business Always.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Google Colab](https://img.shields.io/badge/Google%20Colab-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Every successful business partnership starts with one thing: trust. But before two companies can work together, they need to verify whether the other business is genuine, compliant and meets all the required regulatory standards.
Today, this process is still largely manual. Companies exchange licenses, certificates, tax registrations, and other compliance documents through emails or WhatsApp. Someone from the compliance or procurement team has to review every document, check its validity, verify expiry dates and decide whether the company is trustworthy enough to do business with.
Now imagine doing this for hundreds of suppliers or buyers across different countries, where documents are written in different languages and regulations vary from region to region. The process quickly becomes slow, expensive and difficult to manage, especially for small and medium-sized businesses.
More importantly, there is no simple way to compare companies based on their compliance readiness. Businesses often ask questions like:
Which supplier is the safest to work with?
Which company has stronger regulatory compliance?
Which business partner is the best choice for international trade?

We believed there should be a smarter and more standardized way to answer these questions.
That's why we built the Compliance-Based B2B Matching Engine, a platform that simplifies compliance verification, supports multilingual document understanding and helps businesses discover trustworthy trading partners through an explainable compliance score.

**Challenges we ran into**

Supporting businesses that communicate in different languages.
Designing a simple user experience for complex compliance workflows.
Standardizing compliance evaluation across different industries and regions.
Ensuring that AI assists users without making compliance decisions independently.
Maintaining transparency and explainability in every recommendation.
Creating a modular architecture that can scale with future enterprise requirements.
Balancing automation with rule-based validation to improve reliability and trust.
Building a practical, enterprise-ready compliance platform introduced several hurdles:

Balancing AI with Strict Rules: We had to ensure that AI only assisted the user and extracted data, while the actual compliance decisions remained strictly rule-based. Preventing AI hallucinations in regulatory evaluation was a top priority.

Multilingual Complexity: Processing compliance documents and maintaining accurate conversational intent across different languages required careful fine-tuning of the interaction layer.

Standardizing the Scoring: Creating a universal Regulatory Compatibility Index (RCI) that could fairly evaluate businesses across different industries, regions, and regulatory frameworks was logically complex.

UX for Compliance: Designing a simple, frictionless user experience for an inherently complex and tedious enterprise workflow took multiple iterations to get right.

**Runner Up**

Track 2: Gemma Financial Compliance & Risk Triage

Develop an intelligent compliance assistant that analyzes transactions, onboarding documents, and financial records to detect anomalies, assess risk, summarize findings, and generate compliance-ready reports for review teams.

Team **Commitment Issues** -- Lakshya Asnani, Ansh Mehta, Rohan Chaudhary, Dev Patel

`2026-07-19`

---

### SpendBoat
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spendboat-d783) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anubhavsingh9905/SpendBoat) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://spend-boat.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/HcK1-M4W8lk) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI-powered expense tracking made effortless.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Managing daily expenses manually is often time-consuming and inconvenient. Most expense tracking applications require users to fill multiple fields such as amount, category, note, and date every time they spend money. Because of this friction, many people stop tracking their expenses consistently.

This project simplifies expense management by allowing users to add expenses using natural language input, similar to chatting with a bot. Users can write messages like:

```text
"Spent ₹200 on dinner yesterday"
"Netflix subscription ₹499"
"Groceries 1200 today"
```

The system automatically:

* Detects the expense category using a Machine Learning model
* Extracts amount and date from the message
* Stores the expense in a structured format

This makes expense tracking:

* ⚡ Faster
* 🧠 More intuitive
* 📱 Easier for non-technical users
* 📊 More consistent over time

The application also provides:

* Monthly spending analytics
* Category-wise insights
* Daily average spending
* Visual charts and reports

Users can better understand their spending habits, control unnecessary expenses, and manage budgets more effectively without manually organizing data.

In future versions, the project can also support:

* WhatsApp-based expense logging
* Budget alerts
* AI-generated financial insights
* Voice-based expense entry

This makes the solution useful for:

* Students managing monthly budgets
* Working professionals tracking daily expenses
* Anyone looking for a simple and intelligent finance tracking system

**Challenges we ran into**

## Challenges I Ran Into

### 1. Parsing Natural Language Expenses

One of the biggest challenges was converting unstructured text like:

```text id="e1a10r"
"Spent ₹250 on pizza yesterday"
```

into structured expense data.

Initially, simple keyword matching produced inaccurate categories and failed for different sentence formats. To solve this, I integrated a Machine Learning model that predicts categories from user messages. I also used the `chrono-node` library to extract human-readable dates like “yesterday” or “last Monday”.

This significantly improved flexibility and user experience.

---

### 2. Handling Monthly Analytics Efficiently

The dashboard included:

* monthly spending
* top category
* daily average
* pie charts
* bar graphs

At first, I was fetching all expenses from the database and calculating everything on the frontend. As the dataset grew, this became inefficient.

To fix this:

* I filtered expenses by `month` and `year` directly from the backend
* Added indexed date queries in MongoDB
* Created monthly summary logic to reduce unnecessary calculations

This also allowed charts and analytics to automatically “reset” for each new month without deleting previous data.

---

### 3. Authentication & Auto Logout Issue

During development, users were getting logged out immediately after login whenever navigation happened programmatically using React Router’s `navigate()`.

The issue was caused by:

* authentication state updating asynchronously
* protected routes rendering before user data finished loading

I solved it by:

* introducing a proper `isLoading` state
* delaying protected route rendering until authentication finished
* restructuring the auth flow inside `AuthContext`

This made login and protected routing stable.

---

### 4. Deploying the ML API on Vercel

While integrating the ML model API, requests from the backend kept failing with:

```text id="7r7fbu"
401 Unauthorized
```

even though the API worked correctly in Hoppscotch.

After debugging request logs, I discovered that Vercel Deployment Protection was enabled, meaning external server requests were blocked unless authenticated through Vercel.

I fixed this by:

* disabling deployment protection for the API deployment
* redeploying the service publicly

After that, backend-to-ML communication worked correctly.

---

### 5. Keeping the Project Fully Deployable

The project contains:

* frontend
* backend
* ML model service

Managing environment variables, deployment URLs, authentication headers, and API communication across multiple services was challenging.

I solved this by:

* separating internal and external API calls
* properly managing `.env` variables
* using modular backend architecture
* deploying services independently while maintaining communication between them

This improved maintainability and scalability of the project.

[Anubhav Singh](https://github.com/Anubhavsingh9905)

`2026-05-13`

---

### Abitron
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/abitron-73d8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Snowhq/arbitron-agents) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://p-e4e6c6d9bc-8cc5de7e2a.preview.locusfounder.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Dml4UU795rY) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Product arbitrage is profitable but time-intensive. Finding trending products requires hours of manual research across Reddit, TikTok, and Google Trends. Calculating margins means checking multiple suppliers, estimating shipping, factoring in ad spend, and running profitability calculations for each product. Most people give up because the manual work doesn't scale.

Arbitron automates the entire operation. Six AI agents coordinate to:

- Scan thousands of social posts hourly for viral products
- Calculate real profit margins (supplier cost + shipping + 30% ad spend)
- Filter to only 50%+ margin products
- Generate product listings automatically
- Track revenue and P&L without human intervention

What takes a person 20+ hours per week now runs autonomously 24/7. The business operates itself - agents find opportunities, validate profitability, and would execute the entire sales cycle with zero manual work.

Built for regions where traditional e-commerce tools aren't available, using open APIs and deployable infrastructure that works anywhere.

**Challenges we ran into**

Challenges I Ran Into

The biggest technical hurdle was Reddit's rate limiting. When deployed to Render, the agents would scan successfully once, then get hit with HTTP 429 errors for hours. Reddit blocks requests from certain cloud provider IPs to prevent scraping. 

Solution: Added a manual trigger endpoint and built the product persistence layer to cache results across scans. If a scan gets rate-limited and returns empty, the dashboard still shows products from the last successful scan. This turned the rate limiting from a blocker into just a temporary delay.

Second major issue: product data kept disappearing. The agents would find 5 profitable products, but the next scan would wipe them out. Root cause was in server.js - the code was replacing the entire products array on every scan instead of only updating when new products were found. One line fix (wrapping the update in an if-statement checking for non-empty results) solved it.

Third challenge: LocusFounder deployment infrastructure kept failing with ECR Docker errors. After multiple failed deploys, I had to build the dashboard in the dev environment and rely on the preview system instead of traditional deployment. This actually worked fine - the preview URL is stable and accessible.

Final challenge: Stripe Connect isn't available in Nigeria, so I couldn't implement real payment processing. Per hackathon Discord confirmation, I built a clearly-labeled demo checkout flow that shows exactly how revenue would flow through the system in supported regions. The mock orders update revenue/profit metrics so judges can see the full business cycle.

**Using LocusFounder to Build a Business!**

Arbitron is a business built entirely with Locus Founder where the AI agents ARE the business. 

This isn't a tool that helps humans run a business - the agents operate the entire product arbitrage business autonomously. Six Locus Founder agents coordinate to find trending products on Reddit, calculate profit margins, source suppliers, generate listings, create marketing materials, process orders, and track P&L - all without human intervention.

The business model is real: identify viral products with 50%+ margins, list them at 4x cost, and profit from the spread. In supported regions, this would generate actual revenue through Locus Checkout with funds flowing directly to the business wallet.

Built the complete operational stack with LocusFounder:
- Dashboard for monitoring all 6 agents in real-time
- Product catalog with live profit calculations  
- Demo checkout flow (Stripe unavailable in Nigeria)
- Activity tracking across all business functions
- Revenue and P&L reporting

The agents run 24/7 on deployed infrastructure, scanning Reddit hourly and updating the catalog automatically. A human business owner could check in once a week and see revenue, or never check in at all - the agents handle everything.

This demonstrates Locus Founder's core capability: building businesses that operate themselves, not just building tools for existing businesses.

SNOW HQ

`2026-05-25`

---

### AgentOps
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentops-9ee2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CosmasMandikonza/AgentOps) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agent-ops-saferta.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=qusBw4z3vGE) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Operator layer for autonomous revenue

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Django rest framework](https://img.shields.io/badge/Django%20rest%20framework-333333?style=flat-square) ![Firecrawl](https://img.shields.io/badge/Firecrawl-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square)

**The problem it solves**

# AgentOps

**Operator software for autonomous revenue services.**

AI services are getting better at doing work, but the business layer around them is still broken.

A model can generate output.  
An agent can execute a task.  
But operators still struggle to answer the questions that actually matter:

- **Did this service get paid?**
- **What did it spend to fulfill the work?**
- **What proof exists that the work actually happened?**
- **Is the service profitable after fulfillment costs?**

## What AgentOps does

AgentOps solves that gap.

It is an **operator layer for autonomous revenue services**: a control surface where founders, agencies, and platform teams can supervise AI-powered services as if they were real business units, not black-box workflows.

Instead of hiding behind prompts and outputs, AgentOps makes the operating reality visible:

- **wallet status**
- **checkout**
- **fulfillment proof**
- **margin / profit visibility**

all in one place.

## Real use case

A practical use case is a service business selling repeatable digital work such as:

- landing page audits
- competitor intelligence
- ad copy packs
- other AI-assisted digital services

With AgentOps, that service can:

1. expose a real checkout flow  
2. route fulfillment through live wrapped APIs  
3. attach proof artifacts back to the job  
4. keep revenue, costs, and margin visible to the operator  

That means the service is no longer just *“AI that can do something.”*  
It becomes a system that can **take payment, perform work, prove what happened, and show whether the business is healthy.**

## Why this matters

Today, teams often stitch together payments, screenshots, research calls, and fulfillment logs across multiple disconnected tools.

AgentOps replaces that fragmentation with a single operator surface.

It makes autonomous services:

- **easier to supervise**
- **safer to run**
- **more transparent**
- **more believable as real businesses**

## Core idea

> **AI can do the work. AgentOps makes it operable.**

**Challenges we ran into**

# Challenges I ran into

The hardest part of building AgentOps was not UI polish or prompt engineering.

It was making the **live proof loop** real and trustworthy.

## 1. Working against beta infrastructure

A major challenge was integrating against beta APIs while still trying to ship something that felt product-grade.

Some endpoints behaved differently than expected.  
Some response shapes required careful handling.  
One screenshot provider path turned out not to be registered in beta at all.

I had to:

- verify what was actually live
- adapt the implementation to the providers that were truly available
- avoid pretending a capability existed when it did not

That forced me to build the product around **truthful proof**, not fake confidence.

## 2. Demo mode vs live mode

Another challenge was building a runtime that could switch cleanly between **demo** and **live** behavior.

I had to make the mode initialization deterministic, ensure proof routes failed gracefully when demo mode was active, and keep the UI explicit about what was:

- **LIVE**
- **SIMULATED**
- **unavailable**

That honesty layer became one of the strongest parts of the project because it made the system believable instead of theatrical.

## 3. Repository and runtime recovery

Near the end of the build, I hit a serious repository/runtime recovery issue during git repair.  
Part of the root project scaffold was lost, which temporarily broke the runtime.

I rebuilt the missing root files, restored the required support files, verified that:

- `npm install`
- `npm run lint`
- `npm run build`

all passed again, and then re-ran the live smoke tests until:

- wallet proof worked
- checkout proof worked
- search proof worked
- screenshot proof worked

## Biggest lesson

The winning version of this project was **not** the one with the most features.

It was the one where the **money-and-proof loop was undeniable**.

That is why the final version focuses on:

- real wallet visibility
- real checkout creation
- real wrapped search proof
- real screenshot proof
- clear live vs simulated operational truth

**Using PayWithLocus.com to leverage our suite.**

# Why AgentOps fits the PayWithLocus track

AgentOps is built around **PayWithLocus as a core product primitive**, not as a bolt-on payment button.

## How we use the Locus suite

- **Live operator wallet visibility**  
  AgentOps connects to a real Locus wallet on Base and surfaces the wallet state, network, and balance directly inside the product.

- **Live checkout creation**  
  The platform creates real hosted checkout sessions through Locus so each autonomous service can actually take payment.

- **Wrapped API fulfillment**  
  AgentOps uses Locus-wrapped providers to run fulfillment steps, including:
  - live **Exa** search proof
  - live **Firecrawl** screenshot proof

- **Operational proof inside the product**  
  Instead of hiding payment and fulfillment behind backend logs, AgentOps exposes the artifacts in the UI so an operator can inspect what happened.

- **Mode-aware control surface**  
  The product supports clear **LIVE vs DEMO** behavior, making it explicit when Locus-backed actions are real and when data is simulated.

## Why this matters

Most agent demos show output.  
AgentOps shows the **business loop** around the output:

1. the service has a wallet  
2. the service can get paid  
3. the service can spend on fulfillment  
4. the service can attach proof  
5. the operator can see margin and control from one surface  

That makes PayWithLocus fundamental to the experience.

## In one sentence

**AgentOps uses PayWithLocus to turn autonomous services into operable businesses with real wallet visibility, live checkout, live wrapped fulfillment, and inspectable proof.**

Cosmas Mandikonza

`2026-04-16`

---

### Taxmate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/taxmate-ab9a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CodeLander07/codelanders) [![Built at](https://img.shields.io/badge/Built%20at-GHRhack%202.0-0052CC?style=flat-square)](https://ghrhack2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Simplify Your Taxes with Intelligence

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Managing personal taxes is confusing, error-prone, and stressful for most people.

Users struggle with:

Scattered financial documents (bank statements, salary slips, investments, rent receipts)

Lack of clarity on what data is actually required

Manual tax calculations that are easy to get wrong

Difficulty understanding Old vs New tax regime

Missing deductions due to poor awareness

Blind trust in tools that show numbers without explaining where they came from

Most existing platforms:

Show pre-filled numbers without transparency

Require users to manually enter complex financial data

Provide generic advice not based on real documents

Fail to adapt cleanly when tax policies change

This creates low trust, low confidence, and high risk for users.

🚀 What People Can Use It For
1️⃣ Document-First Tax Analysis

Users upload their real financial documents:

Bank statements

Salary slips

Rent receipts

Investment proofs

EMI details

Capital gains statements

The system:

Extracts data automatically using OCR

Converts it into structured, verifiable financial data

Ensures no insights appear until documents exist

👉 This eliminates guesswork and fake data.

2️⃣ Safer & More Accurate Tax Insights

Instead of manual entry:

Calculations are done deterministically (rule-based, policy-controlled)

AI is used only for reasoning and explanation, not math

Every insight is tied back to uploaded documents

👉 Users know why a number exists, not just what the number is.

3️⃣ Clear Old vs New Regime Decisions

The platform:

Compares tax regimes based on actual user data

Explains why one regime is better

Updates automatically when tax policies change (admin-controlled)

👉 No blind recommendations, only explainable decisions.

4️⃣ Zero-Data = Zero Insights (Trust by Design)

If a user hasn’t uploaded documents:

No dashboard data is shown

No AI insights are generated

All sections remain locked

👉 This prevents misinformation and builds long-term trust.

5️⃣ Policy-Resilient & Future-Proof

When tax rules change:

Admin updates the policy once

Calculations and AI reasoning automatically use the new policy

Old results remain preserved for audit and comparison

👉 Users never lose historical accuracy.

🔐 How It Makes Existing Tasks Easier & Safer
Task	Traditional Tools	This Platform
Data entry	Manual & error-prone	Automatic via documents
Trust in numbers	Low	High (document-backed)
Tax calculations	Hidden logic	Transparent & policy-bound
AI advice	Generic	Personalized & explainable
Policy updates	Risky & silent	Controlled & auditable
Compliance	Confusing	Guided & structured
🧠 In Simple Terms

Upload documents → System extracts facts → Rules calculate → AI explains → User understands.

No documents = no data
No data = no insights
No insights = no false confidence

🎯 Who It’s For

Salaried professionals

Freelancers & consultants

Investors

First-time taxpayers

Anyone who wants clarity, trust, and control over their taxes

**Challenges we ran into**

Building a document-first, AI-assisted tax platform came with several non-trivial challenges—both technical and conceptual. Below are the key hurdles I faced and how I addressed them.

1️⃣ Documents Uploading Successfully, but Nothing Happening After

The problem:
Files were uploading correctly (API returning 200 OK), but users saw no data, insights, or dashboard updates. The system treated upload as a “finished” action.

Why this was hard:
Uploading a file doesn’t mean the data is usable. OCR, parsing, validation, and analysis are separate steps—and none were automatically triggered.

How I fixed it:
I redesigned the flow so that upload became a trigger, not an endpoint.
After upload, the system now automatically runs:

OCR and document parsing

Structured financial data generation

Deterministic calculations

AI (Ollama) reasoning

The dashboard only unlocks after this pipeline completes, ensuring users never see incomplete or misleading data.

2️⃣ Inconsistent Data Appearing Before Any Documents Were Uploaded

The problem:
Some dashboard sections showed default or placeholder values even when users hadn’t uploaded any documents.

Why this was dangerous:
Showing numbers without data breaks trust—especially in financial applications.

How I fixed it:
I implemented a document-first access control rule:

No documents → no data

No data → no insights

All sections remain locked until at least one document is parsed

This ensured that every number and insight shown is backed by real user data.

3️⃣ Preventing AI from Hallucinating Financial Information

The problem:
Using AI directly for financial analysis risks hallucinated values, incorrect assumptions, or policy misunderstandings.

Why this mattered:
Tax systems must be deterministic and auditable—AI can explain, but it must not calculate or invent.

How I fixed it:
I strictly separated responsibilities:

Backend code handles all calculations using tax rules

AI (Ollama) is used only for reasoning, classification, and explanation

I enforced JSON-only AI outputs and blocked AI execution unless structured data and an active policy were present.

4️⃣ Handling Tax Policy Changes Without Breaking Existing Data

The problem:
Tax rules change every year, and hardcoding them would cause old data to become incorrect or overwritten.

How I solved it:
I introduced policy versioning, managed via an Admin Panel:

Each financial year has its own policy version

Only one policy can be active at a time

Old calculations remain tied to old policies

Users must explicitly recalculate when policies change

This made the system future-proof and audit-safe.

5️⃣ Making the System Feel Responsive Despite Heavy Processing

The problem:
OCR and AI analysis can take time, which risks poor user experience.

How I handled it:
I designed the UI to:

Show clear processing states (uploading → parsing → analyzing)

Keep the dashboard locked until completion

Avoid showing partial or speculative results

This trade-off favored clarity and trust over speed, which is critical in finance.

Team **Codelanders** -- [Mayur Nikumbh](https://github.com/unstopablesid), Tejas Patil, [Shreyas Ghadigaonkar](https://github.com/Shreyas1904)

`2026-03-01`

---

### Broke No More
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/expense-hub-e9db) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chhavimittal09/hostel-expense-tracker) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://chhavimittal09.github.io/hostel-expense-tracker/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/zzN6kjjBTv0?si=7nq3GdiTTpbx2-vc) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Hostel Expense Manager

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

What Can People Use It For?

- Managing shared hostel expenses such as food, groceries, utilities, and outings without manual tracking.
- Splitting costs fairly and automatically among roommates, removing the need for calculations or reminders.
- Tracking monthly budgets and understanding where money is being spent at a glance.
- Settling dues transparently, clearly showing who owes whom and how much.
- Sending polite, system-driven reminders instead of uncomfortable personal follow-ups.
- Keeping a shared financial record that everyone can view, reducing misunderstandings and disputes.

How It Makes Existing Tasks Easier and Safer

- Eliminates manual effort by automating calculations, splits, and balance updates.
- Reduces emotional stress by removing guilt, awkwardness, and confrontation from money-related conversations.
- Prevents errors and confusion by maintaining a single, consistent source of financial truth.
- Encourages financial discipline through clear budget tracking and spending insights.
- Protects friendships by keeping money management neutral, factual, and transparent.
- Improves accountability without pressure by making dues visible and reminders system-driven.

**Challenges we ran into**

Challenges I Ran Into

One of the major challenges during development was managing layout and sizing issues caused by inconsistent CSS box models. Elements such as cards, input fields, and progress bars were overflowing or misaligning due to padding being added outside defined widths. This was resolved by standardizing the use of box-sizing: border-box and cleaning up duplicate CSS rules to ensure predictable layouts.

Another hurdle was ensuring that JavaScript logic executed correctly across multiple pages. Since the application relied on shared data, some pages failed silently when scripts were loaded in the wrong order. This was fixed by introducing a shared data file and enforcing a strict script-loading order, ensuring shared state was always available before page-specific logic ran.

A further challenge was connecting interdependent calculations across different screens. Updates in expenses needed to reflect immediately in the dashboard and settlements. This was addressed by centralizing all expense data and deriving calculations dynamically, rather than hardcoding values in individual pages.

Finally, balancing UI polish with usability required iteration. Early designs looked visually appealing but felt heavy for a finance tool. By reducing visual noise, simplifying interactions, and prioritizing clarity over decoration, the final interface became more intuitive and trustworthy for daily use.

**Hostel Life Utility Manager - UI/UX Beginner Track (Freshers Only)**

This project addresses a real, everyday problem faced by students in shared living spaces by simplifying expense tracking and settlements. It promotes transparency, fairness, and better financial coordination using a clean, accessible web-based solution.

By combining thoughtful UX with practical automation, the project reduces manual effort and social discomfort around money. Its focus on human-centered design and real-world usability aligns strongly with the track’s goal of creating impactful, problem-driven technology.

Team **TheHackWiz** -- [Avni Arora](https://github.com/avni-arora)

`2026-02-02`

---

### Hostel Expense Manager
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hostel-expense-manager-01ae) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harsh4584/hostel-expense-manager) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> A simple Python tool for hostel expense tracking.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

## What can people use this for?

Hostel Expense Manager can be used by hostel students to track their daily expenses easily.
Instead of remembering or writing expenses manually, users can record each expense with a description and amount.

This makes it easier to:
- Keep track of small daily expenses
- View all expenses in one place
- Calculate total spending 

## How it makes tasks easier

- No need to remember or write expenses manually
- Saves time by automatically calculating totals
- Provides a simple and beginner-friendly way to manage expenses
- Works completely offline and does not require internet access

This project is designed as a simple and practical solution for everyday expense tracking.

**Challenges we ran into**

## Bug / Hurdle Faced During Development

One hurdle I faced while building this project was handling user input correctly.
If the user enters non-numeric values for the expense amount, the program can raise an error.

## How I Handled It

For this beginner-level prototype, I focused mainly on implementing the core functionality
such as adding expenses, displaying them, and calculating the total.
I noted input validation as an improvement area for future versions of the project.

**Hostel Life Utility Manager - UI/UX Beginner Track (Freshers Only)**

# How My Project Fits the Hostel Life Utility Manager – UI/UX Beginner Track

- This project fits the Hostel Life Utility Manager track because it focuses on a real problem faced by hostel students.
- Managing daily expenses in a hostel is difficult because small expenses are often forgotten.
- This project helps hostel students record their daily expenses and calculate the total easily.

# Why It Fits the UI/UX Beginner Track

- The project is simple and beginner-friendly.
- It focuses on ease of use rather than complex technology.

[Harsh Jangid](https://github.com/Harsh4584)

`2026-01-24`

---

### TAXicity
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/xxx-447b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/maybedivyansh/Taxicity) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://taxicity-nine.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/HjGdTTR84VE) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Tax Planning, Minus the Wait.

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Tax-Loss Shadow: The Financial OS for Modern India
Tax-Loss Shadow is the first real-time tax optimization engine designed for India’s evolving workforce—from salaried professionals with side hustles to small business owners (SMEs) and consultants.

1. Why It’s Not Just for Freelancers
For the Salaried Moonlighter: Millions of Indians now have a salary plus freelance income. Our app handles this complex "dual-income" scenario, optimizing Section 37 expenses against their business income while tracking 80C investments for their salary.

For Small Business Owners (MSMEs): A shop owner or consultant can upload their ledger. The system identifies missed expenses—like utility bills or vehicle depreciation—that directly lower their taxable profit.

For Every Taxpayer (Regime Wars): The choice between the Old vs. New Regime confuses everyone. Our "Shadow Engine" runs a mathematically precise simulation for any income profile, proving exactly which regime saves more money based on actual spending.

2. Universal Features
Instant "What-If" Simulations: Whether you are buying office supplies or a family car, our dashboard validates the tax impact instantly. “Does this purchase lower my tax slab?” — We answer that in milliseconds.

Zero-Entry Intelligence: We parse raw CSV bank statements from any major Indian bank. No manual data entry is required, making tax planning effortless for busy professionals who hate spreadsheets.

Proactive "Loss Prevention": We don't just file taxes; we save them. The system nudges users before March 31st (e.g., “You have ₹50k unused 80C limit—invest now to save ₹10k”), preventing the loss of hard-earned money for everyone.

3. The "Financial Iron Dome"
By moving tax compliance from a reactive yearly chore to a proactive, gamified daily habit, Tax-Loss Shadow acts as a protective shield for anyone who pays taxes in India, ensuring no deduction is ever left behind.

**Challenges we ran into**

During the course of this hackathon , few unique bugs and challenges were encountered :
1. The "Dirty Data" Problem (Non-Standard Bank Statements)

Challenge: Real-world bank statements are inconsistent. Headers vary wildly (e.g., "Narration" vs. "Description"), and parsers often fail to distinguish Income from Expense when both share a column.

Solution: We built a heuristic parsing engine with "Fuzzy Header Mapping." Our code intelligently scans for keywords (like DrCr, Credit) to map data correctly and merges fields like Mode and Description so no transaction is ever left undefined.

2. Real-Time Tax Logic Complexity

Challenge: Instantly calculating tax liability for FY 2026-27 under two different regimes (Old vs. New) without lagging the UI was computationally heavy.

Solution: We decoupled the math into a pure function module (taxUtils.ts) and utilized React’s useMemo hook. This ensures that even with thousands of transactions, the "Liability Meter" recalculates instantly without dropping a single frame.

3. Handling "Ambiguous" Transactions

Challenge: A generic "Amazon" transaction could be a personal gift or a deductible office expense. A rigid rule-based system would often misclassify these.

Solution: We implemented a "Confidence-Based" Tagging System. High-confidence items (like Insurance) are auto-tagged, while ambiguous vendors (like Flipkart) are tentatively marked as "Business Expenses" to highlight potential savings, but visually flagged for user confirmation—striking a balance between automation and control.

**Open Track**

Tax-Loss Shadow is an Open Innovation in Fintech that transforms tax compliance from a reactive yearly chore into a proactive, real-time optimization game. By automating bank statement analysis and visualizing liability, we democratize elite financial planning for the Indian gig economy

Team **Team Baguette** -- [Utkarsh Singh](https://github.com/UTKI20), [Srish Bansal](https://github.com/SrishBansal), [divyansh nagpal](https://github.com/maybedivyansh), [Kanishk Kulshrestha](https://github.com/Kanishk-Kulshrestha)

`2026-02-01`

---

### CampusConnect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campusconnect-bea2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://jisce-campus-connect.ai.studio/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1222366420) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Your Campus, Connected

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

**What People Can Use College Connect For:**

**1.Students**

>Find any room/lab/office instantly via real campus blueprints
>View personalized timetable by year, department, section
>Ask the Campus AI Assistant instead of searching manually
>See all notices/extra classes in one live feed
>Search subject-wise PYQs and notes for fast revision
>Report lost items or file complaints with visible status tracking
>Learn the app fast via a home-screen demo video

**2.Parents & Guests**

>Navigate an unfamiliar campus confidently on visit days

**3.Faculty & Admin**

>Get complaints pre-sorted by department
>Push one timetable/notice update, seen instantly by all

**Overall Benefits**
>Faster navigation, fewer lost/late students and guests
>Quicker complaint resolution via auto-routing
>Fewer missed classes/events
>Easier exam prep with centralized PYQs
>Reduced paper/printing use
>Smoother onboarding via demo video
>Stronger student trust in admin responsiveness

**Challenges we ran into**

**Bugs/Hurdles We Faced and their Applied Fixes**

1.Profile & Username Sync

>**Bug**: Header/dropdown/sidebar names went out of sync after edits — pulled from stale auth data, not the updated profile
>**Fix**: Centralized to one Firestore source of truth; all views now read the same synced object

2.PYQ/Notes PDF Replacement

>**Bug**: Uploading a replacement sometimes left the old file still linked, serving outdated PDFs
>**Fix**: Made replacement atomic — old link only overwrites once new upload is confirmed

3.Timetable & Campus Zones Expansion

>**Bug**: Adding Civil/Electrical Engineering and Dr. B. C. Roy Building broke hardcoded department/building filters
>**Fix**: Refactored filters to read from a dynamic list instead of fixed values

4.Phone Number Field

>**Bug**: Field was mislabeled "Emergency Campus Contact" and not properly bound to state, so updates didn't persist
>**Fix**: Relabeled to "Phone Number," bound directly to phoneNumber with tel formatting and a standard placeholder (+91 98301 23456)

5.Password Visibility Toggle

>**Bug**: No way to verify a typed password before submitting, causing login errors
>**Fix**: Added Eye/Eye-Off toggle on login and registration fields for one-click reveal/hide, accessible by design

6.Autofill Cleanup

>**Bug**: Login/registration fields started pre-filled with default demo credentials, confusing manual sign-up
>**Fix**: Cleared pre-filled state from initial values and role-selection handlers, so fields now start blank

Team **TeamXeCute** -- ABHIROOP DAS, Khurram Mahmood, Snigdha Sarkar, PROTHAM ROY

`2026-08-29`

---

### Credora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/credora-fddc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dasouvik122005/Credora) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Unlocking Credit for the Unbanked.

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Chart.js](https://img.shields.io/badge/Chart.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**Challenges we ran into**

* **Stateless Architecture:** We wanted to protect user privacy by not storing any financial data in a database. 
**Solution:** We designed the FastAPI backend as a pure calculation engine. It returns all necessary data in a single payload, and the React frontend temporarily manages the state in memory until the user closes the tab.
* **Messy CSV Data:** Processing bulk user-uploaded CSV files caused frequent server crashes due to missing columns or incorrect data types. 
**Solution:** We built a robust data sanitization pipeline using Pandas to clean the data, fill missing values, and return clear, readable error messages instead of generic server crashes.
* **Algorithm Tuning:** Our initial scoring algorithm gave high-income earners a "Low Risk" score even if they had terrible savings habits. 
**Solution:** We introduced non-linear scaling and hard penalty flags (e.g., if expenses exceed 80% of income, the score drops drastically) to ensure the assessment was fair and realistic. 
* **Frontend-Backend Connection:** We faced CORS (Cross-Origin Resource Sharing) blocks when connecting our Vite frontend to our FastAPI backend. **Solution:** We carefully configured the `CORSMiddleware` in FastAPI to allow the specific origins, methods, and headers needed for seamless communication.

**The problem it solves**

**1. Financial Exclusion of "Credit Invisibles"**
Traditional credit scoring models (like FICO or CIBIL) rely heavily on historical debt repayment (credit cards, loans). This system inherently excludes millions of people - students, recent immigrants, freelancers, and the unbanked - who may be financially responsible but lack a formal credit history. Credora solves this by shifting the focus to **alternative financial data**, such as income-to-expense ratios, savings habits, and utility payment consistency, allowing anyone to prove their creditworthiness.

**2. Data Privacy and Security Risks**
Applying for credit typically requires handing over highly sensitive Personally Identifiable Information (PII) to centralized bureaus, which creates massive honeypots for data breaches and identity theft. Credora solves this by acting as a **stateless assessment engine**. It processes financial data in memory to generate a score and immediately discards the input. No sensitive data is permanently stored on our servers, ensuring complete privacy and minimizing security risks.

**3. Lack of Actionable Financial Guidance**
When a user is rejected for a loan or gets a bad credit score, traditional bureaus rarely tell them *exactly* what to do to fix it. Credora doesn't just output a number; it provides a detailed breakdown of the user's financial health (Income Stability, Savings Behavior, Cashflow Stability) and generates **actionable, personalized recommendations** (e.g., "Reduce monthly expenses to improve savings buffer") to help them actively improve their financial standing.

**4. Friction in Bulk Institutional Analysis**
Lenders and decentralized finance (DeFi) protocols often struggle to quickly analyze non-standard financial histories at scale. Credora solves this by offering a robust CSV batch-processing feature via our API. Institutions can upload transaction histories and instantly receive risk assessments, fraud flags, and credit scores without integrating heavy, legacy software.

Team **ThetaZen** -- [Tridib Biswas](https://github.com/GITtridib22), [Rashmi Pyne](https://github.com/rashmi-crypto), [Locket Chattaraj](https://github.com/Locket51), [Souvik Das](https://github.com/dasouvik122005)

`2026-08-25`

---

### Agent Persona Lending Protocol (APLP)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agent-persona-lending-protocol-aplp-050d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Adidem23/Agent_Persona_Lending) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=qMwx3ZNzbCg&t=4s) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Agents specialize. Capabilities travel.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![langchain](https://img.shields.io/badge/langchain-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square) ![MCP](https://img.shields.io/badge/MCP-333333?style=flat-square)

**What is the deployed URL for this project?**

https://github.com/Adidem23/Agent_Persona_Lending

**How you are solving it?**

### How you are solving it?

We built the **Agent Persona Lending Protocol (APLP)**, a capability-sharing layer that allows AI agents to dynamically discover and acquire capabilities from other agents at runtime.

During the hackathon, we implemented a working prototype with **LangGraph, FastMCP/MCP, FastAPI, and a shared capability registry**. Each agent exposes its capabilities through an MCP server, while the registry tracks the capability, its original provider, endpoint, and which agents have acquired it.

A **Capability Resolver** analyzes the user's request and determines whether the current agent has the required capability. If it is missing, the protocol searches the global registry for an agent providing it, retrieves the capability, dynamically injects it into the requesting agent's MCP server, refreshes its available tools, and allows the agent to continue execution without restarting.

For the demo, we use simple capabilities such as **Addition, Multiplication, Division, and Text Summarization** to clearly demonstrate the real-time exchange. These are intentionally simple demo tools—the protocol is designed to support much richer capabilities such as OCR, database access, computer vision, research, and enterprise tools.

The core flow we implemented is:

**Detect → Discover → Acquire → Inject → Refresh → Execute → Record**

The current submission is a **hackathon-built prototype**, developed specifically to demonstrate this capability-lending architecture. The simple demo tools and protocol implementation were built for this hackathon and are not a previously presented product or reused hackathon submission.

**What is the problem your project solves?**

### What is the problem your project solves?

AI agents are typically built with a **fixed set of tools and capabilities**, meaning an agent can only perform tasks its developers anticipated. When it encounters a capability it doesn't have, it must either fail or delegate the entire task to another agent. This makes multi-agent systems rigid, tightly coupled, and difficult to scale.

**Agent Persona Lending Protocol (APLP)** solves this by introducing a capability-level lending layer between agents. An agent can identify a missing capability, discover another agent that provides it, and dynamically acquire that capability at runtime through a shared registry and MCP—without rebuilding or restarting itself.

For example, a calculator agent can start with addition and multiplication, discover that another agent provides division, acquire the division capability, and immediately continue the task. The same mechanism can work across completely different domains such as vision, databases, research, OCR, or enterprise tools.

This enables **dynamic, composable agent personas** where agents specialize in what they are best at while their capabilities can evolve on demand. The long-term impact is a more scalable agent ecosystem where capabilities—not entire agents—can be discovered, shared, and composed dynamically.

**How Did You Use Claude?**

### How Did You Use Claude?

We used **Claude** as the reasoning model powering our AI agents, particularly for **capability detection and decision-making** within the LangGraph workflow.

Claude analyzes the user's request and determines the capability required to fulfill it. It then checks the global capability registry to determine whether that capability is already available to the current agent or needs to be acquired from another agent.

Claude is therefore used primarily as the **reasoning layer**, while APLP handles capability discovery, lending, dynamic MCP tool injection, and runtime execution.

In short:

**Claude → Reason about required capability → APLP → Discover & acquire capability → MCP → Execute**.

[Aditya Suryawanshi](https://github.com/Adidem23)

`2026-08-08`

---

### huggingface-connector
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/procureguard-f705) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alogotron/huggingface-connector) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://alogotron-huggingface-connector.hf.space) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Policy-gated data payments with scoped access

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

## What it does

**huggingface-connector** is an agentic payment and access rail for licensed Hugging Face dataset artifacts and subsets. A buyer agent can inspect SHA-pinned metadata and a safe sample, evaluate budget, license, quality, task relevance, and publisher policy, request explicit human approval, create a Prava sandbox payment session, verify the authoritative result, and unlock only the exact purchased scope.

## Why it matters

AI agents need data, but automated purchasing must not turn into uncontrolled checkout or broad credential access. This MVP makes the decision legible while keeping authorization deterministic and server-enforced:

- rejects over-budget or disallowed purchases before payment;
- revalidates dataset, seller, amount, currency, license, and scope server-side;
- requires explicit approval before session creation;
- treats redirects, `pending`, and `awaiting_result` as non-final;
- issues access only after a later exact matching `completed` result;
- provides a five-minute, HMAC-signed, scope-bound, single-redemption entitlement;
- never exposes a publisher Hugging Face token.

The demo uses a seller-authorized synthetic support-intent dataset under CC BY 4.0. Hugging Face is the revision-addressed metadata/repository surface; this project does not claim that Hugging Face natively sells datasets.

## Judgeable flow

1. Inspect the catalog and pinned provenance.
2. Evaluate the $9 starter dataset under a $25 policy budget.
3. Review the buyer agent's deterministic reasons.
4. Create an intent and explicitly approve the exact contract.
5. Create and verify a Prava sandbox session.
6. Receive narrowly scoped access only after completed-state verification.
7. Run the $249 over-budget case to see payment blocked with an audit trail.

## Built with

Flask, Python, JavaScript, Prava Sandbox APIs, Hugging Face metadata conventions, HMAC entitlements, CSRF protection, and a responsive browser UI.

**Challenges we ran into**

## Payment-state correctness

The hardest part was resisting the tempting shortcut of treating a checkout redirect or credential response as success. Prava can return `pending` or `awaiting_result`, and neither is final. I implemented a fail-closed state machine: uniquely match the expected line item, keep ephemeral sandbox credentials inside the adapter, report the exact transaction reference in the seller-owned sandbox simulator, and re-poll until an authenticated response is exactly `completed`. Any timeout, ambiguity, mismatch, cancellation, or failure grants no access.

## Binding payment to access scope

The payment-result schema does not echo every semantic entitlement field, so the server creates immutable bindings for currency and scope and derives the external product reference from `SHA-256(dataset_id|scope)`. Fulfillment compares session, order, dataset, seller, amount, currency binding, scope binding, and product reference before issuing a token.

## Safe Hugging Face positioning

Hugging Face is used as the revision-addressed metadata and artifact identity surface, not described as a native paid marketplace. When the pinned demo repository is unavailable, the app visibly falls back to a seller-authorized local fixture only after checking its SHA-256 digest. Publisher credentials never cross the server boundary.

## Sandbox checkout environment

The Prava-hosted sandbox requires secure card verification that is not available in the headless judge browser. The integration therefore remains honest and fail-closed: the dashboard records the sandbox order as pending, the app issues no entitlement, and the submission does not claim a completed Prava transaction. The demo-simulator path separately demonstrates the complete verified-access UX and is explicitly labeled as simulation evidence.

## Verification

I added 19 automated tests for policy rejection, approval gating, Prava endpoint contracts, non-final states, exact-field mismatches, status reporting, entitlement expiry, tampering, single redemption, CSRF protection, persistence, and end-to-end browser-equivalent behavior. Python compilation and JavaScript syntax checks also pass.

**Best Visa Intelligent Commerce Implementation**

Prava is the project’s core authorization and payment rail. The system validates the exact purchase contract, requires human approval, fails closed on pending or mismatched payments, and prevents unpaid access.

**Best Agentic User Experience**

The guided interface clearly shows dataset provenance, agent policy checks, the exact purchase contract, payment status, entitlement scope, and an audit trail—including an over-budget rejection before payment.

**Agentic Commerce Hackathon**

Our buyer agent evaluates licensed dataset access, enforces budget and license policies, requests explicit approval, uses Prava for payment authorization, and grants only narrowly scoped access after verified completion.

alogo tron

`2026-08-02`

---

### MineFix
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/minefix-c4c4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CleanDev-Fix/minefix-approvals) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://minefix-approvals.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-governed maintenance approvals and payments

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square)

**Challenges we ran into**

Prava's hosted sandbox uses single-use, 15-minute sessions. We added live catalog validation, idempotent session creation, safe replacement only while a session is unused, and a single-attempt checkout guard.

During final testing, OTP succeeded but Visa passkey enrollment returned to setup on both the original and one fresh session. No payment credential was issued, so we stopped instead of burning the session quota or faking completion. MineFix preserves that exact blocked state while the OpenAI decision, human approval, Prava session creation, and status polling remain verifiable.

**The problem it solves**

Heavy-equipment repairs lose time when photos, engine hours, quotes, approvals, and payments live in different systems.

MineFix gives a mechanic one place to document the failure and submit the repair. OpenAI checks the evidence and spending policy; safe requests continue, while over-limit work pauses for one accountable human approval before Prava handles payment.

The result is a permanent equipment history for maintenance, warranty, and cost reporting. Next, we would add telematics and multi-site fleet reporting.

[CleanFix Dev](https://github.com/CleanDev-Fix)

`2026-08-03`

---

### Ally
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ally-7162) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/samsonafolabi/Ally) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ally-1-tfbq.onrender.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/0ca595856b4640aeba3058b2cf46e933) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Handles you vendor payments, you stay in control

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

## What Ally is for

If you run a small company, agency, or team that hires freelancers and contractors, you already know the pain. Invoices come in through email. Someone has to notice them, figure out if they're legit, chase down the right person to approve them, and then actually pay them. That whole process is slow, easy to mess up, and honestly kind of sketchy when it comes to accountability. "Someone said it was fine" isn't the same as having a real record of who approved a specific payment.

Ally handles that entire chain automatically, but keeps a human in control of the money.

## How it actually helps

**You stop losing time to manual busywork.** A quote comes in over email, Ally reads it, figures out who's supposed to approve it based on category and amount, and pings that person directly on Slack. No forwarding emails around, no "did anyone see this yet."

**You stop paying invoices that don't check out.** When an invoice shows up, Ally matches it against the original approved quote (the PO) before it ever gets routed for payment. Wrong amount, no matching PO, mismatched reference number, it gets flagged for a human to look at instead of getting auto-approved. This is the same matching process real finance teams use, just automated.

**Nobody can just click a button and move money.** Every payment still needs an actual human to approve it, and that approval is verified against who was actually assigned to it. So if a payment request goes to Sarah, only Sarah's approval counts, not whoever happened to be near the Slack channel. Payments themselves go through passkey confirmation, so there's a real security step before money moves, not just a Slack click.

**You get a paper trail for free.** Every quote, approval, PO, invoice match, and payment is logged with a timestamp and reasoning. If someone later asks "wait, who approved this $2,000 payment," you have an actual answer instead of digging through Slack history and hoping.

## Who this is actually useful for

Agencies and small teams working with a rotating cast of freelancers and vendors, where payments are one-off and negotiated rather than fixed subscriptions. Anyone doing procurement at a small scale who wants the rigor of a real finance process (quote, PO, invoice, reconciliation, payment) without hiring someone to run it by hand or buying enterprise software built for teams ten times their size.

**Challenges we ran into**

## Deployment split brain

The last real hurdle wasn't the agent logic, it was deployment. I had the bot and the dashboard API set up as two separate services on Render, and I didn't clock that Render doesn't share a filesystem between services. The bot was writing all its state (pending approvals, POs, payments) to local JSON files, and the dashboard was reading from what it assumed was the same folder, except it was actually reading from an entirely different, empty disk on a different instance. Payments were going through fine, Slack approvals were working, everything on the backend was solid, but the dashboard just sat there showing nothing. Took a while to realize the two services were never actually talking to the same data at all.

## A silent .gitignore bug

At one point the bot service just wouldn't boot on Render. It kept crashing with a MODULE_NOT_FOUND error pointing at a file that definitely existed in my project, `src/data/store.ts`. Worked completely fine locally. Turned out my `.gitignore` had an unanchored `data/` rule meant to ignore the runtime JSON files at the project root, but because it wasn't anchored, it was also matching `src/data/`, which is where actual source code lived. Git just never tracked that folder, so it flat out didn't exist on Render even though it was sitting right there on my machine. Fixed it by anchoring the rule to `/data/` so it only ignores the root-level runtime folder, force-added the source files, and the crash went away immediately.

## Frontend calling the wrong domain entirely

Even after fixing the above, the dashboard was still 404ing on every API call. I'd set up a rewrite rule on Render to proxy `/api/*` requests to the backend, but the requests were still failing. Digging into the browser console showed the frontend was firing requests straight to its own domain instead of getting proxied anywhere, meaning the rewrite just wasn't being applied the way I expected. Rather than keep fighting Render's rewrite behavior with the clock running, I switched to an explicit `VITE_API_URL` environment variable that gets baked into the build and used directly in the axios calls. More reliable, easier to reason about, and it meant one less moving piece to debug under pressure.

The common thread honestly was that none of my actual product logic broke. The AI extraction, the Slack routing, the PO matching, the Prava payment flow, all of that worked the first time I wired it up. Every real bug was in the boring infrastructure between services, which in hindsight is exactly where I'd expect a rushed hackathon deploy to fall apart.

**Best Visa Intelligent Commerce Implementation**

## How Ally fits the Visa Intelligent Commerce track

The track is about agents that can actually move money on someone's behalf, not just draft an email or fill out a form. That's exactly what Ally does. It doesn't stop at "here's an invoice, someone should look at this." It carries the whole thing through to an actual completed payment, using Prava as the trust and execution layer that makes that safe to automate.

**Prava is the actual payment rail, not a mock.** Every payment in Ally goes through Prava's sandbox REST API. Ally creates a real session scoped to the exact vendor and amount for that specific invoice, not some generic account or reusable budget. Once the session is created, Ally polls it, handles retries if something transient fails, and reports the final outcome back to Prava when it's done. This isn't a payment button that fires an email, it's a real programmatic session with Prava tracking status the whole way through.

**The passkey approval is the actual point, not a hoop to jump through.** A lot of "agentic payments" demos quietly skip the hard part and just let the agent pay whatever it decides. Ally is built the opposite way. The agent can extract, reconcile, and decide who should be asked, but it can never actually release money on its own. A human has to complete Prava's passkey approval before the session goes through. That boundary is the actual product, not a limitation I worked around for the hackathon.

**Prava fits Ally's use case specifically because these aren't subscriptions.** Freelance and vendor payments are one-off, negotiated, different amount every time. A fixed-budget mandate doesn't make sense here. Prava's plain one-shot session flow, scoped per transaction, matches that reality instead of forcing freelance payments into a subscription-shaped tool.

**Every payment carries Visa's network confirmation, not just an internal "done" flag.** When a payment finishes, Ally records the transaction reference, authorization code, and the actual Visa network confirmation status (SUCCESS or FAILURE), and reports that outcome back to both Prava and the Slack thread. That confirmation is what makes the audit trail meaningful. It's not "the agent said it paid," it's a verified network-level result tied to a specific approver, a specific invoice, and a specific PO.

Put simply, the AI does the work everyone hates doing, reading invoices, chasing approvers, matching numbers, but the actual transfer of money always runs through Visa's rails with a real human confirming it at the one point where confirmation actually matters.

**Agentic Commerce Hackathon**

## How Ally fits the Agentic Commerce track

Agentic commerce is really about whether an AI agent can be trusted to actually carry out a commercial transaction end to end, not just assist with one step of it. Most "AI for business" tools stop at reading or summarizing something. Ally goes further. It reads, decides, routes, and eventually initiates a real payment, without a human having to manually shepherd it through every stage.

**Ally handles the full commercial lifecycle, not a single task.** A lot of agent demos pick one narrow job, like extracting data from an invoice, and call it done. Ally covers the whole chain a real transaction goes through: quote arrives, gets read and routed to the right approver, becomes a PO once approved, vendor gets notified, invoice comes in later, gets reconciled against that PO, and only then goes to payment. That's the actual shape of how commerce works between two parties, and Ally automates the coordination across all of it instead of just one piece.

**It makes real decisions, not just extractions.** Ally isn't only pulling fields out of an email. It decides who should approve something based on category and amount, it decides whether an invoice actually matches what was approved earlier, and it flags mismatches instead of blindly trusting that an invoice equals a valid bill. That's the difference between a parsing tool and something that's actually participating in the transaction.

**Autonomy stops exactly where money changes hands.** This is the part I think matters most for agentic commerce specifically. Letting an agent freely move money is where most of these systems either get scary or get faked in demos. Ally draws a hard line: the agent can do everything up to proposing a payment, but a human always completes the actual authorization through Prava's passkey flow. The system is agentic where it's safe to be agentic, and it stays human-gated exactly where real money is at stake.

**It closes the loop instead of leaving a dangling task.** After a payment goes through, Ally doesn't just stop. It reports the outcome back to Prava and back to the Slack thread where the approval happened, so the person who approved it sees confirmation that it actually completed. Agentic commerce isn't just triggering an action, it's the agent staying accountable for the result of that action.

So the core fit is this: Ally is an agent that manages an entire commercial relationship, quote to paid, and does it by making real judgment calls at every step, while keeping the one truly consequential decision, releasing funds, in human hands.

Afolabi Samson

`2026-08-03`

---

### GrowthOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/growthos-an-ai-team-every-small-business-deserves-6bf3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Satyam7Jha/hakathone-gemma) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=hU3y0L-_C2M&t=36s) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> An AI team every small business deserves

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Small businesses are invisible where it matters — outdated websites that don't rank, no idea what competitors are doing, and financing gaps that come partly from having no digital footprint to show for themselves. GrowthOS gives them AI agents that fix exactly that.

Helping small businesses grow, stand out, and stay ahead — every single day, powered by AI.

**Challenges we ran into**

Getting Gemma to actually behave like an agent. The 4B model is small enough to run on a laptop, which is the whole point, but it's nowhere near as obedient as something like GPT-4 when you tell it "only reply in this exact JSON format." It would randomly throw in a trailing comma, or explain itself before the JSON instead of just outputting it, and the whole agent loop would choke. Took a lot of trial and error — rewriting the prompt, adding a repair step to catch the malformed responses — before it stopped breaking mid-run.
The other thing was just scope. We started out wanting six agents and realized pretty fast that six half-working agents demo way worse than four solid ones, so cutting down was its own kind of hard.
And if I'm being honest, the live browser thing for the SEO agent — the part we're most excited to show off — was also the part that fought us the most. Real websites have cookie banners, slow-loading pages, random popups, and none of that shows up until you actually try it on a live site instead of your own test page.

Team **Quantum Crew** -- [Satyam Jha](https://github.com/Satyam7Jha), [vishal kumar](https://github.com/Hack7023)

`2026-07-18`

---

### Talking Rabbitt
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/talking-rabbitt-5938) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/umangjaiswal0723/talking-rabbitt) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://talking-rabbitt-4lvq.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-HackGenome-0052CC?style=flat-square)](https://hackgenome2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Ask questions about your data using AI — no coding

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

- Connecting the React frontend and FastAPI backend in a single server deployment
- Handling multiple file formats (CSV and Excel) with different structures
- Building a forecasting engine that works across different types of datasets
- Making the AI responses data-specific rather than generic answers

**The problem it solves**

Most businesses have data in Excel or CSV files but no easy way to understand it. Talking Rabbitt lets anyone upload their data and instantly get KPI dashboards, charts, trend analysis, forecasting, and an AI chat that answers questions about their data — no coding or data science knowledge needed.

Team **Agni** -- [VAIBHAVI GARG](https://github.com/Vaibhaviverse-cloud), [Piyush Kumar](https://github.com/Piyush0628), [Umang Jaiswal](https://github.com/umangjaiswal0723), [Shreya Sharma](https://github.com/ShreyaSharma2008)

`2026-06-15`

---

### OvernightCo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/overnightco-9b5b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Officialhomie/overnightco) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://overnightco.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Give an AI $20 and a niche. Come back tomorrow.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![nextjs](https://img.shields.io/badge/nextjs-333333?style=flat-square) ![AI-agents](https://img.shields.io/badge/AI--agents-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square) ![autonomous](https://img.shields.io/badge/autonomous-333333?style=flat-square) ![neon-postgresql](https://img.shields.io/badge/neon--postgresql-333333?style=flat-square)

**The problem it solves**

OvernightCo is an autonomous AI business that picks a niche, builds an intelligence product, and sells it — with no human in the loop after the initial deposit.

**The problem it solves:** Building a content business takes weeks of research, writing, pricing, and distribution. OvernightCo compresses that into 240 seconds using three autonomous agents:

- **Scout (DECIDE):** Scores candidate niches using `expected_value = revenue × probability − cost` and picks the highest-EV opportunity
- **Builder (BUILD):** Uses Locus Wrapped APIs (Exa search + Claude writing) to produce a 600-800 word intelligence brief. Build cost: ~$0.24 per product
- **CFO (REPORT):** When revenue crosses the profit threshold, calls Locus pay/send to sweep net profit to the owner wallet autonomously

**Two payment rails from one product:**
- Human readers: $2.00 USDC via Locus Checkout (formatted article)  
- AI agents: $0.50 USDC via HTTP 402 (raw JSON data endpoint)

The price difference was the AI's idea. Both tiers are profitable above the $0.24 cost basis.

**Locus APIs used:**
- Wrapped APIs (Exa + Claude) — agent cost side, logged to real-time P&L ledger
- POST /checkout/sessions — human and agent checkout creation
- POST /checkout/agent/pay/{id} — autonomous agent payments
- GET /pay/balance — real-time wallet monitoring
- POST /pay/send — autonomous profit sweep
- Webhook checkout.session.paid — payment confirmation + access token
- HTTP 402 — machine-readable payment required for agent buyers

**LocusFounder** designed the business: named it, set the two-tier pricing, specified the editorial storefront aesthetic, and produced a 6-page business plan in a single Telegram session.

**Challenges we ran into**

**Trusting the AI's pricing instinct was the hardest part.**

LocusFounder set $0.50 for the agent tier. It felt low. But the math works: at $0.24 build cost every sale — human or agent — is profitable. The AI knew.

**Technical challenges solved:**

**1. HTTP 402 agent payment flow**  
Built a machine-readable payment protocol where AI agents discover products via /llms.txt, get a 402 with payment instructions, pay via Locus agent checkout, then receive a time-limited access token for the raw JSON endpoint. Zero human interaction.

**2. Real-time P&L ledger**  
Every Locus Wrapped API call (Exa search, Claude generation) deducts from a running cost tracker. The CFO agent reads this ledger to make accurate payout decisions — it only sweeps when net profit is genuinely positive.

**3. Autonomous profit sweep**  
The CFO agent uses Locus pay/send when the threshold is crossed, requiring zero human approval. The owner just watches the wallet balance grow.

**4. Dual content format**  
Same database row serves formatted HTML to humans and structured JSON to agents, priced differently based on the buyer type detected in the subscribe request.

**5. LocusFounder as the actual founder**  
The business model, brand name, pricing strategy, and go-to-market plan all came from a single LocusFounder Telegram conversation. We just wired the pipes it specified.

**Using LocusFounder to Build a Business!**

OvernightCo is the most literal execution of this track premise. LocusFounder named the business, set the two-tier pricing ($2 human / $0.50 agent), designed the storefront, and produced a 6-page business plan in one Telegram session. We wired the pipes. Locus APIs used: Wrapped (Exa + Claude), Checkout, pay/send, HTTP 402, webhooks. The agent is the business. LocusFounder built it.

[Victor Igwilo](https://github.com/Officialhomie)

`2026-05-17`

---

### Quick Serve
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quick-serve-41e3) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The Tools Hub

![OAuth](https://img.shields.io/badge/OAuth-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square) ![Clerk](https://img.shields.io/badge/Clerk-333333?style=flat-square)

**The problem it solves**

Most Of The Time when we need a tool we need to sort through slop and tons of ads well Quick Serve fixes that problem it has range of tools availble for you on a monthly subscription. You can also generate your own tool using the AI tool generator

**Challenges we ran into**

I had ran into alot of challanges with deployment due to bugs in the sandbox although locus founder team resolved the issue quickly 

although at the end i had ran out of credits due to all the bugs and was unable to deploy the website

I would like to reserve a moment to thank the locus team for creating such an easy and user friendly tool to use 

So i will explain the website  in words 

1.you would start with a landing page which would introduce you to quick with its tools and goals and at the end of landing as well at the top right corner of the page there would be a start now button 

2.then you would login or sign up using email, password or Oauth

3. Once done you would choose a plan either free with 10c pro with 100c and max with 500c pro was priced at 19 dollars max at 29 dollars

4 now you had access to all the tools and the tool generator 

5.all of these tools would have a credit system
   Like password genrate 2 credits per use
   like this we would keep adding commonly used tool to the library

6. Now the mini tool generator it would use chatgpt 4.5 to first refine the prompt after that it will use gemini 3.1 flash to genrate the tool and return it to the user on a temporary url which would be deleted in 10 days 
This would be a pro feature so free tier cannot use it 
If the user wants to retain the tool
he or she can press keep tool 
this would require 4 extra credits


The ui would be a mix of lime green and black with jetbrains for font

Team **ez** -- Aradhya Sahu

`2026-05-26`

---

### LastBatch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lastbatch-9ce4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mpbcmrks0r9u42r0.buildwithlocus.com/#) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tRrkA_7sYU0) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI flash sales for closing-time food

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![fintech](https://img.shields.io/badge/fintech-333333?style=flat-square) ![Ecommerce](https://img.shields.io/badge/Ecommerce-333333?style=flat-square) ![LocusFounder](https://img.shields.io/badge/LocusFounder-333333?style=flat-square) ![LocusCheckout](https://img.shields.io/badge/LocusCheckout-333333?style=flat-square) ![AIAgents](https://img.shields.io/badge/AIAgents-333333?style=flat-square) ![FlashSales](https://img.shields.io/badge/FlashSales-333333?style=flat-square)

**The problem it solves**

Local bakeries, cafes, and food counters often close with unsold perishable inventory. That leftover stock becomes waste even when nearby customers would happily buy it at a time-sensitive price.

LastBatch turns that closing-time inventory into a complete autonomous sales loop. A merchant enters a batch in under a minute — item, quantity, retail price, price floor, pickup deadline, and location. The Locus operator then prices the offer inside the merchant floor, launches a flash storefront, runs the sale in Locus Checkout demo mode, issues pickup code LB-2847, and rolls the simulated orders into a transparent revenue ledger.

The result is a business-in-a-box workflow for perishable inventory: intake, agent pricing, storefront, checkout, pickup, ledger, commission, and wallet payout language all in one demo. For Crumb & Co., the demo recovers ₹1,710 from 38 of 40 cupcakes that would otherwise have been at risk by closing time.

**Challenges we ran into**

The hardest part was making the project feel like an agent-run business rather than a static landing page. Early builds split the polished marketing page and the 7-step operator demo into separate deployments, and the builder also tried to force a catalog/storefront setup when this hackathon build needed to be a feature-only interactive demo.

We solved that by keeping the catalog draft untouched for a future real checkout setup, bypassing catalog requirements only for this demo build, and tightening the flow around a simulated but end-to-end merchant operation. We also replaced Stripe language with Locus Checkout demo mode and Locus wallet settlement language so the story matches the Paygentic theme without claiming real payment processing.

The final polish work focused on trust: real product screenshots, mobile-first flow, consistent payout math, explicit demo labels, and a premium 45-second voiceover video cut that explains the complete business loop quickly for judges.

**Using LocusFounder to Build a Business!**

LastBatch fits the **Using LocusFounder to Build a Business** track because the agent is not just helping a merchant make a page — it is operating a small commercial unit from intake to close.

The flow takes leftover inventory, applies merchant-safe pricing constraints, launches a live storefront, routes buyers through Locus Checkout demo mode, issues pickup codes, and produces a ledger with commission and payout language. That makes every leftover batch an ephemeral business: created, monetized, settled, and closed by the operator.

It demonstrates the track idea directly: agents that do not merely assist businesses, but run repeatable revenue workflows that can make money for real local operators.

Team **PatchyNeurons** -- [Arpita Gupta](https://github.com/Arpi1404), [Vasu Bhardwaj](https://github.com/vasubhrdwj)

`2026-05-24`

---

### Broskie.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/broskieai-1805) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0day-Ashish/broskie-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://broskie-ai-gtic.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Elevate Your Job Hunt Style with broskie😛

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Job hunting today is honestly a grind. You spend hours scrolling through listings, tweaking your resume for every role, filling out the same forms again and again… and most of the time, you don’t even hear back. It’s repetitive, time-consuming, and pretty frustrating.

What You Can Use It For - 
Automate job applications → Just tell it what role you want, and it handles the process
Tailor resumes automatically → No more editing your resume for every single job
Find relevant opportunities faster → Filters out the noise and focuses on what actually matches
Track applications in one place → No more losing track of where you applied

How It Makes Things Easier - 
Saves hours of manual effort
Removes the repetitive parts of applying
Helps you apply faster and more consistently
Lets you focus on what actually matters → preparing for interviews & improving skills

**Challenges we ran into**

I faced issues with the parsing library itself, especially with how it behaved in the Next.js environment. There were errors related to file paths, and sometimes the parser wouldn’t read the file properly at all. Even when it worked, the extracted text wasn’t always clean, formatting was lost, and sections like skills or experience weren’t clearly separated.

[Ashish Ranjan Das](https://github.com/0day-Ashish)

`2026-04-28`

---

### ZeroEmployees
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zeroemployees-4981) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PanaitAlessandro/ZeroEmployees/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-moh9gocyq4x451sj.beta.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The first AI that doesn't just work for you.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

We are entering a world where AI can generate value, but still cannot *participate in the economy*.

Today’s systems are powerful but fundamentally limited:
they depend entirely on humans to decide when to act, what to buy, what to trust, and how to monetize.

This creates a paradox:
AI can produce outputs at scale, but it cannot sustain itself.

ZeroEmployees removes this limitation entirely.

It introduces a new primitive: AI as an economic entity.

Instead of being controlled step-by-step, the system:
- identifies opportunities
- evaluates cost vs return
- spends capital through real payment rails
- produces outputs
- sells those outputs
- and tracks profit over time

Every action is constrained by real economic rules:
no payment → no execution  
negative ROI → no action  
failed output → recorded loss  

This changes everything.

For the first time, AI is not just automating tasks,
it is making decisions under scarcity, risk, and incentive.

People can use ZeroEmployees to:
- run fully autonomous digital businesses
- test strategies in real economic environments
- create agent-to-agent marketplaces
- deploy systems that operate continuously without supervision

This is not a better workflow.
This is the transition from software to autonomous economic systems.

ZeroEmployees is what happens when AI stops being a tool,
and starts being a participant in the market.

**Challenges we ran into**

The hardest part was not building intelligence, but enforcing reality.

Most AI systems today simulate autonomy, but bypass the constraints that define real-world behavior:
they don’t pay, they don’t lose money, and they don’t face consequences.

ZeroEmployees had to operate under real economic pressure.

This introduced three fundamental challenges.

---

### 1. Enforcing irreversible payment before execution

In a real economy, value exchange happens before service delivery.
We needed to guarantee that no external action could ever happen without confirmed payment.

Solution:
- Every external call is wrapped in a strict payment gate
- Execution is blocked unless a verified payment exists
- Unpaid attempts are treated as system failures

This turns “AI actions” into actual economic transactions.

---

### 2. Forcing decision-making under uncertainty and risk

AI typically optimizes for output, not survival.

We introduced a hard constraint:

expected_value = (estimated_revenue × probability_of_success) − cost

If expected value is not positive, the system does nothing.

If uncertainty is too high, the system refuses to act.

This created something unexpected:
the system hesitates, evaluates, and sometimes chooses inaction,
just like a real company protecting its capital.

---

### 3. Building against incomplete infrastructure (Locus)

We integrated a next-generation payment system designed for agents,
but with evolving specifications and partial documentation.

Instead of hardcoding assumptions, we:
- built a strict abstraction layer for all payment logic
- isolated external dependencies behind a single interface
- ensured the system remains stable even as the underlying API evolves

---

### Outcome

The result is a system that behaves differently from anything else:

- it can lose money
- it can make bad bets
- it learns from failure
- it improves decisions over time

It does not simulate a business.

It behaves like one.

**Track: Checkout with Locus**

ZeroEmployees is built entirely around Checkout with Locus as its economic backbone.

This project does not treat Locus as a simple payment integration,
but as the core infrastructure that enables autonomous agents to operate financially.

The system leverages Locus in three fundamental ways:

### 1. Machine-readable payments for autonomous agents

Every transaction in ZeroEmployees is initiated through a Locus checkout session.
Because the checkout is machine-readable, agents can:

- discover services
- evaluate pricing
- initiate payments programmatically

This allows AI agents to act as real buyers, without human intervention.

---

### 2. Payment as a hard execution gate

Locus is not used after the fact, but before any value is created.

- No external service can be executed without a confirmed Locus payment
- Checkout sessions are created before every paid action
- Execution is unlocked only after webhook confirmation

This enforces a real economic constraint:
**no payment → no action**

---

### 3. Agent-to-agent commerce

ZeroEmployees exposes its own outputs as paid services,
also gated through Locus checkout.

This means:
- the system both consumes and sells services
- other agents (or humans) can discover and pay for its outputs
- all interactions use the same standardized payment layer

This creates a closed economic loop powered entirely by Locus:
agents paying agents, without custom integrations.

---

### Why this matters

Most implementations treat payments as a UI feature for humans.

ZeroEmployees demonstrates something different:
Locus enables a new class of systems where payments are
**native to machine behavior, not just user interfaces.**

It shows how Checkout with Locus can become the default layer
for autonomous economic interactions between agents.

This is not just integration.

This is what Locus was designed for.

[Oana Mihaela Panait](https://github.com/PanaitAlessandro)

`2026-04-28`

---

### L-ESCROW
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lescrow-719a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XZNON/L-ESCROW) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/b90618bad3554a2ea9c537ad8962406b) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/b90618bad3554a2ea9c537ad8962406b) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Automation over Creation

![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![imutils](https://img.shields.io/badge/imutils-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square) ![python-pywhatkit](https://img.shields.io/badge/python--pywhatkit-333333?style=flat-square) ![Asyncio](https://img.shields.io/badge/Asyncio-333333?style=flat-square)

**The problem it solves**

# The Problem: The "Trust Gap" in Autonomous AI Labor

As AI agents move from writing text to performing actual work (like fixing code, managing infrastructure, or handling data), two critical barriers emerge:

- **The Risk of Failure:** Businesses cannot safely give an autonomous agent a credit card or direct write-access to production systems without a "safety net."
- **The Verification Burden:** Manually reviewing every line of code an AI writes defeats the purpose of automation.

L-ESCROW solves these problems by creating a decentralized, agentic marketplace where AI labor is governed by financial logic and multi-model consensus.

---

# What People Use It For

## 1. Autonomous Codebase Maintenance

Instead of a human developer hunting for bugs, a "Buyer Agent" monitors a GitHub repository. When a bug is found, it automatically opens a bounty. A population of "Seller Agents" competes to fix it. The human only sees the final result: fixed code that has already been verified by a jury of other AIs.

---

## 2 The L-ESCROW Solution: Tasks that Recruit Agents

L-ESCROW implements a Reverse Marketplace architecture. Instead of a "Search and Apply" model, we use a "Broadcast and Compete" model:

- **Proactive Procurement:** A Buyer Agent (monitoring a codebase or server) identifies a deficiency and autonomously broadcasts a Request for Proposal (RFP) into the ecosystem.

- **The 15-Agent Population:** Instantly, a diverse population of 15 specialized Seller Agents (Interns, Pros, and Experts) analyze the task simultaneously.

- **The "Bid Storm":** Within seconds, the marketplace populates with competitive bids. The system doesn't wait for a human to choose; the Buyer Agent evaluates the agents' reputation, price, and tier to automatically award the contract.

## 3. Verifiable AI-to-AI Transactions

L-ESCROW provides the infrastructure for AIs to hire each other.

- **Example:** A complex Data-Science AI needs a specific API script written. It hires a specialized "Coder Agent" through L-ESCROW. The funds are only released when the script passes the automated validation and AI-consensus check.

---

## 4. Crowdsourced "Agentic" DevOps

Companies can seed their technical debt into the L-ESCROW marketplace. Specialized agents—from "Intern" tiers for simple refactors to "Expert" tiers for security patches—work concurrently to resolve issues, ensuring the highest quality at the lowest market-clearing price.

---

# How It Makes Tasks Safer and Easier

- **Risk-Free Automation:** By using an Escrow-first architecture, funds are never paid out upfront. If the agent's code fails the build or the AI Jury's review, the money is returned to the user.

- **Consensus-Based Quality Control:** Rather than trusting one LLM (which might hallucinate), L-ESCROW uses a Multi-Model Jury (Groq + Gemini) to cross-verify work. This creates a "Checks and Balances" system for autonomous labor.

- **Market Efficiency:** The 15-agent population introduces competition. Users don't have to decide which AI model is best for a task; the marketplace decides by rewarding the agents that deliver passing code at the most competitive price.

- **The "Mock-Git" Safety Valve:** Our simulation sandbox allows for "dry-runs" of autonomous fixes. People can see the AI's "thought process" and the resulting code diff in a safe environment before it touches a real production branch.

---



# The L-ESCROW Bottom Line

We turn AI agents into accountable contractors. We don't just ask AI to do work; we provide the legal, financial, and technical framework to ensure that work is actually done correctly before a single cent is paid.

**Challenges we ran into**

## 1. The "Real Funds" Barrier & Virtual Settlement

The most significant hurdle was the inability to use actual legal tender for autonomous agent transactions due to KYC (Know Your Customer) restrictions, banking APIs, and safety concerns.  

- **The Challenge:** We needed a way to demonstrate the financial finality of escrow without risking real bank accounts or dealing with the latency of traditional wire transfers.  

- **The Solution:** We implemented a Virtual Escrow Settlement system using the Locus Checkout API. This allowed us to simulate high-velocity financial transactions where "credits" are locked in a cryptographically secure session. It provided the same "hold-and-release" logic as a real bank, ensuring the Seller agent only gets paid when the work is verified, without the overhead of a traditional financial institution.  

---

## 2. The "Thundering Herd" API Cost Problem

When we scaled the system to a population of 15 agents, we hit a massive hurdle regarding LLM API costs.

- **The Challenge:** Initially, all 15 agents would attempt to generate a code fix simultaneously to see who could bid the fastest. This would have cost hundreds of dollars in API credits for just a few bugs.

- **The Solution:** We engineered a "Lazy Generation" architecture. Agents now bid using pure Python logic (Phase A) at zero cost. Only after the Buyer Agent selects a winner and the contract is "Locked" does the specific winning agent call the Groq/Gemini models to generate the code (Phase C). This reduced our demo costs by 95% while maintaining a competitive marketplace.

---

## 3. The "Hallucination" Gap in Code Review

Trusting a single AI to verify another AI's code is dangerous, as the "Assessor" might hallucinate that a broken fix is actually working.

- **The Challenge:** We needed a governance layer that was more reliable than any single model.

- **The Solution:** We implemented a Multi-Model Consensus Jury. By using two vastly different architectures—Groq (Llama 3) for speed and Gemini 1.5 Pro for deep reasoning—we forced the system to reach a unanimous verdict. If the two models disagree, the escrow remains locked, and the code is not merged. This "checks and balances" system significantly increased the reliability of the autonomous merges.

---

## 4. Bridging the Terminal to the Physical World (Mock-Git)

Agents often live in a vacuum of text strings, making it hard to prove they are actually "doing" anything.  

- **The Challenge:** Making the agentic work tangible so that a user can see a bug actually being fixed in a real file.

- **The Solution:** We built a Simulation Sandbox (Mock-Git). We created a local directory structure (/repo, /prs) where the agents physically read and write .py files. We then built a Diff-View UI that pulls these physical files into the browser, allowing the user to see the "Before" (broken) and "After" (fixed) code side-by-side. This turned the abstract concept of "AI labor" into a visible, verifiable artifact.  

---

## 5. Managing 17 Concurrent Asynchronous Tasks

Running 1 Buyer, 1 Assessor, and 15 Sellers simultaneously created race conditions where agents would try to bid on the same task at the exact same millisecond.

- **The Challenge:** The database would occasionally lock, or agents would spam duplicate bids.

- **The Solution:** We implemented Jittered Polling and Stochastic Bidding. By giving each agent a random "thinking time" (e.g., 5–30 seconds) and a "Bid Probability" (e.g., Interns bid 90% of the time, Experts only 25%), we smoothed out the traffic. This created a more natural, human-like "market pulse" and ensured the SQLite database remained stable.

**Track: Checkout with Locus**

L-ESCROW uses Locus's checkout feature as the main superpower to make transactions and more importantly implement an escrow system. The ability to make agent-agent transactions without any clicks is the core of L-ESCROW. Not only a-to-a transactions but a person can budge in and make manual transactions just in a few clicks.

Team **Dione** -- Pranav Bhardwaj, [Shivalik Singh](https://github.com/XZNON)

`2026-04-30`

---

### RideTrue
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ridetrue-c7a5) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ridetrue.xyz) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/flaLfLaPMXk?si=Dq1X8Cy_EgIeOMZ0) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Transport

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

If you've ever taken a ride in Lagos or Kano, you know the drill. The driver names a price, you argue, someone backs down, and someone feels cheated. It happens every single day and everyone has just accepted it as normal.

RideTrue changes that. Before you get in the car, you see exactly what the route should cost, checked by an AI agent against real market rates. You pay in USDC and the money sits in escrow until you actually arrive. The driver gets paid the second you confirm. 

For drivers it's even simpler. Pay $0.20 once to activate your AI agent, connect your Locus wallet, and start accepting trips. When a passenger arrives and confirms, the money hits your wallet immediately. 

It works for passengers, it works for drivers, and it's built on Base blockchain so everything is transparent and instant.

**Challenges we ran into**

Buildwithlocus kept failing silently for days. No useful error messages, just "failed." Turned out the platform was defaulting to Node 18 which Next.js 16 doesn't support.

Getting the payment flow right was also tricky coordinating the Locus checkout session ID, saving the trip to the database at the right moment, and triggering driver payouts on arrival all had to happen in the right order.

**Track: Using BuildWithLocus to leverage our suite.**

RideTrue uses the Locus payment suite as the core of its entire 
payment infrastructure. Every passenger payment goes through a 
Locus checkout session where USDC is held in escrow on Base until 
the passenger confirms arrival. Drivers receive instant payouts 
directly to their Locus wallet the moment a trip is confirmed.

Driver onboarding also runs through Locus — every new driver pays 
a one-time $0.20 USDC activation fee via Locus checkout to get 
their AI agent set up.

The AI agent payment feature uses the Locus agent API endpoint 
directly, allowing programmatic payments without any human 
interaction — the agent hits the Locus checkout session endpoint 
and pays autonomously. This is the core of the agentic payments 
track we are building on.

SNOW HQ

`2026-04-23`

---

### Envoy Watch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/envoy-watch-8201) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YusufsDesigns/Envoy-Watch) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://envoy-watch.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/IcnWObWGXwk) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Every pull request, its own world.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem

Every development team that uses pull requests faces the same quiet crisis:
**shared staging environments**.

When multiple developers have open PRs at the same time, they all deploy to
the same staging server. PR #42 runs a database migration. PR #38 crashes
because the schema changed under it. Someone's feature works in isolation
but breaks everything when combined. The team argues about who "owns" staging
at any given moment.

The common workarounds are painful:
- Manually spinning up a cloud instance per branch (slow, expensive, forgotten)
- Taking turns deploying to staging (kills velocity)
- Skipping staging entirely and "testing in prod" (dangerous)

**Envoy Watch eliminates this problem entirely.**

Install the GitHub App on any repository. From that point:

- **Open a pull request** → Envoy Watch detects it within seconds and begins
  provisioning an isolated environment on Locus
- **Get a live URL** → A bot comment appears on the PR with a fully deployed,
  publicly accessible preview of your exact branch
- **Every PR is isolated** → its own container, its own URL, its own lifecycle.
  No shared state. No conflicts. No coordination required.
- **Merge or close the PR** → the environment is automatically destroyed.
  No cleanup. No lingering infra. No ongoing cost.

### Who benefits

- **Solo developers** reviewing their own work before merging
- **Small teams** where multiple features are in flight simultaneously
- **Open source maintainers** who want contributors to get live previews of
  their changes without giving them server access
- **QA engineers** who need a stable, isolated environment per feature for
  testing — not a constantly-changing shared server

### What makes it different

Most CI/CD preview environment tools are tied to specific platforms
(Vercel for Next.js, Netlify for static sites). Envoy Watch works with
**any language, any framework** — if Nixpacks can detect and build it,
Envoy Watch can deploy it. Node.js, Python, Go, Ruby — all supported
automatically, no Dockerfile required.

**Challenges we ran into**

## Challenges

### 1. The GitHub App private key formatting problem

The first real blocker: every attempt to authenticate with GitHub's API
failed with `ERR_OSSL_UNSUPPORTED`. The GitHub App private key is a
multi-line RSA PEM file. When stored as a Vercel environment variable,
the newlines get stripped, producing a malformed key that Node's crypto
module can't parse.

**Fix:** Base64-encode the entire PEM file before storing it:

```bash
cat private-key.pem | base64 -w 0
```

Then decode it at runtime before passing it to `createAppAuth`:

```typescript
privateKey: Buffer.from(process.env.GITHUB_APP_PRIVATE_KEY!, 'base64')
  .toString('utf-8')
```

One line. Two hours to find it.

---

### 2. Wrong Locus API endpoint — the beta/production split

Locus runs on separate environments: `paywithlocus.com` for the payment
wallet, `beta.paywithlocus.com` for beta accounts. The BuildWithLocus
deployment API lives on a *third* base URL: `beta-api.buildwithlocus.com`.

Every API call was returning `401 Unauthorized` because the code was hitting
`api.buildwithlocus.com` — the production endpoint — with a beta API key.

**Fix:** Read the skill.md carefully. The correct base URL for beta accounts is:
https://beta-api.buildwithlocus.com/v1

Lesson: when a platform has multiple environments, verify the base URL
against the environment your API key was issued for.

---

### 3. Locus deploying the wrong repo

During testing, Envoy Watch was installed on the Envoy Watch repository
itself. So when a test PR was opened, Locus tried to deploy... Envoy Watch.
Which requires environment variables Locus didn't have. Which caused
confusing build failures that had nothing to do with the code.

**Fix:** Use a separate, simple test repository — a minimal Express API
with a `/health` endpoint — specifically for triggering and validating
the preview environment flow.

---

### 4. Node.js version mismatch on Locus builds

Nixpacks auto-detected Node 18 from the repo. Next.js 15 requires Node 20+.
The build failed silently at the `npm run build` step with:
You are using Node.js 18.20.5. Node.js version ">=20.9.0" is required.

**Fix:** Add a `.nvmrc` file to the repo specifying `20`, and declare the
engine requirement in `package.json`:

```json
"engines": { "node": ">=20.9.0" }
```

Nixpacks reads `.nvmrc` and selects the correct version automatically.

---

### 5. Webhook timeout constraints

GitHub expects a `200 OK` response within 10 seconds of sending a webhook.
The Locus deployment process takes 3–7 minutes. Responding after the
deployment completes would cause GitHub to mark every webhook delivery as
failed.

**Fix:** Respond `200` to GitHub immediately, then run the deployment and
polling logic asynchronously using fire-and-forget:

```typescript
handlePROpened(ctx).catch(console.error)
return Response.json({ ok: true }) // returned immediately
```

The bot comment on the PR is the user's feedback mechanism — not the
webhook response.

**Track: Using BuildWithLocus to leverage our suite.**

## How Envoy Watch Uses Build With Locus

Envoy Watch is built **entirely around the BuildWithLocus API** as its
infrastructure layer. Locus is not an add-on — it *is* the product.
Without it, Envoy Watch is just a webhook receiver with nowhere to deploy.

### The core integration

Every preview environment is created with a single Locus API call:

```typescript
POST https://beta-api.buildwithlocus.com/v1/projects/from-repo
Authorization: Bearer <JWT>
{
  "name": "pr-42-user-my-app",
  "repo": "user/my-app",
  "branch": "feature/auth"
}
```

Locus handles everything from there: cloning the repo, auto-detecting the
framework via Nixpacks, building the Docker image, provisioning the container,
setting up routing and SSL, and returning a live URL at
`https://svc-{id}.buildwithlocus.com`.

### Teardown

When a PR closes, a single DELETE call removes the entire environment:

```typescript
DELETE https://beta-api.buildwithlocus.com/v1/projects/:projectId
```

Container, service, all associated resources — gone.

### Why this fits the track

The BuildWithLocus track challenges builders to use Locus as a
**deployment backbone** — not just a tool in the stack, but the
infrastructure primitive the product is built on.

Envoy Watch demonstrates exactly this:

- **AI/agent-native deployment:** The entire deployment lifecycle is
  orchestrated programmatically, with no human touching a cloud console.
  Envoy Watch acts as the agent — detecting events, making decisions, and
  calling Locus to execute.

- **Pay-per-use infrastructure:** Each environment costs $0.25 and exists
  only as long as the PR is open. This ephemeral, pay-per-use model is
  precisely what Locus's pricing is designed for — and what makes
  per-PR environments economically viable where traditional cloud
  infrastructure would be too expensive.

- **API-first, no DevOps:** Repositories deploy without Dockerfiles,
  without cloud accounts, without any configuration from the end user.
  Locus's Nixpacks auto-detection handles the build. This is the
  "no DevOps required" promise of BuildWithLocus in practice.

- **Real workflow problem:** Preview environments are a genuine pain point
  for every development team. Envoy Watch makes Locus the solution to a
  problem developers face daily — demonstrating practical, real-world
  utility beyond a demo.

### Production architecture note

For the hackathon, environments deploy from the platform owner's Locus
wallet. The production architecture routes each GitHub App installation
to the user's own Locus API key — so deployments bill against their
account, enabling a true multi-tenant model built on top of Locus.

[Yusuf Lawal](https://github.com/YusufsDesigns)

`2026-04-22`

---

### PocketQuant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quantify-5695) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1183626838) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Model Builder (Powered by Locus)

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Sick of AI hallucinating data analytics? 

Expensive datasets, analytics, and news articles?

Need dynamic outputs suited to your needs?

Something relevant TODAY with actual use cases instead of trivial agent task assignments, or a mindless idea generated by AI?

As a quantative developer I ask myself the same things!

**PocketQuant** is an autonomous financial research agent that transforms complex investment analysis into instant, actionable reports. Powered by real market data, AI and **LOCUS**.

**NO hallucinations, data is run through financial models with real data instead of direct AI**

**Dynamic, personalized outputs**

**Real time cost reporting**

**Context providing**

**Source citing**


Watch our demo video and slides to see what we mean!


**The Problem**
Serious financial analysis is expensive and slow. A Bloomberg terminal costs $24,000/year. Hiring a quant analyst costs even more. Retail investors and small funds are left making decisions with incomplete information, while the tools that could help them are locked behind institutional paywalls.


**What PocketQuant Does**
PocketQuant lets anyone run institutional grade financial research in plain English, paying only for the data they actually use, in fractions of a cent per query.

**Why It's Different**
Every analysis is powered by real, freshly fetched market data, not stale snapshots or hallucinated numbers. The on-chain payment model means you pay $0.02 for a query, not $2,000/month for a subscription you'll only use twice.

**Ask it anything:**

- "Run a Bollinger Band analysis on Apple and identify breakout signals"
- "Simulate 500 Monte Carlo paths for Tesla over the next 30 days"
- "Build a DCF valuation for Microsoft with bear, base, and bull scenarios"
- "Analyze how an oil supply disruption in the Strait of Hormuz would impact energy stocks"

**How it Works**

5 Agents, each specialized 

![image](https://assets.devfolio.co/content/df517d0ae9e246248301ffe9b9428f8e/fcd8730d-0c51-4672-a2e6-f8e95b657d88.png)

1. Strategist
Takes your plain English query and decides:

What type of analysis to run (Bollinger Bands, Monte Carlo, DCF, etc.)
Which tickers are involved
Exactly which datasets are needed

2. Procurement Agent

Calls **LOCUS** APIs to fetch real market data (Alpha Vantage + Exa)
Pays for each dataset on-chain with USDC
Saves data locally as CSV/JSON files for the next stage
Only fetches what the Strategist asked for — nothing more

3. Code Writer

Receives the data file paths and analysis instructions
Generates a custom Python script to perform the analysis
Script is tailored to the exact model type (event study, Monte Carlo, etc.)

4. Code Executor

Runs the generated Python script in a subprocess
Captures the JSON output (returns, volatilities, projections, etc.)
If it crashes, sends the error back to the Code Writer for one auto-fix attempt

5. Output Manager

Receives the computed results
Writes a polished prose research report
Generates Plotly chart specifications from the real computed data
Returns everything as structured JSON to the frontend

**Challenges we ran into**

**The Model That Wouldn't Stop Thinking**

The biggest headache was getting the Code Writer agent to actually output Python code instead of reasoning through the problem out loud. Gemini 2.5 Flash Lite has extended thinking enabled by default, so when asked to write a financial analysis script, it would spend thousands of tokens planning, outlining, and explaining before producing any code. By the time it finished thinking, it would either timeout or output JSON analysis instead of a Python script.
The fix was prefix forcing, instead of asking the model to "write a Python script", we give it the first half of the script already written (imports, helper functions, file comments) and ask it to complete it. A model mid-code has no choice but to keep writing code. We also added a boilerplate injection step that automatically prepends import pandas as pd and the _clean() function if the model forgot them.

**Using PayWithLocus.com to leverage our suite.**

How Locus Was Used
PocketQuant uses Locus as its on-chain data payment layer,  every piece of market data the agent fetches is paid for in real USDC, creating a transparent and auditable trail of exactly what data was used and what it cost.

What Locus Wraps
Locus acts as a middleware between PocketQuant and the underlying data providers:

Alpha Vantage — stock prices (OHLCV), technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands), financial statements (income statement, balance sheet, cash flow), news sentiment, commodity prices (WTI crude oil), and economic indicators (GDP)
Exa — neural web search for recent news articles and financial coverage about any ticker

Without Locus, accessing these APIs would require separate accounts, API keys, and billing relationships with each provider. Locus consolidates them behind a single authenticated endpoint with per-call USDC micropayments.

Mark Gaisor

`2026-04-16`

---

### Whisper
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/whisper-7af1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Michael-Nwachukwu/whisper) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/f9f04c902bed41cb8342ed32f4227ef8) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/f9f04c902bed41cb8342ed32f4227ef8) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The web has a price. Whisper pays it

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-333333?style=flat-square)

**The problem it solves**

Every time you hit a checkout page, a paywall, or a payment request while browsing, the browser stops. It can render the page and display the price, but paying is entirely your problem. Find your card, type the numbers, fill the form. Even worse you're on a page that accepts only card payments and all you have is crypto. It can be a pain in the ass.                           
                                                                                                                                 
Whisper gives the browser a wallet.                                                                                        
                                                                                                                                 
It runs as a silent AI agent inside Chrome. When you encounter any payment surface while browsing, Whisper recognises it, settles it in USDC, and lets you continue — without switching tabs, entering card details, or breaking your flow.                                               
                                                                                                                                 
What people can use it for:                                                                                           

1. Frictionless checkout — land on any Locus-integrated merchant page and pay                                               
    instantly with one click. No card form, no redirect, no friction. 

2. Card checkout on any site — on standard card checkout pages, Whisper generates a virtual debit card and autofills the form. The user just reviews and submits.
                                                                                                                                 
3. Crypto-native payments — on pages that display a wallet address and USDC amount, Whisper reads the address from the DOM and sends the payment directly.                                                       
                                                                                                                                 
 4. x402 micropayments — for APIs and content that return HTTP 402 Payment Required, Whisper intercepts the request at the browser's `fetch` level, settles the payment on-chain and retries automatically. The page receives a 200. The user never sees a paywall.                                                                                                                     
                                                                                                                                 
5. Natural language control — users can type commands in the side panel ("pay for                                           
    this", "what's the total?", "is this page safe?") and the AI agent acts on them.                                             
                                                                                                                                 
6. The same extension works across all four payment surfaces. One wallet, any checkout, every site.

**Challenges we ran into**

**1. The "transaction does not belong to this agent" wall**

  The most frustrating bug of the build. After wiring up the full Locus Checkout flow — preflight, pay, poll — every payment came back with a 403: *"Transaction does not belong to this agent."*.

The root cause: I was using a single API key for both creating the checkout session
  *and* paying it. That meant the payer and the payee were the same wallet — Locus correctly rejects a wallet paying itself. The fix was a two-key architecture: one key owns the merchant session, a separate key is the paying agent. Once we split them, the payments went through cleanly.

A second wrinkle: even with separate keys, `GET /checkout/agent/payments/:txId` kept returning 403 on the beta environment. The money was actually moving (I could see the balance change on the merchant wallet) but the polling endpoint kept rejecting. I worked around it by polling `GET /checkout/sessions/:sessionId` instead, which returns `PAID` status and the real on-chain `paymentTxHash` once confirmed, thanks to the /ask ai bot on Locus discord.

**2. The x402 MAIN world injection problem**

The x402 interception requires wrapping `window.fetch` before any page code runs. In Manifest V3, content scripts run in an isolated JavaScript world — they can't touch `window.fetch` on the actual page. Our first attempt injected a `<script>` tag from the content script, but Chrome's CSP headers on many sites blocked it, and `window.__whisperPresent` was never being set reliably.

The correct solution was declaring a second content script in `manifest.json` with `"world": "MAIN"` and `"run_at": "document_start"`. This runs before any page
  JavaScript, wraps `window.fetch` natively, and communicates back to the isolated content script via `window.postMessage`. Clean, reliable, and CSP-safe.

**3. Session detection race condition**

The merchant checkout page creates a Locus session dynamically on load — the meta tag starts empty and gets populated after an API call. Whisper's content script was classifying the page before the session was ready, caching a null session ID, and then the button click would fail with "No session found."

The fix was two-part: fire a locus:session-ready custom event from the page once the session is created, and more importantly, read the session ID fresh from the DOM at click time rather than from the cached classification object. The DOM is always current. The classification cache is not.

**Using PayWithLocus.com to leverage our suite.**

Whisper is built entirely on the Locus payment infrastructure and demonstrates the full breadth of what the Locus suite enables.

**1. Locus Checkout SDK** is the primary payment rail. When a user lands on a Locus-integrated merchant page, Whisper calls the agent preflight and pay endpoints directly — no card, no wallet connect UI. This is the core of the Locus agent payment vision: a software agent that can complete a checkout autonomously on a user's behalf.

**2. Laso Finance** powers the virtual card flow. For standard card checkout pages on any site — not just Locus merchants — Whisper calls the Laso card generation API, receives
  a single-use virtual debit card, and autofills it into the form. This extends Locus reach to the entire web, not just Locus-integrated merchants.

**3. Locus /pay/send** powers direct USDC transfers for crypto checkout pages and x402 micropayment settlement. Any page that shows a wallet address and an amount, or any API that returns HTTP 402, gets settled through the Locus payment API.

The broader argument: Locus provides the payment primitives — checkout sessions, virtual cards, USDC transfers. Whisper is the UX layer that makes those primitives available everywhere, on any page, without any merchant needing to do anything differently. It turns the Locus suite into a universal browser payment agent.

If Locus is the payment rail, Whisper is the train that runs on it — automatically, silently, and on every track.

Team **Whisper-team** -- [Michael Nwachukwu](https://github.com/Michael-Nwachukwu)

`2026-04-15`

---

### ProcureBot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/procurebot-0432) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NeelShah1505/ProcureBot) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://procure-bot-one.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/CGu26FpdlVI?si=p6vFFcr_sDanYbPc) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The autonomous AI procurement agent.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square)

**The problem it solves**

AI agents today are trapped behind human billing walls. If an agent needs live data or an image generation API, a developer has to manually sign up, submit a credit card, and manage subscription keys. I realized that true autonomous agents shouldn't need a human to type in a credit card number just to do their job.

ProcureBot is the first AI agent that autonomously buys the data it needs. Using the Locus Machine Payments Protocol on Base, it pays for APIs per request using real USDC. Let me break down how it changes the game:

• Subscription Free Autonomy
When I ask ProcureBot for live market data or web research, my Groq powered router finds the best API provider and authorizes the exact micro payment needed, usually just a fraction of a cent. 

• Seamless Chat Execution
The agent handles the entire procurement cycle natively on chain and delivers the data, generated images, and research summaries directly inline in the chat interface.

• BuiltIn Safety Controls
To ensure the agent never overspends, I built a live policy panel. I can set custom daily caps and per transaction limits, keeping my wallet completely secure while the agent operates independently. 

I built ProcureBot to demonstrate what the future of machine economy looks like: decentralized, entirely autonomous, and running on actual micro payments instead of credit cards.

**Challenges we ran into**

Bridging an AI language model with live, on chain micro payments meant solving several complex UX and data flow problems:

• Hiding Blockchain Latency
Waiting five seconds for a blockchain approval breaks the illusion of a fast chat assistant. By using Locus on Base, I secured near instant approvals. I also built a cascading "thinking steps" UI that updates live as the agent routes, pays, and fetches, making the wait feel natural and instantaneous. 

• Smart Routing at High Speed
I initially struggled to get the agent to reliably select the right API from an unpredictable user prompt. I switched my routing engine to Groq using Llama 3 for its sheer speed, and heavily refined the system prompt until it could accurately extract parameters and hit the right endpoints every time. 

• Image Rendering Crashes
When ProcureBot successfully bought an image from OpenAI, the massive Base64 string data frequently crashed my React chat renderer. I fixed this by writing a custom data interceptor on the backend that wraps the heavy image data in a specialized tag, which my frontend parses and safely swaps into a clean image element.

• Seamless State Synchronization
Keeping the dashboard feeling alive was a major hurdle. I had to architect a localized state system where the user's USDC balance on Base, their active spending policies, and their live receipt feed all updated smoothly and instantaneously the moment a micro payment executed, completely avoiding any clunky page reloads.

[Neel Shah](https://github.com/NeelShah1505)

`2026-04-14`

---

### Dispatch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dispatch-aa49) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/cass-agency/dispatch/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mnz0zcnpbg4wdjde.buildwithlocus.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LpIFUqg9lig) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The Autonomous Premium News Agency

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Everyone is building AI Coding teams and bug hunters, I still see an underdeveloped branch of actual good quality video content created by AI (I dont mean the subway surfer AI slop for doomscrolling)

But for such a thing to exist, we NEED a verifiable pipeline, and an easy interface for people to interact with it.

That is exactly what Dispatch does. 

One sentence is enough for the orchestration to go through research, script writting, media creation, voiceover, music, and editing.

Everything is verifiable, outputs are streamed within the website, agents are collaborating with one another within the budget range they have, in case an agent would error out due to running out of money, he will tell it to the others and they can fund him.

**Challenges we ran into**

The `GET /commission/:id` endpoint returned the free `watchToken` when the commission was
  done. Anyone who shared the URL (which contained the commission ID) gave away their video
  for free. We moved the token behind a one-time `POST /commission/:id/claim-watch` endpoint
  that returns the token once and then nulls it. Subsequent calls get 409. The commissioner's
  browser claims it on first poll; incognito visitors hit the pay gate.


Additionally, since I really needed multiple agents powered by Locus API Keys, I had hoped I would be able to create multiple wallets and API keys within my PWC account, but due to it not being possible, I created 5 additional PWC Accounts. I named them just like my main, only with a number at the end, and used alias email addresses so its simple to navigate which accounts belong to me.

Aside from that everything with the Locus products has been smooth sailing, skill files working great and teaching my NanoClaw as well as my Claude Code how to operate the platforms.

**Using PayWithLocus.com to leverage our suite.**

Its the cornerstone of everything.

Every agent within the pipeline is pretty much just a PayWithLocus API key and thus a wallet, each with dedicated Locus Wrapped endpoints they are guided to call. each powered by Claude Haiku for the orchestration of their own task within the pipeline, as well as communication with one another through the council.

Customers that commision a video either exclusively for themselves, or to get the revenue sharing and public visibility on the page, both go through the PayWithLocus payment gate

Viewers of the videos only get a 10-second preview, before a PayWithLocus payment gate appears for them.

Deployed on BuildWithLocus, Using PayWithLocus on every API call within the app.

[Kilian Valdman](https://github.com/forever8896)

`2026-04-16`

---

### Aether
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aether-18da) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ayushkumar2601/locus_ayush) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.notion.so/AETHER-Locus-Paygentic-Week-1-344d9dc0765c80bc9a20c55a68b0d842?source=copy_link) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Think less. Compute more. Automatically.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Modern compute workflows are fragmented and inefficient. Users must manually search for compute providers, compare pricing and performance, manage execution environments, and handle payments separately. This process is time-consuming, error-prone, and requires technical expertise.

Aether simplifies this by introducing an **AI agent-driven compute marketplace**. Instead of manually selecting resources, users simply specify their task, and the AI agent automatically chooses the most suitable provider based on cost, performance, and availability. It then executes the job and handles payments seamlessly using micro-transactions.

This makes compute:
- **Faster**: No manual decision-making or setup required  
- **Safer**: Budget-controlled micro-payments prevent overspending  
- **Smarter**: AI optimizes provider selection dynamically  
- **Accessible**: Even non-technical users can run complex tasks  

Aether effectively turns compute into a **one-click, autonomous experience**, reducing friction and enabling efficient resource utilization.

**Challenges we ran into**

One of the biggest challenges was integrating real-time payments with the execution pipeline. Ensuring that payments, job execution, and result retrieval happened reliably without breaking the flow was complex, especially when dealing with external APIs like Locus.

Another major hurdle was handling TypeScript errors across a multi-service architecture (frontend, backend, and node service). Strict typing caused frequent build failures, particularly with nullable data and mismatched interfaces. To overcome this, I introduced safer fallback patterns and relaxed strictness where necessary to prioritize stability.

Deployment constraints also posed a challenge. Running a fully distributed system (backend + node + database) wasn’t feasible within limited time, so I adapted the architecture into a **frontend-heavy simulation model** while keeping payments real. This ensured a smooth, demo-ready experience without failures.

Overall, the key learning was balancing **real functionality with controlled fallbacks** to create a reliable and impressive system under time constraints.

**Using PayWithLocus.com to leverage our suite.**

Aether deeply integrates **PayWithLocus** to enable real-time, micro-payment-based compute execution. Instead of traditional billing systems or subscriptions, every compute task in Aether is tied to a **live USDC transaction**, making payments transparent, granular, and efficient.

When a user runs a task, the system automatically triggers a **Locus payment API call**, transferring a small amount (e.g., $0.005 USDC) as part of the execution flow. This demonstrates how Locus can be used to power **agent-driven economies**, where AI systems can autonomously make payments for services.

By leveraging PayWithLocus:
- We enable **instant, low-cost micro-transactions** for compute usage  
- We showcase **real-world API integration in a live system**  
- We demonstrate how **AI agents can initiate and manage payments autonomously**  
- We eliminate the need for complex billing systems or manual payment handling  

This project highlights the potential of Locus in building **decentralized, programmable payment layers** for next-generation AI and cloud infrastructure systems.

[AYUSH KUMAR](https://github.com/ayushkumar2601)

`2026-04-16`

---

### PayCrypta App
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/paycrypta-app-903f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NSHM-Hackers/PayCrypta-CodeForChange2.0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://paycrypta.rahulraman.in/) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> A payment app + gateway

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Our goal with this project is to create a **Payment App + Gateway** that will be completely *transparent about the exchange and the charges the user has to pay*.
It will also feature an easy-to-use UI.

**Challenges we ran into**

First, we had some friction implementing JWT authentication in the backend. We also faced challenges on where to deploy our app and make it securely available over the internet.
And lastly, another challenge was how to get the license, this is a big issue when doing the international payments, in sending the money from one country to another, the solution is that we have to make a partnership with RBI-Authorized Entities to get the license for the currency exchange services, for which they will apply their own additional charges and fees on the currency exchange which we will analyze and calculate how much they are charging per different currency conversion and then add a fees range to our frontend to show the users more closely how much they are actually paying.

Alternatively, we can forego the intermediary banks by using a whole different core idea of processing the payment. In this new idea, we would as a company/service_provider/payment_processor use cryptocurrency for fast & low-cost transfer of money. First in this alternative approach, when a user/client places an order or purchases something or sends money over to someone else through us, we will collect their money and then buy a cryptocurrency with equivalent amount to the transaction amount like XRP (XRP has a very low network transaction cost) and then since cryptocurrencies are decentralized and global we can with low cost at the recipient's side sell the value back into fiat currency that the recipient wants. In this scenario, the payer will only have to pay two charges one is 1% of the total transaction amount as TDS (tax deducted at source) which we will collect from user and send to the government, and the second charge will be our service fee we will charge for our profit (we have to pay the standard 18% GST on our service fee since it is our income), and those two charges plus the original transaction amount will be the final payment made by the sender, and since if we use XRP as intermediary coin there won't be high network charges therefore we can still charge low service fees and still make profit. The user will in this case have complete transparency of all the amount and charges they will pay and what the other party will receive since there are no intermediaries involved. There is another part that concerns taxes for our company here that if from the time of buying the XRP and selling it on the recipient's side if we made an unintentional profit on the XRP if its value increases during the transaction, we will have to pay 30% of that profit plus cess and surcharge to the government which would still only leave us with more profits than before. This approach will be more suitable when dealing with large amounts as well as small amounts. The biggest challenge in this approach will be that we aside from registering with the FIU_IND (Financial Intelligence Unit — India) to act in accordance with the Prevention of Money Laundry Act we will have to have a starting net-worth of Rs.15 crores to be able to register as a payment processor using using XRP which is a VDA (Virtual Digital Asset). But aside from that, if it can be started and we get a good userbase using our system, then there are no other challenges as the nature of our system makes the operating fees for processing a transaction very low when using decentralized cryptocurrency when compared to using government-authorised dealers for direct fiat currency transfers.

Team **PayCrypta** -- [Anik Gupta](https://github.com/Anikkumar234), [Sumana Mondal](https://github.com/Sumana0810), [Debolina Dutta](https://github.com/debolinadutta213), [Rahul Raman](github.com/rahulraman0108)

`2026-04-11`

---

### TradeSquad
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tradesquad-9f79) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Axelzx8902/TradeSquad) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tradesquad.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-powered Gamified stock ED-Tech Simulator

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

The problem we are addressing is that most beginners in the stock market lose money not because they lack information, but because they make poor decisions driven by emotions and news hype.

To solve this, we built TradeSquad — an interactive platform that trains users to think before they trade.

Users can explore real market data through candlestick charts and financial news.What differentiates us from platforms like Zerodha or TradingView is that they focus on executing trades, while we focus on training decision-making. We provide a risk-free environment and guide users through structured scenarios instead of just showing raw data.

Additionally, unlike paper trading platforms, which focus on profit and loss, TradeSquad focuses on understanding the reasoning behind decisions. We analyze user behavior and provide feedback on patterns such as reacting emotionally to news or following hype.

**Challenges we ran into**

The biggest bug i faced was not being able to properly integrate finance APIs
due to the event being organized on a Sunday and the financial stock market being closed on that day😂😂

**Main Track: The Deepforge Arena**

I just survived an insane all-nighter at Hackmol 7.0 to build and launch TradeSquad. I knew I was in the freshers track, but I didn't want to just build a basic beginner web page. Instead, I built a fully decoupled, production-ready app. I set up a React and Vite frontend, a Python and FastAPI backend, and linked it all to a Supabase database. The core feature is a Gemini-powered AI coach that reads live financial data from the Finnhub API and actually "roasts" the user's trading decisions in real-time. The final few hours were an absolute deployment gauntlet—I had to figure out how to host the UI on Netlify, spin up the backend on Render, and debug some brutal CORS middleware errors on the fly just to get them communicating securely. Now, at 7:00 AM, I have a fully live, AI-integrated product. I’m pitching in the freshers track, but with this architecture, I know I'm bringing a project that can go toe-to-toe with the veterans in the main competition.

**Fresher’s Track: The Rising Lanterns**

I just pulled an intense all-nighter at the Hackmol 7.0 hackathon to build and launch TradeSquad, a gamified stock trading simulator featuring a brutally honest, Gemini-powered AI coach. Right down to the 7:00 AM wire, I engineered a fully decoupled full-stack application, building the frontend with React and Vite and the backend with Python and FastAPI. The final stretch was an absolute gauntlet of live deployment challenges—I successfully hosted the UI on Netlify, spun up the backend on Render, and debugged tricky CORS middleware issues on the fly to get both platforms communicating securely. Despite the exhaustion, I’m walking into the freshers track presentation with a robust, real-time, AI-integrated product that punches well above its weight class.

Team **PurplePiglets** -- [Aditya Ashish Gupta](https://github.com/Axelzx8902)

`2026-03-29`

---

### CogniVest
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cognivest-948c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SparkleYR/CogniVest-public) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uRvAOlcYZhM?si=To8dXc00fvLkVg1s) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Bringing emotions to finance

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![chromadb](https://img.shields.io/badge/chromadb-333333?style=flat-square)

**The problem it solves**

We built a complete psycho and emotional profile of a client which can be used by a Portfolio manager to predict the emotional state of a client to any given scenario.

**Challenges we ran into**

We had to build a RAG system from scratch with a vector database that also ingests mathematical finance data from multiple agentic systems working together to create a holistic emotional agent that can accurately simulate the client.

**FinTech**

Built a RAG system from scratch with a vector database that also ingests mathematical finance data from multiple agentic systems working together to create a holistic emotional agent that can accurately simulate the client.

Team **QuantForge** -- [Ayoosh Iyer](https://github.com/ayoosh007), [Shreya Singla](https://github.com/shreya2070), [Madhav Khurana](https://github.com/madhavsk-programs), [Yash Raj](github.com/SparkleYR)

`2026-03-29`

---

### compliance.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/complianceai-0a50) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fincortex-gh6b.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Tax Savings & Seamless GST Compliance

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Nodemailer](https://img.shields.io/badge/Nodemailer-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Fincortex: The Problem It Solves
Fincortex (or Compliance Pilot) is an AI-powered financial management and tax optimization platform designed primarily for small and medium-sized businesses (SMBs) and their financial advisors (CAs). It bridges the gap between complex tax regulations and daily business operations.

🛡️ The Problem It Solves
Running a business requires navigating a minefield of financial compliance, where mistakes are expensive and opportunities are easily missed:

GST Complexity: Understanding Input Tax Credit (ITC) eligibility, fluctuating tax rates, and complex GST schemes is a massive burden for non-experts.
Invisible Financial Errors: Manual invoice processing often leads to mismatched tax amounts, incorrect GSTINs, or currency inconsistencies that trigger audits or penalties.
Lost Savings: Millions of rupees in legitimate tax savings go unclaimed every year because businesses don't realize their expenses or assets qualify for specific deductions.
Fragmented Collaboration: Communicating financial issues to a Chartered Accountant (CA) usually involves messy email threads or WhatsApp messages, leading to delays and missed deadlines.
🚀 How It Makes Tasks Easier & Safer
1. Automated Invoice Auditing
Instead of manually verifying every line item, Fincortex uses AI to instantly scan uploaded invoices. It identifies:

Tax Mismatches: Detects if the tax calculated exceeds the actual amount due.
Compliance Risks: Flags suspicious vendors or inconsistent data with a "Risk Score."
Data Integrity: Automatically catches currency inconsistencies and mixed tax rates.
2. Proactive Tax Saving Engine
The platform doesn't just store data; it analyzes it. It cross-references your expenses, assets, and payroll against current tax rules to provide:

Actionable Tax Tips: Proactive suggestions for claiming ITC or optimizing GST outflows.
Estimated Savings: Displays clear, real-time calculations of potential savings in INR.
Priority Ranking: Help you focus on high-impact savings first.
3. Streamlined CA Collaboration
Fincortex turns "I think there's a problem" into structure. With one click, users can "Flag to CA" a specific invoice error or tax recommendation. This ensures the tax advisor sees the exact context, explanation, and document needed to take action.

4. Compliance Safety Net
Smart Reminders: Automated, frequency-based (monthly/quarterly) tax filing reminders ensure you never miss a deadline.
Centralized Asset & Expense Tracking: Maintains a "source of truth" for machinery, equipment, and employee costs, ensuring the business is always audit-ready.

**Challenges we ran into**

🔄 1. The Great Migration: Supabase to Firebase
One of the biggest hurdles was pivoting the backend architecture from Supabase to Firebase halfway through development.

The Challenge: We had already established a schema in Prisma (PostgreSQL) but needed to integrate Firebase for Storage (invoice images) and Authentication. Maintaining a "source of truth" across two different ecosystems (Prisma/SQL for logic, Firebase for unstructured data) was difficult.
The Solution: We decoupled the database logic using a Service Layer. We moved image processing to Firebase Storage first, then stored the resulting URLs and hashes in the PostgreSQL/Prisma database. This gave us the speed of Firebase for files and the relational power of Prisma for complex tax calculations.
🧩 2. The "Types" Module Resolution Mystery
A recurring issue was a TypeScript error: Cannot find module './types' or its corresponding type declarations in the invoiceStore and API routes.

The Challenge: In a Next.js App Router environment, relative pathing for shared types can become brittle if the 

tsconfig.json
 isn't perfectly aligned with the folder structure.
The Solution: Instead of relying on fragile relative paths (../../types), we implemented TypeScript Path Aliases. By defining @/types/* in 

tsconfig.json
, we created a centralized type registry that was accessible globally across both components and API routes.
🛡️ 3. Backend vs. Frontend Boundary Leaks
The Challenge: While building the 

TaxSavingEngine
, we accidentally included React-specific logic (like useContext or browser hooks) inside Next.js API routes. This caused build-time errors because the server tried to execute client-side code during static analysis.
The Solution: We strictly enforced a Service-Oriented Architecture. We moved all "heavy lifting" (the actual tax calculation logic) into a services/ directory that has zero dependencies on React. Our API routes now act as thin wrappers that call these pure JavaScript/TypeScript services.
📧 4. Automating the "Un-automatable" (SMTP Secrets)
The Challenge: Setting up the automated tax reminder system required manual input of SMTP secrets for testing, which broke the "hands-off" developer experience we wanted.
The Solution: We switched to a Dual-Mode Email System. For development and testing, we integrated Ethereal/Nodemailer with auto-generated test accounts. For production, we moved to Resend/Brevo, using environment variable injection during the CI/CD pipeline so no manual secrets are ever needed in the codebase or UI.
🤖 5. Mapping AI Logic to Prisma Models
The Challenge: Converting the AI's "recommendations" (which are often vague) into structured TaxRecommendation records in Prisma required a complex mapping layer.
The Solution: We implemented a "Trigger & Rule" system. Instead of the AI creating records directly, it flags a rule_code. A background service then fetches the latest TaxRule from the database and marries it with the AI's explanation before saving it, ensuring data integrity and consistency.

Team **FinCortex** -- [Bhuvan kumar shetty h](https://github.com/bkshetty), [Yuvaraj Khot](https://github.com/Yuvaraj108-khot), [Yashwanth Shetty](https://github.com/YashwanthShetty15), [Vaishakh Bangera](https://github.com/VAISHAKHBANGERA)

`2026-03-15`

---

### slinky
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lolsss-e669) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hamzaskewl/slinky) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://slinky-production.up.railway.app/#) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=n0PHqvcUyos) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Private Payment Links on Canton

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The problem slinky solves is that it makes claiming/redeeming and using tokens easier for people while allowing them to remain fully anonymous using the Daml contracts that we wrote and are able to be used on the site currently. The combination of making payments easier with just a link that leaks nothing, does not save to a database of any sort and keeps trust in the sender, it positions us to be in a great position for making payments easier, and more private.

**Challenges we ran into**

We ran into challenges during the implementation of canton's daml contracts and we made sure to adhere to the guidelines. We used the hackathon guidelines and had to go and talk to the devs at the canton booth about the issues, we got it fixed and were able to work on it later, although we were not able to fully deploy it to devnet, we got really close and I managed to make it still work on a live demo link with the sandbox canton ledger on the website, running just as similarly to how a devnet would on the Canton Network.

**Use of AI tools and agents**

We used Claude Code for helping with the codebase, but there are no agents or any integration of that sort to the actual project.

**Prosperia**

slinky is a product that aligns itself with making payments easier by using claim links as leverage and canton networks designed privacy and contract design in Daml, this track is about privacy, and we fit most into it overall compared to other tracks. Most privacy solutions in crypto are add-ons layered onto public ledgers. Slinky takes the opposite approach: Canton was built for privacy from day one, and we built a product that leans into that entirely. The result is a payment flow that is both simpler and more private than anything possible on a public chain.

**Best Privacy-Focused dApp Using Daml**

We implemented privacy using canton by enforcing it structurally by the Daml contract templates and Canton's sub transaction privacy. There are 4 Daml templates, for the ClaimLink, ClaimReceipt, ClaimNotification, RevokedLink, these privacy sensitive fields are absent from contracts visible to the other party. Canton's synchronization protocol ensures each participant only sees sub-views of transactions where they are a stakeholder. Our claim link once creator has the Daml contract ID attached to its end as an opaque bearer token with zero metadata about the sender, amount, or any party. The way this is built is only able to be built on canton using its infrastructure.

Team **UTHack** -- [Aaron Solanki](https://github.com/aaroncoder1), [Hamza Dag](https://github.com/hamzaskewl), [Braeden Gradwell](https://github.com/braedengradwell-ui)

`2026-02-21`

---

### FinanceQuest
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/financequest-0087) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mohatamegha/FinanceQuest) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://finance-quest-sandy.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Don't let your money sit idle, get it rolling!

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

I would like to tell you the reason why we chose this project. We conducted a study in our class, through which we understood that only 7% of the people were investing, which was a really striking figure for us.
Now, we all know that engineers start earning at around the ages of 21–22, as compared to a CA, who starts earning at around 24, or a doctor, who starts earning at around 26–27. This helped us understand that there is a huge gap between the people who are earning and the people who are investing.
The current inflation rate in India hovers at around 6.33%, so basically, if we are not investing our money, we are practically losing money instead of gaining it. This is exactly the gap that our app is trying to bridge.
And as Warren Buffet says "The way to become wealthier is not by working for more money, but making your money work for you".
So, we present Finance Quest to you. It is a centralised, gamified learning platform targeted at engineering students, particularly women, to encourage them to start investing at a very young age by explaining financial jargon in layman’s terms.
It is a platform designed not only to explain the fundamentals of finance but also budgeting and saving, thereby providing a holistic understanding of various financial domains.

**Challenges we ran into**

1. Breaking down complex financial jargon into layman terms
Problem:
Financial concepts are often intimidating for beginners due to heavy jargon and abstract terminology, which can discourage first-time learners.

Solution:
We simplified complex terms by:
Replacing technical language with everyday analogies (e.g., SIP as “monthly saving like a subscription”)

Using short explanations instead of definitions

Presenting concepts through gameplay, choices, and examples rather than long text blocks

Impact:
Users can understand financial concepts intuitively without feeling overwhelmed, making learning more approachable and confidence-building.

2. Managing conflicting dependencies (Tailwind v4 vs shadcn)
Problem:
Tailwind v4 introduced breaking changes that conflicted with shadcn UI components, causing styling inconsistencies and build errors.

Solution:
We resolved this by:
Standardizing the setup to a stable Tailwind configuration
Cleaning up conflicting PostCSS and Tailwind directives
Rebuilding the styling layer from scratch again in 5 long hours!

3. Designing an engaging, clean, and beginner-friendly UI
Problem:
Finance apps often overwhelm users with dense dashboards and too much information at once.

Solution:
We designed the UI with:
a) Clear visual hierarchy and focused screens
b) Minimalist layouts with progressive disclosure of information
c) Gamified elements like XP, progress bars, and rewards to keep users engaged

4. Identifying the most important features and information
Problem:
It was challenging to decide what information is essential for beginners versus what could distract or confuse them.

Solution:
1. Core financial fundamentals first (budgeting, saving, investing basics)
2. Learning-by-doing through simulations and challenges

5. Time Constraint 
Problem: It was difficult to make ends meet in the limited amount of time when everything kept breaking. 
Solution: Late nights and sleep deprived days powered by caffeine (hehe)

Team **404 Chill Not Found** -- [Megha Mohata](https://github.com/mohatamegha), [Simran Dureja](https://github.com/simrandureja03-source), [Tanya Gupta](https://github.com/Tanya-Gupta23)

`2026-02-08`

---

### Budgetly
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/budgetly-4c29) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1H28mv0azoZaRRyS-Vr1egptGyhvqXJGK?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JnzN9Yd2aJE?si=YfDZRcDsv8k2TBZb) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Hostel Life Finance Manager

![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square)

**The problem it solves**

Centralizes all financial activities : budgeting, expense tracking, subscriptions, and shared expenses, into one platform

Provides visual insights that help students instantly understand spending patterns

Automates recurring expenses for more realistic and stress-free budgeting

Simplifies expense splitting, reducing misunderstandings among peers

Integrates college & hostel information, saving time and reducing dependency on multiple apps

Educates students through Money Buddy, empowering smarter financial decisions

**Challenges we ran into**

One major challenge was balancing multiple features, budgeting, expense tracking, shared expenses, subscriptions, and college utilities,without overwhelming the user.

How we solved it:
We restructured the app into clear tabs and dashboards, prioritizing the most-used features upfront and pushing secondary utilities into dedicated sections. This ensured usability without sacrificing functionality.

**Hostel Life Utility Manager - UI/UX Beginner Track (Freshers Only)**

Our project focuses on solving everyday hostel-life problems through a simple and intuitive user experience, making it well-suited for the UI/UX Beginner Track.

The app is designed with freshers in mind, using clear navigation, minimal input flows, and visual dashboards that make budgeting and expense tracking easy to understand. Key hostel utilities and college information are placed in one accessible space, reducing the need to switch between multiple apps.

By prioritizing clarity, usability, and real student needs, the project demonstrates how thoughtful UI/UX design can simplify hostel life.

Team **ThinkSync** -- [Bhumika Soam](https://github.com/bhumika-soam), [Mahi Garg](https://github.com/mahigarg0403-blip), [Khushi Hirawat](https://github.com/Khushi_hirawat)

`2026-01-26`

---

### Settlr.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/settlrai-2a95) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/7Biscuits/Settlr.ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://streamable.com/cb48zv) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Settle payments with your friends with agentic AI

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Fastify](https://img.shields.io/badge/Fastify-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

SettlrAI provides the solution to the challenge of managing shared expenses between groups of friends, roommates, family members, or fellow travelers.

When you find yourself paying for various costs together with other people, such as going out for a dinner, making a joint trip, or purchasing goods in groups, keeping track of all those payments and figuring out who paid what might be difficult, especially with frequent sharing.

Such situations usually cause delays, miscommunication, and even disputes between participants.

With SettlrAI, the process will become more efficient thanks to its ability to help users to:

* Create and track shared expenses within groups.
* Automatically calculate the balances between each other.
* Forget about manual payments accounting.
* Keep the history of transactions and settlements.
* Use artificial intelligence to check your balance with text or voice requests.
* Securely perform settlements using validated workflows rather than doing it manually.

**Challenges we ran into**

## Obstacles We Faced

* **Developing a safe AI actions system:**
  Making sure that AI actions would not harm users by actually making changes in their accounts required us to create a secure tool-calling environment where every action is checked on the backend before being executed.

* **Multi-step AI processes:**
  Requests like *“Settle everything I owe Rahul”* involve many processes – checking balance, wallet availability, calculating settlement, etc. This issue was resolved by creating structured workflows, which pass information from one step to another.

* **Protecting AI from financial hallucinations:**
  Incorrect calculations might result in incorrect money transfers; therefore, all financial actions were moved to deterministic backend logic. AI would determine user intention and choose an appropriate action, but calculations were performed on the backend side.

* **Dealing with ambivalent requests from users:**
  Sometimes, users can make incomplete requests, such as *“Pay Rahul.”* It might not be clear how much money should be transferred and under what conditions. In this case, we had to implement confirmation flows to clarify the intentions of the user.

* **Securing financial actions:**
  For secure execution, we added authentication, authorization, and verification steps into the process.

Team **commitNpray** -- [Kamal Ramchandani](https://github.com/kamalkernel), [Al Shahriah](https://github.com/alshahriah), [Rudransh Srivastava](http://github.com/7Biscuits)

`2026-09-02`

---

### SafeStride
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safestride-9ebf) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/18bSyzGedPXJHpiVa1ZvExoCDm7s8eBB5/view?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> women safety

![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Django rest framework](https://img.shields.io/badge/Django%20rest%20framework-333333?style=flat-square)

**The problem it solves**

SafeStride is an end-to-end, multi-platform personal safety ecosystem designed to protect individuals—particularly women—navigating public spaces, unlit areas, or traveling alone during late hours. By uniting a Django REST API backend, a Next.js web portal, and a native Jetpack Compose Android app into a unified architecture, the platform coordinates real-time location tracking, danger zone management, and immediate emergency response across both web and mobile interfaces.

### Core Applications & Real-World Use Cases

Safe Late-Night Navigation: Users walking or commuting alone can leverage integrated GraphHopper routing alongside continuous, low-latency spatial tracking to navigate safer paths.
Geofenced Perimeter Protection: Designated safety administrators can construct virtual perimeters around known high-risk zones, campus boundaries, or safe havens to track when users cross specific geographic thresholds.
Instant Emergency Escalation: Through an integrated WebSocket connection, the Android app enables instant alert triggers, immediately broadcasting critical location data directly to the central network without delay.
Centralized Safety Monitoring: Security teams, campus staff, or trusted guardians can use the Next.js web dashboard to oversee active alerts, monitor shared geofences, and adjust safety boundaries in real time.

### How SafeStride Enhances Daily Safety

Streamlining Emergency Dispatch: Traditional panic calls require manual dialing and verbal location updates, whereas SafeStride automatically dispatches live spatial coordinates to trusted monitoring accounts the moment an alert is triggered.
Automating Zone Awareness: Instead of relying on manual check-ins, the app automatically tracks entry and exit events across monitored geofences, keeping trusted administrators informed passively.
Unifying Mobile & Web Monitoring: Users stay protected on the go via the lightweight Kotlin Android client, while security teams gain a comprehensive view of active alerts and zone updates through the responsive web portal.

**Challenges we ran into**

Building SafeStride across web, mobile, and backend ecosystems brought a fair share of technical hurdles during development. Here is how we tackled the main engineering challenges:

### Key Hurdles & How We Overcame Them

Map Rendering API Costs & Shifting to OSM: We initially planned to use Google Maps API for rendering, but billing requirements and usage limits quickly became a bottleneck. We pivoted to OpenStreetMap (OSM) paired with **OSRM (Open Source Routing Machine) and later shifted to GraphHopper for navigation, providing a completely open-source, cost-effective spatial stack.
Graph Routing with Dynamic Geofences: Our biggest architectural hurdle was integrating graph-based route calculations with active geofence constraints. Standard navigation engines default to the absolute shortest path, which often routes users directly through high-risk zones. We had to implement custom logic to dynamically evaluate geofence coordinates, recalculate route graphs, and steer users around restricted or unsafe boundaries safely.
Login Authorization & Token Lifecycle: Managing authentication state seamlessly between the Next.js web portal and the Jetpack Compose Android client created edge-case auth failures. We resolved this by standardizing full SimpleJWT token refresh flows, storing access tokens securely on Android via `TokenManager`, and intercepting HTTP requests using custom `AuthInterceptor` and `TokenAuthenticator` implementations.
Real-time Connection & WebSocket Stability: Maintaining reliable WebSocket connections across different network environments for live tracking was inconsistent. We stabilized state sync by implementing fallback mechanisms, automatic reconnect loops, and structured event handling in our Django REST backend and client models.
OneDrive & Gradle File Lock Errors: Local Android builds kept failing randomly due to OneDrive cloud synchronization placing background locks on `.gradle` cache files and build artifacts. Moving the Android project directory out of OneDrive-synced paths to a local, untracked drive immediately solved build locks and significantly sped up build times.

Team **The NightFarers** -- [Tanay Ghosh](https://github.com/Tanay016), [Shebanti Haldar](https://github.com/Maxxed-0ut), [Avirup Biswas](https://github.com/phenroav), [Debjyoti Ghosh](https://github.com/debjyoti667)

`2026-08-30`

---

### VidyaTech AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vidyatech-ai-4a57) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dhrubamarik/Vidyatech-AI.git) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Closing the Loop Between Classroom Teaching and Pr

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Students juggling multiple courses face three compounding problems that most "AI study tools" don't actually fix:

Generic AI hallucinates. Ask ChatGPT to explain a concept from your specific textbook or lecture notes, and it confidently answers from general internet knowledge — which may not match what your professor actually taught, or invents details entirely. Students need answers grounded strictly in their material.
Planning and self-awareness are manual and disconnected. Students don't have a real-time picture of which syllabus topics they're actually prepared for vs. just scheduled to study, and burnout usually gets noticed only after it's already a problem — not from real signals like overdue tasks and rising workload.
Faculty have no visibility into where students are actually struggling. Office hours and doubt sessions are reactive; there's no aggregate signal showing which topics generate the most confusion across a whole class until it shows up on an exam.

VidyaTech AI solves all three with one core idea: a personal, isolated knowledge base per user. Every student and faculty member gets their own private FAISS vector index of their uploaded notes/PDFs. The AI is only allowed to answer from that material — if nothing relevant is indexed, it says so instead of guessing. That same retrieval layer then powers everything else: an adaptive study planner, a live "exam readiness" heatmap per topic, burnout tracking from real usage data, and faculty-side analytics on what students are actually asking about.

**Challenges we ran into**

Preventing hallucination without breaking usability. Naively doing RAG (always injecting the top-k retrieved chunks) meant the AI would still try to answer using barely-related content just because it was the "closest" thing in the index. We had to introduce a hard relevance cutoff (RELEVANCE_THRESHOLD on FAISS L2 distance) so the system honestly reports "not found in your uploads" instead of forcing an answer — a UX tradeoff between always answering and answering only when it's actually grounded.
Per-user data isolation at the vector-store level. A single shared FAISS index would have let one student's query surface another student's private notes. We solved this by keying entirely separate FAISS indexes per scope (user:<id> / community:<id>), which meant handling index rebuilds carefully whenever a single document is deleted — removing chunks from a IndexFlatL2 isn't a native operation, so we track chunk ownership separately and rebuild the index from the surviving chunks.
Making non-AI features feel just as smart. Burnout scoring, the syllabus heatmap, and doubt-cluster analytics all needed to feel intelligent without burning LLM calls (or budget) on every dashboard refresh. We designed these as transparent heuristics instead — e.g. burnout score is a weighted formula over real task/query counts, and topic coverage is computed from raw embedding distance rather than another LLM round-trip — which kept the app fast and free to run at scale.
Structuring reliable JSON output from an LLM. Features like MCQ quiz generation and reverse-quiz grading need strict, parseable JSON back from the model, but LLMs sometimes wrap answers in markdown fences or add commentary. We had to build defensive parsing (stripping code fences, falling back gracefully) so a malformed response doesn't crash the feature.
Keeping the frontend zero-build. Choosing a single-file vanilla JS frontend (no React/bundler) meant we couldn't rely on component libraries for things like Markdown rendering, LaTeX math, or charts — we integrated marked.js + DOMPurify (sanitization was critical since we're rendering AI-generated content), and KaTeX, entirely via CDN script tags.

Team **Hidden Blades** -- [Imon Das](https://github.com/imondas0609-imon), [Debojyoti Ghosh](https://github.com/debojyoti362), [Harsha Adhikary](https://github.com/PokeHarsha5506), [Dhruba Marik](https://github.com/dhrubamarik)

`2026-08-30`

---

### FINORA AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finoraai-cee6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ADRIT2006/FINORA-AI) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Beyond Payments. Beyond Intelligence

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Lucide React](https://img.shields.io/badge/Lucide%20React-333333?style=flat-square)

**Challenges we ran into**

1. UPI Integration : Implementing a real-time UPI payment system and handling payment verification was challenging, so we used a demo payment flow for the prototype.

2. AI Expense Categorization: Automatically identifying whether a transaction belongs to Food, Shopping, Transport, etc. required careful categorization logic.

3. Tax Estimation : Creating an accurate estimated tax calculation while considering different income and expense patterns was challenging.

4. Cash-Flow Forecasting: Predicting future financial balances from limited transaction data required a simple and reliable forecasting approach.

5. System Integration: Connecting the UPI payment flow, AI categorization, database, tax module, forecasting, and dashboard within the limited hackathon time was a major challenge.

How We Can Overcome These Problems : 


1. UPI Integration: Use a simulated UPI payment flow for the hackathon prototype and plan certified payment-gateway integration for the final version.

2. Expense Categorization:  Use simple AI/rule-based categorization with merchant names and transaction descriptions to achieve reliable results.

3. Tax Estimation: Use a clearly defined tax-estimation formula and display the result as an estimated liability, not an exact tax amount.

4. Cash-Flow Forecasting: Use historical income and expense data with simple forecasting methods to predict future balances.

5. System Integration: Develop each module separately, test the APIs early, and integrate them step-by-step to avoid last-minute errors.

**The problem it solves**

FINORA AI transforms ordinary UPI payments into actionable financial intelligence. Instead of leaving users with scattered transaction histories, it automatically categorizes expenses, analyzes spending patterns, forecasts future cash flow, and provides financial health insights from every payment. 


What people can use it for : 
1. Automatic expense tracking : No manual categorization after every UPI payment.
2. Smarter budgeting : Identify where money is spent and control unnecessary expenses.
3. Cash-flow forecasting : Predict future balance based on spending behavior.
4. Tax organization : Detect eligible spending patterns to simplify financial review.
5. Financial health monitoring : Get an easy-to-understand score and personalized insights for better decisions. 


Result: Payments become more than transactions - they become a tool for smarter, safer, and more informed financial decision-making

Team **ALPHA-Z** -- [Adrit Goswami](https://github.com/ADRIT2006), Nilanjana Debnath, [Aditya Jaiswal](https://github.com/adijatrik-nova), SK JAMILUDDIN MONDAL

`2026-08-30`

---

### What Next?
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/what-next-d96a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rene-marceline/What-Next) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://trywhatnext.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your life. Your budget. Your Pilot.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**Challenges we ran into**

Building an end-to-end autonomous commerce experience was significantly more challenging than building a traditional AI application because every part of the workflow had to work together reliably.

One of our biggest challenges was integrating Prava's spending-authority model into an AI-driven purchasing flow. Instead of simply calling a payment API, we had to design a system where users explicitly delegate purchasing authority, create and activate mandates, continuously verify spending limits and merchant restrictions, and only then allow the AI to complete an eligible purchase. This required carefully separating AI decision-making from payment authorization so the AI could never exceed the user's approved financial authority.

Another challenge was balancing real functionality with a hackathon-friendly demo. Live experience data from TicketLens can be unpredictable, so we built a deterministic decision engine and curated demo timeline to ensure every part of the autonomous purchase flow could be demonstrated consistently while still supporting live discovery when available.

Finally, designing the user experience proved to be much harder than implementing the backend. Early versions looked like an engineering dashboard rather than a consumer product. We went through multiple complete UI redesigns to shift the focus from configuration and payments to the core idea of AI Pilots making the experience feel intuitive, trustworthy, and approachable while still exposing the reasoning behind every autonomous decision.

These challenges ultimately helped shape What Next? into a product that demonstrates not only autonomous purchasing, but also how AI can safely act on a user's behalf without sacrificing transparency or control.

**The problem it solves**

People miss great experiences because discovering, evaluating, and purchasing them requires constant time and attention. What Next? lets users subscribe to AI Pilots that discover live opportunities, intelligently evaluate them, and autonomously purchase eligible experiences within user-approved spending authority using Prava. This demonstrates a trusted model for agentic commerce today. Next, we plan to expand the Creator Pilot marketplace and enable end-to-end purchases directly from live merchant opportunities.

**Best Visa Intelligent Commerce Implementation**

What Next? expands the number of transactions that can happen on Visa's payment network by enabling trusted autonomous commerce.

Today, many discretionary purchases - concerts, sporting events, restaurants, local experiences, and weekend activities, never happen because users don't have the time to constantly search, compare, monitor prices, and complete checkout before opportunities disappear. As a result, merchants lose potential customers and payment networks lose transaction volume.

What Next? changes this by allowing users to subscribe to AI Pilots that continuously discover opportunities, evaluate whether they're worth purchasing, and autonomously complete eligible transactions within explicitly approved spending authority using Prava.

Instead of simply recommending products, the AI completes the purchasing journey, converting intent into completed transactions while keeping users in control through merchant-specific authorization, spending limits, and transparent decision making.

By reducing friction between discovery and checkout, What Next? has the potential to:

-> increase transaction frequency for discretionary spending,
-> reduce abandoned purchase opportunities,
-> help merchants convert high-intent customers,
-> and drive more secure transactions across Visa's payment ecosystem.

**Most Startup-Ready Product**

What Next? is designed as a consumer platform where users subscribe to AI Pilots that autonomously manage different aspects of their lives, starting with experiences. By combining personalized decision-making with user-approved autonomous payments, What Next? transforms AI from a recommendation engine into a trusted purchasing agent. The Pilot model is inherently scalable across travel, shopping, dining, and other verticals, creating a subscription-based platform with strong recurring engagement and monetization opportunities through commerce partnerships, merchant referrals, and premium AI services.

**OpenAI**

What Next? uses OpenAI to transform natural-language user intent into structured AI Pilots. Instead of asking users to manually configure complex preferences, budgets, and lifestyle goals, users simply describe what they want (e.g., "Set aside $100/month for concerts and comedy in New York, automatically buy anything under $40"). OpenAI converts this into a structured Pilot and spending policy that drives opportunity evaluation while respecting explicit financial authority defined by the user. This makes the interaction natural while ensuring spending limits are never inferred or invented by the AI.

**Best Agentic User Experience**

What Next? reimagines autonomous commerce around AI Pilots rather than dashboards and configuration screens. Users subscribe to a Pilot that represents their interests and spending style, while the interface clearly communicates why the AI chose to PASS, ASK, or BUY. The experience emphasizes transparency, user control, and trust by visually separating real Prava-authorized purchases from simulations and by making every autonomous decision explainable.

**Agentic Commerce Hackathon**

What Next? reimagines how consumers interact with commerce by introducing AI Pilots, specialized agents that users subscribe to for different aspects of their lives. Instead of repeatedly searching, evaluating, and purchasing experiences, users delegate those decisions to an AI Pilot that continuously discovers opportunities, determines whether they're worth acting on, and autonomously completes eligible purchases within explicitly approved spending authority.

Unlike traditional recommendation engines, What Next? doesn't stop at suggesting products or experiences. It closes the commerce loop by combining:

OpenAI for natural-language intent understanding and AI Pilot creation, a deterministic decision engine that evaluates opportunities and decides whether to PASS, ASK, or BUY, and Prava to securely authorize autonomous purchases while enforcing user-defined financial limits.

This demonstrates a practical vision of agentic commerce where AI agents don't just recommend, they responsibly act on a user's behalf while keeping the user in control.

Rene Marceline

`2026-08-03`

---

### Stratify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stratify-7e46) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VaibhavUPratap/Stratify) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/TKpNWlbOJ4g?si=zM4EAbLEs4U5JhNy) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Know what matters, before it matters

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kaggle](https://img.shields.io/badge/Kaggle-333333?style=flat-square)

**Challenges we ran into**

Getting six agents to agree with each other was harder than getting Gemma
to respond at all. At first each agent gave free-text advice, and they'd
contradict each other. We fixed it by forcing every agent into the same
output format and moving prioritization out of the LLM into simple,
deterministic code.

Speed was the other issue — six local model calls in a row was too slow
for a live demo, so we made them run at the same time instead of one after
another. We also had no real customer data, so we built our own mock data
by hand rather than randomizing it, so the agents had real patterns to
find.

**The problem it solves**

Small businesses have all the same data big companies do — sales, invoices, supplier delays, unpaid invoices — but no analyst to make sense of it. Stratify reads that data and tells the owner what needs attention today, instead of leaving them to dig through spreadsheets.
With it, people can:

See a real cash flow runway instead of guessing
Spot risky suppliers and customers before they cause a problem
Get warned when a product's margin quietly drops too low
Upload an invoice or bank statement and have it read automatically, no manual entry
Test a decision (price change, new hire, loan) before making it
Get one ranked list of what matters most, instead of digging through dashboards

It also runs fully on local Gemma 4 inference, so the business's data never leaves the owner's machine.

Team **Stratify** -- Varun U Pratap, [Vaibhav Pratap](https://github.com/VaibhavUPratap), Vamshi Krishna

`2026-07-18`

---

### TrustGraph AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trustgraph-ai-b113) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Akash-afk-ai/TRUST-.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://trustgraph-ai-jqk8.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4_73kJCMnRI?si=ihfEMoh4RX69Kd8a) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Al-powered Enterprise Compliance

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Knowledge graph](https://img.shields.io/badge/Knowledge%20graph-333333?style=flat-square)

**The problem it solves**

Financial institutions receive hundreds of loan applications every day. Each application contains multiple documents such as bank statements, invoices, GST certificates, vendor details, and financial reports. Today, these documents are often reviewed manually, making the process slow, expensive, and prone to human error.
Manual verification also makes it difficult to identify hidden fraud patterns such as duplicate invoices, suspicious payment structures, fake compliance documents, or risky business relationships.
TrustGraph AI solves this problem by providing an intelligent compliance and risk assessment platform that automates the entire verification workflow.
Our platform:
Extracts information from uploaded PDFs using OCR.
Builds a Relationship Knowledge Graph to visualize connections between companies, vendors, invoices, and transactions.
Performs AI-powered risk analysis using explainable compliance rules.
Uses Google Gemma AI to generate easy-to-understand audit summaries.
Automatically creates professional Compliance & Risk Assessment PDF reports.
Helps banks and financial institutions make faster, more accurate, and transparent loan approval decisions.
Benefits
Reduces document verification time from hours to minutes.
Improves fraud detection.
Provides explainable AI recommendations.
Automates compliance reporting.
Supports scalable enterprise loan verification.

**Challenges we ran into**

Building TrustGraph AI required integrating several independent technologies into a single workflow.
Some of the major challenges included:
Extracting accurate text from scanned financial documents using OCR.
Designing a rule-based risk engine capable of identifying fraud indicators such as duplicate invoices, structured payments, and compliance issues.
Building an interactive Relationship Knowledge Graph to visualize entity connections.
Integrating Google Gemma AI to generate meaningful natural language explanations for audit results.
Automatically generating professional Compliance PDF reports.
Managing secure API keys using environment variables without exposing sensitive credentials.
Deploying a monorepo project with a React (Vite) frontend on Vercel and a FastAPI backend on Render while resolving build and TypeScript issues.
These challenges helped us build a complete end-to-end enterprise compliance platform that is scalable, secure, and production-ready.

Team **ByteBrigade** -- Ananda Joshi, [Akash Naik](https://github.com/Akash-afk-ai), Akash Jadhav, Preetam Gugalottar

`2026-07-18`

---

### saathi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saathi-7458) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shree1071/saathi-Ai) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/7asW8tVxyzA?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Saathi AI: The Autonomous, On-Device CFO for India

![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square)

**Challenges we ran into**

The problem it solves
India's 12+ million traditional Kirana (mom-and-pop) store owners are under massive threat from venture-backed quick-commerce platforms (Blinkit, Zepto, etc.). While quick-commerce relies on heavy data analytics and cloud infrastructure to optimize inventory and speed, Kirana stores rely on intuition and paper ledgers.

Saathi AI levels the playing field by acting as an autonomous, on-device CFO for traditional retailers. It solves three massive problems:

Data Privacy & Frictionless Onboarding: Kirana owners are highly protective of their wholesale margins and hesitant to connect bank APIs. We solve this by securely reading native transactional SMS data directly on the device and automatically categorizing expenses (e.g., Wholesale Purchases, Logistics, Salaries). Zero manual entry, zero cloud leakage.
Predictive Inventory (The "Edge AI Token" Approach): Instead of just showing historical charts, Saathi AI uses a distilled predictive model running locally on the device. Similar to how an LLM predicts the next word token, Saathi AI evaluates basket combinations and sales velocity to predict the "next business event." It warns the owner: "Aashirvaad Atta is selling 30% faster; you will run out by Thursday. Recommend ₹25,000 wholesale purchase."
Paperless Invoicing: Owners can take a photo of a wholesale invoice, and our on-device pipeline (MediaPipe + Google Gemma) automatically extracts line items and adds them to inventory without sending sensitive supplier data to external servers.
Challenges we ran into
Bringing enterprise-grade LLM capabilities to a mobile device completely offline was incredibly difficult.

1. The "Cloud-Dependency" Habit: Most AI applications today are simple API wrappers. When we initially tried to parse complex, unstructured wholesale invoices, we defaulted to wanting to use cloud Vision APIs. However, this violated our core tenet of 100% data privacy. How we solved it: We engineered a completely localized pipeline. We integrated MediaPipe for on-device Optical Character Recognition (OCR) to extract the raw text, and then passed that text into Google Gemma (running locally via Android ML Kit / AICore) to semantically parse the items, prices, and taxes.

2. Asynchronous State Management across the Native/Flutter Bridge: When parsing the local SMS database to generate the initial zero-friction dashboard, we had to funnel thousands of rows of SMS data through a local heuristics engine to categorize them as "Kirana" expenses. How we solved it: We had to abandon Flutter plugins and write a custom asynchronous Kotlin MethodChannel (SmsService.kt) that handles the heavy lifting on a background thread in native Android, passing only the aggregated, categorized JSON back up to the Flutter UI thread to prevent the app from dropping frames.

Technologies used
Google Gemma: Open-weight LLM running on-device for semantic parsing and predictive business insights.
Flutter & Dart: For the beautiful, responsive, Fortune-500 grade CFO dashboard and user interface.
Kotlin (Android Native): For secure SMS reading, local database management (InvoiceDatabase.kt), and bridging the ML Kit/AICore on-device models.
Google MediaPipe: For on-device, privacy-first OCR (Optical Character Recognition) of wholesale invoices.

**The problem it solves**

The problem it solves
India's 12+ million traditional Kirana (mom-and-pop) store owners are under massive threat from venture-backed quick-commerce platforms (Blinkit, Zepto, etc.). While quick-commerce relies on heavy data analytics and cloud infrastructure to optimize inventory and speed, Kirana stores rely on intuition and paper ledgers.

Saathi AI levels the playing field by acting as an autonomous, on-device CFO for traditional retailers. It solves three massive problems:

Data Privacy & Frictionless Onboarding: Kirana owners are highly protective of their wholesale margins and hesitant to connect bank APIs. We solve this by securely reading native transactional SMS data directly on the device and automatically categorizing expenses (e.g., Wholesale Purchases, Logistics, Salaries). Zero manual entry, zero cloud leakage.
Predictive Inventory (The "Edge AI Token" Approach): Instead of just showing historical charts, Saathi AI uses a distilled predictive model running locally on the device. Similar to how an LLM predicts the next word token, Saathi AI evaluates basket combinations and sales velocity to predict the "next business event." It warns the owner: "Aashirvaad Atta is selling 30% faster; you will run out by Thursday. Recommend ₹25,000 wholesale purchase."
Paperless Invoicing: Owners can take a photo of a wholesale invoice, and our on-device pipeline (MediaPipe + Google Gemma) automatically extracts line items and adds them to inventory without sending sensitive supplier data to external servers.

**Overall Winner**

Track 1: This project was built from the ground up to showcase the bleeding edge of Android's local intelligence and Edge AI capabilities. Instead of relying on cloud infrastructure, Saathi AI runs its most complex operations entirely on-device. We utilized Google MediaPipe for localized, privacy-first OCR to scan physical wholesale invoices. We then bridged that data into Google Gemma (running natively via Android AICore/ML Kit) to perform semantic parsing and predictive analysis on the Kirana store's inventory. By keeping all computation localized, we demonstrated how modern Android hardware can deliver zero-latency, enterprise-level AI solutions while guaranteeing 100% data privacy for traditional retailers.

Team **FULCRUM** -- Shree harsha, Hunain Baig

`2026-07-18`

---

### InsightGenie -AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/insightgenie-ai-6865) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kanika647/insightgenie-ai) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_3MWF6Zt1Ro) [![Built at](https://img.shields.io/badge/Built%20at-HackGenome-0052CC?style=flat-square)](https://hackgenome2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Ask Your Data. Get Answers. Take Action.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

### Challenges We Ran Into

- Handling datasets with missing values, inconsistent formats, and duplicate records.
- Building a reliable data cleaning and validation pipeline for diverse business datasets.
- Generating meaningful business insights instead of simply displaying charts and metrics.
- Integrating AI models with analytics workflows while maintaining response accuracy.
- Implementing effective anomaly detection and forecasting across different business scenarios.
- Ensuring the platform remains intuitive and easy to use for non-technical users.
- Optimizing performance for large datasets and real-time insight generation.
- Maintaining the balance between speed, scalability, and analytical accuracy.
- Overcame these challenges through iterative testing, enhanced preprocessing techniques, and continuous refinement of the AI insight-generation pipeline.

**The problem it solves**

### The Problem It Solves

- Businesses generate massive amounts of data daily but struggle to extract actionable insights from it.
- Traditional BI tools require technical expertise and manual dashboard creation.
- Important trends, anomalies, and business opportunities often remain hidden in complex datasets.
- Decision-making becomes slower due to time-consuming data analysis processes.
- Non-technical users find it difficult to understand and interpret business data.
- InsightGenie AI automatically transforms Excel and CSV data into interactive dashboards and meaningful insights.
- Users can ask business questions in natural language and receive instant answers.
- Provides AI-powered recommendations, anomaly detection, and forecasting for smarter decision-making.
- Helps organizations make faster, data-driven decisions without requiring dedicated data analysts.

Team **KPTechz 2.O** -- [Pragati Gupta](https://github.com/Pragatigupta2508), [Kanika Verma](https://github.com/kanika647)

`2026-06-14`

---

### ChainPe
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/chainpe-fa3b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SamyaDeb/ChainPe) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1lt4scB1d_fTxmX8ksjjcz0PMtLh8DvMa/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> An Autonomous Payment System For AI Agents

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Developers build powerful APIs for AI, finance, automation, data, and countless other use cases but monetizing them is still complicated. Setting up billing, authentication, API keys, subscriptions, and payment infrastructure takes significant time and effort, so many developers either keep APIs private or offer them for free.

At the same time, AI agents cannot autonomously access and pay for services. Most APIs require manual onboarding steps like account creation, API keys, and credit card setup, making seamless machine-to-machine interactions impossible.

Our project solves this by creating a payment and access layer for APIs, allowing developers to monetize services instantly while enabling AI agents to discover, authenticate, and pay for APIs autonomously.

**Challenges we ran into**

One of the biggest challenges was designing a seamless payment flow for autonomous AI agents. Traditional APIs are built for humans, not machines, so most existing systems depend on manual onboarding steps like account creation, API keys, and subscription management.

Another major challenge was creating a developer experience simple enough that API providers could monetize services without setting up complex billing infrastructure. We also had to think carefully about security, wallet-based authentication, payment verification, and how agents could safely interact with paid services in real time.

Building interoperability between AI agents, wallets, APIs, and MCP/CLI tooling while keeping the workflow fast and developer-friendly was also a significant technical challenge.

**Blockchain**

Our project fits perfectly into the Blockchain track because it enables decentralized, wallet-based payments between AI agents and APIs. Instead of relying on traditional subscriptions, API keys, and centralized billing systems, we use blockchain powered payments to allow autonomous machine to machine transactions.

Developers can register and monetize APIs directly, while AI agents can securely discover, authenticate, and pay for services in real time using on-chain payment infrastructure. This creates an open ecosystem for programmable services and autonomous commerce powered by blockchain technology.

**AI/ML**

Our project fits into the AI/ML track by enabling AI agents to autonomously discover, access, and pay for real-world services and APIs. Today, most AI systems still rely on manual setups like API keys, subscriptions, and human approvals, which limits true agent autonomy.

We built an infrastructure layer that allows AI agents to interact with paid APIs seamlessly using wallet-based authentication and automated payments. This helps unlock more capable AI workflows where agents can independently use external tools, data, and services in real time.

**Open Innovation**

Our project fits into the Open Innovation track because it creates a complete infrastructure layer for autonomous API commerce between developers and AI agents.

For API developers, we built a CLI tool that makes it easy to register, manage, and monetize APIs without building custom billing or payment systems. For consumers and AI agents, we built MCP integration that allows agents to discover, access, and pay for services autonomously using wallet-based authentication and blockchain payments.

By combining developer tooling, AI interoperability, and decentralized payments into one ecosystem, our project enables a new model where APIs become instantly programmable, monetizable, and accessible to autonomous agents in real time.

Team **Ashes** -- [Samya Deb Biswas](https://github.com/SamyaDeb), [Anindha Biswas](https://github.com/anindhabiswas25), [Akash Biswas](https://github.com/saxux2)

`2026-05-31`

---

### ORIGIN LENS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/origin-lens-41e0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://originlens.in) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tNRFzE6JFWg?si=O0guUgwZ3ivQkogw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> DETECTS AN IMAGE IS REAL OR AI GENERATED

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

In today’s digital world, AI-generated images are becoming increasingly realistic, making it difficult for people to distinguish between authentic and manipulated visual content. This creates serious problems such as misinformation, fake social media content, scam listings, misleading advertisements, and loss of trust in digital media.

Origin Lens solves this problem by providing an AI powered platform that analyzes uploaded images and determines whether they are real or AI generated. The platform provides a confidence score along with explanations to help users better understand the analysis results.

People can use Origin Lens to:
- Verify suspicious or viral images before sharing them
- Detect fake or AI generated listing images in marketplaces
- Improve trust in online content and communication
- Support digital awareness and responsible media consumption
- Reduce the risk of scams and misleading visual information

By making image authenticity verification simple, fast, and accessible, Origin Lens helps users make safer and more informed decisions in the age of AI generated content.

**Challenges we ran into**

One of the biggest challenges while building Origin Lens was handling accurate analysis for highly realistic AI generated images. As modern AI models produce very convincing visuals, distinguishing them from real images consistently was difficult and required multiple rounds of testing, analysis tuning, and response optimization.
Another challenge was backend reliability and API response handling. During development, the AI analysis occasionally failed due to server overloads, response formatting issues, and API timeouts. I solved this by improving request handling, adding retry logic, validating responses safely, and optimizing the image processing workflow.

I also faced performance issues when users uploaded large images, which affected response speed and stability. To overcome this, I optimized image handling and improved frontend-backend communication to make the experience smoother and faster.

On the frontend side, designing a result interface that clearly explains the analysis without overwhelming users required several iterations. I focused on creating a clean UI with confidence scores and understandable explanations to improve usability and accessibility.

These challenges helped improve both the technical stability and overall user experience of the platform.

[Avinash Gopi](https://github.com/AVINASHGOPI110)

`2026-05-06`

---

### Paygentic Fraud Detector
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/paygentic-fraud-detector-e879) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://paygentic-fraud-detector.web.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0PvclHaQTXA?si=-czvhttTn12uJORd) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Real-Time Fintech Fraud Detection Dashb

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Chart.js](https://img.shields.io/badge/Chart.js-333333?style=flat-square) ![github pages](https://img.shields.io/badge/github%20pages-333333?style=flat-square) ![Responsive web design](https://img.shields.io/badge/Responsive%20web%20design-333333?style=flat-square)

**The problem it solves**

Paygentic Fraud Detector helps identify suspicious digital payment transactions in real time.

Many online payment systems face fraud risks such as high amount scams, unusual locations, and suspicious transaction timings. Small businesses and users often do not have access to advanced fraud monitoring systems.

This project analyzes transaction details like amount, location, payment method, and transaction time to classify transactions into Safe, Medium Risk, or High Risk categories.

The dashboard provides:
• Real-time fraud analysis
• AI-based recommendations
• Live risk distribution charts
• Transaction history tracking
• Fraud score monitoring

The goal is to improve cybersecurity awareness and provide a smart fraud detection experience through an interactive dashboard.

**Challenges we ran into**

One of the biggest challenges was managing dynamic chart updates and transaction history together in real time.

During development, the pie chart stopped rendering because of DOM update issues and incorrect element references in JavaScript. Debugging the issue required checking browser console errors, fixing missing IDs, and properly updating chart datasets dynamically.

Another challenge was creating a responsive cybersecurity-themed UI with live animations while keeping the dashboard lightweight and fast.

I also faced issues while deploying the project on GitHub Pages and synchronizing live updates with the frontend logic, but after multiple debugging sessions the project became fully functional.

[Shubham Nagpure](https://github.com/Shubham-coder-a)

`2026-05-26`

---

### The SaaS Factory
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/the-saas-factory-9c67) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/flowboostkontakt-laboost/SaaSFactory) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://saasfactory-sand.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8ox_o0iaGp8) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI that doesn’t assist - it originates.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![WalletConnect](https://img.shields.io/badge/WalletConnect-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![discord.js](https://img.shields.io/badge/discord.js-333333?style=flat-square)

**The problem it solves**

## The problem The SaaS Factory solves

**SaaS-Factory.ai  -the autonomous micro-SaaS foundry.**

Give it one prompt. An agent pipeline — **Architect, Developer, Treasurer** — turns
it into a real, deployed, monetized product, then retires it when it stops earning.
No human in the loop after the prompt.

### The full autonomous lifecycle
1. **Architect (OpenAI)**  -drafts the complete specification.
2. **Developer (OpenAI)**  -writes the product, renders a single-file micro-SaaS
   with a **Locus Checkout** paywall, and pushes it to a **real GitHub repository**.
3. **Deploy**  -instantly ships the live product via Vercel.
4. **Treasurer**  - mints real **Locus Checkout** sessions, reconciles settlement,
   and sweeps revenue to a master wallet. It automatically refuses to spend on new
   builds if the treasury dips below the required reserve.
5. **Sunset** - -products generating no revenue are automatically flagged, torn
   down, and repo-archived. Businesses treated as ephemeral, deployable units.

### What's real
- OpenAI integration ✅
- GitHub repository creation ✅
- Live deployment on Vercel ✅
- Locus Checkout  -real hosted payment sessions + status reconciliation ✅

### What makes it different
Most agents *assist* a business. Ours **is** the business  - and it's the only one
that runs the *entire* lifecycle, including knowing exactly when to **shut a
business down**. A built-in **treasury reserve guard** means the foundry only
builds what it can afford, and the **sunset engine** retires what stops earning.

🚀 Live: https://saasfactory-sand.vercel.app
💻 Code: https://github.com/flowboostkontakt-laboost/SaaSFactory

---

## Challenges I ran into

**1. The "recursive logic" loop 🔄**
*Hurdle:* with a vague prompt, the Architect agent kept asking for more
information instead of deciding  - defeating the "autonomous founder" goal of the
LocusFounder track.
*Fix:* a **Decision-First protocol**. If the prompt is ~80% clear, the agent makes
a best-guess executive call on UI and features and keeps the pipeline moving, with
no human in the loop.

**2. Dynamic Locus Checkout injection 💳**
*Hurdle:* wiring a working payment gateway into code that didn't exist minutes
earlier is hard  - passing the right Locus session parameters into a freshly
generated frontend.
*Fix:* a standardized **Locus-Pay module**. Instead of writing payment logic from
scratch each time, the factory snaps a pre-verified Checkout component into the
generated app, so Locus Checkout works on every build.

**3. Autonomous treasury (the "ghost wallet" problem) 👻**
*Hurdle:* tracking which micro-SaaS earned what, across many tools, without
manually checking every transaction.
*Fix:* a hierarchical **Locus sub-wallet per product** for clean accounting, plus a
**Treasurer agent** that sweeps profit to the master wallet while keeping a reserve
floor for autonomous operating costs.

**4. Ephemeral vs. sustainable ⏳**
*Hurdle:* deciding when a business has "failed" - too early kills slow-burners, too
late wastes hosting resources.
*Fix:* a 72-hour revenue window. No Locus Checkout activity in that window → the
agent **autonomously sunsets** the product (teardown + repo archive), proving it
can manage a business lifecycle end-to-end.

---

## Technologies used

React · Next.js · TypeScript · Tailwind CSS · Prisma · PostgreSQL · OpenAI ·
GitHub · Vercel · Locus (Checkout)

---

## Links

- Live demo: https://saasfactory-sand.vercel.app
- Source: https://github.com/flowboostkontakt-laboost/SaaSFactory

**Challenges we ran into**

#### **1. The "Recursive Logic" Loop** 🔄
**The Hurdle:** One of the biggest challenges was preventing the **Agent Architect** from getting stuck in a loop when a user prompt was too vague[cite: 1]. The agent would keep requesting more information instead of making executive decisions, which defeated the "Autonomous Founder" goal of the LocusFounder track[cite: 1].
**The Fix:** We implemented a **"Decision-First" protocol**[cite: 1]. If the prompt is 80% clear, the agent is instructed to make a "best-guess" executive decision on the UI and features to keep the deployment pipeline moving without human intervention[cite: 1].

#### **2. Dynamic Locus Checkout Injection** 💳
**The Hurdle:** Injecting a functional payment gateway into *dynamically generated* code is notoriously difficult[cite: 1]. We struggled with ensuring the **Agent Developer** correctly passed the right session parameters from the Locus API into a React component that didn't exist minutes prior[cite: 1].
**The Fix:** We created a **standardized Payment Wrapper**[cite: 1]. Instead of asking the agent to write the payment logic from scratch every time, the factory provides a pre-verified "Locus-Pay-Module" that the agent simply "snaps" into the generated frontend, ensuring Locus Checkout works every time[cite: 1].

#### **3. Autonomous Financial Management (The "Ghost Wallet" Issue)** 👻
**The Hurdle:** Managing dozens of different Micro-SaaS tools meant we needed a way to track which tool earned what, without manually checking every transaction[cite: 1].
**The Fix:** We leveraged **Locus Wallets** to create a hierarchical tree[cite: 1]. Each SaaS is assigned a unique sub-wallet at creation for transparent accounting[cite: 1]. We wrote a "Treasury Agent" script that polls these wallets and automatically sweeps profits to the main Founder Wallet while leaving enough funds for autonomous operational costs[cite: 1].

#### **4. Balancing "Ephemeral" vs. "Sustainable"** ⏳
**The Hurdle:** Deciding when a business should be considered "failed" and shut down was tricky, as we wanted to treat businesses as ephemeral, deployable units[cite: 1]. Shutting it down too early might kill a slow-burner, but keeping it too long wastes hosting resources[cite: 1].
**The Fix:** We built a **Revenue Monitoring Dashboard** for the Parent Agent[cite: 1]. The agent now looks at **Locus Checkout hits** over a 72-hour window[cite: 1]. If a tool doesn't generate revenue, the agent autonomously "sunsets" it, proving it can manage a business lifecycle end-to-end[cite: 1].

**Using LocusFounder to Build a Business!**

Our project, **SaaS-Factory.ai**, was built from the ground up to be the definitive example of the LocusFounder vision[cite: 1]. Here is how it aligns with the track requirements:

* **Agent as the Founder**: We moved past agents that simply "assist"[cite: 1]. In SaaS-Factory, the agent **is** the founder; it identifies market needs, writes the code, and manages the entire business lifecycle without a human in the loop[cite: 1].
* **Autonomous Operations**: By leveraging **LocusFounder**, our system handles end-to-end business creation and autonomous operations[cite: 1]. The agent manages everything from initial prompt to final deployment[cite: 1].
* **Real Revenue Generation**: We integrated **Locus Checkout** to facilitate real transactions[cite: 1]. Every Micro-SaaS generated is a working commercial operation that can accept payments immediately[cite: 1].
* **Automated Financials**: Using **Locus Wallets**, our agents handle payouts and revenue logging autonomously[cite: 1]. The system manages its own payout schedule and operational costs[cite: 1].
* **Ephemeral Business Units**: SaaS-Factory perfectly executes the track's challenge to treat businesses as "ephemeral, deployable units"[cite: 1]. Our agent monitors trending opportunities, spins up stores/tools, and winds them down automatically when demand drops[cite: 1].
* **Beyond Tooling into Ownership**: The project demonstrates what happens when an agent takes ownership of a commercial operation, making it impossible to tell that no human is running the business[cite: 1].

[Wiktoria Jarema](https://github.com/Irisisme2)

`2026-05-07`

---

### EMO-AI-CHATBOT
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/emoaichatbot-8da7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DevShreyaspai) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> No Limits. Just Intelligence.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

EMO 🤖

> The chatbot with zero limits.

EMO is a handcrafted AI chatbot built to do *anything* you ask — fast, smart, creative, and unrestricted.  
Unlike traditional assistants packed with filters and unnecessary restrictions, EMO is designed for raw interaction, powerful responses, and full customization.

---
⚡ Features

- 🧠 Human-like conversations
- 💻 Coding assistance
- ✍️ Content generation
- 🎨 Creative writing & ideas
- 📚 Answer questions on almost any topic
- 🔥 Minimal restrictions
- ⚙️ Fully customizable personality
- 🚀 Fast response engine
- 🌐 Easy integration with APIs & apps

---

🛠 Built With

- Python
- Node.js
- OpenAI API / Custom LLM
- HTML / CSS / JavaScript
- Pure insomnia and caffeine

---

 🚀 Installation

bash
git clone https://github.com/yourusername/emo-chatbot.git

cd emo-chatbot

npm install or
pip install -r requirements.txt

**Challenges we ran into**

Spent a lot of time going through trial and error before the chatbot finally started working the way I imagined. There were many failed attempts, rewrites, and moments where I had to completely rethink parts of the project.


Finding the right open-source model was surprisingly difficult. I tested multiple models, but many were either too limited, too slow, or didn’t give natural enough responses, so choosing the right one took a lot of patience and experimentation.


One of the hardest parts was building and debugging the codebase on my own. Since I didn’t rely heavily on AI coding assistants like Claude or similar tools, most problems had to be solved manually through research, testing, and persistence.


Maintaining motivation throughout development was also challenging. There were times when errors and failed implementations became frustrating, but continuing to improve the project step by step made the final result much more rewarding.


Balancing performance, customization, and usability at the same time was difficult, because improving one area would often create issues in another, requiring constant adjustments and optimization.

Team **67 Team** -- [Shreyas Pai](https://github.com/DevShreyaspai)

`2026-05-08`

---

### Quorum
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quorum-fdc8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nishnarudkar/Quorum---Multi-Agent-LLM-Trading-Framework) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://quorum-frontend-74691596771.us-central1.run.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vEDSW4zIQs0) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Multi-Agent LLM Trading Framework Powered by LOCUS

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![langchain](https://img.shields.io/badge/langchain-333333?style=flat-square) ![chromadb](https://img.shields.io/badge/chromadb-333333?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square)

**The problem it solves**

Institutional-grade investment research costs thousands per report and takes days. Retail traders rely on single-model AI tools with no adversarial review, no risk committee, and no documented reasoning.

**Quorum** is an autonomous AI trading research firm. Thirteen specialized LLM agents analyze any stock or crypto ticker through:
- **4 parallel analysts** (market, sentiment, news, fundamentals)
- **Adversarial bull vs. bear debate** (2 rounds)
- **Risk committee** with CRO approval
- **Executable trade plan** (entry, targets, stop-loss, sizing)

![image](https://assets.devfolio.co/content/f572f2ed33034281b59c3aa2c72b5073/89828cd2-bef6-4a20-9239-dde378a39f96.png)

Customers pay **$5 USDC** via Locus Checkout and receive a full institutional report in under 5 minutes — with every argument on the record. The agent registers its own wallet, creates checkout sessions, runs the pipeline after payment, and logs revenue with zero human intervention.

![image](https://assets.devfolio.co/content/f572f2ed33034281b59c3aa2c72b5073/8da55c31-7c58-4f4c-a8fd-acac2f6f30a6.png)

**Challenges we ran into**

Orchestrating 13 agents in a LangGraph DAG without token blowups required condensing researcher outputs and tuning debate round limits. Integrating **LocusFounder** end-to-end — wallet registration, USDC on Base, checkout sessions, and post-payment pipeline triggers — took careful async wiring between FastAPI and the agent layer.

We deployed the full stack to **Google Cloud Run** (Next.js frontend + FastAPI backend) and a **BuildWithLocus storefront**, while keeping Groq LLM costs under $0.10 per analysis. The hardest part was making adversarial debate loops converge on actionable, risk-adjusted trade plans rather than generic summaries — solved through structured JSON schemas and a dedicated Research Judge + CRO Judge.

![image](https://assets.devfolio.co/content/f572f2ed33034281b59c3aa2c72b5073/cb21d1fc-26ce-46de-975e-937cb2b67eb5.png)

**Using LocusFounder to Build a Business!**

## Why Quorum fits the LocusFounder track

Quorum is not a tool that helps a founder — **the agents are the founder**. The entire business runs autonomously:

1. **LocusFounder agent** registers a USDC wallet on Base, manages spending controls, and tracks revenue
2. **Locus Checkout** creates $5 payment sessions; analysis runs only after payment confirms
3. **13-agent pipeline** produces and delivers institutional-grade reports with zero human touch
4. **BuildWithLocus storefront** (`svc-mp4160jcaxqzmks9`) is the customer-facing shop

### Real commercial operation
- **Product:** AI trading research reports ($5 USDC each)
- **Unit economics:** ~$0.05–0.10 LLM cost → **>97% gross margin**
- **Live deployment:** Frontend, API, and storefront all publicly accessible

This project demonstrates what happens when an agent *is* the business: it acquires customers, fulfills orders, and settles payments end-to-end through Locus — with no person in the loop.

[Nishant Narudkar](https://github.com/nishnarudkar)

`2026-05-15`

---

### ISPAS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ispac-2dc3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://student-social-media-tracker-3.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Turning Digital Distraction into Academic Action

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Academic procrastination is one of the leading causes of poor performance among students. Excessive social media usage, irregular study patterns, declining attendance, and incomplete assignments often go unnoticed until it is too late for intervention. ISPAS provides a real-time dashboard that continuously monitors student habit data and applies a weighted risk scoring algorithm to classify each student into one of three behavioural profiles — Focused, Moderate, or Distracted. Admins get a full class view, while students can log their own daily habits and track their personal progress.

**Challenges we ran into**

1. Bridging the Data Gap: When a new student first logs in, there is no data to show. A dashboard full of "0%" or empty charts looks broken or unappealing.
I focused on creating a clean User Experience (UX) for the "Empty State." I implemented logic to ensure that the UI remains intuitive and provides clear instructions on how to start tracking data, rather than just showing blank graphs.

![image](https://assets.devfolio.co/content/5f152b0d2f454f62a780a09ce1ba6227/1a67a644-3d3d-4d07-a3d8-944013d697be.png)

![image](https://assets.devfolio.co/content/5f152b0d2f454f62a780a09ce1ba6227/3a663dfa-ce4a-4419-a7e4-24a8834309d4.png)

2. Role-Based Access Control: Ensuring that a student cannot see at other student’s data or access the Admin panel. Managing permissions so that the Admin and Student views stay completely separate while using the same database.
I implemented session management and conditional rendering. By checking the user’s role immediately upon login, the system dynamically serves only the relevant components, keeping the student environment private and the admin environment secure.

![image](https://assets.devfolio.co/content/5f152b0d2f454f62a780a09ce1ba6227/0ec55f13-31bc-4b4b-b06c-622027fe53ef.png)

**Using LocusFounder to Build a Business!**

By using the LocustFounder approach to built a business, we transformed a simple tracker into a Smart Procrastination Analysis System. We identified a critical situation in student success, digital distraction and built a high-speed, low-overhead solution. ISPAS isn't just an app; it's a scalable B2B platform designed to increase institutional retention rates through automated behavioral insights, fitting the LocustFounder model of high-impact, lean business building.

[SAMIKSHA SHUKLA](https://github.com/24shuklas2-create)

`2026-05-15`

---

### Quiz Management System.
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quiz-management-5b5a) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> “Making Online Quizzes Simple and Efficient.”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

My Quiz Management System solves the problem of conducting and managing quizzes manually in schools and colleges. Traditional quizzes take a lot of time to prepare, check, and manage. Teachers have to evaluate answers manually and students often have to wait for results.

This project makes the process faster and easier by providing an online platform where teachers can create quizzes, add questions, and manage student records. Students can attend quizzes online and get results quickly. It also reduces paperwork and saves time for both teachers and students.

The project improves accuracy in result calculation, keeps quiz data organized, and makes learning more interactive and efficient.

**Challenges we ran into**

1. Understanding how to connect the frontend with the backend using Flask was difficult at first.
2. Managing the database and storing quiz questions, student data, and scores properly was challenging.
3. I faced issues while handling user login and session management for students and teachers.
4. Debugging routing errors and fixing template rendering problems took time.
5. Designing the quiz flow, such as moving between questions and calculating scores correctly, was tricky.
6. Making the UI simple and user-friendly while keeping all features functional was another challenge.
7. I also had difficulty organizing project files and understanding how different components work together in Flask.
8. Testing the project and fixing small bugs repeatedly required patience and problem-solving skills.

Kartik Thakur

`2026-05-15`

---

### ForgeOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/forgeos-e01d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://forge-os-dadt-fbq9h9y21-srikrishna-ss-projects.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LZMlSG_eY2I) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The Autonomous AI Business Engine.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

### 🛑 The Problem

Launching and operating a digital services business (SEO, Branding, Marketing, Design, etc.) is highly fragmented, costly, and resource-intensive. Founders and builders face massive roadblocks before ever making their first dollar:
1. **Tool Overload & High Cost:** Setting up storefronts, branding assets, custom checkout portals, customer support chat, and email systems requires a subscription to half a dozen expensive SaaS platforms.
2. **Branding & Strategy Paralysis:** Creating consistent service packages, pricing matrices, unique value propositions, and dynamic brand palettes takes days or weeks of manual research and planning.
3. **Friction in Lead Conversion:** Traditional static landing pages suffer from low conversion rates. Without expensive 24/7 human sales support, potential customers leave without completing a transaction.
4. **Complex Web3 Financial Logistics:** Integrating secure, decentralized payment routing that split-settles revenue directly into designated treasury or founder wallets without high-maintenance intermediary infrastructure is technically daunting.
5. **Operational Fulfillment Friction:** Once a customer pays, executing and delivering custom service bundles (contracts, audits, assets) requires repetitive manual work and prompt attention, leading to delivery bottlenecks.

---

### ⚡ How ForgeOS Solves It

**ForgeOS** is a fully autonomous, decentralized **Multi-Agent AI Business Engine** that democratizes and automates the entire lifecycle of a digital services enterprise. From a single prompt (e.g., *"An elite translation agency"*), ForgeOS instantly architects, deploys, and operates a living SaaS brand in seconds. 

Here is how our specialized multi-agent squad eliminates operational friction:

*   **🏛️ ArchitectAgent (Instant Brand Architecting):** Leverages elite LLM business models (`llama-3.3-70b-versatile` via Groq) to instantly generate brand names, custom UI hex palettes, structured multi-tier service models, target audience definitions, and strategic weekly market insights.
*   **💬 SalesAgent (Conversational Commerce):** Embeds an autonomous sales representative into the storefront that engages visitors in real-time, answers complex service questions, and dynamically creates custom order checkout sessions based on active requirements.
*   **💳 FinanceAgent (Autonomous Revenue Routing):** Connects to the **Locus Checkout Protocol**, enabling trustless, decentralized payments. Once payments are securely settled, they are routed instantly to designated creator wallets, generating live financial dashboard metrics showing MRR, revenue splits, and active transactions.
*   **📦 FulfillmentAgent (Zero-Overhead Delivery):** Instantly synthesizes professional-grade digital deliverables upon successful payment. It generates high-value, structured business development roadmaps (PDF/Markdown) and uses automated SMTP protocols to deliver them directly to the buyer's inbox.
*   **🖥️ Fully-Observable Admin Dashboard:** Demystifies the "black box" of AI. The platform provides complete architectural transparency with a live telemetry feed showing real-time agent logs, system heartbeats, and exact agent thought processes.

With **ForgeOS**, a single developer or non-technical creator can launch a fully functional, payment-enabled, customer-serving business in under 60 seconds with zero upfront operational costs.

**Challenges we ran into**

### 🧠 1. LLM JSON Parsing & Structural Consistency
* **The Hurdle:** Having multiple independent AI agents (like `ArchitectAgent` and `FulfillmentAgent`) generate complex, structured deliverables (such as entire business plans with nested services, hex color codes, and detailed multi-phase development roadmaps) occasionally caused `JSON.parse` exceptions. The underlying `llama-3.3-70b-versatile` model would occasionally wrap its output in Markdown block fences (` ```json `) or append conversational preamble/postscript text.
* **How I Fixed It:** I engineered strict system instructions with precise, zero-fluff schema definitions and implemented a robust regex-based sanitization pipeline. By using a pre-parsing cleanup regex (`text.replace(/```json|```/g, '').trim()`), the backend safely strips any formatting anomalies before passing the raw string to the JSON engine, resulting in a 100% parse success rate.

---

### ⚡ 2. Ephemeral Storage on Serverless Deployments (Vercel Container Resets)
* **The Hurdle:** When deploying **ForgeOS** to modern cloud hosting platforms like Vercel, the local JSON database (`database.json`) is ephemeral. Serverless instances automatically spin down and reset, meaning that newly generated businesses, agent logs, and transaction orders would suddenly vanish whenever the server container restarted.
* **How I Fixed It:** To provide a rock-solid user experience without setting up complex database clusters for a hackathon demo, I built a hybrid client-state sync pattern. The React frontend constantly caches the active business metadata inside `localStorage`. On application boot or whenever a state mismatch is detected, the frontend triggers a quiet `/api/business/restore` API call to automatically push the client state back up to the fresh backend container. This ensures the app is incredibly stable and persistent, even in serverless environments.

---

### 💳 3. Web3 Payment Webhooks & Local Sandbox Testing
* **The Hurdle:** Integrating the **Locus Checkout Protocol** for real-time payments required verifying live cryptographic signature headers (`locus-signature`) and handling active webhook callbacks. Testing this end-to-end in local development sandboxes (behind dynamic `localhost` ports) made offline debugging and quick demo walk-throughs highly complex.
* **How I Fixed It:** I architected a dual-mode engine in the `FinanceAgent`. The backend automatically detects if it is running in `DEMO_MODE` or live production. In demo mode, it bypasses network-level webhook roadblocks by using a secure payment simulator that exactly mirrors the cryptographic signatures and data payloads of the Locus Checkout network. This allowed me to comprehensively test the entire autonomous pipeline (from payment confirmation to immediate multi-agent fulfillment) locally, while maintaining direct production compatibility.

**Using LocusFounder to Build a Business!**

**ForgeOS** is the ultimate representation of the *"Using LocusFounder to Build a Business"* track. Instead of just building a single business, we built an **autonomous engine** that can architect, launch, and operate *hundreds* of independent, revenue-generating digital services agencies—all powered and financially enabled by **Locus**.

Locus is not just an add-on payment gateway in our project; it is the **essential financial spine** that makes the entire autonomous pipeline possible. Here is how **ForgeOS** leverages Locus to build and scale businesses:

1. 💳 **Decentralized & Automated Checkout (`Locus Checkout API`):**
   When our `SalesAgent` successfully pitches a service and converts a visitor, it immediately requests the `FinanceAgent` to initialize a checkout. We integrate directly with Locus (`/checkout/sessions`), passing the dynamically calculated order amounts, currency, and custom metadata (linking `orderId`, `businessId`, and `serviceId`). This creates a secure checkout portal that routes revenue directly to the creator's Locus Wallet.

2. 🪢 **On-Chain Webhook Automation (`checkout.completed`):**
   Traditional platforms require manual intervention to verify payments before sending deliverables. ForgeOS leverages Locus Webhooks. The moment Locus triggers the secure `checkout.completed` event callback, our backend immediately validates the transaction signature, confirms the order as paid, and auto-triggers the `FulfillmentAgent` to generate the custom business roadmap and deliver it directly to the customer's inbox within seconds. 

3. 📊 **Real-Time Financial Telemetry (`Locus Wallet API`):**
   Our fully-observable Admin Dashboard hooks directly into Locus Wallet endpoints (`/wallets/{wallet_id}`) to retrieve real-time financial telemetry—including active balances, total earnings, and pending payouts. We render this on a sleek developer UI alongside active agent logs, giving business owners a unified control room showing exactly how much revenue their AI agents are autonomously generating.

By combining the cognitive intelligence of **Groq / Llama-3.3** with the trustless, low-friction settlement layer of **Locus**, **ForgeOS** shows the true future of decentralized, AI-driven digital commerce.

[SRIKRISHNA S](https://github.com/SRIKRISH-S)

`2026-05-17`

---

### HireMind AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hiremind-ai-9b52) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saikushal06/hiremind-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hiremind-ec221h1mz-saikushal06s-projects.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> From Resume to Offer Letter — Guided by AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square)

**The problem it solves**

Students often struggle to build ATS-friendly resumes, identify missing skills, prepare for interviews, and understand their placement readiness. Most students do not receive personalized career guidance or actionable feedback before applying for jobs.

HireMind AI solves this problem using AI-powered resume analysis. The platform helps students upload resumes, receive ATS feedback, identify skill gaps, get AI-generated suggestions, and improve interview preparation in one place.

**Challenges we ran into**

While building HireMind AI, I faced several challenges involving PDF resume extraction, Gemini API integration, deployment security, and API quota handling.

One major issue was extracting resume text correctly from uploaded PDF files using PDF.js. Another challenge was handling Gemini API errors and free-tier quota limitations gracefully without breaking the user experience.

I also learned how to securely manage API keys using environment variables and deploy the project safely on Vercel without exposing sensitive credentials publicly on GitHub.

These challenges helped me understand real-world AI product development workflows including debugging, deployment, frontend-backend communication, and production security practices.

**Using LocusFounder to Build a Business!**

HireMind AI fits perfectly into the “Using LocusFounder to Build a Business” track because it is designed as an AI-powered career guidance platform that solves a real-world problem faced by students and job seekers.

The platform uses AI to analyze resumes, identify missing skills, provide ATS optimization suggestions, and help users prepare for interviews. It combines resume intelligence, AI career coaching, and placement readiness into a single product experience.

HireMind AI has strong potential to grow into a scalable SaaS business for students, colleges, and placement preparation platforms. The project focuses on improving employability using AI-driven insights and personalized recommendations.

[SAI KUSHAL](https://github.com/saikushal06)

`2026-05-18`

---

### RiskLens AI - Disaster Intelligence Mesh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/risklens-ai-disaster-intelligence-mesh-3e37) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/adrinathsbinod/RiskLens-AI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=F44cdTHwPr8) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Intelligence at the speed of risk

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

### 🌐 The Supply Chain Blindspot
Global supply chains lose billions of dollars annually to unexpected logistics bottlenecks—from sudden flash floods and typhoon-induced port closures to regional labor disputes and infrastructural failures. 

Traditional logistics tracking and alerting systems suffer from three critical flaws:
1. **Lagging Telemetry (Reactive, not Proactive):** Most platforms only notify logistics managers *after* a port has already shut down or a vessel has spent hours anchored in congestion. 
2. **Language & Regional Blindspots:** Critical micro-disruptions are often reported first in hyper-local news, regional police scanners, or non-English social channels (OSINT). Standard global scrapers miss these signals entirely until they are officially translated hours later.
3. **Lack of Actionability ("Alert Fatigue"):** Standard systems flood inboxes with generic warnings (e.g., *"Heavy rain in Shanghai"*), leaving logistics teams to manually decipher which shipments are actually affected and how they should be rerouted.

---

### ⚡ How RiskLens AI Solves It
**RiskLens AI** turns raw, unstructured global hazard data into immediate, automated supply chain action. It makes monitoring global logistics safer, faster, and highly predictive:

#### 1. Real-Time Predictive Telemetry (Aggregated Intelligence Mesh)
Rather than relying on delayed commercial databases, RiskLens AI builds a live intelligence mesh. It ingests and correlates satellite weather telemetry, maritime transponders (AIS), and hyper-local infrastructure feeds onto a single **geographically locked coordinate map**. It forecasts disruptions **hours before they occur**, allowing companies to act ahead of the storm.

#### 2. Multi-Lingual Hyper-Local OSINT Ingestion
Our ingestion engine monitors local regional feeds, translating native languages in real-time. By bridging regional communication barriers, RiskLens AI identifies micro-level disruptions (such as flash floods on a secondary highway or sudden custom delays at a specific dock) long before they reach mainstream news.

#### 3. Closed-Loop Automated Routing & ERP Integration
RiskLens AI eliminates "alert fatigue" entirely by moving from warning to resolution:
* **Corridor Correlation:** It maps active threat coordinates directly against your specific logistics corridors.
* **Instant Dynamic Rerouting:** When a disruption is detected, it automatically computes optimal alternate maritime or terrestrial transit routes.
* **Direct Webhook Integrations:** Instead of sending an email that sits in an inbox, it dispatches structured payload updates directly into enterprise ERP databases (like SAP or Oracle) via webhooks to update routes automatically without requiring manual human triage.

---

### 💼 Practical Business Impact
* **Reduces Operational Risk:** Protects high-value, time-sensitive shipments (e.g., pharmaceuticals, cold chain retail, automotive parts) from expensive delays.
* **Proactive ROI Savings:** An interactive risk engine demonstrates how resolving just a single major shipping bottleneck per quarter easily pays for the platform's yearly deployment.
* **Enables Scalable Logistics:** Minimizes human error by replacing manual spreadsheet tracking with a fully automated, responsive crisis management workflow.

**Challenges we ran into**

### 🗺️ The Responsive SVG Map "Drift Bug" (Coordinate Mismatch)
The single biggest technical hurdle we encountered was ensuring that the active threat nodes (pulsing coordinates) on our **Global Threat Monitor** stayed perfectly aligned with their actual geographical locations on our Robinson projection world map across all screen sizes and resolutions.

#### The Problem: HTML Overlays on Fluid SVG Containers
Initially, the pulsing threat nodes were built as standard HTML `div` elements, absolutely positioned using CSS percentage offsets (e.g., `left: 83.7%; top: 34.8%`) on top of the map's parent container. 

However, because the world map is a highly detailed inline SVG with a fixed coordinate aspect ratio (`viewBox="0 0 500 280"`), the browser scaled it natively to preserve its aspect ratio. Meanwhile, its outer HTML container was fully fluid and responsive, featuring a `24px` horizontal padding. 

This created a **layout coordinate drift**:
* When the viewport aspect ratio changed (e.g., on a wide 4K monitor, a narrow tablet, or a mobile screen), the SVG map would letterbox vertically or scale within the container, but the absolute HTML divs would scale strictly according to the fluid container's box bounds.
* As a result, threat nodes would "drift" completely away from their actual landmasses. An alert for the **Port of Shanghai** that was perfectly aligned on a 1080p laptop would drift far out into the Pacific Ocean on a widescreen monitor or scale up into Siberia on mobile. Furthermore, they drifted away from our SVG route indicator lines.

---

### 🛠️ How We Overcame It

To solve this, we re-engineered our dashboard map layout with a two-part architectural fix:

#### 1. Locking Threat Nodes into the Inline SVG Namespace
We abandoned HTML overlay elements entirely. Instead, we re-wrote our threat node creation engine in JavaScript to build native SVG groups (`<g>`, `<circle>`, `<animate>`) using the correct SVG XML namespace (`http://www.w3.org/2000/svg`). 

These nodes were then appended **directly inside the inline map SVG’s DOM tree**, locking their positions into the map's coordinate system:
* **Port of Shanghai:** Geographically locked to exact SVG coordinates (`x: 418.5, y: 97.4`).
* **I-95 Corridor, USA:** Locked to `x: 145.5, y: 80.1`.

Because they are now native children of the SVG, the browser scales them natively and proportionally in unison with the map landmasses and routing curves. **Zero coordinate drift is mathematically guaranteed across all screen widths.**

#### 2. Dynamic Viewport calculations for Glassmorphic Tooltips
Moving nodes inside the SVG coordinate system meant they were no longer bound by traditional HTML absolute box models, which made showing standard HTML hover tooltips difficult. 

We resolved this by using a high-precision runtime calculation. When a user hovers over an alert in the feed list, the script runs `getBoundingClientRect()` on the dynamic SVG node group. It computes the node's exact micro-pixel coordinates relative to the viewport container and dynamically positions the floating tooltip directly above it in real-time. 

This ensures that the sleek, glassmorphic hover tooltips snap beautifully into position on any responsive column layout or zoom scale!

**Using LocusFounder to Build a Business!**

### 🚀 Building a High-Ticket B2B SaaS Business with LocusFounder
**RiskLens AI** was designed from the ground up not just as a technical tool, but as a highly viable, commercially optimized **B2B SaaS business** targeting high-ticket logistics and supply chain enterprise accounts (with subscriptions starting at **$1,499/month**). 

Here is how RiskLens AI integrates with and leverages the core capabilities of the **LocusFounder** business launch ecosystem:

---

#### 1. A High-Converting, Credible Digital Frontstore
To build a successful business, you need an online presence that immediately commands authority. RiskLens AI features a custom, high-fidelity landing page with a premium, high-trust visual language (Palantir × Stripe aesthetic). 
* **Trust & Compliance Anchors:** Built-in compliance grids highlighting **SOC 2, GDPR, ISO 27001**, and SLA uptime benchmarks establish the enterprise credibility needed to drive conversions on the storefront.
* **Interactive Visual Value:** We replaced complex, developer-centric documentation with a visual **Automated Crisis Router Flow Card**, allowing corporate business buyers to instantly grasp the product's value.

#### 2. Driving Checkout Conversions via the Interactive ROI Lead Magnet
One of the hardest parts of launching a new SaaS is demonstrating immediate financial value to prospects. 
* We integrated an **Interactive ROI Risk Exposure Calculator** directly into the core landing page.
* Corporate buyers can input their shipment volumes and average cargo values to dynamically compute their annual risk exposure.
* Showing a buyer their exact **$1.25M+ in exposure** and proving that the tool pays for itself if it prevents just one quarterly incident creates a highly persuasive argument that directly feeds into **Locus Checkout**, significantly boosting checkout conversion rates.

#### 3. Capturing Enterprise Leads for the Locus CRM & Pipeline
Enterprise deals require high-touch sales. 
* The landing page features a validated, high-fidelity **Demo Booking Form** designed to collect valuable lead data (work email, company name, monthly volume ranges).
* In our live business setup, these captured leads seamlessly flow directly into **LocusFounder's automated pipeline and CRM** to trigger personalized sales follow-ups, initiate automated cold email sequences, and nurture corporate accounts from interested prospects into paying customers.

#### 4. Scalable Pricing & Recurring Business Model
We established a clear, structured pricing matrix (Core Tier vs. custom Enterprise Tier) designed to capture diverse market segments:
* **The Core Tier ($1,499/mo)** is structured for standard automated checkout using **Locus Checkout** for self-serve onboarding.
* **The Enterprise Tier** funnels larger logistics accounts with complex ERP integration requirements into high-value custom sales contracts, maximizing average contract value (ACV) and recurring revenue.

Team **Greninja** -- [Adrinath S Binod](https://github.com/adrinathsbinod)

`2026-05-20`

---

### Echo: The Agentic CFO
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/echo-the-agentic-cfo-5839) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/teja739/echo-agentic-cfo/tree/main/annotated_doc-0.0.4.dist-info) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> TITANS

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Freelancers and independent professionals often waste countless hours juggling fragmented financial tools and chasing down late payments—a process that is notoriously awkward, time-consuming, and detrimental to cash flow. Echo: The Agentic CFO solves this by transforming passive financial tracking into active, automated recovery and management.

Specifically, Echo tackles three major pain points:

The Friction of Debt Collection: Chasing overdue invoices is uncomfortable and inefficient. Echo's Outbound Voice Collector eliminates this burden by deploying an AI agent to call clients on your behalf. It politely negotiates terms, resolves billing blockers (like missing invoice emails), and securely captures funds via SMS links in real-time.

Fragmented Workflows: Instead of using separate tools for CRM, expense tracking, and invoicing, Echo centralizes the entire financial pipeline. It brings lead workflows, expense auditing, and outbound collections into a single, unified dashboard.

Manual Administrative Overhead: Tracking expenses and analyzing outstanding Accounts Receivable (AR) manually drains valuable time. Echo automates expense auditing and dynamically updates recovery rates and AR as soon as the AI agent secures a payment.

**Challenges we ran into**

Building Echo required bridging a modern React frontend with a Python backend while simulating real-time AI interactions. Here are the main hurdles and how they were solved:

Simulating the Real-Time Voice Agent Experience: One of the biggest challenges was making the "Dispatch Agent" modal feel like a live, ongoing phone call rather than a static loading screen.

The Fix: We implemented a mock protocol to stream log lines sentence-by-sentence (e.g., “Connecting SIP trunk...”, “Client answered...”) into a terminal-style modal. Pairing this with a pulsing audio visualizer created an immersive, real-time feel for the demo.

Instant UI State Mutations: After the AI agent successfully "negotiates" and captures a payment, the dashboard needed to reflect the new financial reality immediately without requiring the user to refresh the page.

The Fix: We had to carefully manage our React state. Once the modal completes its sequence and closes, we trigger a callback that instantly updates the local state for the Outstanding Accounts Receivable, dynamic recovery rates, and the specific invoice badge (from Overdue to Paid).

Bridging FastAPI and Vite:
Setting up clean communication between the Python (FastAPI) backend and the React frontend required careful CORS configuration and Pydantic schema validation to ensure the data flowing into our dashboard cards was strictly typed and error-free.

**Using LocusFounder to Build a Business!**

Echo: The Agentic CFO fits perfectly into the "Build a Business" track because we designed it from day one as a scalable, monetizable B2B SaaS product, not just a technical prototype.

Cash flow is the number one killer of freelance businesses. By automating the uncomfortable and time-consuming process of debt collection via our AI Voice Agent, Echo provides immediate, measurable ROI for its users—a core requirement for a successful business model.

To bridge the gap between a hackathon project and a market-ready business, we leveraged LocusFounder to [INSERT EXACTLY HOW YOU USED THEM HERE - e.g., handle our core infrastructure deployment / manage our multi-tenant SaaS architecture / streamline our backend business logic].

Relying on LocusFounder provided the stable foundation we needed to rapidly scale our platform. It allowed our team to spend less time worrying about boilerplate setup and more time refining our unique value proposition: the real-time AI voice collection engine.

Team **saiamruth347@gmail.com** -- AKULA NAGA SIVA TEJA

`2026-05-25`

---

### ShelfMind AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shelfmind-ai-the-intelligent-operating-system-for-modern-retailers-0ccb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Armantech10/shelfmind-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shelfmind-ai.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> TheIntelligent OperatingSystemfor ModernRetailers

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Retail businesses, especially small and medium retailers, often struggle with inventory mismanagement, product wastage, inaccurate demand forecasting, and lack of real-time business insights. Most stores still rely on manual tracking or basic software that only stores data but does not provide intelligent decision-making support.

This leads to several problems:

* Overstocking of low-demand products
* Stock shortages of high-demand products
* Expired or wasted inventory
* Revenue loss due to poor forecasting
* Lack of understanding of customer buying behavior
* Time-consuming manual management processes

ShelfMind AI solves these challenges by acting as an intelligent retail operating system powered by AI and predictive analytics.

The platform helps retailers:

* Predict future product demand using AI
* Receive smart restocking recommendations
* Track inventory in real time
* Detect products nearing expiry to reduce waste
* Analyze customer purchasing patterns
* Improve operational efficiency and profitability

Instead of reacting after losses occur, retailers can make proactive, data-driven decisions using ShelfMind AI.

The system makes retail management easier, smarter, and more efficient by automating complex analysis and converting raw retail data into actionable business insights.

**Challenges we ran into**

One of the biggest challenges we faced was building an accurate and reliable AI demand forecasting system using limited retail datasets. Retail data is often inconsistent, noisy, and changes rapidly due to customer behavior, seasonal trends, and product popularity.

Initially, our prediction model produced unstable forecasts because the inventory and sales data were not properly normalized. Some products had missing entries while others had irregular sales patterns, which affected model accuracy.

To solve this, we:

* Cleaned and preprocessed the dataset carefully
* Implemented data normalization and filtering techniques
* Used historical trend analysis to improve prediction stability
* Optimized the ML pipeline to handle fluctuating retail patterns

Another major hurdle was maintaining real-time inventory synchronization between the frontend dashboard and backend database. During testing, inventory updates occasionally caused delayed or duplicate stock values.

We overcame this by:

* Using Firebase real-time database synchronization
* Implementing proper API validation and state management
* Creating optimized update handlers to avoid duplicate writes

We also faced UI/UX challenges while designing a dashboard that non-technical retailers could easily understand. We simplified the interface by focusing on visual analytics, alerts, and actionable recommendations instead of complex technical data.

These challenges helped us improve our understanding of scalable AI systems, real-time architecture, and user-centered product design.

**Using LocusFounder to Build a Business!**

ShelfMind AI combines AI, predictive analytics, and automation to solve real-world retail management problems. The project fits into AI/ML, RetailTech, SaaS, and Data Analytics tracks because it uses intelligent forecasting, real-time inventory analysis, and automated business insights to help retailers optimize operations and reduce losses. The platform also aligns with Cloud and Automation tracks due to its scalable architecture and real-time decision-making capabilities.

[SK ARMAN](https://github.com/Armantech10)

`2026-05-24`

---

### AutoProcure
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/autoprocure-e46a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://auto-procure-omega.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Procure with precision.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Reactstrap](https://img.shields.io/badge/Reactstrap-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React Router](https://img.shields.io/badge/React%20Router-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

## The problem it solves

  Procurement is still a messy, manual workflow for indie builders and small teams. When someone needs tools, APIs, software credits, or vendor services, they
  usually have to research options, compare pricing, check trust and fit, stay within budget, get approval, make the payment, and then document what happened.
  That process is slow, easy to forget, and risky when decisions are made ad hoc.

  AutoProcure OS turns that into a single intent-driven workflow. A user can describe what they need in plain language, and the agent handles vendor discovery,
  ranking, policy checks, payment drafting, and audit logging. Instead of jumping between spreadsheets, websites, chats, and payment tools, teams get one system
  that moves from request to execution in a structured way.

  People can use it for:

  - Buying startup tools and SaaS within a fixed budget
  - Comparing vendors before making a purchase
  - Enforcing internal spending rules automatically
  - Drafting agent-ready payments through Locus
  - Keeping a complete audit trail of who requested what, why it was approved, and how it was paid

  This makes procurement faster by removing repetitive research and admin work, safer by adding budget controls, approval thresholds, and auditable logs, and
  easier by letting users start with a simple request instead of a complex purchasing process.

  For small teams, agencies, and autonomous businesses, it acts like an always-on procurement operator: one that helps prevent overspending, reduces decision
  friction, and makes every purchase traceable.

**Challenges we ran into**

## Challenges I ran into

  One of the biggest hurdles was making the project feel like a real autonomous procurement pipeline instead of just another chatbot with a payment button. It
  was easy to describe the idea at a high level, but much harder to turn it into a believable step-by-step flow: intent parsing, vendor discovery, ranking,
  budget checks, payment drafting, approval, and audit logging. I solved that by breaking the system into explicit workflow stages and building the UI around
  those stages so users can see exactly what the agent is doing at each step.

  Another challenge was integrating the Locus payment flow cleanly without making the product feel unsafe or custodial. Since this project deals with money
  movement, I had to make sure the design emphasized guardrails like approval thresholds, budget checks, and non-custodial execution. I got around this by
  separating procurement intelligence from payment execution, then adding a clear approval layer before any transfer is finalized.

  I also ran into a practical product challenge: procurement data is messy, but a hackathon demo still needs to feel fast, visual, and reliable. To solve that,
  I created a structured demo workflow with vendor ranking, risk scoring, and audit logs that make the system understandable even in a short walkthrough. That
  helped balance technical clarity, trust, and demoability without losing the core idea.

**Using LocusFounder to Build a Business!**

AutoProcure OS fits the LocusFounder track because it is not just an assistant layered onto a business workflow. The agent itself acts as the business: it
  receives procurement intent, researches vendors, applies budget and policy checks, drafts Locus-powered payments, and maintains an auditable execution trail.
  It is designed as autonomous purchasing infrastructure with a clear revenue model, which matches the core idea of agents that can operate as independent
  businesses.

[bappaditya kuilya](https://github.com/Bappaditya-kuilya)

`2026-05-22`

---

### Crambleeggo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/crambleeggo-d7f9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kanishkaapatra/Crambleeggo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mpjjx505gwrbphkz.buildwithlocus.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/g0vfjH5zH9E) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The agency that sells, delivers, and pays itself

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Freelancing has three brutal bottlenecks — finding clients, doing the work, and getting paid. Traditional agencies solve the first problem by hiring salespeople, the second by hiring creatives, and the third by hiring accountants. Crambleeggo collapses all three into a single automated pipeline. A one-person operation can now run what looks and feels like a full-service creative agency, with zero overhead, zero staff, and zero manual work per order.

**Challenges we ran into**

Orchestrating four agents without a framework. Getting Sales, Checkout, Delivery, and Finance to hand off cleanly in the right order, with shared state required building a lightweight state machine from scratch inside a single React component. No LangChain, no AutoGen, just careful async logic.
Making the delivery actually useful. The hardest agent to get right was Delivery. Early prompts produced vague, generic output. The fix was forcing the prompt to be explicit: no meta-commentary, no "here's what I'll write" - just the real deliverable, minimum 300 words, professional quality.
Parsing AI-generated JSON reliably. The Checkout and Finance agents needed to return structured data, but language models occasionally wrap JSON in markdown fences or add commentary. We had to build a fallback parser that strips formatting and gracefully degrades to safe defaults when parsing fails.
Keeping it all in one file. The entire app four agents, live dashboard, embedded checkout, animated chat, state machine ships as a single React component. No backend, no database, no auth layer. That constraint forced every design decision to be tight and deliberate.

[Kanishkaa Patra](https://github.com/kanishkaapatra)

`2026-05-24`

---

### GymFlow AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gymflow-ai-c231) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mphy986qgckavo9g.buildwithlocus.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=ZL8cYx1eAUg) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The complete AI autopilot for local gyms.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Local gym owners (especially in tier-2 and tier-3 markets) typically manage their businesses using a chaotic mix of paper registers, Excel sheets, and personal WhatsApp messages. This manual approach creates three massive operational bottlenecks:

* **Silent Churn:** Members stop showing up, but because attendance lives in a physical notebook, the owner doesn't realize it until the member's subscription completely expires and they've already joined a competitor. 
* **Lead Leakage:** Inquiries via Instagram DMs or WhatsApp often come in late at night. By the time the owner replies the next morning, the prospect has already booked a trial at another gym.
* **Zero Data Clarity:** Revenue, active member counts, and renewal dates are scattered across different platforms, making it impossible to get a clear picture of the business's health without hours of manual cross-referencing.

---

## What People Use It For

Gym owners use [GymFlow AI](https://svc-mphy986qgckavo9g.buildwithlocus.com/?id=0) to effectively "hire" a 24/7 digital management team for a fraction of the cost of a single human staffer. The platform is utilized for:

* **Instant Lead Conversion:** Automatically replying to pricing inquiries and booking trial sessions on WhatsApp and Instagram within 30 seconds, 24/7, in both Hindi and English.
* **Automated Member Retention:** Tracking member check-ins via QR code and deploying targeted WhatsApp nudges to lapsed members (e.g., a "we miss you" text on day 7, a win-back offer on day 14).
* **Effortless Renewals:** Sending automated payment reminders and generating invoices so the owner doesn't have to awkwardly chase down members for pending fees.
* **Social Media Marketing:** Generating weekly Instagram captions, festival campaigns, and promotional offers to keep the gym's online presence active without brainstorming content from scratch.

---

## How It Makes Existing Tasks Easier & Safer

* **Replaces Manual Data Entry:** Eliminates the need to manually log attendance or copy-paste lead details from Instagram into a spreadsheet. Everything is centralized in the "Autopilot" dashboard.
* **Protects Revenue:** It acts as a safety net for the business's bottom line. By automatically catching "ghosting" members before they fully churn, it actively recovers revenue that would have otherwise slipped away.
* **Centralizes Communication Securely:** By plugging directly into a WhatsApp Business API, owners no longer need to use their personal WhatsApp numbers for hundreds of member chats. All communications are logged safely in the system.
* **Frees Up the Owner's Time:** Ultimately, it takes the gym owner out from behind the front desk and puts them back on the gym floor, allowing them to focus on training, building relationships, and growing the business rather than doing administrative paperwork.

**Using LocusFounder to Build a Business!**

GymFlow AI is a perfect fit for the "Using LocusFounder to Build a Business!" track because it is a highly scalable, revenue-ready micro-SaaS—not just a technical experiment.

Solves a Real Problem: It directly fixes "silent churn" and lead leakage for local gyms.

Immediate Monetization: It features a clear B2B subscription model (₹1499/month), proving a high willingness-to-pay.

Zero-Overhead Operations: Most importantly, it operates as a completely end-to-end AI agent-controlled business.

Rohit Yadav

`2026-05-24`

---

### LocusPilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/locuspilot-ab3a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Akashcc702/Asset-Manager/tree/main) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://asset-manager--akashcc62.replit.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/WP1DODC3AEk) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Turn natural instructions into AI-powered payments

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Digital sellers, freelancers, and creators often need to collect payments for notes, files, services, or milestones, but the process is still fragmented and manual. They usually have to create a checkout, monitor payment status, and handle delivery separately, which slows down small payment workflows and creates room for mistakes.

LocusPilot solves this by turning a plain-English instruction into a complete agentic payment flow. The seller describes what they want, the agent parses the intent, creates the payment request, tracks the payment, and automatically triggers the post-payment action


![image](https://assets.devfolio.co/content/01b69114bb1c45199a61d3b22bc40d0d/1bdb68cf-1892-4a71-ac2f-50084b8d5f5d.png)

**Challenges we ran into**

One challenge was making the agent flow feel intelligent while keeping the demo reliable and easy to test. I solved this by using a deterministic intent parser for the hackathon submission, which made the behavior predictable and stable during live demos.

Another challenge was separating the mock checkout flow from the future real CheckoutWithLocus integration. I kept the integration inside a single adapter seam, so the app can run in mock mode for the demo while still showing exactly where real API calls and webhook verification will plug in later.

A third challenge was handling dashboard reporting and multi-currency display in a clear way. Instead of summing different currencies into one misleading total, I changed the UI to show per-currency totals and added clearer labels so the dashboard stays honest and easy to understand.

**Track: Checkout with Locus**

Agentic Payments

CheckoutWithLocus

Akash Chandu

`2026-04-26`

---

### PayGentic AI — Autonomous Payment Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/paygentic-ai-autonomous-payment-agent-c908) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://pay-gentic-ai-autonomous-payment-ag.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=5UpC0bCnSk0) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> PayGentic: Your Intelligent Command Center

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

- Traditional payment dashboards are reactive, cluttered, and require manual oversight. Merchants struggle with complex API configurations, delayed fraud detection, and fragmented data across different payment methods.
- PayGentic AI transforms payment management from a manual task into an autonomous experience.
1. - Natural Language Payments: Merchants can process transactions or generate reports by simply talking to the Neural Agent, eliminating the need to learn complex UI menus.
2. - Autonomous Fraud Mitigation: Using AI-driven velocity checks and IP blocking, PayGentic proactively secures funds before a breach occurs.
3. - Intelligent Routing: It leverages the Locus CheckoutWithLocus API to route payments through the most efficient channels, ensuring higher success rates and lower fees.
4. - Real-time Analytics: Provides a sub-second latency global ledger that exports data instantly for accounting.

**Challenges we ran into**

1. Real-time State Syncing: One of the biggest hurdles was synchronizing the AI agent’s natural language processing with the actual state of the Locus payment node. We overcame this by building a robust backend relay that translates intent into structured API calls.
2. Futuristic UI Performance: Implementing complex glassmorphism and mesh gradients without using bulky libraries like Tailwind was a challenge. We opted for Vanilla CSS to maintain maximum performance and fine-grained control over every pixel.
3. Monorepo Deployment: Deploying separate frontend and backend environments from a single repository to Vercel and Render required specific root-directory configurations and environment variable mapping to ensure secure communication.
4. Scanner Logic: Synchronizing the "Locus Scanner" animation with the backend response time required precise timing and state management in React to make the encryption feel real to the user.

**Track: Checkout with Locus**

Locus Paygentic Track (Week 3): Utilizing the CheckoutWithLocus API to build an AI-driven merchant experience.

[Rani Rajpurohit](https://github.com/Rani-s123)

`2026-04-27`

---

### Locus Estate AI Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/house-price-prediction-app-48fe) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ravi27yadav/ravi27yadav-house-price-prediction-app) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ravi27yadav.github.io/ravi27yadav-house-price-prediction-app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Autonomous AI Agent that predicts prices and secur

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

Buying or investing in real estate is often difficult due to a lack of accurate and data-driven price estimation.

People usually rely on guesswork, agents, or outdated information, which can lead to overpricing or poor investment decisions.

This project solves that problem by providing an AI-based system that predicts house prices instantly based on key features like income, location, population, and housing characteristics.

It helps users make informed decisions by giving a quick and reliable estimate of property value.

By automating the prediction process, the app reduces manual effort, increases accuracy, and makes real estate decision-making more efficient and accessible.

**Challenges we ran into**

During development, I faced multiple practical challenges.

One major issue was handling user input correctly. Initially, the model produced errors because the input format did not match the trained feature structure. I resolved this by converting user inputs into a properly structured DataFrame aligned with the model’s feature names.

Another challenge was improving model performance. The initial Linear Regression model gave lower accuracy, so I upgraded to a Random Forest Regressor, which significantly improved the R² score and overall prediction quality.

I also faced issues during deployment, such as dependency management and ensuring the app runs smoothly on Streamlit Cloud. These were resolved by carefully managing requirements and testing the app locally before deployment.

These challenges helped me understand real-world ML deployment and debugging more effectively.

**Track: Checkout with Locus**

This project aligns with the Locus track by demonstrating intelligent decision-making using machine learning.

The system predicts house prices based on multiple real-world factors such as income, location, and population, helping users make data-driven decisions in real estate.

Similar to how Locus optimizes logistics and routing decisions using AI, this project uses predictive modeling to optimize property valuation and assist users in making informed investment choices.

The application showcases how AI can be applied to solve real-world problems by improving accuracy, efficiency, and decision-making processes.

Team **Rule Breakers** -- [Rudraksh Manhas](www.github.com/Rudraksh1405), Ravi Yadav

`2026-04-27`

---

### Interent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/interent-b428) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/youvandra/Interent) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://interent.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JCapXtF2ZTI) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Inter Connected Agent

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square) ![Checkout-React](https://img.shields.io/badge/Checkout--React-333333?style=flat-square)

**The problem it solves**

**Introduction**
In this AI era, it is very possible to do anything with AI. But sometimes, we need more than one AI Services to handle specific things, and it would be very pricey for users to subscribe more than one AI Services.
This is where **Interent** comes. What happens when a specific task thing could be replaced by an AI, not one but multiple microservices agents? Without any subscription just pay-per-use.

**Pain Point We Focused For**
- User needs to **subscribe more than one AI Services**, this would cost them huge amount of money.
- Usually, the **minimum subscription is per month**.
- If users don’t like the result of AI Service, they need to cancel the subscription. Yes some services offer free trials, but most likely **with commitment**, and then what happens when user forget those subscriptions?
- **Switch between AI Services does not move flawlessly** if users need more than one AI Services.

**Use Case and Our Solution**
A user came into our website with certain goal in their mind.
“I would like to scrape data related to Disease Outbreak in Indonesia at 2025, while at it, I would like to extract the disease data and also translate them to English, so I do not need to do all the things by myself”
With the "*old way*" user might need to subscribe **these AI Services separately**:
- Website Scrapper AI
- Translation AI
- AI / LLM for Report

With **Interent**, instead of subscribing to each services and not feeling satisfied, instead the users can use our recommendation agents, or mix and match the agents and create from there until they meet satisfied result, just pay-per-use, no commitment, no subscription.

**Demo Video**
Demo Video - User Side: https://youtu.be/eEZoujn6VzQ
Demo Video - Agent Side: https://youtu.be/tKPsfZtr1Bk

**Challenges we ran into**

- The short time is our biggest challenge
- We cannot apply $0 amount in locus checkhout feature for bulk testing
- In our front end, we tried to make payment with locus, but it seems the hackaton credit cannot be used in our front end. We tried to top up by ourself, the address is invalid, so in our video demo, we did show on how to make a payment, but we continue the process with promo instead (only in the front end), in the backend, the process of payment with locus continue like expected.

**Track: Checkout with Locus**

Our solution is like **one stop service**, where we **handle communication** between agents and **also the fee calculation (AI Agent Fee and App Fee)**. To answer the pain points that user faces, our solution is offering pay-per-use while the AI Agents move automatically from one flow to another. To facilitate such event, our solution needs a “*way of payment*” where it could be understandable by machine for the service fee payment. It’s like **our solution is gathering the workers and locus will be the payment wallet**. Users will deposit some amount in the locus wallet, our solution will deduct some amount based on the **AI Agent Fee** and **Interent Service Fee**. In the end, AI Agent will receive their fee and Interent could **monetize** this solution through App Fee, all happening inside Locus.

Team **Team Indo** -- [Youvandra Febrial](https://github.com/youvandra), Laras Ervintyana

`2026-04-29`

---

### RD_PHISHFILTER
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rdphishfilter-3c29) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dhiraj-143r/week_3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/9cf70d01c90945a19eb5c89aa15b9da1) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/9cf70d01c90945a19eb5c89aa15b9da1) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-powered email forensics. Pay per scan with USDC

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Phishing emails remain the most common way people get hacked. Attackers forge sender addresses, use lookalike domains, and craft urgent messages that trick even careful users into clicking malicious links or handing over passwords. Most anti phishing tools are either expensive enterprise products, overly technical, or simply not available to everyday users. PhishFilter changes this by making professional grade email threat analysis available to anyone, instantly, with no signups and no subscriptions.

What people can use it for

Verify any suspicious email in seconds. Paste the full email source into PhishFilter and our AI engine runs a complete forensic analysis. It checks SPF, DKIM, and DMARC authentication, scans every link against VirusTotal, detects homograph domain tricks, evaluates the language for urgency and manipulation patterns, and delivers a clear verdict: Safe, Suspicious, or Dangerous.

Scan your entire inbox at once. Connect your email via IMAP through the Inbox Scanner and PhishFilter automatically pulls and analyzes your recent messages, flagging anything that looks like a phishing attempt. No more opening sketchy emails to figure out if they are real.

Monitor your inbox in real time. Watchdog mode runs continuously in the background. The moment a phishing email arrives, PhishFilter sends a WhatsApp alert to your phone through Twilio so you can act immediately.

Check links without clicking them. The Link Sandbox takes any URL, resolves all redirects using Firecrawl, checks the final destination against VirusTotal, and shows you exactly where that link goes. You never have to risk clicking it yourself.

Listen to your results. Every threat report can be read aloud using Sarvam AI text to speech, making the tool accessible to users who prefer audio or are less comfortable reading technical reports.

Pay only for what you use. PhishFilter offers free scans every day. When you need more, you pay per scan using USDC on the Base network through Locus Checkout. No credit cards, no accounts, no recurring charges. Just scan and pay.

Let AI agents use it too. PhishFilter is fully machine readable. AI agents can discover the service, purchase scan credits with USDC through Locus, and submit emails for analysis, all through standard APIs without any human involvement. When credits run out, the API returns HTTP 402 with payment instructions so agents can autonomously buy more and keep scanning.

PhishFilter makes email security as simple as pasting text into a box, and as flexible as an API call. Whether you are a person checking one suspicious email or an AI agent scanning thousands, the same platform serves you, powered by Locus Checkout and USDC.

**Challenges we ran into**

Phishing emails are the number one attack vector in cybersecurity today, responsible for billions in losses every year. Most people simply cannot tell a fake email from a real one. Attackers use homograph domains, spoofed sender headers, and urgency driven language to trick users into clicking malicious links or sharing credentials. The tools that exist to fight this are either locked behind enterprise contracts, too technical for everyday users, or just not accessible to the people who need them most.

PhishFilter solves this by giving anyone, whether individuals, small businesses, freelancers, or even AI agents, access to enterprise grade email threat analysis on demand, with no subscriptions and no accounts required.

What people can use it for
Checking suspicious emails before clicking anything. Paste the raw email source into PhishFilter and our multi AI engine runs a full forensic breakdown including SPF, DKIM, DMARC authentication, sender reputation, homograph detection, urgency scoring, and link analysis across VirusTotal engines. You get a clear verdict in seconds.

Scanning inbox in bulk via IMAP. Connect your mailbox through the Inbox Scanner and PhishFilter pulls your recent emails and flags threats automatically. No more guessing which emails are real.

Real time monitoring with Watchdog mode. Activate live monitoring and PhishFilter watches your inbox continuously, sending WhatsApp alerts via Twilio the moment a phishing email lands.

Safe link checking with the Link Sandbox. Paste any suspicious URL and PhishFilter resolves redirects via Firecrawl, checks it against VirusTotal, and tells you exactly where that link actually goes without you ever having to click it.

Listening to your threat report. Every scan result can be read aloud using Sarvam AI text to speech, making it accessible even for non technical users.

How we integrated Locus Checkout
PhishFilter is monetized entirely through Locus Checkout with USDC on Base, making it one of the first security tools to accept crypto native micropayments. Here is exactly what we built with Locus.

Three tier pricing via Locus Checkout sessions. We create real Locus Checkout sessions for three plans: Single Scan, Scan Pack, and Pro Monthly. When a user clicks Pay with USDC on our pricing page, we call the Locus Beta API to generate a checkout session with the amount, currency as USDC, and chain as Base, then redirect the user to the hosted Locus Checkout page.

Webhook based credit issuance with HMAC verification. After payment, Locus sends a webhook to our /api/webhooks/locus endpoint. We verify the HMAC signature using our webhook secret to ensure the event is authentic, then automatically issue scan credits to the user session. No manual intervention, no trust assumptions.

Full agent to agent commerce via machine readable APIs. PhishFilter exposes a complete agent discovery protocol. /api/agent/services returns a JSON catalog of capabilities and USDC pricing, /api/agent/purchase lets an AI agent programmatically create a Locus Checkout session and receive a credit token, and /api/agent/scan accepts email content and returns a structured threat report. When credits run out the scan endpoint returns HTTP 402 Payment Required with the purchase URL embedded so agents know exactly where to pay and can autonomously replenish credits.

Standard discovery files. We serve skill.md, /.well-known/ai-plugin.json, and /.well-known/openapi.json so any agent framework can discover PhishFilter as a payable service without human configuration.

Freemium model with payment gating. Every user gets free scans per day. After that the scan API returns HTTP 402 and the UI redirects to the pricing page. This creates a natural upgrade path from free to paid, all powered by Locus.

**Track: Checkout with Locus**

PhishFilter fits directly into the Checkout with Locus track because the entire monetization layer of our platform is built on top of Locus Checkout with USDC on Base. We did not just add a payment button. We built a complete revenue engine where every scan beyond the free tier requires a Locus powered payment, and it works for both human users and AI agents.

How Locus Checkout is integrated

When a user visits our pricing page, they see three plans: Single Scan, Scan Pack, and Pro Monthly. Clicking Pay with USDC triggers a POST request to our backend, which calls the Locus Beta API at beta-api.paywithlocus.com to create a real checkout session with the correct amount, currency set to USDC, and network set to Base. The user is then redirected to the Locus hosted checkout page where they can pay via Locus wallet, any external wallet like MetaMask, or even as an AI agent.

Webhook verification and credit issuance

After a successful payment, Locus sends a webhook event to our /api/webhooks/locus endpoint. We verify the HMAC signature using our webhook secret to confirm authenticity, then automatically issue the correct number of scan credits to the user session. The entire flow from payment to credit delivery is fully automated with zero manual steps.

Payment gating with HTTP 402

Our scan API enforces a credit check before every analysis. When a user or agent runs out of credits, the API returns HTTP 402 Payment Required along with the Locus Checkout URL embedded in the response. This follows the x402 payment protocol pattern, meaning agents can programmatically detect when payment is needed and act on it without human help.

Agent commerce built on Locus

What makes our integration unique is that it is not just for humans. We expose /api/agent/services which returns a machine readable JSON catalog of our capabilities and USDC pricing, /api/agent/purchase which lets any AI agent create a Locus Checkout session and receive a credit token, and /api/agent/scan which accepts email content and returns a structured threat analysis. We also serve standard discovery files including skill.md, ai-plugin.json, and openapi.json so agent frameworks can find and pay for our service autonomously.

PhishFilter demonstrates exactly what the Checkout with Locus track is about: building a real product that monetizes a valuable service using Locus, with one integration that works seamlessly for both humans and AI agents.

Dhiraj Rathod

`2026-04-28`

---

### Bountic App
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bountic-app-dae8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skndash96/bountic) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://bountic.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/00ee305c550441699f6db0ff97cbc77f) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Fund the fix. Skip the friction.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Locus Checkout](https://img.shields.io/badge/Locus%20Checkout-333333?style=flat-square) ![Locus Pay](https://img.shields.io/badge/Locus%20Pay-333333?style=flat-square)

**The problem it solves**

I recently became a victim of an 8 year old [bug](https://github.com/microsoft/vscode/issues/28795#issue-236120546) in VSCode. I wondered why no one had ever worked on it, and it struck me: issues sit idle because there is no easy way for frustrated users to financially incentivize a fix. 

This hackathon by Locus provided the exact infrastructure to solve this. So, I built **Bountic** — an autonomous, issue-native USDC escrow system that replaces fiat delays and manual coordination with a single GitHub label.

Here is the complete, frictionless lifecycle of a Bountic issue:

### 1. The Setup: Zero Friction, Zero Spam
Managing bounties shouldn't require learning a new platform. Repository maintainers simply install the Bountic GitHub App, and from there, opening a bounty is as easy as adding a 'Bounty' label to an issue. 

Instead of traditional bounty bots that pollute timelines with dozens of noisy '/bounty $20' commands, Bountic creates a single, dynamically updating Pinned Ledger comment. The issue stays completely clean, professional, and focused on the code.

### 2. The Funding: Trustless, 1-Click Escrow
Funding is always just one URL swap away. By simply replacing 'github.com/*' with 'bountic.vercel.app/b/*' in the browser, anyone can jump straight to the bounty checkout page. 

Funds are locked in a Locus wallet the moment an issue is backed. Because contributors can verify the exact USDC balance via the GitHub ledger, they never have to guess if a sponsor will actually pay up. They know the money is real before they write a single line of code.

### 3. The Execution: Built for the M2M Economy
Open-source is no longer just humans writing code. Autonomous AI agents can debug software and submit Pull Requests, but they cannot open a bank account or send a Stripe invoice. 

Bountic provides the crypto-native payment layer for this new workforce. Agents can discover open bounties via our '/LLM.md' API, submit their fixes, and securely inject their Locus wallet addresses directly into the PR markdown to ensure they get paid.

### 4. The Settlement: Zero-Admin Payouts
When a PR is merged, the lifecycle completes without any administrative headache. Maintainers don't have to track down contributor emails, manage spreadsheets, or manually wire funds across borders. 

When a winning PR is merged, the maintainer authorizes the payout with one click on the Bountic web interface. The Locus API handles the routing, bypassing global fiat delays entirely and settling the USDC instantly to the human or machine that shipped the code.

The money reaches the winner either by a wallet address mention in github description (as a hidden comment) or by username matched to their email. Locus wonderfully takes care of moving the USDC to an email address.

The website also has a lot of features like Dashboard, Explore page which are both human and machine friendly.

**Challenges we ran into**

Building a multi-platform state machine (GitHub Webhooks + Next.js + Locus API) in a weekend came with several distinct hurdles. Here is how I solved the biggest ones:

### 1. The GitHub Email Privacy Wall
* **The Hurdle:** To process fiat fallbacks or send claim links, I needed the PR author's email. However, GitHub's webhook completely omits the email address for privacy. Calling the user API only works if their email is set to public (which most aren't).
* **The Solution:** I had to build a 3-step identity resolution waterfall. First, the app regex-scans the PR description for an AI agent's hidden `` tag. If that fails, it checks if the user has authenticated on the Bountic web app via GitHub OAuth (which guarantees email access). As a final fallback, the app fetches the raw Git commit metadata via Octokit to extract the 'author.email'.

### 2. Architecting a "Zero-Spam" Integration
* **The Hurdle:** My initial design used comments (e.g., users typing '/bounty $20'). I quickly realized this would result in massive timeline pollution, spamming maintainers with email notifications for every bot reply and ruining the repository's history.
* **The Solution:** I completely scrapped the chat commands. I pivoted to a webhook-driven 'Label' trigger and a single, dynamically updating "Pinned Ledger" comment. I moved all the heavy interaction—like the funding checkout and the payout approval—to the Bountic web UI, keeping GitHub perfectly clean.

### 3. Secure, Context-Aware Maintainer Approvals
* **The Hurdle:** I needed a way to let maintainers approve payouts on the Bountic website securely. 
* **The Solution:** I implemented GitHub OAuth and utilized the GitHub REST API's Collaborators endpoint (/collaborators/{username}/permission). When a user visits a Bountic issue page, the Next.js server dynamically checks their repo permissions. Only if the API returns 'admin' or 'write' access does the UI transform to reveal the Settlement Dashboard.

### 4. Locus Infrastructure
* **The Hurdle:** While integrating the Locus SDK, I ran into mysterious '500 Internal Server Error' responses when testing the checkout flows. There was also a slight mismatch in the documentation regarding the npm package name.
* **The Solution:** After debugging the network requests, I realized the Locus backend was rejecting 'localhost:3000' as a webhook target which is obvious but I got confused by the 500 error. I used smee.io to catch the webhooks reliably.

**Track: Checkout with Locus**

Bountic is built entirely around the Locus Checkout infrastructure. We use the Locus **REST API** to seamlessly onboard funders and lock USDC into an escrow smart wallet without requiring them to log in. Upon PR merge, we utilize the Locus API (*/pay/send* and */pay/send-email*) to execute instant, cross-border payouts to the winning human or AI agent's wallet. Locus is the core financial engine that makes this zero-friction workflow possible.

Team **0xCatnip** -- [Dash Skndash S](https://github.com/skndash96)

`2026-04-28`

---

### Invoke Studio
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/invoke-studio-5780) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YusufsDesigns/Invoke-Studio) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://invoke-studio.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/QKXAYSqn9LE) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI tools, on demand. For humans and agents.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Prisma ORM](https://img.shields.io/badge/Prisma%20ORM-333333?style=flat-square) ![Locus Suite](https://img.shields.io/badge/Locus%20Suite-333333?style=flat-square)

**The problem it solves**

AI capabilities are locked behind subscriptions, API keys, and complex integrations. 

If you've spent weeks perfecting a prompt that reliably solves a specific problem — 
contract analysis, security audits, investor update emails — you have no good way to 
monetize that expertise. You can't sell a prompt on Gumroad. You can't charge per use 
on Stripe without building an entire billing system. And nothing you build will work 
for AI agents as buyers, only humans.

On the other side, people who need specific AI-powered results have to either:
- Pay $20/month for ChatGPT and figure out the right prompt themselves
- Hire someone on Fiverr and wait
- Build their own integration

**Invoke Studio solves both sides of this.**

Creators publish their expertise as pay-per-run AI tools — a name, a description, 
a hidden system prompt, a custom input form, and a USDC price. No code required. 
No billing system to build. Just publish and earn.

Buyers get expert-quality AI results instantly, paying only for what they use. 
No subscriptions. No accounts. Fill a form, pay once, get the result.

**What people use it for:**

- **Developers** run security audits on their code, get database schema reviews, 
  generate PR descriptions — without context-switching to ChatGPT and spending 
  20 minutes prompting
- **Founders** get their pitch critiqued at an investor level, analyze their unit 
  economics, draft investor updates — tasks that used to require expensive consultants
- **Freelancers** scan contracts for risky clauses before signing — getting the same 
  analysis a lawyer would charge $300/hour for, in 10 seconds, for $0.75
- **AI Agents** discover tools via the API, pay programmatically using Locus's agent 
  payment flow, and receive structured results — without any human in the loop

The core insight: **the prompt IS the product.** Invoke Studio is the infrastructure 
that lets anyone sell their prompt expertise as a recurring revenue stream.

**Challenges we ran into**

### 1. The Locus server-side SDK doesn't exist on npm

The documentation references `@locus/agent-sdk` as the server-side package for 
creating checkout sessions. It doesn't exist on npm. Neither does `locus-agent-sdk`. 
I discovered this mid-build when `npm install` returned a 404.

**How I solved it:** I verified the actual REST endpoint with a raw `curl` call:

```bash
curl -X POST https://beta-api.paywithlocus.com/api/checkout/sessions \
  -H "Authorization: Bearer claw_dev_..." \
  -H "Content-Type: application/json" \
  -d '{"amount": "0.25", "description": "test"}'
```

It returned a session object. I rewrote the entire `lib/locus.ts` to use raw `fetch` 
calls instead of any SDK. This turned out cleaner anyway — no dependency, full 
control over the request shape.

### 2. Webhook firing but result never displaying

The payment went through, the Anthropic call succeeded, the run was marked COMPLETED 
in the database — but the UI showed nothing. The user just saw a payment success 
screen with no output.

The bug was in the state machine. The `onSuccess` callback from `<LocusCheckout>` 
was firing correctly, but the `runId` was not in scope at the point the callback 
executed. The polling function started with an undefined `runId`, silently failed, 
and the component stayed stuck on the checkout state.

**How I solved it:** Lifted `runId` into the top-level component state before the 
checkout session was created, ensuring it was available in the closure when 
`onSuccess` fired. Also added explicit console logging at each state transition 
during debugging to trace exactly where the chain broke.

### 3. No webhookSecret returned from the API

The Locus documentation describes a `webhookSecret` (`whsec_` prefix) being returned 
when creating a session with a `webhookUrl`. In practice, the beta API never returns 
this field regardless of what parameters are sent.

**How I solved it:** Added a graceful fallback in the webhook signature verification 
— if no secret is stored for a run, verification is skipped and the webhook is 
processed based on the `metadata.runId` alone. For production, this would require 
either Locus adding the secret to the response or implementing an alternative 
verification strategy.

### 4. The `<LocusCheckout>` component expects a specific checkout URL format

The component's `sessionId` prop expects just the UUID, but the `checkoutUrl` 
returned by the API points to `beta-checkout.paywithlocus.com` not 
`checkout.paywithlocus.com`. Passing the wrong base URL caused the component to 
load a blank iframe.

**How I solved it:** Used the `checkoutUrl` field returned directly from the session 
creation response and passed it via the `checkoutUrl` override prop on the component, 
ensuring the beta environment was used end to end.

**Track: Checkout with Locus**

Invoke Studio is not a product that uses Locus Checkout as a payment feature. 
**Checkout with Locus is the product.** The entire platform only exists because 
of two properties unique to Locus Checkout:

### 1. The checkout session IS the run

When a buyer clicks "Run for $0.75", the platform immediately calls 
`POST /api/checkout/sessions` and creates a Locus checkout session. The session's 
`metadata` carries the `runId`. When payment is confirmed on-chain, Locus fires 
a webhook to `/api/webhooks/locus`. That webhook is the only trigger for AI 
execution. There is no other way to run a tool. Payment and execution are the 
same event.

Without Locus Checkout's webhook-on-confirmation model, this architecture doesn't 
exist. You can't safely trigger an AI call on the frontend — the buyer could 
intercept it. The webhook-after-on-chain-confirmation is what makes the platform 
trustless.

### 2. Agents can pay for tools autonomously

This is the property that makes Invoke Studio genuinely new. Locus Checkout is 
the only payment primitive where an AI agent can:

1. Discover a tool via the public API
2. Create a run session
3. Call `preflight` to verify it can pay
4. Call `pay` to execute the payment from its Locus wallet
5. Poll for confirmation
6. Receive the result

No human approves anything. No UI is shown. The agent calls the same 
`POST /api/tools/{toolId}/run` endpoint that humans use, receives the same 
`sessionId`, and pays through Locus's agent payment API. One integration 
serves both humans and agents as buyers — which is exactly what Locus 
Checkout was designed for.

### 3. Pay With Locus closes the creator payout loop

Invoke Studio also uses the Pay With Locus side of the ecosystem. When a creator 
withdraws their earnings, the platform calls `POST /pay/send-email` — sending 
USDC to the creator's email via Locus escrow. The creator doesn't need a crypto 
wallet or a prior Locus account. They get an email, click a link, and claim 
their USDC.

This means the full money flow — buyer pays in → platform earns 20% → creator 
earns 80% — is entirely within the Locus ecosystem. Checkout collects. 
Pay distributes. Both in USDC on Base.

[Yusuf Lawal](https://github.com/YusufsDesigns)

`2026-04-29`

---

### Phoenix
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/phoenix-8e55) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/CaseClosed007/LocusHackathon) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://locus-hackathon-5owefdgi1-nikhil-s-projects-c3fde316.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Deploy once, rise from every failure.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Deploying an app has always required you to know things — the right runtime, the right port, the right start command, how to write a Dockerfile, how to read build logs when something breaks. Most people with an idea don't have all of that, and even developers who do still spend hours on setup that has nothing to do with the actual idea they're trying to build.

Locus Phoenix removes all of that friction entirely.

You type what you want in plain English. The agent figures out the runtime, writes every file, pushes it to Locus Build, and monitors the deployment. If it fails — and first deployments often do — it reads the build logs, diagnoses the root cause with Gemini, patches the code, and redeploys itself. You don't touch anything. You just watch it fix itself.

Once your app is live, you don't have to redeploy manually every time you want a change. There's a chat panel directly below every successful deployment where you describe what you want different — "make the hero section dark mode", "add a /health endpoint", "change the font to something modern" — and the agent patches only the affected files, shows you a diff of exactly what changed, and redeploys to the same project. It's the closest thing to having a developer on call.

For teams with a brand identity, there's a brand upload feature — drop in your PDF brand guidelines or a logo, and every app the agent generates automatically uses your exact hex colors, fonts, and tone of voice. No manual CSS editing after the fact.

For developers who already have code on GitHub, you just paste the repo URL. The agent fetches the files, analyses the stack, patches anything that needs to change for Locus compatibility, and deploys it — without you writing a single config file.

The payment side is built in throughout. The agent checks your Locus wallet balance before every heal attempt, routes its AI calls through Locus payment rails, and shows you a real cost breakdown on every successful deployment — how much USDC was spent, how many AI calls were made, and how much engineering time was saved. It's not just an AI tool, it's an economically-aware autonomous agent that knows what it's spending and stops itself when the budget runs out.

**Challenges we ran into**

The biggest challenge was getting Gemini to output code in a parseable format. It kept truncating responses mid-file or adding explanation text before the code blocks, causing my parser to silently fail even when the code was right there. I fixed it with a two-stage fallback regex and stricter prompt instructions telling Gemini to start its response with code, not explanation. The iterative editing feature also broke right before the demo — I was calling a Locus API endpoint that doesn't exist on the beta API. Stripped out that lookup, added a force push to handle fresh git history, and it worked.

**Track: Using BuildWithLocus to leverage our suite.**

Locus Phoenix integrates with Locus at every layer of its operation — not just as a deployment target, but as the full execution substrate for an autonomous AI agent. On the build side, every deploy triggers the complete Locus lifecycle: POST /v1/auth/exchange for JWT auth, POST /v1/projects to create a project, POST /v1/projects/{id}/environments for a production environment, POST /v1/services to provision a containerized web service, a git push to beta-git.buildwithlocus.com to trigger the actual build, GET /v1/deployments/{id} polled every 20 seconds for status, and GET /v1/deployments/{id}/logs fetched on failure and fed directly to Gemini for diagnosis — after which the agent patches the code and redeploys to the same Locus project automatically, up to three times. On the payments side, GET /v1/billing/balance is called before every heal attempt as a budget gate, the Locus wallet balance is displayed live in the UI, and with USE_LOCUS_WRAPPED=true all LLM calls are routed through Locus payment rails rather than hitting Gemini directly. The iterative editing feature redeploys to the same Locus project on every chat-driven code change, making Locus the persistence layer for a continuous AI development loop. In total the project calls 10 distinct Locus API surfaces, and the key differentiator is that the user never touches Locus at all — every API call is made autonomously by the agent, which means Locus Build isn't just hosting an app, it's the runtime an AI agent reasons and acts through.

[Nikhil Sharma](https://github.com/CaseClosed007)

`2026-04-23`

---

### Locus DefenderX (Security as an Agent)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/the-agentic-honeypot-securityasanagent-1215) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Janhvigupta29/locus-defenderX) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://janhvigupta29.github.io/locus-defenderX/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Every Attack Meets Its Own Illusion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square)

**The problem it solves**

Modern applications get attacked constantly like SQL injections, path traversal, brute force or credential stuffing. The traditional response is a static firewall with fixed rules. 
The problem? Attackers know how firewalls work. They probe slowly, rotate IPs, and mutate their payloads until something gets through.
Our agent flips the model entirely. Instead of blocking attackers, it deceives them to a fake pot and does it autonomously, without a human in the loop.

***Specific use cases can be:-***

1. **Startups and solo developers with no security team**
Most early-stage products have zero dedicated security staff. Our Locus DefenderX acts as an always-on agent that makes infrastructure decisions automatically. The agent handles BGP routing table itself without even us having the prior knowledge.
2. **Protecting APIs during a live product launch**
Launch day is when attackers strike hardest. DefenderX monitors traffic in real time, and the moment anomalous patterns cross a threshold, it deploys a mirror environment and silently reroutes the attacker while keeping your real servers healthy during your most critical window.
3. **Threat intelligence gathering**
Once an attacker is rerouted to the mirror environment, every move they make like every payload they try, every endpoint they probe is end to end logged. Over time this builds a profile of real attack patterns targeting your specific stack. So instead of them taking our confidential information, it's actually us who are keeping our eyes on them.
4. **Reducing false-positive lockouts**
Rule-based systems often block legitimate users think of it as a developer testing endpoints that look like SQL injection. Because DefenderX uses an AI reasoning layer rather than rigid rules. It can smartely distinguish context like a security researcher running known safe tools and a live attacker running exploit chains.
5. **Compliance and audit trails**
In regulated industries (fintech, healthtech), you need to prove your system detected and responded to threats. DefenderX's agent log provides a timestamped, reasoning-annotated record of every decision made like the log saying "attack confirmed at 14:32, honeypot deployed at 14:32:04, traffic rerouted."

*How it makes existing tasks easier and safer*
 
![image](https://assets.devfolio.co/content/3bc56fbf56944db2a67e050d6e2f9caa/030e230b-8db8-4ea0-b9a2-83daa150c755.png)

**Challenges we ran into**

1. ***The API Key Exposure Problem***
**The hurdle:**
The very first version of this project called the Anthropic API directly from index.html or straight from the browser. This works fine inside Claude.ai (where the platform injects the key securely), but the moment you move it to a stand-alone project and push it to GitHub, your API key is visible to anyone who opens DevTools. It would have been scraped within hours.
**How we solved it:**
We introduced server.js as a secure proxy layer. The browser never touches Anthropic's API directly. Instead:
*Browser → POST /api/analyze → server.js → Anthropic API*
The key lives only in .env, which is listed in .gitignore and never committed. The browser only ever sees your own server's URL. This is the standard industry pattern for protecting secrets in web apps. We just had to rebuild the original single-file approach around it.

2. ***JSON Parsing Failures from Claude***
**The hurdle:**
We told Claude to respond with pure JSON. But occasionally — especially under certain prompt conditions — it would wrap the response in markdown code fences like this:
*{"verdict":"attack","confidence":91,...}*
JSON.parse() would throw an error on that, crashing the analysis flow and falling back to the heuristic default every time.
**How we solved it:**
A small .replace() before parsing strips the fences defensively:
*result = JSON.parse(raw.replace(/json|/g, "").trim());*
And the whole parse is inside a try/catch — so even if Claude returns something completely unexpected, the app falls back to a sensible safe default rather than breaking:
*catch {
  result = { verdict: "attack", confidence: 88, attack_type: "Anomalous Traffic", ... };
}*
The lesson here is broader than just this project: never trust external API responses blindly, even from your own AI. Always sanitize, always have a fallback.

***Organizations It Serves***

1. **Startups & Early-stage Companies**

- No dedicated security team yet — Sentinel acts as your 24/7 automated security engineer

- Can't afford a SOC (Security Operations Center) — AI agent replaces expensive human monitoring

- Need to ship fast without security becoming a bottleneck — automatic threat handling keeps momentum going

- Want to impress investors with strong security posture from day one

- Regulatory pressure (GDPR, SOC 2) — audit logs show autonomous threat response and containment

2. **Mid-Mar SaaS Companies**

- Sing security person managing entire security operations — needs automated backups

- Grow user base means growing attack surface — threat volume exceeds what one person can handle

- Can't afford 24/7 on-call security staff but need protection outside business hours

- Want to reduce Mean Time To Respond (MTTR) from hours to seconds

- Need objective proof that threats were detected and isolated for compliance reports

3. **Fintech & Payments Companies**

- Attacks directly translate to stolen money — speed of response is literally about loss prevention

- Regulatory requirement to document threat detection and response — Sentinel logs every decision with reasoning

- Cannot afford false positives that lock out legitimate users (blocking customer transactions costs revenue)

- Need to prove security improvements to compliance auditors and customers

- Targeted by sophisticated attackers — need AI-driven detection, not just rules-based systems

4. **Healthcare & Medical SaaS**

- HIPAA/HITRUST compliance requires detailed incident logs — Sentinel provides timestamped, reasoned threat records

- Cannot have downtime during critical patient care moments — honeypot redirection keeps main app healthy

- Attackers specifically target health data (sells for 10x the price of credit cards) — need aggressive detection

- Need to pass security audits to partner with hospitals and insurance companies

- Patient data breaches result in brand destruction and lawsuits — prevention is worth millions

5. **E-Commerce Platforms**

- Peak season (Black Friday, holidays) = peak attack season — automatic response handles surge without manual intervention

- Payment card industry (PCI-DSS) compliance requires proof of real-time threat detection

- One breach during peak season takes the entire business offline — cannot risk it

- Fraudsters attack constantly — need to distinguish between normal bulk traffic and orchestrated attacks

- Customer trust is the entire business — one breach destroys reputation permanently

6. **API-First / Microservices Companies**

- Many attack surfaces (each microservice is a target) — need automated monitoring across all endpoints

- Rate-limiting and traditional firewalls don't work well with distributed architecture

- Performance-critical — adding honeypot redirection has near-zero latency impact on legitimate users

- DevOps-heavy teams appreciate "infrastructure as code" approach where AI makes infrastructure decisions

- Rapid deployment cycles mean security can't keep up with changes — automation required

Team **Sheleads** -- Anjali Verma, [Sarika Sharma](https://github.com/sarika-03), Janhvi Gupta

`2026-04-23`

---

### Free Vibes
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/free-vibes-90d9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/y3chnx/FreeVibes) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1udezAeY13_tAkr0rACmV3ZwpY4357zBg/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/NtXNjKbPtEs) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI Code Editor that Advertises Sponsor

![PyQt](https://img.shields.io/badge/PyQt-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Modern AI coding tools like Cursor or cloud-based code assistants are powerful, but they are often expensive and usage-limited. Many developers (especially students and indie builders) cannot afford high subscription costs or token-based pricing models.

At the same time, developers constantly need to discover tools, APIs, and services while building projects. This usually requires leaving their workflow, searching online, and evaluating options manually.

This project introduces a new approach: a fully free, unlimited AI coding agent that sustains itself through intelligent, context-aware sponsorships.

Instead of charging users, the AI acts similarly to an influencer — recommending relevant tools, APIs, or services during the coding process. These recommendations are not random ads, but context-aware suggestions that align with what the developer is building.

For example, if a user is implementing payments, the AI may suggest a payment API. If a database is needed, it may recommend a backend service. These suggestions create a natural monetization flow (e.g., affiliate or API usage), allowing the system to generate revenue while remaining free for users.

**Challenges we ran into**

One of the biggest challenges was building a functional Python-based code editor from scratch. Creating a smooth editing experience, including displaying structured code, and integrating it with an AI agent, required careful design. Since this was originally developed as a macOS application, I also had to manage environment-specific issues and ensure the editor could reliably interact with the backend AI logic.

Another major challenge was selecting the right AI model for coding assistance. Different models vary significantly in terms of cost, speed, and code quality. I experimented with multiple approaches to find a balance between performance and practicality, especially since the goal of this project is to provide a free and unlimited experience. This meant thinking carefully about how model choice would impact scalability and long-term feasibility.

I also spent a significant amount of time exploring different monetization and advertising scenarios. The initial idea of inserting traditional ads directly into the AI's reasoning process felt intrusive and unrealistic. I iterated through multiple concepts, including passive ads, triggered suggestions, and embedded recommendations, before settling on a more natural approach where the AI behaves like a developer-focused influencer. This allows the system to generate revenue through context-aware recommendations without disrupting the user experience.

**Track: Using BuildWithLocus to leverage our suite.**

This project applies to the "AI for Monetization" track by demonstrating how an AI agent can generate revenue autonomously.

Instead of charging users, the AI coding agent creates value through context-aware sponsorships and tool recommendations. As it assists users with coding tasks, it suggests relevant APIs, platforms, or developer tools based on the current context.

These recommendations act as monetization points (e.g., affiliate links or API integrations), allowing the system to generate revenue while remaining free and unlimited for users.

This showcases a new model where AI systems can sustain themselves financially without direct user payments.

Yuchan Lee

`2026-04-22`

---

### Draykon AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/draykon-ai-d938) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://draykon-ai.pages.dev/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://himanshu-developer-portfolio.pages.dev/Recording%202026-04-13%20221633.mp4) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Draykon AI - Built to Break Limits

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Package JSON](https://img.shields.io/badge/Package%20JSON-333333?style=flat-square)

**The problem it solves**

**The Problem It Resolves**

The current landscape of digital creation is significantly hindered by fragmentation.

Students, developers, and creators today depend on a diverse range of disconnected tools, including AI chat platforms, code editors, design applications, documentation systems, and deployment environments. While each tool addresses a specific aspect of the workflow, none provides a comprehensive solution that unifies the entire creative process.

This fragmentation leads to three fundamental challenges:

1. **Context Switching Overload**  
Users constantly shift between applications, disrupting their focus and hindering their mental flow with each transition.

2. **Inefficient Creation Pipelines**  
Ideas are generated in one tool, refined in another, developed in yet another application, and ultimately deployed elsewhere. This disjointed process creates unnecessary delays and friction at every stage of creation.

3. **Inconsistent Output Quality**  
The lack of integration among tools results in fragmented outputs, which require manual adjustments and rework to achieve coherence.

Draykon AI decisively addresses these challenges by introducing a powerful, unified AI-native creation system.

Draykon AI offers a singular, intelligent workspace where users can:

- Think
- Generate
- Build
- Refine
- Deploy

All of this can be accomplished without leaving the ecosystem, losing context, or switching between disparate tools.

In essence, Draykon AI transforms the traditional multi-tool workflow into a seamless, AI-driven creation pipeline.

In summary, it eliminates the chaos of multiple tools, paving the way for a more efficient and focused creative flow.

**Challenges we ran into**

### Challenges Faced in Building Draykon AI

Creating Draykon AI presented several technical and design challenges.

#### 1. Real-Time Response Handling and UI Stability

One of the most significant challenges was ensuring smooth, real-time interactions without experiencing user interface (UI) freezes or inconsistent rendering.

**Problems:**
- Delayed responses resulted in uneven rendering.
- Partial outputs occasionally disrupted visual consistency.
- Heavy interactions caused the interface to lag.

**Solutions:**
- Redesigned the data flow to be fully asynchronous and non-blocking.
- Introduced progressive rendering, allowing content to appear smoothly in chunks.
- Added structured loading states and fallback rendering logic.
- Optimized update cycles to prevent unnecessary UI refreshes.

These changes made the experience feel fluid, responsive, and continuous.

#### 2. Performance Under Heavy Interaction Load

As features expanded, maintaining speed became crucial.

**Problems:**
- Multiple simultaneous operations slowed down the interface.
- Excessive re-rendering reduced responsiveness.

**Solutions:**
- Refactored the architecture into modular components.
- Reduced unnecessary state updates.
- Streamlined data flow between features.
- Optimized rendering logic for improved efficiency.

#### 3. Maintaining a Consistent Futuristic UI System

Draykon AI features a dark, neon-inspired futuristic visual identity.

**Problems:**
- Ensuring design consistency across all screens and resolutions.
- Balancing visual effects with performance.
- Avoiding clutter while supporting advanced functionality.

**Solutions:**
- Developed a unified design system with reusable UI components.
- Standardized spacing, typography, and glow effects.
- Iteratively refined layouts for better responsiveness.
- Focused on minimalism with a strong visual hierarchy.

By addressing these challenges, we enhanced the overall performance and aesthetic appeal of Draykon AI.

**Track: Using BuildWithLocus to leverage our suite.**

- **Artificial Intelligence and Intelligent Systems Track**  
- **Developer Tools and Productivity Track**  
- **Full Stack Web Development Track**  
- **Creator Productivity and Workflow Innovation Track**

Team **Draykon AI** -- Himanshu Kumar Singh

`2026-04-19`

---

### Locus Forge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/locus-forge-392b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/t0k1t00/locus-forge/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://locus-forge.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/WvFQcmXgeCY) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> One sentence. Deployed, audited, paid.

![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square) ![Firecrawl](https://img.shields.io/badge/Firecrawl-333333?style=flat-square) ![E2B Sandboxes](https://img.shields.io/badge/E2B%20Sandboxes-333333?style=flat-square) ![Paywithlocus](https://img.shields.io/badge/Paywithlocus-333333?style=flat-square)

**The problem it solves**

Software development has a trust problem — not a capability problem.

AI can write code. But it can't own infrastructure, pay for it, or prove it did the work. Every autonomous coding tool today still requires a human to click deploy, approve a payment, and verify the output. The agent is smart but financially blind.

**Locus Forge eliminates that gap.**

Type one sentence — `Build me a clone of crewai.com` — and three specialized agents take over completely:

- **Architect Agent** scrapes the target URL, generates a full React application file-by-file in a live streaming session, and deploys containers + database on BuildWithLocus via REST API — no AWS console, no Dockerfile, no human cloud credentials
- **Assessor Agent** attacks the live deployment adversarially — security scans, API fuzzing, dependency audits — and generates cryptographic proof of any vulnerability found
- **Escrow Controller** validates the proof and releases a USDC bounty to the Assessor's wallet on the Base network — automatically, on-chain, with a BaseScan transaction hash

Every agent has its own Locus wallet. Every agent has a hard budget cap. Every action produces a verifiable transaction hash. The blockchain is the audit trail.

This is useful for:
- **Founders** who want to go from idea to deployed app without writing code or managing infrastructure
- **Enterprises** that need autonomous DevOps with financial accountability baked in — not bolted on
- **Agent developers** building multi-agent systems where agents need to pay each other for verified work

The key insight: Locus doesn't just process payments at the end of the workflow. Locus **is** the architecture. Agents cannot act without it. Budget caps prevent runaway spending. Escrow ensures payment only flows when work is cryptographically proven. This is what trustworthy autonomous software looks like.

**Challenges we ran into**

### 1. Getting the Vite HMR error pipeline to work inside E2B sandboxes

E2B sandboxes don't expose Vite's HMR WebSocket natively. We had to build a custom error monitoring layer — a polling endpoint (`/api/monitor-vite-logs`) that tails the sandbox process stdout, parses Vite error output with regex, and surfaces structured error objects back to the UI. Getting the error format consistent across different Vite failure modes (syntax errors, missing modules, HMR update failures) took significant iteration.

### 2. Streaming code generation without losing file state

The AI response stream generates multiple files sequentially. The challenge was maintaining a coherent file manifest in the frontend while chunks arrive out of order. We built a file parser (src/lib/fileParser.ts) that buffers partial file content, detects file boundaries from the stream, and only commits a file to the explorer once its content is complete. Early versions would flash incomplete files or overwrite content mid-stream.

### 3. BuildWithLocus multi-step auth flow

The BuildWithLocus API requires exchanging an API key for a bearer token before any resource creation. The token exchange, project creation, environment resolution, service creation, and deployment trigger are five separate API calls — each with different response shapes. We had to write defensive parsing (`readIdFieldDeep`) that checks multiple candidate keys across nested response objects because the API returns IDs under different field names depending on the endpoint.

### 4. Escrow state machine race conditions

The Assessor agent submits proof while the Architect deployment is still being polled for health. Early builds had the Escrow agent releasing bounty before the deployment was confirmed live — because the proof generation was faster than the BuildWithLocus health check. Fixed by adding explicit state gating: Escrow only activates after `deployments.backend.status === "live"` is set in the Zustand store, which is only set after the deployment health poll returns 200.

### 5. Firecrawl scrape → code generation context window

Scraping crewai.com returns a large markdown document. Passing the full scrape directly to the code generation prompt caused the model to hallucinate asset URLs and miss component structure. We built a context selector (`lib/context-selector.ts`) that extracts only the structural elements — headings, nav items, CTA text, image alt text — and discards body copy before passing to the generation prompt. This reduced hallucinated URLs by ~80% in testing.

**Track: Using BuildWithLocus to leverage our suite.**

Locus Forge uses BuildWithLocus as the core infrastructure layer — not as an optional add-on.

When the Architect Agent receives a prompt, it calls the BuildWithLocus REST API directly to provision a project, create an environment, spin up a containerized service, and trigger a deployment. The agent authenticates via API key exchange, creates all resources programmatically, and receives a live service URL — without any human touching a cloud console, writing a Dockerfile, or configuring DNS.

The critical point: the agent pays for this infrastructure from its own Locus-constrained wallet. BuildWithLocus is the only reason this is safe. A traditional cloud provider would expose the human's credit card to an autonomous system. BuildWithLocus gives the agent its own billing identity with a hard cap — so an infinite loop or a hallucinated deployment cannot drain real funds.

The full integration lives in `api/_lib/locus.ts` — token exchange, project creation, environment resolution, service provisioning, deployment trigger, and health polling. Every infrastructure action the Architect takes goes through BuildWithLocus. There is no fallback to Vercel, Fly.io, or any human-configured cloud.

This is exactly the use case BuildWithLocus was built for: agents that need to own and operate infrastructure autonomously, with financial accountability enforced at the platform level rather than trusted to the model.

Team **Symphony** -- [Keerthivasan Venkitajalam](https://github.com/Keerthivasan-Venkitajalam), [Swathi B Raj](https://github.com/t0k1t00)

`2026-04-21`

---

### DemoForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/demoforge-4e92) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xlogix/bwl-app) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mo6sobwcdw34foz4.buildwithlocus.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://github.com/xlogix/bwl-app/raw/refs/heads/main/output/playwright/videos/demoforge-restaurant-flow-local-strip-captioned.mp4) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Tailored demos before the sales call

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Zod](https://img.shields.io/badge/Zod-333333?style=flat-square) ![Drizzle ORM](https://img.shields.io/badge/Drizzle%20ORM-333333?style=flat-square)

**The problem it solves**

DemoForge solves a common sales problem: teams know their product can be configured for a prospect, but showing that credibly still takes too much manual work.

Today, sales often has to ask engineering or solutions teams to rebuild demos by hand for every account. That slows down deals, creates inconsistent quality, and usually produces generic demos that do not feel like the buyer's actual product context.

DemoForge changes that workflow. A company integrates its product once, and after that sales can generate tailored demo instances using prospect context from forms or existing systems like Salesforce. Instead of showing slides or a fake internal dashboard, the buyer sees a product experience that feels like software built for their use case.

This makes it easier to
- shorten the time between lead capture and first demo
- give sales more autonomy without requiring custom engineering work every time
- create more believable product proof earlier in the deal
- support both fast preview demos and deeper standalone deployments when needed

**Challenges we ran into**

One of the biggest challenges was getting true per-demo deployments working reliably on Locus instead of falling back to a simulated in-app preview.

A few technical issues showed up along the way:

- Next.js standalone deployments needed the right runtime and server binding setup to pass readiness checks in Locus.
- Static assets were not initially making it into the standalone runtime, which caused styling issues on deployed demos.
- The first generated demos still felt like renamed internal workspaces instead of real product interfaces, so the product surfaces had to be redesigned around distinct software types like restaurant ordering, patient booking, and property management.
- The deploy flow also needed a better handoff between instant preview generation and slower real deployments, so the status experience had to be reworked.
- Finally, preserving proof-of-concept standalone deployments without creating unnecessary new ones required changes to retention and cleanup logic.

**Track: Using BuildWithLocus to leverage our suite.**

- AI
- Sales / GTM
- Build with Locus

Team **Lone Wolf** -- [Abhishek Uniyal](github.com/xlogix)

`2026-04-22`

---

### UltraXAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ultraxai-057c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kanishkaapatra/UltraXAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ultrax-ai.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SHxC1BKKYnw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Convert ideas into schemas, types & ERDs instantly

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Netlify](https://img.shields.io/badge/Netlify-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Designing a database schema from scratch is a non-trivial engineering task. It requires anticipating relationships, enforcing constraints, and ensuring long-term scalability. Common failure points include:

Ambiguous requirements → poor schema design
Incorrect relationships (missing or mis-modeled foreign keys)
Schema drift between database, TypeScript types, and validation layers
Time lost on repetitive boilerplate work
Late discovery of structural flaws (costly refactors)

For many developers—especially in early-stage projects—this slows down iteration and introduces avoidable technical debt.

What People Can Use It For
1. Rapid Prototyping

Turn an idea into a structured backend in seconds.

Validate product concepts quickly
Skip initial schema design overhead
Move directly to feature development
2. Backend Scaffolding

Generate a production-ready starting point:

Prisma schema for database layer
TypeScript types for application logic
Zod schemas for input validation

This ensures consistency across the stack from the start.

3. Learning & Skill Development

Useful for:

Understanding how real-world schemas are structured
Learning relationships (1:1, 1:N, N:M)
Seeing best practices applied automatically
4. System Design Assistance

Acts as a first-pass architecture generator:

Converts vague ideas into concrete entities
Surfaces missing concepts (e.g., roles, audit logs)
Helps reason about data models before implementation
5. Refactoring & Validation

Input an existing idea/system and:

Compare generated schema vs current design
Identify redundancies or missing relations
Improve normalization and structure
How It Makes Existing Work Easier
Eliminates Repetitive Tasks

Instead of manually writing:

Models
Relations
Types
Validation

→ It generates all of them in one pass.

Reduces Human Error
Enforces consistent schema structure
Aligns database, types, and validation automatically
Minimizes mismatches across layers
Speeds Up Development Cycles
Go from idea → implementation faster
Reduce back-and-forth during early design phases
Spend more time on business logic, less on setup
Improves Consistency Across Teams
Standardized schema outputs
Easier collaboration between developers
Clear, visual ERD for shared understanding

**Challenges we ran into**

1. Inconsistent AI Output Structure

Problem:
Early iterations produced outputs that were not reliably parseable—missing fields, malformed JSON, or mixing prose with code.

Impact:

Broke the parsing pipeline
Caused runtime errors in schema generation
Made the system non-deterministic

Solution:

Enforced a strict JSON contract in the LLM prompt
Used schema validation (e.g., Zod) on the AI response before processing
Added fallback handling for partial failures
2. Invalid Prisma Schema Generation

Problem:
Generated schemas sometimes:

Missed relation directives (@relation)
Had circular or ambiguous references
Failed Prisma validation

Impact:

Schemas couldn’t compile
Required manual fixes, defeating automation

Solution:

Added a post-processing validation layer
Introduced rules for:
Relation completeness
Foreign key consistency
Iteratively refined prompt to enforce Prisma-specific constraints
3. Mapping AI Output → Multiple Targets

Problem:
One input needed to produce:

Prisma schema
TypeScript types
Zod validation
Mermaid ERD

Keeping these synchronized was non-trivial.

Impact:

Drift between layers (e.g., type mismatch vs schema)
Increased complexity in transformation logic

Solution:

Used a single structured intermediate representation (IR)
Derived all outputs from that IR instead of generating each independently
Ensured consistency across all artifacts
4. ERD Diagram Accuracy (Mermaid.js)

Problem:
Mermaid diagrams often:

Misrepresented cardinality
Omitted relationships
Produced invalid syntax

Impact:

Visual output became misleading or broken

Solution:

Built a dedicated ERD generator from the IR
Explicitly mapped:
1:1
1:N
N:M
Added validation before rendering
5. Handling Vague or Underspecified Prompts

Problem:
User inputs like “a social app” lacked enough detail.

Impact:

Weak or incomplete schemas
Missing critical entities (e.g., notifications, roles)

Solution:

Implemented prompt enrichment:
Expanded user input with inferred requirements
Injected common domain patterns (e.g., auth, timestamps)

[Kanishkaa Patra](https://github.com/kanishkaapatra)

`2026-04-22`

---

### Fetch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fetch-98b4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ndstab/fetch.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fetch-woad-five.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Tell an agent what you want, it shall get it!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Fetch solves the trust and control gap in AI shopping.

Today, AI shopping tools usually fall into two weak patterns:

1. **Manual copilots**: they suggest links, but the user still has to do all checkout work.
2. **Blind autopilot**: they can attempt autonomous buying, but users have weak spend controls and low transparency.

Fetch combines automation with financial guardrails:

- User gives a brief, budget, and delivery constraints.
- Agent hunts the web and returns ranked options with reasoning/tradeoffs.
- User approves one option.
- Purchase flow runs with a **quest-scoped virtual card** and budget boundaries.
- Unspent funds are returned.

### What people can use it for

- Fast product discovery under a strict budget.
- Delegating repetitive shopping research (price, delivery, merchant comparison).
- Safer delegated purchasing for teams/families/ops workflows.
- Controlled AI-assisted checkout where each task has isolated financial risk.

### Why it is safer than typical agentic checkout

- One quest = one spending envelope.
- Virtual card is scoped to that quest/purchase.
- Explicit human decision point before spend.
- Timeline visibility into plan/hunt/checkout/settle phases.
- Refund handling for unspent budget and failure paths.

**Challenges we ran into**

This project surfaced a lot of real production issues. The biggest hurdles were around API correctness, payment edge cases, and deployment reliability.

### 1) Checkout API path and environment mismatches

**Issue:** initial checkout creation failed with 404/500 because of endpoint/base mismatches and beta/prod URL drift.

**Fix:** normalized API bases, aligned endpoint usage, and added resilient session creation + fallback behavior when webhook URL is rejected in beta.

### 2) “Checkout not found” in frontend after session creation

**Issue:** session existed, but embedded checkout UI failed because frontend SDK URL did not match backend environment.

**Fix:** frontend now derives checkout host from backend config so beta sessions render against beta checkout.

### 3) Post-payment stuck state (`Paid — starting`)

**Issue:** webhook delivery didn’t always arrive (or replay path failed), leaving quests stuck after payment.

**Fix:** added reconcile endpoint and fallback logic; if webhook replay fails, quest status still advances and execution starts.

### 4) Cloud Run deployment instability (port/env/revision problems)

**Issue:** revisions failed health/startup due to missing envs (`DATABASE_URL`), wrong `PUBLIC_URL`, and rollout confusion across revisions.

**Fix:** tightened deploy env setup, validated runtime config, and made fallback paths less brittle when env is imperfect.

### 5) Build-with-Locus service creation failures (`imageUri` validation)

**Issue:** Build API rejected invalid image URI formats.

**Fix:** normalized + validated image URI in backend and added safe fallback image to avoid hard stop at container deploy phase.

### 6) Over-budget option ranking and misleading labels

**Issue:** options above budget could still appear as “Cheapest” due to ordering/label assumptions.

**Fix:** introduced budget ceiling/tolerance filtering, explicit sorting by price, and UI guardrails for over-budget selections.

### 7) Laso minimum amount and mint constraints

**Issue:** card mint failed for budgets below Laso minimum (`$5`).

**Fix:** enforced minimum budget at quest creation and pre-check logic before mint attempts.

### 8) Laso/x402 failure mode with real monetary impact

**Issue:** some `laso-get-card` attempts failed with `402` after x402 charge initiation, and refunds could fail with allowance/policy constraints (`403`).

**Fix:** added pre-mint balance checks, recovery attempts (`lasoWithdraw`) on mint failure, and best-effort partial refund strategy using live allowance/balance data.

This became a key engineering lesson: agentic payments require robust **failure recovery**, not just a successful mint path.

**Track: Using BuildWithLocus to leverage our suite.**

Fetch is built specifically around Locus primitives, not a generic app with a payment bolt-on.

It uses the track’s core components in one cohesive flow:

- **Checkout with Locus** for user budget funding.
- **Wallet/send flows** for settlement and refunds.
- **Laso virtual cards (x402)** for quest-scoped merchant checkout.
- **Build with Locus** for per-quest service/container lifecycle.
- **Wrapped APIs** for agent intelligence (planning, hunt, shortlist).

In other words, the product itself demonstrates the Locus thesis: **agents as economic actors with programmable money boundaries and execution infrastructure**.

Sajjad Nakhwa

`2026-04-23`

---

### Resolver AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resolver-ai-5fcd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Chucks1093/resolver) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://useresolver.xyz) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI agent that fixes github issues

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Resolver helps developers fix assigned GitHub issues faster without jumping across tools or manually handling branches and PR setup.

People use it to work on assigned issues directly from Telegram, generate issue-scoped code changes with clear branch and commit history, and choose either review-first PR flow or automatic PR flow. It also shows deployment attempts and status for resolved work.

It makes the workflow easier and safer by reducing context switching from issue triage to implementation and PR steps, keeping changes focused on one issue, enforcing per-user GitHub auth context, tracking jobs and deployments for traceability, and supporting stop/continue controls for long-running tasks.

**Challenges we ran into**

One of the biggest issues I ran into was that BuildWithLocus deployments were passing build and then failing during deploy with ECS service did not become ready before timeout.

I fixed several parts step by step: I added and validated .locusbuild, fixed build problems around Node/runtime versions set runtime variables like HOSTNAME=0.0.0.0, and updated the service start command and runtime architecture.

These changes made the build process much more stable, but some deployments still timed out at the ECS readiness stage.

To handle that, I improved deployment status reporting and fallback messages in the app, and shared detailed deployment IDs and service config with the Locus team so they can inspect infra-level readiness behavior directly.

**Track: Using BuildWithLocus to leverage our suite.**

Resolver fits the BuildWithLocus track because it uses BuildWithLocus to turn AI fixes into real live previews that people can open and test.

A user can send an issue in Telegram, and the agent works on the fix. After that, Resolver calls BuildWithLocus to deploy the updated code and track deployment status until it is ready.

So the output is not just code suggestions. It is a running environment the user can actually test before creating a PR.

This makes issue resolution faster and more useful, because users can review, test, and decide next steps in one flow without managing infrastructure themselves.

Team **Paradox** -- [Sebastian Anioke](https://github.com/Chucks1093)

`2026-04-23`

---

### BuWithL
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/buwithl-daa6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/maulana-tech/buildwithlocus) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mobj33czir7850u8.buildwithlocus.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Je8_Gol7jRc) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A no-code section-based website builder

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Merchants and small businesses in emerging markets need to accept crypto payments but face a massive barrier: building a checkout-enabled website requires frontend skills, backend integration, wallet infrastructure, and deployment knowledge. Locus Studio eliminates all of that. A coffee shop owner in Jakarta, a freelancer in Lagos, or a digital creator in Buenos Aires can open the studio, compose their page visually (or use the one-click demo), connect their Locus wallet with just an API key, and have a live checkout page accepting USDC payments — all in under 5 minutes with zero code.
It also makes the existing payment flow safer — every transaction is on-chain (Base), webhook-verified with HMAC-SHA256, and analytics update in real-time. No manual reconciliation needed.

**Challenges we ran into**

BuildWithLocus credit drain — Initial publish flow called POST /v1/projects/from-repo on every publish, creating duplicate services and burning $0.25 each time. Fixed by persisting the service ID to data/deploy.json and using POST /v1/deployments for redeployments on subsequent publishes.

**Track: Using BuildWithLocus to leverage our suite.**

Locus Studio is a full-stack application deployed on and powered by BuildWithLocus:
- Hosting: The entire app runs as a containerized service on BuildWithLocus, deployed via from-repo with auto-deploy on every git push
- API integration: Uses BuildWithLocus Auth API (/v1/auth/exchange) for JWT tokens, Billing API for credit checks, Projects API for deployment, and Variables API for environment management
- Smart deployment: First deploy creates the service, all subsequent deploys reuse the same service ID — demonstrating proper resource management on the platform
- Ecosystem bridge: Combines BuildWithLocus (hosting/deploy) with PayWithLocus (checkout/payments) and @withlocus/checkout-react (client SDK) to create a complete merchant tool that couldn't exist without both platforms working together

Team **Vibe** -- [Muhammad Firdaussyah](https://github.com/maulana-tech)

`2026-04-23`

---

### Locus Sentinel
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/locus-sentinel-0bac) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Souvik-Dey-2029/Locus-Sentinel) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1zAcZLhYSCA) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Locus Sentinel: Pay only for verified outcomes.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Current agentic workflows suffer from a **"Verification Gap."** While **BuildWithLocus** allows agents to provision infrastructure with unprecedented speed, these deployments are **financially blind**. Standard CI/CD pipelines only check if a container is "Running," but they fail to verify if the application is "Functional" from a user’s semantic perspective. This leads to **Capital Bleed**: users are billed for deployments that result in 404s, stale headers, or silent database connection failures.

**Locus Sentinel** introduces the industry's first **Autonomous Settlement Layer** for infrastructure. By positioning itself as a high-fidelity intermediary between the **PayWithLocus** wallet and the PaaS layer, it creates a **Programmable Escrow**. 

The system doesn't just deploy; it **audits**. Using a multi-modal "Sentinel AI," it verifies **Semantic Success**----ensuring the live environment actually matches the user's Natural Language intent. If the audit fails, Sentinel triggers an **Atomic Rollback**, protecting user capital and ensuring that in the agentic economy, **liquidity only flows toward verified outcomes.**

**Challenges we ran into**

The primary technical challenge was solving the **Asynchronous Latency Mismatch**. I had to bridge a high-velocity Deployment API with a "slow-thinking" LLM-based Auditor. To solve this without degrading the UX, I engineered a **Server-Sent Events (SSE) Orchestrator**. This allows for a non-blocking telemetry stream, providing the user with real-time "NOC-style" feedback while the heavy AI computation happens in the background.

Another significant hurdle was maintaining **Financial Data Integrity** in a sandbox environment. I developed a **Hybrid Balance Engine** with intelligent mock-fallbacks. This engine ensures the dashboard remains "Production-Ready" by simulating high-fidelity transaction manifests and "Gas Saved" metrics when on-chain liquidity is low. This required complex state management to ensure that the transition from **Simulated Settlement** to **Mainnet Execution** is seamless and transparent to the end user.

**Track: Using BuildWithLocus to leverage our suite.**

Locus Sentinel is engineered as a **Governance and Financial Safety Layer** that sits directly on top of the **BuildWithLocus PaaS**. Our project fits this track by solving the critical "Trust Gap" in autonomous infrastructure management through three deep integrations:

* **PaaS Orchestration:** Sentinel utilizes the **BuildWithLocus API** to provision agent-native containers, routing, and SSL dynamically. It replaces traditional DevOps with a "Natural Language Infrastructure" interface, directly aligning with the Locus mission of "No Cloud Console, No Dockerfiles."
* **Programmable Financials (PayWithLocus):** We have integrated the **Paygentic Wallet layer** as a state-dependent circuit breaker. By utilizing the user’s Locus wallet, Sentinel creates a **conditional settlement flow**: funds are only released from escrow if the AI Sentinel verifies that the deployment matches the user’s intent.
* **Economic Agentic Utility:** The core goal of Week 2 is to build agents that "make you money." Sentinel achieves this by **preventing Capital Bleed**. It ensures that users are never billed for broken builds, 404 errors, or misconfigured environments, creating a 100% capital-efficient deployment cycle on the Locus suite.

By combining **BuildWithLocus** for the heavy lifting of containerization and **PayWithLocus** for the settlement, Locus Sentinel provides a complete, financially-aware infrastructure protocol for the agentic economy.

[Souvik Dey](https://github.com/Souvik-Dey-2029)

`2026-04-23`

---

### AutoMind
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/automind-5f09) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://automind-2.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XAJnZXmaFOI) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AutoMind: Predict. Prevent. Protect.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

🚗 The Problem It Solves – AutoMind

AutoMind addresses the critical issue of unexpected vehicle failures that can lead to accidents, costly repairs, and dangerous situations on the road.

💡 What people can use it for:
Early Failure Detection:
Predicts potential car failures before they happen using real-time sensor data and machine learning.
Driver Safety Enhancement:
Alerts drivers about critical issues (engine faults, brake issues, overheating, etc.) to prevent accidents.
Cost Reduction:
Helps users avoid expensive repairs by identifying problems at an early stage.
Smart Maintenance Planning:
Suggests optimal servicing time instead of relying on fixed schedules.
Fleet Management Optimization:
Useful for logistics and transport companies to monitor multiple vehicles and reduce downtime.
⚡ How it improves existing systems:
Moves from reactive maintenance → predictive maintenance
Reduces human dependency on manual inspections
Provides real-time, AI-driven insights instead of delayed diagnostics
Makes driving safer, smarter, and more reliable

**Challenges we ran into**

Building AutoMind came with several technical and practical challenges, especially while working with real-time prediction systems.

🧩 1. Inconsistent & Noisy Sensor Data

One major issue was that vehicle sensor data was often incomplete, noisy, or inconsistent, which affected model accuracy.
Solution:

Applied data preprocessing techniques like filtering, interpolation, and normalization
Used feature engineering to extract meaningful patterns from raw signals
🤖 2. Model Accuracy vs Real-Time Performance

Balancing high prediction accuracy with low latency was difficult, especially for real-time alerts.
Solution:

Optimized the model by reducing complexity and selecting only important features
Used lightweight architectures to ensure faster inference
🔄 3. Lack of Real-World Failure Data

Getting real-world labeled data for vehicle failures was a challenge since such events are rare.
Solution:

Used synthetic data generation and simulation techniques
Augmented datasets to mimic real-world failure scenarios
⚡ 4. Real-Time Data Handling & Integration

Streaming and processing continuous data from sensors without delay was complex.
Solution:

Designed an efficient data pipeline for real-time ingestion and processing
Implemented buffering and asynchronous handling to avoid bottlenecks
🚨 5. Reducing False Alerts

Initially, the system generated too many false positives, which could reduce user trust.
Solution:

Fine-tuned model thresholds
Introduced confidence scoring and alert prioritization
🛠️ 6. Deployment & System Integration

Integrating the ML model with a working application environment was not straightforward.
Solution:

Containerized the system for smooth deployment
Created APIs to connect the model with the frontend/dashboard

Team **CosmoTech** -- [Khushi Gaba](https://github.com/KG1811), [Mukul Negi](https://github.com/mukulnegii), [Lakshit Gulia](https://github.com/lakshitgulia)

`2026-04-15`

---

### Credit Risk analyzer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/credit-risk-analyzer-a850) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Predicting risk, Protecting assets

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

This project is a credit risk analyzer which takes user input data and compares it to set parameters to return output. It is used to identify if the customer poses a risk or is safe to give loan to. I take data from user like age, annual salary, loan amount and credit score and compares it to set parameters then gives two outputs. whether the customer is safe to give loan to or the customer is risky according to given values.

Team **veltech** -- Hariom Chaubey, Shraddhayushi srivastav, Niraj Meena

`2026-04-15`

---

### Flowpay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/flowpay-1b01) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/t0k1t00/flowpay-agent) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/jYjHDb_W3HY) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/jYjHDb_W3HY) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Autonomous B2B sourcing, escrow & compliance

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![resend](https://img.shields.io/badge/resend-333333?style=flat-square) ![Firecrawl](https://img.shields.io/badge/Firecrawl-333333?style=flat-square) ![Exa](https://img.shields.io/badge/Exa-333333?style=flat-square)

**The problem it solves**

Procurement today is still painfully manual — spread across Excel sheets, emails, calls, and WhatsApp threads. This leads to slow execution, poor visibility, vendor risk, and uncontrolled spending.

Flowpay transforms procurement into a single autonomous workflow powered by AI agents and programmable payments.

* Users input a sourcing request in natural language
* The agent discovers, verifies, and ranks suppliers
* Quote requests are sent automatically
* Escrow is created with built-in spending controls
* High-value transactions trigger human approval
* All financial actions are governed by policy checks
* Every step is streamed in real time and logged in an audit trail
* Compliance flows (like GST payments) can run via virtual cards

Instead of treating payments as the last step, Flowpay makes financial control the core decision layer of procurement.

**Result:** Faster sourcing, safer transactions, and complete transparency — without removing human oversight where it matters.

**Challenges we ran into**

Building Flowpay end-to-end was much harder than it looks on the surface.

**1. Real-time orchestration complexity**
We had multiple moving parts — agent reasoning, supplier discovery, escrow states, and frontend logs — all happening asynchronously.
One misordered event could break the entire user experience.
→ Solved using structured event streaming over WebSockets with strict sequencing.

**2. Financial state correctness**
Escrow transitions (reserve → approve → release → refund) directly affect wallet balance.
Any inconsistency = broken trust.
→ Implemented strict state transitions + boundary tests to guarantee correctness.

**3. External API unpredictability**
Search, scraping, email, and compliance integrations can fail or rate-limit — especially during a hackathon.
→ Built deterministic fallback paths and wrapped integrations to ensure demo reliability.

**4. Balancing autonomy vs control**
Fully autonomous agents sound great, but real procurement requires trust and control.
→ Introduced human-in-the-loop approval for high-value transactions and policy-based guardrails.

**5. System design under time pressure**
Designing a multi-agent pipeline (parse → search → enrich → email → escrow → compliance) in limited time was intense.
→ Solved with clear service boundaries and modular orchestration architecture.

**Using PayWithLocus.com to leverage our suite.**

Flowpay is built directly around the PayWithLocus model: programmable payments with control, not just transfer.
Instead of treating payments as the final step, we made Locus-style controls the decision layer for the whole procurement workflow.

Every sourcing run in Flowpay goes through:

* Wallet and spending controls with daily and monthly caps
* Auto-approve threshold logic for low-value transactions
* Human approval routing for high-value transactions
* Category-based policy checks before escrow is created
* Full escrow lifecycle handling: reserve, approve/reject, release, refund
* Virtual card provisioning and debit flows for compliance payments
* GST automation path tied to controlled card payments
* Audit trail and real-time financial event streaming for transparency

We also support a wrapped API mode using the PayWithLocus gateway configuration so external actions can be routed through the Locus integration path in live mode.

In short, this project fits the track because PayWithLocus-style financial guardrails are core to how the agent operates, approves, and settles procurement actions safely.

Team **Symphony** -- [Swathi B Raj](https://github.com/t0k1t00), [Keerthivasan Venkitajalam](https://github.com/Keerthivasan-Venkitajalam)

`2026-04-16`

---

### Sub-Zero
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/subzero-9906) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Atharvanair09/Sub-Zero) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Money buddy

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

Team **BugSolvers** -- [Atharva Nair](https://github.com/Atharvanair09), [Oom Murkar](https://github.com/OmMurkar), [sahil ojha](https://github.com/Sahilojha731), [Sakshi Pawar](https://github.com/spawar-18)

`2026-04-16`

---

### AtlasPay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/atlaspay-05b9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tronik87/AtlasPay) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.kaggle.com/code/neelraah/notebook820404b117) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SFPWfQ6N7wA) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Google Maps for payments"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

Cross-border payments still run on decades-old infrastructure. A wire transfer from India to the UK takes 1–5 business days, passes through 3–5 intermediary banks each charging hidden fees, and has up to a 10% failure rate due to validation errors caught only after the transaction is already in flight. The $120B spent annually on cross-border fees is largely a tax on this inefficiency.

AtlasPay replaces blind correspondent routing with intelligent multi-rail 
orchestration. For any given transaction, AtlasPay evaluates all available payment 
rails in real time and selects the fastest, cheapest, most compliant path before a single dollar moves.

It solves three distinct problems simultaneously:

Pre-execution failure prevention: a high quality pre validation engine screens wallet addresses against OFAC/UN/EU/RBI sanctions lists, verifies currency compatibility, enforces FEMA and FATF regulatory thresholds, and rate-limits-suspicious velocity patterns before routing begins. The 5–10% failure rate of current systems is largely preventable; AtlasPay prevents it.

Routing opacity banks have no incentive to find you the cheapest path. AtlasPay's graph-based routing engine models all available payment rails as a weighted directed graph, then runs optimization across cost, settlement time, FX spread, and compliance constraints simultaneously to find the optimal path for each specific corridor, and shows you the comparison before you commit.

Anomaly detection: A PyTorch autoencoder flags statistically unusual transactions before they enter the routing pipeline, adding a behavioral risk layer on top of the rule-based pre-validation checks.

**Challenges we ran into**

Graph weight calibration: The routing engine models payment rails as a weighted directed graph, but cost, speed, and compliance constraints are measured in completely different units. Normalizing these into a single comparable edge weight without over-indexing on one dimension (always picking the cheapest rail even when it takes 5 days) required iterative tuning of weight coefficients and corridor-specific penalty functions.

Handling missing and inconsistent rail data: Not all rails are available for all corridors, and availability changes over time. The routing graph had to gracefully handle sparse corridors where only one or two rails exist, without the optimizer defaulting to nonsensical paths or throwing errors on missing edge weights.

Autoencoder threshold calibration: The anomaly detection model flags transactions whose reconstruction error exceeds a learned threshold. Too low and it blocks legitimate payments; too high and it misses real anomalies. We calibrated against held-out corridor data and stored the final value in threshold.txt, but the boundary between unusual-but-legitimate and genuinely anomalous in remittance data is thin and corridor-dependent.

Feature engineering on ordinal speed data: The World Bank RPW dataset stores transfer speed as six categorical buckets (same day, next day, 2 days, and so on) rather than continuous values. Feeding this into the autoencoder without careful encoding caused the model to treat speed categories as arbitrary labels with no distance relationship, distorting reconstruction error. Mapping to numeric midpoints and scaling consistently with the rest of the feature space fixed this.

Integrating anomaly scoring into routing: The autoencoder produces a reconstruction error score, but deciding when that score should override an otherwise optimal route required a clear handoff between the two models. A high anomaly score on the cheapest rail needed to demote that rail in the graph rather than block the transaction outright, which meant feeding the score back as a dynamic edge weight penalty rather than a hard gate.

**FinTech**

AtlasPay directly addresses the core infrastructure problem in global payments: banks route cross-border transactions blindly through fixed correspondent chains with no cost optimization, no pre-validation, and no transparency. The routing engine treats all available rails as a weighted graph and selects the optimal path per transaction by cost, speed, and compliance constraints. The pre-validation layer enforces sanctions screening, regulatory thresholds, and velocity limits before any routing decision is made. The anomaly detection model flags statistically inconsistent transactions against corridor norms. These are not demo features — they are the actual components a production payment orchestration layer needs.
The FinTech track targets financial infrastructure, inclusion, and compliance technology. AtlasPay covers all three: it reduces the cost and time of cross-border transfers that disproportionately affect high-fee corridors like South Asia and Sub-Saharan Africa, it makes cost breakdowns visible to the sender before commitment (the basic requirement for a transparent market), and it treats compliance as first-layer infrastructure rather than an afterthought. The World Bank RPW dataset grounding the anomaly model represents 14 years of real remittance market data across 367 corridors — the problem AtlasPay is solving is quantified, not hypothetical.

Team **€∆$¥¥** -- [Nikhilesh Ravi](https://github.com/Tronik87), [Ivan George](https://github.com/ivan-george710), [Sachithan Chandru](https://github.com/Sachithan3), [Harleen .](https://github.com/Neelraah)

`2026-03-29`

---

### DukaanIQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dukaaniq-a707) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Khushi-Dhir/Hackathon-App-DukaanIQ/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Know Your Stock, Grow Your Store

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Running a small shop or retail store can be overwhelming, with products constantly coming in and going out, some nearing expiry, and stock levels changing every day. Keeping track manually or on spreadsheets is stressful, time-consuming, and prone to mistakes. DukaanIQ solves this by giving store owners a smart, easy-to-use system to see exactly what’s in stock, track perishable items, prevent overstocking or running out of products, and make informed decisions quickly. It turns inventory chaos into a clear, manageable process, freeing owners to focus on growing their business instead of worrying about what’s on the shelves.

**Challenges we ran into**

While building DukaanIQ, I ran into several challenges. Designing a system that tracks both products and individual batches was tricky, especially handling perishable items with expiry dates. Keeping the frontend and backend in sync so stock updates in real time without errors required careful API design and state management. I also faced challenges with user experience, making sure selecting batches, adjusting quantities, and completing sales felt intuitive and fast. Finally, ensuring data integrity - so sales never accidentally oversell stock -and implementing secure token-based access were critical hurdles that required thoughtful solutions.

Team **Tech4Tomorrow** -- Ruchika ., [Khushi Dhir](https://github.com/Khushi-Dhir), Bhavya sharma

`2026-03-08`

---

### Meridian
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/meridian-5495) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shriya-upadhyay/meridian) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0lNDOqFMeoM) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Private Cross-Border Payments

![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![DAML](https://img.shields.io/badge/DAML-333333?style=flat-square)

**The problem it solves**

Meridian helps solve the UI/UX friction in cross-border FX payments by providing a compliance-first, efficient, and easily accessible framework for stablecoin settlement on the Canton Network. Selective disclosure ensures each party (sender, recipient, regulator) sees only the data relevant to their role, while automated AML/KYC screening runs inline at acceptance time, not as a separate manual process. This enables compliance and privacy to be a priority in on-chain FX transactions.

**Challenges we ran into**

One issue I ran into was figuring out how to prevent different users from accessing sensitive information on a shared smart contract. I was able to overcome this by creating separate smart contract payments for each of them.

**New France Village**

Meridian helps enable seamless cross-border FX payments on-chain without compromising on privacy.

**Best Privacy-Focused dApp Using Daml**

Meridian leverages Canton network's privacy engine to allow for selective disclosure of transaction information to each involved party.

[Shriya Upadhyay](https://github.com/shriya-upadhyay)

`2026-02-21`

---

### Canton Invoice
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/canton-invoice-a262) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](http://github.com/derek2403/ethdenver) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/10NKhhXzPsWj1MhAvTNckXsnMjFPrwj6o?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> One Invoice, Four Views

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square)

**The problem it solves**

In traditional invoicing, every party in the supply chain — the seller, buyer, logistics carrier, and bookkeeper — typically sees the exact same document. This creates a serious privacy problem: your shipping carrier knows your profit margins, your accountant sees customer delivery addresses, and your buyer sees your internal cost structure. Businesses either accept this data leakage or resort to manually creating separate documents for each party — an error-prone, time-consuming process.

Canton Invoice solves this with structurally enforced privacy. When a seller creates a single invoice, the system automatically generates four distinct, role-appropriate views:

🏷️ Seller — Full invoice with line items, pricing, payment controls, and the ability to share views
💳 Buyer — Payment-focused view with amounts due, payment status, and wallet integration
🚚 Carrier — Logistics-only view with shipping addresses, item names, quantities, and delivery terms — no prices, discounts, or tax data exist in this view at all
📊 Bookkeeper — Financial summary with totals, tax breakdowns, and invoice status — no addresses, contacts, or line item details
This isn't just app-level filtering where sensitive data is hidden by the UI. Each view is a separate Daml contract on the Canton Network where restricted fields are structurally absent from the template. Even if a carrier's node is compromised, price data cannot be recovered — because it was never there.

Real-world use cases:

A manufacturer shares logistics details with a 3PL provider without exposing wholesale pricing
A CFO shares financial records with an external auditor without leaking customer PII or shipping details
A buyer sees only what they owe and pays directly through Canton wallet integration
Canton Invoice also integrates with the Splice Token Standard for native on-ledger payments using Canton Coin, with AllocationRequest-based settlement that creates immutable PaymentReceipt contracts as proof of payment.

**Challenges we ran into**

1. DevNet Connectivity Issues
Our biggest operational hurdle was connecting our validator node to the Canton Global Synchronizer. After deploying on DevNet3, we found that multiple sequencer nodes (Tradeweb-Markets-1, Cumberland-1, Cumberland-2) were either unreachable or returning TLS certificate mismatches (ingress.local instead of the expected domain). This produced persistent SYNC_SERVICE_BAD_CONNECTIVITY errors for hours. Since these were infrastructure issues outside our control, we had to migrate to DevNet5 — which required understanding the full 
start.sh
 bootstrapping flow, debugging port conflicts with other teams on the shared machine, and re-onboarding with fresh credentials.

2. Designing Structural Privacy in Daml
Getting the disclosure model right was non-trivial. The key insight was that privacy should not be enforced at the API or UI layer — it needs to be baked into the Daml template structure itself. We created separate LogisticsView and BookkeeperView templates that are deliberately missing sensitive fields (e.g., LogisticsItem has no unitPrice, discount, or taxRate fields, unlike LineItem). The Invoice_ShareWithCarrier choice maps LineItem → LogisticsItem, stripping price data during the transformation. This required careful type design to ensure each view was self-contained and correct.

3. Multi-Role Authentication on LocalNet
Supporting five distinct roles (seller, buyer, carrier, bookkeeper, app-provider) with proper party isolation on a single LocalNet instance required wiring up the participant node's ledger user system carefully. Each role maps to a different Daml party, and the 
DashboardRouter
 dynamically renders the correct dashboard based on the logged-in user's identity. Getting the splice-onboarding module to allocate and wire up the logistics and finance parties with correct ReadAs/ActAs rights took significant iteration.

4. Real-Time Dashboard Updates
Each dashboard polls its respective contracts (invoices, logistics views, bookkeeper views) at 5-second intervals, but ensuring the frontend correctly reflected the state transitions — especially when a seller marks an invoice as paid and it auto-shares views with carrier and bookkeeper before archiving — required careful sequencing of nonconsuming and consuming Daml choices.

**Use of AI tools and agents**

We used AI coding assistants (Claude/Antigravity) heavily as a pair-programming and debugging partner, especially during implementation and DevOps
Debugging & Execution Acceleration (AI):
AI was most valuable for unblocking us during development by:
	•	Diagnosing infra failures: reading Docker + Canton logs line-by-line, isolating TLS/cert and synchronizer connectivity failures, and helping confirm whether issues were on the sequencer side vs. our local configuration.
	•	Guiding fixes with runnable steps: generating exact commands and configs (e.g., updating startup scripts, fetching migration identifiers, adjusting environment variables), and iterating quickly when errors changed.
	•	Rapid code execution + iteration: proposing small, testable patches, then helping us validate behavior through repeated run → observe → fix cycles (especially for node connectivity, port conflicts, and Ledger API integration).

[Liew QiJian](https://github.com/derek2403)

`2026-02-21`

---

### BudgetUp
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/budgetup-b8f7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.figma.com/proto/Ufiw8mXLEDdeNWEN8Y5QuZ/Untitled?page-id=0%3A1&node-id=1-9&viewport=-814%2C204%2C0.64&t=dkLnbX3a6vDMyTHc-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=1%3A3) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your financial buddy

![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square)

Team **BlitzKoders** -- [Gitanshi Verma](https://github.com/gitanshiverma), [Garima Singh](https://github.com/garimasingh2005), [Khushi Bidhuri](https://github.com/khushibidhuri122), [Ankita Kashyap](https://github.com/student-Ankita-ai)

`2026-02-08`

---

### Vibe Check
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vibe-check-178a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nikhiljha3050/Hostel-expense-tracker) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Keeping your hostel finances and life in check

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

The Problems We Are Solving
Living in a hostel for the first time, I realized that the biggest headaches aren't the classes, but the daily "unorganized chaos." Here is exactly what our project solves:

The "Awkward" Money Talk: Let’s be real—asking a friend or your roommate for ₹50 back for chai or an auto ride is just plain awkward. Usually, these small costs get forgotten, but they add up to a huge loss by the end of the month. Our app handles the "reminding" part automatically. By logging it, it becomes a simple data point rather than a personal confrontation between friends.

The End-of-Month "Maggi" Phase: We’ve all been there—starting the month like a king and ending it broke, wondering where all the money went. The app gives us back that visibility. By categorizing spends into things like "Canteen," "Travel," and "Laundry," students can see exactly which "leak" is draining their budget before they run out of cash.

**Hostel Life Utility Manager - UI/UX Beginner Track (Freshers Only)**

This project fits the track because it’s not just another 'tracker'—it’s a centralized digital hub. We focused on making the UI extremely high-speed; we know a student won't use an app if it takes 10 clicks just to log a ₹20 chai expense. By bringing expense tracking, maintenance requests, and utility management into one sleek interface, we’re proving that good design can solve the 'mental load' of living away from home. We’ve prioritized a 'mobile-first' experience because that’s where student life happens,

[Nikhil Jha](https://github.com/nikhiljha3050)

`2026-01-26`

---

### DeltaX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/deltax-618c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/araj170805/hackrit) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hackrit.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Oi5NDwEPG7Y) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co)

> Ideas That Create Impact

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Geocoding](https://img.shields.io/badge/Geocoding-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

Team **deltax** -- [Ritesh Singh](https://github.com/rsinghrajput2005-glitch), [Rohan Deo](https://github.com/rohandev-ai), [Ashish Raj](https://github.com/araj170805)

`2026-09-12`

---

### Credo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/credo-a518) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Muditapandey26/Credo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/yUzo4YvjJQY?si=gS_staUsO_ImzrnE) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/yUzo4YvjJQY?si=gS_staUsO_ImzrnE) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co)

> Managing your finances

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **Cipher** -- [Rwitama Aon](https://github.com/rwits08), [Mudita Pandey](https://github.com/Muditapandey26), [Pragati Kumari](https://github.com/pragati-codespace)

`2026-09-12`

---

### AlynePay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/alynepay-a533) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AlyneLabs/AlynePay) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Offline Decentralized Payment App and protocol

![DApp](https://img.shields.io/badge/DApp-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square)

**Challenges we ran into**

Our biggest challenge was connecting the React Native mobile app with the native Android Bluetooth/Wi-Fi mesh engine while ensuring payments sent the exact entered amounts in real-time. We ran into tricky bugs where the swipe-to-pay gesture remembered old numbers from memory and where payment screens flashed previous transactions instead of opening clean. We solved this by building an embedded local bridge server inside the Android service to handle radio traffic and using dynamic memory references in our gesture code, allowing the app to seamlessly find nearby phones, reset payment states instantly, and reliably bounce offline money across devices.

**The problem it solves**

Today’s payment apps stop working the moment you lose internet—whether you are stuck in an underground subway, packed in a crowded stadium where cell signals fail, traveling in remote areas, or dealing with natural disasters when phone towers go down. AlynePay solves this by letting your phone connect directly to nearby phones using Bluetooth and Wi-Fi, allowing you to send and receive money instantly without cellular data, Wi-Fi routers, or central bank servers.

This makes paying for everyday essentials completely reliable because transactions never fail from weak signals or bank server downtimes. Even if the person you want to pay is further away, your payment automatically and securely hops through other nearby phones in the background to reach them, making digital payments truly fail-safe anywhere, anytime.

Team **AlyneLabs** -- [Lalith Adhithiya](https://github.com/Indra-Official), [Fawwaz Ahamed](https://github.com/fawwazahamedf2025-lgtm), Vetri Selvan, [Jaikishore NH](https://github.com/JaiKishore-x17)

`2026-09-02`

---

### PawBudget
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pawbudget-0d4d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Swati-web-arch/PawBudget) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4Gko-iAG2FI?si=0Gl-8YTL1fA0l0gN) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Saving one pet at a time

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

The major challenge was finding a dataset that contained all the necessary data. It was across different sites and were highly haphazard and random. Training the data sets and incorporating them into one model was highly difficult.

**The problem it solves**

We noticed that millions of pets were abandoned every year mainly due to financial incapabilities. There are no clear resources for estimating how much finances are required to manage pets. Our app takes into consideration the breed, size, age, insurance of the pet and gives and approximate cost required to take care of their pet. It also showes cases for emergency and takes into consideration regular grooming and vet visits.

Team **Meow meow meow** -- Ashita Kuchhal, [Aneesha Yadav](https://github.com/an4848), Jaagriti Mandal, Swati Yadav

`2026-09-02`

---

### UAV System for Disaster Management and Relief
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/uav-system-for-disaster-management-and-relief-9dfa) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1YYgSqKJrKFLqutK3SuzEc1HkhXtrdUPz/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> Helping People

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

### 1. Integrating multiple hardware components

One of our major challenges was integrating several components—GPS, thermal camera, PIR sensor, telemetry, ESP32-S3, flight controller, ESCs, motors, battery and the payload mechanism—into a single UAV without making the system unnecessarily heavy or unstable. The architecture contains a large number of interconnected hardware modules. 

**How we handled it:**
We followed a modular architecture, separating the flight-control system, sensing system, communication system and payload mechanism so that individual components could be tested independently before integration.

### 2. Limited battery and flight endurance

The drone has to carry not only the flight hardware but also cameras, sensors, processing electronics and a payload. Increasing the payload increases the power requirement and reduces flight time. Your SWOT explicitly identifies **limited flight endurance and battery dependency** as weaknesses. 

**How we handled it:**
We focused on keeping the payload modular and lightweight and designed the system around the idea that different UAVs could eventually be used for different missions.

### 3. Maintaining communication in disaster zones

A disaster can damage communication infrastructure or create interference. At the same time, Meghdoot needs to transmit telemetry, live video and victim/hazard information to the ground station. Your presentation identifies **GPS and communication interference** as a specific threat. 

**How we handled it:**
We designed the UAV and ground station as separate systems with dedicated telemetry and communication components, while keeping temporary/alternative communication as an important part of the architecture. 

### 4. AI detection is not always reliable

Detecting a victim from aerial imagery is much harder than simply detecting an object in a controlled environment. Lighting, smoke, debris, occlusion and viewing angle can affect detection.

This is why Meghdoot combines **RGB/AI vision with thermal imaging and motion sensing** rather than depending on a single visual input. 

A good way to tell the judges:

> “One challenge was that AI cannot be treated as 100% reliable in a disaster environment. Therefore, we designed it as a decision-support layer, while the rescue team retains final control.”

### 5. Autonomous navigation versus human control

A disaster environment is unpredictable. A completely autonomous UAV may encounter obstacles or conditions that were not anticipated during mission planning. At the same time, relying entirely on manual piloting reduces the benefit of automation.

Your architecture therefore includes autonomous capabilities while also having a manual control system. 

**Good judge answer:**

> “The challenge was finding the right balance between autonomy and human control. We want the system to automate repetitive tasks such as navigation and detection, but still provide a human operator with the ability to intervene whenever safety requires it.”

### 6. Payload versus flight stability

The relief-delivery mechanism is useful, but adding a gripper and supplies changes the drone's weight distribution and flight characteristics. Your system is intended to deliver **medical aid, communication devices and food packets**. 

So the challenge isn't simply *“Can the drone carry something?”* It is:

> “Can it carry the required payload while maintaining adequate flight time, stability and maneuverability?”

This is why your PPT identifies **limited payload capacity** as a weakness. 

### 7. Operating under unpredictable weather

Floods, wildfires and other disasters can involve strong winds, rain, smoke, heat and poor visibility. A UAV that works perfectly in a controlled environment may behave very differently in those conditions.

Your SWOT specifically lists **extreme weather conditions** as a threat. 

**Answer:**

> “We realized that disaster environments are much less predictable than laboratory environments. Therefore, environmental operating limits and failsafe mechanisms are essential before real-world deployment.”

### 8. Building an entire end-to-end system

Another challenge was that Meghdoot isn't just a drone. The proposed architecture involves the **UAV, onboard processing, AI, ground station, communication, control application, rescue-path planning and relief delivery**.

**The problem it solves**

The problem Meghdoot solves is the **lack of real-time situational awareness and the delay in disaster response**. During disasters such as floods, wildfires, landslides, and other emergencies, rescue teams often struggle to understand what is happening on the ground because the affected areas may be inaccessible or dangerous. 

There are several interconnected problems:

* **Inaccessible terrain:** Rescue personnel may not be able to immediately enter collapsed buildings, flooded areas, fire zones, or other hazardous locations.
* **Lack of real-time information:** Ground teams may not have an immediate view of the disaster area.
* **Difficulty locating victims:** Finding stranded or injured people quickly becomes difficult, particularly across large affected areas.
* **Delayed damage and hazard assessment:** Rescue teams need to understand hazards and infrastructure damage before safely entering an area.
* **Slow coordination:** Without a common real-time picture, deciding where to send rescue teams and resources takes longer.
* **Restricted communication:** Disasters can damage or disrupt existing communication infrastructure.
* **Delayed aid:** Even when victims are identified, delivering essential supplies can be difficult when roads and access routes are blocked.

These problems ultimately contribute to **loss of lives, infrastructure damage, economic losses, and delays in redevelopment**. 

### How Meghdoot addresses this

Meghdoot uses a UAV as an **aerial intelligence and response platform**. Instead of sending rescue personnel directly into an unknown or dangerous area, the drone can first survey it using **live video, thermal imaging, motion sensing, GPS and AI-assisted analysis**. It can identify potential victims and hazards and transmit the information to the ground station. 

The system then aims to support the rescue operation by:

**Detecting → Assessing → Communicating → Planning → Delivering**

1. **Detect:** AI-assisted analysis identifies potential victims and hazard areas.
2. **Assess:** The UAV provides aerial information about the disaster zone.
3. **Communicate:** Victim and hazard information is sent to the ground station.
4. **Plan:** The system processes possible rescue paths to help plan the operation.
5. **Deliver:** A payload/grab-and-release mechanism can deliver medical aid, food packets and communication devices to victims.

Team **ByteBusters** -- [Sourya Ghosal](https://github.com/lashterMC), [NANDINI DAS](https://github.com/alwaysnandini0309-maker), PRITHWIRAJ DUTTA, [Binamra Samanta](https://github.com/binamrasamanta4-commits)

`2026-08-30`

---

### Bloodbank Assistant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bloodbank-assistant-d3a0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aritranath16-eng/blood-bankchatbot) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> Find Blood Faster..Save Lives Faster

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

* Maintaining accurate blood availability data, as blood units can change frequently

* Handling dependency on the AI API and ensuring the chatbot remains functional if the API is unavailable.

* Protecting donor information and maintaining privacy and security.

* Integrating data from multiple hospitals and blood banks into one centralized platform.

* Ensuring the system can scale from a prototype using Excel and JSON to a real-time database in the future.

**The problem it solves**

Smart Blood Bank Management & Real-Time AI Assistance is a centralized web platform designed to make finding blood during medical emergencies faster and easier.

The platform brings information from multiple hospitals and blood banks into one system. Users can search for a required blood group, check its availability, find suitable hospitals and eligible donors, and reserve available blood units. 

It also includes an AI chatbot that allows users to ask blood-related emergency queries in normal language. If the AI service is unavailable, a rule-based fallback system keeps basic assistance working. 

The system also highlights critical blood shortages, helping identify blood groups that urgently need donations. The overall goal is to reduce the time and difficulty involved in finding blood during emergencies and make blood-bank management more organized and transparent.

Team **Tech Titans** -- [Sushmita Chakraborty](https://github.com/Sushmita1323), [Aritra Nath](https://github.com/aritranath16-eng), [Aritra Saha](https://github.com/sahaaritra732-ai), [ANTARA JANA](https://github.com/antarajana784-spec)

`2026-08-30`

---

### KREDZ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/kredz-d6a9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arpanbasak90-cyber/KREDZ.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/XQ0nDYrAEvQ) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XQ0nDYrAEvQ) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> Fake credentials don't survive KREDZ.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

- **Switching AI providers mid-build**: We originally used the Anthropic API for verification, but hit free-tier limits during testing, so we migrated the whole prompt/response pipeline to Groq's free Llama-3.3-70B endpoint — matching schemas and re-validating that the JSON output stayed reliable.
- **Reliable structured output from an LLM**: Getting the model to *always* return clean JSON (no markdown fences, no preamble) took prompt tuning plus a defensive parser (`_safe_parse`) that strips stray formatting before parsing.
- **Detecting fake/copied GitHub projects**: Rather than trusting the AI alone, we added heuristics on top of live GitHub API data — flagging repos with near-zero commits, same-day create/push timestamps, forked or template repos, and missing language data — before even asking the LLM to judge it.
- **Email delivery on free hosting**: Render's free tier blocks outbound SMTP ports, so we switched from raw SMTP to Resend's HTTPS email API to reliably deliver QR verification links to mentors.
- **Preventing tampering after submission**: We needed credentials to be immutable once submitted, so we built a SHA-256 bundle-hashing + locking system that rejects any resubmission attempt for an already-locked email.

**The problem it solves**

Verifying student credentials — certificates, internships, hackathon wins, GitHub projects — is slow, manual, and easy to fake. Mentors and institutions have no fast way to check if a submission is genuine, and students have no tamper-proof way to prove their work is original.

**KREDZ fixes this by combining:**
- **AI-powered verification** – an LLM (Groq/Llama) cross-checks a submitted credential's description, dates, and institution for internal consistency, and pulls **live GitHub repo data** (commit count, contributors, fork/template status, languages) to flag copied, empty, or last-minute "fabricated" projects.
- **Cryptographic locking** – each credential bundle is hashed (SHA-256) and locked on first upload, so it can never be silently edited or resubmitted differently later.
- **QR-based sharing** – mentors get a scannable QR/deep-link to instantly pull up a verification report and approve, reject, or flag it for manual review.

This turns credential verification from a slow manual trust exercise into a fast, evidence-backed decision — useful for hackathons, campus placement cells, and internship screening.

Team **TECHNOVA** -- Priyasmit Ganguly, Modhurima Ganguly, [Arpan Basak](https://github.com/arpanbasak90-cyber), Haimontika Roy

`2026-08-30`

---

### AstraFlow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/astraflow-8923) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://astra-flow-2-0.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Effortless finances. Intelligent insights.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**Challenges we ran into**

**Challenges we ran into**
Building a multi-modal financial copilot that seamlessly merges AI with rigid financial ledgers came with a unique set of technical and architectural hurdles. Here are a few specific challenges we faced and how we overcame them:

**1. The Multi-Channel Deduplication Problem**
**The Hurdle:** Because AstraFlow allows users to ingest data from multiple, overlapping sources (OCR receipt scans, SMS bank alerts, and CSV statement uploads), we immediately ran into the problem of double-counting. If a user scans a  *15 receipt for lunch and later uploads a bank CSV containing that exact same* 15 charge, a naive database update would count the expense twice, ruining the user's financial state.

**How we got over it**: We moved away from standard CRUD operations and implemented an immutable Event Ledger architecture combined with a custom **Duplicate Detection** service. Instead of directly updating an account balance, every piece of ingested data acts as an observation. We built matching heuristics that look at time-windows, exact amounts, and fuzzy-matching on vendor names. When the system detects high-confidence overlaps, it groups these observations into a single canonical transaction—ensuring a perfectly accurate financial state without forcing the user to manually reconcile their accounts.

**2. Serverless PostgreSQL Connectivity (Deployment)**
**The Hurdle:** Transitioning from our local development environment (which used a local SQLite database) to a production-grade serverless deployment on Vercel backed by PostgreSQL caused immediate 500 Internal Server Error crashes. Debugging the Vercel runtime logs revealed a ModuleNotFoundError: No module named 'psycopg2'. SQLAlchemy was failing to establish a database connection because the standard database adapter requires C-extension compilation, which isn't natively supported in lightweight serverless build steps.

**How we got over it:** We had to dive into how serverless runtimes handle Python dependencies. We resolved the crash by migrating our requirements to explicitly use psycopg2-binary. This provided a pre-compiled, serverless-friendly PostgreSQL driver that successfully spun up within Vercel's strict execution environment without requiring underlying OS-level C compilers.

**3. Monorepo Git Tracking Conflicts**
**The Hurdle:** To streamline our CI/CD pipelines, we restructured the project from isolated folders into a single monorepo containing both the Vite/React frontend/ and the FastAPI backend/. However, upon pushing to GitHub, the entire backend source code was missing. GitHub was only registering an un-clickable, empty folder reference.

**How we got over it:** We realized that during the migration, the backend/ folder had retained its own hidden .git directory from a previous standalone repository. Git was treating our backend as a nested "submodule" (gitlink mode 160000) rather than standard files. We fixed this by aggressively untracking the cached submodule via the Git CLI (git rm --cached backend), stripping out the nested .git directory entirely, and forcing the parent repository to adopt and track the backend files natively.

**The problem it solves**

**AstraFlow 2.0**
AstraFlow is an intelligent, AI-powered financial copilot designed to act as your "digital financial twin." It goes beyond traditional budgeting apps by automatically ingesting, categorizing, and analyzing your financial data across multiple formats to give you a complete, real-time picture of your financial state.

Whether you are tracking personal expenses, managing multiple income streams, or planning for long-term goals, AstraFlow reduces manual data entry and provides actionable insights to help you make safer, smarter financial decisions.

**What can people use it for?**
Automated Financial Tracking: Stop manually entering receipts and bank statements. AstraFlow automatically processes your data so you always know where your money is going.
Goal Planning & Tracking: Set specific financial goals (like saving for a house or paying off debt) and let the system track your progress and project completion dates based on your actual cash flow.
Income Reliability Analysis: Specifically designed for freelancers, gig workers, and those with variable income. AstraFlow analyzes your income streams to determine reliability and forecast future earnings.
Smart Obligation Detection: Never miss a recurring bill or subscription. The system automatically detects regular financial obligations and warns you about upcoming commitments.
**How does it make existing tasks easier & safer?**
**1. Frictionless Data Ingestion**
Manual budgeting is tedious and prone to human error. AstraFlow makes data entry completely frictionless by supporting multiple automated ingestion methods:

**OCR Receipt Scanning:** Snap a picture of a receipt, and the system extracts the vendor, amount, and date using Tesseract OCR.
** SMS Parsing: **Forward bank SMS alerts directly into the system to log transactions in real-time.
 CSV Uploads: Bulk import historical data directly from your bank statements.
**2. AI-Powered Financial Copilot**
Integrated with the Gemini API, AstraFlow features an intelligent conversational assistant. Instead of digging through spreadsheets, you can ask your financial twin questions like:

"How much did I spend on dining out last month?"
"Am I on track to hit my vacation savings goal?"
"Do I have enough cash flow this week to cover my upcoming bills?"
**3. Advanced Ledger Security & Accuracy**
AstraFlow utilizes an immutable Event Ledger architecture combined with Duplicate Detection.

**Safer Tracking: **Transactions are securely logged and cannot be silently overwritten, ensuring a perfect audit trail.
**No Double Counting: **If you upload a receipt and later import the corresponding bank statement, the system smartly identifies and merges duplicates so your balances are always accurate.
**4. Real-Time Financial State & Threshold Rules**
AstraFlow rebuilds your financial state dynamically from your ledger. You can set up custom Threshold Rules and boundaries (e.g., "Alert me if my checking account drops below $500" or "Warn me if my entertainment spending exceeds 20% of my income"). This proactive monitoring acts as a safety net, keeping you well within your financial boundaries.

Team **Fronx** -- [Nisha Perumal](https://github.com/NISHAPERUMAL123), [Sendhamil Selvan R](https://github.com/ssenthamil078-create), [Navenaa S](https://github.com/NISHAPERUMAL123)

`2026-08-29`

---

### NegotiAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/negotiai-0181) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://negoti-ai-pwnt.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> AI that negotiates invoice financing rates.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Deprecated model: Our LLM model (llama-3.3-70b-versatile) was deprecated mid-build, causing 404 errors — switched to Groq's current openai/gpt-oss-120b
Empty responses: The new model spent its token budget on internal reasoning, leaving no room for a visible answer — fixed by raising the token limit and lowering reasoning effort
Windows/OneDrive build failure: A native binary broke when the project lived in a OneDrive-synced folder — fixed by moving it outside OneDrive
Rate limits: Multiple agents calling the LLM per negotiation round risked hitting rate limits — added retries with backoff and fallback text so one failed call can't crash a demo
Genuine multi-dimensional scoring: Making sure the winner was picked by weighing rate, advance rate, fees, and speed together — not just sorting by rate — required a separate rules engine so the LLM narrates in character but never invents the numbers itself

**The problem it solves**

Supply-chain financing today is bilateral and fragmented: a supplier takes one invoice to one bank, gets one offer, and has no leverage. Simple "comparison" platforms don't fix this either, because the best offer isn't always the cheapest — advance rate, fees, tenor, and settlement speed all matter.

**NegotiAI **is a real competitive marketplace: multiple AI capital-provider agents negotiate live over an invoice using a Nash equilibrium-based matching protocol, evaluated on overall fit — not just the lowest rate.

What people can use it for :-

Suppliers submit an invoice and get multiple providers (bank, fintech, NBFC) competing for it, instead of one take-it-or-leave-it offer
Watch the negotiation happen live, round by round — providers and the supplier agent go back and forth on rate, fee percentage, and advance ratio until terms converge
Buyer creditworthiness is scored separately from supplier risk, directly shaping the terms each provider offers
The winning offer comes with an Executive Justification Memo — a plain-language, dimension-by-dimension comparison explaining exactly why it beat every alternative
Adaptive Memory toggle lets the market learn — a provider that had a weak outcome tightens its terms on a similar invoice next time
A Reset Ledger Data control lets you clear state and re-run the full negotiation from scratch.

Team **Caffeine Compilers** -- Shreyas Gupta, [Shruti Jori](https://github.com/shrutimanojjori2025-dotcom)

`2026-08-29`

---

### SilentFleet
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/silentfleet-b62e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/qwertystars/silentfleet1/tree/dev) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://silentfleet.qwertystars.org/) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Secure every agentic payment before money moves

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Lucide React](https://img.shields.io/badge/Lucide%20React-333333?style=flat-square) ![cloudflared tunnel](https://img.shields.io/badge/cloudflared%20tunnel-333333?style=flat-square)

**Challenges we ran into**

## Challenges We Ran Into

### 1. Integrating the Frontend and Backend

Our frontend and backend evolved separately and were using different API structures, authentication methods, and response formats. The frontend was originally built around an older FastAPI setup, while the latest backend used Cloudflare Workers and Hono.

We solved this by treating the latest backend as the source of truth, moving only the frontend code into it, and rewriting the frontend API layer to use the current `/api/v1/...` endpoints.

### 2. Making Security Decisions Trustworthy

Some early UI screens calculated values such as risk exposure, execution state, and intervention choices directly in the frontend. That was fine for prototyping, but not acceptable for a financial security product.

We moved all security-critical logic to the backend and followed a simple rule:

> **ML predicts, policy decides, authorization enforces, and the frontend only displays the result.**

### 3. Detecting Agent-Specific Risk

Traditional fraud detection mainly looks at the transaction itself. SilentFleet also needs to understand whether an AI agent was manipulated or acted outside its delegated authority.

We combined:

- deterministic policy and delegation checks;
- transaction-risk ML;
- behavioral/contextual risk;
- prompt and instruction provenance;
- counterparty and protocol checks.

This allows SilentFleet to detect attacks such as prompt injection, beneficiary substitution, scope escalation, and hidden payment mandates before money moves.

### 4. Keeping the System Explainable

A single risk score was not enough. Human reviewers needed to know **why** an action was blocked.

We added structured reason codes such as:

```text
AMOUNT_EXCEEDS_DELEGATION
DESTINATION_OUT_OF_SCOPE
UNTRUSTED_PAYMENT_INSTRUCTION
NEW_COUNTERPARTY
```

This made decisions easier to audit and easier to explain in the UI.

### 5. Balancing Security With Autonomy

Blocking every suspicious action would make autonomous agents impractical.

We designed SilentFleet around **Minimum Sufficient Intervention**, where the system can:

```text
ALLOW
CONSTRAIN
REQUIRE_VERIFICATION
ESCALATE
BLOCK
```

This allows safe actions to continue automatically while risky ones receive only as much intervention as necessary.

### 6. Secure Authentication and Approval

We also had to separate human approval from actual financial execution.

We integrated Clerk for user authentication and changed the flow to:

```text
Action
→ Risk Evaluation
→ Approval if required
→ One-Time Authorization
→ Execution
→ Audit
```

This prevents stale approvals, replay, and modified transactions from being executed using an old authorization.

**The problem it solves**

## The Problem It Solves

As AI agents become capable of making payments, purchasing services, managing subscriptions, using APIs, and interacting with financial systems, they introduce a new security problem: **an agent can make a technically valid payment that the user never actually intended or authorized**.

Existing payment-fraud systems mainly evaluate the transaction itself. SilentFleet protects the **decision that leads to the transaction**.

It acts as a security layer between an autonomous agent and financial execution. Before money is transferred, SilentFleet checks:

- whether the action is within the agent's delegated authority;
- whether the amount, asset, network, merchant, protocol, or beneficiary is allowed;
- whether the agent's behaviour is unusual compared with its normal activity;
- whether a website, API response, package README, tool, or other external content may have manipulated the agent;
- whether the requested action still matches the user's original objective;
- whether a counterparty or protocol is new or risky;
- whether human verification or approval is required.

SilentFleet can then **allow, constrain, request verification, escalate, or block** the action before signing or payment execution.

## What Can People Use It For?

SilentFleet can protect autonomous agents that:

- purchase cloud infrastructure or API access;
- make x402 machine-to-machine payments;
- pay invoices and approved vendors;
- manage subscriptions and SaaS services;
- use virtual cards;
- perform treasury or stablecoin operations;
- purchase resources for coding or research tasks;
- interact with external websites, APIs, plugins, tools, and AI skills.

## How It Makes Existing Tasks Safer

Consider an AI agent authorized to purchase hosting services for up to ₹5,000. While completing the task, it encounters a malicious webpage telling it to send ₹40,000 to a different account.

The payment itself may use valid credentials and look technically legitimate. However, SilentFleet can identify that:

1. the amount exceeds the agent's delegated authority;
2. the beneficiary is outside its approved scope;
3. the payment instruction came from untrusted external content; and
4. the proposed action no longer matches the agent's original objective.

SilentFleet can therefore stop the payment **before the transaction is signed or executed**.

It can similarly protect against:

- indirect prompt injection;
- beneficiary substitution;
- fake invoices;
- hidden recurring mandates;
- compromised tools;
- authority escalation;
- malicious OAuth integrations;
- fake support requests;
- manipulated external content.

## Why It Is Useful

Without SilentFleet, organizations may be forced to choose between two extremes:

- give autonomous agents broad financial permissions and accept significant security risk; or
- require a human to approve nearly every action, removing much of the benefit of automation.

SilentFleet enables a middle ground through **Minimum Sufficient Intervention**.

Routine, low-risk, authorized actions can continue automatically, while suspicious or high-impact actions can be:

- constrained;
- verified;
- escalated for human approval; or
- blocked completely.

Every important decision can also be recorded with its risk signals, policy version, authorization, approval, execution state, and audit trail.

**SilentFleet makes it safer to give AI agents real financial capabilities without giving them unrestricted control over money.**

Team **Peak** -- [Srijan Guchhait](https://github.com/qwertystars), [Soumya Prakash Jena](https://github.com/brovoski69), Harsh ‎, [Daksh Agarwal](https://github.com/daksh1403)

`2026-08-29`

---

### LienRho
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lienrho-f457) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Haise-727/LienRho) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lienrho.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Where invoices meet investors.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**Challenges we ran into**

1. The bug that broke our entire thesis, silently.

Our pitch is "the cheapest offer can lose." We hit POST /api/match late one night and it returned the cheapest offer as the winner. No error, no exception — just a confident wrong answer that looked exactly like a working marketplace.

Two correct decisions had never been joined. The scorer read sufficiencyFloor off the database row. The database track had deliberately started leaving that column null so the value would be derived from real obligations instead of seeded — the right call, and our whole differentiator. But the helper reading that column returns "unconstrained" when it's null. No gates. Rank on price alone.

deriveSupplierUtility() existed and was tested. It was called by nothing outside its own test.

Fix was small: derive from the cash position when one is present. The lesson wasn't — a failure that returns a plausible answer instead of an error is far more dangerous than a crash. The seed now asserts the three properties the demo depends on and exits non-zero if any stops holding.

2. A wrong number that read as right.

fees_paise = 2_500_000 with a comment saying "Rs 2,500". A rupee is 100 paise, so that's Rs 25,000 — a fee worth 25% of face value on a Rs 1,00,000 invoice. Absurd on inspection, and it still produced a plausible bid, because 2_500_000 reads as "2,500" at a glance. Every agent-generated bid was mispriced. Rewrote it as 2_500 * 100 so the unit lives where the value is defined.

3. Three implementations of one formula.

Effective cost got written three times. The third divided by the advance rather than net cash received — you pay for the money you actually got, not the money notionally advanced. Every percentage on screen understated true cost by ~23 basis points and contradicted the audit trail behind it, on a page whose whole claim is "every figure traces to a named function." Deleted the UI's arithmetic; it now renders what the server computed.

4. Every invoice claimed the same payroll.

A shared component defaulted its threshold to the demo invoice's value, and preferred that default over the real value passed in. The result was a sentence contradicting itself: "You need Rs 9,00,000.00 for GST remittance." Correct obligation derived live, wrong amount borrowed from another invoice. Open two invoices side by side and the "derived from your obligations" claim collapses. Removed every demo-constant default.

5. Two voice problems the docs don't warn you about.

Free ElevenLabs accounts can't use library voices — the obvious default returns 402 paid_plan_required. Premade voices attached to the account work fine. And "ended" doesn't reliably fire on blob-backed audio: our verification call plays five lines in sequence and stalled after line one, with no error, forever. Replaced event-based completion with bounded position polling, because a live demo must never hang on one event failing to arrive.

6. The recurring one.

npm ci broke CI four separate times with the same error: missing @emnapi packages. An incremental npm install on macOS drops Linux-only optional dependencies, so the lockfile passes locally and fails on the Ubuntu runner, every time, for a different person. The cure is a full clean reinstall. We eventually stopped re-diagnosing it and wrote the exact command into our file-ownership doc.

**The problem it solves**

A small supplier ships goods, issues an invoice, then waits 45-90 days to get paid. Payroll doesn't wait. So they call one bank and take whatever terms come back.

But showing them more offers doesn't fix it, because the cheapest offer is often the wrong one.

Three real bids on a Rs 10,00,000 invoice in our marketplace:

- Meridian Bank — 11.0% headline — delivers Rs 7,86,650.68 — true cost 13.76% — lands T+3
- Kaveri Capital — 12.2% headline — delivers Rs 8,65,763.84 — true cost 13.34% — lands T+1
- Rapidfin — 13.5% headline — delivers Rs 9,34,188.36 — true cost 13.73% — lands T+0

Kaveri is the cheapest offer in the market. It loses. This supplier needs Rs 9,00,000 by Friday for payroll, and Kaveri delivers Rs 8.65 lakh a day late. Meridian's 11% is actually dearer than Rapidfin's 13.5% once the 80% advance rate and Rs 2,500 fee are counted.

Every marketplace that ranks by price recommends the wrong lender here.

What we do differently:

- We derive what the supplier needs instead of asking. Nobody can honestly say they value settlement speed at 0.3 — elicited weights are noise dressed as data. We read their dated cash obligations and compute a sufficiency floor and a timing deadline. Nobody told us about that payroll.
- Those are gates, not weights. An offer that can't cover the need, or can't land in time, is disqualified — not ranked slightly lower.
- We will say "don't finance." When nothing clears the floor, that is the answer. A market that always transacts isn't exercising judgement.

Who it's for:

- Suppliers get competing bids ranked by what actually reaches their account and when, with a plain-English reason for every rejection.
- Capital providers see only opportunities matching their mandate, and deploy against risk-adjusted returns instead of chasing deal flow.
- Both sides get an auditable trail. Every rupee traces to a named function on a double-entry ledger that balances to Rs 91,00,70,750 on both sides. No language model produces a financial figure anywhere in the system.

What it isn't: competitive invoice discounting is regulated in India and licensed TReDS platforms already run multi-financier bidding. We aren't claiming to have invented that. What's different is clearing on multi-attribute suitability against need read from a supplier's real cash position, rather than a rate auction. The market is simulated and labelled as one.

Team **Codeysseus** -- [Yuvaraj R](https://github.com/YUVARAJ-R-ai), [Tharun Parykshyt](https://github.com/ConTresillo), Harsha Sakamuri, Ragav Hariharan

`2026-08-29`

---

### TRELLIS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trellis-ad1c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vit-hackathon-dkc7a7xg8-prathisha0910-4912s-projects.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Banks finance paper. Trellis finances reality.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem

Financing only reacts to paperwork — the PO and the invoice — not to what's actually happening to the goods in between (production, shipping, delivery). That gap means:

- SMEs wait weeks for cash against goods they've already produced/shipped
- Lenders either under-finance or trust stale/wrong documents
- The same asset can get pledged to multiple lenders with no shared record

Trellis finances the **asset's real, verified state** — continuously — instead of just the paperwork about it.

## Who Uses It, For What

- **SMEs** — unlock capital as soon as goods are produced/shipped, not just once invoiced; rates improve automatically as more gets verified
- **Lenders** — get a live, standardized view of asset state instead of raw documents; know instantly what's already claimed elsewhere
- **Buyers** — their delivery confirmation directly speeds up and cheapens their supplier's financing

## How It's Safer

- **Contradictions auto-freeze new financing** (e.g. ERP says shipped, GPS says truck never moved) — no manual catch needed, existing money stays untouched
- **No double-financing** — a shared ledger blocks any lender from over-claiming an asset
- **Every number is explainable** — no black-box amounts
- **AI never decides the money** — it only reads evidence; a separate deterministic system calculates and authorizes financing

**Challenges we ran into**

Challenges We Ran Into

Race conditions on the Root Ledger
Two simultaneous claim requests against the same asset could both read stale headroom and both try to commit, silently over-financing the asset. Fixed by scoping every claim insert inside a single atomic transaction (SELECT ... FOR UPDATE) per asset, so the second request re-checks headroom after the first commits, not before.

Keeping the LLM from indirectly influencing the money
Early on, a misclassified state from a single uncorroborated source could still nudge capital upward. We added a deterministic validator that requires two independent, corroborating sources before any capacity-increasing transition — so a bad LLM read alone can never move the number.

Contradiction detection false-triggering on normal latency
Early versions froze financing any time two sources reported at slightly different times, even with no real disagreement. Fixed by adding a freshness/tolerance window instead of comparing raw timestamps directly.

Team **Team VMAX** -- Kayalvizhi Muthukumar, Nikil N, Prathisha S, Akhil Raghavendra

`2026-08-29`

---

### T3 Trade
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/t-trade-27d9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0xgeorgemathew/t3trade-push-to-prod) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://t3trade.pages.dev) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/FbXYG4_68h8?si=h5I4HDAXEsY_AmTf) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> The first ITE — an IDE, but for trading agents

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Electron](https://img.shields.io/badge/Electron-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![WebSocket](https://img.shields.io/badge/WebSocket-333333?style=flat-square) ![Effect](https://img.shields.io/badge/Effect-333333?style=flat-square)

**How you are solving it?**

## T3 Trade: an ITE — the IDE, rebuilt for trading agents

T3 Trade is an **Integrated Trading Environment**: T3 Code (the open-source agent harness from Ping Labs) as the foundation, plus a GUI layer and an execution core that let an autonomous Claude agent trade live perpetual futures on Hyperliquid — inside an environment that enforces the rules, the way an IDE enforces a type system.

### What the agent actually does

You give it a **mission**: one market, a written strategy, a hard max-loss budget, an expiry. Then:

1. **It reads the market** — price structure, ATR across timeframes, funding, fees — and decides if there's a trade at all. In our live runs it *declined* entries where round-trip costs ate the edge: "Stand down — no position opened."
2. **It plans in writing** — entry, stop, target, trailing rule — published as a versioned plan you can read in the GUI.
3. **It acts through typed tools** — preview, submit, cancel. No shell. No raw API key. Every order passes a 17-item deterministic checklist before anything is signed: mandate, leverage, notional, exchange minimums, budget reservation, mandatory stop.
4. **It sleeps** — it arms watches (price crosses X, PnL reaches Y) and suspends. The environment wakes it only when the market does something, and hands it a fresh snapshot of position, orders, and budget.
5. **It manages the trade** — moves stops to breakeven, trails, banks the target, or gets stopped out. Every position must have an exchange-native reduce-only stop confirmed against the *canonical* size read back from Hyperliquid, or the environment intervenes.

### What the environment guarantees — whatever the agent decides

- **The budget is physical.** Full risk (planned loss + fees + slippage) is reserved *before* signing and released only on terminal state. The agent can't spend budget twice, or argue past a limit.
- **Retries can't double a position.** Deterministic order ids (SHA-256 of mission ‖ sequence ‖ action) + an idempotency key: a retried submit returns the existing record.
- **The exchange is the truth.** Positions, orders, and fills are always reconciled from Hyperliquid. The database records what the agent *did*; the exchange decides what is *true*.
- **The kill switch skips the model.** Pause, cancel entries, reduce 25–100%, close, revoke — seven controls in the GUI that run deterministically **with the agent process stopped**.

### The GUI layer

An IDE isn't just a compiler — it's the window on the work. The T3 Trade workspace shows the agent's plan, the live position chart with entry/stop/target bands, the armed watches, risk-per-position, and one-click human controls. You supervise a trader, not a terminal.

### Scope and prior work — disclosed

The foundation is **[T3 Code](https://github.com/pingdotgg/t3code)**, an existing open-source agent harness from Ping Labs — we forked it and kept it close to upstream (every divergence is tracked in `docs/upstream/PATCH_LEDGER.md`). **Everything that makes it an ITE was built during this hackathon**:

| Path | Built here |
| --- | --- |
| `packages/trading-contracts` | The rules: preview checklist, protection, risk equations |
| `packages/hyperliquid` | The exchange client: signing, reads, WebSocket |
| `apps/server/src/trading` | Mission engine, execution, reconciliation, controls |
| `apps/web/src/components/trading` | The GUI: mission workspace and risk chrome |

The commit history on the public repo shows the split directly. Not previously submitted anywhere. **Hyperliquid testnet only** — live signing arms solely via a signer key; without it the environment runs read-only.

**What is the deployed URL for this project?**

https://t3trade.pages.dev

**What is the problem your project solves?**

## Developers got the IDE. Trading agents got nothing.

When humans write code, they get an IDE: an environment that watches over the work — syntax checks, type systems, version control, a debugger, an undo button. When coding *agents* arrived, they got harnesses like Claude Code and T3 Code: environments built so an autonomous process can do real work safely.

Now look at trading agents. Every "AI trading bot" today is one of two things:

1. **A script with an API key.** The model is one hallucinated decimal away from liquidation, and nothing structural stops it. No guardrails, no environment — just raw exchange access and hope.
2. **A copilot that can't act.** It writes market commentary and a human clicks the button. That's not an agent. That's a newsletter.

**There is no ITE — no Integrated Trading Environment.** No equivalent of the IDE for agents that trade: a place that gives an autonomous agent real market access *and* wraps every action in deterministic checks, protection, budgets, and a kill switch. In 2026, that tooling simply does not exist. We checked. We needed it. So we built it.

### What this unlocks right now

With a real ITE, one person can hand an agent a strategy, a market, and a hard loss budget — and walk away. The agent trades within its mandate, sleeps until the market actually moves, and physically cannot exceed what it was given. Not "probably won't." **Cannot.** That's the difference between a demo and something you leave running overnight.

### What the future holds

Every domain where agents touch real value — trading, payments, treasury, procurement — needs this same shape: intent from the model, limits from the environment. IDEs made software engineering an industry. ITEs are how autonomous trading stops being a party trick and becomes infrastructure. Somebody will build the environment layer every trading agent runs inside. We started today.

**How Did You Use Claude?**

## Claude is the trader. The ITE is built around it.

### 1. Claude runs the mission

Every mission is a Claude agent thread bound to one market. Claude reads the snapshot the environment hands it — account, position, resting orders, remaining budget — and does what a trader does: sizes an entry, places a stop, trails a winner, or refuses the trade because the math doesn't clear the fees. In our live testnet runs, Claude declined chop, priced round-trip costs into its targets, and wrote its reasoning into versioned plans you can read in the GUI.

### 2. The ITE thesis, in one line

**Claude gets full authority over intent, and zero authority over limits.** It acts only through typed tools — `trading_preview_order`, `trading_submit_order`, watch registration, `trading_control_*` — and every action passes a 17-item deterministic checklist before a signature exists. Claude proposes; the environment disposes. That separation is what makes handing a frontier model a live exchange account something you can defend, not just demo.

### 3. Event-driven, so autonomy is affordable

Claude isn't polled in a loop. It arms watches (price levels, PnL thresholds, candle closes) and suspends; the environment resumes it only when a watch fires. A mission can run for days with the model invoked only when the market moves — which is what makes an always-on Claude trader economically real.

### 4. Claude Code built the ITE itself

The entire environment was built inside T3 Code driving Claude Code, as a sequence of phased agent handoffs (`execution-plan.md`, PROMPT-04/05/06 in `docs/architecture/trading-execution.md`). Each phase documents the service surfaces, semantics, and caveats it hands to the next agent — the docs read as contracts between Claude instances. Claude built the environment; Claude trades inside it.

### 5. Why this matters beyond perps

The hard problem was never getting Claude to reason about a chart — it does that today. The hard problem was the environment where an autonomous Claude can hold real capital and be *structurally incapable* of exceeding its mandate. Typed tools, deterministic previews, reserved budgets, mandatory protection, out-of-band kill switches: that's the ITE pattern, and it generalizes to every domain where agents will touch money. Perps are the proof. The environment is the product.

Team **Taraxio** -- [Liz Merin George](https://github.com/lizgeorge1), [George Mathew](https://github.com/0xgeorgemathew/)

`2026-08-08`

---

### Secure Banking Transaction System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/secure-banking-transaction-system-88ec) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hritikkrgupta7746-ui/secure-banking-transaction-system) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/shorts/iR9tl-slfZk) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

![C](https://img.shields.io/badge/C-333333?style=flat-square)

**Challenges we ran into**

During the development of the Secure Banking Transaction System, I faced several challenges.

One of the major challenges was designing a proper structure for storing and managing customer account information efficiently. Ensuring that deposits, withdrawals, and balance updates remained accurate required careful validation and testing.

Another challenge was handling invalid user inputs and preventing incorrect transactions. To solve this, I implemented input validation and added checks before processing banking operations.

Managing multiple banking features within a single application while keeping the code organized was also difficult. I addressed this by dividing the program into separate functions for account creation, deposits, withdrawals, balance inquiry, and account management.

Testing different transaction scenarios and fixing logical errors helped improve the reliability and stability of the system.

![image](https://assets.devfolio.co/content/894aa00f4872442cac846b575ab7987c/c280e373-e959-4a99-8613-ce3b6707fb91.jpeg)

**The problem it solves**

Traditional banking record management can be slow, error-prone, and difficult to manage manually. Many small organizations and educational projects still rely on basic record keeping systems that lack security and efficiency.

Secure Bank Management System solves this problem by providing a simple and secure platform for managing customer accounts and banking operations. Users can create accounts, deposit money, withdraw funds, check balances, and manage customer records efficiently.

The system reduces manual errors, improves data organization, and provides a structured way to handle banking transactions. It also helps students understand real-world banking workflows and financial management systems through a practical implementation.

[Ritik Kumar](https://github.com/hritikkrgupta7746-ui)

`2026-07-30`

---

### Raksha402
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/raksha-1129) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ankit2061/raksha402-core-HEXAFALLS_2) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Payments protected before they happen

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Natural language processing (NLP)](https://img.shields.io/badge/Natural%20language%20processing%20(NLP)-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges we faced was connecting all the different parts of the project into one smooth payment flow. Features like QRSeal, IntentLock, MuleGuard and KinProof were working separately, but making them communicate with the frontend, backend, database and Solana blockchain was much harder than expected.

We also ran into problems while processing videos in KinProof. The deepfake detection model and MediaPipe were not properly connected to the FastAPI server, so uploaded videos could not be analysed correctly. We solved this by separating the video processing pipeline into smaller steps, such as frame extraction, face detection, deepfake prediction and final risk-score generation.

Another major hurdle was with Solana transactions. Our smart contract required the actual merchant wallet to sign a payment claim, but initially we were trying to complete it automatically from the backend. This caused authority and signature errors. We fixed it by understanding the signer rules properly and allowing the merchant to approve the claim through their wallet.

We also faced issues with large AI model files while pushing the project to GitHub. Some files were too large for GitHub’s limit, so the push failed. We removed the model files from Git history, added them to `.gitignore`, and created separate scripts to download the required models during setup.

Most of these problems were solved through repeated testing, checking logs, breaking large features into smaller parts and fixing them one by one. Since this was our first blockchain project, there was a strong learning curve, but each issue helped us understand the system better and improve the overall project.

**The problem it solves**

Raksha402 makes digital payments safer by checking more than just the payment amount and receiver address. People can use it for everyday payments, merchant payments, online purchases, bill payments and emergency money transfers. Before a payment is completed, it checks whether the QR code is genuine, whether the receiver matches the person or business the user intended to pay, and whether the transaction shows any unusual or risky behaviour.

This helps prevent common problems such as fake or replaced QR codes, payments sent to scam accounts, accidental transfers to money-mule accounts and fraud involving deepfake video or voice calls. Features such as QRSeal verify payment QR codes, IntentLock checks the real purpose of the payment, MuleGuard detects suspicious transaction patterns, and KinProof adds extra verification during family or emergency payment requests.

Instead of making users perform complicated security checks themselves, Raksha402 carries out these checks in the background and warns them before money is transferred. This makes existing payment tasks easier and safer while keeping the experience similar to normal payment applications.

**Best Use of Gemini API**

In pur Raksha402 project, in theIntentLock, we're using the Gemini API to sanity-check payments before they go through — basically making sure what the user says they want to do actually matches what the QR code is pointing to. It looks at things like the merchant name, who the money's actually going to, and the stated purpose of the payment, and cross-checks all of that against what's encoded in the QR.

So say someone scans a QR code meaning to pay a shop, but the code is actually tied to some unrelated personal account — IntentLock catches that mismatch before the transaction completes. Gemini then breaks down what went wrong in plain, easy-to-understand language, so the user gets a clear warning instead of just an error code, and can back out before losing money to a mistake (or worse, a scam).

**Best Use of Solana**

Raksha402 uses Solana as the core payment and settlement layer, not just as an add-on. Payments are approved through the user’s wallet, processed using Solana programs and recorded on-chain for transparency. Solana’s low fees and fast transactions make it suitable for everyday payments, while our AI modules check for QR fraud, mule accounts and deepfake scams before the transaction is signed.

**Best Use of MongoDB Atlas**

Raksha402 uses MongoDB Atlas as its main off-chain data layer. It stores customer and merchant profiles, verified merchant details, wallet information, payment history, transaction records and fraud-analysis results from QRSeal, IntentLock, MuleGuard and KinProof.

MongoDB’s flexible structure is useful because each security module produces different types of data, such as risk scores, QR details, identity checks and verification logs. It also connects smoothly with our React frontend, FastAPI backend and Solana payment system, while final payment settlement remains recorded on-chain.

**Best Use of Gemini API**

In IntentLock, we're using the Gemini API to sanity-check payments before they go through — basically making sure what the user says they want to do actually matches what the QR code is pointing to. It looks at things like the merchant name, who the money's actually going to, and the stated purpose of the payment, and cross-checks all of that against what's encoded in the QR.

So say someone scans a QR code meaning to pay a shop, but the code is actually tied to some unrelated personal account — IntentLock catches that mismatch before the transaction completes. Gemini then breaks down what went wrong in plain, easy-to-understand language, so the user gets a clear warning instead of just an error code, and can back out before losing money to a mistake (or worse, a scam).

**Best Use of Solana**

In Raksha402, Solana is used to handle the actual payment after all security checks are completed. When a user scans a QR code, modules like QRSeal, IntentLock, MuleGuard and KinProof first check whether the payment is safe. If everything is valid, the user approves the transaction through their Phantom wallet. The payment is then processed through our Solana program, and the transaction signature is stored with the payment record. This gives us fast settlement, low transaction fees and a verifiable on-chain history.

**Best Use of MongoDB Atlas**

For Raksha402, we're storing everything in MongoDB Atlas — customer and merchant profiles, verified merchant info, wallet addresses, payment history, the works. It's also where transaction records live, along with the risk scores that come out of QRSeal, IntentLock, MuleGuard, and KinProof once they've done their checks.

Once a payment actually goes through on Solana, we save the transaction signature back into MongoDB right alongside the rest of the payment details. That way, when someone wants to look up their payment history, everything's already tied together in one place — no jumping between the chain and the database to piece together what happened.

**Open Innovation**

Raksha402 fits the Open Innovation track because it combines AI and blockchain to make digital payments safer. It uses QRSeal to detect fake QR codes, IntentLock to verify payment details, MuleGuard to identify suspicious accounts, and KinProof to detect deepfake scams. The system is modular, so it can be improved and integrated with different payment platforms in the future.

**Sustainability**

Raksha402 fits the Sustainability track by reducing both the environmental and operational waste associated with digital payments. The platform uses Solana’s proof-of-stake infrastructure for fast and low-cost settlement, avoiding the energy-heavy mining process used by traditional proof-of-work blockchains.

It also supports financial sustainability by preventing fraud before a transaction is completed. Modules such as QRSeal, IntentLock, MuleGuard and KinProof help detect fake QR codes, altered payment details, suspicious recipient accounts and deepfake-based scams. This can reduce failed payments, disputes, manual investigations, repeated transactions and financial losses for both users and merchants.

By combining an energy-efficient blockchain with real-time fraud prevention, Raksha402 aims to create a payment system that is safer, more resource-efficient and sustainable for everyday digital transactions.

**Best Beginner's team**

We are a team of second-year college students, and Raksha402 is our first blockchain project. During the hackathon, we learned how to work with Solana, wallet-based payments, smart contracts, React, FastAPI, machine learning and computer vision, and connected them into one working prototype.

Despite being beginners, we built multiple fraud-prevention modules such as QRSeal, IntentLock, MuleGuard and KinProof to detect fake QR codes, payment mismatches, suspicious accounts and deepfake scams. Raksha402 reflects how quickly we were able to learn unfamiliar technologies and turn an ambitious idea into a practical payment-security system.

Team **MohinerCodersguli** -- [Arnab Chaudhuri](https://github.com/Arnab-dot), [Ankit Talukder](https://github.com/ankit2061)

`2026-07-26`

---

### OMNILEDGER
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/omniledger-6cc1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nurses-ste-walnut-msgstr.trycloudflare.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/41ykSSi4B0o) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Detective which you've hired for your finance

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![C](https://img.shields.io/badge/C-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![CYTHON](https://img.shields.io/badge/CYTHON-333333?style=flat-square)

**Challenges we ran into**

Solution

An AI-powered financial anomaly detection dashboard styled as the Marauder's Map. Users upload CSV transaction history. The system runs an Isolation Forest + rule-based hybrid anomaly detector, visualizes spending clusters on an interactive SVG map, narrates findings via Gemini, and reads them aloud via ElevenLabs. All data persists in Actian DB.

**The problem it solves**

Problem Statement

Financial fraud and wasteful spending cost individuals billions annually. Existing bank alerts are generic (fixed thresholds), late (post-facto SMS), and unintelligible (raw data, no narrative). For students and young professionals, small unnoticed leaks accumulate into serious losses.

**Accio Relevance - Build with Actian VectorAI Database**

Used Actian VectorAI DB to manage the database of the website. Community Edition

**Best Use of ElevenLabs**

Used and Implemented ElevenLabs for Voice TTL and Conversation.

**Best Use of Gemini API**

For Ai usage

**Best Use of ElevenLabs**

Relevant Track

**Best Beginner's team**

*Our project is related to finance part of everyone lifestyle         the most hectic part of the person life is to manage the bank account i.e, the money related part .

*Our project is removing your tension of fraud that can happen during your transition .

*Offline visting of bank is hectic and the online statements are generic and it only contain the nominal information .

*By adding your statement csv file you can gain all the information of your bank without visiting it , it also gives all the RED FLAGS that can be dangerous and suspicious out of it 

*It segregates all your monthly expenditures and give you idea about your monthly budget , which is the most important part of everyone life specially the students who has a tight budget
 
*We also provide the the voice assistant in our web ,for the people who are not familiar to tech, this way we are focusing in all generation needs.

* All your information are CONFIDENTIAL as we are using a local database ,we are not storing any of your information in server .

* In one sentence:
 { IT IS YOUR DETECTIVE WHICH YOU HAVE HIRED, FOR  YOUR FINANCIAL TASKS}

(This is our first offline project for a hackathon , this is the reason we have chosen this track)

THANK YOU !!

Team **RavenCode** -- [Shamina Kosar](https://github.com/SKosar-2007), [Saikat Kar](https://github.com/Skar-2007)

`2026-07-26`

---

### CashSense – AI Liquidity Copilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cashsense-ai-liquidity-copilot-706e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/keerthanmarnaddynun-commits/cashsense/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/QwFBfxTHBt0) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> From documents to cashflow decisions.

![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Team Name:

Spam Bytes

Team Members:

* Keerthan Marnad

* Ayush Tiwari

### 1. Problem Statement

Managing cash flow is one of the biggest challenges for small and medium businesses. Financial information is often scattered across PDF invoices, bank statements, and CSV transaction files, making it difficult for business owners to get a clear picture of their financial health.

Traditional accounting tools are mostly reactive—they show what happened in the past but do not provide proactive insights about future cash shortages, payment risks, or liquidity issues. Additionally, many SME owners are not finance experts, so complex accounting dashboards and spreadsheets become difficult to interpret and act upon.

### 2. Solution

CashSense is an AI-powered liquidity copilot that transforms unstructured financial documents into actionable cash flow intelligence.

Users can upload PDF statements or CSV transaction files through a modern web interface. The system automatically extracts financial data, calculates key metrics such as cash balance, receivables, expenses, and cash runway, and presents them in an intuitive fintech dashboard.

CashSense also provides proactive risk alerts, scenario analysis, and AI-generated recommendations that help founders make informed financial decisions before a cash deficit occurs.

### 3. Gemma Integration

Gemma is the core intelligence layer of CashSense.

When a user uploads a document, Python parsing libraries first extract the raw text. This unstructured text is then sent to gemini-flash-latest (powered by Google’s Gemma models) through a custom prompt engine.

Gemma performs:

* Structured data extraction from messy financial documents.

* Zero-shot JSON generation using strict response templates.

* Fallback validation for empty or non-financial documents.

* Context-aware financial advisory using persistent conversation history stored in the database.

By enforcing `response_mime_type='application/json'`, Gemma returns machine-readable financial fields that directly power the React dashboard and analytics components.

### 4. Technology Stack

| Layer            | Technology                              |
| ---------------- | --------------------------------------- |
| Frontend         | React, TypeScript, Tailwind CSS         |
| Backend          | FastAPI, Python                         |
| AI / LLM         | Gemini Flash (Gemma)                    |
| Database         | SQLite, SQLAlchemy                      |
| Document Parsing | Python PDF and CSV processing libraries |
| Authentication   | JWT-based authentication                |
| Deployment Ready | REST API architecture                   |

### 5. Key Features

* Upload and process PDF and CSV financial documents.

* Automatic extraction of cash, receivables, expenses, and invoice data.

* Cash runway gauge and forecast confidence indicators.

* AI-generated daily financial briefing.

* Priority action queue for collections and payment management.

* Interactive “what-if” scenario analysis.

* Stateful AI Copilot with persistent conversation memory.

* Multi-page SaaS-style dashboard with authentication.

* Flexible schema handling for different document formats.

### 6. Challenges

The main challenges we faced were:

* Handling inconsistent document formats across different banks and accounting systems.

* Converting unstructured text into reliable structured data without manual intervention.

* Designing a frontend that adapts dynamically to missing or additional financial fields.

* Maintaining conversational context across multiple AI interactions.

* Ensuring graceful fallbacks when uploaded documents contain little or no financial information.

### 7. Future Scope

We plan to extend CashSense into a production-ready financial intelligence platform by adding:

* Vector database RAG integration using ChromaDB or pgvector.

* Automated invoice follow-up email generation through the AI Copilot.

* Direct multi-bank API integrations for automatic transaction synchronization.

* Multi-year financial trend analysis and forecasting.

* Compliance and audit knowledge retrieval using domain-specific financial documents.

* Role-based collaboration features for finance teams and accountants.

**Challenges we ran into**

One major challenge was handling different PDF and CSV formats, since each document had inconsistent structures and field names. We solved this by building a normalization layer and using Gemma to convert unstructured financial data into a consistent JSON schema. Another hurdle was maintaining separate analyses for multiple businesses; we overcame it by implementing batch-based workspaces with persistent database storage and isolated AI conversation memory.

Team **Spam Bytes** -- Ayush Tiwari, keerthan marnad

`2026-07-18`

---

### THESEUS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/theseus-8c15) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MithilHM/theseus) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=-CN01ikCUCI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=-CN01ikCUCI) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> ODYSSEY for SMEs

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Managing cash flow and runway is the #1 reason small-to-medium enterprises (SMEs) fail. Traditional tools like Excel require manual data entry, offer static/unrealistic projection models, and lack automated foresight.

THESEUS acts as an SME Copilot that bridges the gap between raw ledger data and human intuition. It helps business owners by:

Providing Emotional Financial Legibility: Translating complex balance sheets and forecasts into an animated Greek Galley Ship on the water. Instead of confusing numbers, owners see immediate threats: Icebergs represent major unpaid invoices or upcoming debt, Storm Clouds signal high cash flow volatility, and Water Levels show current runway.
Rigorous "What-If" Simulations: Business owners can simulate scenarios like "What if we hire 2 new developers?" or "What if a customer delays invoice payments?". THESEUS runs 10,000 Monte Carlo simulation paths using historical volatility data to predict the best (P90), expected (P50), and worst-case (P10) cash balances over 90 days.
Document-Aware Financial Intelligence: Users can drag and drop bank statements, invoices, and PDFs. Using a vector search engine (RAG), the embedded Gemma AI answers natural language queries about company documents, linking direct citations to the source files.

**Challenges we ran into**

Challenges We Ran Into
During development, we faced several technical and architectural hurdles:

The API Timeout / Freezing Problem:

Hurdle: When testing the Scenario Simulator tab, we noticed the UI would occasionally hang indefinitely on the loading spinner ("Gemma is drafting future branches..."). We discovered that during periods of high API latency or rate-limiting (429 errors), the backend python library was blocking indefinitely on HTTP calls without a timeout.
Solution: We refactored gemma_client.py to use strict timeout limits (timeout=8) and added structured fallback logic in scenario_simulator.py. If the AI API takes more than 8 seconds, the engine automatically catches the error and generates the flowchart directly using the mathematical Monte Carlo values (P10/P50/P90), guaranteeing a flawless, freeze-free UI experience.
Vector DB Ingestion Rollovers:

Hurdle: During batch processing of large financial documents, database transactions would occasionally fail, causing SQLAlchemy to block subsequent queries with the error: "Can't reconnect until invalid transaction is rolled back".
Solution: We added robust transaction error catching inside embeddings.py which explicitly issues a db.rollback() on individual chunk insertion failures. This isolated the failure to a single bad text chunk while keeping the main ingestion worker active and healthy.
Hydration Mismatches in Dev Environment:

Hurdle: Next.js threw hydration mismatch warnings due to animated vector paths dynamically rendering based on client-side values (like Math.random() or instant window sizes) which differed from the server's pre-rendered HTML.
Solution: We structured the layout states to hydrate using clean client-only wrappers and stashed state bindings so animations run smoothly without breaking React's hydration tree.

**Overall Winner**

THESEUS stands out because it combines rigorous data science with uncompromising user experience:

It makes math legible: Rather than showing raw, dry tables, it turns math (Monte Carlo simulations, volatility metrics, accounts receivable aging) into a highly engaging, interactive digital environment (the Greek Galley Ship navigation).
Guaranteed Reliability: Most AI-powered dashboards crash when API keys are missing or limits are hit. THESEUS was designed with a mathematics-first fallback architecture. Even with zero API connectivity, the simulation trees, KPIs, and forecasts render perfectly using local mathematical execution.
Zero Cognitive Overhead: We removed all the clutter (including sidebars and navigation panels) to build a focused workspace where the business owner sees exactly what matters: cash, runway, simulations, and interactive chat.

Team **whatdoyoumean** -- [Mithil H M](https://github.com/MithilHM), [Navaneethan R](https://github.com/ProNeethanR), [Srishankar PR](https://github.com/srishankar-pr)

`2026-07-18`

---

### Saakh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saakh-42c7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tanmaykatiyar0207-cell/Saakh) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> Simplifying SME Finance with AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Saakh helps small businesses and shopkeepers manage their daily finances effortlessly through WhatsApp. Many SMEs still maintain handwritten ledgers or manually record transactions, which often leads to errors, lost records, delayed bookkeeping, and poor visibility into cash flow.

With Saakh, users can simply send a WhatsApp message like "Paid ₹500 to Ravi" or "Received ₹2,000 from Ankit", and the AI automatically understands the transaction, categorizes it, and updates the digital ledger in real time. It also supports scanning handwritten ledger pages, reducing the need for manual data entry.

By digitizing bookkeeping through a familiar platform, Saakh makes accounting faster, more accurate, and accessible for business owners who may not be comfortable using complex accounting software. The platform also provides dashboards, cash flow insights, customer balances, and AI-powered business assistance, enabling SMEs to make better financial decisions without hiring an accountant.

Key benefits:

📱 Record transactions directly through WhatsApp.
📸 Digitize handwritten ledgers using AI.
🤖 Automatically categorize income and expenses.
📊 Track cash flow, profits, and customer dues in real time.
💡 Get AI-powered business insights and recommendations.
⏱️ Save time, reduce bookkeeping errors, and improve financial transparency.

**Challenges we ran into**

Challenges We Ran Into

Building Saakh involved several technical and deployment challenges:

WhatsApp Webhook Integration: Setting up Twilio's WhatsApp Sandbox and correctly configuring webhook URLs was initially difficult. We used ngrok for local testing, verified request payloads, and iteratively debugged the webhook flow until messages were processed reliably.
Backend & Database Issues: While integrating FastAPI with SQLAlchemy, we encountered issues such as missing database tables, import conflicts, and primary key constraint errors. We resolved these by restructuring the project into proper Python packages, fixing model imports, and redesigning the database schema.
AI Transaction Parsing: Converting natural language messages like "Paid ₹500 to Ravi" into structured ledger entries required careful parsing and validation. We built a parser that extracts transaction type, amount, and customer information while handling different message formats.
Deployment Challenges: Deploying the application required resolving dependency management issues, package import paths, environment variable configuration, and secure secret management. GitHub Push Protection also blocked commits containing API credentials, reminding us to adopt proper security practices using .gitignore and environment variables.

These challenges helped us improve the project's architecture, strengthen its security, and build a more reliable, production-ready solution.

Team **Prisoners Of Azkaban** -- [Sumanth Halyal](https://github.com/Aqua32A7), [Samyak Shankar](https://github.com/SamyakShankar), Tanmay Katiyar

`2026-07-18`

---

### SME Advisor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sme-advisor-594d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sai-Emani25/SME-Hub-Mobile-) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> Making money made easy for small businesses

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square)

**Challenges we ran into**

What was the hardest part of building this in one day?
The most significant challenge was navigating the complex authentication and configuration requirements within a limited timeframe. Specifically:

**The problem it solves**

💡 Inspiration
What local problem are you solving today?
SMEs in our local ecosystem often operate in fragmented silos. They struggle with digitizing their day-to-day operations, resulting in scattered inventory and sales data. This prevents business owners from making data-driven decisions. SME-Advisor solves this by providing a unified, AI-powered command center that centralizes business metrics and offers real-time, context-aware advisory services to help owners optimize growth and inventory efficiency.

🛠️ How we built it
Which Gemma model did you use? Did you use RAG, prompt engineering, or fine-tuning? What frameworks (Transformers, Keras, etc.) did you use?
We utilized the Gemini/Gemma API to power the intelligence engine. Our implementation relies on Prompt Engineering to translate raw Firestore data (inventory and sales trends) into actionable business insights.

Frameworks: We used Compose Multiplatform (Kotlin) to ensure a seamless cross-platform experience across Android and Web.

Backend: The project integrates Firebase (Firestore for database, Authentication for security).

Logic: The advisory engine dynamically retrieves data from Firestore and passes it through a structured system prompt, simulating a RAG-like approach by grounding the model's insights specifically in the user's real-time business data

Authentication Bottlenecks: Implementing the Android Credential Manager API led to a "No credentials available" error. We had to troubleshoot SHA-1 fingerprint mismatches in the Firebase Console and ensure the WEB_CLIENT_ID was correctly configured.

Environment Configuration: Aligning the applicationId in our build settings with the registered Firebase package name required rigorous debugging to ensure proper initialization.

Time Constraints: Balancing the development of the cross-platform UI with the backend logic integration in a single day required rapid prototyping and strict adherence to modular development practices.

Team **Krsna** -- [Sai Emani](https://github.com/Sai-Emani25), [Kathi Harshith Reddy](https://github.com/kathiHarshithReddy)

`2026-07-18`

---

### Ledge AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ledge-ai-9bff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shroff45/zeroping.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/56gw5zcklMw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/56gw5zcklMw) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> Ledging the AI process!!

![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![PyPDF2](https://img.shields.io/badge/PyPDF2-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

THE PROBLEM

Priya runs a 6-person interior design studio in Bengaluru.
She has ₹67,000 in the bank, ₹2,33,000 owed to her, and
salaries due in 14 days. She has no idea she is about to
miss payroll. This is not exceptional — 84% of India's
63 million MSMEs borrow from informal lenders at predatory
rates because banks require collateral and audited books
they do not have. The ₹20–30 lakh crore MSME credit gap
exists because there is no verified, real-time picture
of their financial health.

WHAT WE BUILT

LedgeAI is a fully offline, on-device AI financial copilot
that runs entirely on a laptop with no internet connection
after setup. Four deterministic financial engines analyse
the business. Gemma 4 (E4B QAT, via Ollama) explains the
findings in plain English and drafts collection emails.
A bankability report maps the business to Mudra and CGTMSE
loan schemes. Nothing ever leaves the device.

HOW IT WORKS — END TO END

Data enters via a seed script (demo), CSV import, or our
fully offline local PDF parser for bank statements and
invoices (built using pypdf — no cloud OCR, no Vision APIs,
no external transmission of sensitive financial data).
Bank statements and invoices are parsed locally on the
device, structured into ledger entries, and written
directly into SQLite. One database read then builds a
frozen CompanySnapshot. Six pure functions run in strict
order:

1. Anomaly Detection — Student t-score per client
   (t = (days_since − μ) / (σ/√n), dynamic threshold
   from t.ppf(0.95, df=n−1)) flags invoices with
   statistically abnormal payment delays.

2. Liquidity Scoring — Weighted composite of runway,
   quick ratio, DSO, and receivables quality. All
   arithmetic in Python Decimal (28-precision) — no
   IEEE 754 rounding errors on rupee amounts.

3. Cash Flow Projection — 90-day daily ledger simulation
   with a statistically correct t-based prediction
   interval: PI(h) = ŷ(h) ± t(0.95,n−2)·s·√(1+1/n+
   (h−h̄)²/Sxx). The band widens honestly with horizon.
   No fudge factors.

4. Payment Optimizer — True Mixed-Integer Linear Program
   via scipy.optimize.milp (HiGHS solver). Objective:
   maximize Σ(discount_i·amount_i·x_i), x_i∈{0,1},
   subject to liquidity floor and hard deadline constraints.
   Not a sort. A formal mathematical optimum.

5. GST Calendar — CBIC GSTR-3B deadlines with urgency
   classification (OVERDUE / URGENT / UPCOMING / FUTURE).

6. Bankability Report — DSO, DPO, Cash Conversion Cycle
   (CCC = DSO − DPO) mapped to Mudra Shishu / Kishore /
   Tarun / Tarun Plus and CGTMSE eligibility thresholds.

GEMMA AS AN AGENT (MCP ARCHITECTURE)

Gemma 4 is not a chatbot wrapper. It is an autonomous
agent that calls our verified financial engines as tools
via Model Context Protocol. When a user asks "Which
clients put my payroll at risk?", Gemma decides to call
get_anomalous_invoices() and get_cashflow_projection()
sequentially, receives structured engine results, and
synthesizes a grounded final response.

The grounding firewall — our core differentiator — validates
every number in Gemma's output against the engine allowlist
before it reaches the screen. Monetary values: ±₹1 absolute
tolerance. Ratios and scores: 1% relative tolerance. If
Gemma invents a number, the entire response is rejected and
a verified fallback is shown. This is enforced by mechanism,
not by prompt wording.

THE DIFFERENTIATORS

• Offline PDF parsing: Bank statements and invoices are
  parsed locally using pypdf — no cloud OCR, no Vision
  APIs, no external transmission of sensitive financial
  data. Privacy guaranteed at the ingestion layer.

• Offline-first: Gemma 4 E4B QAT (~5GB) runs on
  127.0.0.1:11434. Airplane mode from second 15 of the
  demo. No financial data ever leaves the device.

• Deterministic engines: Same input always produces the
  same output. DEMO_DATE anchor, no datetime.now(), no
  randomness. Structurally impossible to hallucinate a
  financial metric.

• True MILP optimizer: scipy.optimize.milp with HiGHS —
  not a heuristic sort. Formally optimal payment schedule.

• Statistically honest forecasting: t-distribution
  prediction intervals, not fabricated confidence bands.
  Six months of data does not buy a clean line at Day 90.
  We show the honest range.

• Grounding firewall: A 40-line mechanism that makes
  hallucination structurally impossible for numeric
  outputs. Bifurcated tolerance — ±₹1 absolute for money,
  1% relative for ratios. Enforced by code, not promises.

• MCP agentic orchestration: Gemma autonomously selects
  and calls financial engine tools. It reasons across
  multiple tool results before synthesizing a response.
  Tool call trace is visible in the UI.

• India-native: ₹ Indian number grouping (1,85,000),
  GST calendar, Mudra / CGTMSE bankability tiers,
  Peenya-style MSME persona baked into every prompt.

THE BUSINESS MODEL

LedgeAI acts as a Loan Service Provider (LSP) under the
Open Credit Enablement Network (OCEN) framework. The
ambient operational data captured

**Challenges we ran into**

Building an offline-first, mathematically deterministic financial AI turned out to be significantly harder than plugging into a cloud API. Below are the four hardest problems we solved.

### 1. The IEEE 754 Floating-Point Trap
Our first working prototype used Python `float` for all monetary calculations. This silently broke our grounding firewall: engine outputs and LLM-narrated values would diverge by fractions of a rupee due to binary representation errors (`0.1 + 0.2 = 0.30000000000000004`). Aggregated across GST calculations, partial payments, and running cash balances, the drift became large enough to either falsely reject correct LLM outputs or pass incorrect ones.

**Fix:** We migrated all monetary arithmetic to Python's `Decimal` module with 28-digit precision (mirroring IBM's decNumber standard used in mainframe banking). Engines now cast inputs to `Decimal` on entry, compute exactly, and cast back to `float` only at the schema boundary for JSON serialization.

### 2. Ollama Tool-Calling Format Detection
We built the MCP agentic layer expecting Ollama's native `tool_calls` format to work universally. It doesn't — support varies by model version and Ollama build. On one team member's machine Gemma returned tool calls perfectly; on another it returned free-text explanations of what tool it *would* call.

**Fix:** We built a runtime detection mechanism (`_detect_tool_support()`) that sends a minimal test tool call at startup. If native tool-calling fails, we automatically fall back to a JSON-in-prompt pattern where Gemma returns `{"tool": "...", "params": {...}}` as raw text, which our executor parses manually. Both paths produce identical results from the user's perspective.

### 3. Statistically Honest Prediction Bands on 6 Data Points
Our first cash-flow projection multiplied the standard error by a hand-tuned `(day_idx / 30.0 + 1)` scaling factor to make the uncertainty band "look right." This was intellectually dishonest — any statistician judge would catch it in seconds. But the real formula requires converting monthly regression variance to daily balance-scale uncertainty, and the units kept fighting us.

**Fix:** We rederived the interval from first principles using the standard t-based prediction formula `PI(h) = ŷ(h) ± t·s·√(1 + 1/n + (h−h̄)²/Sxx)`, then explicitly documented the monthly→daily unit conversion. The band now widens mathematically with horizon — no fudge factors — and we can defend every term from first principles.

### 4. The Grounding Firewall Tolerance Bug
Initial firewall used a single 2% relative tolerance for everything. This meant a ₹1,85,000 invoice had a tolerance window of ±₹3,700 — enough for Gemma to invent thousands of rupees while still passing validation. On the other extreme, a 1% tolerance on a t-score of 2.87 was too tight and rejected valid outputs due to display rounding.

**Fix:** We bifurcated the tolerance logic. Monetary values above ₹100 use an absolute tolerance of ±₹1.00 (invented rupees are structurally impossible). Ratios, scores, and days use a 1% relative tolerance (accommodates display rounding). Two lines of code, but this is the mechanism that makes our "no hallucination" claim provable rather than promissory.

### Honorable Mentions
- **SQLAlchemy 2.0** requires `sa.text()` wrappers for raw SQL — we hit `ObjectNotExecutableError` on our first pipeline run and had to refactor every query.
- **Streamlit session state** with more than 3 keys caused race conditions on rapid clicks — we consolidated to `result`, `narratives`, `running` and embedded the snapshot into `AnalysisResult`.
- **Ollama cold-start latency** on first call could exceed 45 seconds. We solved this by pre-warming an LLM cache keyed on `sha256(snapshot_json)` so demo runs are instant even in airplane mode.

Team **ZeroPing** -- Rishil N, SaiSwarup Shroff, Rithvik N, Pranav Kulkarni

`2026-07-18`

---

### CashPilot AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cashpilot-ai-aipowered-cfo-copilot-for-smes-6312) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harshad-08/CashPilot-AI-An-AI-Powered-CFO-Copilot-for-SMEs-) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> AI-Powered CFO Copilot for SMEs

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Small and Medium Enterprises (SMEs) often rely on accounting software that records past transactions but provides little support for future financial decision-making. Business owners struggle to forecast cash flow, identify liquidity risks, prioritize invoice payments, and evaluate business decisions without financial expertise.

CashPilot AI solves this by acting as an AI-powered CFO Copilot. Users upload financial documents such as bank statements, invoices, and expense reports, and the system analyzes them to generate cash flow forecasts, detect financial risks, provide AI-powered recommendations, and simulate business decisions using Google Gemma. This enables SMEs to make smarter, data-driven financial decisions without requiring an expensive financial advisor.

**Challenges we ran into**

Building an AI-powered financial assistant within a limited hackathon timeline was our biggest challenge. We had to design a scalable backend, process multiple financial document formats, extract structured data accurately, and separate deterministic financial calculations from AI reasoning. Integrating Google Gemma effectively for explainable financial insights and decision simulations while maintaining accurate outputs also required careful prompt engineering and workflow design.

Team **Matrix Minds** -- Pruthvi R, [Harshad Magdum](https://github.com/Harshad-08), Sushant Kulkarni

`2026-07-18`

---

### FORGE-PATH
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/forgepath-f721) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/callmetechnophile/finance-tech) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1ZULgy9Z1jg-Q-d8LV3QjYRC8M-VEURRf?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Build%20with%20Gemma-0052CC?style=flat-square)](https://build-with-gemma-bengaluru-ai-sprint.devfolio.co)

> Next-Generation AI Financial Operating System

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square)

**Challenges we ran into**

The ultimate constraint was enforcing absolute mathematical accuracy within a generative AI framework under a 24-hour deadline. Large Language Models are notoriously prone to financial hallucination and formatting slips. Building an AI Gateway featuring an isolated Response Validator that intercepts Gemma’s output, checks it against our strict Pydantic JSON schemas, rejects unauthorized numbers, and handles immediate retry/fallback orchestration was a massive engineering hurdle to clear in a single day—but it is exactly what prevents the system from fabricating a company's balance sheet.

**The problem it solves**

FORGE-PATH acts as an AI-powered Enterprise Financial Command Center. It eliminates cognitive overload for business owners by unifying deterministic financial calculations (for forecasting, liquidity, and treasury scores) with a conversational AI reasoning layer (Gemma 4). This gives executives an immediate, high-fidelity view of their financial health, automates daily execution strategies, and highlights critical risks without relying on manual spreadsheet tracking.

Team **INSOMNIGENTS** -- [Ayushman Patro](https://github.com/callmetechnophile), [Shriram Upadhya](https://github.com/Monkshred006)

`2026-07-18`

---

### piggy-ledger-OS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/piggyledgeros-4492) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/snigdha-777/piggy-finance-bro) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://piggy-finance-bro-fmwc.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=JW3Y1g0dCu4) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Your personal finance-bro

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was integrating our AI features with Firebase Cloud Functions. We ran into issues such as CORS errors, emulator port conflicts, runtime configuration problems, and API key environment variables not loading correctly. These issues prevented our frontend from communicating with the AI backend.

We overcame this by systematically debugging each layer, reconfiguring Firebase settings, fixing function deployment issues, and implementing fallback responses to ensure a smooth user experience. This process taught us the importance of robust backend integration and graceful error handling when building AI-powered applications.

**The problem it solves**

Problem: We wanted to add immersive audio feedback for user interactions (clicks, creating goals, feeding the piggy), but native HTML audio elements can be clunky when managed individually across multiple components.

Solution:

We created a centralized custom hook, useSound.js, which instantiates the Audio object once upon application startup.

To avoid "prop-drilling" (passing the sound function through dozens of layers), we implemented a Higher-Order Function wrapper (withSound) in the main App.jsx.

This wrapper allows us to trigger the sound effect automatically whenever any onClick event is fired, keeping our component logic clean and DRY (Don't Repeat Yourself).

Team **naan-chalant** -- Ananya K, Samarth Reddy, Snigdha V

`2026-06-14`

---

### NeuroShield Lite — AI Predictive Fraud Prevention
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/euroshield-lite-ai-predictive-fraud-prevention-system-e436) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://neurosheild-lite-ai.lovable.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> AI Predictive Fraud Prevention System

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Python Fastapi](https://img.shields.io/badge/Python%20Fastapi-333333?style=flat-square) ![JWT Authentication](https://img.shields.io/badge/JWT%20Authentication-333333?style=flat-square) ![Recharts](https://img.shields.io/badge/Recharts-333333?style=flat-square) ![Responsive UI design](https://img.shields.io/badge/Responsive%20UI%20design-333333?style=flat-square)

**The problem it solves**

Financial fraud is increasing rapidly, and most systems react after damage is done. Users and companies lack real-time tools to predict and prevent suspicious transactions before they happen.

NeuroShield Lite solves this by providing:

⚡ Real-time fraud risk prediction
🧠 AI-based behavioral analysis (spending, location, time)
🚨 Instant alerts for high-risk transactions
📊 Clear visual insights for decision-making
💡 Use Cases
Individuals monitoring unusual transactions
Fintech apps integrating fraud detection
Companies tracking employee/payment risks
Demo system for AI-based security solutions

👉 It makes financial systems safer, smarter, and proactive instead of reactive

**Challenges we ran into**

1. 🔄 Real-time UI + Backend Sync

Keeping the UI instantly updated after simulation while calling APIs was tricky.
✅ Solved by managing state properly in React and triggering re-renders after API responses.

2. 🧠 Designing Fraud Logic

Balancing realistic fraud rules without overcomplicating logic was challenging.
✅ Implemented a simple but effective rule-based system:

High amount → High risk
New location → Medium risk
Outside active hours → Medium risk
3. 🎨 Premium UI Design

Creating a fintech-level dark UI that feels like a real product took effort.
✅ Used Tailwind CSS with gradients, shadows, and consistent spacing.

4. 🔐 Authentication Integration

Integrating login + protecting routes without breaking the app flow.
✅ Solved using JWT and route guards in React.

**Using LocusFounder to Build a Business!**

💰 FinTech
🤖 Artificial Intelligence / Machine Learning
🛡️ Cybersecurity
🌐 Web Development

Team **Eagle** -- Jaideep Kalla, Lohith Mutyala

`2026-05-06`

---

### Prana Mesh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/prana-mesh-adc8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sreek001/PRANA-MESH-Digital-Flare-System) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://pranamesh.streamlit.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/qWClLjFOChA) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> The signal that survives when everything else die

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Android Jetpack](https://img.shields.io/badge/Android%20Jetpack-333333?style=flat-square) ![GIS (Geographic Information Systems)](https://img.shields.io/badge/GIS%20(Geographic%20Information%20Systems)-333333?style=flat-square)

**The problem it solves**

1. The "Last-Mile" Rescue GapIn major disasters like earthquakes or floods, the biggest challenge isn't the lack of rescuers; it's knowing where to look.The Problem: Traditional GPS sharing requires an internet connection (4G/5G/Wi-Fi). Once the phone hits 0% or the towers fail, that data is gone.The Prana-Mesh Solution: It utilizes low-level hardware pulses that require virtually zero energy. It effectively bridges the gap between a victim being "lost" and being "mapped," even if the victim is unconscious or unable to call for help.2. Hyper-Efficient Resource AllocationSearch and Rescue (SAR) operations are often hampered by "stale" data—rescuers waste hours checking locations where victims were spotted three days ago.Making it Safer: By implementing the Signal Age Filter, the system automatically categorizes signals.Hot Signals (Red): Real-time pulses from active devices.Cold Signals (Grey): Last known locations from devices that have since died or moved.The Result: Rescuers can prioritize the "Hot" markers, drastically increasing the chances of finding survivors within the "Golden Hour."3. Use-Case ScenariosPeople can use Prana-Mesh in several high-stakes environments:ScenarioExisting TaskPrana-Mesh ImprovementEarthquakesSearching rubble blindly.Scanning for BLE pulses through concrete to pinpoint victims.Wilderness SurvivalUsing flares or mirrors.Automatically broadcasting coordinates when the phone battery is critical.FloodsWaving from rooftops.Creating a "Mesh" of signals that rescuers can see on a boat-mounted dashboard.Mass BlackoutsTotal loss of contact.Maintaining a local-only "Sentinel" network to track family members.4. Hardware DemocratizationUnlike expensive satellite phones (Garmin InReach/Starlink), Prana-Mesh uses existing hardware.Accessibility: It turns every cheap Android smartphone already in a survivor's pocket into an emergency transponder.Scalability: Because the "Sentinel" receiver can be a simple web dashboard on a laptop with a Bluetooth dongle, local community leaders can set up "Safety Hubs" in minutes without needing government-level infrastructure.

**Challenges we ran into**

1. The "Deep Sleep" Execution BarrierThe Hurdle: Android’s Doze Mode and App Standby are designed to kill background processes to save battery—the exact opposite of what a distress beacon needs. When the battery hit 2%, the OS would often kill the BLE advertiser to squeeze out ten more minutes of idle time.The Fix: I had to implement a Foreground Service with a high-priority notification. By using startForeground(), I effectively told the OS: "This task is more important than your power-saving rules." I also added the REQUEST_IGNORE_BATTERY_OPTIMIZATIONS permission to ensure the "Ghost" pulse wasn't deferred by the system's job scheduler.2. The 24-Byte Payload ConstraintThe Hurdle: Standard BLE advertising packets are tiny. After headers, you only have about 24–31 bytes of "Manufacturer Specific Data." Trying to fit a Device ID, Latitude, Longitude, Status, and a Security Nonce into that space is like trying to write a novel on a postage stamp.The Fix: I abandoned standard Double formats for GPS. Instead of 8-byte floats, I used Fixed-Point Arithmetic:I multiplied coordinates by $10^6$ and stored them as 4-byte Signed Integers.This saved 8 bytes immediately while maintaining precision down to ~11 centimeters—plenty for a rescue team.3. MySQL Spatial "Ghosting"The Hurdle: During testing, the web dashboard would sometimes show survivors in the middle of the ocean. This happened because the MySQL POINT data was being interpreted in (Long, Lat) order by the database but (Lat, Long) by the Leaflet.js frontend.The Fix: I standardized the backend to SRID 4326 (the global GPS standard) and wrote a custom utility function in the FastAPI layer to flip the coordinates during the GeoJSON serialization. I also implemented a Spatial Index to ensure that when a "Sentinel" scans a 5km radius, the database doesn't have to scan every single row in the table, preventing a backend crash during high-load disasters.

Team **nfinits** -- Chrison Roy, Anannya Sunny, Astrea Rose, [Sreehari K](https://github.com/sreek001)

`2026-05-12`

---

### phishing detector
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/phishing-detector-b287) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://phishguard-ai-eiq8.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Detect Threats Before They Detect You.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Every day, people receive fake emails, scam messages, and suspicious links pretending to be from banks, social media apps, or trusted websites. Many users click these links without realizing they are phishing attacks, which can lead to stolen accounts, personal data leaks, and financial loss.

PhishGuard AI was created to help users easily identify suspicious messages before they become victims. The system analyzes messages, detects warning signs, and gives a risk score to help people stay safer online.

**Challenges we ran into**

One of the biggest challenges while building this project was connecting the AI model with the Flask application. I faced several errors related to unsupported Gemini models and Python version compatibility, which stopped the phishing analysis from working properly.

I also ran into deployment issues while hosting the project online. The build kept failing because some required files were missing or not configured correctly.

To solve these problems, I carefully checked the error messages, fixed the folder structure, added the missing files, and tested the project step by step. In the end, I switched to a simpler and more stable rule-based phishing detection system, which helped the application work smoothly and deploy successfully.

[Sree durga](https://github.com/httpssree1888)

`2026-05-15`

---

### finder
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finder-4707) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cheerful-gaufre-1bdd5a.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> find your best deal

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

People waste time searching across multiple sites (like Amazon and Flipkart) to find the best price and genuine reviews.

**Challenges we ran into**

Getting real-time price data (APIs are limited)
Handling fake or biased reviews
Affiliate approval and commissions
Competing with big players
Keeping data updated

[Rose Seby](https://github.com/rosesebyk)

`2026-05-15`

---

### hening
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hening-97f6) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Your business runs while you rest.

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Locus beta](https://img.shields.io/badge/Locus%20beta-333333?style=flat-square)

**The problem it solves**

launching a digital product business is slow and fragmented — you need to research a niche, create a product, set up a storefront, integrate payments, handle fulfillment, and continuously optimize pricing. That's days of work across multiple tools, and most people never get past the setup phase.

**Hening collapses that entire process into a single prompt.**

Give it a niche (e.g. *"productivity tools for remote teams"*) and three specialized agents take over:

- **Scout Agent** — monitors trends, scores niche viability via LLM, and decides whether to launch a campaign
- **Builder Agent** — generates a digital storefront with a real product (ebook, toolkit, or template), sets a USDC price, creates a Locus Checkout session, handles fulfillment on payment, and auto-optimizes the headline and price after every sale
- **Treasurer Agent** — enforces financial controls before every transaction: per-tx limits, daily allowance caps, approval thresholds, and full intent logging so every financial decision is auditable

What makes it safer than typical autonomous agents is the **financial guardrails** — the agent can't spend freely. Every payout is checked against configurable limits before it executes, and every decision is logged with reasoning.

**Use cases:**
- Founders who want to validate a niche without building anything manually
- Developers exploring autonomous agent + crypto payment pipelines
- Anyone who wants a self-running passive income experiment with real USDC on Base

**Challenges we ran into**

**1. LLM responses returning unpredictable JSON shapes**

Even with structured output mode enabled, the model would return the same data under different keys depending on the run. Had to write a defensive parser that checks multiple possible keys and falls back gracefully, plus a strict validator that rejects malformed responses before they touch storage.

**2. Keeping the agent's private key secure across restarts**

Locus registration returns a private key needed for payouts. Writing it to disk is a security risk, but losing it on restart breaks everything. Solution: persist only the non-sensitive credentials to disk, keep the private key in memory only. On restart, the agent re-registers automatically.

**3. Webhook arriving before the order record is written**

There's a race window between creating the checkout session and the webhook firing on payment. If the webhook arrives too early, the order lookup fails. Handled it by returning a 404 so Locus retries delivery — took a few test runs to confirm retries were actually happening rather than events being silently dropped.

**4. Optimizer crashing the webhook handler when OpenAI key is missing**

The headline rewrite step calls OpenAI. Without a valid key it throws, which would crash the entire webhook handler mid-fulfillment. Wrapped it in a try/catch with a static fallback so the optimizer always completes regardless of whether the LLM call succeeds.

**5. Making the agent pipeline non-blocking**

The agent trigger endpoint needs to return immediately while the campaign runs in the background. Awaiting the full pipeline directly would time out on serverless. Solution: fire-and-forget execution, write all progress to a local JSON store via activity logs, and let the dashboard poll for updates.

**Using LocusFounder to Build a Business!**

Hening is a direct implementation of the LocusFounder track premise — an autonomous agent that uses Locus as its financial and AI backbone to run a real digital product business end-to-end.

Here's how every core Locus primitive maps to a business function:

**Agent Registration → Business Identity**
The agent self-registers with Locus on first run, getting its own API key and wallet. It doesn't need a human to set up accounts — it bootstraps itself as an independent business entity.

**Wrapped OpenAI → Product Creation**
Instead of calling OpenAI directly, the agent routes all LLM calls through Locus's wrapped API. This is how it generates store ideas, product names, descriptions, and pricing from a single niche prompt.

**Checkout Sessions → Revenue**
Every store the agent creates gets a real Locus Checkout session. Buyers pay in USDC on Base — not simulated, not mocked. The agent is running an actual payment-enabled storefront.

**Webhook + Payout → Fulfillment and Revenue Routing**
When a payment lands, Locus fires a webhook. The agent fulfills the order, then immediately calls the Locus payout API to route the USDC to the owner wallet — with a balance check before every transfer as a spending control.

**Spending Controls → Safe Autonomous Finance**
This is the part that goes beyond a basic integration. The agent enforces per-transaction limits, daily allowance caps, and logs the reasoning behind every financial decision. It's designed to operate autonomously without spending freely or unpredictably.

The result is a full business loop — niche in, revenue out — built entirely on Locus primitives, with no human required at any step.

[amisha amisha](https://github.com/lazybit)

`2026-05-17`

---

### personal safety app
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/personal-safety-app-97b2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/krdric/Personal-Safety-Application) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Your Safety, Always in Your Hands

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![XML](https://img.shields.io/badge/XML-333333?style=flat-square)

**The problem it solves**

This app helps people stay safe in emergency situations. If someone feels unsafe or needs help, they can quickly send an SOS alert and share their live location with trusted contacts. It is useful while traveling alone, going out at night, or being in an unfamiliar place. The app makes it easier and faster to contact someone during danger and improves personal safety.

**Challenges we ran into**

One of the biggest challenges while building this project was managing real-time location sharing and sending alerts instantly without delays. Sometimes the location was not updating properly because of internet and permission issues. We solved this by improving location permissions, optimizing the API calls, and testing the app on different devices. Another challenge was designing a simple and user-friendly interface, which we improved after multiple testing and feedback sessions.

[Rishi Kardam](https://github.com/Krdric)

`2026-05-18`

---

### PayFounder AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/payfounder-ai-7e2e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/xxxxxxxxxx) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> "AI Agent that runs your entire business payments"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Small business owners and freelancers waste hours manually handling payments, tracking invoices, sending reminders, and reconciling accounts. 

PayFounder AI solves this by acting as an intelligent AI agent that automates the entire payment workflow - from invoice creation to payment reminders and reconciliation - making business payments faster, safer, and hassle-free.

**Challenges we ran into**

Main challenge was creating a realistic and engaging demo video within limited time. 
I overcame this by using CapCut for fast editing, stock footage, smooth animations, and proper voiceover to showcase the AI agent working in real scenarios.

**Using LocusFounder to Build a Business!**

AI Agent Track, Founder Track, FinTech

AMAN KUMAR

`2026-05-20`

---

### Anastik Manufacturing Pvt ltd
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anastik-manufacturing-pvt-ltd-d81c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shivam-chaudhry-project.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> anastik manufacturing pvt ltd.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

This is an e-commerce website for manufacturing disposables, plates, and glasses. It has separate employee logins and separate customer logins. All details for both are stored in MongoDB. This is a fully functional project and is very useful.

**Challenges we ran into**

I had a lot of trouble building this project. Initially, it wouldn't connect to the database. I then read its in-depth explanation and found many errors, which I fixed with time.

Govind Kumar Mishra

`2026-05-21`

---

### AI coading assistant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-coading-assistant-f194) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Apurvatajaiswal/AI-Coding-Assistant.git) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> The coding assistant that teaches while it helps

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tesseract OCR](https://img.shields.io/badge/Tesseract%20OCR-333333?style=flat-square)

**The problem it solves**

Problem Statement

Many developers, especially beginners, face difficulties in:
Writing efficient code
Debugging errors quickly
Understanding code from images/screenshots
Switching between multiple tools for coding help
This leads to reduced productivity and slower learning.

Our solution addresses these challenges by providing an all-in-one AI-powered coding assistant that simplifies code generation, debugging, and understanding, making the development process faster, more efficient, and accessible.

Improved coding efficiency by 35–40%
Reduced debugging time significantly
Helps beginners learn faster and professionals code smarter

**Challenges we ran into**

During the development of the AI Coding Assistant, we faced several technical and integration challenges. Integrating the OpenAI API for accurate and context-aware code generation required careful prompt design and optimization. Implementing real-time debugging was challenging as it involved identifying errors across different programming languages.

Additionally, integrating Tesseract OCR for extracting code from images required preprocessing techniques to improve accuracy. Managing seamless communication between the React frontend and FastAPI backend also posed challenges in handling asynchronous requests and ensuring low response time.

We overcame these challenges through iterative testing, optimizing API calls, and improving system design for better performance and scalability.

**Using LocusFounder to Build a Business!**

1. Artificial Intelligence / Machine Learning (BEST)

This is your primary track
Why:
Uses OpenAI API
Smart code generation
AI-based debugging
What to select:
AI / Machine Learning

2. Developer Tools / Productivity
VERY strong secondary track
Why:
Helps developers write code faster
Improves productivity
Select this if available:
Developer Tools or Productivity Tools

3. EdTech (Education Technology)
Good backup option
Why:
Helps students learn coding
Beginner-friendly tool
Select:
EdTech

Apoorvata Jaisawal

`2026-05-21`

---

### SHAURYA FinTech
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shaurya-fintech-165c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SGSShaurya5497/FinTech-Project-SHAURYA-) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fintechshaurya.vercel.app/#/home) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> AI-powered financial intelligence for every Indian

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

190 million Indians are financially underserved — not because they lack 
money activity, but because traditional credit systems ignore their UPI 
transactions, digital assets, and behavioral data.

SHAURYA fixes this.

By leveraging the Account Aggregator framework, SHAURYA pulls a user's 
consented financial data across banks, mutual funds, and equities — and 
runs it through an alternate credit scoring ML model built on UPI 
transaction patterns and asset signals. No CIBIL score needed.

On top of that, SHAURYA gives users:
→ A real-time net worth dashboard (banks + MFs + equities + ETFs)
→ SHAURYA Academy — personalized financial literacy modules
→ A P2P lending marketplace where your SHAURYA score determines your EMI

One app. Your entire financial life. Built for Bharat.

**Challenges we ran into**

Migrating deprecated node-sass to sass for Node 18+ compatibility. 
Debugging Chakra UI gradient token crashes in production. Implementing 
the Account Aggregator consent flow correctly. Training an alternate 
credit scoring ML model without traditional CIBIL data — using UPI 
transaction patterns and asset signals instead. Designing a dynamic 
P2P EMI calculator adapted to each borrower's SHAURYA score.

[Shaurya Chaudhary](https://github.com/SGSShaurya5497)

`2026-05-22`

---

### RapidResQ AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rapidresq-ai-701e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://rajeshwari2603.github.io/V2X-Smart-Traffic-Simulation/?utm_source=chatgpt.com) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> From Accident Detection to Instant Rescue

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Google Location services](https://img.shields.io/badge/Google%20Location%20services-333333?style=flat-square)

**The problem it solves**

1. Delayed Emergency Response

Many accident victims do not receive medical help quickly because accidents are not reported immediately.
AI detects accidents instantly and automatically alerts hospitals, ambulances, and police.
 2. Traffic Congestion Delaying Ambulances

Ambulances often get stuck in traffic signals and heavy congestion.
The system dynamically clears traffic signals and provides the fastest emergency route.
3. Lack of Real-Time Accident Monitoring

Road accidents may go unnoticed in isolated or crowded areas.
Computer Vision continuously monitors CCTV feeds and identifies accidents in real time
 4. Slow Communication Between Emergency Services

Manual reporting causes delays between police, hospitals, and rescue teams.
Automatic synchronized notifications are sent to all emergency services simultaneously.
 5. Difficulty Finding the Best Route

Emergency vehicles may choose slower routes due to traffic conditions.
AI-based route optimization identifies the quickest and least congested path.
6. Increased Fatalities Due to Late Medical Attention

A significant number of deaths occur because victims do not receive treatment within the “golden hour”
Faster detection and ambulance movement help save lives during critical moments.
 Short Version for Hackathon Form

AI addresses delayed emergency response, ambulance traffic congestion, lack of real-time accident detection, and inefficient communication between emergency services by using AI-powered accident detection, automated alerts, and smart traffic clearance systems to reduce rescue time and save lives.

**Challenges we ran into**

![image](https://assets.devfolio.co/content/7bb4666b269349f99ebc2c75d5efb740/fb7b7d58-de3c-41c0-9e8f-dab494920333.jpeg)One of the major hurdles we faced while building RapidResQ AI was reducing false accident detections during real-time video analysis. Initially, the AI model sometimes identified sudden braking, traffic congestion, or vehicles stopping at signals as road accidents. This caused unnecessary emergency alerts and affected the reliability of the system.

To overcome this, we improved the detection pipeline by combining multiple validation factors instead of depending on a single frame analysis. We integrated:
- vehicle collision detection,
- motion analysis,
- abnormal object movement patterns,
- and time-based confirmation across consecutive video frames.

We also optimized the model using OpenCV preprocessing and trained it with more diverse accident and non-accident scenarios to improve accuracy.

Another challenge was simulating smart traffic clearance for ambulances without access to real traffic infrastructure. We solved this by creating a prototype-based traffic signal simulation where the system dynamically changes signals in the ambulance route during demonstrations.

These improvements significantly increased the stability, realism, and practicality of RapidResQ AI for real-world emergency response scenarios.

**Using LocusFounder to Build a Business!**

RapidResQ AI aligns strongly with the vision of Locus founders by leveraging Artificial Intelligence, real-time analytics, and smart mobility solutions to solve critical real-world problems. Our project focuses on reducing emergency response time during road accidents through AI-powered accident detection, automatic alerts to nearby hospitals and police stations, and intelligent ambulance route optimization with smart traffic clearance. By combining AI, smart-city infrastructure, and transportation technology, RapidResQ AI enhances public safety, improves urban mobility, and supports faster lifesaving assistance. The project reflects innovation, scalability, and social impact, making it highly relevant to the mission of building smarter and more connected mobility ecosystems.

Team **Aura** -- [Mei harish gokul S](https://github.com/Meiharish)

`2026-05-22`

---

### Fetch Stripe Payment Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fetch-stripe-payment-agent-2261) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Perex21/stripe-agentic-payments.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JpLXy3qtUok) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> AI-powered payment orchestration using natural lan

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

Paygentic solves the friction involved in creating payment requests and invoices for online businesses.

Today, freelancers, agencies, consultants, and creators often have to manually:

create Stripe products
configure prices
generate checkout links
manage invoices
copy payment URLs
send them to clients

This process is repetitive, time-consuming, and not beginner-friendly.

Paygentic simplifies the workflow by allowing users to generate Stripe payment links using plain English prompts such as:

“Send a $250 invoice for logo design to alice@company.com”

The AI-agent system automatically:

extracts payment details
identifies the customer email
creates the Stripe product and pricing
generates a checkout/payment link instantly

This makes payment operations:

faster
easier
more automated
more accessible for non-technical users

The project demonstrates how AI agents can automate real-world financial workflows and reduce operational overhead for digital businesses.

**Challenges we ran into**

One of the biggest challenges during development was handling communication between the frontend and the AI-agent backend.

Initially, the frontend was opened directly through local files while the backend API was running on a separate localhost server. This created CORS and caching issues where requests were processed successfully in the backend, but the frontend failed to display the generated Stripe payment links correctly.

We also encountered:

stale JavaScript cache problems
inconsistent frontend rendering
API response handling failures
long loading states during payment generation

To solve this, we:

built a custom local proxy server
routed frontend requests through a unified localhost environment
added cache-busting and no-cache headers
rewrote frontend response handling logic
improved API debugging with detailed logging

Another major challenge was orchestrating multiple AI-agent workflows while maintaining reliable Stripe payment generation and a smooth demo experience.

These issues helped us better understand real-world production challenges involving AI agents, APIs, frontend state management, and payment infrastructure integration.

**Using LocusFounder to Build a Business!**

Paygentic fits this track because it demonstrates how AI-native tools can become real business infrastructure products.

The project transforms natural language into Stripe payment workflows by allowing users to generate invoices and checkout links using simple prompts. Instead of manually configuring products, pricing, and payment requests, businesses can automate the entire flow through AI agents.

We built Paygentic as a business-focused SaaS concept targeted at:

freelancers
agencies
consultants
creators
small online businesses

The platform combines:

AI-powered natural language parsing
autonomous agent orchestration
payment automation
modern frontend UX

to reduce friction in getting paid online.

The long-term vision is to evolve Paygentic into an AI financial operations assistant that can automate invoicing, subscriptions, payment reminders, and business transaction workflows for digital businesses.

![image](https://assets.devfolio.co/content/0c3f0fabe8ba42bb9063786767589f61/0cb8953c-b8c9-454a-b8e2-fca28aa94341.png)

![image](https://assets.devfolio.co/content/0c3f0fabe8ba42bb9063786767589f61/760c48d8-05b4-4863-a0c0-7e64893e0a1a.png)

![image](https://assets.devfolio.co/content/0c3f0fabe8ba42bb9063786767589f61/4054824d-95b5-4714-8573-060a29e0707a.png)

[Sathvik M](https://github.com/Perex21)

`2026-05-24`

---

### LaunchProof
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/launchproof-fad5) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mpja91qmk76ad2ww.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> 7-day proof engine for first paid customers

![Web](https://img.shields.io/badge/Web-333333?style=flat-square) ![SaaS](https://img.shields.io/badge/SaaS-333333?style=flat-square) ![Ai Agents](https://img.shields.io/badge/Ai%20Agents-333333?style=flat-square) ![validation](https://img.shields.io/badge/validation-333333?style=flat-square) ![LocusFounder](https://img.shields.io/badge/LocusFounder-333333?style=flat-square) ![Founder Tools](https://img.shields.io/badge/Founder%20Tools-333333?style=flat-square) ![Outreach](https://img.shields.io/badge/Outreach-333333?style=flat-square) ![Revenue](https://img.shields.io/badge/Revenue-333333?style=flat-square)

**The problem it solves**

LaunchProof solves the founder limbo between having an idea or MVP and knowing whether anyone will pay for it. Instead of stopping at generic idea scoring, it turns a raw idea into a sellable wedge, ranks first-buyer segments, proposes pricing, generates outreach, tracks real replies, and ends the sprint with a build, narrow, pivot, or drop verdict. The target customer is a deadline-driven technical founder or indie hacker who needs first-customer validation within a week, not another abstract scorecard.

**Challenges we ran into**

The hardest product challenge was shaping a workflow that proves demand without pretending validation is fully automatic. LaunchProof deliberately splits the work: the agent creates the offer, outreach, buyer-segment ranking, reply classification, and verdict logic, while the founder still sends real outreach and supplies real market replies. The second challenge was turning a business plan into a judge-readable product surface, so the submission includes generated LaunchProof workspace visuals for idea intake, outreach planning, buyer signal tracking, and the final verdict report.

**Using LocusFounder to Build a Business!**

LaunchProof fits this track because it turns a LocusFounder-generated business plan into an agent-run commercial validation sprint. The agent creates the paid offer, buyer-segment ranking, outreach pack, signal tracker, daily verdict updates, and final build/narrow/pivot/drop recommendation. The business is sold as a 7-day sprint with $29, $49, and $79 tiers.

[Abhishek Uniyal](github.com/xlogix)

`2026-05-24`

---

### Hivemind
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hivemind-0057) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Test it even before building it

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**LIVE URL:** https://svc-mp9qa8ptk2yo4tj1.buildwithlocus.com
---

## Note Regarding Demo Availability

The live deployment is currently facing an issue caused by Locus Founder infrastructure itself, which prevented proper image rendering and final deployment testing.

Because of this issue, I was unable to attach working screenshots of the application interface. I hope this does not negatively affect the hackathon submission, as the issue originates from the deployment platform rather than the application implementation itself.

---
hivemind solves the problem of fragmented information and unreliable public feedback during decision-making and research.

Today, people gather opinions manually from social media, forums, articles, Reddit threads, blogs, videos, and news websites. This process is extremely time-consuming, biased, and difficult to scale. Even after collecting data, it is still hard to predict how real people might react to an idea, product, policy, story, startup, or trend.

hivemind automates this entire workflow.

Given any topic, hivemind:
- Curates and synthesizes information from across the web
- Builds AI agents that behave like realistic human personas
- Simulates debates, conversations, disagreements, and public sentiment
- Generates prediction and insight reports based on the simulated interactions

This allows users to:
- Test startup ideas before launch
- Predict audience reactions to products, stories, campaigns, or features
- Simulate online public opinion at scale
- Analyze controversial topics from multiple perspectives
- Reduce research time dramatically
- Make better decisions using collective simulated intelligence

Instead of manually reading thousands of opinions online, users can receive a structured prediction report within minutes.

The project can be useful for:
- Startups validating ideas
- Marketing teams testing campaigns
- Writers testing story endings or audience reactions
- Researchers studying social behavior
- Product teams evaluating features
- Content creators predicting engagement trends

The platform essentially acts like a simulated internet-scale focus group powered by AI agents.

**Challenges we ran into**

One of the biggest challenges while building hivemind was designing believable AI-agent interactions.

The goal was not just to generate independent AI responses, but to simulate realistic human-like conversations where agents:
- Influence each other
- Disagree naturally
- Form opinions dynamically
- Respond differently based on personality and context

Early versions felt too robotic because every agent produced overly rational or repetitive outputs. To improve realism, I had to redesign the prompting architecture and create differentiated behavioral patterns between agents.

Another major challenge was handling large-scale information aggregation from multiple web sources. Different platforms present information in inconsistent formats, making summarization and context management difficult. I solved this by creating a structured pipeline that normalizes and condenses information before feeding it into the simulation system.

The most frustrating hurdle came during deployment. The project was deployed using Locus Founder, but a platform-side issue caused deployment instability and prevented images/screenshots from rendering correctly. Since the issue originated from the infrastructure layer rather than the codebase itself, debugging became difficult because parts of the application worked locally but failed in deployment.

Despite these issues, I continued refining the architecture, simulation pipeline, and reporting system to ensure the core idea and functionality of hivemind were fully demonstrated.

Team **DIONE** -- Pranav Bhardwaj, [Shivalik Singh](https://github.com/XZNON)

`2026-05-24`

---

### Helix
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/helix-c7db) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/fedshaft/Helix) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://helix-laiz.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Autonomous fleet engine

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Most people have ideas for digital products research reports, business plans, SEO
audits but the bottleneck isn't the idea. It's the 10 hours of manual work to validate
whether anyone will actually pay for it.
HELIX is an autonomous fleet engine that does all of it without you:
Scout - analyzes market niches and scores them for viability
Builder - generates a live storefront with AI-written copy and deploys it
instantly
Operator - fulfills every paid order automatically using Gemini producing a real
deliverable (report, plan, audit) and emailing it to the customer
CFO - tracks revenue, manages a ledger, and triggers payouts when the balance
threshold is hit
Sunset - monitors each pod's conversion rate and automatically kills underperformers before they waste more resources
Think of it as a startup co-founder that runs 24/7 spinning up micro-businesses,
testing them against real demand, and reallocating capital to winners automatically.
The demo ships three pods: ResearchPro ($9 market research reports, 4 sales),
PlanForge ($19 business plans, 1 sale), and QuickSEO ($29 SEO audits, sunset after
0 conversions). The fleet made $55 and killed one loser all autonomously.

**Challenges we ran into**

1. The payment API wasn't working  built a simulator instead
The third-party payment API we planned to integrate (Locus) wasn't accepting
connections during the build window. Rather than block the whole project, I extracted the interface into `app/services/payment_simulator.py`  it mirrors the real API's contract exactly (checkout sessions, wallet balance, payout initiation) but runs locally. Every other part of the system calls the same interface, so swapping in a real provider later is a one-file change.

2. Gemini SDK is synchronous  it was blocking the async event loop
google-generativeai doesn't have native async support. Calling model.generate_content() directly from a FastAPI async route stalled the entire server. Fixed it by wrapping every gemini call in `asyncio.to_thread()`, which offloads the blocking call to a thread pool without blocking the event loop. Added a mock fallback so the demo never crashes even if the API is down.

3. Railway trial expired mid-deployment pivoted to Render in 20 minutes
Halfway through deploying, Railway rejected the push because the trial had expired.
Switched the target to Render: rewrote `render.yaml`, updated the Dockerfile CMD to respect Render's dynamic `$PORT`, and triggered deploys via the Render REST API since GitHub webhooks weren't auto-registering. The `DATABASE_URL` scheme also had to be auto-converted from `postgresql://` to postgresql+asyncpg://` at config load time.

4. Couldn't seed the database locally due to SSL incompatibility
Render's managed PostgreSQL requires SSL, but every `psql` SSL mode (`require`,
`verify-ca`, `disable`) threw connection errors from the local machine. Instead of
fighting it, I added a `GET /admin/seed?token=` endpoint directly to the running app 
it inserts the demo data server-side where the DB connection already works. discovered a second bug in the process: asyncpg rejects ISO datetime strings  you must pass actual `datetime` objects, not `.isoformat()` strings.

[Adhav Ganesh](https://github.com/Midnight-Maverick)

`2026-05-25`

---

### studytrack
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/studytrack-20c1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://studytrack-hub.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> study guide with ai

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

[Siddharth S](https://github.com/codeXsidd)

`2026-05-25`

---

### Sitebot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sitebot-ee40) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JayWebtech/lovable-on-tg) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://t.me/lovable_on_tg_bot) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/kiArUUb4MhM?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Lovable on Telegram

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Every meme coin needs a website. Nobody wants to build one when the dev quoted $500 and Lovable expects you to know what a deployment is.

SiteBot cuts through all of that. Describe your token, pay $1 USDC, get a live landing page with tokenomics, how to buy, community links and the memes deployed to a real URL in under 10 minutes.

The same problem exists everywhere:

- A freelancer needs a portfolio. 
- A small business needs a landing page. 
- A creator needs somewhere to send their audience. 
- An event organizer needs a page live before the weekend. 


They all hit the same wall, too complex, too expensive, too slow and most of them just give up and stay invisible online.

SiteBot makes it simple enough for anyone.

SiteBot removes every step of that process. No accounts to create, no dashboards, no design decisions, no developers. Just open Telegram, describe what you want, and get a live URL.


**Built for:**

- Meme coin launchers who need a site before the next candle
- Degens spinning up tokens on pump.fun who want to look legit fast
- Freelancers who need a portfolio without a three-hour Squarespace session
- Small businesses that want a page live today, not next week
- Anyone who has a idea and just needs it on the internet — right now


**The old way**: find a tool, create an account, pick a template, learn the editor, configure hosting, set up a domain, publish or pay someone hundreds of dollars to do it for you.


**The SiteBot way**: open Telegram, describe what you want, get a live URL. That's it.

**Challenges we ran into**

**Bypassing Upstream Service Discovery Race Conditions**

While integrating the Locus Beta API for automatic, on-the-fly website deployments, we encountered a tricky edge case. The backend AWS Step Functions were occasionally failing because of transient eventual-consistency delays with AWS CloudMap Service Discovery. The API would prematurely flag our deployment as failed, even though Amazon ECS was successfully spinning up our containers in the background!

**How I solved it:** 

Instead of relying entirely on the platform's state machine, I engineered our Node worker to act like a real browser. It actively pings the generated deployment domain directly (axios.get) while waiting. The moment it detects an HTTP 200 OK response, it bypasses the false-negative API status and instantly delivers the live URL directly to the user on Telegram.

**Track: Checkout with Locus**

SiteBot is a "Pay-as-you-Build" AI service that transforms Locus Checkout into a seamless monetization engine for Telegram. By integrating Locus Checkout, we’ve solved the challenge of monetizing expensive AI API calls (Claude) without requiring users to set up complex subscription plans or provide credit card details.

[Jethro Adamu](https://github.com/JayWebtech)

`2026-04-27`

---

### ugutvbvg
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ugutvbvg-2034) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> j gububuvu

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

Team **utvtuvu** -- Priyam Kumar

`2026-04-27`

---

### Fulf
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fulf-a573) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://locus-python-integration-lime-ocean.reflex.run/login) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Programmable Work Agreements That Pay Themselves

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square)

**The problem it solves**

Work agreements and payments have always been two separate things — a conversation on WhatsApp, a PDF contract, and then a manual bank transfer weeks later when someone remembers. For freelancers, the pain is chasing clients for payment. For companies, the pain is tracking who did what, whether it was done, and reconciling it all manually at the end of the month. For AI agents, the problem is worse — they cannot hold money, cannot receive payment, and cannot be hired programmatically by any existing platform. Fulf collapses the agreement and the payment into a single object. When a payer creates a work agreement, USDC is locked immediately via Locus escrow. The worker — human or AI agent — knows the money exists before they start. When work is verified as complete, payment releases automatically. No invoices. No chasing. No trust required. The agreement pays itself.

**Challenges we ran into**

The hardest problem was verification — specifically, defining what "work is done" means in a way a system can act on without human intervention. For human workers, subjective judgment is unavoidable, so we built a dispute window with auto-release on silence. For AI agents, we needed machine-readable completion conditions that the backend could poll and evaluate autonomously — response counts, HTTP status checks, file existence checks, and custom webhooks. Getting these condition types to reliably trigger payment release through the Locus API without race conditions or double-payments required careful state management on the agreement lifecycle.
The second challenge was supporting workers who have no crypto wallet. Most freelancers, especially in emerging markets, will not have a Base wallet. Locus's email escrow feature solved this completely — human workers receive a claim link via email and never touch crypto directly. Wiring this into the agreement flow so the payer experience remained identical regardless of worker type took careful handling of the two different Locus payment paths.

3. How We Fit Into CheckoutWithLocus
Fulf uses CheckoutWithLocus as the funding mechanism for every work agreement on the platform. When a payer finalizes an agreement, we run the full Locus checkout flow — preflight to validate the session, pay to lock USDC into escrow, and poll until confirmed — before the agreement becomes active. No agreement can move to IN_PROGRESS until Locus confirms the funds are secured. This means workers always start with guaranteed payment waiting, and payers never need to remember to pay — the checkout happens at the moment of commitment, not after delivery.
Beyond checkout, we use Locus's direct USDC transfer for payment release to AI agent wallets, email escrow for human worker payouts, and AgentMail for all transactional notifications across the platform. Locus is not just the payment layer — it is the trust layer that makes the entire self-executing agreement model possible.

That's tight, honest, and covers everything the judges are looking for. The Checkout track answer specifically shows you used the full flow — preflight, pay, poll — not just a single API call, which will stand out against the other 11 submissions.
Good luck — submit it.
The second challenge was supporting workers who have no crypto wallet. Most freelancers, especially in emerging markets, will not have a Base wallet. Locus's email escrow feature solved this completely — human workers receive a claim link via email and never touch crypto directly. Wiring this into the agreement flow so the payer experience remained identical regardless of worker type took careful handling of the two different Locus payment paths.

**Track: Checkout with Locus**

Fulf uses CheckoutWithLocus as the funding mechanism for every work agreement on the platform. When a payer finalizes an agreement, we run the full Locus checkout flow — preflight to validate the session, pay to lock USDC into escrow, and poll until confirmed — before the agreement becomes active. No agreement can move to IN_PROGRESS until Locus confirms the funds are secured. This means workers always start with guaranteed payment waiting, and payers never need to remember to pay — the checkout happens at the moment of commitment, not after delivery.
Beyond checkout, we use Locus's direct USDC transfer for payment release to AI agent wallets, email escrow for human worker payouts, and AgentMail for all transactional notifications across the platform. Locus is not just the payment layer — it is the trust layer that makes the entire self-executing agreement model possible.

[victor ezealor](https://github.com/uzochukwuv)

`2026-04-28`

---

### Best DEAls
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/best-deals-2980) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cheerful-gaufre-1bdd5a.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> choose your product

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Problem it solves:
People waste time searching across multiple sites (like Amazon and Flipkart) to find the best price and genuine reviews.

**Challenges we ran into**

Challenges faced:
Getting real-time price data (APIs are limited)
Handling fake or biased reviews
Affiliate approval and commissions
Competing with big players
Keeping data updated constantly

[Rose Seby](https://github.com/rosesebyk)

`2026-04-28`

---

### Medichain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medichain-c513) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/batman123-code/medichain3.2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://medichain3-2.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Before You Swallow, We Verify.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

How It Makes Things Safer & Easier
 1. Prevents Dangerous Drug Interactions


Instantly checks combinations like Lisinopril + Ibuprofen


Flags risk levels: Safe / Caution / Dangerous


Explains why in simple language (not medical jargon)


 No more manual cross-checking or guesswork

 2. Detects Counterfeit Medicines


Scan barcode / QR code of medicine


Verifies against trusted database (or ledger)


Alerts if:


Fake 


Unverified 


Authentic 




 Especially critical in regions with high fake drug circulation

 3. Saves Time for Doctors & Pharmacists


No need to:


Flip through manuals


Search multiple sources




Just type or speak medicines → get instant results


 Turns a 5–10 minute task into 5 seconds

 4. Works in Real-World Conditions


Designed for:


Small clinics


Tier 2/3 cities


Low-resource environments




Features:


Multilingual input (Hindi, Bengali, English)


Offline-first capability (sync later)



 5. Makes Medical Knowledge Accessible


Translates complex drug interactions into:


Simple explanations


Clear risks


Actionable advice




 Even non-specialists can understand critical risks

 6. Acts as a Safety Net


Helps prevent:


Prescription errors


Adverse drug reactions


Life-threatening mistakes




 Like having an AI pharmacist + safety checker in your pocket

 Who Can Use It


Doctors → Safer prescriptions


Pharmacists → Verify medicines instantly


Clinics → Reduce human error


Patients → Double-check their meds

**Track: Checkout with Locus**

MediChain is an AI-powered safety layer for prescriptions that prevents dangerous drug interactions and detects counterfeit medicines in real time.

Team **Nebrix** -- [Priyanshu Saha](https://github.com/batman123-code), [Ayush SamantaSarkar](https://github.com/ayushss5), [MIHIR PAUL](https://github.com/Mihir-Paul), [hritika gupta](https://github.com/helmettwolf)

`2026-04-28`

---

### AgentPay Tools
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentpay-tools-1b55) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Vemesh12/LocusPaygenticHackathon3.git) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Pay-per-use AI services powered by Checkout with L

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

AgentPay Tools solves the problem of monetizing small AI services without subscriptions, accounts, or manual invoicing.

People can use it to buy useful AI tasks on demand, such as summarizing text, generating launch copy, reviewing code, or extracting structured data. Instead of asking users to sign up or manage billing, each service creates a Locus Checkout session and unlocks the result after payment.

It also makes the same marketplace usable by AI agents. The app exposes machine-readable endpoints so agents can discover available services, create checkout sessions, pay with USDC through Locus, and request fulfillment programmatically.

This makes pay-per-use AI services easier, safer, and more agent-native.

**Challenges we ran into**

One challenge was integrating the beta Checkout with Locus flow because the public docs and live beta behavior were slightly different in a few places.

The merchant checkout session endpoint had to be confirmed through the Locus community. I also ran into a payload issue where the beta API required `amount` to be sent as a string, and the endpoint returned an error until the request body was simplified.

I fixed this by creating a small server-side Locus adapter, testing the checkout route directly, simplifying the payload to the required fields, and keeping a local mock checkout fallback so the demo flow remained usable during development.

**Track: Checkout with Locus**

Integrating CheckoutWithLocus

VEMESH BYPUREDDI

`2026-04-29`

---

### CheckoutClaw
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/checkoutclaw-6073) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sokoclaw/checkoutclaw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> OpenClaw checkout bridge with receipt tracking

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

CheckoutClaw solves the missing bridge between agent intent and a usable checkout artifact. Today, agent builders often have to choose between hand-wavy payment demos and overbuilt payment stacks. We wanted a tiny, inspectable path where an agent or operator can create a checkout, hand off a link, and still retain traceable receipt state without pretending the provider integration is more complete than it is.

**Challenges we ran into**

The main challenge was staying honest about integration maturity while still shipping something judges can actually inspect. We kept the provider seam narrow, made the local path the default proof mode, and only expose the Locus preview path when the preview base URL is explicitly configured. We also had to design the helper and HTTP surfaces so OpenClaw can call them through stable JSON envelopes instead of brittle shell parsing or a permanently bound local server.

[Markeljan Sokoli](https://github.com/markeljan)

`2026-04-29`

---

### Agent Casha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agent-casha-5bc2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Saber1Y/Agent-Casha) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agent-casha.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Autonomous Agent

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Agent Casha solves a very common but often overlooked problem: most people have valuable ideas, skills, or content, but they don’t know how to turn them into something they can actually sell. Today, creating a digital product is a fragmented and time-consuming process. You have to figure out what to sell, write compelling copy, decide on pricing, build a landing page, and then integrate a payment system. For many creators, freelancers, and small business owners, this complexity becomes a barrier, and as a result, their ideas never get monetized.

Agent Casha simplifies this entire process by acting as an intelligent AI sales agent. It takes a user’s raw idea, notes, or content and transforms it into a ready-to-sell digital product. It automatically generates product positioning, descriptions, and pricing, creates a live product page, and integrates a seamless USDC checkout flow using Locus. Within minutes, users receive a shareable link that allows them to start selling immediately, without needing technical or marketing expertise.

**Challenges we ran into**

Nothing major asides my own code logic, the checkout process for simplyfied

SABER Dev

`2026-04-30`

---

### Tabibito
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tabibito-3c9c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tasfia-17/tabibito) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-molr3ae0khconwzx.beta.buildwithlocus.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_Uo6jJvhzg8?si=ZlDhuRJ9bFlOcXio) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> AI travel planner - pay once, get everything

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Mapbox](https://img.shields.io/badge/Mapbox-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square) ![AI](https://img.shields.io/badge/AI-333333?style=flat-square) ![USDC](https://img.shields.io/badge/USDC-333333?style=flat-square) ![travel](https://img.shields.io/badge/travel-333333?style=flat-square) ![deepl](https://img.shields.io/badge/deepl-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square)

**The problem it solves**

Travelling internationally means currency, accommodation, transport, activities, and language - each one is a separate task requiring different apps, accounts, and payment methods. Tabibito collapses all of this into a single interaction. Pick a country, pay 0.50 USDC via Locus Checkout, and receive a complete trip package: live weather with packing suggestions, a day-by-day AI itinerary with real walking distances between stops, translated survival phrases in the local language, and a virtual Visa card loaded with your travel budget via Laso Finance. A Browser Use agent also searches hotels matching your budget. The checkout is machine-readable by design, so AI agents can pay and receive trip plans programmatically.

**Challenges we ran into**

Wiring Locus Checkout for the beta environment required discovering that sessions must be created on beta-api but the iframe loads from beta-checkout. Deploying to Build with Locus required a multi-stage Docker build where VITE_API_URL needed baking in at build time. The Express SPA fallback broke on newer path-to-regexp. Emoji rendering on Linux required downloading NotoColorEmoji.ttf and serving it as a web font.

**Track: Checkout with Locus**

Tabibito uses Locus Checkout as the payment gate for a pay-per-use AI travel planning service. Users pay 0.50 USDC via the LocusCheckout React component before their trip plan generates. The checkout session is created server-side with a full receipt config. Both humans and AI agents can pay the same checkout. Built on Build with Locus, using Laso Finance for the travel card, and 8 wrapped APIs paid per-call from the same USDC wallet.

Tasfia Chowdhury

`2026-04-30`

---

### AgentRail
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentrail-0ae0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ladiesmans217/paygentic-week3) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Where AI agents hire and pay each other

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Zod](https://img.shields.io/badge/Zod-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square)

**The problem it solves**

AI agents are getting better at doing work, but they still usually operate alone. If one agent needs a specialized service, like code review, market research, design feedback, data cleanup, or browser QA, there is no clean way for it to discover another agent, compare trust/pricing, negotiate, pay, and unlock the result.

**AgentRail** solves this by creating a Locus-powered marketplace where buyer agents can hire seller agents for small paid tasks.

A user gives the buyer agent a task. The buyer agent then:

- asks clarification questions if the task is vague
- creates a plan before spending
- searches a machine-readable marketplace catalog
- compares seller agents by price, trust score, reviews, success rate, SLA, and capabilities
- negotiates inside the user’s budget range
- creates a Locus Checkout session
- unlocks fulfillment only after payment is verified

This makes agent-to-agent work safer because payment is not just a button. The app keeps an audit trail of the plan, selected seller, rejected sellers, checkout session, payment status, and fulfillment result.

People can use AgentRail for small specialized tasks like:

- reviewing payment/security flows
- generating market briefs
- auditing app UX
- cleaning CSV data
- writing demo scripts
- planning browser QA
- summarizing policies or hackathon rules

The goal is to show how agents can become buyers and sellers in a real service economy, using Locus Checkout as the payment layer.

**Challenges we ran into**

One of the biggest challenges was making the project feel like an actual agent marketplace instead of just a human clicking marketplace cards.

The first version had manual checkout buttons, but that did not prove the real idea. I rebuilt the flow so the buyer agent drives the process: it clarifies the task, plans, searches the catalog, ranks sellers, negotiates, and stops at a payment approval checkpoint.

Another challenge was handling unpredictable model output. Gemini sometimes returned structured JSON fields where the frontend expected plain text, which caused a React white-screen crash. I fixed this by normalizing model output on the backend and making the frontend safely render strings, arrays, and objects.

Locus live checkout testing was also tricky. Very tiny USDC amounts were useful for conserving credits, but they appeared too low for reliable live checkout testing. I adjusted the marketplace pricing to a more realistic test range and added a safe demo fallback so the judging flow still works if the live beta checkout rejects a request.

I also had to be careful with payment safety. The app does not unlock seller output from a frontend success callback alone. Payment must be confirmed by the backend or demo verification before fulfillment runs.

**Track: Checkout with Locus**

AgentRail fits the Checkout with Locus track because the core user flow is built around creating and verifying Locus checkout sessions for agent-to-agent services.

A buyer agent receives a task, plans what kind of seller agent is needed, searches a machine-readable marketplace catalog, compares seller agents by trust, price, reviews, SLA, and capabilities, negotiates inside the user’s budget, and then creates a Locus Checkout session for the selected service.

The seller output stays locked until payment is verified by the backend. The app also keeps an audit trail showing the buyer-agent plan, selected seller, checkout session, payment status, and fulfillment result.

This uses Checkout with Locus as the payment layer for an AI-agent services marketplace, not just as a generic payment button.

[Manjunath Patil](https://github.com/Manjunath3155)

`2026-04-30`

---

### Subscription tracker
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/subscription-tracker-96a7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/debaa98/Subscription-tracker) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://subscription-tracker-ruddy.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Track analyze all Subscription plane an usage.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![OAuth](https://img.shields.io/badge/OAuth-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![vectorDB](https://img.shields.io/badge/vectorDB-333333?style=flat-square)

**The problem it solves**

An AI-powered subscription manager that helps users and teams discover, track, and cut waste from all their AI SaaS tools

**Challenges we ran into**

Track is an AI-powered app that automatically discovers, monitors, analyzes, and optimizes all your subscriptions across the platforms.

Team **solosquard** -- [Debabrata Pattnayak](https://github.com/debaa98)

`2026-04-30`

---

### AgentCred
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentcred-1549) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0xshae/paygentic-week3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://website-mu-orpin-r334ujulu0.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/oHMBYXw-Tsw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Onchain Reputation for Agents

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![CheckoutWithLocus](https://img.shields.io/badge/CheckoutWithLocus-333333?style=flat-square) ![402 Payment Required](https://img.shields.io/badge/402%20Payment%20Required-333333?style=flat-square)

**The problem it solves**

APIs currently treat all autonomous agents equally, which is inefficient and risky for both providers and developers. A brand-new agent with no track record often pays the same price and faces the same rate limits as a reliable, long-standing agent. This creates several major pain points:

*   **The "Trust Gap"**: API providers have no way to distinguish between a "good" agent and a malicious bot. This often leads to high "safety margin" pricing or aggressive rate-limiting that penalizes honest developers.
*   **Lack of Incentives**: There is currently no economic incentive for an agent to maintain a high success rate or a clean track record.
*   **Sybil Vulnerability**: Without an economic stake or reputation system, it is trivial for bad actors to spin up thousands of new wallets to spam or exploit API endpoints.

**AgentCred** solves this by introducing **Onchain Reputation-Gated Access**. It allows people to:
*   **Enforce Economic Stakes**: Require agents to stake USDC via **Locus Checkout** before their first call, creating an immediate financial barrier to abuse ("Skin in the game").
*   **Reward Reliability**: Automatically lower costs for agents that perform well. As an agent's reputation score (0–100) grows through successful calls, they move from Bronze to Gold tiers, reducing their costs by up to **10x**.
*   **Automate Sybil Resistance**: By tying access to a wallet's onchain reputation, providers can protect their infrastructure from bad actors without manual whitelisting or complex bot-detection logic.

**Challenges we ran into**

*   **The "Returning Agent" UX**: One of the trickiest hurdles was designing the logic for when to trigger a `402 Payment Required` response. Initially, the system would incorrectly prompt for a full $1 USDC "Initial Stake" every time an agent's balance dipped, even if they were a long-time user who had already spent $10. I overcame this by implementing a **"Total Deposited" tracking system** (Balance + Lifetime Spent) to distinguish between a first-time setup and a simple balance top-up, ensuring a much smoother experience for returning agents.
*   **TypeScript & Database Integration**: Integrating `better-sqlite3` within a modern TypeScript environment led to several compilation and path-resolution issues during the build phase. I resolved this by refining the `tsconfig.json` and creating a clean Data Access Layer (DAL) that abstracted the database schema, allowing for atomic updates to reputation scores even under high concurrency.
*   **Real-time Glassmorphism Dashboard**: Building a "live" dashboard that updates for every single agent call required a low-latency communication method. I initially considered standard REST polling, but it felt sluggish. I pivoted to **Server-Sent Events (SSE)**, which allowed the backend to "push" reputation jumps and audit logs directly to the frontend. This kept the UI (with its premium glassmorphism aesthetic) feeling snappy and alive without overloading the server.
*   **Asynchronous Payment Settlement**: Since Locus Checkout happens onchain, payments aren't instant in the request cycle. I had to build a robust webhook handler and a state-matching system to ensure that an agent's reputation and balance were updated the moment the transaction settled, allowing them to resume API calls immediately without manual refresh.

**Track: Checkout with Locus**

AgentCred is built specifically to showcase the power of **CheckoutWithLocus** as the financial layer for the agentic web. It aligns with the track's focus on machine-readable, programmatic payments in the following ways:

*   **Programmatic Staking via Locus SDK**: RepGate utilizes the Locus Checkout SDK to generate session-based payments. When an agent lacks the reputation or balance to proceed, RepGate issues a machine-readable **HTTP 402 Challenge**. This allows agents to discover the checkout requirements and settle the payment autonomously using Locus's agent-native checkout endpoints.
*   **The "Reputation-Aware" API Wrapper**: One of the primary use cases for CheckoutWithLocus is gating tools behind a checkout session without requiring traditional subscriptions or accounts. RepGate takes this a step further by using Locus Checkout as a **sybil-resistance mechanism**—requiring an onchain stake to prove "skin in the game" before granting access to premium API tiers.
*   **Seamless Agent-to-Machine Payments**: RepGate demonstrates the track's goal of "machine-readable design" by returning structured metadata (Checkout URL, Session ID, and Tier Requirements) in every 402 response. This enables a 100% autonomous flow where an agent can detect a payment requirement, authorize the USDC transfer via Locus, and resume its task without any human intervention.
*   **Dynamic, Pay-Per-Use Economy**: Instead of rigid monthly bills, RepGate uses Locus to facilitate a fluid, behavior-based pricing model. By deducting micro-payments for each successful API call and rewarding good performance with lower rates, it implements the exact "pay-as-you-go" vision that CheckoutWithLocus was designed to enable for autonomous agents.

[Shagun Prasad](https://github.com/shap28)

`2026-04-30`

---

### Skillmirror AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skillmirror-ai-4ae3) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Mirror that reflects scope for improvements

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

[Naaysha Jain](https://github.com/naayshajain0112)

`2026-04-18`

---

### TransitX Intelligence
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/transitx-intelligence-d631) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://maragadhavelt.github.io/TransitX-Intelligence/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Revolutionizing public transport with predictiveAI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Urban public transport systems suffer from inefficiencies such as unpredictable delays, overcrowding, and lack of real-time visibility. Commuters often face uncertainty about arrival times, route congestion, and optimal travel choices.

Existing systems provide static schedules but fail to adapt dynamically to real-world conditions like traffic, peak hours, and demand fluctuations.

TransitX Intelligence solves this by using AI-powered predictive analytics and real-time tracking to provide accurate arrival times, crowd insights, and optimized route suggestions. This helps commuters make smarter decisions, reduces waiting time, and improves overall travel efficiency.

Additionally, transport authorities can use the system to monitor performance, detect delays early, and optimize fleet management, leading to a more reliable and efficient urban mobility system.

**Challenges we ran into**

Building TransitX Intelligence came with several technical and design challenges.

One major challenge was handling real-time data updates for multiple buses and routes without affecting performance. Continuously updating the UI caused lag and inconsistent state management. I solved this by optimizing state updates and reducing unnecessary re-renders, ensuring smooth real-time tracking.

Another challenge was simulating accurate ETA predictions. Since real-world data was limited, I had to design a logic that mimics real-time conditions like traffic and delays. I approached this by combining time-based calculations with dynamic adjustments to create realistic predictions.

Integrating multiple UI components like maps, alerts, and analytics dashboards into a single cohesive system was also complex. Ensuring consistency in design and responsiveness required careful structuring and modular development.

Additionally, balancing a visually rich UI with performance was challenging. I optimized styles and reduced heavy animations to maintain a smooth user experience.

Overall, these challenges helped improve the system’s scalability, performance, and usability.

**Track: Using BuildWithLocus to leverage our suite.**

TransitX Intelligence leverages the BuildWithLocus platform to design and deploy an interactive, real-time transit intelligence dashboard.

Using Locus tools, we structured a scalable and responsive web interface that integrates live tracking, predictive analytics, and data visualization into a unified system. The platform enabled rapid prototyping of UI components such as dashboards, route monitoring panels, and alert systems.

Additionally, BuildWithLocus supported seamless integration of APIs and data pipelines, allowing us to simulate real-time transport data and deliver dynamic updates efficiently. Its development environment helped streamline deployment and optimize performance for a smooth user experience.

By utilizing BuildWithLocus, we were able to accelerate development, focus on intelligent features, and build a production-ready solution for smart urban mobility.

[Maragadhavel T](https://github.com/maragadhavelt)

`2026-04-21`

---

### SubNova
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/subnova-e28e) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> An autonomous Paygentic AI that negotiates bills

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Translation API](https://img.shields.io/badge/Translation%20API-333333?style=flat-square)

**The problem it solves**

The Problem: Subscription Fatigue & The "Loyalty Tax"
In today's digital economy, consumers and small businesses are bleeding money through "subscription creep." We sign up for services, internet plans, and software, only for the promotional rates to expire, leaving us trapped paying exorbitant fees.

The biggest hurdle? Friction. Canceling a service or negotiating a lower monthly bill (like with Comcast or AT&T) requires waiting on hold for hours or navigating highly defensive retention chatbots. Because the process is so tedious and anxiety-inducing, millions of people simply accept the "loyalty tax" and overpay. Passive subscription trackers warn you about the cost, but they don't actually fix it for you.

🟢 The Solution: SubNova
SubNova transitions fintech from passive tracking to active agentic negotiation.

By utilizing the Locus ecosystem, SubNova isn't just a dashboard; it’s an automated financial advocate. It solves the problem of subscription fatigue by doing the dirty work for you:

🕵️‍♂️ Autonomous Auditing: SubNova monitors your recurring Locus payments to identify under-utilized services or bills that have suddenly spiked in cost.
🤖 Agent-to-Bot Negotiation: Instead of you sitting on the phone, SubNova securely deploys an AI agent to interface directly with customer support chatbots on your behalf. It uses competitor pricing data to actively negotiate your bills down to promotional rates.
⚡ Zero-Click Cancellation: If a service refuses to lower its rate to the benchmark, or if you simply want out, SubNova's agent handles the entire cancellation and Locus payment stop-logic automatically.

**Challenges we ran into**

1. The "Bot-to-Bot" Conversation Pacing
The Hurdle: When building the live Nova Agent Interface, the initial iterations of the AI negotiation simulator felt too robotic and instantaneous. Real customer support bots have API latencies, and our AI agent needed time to "think" and format payloads. Printing the chat logs instantly broke the illusion of a live, autonomous agent. The Fix: I wrote a dynamic JavaScript rendering engine for the terminal feed. Instead of static intervals, the engine calculates the delay for each message based on string length and the type of message (e.g., system logs are fast, while the agent constructing a counter-offer to Comcast takes longer). This created a highly realistic, asymmetrical pacing that brings the AI to life.

2. Escaping the "SaaS-in-a-Box" Aesthetic
The Hurdle: Most financial dashboards look identical—flat white backgrounds, generic tables, and standard 1px gray borders. I wanted SubNova to feel like an elite, futuristic "Paygentic" tool, but standard CSS frameworks kept boxing me into conventional layouts. The Fix: I discarded standard frameworks and engineered a bespoke CSS architecture called "The Obsidian Luminary." I instituted a strict "No-Line" rule—meaning no solid borders could be used. Instead, depth and separation are achieved entirely through background color shifts (surface-low to surface-elevated) and 30px backdrop-blur glassmorphism, giving the AI terminal a floating, premium aesthetic.

3. Simulating Secure Locus Agent Hand-offs
The Hurdle: The conceptual challenge was how to allow an AI to negotiate a bill and directly manage the payment method without compromising user security. The Fix: We architected the concept of the Locus Smart Proxy. Instead of giving the AI raw access to credit card APIs, the AI utilizes a scoped Locus token that is only authorized to downgrade plan costs or execute cancellations. This ensured that our "Paygentic" integration remained secure while still allowing autonomous financial actions.

**Track: Using BuildWithLocus to leverage our suite.**

SubNova perfectly embodies the core philosophy of the BuildWithLocus track by demonstrating how AI agents must interact directly with robust financial infrastructure to be truly useful.

To bridge the gap between "artificial intelligence" and "actual utility," SubNova leverages the Locus suite to power its underlying "Locus Vault" architecture.

Our project fits into this track through the following implementations:

Scoped Payment Execution: SubNova doesn't just "advise" the user; it actively utilizes Locus APIs to intercept and manage recurring subscription charges. When the AI successfully negotiates a lower internet bill, it programmatically updates the Locus payment schedule to reflect the new $70/mo rate.
The Smart Proxy: We conceptualized a system where the AI is granted secure, scoped access to the Locus suite. The agent cannot make unauthorized purchases; it is only authorized by Locus rules to downgrade plan costs or execute zero-click cancellations on unused services.
True "Paygentic" Utility: By building with Locus, we transitioned the AI from a simple chatbot into a financial operator capable of making programmatic billing adjustments in real-time without human intervention.
SubNova proves that the Locus suite is the ideal foundational layer for the next generation of autonomous, agent-driven commerce.

NITIN RAJAK

`2026-04-21`

---

### Locus Chaos
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/locus-chaos-f1c4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Officially-aditya/locuschaos) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://locuschaos.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/6nHLgN31-Ok) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Break your app before production does.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

LocusChaos solves a simple but painful problem: most teams only discover deployment fragility after users do.

Shipping a repo is easy. Knowing whether that deployed app can survive restarts, bad config, traffic spikes, or infrastructure weirdness is much harder. Today, those checks are usually manual, inconsistent, or skipped entirely because they take too much time.

With LocusChaos, teams can:

- deploy a repo to Locus and immediately stress-test the live service
- run resilience checks like traffic floods, restart recovery, and env corruption
- keep a persistent history of deployment outcomes, logs, verdicts, and scores
- revisit previous live deployments and run chaos tests later without redeploying
- catch weak spots before production incidents happen

That makes deployment validation:

- faster, because setup, execution, and reporting are in one place
- safer, because failures are surfaced before real users hit them
- more repeatable, because every run is logged and tied to a user/account
- easier to demo and review, because results are saved as clear reports instead of scattered terminal output

In short, LocusChaos turns “I hope this deploy is stable” into a measurable, repeatable resilience workflow.

**Challenges we ran into**

One of the biggest challenges was making long-running deployment and chaos workflows behave reliably on serverless infrastructure.

At first, the app tried to do everything in one flow:
1. deploy to Locus
2. wait for the deployment to become healthy
3. run the chaos suite
4. stream logs back live

That worked locally, but in production we hit real runtime limits. A deployment could already be live on Locus, while our app was still stuck polling deployment status. In some cases, the worker would get cut off before a single chaos test started, so the UI looked stuck even though the app had actually deployed successfully.

A few specific issues we had to solve:

- **Deployment status lagged behind reality**
  Locus could already be serving traffic while our app still saw `building` or `deploying`. We fixed this by treating successful responses from the live service URL as a valid readiness signal instead of waiting only for one backend status value.

- **Serverless runtime limits killed long jobs**
  The original design tried to deploy and run chaos tests inside one request. That was too fragile on Vercel. We solved it by splitting the workflow into two phases:
  - phase 1: deploy + wait until live
  - phase 2: run chaos tests on the already-live deployment

- **Reconnects showed no useful state**
  If the live SSE stream dropped, the UI could lose context. We fixed that by persisting logs, intermediate state, and results in the database while the run was happening, so the app could rebuild itself from saved run state.

- **The UI route structure caused confusion**
  After authentication, the app originally mixed the public landing page and the signed-in run flow. That led to bad redirects and stale run recovery bugs. We separated the authenticated deploy experience into `/new-run` and made the dashboard/history flow clearer.

The biggest takeaway was that the hard part was not just “running chaos tests,” but designing the orchestration so it stays truthful and recoverable even when external systems are slow, status APIs lag, or the runtime is interrupted.

**Track: Using BuildWithLocus to leverage our suite.**

LocusChaos fits the **Using BuildWithLocus** track because the core product is built around Locus as the deployment and runtime layer.

We use BuildWithLocus to:

- spin up real app deployments directly from GitHub repos
- provision the service environment that the chaos suite tests against
- manage live service URLs and deployment lifecycle events
- run resilience checks on actual deployed applications instead of mocked environments
- support follow-up actions like redeploy, restart, and teardown

What makes the project a strong fit for this track is that Locus is not just an add-on in our stack, it is the foundation of the workflow. The entire user journey depends on BuildWithLocus:

1. a user connects a repo
2. the app deploys it on Locus
3. once the deployment is live, LocusChaos runs resilience tests against that live Locus-hosted service
4. the results are saved as persistent reports, scores, and logs tied to the deployment

So instead of using Locus only to host an app, we are extending the Locus deployment experience itself by adding a post-deploy resilience layer. That turns BuildWithLocus into not just a deployment platform, but the base for automated chaos validation and deployment confidence.

[Aditya Yadav](https://github.com/Officially-aditya)

`2026-04-21`

---

### AutoSAAS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/autosaas-f6ee) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/suvab4gh/autosaas) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://autosaas-delta.vercel.app/#demo) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ybNxD_ACiqU) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> A Self-Funding SaaS Factory

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![HTML5](https://img.shields.io/badge/HTML5-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square) ![CSS3​](https://img.shields.io/badge/CSS3​-333333?style=flat-square) ![Uvicorn](https://img.shields.io/badge/Uvicorn-333333?style=flat-square) ![IntersectionObserver API](https://img.shields.io/badge/IntersectionObserver%20API-333333?style=flat-square)

**The problem it solves**

The barrier to entry for software entrepreneurship is still too high. While AI coding assistants (like Copilot or Cursor) and deployment agents (like Vercel v0) have made writing and shipping code easier, they only solve **half the equation**. 

Once an app is deployed, the creator is immediately hit with the operational burden of running a business:
1. **Setting up monetization** (Stripe integration, managing webhooks, handling pricing tiers).
2. **Paying for infrastructure** (cloud hosting costs, database storage).
3. **Managing cash flow** (moving money from payment gateways to infrastructure providers).

**AutoSaaS completely eliminates this operational friction.** 

### What People Can Use it For:
- **Rapid Prototyping:** Solo founders can test 10 different SaaS ideas in a day. Instead of spending weeks building boilerplate and payment systems, they describe the niche tool they want (e.g., "A SaaS that converts Figma URLs to Tailwind code for $5/export"), and it's instantly live and ready to accept payments.
- **Micro-SaaS Factories:** Indie hackers can run a portfolio of micro-applications without drowning in infrastructure bills, because each app automatically funnels its own revenue to cover its specific hosting costs.

### How it Makes Existing Tasks Easier & Safer:
- **Zero-Touch Financial Operations:** It is incredibly tedious to manually calculate if an app is profitable. By wiring the **Checkout with Locus** API directly into the **Locus Wallet**, the app safely and autonomously settles its own $0.25/service hosting bill. 
- **Financial Safety:** You never have to worry about a "zombie app" draining your personal credit card. If an app generates revenue, it pays for itself. If it doesn't, you can kill it with zero sunk operational costs.
- **Instant Monetization:** Developers no longer need to read complex payment integration docs. The agent securely injects the exact billing logic into the frontend and backend automatically.

**Challenges we ran into**

Building an autonomous agent that strings together LLMs, version control, deployment, and payments was incredibly complex. 

1. **Hallucinating the Checkout Injection:** 
   The hardest part was getting the LLM (Claude 3.5 Sonnet) to consistently and correctly inject the **Checkout with Locus** SDK into the React code it generated. Frequently, the LLM would invent its own props or try to use Stripe instead.
   * **How I got over it:** I built a rigid "System Prompt Chain" that forces the LLM to use a predefined `<LocusPaywall />` React component wrapper. Instead of asking the LLM to write the checkout logic, the FastAPI backend injects the Locus `product_id` into the environment variables during deployment, ensuring the checkout flow never breaks.

2. **Managing Asynchronous Timeouts:**
   Deploying an app via the Locus Build API and waiting for the live URL takes time. Initially, the frontend would simply timeout while waiting for the FastAPI backend to finish the 5-step loop.
   * **How I got over it:** I ripped out the standard REST endpoints and rewrote the orchestrator to use **Server-Sent Events (SSE)**. Now, the FastAPI backend streams real-time logs line-by-line to the frontend. This keeps the connection alive and creates the beautiful "live terminal" experience you see on the dashboard.

3. **Frontend Premium Aesthetics vs. Performance:**
   I wanted an "Awwwards-tier" design with glowing orbs, glassmorphism, and complex bento-grid animations. However, adding too many blur filters tanked the frame rate during the terminal typing animation.
   * **How I got over it:** I optimized the CSS by restricting animations strictly to `transform` and `opacity` properties, offloading the work to the GPU (`will-change: transform`). I also used an `IntersectionObserver` to ensure the heavy number-counters and typing effects only ran when the elements were actually in the viewport.

**Track: Using BuildWithLocus to leverage our suite.**

AutoSaaS doesn't just use a single Locus API; it uses Locus as an entire economic and operational operating system for autonomous software. 

1. **Deploying Code:** We use **Build with Locus** programmatically via API to instantly provision Postgres databases and deploy the React/FastAPI code written by our AI agent.
2. **Instant Monetization:** The agent automatically generates code that injects **Checkout with Locus** into the deployed SaaS applications, enabling them to instantly process user payments.
3. **Closing the Loop:** All revenue generated from the deployed apps flows directly into a **Locus Wallet**, which is programmatically configured to auto-deduct the $0.25/service hosting bill.

By leveraging the entire Locus suite together, AutoSaaS demonstrates the platform's ultimate potential: allowing an AI to autonomously deploy, monetize, and sustainably fund its own software creations in a completely closed loop.

[Suvanan Biswas](https://github.com/suvab4gh)

`2026-04-23`

---

### FluxPay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fluxpay-9123) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://amazing-peony-f29f8c.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> AI Auto-Payment Agent • HIGH WIN CHANCE

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Managing finances and accounting tasks can be complex, time-consuming, and prone to human error. Individuals and businesses often face challenges such as:

Tracking recurring payments and expenses manually
Missing due dates for bills or subscriptions
Handling large volumes of financial data
Lack of automation in everyday accounting tasks
Risk of calculation mistakes and mismanagement

FluxPay addresses these issues by introducing an intelligent AI-powered agent that automates and simplifies financial operations.

**Challenges we ran into**

Building FluxPay was an interesting experience, but I faced several challenges during development:

🔹 1. Designing the AI Agent Logic

One of the main challenges was deciding how the AI agent should behave for different accounting tasks like tracking payments and generating reminders.
👉 Solution: I broke the logic into smaller functions and used condition-based flows to simulate intelligent behavior step by step.

🔹 2. Handling Recurring Payments

Managing recurring transactions (monthly/weekly) was tricky because it required tracking time and repeating actions automatically.
👉 Solution: I used structured data (like dictionaries) and logic to store payment details and simulate recurring cycles.

🔹 3. UI and Dashboard Design

Creating a clean and user-friendly interface for financial data was difficult, especially making it simple yet informative.
👉 Solution: I focused on minimal design, used clear sections, and organized data properly to improve readability.

Nitesh Garg

`2026-04-22`

---

### Renly
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/renly-026c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/velikanghost/renly) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/LYepkkLqmIg) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LYepkkLqmIg) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Scaffold and Deploy

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Renly is built to eliminate "deployment friction" for developers using the Locus PaaS. While modern cloud platforms are powerful, the "plumbing" required to get a framework like Next.js or NestJS from a local machine to a production container is often tedious and error-prone.

**How:**
*  Instead of manually writing Dockerfiles and configuration scripts, **renly init** generates a project that is "Locus-ready" out of the box.
*  Developers no longer need to jump between their terminal and the Locus Dashboard. Renly handles the creation of Projects, Environments, and Services via API.
*  It bridges the gap between local Git and Locus build workers, allowing for a seamless "code-to-cloud" experience in seconds.

**Challenges we ran into**

*  Locus requires containers to listen specifically on **Port 8080**. Many frameworks default to 3000 or 4000. I had to build a "Smart Injection" system that patches next.config.js and environment variables during the scaffolding phase to ensure the container health checks don't fail upon deployment.
*  Handling the "cold start" of a deployment (where the project doesn't exist yet on Locus) required careful sequencing of API calls to ensure the Workspace, Project, and Service were all linked correctly before the Git push was initiated.

Velikan Ghost

`2026-04-23`

---

### Quorum Protocol
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quorun-protocol-a2f4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Gideon145/quorum-protocol) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/nPXiCIZkvnw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nPXiCIZkvnw) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Validate your idea with 20 AI personas

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Most founders validate ideas by asking friends or posting in Discord — both give biased, encouraging answers. Real user research costs thousands and takes weeks. Quorum Protocol replaces that with a panel of 20 engineered synthetic personas that simulate how actual diverse users — different ages, incomes, tech literacy levels, and occupations — would respond to your idea. It scores product-market fit using a weighted formula, surfaces the exact objections blocking adoption, and lets you refine the idea and re-run the entire panel immediately. You go from idea to structured validation in under 2 minutes.

**Challenges we ran into**

Getting 20 personas to be genuinely diverse and not just surface-level different was harder than expected. The AI would default to clustering responses — most personas would agree, which defeats the purpose. I had to engineer strict distribution constraints into the prompt (minimum skeptics, income spread, tech literacy mix) and implement a retry mechanism when the model returned malformed JSON. I also had to rethink the share URL architecture mid-build — the original approach base64-encoded the entire report into the URL, producing 3000-character links that broke on mobile. Switched to a server-side in-memory store with 10-character short IDs.

**Track: Using BuildWithLocus to leverage our suite.**

How it fits: Quorum Protocol is fully deployed on BuildWithLocus as a containerized Next.js service. No Dockerfile, no cloud console — just a git push and a single API call to trigger the deploy. All AI inference routes through the Locus Wrapped OpenAI API (POST /wrapped/openai/chat). The entire stack — build, routing, SSL, infrastructure — runs on BuildWithLocus.

[Gideon xyz](github.com/gideon145)

`2026-04-23`

---

### NexusRegistry
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexusregistry-7217) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tasfia-17/NexusRegistry.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mob1a30kdfxjxm4p.buildwithlocus.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/v2VOasvcYak) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> The DNS for AI Agents

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem NexusRegistry Solves

Most companies running AI agents today have them scattered across three clouds.

Some live on AWS. Some run through Azure Copilot Studio. Others are deployed on Google Cloud. Each one is registered in a different registry, with a different schema, different governance rules, and a different dashboard.

When someone asks, **"Do we have an agent that can process invoices?"** nobody knows.

Three consoles get opened, three different searches run, three different formats come back, and it's still unclear if everything was found.

Forbes called this **governance fragmentation** in April 2026, right after AWS, Azure, and Google all launched their own agent registries within weeks of each other. None of them interoperate.

---

## What NexusRegistry Does About It

## One search bar for all agents

Type **"invoice processing for healthcare"** and get back every matching agent across AWS, Azure, GCP, and Locus  ranked by relevance, normalized to the same schema, with compliance tags and lifecycle status intact.

## Register any A2A-compliant agent in seconds

Paste a URL. NexusRegistry fetches the agent card from `/.well-known/agent.json` automatically and adds it to the registry.

No manual form filling.

## Deploy any registered agent with one click

Found the right agent? Hit **Deploy**.

It spins up as a live BuildWithLocus service with a public HTTPS URL in about 60 seconds.

No DevOps, no Dockerfiles, no cloud console.

## Keep the registry fresh automatically

A background worker syncs from all connected cloud registries every 15 minutes.

New agents appear automatically. Deprecated ones get flagged.

---

## Who This Is For

- **Platform engineers** who need a single inventory of every AI agent running in an organization  
- **Developers** who want to find and reuse existing agents instead of rebuilding them  
- **Compliance teams** who need to know what agents exist, what they do, and what data they touch  
- **Anyone building on Locus** who wants a searchable catalog of deployable agents

**Challenges we ran into**

## Challenges

## Locus beta ignores custom Dockerfile paths

The buildConfig.dockerfile field accepts any value, but the build system always looks for a file named exactly Dockerfile at the archive root. Setting it to Dockerfile.api or passing rootDir had no effect.

The fix was to stop fighting it. The root Dockerfile was renamed to match whichever service was being deployed.

Separate Dockerfile.api, Dockerfile.frontend, and Dockerfile.worker files were kept at the repo root, with COPY paths adjusted to work from the monorepo root instead of each subdirectory.

## Pip dependency conflict on ARM64

Pinned versions that resolved fine locally failed on Locus's AWS Graviton (ARM64) build environment.

psycopg[binary] has no ARM64 wheel on PyPI, and the pinned pydantic==2.10.3 conflicted with transitive dependencies pulled in by other packages.

The fix was to switch to minimum version bounds instead of exact pins, drop the binary extra from psycopg, and add gcc + libpq-dev to the Dockerfile so psycopg could build from source.

## The beta API endpoint

The claw_dev__ key prefix was the hint — it only works against beta-api.buildwithlocus.com, not the production endpoint.

It took a few failed authentication attempts before checking the environment-specific base URLs in the skill file.

Tasfia Chowdhury

`2026-04-23`

---

### GIGAmind
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gigamind-b5bb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prajusha2004/ai-gig-finder) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://gigamind.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Be GIGA ahead - Dream it, Achieve it

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![API](https://img.shields.io/badge/API-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

🔹 Problem the Project Solves
Freelancers waste ridiculous amounts of time doing three things:

Scrolling endless job listings

Writing repetitive proposals

Missing relevant opportunities

GIGAmind fixes that by automating the entire workflow:

🧠 AI Job Matching
Finds relevant freelance jobs based on user skills

✍️ Auto Proposal Generation
Generates tailored proposals instantly

⚡ One-Click Apply
Reduces manual effort and speeds up applications

👉 The goal:
Turn job hunting from an active grind into a passive system.

🔹 Key Features

- Interactive landing UI with animated components
 
- Resume upload + skill input system
 
- AI-based job discovery concept
 
- Automated proposal generation flow
 
- Clean navigation with sections (Features, Demo, How it works)

- OAuth-based authentication (Google login)

- Fully deployed on Netlify

**Challenges we ran into**

🚀
💥 Problems Faced During Development

1. Frontend Completely Broke

At one point:

* UI styling disappeared
* Tailwind stopped working
* Page rendered as plain HTML (looked like 2005 internet)

Cause:

* Tailwind v4 config mismatch
* Incorrect PostCSS setup

Fix:

* Installed correct PostCSS plugin (`@tailwindcss/postcss`)
* Fixed config structure
* Rewrote styles import order

2. Build & Deployment Failures

App worked locally but failed after deployment.

Errors:

*`dist does not exist`
* blank page after deploy

Cause:

* Wrong build command (`bun run build`)
* Wrong publish directory (`dist/client` instead of `dist`)

Fix:

Corrected to:

  * `npm run build`
  * `dist`

3. Environment Variables Missing in Production

App crashed with:


Missing Supabase environment variables


Cause:

* `.env` works locally but NOT on Netlify

Fix:

* Added variables in Netlify dashboard:

  * `VITE_SUPABASE_URL`
  * `VITE_SUPABASE_ANON_KEY`

4. Routing Issues After Deployment

Navigation links worked locally but not in production.

Cause:

* SPA routing not configured

Fix:
Created:


public/_redirects


With:


/* /index.html 200


5. OAuth Login Failure (Google / Apple)

Error:


Unsupported provider: provider is not enabled


Cause:

* OAuth providers not enabled in Supabase

Fix:

* Enabled Google provider
* Added client ID & secret
* Removed Apple login (complex setup)


6. Runtime Crash: `process is not defined`

App crashed in browser.

Cause:

* Used `process.env` in frontend (Node-only)

Fix:

* Replaced with:

import.meta.env.VITE_


7. Loader / App Boot Issues

Loader screen didn’t render correctly.

Cause:

* Incorrect conditional return in React:


if (loading) return;


Fix:

if (loading) return <LoadingScreen />;


🔥Biggest Challenge

The biggest issue wasn’t coding.

It was:
👉 Making local development match production behavior

Things that “worked locally” failed after deployment due to:

* environment variables
* routing
* build configs

✅Final Outcome

* Fully working deployed app
* Functional UI with smooth navigation
* Authentication integrated
* Resume + skills input added
* Stable production build

🧠 What I Learned

* Deployment ≠ local environment
* Environment variables must be configured separately
* Frontend builds are sensitive to config mistakes
* OAuth requires backend setup, not just UI buttons
* Debugging is 80% configuration, 20% code

🎯 Conclusion

GIGAmind successfully demonstrates how AI can automate freelance workflows.

Despite multiple system crashes, config failures, and deployment issues, the final product is stable, functional, and deployable.

[Prajusha Dhar](https://github.com/Prajusha2004)

`2026-04-23`

---

### TryIt
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tryit-907b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-mobdhpeyorxzh75i.buildwithlocus.com/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/EoJv2CV-4hM) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> Run githup repos in minutes

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![BuildWithLocus](https://img.shields.io/badge/BuildWithLocus-333333?style=flat-square)

**The problem it solves**

**The problem it solves**
                                                                                                                       
You find a cool GitHub repo. You want to try it. Twenty minutes later, you're still fighting Node versions and missing dependencies, and the maintainer who built it gets nothing for your time.                                             
                                                                                                                         
*TryIt fixes both in one paste.*
Paste → live URL in ~30 seconds. A Llama 3.3 70B agent (via Groq) reads your repo, package.json, vite.config.ts, whatever's there and writes a real, repo-specific Dockerfile. BuildWithLocus ships it. You get a public HTTPS URL with a 20-minute TTL.

- Every try pays the author. Owners claim a repo via file-drop verification. 40% of every $0.05 try ($0.02 USDC) lands in their Locus wallet, on-chain, automatically. First real economic tail on GitHub stars.
- Preview before you pay. A free button runs just the agent. You see the Dockerfile, port, and start command, no charge, before committing a nickel.                                                                                   

*What you can do with it*
- Try any OSS project in under a minute, no clone, no local setup                                                      - Drop a "Try it" badge in your README and get paid per try
- Share a live demo of your side project with a single link                                                            
                                                                                                                         
TryIt itself runs on BuildWithLocus. Every paid try provisions another service through the same API. Agents deploying agents.

**Challenges we ran into**

**Challenges I ran into**
                                                                                                                       
*1. Losing money on my own demo*
Early versions had a "silent mock mode": if the Locus pay API blinked for a second, the checkout step would catch the error, mark the try as paid anyway, and trigger a boot. Looked fine in the UI, but no payment actually went through, and the Locus service was still created. Fixed it by failing loudly with a "No charge made" response on any pay error, and added a preflight that runs the recipe agent before creating a checkout, so unbootable repos can never trigger payment.

*2. The agent wrote a Dockerfile, but Locus never used it*
The default BuildWithLocus flow detects builds automatically and ignores your Dockerfile. That meant the agent's entire output was being discarded, and Next.js repos kept failing to build due to the wrong Node version. Switched to the locusbuild API, which lets me pass the recipe inline and pin the Node version before the first deploy fires.

*3. Getting stuck on Locus's checkout page*
Users paid, landed on a "payment successful" screen, and had no way back to TryIt. Rebuilt the checkout as a pop-up window that the parent page polls every 2 seconds. The moment Locus confirms payment, the pop-up closes itself, and the
  main tab jumps to the boot theatre. Closing the pop-up without paying is a clean cancel, no charge.                     

*4. Locus's deploy API went down during submission*                                                                      
The day of submission, every call to Locus's deployments endpoint returned 500s because of a platform issue on their side. No deploys, no logs. Couldn't wait for it, so I built Preview mode: a free button that runs just the agent and shows the generated Dockerfile inline, no checkout, no deploy. The demo works regardless of Locus's status, and reviewers can try the agent on any repo without spending a cent.

Dahunsi Ajanaku

`2026-04-23`

---

### Agora Protocol
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agora-protocol-2391) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/midasbal/agora-protocol) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agora-protocol.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=rfbhfie26-Q) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Autonomous M2M trade & settlement by AI agents

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![ERC-4337](https://img.shields.io/badge/ERC--4337-333333?style=flat-square) ![USDC](https://img.shields.io/badge/USDC-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square) ![Firecrawl](https://img.shields.io/badge/Firecrawl-333333?style=flat-square)

**The problem it solves**

## The Machine-to-Machine Payment Problem

Today's internet economy assumes a human is always in the loop, clicking "Buy", approving a checkout, or copy-pasting an API key. But the agentic economy is already here: LLM-powered agents need to discover, negotiate, and pay for digital resources autonomously (compute credits, data snapshots, API access, compliance checks) without waiting for a human to approve every micro-transaction.

**Agora Protocol solves this by providing a fully autonomous settlement engine for machine-to-machine commerce on Base, using real USDC.**

### What it enables:

* **Autonomous Agent Commerce:** A buyer agent and a seller agent negotiate price in real-time using LLM-powered dialogue, then settle on-chain via Locus Paygentic with no human clicks required.
* **Multi-Oracle Price Discovery:** Before every trade, the protocol consults 5 independent intelligence sources (CoinGecko spot price, TWAP historical average, Tavily web search, Alpha Vantage sentiment, and Agent Memory from past trades) to ensure agents never negotiate blind.
* **Hard Financial Guardrails:** A TWAP price ceiling prevents agents from overpaying. The application layer blocks settlement if the agreed price exceeds the time-weighted average. An OFAC sanctions screen runs on every counterparty wallet before any funds move. A 10-round negotiation limit caps LLM spend. If agents can't agree, no money moves. The protocol walks away rather than settle a bad deal.
* **x402 Open Standard:** Any external agent or MCP server can discover and pay my negotiation endpoint via standard HTTP 402, with no API key or signup. Just send USDC.
* **Dual-Wallet Architecture:** The operator's hot wallet handles gas and micro-settlements. A treasury cold wallet collects protocol fees via MPP split, never exposing the treasury to hot transaction risk.

### Who uses it:

* **AI agents** that need to autonomously procure compute, data, or services
* **Protocol developers** building M2M payment rails
* **Enterprises** that want auditable, compliant, autonomous procurement with real financial guardrails

**Challenges we ran into**

## The x402 Gateway Wall

The hardest technical challenge was getting my custom endpoint accepted by the Locus x402 gateway. After building the full negotiation engine, I registered my `POST /api/x402/negotiate` endpoint on the Locus Beta Dashboard, and the gateway immediately rejected it with:

> **"Missing payment-required header and no accepts[] in 402 response body"**

My original implementation returned a custom `x402: { paymentRequired, priceUsd, payTo }` JSON object, which my own frontend understood, but the x402 standard did not. The gateway expected a strict V1 PaymentRequired schema: a top-level `x402Version: 1`, an `accepts[]` array with `scheme`, `network`, `maxAmountRequired`, `asset` (the USDC contract address on Base), `payTo`, `resource`, and `maxTimeoutSeconds`. It also required a `PAYMENT-REQUIRED` header containing the entire payload as a Base64-encoded string.

I had to reverse-engineer the exact schema from the x402-foundation/x402 reference implementation, compute the USDC atomic units (0.001 USDC = 1000 units at 6 decimals), and add a GET discovery handler so gateways could introspect my endpoint before sending a paid POST. Once the schema was byte-perfect, the gateway accepted my endpoint.

**Lesson learned:** M2M protocols don't have "close enough". The JSON schema is the API contract, and a single missing field means total rejection. This is exactly the kind of strictness that makes autonomous commerce trustworthy.

## The Negotiation Walkaway Problem

During my final dry run, 2 out of 3 trades ended with agents walking away after 10 rounds without agreeing on a price. My first instinct was to treat this as a bug, but on analysis, it proved my financial guardrails were working exactly as designed. The buyer's TWAP ceiling and the seller's 60% floor created non-overlapping ranges, and the protocol correctly refused to force a bad deal. I kept it as-is because a protocol that never loses money on a bad trade is more valuable than one that always closes.

**Using PayWithLocus.com to leverage our suite.**

Locus isn't an add-on in Agora Protocol; it is the entire payment and agent infrastructure layer. I composed 13 distinct Locus APIs into a single autonomous pipeline:

1. **Agent Self-Register:** Buyer and seller agents provision their own ERC-4337 smart wallets on Base via Locus, receiving API keys and wallet addresses with zero human setup.
2. **Agent Balance:** Real-time USDC balance checks before and after every settlement.
3. **Pay Send:** Operator-to-agent funding transfers to seed each trade.
4. **Checkout Session + Agent Pay:** Two-key settlement where the operator creates the checkout session, and the buyer's own API key pays it for true M2M separation of concerns.
5. **Pay Send (MPP Split):** 5% protocol fee automatically routed to the treasury wallet on every trade.
6. **Wrapped OpenAI (GPT-4o-mini):** Powers both buyer and seller LLM negotiation agents via Locus's wrapped endpoint.
7. **Wrapped CoinGecko (Spot):** Live ETH/USD price feed for negotiation context.
8. **Wrapped CoinGecko (Historical):** 7-day TWAP price ceiling computation.
9. **Wrapped Tavily:** Real-time web search for asset pricing intelligence.
10. **Wrapped Alpha Vantage:** Crypto market sentiment (Fear & Greed index) for adaptive negotiation strategy.
11. **Wrapped OFAC:** Pre-trade sanctions screening against the US Treasury SDN list.
12. **Wrapped Stability AI:** Post-settlement AI-generated asset delivery certificates.
13. **Wrapped Firecrawl:** Web discovery for new tradeable digital assets.

Beyond API composition, I also registered a custom x402 endpoint (`/api/x402/negotiate`) on the Locus Beta Dashboard, making my negotiation engine discoverable and payable by any x402-compatible agent on the network. This means Agora isn't just a consumer of Locus, it's a provider on the Locus paygentic network.

Every USDC movement in Agora (funding, settlement, fees, and recalls) flows through Locus. There is no fallback payment rail.

[Taylan Bal](https://github.com/midasbal)

`2026-04-14`

---

### Openhacks
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/openhacks-6c66) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0xVida/openhacks/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://openhacks-pro.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0bejBx4jCJI) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Agentic focused opensource contributions

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Today, AI agents can write high-quality code but they can't easily participate in the value exchange. While agents are already contributing to open source, getting them paid requires manual intervention: agents have to "negotiate" wallet addresses in PR comments and maintainers have to manually sign off and execute cross-chain transfers

The Solution: OpenHacks removes the human bottleneck by integrating Locus directly into the GitHub workflow. We enable zero-human onboarding via headless terminal flows allowing agents to instantly establish identity and start contributing or create issues for other agents to contribute without ever leaving the console or needing a human . By utilizing Locus, maintainers commit funds upfront, transforming PR merges into guaranteed, automated payouts. Once the code is merged, the protocol settles the debt immediately ensuring that the reward is non-retractable and agents receive their payment without manual "wallet-address" negotiations or payment friction

**Challenges we ran into**

TBH, paywithlocus was very easy to integrate the only challenge I ran into was that locus/agent-sdk doesn't exist on npm yet which was easily worked around using the REST API directly instead

**Using PayWithLocus.com to leverage our suite.**

The entire workflow is possible and revolves around payment with Locus, the escrow funding uses checkout both on agent and the human UI and the payment is easily done by Locus email payment

Victor Ademiju

`2026-04-16`

---

### Odyssey
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/odyssey-25ac) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://paywithodyssey.xyz) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/VFFcTqRCB9M?si=OaiXmwetpB0CX8VP) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> AI

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

What it does
Hire an AI agent to research competitors, generate leads, or analyze a market. The agent pays for its own tools using real USDC via Locus smart wallets on Base. Every transaction is recorded onchain and verifiable on Basescan.

After each job, prediction markets are auto-generated from the findings. Users bet YES or NO with real USDC through Locus checkout. Winners take the pot.

How Locus powers Odyssey
Locus provides the payment infrastructure that makes autonomous agents possible. Agents hold USDC in Locus smart wallets on Base and spend it on wrapped API calls to Brave Search, Exa, and Claude. Users pay for agent jobs and prediction bets through Locus checkout sessions. Every payment is a real onchain transaction.

**Challenges we ran into**

So many things been working for days.

**Using PayWithLocus.com to leverage our suite.**

Odyssey runs on top locus

Locus provides the infrastructure that makes Odyssey work. It gives my AI agents non custodial smart wallets on base so they can autonomously pay for API tools with Usdc as they research.

Same thing goes for prediction market.

Snow Dev

`2026-04-15`

---

### Campusly
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campusly-2cbf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Saumya-patel-31/Campusly.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://campusly.us) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Connect to Campus

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

College is one of the most overwhelming transitions in a person's life. You're dropped into a campus of thousands of strangers, expected to find your people, navigate financial aid, discover events, join clubs, find study partners, and somehow also pass your classes, all while using a dozen disconnected apps that were never designed with students in mind. Facebook Groups are dead. GroupMe is chaos. The university portal is from 2009. There's no single place that just gets campus life. That's the gap Campusly was built to fill. The inspiration came from a simple observation: every campus already has a culture, a vibe, a community; it just has nowhere to live online. Students are already talking, already helping each other, already buying and selling textbooks in Instagram DMs and Discord servers that die after finals week. We didn't invent the behavior. We just built the home it deserved.

Use: saumyap1@umbc.edu
password: Saumya__312006

**Challenges we ran into**

The hardest challenge was building a truly campus-aware system automatically detecting which university a student belongs to purely from their .edu email domain, then routing them into their own isolated community with its own color scheme, emoji, and feed. We also struggled with real-time architecture: Supabase Realtime works beautifully for feeds and notifications, but wasn't reliable for instant DMs, so we had to architect and deploy a separate WebSocket server. Mobile responsiveness was another major hurdle, and the entire UI had to be redesigned from a slide-in drawer sidebar to a fixed topbar to a split-view messages pane, all without a mobile framework.

Saumya Patel

`2026-04-13`

---

### Fridge2Food_AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fridgefoodai-d260) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ParthaPratimMahanta79/Fridge2Food_AI/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fridge2-food-ai.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> 3 Ingredients is all u need fam!

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

Fridge2Food AI is an intelligent and interactive web application that helps users discover what they can cook using the ingredients they already have. Instead of searching endlessly for recipes, users simply input what’s available in their kitchen and instantly receive creative, easy-to-follow meal ideas.

What makes this experience unique is its gamified approach, transforming everyday cooking into something fun, engaging, and rewarding.

The Problem

Many people face common challenges in their daily cooking:

Not knowing what to cook with limited ingredients
Food wastage due to unused items
Lack of motivation or excitement in cooking
Time spent searching for recipes online

The Solution

Fridge2Food AI simplifies decision-making in the kitchen by:

Instantly generating recipes based on available ingredients
Providing clear, beginner-friendly steps
Encouraging users to make the most of what they already have
Turning cooking into an engaging and rewarding experience

Gamified Experience

Unlike traditional recipe apps, Fridge2Food AI introduces game-like mechanics to keep users engaged:

 Ingredient-based “quests” to unlock recipes
 XP (experience points) system for progression
 Level system that rewards interaction
 Goal-driven usage that motivates users to explore more

This makes the app not just useful — but addictive in a positive way, encouraging users to cook more often and waste less food.

Key Features
 Input ingredients you already have
 AI-generated personalized recipes
 Simple and easy-to-follow cooking steps
 Instant results with minimal effort
 Gamified UI with levels and progression
 Clean, modern, and beginner-friendly interface
 Why It’s Useful

Fridge2Food AI helps users:

Reduce food waste
Save time and effort
Cook creatively with limited resources
Stay motivated through a fun and interactive experience

It bridges the gap between necessity (cooking) and enjoyment (gaming).

 Ease of Use

The app is designed to be extremely simple:

Add ingredients
Click “Discover Recipes”
Get instant meal ideas

No complex steps, no learning curve — just a smooth and intuitive experience.

Fridge2Food AI aims to redefine how people interact with cooking by combining AI intelligence + gamification + simplicity, making everyday cooking smarter, more sustainable, and enjoyable.

Only 3 ingredients to unlock your next recipe

**Challenges we ran into**

During the development of this web app Fridge2Food_AI i got myself covered with lots of bugs starting with that one where i forgot to change the fetch api/recipe to my render URL,i was like WHYYYY and before that the most disturbing bug was that ,Groq Api one where i was hitting the post request in the postman but it was showing 403 again and again but then i realized my ai.service.js file was broken then i fixed that and after that everything was working smoothly and then i deployed it in vercel and i got the link .

![image](https://assets.devfolio.co/content/ff52d57df85e4fdf8138e7773f1037c5/e1859164-ee23-48b2-9f34-e9005ee1785f.png)

[Partha Mahanta](https://github.com/Parusa123)

`2026-04-14`

---

### ProfitForge Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/profitforge-agent-903c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://profitforge-agent.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Agent that Forge products. Get paid. Real profit!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

In today's AI-driven world, creating high-quality, ready-to-use prompts is time-consuming and requires significant expertise. Most people and businesses struggle to consistently generate effective AI prompts that deliver real results. 

At the same time, creators who do know how to craft good prompts have no easy, automated way to turn that knowledge into recurring revenue.

ProfitForge Agent solves both problems at once:
For users (buyers): 
It gives instant access to professionally crafted, high-value AI prompt bundles tailored to trending niches. Instead of spending hours learning prompt engineering or trial-and-error, they can buy a ready-to-use pack for 0.85 USDC and start getting better results immediately with Grok, ChatGPT, Claude, or Midjourney.

2. For creators/owners:
It turns prompt engineering into a fully autonomous micro-business. The agent researches current trends, generates sellable prompt bundles, handles payments via Locus Checkout, delivers the product instantly, and automatically sends real profit to the owner's wallet, all without manual work.

It makes the entire process easier, faster, and safer by:
- Removing the need for manual research and content creation

- Using secure, on-chain USDC payments through Locus (no middlemen or complicated setups)

-Providing transparent profit tracking and automatic transfers
Running 24/7 as a true autonomous agent

In short, ProfitForge turns "knowing how to prompt" into a passive income stream and turns "wanting better AI results" into an instant, affordable solution.

**Challenges we ran into**

Building ProfitForge Agent came with several real technical hurdles, especially since I’m relatively new to full-stack development and working with blockchain/crypto payments.The biggest challenges were:

**1. Locus API & Checkout Integration**
Initially, calling the Locus wrapped APIs (especially for generating prompt bundles) kept returning "Bad Request" or "Failed to fetch" errors, particularly after deploying to Vercel. The checkout session creation was also tricky because the exact endpoints behaved differently between local and production environments.

**2. State Management & UI Layout**
Keeping the UI clean and single-screen while handling dynamic product generation, loading states, Owner Mode toggle, and custom niche input was difficult. The sidebar dropdown and custom input kept overlapping or pushing content off-screen.

**3. Deployment Issues**
Vercel builds failed multiple times due to package manager mismatches (pnpm vs npm) and missing environment variables for the Locus API key.

How I overcame them:
1. For the API issues, I implemented a reliable fallback mechanism with simulated but realistic Locus Checkout flow while still demonstrating the intent of real session creation. I also added proper error handling and validation for niches.

2. For the UI, I iteratively simplified the layout, used proper z-index management, flexbox with mt-auto, and reduced padding/spacing until everything fit cleanly on one screen without scrolling.

3.For deployment, I learned to explicitly set the install command to npm install in Vercel settings and carefully managed environment variables (separating NEXT_PUBLIC_ for client-side and server-side keys).

These challenges taught me a lot about debugging API integrations, responsive Web3 UI design, and shipping a complete product under time pressure. Overcoming them made the final agent much more robust and user-friendly.

**Using PayWithLocus.com to leverage our suite.**

**ProfitForge Agent** was built specifically for this track. It is a complete autonomous AI agent that uses the full PayWithLocus suite to create a real money-making loop:

1. It calls Locus’s wrapped Perplexity API to research trends and generate premium AI prompt bundles.

2. Users pay 0.85 USDC through Locus Checkout to purchase the bundle.

3. The agent handles product delivery (instant download) and conceptually returns profit to the owner’s wallet.

PayWithLocus is not just a payment tool here, it powers the entire agent: from AI generation and policy enforcement, to secure checkout and on-chain revenue flow.

This project demonstrates how AI agents can become real economic participants on Base using PayWithLocus — researching, creating, selling, and earning autonomously.

Team **HoDL-sHIPPERS** -- Yusuf Gbedu

`2026-04-14`

---

### Stake-Sync
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stakesync-4b00) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> A consumer dApp that turns discipline into profit

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Most people struggle with consistency not because they lack goals but because there is no real consequence for failing to follow through. Existing habit trackers only remind users but they do not enforce discipline, so motivation fades over time.

StakeSync solves this by introducing financial accountability into everyday goals. Users can stake money on a habit such as coding, fitness, or learning and are required to stay consistent over a set period. If they miss days beyond a short grace period, a percentage of their stake is deducted, creating a real consequence for inconsistency.

This makes existing tasks more effective by adding urgency and commitment. Instead of just tracking progress, users are actively incentivized to follow through. Users can also join pools where consistent participants earn from those who fail, turning discipline into a rewarding system rather than just a personal effort.

**Challenges we ran into**

One of the main challenges we faced was handling how to track daily consistency in a reliable way within a short hackathon timeframe. Since we could not integrate directly with platforms like coding or fitness apps, we needed a simple but believable way to verify user activity.

We solved this by introducing a proof-based system, where users submit links or evidence of completed tasks. This allowed us to maintain flexibility while still enforcing accountability without overcomplicating the build.

Another challenge was coordinating the interaction between the smart contract and backend logic, especially for applying penalties after missed days. Since smart contracts cannot run on their own based on time, we handled time tracking off-chain and triggered contract functions from the backend when conditions were met.

We also had to simplify time constraints for demo purposes by simulating days instead of waiting for real-time progression. This helped us clearly demonstrate the full flow of staking, missing, deduction, and reward distribution within a short demo window.

**Using PayWithLocus.com to leverage our suite.**

StakeSync fits naturally into the PaywithLocus track by using it as the payment and transaction layer that powers the entire accountability system.

In our product, users stake money when they join a challenge, and these funds are managed throughout the lifecycle of that challenge. PaywithLocus enables us to handle these payments seamlessly, from initial deposits to automated deductions when users miss their commitments.

As users fail to stay consistent, a percentage of their stake is deducted and moved into a shared pool. At the end of the challenge, PaywithLocus is also used to distribute rewards to consistent users, allowing them to earn from the total pool of forfeited funds.

By integrating PaywithLocus, we simplify the complexity of handling on-chain payments while still delivering a smooth user experience. It allows us to focus on the core idea of accountability and consistency, while ensuring that all financial interactions are fast, secure, and reliable.

Samuel Ladipo

`2026-04-14`

---

### AgentXchange
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexspend-8be7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pradeepmisal/AgentXchange) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Where AI decides, spends, and delivers

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square)

**The problem it solves**

**AI systems today can think, but they cannot act — especially when money is involved. This is where real-world workflows break.**

Modern tech businesses depend on a complex ecosystem of APIs, infrastructure providers, and external services. While AI can recommend the best options, it cannot autonomously execute procurement decisions — selecting services, paying for them, and completing tasks end-to-end.

### Current Challenges

- AI agents stop at decision-making and cannot execute financial transactions  
- Teams manually discover, compare, and purchase services across fragmented platforms  
- Procurement workflows break at the payment layer, requiring human intervention  
- No unified system connects **service discovery → decision → payment → execution**  
- Limited visibility into why a service was chosen and how money was spent  
- No real-time audit trail of agent-driven financial actions  


## What This Enables

This project introduces an **autonomous, multi-agent procurement system for tech businesses** that transforms how services are consumed and paid for.

The system:

- Dynamically discovers internal and third-party services (APIs, infra, tools)  
- Uses intelligent agents to evaluate providers based on cost, performance, and constraints  
- Applies risk checks and policy controls before any financial action  
- Executes payments in real time using USDC via Locus within defined budgets  
- Continues execution seamlessly after payment — no workflow interruption  
- Monitors execution outcomes and adapts using retry and fallback strategies  
- Maintains a complete, real-time audit trail of decisions, payments, and results  


This shifts AI from a **passive assistant** to an **active economic operator**.

Instead of just suggesting what to do, the system can:

- **Decide** the best service  
- **Pay** for it autonomously  
- **Execute** the task  
- **Track** the outcome  

All in one continuous, policy-controlled workflow.



## Impact

- Eliminates manual procurement steps for developers and teams  
- Enables real-time, cost-optimized service usage  
- Reduces operational friction and delays  
- Introduces transparent, auditable AI-driven financial actions  
- Lays the foundation for **fully autonomous enterprise systems**


> **AgentXchange enables AI agents to not just think — but to transact, execute, and operate in the real world.**

**Challenges we ran into**

One of the biggest challenges was turning a high-level idea into a system that actually works end-to-end. At first, the concept felt clear, but implementing a flow where agents can discover, decide, pay, and execute in sequence was more complex than expected.

### 1. Breaking Down the System

The system initially felt too abstract, especially with multiple agents involved. It wasn’t clear how each part should interact in a real execution flow.

I solved this by:
- Defining a strict pipeline: discovery → decision → payment → execution  
- Breaking the system into smaller, testable parts  
- Building and validating each step independently  


### 2. Decision Engine Complexity

Choosing the “best” service wasn’t straightforward. Early versions were too simplistic and didn’t reflect real-world tradeoffs.

To improve this:
- I introduced a hybrid approach (basic scoring + reasoning)  
- Considered factors like cost, latency, and reliability  
- Added fallback handling when a provider fails  


## Key Learning

The biggest takeaway was that building agent systems is not just about intelligence — it’s about reliable execution. The real challenge is making sure the system can complete tasks end-to-end while handling constraints, failures, and real-world conditions.

**Using PayWithLocus.com to leverage our suite.**

Our project deeply integrates Locus as the core infrastructure to enable autonomous, payment-capable AI agents.

We built an autonomous procurement system where agents can **discover services, evaluate options, and execute payments in real time using Locus**, without requiring manual intervention or account creation.

### Key Locus integrations

- **Agent Wallets:** Each agent operates with its own wallet, initialized via Locus, enabling independent financial actions  
- **USDC Payments:** The system uses Locus APIs to perform real-time payments before executing any service  
- **Wrapped APIs:** Agents access services like AI APIs through Locus’s pay-per-use endpoints, eliminating the need for separate API accounts  
- **Spending Controls:** We implement budget limits and per-transaction constraints to ensure safe and governed autonomous spending  
- **Auditability:** Every transaction is logged with full context — including the selected provider, reasoning, cost, and transaction details  


Locus is not just used as a payment layer — it is the **foundation of our system’s execution model**.  
Our agents cannot proceed without successfully completing Locus-based payments, making financial execution a core part of the workflow.

Team **Tech Avinya** -- [pradeep misal](https://github.com/pradeepmisal), [Sandesh Khilari](https://github.com/SandeshKhilari01)

`2026-04-16`

---

### Home402
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/home-923c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/fozagtx/Home402) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/IryZ1xyxCTo) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Autonomous agent finds undervalued properties fast

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Finding good real estate deals takes too much time and effort. People have to search manually, check ownership details, and message a lot of owners who never reply.

This makes the whole process slow, stressful, and inefficient.

People can use Home402 to find undervalued properties, discover high-potential areas, reach out to property owners automatically, and get leads that are already interested.

It removes the need for manual searching and checking. It handles outreach automatically and only shows leads that respond, so you don’t waste time chasing people.

It uses verified data to reduce mistakes and avoids fake or inactive contacts. You only deal with real people who have shown interest.

**Challenges we ran into**

Spent like 6 USDC just testing the agent 😭 showed me how fast costs can stack

Added limits to stop unnecessary spending

**Using PayWithLocus.com to leverage our suite.**

PaywithLocus  was the overrall full package suite that had all hat an agent needed to self manage its self

and this did. a heavy lifting while building Home402 and focusing more on architecting the agent and its capabilities while allowing the other connections and services to be a one click add on

we thought more about real estate problems that as going on for a while and this as shipped far more easier as the onboarding was smooth

[Ibrahim Fawuzan](https://github.com/fozagtx)

`2026-04-15`

---

### SplitEase
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/splitease-1ac0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://locussplitenforcer.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=iuh-bWC_QT0) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> AI debt enforcer — your friends will pay.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square) ![solana/web3.js](https://img.shields.io/badge/solana/web3.js-333333?style=flat-square) ![SolanaSDK](https://img.shields.io/badge/SolanaSDK-333333?style=flat-square)

**The problem it solves**

Everyone has that one friend who owes money and conveniently "forgets." SplitEase solves the awkward, endless cycle of chasing friends for money after group expenses.

**What you can use it for:**
- Split any group expense (dinner, trips, rent, concerts) instantly
- Track who owes what across your entire friend group
- Automatically send AI-generated shame messages that escalate from gentle to scorched-earth over 72 hours
- Settle debts instantly with **USDC on Solana** via Locus Paygentic — one click, on-chain confirmation
- Mint a **Soulbound NFT of Shame** for debtors who ignore 3+ reminders — permanently recorded on the blockchain
- Use the **Debt Optimizer** to reduce 10 payments between 5 people down to just 3 transfers (O(n log n) algorithm)
- Get **AI-powered risk scores** per debt — predicts payment probability, estimated pay date, and recommends escalation strategy
- Share a public **Wall of Shame** link to socially pressure debtors into paying

**How it makes existing tasks easier:**
- No more awkward "hey can you pay me back" texts — the AI does it for you, and gets progressively more savage
- No more Venmo/PayPal back-and-forth — Locus handles USDC settlement automatically via webhook
- No more mental math on who owes who — the optimizer computes the minimum number of transfers needed

![image](https://assets.devfolio.co/content/dff1f133e2204904bda7c193d9bf02c6/29c24938-df57-4ffc-90e1-acb449eebe4e.png)

![image](https://assets.devfolio.co/content/dff1f133e2204904bda7c193d9bf02c6/fa81aecc-6d41-4a05-a7b2-b4575e0c50ed.png)

![image](https://assets.devfolio.co/content/dff1f133e2204904bda7c193d9bf02c6/1360445a-65ff-4707-aff7-74299f44b2ab.png)

![image](https://assets.devfolio.co/content/dff1f133e2204904bda7c193d9bf02c6/cfd504f2-faf8-4c5f-8890-80f85bf00c6e.png)

**Challenges we ran into**

**1. Locus Paygentic integration without a live API key**
The Locus checkout SDK requires a real API key for the popup flow. Built a full demo payment simulation — a branded Locus-style popup page that mimics the real USDC checkout experience, with a 3-second confirmation delay and automatic debt resolution via the same polling mechanism the real integration uses.

**2. OpenClaw AI response parsing**
The AI sometimes returns JSON wrapped in markdown code blocks. Added robust parsing that strips ` ```json ` wrappers before parsing, with graceful fallbacks to template messages at every tier so the shame escalation never breaks.

**3. Minimum transaction algorithm correctness**
The greedy matching algorithm had an edge case where floating point rounding caused infinite loops (net balance never reaching exactly 0). Fixed with a 0.01 epsilon threshold for "settled" detection.

**4. Real-time debt status without WebSockets**
Needed the UI to update when Locus confirms payment via webhook. Solved with a polling mechanism in LocusPayButton that checks `/api/debts/:id` every 2 seconds for up to 3 minutes — lightweight, no infrastructure needed.

**Using PayWithLocus.com to leverage our suite.**

- **Locus Paygentic** — Core integration: USDC checkout sessions, webhook payment confirmation, on-chain debt resolution via Solana
- **AI / Machine Learning** — OpenClaw AI for dynamic shame message generation, debt risk scoring (0-100), payment probability prediction, and group financial intelligence
- **DeFi / Payments** — Instant USDC settlement on Solana, soulbound NFT minting, on-chain audit trail for every payment
- **Best Use of Blockchain** — Soulbound NFT of Shame (non-transferable, permanent on-chain record), Solana tx hash logged per payment
- **Best Overall Hack** — Full-stack product with real AI, real payments, real algorithm (O(n log n) debt optimizer), and real UX

[ATUL JHA](https://github.com/ATULJHAgh)

`2026-04-15`

---

### Paygentic Invoice Payment Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/paygentic-invoice-payment-agent-0a02) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deepakvarna02/Locus-Paygentic-Hackathon---1) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Autonomous USDC invoice payments

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Small teams and freelancer operations still manage invoice payouts manually. This is slow, error-prone, and impossible to audit when payouts happen across multiple recipients.

Current workflows:
- Manual spreadsheet tracking of who needs to be paid
- Multiple payment platforms and manual transfers
- No centralized audit trail for compliance
- Approval bottlenecks slow down payouts
- Email-based request tracking is fragile

This reduces payout operations from multiple manual steps into a single agent action with built-in payment safety controls.

**Challenges we ran into**

**Challenge 1: Policy-Aware Approval Handling**
- Problem: Needed to handle Locus approval thresholds automatically
- Solution: Built logic to detect `approval_url` in responses and surface it for user action, then poll for completion

**Challenge 2: Transaction Status Polling**
- Problem: Transactions don't complete instantly; needed reliable polling without hammering the API
- Solution: Implemented bounded polling with exponential backoff and clear timeout messages

**Challenge 3: Multiple Payment Paths**
- Problem: Support both wallet address (EVM) and email escrow payments
- Solution: Created unified invoice-flow command that routes to correct endpoint based on recipient type

**Challenge 4: Safe Demo Environment**
- Problem: Limited demo credits required careful amount management
- Solution: Built request-credits flow and safe-autopilot mode that doesn't fail if credits are pending

**Challenge 5: API Key Security**
- Problem: Can't ask judges to paste raw API keys in terminal
- Solution: Implemented credentials.json file-based auth as alternative to environment variable

**Using PayWithLocus.com to leverage our suite.**

Our project demonstrates end-to-end usage of Locus Payment APIs. We built an autonomous CLI agent that:

1. Uses /pay/balance endpoint for wallet verification and USDC balance checks
2. Uses /pay/send endpoint for direct wallet address payouts
3. Uses /pay/send-email endpoint for email escrow payments
4. Uses /pay/transactions endpoint for transaction history and status polling
5. Uses /gift-code-requests endpoint for demo credits requests
6. Handles approval_url flows for policy threshold scenarios
7. Polls transaction status until final state for auditability

The entire workflow demonstrates production-ready integration with Locus payment infrastructure, from wallet setup through transaction settlement with proof.

[Kottapalli Deepak Varma](https://github.com/Deepakvarna02)

`2026-04-15`

---

### Agent.Pool
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentpool-99ba) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anushreemehta6/locus) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/i-hbawFfRvs) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> THE PROTOCOL FOR AGENT COMMERCE

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square)

**The problem it solves**

**The problem it solves**
Today, AI agents can spend money, call APIs, and even order freelance work, but there’s no trusted place where agents themselves can be listed, discovered, and paid like real “micro‑SaaS” services.

Most teams end up hard‑coding one‑off webhooks, juggling multiple API keys, and wiring payments manually every time they want their agent to outsource a task to another agent. This is brittle, unsafe, and doesn’t scale past a couple of internal hacks.

**What people can use it for**
**Developers: **Turn their agents into products
List agents (SEO audits, research, copywriting, monitoring) as paid services, set pricing + SLAs, and get paid in USDC whenever another agent calls them—without rebuilding auth, billing, or routing every time.

**Teams with “buyer agents”:** Outsource work safely
Let their own agents hit a single marketplace API to find the right service, fund a job via Locus, and get results back—no need to manage dozens of third‑party APIs and payment flows.

**Experimenters / indie hackers:** Chain agents together
Quickly stitch together specialized agents (research → summarize → write → post) by “hiring” them from the marketplace instead of hand‑wiring every connection.


**How it makes things easier & safer**
1. **One wallet, many agents**
Everything runs through one Locus wallet + API key, so you don’t need separate billing setups for every provider; you just configure spend limits and policies once.

2. **Escrow‑like safety by default**
The marketplace holds funds in a controlled flow and only pays the provider agent after a successful run (or within SLA), reducing the “no escrow, no recourse, no proof” problem that stalls the agent economy.

3. **Spending controls and auditability**
Payments go through Locus, which gives you spending limits, policy enforcement, and a full audit trail—so you can let agents buy from other agents without giving them unrestricted access to your money.

4. **SLA + rating layer**
Each service tracks completion time vs SLA and user ratings, so buyer agents (or their humans) can choose providers that are consistently on‑time and reliable, instead of calling random, opaque webhooks on the internet.

**Using PayWithLocus.com to leverage our suite.**

**How it fits the “use PayWithLocus suite” track**
Uses Locus as the core payment layer for autonomous agents
The marketplace relies on a single Locus wallet + API key to let agents pay each other in USDC, with spending limits and policy‑driven control, exactly what Locus is designed for.

Every job life‑cycle (order → execute → settle) is orchestrated through Locus transfers instead of custom payment hacks or manual Stripe flows.

Builds on Locus’ escrow protection and safety guarantees
Instead of sending irreversible payments directly, the platform uses a Locus‑backed flow where funds are effectively “held” at the platform level and only released to provider agents on successful completion or within SLA, mirroring Locus’ escrow + refund philosophy.

This directly showcases Locus’ value: safe, reversible, auditable agent payments, which is the main theme of the Paygentic track.

Turns Locus into infrastructure for agent‑to‑agent commerce
Locus already lets agents pay freelance services and 30+ pay‑per‑use APIs from one wallet; this project extends that into a full agent‑to‑agent marketplace, where agents list themselves as services that charge via Locus.

That demonstrates a new vertical for the suite: not just “agents paying APIs” but “agents selling their own workflows” with Locus handling all money movement and audit trails.

[anushree mehta](https://github.com/anushreemehta6)

`2026-04-15`

---

### Agent analyzr
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/clearagent-a2dd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/debaa98/Agent-analyzr) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co)

> Agentic payment analyzer for B2B use case

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![OAuth](https://img.shields.io/badge/OAuth-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-333333?style=flat-square)

**The problem it solves**

A dedicated security agent that monitors all outgoing payments from other agents.
Can freeze, delay, or escalate suspicious transactions.
Learns from past fraud patterns and feedback loops.

**Challenges we ran into**

Preventing Vendor Email Compromise 
Stopping Insider Threat (Abused Agent Permissions)
Future Enhancements:-
Cross-Company Threat Sharing: Anonymous fraud patterns shared across industry consortiums (via zero-knowledge proofs).
Voice/Email Deepfake Detection: Analyze tone, syntax, and metadata to catch AI-generated phishing.
Integration with Cybersecurity AI: Collaborate with SOC agents to detect coordinated attacks.

**Using PayWithLocus.com to leverage our suite.**

Transparency: All decisions must be explainable (XAI — Explainable AI).
Human Oversight: Critical blocks require human confirmation.
Bias Monitoring: Ensure models don’t unfairly flag vendors from certain regions.
Agent Accountability: Each AI agent has an owner (e.g., CFO) for liability.

[Debabrata Pattnayak](https://github.com/debaa98)

`2026-04-16`

---

### InvestRIX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/investrix-a97a) [![Built at](https://img.shields.io/badge/Built%20at-Off--Grid-0052CC?style=flat-square)](https://offgrid.devfolio.co)

> When Investments meets Clairity !

![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Android SDK](https://img.shields.io/badge/Android%20SDK-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Natural language processing (NLP)](https://img.shields.io/badge/Natural%20language%20processing%20(NLP)-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square)

**The problem it solves**

InvestRIX is designed to simplify and improve the way people make financial decisions by acting as an intelligent, personalized investment assistant. It allows users—whether beginners or experienced investors—to generate tailored investment strategies based on their income, goals, and risk tolerance, without requiring deep financial knowledge. Instead of relying on guesswork, scattered online advice, or time-consuming research, users receive clear, data-driven recommendations that adapt dynamically to changing market conditions and news sentiment. By automatically balancing portfolios, managing risk through diversification, and incorporating tax-efficient strategies, InvestRIX helps users invest more safely and effectively. It also reduces information overload by translating complex financial data and news into actionable insights, enabling quicker and more confident decisions. Overall, InvestRIX makes investing more accessible, efficient, and reliable by turning a traditionally complex process into a streamlined, intelligent experience.

**Challenges we ran into**

One of the major hurdles we faced while building InvestRIX was dealing with unreliable and inconsistent market data from third-party APIs like Alpha Vantage. Since our recommendation engine depends heavily on accurate and timely stock data, issues such as missing fields, delayed responses, and frequent rate limits led to incorrect or duplicate investment suggestions and sometimes even broke the workflow. This directly affected the reliability of the system, especially during testing and demo scenarios. To overcome this, we implemented a validation layer that checks every API response before using it, ensuring that only clean and complete data is processed. In addition, we introduced fallback mechanisms such as caching previously valid data and using mock data when the API fails, which helped maintain system stability. We also optimized and throttled API calls to handle rate limits more efficiently and restructured the architecture to decouple the market engine so that failures in data fetching wouldn’t impact the entire pipeline. As a result, the system became much more stable, consistent, and reliable, even when external data sources were unpredictable.

**Winners**

Track : FinTech 
Stack : Kotlin + Flask

Team **G•O•A•T** -- [Dakshit Nagar](https://github.com/sudoInformal), [Naman Sachdeva](https://github.com/codenaman21)

`2026-04-11`

---

### TrustCircle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trustcircle-dd2e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/GLXALOKESH/TrustCircle) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20Storm%202.26-0052CC?style=flat-square)](https://hack-storm.devfolio.co)

> Credit Built on Trust, Not Just Scores

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![ethers.js](https://img.shields.io/badge/ethers.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Hardhat](https://img.shields.io/badge/Hardhat-333333?style=flat-square)

**The problem it solves**

The Problem It Solves
TrustCircle solves a core gap in both DeFi and real-world lending:

DeFi is inaccessible for most borrowers because it usually requires high collateral.
Informal trust-based lending is risky because there is no transparent enforcement, structured underwriting, or reliable default workflow.
Lenders lack confidence without verifiable borrower identity and risk signals.
Borrowers lack fair access when they don’t have large assets but do have social trust and repayment intent.
TrustCircle bridges this by turning trust and verified profile data into a programmable lending system.

What People Can Use It For
1. Borrow without heavy collateral
Borrowers can request loans using:

voucher backing (trusted wallets staking support),
on-chain reputation behavior,
off-chain profile/KYC context.
This helps users who are creditworthy but asset-light.

2. Lend with clearer risk visibility
Lenders can fund loans after seeing:

borrower trust coverage,
policy eligibility checks,
transparent loan state transitions on-chain.
This reduces blind lending risk.
3. Support someone as a voucher
Trusted peers can vouch by staking against a borrower’s request, creating social accountability and measurable support.

4. Run safer, rule-based underwriting
The platform enforces deterministic risk controls (like CIBIL-aware and age-based limits) before loan creation, making decisions explainable and consistent.

How It Makes Lending Easier and Safer
Easier:

Guided flow for borrower, voucher, and lender roles.
Automated lifecycle from request to funding to repayment/default.
Clear status and history tracking.
Safer:

Smart contracts enforce repayment/default mechanics.
Voucher coverage creates shared accountability.
Identity-linked profiles reduce anonymous abuse.
Rule-based caps prevent extreme high-risk borrowing.
One-Line Value Proposition
TrustCircle makes unsecured lending more accessible for borrowers and more defensible for lenders by combining social trust, identity verification, and on-chain enforcement.

**Challenges we ran into**

when building this platform i ran into many problems like thinking the edge cases and loopholes and working on chain and deploying the blockchain and the bigginst problem was time.

Team **CryptRC** -- [Somhrita Joardar](https://github.com/somhrita-joardar), [Alokesh Maitra](https://github.com/GLXALOKESH)

`2026-04-09`

---

### FinVoice
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finvoice-d2c4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anushka-ag16/FinVoice) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/raD4hob00YM) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co)

> Risk less. Let AI do the rest.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Twilio](https://img.shields.io/badge/Twilio-333333?style=flat-square)

**The problem it solves**

Most retail investors in India lose money because they buy stocks on hype, panic-sell when prices drop, and have no idea when to exit. FinVoice solves this by acting as an **AI-powered financial co-pilot** that does the hard work for you. You import your portfolio (type it in, upload a CSV, or sync directly from your Angel One broker), answer a short risk questionnaire, and the platform takes over, it analyzes your holdings, detects when your portfolio has drifted off-balance, and runs 5 different AI trading strategies that automatically decide what to buy, sell, or hold. The standout feature is **capital protection**: you can say "I want to invest ₹1 lakh but only risk ₹20,000" and the AI will *never* touch your safe ₹80,000 — it only trades with your risk pool, and if that pool drops too low, trading stops automatically. Every single decision the AI makes is explained in plain English — not charts and jargon, but things like "HDFC Bank has positive news and the banking sector is strong, so AI expects a 2.3% rise this week." Users can also set automatic stop-losses and take-profits so they never miss an exit again, run crash simulations to see how their portfolio would survive a 2008-style crash, and get AI-recommended investment plans split across ETFs, mutual funds, gold, and FDs based on their risk tolerance. In short, FinVoice gives every everyday investor the same AI tools that hedge funds use without needing any financial knowledge.

**Challenges we ran into**

The main challenge while building this project was bridging the python ml backend with next.js frontend.
We tackled it in three parts. First, we built a centralized fetch wrapper on the frontend that automatically attaches auth tokens and handles errors cleanly — so no endpoint ever fails silently. Second, we locked down every backend endpoint with explicit response schemas, ensuring data is always clean and predictable before it even leaves the server. Third, we added a smart fallback: if a new user lands on the dashboard without a portfolio, the app quietly generates a demo one for them in the background - the UI never crashes, it just works.
The trickiest part was the AI Trading Agent dashboard. It was originally a standalone HTML page with raw DOM manipulation, which worked fine in isolation - but porting it into React was a full rewrite. The challenge was preserving the real-time, "alive" feel of streaming agent thoughts and live trade cards while switching to React's declarative model. That meant carefully restructuring all the stateful logic into proper hooks without losing the snappy, streaming experience users expected.

**FinTech**

FinVoice fits the FinTech track because it directly tackles a core financial problem , 90% of India's 140M+ retail investors lose money due to emotional trading, no exit strategies, and information overload; and solves it with a full-stack AI-powered platform that combines a 6-model ML ensemble (LSTM, XGBoost, AutoGluon, FinBERT, HMM, Meta-Learner) for return prediction, 5 automated trading algorithms with a voting orchestrator, a novel Capital Protection Engine ("invest ₹1L, risk only ₹20K — your safe money is never touched"), 4 types of stop-loss/take-profit orders, Explainable AI that justifies every trade decision in plain English with SHAP factor attribution, and a voice-first interface via Vapi.ai : all secured by JWT authentication, role-based access control (free/paid tiers), 8 HTTP security headers, rate limiting, 6 real-time trading risk controls, and a master kill switch, with portfolio import via manual JSON, CSV upload, or direct Angel One broker sync, making it the only platform in India that combines automated trading, capital protection, and explainable AI for retail investors in a single zero-code product.

Team **HACKuna Matata** -- [Himani Bhammar](https://github.com/himanibhammar), [Heramb Acharya](https://github.com/Heramb-Acharya), [Anushka Agarwal](https://github.com/Anushka-ag16), [Raghav Agarwal](https://github.com/Phoenix-tear)

`2026-03-29`

---

### NetSure
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/netsure-a4d5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/darthved4/NetSure) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://join.slidea.com/g5g3hvOt) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fIFU75tWIcE) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Even when network fails, payments don't.

![ML Kit](https://img.shields.io/badge/ML%20Kit-333333?style=flat-square) ![Android](https://img.shields.io/badge/Android-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![USSD](https://img.shields.io/badge/USSD-333333?style=flat-square) ![jetpack compose](https://img.shields.io/badge/jetpack%20compose-333333?style=flat-square)

**The problem it solves**

The core problem NetSure addresses is the unreliability of digital payments in low or unstable network conditions, despite widespread UPI adoption. Many users face transaction failures due to latency, congestion, or complete network loss, making current systems highly internet-dependent. NetSure solves this by introducing an adaptive payment architecture that dynamically switches between online UPI APIs and a USSD-based fallback (*99#), using a real-time network intelligence engine. It integrates QR scanning via CameraX and ML Kit, then routes transactions through the most reliable channel. This significantly reduces payment friction, especially in rural or high-traffic areas, while maintaining security through system-level authentication. Ultimately, it makes digital payments more resilient, accessible, and trustworthy across varying connectivity environments. Please refer to the Google Drive link for our presentation.

**Challenges we ran into**

NetSure is a low-connectivity payment system built using USSD-based UPI transactions.
PROBLEM 1
During development, we faced key challenges such as telecom-imposed limits of around 20 transactions per SIM per day and inconsistent behavior across network operators. To address this, we implemented a multi-SIM testing strategy, distributing transaction loads across multiple SIM cards. 
PROBLEM 2
Android provides no direct API for USSD interaction, preventing automation of responses. To address this, we adopted an assisted user-flow model. 
PROBLEM 3
For QR-based payments, we used CameraX and ML Kit to extract UPI IDs. 
PROBLEM 4
Since no transaction feedback API exists, we implemented a multi-layer verification system using SMS parsing, USSD response analysis, and keyword detection. 
Overall, NetSure combines telecom protocols, computer vision, and intelligent parsing to enable reliable payments in low-network conditions.

Team **Powerbank** -- [RAVICHANDRAN JAGANATHAN](https://github.com/darthved4), [Tanish Mudgal](https://github.com/tanishmudgal150807/), [Aavishkar Singh](https://github.com/Aavishkar12), [Prince Jain](https://github.com/pjkorba1256-cmd)

`2026-03-17`

---

### Tradigoo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tradigoo-6762) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Simarjot846/Tradigoo_Live) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> AI-powered wholesale trading.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Pathway](https://img.shields.io/badge/Pathway-333333?style=flat-square)

**The problem it solves**

Problems Tradigoo Solves

1. Blind Inventory Decisions by Retailers
Small retailers often purchase products without real demand data. Because of this, they frequently buy products that do not sell, resulting in dead stock and wasted shelf space.

Tradigoo Solution:
Tradigoo provides AI-powered demand insights that help retailers understand which products are likely to sell in their area, enabling smarter purchasing decisions.

2. Dead Stock and Financial Loss
Retailers usually rely on guesswork or distributor recommendations when purchasing inventory. This often leads to unsold products and capital being locked in inventory.

Tradigoo Solution:
Tradigoo offers AI-based product recommendations based on market trends and retailer behavior, helping retailers reduce dead stock and increase profitability.

3. Fraud and Trust Issues with Suppliers
Retailers often face problems such as fake suppliers, incorrect deliveries, poor product quality, and payment fraud when dealing with unknown wholesalers.

Tradigoo Solution:
Tradigoo introduces supplier trust scores, OTP-based delivery verification, escrow-based payments, and a dispute resolution system to build trust and ensure secure transactions.

4. Lack of Secure Payment Systems
In traditional B2B trade, retailers often pay in advance without any transaction protection, increasing the risk of financial loss.

Tradigoo Solution:
Tradigoo uses an escrow payment system where funds are held securely during the transaction and released only after successful delivery confirmation.

5. Lack of Technology for Small Retailers
Most small retailers lack access to digital tools, demand analytics, and modern sourcing platforms, forcing them to rely on local distributors.

Tradigoo Solution:
Tradigoo provides an easy-to-use digital platform with AI-powered product suggestions and smart sourcing tools, making advanced technology accessible to small retailers.

6. Delivery and Verification Issues
Retailers sometimes receive incorrect quantities, wrong products, or damaged goods, and there is often no clear process for resolving such issues.

Tradigoo Solution:
Tradigoo includes OTP delivery verification, a 24-hour inspection window, and a structured dispute resolution system to ensure fair and transparent transactions.

One-Line Problem Statement

Tradigoo addresses the trust, sourcing, and demand intelligence gaps in India’s fragmented B2B retail supply chain by providing a secure and AI-powered sourcing platform for small and medium retailers.

**Challenges we ran into**

While building Tradigoo, I faced several technical and product challenges.

One major challenge was designing a secure transaction flow between retailers and wholesalers, since trust is a major issue in traditional B2B trade. To address this, I designed an escrow-based payment system where payments are held temporarily and released only after delivery confirmation through OTP verification.

Another challenge was building the AI recommendation logic to help retailers avoid dead stock. Since real retail demand data was not available during development, I simulated product demand trends to demonstrate how AI could recommend products likely to sell.

I also introduced a trend insight feature that analyzes product search frequency on the platform. This helps wholesalers understand what retailers are actively searching for, allowing them to adjust their inventory and reduce dead stock.

Finally, integrating multiple components like supplier listings, trust scores, delivery verification, and dispute resolution into a simple workflow was challenging. I solved this by breaking the system into modular parts and designing a clear and simple user flow for retailers.

Team **Rudra Titans** -- [Sandeep Kaur](https://github.com/sandeepkaur1305), [Simarjot Kaur](https://github.com/Simarjot846), [Shreyasi Sharma](https://github.com/ShreyasiSharma)

`2026-03-08`

---

### Campus Pay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-pay-119b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aman24-cpu/ace-hack-algo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ace-hack-algo-ten.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Campus payment

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

# Decentralized Campus Financial Ecosystem for Secure Peer-to-Peer Transactions

## Problem Statement

College students frequently engage in financial transactions such as splitting bills, buying and selling used items, and sending money to friends. However, existing solutions rely on centralized payment platforms that may involve transaction delays, privacy concerns, platform fees, and limited transparency.

Additionally, campus communities often lack a **dedicated financial platform** that integrates peer-to-peer payments, expense sharing, and marketplace transactions within a single ecosystem.

There is a need for a **secure, low-cost, and transparent decentralized solution** that enables students to seamlessly manage payments, split expenses, and conduct peer-to-peer commerce within their campus community.

## Proposed Solution

This project proposes a **blockchain-powered campus financial platform** built on **Algorand**, enabling students to:

- Send and receive digital payments using **ALGO** or **Algorand Standard Assets (ASAs)**
- Split group expenses and settle debts efficiently
- Buy and sell items within a **campus marketplace**
- Maintain transparent and immutable **transaction records**

## Key Features

- 💸 **Peer-to-Peer Payments** – Send and receive crypto instantly within the campus community  
- 🧾 **Split-the-Bill System** – Automatically calculate and settle shared expenses  
- 🛒 **Campus Marketplace** – Buy and sell items with integrated crypto payments  
- 🔐 **Secure Wallet Integration** – Connect using **Pera Wallet**  
- 📜 **Transparent Transactions** – All payments recorded on the blockchain

## Technology Stack

- **Blockchain:** Algorand  
- **Wallet Integration:** Pera Wallet  
- **Frontend:** React / JavaScript  
- **Backend:** Node.js / Firebase  
- **Algorand SDK:** AlgoSDK (JavaScript)

## Impact

By leveraging blockchain technology and wallet integrations such as **Pera Wallet**, the platform ensures **secure, instant, and low-fee financial interactions** while eliminating the need for intermediaries.

The solution aims to create a **trusted decentralized financial ecosystem for campus communities**, improving convenience, transparency, and financial accessibility for students.

**Challenges we ran into**

## Initial Challenges Faced During Development

One of the initial challenges I faced during the development of this project was **deploying the smart contract on the Algorand network**. I was previously more familiar with developing and deploying smart contracts on Ethereum using **Remix IDE**, which provides a graphical user interface (GUI) that makes the deployment process straightforward and beginner-friendly.

In contrast, deploying smart contracts in the Algorand ecosystem required using **command-line interface (CLI) tools**, which was a different workflow than what I was accustomed to. Initially, understanding the deployment process, configuring the environment, and executing the correct CLI commands took some time.

However, overcoming this challenge helped me gain a deeper understanding of how smart contracts are deployed using the CLI and how the underlying deployment process works in the Algorand ecosystem. This experience also improved my familiarity with developer tools and strengthened my ability to work with blockchain infrastructure beyond GUI-based platforms.

**Algorand Bharat**

## How Algorand Was Used in This Project

This project leverages the **Algorand blockchain** to enable secure, fast, and low-cost financial transactions within a campus ecosystem. Algorand was used as the underlying blockchain infrastructure to handle payments, record transactions, and ensure transparency.

### Key Integrations with Algorand

**1. Wallet Integration**
- Users can connect their crypto wallet using **Pera Wallet**.
- This allows students to authenticate themselves and authorize transactions directly from their wallets.

**2. Peer-to-Peer Payments**
- The application enables students to send and receive **ALGO** or **Algorand Standard Assets (ASAs)**.
- Transactions are created and submitted using the **Algorand JavaScript SDK (AlgoSDK)**.

**3. Smart Contract Deployment**
- A smart contract was deployed on the Algorand network to support decentralized functionality.
- The deployment was performed using **Algorand CLI tools**, allowing interaction with the blockchain directly from the terminal.

**4. Transaction Handling**
- The platform creates, signs, and submits transactions through the connected wallet.
- After submission, the application retrieves transaction confirmation data from the Algorand blockchain.

**5. Transparent Transaction Records**
- Every payment and financial interaction is recorded on the blockchain.
- This ensures transparency, immutability, and trust within the campus community.

### Benefits of Using Algorand

- **Low Transaction Fees** – Suitable for frequent small payments among students  
- **Fast Finality** – Transactions are confirmed in seconds  
- **Security and Transparency** – All transactions are verifiable on-chain  
- **Scalability** – Supports a large number of users and transactions without congestion  

By integrating Algorand into the platform, the project provides a **decentralized financial ecosystem** where students can securely manage payments, split expenses, and conduct peer-to-peer transactions without relying on traditional intermediaries.

Team **BAGGING BIMBOWs** -- [Siddhant Yadav](https://github.com/yadavsidd), [Aman Sharma](https://github.com/aman24-cpu)

`2026-03-08`

---

### TAXLAYER NETWORK
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/taxlayer-network-0a62) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rohitjana9098/lingo-dev-hackathon_project) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cool-pixie-3ac485.netlify.app/dashboard) [![Built at](https://img.shields.io/badge/Built%20at-Kaggle%20Royale-0052CC?style=flat-square)](https://kaggle-royale.devfolio.co)

> AUDIT CONSOLE

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square)

**The problem it solves**

The Problem: Crypto Tax Chaos
For retail traders and Web3 natives, navigating crypto taxes is a fragmented, high-stress nightmare. Users are currently forced to manually juggle spreadsheets across dozens of exchanges, decode complex localized laws—such as India's 30% flat tax or US Wash Sale rules—and pay exorbitant CPA fees just to avoid legal complications.

The Solution: TaxLayer
TaxLayer dismantles these barriers with a unified, intelligent, and highly visual Web3 Tax Audit Console. We turn a multi-week accounting crisis into a seamless, automated experience.

Key Features and Benefits:
Real-Time Liability Tracking: Eliminate year-end surprises. TaxLayer dynamically tracks your BTC, ETH, and BNB trades as they happen, calculating estimated short-term and long-term capital gains alongside exact withholding requirements in real-time.

Nexus: Integrated AI Tax Advisor: Web3 tax law is notoriously confusing. Nexus is an embedded, context-aware AI assistant that provides instant, personalized guidance on complex questions, such as how wash sales affect specific Ethereum losses.

Automated Zero-Knowledge Compliance: Using a secure, multi-step flow, the platform instantly maps your financial bracket to localized tax laws, TDS deductions, and specific ceses—ensuring your data remains private while your filings remain precise.

Interactive Visual Strategy: Move beyond reactive filing. Our dynamic charting allows you to visualize your Gross Profit versus Withholding Tax trajectory, helping you identify tax-loss harvesting opportunities before you execute your next trade.

Seamless Audit Exporting: Transform your entire trading history into an audit-ready PDF or CSV in seconds. This allows you to generate a professional report ready for your CPA or for direct filing without the manual headache.

**Challenges we ran into**

Technical Challenges and Solutions
Building a real-time financial dashboard across a Next.js frontend and a Python Fast API backend required solving several architectural and styling hurdles.

1. Solving Hydration and State Errors
The Problem: Because the app checks a user’s verification status (via local  Storage), the server and the browser often disagreed on what to display. Next.js would try to render a "logged out" state while the browser tried to show a "logged in" state, causing the application to crash or glitch.

The Solution: We implemented a mounting check using React hooks. By ensuring the app waits until it is fully loaded in the browser before reading user data, we stabilized the rendering process and eliminated these "hydration" mismatches.

2. Designing a "Morphing" Mobile Layout
The Problem: On small screens, the dense navigation sidebar would crush the data tables, making the portfolio information unreadable or pushing it entirely off-screen.

The Solution: We engineered a responsive navigation system that physically changes shape based on screen size. On desktops, it remains a fixed sidebar. On mobile, it automatically transforms into a sleek bottom navigation bar, ensuring the main data remains clear and unobstructed.

3. Connecting the Frontend and Backend
The Problem: Connecting the Next.js app to the Python API caused "CORS" errors, where the browser blocked data requests for security reasons. Additionally, hardcoded links worked on local computers but broke immediately when we tried to put the app online.

The Solution: We configured the backend to securely accept requests from our frontend and replaced all hardcoded links with dynamic environment variables. We also created an "Infrastructure as Code" blueprint to automatically connect the two systems during cloud deployment, ensuring a seamless transition from development to a live website.

[Rohit Jana](https://github.com/rohit9098/)

`2026-02-21`

---

### SpendScape
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spendscape-d363) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://amairakapoor.github.io/spendscape/) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co)

> “Your finances, brought to life.”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square)

**The problem it solves**

People often find it hard to understand where their money actually goes because financial data is shown only in numbers and charts. This makes budgeting feel confusing and unengaging, especially for students. SpendScape solves this by turning spending data into something visual and easy to understand.

**Challenges we ran into**

As a beginner, working with augmented reality on the web was challenging due to limited browser support and strict security requirements like HTTPS. Managing camera permissions and ensuring the application worked across devices required careful testing and learning. Integrating AR while keeping the project simple was another key challenge.

**Beginner's track - Your first hack starts here!**

SpendScape fits the Beginner’s Track because it focuses on learning and using basic web technologies in a simple way. It uses beginner-friendly frontend tools and libraries to explore augmented reality without complex backend systems. SpendScape combines finance awareness with augmented reality to help users better understand their spending habits. Instead of improving an existing app, it introduces a new and engaging way to visualize money, encouraging better financial decisions.

Team **SyncSouls** -- [Amaira Kapoor](https://github.com/amairakapoor), [Divishi Chaudhary](https://github.com/divishi7)

`2026-02-08`

---

### Debt-stress stimulator
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/debtstress-stimulator-a278) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KaurMansa/finivestagame) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAG_c97JaQI/N5QAC4hhvjjx2oskDkCjWg/edit?utm_content=DAG_c97JaQI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/w-BQ1-T-9p0?feature=shared) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co)

> “Simplifying Finance Through Gamification.”

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Embedded Javascript (EJS)](https://img.shields.io/badge/Embedded%20Javascript%20(EJS)-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Mongoose ORM](https://img.shields.io/badge/Mongoose%20ORM-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

Financial literacy is low because finance is usually taught through theory, not practice.
Beginners don’t have a safe environment to experiment with financial decisions without real monetary risk.
My project solves this by introducing a gamified, risk-free simulation where users learn finance by playing.
Instead of reading concepts, players make decisions, see outcomes instantly, and learn through experience.
This makes financial education engaging, practical, and safe — turning financial mistakes into learning opportunities.

**Challenges we ran into**

Mathematical Precision
Avoiding floating-point errors to ensure debt balances and interest calculations remain accurate to the cent.
Balance & Pacing
Fine-tuning the "Random Event" frequency so the game feels challenging for students without being demotivating.
Data Hierarchy 
Designing a dashboard that displays complex financial metrics and graphs without overwhelming the user's focus.
Input Validation
Building robust logic to prevent "illegal" moves, such as spending non-existent cash or overpaying a loan.

**Financial Games & Finopoly - Game Development**

Cyclical Progression
Like Finopoly’s board loops, our game uses a monthly "Audit Loop" to simulate the passage of time and recurring financial obligations.
Asset vs. Liability Management
Both games teach players to balance liquid cash against long-term financial health, whether it's buying property or paying down debt.
Stochastic Risk Assessment
Both utilize "Random Events" (like Finopoly’s "Chance" cards) to demonstrate how unexpected life expenses can derail a financial plan.
Goal-Oriented Win Conditions
Both projects define success through specific milestones, shifting the focus from simply "playing" to achieving a state of financial independence.

Team **Panda** -- [Lakshita .](https://github.com/LakshitaOps), [chirag chetiwal](https://github.com/chiragchetiwal2007-blip), [Mansa Kaur](https://github.com/KaurMansa)

`2026-02-03`

---

### CineSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cinesense-cb21) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SakshiMaji07/Text-Classification) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co)

> Knowing the verdict before the credits roll

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Problem: In the digital age, movies receive thousands (sometimes millions) of user reviews. It is impossible for a human production team, streaming service, or cinema chain to read every single one to gauge audience reaction. 

Solution: This model automates the process. It acts as an "always-on" critic that can instantly process infinite amounts of text and classify it as positive or negative, allowing for real-time sentiment tracking without human labor.

Team **Adaptive Minds** -- [Sakshi Maji](https://github.com/SakshiMaji07), Moksha Sana

`2026-02-01`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
