# Finance and Fintech

![Projects](https://img.shields.io/badge/Projects-121-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

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

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
