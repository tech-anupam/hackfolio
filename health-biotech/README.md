# Health and Biotech

![Projects](https://img.shields.io/badge/Projects-109-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

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

### medScript
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medscript-9df6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RitochitGhosh/medScript) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1175873983?fl=pl&fe=sh) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-9-FF6B6B?style=flat-square)

> Clinical documentation, reimagined for doctors

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![SHA-256 Hashes](https://img.shields.io/badge/SHA--256%20Hashes-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem

A typical doctor in India sees 40–80 patients per day in OPD. For each one, they manually write notes, recall drug dosages from memory, maintain error-prone paper prescriptions, and have no structured records for follow-ups. That's hours of paperwork daily — on top of clinical work. Junior doctors in rural and semi-urban settings have it worse: no specialists to consult, no access to clinical guidelines, and no system to flag risky cases.


---


## The Solution

**medScript** is a voice-first AI clinical assistant for outpatient doctors.

- **Doctor speaks** — records a short voice note during or after consultation
- **AI structures** — generates a complete SOAP note, ICD-10 diagnosis with confidence scores, drug prescriptions with dosage and duration, and red-flag alerts
- **Doctor reviews** — resolves AI-flagged uncertainties, approves, and finalizes in under a minute
- **Patient gets a clean record** — accessible via a 6-character privacy code, no PII exposed
- **Encrypted at rest** — AES-256-GCM; only the treating doctor and patient can access it

> Documentation per consultation drops from 8–12 minutes to under 2.

---

## Why India Specifically

- Rural doctors lack specialist access — AI diagnosis suggestions with confidence scores act as a second opinion
- Drug names shown with local Indian brand equivalents — directly actionable
- Government hospital referral search built in
- Offline-first — core workflow runs without internet; syncs when connected
- DPDP Act compliant — patient data encrypted, identified only by code

---

## Expansion

Pharmacy partnerships · Lab referral integrations · Insurance pre-authorization via structured ICD-10 output · Anonymized case library for medical education

**Challenges we ran into**

## Challenges We Ran Into

### 1. Cellular Network Killed Our Fine-Tuned Model

We trained a medical LLM on a Kaggle dataset for ~4 hours. When it came time to deploy, slow cellular data made the model endpoint unreliable and too latency-heavy for real-time consultation workflows. We pivoted to a **RAG pipeline** over a curated India-specific medical knowledge base — faster, more controllable, and easier to update without retraining.

---

### 2. Encrypting Patient Data Without Breaking Queries

Adding AES-256-GCM encryption at rest meant every sensitive field (SOAP notes, transcripts, diagnoses, prescriptions) had to change from queryable JSONB to opaque TEXT columns. The hard constraint: **HITL flags had to stay as plain JSONB** because our critical-patient SQL query uses `jsonb_array_elements()` on them. Getting encryption/decryption to sit cleanly in the data layer — invisible to the application above it — required careful separation between what must be private and what must be queryable.

---

### 3. Conditional RAG — Useful Without Always Hitting the Vector DB

The RAG pipeline only activates when the AI's diagnosis confidence falls below a threshold or when red flags are present. Implementing this conditionally required:

- Building a **retrieval gate**
- Chunking India-specific clinical guidelines into MongoDB Atlas with vector embeddings
- Wiring the vector search index correctly

Atlas requires the search index to be created manually in the UI before queries work — which cost us significant debugging time before we realized it wasn't a code issue at all.

**Healthcare**

# Why It Belongs in the Healthcare Track

MedScript AI is not a generic AI tool with a healthcare skin. It is built ground-up for a specific, acute clinical problem:

Indian primary care doctors see 30–60 patients/day. Documentation takes 15–20 minutes per patient — that's up to 10 hours of paperwork daily. MedScript AI cuts that to under 3 minutes per consultation.

---

## Core Healthcare Qualifications

| Criteria | What MedScript Does |
|---|---|
| **Clinical Accuracy** | GPT-4o-mini generates SOAP notes with per-section confidence scores; low-confidence sections are flagged and locked until a doctor manually reviews (HITL) |
| **Safety** | Drug interaction checker flags mild/moderate/severe combinations before prescription is finalized |
| **Compliance** | Doctor license numbers captured on onboarding; full audit trail of every AI suggestion, doctor edit, and approval |
| **Privacy** | PHI (SOAP notes, diagnoses, prescriptions) encrypted with AES-256-GCM; RBAC ensures only the treating doctor and their patient can access records |
| **Local Clinical Relevance** | RAG knowledge base tuned to Indian disease burden (dengue, typhoid, TB, malaria), ICD-10 codes, and Indian drug market pricing in INR |
| **Continuity of Care** | Prior consultation history automatically injected into LLM context for every new visit |

---

## How It Helps Doctors Monetarily

**Time = Money in primary care:**

- A doctor saving 8 hours/day on paperwork can see ~16 additional patients/day (at 30 min average consultation)
- At even ₹200–₹500 per consultation fee, that is ₹3,200–₹8,000 in additional daily revenue per doctor
- Over a month: ₹64,000–₹1,60,000 in incremental income — from time that was previously lost to documentation

**Beyond time savings:**

- **Better diagnosis → fewer revisits:** Differential diagnoses with red flags reduce missed diagnoses, protecting doctors from liability and reducing costly re-consultations
- **Prescription accuracy → patient trust:** Auto-enriched prescriptions with Indian brand names and INR prices reduce pharmacist confusion and improve patient adherence, which drives word-of-mouth and repeat visits
- **Critical patient flagging:** Prioritizing high-risk patients reduces emergency escalations that are expensive and reputation-damaging for a clinic

Team **Hackaut** -- [Ritochit Ghosh](https://github.com/RitochitGhosh), [Tamojit Mandal](https://github.com/TamojitMandal), [Aritra Ray](https://github.com/rayAritra)

`2026-03-22`

---

### Healix
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healix-6ce0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIRACULOUS65/Healix) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_Km0i77k7SM) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Healix: Trusted healthcare, powered smart

![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Python Flask](https://img.shields.io/badge/Python%20Flask-333333?style=flat-square) ![Prisma ORM](https://img.shields.io/badge/Prisma%20ORM-333333?style=flat-square) ![Better-auth](https://img.shields.io/badge/Better--auth-333333?style=flat-square) ![Html5-qrcode](https://img.shields.io/badge/Html5--qrcode-333333?style=flat-square) ![Next.js 16 (App Router)](https://img.shields.io/badge/Next.js%2016%20(App%20Router)-333333?style=flat-square) ![Algorand (algosdk & Pera Wallet)](https://img.shields.io/badge/Algorand%20(algosdk%20&%20Pera%20Wallet)-333333?style=flat-square)

**The problem it solves**

**Imagine walking into a hospital.** You're carrying a bulky folder stuffed with past prescriptions, fading lab reports, and scattered X-rays. The doctor has exactly 5 minutes to understand your entire medical history. Down the street, a pharmacy is dispensing medication, hoping the batch they received isn't counterfeit. 

Right now, healthcare data is a chaotic mess. It’s fragmented, easily lost, hard to trust, and dangerously over-exposed. We still treat our most critical data—our health records—like old grocery receipts.

**Enter Healix.** 

Healix isn't just another medical app; it's a **privacy-first healthcare ecosystem** that brings order, speed, and absolute trust to the entire medical journey. We are completely rewiring how medical data moves between the people who own it and the professionals who need it.

---

### 🚀 What People Can Use It For (And How We Make Life Easier & Safer)

Healix is built around a powerful **role-based architecture**, ensuring everyone gets exactly what they need—nothing more, nothing less. 

*   **🛡️ For Patients: Total Ownership & Control**
    *   **The Old Way:** You leave copies of your sensitive reports everywhere and have zero idea who is looking at them.
    *   **The Healix Way:** You are the absolute gatekeeper of your health. You upload your documents and grant explicit, file-by-file access to hospitals. Every time a hospital views your file, you get an instant notification. *Your data, your rules.*

*   **⚕️ For Doctors: AI-Powered Clarity**
    *   **The Old Way:** Skimming through 50-page raw medical files while the patient waits.
    *   **The Healix Way:** Doctors never touch raw files. Instead, our integrated AI engine instantly summarizes the patient's history. Doctors get a clean, actionable "cheat sheet" to make faster, sharper diagnoses, and then generate a secure, structured **Prescription QR Code**.

*   **🏥 For Hospitals: Frictionless & Auditable Access**
    *   **The Old Way:** Begging patients to email files or hunting down past records manually.
    *   **The Healix Way:** Hospitals search a patient ID and instantly access *only* the documents the patient has permitted. Total compliance, seamless workflow, and perfect audit trails.

*   **💊 For Pharmacies: Instant Prescription Scans**
    *   **The Old Way:** Squinting to read doctor handwriting, leading to potentially fatal dispensing errors.
    *   **The Healix Way:** The pharmacist simply scans the patient's Prescription QR code. Instantly, exact medicine details and dosage instructions populate on their screen. Fast, paperless, and 100% error-free.

*   **🔗 For Vendors & Consumers: Unbreakable Authenticity**
    *   **The Old Way:** Wondering if the expensive life-saving medicine you just bought is a dangerous counterfeit.
    *   **The Healix Way:** Vendors register medicine batches on the **Algorand Blockchain**. Every bottle gets an immutable cryptographic hash. Anyone—a pharmacist or a patient—can scan the medicine's QR code to verify its on-chain authenticity in milliseconds. *One scan, absolute truth.*

---

### ❤️ The Vibe: Why We Built This

We built Healix because we believe that navigating the healthcare system should be about healing, not doing admin work. We believe you shouldn't have to surrender your privacy to get good treatment. And we believe you should never have to second-guess the pill you are about to swallow. 

Healix elegantly bridges the gap between Web3 security, AI intelligence, and human-centric design. We are removing the friction from hospital check-ins, the guesswork from pharmacy visits, and the fear from medical data sharing. 

We aren't just building a platform; we are building a network of trust. **Welcome to healthcare, evolved.**

**Challenges we ran into**

Building Healix wasn't just about spinning up a web app; it was about orchestrating a complex, multi-layered ecosystem. We had to seamlessly connect a sleek frontend, a robust relational database, an AI microservice, and a Web3 blockchain layer—all while managing strict access controls across **five distinct user roles**. 

Here is a quick look at the architectural beast we were trying to tame:

### 🏗️ The Architecture Complexity Matrix

| Layer | Technology | Purpose | The Challenge Factor |
| :--- | :--- | :--- | :--- |
| **Frontend & Core API** | Next.js 16 (App Router) | UI, Routing, Server Actions | Managing strict state and redirection across 5 different roles. |
| **Authentication** | Better-Auth | Session management | Linking standard email auth with specific healthcare roles. |
| **Database** | Supabase (Prisma ORM) | Core relational data | Complex permissions (e.g., Hospital can only see *some* patient files). |
| **AI/ML Service** | Python (Flask + DeepFace) | Document summary & Face Match | Keeping heavy Python tasks from blocking the Next.js UI. |
| **Blockchain** | Algorand (Pera Wallet) | Medicine batch authenticity | Bridging traditional Web2 state with Web3 wallet connection states. |

With so many moving parts, things broke. A lot. Here are the major hurdles we faced and how we crushed them:

---

### 🚦 1. The Multi-Role Routing Labyrinth
**The Hurdle:** 
Healix supports 5 distinct roles (Patient, Doctor, Hospital, Pharmacy, Vendor). Initially, we handled role-based routing at the component level. This resulted in a nightmare of infinite redirection loops. A logged-in doctor would try to access the dashboard, hit a flicker of the login screen, and get bounced back out. It was completely broken.

**The Fix:** 
We scrapped component-level checks and moved everything to **Next.js Middleware**. We intercepted every single request at the edge, checked the session token, verified the user's role in the payload, and instantly rewrote the URL to the correct dashboard before the page even began to render. The flickering stopped, and our routing became bulletproof.

### 📷 2. The "Haunted" QR Scanner
**The Hurdle:** 
For the Pharmacy and Patient roles, we relied heavily on QR code scanning (using `html5-qrcode` in React). However, when a pharmacist navigated away from the scanning page, the camera hardware wouldn't release. If they tried to scan again, the app would crash with a "Camera already in use" error. The camera was essentially "haunted" by the previous component state.

**The Fix:** 
React’s strict mode and functional component lifecycles were tearing down the UI faster than the camera stream could close. We had to write a highly strict `useEffect` cleanup function that explicitly awaited the `html5QrcodeScanner.clear()` promise before allowing the component to fully unmount. We also implemented a global standard to only ever mount one scanner instance at a time across the entire DOM.

### ⛓️ 3. Web2 Meets Web3: The Wallet Disconnect
**The Hurdle:** 
To verify medicine authenticity, Vendors need to register batches on the Algorand blockchain. We integrated the Pera Wallet connect SDK. However, because Next.js aggressively triggers re-renders on state changes, the wallet connection object kept getting wiped out. Vendors would connect their wallet, click "Register Batch," and find out their wallet had silently disconnected seconds earlier.

**The Fix:** 
We had to stop treating the Web3 wallet like a local UI state. We elevated the Algorand Wallet Provider to the absolute highest level of the app (inside `layout.tsx`). By doing this, the wallet state persisted outside of the page-level rendering cycle, maintaining a rock-solid connection regardless of how many times the user navigated or submitted forms.

### 🤖 4. AI Microservice Bottlenecks
**The Hurdle:** 
We built an external Python Flask microservice to handle AI document summarization and DeepFace facial recognition. Initially, when a doctor requested a summary, the Next.js backend would wait synchronously for the Python server to finish processing the PDF. This caused Vercel serverless function timeouts (504 errors) because the AI was taking longer than the 10-second limit.

**The Fix:** 
We decoupled the heavy lifting. Instead of waiting for the AI to finish, the Next.js app now fires an asynchronous request to the Python service and immediately returns a "Processing" status to the UI. We implemented a lightweight polling mechanism on the frontend that checks back every few seconds until the summary is ready, keeping the UI snappy and entirely eliminating server timeouts.

**Web3**

Most Web3 projects try to force a blockchain into a problem that doesn't need it. **Healix does the exact opposite.** We took a globally critical, life-threatening problem—counterfeit medications and untraceable pharmaceutical supply chains—and applied Web3 technology precisely where it belongs: **Immutable Authentication & Provenance.**

Healix isn't a speculative token project; it is a **Real-World Asset (RWA) verification engine** built directly on top of the Algorand blockchain. 

Here is how Healix leverages the power of Web3 to create an unbreakable chain of trust:

### ⛓️ The Decentralized Trust Architecture

| Web3 Principle | The Real-World Epidemic | The Healix Protocol (Web3 Integrated) |
| :--- | :--- | :--- |
| **Trustless Verification** | Patients and pharmacists blindly trust the packaging of the medicine they scan. | **Zero-Knowledge Dependency**. You don't trust the Healix database; you trust the on-chain cryptographic hash. We use `algosdk` to commit batch hashes directly to Algorand. |
| **Immutable Provenance** | A counterfeit batch enters the supply chain seamlessly because centralized databases can be altered or hacked. | **Decentralized Ledger Technology (DLT)**. Vendors connect via **Pera Wallet Connect** and register their batch data. The blockchain timestamp and hash are mathematically impossible to forge or mutate. |
| **Decentralized Identifiers (DIDs)** | Vendor identities are easily spoofed in traditional web environments. | **Cryptographic Signatures**. Every batch is inextricably tied to the vendor's wallet address. Authenticity is guaranteed by cryptographic consensus, not a simple database row. |

### 🔥 The Vibe: Why This is a Masterclass in Web3 Utility

Healix stands out in the Web3 track because it bridges the gap between the blockchain and the physical world. Judges are tired of theoretical DeFi protocols—we built something that *actually touches human lives today.*

1.  **Bridging Web2 and Web3 Seamlessly:** We didn't build a clunky dApp that forces grandmas to manage seed phrases. The complex Web3 logic (Pera Wallet, smart contract hashing) is handled on the Vendor side. For the end-user (the pharmacist or patient), verifying an on-chain asset is as simple as scanning a QR code with their phone. *Frictionless Web3 adoption.*
2.  **Choosing the Right Chain:** We built on **Algorand** because healthcare demands extreme speed, micro-cent transaction fees, and absolute finality. We don't have time for network congestion when verifying life-saving drugs. 
3.  **Solving a Multi-Billion Dollar Crisis:** The counterfeit drug market is a multi-billion dollar illicit industry that costs lives. Healix uses blockchain for what it was fundamentally designed to do: eliminating trust in intermediaries and providing absolute, unforgeable truth.

We didn't just slap a wallet connection on a website. **Healix uses Web3 as the ultimate, unhackable source of truth for physical healthcare assets.** We are bringing the blockchain out of the browser and into the pharmacy. 

*This is the future of pharmaceutical provenance. This is Web3, executing at scale.*

**Open Innovation**

The Open-Innovation track exists for ideas that refuse to be put in a box. It’s for engineering that breaks boundaries and fuses entirely different technological domains to solve massive, systemic problems. 

**Healix is the definition of Open Innovation.** It fundamentally rejects the idea that a healthcare problem can only be solved with traditional HealthTech. 

We didn't build a single app; we built a **Cross-Disciplinary Digital Public Infrastructure (DPI)**. By aggressively smashing together Artificial Intelligence, Web3 Decentralized Ledgers, and advanced Web2 access controls, we forged a unified ecosystem that redefines how human trust scales.

Here is how Healix leverages absolute Open Innovation:

### 🌌 The Cross-Disciplinary Architecture

| Tech Domain | Traditional Silo | The Healix Convergence (Open Innovation) |
| :--- | :--- | :--- |
| **Artificial Intelligence** | Stuck in predictive diagnostics or isolated chatbots. | **Workflow AI.** We deployed Python-backed `DeepFace` for biometric nurse check-ins and NLP for asynchronous medical history summarization. The AI works invisibly to eliminate human friction. |
| **Web3 / Blockchain** | Confined to DeFi, NFTs, or speculative tokenomics. | **Trust as a Service (TaaS).** We utilize the absolute finality of the Algorand blockchain to create an immutable registry for physical medicine batches. Real-World Asset (RWA) verification at the scan of a QR code. |
| **Advanced Web2 Routing** | Simple CRUD apps with basic user roles. | **Zero-Trust Role-Based Access Control (RBAC).** A unified Next.js architecture where one system serves 5 totally isolated, cryptographically secure dashboards (Patient, Doctor, Pharmacy, Hospital, Vendor). |

### 🔥 The Vibe: Why This is a Masterclass in Open Innovation

Healix hits every major checkpoint a judge is looking for in an Open-Innovation winner:

1.  **The "Platform over Product" Approach:** Healix isn't a feature; it's an ecosystem. If you just build a symptom checker, you are a product. By building a network that connects **Vendors** to **Pharmacies** to **Patients** to **Doctors** to **Hospitals**, we built a platform capable of supporting the entire medical economy.
2.  **Unprecedented Tech Synergy:** We proved that you don't have to choose between Web2 UX, Web3 Security, and AI Intelligence. Healix seamlessly masks the complex Algorand wallet states and asynchronous Python deep-learning tasks behind a sleek, instant React/Tailwind frontend. The user just sees magic.
3.  **Solving the "Trust" Equation:** Open innovation is about solving problems that plague multiple industries. The core problem Healix solves isn't just healthcare; it's **Trust**. Trusting that a doctor knows your history. Trusting that a hospital won't leak your data. Trusting that a pill isn't counterfeit. We solved the Trust Equation using mathematics and code.

We built Healix because systemic problems require radical, multi-disciplinary solutions. We tore down the walls between Blockchain, Machine Learning, and traditional Software Engineering to build something entirely new. 

*Healix doesn't fit into a standard category because it is building a new one. This is what true Open Innovation looks like.*

**Algorand**

When building a mission-critical healthcare application, you cannot compromise on speed, cost, or finality. You cannot tell a pharmacist to "wait for network congestion to clear" before verifying a life-saving drug. You cannot charge a vendor $50 in gas fees just to register a batch of paracetamol. 

That is exactly why **we didn't just 'use' a blockchain; we specifically architected Healix around Algorand.**

Healix transforms Algorand from a financial ledger into an **Enterprise-Grade Verification Engine for Real-World Assets (RWAs).** We utilize Algorand’s Pure Proof-of-Stake (PPoS) network to mathematically guarantee the authenticity of pharmaceutical supply chains.

Here is how Healix leverages the raw power of the Algorand ecosystem:

### ⚡ The Algorand Architecture Advantage

| Healthcare Requirement | The L1 Bottleneck (Other Chains) | The Healix + Algorand Solution |
| :--- | :--- | :--- |
| **Instant Verification** | Network congestion and slow block times delay critical medical operations. | **Sub-3 Second Finality.** A pharmacist scans a QR code, and Algorand verifies the cryptographic medicine hash instantly. Zero wait time. Absolute certainty. |
| **Micro-Transaction Viability** | High/variable gas fees make registering individual medicine batches financially impossible. | **Algorand's Fractional Fees.** Using `algosdk`, vendors register thousands of batches directly on-chain for mere fractions of a cent, making our supply-chain model infinitely scalable. |
| **Seamless Web3 UX** | Clunky wallet integrations scare off traditional enterprise users (like pharmaceutical vendors). | **Native Pera Wallet Integration.** We embedded the Pera Wallet Connect SDK directly into our Next.js dashboard, creating a frictionless Web2 frontend for a powerful Web3 backend. |

### 🔥 The Vibe: Why This Wins the Algorand Track

Healix hits precisely what the Algorand Foundation wants to see: **Real-world adoption, massive scale potential, and native tooling.**

1.  **Solving a Multi-Billion Dollar Global Crisis:** The counterfeit drug market is lethal and massive. We aren't building a toy protocol; we are deploying Algorand to solve a literal life-or-death supply chain problem. By committing medicine hashes to the Algorand ledger, we execute trustless medicine verification at a global scale.
2.  **No Pointless Tokens:** We didn’t force a random "Health Coin" into the project just to use Web3. We used Algorand for what it was fundamentally designed to do—serving as an immutable, unhackable, high-throughput source of truth. 
3.  **Perfect Tech Synergy (Next.js + Algosdk):** We built a hyper-modern Web2 ecosystem (Next.js 16 App Router) and cleanly injected Web3 state using Algorand’s native SDKs. Vendors sign transactions via Pera Wallet in the browser, and the blockchain does the heavy lifting in the background.

We chose Algorand because when human lives and medical data are on the line, you need a blockchain that doesn't fork, doesn't crash, and doesn't cost a fortune. 

*Healix isn't just an app on Algorand; it is a testament to what Algorand can actually do for the real world.*

**Healthcare**

Healix doesn't just "fit" into the Healthcare track—it completely re-engineers the failing infrastructure beneath it. 

Most healthcare hacks focus on a single vertical: *just* an ML model for disease detection, or *just* a telemedicine UI. **Healix is different.** We didn't build a band-aid; we built a **comprehensive, end-to-end Healthcare Operating System**. We tackled the literal flow of life-saving data from the moment a patient walks into a hospital to the second they swallow a pill.

Here is exactly how Healix dominates the core pillars of modern HealthTech:

### 🧬 The "HealthTech Trifecta" 

| Core Principle | The Healthcare Problem | The Healix Solution (Buzzword Compliant) |
| :--- | :--- | :--- |
| **Data Interoperability & Privacy** | Patient records are siloed, hopelessly fragmented, and wildly vulnerable to breaches. | **Zero-Trust Role-Based Access Control (RBAC)**. Patients own their data layer. Hospitals only get explicit, heavily audited access. |
| **Clinical Decision Support (CDS)** | Doctors suffer from chronic burnout reading 50-page raw medical histories. | **AI-Native Summarization Microservices**. We use Python-backed async NLP to turn chaotic patient histories into instant, actionable insights. |
| **Supply Chain Integrity** | The World Health Organization estimates 1 in 10 medical products in developing nations are substandard or falsified. | **Immutable Blockchain Verification**. Every medicine batch gets a cryptographic hash on the Algorand ledger. Scan the QR, and you prove cryptographic authenticity in milliseconds. |

### 🔥 The Vibe: Why This is a Winning HealthTech Hack

Healix hits every major checkpoint a judge is looking for in the Healthcare Track:

1.  **Immediate Real-World Utility:** We aren't proposing a 10-year theoretical research project. We built a platform that a local clinic and pharmacy could adopt *tomorrow*. It relies on everyday tech—QR codes and smartphones—to bridge complex Web3 and AI infrastructure.
2.  **Radical Patient Agency:** We are pushing back against the dystopian idea that massive health conglomerates own your data. Our architecture enforces the idea that **you** are the absolute gatekeeper of your body's data.
3.  **Frictionless Healthcare Delivery:** When you eliminate the sheer administrative friction of entering data, reading bad handwriting, and doubting medicine origins, you give doctors and pharmacists their time back. And in healthcare, time saved is literally lives saved.

We built Healix because the current healthcare loop is fundamentally broken. By fusing **Deep Learning**, **Decentralized Ledgers**, and **Modern Full-Stack Frameworks**, we have forged a system that is transparent, blindingly fast, and mathematically impossible to fake. 

*We aren't just participating in the Healthcare track. We are setting the standard for it.*

Team **Team Chocolate Coffee** -- [Archishman Sarkar](https://github.com/ArchishmanS2005), [Suparna Panda](https://github.com/suparna39), [Devargho Chakraborty](https://github.com/Boredooms), [Sushovan Ghosh](https://github.com/MIRACULOUS65)

`2026-03-22`

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

### InfinityCare
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/infinitycare-4287) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIRACULOUS65/InfinityCare) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1qN5w-XmN7DEQt9R9XaJ4tOMY9qEwJIAg?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Patients own the data. Doctors read AI summaries.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Algorand](https://img.shields.io/badge/Algorand-333333?style=flat-square) ![tesseract.js](https://img.shields.io/badge/tesseract.js-333333?style=flat-square)

**The problem it solves**

# 🏥 The Problem InfinityCare Solves

> Healthcare today is broken at the data layer. InfinityCare fixes it.

---

## The Core Problem

Modern healthcare generates enormous amounts of sensitive data — prescriptions, lab reports, discharge summaries, medicine records — but the systems managing this data are **siloed, insecure, forgeable, and inaccessible at the moments that matter most**.

| Problem | Real-World Impact |
|---|---|
| Paper prescriptions are easily forged | Counterfeit drugs, prescription fraud |
| Fake medicines enter supply chains | Patient deaths, loss of trust |
| Emergency rooms can't identify unconscious patients | Delayed treatment, wrong diagnosis |
| Patient records locked in single-hospital silos | Doctors make decisions without full history |
| No audit trail for who accessed what | Zero accountability, zero patient control |
| AI tools require raw document uploads to third parties | Privacy violations, HIPAA risks |

---

## Who Suffers

```
Patients     → No control over their own medical records
Doctors      → Make decisions with incomplete or unavailable history
Hospitals    → Can't verify patient identity in emergencies
Pharmacies   → No way to confirm if a prescription is real
Vendors      → Medicine authenticity unverifiable at point of sale
```

---

## What InfinityCare Solves

### 🔐 1. Patient-Owned Medical Records
Patients upload their documents (lab reports, prescriptions, insurance) to a **encrypted, personal medical vault**. They explicitly grant or revoke access per institution — no hospital sees your records without your consent toggle.

### 🧬 2. Biometric Emergency Identification
If a patient arrives unconscious at a hospital, a nurse can run **DeepFace neural network matching** against the registered patient database to identify them in seconds — unlocking only the records that patient pre-authorized for hospital access.

### 💊 3. Blockchain-Verified Medicine Supply Chain
Every medicine batch is registered on the **Algorand blockchain** by the vendor at manufacture. A unique QR code is generated and attached. Pharmacies and patients can scan this QR to verify authenticity — `GENUINE`, `EXPIRED`, `TAMPERED`, or `SUSPICIOUS` — with an immutable on-chain record that cannot be faked or revised.

### 📄 4. AI-Powered Prescription & Document Analysis
Patients can upload any medical document and receive an **AI-generated clinical summary** — symptoms, medicines, dosage, and notes extracted automatically. A separate disease prediction engine takes symptom input and returns ranked differential diagnoses. Everything runs through server-side proxies: no raw medical data touches a third-party API directly.

### 🖊️ 5. Digital Doctor Prescriptions with QR Codes
Doctors issue digital prescriptions signed with their uploaded signature and encoded as a **scannable QR code**. Pharmacies scan the QR to instantly pull and verify the prescription — eliminating handwriting errors, forgeries, and lost paper slips.

### 📋 6. Full Audit Trails with Patient Notifications
Every time a hospital accesses a patient's record, an **access log is written and the patient is notified in real time**. Patients see exactly who viewed what and when — creating genuine accountability in a space that currently has none.

---

## The Unified Stack

InfinityCare doesn't solve these as disconnected features — it's one coherent platform with **role-based access** for every actor in the healthcare chain:

```
PATIENT  → Upload docs · Grant access · Get AI summaries · Verify medicines · View notifications
DOCTOR   → Issue digital prescriptions · View patient summaries · Track dispensing
HOSPITAL → Search patients · Emergency face ID · View authorized records
NURSE    → Run emergency biometric face matching
PHARMACY → Scan & validate prescriptions · Log dispensing · Check medicine stock
VENDOR   → Register medicines on blockchain · Generate verification QRs
```

---

## Why Now, Why Blockchain + AI + Biometrics

These three technologies have historically been used in isolation. InfinityCare  is one of the first attempts to combine them into a **single, end-to-end healthcare trust layer**:

- **Blockchain** makes medicine provenance immutable and publicly verifiable
- **AI** makes patient data useful without requiring human intermediaries
- **Biometrics** solves the hardest identity problem in healthcare: the unconscious patient

Together, they eliminate the three biggest failure points in healthcare data: **forgery, inaccessibility, and lack of consent**.

---

*Built for Hacktropica Hackathon · InfinityCare — Trust Infrastructure for Healthcare*

**Challenges we ran into**

# 🚧 Challenges I Ran Into

> A candid breakdown of the real technical challenges faced while building **InfinityCare** — a full-stack healthcare platform combining blockchain medicine verification, AI-powered document analysis, biometric face recognition, and a multi-role access control system, all built under hackathon time constraints.
---

## 1. Prisma Client Not Generating After `npm install`

**Q: Why did the app crash with `Cannot find module '.prisma/client/default'` immediately after cloning and installing?**

A: Prisma generates its typed client into `node_modules/@prisma/client` at build time via `prisma generate`. This generated output is gitignored, so a fresh `npm install` alone is never enough. The app would boot, hit [src/lib/db.ts], and immediately throw a runtime crash before a single page could render.

**Fix:** Run `npx prisma generate` after every `npm install`. We also added it as a `postinstall` script so it's automated.

| Step | Command |
| Install deps | `npm install` |
| Generate Prisma client | `npx prisma generate` |
| Start dev server | `npm run dev` |

---

## 2. Prisma + Supabase Connection Pooling (`PrismaPg` Adapter)

**Q: Why couldn't we just use the default Prisma connection string with Supabase?**

A: Supabase's hosted Postgres requires connection pooling via PgBouncer for high-concurrency serverless environments (Next.js API routes spin up per-request). The standard `DATABASE_URL` with `?pgbouncer=true` added breaks Prisma's native migrations and client. We had to use the `@prisma/adapter-pg` driver adapter combined with the `pg` connection pool, while stripping query params (`?pgbouncer=true`) when connecting from the Python service.

```ts
// src/lib/db.ts - The non-obvious solution
const pool = new Pool({ connectionString });
// @ts-expect-error mismatched @types/pg between pg and @prisma/adapter-pg
const adapter = new PrismaPg(pool);
```

The `@ts-expect-error` suppression itself is a symptom of the version mismatch between `pg`, `@types/pg`, and `@prisma/adapter-pg` — all three need to be pinned to aligned versions.

---

## 3. Integrating BetterAuth with a Custom `role` Field

**Q: Adding user roles (`PATIENT`, `DOCTOR`, `HOSPITAL`, etc.) clashed with BetterAuth's opinionated user schema — how did we handle it?**

A: BetterAuth generates its own `User` table via its own migration system. Our Prisma schema needed an additional `role` enum field that BetterAuth doesn't know about. The challenge was keeping BetterAuth's session/account tables in sync while adding our domain-specific fields without breaking the adapter.

**Solution:** Declared `role` as an `additionalFields` in the BetterAuth config with `input: true` so it's accepted during sign-up. We also had to ensure the Prisma schema's `Role` enum exactly matched what the auth client sent, and that the middleware could read it from the session cookie without an extra DB round-trip.

---

## 4. Algorand Blockchain Integration — Signing Transactions in the Browser

**Q: How did we handle wallet signing for medicine registration without exposing private keys or writing a custom wallet?**

A: We used the **Pera Wallet** SDK for browser-based transaction signing. The tricky part: `algosdk` generates a `Transaction` object server-side (or in a utility), but signing must happen client-side via the user's connected wallet. This meant:

1. Building the transaction on the client using `algosdk.makePaymentTxnWithSuggestedParamsFromObject`
2. Encoding medicine metadata as a UTF-8 `note` field (max 1KB on Algorand)
3. Sending the signed transaction to the Algorand Testnet via AlgoNode's public API (no token needed)

A 0-ALGO self-payment with a JSON note is the canonical "data anchoring" pattern on Algorand — but finding that pattern and understanding its constraints took significant research time.

| Constraint | Value |
|---|---|
| Max `note` size | 1,024 bytes |
| Network used | Algorand Testnet (AlgoNode) |
| Transaction cost | 0.001 ALGO (min fee) |
| Signing method | Pera Wallet SDK |

---

## 5. DeepFace Python Service — Cold Start, Dependencies & CORS

**Q: The face recognition feature requires a Python Flask service running locally. What made this difficult?**

A: Several compounding issues:

- **TensorFlow download size:** `deepface` depends on `tensorflow` (~350MB). On a weak or throttled network (common at hackathons), pip would fail mid-download with `Connection forcibly closed by remote host`.
- **Module not found at runtime:** `psycopg2` and `deepface` weren't in the system Python — we had to create a dedicated `venv` and install into it.
- **VGG-Face model auto-download:** The first `/match` request triggers DeepFace to download the VGG-Face model weights (~550MB) into `~/.deepface/weights/`. This adds a >1 minute cold start to the very first recognition attempt with no UI feedback.
- **CORS:** The Next.js frontend (`:3000`) calling

**Best Use of Presage SDK**

# Presage Technologies — Integration with InfinityCare

## What is Presage?

Presage Technologies provides the **SmartSpectra SDK** — a contactless, camera-based vital-sign monitoring solution. Using only a standard smartphone or webcam, the SDK extracts real-time physiological data through advanced computer vision and signal processing, **without any wearable hardware or physical sensors**.

### Vitals it can measure:
| Metric | Description |
|---|---|
| **Heart Rate (Pulse)** | Real-time BPM via remote photoplethysmography (rPPG) |
| **Heart Rate Variability (HRV)** | Stress and autonomic nervous system indicator |
| **Breathing Rate** | Respiratory cycles per minute |
| **Inhale/Exhale Ratio** | Respiratory pattern analysis |
| **Blood Pressure (Relative)** | Derived from pulse waveform analysis |
| **Apnea Detection** | Identifies pauses in breathing |
| **Facial Landmark Tracking** | Blink, expression, focus & excitement analysis |

---

## How Presage Fits InfinityCare

InfinityCare is a privacy-first, multi-role healthcare ecosystem. Presage's contactless vitals monitoring integrates naturally into several critical workflows:

### 1. Nurse Station — Emergency Triage (Highest-Impact Use Case)

The **Nurse Dashboard** already uses a camera-based flow (DeepFace) to biometrically identify unconscious or unresponsive patients. Presage extends this exact same camera session to simultaneously capture vitals:

- A nurse activates **Patient Face ID Match** → the camera opens
- **DeepFace** identifies the patient by face
- **Presage SmartSpectra**, running in parallel on the same video feed, captures **heart rate, breathing rate, HRV, and blood pressure**
- The vitals are instantly attached to the identified patient's record and pushed to the treating doctor's AI summary

This means a single camera scan in an emergency produces **identity + live vitals** — zero contact, zero wearable setup, zero wasted time.

### 2. Patient Self-Monitoring — At-Home Health Checks

Patients can use their own device camera from the **Patient Dashboard** to record a quick vitals check:

- Open the "Check My Vitals" feature → camera activates for ~30 seconds
- Presage captures heart rate, breathing rate, HRV, and blood pressure
- Results are stored as a timestamped health document in the patient's **encrypted medical vault**
- The patient retains full ownership and access control (consistent with InfinityCare's zero-trust model)
- Over time, this creates a longitudinal vitals trend that doctors can review via **AI Summaries**

### 3. Doctor Intelligence — Pre-Consultation Vitals

Before a consultation, patients can perform a Presage scan. The data flows into the **AI Summary** pipeline that doctors already use:

- Doctor opens the patient's AI-generated summary
- Latest Presage vitals (HR, BP trend, respiratory patterns) are included alongside lab reports and prescriptions
- Reduces cognitive overload — the doctor sees a holistic snapshot without manually collecting vitals

### 4. Hospital Admission — Contactless Screening

At hospital check-in, a receptionist or kiosk can use a tablet camera to collect baseline vitals before the patient even steps into a ward:

- No thermometers, no cuffs, no oximeters needed at the screening stage
- Vitals are logged against the patient's record via the **Hospital Dashboard**
- Speeds up the admission pipeline, especially during high-volume situations (epidemics, mass casualty events)

---

## Why Presage is the Right Fit

| InfinityCare Principle | Presage Alignment |
|---|---|
| **Zero-trust, patient-owned data** | Vitals captured via Presage are stored in the patient's encrypted vault — only accessible with explicit patient permission |
| **AI-powered clinical intelligence** | Presage vitals feed directly into the AI summary pipeline, enriching the data doctors already use |
| **Camera-first biometric infrastructure** | The app already uses camera-based DeepFace for identification — Presage reuses the same camera hardware with zero additional cost |
| **Contactless & accessible** | No wearables, no external hardware — works on any smartphone or webcam the user already owns |
| **Privacy-conscious processing** | Presage processes video data locally/on-device, aligning with InfinityCare's stance on minimizing data transmission |

---

## Technical Integration Summary

- **Platform**: SmartSpectra SDK available for iOS, Android, and C++ (desktop/webcam)
- **Frontend**: Integrate the SDK into the Next.js app via a WebView/iframe for the scan flow, or natively in mobile builds
- **Backend**: Vitals data is posted to the existing API layer and stored via Prisma in the same database as medical documents
- **Nurse Flow**: Runs alongside DeepFace in the [FaceMatchModal](file:///c:/hackathon/hacktropica/health/health/healix-app/src/components/nurse/FaceMatchModal.tsx#26-251) — one camera session, two outputs (identity + vitals)
- **Patient Flow**: New "Check My Vitals" card on the Patient Dashboard, st

**Best Use of Gemini API**

# Google Gemini AI — Integration with InfinityCare

## What is Gemini AI?

**Google Gemini** is a family of large language models (LLMs) developed by Google DeepMind. InfinityCare uses **Gemini 2.5 Flash** — a fast, cost-efficient model optimised for structured JSON output — as its **primary AI engine** for clinical intelligence across the platform.

---

## Where Gemini is Used

Gemini powers the **AI Clinical Summarization Pipeline** — the core intelligence layer that transforms raw medical text into structured, actionable clinical data.

### The Full Pipeline

```
Prescription Image → Tesseract.js OCR → Raw Text → Gemini 2.5 Flash → Structured JSON
```

1. **Patient uploads** a prescription or lab report image via the **AI Prescription Analysis** modal
2. **Tesseract.js** (browser-side OCR) extracts raw text from the image — enhanced with 2× upscaling and adaptive thresholding for medical document clarity
3. The extracted text is sent to **`POST /api/ai/summarize`**, which calls **Gemini 2.5 Flash** via the Generative Language API
4. Gemini returns a **structured JSON** response with:

| Field | Description |
|---|---|
| `patientOverview` | Brief patient description from the document |
| `symptoms` | Array of extracted symptoms/clinical findings |
| `medicines` | Array of prescribed medication names |
| `dosage` | Dosage instructions and frequency |
| `notes` | Special precautions and additional clinical notes |

5. The extracted symptoms are **automatically forwarded** to a separate **Disease Prediction ML API** that returns ranked disease probabilities with confidence scores

---

## How Each Role Benefits

### Patient — "Scan Prescription" (AI Prescription Analysis)

- Patient uploads a photo of a handwritten or printed prescription
- Gemini extracts structured clinical data in seconds
- Results display in a split-view: **Clinical Summary** tab + **Disease Predictions** tab
- Patient can **save** the AI summary to their encrypted medical vault for future reference and doctor sharing

### Doctor — "AI Patient Summaries"

- Doctors see Gemini-generated summaries shared by their patients — not raw records
- Each summary includes extracted symptoms, medications, dosage plans, and precautions
- This **reduces cognitive overload** and speeds up pre-consultation review
- Doctors work with clean, structured data instead of deciphering handwriting or scanning through pages

### Nurse — Emergency Triage Support

- After identifying an unresponsive patient via Face ID, any saved AI summaries are immediately accessible
- Gives emergency staff a fast snapshot of a patient's recent medications and conditions without manual record lookup

---

## Resilient Fallback Chain

The summarization API is designed for **zero downtime** with a cascading fallback architecture:

```
1. Gemini 2.5 Flash     ← Primary (fastest, structured JSON output)
2. Ollama Cloud (LLaMA)  ← Secondary (OpenAI-compatible endpoint)
3. Custom Healthcare AI   ← Tertiary (self-hosted ML backend)
4. Degraded Response      ← Graceful fallback (returns raw OCR text with warning)
```

If Gemini is unavailable (rate limits, network issues), the system **automatically** tries the next provider — the patient never sees a hard failure. All keys are server-side only and never exposed to the browser.

---

## Why Gemini is the Right Fit

| Requirement | Gemini Alignment |
|---|---|
| **Structured JSON output** | Gemini natively supports `responseMimeType: "application/json"` — no fragile regex parsing needed |
| **Medical text comprehension** | Handles handwritten prescriptions, medical abbreviations, and clinical jargon with high accuracy |
| **Speed** | Gemini 2.5 Flash returns responses in 1–3 seconds — critical for real-time patient workflows |
| **Server-side security** | API key stays in backend env vars; patient data never touches Google servers beyond the API call |
| **Cost efficiency** | Flash model pricing is minimal per request — sustainable for frequent per-prescription analysis |
| **Privacy-first architecture** | Only the extracted OCR text (not the original image) is sent to Gemini, minimising data exposure |

---

## Technical Summary

| Component | Details |
|---|---|
| **Model** | `gemini-2.5-flash` via Generative Language API |
| **API Route** | [/api/ai/summarize](file:///c:/hackathon/hacktropica/health/health/healix-app/src/app/api/ai/summarize/route.ts) |
| **Client Service** | [analysisService.ts](file:///c:/hackathon/hacktropica/health/health/healix-app/src/lib/services/analysisService.ts) |
| **Patient UI** | [PrescriptionAnalysisModal.tsx](file:///c:/hackathon/hacktropica/health/health/healix-app/src/components/patient/PrescriptionAnalysisModal.tsx) |
| **Doctor UI** | [PatientAISummariesModal.tsx](file:///c:/hackathon/hacktropica/health/health/healix-app/src/components/doctor/PatientAISummariesModal.tsx) |
| **OCR Engine** | Tesseract.js (browser-side, no server dependency) |
| **Prediction API** | Separate ML service on Render →

Team **Team Chocolate Coffee** -- [Devargho Chakraborty](https://github.com/Boredooms), [Suparna Panda](https://github.com/suparna39), [Archishman Sarkar](https://github.com/ArchishmanS2005), [Sushovan Ghosh](https://github.com/MIRACULOUS65)

`2026-04-05`

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

### LifeLinkTwin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifelinktwin-8557) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/krishujha21/LifeLinkTwin) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lifelinktwin.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/69ed8908ceea410ebe4e5a978217bbc8) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Real-Time Health Monitoring with AI Twins

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**What Can People Use LifeLink Twin For**

- Continuous Persoanalyzingh Monitoring  
  Users can track important health metrics such as heart rate, oxygen levels, and temperature in real time. This helps individuals stay aware of their health status without needing constant hospital visits.

- Early Detection of Health Issues  
  The system analyzes patterns in vital data and detects unusual trends early. This allows potential health issues to be identified before they turn into serious medical emergencies.

- Remote Patient Monitoring for Doctors  
  Doctors can monitor patients remotely through a centralized dashboard. This reduces the need for frequent in-person visits and allows doctors to keep track of patient health continuously.

- Reducing False Medical Alerts  
  The system uses multi-parameter validation and time-window analysis to avoid false alarms caused by temporary spikes in vitals. This helps doctors focus on real emergencies instead of unnecessary alerts.

- Health Trend Analysis  
  LifeLink Twin records historical health data and visualizes trends over time. This helps doctors understand how a patient’s condition is evolving and supports better clinical decision-making.

- Smart Health Insights  
  Instead of only showing raw numbers, the system converts vital data into meaningful insights such as health risk scores, stability indicators, and health event summaries.

- Benefits for Patients  
  Patients gain better awareness of their health through real-time monitoring and early warnings. This can help prevent medical emergencies and reduce hospital visits. It also encourages proactive and preventive healthcare.

- Benefits for Doctors  
  Doctors can monitor multiple patients simultaneously, receive prioritized alerts, and quickly identify high-risk cases. This improves efficiency, reduces workload, and enables faster medical response when needed.

- Healthcare Research and Simulation  
  The built-in data simulation allows researchers and developers to test monitoring systems and health algorithms without relying on expensive medical hardware.

- Supporting Preventive Healthcare  
  By continuously analyzing health data and predicting potential risks, LifeLink Twin helps shift healthcare from reactive treatment to preventive care.

**Challenges we ran into**

**Challenges I Ran Into**

- Handling false health alerts caused by temporary heart rate spikes or normal emotional reactions.

- Ensuring smooth real-time data updates without UI lag, graph flickering, or delayed alerts.

- Generating realistic simulated health data instead of unrealistic random values.

- Balancing system complexity with the limited time and scope of a hackathon project.

- Converting raw vital data into meaningful insights that doctors and users can easily understand.

Team **CodeCanvas** -- Likhith K, Manasvi Daga, Gayatri Desai, Deshik Jha

`2026-03-17`

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

### Neurocure+
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neurocure-cee9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tirthasadhu015-dot/NeuroCure-Ai-Backend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://r8rjxzl9-5000.inc1.devtunnels.ms/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/wX5Qv_INugs) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Ai Medical Assistant

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

1. Addressing the "Self-Diagnosis" Gap
Most people use standard search engines to look up symptoms, which often leads to overwhelming, unvetted information or unnecessary panic. NeuroCure+ provides a structured, direct interface that maps specific symptoms to verified medical data, offering a clearer first point of reference.

2. Immediate Guidance in Low-Resource Areas
In regions where access to immediate medical consultation is limited or delayed, people often lack basic knowledge regarding medication dosages and necessary precautions. NeuroCure+ serves as an AI Medical Assistant that provides instant information on:

Medicine Identification: Matching symptoms to the right medication.

Safety First: Highlighting critical precautions and severity levels to help users understand when they can manage at home versus when they must seek urgent professional help.

3. Streamlining Medical Data Accessibility
Medical information is often locked in complex databases or dense PDF documents. This project solves the problem of data fragmentation by centralizing symptoms, dosages, and precautions into a lightweight, responsive web application that anyone can use, regardless of their technical or medical expertise.

4. Reducing Healthcare Overburden
By providing quick answers for minor symptoms and clear "Severity" indicators, the tool helps users filter through minor issues. This potentially reduces the burden on primary care facilities by ensuring that patients are better informed about the urgency of their condition before they even walk through the clinic door.

**Challenges we ran into**

1. Environment & Dependency Management
One of the first hurdles was a Python interpreter mismatch within VS Code. Despite having a virtual environment (.venv) set up, the IDE wasn't correctly mapping the libraries (Flask, Pandas, Flask-CORS) to the active workspace. This led to "Import could not be resolved" errors even after successful installation.

Solution: I resolved this by manually re-configuring the Python Path in VS Code and ensuring the environment was properly activated before running the Flask server.

2. Medical Data Normalization
Working with a CSV-based medical database presented challenges with data consistency. Some symptom entries had trailing spaces, mixed casing, or missing values ( NaN ), which caused the search algorithm to fail even on exact symptom matches.

Solution: I implemented a robust preprocessing pipeline using Pandas. This included stripping whitespace from column headers, normalizing all symptoms to lowercase, and filling empty data points with fallback strings to prevent the backend from crashing during a search.

3. Search Query Flexibility
Initially, the chatbot only responded to exact string matches. If a user typed "I have a fever" but the database only had "fever," the system returned no results.

Solution: I upgraded the search logic from strict equality to a multi-tier matching system:

Strict exact match.

Substring matching (checking if the database symptom exists within the user's message).

Token-based matching to identify keywords even in complex sentences.

4. Cross-Origin Resource Sharing (CORS)
Connecting the frontend to the Flask backend initially caused blocked requests due to security policies.

Solution: Integrated the Flask-CORS library to bridge the gap between the server and the web UI, allowing seamless data flow between the AI assistant and the user interface.

Team **T2-Neurobyte** -- [KARAMVEER VISHWAKARMA](https://github.com/Karamveer0003), [Suman Chattopadhyay](https://github.com/sumanchattopadhyay2910-wq), [Tahseen Fatma](https://github.com/tahseen9832-jpg), [Tirtha Sadhu](https://github.com/tirthasadhu015-dot)

`2026-04-11`

---

### VitalSync
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitalsync-bd28) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Pranav-mb-dev/VitalSync-Codecrew) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vitalsync-01.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> A Family Link for Healthier Life

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![SPRINGBOOT](https://img.shields.io/badge/SPRINGBOOT-333333?style=flat-square)

**The problem it solves**

🎙️ The Highlight: Voice-First Healthcare
The standout feature of this app is its Voice Navigation and AI Voice Chat. Instead of fumbling through menus, users can simply talk to the app.

Interactive Explanations: Ask, "Hey, can you explain my latest blood report?" and the AI will analyze the biomarkers to give you a user preffered language's summary.

Hands-Free Logging: Perfect for elderly patients or busy caregivers—log meals or symptoms just by speaking.

Multilingual Support: Communicate naturally in English, Tamil, Hindi, Kannada, or Telugu.

🛠️ How It Solves The Problems
For Patients: Independence and Clarity
The "One-and-Done" Log: Medicines are tracked by time of day (Noon, Evening, etc.). Once you log it, the system locks it to prevent accidental double-dosing—keeping you safe.

AI Diet & Reports: Don't know what to eat? Let the AI generate a diet chart. Confused by medical jargon? The AI extracts biomarkers from uploaded reports and explains them instantly.

One-Touch SOS: A critical SOS button sends an immediate alert to your caregiver if things take a turn.

For Caregivers: Peace of Mind
Remote Mirroring: Your dashboard reflects the patient's vitals, health score, and medicine logs in real-time. If they miss a dose, you’ll know.

Proactive Alerts: You don't have to "check-in" constantly. If the patient’s Health Score drops or they trigger an SOS, you get an emergency notification immediately.

**Challenges we ran into**

1. The "Accent Gap": Mastering Indian Dialects
The Hurdle: Most off-the-shelf Speech-to-Text (STT) models are trained on Western accents. When we tested the app with Indian English or regional languages like Tamil and Kannada, the AI frequently "hallucinated" words or simply failed to understand medical terms spoken with a local inflection.

The Solution: We had to move away from generic models and implement localized acoustic models. We integrated specialized APIs that support Indian English (en-IN) and regional dialects. We also built a custom "Medical Dictionary" layer that prioritizes health-related keywords, ensuring that even if the accent is thick, the intent (like "Log Medicine") is correctly identified.

2. The "Dual Voice" Glitch: Fallback Chaos
The Hurdle: To ensure the app never went silent, we implemented a fallback voice mechanism. However, a race condition occurred: if the primary high-quality AI voice took too long to load, the fallback voice would trigger while the primary was still starting. This resulted in two voices speaking over each other—a confusing "echo" effect for the user.

The Solution: We implemented a Strict State Manager for the audio output. We created a "Voice Controller" that locks the audio channel. Now, the fallback only initializes if a TimeoutException is explicitly thrown by the primary service, and it must pass a "Channel-Is-Idle" check before making a sound. No more AI arguments!

3. Voice Navigation: The "Silent Treatment"
The Hurdle: Initially, our voice navigation simply wouldn't fire. The app would recognize the words ("Go to Dashboard"), but the screen wouldn't change. The routing engine wasn't "listening" to the AI’s output; it was two separate systems living in the same house but not talking to each other.

The Solution: We mapped specific Intent Keywords directly to our app's deep-linking system. We used a global state (like a "Navigation Listener") that constantly watches for verified intent strings from the AI. Once the AI confirms the command, it triggers a clean route transition—making the hands-free experience actually work.

4. Google Fit Synchronization Lag
The Hurdle: Fetching Blood Glucose and $O_2$ levels every hour was originally causing the UI to stutter or show "No Data" while the API call was pending.

The Solution: We shifted the Google Fit sync to a Background Worker. The app now fetches data silently in the background and updates a local database. When the user opens their Progress tab, the graph pulls from the local cache instantly while the background refresh continues quietly.

**Open Innovation**

🏗️ 1. Ecosystem Interoperability
Open innovation thrives on "co-creation" rather than building in a vacuum. External Data Integration: By syncing with Google Fit, your app doesn't try to reinvent health tracking. Instead, it leverages an existing global data ecosystem to provide real-time vitals like Blood Glucose and $O_2$.The Triple-Stakeholder Model: Connecting the Patient, Caregiver, and Doctor into one fluid communication loop is the definition of a collaborative innovation. It turns health management from a solo task into a shared responsibility.

🌍 2. Democratizing Technology (Inclusion)
A key part of open innovation is making high-tech solutions accessible to the "edge cases"- people who are often left behind by standard tech.
Multilingual Voice Interface: By supporting Tamil, Hindi, Kannada, and Telugu, you are breaking the language barrier. This allows users who aren't tech-savvy or fluent in English to participate in the digital health revolution.
Voice-First UX: Navigating an app via voice isn't just a "cool feature"; it’s an inclusive innovation for elderly patients or those with motor impairments who struggle with small touch targets on a mobile screen.
🔓 3. Translating Complexity
Open innovation often involves taking "expert knowledge" (like a medical report) and making it "open" and understandable for the layperson.AI Biomarker Extraction: Your app takes complex, jargon-heavy medical reports and uses AI to "translate" them into plain language. This empowers patients to understand their own health data, moving the power from the institution (the lab/hospital) to the individual.🛠️ 4. Solving the "Context Gap" You addressed a classic open innovation challenge: taking a global technology (AI Voice) and localizing it for a specific environment.
The Indian Accent Challenge: Standard AI models often fail in diverse linguistic landscapes. By refining the voice chat to handle Indian accents and regional nuances, you’ve adapted "Open AI" concepts to solve a high-friction, local problem.

Team **CodeCrew** -- [Pranav Bhargav_M](https://github.com/zapgeek), [Venkatachalam S](https://github.com/Venkat7123), [Jaiharish R](https://github.com/Jaiharish-23), [Vasandhan PKG](https://github.com/VasandhanPKG)

`2026-03-29`

---

### PULSE AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pulse-ai-c011) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/C69NKIhTi3I?si=RSvLeepl6W3ZjDky) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Your Intelligent Health Companion

![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Uvicorn](https://img.shields.io/badge/Uvicorn-333333?style=flat-square)

**The problem it solves**

PulseAI addresses three critical pain points in modern healthcare:

1. The "Medical Jargon" Gap: Most patients leave a doctor's consultation with only a partial understanding of their diagnosis. PulseAI uses AI to translate complex medical terminology into clear, actionable English, ensuring patients truly understand their health.
2. Information Overload & Adherence: Patients often struggle to remember medication dosages, dietary restrictions, and lifestyle advice. By extracting this data from audio or photos and creating "Health Routines," PulseAI increases adherence and improves recovery outcomes.
3. Administrative Friction: Scheduling and billing often feel disconnected. PulseAI bridges this by allowing patients to book "TBD" appointments directly and giving doctors a streamlined dashboard to manage their schedules and track payments.


In short, PulseAI replaces confusion with clarity, ensuring the doctor's advice is correctly understood, remembered, and acted upon.

**Challenges we ran into**

During the development of PulseAI, we navigated several technical challenges to ensure a seamless experience. Here’s a summary of the main hurdles:

1. Dependency Synchronization: We faced npm version conflicts between React Native and its core type definitions. Resolving these required carefully aligning package versions to ensure stability on mobile.
2. Environment Configuration: The backend initially struggled with missing Python libraries (like google-generativeai and sqlalchemy). We had to troubleshoot the virtual environment and pip installation process to ensure all AI and database dependencies were properly recognized.
3. Module Discovery Issues: We encountered ImportErrors while trying to set up the secondary services (OCR and LLM). The fix involved adding init, .py
 files to every backend directory to ensure Python could "see" the internal routes and services as a unified package.
Dynamic Role-Based Routing: Transitioning the app from a single-user flow to a sophisticated Doctor/Patient ecosystem was a major architectural update. We had to restructure the entire navigation stack in App.js to dynamically route users based on their role and persist that state across app restarts.
3. External API Resilience: Since the app relies on critical external services (Google Gemini, Vision API, and Neon DB), we implemented fallback mechanisms (like the mock-AI response and offline PDF reading) so the app remains functional even if a service is temporarily unreachable.

Each of these challenges helped make the final architecture more robust and ready for real-world medical data handling!

**Healthcare**

PulseAI fits perfectly into the Healthcare & Medical Technology track because it directly addresses the "Information Gap" between providers and patients, one of the biggest barriers to effective care.

Here’s how it aligns with key healthcare objectives:

1. Enhancing Patient Agency & Health Literacy: By using AI to translate complex medical jargon into plain English, PulseAI empowers patients to understand their own health. High health literacy is scientifically linked to better long-term medical outcomes.

2. Improving Treatment Adherence: The "My Health Routine" feature converts a doctor's dense advice into actionable daily tasks (medication alerts, dietary avoidance, lifestyle changes). This directly tackles the problem of patient non-compliance, which costs the global healthcare system billions annually.

3. Digitizing the "Last Mile" of Care: It bridges the gap between the physical consultation and the patient's home life. By using OCR for handwritten prescriptions and AI for audio consultations, it ensures no detail is lost or forgotten once the patient leaves the clinic.

4. Provider Efficiency: The Doctor Dashboard streamlines appointment management and payment tracking, allowing healthcare providers to focus more on patient care and less on administrative overhead.

5. Data-Driven Preventive Care: Features like the BMI tracker and localized health routine advice move healthcare from a reactive model to a proactive, preventive one.

In a track focused on innovation, accessibility, and improving the quality of care, PulseAI stands out as a practical, AI-driven solution that humanizes technology for better patient health.

Team **Dev_Zero** -- [Sayan Ghosh](https://github.com/sayanghoshcode16), [PARAMITA DAS](https://github.com/Rai2608), [Olivia Das](https://github.com/Absoluteolivia)

`2026-03-22`

---

### curaAI-ML system for predicting drug toxicity
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/curaaiml-systemfor-predicting-drug-toxicity-b6b5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Damselin/chemo-toxicity-prediction) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/e/2PACX-1vSHZg35xBuw6uSSaQzpE1JYl3mnbw8qJxcizsuuhknjpuj-xuXLwetW9eLOqPdM1w/pub?start=false&loop=false&delayms=3000) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> early detection.safer treatment.smarter healthcare

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Chemotherapy treatment, while effective, often comes with severe and sometimes unpredictable side effects (toxicity). Currently, doctors rely heavily on experience and general guidelines rather than personalized risk predictions for each patient.

This project solves that problem by providing an AI-based system that predicts the likelihood of chemotherapy toxicity using patient-specific data such as age, BMI, lab values, and symptoms.

By using this tool, healthcare professionals can:
- Identify high-risk patients early
- Adjust treatment plans proactively
- Reduce complications and hospitalizations
- Improve overall patient safety

It also simplifies decision-making by converting complex medical data into an easy-to-understand risk score and prediction, making the process faster and more data-driven.

In the future, such systems can support personalized medicine and smarter healthcare decisions at scale.

**Challenges we ran into**

During the development of this project, I faced multiple practical challenges.

One of the main issues was handling communication between the frontend and backend. Initially, the API requests were failing due to incorrect headers and CORS-related issues, which resulted in errors like "Unsupported Media Type" and connection failures. I resolved this by properly configuring the request headers and ensuring JSON data was correctly formatted.

Another challenge was aligning the machine learning model with real-time user input. Since the model was trained using processed data (with encoding), I had to make sure that incoming input from the frontend matched the training format. This required careful preprocessing using techniques like one-hot encoding and column alignment.

I also encountered issues with local API testing tools and debugging prediction outputs. Tools like Hoppscotch sometimes did not send headers correctly, which made debugging harder. Switching to direct frontend integration helped resolve this.

Finally, integrating everything into a working full-stack system within limited time was challenging, but breaking the problem into smaller parts (model → API → frontend) helped in successfully completing the project.

Team **curaAI** -- [Kashishh Shrivastava](https://github.com/Kashishhh24), Roshny Nachammai, [Pratistha Acharya](https://github.com/pratistha-a)

`2026-03-17`

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

### Gaze Connects
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gaze-connects-95a6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sahilchabra09/gaze-connects) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://gaze-connect.nodehq.in) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SAEbWiR2S6o?si=nVIRuHYF-mCnrOKg) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Empowering Patients with Paralysis

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![MQTT](https://img.shields.io/badge/MQTT-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square)

**The problem it solves**

“Paralyzed Individuals Struggle to
Communicate and Live
Independently”
1. Communication is Painfully Slow
Even typing a simple sentence using eye-trackers takes minutes
2. Lack of Independence
Users cannot control basic devices like lights, fans, or calls
3. High Cost of Existing Solutions
Commercial eye-trackers cost ₹2–5 lakh ($5,000+)
4. Constant Dependency
Users rely on caregivers 24/7 for basic needs

**Challenges we ran into**

The major challenges we ran into during the development of this project involved accuracy. Initially, accuracy was not very good because we used a very dumbed-down approach to eye tracking. 

It became much better when we tried to control the lighting in our surroundings, which actually increased the eye tracker's accuracy significantly.

Since it was a feature-rich project, we had to cut down some features because the hackathon was only 24 hours. Overall, we are happy with what we built. It is a very good project, I would say.

**Main Track: The Deepforge Arena**

Our project is an innovation in the field of human-computer interaction. It is a simplified, affordable alternative to the expensive eye trackers currently on the market.

This project, Gaze Connects, is designed to help patients worldwide who are paralyzed and unable to move their bodies or speak. It aims to free them from the need for constant caretaking by giving them the ability to control their surroundings.

The platform allows users to:
1. Control their appliances
2. Chat with people nearby
3. Message others to ask for help

By using the messaging app we have built into this platform, they can communicate exactly what they need without requiring a caretaker to be present at all times.

Team **StrawHats** -- [Arunya Mahajan](https://github.com/Ester-D-Kate), [Tushar Dhingra](github.com/TDHINGRA16)

`2026-03-29`

---

### careOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/careos-7e3a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/malaypratihar2710/index) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4ZsvVooQkR8) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Hospital Management System

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Problems Solved by CareOS
1. 📄 Paper-Based Record Issues
Patient data stored in files → easily lost or damaged
Hard to access past records quickly

2. 🔍 Lack of Centralized System
Different departments use separate systems
No single platform for all hospital operations

3. ⏳ Long Waiting Times
No proper queue system
Patients don’t know when their turn will come

4. 🛏️ Poor Bed Management
Staff unaware of available beds
Delays in admitting patients, especially in emergencies

5. 👩‍⚕️ Inefficient Staff Scheduling
Manual shift planning leads to confusion
Overlapping or missing shifts

6. 💊 Medication Tracking Problems
No proper tracking of prescribed medicines
Risk of missed doses or wrong timing

7. 🚨 Slow Emergency Response
No instant alert system for critical patients
Delay in notifying doctors/nurses

8. 📣 Weak Communication System
Patients cannot easily raise complaints
Admin doesn’t get real-time feedback

9. 📊 No Real-Time Data Visibility
Hospital status (beds, patients, staff) not updated live
Decisions are delayed or inaccurate

10. 🔐 Data Mismanagement & Security Issues
Unauthorized access to patient data
No role-based control (admin/nurse/patient)

11. 🔄 Redundant & Repetitive Work
Same data entered multiple times
Wastes time and increases errors

12. 😵 Lack of Patient Transparency
Patients don’t know:
their queue status
prescribed medicines
treatment updates

**Best Beginners' Team**

We are a team of first-year Computer Science students participating in our first hackathon, driven by curiosity and a strong desire to learn. As beginners, we focused on building a practical and impactful solution—CareOS—while continuously improving our technical and problem-solving skills throughout the process. Despite limited experience, we collaborated effectively, adapted quickly to challenges, and remained committed to delivering a functional and meaningful project. This journey reflects our enthusiasm, teamwork, and willingness to grow as developers.

**Healthcare**

We are a team of first-year Computer Science students participating in our first hackathon, focused on solving real-world challenges in healthcare. Through our project, CareOS, we aim to improve hospital efficiency by digitizing patient management, staff coordination, and resource tracking. As beginners, we approached this problem with a fresh perspective, emphasizing simplicity, usability, and impact. Despite limited experience, we worked collaboratively to build a practical solution that can enhance patient care and streamline hospital operations.

Team **Runtime Terrors** -- [CHINMOY DAS](https://github.com/Cdas2006), [SUDIPTO HALDAR](https://github.com/sudiptohaldar-sam), [Malay Pratihar](https://github.com/malaypratihar2710), [Nakshatra Naskar](https://github.com/nakshatra365)

`2026-03-22`

---

### FarmRakshak
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/farmrakshak-f746) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://Farmrakshak0.netlify.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sfhPZ2IrpU0) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> FarmRakshak – AI Guardian for Livestock Health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![HTML/CSS](https://img.shields.io/badge/HTML/CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

India is the world's 3rd largest egg producer and runs a ₹3 lakh crore poultry industry — yet the farmers powering this industry have absolutely no AI tools, no real-time alerts, and no intelligent support system in their own language.

When a disease like Newcastle or Bird Flu hits a farm, the farmer has no way to detect it early. The nearest vet is often 30 to 50 kilometres away. By the time help arrives, hundreds of birds are already dead and the financial damage is done.

The problem runs deeper than disease. 65% of Indian farmers are not comfortable typing on a smartphone — making every existing agri-tech app useless for them. They have no weather-to-action guidance, no FCR tracking, no market price intelligence, and no awareness of the government subsidies they qualify for.

The result: ₹18,000 crore lost every year to preventable causes, families pushed into debt cycles, and a ₹3 lakh crore industry running completely blind.

FarmRakshak solves this — with AI that speaks Hindi, diagnoses disease from a photo in 3 seconds, sends WhatsApp alerts before problems occur, and costs the farmer absolutely nothing.

**Challenges we ran into**

API (1) — Large phone photos crashing Gemini with 400 errors (fixed with canvas resizer), wrong model name causing 404s (gemini-1.5-flash vs gemini-1.5-flash-latest), Gemini wrapping JSON in markdown code fences breaking JSON.parse(), and AI giving generic answers instead of farm-specific ones (fixed by injecting full farm context into every prompt).
🔧 Technical (2) — CORS blocking API calls when running from file:// (fixed by deploying to Netlify), and API key not persisting because of window.onload timing + wrong event listener.
 Deployment (3) — Netlify showing blank page because only index.html was uploaded instead of the full folder, plus CSP headers blocking Google Fonts.

**Best Use of Gemini 3 [Google Deepmind]**

We used gemini

Team **Cosmic Titans** -- [Aditya Prakash Gupta](https://github.com/Aditya23011c), [Mratunjay Pandey](https://github.com/Mratunjaypandey), [Sishant Verma](https://github.com/Sishant-verma), [Soni Gautam](https://github.com/soni-hash)

`2026-03-15`

---

### AERO-H
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aeroh-2235) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anilove-23/AERO-H) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1wg_TNGL-xDOkodry5dRZx4FV2LpDBQbI/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Emerency app for medical support

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Multer](https://img.shields.io/badge/Multer-333333?style=flat-square)

**The problem it solves**

In medical emergencies, every second is critical, yet current emergency response systems are often slow, fragmented, and inefficient.

Many healthcare systems face several key challenges:

1️⃣ Delayed Emergency Response

When an emergency occurs, patients or bystanders often struggle to quickly report symptoms and find appropriate medical help. Delays in communication and decision-making can significantly worsen patient outcomes.

⸻

2️⃣ Lack of Intelligent Triage

Emergency systems usually rely on manual assessment or basic categorization, which may not accurately evaluate the severity of a patient’s condition. This can result in critical patients waiting too long for care.

⸻

3️⃣ Inefficient Resource Allocation

Hospitals, doctors, and ambulances are often dispatched without considering:
	•	Real-time availability
	•	Location proximity
	•	Hospital capacity
	•	Required medical specialization

This leads to ambulance delays, overcrowded hospitals, and inefficient use of medical resources.

⸻

4️⃣ Limited Accessibility During Emergencies

In stressful or critical situations, patients may not be able to type detailed symptoms. Many emergency systems lack voice-based reporting, making it harder for users to communicate quickly.

⸻

5️⃣ Lack of Predictive Healthcare Insights

Hospitals often struggle to anticipate future patient demand, which leads to:
	•	ICU bed shortages
	•	Overloaded emergency departments
	•	Poor preparation for sudden surges in patients
How AERO-H Addresses This

AERO-H introduces an AI-powered emergency coordination platform that:
	•	Uses AI to analyze symptoms and determine emergency severity
	•	Enables voice-based emergency reporting
	•	Allocates optimal hospitals, doctors, and ambulances
	•	Provides instant first-aid guidance
	•	Predicts hospital demand and resource availability

This creates a smarter, faster, and more efficient emergency response system.

**Challenges we ran into**

1️⃣ Reliable AI Response Handling

Integrating AI models such as Gemini into a real-time emergency workflow required careful handling of:
	•	API rate limits
	•	inconsistent response formats
	•	failure scenarios

To ensure system reliability, fallback mechanisms were implemented so that the platform can still process emergencies even if AI services are temporarily unavailable.

⸻

2️⃣ Speech-to-Text Integration

Building a voice-based emergency reporting feature introduced challenges such as:
	•	handling different audio formats
	•	ensuring reliable transcription
	•	managing file uploads and processing

The system was designed to support multiple audio types and fallback transcription methods to maintain usability.

⸻

3️⃣ Real-Time Resource Allocation

Allocating hospitals, doctors, and ambulances dynamically required coordinating multiple data sources in real time.

Challenges included:
	•	ensuring accurate availability status
	•	selecting optimal resources based on location
	•	maintaining system performance under multiple requests

⸻

4️⃣ Geospatial Resource Detection

Identifying the nearest ambulance required implementing geospatial queries and indexing, which involved:
	•	structuring location data correctly
	•	configuring geospatial indexes
	•	optimizing queries for performance

⸻

5️⃣ System Reliability and Fallback Design

Emergency systems cannot fail during critical moments.

To ensure reliability, the platform includes:
	•	AI fallback logic
	•	error handling for external services
	•	resource allocation fallbacks

This ensures that the system can continue operating even when some services fail.

**Electrothon 8.0 Winners**

AERO-H addresses a critical real-world problem—slow and inefficient emergency response systems. It uses AI-powered symptom analysis, voice-based emergency reporting, and intelligent resource allocation to quickly determine the severity of a medical situation and automatically assign the nearest ambulance, appropriate hospital, and available doctor.

By combining AI decision-making, real-time data, and predictive healthcare insights, AERO-H enables faster, smarter, and more accessible emergency response, demonstrating both technical innovation and strong real-world impact, which aligns with the goals of Electrothon.

**Requestly Track**

AERO-H involves multiple APIs and real-time emergency workflows, including AI triage, voice processing, and resource allocation. During development, Requestly helped simulate and debug different API scenarios by modifying requests and responses, allowing us to test fallback logic, error handling, and system reliability without changing backend code. This made it easier to ensure the emergency system behaves correctly even when external services fail or return unexpected responses.

**ElevenLabs**

AERO-H uses ElevenLabs to generate clear, human-like voice instructions during emergencies. After AI analyzes the patient’s symptoms and determines the priority of the situation, the system converts the generated emergency guidance into audio. This allows patients or bystanders to receive immediate spoken instructions and updates, such as first-aid guidance and confirmation that an ambulance has been dispatched, making the system more accessible and useful in high-stress situations where reading text may not be practical.

**Best Use of Gemini 3 [Google Deepmind]**

AERO-H uses Gemini as the core intelligence layer of the system. Gemini analyzes emergency symptoms, determines severity and priority, recommends medical specialization, and generates first-aid guidance in real time. It also powers voice-based emergency reporting by converting spoken audio into structured medical symptoms. By integrating Gemini into multiple stages of the emergency workflow, AERO-H demonstrates how generative AI can support faster medical decision-making and improve emergency response systems.

Team **Code for Bugs** -- [Anilove k](https://github.com/anilove-23), [Shreyans Jain](https://github.com/Shreyans18-art), [Tanisha Chandok](https://github.com/tchandok30)

`2026-03-15`

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

### OptiPay Health AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/optipay-health-ai-7bb9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/masoomul786/OptiPay-Health-AI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=6ogy24CzSmo) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> From prescription to full health, automated by AI

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![TailWindCSS](https://img.shields.io/badge/TailWindCSS-333333?style=flat-square) ![LMStudio](https://img.shields.io/badge/LMStudio-333333?style=flat-square) ![Locus](https://img.shields.io/badge/Locus-333333?style=flat-square)

**The problem it solves**

## 🧾 The Problem It Solves

**Healthcare today is fragmented, expensive, and inefficient.**

After receiving a prescription, patients must manually navigate multiple disconnected systems:

* 🔍 **Overpaying for Medicines**  
  Users check multiple platforms yet still fail to find the lowest prices.

* 🍽️ **No Actionable Diet Guidance**  
  Prescriptions do not translate into practical food or nutrition decisions.

* 🛒 **Fragmented Purchasing Flow**  
  Medicines, groceries, and meals exist in separate ecosystems with no coordination.

* 💳 **Friction in Payments**  
  Users must repeatedly switch platforms and payment systems.

* ⚠️ **Lack of Intelligent Decision-Making**  
  No system actively optimizes cost, safety, and health outcomes in a single flow.

---

👉 **Core Gap:**  
There is no intelligent system that can **understand a prescription and take financial + health actions automatically.**

👉 This gap represents both a **health problem and a financial inefficiency problem.**

---

## 🚀 What People Can Use It For

**OptiPay Health AI is an autonomous AI health agent that autonomously converts prescriptions into optimized decisions and executes them end-to-end.**

Users can:

### 🧠 Understand & Interpret Prescriptions

* Extract medicines, conditions, and deficiencies automatically  
* Get simplified insights instantly  

### 🥗 Generate Actionable Health Plans

* Personalized diet aligned with medical needs  
* Avoid harmful foods and allergens  

### 🛍️ Optimize Purchases Across Platforms

* Compare prices across pharmacies and grocery stores  
* Automatically select the **lowest-cost valid options**  

### 💳 Execute Payments Instantly

* Complete the entire purchase in one step via Locus Pay  
* No manual checkout across multiple apps  

### 🤖 Enable Autonomous Health Management

* Activate autopilot mode for recurring orders  
* Let the system manage health needs continuously  

---

## ⚡ How It Makes Tasks Easier, Safer & More Cost-Efficient

### 💰 Saves Money (Core Hackathon Focus)

* Automatically selects the cheapest medicines and foods  
* Reduces unnecessary spending across platforms  

### ⏱️ Saves Time  

* Converts a multi-step process into a **single AI-driven flow (~60 seconds)**  

### 🛡️ Improves Safety  

* Detects allergies  
* Avoids harmful food–medicine combinations  
* Aligns diet with treatment  

### 🤖 Introduces True AI Agent Behavior  

Instead of just giving suggestions, the system:

* analyzes  
* decides  
* optimizes  
* **executes transactions**  

### 🔗 Unifies the Entire Flow  

Combines:  
**Healthcare + Nutrition + Commerce + Payment → One Intelligent System**

---

## 🎯 Summary

**OptiPay Health AI is not just a health assistant — it is an AI agent that transforms prescriptions into optimized, cost-efficient, and fully executed health decisions.**
**It actively reduces healthcare costs by making optimized purchasing decisions and executing them autonomously.**

**This is not just AI assistance — it is AI execution.**

**Challenges we ran into**

## ⚠️ Challenges I Ran Into

### 🤖 AI Output Consistency  
**Problem:** AI sometimes returned unstructured or inconsistent responses.  
**Solution:** Enforced strict JSON output via prompt engineering and added backend validation + fallback mock responses to ensure reliability.

---

### 🧠 Medicine → Diet Mapping  
**Problem:** Generating accurate diet plans based on medicines was complex.  
**Solution:** Designed rule-based prompts (e.g., iron → iron-rich foods + vitamin C) with constraints for allergies and preferences.

---

### 💳 Locus Pay Integration  
**Problem:** Faced issues with incorrect API endpoints and handling transaction states.  
**Solution:** Fixed API usage (`/pay/send`), corrected base URL, and handled `PENDING_APPROVAL` properly. Also added a Demo Mode for safe testing.

---

### 🛍️ Price Optimization Logic  
**Problem:** Comparing prices across multiple stores efficiently.  
**Solution:** Built a unified system to fetch, sort, and auto-select the cheapest valid options with allergen filtering.

---

### ⚙️ End-to-End Flow  
**Problem:** Managing smooth data flow across AI → cart → payment.  
**Solution:** Used centralized state management and fallback handling to ensure a seamless experience.

---

## 🎯 Key Takeaway

**The biggest challenge was making a complex multi-step system work as a single autonomous AI agent — reliably, in real time.**

**Track: Using BuildWithLocus to leverage our suite.**

I built OptiPay as a **complete showcase of Locus Payment infrastructure**. Rather than just accepting payments, we utilize **3 core Locus integrations** where removing any one breaks a critical feature.

**1]. Locus Infrastructure (BuildWithLocus):**
- Deployed via `.locusbuild` configuration
- React Vite frontend + Python FastAPI backend
- Dynamic port wiring using Locus URL templates

**2]. Locus Pay & Autonomous Payments:**
- **`POST /pay/send`** — AI autonomously executes USDC payments on Base network after prescription analysis
- **`GET /pay/balance`** — Verifies wallet has sufficient funds before transaction
- **Error Handling** — Managed HTTP codes (401 invalid key, 403 spending limit, 429 rate limit)

**3]. Locus Wallet Management:**
- Real-time balance tracking dashboard
- Transaction history per order
- Multi-transaction orchestration (medicines + groceries + food delivery = 1 payment)

**Result:** Autonomous healthcare agent powered entirely by Locus. Each integration is essential—remove Locus Pay and the autonomous payment system collapses.

**Status:** ✅ Live Locus API integration | ✅ Real USDC on Base | ✅ Production-grade error handling

---

Masoomul Haque

`2026-04-23`

---

### Rakshak AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rakshak-ai-02f8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prachikumari850/rakshakai-clean) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/UEmd27nRr8M?feature=shared) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your 360 health emergency shield

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

# 🛡️ Rakshak AI — Your 360° Health Emergency Shield

A real-time healthcare emergency platform with AI risk prediction, SOS alerts, QR medical passports, and Google Fit integration.

## Features
- 🧠 **Health Risk Prediction** — Rule-based scoring using BMI, age, lifestyle + Google Fit data
- 🚨 **SOS Emergency** — One-click alert with live GPS via Socket.io
- 🪪 **Medical Passport** — QR code linking to your emergency medical profile
- 🗺️ **Hospital Finder** — Live map using Leaflet.js + OpenStreetMap (free)
- 📈 **Recovery Tracker** — Daily vitals logging with trend charts
- 🏃 **Google Fit Sync** — Steps, heart rate, and sleep via OAuth 2.0

## Tech Stack
`React` `Node.js` `Express` `MongoDB` `Socket.io` `Google Fit API` `Leaflet.js` `JWT` `Recharts`

## Quick Start
```bash
# Backend
cd backend && npm install && npm run dev

# Frontend
cd frontend && npm install && npm run dev
```

## Environment Variables

**`backend/.env`**
```env
PORT=5000
MONGO_URI=your_mongodb_atlas_uri
JWT_SECRET=your_secret_key
CLIENT_URL=http://localhost:5173
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

**`frontend/.env`**
```env
VITE_API_URL=http://localhost:5000/api
VITE_SOCKET_URL=http://localhost:5000
VITE_GOOGLE_CLIENT_ID=your_google_client_id
```

## Deploy
- **Frontend** → [Vercel](https://vercel.com)
- **Backend** → [Render](https://render.com)
- **Database** → [MongoDB Atlas](https://mongodb.com/atlas)

## Google Fit Setup
1. Enable **Fitness API** in Google Cloud Console
2. Create OAuth 2.0 credentials (Web Application)
3. Add redirect URI: `http://localhost:5173/fit-callback`

---
*Built for India's healthcare emergency needs* 🇮🇳

Team **Unfazed X** -- [Prachi Kumari](https://github.com/prachikumari850), [Pihu Singhal](https://github.com/pihusinghal), [Pragya Snehi](https://github.com/pragya-snehi)

`2026-04-04`

---

### RenQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/renq-43bc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Waseemhussain11/Quantum-Drug-Discovery) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/KqhOxkaQuXM?si=nrWtqVTmO5P8L-ab) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Stimulate drug ,predict drug,discover drug"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Drug discovery is one of the most expensive, time-consuming, and failure-prone processes in modern science. On average, bringing a single drug to market can cost billions of dollars and take over a decade, with a high failure rate during early-stage screening.
One of the critical challenges is identifying whether a molecule can effectively inhibit a biological target (like BACE-1 for Alzheimer’s disease) before expensive lab testing begins.

**Challenges we ran into**

1.Quantum models (QSVM with ZZFeatureMap) are computationally expensive and slow, especially when scaling beyond small datasets.
2.Combining outputs from XGBoost and Quantum SVM in a meaningful way was non-trivial due to differences in prediction distributions
3.Converting SMILES data into meaningful numerical representations while preserving chemical properties.
4.Real-time predictions were slow due to heavy computation in backend pipelines.

**Open Innovation**

A state-of-the-art drug discovery platform that leverages Hybrid Quantum-Classical Machine Learning to predict the inhibition of BACE-1 (Beta-secretase 1), a critical enzyme implicated in Alzheimer's disease.

Team **Team Tech innovators** -- [Jeet Verma](https://github.com/jeetver1809), [Hemanth Kumar Musirana](https://github.com/HemanthKumarMusirana), [WaseemHussain Abdul](https://github.com/Waseemhussain11), [Narayan Naidu Maddina](https://github.com/nandu3153)

`2026-03-29`

---

### PollyRoutes
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pollyroutes-b405) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Debzoti/anti-pollution-routes) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=zgNbamREZgs&sttick=0) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Pollution-aware navigation for healthier journeys.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

PollyRoutes addresses the critical issue of urban air pollution exposure during daily commutes by empowering citizens to make informed, health-conscious travel decisions—existing navigation apps optimize only for time and distance, ignoring air quality, leaving commuters unknowingly exposed to high pollution zones that contribute to respiratory diseases and long-term health issues, particularly affecting vulnerable populations like children, elderly, and those with pre-existing conditions.

**Challenges we ran into**

We encountered significant technical hurdles including API rate limiting when fetching real-time environmental data for multiple route coordinates, requiring us to implement intelligent sampling strategies and coordinate-level caching to balance data accuracy with API constraints; integrating multiple heterogeneous data sources (AQI, weather, traffic) with varying data formats, update frequencies, and geographic coverage; handling sparse environmental monitoring station data by developing interpolation techniques; and optimizing the Pollution Exposure Score algorithm to account for complex factors like wind direction, traffic congestion, and travel time while maintaining real-time performance for a responsive user experience.

**Open Innovation**

PollyRoutes fits the Open Innovation track because it integrates multiple open-source technologies and public APIs (Ola Maps, OpenWeatherMap, OpenAQ, TomTom Traffic) to create a novel solution that addresses urban air pollution through intelligent routing. The project leverages openly available environmental data, combines it with real-time traffic and weather information, and applies an innovative Pollution Exposure Score (PES) algorithm to help citizens make healthier travel choices. By making this solution open-source and API-driven, it enables collaboration, allows other developers to build upon the platform, and promotes data transparency in addressing public health challenges—embodying the core principles of open innovation where diverse data sources and technologies converge to solve real-world problems collaboratively.

Team **The yappers** -- [Pratyay Mustafi](https://github.com/Pratyay360), [Debjyoti Sarkar](https://github.com/Debzoti), [Haresh Khan](https://github.com/hareshkhan01)

`2026-03-22`

---

### NovaPulse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/novapulse-49d7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arkoparno/NovaPulse) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nova-pulse-chi.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vZGm30CaeEw?si=MAVG24FRZQvNxZho) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Contactless Health Triage Platform

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![ONNX](https://img.shields.io/badge/ONNX-333333?style=flat-square) ![Vanilla JS](https://img.shields.io/badge/Vanilla%20JS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Mediapipe](https://img.shields.io/badge/Mediapipe-333333?style=flat-square)

**The problem it solves**

Over 600 million rural Indians lack access to basic diagnostic equipment. A pulse oximeter, ECG machine, or HRV monitor can cost thousands of rupees and require trained operators — making early cardiac and stress triage nearly impossible at the last mile of healthcare.
NovaPulse turns any phone or laptop camera into a contactless vitals monitor. In 25 seconds, using only ambient light and a standard RGB camera, it extracts:

Heart Rate via CHROM rPPG signal processing
AFib Risk via Poincaré Plot geometry + Shannon Entropy
Stress Level via HRV RMSSD quantification
Autonomic Balance via Goertzel LF/HF frequency analysis
Arterial Stiffness via pulse waveform AIx morphology

Zero hardware. Zero app install. Zero data leave the device. Every algorithm traces to a peer-reviewed paper with a named dataset

**Challenges we ran into**

The signal we're extracting is less than 0.5% of total pixel brightness. Everything else — lighting flicker, breathing, minor head movement — is louder than the heartbeat itself.
The first real wall we hit was the CHROM implementation producing clean-looking but completely wrong output. MediaPipe returns normalized 0–1 landmark coordinates. We weren't multiplying by video dimensions consistently, so the forehead ROI was silently drifting by 200–300 pixels across frames. The signal looked like it was working until we drew the extraction box on screen and saw it tracking the ceiling.
Peak detection was our next headache. Early builds had a false peak rate of roughly 30–40% on cheap webcams in dim light — beats getting double-counted or missed entirely. We tightened the prominence threshold, added a 400ms refractory gate, and ran a post-filter that removes any peak pair producing a physiologically impossible IBI under 300ms or over 1500ms. That brought the error rate down to under 8% in normal conditions.
AFib confidence was the sneakiest bug. Shannon entropy on a 20-IBI sequence is naturally elevated just from small sample statistics — not from actual arrhythmia. The classifier was reporting high-confidence AFib on healthy rhythms with short sequences. We built an adaptive confidence cap tied to sample size. Under 20 IBIs the system returns insufficient data. CONCERN is never displayed below 40% confidence regardless of feature scores.

**Best Beginners' Team**

None of the four of us had ever competed in a hackathon before Binary v2. No prior submissions. No previous Devfolio profiles with projects. This is the first time all four of us sat down together under a deadline and built something from scratch.
That context matters because NovaPulse wasn't built by people who knew what they were doing from day one. It was built by four first-year and second-year students who had never implemented a signal processing pipeline, never touched MediaPipe, never written a Butterworth IIR filter, and had no prior experience with rPPG literature. We started by reading papers. We spent the first few hours just understanding what CHROM actually does mathematically before writing a single line of code.
The learning curve was steep and completely self-directed. There was no senior team member who had done this before. When the forehead ROI was silently drifting because we weren't multiplying normalized MediaPipe coordinates by video dimensions, nobody on the team immediately knew why the signal looked wrong. We debugged it ourselves by drawing the extraction box on screen and watching it track the ceiling instead of the forehead. That's a beginner mistake caught through beginner persistence.
The AFib confidence bug, the phase lag from the moving average, the false peak rate on cheap webcams — every one of those problems was encountered and solved for the first time by this team, at this hackathon, with no prior reference point.
What makes this Best Beginners' submission isn't that the project is simple. It's that four people who had never done any of this before figured out how to do all of it in under 36 hours.

**Healthcare**

India has roughly 1 doctor per 1500 people in rural areas. A patient presenting with palpitations or fatigue has no realistic path to an ECG, pulse oximeter, or HRV monitor without traveling hours to a city. By the time they get there, the moment has passed or become an emergency.
NovaPulse removes the hardware dependency entirely.
A health worker with a ₹5000 Android phone runs a 25-second contactless scan and generates a clinical-format triage report covering seven physiological markers — heart rate, cardiac rhythm, AFib risk, stress level, autonomic balance, arterial stiffness, and peripheral perfusion. No finger clip. No chest electrodes. No app install. Nothing leaves the device.
The clinical grounding is specific. The AFib classifier is validated against the MIT-BIH Arrhythmia Database. HRV thresholds come from the Task Force ESC/NASPE 1996 study on 857 subjects. Perfusion index ranges from a 100-patient ICU dataset. Every threshold has a published source behind it.
The report exports as a PDF, shareable over WhatsApp in seconds. A remote doctor can triage whether a patient needs urgent referral or routine follow-up — without either party needing anything beyond a phone.
This is not a wellness app. It is a first-contact triage tool built for the healthcare access gap affecting 600 million rural Indians. That is precisely what this track exists for.

Team **Nova** -- [ARKOPARNO DAS](https://github.com/Arkoparno), [Prithibe Majumder](https://github.com/24f2007601), [Srijit Roy](https://github.com/Srijit4514), [Anushka Verma](https://github.com/aceholland)

`2026-03-22`

---

### Breast Cancer Classification with Explainable AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/breast-cancer-classification-with-explainable-ai-420d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ArnabH2004/breast-cancer-xai.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/cbf20869fd6343acab2e75916a05eabf) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/cbf20869fd6343acab2e75916a05eabf) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Accurate diagnosis meets explainable intelligence.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Our project simplifies breast cancer diagnosis by using AI to accurately classify medical images while providing visual explanations through Grad-CAM. This ensures faster, more reliable, and transparent decision-making for healthcare professionals.

**Challenges we ran into**

During development, we faced multiple challenges across both the model and deployment stages. One major issue was handling medical image preprocessing, as inconsistent image sizes and quality affected model performance. We resolved this by applying proper normalization, resizing, and augmentation techniques.

Another challenge was integrating Explainable AI using Grad-CAM with our ResNet50 model. Initially, the heatmaps were not aligning correctly with the regions of interest. After debugging the model layers and selecting the appropriate convolutional layer, we were able to generate meaningful visual explanations.

We also encountered environment and dependency issues while setting up the project using Docker and managing Python packages. This was resolved by carefully configuring the environment and ensuring compatibility across all libraries.

Overall, these challenges helped us improve the robustness, interpretability, and usability of our system.

Team **MindForge** -- soham santra, Suman Mandal, Arnab Hazra, Indrajit Roy

`2026-03-17`

---

### HealthPulse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthpulse-7f80) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://champsparshsingh.github.io/v0-healthcare-dashboard/dashboard) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI powered hypertension management

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

In current world, millions of patients own primitive blood pressure monitors that store data locally or on paper. No connectivity. No alerts. No safety net. Moreover, if a patient experiences high bp levels, there is no immediate care available. 

So, here we a team of 3 joint hands together to form a website for these problems.
Our website currently includes manual way of adding your bp which would be directly connected to doctor's portal and if there is an emergency, doctor can easily treat the patient...
In future we are planning to make this an app and add family members in that app so that they are also notified about hypertension of any family member. 
This project currently shows trend of BP by manual entries 3 times a day over a week by presenting a graph...
We are also planning to add bluetooth modules in machines to easily get data automatically from machine itself.

**Challenges we ran into**

I searched upon a hardware-software bridge architecture using ESP32 microcontrollers. I researched non-invasive methods like OCR (Optical Character Recognition) via ESP32-CAM to read "dumb" LCD screens and transmit data via Bluetooth Low Energy (BLE) to the dashboard.

I developed a clinical logic engine based on hypertension guidelines. I implemented a system that maps systolic and diastolic inputs to specific risk tiers (Low, Normal, Elevated and High) in real-time.

Earlier I hadn't worked upon GitHub so I had to research about how to push codes in that. 
I had a lot of errors in coding as I had a little experience of front end.
I had tried to include family part and show it as a popup but instead I got repeated errors so I was able to push codes but it isn't showing in the website as such.
I had to correct my UI multiple times on the basis of reviews from peers and family members so as to find perfect colour scheme...

**Electrothon 8.0 Winners**

I used Health care theme.

**Electrothon 8.0 Honors Track**

Best Beginner Hack

Team **CODE HACKERS** -- [Sparsh Singh](https://github.com/champsparshsingh), [Siddhant Kapoor](https://github.com/siddhant952005-eng), [Vanshika Vanshika](https://github.com/25bme115-alt)

`2026-03-15`

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

### BioSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/biosense-4de7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/QIQVincent/biosense) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/e1-UzrDLAGk) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> AI-powered biometric health aggregator

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Use of Genspark**

We attempted to use Genspark Build with Opus to accelerate the initial app generation but encountered issues with the agent completing the full application. We pivoted to building entirely with Claude AI via Claude Code.

**How you are solving it**

BioSense ingests data from four wearables (Apple Watch, Oura Ring, Whoop, Muse) and surfaces unified insights through a React dashboard. It scores health across 4 dimensions (HRV, sleep, recovery, stress) with RED/AMBER/GREEN traffic-light status, detects anomalies across 20+ metrics, and generates rule-based recommendations. Stack: Node.js + Express + SQLite + React + Recharts + Tailwind CSS, deployed on Vercel.

**What is the deployed URL for this project?**

https://diagnostic-gold.vercel.app

**Use of Claude**

Claude AI (via Claude Code) was used to build BioSense from the ground up — architecture, feature development, bug fixing, and deployment. We used targeted prompts to generate the Express backend, SQLite schema, React frontend, health scoring algorithm, and Vercel deployment setup.

**The problem your project solves**

Internal health and wellness monitoring for teams is fragmented across multiple wearable devices with no unified dashboard. Teams lack visibility into biometric signals — HRV, sleep quality, recovery, and stress — that directly impact productivity and burnout. Without a centralized tool, these signals stay siloed and never become actionable.

**Hackathon Prizes**

General

Team **Futurists** -- [shaowei png](https://github.com/shaoweipng), [Kuan yew Yong](https://github.com/Nil), [Vincent Ho](https://github.com/QIQVincent)

`2026-04-24`

---

### PTPh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ptph-a373) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Xateh/PTPh) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/dd2594d615bc4e7aaf63d098959d05a6) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> Medical Helper

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**Use of Claude**

Patient analysis & internal agent

**The problem your project solves**

Problem statements

- Healthcare workers need to take extra time to note and make reports **when handing off a patient to the next shift specialist**  
  - Requires recounting information that may be distracted from other situations  
  - Delays in information on critical things  
  - Timeline may be inaccurate  
  - Not remembering all information  
    → to make sure no missing, they go through a ward twice a day (in Japan)  
    ↔ still, juniors forget to ask important questions :(  
- **Not knowing what information the next doctor might need**  
  - The core reason handoff **in person** exists: the doctor taking the shift might have specific questions, which is not explicitly recorded in ER  
  - AI is able to see the missing bits / capture & retrieve more information than in ER  
  - AI will be asking questions until it’s sure that it has grasped 99% of the previous doctor’s “context” about the patient

    → can be 

**Our solutions**

- **Holding the context of the previous doctor within an agentic system**  
  - The doctor now does the handoff **to the AI system**, that aims to be **as inquisitive (collects data points about patient data, diagnoses, and treatment strategy) as** **the next doctor taking the shift**  
  - Every **important bit of knowledge** that the **AI assumes has to go through the verification pipeline:**  
    - Presented for verification to the doctor as a list of bullet points spanning the knowledge space  
    - The doctors goes through bullet points  
    - Options presented to the doctor: **Accept**, **Accept with modification, Reject**  
    - Approved points act as a **single source of ground truth**  
  - Important: **AI doesn’t invent the knowledge; it collects it from the doctor** through **point-by-point validation** and the **follow-up questions** (that AI believes (through deep thinking analysis) that this information is missing yet the next doctor might need it)  
  - The next doctor then communicates with the system, thus allowing the previous doctor to be dismissed earlier  
- Enable voice inputs for the healthcare workers  
- Notes down in the moment (preferably always on)  
  - Need to respect the patient data privacy  
  - Accuracy: ask approval for important points  
    ↔ can also store unapproved transcripts, as it can be helpful in future in case no other information is available  
- Need to harness and **avoid adding additional information**  
- Provide suggestions for doctors on the subsequent (e.g., before visit of each patient in rounds)

Benefits:

- Less information loss for handsoff  
- Less manpower for handsoff  
- More effective collection of patient information – by (i) lesser duplication overhead and (ii) timely reminder of patient information (e.g., personality & latest news) before each visit  
- Less memory needed after handsoff – information sharing can be done before each patient visit instead of in the morning, reducing the amount of long-term memory

Restrictions:

* Can’t come up with knowledge  
* Can’t assume; everything that AI wants to assume has to be verified via a follow up question  
* Can’t add knowledge to the knowledge base unless explicitly verified by the doctor  
  * Even an interaction transcript doesn’t constitute a valid knowledge source as it might contain transcription errors  
* Every factual statement (that AI produces to the doctor taking over the shift) should have a reference to the bullet points that were **explicitly approved** by the previous doctor  
  * In the case of knowledge can’t be verified through the approved knowledge base but is still **present within the unstructured data** (transcripts, journals, logs), (expected to be in \<5% of cases, 95% of knowledge should be verified), the agent flags it and provides the reference to wherever the knowledge was taken from

The interaction pipeline:

* During the round  
  * Before the doctor visits the patient in the ward: the system reminds the doctor of their personality, latest news on them (e.g., treatments, consideration), and potentially beneficial things to ask  
  * During the doctor’s visit: the transcript is auto-generated via voice; important parts were extracted by the system, and the **doctor is asked to verify them**  
  * The system “interviews” doctors to get more insights into the diagnoses, treatment plan, strategy, and anything else that should be extracted and handed over.  
  * The system can handle emergencies, which requires prompt information retrieval  
* At the time the doctor finishes their shift (after the round)  
  * The system finalizes the knowledge and ask the doctor the final questions  
* At the time the new doctor comes in  
  * At this moment, for each patient, the system has access to transcripts (with important information verified), treatment logs, journals, the previous doctors’ decision notes, etc. (unstructured data)  
  * For each patient, the system generates a summary for the new doctor, focusing on changes recently

**Use of Genspark**

Audio transcription & patient analysis

**What is the deployed URL for this project?**

https://pt-ph.vercel.app?_vercel_share=QMode8krApfi9v4HSj3wl7c8JjmnPfLU

Team **one_day_to_final_exam** -- [Roman Yanushevskyi](https://github.com/wailydest), [Hibiki Nishiwaki](https://github.com/h-b-k-nishi), [XuAn Teh](https://github.com/Xateh)

`2026-04-24`

---

### VisionCare AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/visioncare-ai-3238) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> “Smart screen. Healthy eyes.”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Our solution is designed to help users manage their screen usage at night and improve overall sleep quality. It can be used for:

1.Reducing insomnia caused by late-night screen exposure
2.Minimizing eye strain through automatic blue light adjustment
3.Practicing relaxation using guided meditation sessions
4.Improving sleep readiness with calming music
5.Tracking digital habits via weekly screen-time reports

**Challenges we ran into**

Screen Color Adjustment Limitation

Problem:
One of the biggest challenges was implementing automatic screen color changes (mild blue at 10 PM and deeper blue at 12 AM). Browsers do not allow direct control over system-level screen color or blue light settings.

Solution:
We overcame this by applying a CSS-based overlay filter that simulates blue light reduction. Using JavaScript timers, we dynamically changed the overlay intensity based on time, giving a similar effect to native night mode.

Accurate Time-Based Triggers

Problem:
Ensuring that the screen changes happen exactly at the right time (10:00 PM and 12:00 AM) was tricky, especially when users keep the app open for long durations.

Solution:
We implemented a real-time clock check using JavaScript (setInterval), which continuously monitors the system time and updates the UI instantly when conditions are met.

**Track: Using BuildWithLocus to leverage our suite.**

While building this project, we faced several challenges. One major issue was that browsers do not allow direct control over system-level blue light or screen color settings. To overcome this, we implemented a CSS-based overlay filter that simulates the blue light reduction effect.

Another challenge was ensuring accurate time-based triggers at exactly 10 PM and 12 AM. We solved this by using a real-time monitoring approach with JavaScript (setInterval) to continuously check the system time and apply changes instantly.

Team **Innovators** -- A. Sadhana, Janani V, Kamala Ekambaram

`2026-04-21`

---

### ABHA-Integrated Clinical Middleware
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/abhaintegrated-clinical-middleware-eb72) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PranavHarlalka/abha-middleware-hackathon.git) [![Built at](https://img.shields.io/badge/Built%20at-DAYZERO%202.0-0052CC?style=flat-square)](https://dayzero2o.devfolio.co)

> ABHA-Integrated Clinical Middleware

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Spring Boot](https://img.shields.io/badge/Spring%20Boot-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

Team **Cache & Care** -- [Mugdha Narayan](https://github.com/mn8292-dev), [Pranav Harlalka](https://github.com/PranavHarlalka)

`2026-04-16`

---

### NutriWise
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nutriwise-4133) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ritikkumar27/fuzzydevs_nutriwise.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nw56OtT4o60) [![Built at](https://img.shields.io/badge/Built%20at-DAYZERO%202.0-0052CC?style=flat-square)](https://dayzero2o.devfolio.co)

> Decode Your Food. Transform Your Health.

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

PROBLEM STATEMENT:
People struggle to make informed and personalized dietary decisions because nutritional information is either hard to access, difficult to understand, or not tailored to individual health conditions.

Explanation;
Information Gap
Most users don’t understand nutrition labels or ingredient impacts.
Lack of Personalization
Existing apps give generic advice, not tailored to:
diseases (diabetes, hypertension)
allergies
fitness goals
No Real-Time Guidance
Users make food choices instantly (shopping/eating), but:
analysis is delayed or manual
no immediate feedback
Fragmented Experience
Tracking, analysis, and recommendations are in separate apps or tools
Health Risks
Poor food choices can worsen chronic conditions due to lack of awareness

👉 “Lack of real-time, personalized nutrition guidance makes it difficult for individuals to make healthy and safe dietary choices.”

**Challenges we ran into**

1.  Accurate Nutrition Data Retrieval
Finding reliable and consistent nutrition data for Indian food items was difficult
Barcode databases were often incomplete or inconsistent
Had to handle missing or incorrect nutritional values

2.  AI Response Consistency (Gemini Integration)
AI responses were sometimes:
Too generic
Not aligned with user health conditions
Required careful prompt engineering to get:
personalized
medically relevant outputs
Balancing AI creativity vs factual accuracy was tricky

3.  Combining Rule-Based Logic with AI
Designing a system where:
Rule engine gives deterministic safety checks
AI gives contextual recommendations
Avoiding conflicts like:
Rule says “Avoid” but AI says “Moderate”
Needed a clear priority system (rules > AI)

4.  Barcode Scanning Reliability
Camera scanning issues:
Low light conditions
Blurry scans
Unsupported barcodes
Needed fallback:
manual input option

5.  Personalization Complexity
Handling multiple user factors:
diseases
allergies
fitness goals
Creating a flexible user profile model that scales was challenging

6. User Experience & Simplicity
Making a complex system feel simple:
Not overwhelming users with too much data
Presenting insights in an actionable way

7. Time Constraints (Hackathon Reality)
Building:
frontend + backend + AI + logic engine
within limited time
Prioritizing:
core features over perfection

Team **FuzzyDevs** -- [Ritik Kumar](https://github.com/ritikkumar27), [Swapnendu Karmakar](https://github.com/swapnendu-karmakar), [Shrey Patil](https://github.com/ShreyPatil1003), [Yash Kumar](https://github.com/belezerio)

`2026-04-17`

---

### MindSpace AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mindspace-ai-6db1) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/_PoytXdVeVY?si=YsnhJoG-r3IhnC9J) [![Built at](https://img.shields.io/badge/Built%20at-Off--Grid-0052CC?style=flat-square)](https://offgrid.devfolio.co)

> A mental health AI application ,your therapy buddy

![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Apache Maven](https://img.shields.io/badge/Apache%20Maven-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square)

**The problem it solves**

Mental health is one of the most ignored yet critical issues today, especially among students and young professionals. Many people struggle silently because they either don’t have immediate support or hesitate to share their feelings due to fear of judgment and lack of privacy.

Our solution, MindSpace AI, creates a safe and accessible digital space where users can express their emotions freely, track their mental state, and receive support instantly. The platform combines AI-driven insights with human-like interaction to provide both immediate assistance and emotional connection.

Users can analyze their thoughts, track moods and habits, and interact through an AI chatbot or anonymously with others facing similar challenges. This ensures that even if someone doesn’t have access to professional help, they are never truly alone.

By focusing on privacy, accessibility, and emotional support, MindSpace AI aims to reduce stigma around mental health and provide a scalable solution that can be used anytime, anywhere.

**Challenges we ran into**

Building this project was both exciting and challenging, especially because the tech stack — Spring Boot for backend and Flutter for frontend — was completely new to me. Learning how to structure a full-stack application, handle API integrations, and manage state between frontend and backend in such a limited time was a major challenge.

One of the key difficulties was debugging real-time integration issues. While APIs were working perfectly in Postman, connecting them seamlessly with the Flutter frontend required careful handling of headers, tokens, and network configurations. Issues like authorization errors, incorrect request formats, and device-based networking (emulator vs real device) took time to identify and fix.

Another challenge was designing a smooth and engaging user experience while maintaining performance. Implementing features like AI chat simulation, anonymous interaction, and dynamic UI responses required balancing logic with design.

Additionally, building a meaningful mental wellness experience rather than just a technical product pushed me to think more from a user’s perspective — ensuring the app feels supportive, safe, and intuitive.

Overall, this project pushed me out of my comfort zone, helped me learn new technologies rapidly, and improved my problem-solving and debugging skills significantly.

Team **LearnX** -- [Parth Patel](https://github.com/Createaneww), [ADITYA GUPTA](https://github.com/AdityaGupta139), [Praful Bajpai](https://github.com/prafulbajpai)

`2026-04-11`

---

### AI-Based Crop Health & Pest Risk Predictor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aibased-crop-health-and-pest-risk-predictor-e3cb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/akshay-paramanik/RunnerExpo-Hackathon-Crop-health-and-pest-risk-predictor-.git) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co)

> Smarter Crops, Better Yields.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Google Colab](https://img.shields.io/badge/Google%20Colab-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

🌾 AI-based Crop Health & Pest Risk Predictor

An intelligent agriculture system that combines IoT, Satellite Data, Weather APIs, and AI (CNN + LSTM) to provide real-time crop monitoring and future risk prediction for farmers.

🚜 Problem Statement

Farmers often rely on manual observation and delayed data to monitor crop health. This leads to:

Late detection of pests and diseases
Poor irrigation decisions due to uncertain rainfall
No predictive insights about crop health
Reduced yield and financial loss
💡 Solution

This system provides:

📡 Real-time monitoring using sensor data
🛰️ Crop health tracking using NDVI (satellite data)
🌦️ Rainfall prediction using weather APIs
🐛 Pest detection using CNN (image analysis)
🔮 Future crop health prediction using LSTM
⚙️ Smart decision engine for actionable recommendations
⚙️ How It Works
ESP32 Sensors (5 min data)
        ↓
MongoDB (Data Storage)
        ↓
Node.js Backend
        ↓
        ├── CNN Model (Image → Pest Detection)
        ├── LSTM Model (24-step data → Future NDVI)
        ↓
Decision Engine (Rules + AI)
        ↓
React Dashboard (User Interface)
🔄 System Flow
Sensor data (temperature, humidity, soil moisture) is collected every 5 minutes
Weather API provides rainfall forecast
Satellite provides NDVI (crop health index)
User uploads crop image → CNN detects disease
Backend fetches last 24 data points → sends to LSTM
LSTM predicts future NDVI (crop health trend)
Decision engine generates actions
Results shown on dashboard
🧠 AI Models
🔹 CNN (Convolutional Neural Network)
Input: Crop image
Output: Disease type + confidence
Purpose: Detect pest/disease
🔹 LSTM (Long Short-Term Memory)
Input: Last 24 time steps

Features:

[temp, humidity, soil, rain, ndvi, pest]
Output: Predicted NDVI
Purpose: Predict future crop health
📊 Example Output
{
  "current_ndvi": 0.62,
  "predicted_ndvi": 0.48,
  "risk": "HIGH",
  "pest": {
    "disease": "leaf_blight",
    "confidence": 0.85
  },
  "actions": [
    "Spray fungicide immediately",
    "Skip irrigation (rain expected)",
    "Monitor crop closely"
  ]
}
🛠️ Tech Stack
🌐 Frontend
React.js
🧠 Backend
Node.js + Express.js
MongoDB
🤖 AI/ML
Python (Flask)
TensorFlow / Keras
Scikit-learn
🌍 APIs & Data Sources
OpenWeather API
Satellite NDVI data

⚡ Key Features
Real-time + predictive insights
Multi-source data integration
AI-driven decision making
Farmer-friendly dashboard
Scalable architecture

🎯 Impact
Reduces crop loss
Improves decision-making
Saves water and pesticide usage
Enables smart farming
🔮 Future Improvements
Mobile app for farmers
Multilingual support
Government scheme integration
Advanced pest classification

**Challenges we ran into**

1. Hardware Integration (ESP32 + Sensors)

One of the biggest challenges was integrating ESP32 with soil moisture and DHT11 sensors and ensuring reliable data transmission.

Faced issues like:
Inconsistent sensor readings
Network delays and API failures
Data not syncing properly with backend

How I solved it:

Implemented data validation and filtering before sending to backend
Used retry mechanisms for API calls
Structured the data flow to ensure consistent 5-minute interval updates
🧠 2. AI Model Design (CNN + LSTM)

Designing AI models that actually work together was challenging.

Problems faced:
Confusion on how to combine CNN (image) and LSTM (time-series)
Handling multiple data sources (sensor, weather, NDVI)
Training LSTM without real-world dataset

How I solved it:

Clearly separated responsibilities:
CNN → detects pest/disease
LSTM → predicts future crop health (NDVI)
Generated synthetic training data to simulate real conditions

Standardized input format:

[temp, humidity, soil, rain, ndvi, pest]
⚙️ 3. Backend Decision Logic

Another major challenge was converting AI outputs into meaningful actions for farmers.

Issues faced:
LSTM only gives a number (NDVI), not decisions
CNN gives disease label but not recommendations
Combining multiple signals into one output

How I solved it:

Built a rule-based decision engine:
Combined CNN + LSTM + weather + sensor data
Converted predictions into actionable insights
Example:
Pest detected + NDVI dropping → “Spray pesticide immediately”
Low soil moisture + rain forecast → “Skip irrigation”
🔄 4. Data Synchronization

Handling data with different frequencies was tricky:

Sensor data → every 5 minutes
Weather data → hourly
NDVI → daily

How I solved it:

Normalized all data into a common sequence format (24 time steps)
Used the latest available values where needed
Ensured LSTM always receives consistent input

Team **RunnerExpo** -- [subham singh](https://github.com/subhamsi22), [Rupak Chakraborty](https://github.com/Rupak-25), [Bishwajit Gorai](https://github.com/imbishwajit03), [Akshay Paramanik](https://github.com/akshay-paramanik)

`2026-04-11`

---

### AI-Powered Clinical Decision Support System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-clinical-decision-support-system-4b44) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://medi-co-pilot.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Matrix%203-0052CC?style=flat-square)](https://matrix-3.devfolio.co)

> For the Doc

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

The Problems CoDeX Solves

The Specialist Knowledge Gap: Doctors in Tier-2 and Tier-3 cities often operate in isolation, lacking immediate access to the specialist expertise required to manage complex medical cases.


Geographic Inequality: There is a significant imbalance in healthcare access, where rural providers are often overwhelmed and undersupported, creating bottlenecks in life-saving care.


Data Fragmentation: Medical information is often scattered across physical notes, lab report PDFs, and fragmented patient histories, making it difficult to form a complete and integrated clinical picture.


Cognitive Overload and Burnout: High patient volumes combined with a lack of digital decision support tools increase the risk of diagnostic delays and medical errors.


Diagnostic Errors: Globally, diagnostic errors lead to approximately 800,000 deaths or permanent disabilities annually and account for nearly 15% of wasted healthcare spending.


Prescription Risks: A lack of real-time safety checks leads to unnecessary hospitalizations and potentially fatal drug-to-drug interactions.

**Challenges we ran into**

Complex Multi-Modal Data Extraction: Implementing an OCR pipeline using Google Cloud Vision (GCV) to accurately extract structured data from varied sources—including handwritten notes and printed lab reports—posed significant technical hurdles.Integrating Fragmented Data: Mapping unstructured patient history and disparate lab images into a unified longitudinal record required complex parsing to ensure a complete clinical picture.Real-Time Performance and Scalability: Delivering instant AI reasoning via Claude 3.5 while managing state with Redis and Server-Sent Events (SSE) for streaming responses required careful optimization of the async FastAPI server.Ensuring Clinical Safety: Building a reliable safety layer using Neo4j to traverse complex drug interaction graphs and flag contraindications in real-time was a critical but difficult implementation task.Knowledge Base Accuracy: Implementing Retrieval-Augmented Generation (RAG) with LangChain and Pinecone to strictly follow WHO and DrugBank guidelines was essential to avoid AI hallucinations in a medical context.

**Grand Cash Prize Pool – ₹50,000**

Health Care

Team **CoDeX** -- [vansh verma](https://github.com/vanshverma20), Aakash Rana, Prabhat Upadhyay, [Shubham shukla](https://github.com/shbhmexe)

`2026-04-07`

---

### MediTwin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/meditwin-2523) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tirtha2903/meditwin/tree/main) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/zMrCwirYUVQ) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Predicting Healthcare before it becomes a crisis.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![d3.js](https://img.shields.io/badge/d3.js-333333?style=flat-square) ![React Router](https://img.shields.io/badge/React%20Router-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

# 🚨 Problem Statement

Healthcare today is **reactive, not predictive**.

People only discover cardiovascular issues **after symptoms appear**, often when it’s too late.

## ❗ Key Issues

* ❌ Doctor visits are expensive and inaccessible
* ❌ Wearables are costly
* ❌ Health data is hard to interpret
* ❌ No early warning system

---

## 💡 How MediTwin AI Solves This

MediTwin AI makes healthcare:

### ✅ Easier

* Instant health check in 30 seconds
* No device required

### ✅ Safer

* Early risk detection
* Preventive insights

### ✅ Smarter

* Predicts future health trends
* Suggests actionable improvements

---

## 🎯 Impact

* Reduces late diagnosis
* Improves preventive care
* Makes healthcare accessible to everyone

---

## 🧠 Core Idea

> “From invisible risk to visible future.”

MediTwin AI transforms raw health data into:

* Predictions
* Explanations
* Actions

**Challenges we ran into**

# ⚡ Challenges Faced

## 1. Presage SDK Integration

### Problem:

* Missing headers (smartspectra, physiology)
* Complex C++ SDK setup
* Camera pipeline issues

### Solution:

* Fixed include paths manually
* Used DroidCam to simulate webcam input
* Created fallback simulation for demo stability

---

## 2. Git & Permission Errors

### Problem:

* Permission denied in build folders
* Rebase conflicts
* Push rejected errors

### Solution:

* Fixed ownership using:

  ```bash
  sudo chown -R $USER:$USER
  ```
* Cleaned build directories
* Used proper git workflow (pull → rebase → push)

---

## 3. API Integration Issues

### Problem:

* ElevenLabs and Gemini setup
* API key handling
* Rate limits

### Solution:

* Used environment variables
* Optimized API calls
* Added fallback responses

---

## 4. Real-Time Camera Processing

### Problem:

* Capturing stable video feed
* Integrating with SDK

### Solution:

* Used DroidCam as webcam
* Tested via OpenCV pipeline
* Simulated vitals when needed

---

## 5. UI Complexity

### Problem:

* Managing multiple data states
* Designing dual (present vs future) view

### Solution:

* Modular React components
* Clean dashboard separation
* Visual risk indicators

---

## 🧠 Key Learning

> “In hackathons, solving 80% reliably beats 100% complexity.”

**Best Use of ElevenLabs**

MediTwin AI uses ElevenLabs to convert complex health predictions into natural, human-like voice reports, making medical insights more accessible and engaging. Instead of reading technical data, users can hear their health status explained in simple language, improving understanding and accessibility—especially for non-technical users and visually impaired individuals.

This transforms the experience from a static dashboard into an interactive, conversational healthcare assistant.

**Best Use of Presage SDK**

MediTwin AI leverages Presage’s human sensing capabilities to enable contactless vital monitoring using just a camera. By extracting signals like heart rate and engagement levels in real time, the system eliminates the need for expensive wearables or medical devices.

This allows users to generate accurate health inputs instantly, which feed into the Digital Twin model for prediction—making healthcare more accessible, scalable, and frictionless.

**Best Use of Gemini API**

MediTwin AI uses the Gemini API as a context-aware reasoning engine that interprets Digital Twin outputs and transforms them into personalized, explainable health insights. Instead of showing raw ML predictions, Gemini analyzes risk factors, identifies key drivers like blood pressure or cholesterol, and generates human-like explanations and actionable recommendations tailored to each user.

It also enables an interactive health assistant where users can ask follow-up questions about their condition, effectively turning complex predictive analytics into a conversational decision-support system.

**Best Use Superplane**

MediTwin AI uses Superplane to power event-driven healthcare workflows, where critical health predictions automatically trigger intelligent actions. When a high-risk scan is detected, Superplane initiates workflows such as generating alerts, updating dashboards, and preparing reports in real time.

This transforms the system from a passive prediction tool into a proactive healthcare platform, enabling faster response, better monitoring, and scalable automation of critical health events.

Team **Attitude Adjustment** -- [Tirthankar Das](https://github.com/Tirtha2903), [Diptanil Sen](https://github.com/Diptanil-Sen), [Raunak Biswas](https://github.com/RaunakBis1)

`2026-04-05`

---

### Fiora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fiora-f6fc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/T1dutta/Fiora.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/gHNphwlNTEo) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Women's Health Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

## Problem It Solves:

## Women’s health tracking today is fragmented, reactive, and impersonal:

- Period apps only log dates i.e. no deep health insights
- Symptoms are often ignored until conditions worsen
- No integration of real-time body signals (heart rate, sleep, stress)
- Lack of early detection for issues like irregular cycles or endometriosis
- Minimal support for emergency alerts or partner involvement

## What People Can Use It For: 

🩸 Smart Period Tracking
Log cycles, symptoms, and flow
Get accurate predictions using historical + real-time data

🧠 AI-Powered Health Insights
Detect irregularities early
Identify potential risks (e.g., hormonal imbalance, chronic pain patterns)

⌚ Real-Time Health Monitoring
Sync smartwatch data (heart rate, sleep, activity)
Combine with symptoms for context-aware analysis

🚨 Safety & Support System
Alert trusted contacts during severe symptoms
Enable proactive care instead of reactive treatment

💬 AI Health Assistant
Ask questions anytime
Get personalized, context-aware responses

📚 Learn & Earn
Access educational content
Earn points through quizzes → redeem for products

## How It Makes Things Better

From manual tracking → intelligent prediction
From isolated symptoms → connected health insights
From delayed diagnosis → early detection
From passive apps → proactive health companion
From individual struggle → supported ecosystem

**Challenges we ran into**

Smartwatch Integration
Website crashed while connecting the components so ran into issues while deploying

**Best Use of MongoDB**

Best Use of MongoDB in This App includes:

Flexible Schema for Health Data:
Store dynamic user data (cycles, symptoms, smartwatch inputs) without rigid structure.

User-Centric Document Model:
Keep all related data (profile + history + preferences) in a single document for fast access.

Time-Series Data Handling:
Efficiently store and query chronological data like period logs, heart rate, sleep patterns.

Scalable for Real-Time Updates:
Handles frequent writes from users + wearable devices smoothly.

Quick Aggregations for Insights:
Compute cycle averages, symptom trends, and anomaly detection directly in DB.

**Best Use of ElevenLabs**

Best Use of ElevenLabs in the App includes:

Voice-enabled AI Health Assistant
→ Convert chatbot responses into natural, empathetic voice for hands-free support

Emotional Support Mode
→ Calm, human-like voice guidance during pain, stress, or anxiety

Accessibility Enhancement
→ Helps users who prefer listening over reading

Smart Alerts & Reminders
→ Voice-based notifications for medication, cycle updates, or severe symptom alerts

**Best Use of Gemini API**

Best Use of Gemini in the App includes:

Context-Aware Health Chatbot
→ Understand user history (cycle, symptoms, watch data) and give personalized advice

Symptom Analysis & Insight Generation
→ Interpret patterns and explain risks in simple language

Educational Content + Quiz Generation
→ Auto-create health content and interactive questions

Smart Report Summarization
→ Convert raw health data into clear, actionable insights

Team **The Cliqúe** -- [Sulagna Palit](https://github.com/sulagnapalit27), [Soumili Ghosh](https://github.com/Soumili-2004), [Priyanka Sett](https://github.com/Priyanka200702), [Titli Dutta](https://github.com/T1dutta)

`2026-04-05`

---

### Smart Medical Bill Analyzer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-medical-bill-analyzer-ff38) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dipan-byte/Fraud-detection-in-healthcare) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GXkcJQ_ip58) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> AI-powered transparency in healthcare billing.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**

In today’s healthcare system, medical bills are often confusing, non-transparent, and difficult to verify. Patients—especially in private hospitals—are frequently unaware of what they are being charged for.

This lack of clarity opens the door to serious issues like:

**Overbilling** – Charging far beyond standard rates
**Duplicate Charges** – Same service billed multiple times
**Unnecessary Tests** – Added only to increase revenue
**Hidden Costs** – Charges that are unclear or not explained

Most patients simply trust the bill — and end up paying more than they should.

**Challenges we ran into**

1. Extracting Data from Medical Bills (OCR Issues)

Medical bills come in different formats (PDFs, images, handwritten notes), making it difficult to extract accurate data.

Problem: OCR tools sometimes misread numbers or medical terms
Solution: Implemented preprocessing techniques (image cleaning, contrast enhancement) and structured parsing to improve accuracy
2. Lack of Standard Medical Pricing Data

There is no universal database for hospital pricing, especially in private healthcare.

Problem: Hard to compare whether a charge is “normal” or “fraudulent”
Solution: Created a custom dataset using approximate market rates and publicly available healthcare pricing references

Team **2SAD** -- [Dipan Mallick](https://github.com/Dipan-byte), [Sagnik Adhikary](https://github.com/sagnikishere)

`2026-04-05`

---

### Dava Darpan
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dava-darpan-d839) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Adarshcsds/DavaDarpan) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/3KRHJaiLRQc) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3KRHJaiLRQc) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> One Platform. Complete Patient Care

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Twilio](https://img.shields.io/badge/Twilio-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square)

**The problem it solves**

🚨 Problem Points
👨‍👩‍👧‍👦 Lack of Family Transparency – Families cannot track patient condition, treatment, or progress in real-time

📄 Heavy Paperwork – Reports and prescriptions are physical, easily lost or mismanaged

💻 Unorganized Digital Systems – Existing systems are not centralized or user-friendly

🤖 No Instant Support – Patients don’t get quick help for doubts when doctors are unavailable

📁 No Central Record Storage – Medical reports are scattered, no single secure platform

💰 No Expense Tracking – Patients cannot clearly track treatment costs

**Challenges we ran into**

📲 Live OTP Integration – Implementing real-time OTP verification (Twilio) and handling delays, retries, and security validation

![image](https://assets.devfolio.co/content/7a7c97e242a546cea299afe4349080c3/bbb2442e-9ac1-4bc5-a5dd-26224afd671f.jpeg)

🩻 X-Ray Analyzer Development – Difficulty in processing medical images and generating meaningful analysis using AI models
🔄 Real-Time Data Sync – Ensuring nurse-entered data (vitals, medicines, reports) is instantly visible to the patient without delay
🧠 AI Chatbot Accuracy – Making the AI (Gemini) give reliable and relevant medical responses
🔐 Data Security & Access Control – Managing patient data securely while allowing role-based access (patient vs nurse)

Team **Dava Darpan** -- [Hemant Sharma](https://github.com/sharma01hemant06-oss), [Manav Rastogi](https://github.com/manav1920), [Adarsh Dubey](https://github.com/Adarshcsds), [Mansi Pandey](https://github.com/mansipandey25)

`2026-04-04`

---

### SymbioMed
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/symbiomed-6fff) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtube.com/shorts/5O4y8L2C7IY?si=u75wSXdAZKCZGtOl) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/5O4y8L2C7IY?si=u75wSXdAZKCZGtOl) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Unified AYUSH patient records for modern clinics

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Postman](https://img.shields.io/badge/Postman-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square)

**The problem it solves**

India's AYUSH sector (Ayurveda, Yoga, Unani, Siddha, Homeopathy) 
lacks a unified digital system for patient records. Doctors maintain 
paper records, leading to lost history, duplicate tests, and poor 
continuity of care.

SymbioMed solves this by providing:
- **Centralized patient records** for AYUSH practitioners
- **ABHA number integration** for unique patient identification
- **Real-time data access** across multiple clinic visits
- **Structured intake forms** for new and existing patients
- **Secure Firebase-backed storage** with role-based access

This makes AYUSH clinics faster, paperless, and more professional.

**Challenges we ran into**

- **Firebase Auth + Firestore sync**: Managing real-time patient data 
  with proper security rules was complex — solved by structuring 
  Firestore collections carefully with doctor-specific access.

- **ABHA number validation**: Integrating ABHA (Ayushman Bharat 
  Health Account) lookup required handling edge cases where records 
  don't exist yet — solved with fallback to new patient registration flow.

- **REST API Integration**: Connecting to ABHA (Ayushman Bharat 
  Health Account) API for patient record lookup required handling 
  authentication tokens, network timeouts, and inconsistent API 
  responses — solved using Flutter's HTTP package with try-catch 
  error handling and a manual entry fallback when API fails.

- **Microservice Fault Tolerance**: Managing scenarios where 
  individual backend microservices were unreachable required 
  service-level error boundaries — each service failure was 
  caught independently so one failing service never crashed 
  the entire app flow.

Team **RAT RACER** -- [Rudra Narayan](https://github.com/Rudra), [Mohd_Azam Khan](https://github.com/Mohdazam), [Mohd Mehdi](https://github.com/Mohmmadmehdi21)

`2026-04-04`

---

### CARELINK
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carelink-241b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ayushkumarak018-stack/carelink) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fL3_Zo7CPzI) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Smart Health, Early Detection, Better Lives

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Google Maps API](https://img.shields.io/badge/Google%20Maps%20API-333333?style=flat-square)

**The problem it solves**

🚑 The Problem It Solves

Healthcare today suffers from:
•	Doctor–Patient Communication Gaps → unclear symptom descriptions often lead to misdiagnosis.
•	Ignored or Hidden Symptoms → patients may not recognize early warning signs.
•	Scattered Medical Records → paper reports and fragmented systems make continuity of care difficult.
•	Poor Specialist Guidance → patients struggle to find the right doctor quickly.
•	Hidden Mental Health Issues → stress and mood disorders often remain undetected.

💡 How People Can Use CARELINK
•	Patients
o	Use the AI Symptom Translator to turn confusing descriptions into clear summaries.
o	Carry a QR based Digital Health ID for unified, portable medical records.
o	Get real time risk predictions and alerts for urgent conditions.
o	Receive specialist recommendations without guesswork.
o	Track mental health signals with the Mood & Stress Analyzer.
•	Clinicians
o	Access structured patient summaries instantly.
o	Review vitals from wearables in real time.
o	Conduct WebRTC consults with synced records and triage dashboards.
o	Trust encrypted storage and immutable logs for secure, compliant data handling.

🔒 How It Makes Tasks Easier & Safer
•	Easier:
o	Unified records reduce paperwork and confusion.
o	AI summaries save doctors time in triage.
o	Patients get guided pathways instead of navigating healthcare alone.
•	Safer:
o	Early detection lowers risk of severe outcomes.
o	Encrypted storage and blockchain audit logs protect privacy.
o	Emergency alerts ensure timely intervention.

**Challenges we ran into**

⚡ Challenges I Ran Into

Building CARELINK wasn’t without hurdles. Some of the key challenges included:
•🔗 Integrating Wearables with Edge Gateways BLE devices often dropped connections or sent inconsistent data packets. Solution: We implemented a data normalization layer and retry logic at the edge gateway, ensuring stable streams before forwarding to the cloud.
•🧠 AI Symptom Translator Accuracy Early versions of the NLP model produced vague or overly technical summaries. Solution: We fine tuned the pipeline using domain specific datasets and added a rule based post processing layer to make outputs more clinician friendly.
•🌐 Real Time Consults in Low Network Zones WebRTC calls struggled in rural areas with poor connectivity. Solution: We added lightweight inference at the edge (TFLite/ PyTorch Mobile) and fallback to audio only consults when bandwidth was limited.
•🔒 Security & Compliance Balancing accessibility with strict privacy requirements was tricky. Solution: We used AES 256 encryption for storage, TLS for transmission, and explored blockchain based audit logs to reassure judges about data integrity.

Team **CareLink** -- [Siddhant Mishra](https://github.com/Siddhant2310), [Ayush Kumar](https://github.com/ayushkumarak018-stack), [Krishna maurya](https://github.com/Krishna-0205), [Pragya Pandey](https://github.com/pp6240815-web)

`2026-04-04`

---

### MediVault
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medivault-3fdc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ujjwal0563/MediVault) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/W7kwMIL3Efg?si=azCtWlnqwhNkQajE) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Smart Digital Health Record and Analysis System

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![Cron Scheduler](https://img.shields.io/badge/Cron%20Scheduler-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

MediVault is a smart Health care monitoring system integrated with AI intelligence to provide seamless experience for patients.

**Challenges we ran into**

AI integration was the most challenging part. Along with apk build

Team **RUSK** -- [Shashank Awasthi](https://github.com/SShashankkAwasthii), [Ujjwal Kesarwani](https://github.com/ujjwal0563), [Ritwiz Shukla](https://github.com/ritwizshukla749-byte), [Keshav Saini](https://github.com/keshavsaini0007)

`2026-04-04`

---

### ProtPocket
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/protpocket-dd1a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ayush00git/ProtPocket) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://protpocket.ayushz.me/) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> From predicted complex to drug lead.

![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Autodock vina](https://img.shields.io/badge/Autodock%20vina-333333?style=flat-square) ![Fpocket](https://img.shields.io/badge/Fpocket-333333?style=flat-square)

**The problem it solves**

**Protpocket** addresses key challenges in protein research and drug discovery:  

- **Quick identification of binding pockets:** Automates detection and ranking, saving researchers hours of manual work.  
- **Druggability insights:** Provides a **druggability score** for each pocket, helping prioritize promising drug targets.  
- **Integrated datasets:** Combines **UniProt**, **AlphaFold**, and **ChEMBL** for comprehensive protein-ligand information.  
- **Saves time and labor:** Reduces trial-and-error in experiments and expensive computational runs.  
- **Increases research safety:** Minimizes errors by validating targets before experimental testing.

**Challenges we ran into**

Building **Protpocket** came with several hurdles:  

- **Integrating multiple datasets:** Combining **UniProt**, **AlphaFold**, and **ChEMBL** data into a single platform was tricky due to inconsistent formats and missing entries.  
  - *Solution:* Custom parsers and normalization scripts were written to standardize the data.  

- **Protein pocket detection on large structures:** Some proteins are huge, making pocket identification computationally expensive.  
  - *Solution:* Optimized **fpocket** parameters and parallel processing to reduce runtime.  
- **Druggability scoring validation:** Ensuring that the pocket rankings were meaningful required cross-referencing known ligands.  
  - *Solution:* Built a test set of known protein-ligand complexes to benchmark and fine-tune the scoring algorithm.  

---

**Main Track: The Deepforge Arena**

- **HealthTech / Bioinformatics** – Protein analysis, drug discovery, and disease research.  
- **Data & Analytics** – Using **fpocket** and **AutoDock Vina** for pocket detection and ligand docking insights.  
- **Research Tools / Productivity** – Integrates **UniProt**, **AlphaFold**, and **ChEMBL** datasets to accelerate lab workflows and reduce trial-and-error experiments.

Team **helicopter** -- [Arshita Jaryal](https://github.com/jaryalarshita), [Ayush Kumar](https://github.com/ayush00git)

`2026-03-29`

---

### Second Chance
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/second-chance-1512) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Faizshaikh6280/secondchancefrontend_final) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://secondchancefrontend-final.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LstvCkDzyEI) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> Drug addiction does not destroy just one person —

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**Problem Statement**
Drug addiction does not destroy just one person — it destroys the entire
family around them. No one wants to send their loved one to a rehabilitation
center (Nasha Mukti Kendra), yet families are often left with no better choice.
***Sub Problems :***
1. Withdrawal from addiction can trigger severe physical reactions such as body shaking,
instability, and medical emergencies, making the recovery journey immediately dangerous.
2. Addiction recovery is not just about quitting; it must rebuild broken family trust, social
status, mental stability, and long-term damage to organs and daily life.
3. Addicted individuals often suffer from guilt, hopelessness, and loneliness, believing their
life is already destroyed and that recovery is no longer possible

**Proposed Solution**
SecondChance aims to give a new life to the addicted person by
helping individuals recovering their lives, rebuild broken trust, and
give families a real path to hope, healing, and a fresh start.
Our solution works in 3 layers:
**● Emergency Coping System** — interrupt relapse in real time
through a 7-stage psychological intervention system.
**● AI-Powered Recovery & Deit Plan Generator** — AI-powered digital rehab
assistant that creates personalized recovery plans, builds healthy
habits, and the model continuously learns what’s working best .
**● Global Recovery Community** — AI-driven clustering to connect
users with similar struggles, transforming recovery from isolation
into a community-powered journey of support, accountability, and
motivation.

**Challenges we ran into**

**Understanding the Behavioral Patterns of Individuals with Addiction:**

We engaged with medical professionals and individuals struggling with drug addiction to understand their experiences—how they feel, what they need, and the barriers that prevent them from overcoming addiction.

**Identifying Scientific Methodologies and Understanding Brain Function:**

We reviewed extensive research literature and consulted with medical experts to gain insights into evidence-based methodologies and the underlying functioning of the human brain.

**Main Track: The Deepforge Arena**

We have validated that our app addresses a significant and deeply painful problem faced by millions of people worldwide.

Overcoming addiction is an extremely challenging journey, and access to professional therapy is often limited due to high costs.

To bridge this gap, we have developed an AI-powered, 24/7 support agent that provides continuous, affordable assistance—delivering guidance and interventions aligned with professional therapeutic approaches.
 
![image](https://assets.devfolio.co/content/2082c024019d4a8b94e2346f64a358a0/13c225c4-1390-4a9a-ae03-9dc31650dd9f.png)

**Fresher’s Track: The Rising Lanterns**

As We are first year students  the solution of ours does not exists in market and people are willing to pay for such products , we belive this is Rising Lanters 
because We have validated that our app addresses a significant and deeply painful problem faced by millions of people worldwide.

Overcoming addiction is an extremely challenging journey, and access to professional therapy is often limited due to high costs.

To bridge this gap, we have developed an AI-powered, 24/7 support agent that provides continuous, affordable assistance—delivering guidance and interventions aligned with professional therapeutic approaches.

Team **Dabang Coders** -- [Faiz Alam](https://github.com/Faizshaikh6280)

`2026-03-29`

---

### RogNidhi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rognidhi-e567) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/royalmaddy07/RogNidhi.git) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> Your Lifelong Digital Health Treasury

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The Problem : Fragmented Medical Histories Compromise Care
Problem description : A patient’s complete medical history remains scattered across paper files, PDFs and 
incompatible electronic systems in different doctor’s offices, different hospitals and different labs.
Patient’s have to remember every detail of their complex medical history and keep them in one place.
Patients struggle to remember years of test results. Each new doctor starts from scratch. Doctors waste 
precious time piecing together incomplete histories instead of delivering care.
This fragmentation leads to redundant tests, delayed diagnoses, medical errors, and a healthcare 
experience that leaves both patients and providers frustrated

**Challenges we ran into**

Integrating the various modules and getting knowledge about newer stack

Team **TLE** -- [Udayveer Singh](https://github.com/uveer18), [Ashima Sood](https://github.com/D104-star)

`2026-03-29`

---

### Med Tech
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/med-tech-a292) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://med-tech-project-bwyb.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/e74c629c8e9b41a19643666ef24d62e2) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co)

> Enhancement of health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

In today’s fast-paced world, integrating smart technology into healthcare can transform the way patients and doctors interact—making the entire system more efficient, accessible, and safe.
The introduction of automated token generation with real-time updates eliminates long waiting times and confusion. Patients can easily track their position in the queue, reducing overcrowding and ensuring a more organised flow within medical facilities.
A well-structured calendar system allows patients to book appointments according to doctor availability, minimising scheduling conflicts and saving valuable time for both patients and healthcare professionals.
With the integration of shortest route navigation via Google Maps, patients can reach hospitals or clinics quickly and efficiently—an especially critical feature during emergencies when every minute matters.
Features like dark mode and page translation enhance accessibility and user comfort. Whether it’s reducing eye strain or breaking language barriers, these additions ensure that healthcare services are inclusive and easy to use for everyone.
The system also maintains a comprehensive database of doctors, including their names, specialities, and availability. This empowers patients to choose the right healthcare provider based on their needs, leading to more accurate and timely treatments.
A token-based queue management system ensures fairness and structure, allowing patients to be attended to in an orderly manner. For administrators, advanced controls such as manual token deletion and automatic removal of expired tokens after two hours help maintain system accuracy and prevent misuse.
Finally, a centralised dashboard offers a quick and clear overview of patient activity, enabling healthcare staff to monitor, manage, and respond efficiently in real time.
Together, these features create a smart healthcare ecosystem—one that reduces waiting times, improves accessibility, enhances transparency, and ultimately makes the medical field more organised, reliable, and safe for every patient.

**Challenges we ran into**

As a first-year student, building this website for the medical field was both exciting and challenging. I faced many difficulties while coding and had to learn from different platforms to overcome them. There were moments of panic when things didn’t work, especially when the code refused to run even at the last stage.
But by pushing through every challenge and not giving up, we finally made it here. This project is the result of our hard work, learning, and determination. We have truly given our best to make it meaningful, efficient, and helpful

**Healthcare**

In today's world, integrating smart technology in
healthcare can revolutionise patient-doctor interactions,
enhancing efficiency, accessibility, and safety.
Automated token generation with real-time updates
reduces waiting times, while a structured calendar
The system allows for seamless appointment scheduling.

Google Maps navigation helps patients reach facilities
quickly, which is vital during emergencies. Features like
dark mode and page translation improve accessibility for
all users.
A comprehensive database of doctors enables informed
patient choices for timely treatments. A token-based
The queue management system ensures orderliness, with
administrative controls in place to maintain accuracy.
Finally, a centralised dashboard helps healthcare staff

Team **beta.block** -- [Dhritiman Murmu](https://github.com/dhritimanmurmu-bit), [Dip Nandi](https://github.com/SMILINGzero2), [Santanu Das](https://github.com/santanu07-glitch), [Sreejita Sinha](https://github.com/SREEJITA-KGEC)

`2026-03-22`

---

### Sahayak-Visit Prep Assistant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sahayakvisit-prep-assistant-2a77) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/srishti-1935/SAHAYAK-Visit-Prep-Assistant) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sahayak-visit-prep-assistant-qcr9hvdbdcdtjxyqswuido.streamlit.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Advancing medical care

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Streamlit.io](https://img.shields.io/badge/Streamlit.io-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![Groq API](https://img.shields.io/badge/Groq%20API-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves:**
Every year, millions of patients visit government hospitals in India and leave without receiving care — not because treatment wasn't available, but because they didn't know where to go, what to bring, or what to say.
The system exists. The help is there. But the navigation is broken.

**Who it helps and how**
The first-time visitor
A patient visiting a government hospital for the first time has no idea which of the 10+ OPD departments to go to, which counter to register at, or what documents to carry. They spend hours being redirected from counter to counter. Sahayak tells them exactly where to go and what to bring — before they leave home.
The scheme-eligible patient who never claims benefits
Crores of Indians are eligible for free or subsidised treatment under Ayushman Bharat and state schemes like CMCHIS — but never access it because they don't know they qualify or don't know what to say at the billing counter. Sahayak checks eligibility automatically and gives them the exact script to use.
The caregiver accompanying an elderly parent
A son or daughter bringing an elderly parent to hospital often has no medical background and no idea how to communicate the patient's history to a doctor efficiently. Sahayak generates a structured summary and doctor questions tailored to the patient's condition and age.
The patient with a language barrier
Most hospital navigation tools, signage, and online resources exist only in English or Hindi. Sahayak generates the entire visit card in the patient's preferred language — Tamil, Hindi, or English — so nothing gets lost in translation at a stressful moment.
The returning patient with test results
A patient coming back with lab reports or a referral letter often doesn't know which specialist to see next or how to summarize their history for a new doctor. Sahayak reads the situation and prepares a second-visit card that connects the dots.
**What makes it different from just Googling**
A Google search tells you what departments a hospital has. Sahayak tells this patient, going to this hospital, with this condition, what to do tomorrow morning. The personalization is the entire product — generic information already exists everywhere and helps nobody who doesn't know how to use it.

**Challenges we ran into**

**Regional language support**
Supporting Tamil, Hindi, and English in the same application required identifying the right font files, understanding how PDF libraries handle non-Latin scripts, and building a language detection and switching system. Standard libraries do not handle this out of the box — custom Noto fonts had to be sourced, downloaded, and integrated manually.

**Prompt engineering reliability**
Getting Claude to consistently return clean structured JSON across all patient scenarios was not straightforward. The prompt had to be carefully designed to handle edge cases — symptoms that map to multiple departments, patients with no scheme card, conditions that might need emergency routing instead of OPD routing — without breaking the JSON structure that the rest of the code depends on.

**Data verification constraints**
Real hospital data — OPD timings, block and floor numbers, token availability — could not be verified without ground-level access. Columns that seemed useful had to be deliberately excluded from the knowledge base because including unverified data would produce a card that actively misleads patients. This required conscious data integrity decisions throughout the research phase.

**Scheme eligibility accuracy**
Government scheme rules are complex, state-specific, and not always clearly documented online. Accurately representing Ayushman Bharat and CMCHIS eligibility criteria in a way that Claude could apply correctly required sourcing directly from NHA documentation rather than secondary sources.

Team **Synapse** -- SRISHTI SRIVASTAVA, Smirta Pathak

`2026-03-17`

---

### DischargeShield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dischargeshield-888d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/teambazooka26/DischargeShield) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://discharge-shield.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/-FP3GGBLRAI) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> You hospital discharge papers, made simple.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

DischargeShield can be used to make **hospital discharge instructions easier to understand and safer to follow.** Patients often leave the hospital with prescriptions, follow-up dates, diet rules, warning signs, and medical terms that feel confusing or overwhelming. Our project turns that information into **simple, clear, actionable guidance**.

People can use it to quickly understand **what medicines to take, when to take them, what to do today, what to do this week, and when to seek urgent help**. It also makes existing tasks easier by reducing the need to repeatedly decode complicated discharge papers or depend fully on someone else to explain them. Features like **audio support and simplified instructions** are especially useful for elderly patients, caregivers, and people who are not comfortable with medical language.

In short, it improves safety by helping reduce **medication mistakes, missed follow-ups, and confusion after leaving the hospital**, while making recovery instructions much more accessible and user 

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/a83ef5a2-48d6-491e-b339-86dfa468e353.jpeg)

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/1ad40f30-a908-459d-98fc-e47cc3e6f191.jpeg)

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/6f52b66a-8150-441c-9d3b-f1bd429a9948.jpeg)

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/895de6b3-96ed-4fb4-9fd5-c2f9c1461082.jpeg)friendly.

**Challenges we ran into**

One specific hurdle we ran into was integrating the **audio feature** into the project in a simple and usable way. We wanted the app to provide audio support so users could listen to instructions instead of only reading them, but building a fully custom audio generation pipeline was too heavy for our current scope, time, and resources.

We got around this by using **AI-generated audio files that were available for free download**. Instead of spending too much time building the audio system from scratch, we focused on integrating those ready to use audio assets into the app properly. This helped us add the feature faster, keep the project lightweight, and still deliver the accessibility benefit we wanted for users.

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/3402b717-ad5a-4e1b-adff-2e5707cc1f63.png)

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/a9bdb924-f5ce-48f7-8e23-480ea38592ef.png)

![image](https://assets.devfolio.co/content/56b07181f2a747109b57a150185c3964/4e06854b-1899-47f1-ac0d-9eb494438c6c.png)

Team **BAZOOKA** -- Jahnavi Dave, Shristi Kumari, Vaidehi Govani, Khushi Vasa

`2026-03-17`

---

### Affinite
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/affinite-8562) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sid-techweb/Drug-Protein-Interaction-.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0fDipm3L9mc) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Revolutionizing Drug Discovery with Multimodal AI

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Drug discovery is a slow and expensive process, where identifying effective drug–target interactions requires extensive laboratory experimentation. This leads to long development timelines and high costs, making it difficult to quickly identify promising drug candidates.

What Can People Use It For

* Identifying potential drug–target interactions
* Screening large numbers of drug compounds quickly
* Prioritizing promising candidates for laboratory testing
* Supporting early-stage drug discovery research

How It Makes Tasks Easier / Safer

* Speeds up the process of identifying viable drug candidates
* Reduces reliance on costly and time-consuming lab experiments
* Enables researchers to focus only on the most promising compounds
* Improves efficiency in early-stage drug discovery workflows

**Challenges we ran into**

1. Lack of Data Availability

High-quality, labeled drug–target interaction data is limited and often not easily accessible. This made training and validating the model difficult.
Solution: We used publicly available datasets and carefully filtered and preprocessed the data to ensure quality and consistency.

2. Multimodal Integration Complexity

Combining drug molecular data (graphs) with protein sequence embeddings was challenging due to differences in data representation and dimensionality.
Solution: We standardized embeddings and used a fusion layer to align and combine both feature spaces effectively.

3. Computational Constraints

Running large models (especially protein language models) required high computational resources.
Solution: We used precomputed embeddings and optimized batch processing to reduce runtime and resource usage.

4. Model Accuracy & Tuning

Achieving reliable prediction accuracy required multiple iterations and tuning.
Solution: We experimented with different architectures and parameters, refining the model based on performance metrics.

Team **Helix Hackers** -- [Siva Balaji](https://github.com/sb-tech-dev), [Siddharth S](https://github.com/Sid-techweb), [Sherwin SK](https://github.com/sherwinsyruskaden-code), Sriram S

`2026-03-17`

---

### SafeRx
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saferx-6874) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RajdeepAnandkumarSingh/safeRx-main-deployment) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://saferx-kw0k7n3ex-rajdeepsingh1458-7603s-projects.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Bytecamp'26-0052CC?style=flat-square)](https://bytecamp-26.devfolio.co)

> GraphRAG-Powered Clinical Safety Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Every year, medication errors harm over 1.3 million people globally. Current healthcare systems face two critical failures:

AI Hallucinations: Generic AI models often 'invent' medical facts, making them too dangerous for clinical use.

Prescribing Cascades: Doctors often treat a new symptom with a second drug, unaware it is actually a side effect of the first.

Existing software flags too many 'minor' risks, causing alert fatigue, while failing to explain if an interaction can be managed simply by Time-Spaced Dosing. We need a system that provides deterministic biological evidence, not just a guess

**Challenges we ran into**

1) The "Gated Model" Permission WallThe Hurdle: We initially ran into a 403 Permission Denied error when trying to use Llama 3.3 70B through Featherless.ai. Because it’s a "gated" model, Meta requires a signed license agreement on Hugging Face before the API will grant access.The Solution: We implemented a Dual-Model Strategy. We requested the official license for the high-power 70B model for our final production version, but we immediately pivoted our code to use Llama 3.1 8B as a high-speed fallback. This ensured our development never stopped and taught us the importance of API Permission Management in production AI.
2. The "Indications Only" Blindspot (The 50% Accuracy Bug)The Hurdle: During our first accuracy audit, the system scored only 50%. It caught obvious drug duplicates (like two blood pressure meds) but missed complex interactions like Aspirin and Warfarin. We realized our Graph was too "shallow"—it only contained "Drug $\rightarrow$ Indication" links.The Solution: We went back to the Data Processing stage and expanded our ontology. We added Proteins, Enzymes, and Biological Targets to our Neo4j filters. By adding these "biological side-streets," we enabled our GraphRAG engine to see the hidden paths that cause bleeding risks, pushing our accuracy toward 100%.
3. The "Silent Failure" Ingestion BugThe Hurdle: When uploading millions of medical relationships from PrimeKG to Neo4j AuraDB, the connection would sometimes "choke" or timeout, leaving us with a half-empty graph. The worst part was it failed "silently," so the AI would just report "No risk found" because the data was missing.The Solution: We built a Verified Ingestion Pipeline. Instead of one giant upload, we wrote a script to process the data in Batches of 2,000 using the UNWIND command in Cypher. We added a Verification Layer that counts the relationships in the database after every batch. If the count doesn't match our CSV, the system alerts us, ensuring our "Source of Truth" is always complete.
4. Fuzzy Name Matching (The "Human Error" Hurdle)The Hurdle: In our early tests, if a user typed "aspirin" (lowercase) or "Aspirin-pill," the system returned zero results because Neo4j looks for an exact string match.The Solution: We replaced exact matching with Regex-based Case-Insensitivity (=~ '(?i)' + $drug) and are now implementing a Vector Index within Neo4j. This allows the system to find the "closest" medical node even if there is a typo, making the tool much more usable in a fast-paced hospital environment.

**HealthTech**

SafeRx is a GraphRAG-powered clinical safety platform that anchors AI reasoning in Harvard’s PrimeKG.Deterministic Retrieval: Uses Neo4j to map 110,000+ nodes, identifying biological paths (Distance $\le$ 2) that link drugs through shared enzymes, targets, or side effects.Grounded AI: Uses Featherless.ai (Llama 3.3 70B) to translate graph data into clinical reports, eliminating hallucinations by sticking strictly to retrieved evidence.Management Logic: Distinguishes between Timing-Independent risks (e.g., therapeutic duplication) and Timing-Dependent metabolic conflicts, providing actionable management strategies.How it fits HealthTech (HT2)SafeRx solves the "Specialist Silo" problem described in Problem Statement
While standard tools check isolated pairs, SafeRx uses its knowledge graph to identify indirect biological pathways and complex metabolic cascades that emerge when multiple specialists prescribe for chronic conditions.

Team **Code Trekkers** -- [Sumith Shetty](https://github.com/sumithshetty2005), [Rajdeep Singh](https://github.com/RajdeepAnandkumarSingh), [Pranay Sharma](https://github.com/Pranay64s)

`2026-03-15`

---

### ChronoBio
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/chronobio-a269) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Umarkhan-07/innov8ors) [![Built at](https://img.shields.io/badge/Built%20at-Bytecamp'26-0052CC?style=flat-square)](https://bytecamp-26.devfolio.co)

> Chronobiology-Aware Medication Scheduling

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square)

Team **Team Innov8ors** -- [Affan Mongal](https://github.com/affu786-star), [Roshan Varak](https://github.com/Roshan-Varak), [Umar Khan](https://github.com/Umarkhan-07), [Govind Manjarekar](https://github.com/govind-manjarekar)

`2026-03-15`

---

### ChronoMed
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/chronomed-1f25) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SwarikaaM/techNova) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/PtfDcAam2ZA?si=2wvShOS2G3KL2V0f) [![Built at](https://img.shields.io/badge/Built%20at-Bytecamp'26-0052CC?style=flat-square)](https://bytecamp-26.devfolio.co)

> Chronobiology-Aware Medication Scheduling

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

Team **TechNova** -- [Esha Ramakrishnan](https://github.com/eshaa2005), [Swarika Maurya](https://github.com/SwarikaaM), [Divya Mudaliar](https://github.com/Divya-0508), [nancy maruthuvar](https://github.com/Nancy-20050)

`2026-03-15`

---

### MedAgent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medagent-aa74) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Kavee12345/MedAgent.git) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> An AI-powered healthcare assistant

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Triage Uncertainty: Patients often struggle to decide 
if their symptoms warrant a costly or time-consuming 
doctor's visit, leading to delayed care or unnecessary 
ER overcrowding.

Remote Care Anxiety: People living far from their 
elderly parents face immense anxiety trying to track 
their daily health status, medical adherence, and 
emerging symptoms remotely.

Scattered History: Medical records, lab results, and 
personal health notes are often fragmented, making it 
incredibly difficult to provide a comprehensive history 
to a physician during a brief 15-minute appointment.

**Challenges we ran into**

Voice Loop: Fixed the bot transcribing its own voice by using strict React state and onend speech events to mute the mic while the bot speaks.

LLM Over-Asking: Tamed the Gemini model's habit of asking multiple questions at once through aggressive prompt engineering that enforced strict, single-question responses.

RAG Data Loss: Prevented lab result values from being cut off during PDF retrieval by upgrading to semantic chunking with a 64-token overlap.

SSE UI Lag: Resolved massive UI flickering during real-time token streaming by accumulating text in a useRef and throttling React state updates.

Overall: Integrating browser voice APIs, streaming LLMs, and vector databases ultimately required tight synchronization between prompt constraints and frontend rendering logic.

**Best Use of Gemini 3 [Google Deepmind]**

Gemini 2.5-flash provided the ultra-low latency required to make our continuous voice conversation loop feel natural and instantaneous.

Its generous free tier enabled us to extensively test our Retrieval-Augmented Generation (RAG) pipeline without hitting hackathon budget limits.

The model demonstrated exceptional strictness in following our system prompts, allowing us to successfully restrict it to asking one question at a time.

Gemini's strong reasoning capabilities made it highly accurate at analyzing user symptoms to reliably trigger our emergency escalation protocols.

It effortlessly processed complex medical context by analyzing both the user's persistent health notes and the retrieved document chunks simultaneously.

The ecosystem integration was seamless, pairing perfectly with Google's text-embedding-004 model to build out our pgvector database.

Its robust text-streaming support via Server-Sent Events (SSE) eliminated wait times, allowing the frontend text-to-speech to begin almost immediately.

Team **None** -- [Kunal Koushik](https://github.com/KunalKoushik), [Kavita Chaudhary](https://github.com/Kaveee12345), [Nikhil Sharma](https://github.com/CaseClosed007)

`2026-03-15`

---

### bloom cycle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bloom-cycle-5d04) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/386anshikasharma-cyber/bloom-cycle1) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> ai powered period health tracker

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

ai powered period health tracker project.it includes featured that are backed by real life effects on the behavious of the user like mood swings and other effects like spotting extra.

**Challenges we ran into**

making the project for the first time was a bit of a task.

**Electrothon 8.0 Winners**

for the 1st three positions.

**Electrothon 8.0 Honors Track**

appyling for all girls team and best beginners hack.

Team **BinaryBabes** -- [Vaishnavi Tomer](https://github.com/Vaishnavi-Tee), [Simran .](https://github.com/siimran-27), [Anshika Sharma](https://github.com/386anshikasharma-cyber)

`2026-03-15`

---

### ANUVARTAN
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anuvartan-89cb) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=e8Yvq8RJk2g) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=e8Yvq8RJk2g) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> From Hospital to Home, Recovery Never Stops.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square)

**The problem it solves**

## The Problem it Solves

Anuvartan addresses a critical gap in healthcare that occurs **after patients are discharged from hospitals**. Many patients return home with complex prescriptions, recovery instructions, and wound care guidelines but receive little or no continuous monitoring. Because of this, early warning signs such as infection, medication mistakes, or worsening symptoms often go unnoticed until they become serious. This leads to **avoidable hospital readmissions, higher treatment costs, and increased health risks for patients**.

Post-discharge care is especially challenging in countries like India where patients may live far from hospitals, have limited medical knowledge, or struggle to interpret prescriptions. Anuvartan helps bridge this gap by providing **AI-powered monitoring, guidance, and communication between patients and healthcare providers during recovery**.

---

## What People Can Use It For

### 🧑‍⚕️ Patients and Families
- **Daily Recovery Monitoring**  
  Patients can report symptoms such as pain, fever, activity level, and overall condition from home using a simple app or messaging interface.

- **Medicine Guidance from Prescriptions**  
  The system reads discharge prescriptions and explains medicine schedules clearly, helping patients understand **when and how to take each medication**.

- **Symptom and Wound Tracking**  
  Patients can upload wound photos and describe symptoms so that potential complications can be detected early.

- **Medical Guidance Chatbot**  
  A chatbot helps answer recovery-related questions and guides patients on when they should contact their doctor.

- **Emergency Alerts**  
  If dangerous symptoms appear, the system can quickly notify healthcare providers for immediate attention.

---

### 👩‍⚕️ Nurses and Care Coordinators
- **Prioritized Patient Monitoring**  
  Nurses receive a dashboard showing patients categorized by risk levels so they can focus on those who need attention first.

- **Centralized Patient Updates**  
  Instead of handling scattered phone calls and messages, all patient updates and reports appear in one organized system.

- **Quick Escalation to Doctors**  
  If a patient's condition worsens, nurses can easily escalate the case to a doctor with all relevant information attached.

---

### 👨‍⚕️ Doctors
- **Early Detection of Complications**  
  Doctors can identify patients at risk of complications before conditions become severe.

- **Data-Driven Clinical Decisions**  
  Instead of reviewing multiple reports manually, doctors receive structured summaries of patient symptoms, recovery trends, and alerts.

- **Reduced Unnecessary Readmissions**  
  Many complications can be treated early through remote guidance, reducing hospital visits and improving patient outcomes.

---

## How It Makes Healthcare Safer and Easier

- Detects complications **earlier through continuous monitoring**
- Reduces **medication errors and confusion about prescriptions**
- Enables **remote patient care without frequent hospital visits**
- Improves **communication between patients and healthcare teams**
- Makes follow-up care **accessible even for rural or remote patients**

In short, **Anuvartan transforms the risky and unmonitored recovery period after hospital discharge into a guided, monitored, and safer healing process for patients and healthcare providers.**

**Challenges we ran into**

## Challenges I Ran Into

### 1. Understanding Unstructured Medical Prescriptions
One major challenge was extracting accurate information from **handwritten or poorly formatted discharge prescriptions**. Many prescriptions contain abbreviations, inconsistent formatting, or unclear handwriting, which caused OCR systems to produce incorrect or incomplete text.

**How I solved it:**  
I implemented a two-step pipeline:
1. **OCR extraction** to convert prescription images into raw text.
2. **Gemini-based interpretation** to clean, structure, and understand the extracted information.

Prompt engineering was used to guide the AI model to identify medicine names, dosage, frequency, and duration more reliably. This significantly improved the accuracy of the prescription explanation feature.

---

### 2. Preventing Unsafe AI Medical Advice
Another challenge was ensuring that the chatbot did **not generate unsafe medical recommendations**. Large language models can sometimes produce overly confident responses, which is risky in healthcare.

**How I solved it:**  
I implemented a **rule-based safety layer** along with prompt constraints. The chatbot is restricted to providing only **educational guidance and recovery-related support**, while serious symptoms trigger an **automatic escalation to nurses or doctors**. This ensures that AI assists rather than replaces clinical decision-making.

---

### 3. Designing a Simple Interface for Non-Technical Users
Many patients, especially in rural areas, are not comfortable using complex mobile applications. A complicated interface could reduce adoption.

**How I solved it:**  
I designed the interaction flow to be **very simple and conversational**, supporting platforms like **WhatsApp and lightweight mobile interfaces**. Patients only need to answer simple daily questions or upload images, making the system accessible even for users with limited technical knowledge.

---

### 4. Managing Large Amounts of Patient Updates
As the system monitors many patients simultaneously, handling large volumes of daily symptom reports and messages became difficult to organize.

**How I solved it:**  
I implemented a **risk-based prioritization system** that categorizes patients into **Green, Yellow, and Red risk levels**. This helps nurses and doctors quickly identify which patients need immediate attention instead of manually reviewing every update.

---

Overall, these challenges helped shape Anuvartan into a **safer, more reliable, and user-friendly AI-powered healthcare monitoring system**.

**Electrothon 8.0 Winners**

## How Our Project Fits the Electrothon 8.0 Track

Anuvartan aligns strongly with the goals of Electrothon 8.0 by solving a real-world healthcare problem using AI-driven technology. The project focuses on improving post-discharge patient care by combining AI, automation, and intelligent monitoring systems.

Using Google DeepMind’s Gemini models, the system analyzes prescriptions, interprets patient symptoms, and helps detect early signs of complications during recovery. This enables hospitals to monitor discharged patients remotely and intervene early when risks appear.

The project demonstrates how AI can be applied to create practical healthcare solutions that improve patient safety, reduce hospital readmissions, and make medical follow-up accessible even for rural populations.

By addressing a critical healthcare gap with scalable AI technology, Anuvartan reflects the innovation, social impact, and technical creativity encouraged by the Electrothon hackathon.

**ElevenLabs**

## How Our Project Uses ElevenLabs

Anuvartan uses ElevenLabs to provide voice-based assistance for patients during their post-discharge recovery period. Many patients, especially elderly users or people in rural areas, may find it difficult to read long instructions or interact with complex apps. To solve this, ElevenLabs is used to convert important medical information into clear and natural voice guidance.

The system can generate voice explanations for prescription instructions, medicine schedules, and recovery guidelines. Patients can listen to these instructions in a natural human-like voice instead of reading complicated medical text.

Additionally, the voice system can be used to deliver reminders for taking medicines, reporting daily symptoms, or following recovery steps. This improves accessibility and ensures patients better understand their treatment plan.

By integrating ElevenLabs voice technology, Anuvartan makes healthcare communication more accessible, especially for patients who prefer voice interaction or have difficulty reading medical instructions.

**Vultr**

## How Our Project Uses Vultr

Anuvartan uses Vultr’s cloud infrastructure to host and run the backend services that power the AI-driven healthcare monitoring system. The application backend, APIs, and databases are deployed on Vultr cloud servers to ensure reliable and scalable performance.

Vultr provides the compute resources needed to handle patient data processing, AI model integration, and real-time communication between patients, nurses, and doctors. As patients submit daily recovery updates, wound images, and symptom reports, the backend processes this data and delivers insights through dashboards for healthcare providers.

Using Vultr’s scalable cloud environment allows Anuvartan to support a growing number of patients and hospitals without requiring expensive infrastructure. The platform can easily scale to handle thousands of users while maintaining fast response times and secure data handling.

By leveraging Vultr’s cloud computing capabilities, Anuvartan ensures a reliable, scalable, and high-performance backend system for AI-powered post-discharge patient monitoring.

**Best Use of Gemini 3 [Google Deepmind]**

## How Our Project Uses Gemini 3 (Google DeepMind)

Anuvartan uses Google DeepMind’s Gemini model as the core AI reasoning engine to assist in post-discharge patient monitoring and recovery management.

First, Gemini is used to interpret discharge prescriptions. After a patient uploads a prescription image, an OCR pipeline extracts the text and Gemini analyzes it to identify medicines, dosage, timing, and duration. The model then converts this complex medical information into simple explanations in Hindi or English so patients clearly understand their medication schedule.

Second, Gemini powers the recovery support chatbot. Patients can ask questions about symptoms, medicines, or recovery conditions. Gemini processes natural language queries and provides context-aware guidance while following safety rules to avoid giving unsafe medical advice.

Third, Gemini helps analyze daily patient updates such as pain level, fever, and symptom descriptions. The model interprets this data to assist in identifying possible risks and supports the system in categorizing patients into risk levels (Green, Yellow, Red) so nurses and doctors can prioritize care.

By using Gemini for medical document understanding, intelligent patient interaction, and recovery monitoring, Anuvartan demonstrates a practical real-world application of Google DeepMind AI to improve patient safety and reduce avoidable hospital readmissions.

Team **Anuvartan** -- [Abhyuday Jain](https://github.com/Avalanche2825), [Aditya Raj](https://github.com/Aditya-Coder477), [Ashish Prajapati](https://github.com/ashishprajapati2006), [Gaurav Pareta](https://github.com/GAURAVPARETA555)

`2026-03-15`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
