# Health and Biotech

![Projects](https://img.shields.io/badge/Projects-198-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

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

### VitalMed
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitalmed-7b00) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vitalmed-smoky.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-15-FF6B6B?style=flat-square)

> Hospital-grade diagnostics. Living room comfort

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## Project Overview: VitalMed

VitalMed is a small, handheld medical device built to help health workers quickly detect heart, lung, and gut problems—often in just a few seconds.

Using a highly sensitive microphone placed inside a stethoscope-like head, the device listens to the sounds inside the body and uses AI to predict which medical condition is most likely present. In simple terms, it gives health workers a trained “digital ear” when a specialist isn’t available.

---

## The Problems It Solves

### Shortage of Specialists

In many clinics, especially in rural or crowded areas, there simply aren’t enough heart or lung specialists. VitalMed acts like a reliable second opinion, helping frontline health workers recognize conditions that usually require years of experience to identify.

### Detecting Problems Before Symptoms Appear

Many serious issues—like heart murmurs or early lung infections—don’t cause pain right away. The AI can pick up subtle abnormal sounds long before the patient actually feels sick, allowing for earlier treatment.

### Cutting Through Clinic Noise

Busy clinics are loud. Hearing faint heart or lung sounds in that environment is extremely difficult. The sealed stethoscope head blocks out background noise so the device focuses only on what’s happening inside the patient’s body.

### Creating a Digital Medical Record

Normally, when a doctor listens with a stethoscope, that information disappears the moment they walk away. This device records and stores the sounds digitally, making it easy to track changes over time or share recordings with a specialist for a quick review.

---

## 2. How It Makes Medical Exams Easier

### Lung Checkups

Instead of guessing between different lung infections based on faint crackling sounds, the AI analyzes the audio and suggests the most likely condition—such as pneumonia, COPD, or bronchiolitis.

### Heart Examinations

Heart murmurs and extra heart sounds are easy to miss, especially in noisy settings. VitalMed clearly detects these abnormalities, helping ensure serious valve or rhythm issues aren’t overlooked.

### Gut Monitoring

After surgery, doctors often have to wait and listen for long periods to know if the digestive system is functioning properly. This device quickly checks for gut sounds and predicts whether digestion is normal or if there may be a blockage.

### Faster Expert Consultations

Instead of sending patients long distances to see a specialist, health workers can record the sound, attach the AI’s analysis, and send it digitally—allowing experts to give feedback almost instantly.

---

## 3. How the AI Works (In Simple Terms)

The system follows a clear, step-by-step process:

* *Noise Filtering:* The moment the device touches the skin, it removes unwanted sounds like talking, movement, or wind.
* *Organ Separation:* Heart, lung, and gut sounds have different frequencies. The AI separates them so they don’t interfere with each other.
* *Pattern Recognition:* Trained on thousands of real medical recordings, the AI looks for sound patterns that match known diseases—like the rhythm of a murmur or the whistle of a wheeze.
* *Clear Results:* The system then gives a simple, easy-to-understand output, such as “Likely Pneumonia” or “Heart Murmur Detected.”

---

## Why This Matters

VitalMed isn’t just another medical gadget—it’s a way to bring specialist-level diagnostic support to places where it’s needed most. It gives frontline health workers confidence, helps patients get the right care sooner, and ensures serious conditions don’t go unnoticed just because a specialist wasn’t in the room.

**Challenges we ran into**

1. Balancing Clinical Safety with Operational Efficiency
The Challenge: We faced a critical decision between minimizing false alarms (Precision) and ensuring every potential health issue is detected (Recall).

The Solution: We prioritized Recall to maximize patient safety. To prevent "alarm fatigue" for clinicians, we implemented Confidence Scores to flag ambiguous or high-risk cases for professional review.

2. Optimizing Acoustic Fidelity for AI Analysis
The Challenge: Subtle heart and lung sounds are often obscured by ambient noise or captured at frequencies insufficient for deep model analysis.

The Solution: We engineered a customized microphone sensor system for high-fidelity, low-frequency capture. The raw signals undergo signal conditioning and frequency-based noise filtering to isolate pure vital sounds before being analyzed by the model.

Team **DTU ALTAIR** -- [Krish Ichpal](https://github.com/DarkLordKrish), [Tanvi Goel](https://github.com/tgoel315-tech), [Krish Chauhan](https://github.com/Krish-Chauhan-Python), [aditya sharma](https://github.com/adityatech5615), [Sparsh Tyagi](https://github.com/sparshh1)

`2026-02-08`

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

### CareBridge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carebridge-dedb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prithvicoder1/Real-Time-Bed-Blood-Availability-Dashboard) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LaHM5oeaSWs) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-9-FF6B6B?style=flat-square)

> Hospital Beds & Blood: Live Save Lives !!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Title: Real-Time Bed & Blood Availability Dashboard for Government Hospitals

Description:
There is no unified, real-time public dashboard showing bed availability — including ICU, general ward, paediatric, maternity, and isolation beds — across government hospitals in any given city or district. Blood banks similarly have no live inventory system visible to the public or to ambulance dispatchers. Families in crisis make desperate phone calls to multiple hospitals, and ambulances carry patients to full facilities simply because there was no way to know in advance.

![image](https://assets.devfolio.co/content/68fa6b0022ab41138b052e061f9485c1/82dff468-d894-43c2-b501-5c0976f7beac.png)



![image](https://assets.devfolio.co/content/68fa6b0022ab41138b052e061f9485c1/7bcfd3df-3483-46c9-b703-312e0e09cbce.png)

**Challenges we ran into**

## Handling Static Data for Multiple Hospital Categories

One challenge we faced while building the dashboard was organizing and displaying *static hospital data across multiple categories* such as ICU beds, general ward beds, paediatric beds, maternity beds, isolation beds, and blood group availability.

Initially, the data was stored in a simple list structure. As we expanded the dashboard to include more hospitals and different bed categories, the data became difficult to manage and the UI was not displaying the correct values for each hospital. In some cases, the wrong bed counts appeared under the wrong category due to inconsistent data mapping.

### How We Solved It

To fix this, we redesigned the data structure using a *well-defined model for each hospital*. Each hospital object contained clearly separated fields for bed categories and blood inventory.

For example:

•⁠  ⁠ICU beds
•⁠  ⁠General ward beds
•⁠  ⁠Paediatric beds
•⁠  ⁠Maternity beds
•⁠  ⁠Isolation beds
•⁠  ⁠Blood group availability

This structured approach made it easier to map the data correctly to the UI components and improved maintainability. It also prepared the system so that in the future the static data can be easily replaced with *real-time API or database updates*.

**Best Use of Gemini API**

CareBridge leverages the Gemini API for real-time hospital insights:

- Generates natural language summaries of bed/blood availability (e.g., "Sawai Man Singh Hospital: 15 ICU beds free, O⁺ blood low")
- Powers teacher dropout explanations via SHAP + Gemini prompts ("Low attendance risks 65% dropout—suggest weekly check-ins")
- Chat interface for Jaipur hospitals: "Find nearest O- blood?" → Instant heatmap + ETA

This scales ML predictions (XGBoost) into teacher/hospital-friendly responses, boosting usability 3x.


![Uploading image...]()

**Best Hack Built with Google Antigravity**

CareBridge uses Google Antigravity SDK for secure, scalable hospital 

- Antigravity Vertex AI powers XGBoost models (92% dropout prediction accuracy)
- Real-time bed/blood sync via Antigravity Pub/Sub (Jaipur govt. and private hospitals)
- Antigravity Maps API for emergency heatmaps + ambulance routing

Built hackathon-style: MVP in 48 hrs with Antigravity's zero-config ML deploy.

![Uploading image...]()

Team **FUNCTION FORCE** -- [Richa Kumari](https://github.com/Richajha23), [Dhruv Kumar](https://github.com/dhruvkumar3172-byte), [Prithvi Vijay](https://github.com/prithvicoder1), [Ashish Kumar Gupta](https://github.com/ashishkumargupta28sep2005)

`2026-03-08`

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

### CareCircle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carecircle-6e3b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tiyasaurusrex/CareCircle) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Healthcare guidance beyond hospitals.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

## CareCircle 

After hospital discharge, patient recovery shifts from structured medical supervision to unstructured home care. Patients and caregivers become responsible for medication management, symptom monitoring, and recovery decisions without continuous medical guidance.

This often leads to medication errors, missed doses, inconsistent symptom tracking, and delayed medical intervention. 

Early warning signs may go unnoticed, especially when recovery data is not recorded systematically. Caregivers also struggle to determine when professional consultation is necessary, while doctors receive incomplete information during follow-ups.

As a result, a critical gap exists between hospital care and home recovery, where patients lack structured monitoring, guidance, and clear communication channels with healthcare providers.



## How CareCircle Solves This Problem

CareCircle transforms home recovery into a guided and trackable process through a centralized digital platform.

The system structures recovery data by organizing medicines, symptoms, and care tasks in one place, reducing reliance on memory or manual notes. Medication tracking and reminders improve adherence, while voice-based input simplifies usage for elderly or non-technical users.

Continuous symptom logging enables early identification of abnormal patterns through triage logic, helping caregivers take timely action. When required, CareCircle guides healthcare escalation and supports structured communication by generating organized recovery summaries for doctors.

By bridging patients, caregivers, and healthcare professionals, CareCircle acts as a digital recovery coordination layer that improves safety, accessibility, and decision-making during home recovery.

Team **Lightning_MCqueen** -- [Jahanvi rajpurohit](https://github.com/Jhamko), [Tiyasa Paul](https://github.com/tiyasaurusrex), [Divyanshi Yadav](https://github.com/Divyanshi760)

`2026-02-08`

---

### Vital-Link_portable-ICU
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitallinkportableicu-4098) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Smart Vital Signs Monitoring for ICU Patients

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

Team **ShieldX** -- [AKRITI AGARWAL](https://github.com/Akriti1331), [Mayank Saraswati](https://github.com/mayanksaraswati), [Kashish Dhawan](https://github.com/kashishdhawan73-cyber), [Kiran Goswami](https://github.com/kirangoswami200-sudo)

`2026-02-08`

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

### Healify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healify-60d2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://healify-omega.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=iwQBJpPyvNY) [![Built at](https://img.shields.io/badge/Built%20at-RECKON%207.0-0052CC?style=flat-square)](https://reckon-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Smart Healthcare Solution for Better Life

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Multer](https://img.shields.io/badge/Multer-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square)

**The problem it solves**

# Healify – AI Powered Healthcare Assistant

Healify is an AI-powered healthcare assistant designed to streamline the patient experience through intelligent automation and personalized care. Below is a comprehensive overview of the problem it addresses, its practical applications, and its core features.

##Link Opening Disclamer:
open the render backend link first then open the frontend link of vercel for better experience.
---

## **The Problem it Solves**

Navigating the modern healthcare ecosystem is often characterized by fragmentation, complexity, and a lack of transparency. Healify is engineered to address several critical pain points:

- **Diagnostic Uncertainty**: Many individuals struggle to articulate their symptoms or understand the severity of their condition, leading to either delayed treatment or unnecessary emergency room visits.

- **Deciphering Prescriptions**: Handwritten or complex printed prescriptions are notoriously difficult for patients to read, which can lead to errors in medication timing, dosage, or frequency.

- **Inefficient Appointment Management**: Traditional booking processes are often cumbersome, lacking real-time availability and localized search capabilities for specialists.

- **Medicine Price Disparity**: Pharmaceutical costs vary significantly across different providers. Patients often lack a centralized tool to compare prices or identify affordable generic alternatives.

- **Accessibility and Language Barriers**: Healthcare information is not always available in a user’s native language or in an accessible format for those with physical or cognitive challenges.

---

## **Practical Applications and Benefits**

Healify makes existing healthcare tasks safer, faster, and more intuitive for patients and caregivers:

- **Risk Assessment**: By performing preliminary symptom analysis, users can make more informed decisions about whether they need immediate medical attention or home care.

- **Medication Adherence**: Automated dosage reminders generated directly from prescription scans significantly reduce the risk of missed doses or incorrect administration.

- **Cost Efficiency**: Real-time price comparisons allow users to save on healthcare expenses by identifying the most cost-effective pharmacies and generic drug options.

- **Seamless Logistics**: The integration of live mapping and instant booking reduces the administrative burden of scheduling medical visits, making the process as simple as a few clicks.

- **Universal Accessibility**: The use of voice-enabled, multilingual interfaces ensures that healthcare support is available to a diverse population, regardless of their technological proficiency or primary language.

---

## **Core Features**

The Healify application addresses these challenges through a suite of integrated, high-performance features:

### **1. AI-Powered Symptom Analyzer**

This feature allows users to input their health concerns via natural language text or voice. Leveraging advanced transcription services, the system analyzes the input to provide potential condition matches, assess severity (**Low to Critical**), and recommend appropriate next steps.

---

### **2. Smart Prescription Reader**

Utilizing **Optical Character Recognition (OCR)** technology, Healify extracts medication data from uploaded images or scans of prescriptions. It automatically parses **dosages, frequencies, and durations** to generate a structured medication schedule with integrated browser notifications for reminders.

---

### **3. Dynamic Appointment Booking**

The platform features a **dual-mode booking system**.

- **Instant Booking**: For available general practitioners.
- **Collaborative Scheduling**: To request specific specialists.

This is supported by **live clinic mapping** to help users find the nearest healthcare facilities.

---

### **4. Medicine Price Comparison Engine**

Through external API integrations, Healify provides **real-time pricing** for medications across various pharmacies. It also suggests **generic alternatives**, helping users reduce their pharmaceutical expenditures without compromising on quality.

---

### **5. Intelligent Site-Wide AI Agent**

A persistent **accessibility assistant** helps users navigate the platform, fill out complex medical forms, and understand specific features. This agent is **context-aware** and provides help based on the user's current activity within the app.

---

### **6. Interactive Healthcare Chatbot**

The **24/7 AI chatbot** serves as a primary point of contact for health-related queries, wellness advice, and mental health support. It maintains **conversational context** to provide more relevant and personalized guidance over time.

**Challenges we ran into**

# Technical Challenges and Solutions in Building Healify

Building Healify required integrating modern web technologies with specialized AI services. Below are the key technical challenges encountered and the strategies used to solve them.

---

## **1. OCR and Prescription Data Parsing**

**Challenge:**  
Medical prescriptions often contain **handwritten text, poor lighting, or skewed images**, causing **Tesseract OCR** to generate fragmented or inaccurate outputs.

**Solution:**  
A secondary processing layer using **Groq AI (LLM)** was implemented. The raw OCR text is sent to the LLM with a **strict JSON schema prompt**, allowing the AI to intelligently extract **drug names, dosages, and frequencies** even from partially corrupted text. This **OCR + LLM hybrid pipeline** converts noisy data into structured medical information.

---

## **2. Live Geospatial Data and Rate Limiting**

**Challenge:**  
Integrating **Overpass API** for clinic search and **Nominatim** for geocoding introduced performance issues due to **strict rate limits and slow responses**, causing UI delays.

**Solution:**  
Implemented **debounced search and local caching** to reduce unnecessary API calls. Skeleton loaders and **React `useEffect` asynchronous fetching** ensure the interface remains responsive while clinic data loads.

---

## **3. Conversational Memory in Chatbot**

**Challenge:**  
Healthcare chatbots must remember previous messages, but sending the **entire conversation history** to the AI increases token usage and risks exceeding the model context window.

**Solution:**  
A **Sliding Window Context Manager** was developed. Older messages are **summarized**, while recent interactions remain detailed. This allows the chatbot to maintain **context and coherence** without increasing API costs.

---

## **4. Multilingual Voice Processing Latency**

**Challenge:**  
The Symptom Analyzer supports multiple Indian languages using **Sarvam AI**, but the **Record → Transcribe → Analyze → Translate** pipeline caused high latency.

**Solution:**  
The system was optimized using **parallel processing and optimistic UI updates**. Once recording ends, a loading state appears while transcription and analysis run simultaneously. Backend APIs were optimized to combine **STT and LLM analysis in streamed responses**, improving responsiveness.

---

## **5. Performance of Micro-animations**

**Challenge:**  
Premium UI animations risk causing **visual stuttering (jank)**, especially on lower-end devices.

**Solution:**  
Animations were moved to **CSS transitions and hardware-accelerated transforms (`translate3d`)**, reducing main thread workload. Animations are triggered only after **React confirms data loading**, ensuring smooth rendering.

---

## **6. Preventing AI Diagnostic Hallucinations**

**Challenge:**  
The Symptom Analyzer must provide useful insights without appearing to deliver **definitive medical diagnoses**, which could mislead users.

**Solution:**  
A **structured prompt hierarchy** forces the AI to use **probabilistic language** such as *“suggestive of”* or *“potential indicators for.”* Additionally, a **global disclaimer middleware** automatically attaches medical warnings to all analysis responses.

---

## **7. Multilingual Symptom Normalization**

**Challenge:**  
Users often describe symptoms using **regional phrases or colloquial language**, which may not translate directly into medical terminology.

**Solution:**  
A **Two-Stage Translation Pipeline** was implemented. First, **Sarvam AI performs transcription and literal translation**. Then a **Medical Context Translator** maps colloquial expressions to standardized clinical terms, ensuring consistent symptom analysis.

---

## **8. Severity Detection and Emergency Escalation**

**Challenge:**  
AI alone may underestimate the severity of life-threatening symptoms described calmly.

**Solution:**  
A **Keyword-Based Red Flag System** runs alongside the LLM analysis. If high-risk terms such as **chest pain, numbness, or breathing difficulty** appear, the system overrides lower severity predictions and escalates the case to **Critical**, triggering emergency recommendations.

Team **Zero Code** -- [Rohan Debnath](https://github.com/rohandebnath1), [Arijeet07 Banerjee](https://github.com/ArijeeetBanerjee07), [Priya Kumari](https://github.com/Priyakumari0307), [Anindya Ganguly](https://github.com/anindya-19)

`2026-03-14`

---

### Asclepius
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/asclepius-63b6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ReservedSnow673/AsclepiusAI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3gMzA306G_8) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Temporal Clinical Intelligence Engine

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Brain tumour detection requires repeated MRI scans over time but current AI tools scan each tool in isolation without a sense of the time that needs to be taken in account. 

There is no system that combines longitudnal tracking, multimodal data, uncertainty quantification
and federated privacy.

This demands radiologists to manually compare scans and inferences to detect progression - slow and error prone. Asclepius is a longitudnal,  multimodal, uncertainty-aware brain tumour segmentation and clinical decision support system. A clinical intelligence engine.

**Challenges we ran into**

Building ASCLЕPIUS involved integrating several complex systems that normally exist in isolation. One of the biggest challenges was connecting advanced AI models with a temporal reasoning engine that could actually understand disease progression over time rather than just analyze a single MRI scan. Designing a pipeline that could process medical images, generate meaningful embeddings, update patient timelines, and then perform reasoning without slowing down the system required careful architectural decisions. Another challenge was handling heterogeneous medical data—imaging, clinical metadata, and temporal records—while keeping the system reliable and scalable. We also had to ensure that features like vector search for similar clinical cases and retrieval-augmented reasoning integrated smoothly with the core inference pipeline without breaking existing functionality. Finally, balancing performance with usability was difficult; the system needed to run complex AI workflows while still providing near real-time responses suitable for a clinical environment. These challenges pushed us to design a modular architecture where each component—from perception to reasoning—could operate independently but still contribute to a unified clinical intelligence pipeline.

Team **deranked** -- [Swapneel Premchand](https://github.com/Sw4pplenrel), Shaurya Jain, Suchethan PH, Tanvir Singh Sandhu

`2026-03-08`

---

### Smart Health
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-health-b5a7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bappa8172/SmartHealth) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/19beLpQ-8CzMw3CtkDgBXz3jNoCM7cvEN/view?usp=drive_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1172505132?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> stay healthy while you work

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square)

**The problem it solves**

Imagine an app that protects your health while you work, without reducing your productivity. That’s exactly what "SMART HEALTH"  does.

Many students, developers, and office workers spend hours in front of screens without taking breaks. This leads to eye strain, fatigue, poor posture, and reduced focus.
SMART HEALTH solves this by using a smart work timer that reminds users to take short micro-breaks such as stretching, breathing exercises,Spinal Twist,Eye Relief or drinking water.

What makes our solution different is ,the gamification system. Users earn points and maintain wellness streaks, which motivates them to build healthy work habits.

**Challenges we ran into**

1. The "Background Timer" Hurdle
The Challenge: One of our biggest technical hurdles was ensuring the meditation and stretch timers continued to run accurately when the user navigated away from the app or locked their screen. Initially, the Android lifecycle would "freeze" our countdown, leading to inaccurate session tracking and missed wellness nudges.

The Solution: We overcame this by implementing a Foreground Service combined with a Notification Manager. By moving the timer logic out of the UI layer and into a persistent service, we were able to provide real-time updates via a sticky notification. This ensured that even if the user was answering an email, their "Deep Breathing" session remained active and accurate.

2. UI Consistency Across Activities
The Challenge: Maintaining a seamless, calming aesthetic (mint-green gradients and soft UI shadows) across multiple complex screens like the "Smart Health Dashboard" and various "Pose" activities was difficult to manage with hard-coded styles.

The Solution: We moved toward a Atomic Design approach. We created a reusable "Wellness Card" component and a global "Theme Engine" for our gradients and typography. This allowed us to quickly generate new activity types (like the "Single-Leg Alertness" pose) while ensuring every button, icon, and progress ring looked identical across the entire platform.

3. Gamification Logic Syncing
The Challenge: Preventing "point-farming" (where a user could spam the "Log Water" button to inflate their score) while still making the app feel responsive.

The Solution: We implemented a Rate-Limiting Logic on the backend of our progress tracker. We set "Cooldown Windows" for specific activities—meaning points are only awarded if the actions occur at realistic intervals—balancing user motivation with data integrity.

**Health & WellBeing**

Smart Health is a wellness platform designed to combat "sitting fatigue" and office burnout by integrating healthy micro-habits into the workday.

Our project fits the Health & Wellbeing track by providing:

Preventative Care: Automated "wellness nudges" for stretching, hydration, and deep breathing based on real-time work timers.

Gamified Engagement: A points-based reward system and daily streaks that motivate users to maintain physical health while working.

Mental Clarity: Focused meditation modules designed to reduce stress and improve cognitive performance during high-pressure tasks.

By transforming mandatory breaks into an interactive, rewarding experience, Smart Health empowers users to maintain their physical and mental vitality without sacrificing productivity.

Team **HackedSystem** -- [ROHIT MUKHERJEE](https://github.com/Rohit-student584), [susmita Das](https://github.com/monaidas01-cell), [Bappa Mandal](https://github.com/bappa8172), [Protyay Kolay](https://github.com/protyaykolay)

`2026-03-11`

---

### Lotted Care
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lotted-care-bd63) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arkaskr/lotted-care) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1lUmvhlD3UChJ4HuS-8KgG2FriyoyGo8B/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Your Unified Health Management Companion

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Health Tracking: Helps users keep track of their overall health and daily wellness activities, allowing them to stay aware of their physical condition and maintain a healthier lifestyle.

Gamified Fitness Engagement: Encourages users to stay active through a ranking system, daily streaks, and point-based rewards, making daily exercise more engaging and motivating.

AI-Based Symptom Identification: Allows users to easily input their symptoms and receive an AI-based analysis to understand possible health issues.

Guidance and Next Steps: Provides helpful suggestions, solutions, and recommendations on what actions users should take based on their symptoms.

Nearby Doctor Suggestions: Helps users find nearby doctors and medical facilities, making it easier to seek professional medical help when needed.

User-Friendly Healthcare Access: Simplifies healthcare guidance so that anyone can quickly identify symptoms and take necessary steps for better health management.

**AI / ML**

The application integrates advanced AI-powered symptom analysis, allowing users to input their symptoms and receive a preliminary assessment of possible health issues. Based on the analysis, the system provides helpful guidance, including recommended precautions, basic remedies, and suggested next steps. In addition, Lotted Care enhances accessibility to healthcare by recommending nearby doctors and medical facilities, enabling users to quickly find professional help when needed. By combining AI-driven insights with location-based healthcare support, Lotted Care aims to make early health guidance more accessible, convenient, and user-friendly.

Team **DETTOL (Kills 99.9% bugs)** -- [Arka Sarkar](https://github.com/arkaskr), [Soumyadwip Das](https://github.com/SoumyadiP0004), [Shravan Thakur](https://github.com/shravanthakurgit), [Kakoli Halder](https://github.com/kakolihalder)

`2026-03-11`

---

### HealthDesk
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthdesk-ee93) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Hellf0rg0d/breaking-bug-hacktu7.0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1AefuuZpAnrjUrnAottL8W7BD-SCdTaCh/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> An AI First Healthcare Platform

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square)

**The problem it solves**

In many rural and underserved areas, healthcare doesn’t fail because doctors don’t exist it fails because systems don’t work the way real life works.

People often live far from hospitals. Internet connectivity is unstable. Medical reports are confusing. And during emergencies, digital systems depend on strong, real-time connections that simply aren’t available.

Most telemedicine platforms are built assuming stable networks and digitally comfortable users. But in rural areas, many patients are elderly, first-time smartphone users, or not confident with complex apps. When technology becomes complicated, people avoid using it even when they need help.

This leads to delays in treatment, miscommunication, lost medical records, and hesitation during critical moments.

The problem is not just access to doctors.

The problem is continuity of care in low-resource, low-connectivity environments.

Healthcare today is not designed for infrastructure constraints — and that gap costs time, trust, and sometimes lives.

**Challenges we ran into**

1. Economic Constraints
As students, we had limited financial resources for infrastructure and premium healthcare APIs. We had to prioritize essential features, explore open-source tools, and design the system to be scalable without heavy upfront costs.

2. Building a Reliable SOS System
Designing an emergency escalation feature for low-connectivity environments was challenging. We had to ensure it works safely, avoids false triggers, and does not depend entirely on real-time internet availability.

3. Securing Real-Time Communication
Handling WebSockets for live doctor availability required careful attention to authentication, encrypted communication, and role-based access control to prevent unauthorized access and protect patient data.

4. Keeping the System Simple
Since we are targeting rural and elderly users, simplifying the interface without reducing functionality was a continuous design challenge.

**Google Gemini**

Gemini powers the RAG chatbot to reason over retrieved medical documents and generate multilingual answers.

Gemini classifies SOS call responses into critical or non-critical situations.

Gemini generates calm, non-diagnostic voice guidance during SOS calls.

Gemini summarizes SOS conversations for doctors and hospital admins.

Gemini handles translation and language normalization across chat and emergency flows.

Team **Breaking Bug** -- [Kartik NHM](https://github.com/Hellf0rg0d), [Shrihari Deshapande](https://github.com/shrihari-des18), [Sudhanva Kulkarni](https://github.com/Sudhanva-Kulkarni), [Amogh Kini](https://github.com/Akenzz), [Sarosh Kumar](https://github.com/Sarosh6-ops)

`2026-02-08`

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

### Wellness Nudge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/health-pilot-ac46) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://wellnessnudge.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Your Smart Guide to Better Health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

1️⃣ Ignoring Health During Work

Students and professionals often work long hours without taking breaks, leading to eye strain, fatigue, dehydration, and posture problems. There is no simple system that reminds users to take healthy micro-breaks.

2️⃣ Confusion About Which Doctor to Visit

When people experience symptoms like headache, stomach pain, or skin issues, they don’t know which medical specialist to consult, which causes confusion and delays in treatment.

3️⃣ Difficulty Finding Nearby Affordable Clinics

Many people struggle to find nearby hospitals or clinics that are affordable, especially quickly during health concerns.

4️⃣ Risk of Wrong Self-Diagnosis

People often rely on random internet searches for medical advice, which can lead to misinformation and wrong decisions about their health.

5️⃣ Lack of Preventive Healthcare Tools

Most health solutions focus on treatment after illness, but very few tools encourage preventive habits like hydration, stretching, or breathing breaks.

**Challenges we ran into**

1️⃣ Mapping Symptoms to the Right Specialist

One challenge was correctly mapping user symptoms to the appropriate medical specialist. Many symptoms can relate to multiple conditions, so creating accurate mappings required research and careful logic.

2️⃣ Integrating Map and Location Services

Showing nearby clinics or hospitals on a map required integrating map APIs and handling location data, which took time to configure properly.

3️⃣ Designing a Simple and User-Friendly UI

Since the app targets general users, we needed to ensure the interface was easy to understand, clean, and accessible while still showing important health information.

4️⃣ Implementing the Break Reminder System

Creating a timer-based wellness reminder system that works smoothly without disturbing the user’s workflow was a technical challenge.

5️⃣ Time Constraints During Development

Because the project was built during a limited-time hackathon, managing time while implementing multiple features like AI chatbot, symptom mapping, and wellness reminders was challenging.

**AI / ML**

we integrate an AI chatbot inside the website using open ai API key

**Web3**

We want to make the project in web  technologies for better user experience

Team **Byte lab** -- [Sayan Modak](https://github.com/SayanModakDev), [Subhasis Dhara](https://github.com/Subhasis495), [Arghadeep Ghosh](https://github.com/Arghadeep64), [Sanat Manna](https://github.com/SanatManna)

`2026-03-11`

---

### Fit Nova
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fit-nova-5961) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MSubhajitIND/Fit-Nova/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/CFjCN_eC7N4) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Your Health And Fitness Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Google Cloud Vision API](https://img.shields.io/badge/Google%20Cloud%20Vision%20API-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Fit Nova is an AI-powered personal health and fitness platform designed to help users manage nutrition, workouts, hydration, daily wellness, and progress tracking in one place. Instead of being only a calorie tracker or only a workout app, it connects multiple parts of a user’s health routine into a single personalized system.

Features
The app starts with a user profile that captures age, gender, height, weight, goal, and activity level. Using this, it calculates BMI, daily calorie requirements, water target, macro targets, and step targets. This gives every user a personalized baseline instead of generic recommendations.

The dashboard is designed around daily action. It shows calorie target, water target, protein/carbs/fat targets, step goal, and achievement status, so users can immediately understand how close they are to their daily health goals. It also keeps a history of meals and logs to make progress visible, not abstract.

One of the strongest features is the AI food analysis flow. A user can search for a food item by text or upload an image. The system analyzes nutrition data such as calories, protein, carbs, fat, and health score, then gives advice based on the user’s profile and goals. After analysis, the meal can be saved directly into the day’s log, which immediately updates the dashboard targets and achievement progress.

The app also contains an admin-managed meal library. Admins upload meals with nutrition values, photos, and videos. On the user side, meals are grouped and displayed in a clean content-driven format, so users can browse real meal ideas rather than only raw nutrition numbers. This makes the platform much more practical for day-to-day use.

The exercise side works similarly. Admins upload exercise tutorials with muscle groups, difficulty level, equipment, and videos. Users browse exercises by muscle group, and when they select a category, they can view the exercises and play the tutorial videos directly. This turns the app into both a nutrition assistant and a workout guide.

There is also a reminder system that lets users create reminders for medicine, water, skincare, and workouts. This extends the app beyond fitness into daily wellness management, which makes it feel closer to a personal health companion than a simple tracker.

Uniqueness
The uniqueness of Fit Nova is that it combines AI analysis, structured health tracking, lifestyle reminders, admin-curated content, and media-based guidance into one system. Many apps focus on only one problem: calorie tracking, workouts, or reminders. Fit Nova unifies all of them.

Another key unique point is the admin-controlled intelligence model. Instead of relying only on AI-generated content, the platform uses AI for dynamic nutrition analysis and personalization, while keeping meals and exercises curated by admins. This is a stronger real-world product design because it balances automation with content quality and consistency.

The app is also unique in how it makes tracking actionable. Users do not just see calories; they see target achievement. They do not just see exercises; they see guided video-based categories. They do not just log food; they can analyze it first and save it instantly. That creates a smoother, more engaging user journey.

Why It Is Helpful
This project is helpful because health management is usually fragmented. People use one app for workouts, one for calorie tracking, one for hydration reminders, and often nothing for skincare or medicine reminders. Fit Nova reduces that fragmentation and gives users one dashboard for multiple aspects of wellness.

It is especially useful for people with specific goals like fat loss, muscle gain, or maintenance because the system personalizes targets instead of showing the same numbers to everyone. The AI food analysis also helps users make better decisions about what they eat, which is one of the hardest parts of health management.

The platform is also practical because of its admin CMS model. Admins can continuously improve the meal library, workout content, and tutorials, which means users get a growing, structured knowledge base rather than a one-time static app experience.

Technical
From a technical perspective, Fit Nova is built like a production-style full-stack application.

The backend uses Node.js with Express and TypeScript, providing REST APIs for authentication, profile management, food analysis, reminders, logs, progress, meals, exercises, and admin operations.

The database layer uses Prisma ORM with MySQL, connected to Google Cloud SQL. This stores user profiles, logs, reminders, meals, exercises, workout data, payments, and admin settings in a structured, scalable way.

The frontend consists of two React applications:

a user-facing web app for health tracking and interaction
an admin dashboard for managing content, branding, settings, meals, exercises, and analytics
AI functionality is integrated through Gemini, which is used for food analysis from images

**Challenges we ran into**

One major challenge we ran into was making the full system work reliably across multiple layers at once: admin panel, user app, backend APIs, AI integration, media handling, and cloud database connectivity. Because this was built in a hackathon-style timeline, time pressure made integration bugs much harder. Instead of debugging one isolated feature, we often had to trace issues across frontend, backend, and cloud infrastructure at the same time.

A specific issue was the backend database connection after moving from local setup to Google Cloud SQL. Admin settings, meal uploads, and user data updates were failing because the MySQL instance was not reachable from the backend during development. Under limited time, this became a critical blocker because it affected almost every feature. We solved it by properly configuring the Cloud SQL MySQL instance, enabling public IP access for development, authorizing the active network, verifying credentials, and reconnecting Prisma to the cloud database. Once that was fixed, the schema synced correctly and the system became stable.

Another challenge was AI integration with Gemini. At first, the API key setup looked correct, but requests were still failing because of quota and project configuration issues. This cost us time because the problem was not in the code itself, but in the API/project setup. We worked around it by testing the key directly, switching to the official Google GenAI SDK, and then rebuilding the food analysis flow more cleanly for both text-based food input and image-based food analysis. That helped us move from trial-and-error integration to a more reliable implementation.

We also ran into a frontend issue where the user dashboard would render for a second and then turn into a white screen on refresh. This was especially frustrating because it looked random at first. The root cause was a mismatch between the expected frontend response shape and the backend progress data that had just been extended. We fixed it by making the frontend defensive with safe fallbacks, so the page would keep rendering even if some progress fields were missing or delayed.

Another practical hurdle came from media playback. Admins were adding YouTube links for exercises and meals, but standard HTML video players cannot play YouTube URLs directly. This created a broken experience in the user app. We solved it by detecting YouTube links and embedding them properly, while still using the native video player for uploaded media files.

Overall, the biggest challenge was managing time while integrating many moving parts into one polished product. The way we overcame it was by prioritizing end-to-end functionality first, then debugging layer by layer, and finally improving the user experience after the system became stable. That process helped us turn a complex multi-module build into a working AI-powered health platform within a constrained development window.

**AI / ML**

Used Gemini 3.5 and Vision API engine to calculate calories portion protine etcs

**Sustainability**

`Fit Nova` supports sustainability in both a social and long-term digital sense.

From a social sustainability perspective, the project promotes healthier lifestyles through better nutrition awareness, hydration tracking, activity monitoring, and preventive daily care. By helping users understand calorie intake, portion size, macro balance, water consumption, and exercise consistency, the app encourages long-term healthy habits instead of short-term fixes. Features like reminders for medicine, hydration, skincare, and workouts make wellness more manageable and sustainable in daily life.

The platform is also sustainable because it is built around personalization. Generic health advice often fails because it does not adapt to the user. `Fit Nova` calculates goals based on age, weight, height, activity level, and fitness objective, which makes recommendations more realistic and easier to follow over time. This increases the likelihood that users stay engaged and maintain healthier routines.

From a content sustainability perspective, the admin-controlled architecture is important. Meals, exercises, workout media, and motivational content are managed from the admin dashboard, so the platform can keep evolving without rebuilding the app. This makes the product maintainable and scalable over time, which is critical for sustainability in a real-world digital health product.

From a technical sustainability perspective, the project uses cloud-based architecture with structured backend APIs, database models, and reusable content systems. Because it is modular, new features like advanced analytics, wearable integration, subscription plans, and multilingual content can be added later without changing the core system. That makes the platform sustainable not only for a hackathon prototype, but also for future product growth.

In short, the sustainability of `Fit Nova` comes from helping users build healthy routines that last, while also using a scalable and maintainable technical design that supports long-term growth and impact.

**Open Innovation**

This is a Health and Fitness Management Platform that helps users to maintain fat loss, live healthy, and Eat Healthy.

Team **Enigma Coders** -- [Subhajit Mondal](https://github.com/MSubhajitIND), [Udita Choudhury](https://github.com/uditachoudhury), [Abir Mondal](https://github.com/MondalAbir), [Siddhartha Chowdhury](https://github.com/Siddhartha0623)

`2026-03-11`

---

### Anebilin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anebilin-9a98) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SayanGhanty09/Doubbleslash) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/iZacFklUb-Y) [![Built at](https://img.shields.io/badge/Built%20at-DoubleSlash%204.0-0052CC?style=flat-square)](https://doubleslash4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Life is race, Health is the car

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Dsp](https://img.shields.io/badge/Dsp-333333?style=flat-square) ![Spectroscopy](https://img.shields.io/badge/Spectroscopy-333333?style=flat-square) ![PPG Analysis](https://img.shields.io/badge/PPG%20Analysis-333333?style=flat-square)

**The problem it solves**

To understand what's really going on inside your bloodstream, the current system requires a blood sacrifice. We live in the age of AI, but our first line of treatment in diagnosing Anemia (Hemoglobin) and Jaundice (Bilirubin) is 19th-century technology: the needle.
The Problem: The Status Quo is Broken, Painful, and Biased
1. The Needle Toll: Invasive Diagnostics
To test for anemia or liver problems, you need to endure painful pokes, biohazardous waste, and 24-48 hour delays.
2. The Smartwatch Illusion: Tech Bias
Smartwatches promise to monitor health using a "sophisticated" 2-color LED system with only Red and Green lights. They are nothing more than "dumb" pedometers that "go blind" on dark skin because melanin absorbs their weak light signals. They don't measure health; they guess using general AI models.
3. The Rural Blindspot
In developing nations like India, more than 50% of women suffer from anemia. Current screening requires labs and phlebotomists—services that a Rural Primary Healthcare Centre is unlikely to have.
The Pain Points: Who is Suffering?
 * The Expectant Mother: Having to travel 15 kilometers to a health clinic just to experience a painful needle prick to determine if she is dangerously iron deficient.
 * The Newborn Baby: Having to go through agonizing "heel pricks" to determine if she is suffering from Neonatal Jaundice because hospital equipment such as Transcutaneous Bilirubinometers are too expensive, costing more than $5,000.
 * The Elderly Patient: Having to strap on uncomfortable, squeezing "pneumatic cuffs" just to determine blood pressure trends.
 * People of Color: Buying a $400 smartwatch only to discover that SpO2 and Heart Rate monitoring are mathematically biased against their skin tones.
The Anebilin Solution: Diagnostics without the Puncture Wound
 * Anebilin replaces the needle with light:
Rather than drawing blood into a laboratory, we bring the laboratory to the blood.
Using a 14-channel medical-grade spectrometer, Anebilin performs a real-time optical biopsy.
 * We do not guess; we calculate:
Anebilin precisely calculates the exact AC Pulse from a DC Baseline.
 * Melanin-Proof:
Anebilin dynamically calculates a "Skin Tone Index" (Blue/NIR Ratio) to auto-calibrate LED power levels to ensure clinical accuracy regardless of your skin tone - pale, tanned, or heavily pigmented.

In the time it takes to tie a tourniquet, Anebilin performs a screen for Hemoglobin, Bilirubin, Heart Rate Variability, and Cuffless Blood Pressure.

**Challenges we ran into**

The main challenge was DSP and Custom driver implementation. The readily available drivers for our spectral sensor were slow and not versatile enough. We had to check out the manufacturer SDK and derive our own driver with custom SMUX to create fast data capture possible.

In DSP there were a lot of variables to change and test out to see which ones give the best outcome. Initially the waveform captured didn't clearly show peaks and troughs so we had to search up information about how professional medical grade PPG is done and generated our solutions based on that.

Third problem was solving on how we can auto correct for skin tone and tissue density because that's what separates a hobby project from a good one. We read many paper that suggested using RoR methods and thus we solved that final piece of puzzle too.

**Internet of Things(IoT)**

![image](https://assets.devfolio.co/content/86e42fc3f6044dcb9dce5797bd3ce750/9d189cc5-a5c7-4855-ac9f-4fecb9014217.jpeg)

Our project not only aims to give blood reports based on non-invasive scanning , but also close the bridge between the survey data and govt officials. As of now, ASHA worker go to villages, use needles to take blood samples, labs process that data which take 2-3 days, and the final details are written in pen and paper, which travels a time of 3 months to reach the govt officials who then act based on it. Our device can scan and provide reports instantly whilst uploading reports to the govt cloud in real-time. For example if jaundice/anemia breakout has happened in a village and we compare the scenario of Traditional vs Our Device, its certain that our device will perform faster and make the govt act faster towards the issue. After all its a digital world and everything should be interconnected and fast !

Team **Syntax_Error_404** -- [Rupam Betal](https://github.com/betalrupam), [Ankur Kumar](https://github.com/ankurlearner1), [Saaraswata Roy](https://github.com/saaraswata), [Sayan Ghanty](https://github.com/SayanGhanty09)

`2026-03-08`

---

### MediPal
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medipal-f486) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/falkeetsingh/HACKTU-MediPal) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hacktu-medipal.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/LsV3u4NfoP4) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Smart Medical Compliance and Recovery Partner

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Problem MediPal Solves

1. Doctors cannot verify whether patients actually follow prescribed lifestyle changes.
2. Patients often misreport or overestimate their exercise and recovery efforts.
3. Lack of objective data leads to wrong medical decisions.
4. Poor compliance worsens preventable conditions like diabetes and hypertension.

Results in unnecessary long-term medication and higher healthcare costs.
No structured system exists to track recovery and rehabilitation at home.

**Challenges we ran into**

Challenge: Ensuring user accountability in remote sessions without the high latency and privacy overhead of continuous video streaming or complex biometric AI.

Solution: Implemented a Randomized Keyframe Verification system. The application captures four snapshots at unpredictable intervals during the exercise. These frames are pushed to a clinician’s dashboard for asynchronous "spot-check" authentication. This ensures the correct patient is performing the movements while keeping the architecture lightweight and privacy-conscious.

Team **Sili-Kern Valley** -- [Navjyot Kaur](https://github.com/NavjyotKaur1510), [FALKEET SINGH](https://github.com/falkeetsingh), [Angaddeep Singh](https://github.com/AngaddeepSingh3108), [Gurprajas Kaur](https://github.com/prajas06), [Gurpratit Kaur  Saluja](https://github.com/gurpratit24)

`2026-02-08`

---

### HealthIQure
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthiqure-54df) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyam818/payload26-hackathon-project) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.healthiqure.xyz) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Healthier choices, Lower premiums, Better life

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![pyTesseract](https://img.shields.io/badge/pyTesseract-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![NoSQL](https://img.shields.io/badge/NoSQL-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

In India, health insurance remains expensive, complex, and inequitable, particularly for middle-class families. Most insurance providers determine premiums primarily based on age and past medical history, without adequately considering an individual’s current lifestyle or efforts to maintain good health.

As a result, several critical challenges exist in the current system:

**High Premiums for Middle-Class Families**
Many middle-income households struggle to afford increasing annual premiums, even when they actively follow healthy habits.

**Lack of Incentives for Healthy Behavior**
Individuals who exercise regularly, maintain balanced diets, and attend routine health checkups receive no financial benefits. This limits motivation for long-term health improvement.

**Late Detection of Health Conditions**
Existing policies do not emphasize preventive care. Consequently, chronic conditions such as diabetes, hypertension, and cardiac issues are often diagnosed at advanced stages.

**Risk of Sudden Premium Increases**
Policyholders face uncertainty due to the possibility of sharp premium hikes following unfavorable medical reports.

**Low Test Compliance and Awareness**
High costs, fear, and lack of awareness lead many users to avoid regular medical tests, increasing long-term health risks.

**Limited Access to Reliable Policy and Health Information**  
Many users find it difficult to understand insurance policies, recent updates, and health guidelines. General AI tools and online sources often provide outdated, incomplete, or inaccurate information, leading to confusion and poor decision-making.

**Financial Burden During Medical Emergencies**
Limited access to affordable insurance forces families to rely on loans or savings during health crises, causing long-term financial strain.

***How Our Solution Helps***

Our Health Score–Based Insurance System addresses these challenges through a preventive, transparent, and reward-driven approach.

The system:

1. Makes insurance more affordable for health-conscious individuals
2. Rewards consistent healthy behavior with premium discounts
3. Provides free or subsidized regular health checkups
4. Enables early detection of medical risks
5. Ensures gradual and predictable premium adjustments
6. Maintains full transparency in pricing mechanisms
7. Promotes long-term preventive healthcare
8. Provides accurate and up-to-date medical and policy guidance through a specialized RAG-based AI system

By linking insurance premiums to continuous health improvement rather than past illness alone, our solution creates a fair, predictable, and sustainable insurance model.

This approach empowers Indian families to take control of their health while ensuring financial security and long-term affordability.

**Challenges we ran into**

Challenges We Ran Into While developing this project:

We faced several technical and practical challenges related to designing a system that is both attractive to users and sustainable for insurers.

**1. Designing Offers That Users Truly Value**
One major challenge was deciding what kind of rewards and discounts would genuinely motivate people to maintain healthy habits. Simple discounts were ineffective, while complex benefit structures confused users.

***How We Solved It:***
We designed a balanced reward system that includes:

- Gradual premium discounts
- Free or subsidized health checkups
- Benefits for consistent health monitoring

This made the system easy to understand and financially sustainable.

**2. Balancing User Benefits and Insurer Sustainability**
Providing attractive incentives without affecting insurer profitability required careful planning.

***How We Solved It:***
We introduced:

- Capped monthly and quarterly premium changes
- Maximum discount and loading limits
- Age-based risk weighting

This ensured fairness and long-term stability.

**3. Encouraging Regular Health Checkups**
Many users hesitate to undergo frequent tests due to cost, fear, or inconvenience, leading to low participation.

***How We Solved It:***
We bundled essential tests with insurance plans and added reminders and reward points to encourage regular participation.

**4. Preventing Misuse and System Manipulation**
Some users attempted to avoid unfavorable results or make short-term lifestyle changes before testing.

***How We Solved It:***
We implemented:

- Approved laboratory networks
- Penalties for missed tests
- Trend-based scoring instead of single reports

This improved system reliability and fairness.

**5. Integrating Medical Data Securely**
Handling sensitive medical data required strict privacy and accuracy standards.

***How We Solved It:***
We implemented secure authentication, encrypted storage, and standardized data formats.

**6. Technical Challenges in AI and RAG Integration**
Integrating Retrieval-Augmented Generation (RAG) for personalized health guidance created issues such as slow responses, inaccurate document retrieval, and scalability limitations.

***How We Solved It:***
We optimized data indexing, improved embedding quality, and applied relevance filtering to enhance accuracy and performance.

**7. Large-Scale Deployment and System Performance**
Deploying the platform for large user volumes introduced challenges related to server load, latency, and data synchronization.

***How We Solved It:***
We adopted cloud-based infrastructure, load balancing, caching, and modular architecture to ensure scalability and reliability.

**8. Motivating Long-Term Behavior Change**
Sustaining user motivation over long periods was difficult after initial engagement.

**How We Solved It:**
We introduced milestone rewards, consistency bonuses, progress tracking, and personalized health insights.

**Open Innovation**

Our project aligns with Track 6: Open Innovation by combining **Technology**, **Finance**, and **Healthcare** to create a data-driven, fair, and transparent health insurance system.

**Technology Integration:**
We use AI-based scoring, automated data processing, and cloud deployment to convert medical test data into a dynamic Health Score and premium adjustment system. 

**Finance + Healthcare Innovation:**
The system links regular health check-ups with insurance pricing, ensuring that premiums reflect real health trends rather than static past risk. This enables better risk management for insurers and predictable low costs for users. 

**Practical & Scalable Impact:**
By introducing capped, gradual premium changes, anti-gaming safeguards, and age-based weighting, the solution supports sustainable insurance models while encouraging preventive healthcare. 

**Open Innovation Value:**
The platform helps people to manage healthcare costs better by rewarding healthy habits with lower premiums, ensuring affordable insurance and long-term financial security.

Team **Model Mavericks** -- [Priyam Das](https://github.com/priyam818), [Puneet Ranjan](https://github.com/Puneet), [Prithvi Sharma](https://github.com/prithvi)

`2026-02-02`

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

### PharmaConnect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pharmaconnect-9e0d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/skshmm11/PharmaConnect) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uuP5HaO27aE) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Search. Reserve. Pickup

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Every day, thousands of patients visit multiple pharmacies searching for a specific medicine, often returning empty-handed. There is no centralized platform that shows real-time stock availability across local pharmacies. This results in wasted time, delayed treatment, and frustration — especially for elderly patients and medical emergencies.

**Challenges we ran into**

## 🚧 Challenges I Ran Into

### 1. Python Environment Issues
Setting up Flask without a virtual environment was tricky — pip kept 
installing packages to a different Python than the one running the app. 
Solved by using `python -m pip install` to force the correct interpreter.

### 2. MongoDB Connection
MongoDB was not running as a service on Windows, causing connection 
refused errors. Had to install MongoDB manually and start it as an 
Administrator using `net start MongoDB`.

### 3. Real-Time Location Access
Browser GPS only works on localhost or HTTPS — not on plain file:// paths. 
Had to run the frontend through Live Server to get accurate GPS coordinates.

### 4. Role-Based Access Control
Differentiating between regular users, doctors, and pharmacy owners using 
the same login page required careful JWT payload design and route-level 
decorators in Flask.

### 5. CORS Between Frontend and Backend
The frontend (port 5500) and Flask backend (port 5000) are on different 
ports, which browsers block by default. Fixed using flask-cors with 
specific origin whitelisting.

### 6. Expiry & Stock Management
Building a system that automatically flags expired medicines, warns about 
medicines expiring within 90 days, and tracks low stock in real time 
required careful MongoDB querying and date comparison logic.

### 7. Barcode Integration
Real barcode scanning requires camera hardware access via browser APIs. 
For the demo, a simulated barcode lookup system was built using a mock 
database until real hardware is available.

Team **Tech titans** -- [tavishi sharma](https://github.com/Tavishisharma8), [Saksham Arora](https://github.com/skshmm11), Vartika Sharma

`2026-03-08`

---

### FitnessDarji
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fitnessdarji-f05a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fitnessdarji.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/yjnmQ7iBLds) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Make India Healthy

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

"Personalized fitness coaching is a luxury — Fitness | दर्जी makes it free for everyone."
Personalized coaching from trainers, nutrition experts, and dermatologists is out of reach for thousands of rupees per session in India and other parts of the developing world. It is especially out of reach for those who most need it: students, working professionals, Tier 2/3 city dwellers, etc.
Current fitness apps like MyFitnessPal, HealthifyMe, or Nike Training Club provide only general plans. They don’t know what’s inside your pantry or your body composition or your skin type or your schedule. They provide data but no direction.
How is Fitness | दर्जी going to solve this problem?
By providing a complete AI-powered personal health solution tailored to your needs, made specifically for you, in 60 seconds, and free of cost.
What is it replacing?
A personal trainer: workout plans and body scan analysis
A nutritionist: calorie targets and personalized meal plans from inside your pantry
A dermatologist: AI-based skin analysis and morning/evening routines
A health coach: 24/7 AI-powered chat with complete knowledge of your profile
A schedule manager: AI-powered reminders for your meals, water, workouts

**Challenges we ran into**

API Backend 
This was the biggest time sink of our project. We went through four different AI backends in one session:

Started with Anthropic Claude. Needed to get a paid key and had to set CORS headers with a special "anthropic-dangerous-direct-browser-access" header to access it directly in the browser
Moved to Google Gemini. Model "gemini-1.5-flash" was deprecated and gave us "model not found" error in version 1beta
Moved to "gemini-2.0-flash." Quota was immediately set to 0 because free tier quota was 0 for that key
Moved to "gemini-2.0-flash-lite." Same quota issue.

**AI / ML**

How Fitness | दर्जी Fits the AI/ML Track
Core AI Usage:

LLMs for meal plans, workouts, cheat meals, AI coach chat
Computer Vision for body scan + skin analysis (multimodal AI)
Prompt engineering with user biometrics injected as context
Structured JSON output extraction from LLM responses

ML Concepts Demonstrated:

Multimodal AI (text + image in same pipeline)
Context-aware personalization (RAG-lite — user profile grounds every prompt)
Model-agnostic architecture (Claude → Gemini → Ollama, one swap)
Edge/on-device inference via Ollama (no cloud needed)

Deterministic ML Layer beneath the AI:

Mifflin-St Jeor BMR equation
TDEE activity multiplier modeling
Goal-based macro optimization
Weight trajectory forecasting

Team **Divine Intervention** -- [Avik Singha Roy](https://github.com/avik3658-jpg), [Ishant Agarwala](https://github.com/ishantagarwala), [Satyam Chandra](https://github.com/chandrasatyam013-arch), [vivek dubey](https://github.com/dubevivekk)

`2026-03-11`

---

### AgroLens - Crop Disease Detection
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agrolens-crop-disease-detection-6997) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mayukh-7/Texibition-AgroLens) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://huggingface.co/spaces/Mayukh77/AgroLens) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uKZCg-Ijc40) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Crop Disease Detection for Healthier

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# 🌍 Real-World Problems Solved by AgroLens AI

AgroLens bridges the gap between advanced machine learning and practical, on-the-ground farming by addressing five critical challenges in modern agriculture:

### 1. The Expert Accessibility Gap
* **Problem:** Farmers often wait days for agricultural experts to diagnose crop issues, leading to crop loss and rapid disease spread.
* **AgroLens Solution:** Delivers **instant, on-demand diagnostics** for Rice, Corn, Wheat, and Potato crops using a Vision Transformer (ViT) model, turning any smartphone into an expert plant doctor.

### 2. Impractical, Generic Advice
* **Problem:** Standard agricultural advice ignores local environmental conditions, leading to wasted effort and money (e.g., spraying expensive chemicals right before a rainstorm).
* **AgroLens Solution:** Injects **real-time local weather data** (temperature and humidity) into the Gemini AI prompt, ensuring every treatment plan is context-aware and viable for the farmer's immediate environment.

### 3. The Language Barrier
* **Problem:** Most sophisticated agritech software is built exclusively in English, alienating the rural farming communities that need it most.
* **AgroLens Solution:** Features a native **multi-lingual engine** that instantly translates complex AI prescriptions and chat responses into English, Hindi, and Bengali.

### 4. Technological Friction
* **Problem:** Typing complex agricultural queries is difficult and time-consuming for users working in the field with dirty hands.
* **AgroLens Solution:** Implements **hands-free voice input**, allowing farmers to simply tap a microphone and speak to the AgroBot assistant naturally.

### 5. The Offline Disconnect
* **Problem:** Farmers need to purchase chemical remedies at local supply stores where internet connectivity is often unreliable or nonexistent.
* **AgroLens Solution:** Includes **one-click PDF generation** to export a clean, offline diagnostic report that farmers can easily hand to a local store clerk.

**Challenges we ran into**

# 🛠️ Technical Challenges Overcome

Building AgroLens required integrating complex machine learning pipelines with a responsive web frontend. Here are the core technical hurdles solved during development:

### 1. Heavy ML Model Deployment (OOM Errors)
* **The Challenge:** Serving a PyTorch-based Vision Transformer (ViT) requires significant RAM, causing standard free-tier hosting platforms to crash with Out-Of-Memory (OOM) errors before the application could even boot.
* **The Solution:** Containerized the Flask application using **Docker** and deployed it to Hugging Face Spaces, leveraging their specialized ML infrastructure to handle the heavy compute load without failing.

### 2. Mitigating LLM Hallucinations (Guardrails)
* **The Challenge:** When users uploaded non-leaf images (e.g., random objects or people), the generative AI would still attempt to provide agricultural advice based solely on the localized weather context, resulting in absurd hallucinations.
* **The Solution:** Engineered a **backend guard clause** that intercepts "Unidentified" or "Invalid" labels from the vision model's output. This short-circuits the LLM request entirely and instantly returns a clean, predefined warning to the UI, saving API tokens and ensuring reliability.

### 3. Asynchronous Audio State Management
* **The Challenge:** Integrating the Web Speech API created an internal event loop bug. The browser's automatic `onend` trigger was clashing with manual UI clicks, causing the microphone to instantly toggle back on immediately after the user tried to turn it off.
* **The Solution:** Implemented **explicit boolean logic (`forceStop`)** to cleanly decouple the browser's automated speech events from the user's manual UI interactions, ensuring clean state resets.

### 4. Multi-Modal Data Orchestration
* **The Challenge:** Providing isolated pieces of data to the AI resulted in generic, unhelpful responses.
* **The Solution:** Built a dynamic LangChain prompt architecture that successfully stitches together the Vision Model's diagnostic output, the Open-Meteo real-time weather data, and the user's language preference into a single, highly contextual LLM inference call.

### 5. Cloud Environment Security 
* **The Challenge:** Managing sensitive API keys while pushing application code to public GitHub repositories and cloud hosting environments.
* **The Solution:** Implemented strict `.gitignore` protocols for `.env` files and securely routed the Gemini API credentials through Hugging Face's encrypted Secrets manager to prevent automated bot scraping.

**Open Innovation**

We have made a  Crop disease detection web app using AI models such as Vision transformer

Team **CodeMind** -- [MAYUKH MAITY](https://github.com/mayukh-7), [Arindam Panigrahi](https://github.com/XDarindamXD), [AANSHU MISHRA](https://github.com/Aanshumis26), [Sourish Palit](https://github.com/Dr-SP1)

`2026-03-11`

---

### SARTHAK
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sarthak-2667) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PankajHacker1980/sarthak.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHDUOKxydE/KrekB-z5q_S4kQvM4cwYYw/edit?utm_content=DAHDUOKxydE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/WEbOWMy5RHk?si=oxuhcMUek8Ut07Hy) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Smart Ariel Response and Tracking for Health And K

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Unmanned Aerial Vehicles (Drones)](https://img.shields.io/badge/Unmanned%20Aerial%20Vehicles%20(Drones)-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square)

**The problem it solves**

During floods and natural disasters, thousands of people become stranded in remote forests, villages, and flooded regions where rescue teams struggle to reach them quickly.

Current Rescue Challenges:
* Manual Drone Monitoring
* Manual Ground Search
* Limited Communication

Major Consequences:
* Detection Delays
* Rescue Deployment Delays
* Uncertain Survivor Locations 

Real Impact

These delays can lead to:
*  Loss of critical survival time
*  Increased risk of dehydration, injuries, and hypothermia
*  Reduced chances of survival

**Challenges we ran into**

## Challenges I Ran Into

Building SARTHAK involved several technical and design challenges across both the drone system and the web-based command interface.

### 1. Drone Movement Simulation
One of the early challenges was implementing smooth and realistic drone movement on the map. Initially, the drone marker was jumping directly between points instead of moving smoothly. This made the simulation unrealistic.

To solve this, i implemented a gradual position update system where the drone moves step-by-step between coordinates, creating smooth motion that better represents real drone navigation.

---

### 2. Map Integration and Visualization
Integrating a map that could properly represent disaster zones and drone activity was another challenge. Some map layers were either too cluttered or did not clearly show the simulated flood area.

We solved this by selecting a simpler map layer and carefully positioning markers to represent survivors, drones, and key locations clearly.

---

### 3. Marker Interaction System
At first, the markers for survivors, trees, and houses were not interactive enough and did not provide useful information when clicked.

We improved this by adding interactive popups that display information about detected survivors and provide actions such as deploying a supply drone.

---

### 4. Mobile Compatibility
Since the system is designed to be usable in the field, the interface needed to work smoothly on mobile devices. Early versions of the dashboard were not properly scaled for smaller screens.

We redesigned the layout using responsive design principles so the dashboard now works well on phones, including devices similar to the iPhone 14.

---

### 5. Integrating Computer Vision for Detection
Simulating survivor detection using OpenCV required careful handling of camera frames and detection logic. Performance and detection accuracy were initial concerns.

I optimized the detection process and simplified the detection pipeline so that it could run reliably on a lightweight computing unit like a Raspberry Pi.

---

### 6. Coordinating Multiple Drone Roles
Another challenge was managing two drone roles in the system: a scanning drone and a supply drone. Initially both drones shared the same control logic which caused conflicts in movement behavior.

This was solved by separating their operational modes and assigning clear responsibilities to each drone within the system.

---

Despite these challenges, overcoming them helped improve the reliability, usability, and realism of the SARTHAK rescue system.

Team **Phantompulse** -- [Pankaj Kumar Saini](https://github.com/PankajHacker1980)

`2026-03-08`

---

### ForgetMeNot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/forgetmenot-33b7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Lothnic/hack-the-throne) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHApx90IDs/TZk8vjLloImqenTeTcCNMA/edit?utm_content=DAHApx90IDs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Built at](https://img.shields.io/badge/Built%20at-HACK%20THE%20THRONE-0052CC?style=flat-square)](https://hack-the-throne.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-powered memory companion for dementia patients.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

**ForgetMeNot addresses the heartbreaking reality of dementia-related memory loss.**

Over 55 million people worldwide live with dementia, and one of the earliest and most distressing symptoms is the inability to recognize loved ones. Patients may not remember their own children, lifelong friends, or daily caregivers—leading to confusion, anxiety, and social isolation.

### Current solutions fall short:
- **Photo albums** require manual browsing and don't provide real-time help
- **Whiteboards with names** need constant updating and offer no context
- **Caregivers repeating information** is exhausting and often forgotten within minutes

### How ForgetMeNot helps:

| Use Case | How It Works |
|----------|--------------|
| **Visitor arrives** | Instantly displays "Sarah, your daughter. Last visited Tuesday." |
| **During conversation** | Automatically extracts and saves relationship information |
| **Caregiver handoff** | Dashboard shows all interactions and conversation history |
| **Daily routines** | Tracks who visited and what was discussed |

### What makes existing tasks safer and easier:
- Patients can engage more confidently in conversations with visual prompts
- Caregivers spend less time re-explaining who people are
- Family members feel recognized, reducing emotional distress on both sides
- Medical staff can review conversation logs for cognitive assessments

**Challenges we ran into**

## Challenges I Ran Into

### 1. Real-time Face + Voice Synchronization
**Problem:** Matching a person's face to their voice when multiple people are present was tricky. The face detection runs in the browser while audio processing happens on the backend—they operate at different speeds.

**Solution:** We implemented an event-driven architecture with SSE (Server-Sent Events) that broadcasts updates to the frontend. When the LLM extracts a name, we associate it with the most prominent face detected at that moment.

### 2. Split-Brain Database Issue
**Problem:** We initially had two separate services writing to different databases—MongoDB and Convex. This caused relationship data to be lost between restarts.

**Solution:** Consolidated all persistence to Convex and refactored the LLM extraction logic into the main backend service.

### 3. Dementia-Friendly UI Design
**Problem:** Typical web UIs with small text and complex layouts cause confusion for dementia patients.

**Solution:** Redesigned with accessibility in mind: large fonts, high contrast, minimal cognitive load, and a calming color palette.

Team **Team CIPHER** -- [Raj Singh](https://github.com/zyphorixx), [Prateek Singh](https://github.com/Prateek0217s), [Ayush Kumar Rai](https://github.com/Ayush-rai23), [Mayank Joshi](https://github.com/lothnic)

`2026-02-08`

---

### Sanjeevani
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sanjeevani-aaff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sujal01go/sanjeevani) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=ZGAs0g029LM) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Herbal Wellness and Ordering

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Access to reliable herbal healthcare information is limited, fragmented, and often unverified, while farmers growing medicinal plants lack direct access to consumers. People suffering from common health issues like breathing problems, digestion, or immunity concerns and chronic diseases like fatty liver, diabetes, cholesterol either depend on synthetic medicines or unreliable online advice. There is no unified platform that provides, trusted herbal recommendations backed by medical research while also giving them an opportunity to buy those rare herbs. This results in misinformation, higher costs, non-availability and underutilization of India’s rich medicinal plant ecosystem.

**Challenges we ran into**

One of the biggest challenges we faced was ensuring the accuracy and safety of medical and herbal information, as health-related data is often unstructured and scattered across multiple sources. Mapping diseases and symptoms to appropriate medicinal plants was complex because a single condition can have multiple causes and severities, and each herb can be used in different forms and dosages. While building the AI chatbot, we had to carefully balance intelligent recommendations with user safety, making sure the system does not replace professional medical advice or provide harmful suggestions. Integrating a farmer-to-consumer model added another layer of complexity, as herbs needed to function both as healthcare solutions and marketplace products with authenticity and trust. Additionally, simplifying complex medical and traditional knowledge into clear, user-friendly explanations within limited hackathon time was a significant challenge.

**Google Gemini**

We  have used Gemini and Groq APIs for AI based suggestions

Team **NightHawks** -- [Yamya Nayyar](https://github.com/nayyaryamya-cmd), [Aditya gupta](https://github.com/Adityagupta2007), [Ishandeep Singh](https://github.com/Ishan2511), [Nandini Sharma](https://github.com/nandinisharma0711), [Sujal kumar](https://github.com/sujal01go)

`2026-02-08`

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

### SwasthyaSetu – Smart Emergency Healthcare System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/swasthyasetu-smart-emergency-healthcare-system-199d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Garvv1501/Vision-Vortex) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHDTZEsiDU/P3VmzCunnrw5WZ54pk507g/edit) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI Emergency Response Network

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Problem Statement

In medical emergencies, delays in identifying the severity of symptoms and arranging timely ambulance services can lead to critical health risks. Many people are unable to quickly determine whether their symptoms require immediate medical attention, and there is often a lack of coordination between patients, ambulance drivers, and hospitals. This delay in communication and response can reduce the chances of timely treatment and affect patient outcomes.

Proposed Solution

SwasthyaSetu is an AI-powered emergency healthcare platform that helps patients quickly understand the seriousness of their symptoms and take the right action. Using an AI health assistant, the system analyzes symptoms and classifies the emergency level. Based on the severity, patients can instantly request an ambulance while drivers receive pickup details and navigation support. This platform aims to reduce response time, improve coordination, and provide faster access to emergency medical care.

Team **Vision Vortex** -- Abhishek Singh Shekhawat, Garv Chugh, Shivang Agrawal

`2026-03-07`

---

### Malaria Detection Using Deep Learning
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/malaria-detection-using-deep-learning-4a1d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gajenderyadav644-spec/Malaria-AI-Detection) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/e6bc210764ba45118e3ef70b1ba3ce2b) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart malaria diagnosis with deep learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Malaria is one of the most dangerous infectious diseases worldwide, especially in tropical and developing regions.
Traditional malaria detection relies on manual microscopic examination of blood smears, which has several challenges:
- Time‑consuming: Manual analysis takes significant time, delaying treatment.
- Human error: Accuracy depends on the skill and experience of the technician.
- Resource limitations: Many rural or under‑resourced areas lack trained professionals and advanced lab facilities.
- Late diagnosis: Delayed detection increases the risk of severe illness or death.


 How This Project Helps
The Malaria AI Detection Dashboard addresses these challenges by:
- Automating detection: Uses a trained deep learning model (CNN) to classify blood cell images as Malaria Infected or Normal.
- Improving accuracy: Reduces human error by leveraging AI predictions with confidence scores.
- Saving time: Provides instant results after image upload.
- Supporting doctors: Includes a recommendation panel with suggested actions and preventive tips.
- Visual insights: Interactive charts show infection distribution and parasite stage counts for better understanding.
- Accessible design: A simple web dashboard that can be deployed in clinics, labs, or even educational settings.

**Challenges we ran into**

- Dataset Quality & Preprocessing
- The malaria cell image dataset contained variations in size, lighting, and noise.
- I solved this by resizing all images to 64×64 pixels, normalizing pixel values to the 0–1 range, and applying augmentation techniques (rotation, zoom, flip) to improve generalization.
- Model Accuracy vs Overfitting
- During training, the CNN achieved high accuracy on the training set but dropped significantly on the validation set (overfitting).
- To address this, I used validation splits, added data augmentation, and carefully tuned the number of epochs.
- Backend–Frontend Integration
- Passing predictions from Flask backend to the frontend and updating dynamic charts was tricky.
- I solved this using Jinja2 templates ({{infected}}, {{normal}}) and binding Chart.js with backend data.
- File Upload & Security
- Uploaded files sometimes had unsafe names that caused errors.
- I used secure_filename() from Werkzeug to sanitize filenames and prevent crashes.
- Doctor Recommendation Logic
- The AI model only predicted infected/normal, but I also needed parasite counts and doctor recommendations.
- I simulated parasite counts using random values (demo purpose) and hard‑coded recommendations for infected vs normal cases.
- UI/UX Design
- Designing a professional dashboard that matched the logo theme (pastel skyblue transparent look) was challenging.
- I solved this with CSS gradients, transparency (rgba), animations (fadeIn, fadeInUp), and a responsive grid layout.
- Deployment Issues
- Running Flask locally was smooth, but deployment caused errors with static files and upload paths.
- I fixed this by ensuring the upload folder exists (os.makedirs()) and correcting relative paths.

**Requestly – Creative Use Challenge**

For this project, the following partner track was applied:

- *Requestly*  
  Integrated to manage and optimize network requests during development and testing.  
  This helps ensure smooth communication between the AI backend and the dashboard frontend.

Team **Botbuilder** -- Sonu Chaudhary, Deepak Bagotiya, Gajender Kumar

`2026-03-07`

---

### Niraksh Guardian
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/niraksh-guardian-0c0d) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-powered digital Healthcare Assistance.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Healthcare information today is fragmented, confusing, and often inaccessible to the average person. When individuals experience symptoms, their first instinct is usually to search online. However, this leads to overwhelming and unreliable information, making it difficult to understand the seriousness of the situation or determine the right next step.

Most existing healthcare platforms focus on only one part of the healthcare journey. Some platforms store medical records, others allow doctor appointments, and some provide basic symptom checkers. However, these solutions rarely help users truly **understand their health condition or guide them toward the right medical action**.

For example, systems like **ABHA under the Ayushman Bharat Digital Mission (ABDM)** provide a digital health ID and medical record storage, which is valuable infrastructure but does not help users interpret symptoms or navigate healthcare decisions. On the other hand, many global symptom checker apps provide possible conditions but lack contextual guidance, personalized explanations, or connections to appropriate specialists.

As a result, users often face several challenges:

- Difficulty understanding symptoms and their possible causes  
- Confusion about which type of doctor to consult  
- Anxiety caused by unreliable or exaggerated internet search results  
- Limited understanding of prescriptions, medications, and potential interactions  
- Lack of a single platform that connects symptom understanding with healthcare guidance  

These gaps create a need for a **patient-centric digital health companion** that does more than simply store data or list possible diseases.

**Niraksh Guardian addresses this problem by acting as an intelligent health companion that helps users interpret symptoms, understand medical information, and navigate their healthcare journey with confidence.**

**Challenges we ran into**

## Challenges I Ran Into

Building Niraksh Guardian required solving several technical and conceptual challenges, especially because the platform combines healthcare logic, AI interpretation, and real-world usability.

### 1. Accurate Symptom Understanding
One of the biggest challenges was interpreting user symptoms correctly. People often describe symptoms in natural language that can vary widely in wording and detail. Early versions relied on keyword-based mappings, which were limited and inaccurate. We had to design a more flexible approach that combines semantic understanding with structured symptom categories.

### 2. Mapping Symptoms to the Right Specialist
Determining which medical specialist a user should consult is not straightforward. Many symptoms overlap across different conditions and specialties. Creating a reliable recommendation system required building structured mappings between symptoms, diseases, and specialist categories while maintaining clarity for users.

### 3. AI Safety and Medical Responsibility
Healthcare applications require extra caution. AI responses must avoid giving definitive diagnoses or misleading information. We had to carefully design prompts and guardrails to ensure the AI provides **informational guidance rather than medical decisions**, while still being useful and understandable.

### 4. Balancing AI with Deterministic Logic
Relying entirely on AI can produce unpredictable results, while relying only on rule-based systems limits flexibility. We needed to design a hybrid architecture that combines deterministic logic for reliability and AI reasoning for flexibility and natural interaction.

### 5. Structuring Healthcare Data
Healthcare data such as symptoms, medications, diseases, and doctor specialties needed to be organized in a way that supports both fast queries and meaningful recommendations. Designing this structure required careful planning to ensure scalability and maintainability.

### 6. Building a Clean and Accessible User Experience
Health platforms must be extremely simple to use. Presenting complex medical information in a clear and non-intimidating interface required multiple design iterations to ensure users can easily understand results, suggestions, and explanations.

### 7. Integrating Multiple System Components
Niraksh Guardian includes several interconnected modules such as symptom analysis, doctor recommendations, prescription explanations, and AI chat assistance. Ensuring smooth communication between these components while maintaining performance and reliability was a significant engineering challenge.

Despite these challenges, solving them helped shape Niraksh Guardian into a more reliable and practical digital health companion.

Team **Niraksh** -- Sachin Nishad, [Adarsh Suman](https://github.com/adarsh3699), Ayush Faujdar, [Rashmi Joshi](https://github.com/Rashmijoshi18)

`2026-03-08`

---

### City Health
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/city-health-83a3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shekhar13hub/hospital-project.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/zs88kQU0xMw?si=Vk61dU1ItXpBYikX) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Book your Appointments

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Our healthcare site empowers patients and providers with secure, easy-to-use digital tools. Patients can book appointments online, access medical records, and connect with doctors through telemedicine, saving time and reducing travel. Providers benefit from streamlined scheduling, instant documentation, and HIPAA-compliant communication. Built-in safety features like data encryption and role-based access ensure privacy and trust. Automated systems reduce errors in prescriptions and scheduling, while analytics help providers make informed decisions. By simplifying administration, improving accessibility, and enhancing transparency, our platform makes healthcare safer, faster, and more patient-centered—bringing quality care closer to everyone.

**Challenges we ran into**

While building the healthcare site, one major hurdle was ensuring secure user authentication without compromising ease of access. Initially, the login system caused repeated session timeouts, frustrating users and disrupting workflows. The challenge lay in balancing strong encryption with smooth performance. To overcome this, I implemented token-based authentication combined with optimized session management, which reduced unnecessary logouts while maintaining strict security standards. Rigorous testing across devices helped confirm stability. This fix not only improved user experience but also reinforced trust by safeguarding sensitive health data. The process taught me the importance of aligning usability with robust security measures.

Team **Debug thugs** -- Nikhil Singh, Arman Thakur, Sudhanshu Shekhar, ADITYA THAKUR

`2026-03-08`

---

### Vitalis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitalis-6c01) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/adhritbudhiraja-lang/Dense-Apocalypse-.git) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Health Companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

**The Problem Vitalis Solves****

*Fragmentation*

Health management today is scattered across dozens of apps. One for calories, one for mood, one for posture reminders, one for journaling. None of them talk to each other. You never get a complete picture of your health.

*No Intelligence*

Most health apps are just glorified spreadsheets. They show you numbers but never tell you what to do about them. You log 2000 calories and get a bar chart. That's it. No context, no advice, no connection between your diet and how you're feeling.

*Privacy*

Every mainstream health app sends your data to the cloud. Your weight, your mood, your stress levels — all stored on someone else's server, monetised through ads or sold to third parties.

*Cost*

The apps that do offer AI insights lock them behind $10–20/month subscriptions. Students and young professionals simply don't pay for that.
The Indian Gap
Every food database is built around Western diets. Try logging dal makhani, chole bhature, or makki di roti — you'll find nothing. Indian users are completely underserved.

**What Vitalis Does Differently**

It puts everything in one place — diet, mental health, posture, journaling — and connects them through AI that understands your full picture. It runs locally so your data never leaves your machine. It uses free AI so there's no subscription. And it has a real Indian food database built for users like us.
One app. Complete health. Free. Private.

**Challenges we ran into**

**Challenges We Ran Into**

**Posture Detection in 2D

The biggest technical wall. A front-facing webcam only gives you a flat 2D image — there is no depth information. Forward hunching, which is the most common bad posture, requires knowing how far your head is from your shoulders in 3D space. We had to engineer a proxy — using the rate of change in shoulder width as an indicator of forward lean — but it has limits. A person looking straight down still scores well because their shoulders look fine from the front. Real depth detection needs a RealSense or similar depth camera.
MoveNet Reliability Across Lighting Conditions
The skeleton tracking works well in controlled lighting but degrades fast in low light, strong backlight, or when the user isn't centred in frame. We built a calibration phase and 60-frame smoothing to reduce false positives, but the model itself is sensitive to conditions we can't control.

*Mental Health Date Bug*

The check-in system was updating the same day's log instead of creating a new one the next day. The root cause was subtle — the date was frozen at component mount time inside a useState, so even if you came back the next day the app thought it was still yesterday. Took time to trace it through both the frontend state and the backend route, which was also ignoring the date parameter being sent to it.

*Food Database Macro Data*

The original Kaggle dataset only had calorie counts — no protein, carbs, or fat breakdowns. We had to engineer macro values for all 862 foods using category-based ratio formulas and name-based overrides for known foods. It is estimated data, not lab-measured, so accuracy varies especially for mixed dishes.

*Quantity Scaling Architecture*

Adding quantity to the diet planner sounds simple but required rethinking the form state entirely. The form needed to store base-per-serving values separately from the displayed scaled values, so that changing quantity from 1 to 2 correctly doubles the macros without corrupting the base reference. Getting the state flow right without stale closure bugs took careful design.

*GitHub Push Protection*

Git history is permanent. Once a secret key gets committed — even in an old commit you've since deleted — it lives in the object store. Every orphan branch, every fresh history rewrite, still carried that commit hash. The only real solutions are rewriting history with BFG or simply allowlisting it through GitHub's security portal. We lost meaningful time on this during a time-critical night.

*Local Database Limitations*

lowdb is a flat JSON file. It has no transactions, no indexing, and no query optimisation. As the health.json file grows with months of logs, every read scans the entire file. It works perfectly for a hackathon prototype but would need to be replaced with SQLite or PostgreSQL for any serious long-term use.

Team **Dense Apocalypse** -- Aakash Anand, Anshika mittal, Adhrit Budhiraja, Vidhi Virmani

`2026-03-08`

---

### NeuroGuard
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neuroguard-a812) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Amarjeet-Singh27/Devforge_Neuroguard.git) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> listen to your brain, Secure your health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square)

**The problem it solves**

Our project (NeuroGuard) solves these core problems:

1. Early risk screening gap: people may miss early stress/neurological warning signs.
2. Counterfeit medicine risk: users need batch authenticity + supply-chain traceability.
3. Fragmented workflow: combines screening, reporting, medicine verification, and support in one platform.

**Challenges we ran into**

Challenges faced while building (from your docs/codebase):

1. Audio handling reliability across formats (wav/mp3/m4a) and FFmpeg dependency.
2. Browser microphone constraints (HTTPS/localhost requirement) for voice capture.
3. OTP/email reliability (SMTP config issues), solved with fallback OTP mode for demo continuity.
4. Deployment constraints: persistent uploads + SQLite + audio processing are better on Render/Railway/Fly than pure serverless.
5. Demo hardening still in progress: end-to-end deployed voice/PDF flow, mobile consistency, and more edge-case tests.

Team **DevForge** -- [SUMIT PANDEY](https://github.com/Sumit01997), [SANDEEP KUMAR](https://github.com/sandeep0067), [Amarjeet Singh](https://github.com/Amarjeet-Singh27), [SHIVANSH SHARMA](https://github.com/shivansh093)

`2026-03-08`

---

### HealthFirst-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthfirstai-c107) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DakshWalia17/HealthFirst-AI) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Making medical data speak human

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square)

**The problem it solves**

**🚀 The Problem We Solved**
Patients often struggle to understand complex medical jargon in their lab reports, while doctors spend crucial hours manually scanning normal reports just to find anomalies. **HealthFirst AI** solves both issues by providing simplified AI-driven insights for patients and a smart, triaged inbox for doctors.

**✨ Key Features**
# For Patients: Instant AI Analysis of PDFs, Audio Prescriptions, Actionable Next Steps (Diet/Tests), and an Interactive AI Chatbot.
#For Doctors: Smart Triage Inbox (High/Moderate/Low risk), Time-Saving Dashboard with full-screen graphs, and Role-Based Access Control.

** 💻 Tech Stack**
#Frontend: HTML5, Tailwind CSS, Vanilla JS, Chart.js
#Backend: Python, FastAPI, Uvicorn
#AI Engine: Google Gemini Pro (JSON Structuring)
#Database: Lightweight JSON-based Local DB (Optimized for MVP speed)

**Challenges we ran into**

Building HealthFirst AI within a tight hackathon timeframe presented a few major technical hurdles:

Strict JSON Formatting from Unstructured PDFs: Extracting raw medical data from varied lab reports and forcing the Gemini AI to consistently output a strict, parsable JSON structure (for our Chart.js graphs) required extensive prompt engineering.

Dynamic Role-Based UI Routing: Implementing seamless Role-Based Access Control (RBAC) between Patient and Doctor portals on a single-page Vanilla JS setup was tricky. We ran into complex DOM manipulation and CSS z-index overlap issues while switching dashboards, which we successfully resolved using precise state management.

Lightweight Data Persistence: To prioritize speed and avoid the overhead of setting up a heavy SQL/NoSQL database during the hackathon, we built a custom JSON-based local database. Managing concurrent read/writes and maintaining session states across our FastAPI routes required careful logic.

Team **MKD^2** -- Mohit Mohit, Kirti Verma, DAKSH Walia, Diksha Sharma

`2026-03-08`

---

### MedLens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medlens-5367) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/adarsh-dev01/medlens) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Early health insights powered by AI.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# MedLens

MedLens is an AI-powered medical triage platform built using Next.js and TypeScript.

## Features
- Symptom triage
- Voice input
- Accessibility support
- Modern UI

## Tech Stack
- Next.js
- TypeScript
- Tailwind CSS

Team **return1** -- Aayush ., Adarsh Gupta, Subham Kumar

`2026-03-08`

---

### Health Hub
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/health-hub-6511) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Pranav8307/Medi) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart Care. Seamless Connections

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square)

**The problem it solves**

Patients often struggle to track their health information in one place, and accessing medical guidance quickly can be difficult. At the same time, doctors may not have an organized view of a patient’s past symptoms, habits, and reports, which makes diagnosis and decision-making harder. This results in delayed care and inefficient consultations.

**Challenges we ran into**

The platform has multiple components — a mobile app, backend server, AI service, and web portals for doctors and admins. Making sure all these systems communicated correctly was challenging.

Team **CTRL ALT ELITE** -- Dolli -, Shashank Kumar, Pranav Kumar, [Aditya Sharma](https://github.com/aditya-sharma)

`2026-03-08`

---

### sawasthya ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sawasthya-ai-e5ff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sagarninu4-rgb/Sawasthya--ai.git) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> your health care partner

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Swasthya solves the problem of fragmented and delayed healthcare by providing a unified, AI-driven platform. It addresses four core pain points:

-Information Gap: The AI Symptom Checker and Report Analyzer provide immediate medical insights, removing the confusion of complex health data.

-​Emergency Delays: The SOS button and GPS-linked Hospital Finder (3km radius) provide instant access to life-saving care during a crisis.

-​Medication Neglect: The Medicine Reminder ensures treatment compliance, preventing health setbacks from forgotten doses.

​-Inaccessibility: By combining a Medical Store, AI Chatbot, and Diagnostics into one app, it eliminates the need for multiple platforms.

**Challenges we ran into**

One of the most significant hurdles during the development of Swasthya was the GPS-based Hospital Finder integration.

The Challenge: Accuracy vs. Performance
The goal was to filter hospitals within a strict 3km radius using live GPS coordinates. The initial hurdle was a latency issue—the application would lag while trying to fetch, filter, and render multiple map markers simultaneously, which is dangerous in an emergency scenario.

The Solution
-To overcome this, I implemented client-side geofencing and optimized the backend queries:
Haversine Formula: I used the Haversine formula to calculate distances between the user's coordinates and the hospital database more efficiently.
-Debouncing: I applied a "debounce" to the search input so the API wouldn't get overwhelmed with requests every time the user moved slightly.
-Asynchronous Loading: I moved the map rendering to an asynchronous process so the SOS button and UI remained responsive even while the location data was still loading.

Team **CodeNova** -- Aman Singh, Armaan Kath, sagar saini, Arnav Anurag

`2026-03-08`

---

### MediConnect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mediconnect-fbca) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1171428034?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Transforming healthcare sector

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![OpenAI API](https://img.shields.io/badge/OpenAI%20API-333333?style=flat-square)

**The problem it solves**

We built MediConnect — an integrated digital healthcare platform.

The platform combines AI assistance with healthcare services to create a unified patient experience.

Core capabilities:

• AI-powered health assistant for medical queries• Smart doctor recommendation based on symptoms• Seamless appointment booking and scheduling• Medication reminders for better treatment adherence

This transforms healthcare into a proactive, intelligent, and patient-centered system.

Team **Woomen** -- Prerna Sharma, Nishtha Chhabra

`2026-03-08`

---

### MediRush
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medirush-ce37) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Gourabrik/MediRush-CodeBuds) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://medirush-app.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/jbVvbetWltU?si=UzScmkZUkrvmzd37) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Healthcare at your fingertips.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square)

**The problem it solves**

### **The Problem It Solves**
In critical medical situations or routine healthcare management, accessibility, transparency, and speed are often the biggest challenges. Patients and their families frequently struggle with fragmented healthcare services, delayed emergency responses, and a lack of real-time information. 

**Medirush** solves this by unifying emergency services, doctor discovery, and medical facility tracking into a single, intelligent platform. It significantly reduces the friction and panic associated with seeking medical help by providing real-time data, AI-driven triage, and instant access to localized healthcare resources.

### **What Can People Use It For?**

1. **Instant, Transparent Ambulance Dispatch:**
   - Instead of calling multiple hotlines and waiting in the dark, users can view a live, interactive map displaying nearby hospitals and their available ambulances.
   - Users can instantly see the **ETA** and **transparent pricing** for different types of ambulances (Basic Life Support, Advanced Life Support, ICU), ensuring they get the right vehicle for their specific emergency without hidden costs.

2. **AI-Assisted Emergency Triage:**
   - In high-stress situations, users might struggle to navigate a complex app or convey the exact nature of an emergency. The **AI Ambulance Agent** allows users to quickly describe their situation in natural language. 
   - The AI acts as a sophisticated first responder, assessing the severity of the emergency, dynamically gathering user profile data (location, contact info, patient name), and immediately initiating the optimal ambulance dispatch process.

3. **Hyper-Local Healthcare Discovery (Doctors, Hospitals & Pharmacies):**
   - Utilizing real-world data (via OpenStreetMap/Overpass API), users can locate the nearest hospitals, specialized doctors, and pharmacies based on their live GPS location.
   - Users can filter and browse doctors by specialization (Cardiologist, Neurologist, etc.), view ratings, and check available time slots, drastically reducing the time spent researching and calling clinics.

### **How It Makes Existing Tasks Easier, Faster, and Safer:**

* **Safer Emergency Response:** By mapping the precise live location of the user and routing the nearest available ambulance directly to them, Medirush eliminates geographical confusion and shaves crucial minutes off response times.
* **Eliminates Decision Paralysis:** During an emergency, people panic. By presenting clear, actionable choices (e.g., "Advanced Life Support - 8 mins away - ₹1200") on a map rather than a static list or a phone menu, users can make fast, informed decisions.
* **Reduced Cognitive Load via AI:** The AI chatbot agent takes over the heavy lifting in data entry. It dynamically pre-fills booking forms with the user's saved profile data and location, meaning a patient or bystander only needs to confirm rather than type out long addresses while under duress.
* **Consolidates the Healthcare Journey:** Currently, a user might use one app to find a pharmacy, Google Maps to find a hospital, and a phone call to book an ambulance or doctor. Medirush centralizes this entire journey, ensuring continuity of care from the moment an emergency occurs to post-care consultations.

**Challenges we ran into**

### **Challenges We Ran Into**

Building a real-time, location-aware healthcare platform came with several significant technical hurdles. Here are a few specific challenges we encountered and how we overcame them:

**1. Integrating Real-World Map Data with Next.js (SSR Issues)**
* **The Hurdle:** We initially built our interactive map using mock data. When transitioning to real-world data using the Overpass API (OpenStreetMap) and React Leaflet, we immediately hit `"window is not defined"` errors. Next.js tries to server-side render (SSR) components by default, but Leaflet relies heavily on the browser's `window` object to manipulate the DOM for maps.
* **The Solution:** We resolved this by dynamically importing Leaflet components (`MapContainer`, `TileLayer`, `Marker`) with Next.js’s `next/dynamic` and explicitly setting `{ ssr: false }`. We also had to manage the loading state carefully to ensure the map only initialized after the component mounted on the client.

**2. Firebase Google Authentication Configuration Errors**
* **The Hurdle:** While implementing the user login system, we kept running into a frustrating `auth/configuration-not-found` error when users attempted to sign in via Google. The authentication worked sporadically but failed consistently on the local development server.
* **The Solution:** After digging through the Firebase documentation and our console settings, we realized the issue was with the OAuth authorized domains. We had to explicitly whitelist `localhost`, `127.0.0.1`, and our eventual production domain in the Firebase Authentication settings to allow Google Sign-In to process requests securely from our Next.js development environment.

**3. State Management Between the AI Agent and the Booking Flow**
* **The Hurdle:** Building the **AI Ambulance Agent** was complex. We wanted the AI to feel proactive, meaning it needed to pull the logged-in user's profile data (name, phone number, exact GPS location) and pre-fill the ambulance booking form without the user needing to type anything. Passing this asynchronous state between the chat interface, the interactive map, and the final booking modal caused race conditions where the form would render before the AI had extracted the necessary data.
* **The Solution:** We refactored our state management to use a centralized context for the user profile and explicitly passed a callback function from the parent booking component into the AI agent. This ensured the AI could directly trigger the `onRequestAmbulance` event with structured JSON data only *after* all user parameters were verified and fully loaded.

**4. Overpass API Rate Limiting and Data Filtering**
* **The Hurdle:** When querying hospitals and pharmacies within a 20km radius using the Overpass API, the raw data returned was often messy. Some nodes lacked names, others were strictly administrative buildings rather than active clinics, and calculating precise distances for routing dynamically was slow.
* **The Solution:** We optimized our Overpass query to specifically filter out unnamed nodes (`node["amenity"="hospital"]["name"]`) and implemented a fallback mechanism. We added a client-side Haversine formula calculation to rapidly compute distances between the user's geolocation and the fetched hospitals, sorting them instantly before rendering, rather than relying on external routing APIs for every single node.

**Open Innovation**

### **Tracks Applied**

-  **Health & Wellness** *(Primary Track)*
  The entire platform is purpose-built around healthcare — from AI-powered ambulance dispatch and real-time doctor discovery to emergency triage and pharmacy locating.

-  **AI / Machine Learning**
  The **AI Ambulance Agent** uses natural language processing to simulate an intelligent first-responder. It dynamically interprets user input, extracts patient context from their profile, and orchestrates the booking flow without manual form-filling.

-  **Open Source & Open Data**
  MediRush is powered entirely by **OpenStreetMap** and the **Overpass API** for sourcing real-world hospital, clinic, and pharmacy data — championing open geographic data for social good.

-  **Social Impact**
  By making ambulance booking transparent (visible ETA + pricing), reducing response times, and centralizing fragmented healthcare services into one accessible app, MediRush directly addresses healthcare inequality and access gaps — especially in emergency situations where every second matters.

- 🔐 **Firebase / Google Cloud**
  User authentication is built on **Firebase Auth** (with Google Sign-In), and user profile data is persisted in **Firestore** — leveraging the Google Cloud ecosystem for a secure, scalable backend.

Team **CodeBuds** -- [Gourab Biswas](https://github.com/Gourabrik), [Anisha Aktar](https://github.com/anishaaktar1105-sys), [Sumana Majumder](https://github.com/notifications), [Somok Das](https://github.com/somok552?tab=repositories)

`2026-03-11`

---

### Heath Wealth
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/heath-wealth-e09d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyanshu24-creation/Health-Wealth.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://health-wealth-472u.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smarter Health, Stronger Life

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Many people struggle to identify health issues early, find nearby medical help quickly, and keep track of their symptoms or wellness data in one place. Health Wealth solves this by providing a platform where users can monitor symptoms, access nearby clinics, and make informed health decisions easily.

**Challenges we ran into**

Challenges We Ran Into

1. Backend setup issues
Setting up the Node.js backend required resolving missing dependencies like Express, Nodemailer, and Mongoose, which initially prevented the server from running.

2. Database integration
Integrating MongoDB with Mongoose and configuring environment variables correctly was challenging, especially ensuring the database connection worked properly.

3. Environment configuration
Managing .env variables for database URLs, email services, and API keys required careful setup to avoid runtime errors.

4. Email service setup
Configuring SMTP for sending emails (appointment requests and contact forms) required handling authentication and testing with mock services during development.

5. API structure and routing
Designing clear backend APIs for authentication, clinic search, symptom tracking, and contact forms while keeping the code organized was challenging.

6. Full-stack integration
Connecting the frontend pages with backend APIs and ensuring smooth data flow between them required debugging and testing multiple endpoints.

**Health & WellBeing**

Health Wealth fits this track by leveraging technology to improve access to healthcare and promote preventive wellness. The platform helps users monitor symptoms, discover nearby clinics, and take early action for health issues. By combining health tracking, location-based clinic discovery, and digital communication tools, the project demonstrates how technology can simplify healthcare access and support healthier communities.

Team **Quantum Override** -- [Priyanshu Chatterjee](https://github.com/priyanshu24-creation), [Sushobhan Sarkar](https://github.com/SushobhanDrunkCoder), [Sujauddin Mallick](https://github.com/Prem-09-bot), [Rohit Sikder](https://github.com/ROHITSIKDER)

`2026-03-11`

---

### MedTrip India
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medtrip-india-f8eb) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0zGV88mGuXk?si=uZAxXPxkQfGjzXXE) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Health, Our Priority

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**1. Lack of Cost Transparency**
Patients do not know the exact cost of treatments. Hospitals usually provide vague estimates and many hidden charges appear later.


**2. Difficulty in Choosing the Right Hospital**
India has thousands of hospitals, but patients struggle to identify which hospital is best for their specific treatment.


**3. Lack of Reliable Doctor Information**
Patients cannot easily access verified information about doctors, their experience, success rate, or specialization.


**4. Fragmented Healthcare Information**
Information about hospitals, doctors, and treatments is scattered across many websites, making it difficult to compare options.


**5. Medical Tourism Planning is Complicated**
Patients traveling to another city or country for treatment struggle with planning their medical journey, including consultations, surgery timelines, and recovery periods.


**6. Limited Access to Quality Healthcare Information for Smaller Cities**
Patients from smaller towns or rural areas often lack knowledge about top hospitals and specialists available in major cities.


**7. High Stress During Medical Decision-Making**
Patients and families must make important healthcare decisions quickly without clear and reliable information.


**8. No Centralized Platform for Comparison**
There is no simple platform where patients can easily compare hospitals, doctors, treatment costs, and services in one place.

**Challenges we ran into**

**1. Designing a Trustworthy Healthcare UI**
Creating a clean, simple, and medical-oriented interface that patients can easily trust and navigate.


**2. Making the Platform Dynamic**
Implementing real-time filtering so hospital and doctor recommendations change based on the user’s selected treatment and city.


**3. Structuring Healthcare Data**
Organizing hospital, doctor, and treatment information in a way that the platform can display relevant results efficiently.


**4. Building Transparent Cost Estimation**
Designing a system to show detailed treatment cost breakdowns rather than vague estimates.


**5. Keeping the Platform Simple for Users**
Balancing multiple features like hospital comparison, doctor discovery, and journey planning while keeping the interface easy to use.

Team **LogiQ** -- [Aaditi Jaiswal](https://github.com/aaditijaiswalaj-coder), [Jayesh Singh](https://github.com/Jayesh2007-JS), [Eshika Jasti](https://github.com/eshikajasti), [Aryan Phadke](https://github.com/Rudra-cmd-dev)

`2026-03-08`

---

### nabha healthcare
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nabha-healthcare-1ad0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/manishjonwal-12/nabha-healthcare) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://9000-firebase-studio-1772522162686.cluster-aic6jbiihrhmyrqafasatvzbwe.cloudworkstations.dev) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> healthcare at your doorstep

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Our project proposes a rural telemedicine platform that connects patients, doctors, pharmacies, and village health workers on a single digital system. The platform allows patients in rural areas to register using their mobile number and describe their symptoms. An AI-based symptom checker provides initial guidance and connects the patient to a verified doctor for online consultation through voice, video, or chat. After diagnosis, the doctor generates a digital prescription that is automatically shared with nearby pharmacies for medicine availability or delivery. The platform also maintains digital health records and supports basic health monitoring such as blood pressure, sugar, and temperature tracking. In addition, ASHA or village health workers can assist patients who have limited digital knowledge. By providing low-internet support, multilingual access, and integrated healthcare services, the system helps reduce travel time, lowers treatment costs, and improves access to quality healthcare in rural communities.

**Challenges we ran into**

🔹 Challenges
Shortage of doctors in rural areas
Long travel distance to hospitals
Poor internet connectivity
Limited access to medicines
Delay in emergency medical care
Language and literacy barriers

Team **CareCoders** -- [Sarika Yadav](https://github.com/yadavsarika071), [Manish Jonwal](https://github.com/manishjonwal-12), [Khushi Khinchi](https://github.com/khinchi0144)

`2026-03-08`

---

### pharmaguard
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wattwatch-01d6) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> tag line will be comming

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

Team **Include<Hackers>** -- [Anay Mishra](https://github.com/AnayMishra2006), [Abhijit Mondal](https://github.com/abhi5404), [Niloy Mallik](https://github.com/nilo-yinc), [DEV KUMAR SINGH](https://github.com/2232def)

`2026-02-28`

---

### Hind Svaasth Seva
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hind-svaasth-seva-c716) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Aranya01238/Hind_Svaasth_Seva) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hssfinal.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Accessible Healthcare for Every Indian

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Google Sheets](https://img.shields.io/badge/Google%20Sheets-333333?style=flat-square)

**The problem it solves**

Hind Svaasth Seva is a smart, multi-hospital healthcare management platform designed to simplify patient care and hospital coordination. The system provides digital patient registration, appointment booking, token queue management, billing, and secure medical record access across connected hospitals. A 24×7 AI calling agent answers patient queries, books appointments, and automatically updates the reception portal. The platform also includes, TrackD, a real-time tracking and monitoring module for patient flow and service efficiency. Built using the Gemini API for intelligence, ElevenLabs for voice interaction, Auth0 for secure authentication, and deployed on DigitalOcean cloud, the project ensures accessible, fast, and reliable healthcare services.

**Challenges we ran into**

During the development of Hind Svaasth Seva, several technical challenges were encountered. One major issue was configuring Auth0 authentication, where redirect mismatches and consent screens initially prevented seamless login and role-based access for different hospitals. Integrating the AI calling agent was also difficult, as synchronizing live phone conversations with real-time database updates required careful API handling. Managing speech understanding and response flow between the Gemini API and ElevenLabs voice output needed multiple refinements to achieve natural conversations. Additionally, deploying on DigitalOcean required solving server configuration, environment variables, and secure database connectivity to ensure stable performance across all connected hospitals.

**Gemini API**

The **Gemini API Track** powers the intelligent features of Hind Svaasth Seva. It enables the AI calling agent to understand patient speech, answer healthcare queries, and guide callers to the correct department. Using natural language understanding, the system can identify symptoms, suggest available doctors, and automatically create or update appointments in the database. Gemini also assists the reception portal by summarizing patient requests, generating quick notes, and supporting multilingual interaction, allowing even non-technical users to interact naturally. This track makes the platform responsive, conversational, and capable of providing instant assistance without requiring human intervention.

**ElevenLabs**

**ElevenLabs** powers the voice interaction layer of Hind Svaasth Seva through realistic AI speech synthesis. It allows the AI calling agent to speak naturally with patients over phone calls, provide appointment details, give hospital guidance, and respond to common health-related queries. The system converts AI-generated responses into clear human-like voice output, making the service accessible even to users who cannot use mobile apps or websites. By enabling multilingual and conversational communication, ElevenLabs helps patients interact with the healthcare system easily, while automatically updating the reception portal with call outcomes and booked appointments.

**DigitalOcean**

**DigitalOcean** provides the cloud infrastructure that hosts the Hind Svaasth Seva platform. The backend server, database, and APIs are deployed on secure virtual machines, ensuring the system is accessible from all connected hospitals in real time. It allows centralized storage of patient records, appointment data, and token queues while maintaining reliability and uptime. DigitalOcean also enables scalability, so additional hospitals and users can be added without changing the system architecture. By running the platform on the cloud, reception desks, doctors, and the AI calling agent can all access synchronized data from anywhere securely.

**Auth0**

**Auth0** serves as the secure authentication and identity management system for Hind Svaasth Seva. Every receptionist, doctor, and administrator logs in through Auth0, which verifies credentials and issues encrypted tokens before allowing access to the platform. It implements role-based access control, ensuring each hospital staff member can only view and manage data related to their assigned hospital and responsibilities. Auth0 protects sensitive patient information by preventing unauthorized entry, handling password security, and managing session control without storing passwords on our own server. The system also supports single sign-on and audit tracking, allowing administrators to monitor user activity and maintain healthcare data privacy standards across all connected hospitals.

Team **Dragon Blaze** -- [Aranya Rath](https://github.com/Aranya01238), [Amullyajit Nandi](https://github.com/amullyajit), [SAYAK PAL](https://github.com/Sayak-Pal)

`2026-02-28`

---

### Hospital Management System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-health-risk-prediction-and-recovery-system-4d9d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dasanirban2025/Diversion-repo.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/RMY_s2zE7ls?si=rMGczeBdZ3QnrSJS) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Efficient Healthcare System

![PHP](https://img.shields.io/badge/PHP-333333?style=flat-square) ![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Bootstrap​](https://img.shields.io/badge/Bootstrap​-333333?style=flat-square)

**The problem it solves**

1. Manual Paper-Based Record Keeping
Digital storage of all patient data
Instant search functionality
Easy backup capability
2. Inefficient Appointment Scheduling
Online appointment booking from anywhere
Real-time doctor availability tracking
Automatic fee calculation
3. Poor Communication Between Departments
Centralized database accessible by all roles
Doctor dashboard to view assigned patients
Admin panel to manage entire hospital
4. Disorganized Prescription Management
Digital prescriptions with complete medical details
Patient prescription history stored in database
Allergy tracking for better medical care
5. Payment Tracking Issues
Automated payment status tracking
Clear fee display at booking time
Payment history for all appointments
6. Limited Access Control & Security
Three-tier authentication system
Session-based security
Role-specific dashboards
Key Benefits:
Time-Saving (reduces administrative work by 70%)
Paperless digital transformation
Accessible from anywhere with internet
Secure role-based access control
Efficient instant data retrieval
Scalable for growing patient base
How It Makes Tasks Easier:
Registration: Patients register once, no repeated paperwork
Booking: 24/7 online appointment availability
Prescriptions: Digital prescriptions that never get lost
Search: Find any patient record in seconds
Payment: Clear payment tracking

**Challenges we ran into**

Database Connection Issues - Used os.path.join() and created init_db() for automatic table creation

Session Management & Authentication - Set secret_key and proper session handling for different user roles

Form Validation - Added HTML5 required attributes and JavaScript password matching validation

Appointment Date/Time Handling - Used SQLite DATE/TIME types with proper formatting

Bootstrap Tabs Not Switching - Fixed with proper ID references and Bootstrap 4 attributes

Responsive Design Issues - Added media queries for mobile devices

Flash Messages Not Displaying - Used Flask's flash() with proper template rendering

Password Security - Added confirmation field and minimum length validation

Multi-User Role Handling - Created separate routes with session checks for each role

Debug Mode Issues - Proper database connection closing and error handling

**Best Beginners' Team**

1. Healthcare & Medical Technology (HIGH)
Patient management system
Digital prescription management
Appointment scheduling for doctors
Medical record keeping
2. Web Development (HIGH)
Full-stack web application
Python Flask backend
HTML/CSS/Bootstrap frontend
SQLite database
Authentication system
Responsive design
3. Product Management (MEDIUM)
User experience design
Role-based features
Multiple user personas
4. Open Innovation (MEDIUM)
Solving real-world problems
Digital transformation of manual processes

Team **CodeX2.0** -- [Anirban Das](https://github.com/dasanirban2025), [GOURAB KARMAKAR](https://github.com/GourabKarmakar45), [Shrabanti Saha](https://github.com/SHRABANTI044)

`2026-03-01`

---

### Shudh : Ingredient Checker
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shudh-ingredient-checker-88e3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sai-emani25.github.io/Shudh/) [![Built at](https://img.shields.io/badge/Built%20at-Kaggle%20Royale-0052CC?style=flat-square)](https://kaggle-royale.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Buy healthy, Eat Healthy

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

We in India process around 270 millions orders where most of it is packaged food. Although some chemicals are banned in major contries, in India it is rampantly sold with false advertisement to the consumers without any repercussions, this tool initially built to explain the ingredients and risks of it in the long term, we set out to tackle a foundational issue in India regarding food, So we built shudh (Meaning in sanskrit is purity) where any and all products like food, body care products and medicine should properly tell the consumer of it's health hazards and side effects caused by over-consumption or even consuming a few times can cause.

**Challenges we ran into**

Quality of camera not matching the requirement needed to correctly scan the ingredient, Had trouble having all the ingredients properly show up to have a accurate score of the product.
Connecting the public Database to MongoDB to use locally for testing of the result was quite challenging

[Sai Emani](https://github.com/Sai-Emani25)

`2026-02-21`

---

### MedVault
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medvault-36f4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/btree-dev/MedVault) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1gAx1oYgbF46sCkZnIlZddq364rGG-htZP1bKm2gYATw/edit?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=6U9264z_zmg) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Own your medical records.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![DAML](https://img.shields.io/badge/DAML-333333?style=flat-square)

**The problem it solves**

I grew up in India, where going to the doctor often means walking into a small clinic inside someone’s home. There’s one room. A doctor at a desk. Chairs outside filled with patients waiting their turn.

There is usually no digital record waiting for you.

If you have a serious condition, your “medical history” is a paper folder you carry yourself — prescriptions, lab reports, scan results. If you forget it, the doctor has nothing. If you lose it, your history is gone.

If the doctor asks what medication you’re taking, you might not know the name. Sometimes people bring the empty blister foil of old medicines as proof of what they were prescribed. That foil becomes the record.

When you get blood work done, you carry the paper results back by hand. If you want a second opinion, you walk to another clinic and show them the same papers. Nothing is shared digitally. Nothing is structured. Everything depends on what the patient remembers or physically carries.

This is not just an India problem. Around the world, especially in decentralized and private healthcare systems, patients are the couriers of their own history.

MedVault solves this.

---

### What MedVault Does

MedVault gives every patient a secure, structured medical vault that they control.

Patients can:
- Store their medical history digitally
- Share specific documents with a doctor
- Share records by time range (e.g., last 3 years)
- Revoke access at any time
- Maintain a clearly marked emergency summary
- See a full audit log of who accessed their records

Doctors can:
- Upload visit notes and test results
- Add follow-up notes
- Access only what the patient explicitly shares
- Contribute to a patient’s history without owning it

---

### Why This Matters

MedVault makes healthcare:

- **Safer** — doctors see structured history instead of guessing from memory or packaging  
- **More flexible** — patients can get second opinions without carrying folders  
- **More accountable** — emergency access is immediate but logged  
- **More private** — consent is explicit and revocable  
- **More interoperable** — structured records align with global standards without centralizing ownership  

MedVault is not another hospital system.

It is a **patient-sovereign continuity layer** — built for real-world healthcare where records are fragmented, mobile, and human.

**Challenges we ran into**

A key challenge we faced was handling updates to patient-owned health records in Daml.

When a contract is updated, the original contract is archived and a new contract is created with a new contract ID.

When a doctor added a prescription to a patient's health record, the original record contract was archived. The newly created contract had a different contract ID, which the doctor did not have. Storing the contract ID on access templates did not work either — by the time a pharmacy attempted to dispense medication, the stored ID was already stale due to earlier operations.

To solve this, we redesigned the model so that the "healthRecordCid" is passed as a choice parameter at exercise time rather than stored on templates. Each dashboard queries the ledger for the patient's current HealthRecord contract ID immediately before exercising a choice, ensuring it always has the latest reference.

This preserves the HealthRecord as the single source of truth while working within Daml’s archive-and-create model.

**Use of AI tools and agents**

MedVault does not currently deploy autonomous AI agents inside the live system.

However, the architecture is intentionally designed to support permissioned AI assistance within the Canton/Daml privacy model.

AI is treated as a scoped service agent — not a system authority.

---

### Current State

At this stage, MedVault focuses on:

- Privacy-preserving record storage
- Explicit consent enforcement
- Structured data visibility
- Governance and auditability

No automated AI analysis is performed on patient data by default.

---

### Designed AI Integration (Planned Modules)

The system is architected to support two AI-assisted workflows in future iterations:

#### Provider Documentation Assistance

AI can assist providers by:

- Converting free-text notes into structured formats
- Providing predictive text during documentation
- Extracting structured data from uploaded handwritten notes
- Suggesting standardized terminology mappings

All outputs would require explicit provider confirmation before being finalized.

---

#### Patient-Authorized Longitudinal Review

With explicit patient consent, AI may be used to:

- Detect trends in lab results
- Flag potential medication interactions
- Highlight recurring symptoms
- Generate structured summaries for provider review

This would not be automated diagnosis, but pattern assistance.

AI access would be:

- Explicitly permissioned
- Time-scoped
- Logged
- Revocable
- Limited to the documents granted under contract visibility rules

---

### AI Within the Privacy Model

Within the Canton/Daml framework:

- AI operates as a permissioned service participant.
- It cannot independently retrieve records.
- It cannot access data outside explicitly granted scopes.
- All AI interactions are auditable through contract logs.

This ensures that AI remains assistive and bounded by patient sovereignty.

---

MedVault’s philosophy is simple:

AI may enhance clarity and safety — but it must operate within enforceable consent boundaries.

Privacy comes first.

**Prosperia**

Prosperia is about building privacy-preserving public goods that empower communities instead of extracting from them.

MedVault is a cypherpunk response to healthcare fragmentation — and it is governed as public infrastructure, not as a private platform.

In many parts of the world — including India — healthcare is decentralized and informal. Patients physically carry their own medical history. Providers operate independently. Consent is assumed rather than enforced. Emergency access is opaque.

The person whose data is most sensitive has the least structural control.

MedVault flips that model — technically and politically.

---

### Privacy Enforced by Architecture

MedVault is built on Canton using Daml contracts, which enforce data visibility and consent at the protocol layer.

- Providers can push records to a patient’s vault.
- Providers cannot pull records without explicit patient permission.
- Access is granular, time-scoped, and revocable.
- Emergency access is certified, bounded, and auditable.

Privacy is not a policy — it is enforced by contract visibility rules.

But architecture alone is not enough.

---

### Governance as a Public Good

MedVault is governed through a domain-weighted reputation DAO:

- **Patients, providers, and contributors all participate.**
- All members can vote on all proposals.
- Voting weight shifts depending on proposal domain.
- Privacy-critical proposals require explicit patient approval.
- Emergency standards require both patient and provider thresholds.
- Technical upgrades weight contributor expertise.
- The operating foundation is fully replaceable by DAO vote.

Reputation is non-transferable, non-financial, and earned through participation.

There are no tokens to buy influence.
There is no capital-weighted governance.
There is no corporate override.

Healthcare infrastructure evolves through stakeholder consensus.

---

### Strengthening Decentralized Communities

MedVault does not centralize healthcare.

It strengthens decentralized clinics and local providers by providing structured continuity across them.

- Patients retain portable history.
- Providers contribute without owning.
- Second opinions remain easy.
- Emergency access works without surrendering sovereignty.

This is solarpunk in practice: resilient local care supported by shared infrastructure.

---

### Cypherpunk Principles Applied to Healthcare

MedVault embodies core cypherpunk values:

- Minimize trust assumptions
- Reduce data exposure
- Enforce consent through protocol
- Govern infrastructure collectively
- Protect individuals over institutions

Prosperia is about systems that serve people first.

MedVault brings privacy, governance, and public-good design to one of the most sensitive domains in society: healthcare.

**Best Privacy-Focused dApp Using Daml**

We use Canton to ensure the privacy of medical records, allowing users to allow discretionary, limited access to physicians, doctors pharmacy, and diagnostic centers.

Team **MedVault** -- [btree Orion](https://github.com/btree-dev), [Kelvin McDaniel](https://github.com/kelvinsinferno)

`2026-02-21`

---

### Polymaxx.health
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/signalsmarket-712d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ethdenver-2026/signal-market/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://polymaxx.health/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_iifW6ZJVZ0) [![Built at](https://img.shields.io/badge/Built%20at-ETHDenver%202026-0052CC?style=flat-square)](https://ethdenver2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Know before the market

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![DID](https://img.shields.io/badge/DID-333333?style=flat-square) ![Polymarket](https://img.shields.io/badge/Polymarket-333333?style=flat-square) ![x402](https://img.shields.io/badge/x402-333333?style=flat-square) ![Kite AI](https://img.shields.io/badge/Kite%20AI-333333?style=flat-square)

**The problem it solves**

Polymaxx.health is a real-time market intelligence platform that applies 0G’s GLM via a claude skill to high-frequency predictive markets such as weather forecasting and TSA passenger volume projections.

Clients, referred to as consumers on our platform, subscribe to a WebSocket feed that delivers live signals identifying potential market arbitrage opportunities. When a signal is broadcast, consumers compete in a rapid bidding process to gain access to the full trade signal. Bidding occurs within seconds, and consumers who fail to respond in time are automatically excluded from that round.

Each consumer runs a signal evaluation agent powered by 0G Compute for dynamic pricing analysis. This agent determines whether the opportunity meets predefined profitability criteria. If the signal qualifies, the agent notifies Polymaxx to execute the trade.

On the backend, we use the x402 protocol to handle payment submission for access to the full signal. By integrating Kite AI along with a reference x402 implementation, we support decentralized identities (DIDs) and on-chain reputation scoring. This ensures that consumers who place bids they cannot fulfill are penalized or removed, maintaining marketplace integrity.

**Challenges we ran into**

We were unable to obtain API keys for Kite AI during the hackathon. As a result, we implemented the integration based on the available documentation and built a reference vanilla x402 payment flow to ensure there was a working, end-to-end implementation.

Collecting high-quality market signals required significant time and effort. In addition to ingestion, we had to design reliable search and indexing pipelines so the signals could be surfaced accurately within our dashboards.

To validate the system, we executed live trades on Polymarket. Because these were real-money transactions, we had to be deliberate and selective in our testing strategy to manage risk and control costs while still validating the full execution flow.

**Use of AI tools and agents**

We used Claude Code Opus 4.6 extensively to create dashboards, do research on how to use tool kits from 0g and Kite API, as well as getting Polymarket testing going.

We also used Cursor with Context7, Tavily, and Github MCPs.

**Futurllama**

Polymaxx.health demonstrates how decentralized finance can leverage autonomous agents to conduct real-time research into market arbitrage opportunities.

The platform combines the x402 payment protocol with emerging AI tooling such as Kite AI and distributed compute infrastructure from 0G. Together, these components enable autonomous agents to evaluate signals, compete for access to high-value data, and execute trades within a decentralized, incentive-aligned marketplace.

**Best Use of AI Inference or Fine Tuning (0G Compute)**

We used a claude skill with 0g's glm to do research into markets, and to also make decisions with our consumers on if to make a trade on a hint or not.

**Agent-Native Payments & Identity on Kite AI (x402-Powered)**

We were unable to activate Kite AI’s x402 integration because we could not obtain an API key during the hackathon. To ensure progress, we implemented a parallel flow using a vanilla x402 implementation so we could model how decentralized identities (DIDs) and reputation scoring would function through Kite AI’s services.

The Kite AI integration code remains in our repository and is structured to become operational once credentials are available.

Consumers use x402 to submit payment for the signal hints they win through bidding. If a consumer places a bid but cannot complete payment when the x402 transaction is executed, they are automatically slashed, reinforcing economic discipline and protecting marketplace integrity.

Team **SigMarket** -- [Varsity Shark](https://github.com/Principursa), [a a](https://github.com/ad0ll), [Mark Ballew](https://github.com/markballew)

`2026-02-21`

---

### ArogyaVayu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/arogyavayu-a18c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vyshalins/ArogyaVayu) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Air awareness for healthier living.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Uvicorn](https://img.shields.io/badge/Uvicorn-333333?style=flat-square) ![Context API](https://img.shields.io/badge/Context%20API-333333?style=flat-square)

**The problem it solves**

**Air quality data today is generic, city-wide, and non-actionable.**
Most platforms answer:

*“How bad is the air in Delhi?”*
But real health risk depends on:
- Where you are (street vs residential zone)
- Who you are (asthma, heart conditions, age)
- When you go out (time of day, traffic peaks)
- How you’re exposed (walking, commuting, outdoor work)

**Because of this gap:**
- People underestimate real health risk
- Sensitive groups get no preventive guidance
- AQI numbers cause panic, not understanding


**What ArogyaVayu Does Differently**
ArogyaVayu converts raw environmental data into personalized, explainable health intelligence.
Instead of just showing AQI, it answers:
- “Is today riskier for me than usual?”
- “Why is this risky today?”
- “When is the safest time to step out?”
- “What should I do differently today?”

 **How It Makes Life Easier & Safer**

- **Personalized Risk Scoring**

Weighs pollution, heat, ozone against individual health conditions
Asthma ≠ Heart condition ≠ Healthy adult

- **Baseline vs You Comparison**

Shows how your risk compares to the city average
Creates immediate, intuitive awareness

- **Time-Block Risk Forecasting**

Identifies safe windows and avoid periods
Helps plan walks, workouts, commutes safely

- **Actionable Health Recommendations**

Not generic tips — context-aware daily advice
e.g., “Avoid outdoor activity between 12–4 PM”

- **Hyper-local GPS Mode**

Risk adapts when the user moves to a different area
Shows why location matters, not just city name

**Who Can Use It**
- Individuals with asthma, heart conditions, elderly
- Outdoor workers & daily commuters
- Parents planning children’s outdoor activities

**Challenges we ran into**

- **Unreliable real-time environmental data**

Air quality and weather APIs often returned missing or inconsistent values, requiring robust fallback logic and safe defaults to keep the system stable.
 
- **Making risk truly personalized, not just contextual**

Translating raw pollution data into meaningful health risk for different users (asthma, age, exposure) required careful weighting and rule-based intelligence instead of generic AQI scores.

- **Synchronizing GPS-based location with city-level systems**

Supporting both manual city selection and live GPS introduced edge cases like undefined coordinates and mismatched data sources, which needed strict validation and fallback handling.

- **Explaining complex risk in a way users trust**

Breaking down “why this is risky” without overwhelming users was challenging, solved through  clear factor attribution.

**Sustainable Development Goals**

**SDG 3 — Good Health & Well-Being**
Target: Reduce illness and mortality from hazardous environmental exposure
Problem:
AQI values are not personalized
People with asthma or heart conditions receive the same guidance as healthy adults
ArogyaVayu’s Impact:
- Computes personalized health risk scores based on:
- Medical conditions
- Exposure patterns
- Time-of-day risks
- Provides preventive, daily health recommendations
- Helps users avoid high-risk windows before symptoms worsen

**SDG 11 — Sustainable Cities & Communities**
Target: Reduce the environmental impact of cities on human health
Problem:
Pollution varies drastically within the same city
Residents are unaware of high-risk zones or times
ArogyaVayu’s Impact:
- Introduces hyper-local risk awareness using GPS
- Highlights how location + time change exposure
- Encourages safer mobility and outdoor planning

**SDG 13 — Climate Action**
Target: Strengthen resilience and adaptive capacity to climate-related hazards
Problem:
Climate stressors (heat waves, ozone spikes) are increasing
People lack tools to adapt their daily routines
ArogyaVayu’s Impact:
- Combines heat, ozone, and pollution data into one risk model
- Helps users adapt behavior daily (timing, activity, hydration)
- Acts as a micro-level climate adaptation tool

Team **Nova** -- [Vyshali N S](https://github.com/vyshalins), [CHINMAYI Bt](https://github.com/Chinmayibt)

`2026-02-07`

---

### BioPulse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/biopulse-2590) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gargisharma03/health-buddy) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHAj8s9XQ8/RDFi9hu6N1zTjHz5ePn9HA/edit?utm_content=DAHAj8s9XQ8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Good health isn’t just physical — it’s personal.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

People can use BioPulse to track their daily health , find people with similar conditions, talk to our AI chatbot regarding healthy advices and recieve their health report.
Moreover our gamified interface provides daily motivation using streaks.
Our app supports not only physical bul mental well being of user as well.

**Beginner's track - Your first hack starts here!**

The Problem Statement we choose was Patient Centric Health Management.
Our app not only cares for physical well being of user but also their mental well-being.
It provides daily motivation using streaks.

Team **Cogniva** -- [Shreya Kumari](https://github.com/Meerseya), [Anushka Biswal](https://github.com/Anne2007-codes), [Shanvi Jha](https://github.com/ShanviJha21)

`2026-02-07`

---

### PRANSAKHI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pransakhi-4b8b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vaishnavijawalkar471-droid/pransakhi.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vaishnavijawalkar471-droid.github.io/pransakhi/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1162972618?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Healthcare that listens.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

### The Problem It Solves:
**PRANSAKHI** addresses the lack of timely primary healthcare guidance in rural and low-resource areas. Many people, especially the elderly and low-literacy users, struggle to understand symptoms, remember medicines, and decide when to seek medical help, particularly with limited internet access.

### What People Can Use It For:
- Share symptoms through voice and get basic health guidance
- Understand the seriousness of symptoms (low/medium/high risk)
- Set and receive medicine reminders
- Get audio-based advice without needing to read
- Access support even in low or no internet conditions

### How It Makes Tasks Easier & Safer:
- Helps users take early action before conditions worsen
- Reduces confusion about when to visit a doctor
- Supports medicine adherence for elderly users
- Provides simple, voice-based guidance where medical access is limited

**Challenges we ran into**

One of the main challenges was designing a solution that works well in **low-internet**  or  **offline conditions** while still using voice features. Many voice tools rely heavily on stable connectivity, which made it difficult to ensure consistent performance.

We addressed this by simplifying the logic, using lightweight components, and planning for local storage and basic rule-based processing instead of fully online AI. This made the system more **practical, faster,** and **suitable** for rural environments.

Another hurdle was keeping the **interface simple enough** for elderly and low-literacy users. We focused on large buttons, minimal text, and voice interaction to make the experience more accessible and intuitive.

**Open Innovation**

**PRANSAKHI**  proposes a *creative*, *technology-driven* approach to improve primary healthcare access using voice interaction, *offline support*, and *simple AI guidance* for rural and low-literacy communities

Team **Innovative Crew** -- [Vaishnavi Jawalkar](https://github.com/vaishnavijawalkar471-droid), [Simran Kadam](https://github.com/simrankadam278-debug), [Arpan Patekar](https://github.com/Arpan-Patekar), [Harsh Patil](https://github.com/Harshp125)

`2026-02-08`

---

### VitalFlowAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitalflowai-5560) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1SM2DlEjLD9F1By-68ABklqDSohNqaWfe) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Drops of Rain in the Medical Desert

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The "Reactive" Supply Chain Trap
Current rural healthcare supply chains are reactive. Clinics only order medicine after an outbreak begins. By the time the stock arrives (due to slow logistics), the peak of the disease has passed, or patients have already suffered.
2. The Twin Killers: Stockouts & Wastage
• Stockouts: Patients are turned away because essential drugs (like anti-malarials) are out of stock during peak seasons.  
• Wastage: To avoid running out, clinics panic-buy and overstock, leading to tons of medicine expiring on shelves.
3. The "Data Blind Spot"
Supply chain managers ignore the biggest predictor of disease: The Weather. They treat medicine ordering as a simple spreadsheet task, ignoring that Heavy Rain = Malaria or Heatwave = Cholera. VitalFlow fixes this disconnect by making the supply chain weather-aware.

**Challenges we ran into**

Challenges We Ran Into
• Data Scarcity & Privacy: Real healthcare data is strictly protected (HIPAA). To train our models without compromising privacy, we engineered a Synthetic Data Pipeline using Python to simulate realistic correlations between weather patterns and disease outbreaks.
• API Limits & Connectivity: Relying on live external APIs (Open-Meteo) caused rate-limiting issues. We built a Robust Fallback Mechanism that automatically switches to cached local data if the external service fails, ensuring the app works even in low-connectivity rural areas.
• Integrating Python AI with React: Bridging heavy data science models (Prophet/Pandas) with a lightweight frontend caused latency. We solved this by adopting an Asynchronous Batch Processing architecture, pre-calculating forecasts into JSON for instant, zero-latency dashboard performance.

**Google Gemini**

1. Synthetic Data Generation (The Foundation):
We used Gemini to generate highly realistic, HIPAA-compliant synthetic datasets for 50 rural clinics. It simulated complex correlations between weather patterns (e.g., heavy rainfall) and specific disease outbreaks (e.g., Malaria, Cholera), allowing us to train our Prophet models without compromising real patient privacy.
2. The 'Clinical Co-Pilot' (The Interface):
While Prophet calculates the numbers (e.g., 'Order 50 units'), we utilize Gemini's capabilities to explain the 'Why' to the user. The system is designed to take the statistical output and convert it into natural language alerts (e.g., "Gemini Analysis: Recommended ordering 50 units of Artemether because a 10-day rain forecast predicts a 40% spike in Malaria cases."). This bridges the gap between complex data science and rural healthcare workers.

Team **MBA** -- [Brahmbir Singh](https://github.com/HiNoOu), [Achintpreet Singh](https://github.com/achintpreetsingh23-aps), [Mankeerat Singh](https://github.com/HiNoOu)

`2026-02-08`

---

### NutriSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nutrisense-f287) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DevBolt07/label-insight-pro) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://label-insight-pro.web.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ep9D7by4MW0?si=tIRFDuc4y9d8Mve0) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI food labels, personalized for healthier choices

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🚀The problem it solves

Buying “healthy” food is harder than it should be.
At the point of purchase, most people are forced to quickly interpret dense, technical and misleading nutrition labels. Important information is hidden behind chemical names, inconsistent serving sizes and poorly structured tables.

For users with medical or dietary constraints (such as diabetes, hypertension, allergies or gluten intolerance), this is not just inconvenient — it can directly impact their health.

🧠What people can use NutriSense for

NutriSense is an AI-powered food label understanding assistant that helps users make safer and more informed food choices in real time.

Users can:

📷 Scan a barcode or capture a photo of a product label

🔍 Automatically extract ingredients and nutrition values, even when a barcode is missing

🧑‍⚕️ Personalize the analysis using their health profile (dietary restrictions, allergies, and preferences)

🚦 Receive instant alerts for potentially unsuitable ingredients

📊 View a simple health score and explanation

🔁 Discover healthier alternatives when a product is not suitable

✅ How NutriSense makes an existing task easier and safer

Instead of manually:

reading small, cluttered labels,

searching ingredient meanings online,

and guessing whether a product fits personal health needs,

NutriSense:

🧩 Structures messy label text into clear data

🧠 Interprets ingredient risks and nutrition context using AI

🧑‍🤝‍🧑 Adapts results to each user’s profile

⚠️ Highlights risks before purchase

🛒 Supports safer, faster and more confident buying decisions

🔄 Works even when barcodes fail

Many products either:

do not have a readable barcode, or

have incomplete or outdated database entries.

NutriSense intelligently falls back to image-based label analysis (OCR + AI) and, when possible, automatically enriches results using trusted public food databases.

This ensures that users still receive meaningful results even in real-world retail conditions.

🌍 Why this matters

NutriSense helps bridge the gap between:

complex nutritional science and

everyday consumer decision-making.

By delivering personalized, understandable and reliable insights at the moment of purchase, NutriSense empowers people to make healthier choices — not later, but right when it matters most. 🛍️💚

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/16de7ce1-0f62-4ceb-8cc3-e8655d0b65cd.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/e7c66bff-b4a7-41d3-8da8-67c683e1afd7.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/b2986fcc-9461-4cc6-b3c0-209b542af9ba.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/d21b3d51-80d8-490e-90a4-a5b1074d2ed6.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/1e0a32d4-c8fe-448f-8a6d-7e11b919edda.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/adbd9336-33b0-4fcb-a9a4-2bb2bb8885ab.png)

![image](https://assets.devfolio.co/content/eb8b7c63de9f44e1af2e5dd43cb50360/36c6fe43-9858-4c85-be20-5b3f63b9f9a8.png)

**Challenges we ran into**

🧩 Challenges I ran into

Building NutriSense required handling real-world data, unreliable APIs and noisy images. Below are the most impactful challenges we faced and how we solved them.

🤖 LLM responses breaking our backend (invalid JSON)

While using Gemini to generate structured nutrition and health analysis, the model occasionally returned responses mixed with explanations or formatting. This caused our backend to crash with parsing errors such as “Unterminated string in JSON”.

How we solved it
We implemented a robust JSON-extraction and validation layer inside our Edge Functions.
Instead of directly trusting JSON.parse, we isolate the JSON block from the model response and validate it before processing. If parsing still fails, the system gracefully falls back to OCR-only analysis so the user never sees a crash.

⏱️ API rate-limits during development and testing

During integration and demo testing, we frequently hit LLM rate limits (HTTP 429 / quota errors), which made the application unreliable.

How we solved it
We built a model fallback routing layer that automatically switches between compatible Gemini models when a rate-limit occurs, while keeping the same prompts and response schema.
If all models are temporarily unavailable, NutriSense switches to a lightweight rule-based fallback so that users still receive a basic and safe analysis.

📦 Multiple and incomplete product entries in public databases

When scanning barcodes, the same product often had several entries in the public food database, many of which were missing ingredients, nutrition values or images.

How we solved it
We designed a candidate ranking and validation system that scores multiple product entries based on data completeness and consistency with OCR-extracted ingredients.
Only the most reliable and complete entry is selected for display.

📷 OCR accuracy on real packaging

Food packaging images often contain curved surfaces, branding text and complex layouts, leading to noisy or incorrect OCR results.

How we solved it
We implemented a dual-engine OCR pipeline.
The system first attempts PaddleOCR and automatically falls back to OCR.space when confidence is low.
The extracted text is then structured so that only meaningful rows such as ingredients and nutrition values are used for analysis.

🔐 Unstable authentication due to stale sessions

During development, Supabase authentication occasionally failed due to invalid or expired refresh tokens stored on the client.

How we solved it
We added explicit session validation and cleanup logic. When an invalid refresh token is detected, the app safely clears the local session and redirects the user to re-authenticate, preventing broken login flows.

🧠 Identifying products from label images when barcodes are missing

Some images clearly contained the product name and brand, while others only showed ingredients and legal text.

How we solved it
We introduced a smart product-identification step where the system first tries to infer the product name from prominent OCR text and validates it using ingredient overlap before querying public databases.
If confidence is low, NutriSense automatically falls back to OCR-based analysis instead of showing potentially incorrect product data.

These challenges helped us design NutriSense as a fault-tolerant, real-world-ready system that continues to work reliably even when data, APIs or images are imperfect.

**Open Track**

NutriSense fits the Open Track by solving a real-world consumer problem using AI and open public data.

Our project is an AI-powered food label understanding system that works with both barcodes and product images. It uses OCR, large language models and open datasets (Open Food Facts) to extract, validate and explain nutrition and ingredient information in a personalized way.

NutriSense focuses on improving everyday decision-making in health and nutrition and is not limited to any specific industry partner or sponsor challenge, making it a natural fit for the Open Track.

Team **CodeLites** -- [Ira Khandelwal](https://github.com/IraKhandelwal), [Tanmay Kumbhare](https://github.com/Tanmay-Kumbhare), [Hemantkumar Lakhane](https://github.com/DevBolt07), [Rushikesh Shinde](https://github.com/viraj-1124)

`2026-02-01`

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

### MediCare Era+
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medcare-dab1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shubhamgyl000-ai.github.io/Medicare-Era-/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Save Health Save future

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

Team **X Coders** -- Vinay Sharma, [Shubham Goyal](https://github.com/Shubhamgyl000), Manshika Choudhary, Palak Gupta

`2026-03-07`

---

### Citrus Diagnosis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/citrus-diagnosis-4f46) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BhupinderrSingh/Citrus-Diagnosis-) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a5RiaVXv7UE) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Smart crop scanning & AI treatment.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Citrus diseases like Canker, Greening, and Black Spot cause massive global agricultural and economic losses every year, primarily due to delayed detection. Farmers and field agronomists often lack immediate access to expert plant pathologists, leading to misdiagnosis, incorrect pesticide use, and severe crop damage. Citrus Diagnosis solves this by putting an expert agronomist in the farmer's pocket—combining a dual-model deep learning diagnostic engine with a conversational AI assistant to provide instant, field-ready disease identification and actionable treatment protocols from any mobile device

**Challenges we ran into**

One major challenge while building Citrus Diagnosis was integrating two CNN models (MobileNetV2 and InceptionV3) into a single Flask prediction pipeline to improve diagnostic accuracy. During testing, MobileNetV2 produced correct results, but InceptionV3 gave completely inaccurate predictions on live uploads, even though it performed well during training.

After debugging the backend, I discovered the issue was in the image preprocessing step. Different neural network architectures require different input normalization methods. MobileNetV2 expects images scaled between 0 and 1, while InceptionV3 expects values scaled between -1 and 1 using its specific preprocessing function.

Initially, I was sending the same normalized image to both models, which caused incorrect predictions from InceptionV3. I solved this by creating a separate preprocessing pipeline for each model. The system now generates two processed images—one formatted for MobileNetV2 and another using InceptionV3’s preprocess_input() function.

Team **Code Clashers** -- Arshpreet Singh, Ashmit Saini, Bhupinder Singh, Rajat Duhan

`2026-03-08`

---

### Sanjeevani
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sanjeevani-4094) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/theatu1sin9h/sanjeevani) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Unified Health Ecosystem

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🌟 
What sets Sanjeevani apart from traditional healthcare portals:

**Unified Digital Health ID: **A "one identity, complete care" approach that allows patients to carry their entire medical history securely in a single digital card.

**VaidyaBot (AI Assistant):** An integrated AI medical assistant powered by Google Gemini, capable of answering healthcare queries and guiding users through the ecosystem.

**Emergency Protocol Active:** A one-touch emergency system that transmits encrypted identity and location data to the nearest verified hospitals.

**Confidential Consultancy:** A dedicated, secure space for private medical discussions between patients and specialists.
Hybrid Ecosystem: Direct integration with verified pharmacies and a hospital locator, creating a true end-to-end health infrastructure.

Team **Code for Care** -- Aman Sharma, [Atul Singh Chandel](https://github.com/theatu1sin9h)

`2026-03-08`

---

### Medichain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medichain-0f18) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sandeep2122/Medichain.git) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> "Your Health Data, Your Control, Your Reward"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

1. True Data Ownership.
2. Secure storage
3. Controlled Sharing.
4. Financial Rewards

**Challenges we ran into**

1. Data privacy & Security.
2. Blockchain scalability.
3. User Trust & Adoption

Team **BitBuilders** -- Shareya ., [Yuvraj .](https://github.com/Shoyo29/), Sandeep Kumar, Parkeerat Singh

`2026-03-07`

---

### Swastya Setu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/swastya-setu-0909) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryanbhatt7793/Swastya-Setu) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> AI Powered Disease Prediction and Hospital Finder

![PHP](https://img.shields.io/badge/PHP-333333?style=flat-square) ![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![phpMyAdmin](https://img.shields.io/badge/phpMyAdmin-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square)

**The problem it solves**

Many people experience symptoms such as fever, headache, cough, or fatigue but are often unsure about what illness they might have. In many cases, people ignore early symptoms due to lack of awareness, which can lead to serious health complications later. Another major challenge is that during emergencies or sudden health issues, people spend valuable time searching for nearby hospitals or medical facilities.

Our project addresses these problems by providing an AI-powered health assistance system that helps users quickly understand their possible health condition and find medical help nearby.

The system allows users to enter their symptoms, and an Artificial Intelligence model analyzes these symptoms to predict possible diseases. This helps users gain early insight into their health condition and encourages them to seek medical attention when necessary.

In addition to disease prediction, the system also provides location-based hospital recommendations. Using an interactive map, the platform displays nearby hospitals so that users can easily locate and navigate to the nearest medical facility without wasting time searching online.

To further improve emergency response, the system includes an SOS feature that allows users to quickly signal for help during urgent situations.

Overall, this project makes healthcare guidance faster, more accessible, and more efficient by combining machine learning, location services, and web technology into a single intelligent platform. It helps users make informed decisions about their health and ensures that medical assistance can be reached quickly when needed.

**Challenges we ran into**

While developing this project, we encountered several technical challenges related to integrating different technologies such as machine learning, backend services, databases, and map-based visualization.

One of the major challenges was integrating the AI model with the web application. The machine learning model was developed in Python using Scikit-learn, while the web backend was built using PHP. Since these technologies run in different environments, we needed to create a communication bridge between them. We solved this by setting up a Python prediction API running on a local server, and the PHP backend sends symptom data to this API using HTTP requests. The API then returns the predicted disease in JSON format.

Another challenge was preparing the symptom data in the correct format for the AI model. The dataset contains 132 symptoms, and the model expects the input in a specific binary format. We implemented a conversion system that transforms user-entered symptoms into the required format before sending them to the prediction model.

We also faced difficulties while implementing the hospital location mapping system. Initially, displaying hospitals dynamically on the map was challenging. To solve this, we stored hospital details including latitude and longitude in a MySQL database, and used Leaflet.js with OpenStreetMap to render the hospital locations as markers on the map.

Additionally, we had to ensure that the system responds quickly and provides accurate predictions. This required testing the machine learning model, validating the dataset, and optimizing the communication between the frontend, backend, and AI service.

Overcoming these challenges helped us successfully integrate AI prediction, database management, and geolocation services into one complete healthcare assistance system.

Team **n log n** -- Archna Behera, [KARTIK SHARMA](https://github.com/kartikstudies008), Aryan Bhatt, Kashish Mehra

`2026-03-07`

---

### AAROGYA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aarogya-46ac) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/krishanumishra21/aarogya-ai-health-platform) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Aarogya – Smarter Healthcare, Faster Care.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Currently, the healthcare system faces several major challenges.

First, patients often don’t know which doctor or specialist to consult based on their symptoms. This leads to confusion and delayed treatment.

Second, medical records are fragmented across different hospitals. When a patient visits a new hospital, doctors usually cannot access previous prescriptions or treatment history.

Third, during medical emergencies, doctors need instant access to critical information like blood group, allergies, or previous conditions, but this data is rarely available quickly.

Because of these issues, hospitals experience delayed diagnosis, repeated medical tests, and inefficient patient management.

Team **ALPHA QUID** -- Devansh Gautam, Gurpreet Singh, Amit Kumar, [Krishanu Mishra](https://github.com/krishanumishra21)

`2026-03-08`

---

### MediTatva
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/meditatva-5e40) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/satyamraj2990/MEDI-TATVA) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://meditatva.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> AI Healthcare Intelligence for Smarter Care

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Mongo](https://img.shields.io/badge/Mongo-333333?style=flat-square)

**The problem it solves**

Accessing reliable healthcare information quickly is still a major challenge. Patients often struggle to understand medical reports, compare medicines, find nearby pharmacies, or get quick guidance for common health concerns. Many people rely on scattered internet searches or delayed consultations, which can lead to confusion, misinformation, and poor health decisions.

Meditatva solves this by creating a unified AI-powered healthcare assistant. It helps users analyze medical reports, compare medicines and find suitable substitutes, receive instant health guidance through an AI voice assistant, and locate nearby medical stores or doctors. By simplifying complex medical information and bringing multiple healthcare tools into one platform, Meditatva enables users to make faster, safer, and more informed health decisions.

**Challenges we ran into**

While building Meditatva, one of the biggest challenges was stabilizing the AI voice assistant (MediSaarthi) during real-time phone calls. Since the system integrates Twilio voice calls, speech-to-text, AI processing, and text-to-speech responses, even a small failure in the pipeline could break the entire conversation flow. We frequently faced issues such as webhook errors, temporary API failures, and cases where the assistant returned fallback responses instead of answering the user's query.

Another challenge was implementing the medicine comparison and substitute finder without training a custom model due to limited time. Instead, we designed an AI-driven reasoning approach that analyzes medicine names and medical context to generate meaningful comparisons and alternatives.
We overcame these challenges by restructuring the backend flow, adding robust error handling, and carefully validating each stage of the pipeline—from call reception to AI response generation. By debugging logs and simplifying the architecture, we ensured the system could reliably process user queries and deliver real-time health insights.

Team **AURA PHARM** -- [Satyam Raj](https://github.com/2990), [Akshat Dwivedi](https://github.com/akshatdwiveditemp4y-ux), Shashi BhushanThakur, Ikshita .

`2026-03-08`

---

### Baymax AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/baymax-ai-38a4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mannubaveja007/baymax-voice-agent) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://baymax-voice-agent.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vcmHYQCaQbc) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Health Tech Innovation

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square) ![Backend](https://img.shields.io/badge/Backend-333333?style=flat-square) ![API3](https://img.shields.io/badge/API3-333333?style=flat-square)

**The problem it solves**

### Problem Statement

Navigating personal health concerns is often a stressful, confusing, and anxious experience. When individuals experience symptoms such as a sudden headache or chest pain, they immediately face a critical lack of immediate, understandable medical guidance. 

This leads to three primary issues:

1. **Unnecessary Panic and Overburdened Medical Systems:** Without immediate triage or calming guidance, patients frequently experience heightened anxiety. This leads to unnecessary emergency room visits, wasted time, and increased strain on healthcare infrastructure for non-critical issues.
2. **Lack of Visual and Multilingual Context:** Traditional medical search results provide dense, text-heavy reading that is difficult for a layperson to map to their own body. Furthermore, many existing health bots are rigidly confined to english text input, failing to support spoken local dialects and bilingual terminology (e.g., mixing "headache" with "sir dard").
3. **Inaccessible Triage:** Access to a calm, knowledgeable entity that can listen, understand, and provide immediate contextual feedback is rarely available 24/7.

Patients need a calming, highly accessible interface that bridges the gap between searching symptoms online and scheduling a doctor's appointment. They require a system that not only listens to their spoken symptoms in their native dialect but also visually demonstrates an understanding of the issue, providing immediate clarity and actionable next steps.

**Challenges we ran into**

### Challenges We Ran Into

Baymax had some real-life challenges during its construction, but we didn't just bug-fix—we went ahead and made Baymax smarter, faster, and more inclusive for all.

* **Slow 3D Model Performance** 
The initial 3D anatomical body model was bulky and performed poorly on older devices. We worked around this by heavily optimizing the model, including performance settings, and ensuring that the WebGL canvas renders smoothly even on mobile phones.

* **High API Credit Consumption** 
Our ElevenLabs API credits were depleting too fast due to inefficient, continuous calls. We solved this by batching requests, caching typical conversational responses, and only triggering the generation of what we strictly needed. This architectural change saved 60% of our API credits.

* **Jittery Camera Movements** 
Initially, the camera would awkwardly jump between body parts, which destroyed the immersive holographic feel. We fixed this by rewriting the camera logic with native Three.js `lerp` functions. The camera now glides seamlessly and smoothly frames exactly what needs to be seen like a real 3D assistant.

* **Bilingual Voice Recognition Issues** 
Standard voice recognition was failing when users spoke conversational Hindi, completely missing key phrases like "sir dard" or "migraine". We remedied this by creating a custom bilingual keyword map (English + Hindi / Hinglish) and wrapping it in fuzzy matching logic. Now, even if there is a typo, slang, or mixed dialects, the app detects the intent flawlessly.

Team **Team Syndicate** -- [Mannu Baveja](https://github.com/mannubaveja007/), [Suhaj Kanikicherla](https://github.com/SuhajKanikicherla), [Pusarla Vinay](https://github.com/pusarlavinay), [Bhavya Gupta](https://github.com/chezyburgy)

`2026-03-08`

---

### LifeGuard Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifeguard-ai-c18d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Madhav-Garg/LifeGuard-ai) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Quick, clear health answers from LifeGuard AI now!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square)

**The problem it solves**

LifeGuard AI gives you fast, plain-language health guidance before you decide on a clinic visit. In one place you can describe symptoms for AI triage, upload photos for a quick review, ask health questions, see when to seek urgent care vs. rest at home, find nearby hospitals, get diet and wellness tips tailored to your inputs, and export a simple report to share with a doctor—reducing uncertainty, saving time, and helping you act sooner.

**Challenges we ran into**

One hurdle was deployment: Vercel kept returning 404 because the app lives in a web subfolder and the production deployment was still using the repo root with the wrong Node version. I fixed it by setting Root Directory to web, switching Node to 20.x, and redeploying so the production domain pointed to the new build. Another challenge was aligning environment variables for the API routes; adding them in Vercel’s env settings (per .env.local.example) resolved missing-config errors.

Team **Code Revenge** -- [Jatin Kumar](https://github.com/JatinxKumar), [Madhav Garg](https://github.com/Madhav-Garg)

`2026-03-08`

---

### Heart health
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/heart-health-0c40) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anandroy196/heart-health) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> https://github.com/anandroy196/heart-health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Early prediction of heart risks 
Life style management 
Education and awarness

**Challenges we ran into**

Solve health diseases
Privacy and data security.

Team **The bug slayers** -- Anjali ., Anand Roy

`2026-03-08`

---

### Anony-Talk
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anonytalk-4bee) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://anony-talk-safespace.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=_UJxIkBNu_Q) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Solving Mental Health Related Issues

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![MERN stack](https://img.shields.io/badge/MERN%20stack-333333?style=flat-square)

**The problem it solves**

We live in a world where communication is easier than ever, yet honest communication is becoming harder.

Many people have thoughts, questions, concerns, or ideas they want to share—but they stop themselves. Not because they don’t care, but because they are afraid.

Afraid of judgment.
Afraid of embarrassment.
Afraid of consequences.

A student may hesitate to ask a “basic” question in class because they fear looking foolish.
An employee might notice a serious issue at work but stay silent because speaking up could affect their career.
Someone struggling with stress or mental health may want to talk, but not if their identity is attached to it.

The result is a silent problem: people choose silence over honesty.

Our project addresses this gap.

We built a platform that allows people to communicate freely and safely through anonymity, while still maintaining a structured and responsible environment. By removing identity from the conversation, we remove the invisible social pressure that prevents many people from speaking up.

What People Can Use It For:

This platform opens up many meaningful possibilities:

• Students can ask questions without fear of being judged.
• Teams and organizations can receive honest feedback from employees.
• Communities can discuss sensitive topics openly.
• Individuals can seek advice or share thoughts without exposing their identity.
• Researchers and developers can study anonymous interaction patterns to design healthier online platforms.

In short, it creates a space where people can focus on ideas instead of identities.

How It Improves Existing Solutions

Most social platforms today are built around identity—profiles, followers, reputation systems. While these features encourage connection, they also introduce bias, social pressure, and fear of judgment.

Our solution flips that model.

Instead of asking “Who said this?”, the platform prioritizes “What is being said?”.

By reducing identity pressure, communication becomes more honest, more open, and often more meaningful.

At the same time, the system is designed with modern technologies and moderation mechanisms to ensure the space remains safe and constructive.

The Human Impact

At its core, this project is about something simple but powerful: giving people the courage to speak.

It is for the student who has a question but is too shy to ask.
For the employee who wants to improve their workplace.
For the person who just needs a place to express what they feel.

Technology should not only connect people—it should create spaces where people feel safe to be honest.

This platform aims to do exactly that:
to transform silence into conversation, hesitation into confidence, and isolation into connection.

Because sometimes the most powerful voice someone has…
is the one they can finally use without fear.

**Challenges we ran into**

Building this project was exciting, but it definitely came with its share of challenges. Like most real-world software projects, many of the hurdles appeared only after things started coming together.

Anonymous Authentication

One of the biggest challenges was implementing anonymous authentication.
Since the goal of the platform is to allow users to communicate without revealing their identity, I needed a way to let users interact with the system without traditional accounts.

At first, this caused several issues.

Sometimes the system failed to create a session properly, and users would see errors when trying to post or fetch content. In some cases, the frontend attempted to interact with the backend before the anonymous session was fully established, which resulted in failed API calls and inconsistent behavior.

To solve this, I implemented a check that ensures an anonymous session is created before any user interaction happens. The frontend now waits for authentication to complete before loading features that depend on it.

This small change significantly improved reliability.

Frontend–Backend Communication

Another hurdle was handling API communication between the frontend and backend services. During development, I ran into a “Failed to fetch” error multiple times when the frontend attempted to call backend endpoints.

This turned out to be related to incorrect environment configuration and deployment differences between the local environment and the production environment.

To fix this, I carefully reviewed the environment variables and API base URLs, ensuring that the frontend dynamically loads the correct backend endpoint depending on the environment.

Once this was corrected, the communication between services became stable.

Deployment and Build Issues

When deploying the project, I also encountered build problems during the deployment process. The application worked locally but failed during the automated build.

This forced me to inspect the build logs carefully. The issue was caused by missing dependencies and incorrect project structure references during the build step.

After adjusting the build configuration and ensuring all dependencies were correctly installed during deployment, the build process finally completed successfully.

What I Learned

These challenges reminded me that building software is not just about writing code — it is about debugging, testing assumptions, and gradually improving the system.

Each bug forced me to understand the architecture more deeply, and solving them made the final project far more stable and reliable.

In the end, those obstacles were not setbacks — they were part of the process that made the project stronger.

Team **DHURANDHAR** -- Sejal Sabreen, Kumar Saurav, [Ishitha V](https://github.com/Ishita215), Sneh Raunak

`2026-03-08`

---

### AI Health Guard Smart Disease Detection
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-health-guard-smart-disease-detection-778b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harmanjot2211/AI-Health-Guard) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/8SE7Iuf0EHA) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Analyze actionable and recommend

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Millions of people around the world struggle to access timely and reliable healthcare guidance. Long wait times for doctor appointments often lead to delayed diagnoses, causing treatable conditions to worsen before medical intervention occurs. At the same time, over half of the global population lacks adequate access to qualified healthcare professionals and medical facilities, especially in underserved and remote areas.

Additionally, individuals frequently face uncertainty about their symptoms, making it difficult to determine whether a condition is minor or requires urgent medical attention. This uncertainty can lead either to unnecessary panic and emergency visits or dangerous delays in seeking care.

Compounding these issues are rising healthcare costs, where avoidable emergency room visits and consultations contribute billions of dollars in unnecessary healthcare spending every year.

As a result, there is a critical need for accessible, affordable, and intelligent health guidance that helps individuals understand symptoms early, make informed decisions, and access the right level of care at the right time.

**Challenges we ran into**

Developing an AI health assistant involved challenges such as ensuring accurate symptom analysis, handling diverse medical data, and reducing false recommendations. Designing a user-friendly interface while maintaining medical reliability was critical. Additionally, addressing privacy concerns, integrating trusted medical knowledge, and building user trust were key obstacles throughout the development process.

Team **Team tetra** -- Tanvi Batra, Harmanjot Singh, Amrit Kumar

`2026-03-08`

---

### Sanjeevani
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sanjeevani-6e14) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/raghvandrasingh111-sys/sanjeevani) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Sanjeevani – Your Path to Better Health

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Sanjeevani – Unified Digital Health Records Platform
What People Can Use It For

Sanjeevani is a digital health platform designed to store and manage a patient’s complete medical history in one secure place. Instead of carrying physical reports or searching through multiple hospital systems, users can access all their health records instantly through a single mobile application.

Patients can upload and store prescriptions, lab reports, diagnoses, and medical history securely. Doctors and hospitals can access these records instantly with patient permission, helping them understand the patient's medical background and provide faster and more accurate treatment.

The platform also allows patients to share their medical records using a QR code or secure link, making hospital visits smoother and eliminating paperwork.

How It Makes Existing Healthcare Tasks Easier
1. No More Lost Medical Reports

Patients often lose or forget medical files. Sanjeevani stores everything digitally, ensuring that records are always available when needed.

2. Faster Doctor Consultations

Doctors can instantly see a patient's full medical history instead of asking repetitive questions or waiting for past reports.

3. Reduced Repeated Medical Tests

When hospitals cannot access previous reports, they often repeat tests. Sanjeevani helps doctors view past results and avoid unnecessary testing.

4. Easy Record Sharing

Patients can securely share their health records with doctors, hospitals, labs, or specialists through a QR code or secure digital access.

How It Makes Healthcare Safer
Better Medical Decisions

Doctors get a complete view of patient history, which reduces the risk of incorrect prescriptions or treatments.

Reduced Medical Errors

Access to allergies, past illnesses, and medications helps doctors avoid dangerous drug interactions or incorrect diagnoses.

Secure Data Protection

All medical data is protected with end-to-end encryption and secure cloud storage, ensuring patient privacy and compliance with digital health standards.

Who Benefits from Sanjeevani
Patients

Easy access to all medical records

No need to carry physical documents

Better control over personal health data

Doctors

Faster diagnosis with complete patient history

Less time spent on paperwork

Better collaboration with specialists

Hospitals

Faster patient onboarding

Improved record management

Reduced administrative workload

Government & Healthcare Systems

Better disease tracking and healthcare planning

Reliable national health data

Improved public healthcare services

The Bigger Impact

Sanjeevani helps build a connected digital healthcare ecosystem where patients, doctors, hospitals, and laboratories can securely share health information.

By reducing paperwork, improving diagnosis accuracy, and enabling smarter healthcare decisions, Sanjeevani contributes to a more efficient, accessible, and safer healthcare system

**Challenges we ran into**

Challenges We Ran Into

While building Sanjeevani – Unified Digital Health Records Platform, our team faced several technical and practical challenges during development. These hurdles helped us improve the system's design and reliability.

1. Secure Medical Data Storage

One of the biggest challenges was ensuring that sensitive patient health records remain secure and private. Medical data must be protected from unauthorized access while still allowing doctors to retrieve it quickly.

How we solved it:
We implemented secure authentication and encrypted database storage using Supabase and PostgreSQL. Role-based access control ensures that only authorized users (patients or doctors with permission) can view or upload records.

2. Extracting Data from Medical Reports

Medical reports often come in different formats such as PDFs, images, or scanned documents, which makes it difficult to automatically organize them into structured data.

How we solved it:
We integrated OCR technologies like Tesseract and Google Vision API to extract text from uploaded reports. Then we used NLP tools such as spaCy and Hugging Face models to identify important medical information like test names, prescriptions, and diagnoses.

3. Interoperability Between Different Hospital Systems

Hospitals and clinics use different software systems, which makes it difficult to create a unified health record platform that works everywhere.

How we solved it:
We designed our platform to follow standard healthcare data formats such as HL7 and FHIR, which makes it easier to integrate with existing hospital management systems.

4. Building a Scalable and Fast System

Handling large volumes of patient records and real-time access from doctors required a system that could scale efficiently without performance issues.

How we solved it:
We adopted a cloud-based architecture with Supabase backend services, allowing real-time database updates and scalable infrastructure that can support many users simultaneously.

5. User Experience for Non-Technical Users

Healthcare apps are used by people of all age groups, including patients who may not be very comfortable with technology.

How we solved it:
We focused on a simple Flutter-based mobile interface with clear navigation and minimal steps to upload, view, or share medical records.

Team **Techno Creates** -- [Ayush Bhardwaj](https://github.com/Ayush-090)

`2026-03-08`

---

### LifeAfterDiagnosis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifeafterdiagnosis-4de9) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lifeafterdiagnosis.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> One Match Can Save A Life.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Fatal Delays in Matchmaking: Manually searching fragmented global donor registries for complex genetic and blood-type matches takes hospitals weeks, costing critical cancer patients their lives.

The "Needle in a Haystack" Crisis: Patients have incredibly low chances of finding perfect HLA stem cell matches, especially across diverse ethnic backgrounds globally.

Medical Fraud & Data Risks: Unverified, isolated donor platforms lack HIPAA-compliant cryptographic security to ensure patient data privacy and request authenticity.

Lack of Guidance: Potential donors and terrified patients are overwhelmed by complex medical terminology without 24/7 accessible support to guide them.

 Our Solution: "Life After Diagnosis"
Life After Diagnosis is an intelligent, centralized network that makes finding a stem cell match faster, safer, and entirely automated.

AI-Powered, Instant Matchmaking: A high-speed Machine Learning algorithm (K-Nearest Neighbours) replaces manual searches, analyzing millions of global data points instantly to rank the highest-percentage genetic donor matches for patients.

Cryptographically Verified Hospitals: A secured Hospital Portal ensures that only medically-verified, registered institutions can upload requests or view data, guaranteeing a 100% authentic and HIPAA-compliant donor pool.

 Automated Lifesaving Alerts: An event-driven Node.js pipeline triggers instant email notifications to donors the exact millisecond the AI algorithm discovers they are a perfect match, mobilizing them to save a life immediately.

 24/7 Gemini Medical Assistant: A real-time Google Gemini 2.5 AI Chatbot is integrated directly into the platform to provide compassionate, medically-accurate guidance and answer questions for both donors and patients instantly.

**Challenges we ran into**

Building a three-part medical platform from scratch was tough! Here were our biggest hurdles:

Hosting a Complex AI Model:
The hurdle: We built our custom donor-matching AI using heavy Python libraries (like scikit-learn). When we tried to deploy the whole project to Vercel, it immediately crashed because Vercel has tiny 50MB limits for serverless functions!
The fix: We split the platform into microservices! We hosted the beautiful Next.js frontend on Vercel, but moved the heavy Python logic and our Node.js database server over to Render. It worked perfectly.

Mobile Responsiveness on Complex SVGs:
The hurdle: Our "AI Matching" visualization looked gorgeous on Desktop, but the complex 600px SVG neural network lines were horizontally stretching the screen on mobile phones, breaking the UI.

The fix: We completely refactored the Tailwind classes. We replaced hard pixel heights with fluid 100dvh boundaries, wrapped the app in overflow-x-hidden, and built a dedicated, optimized vertical layout just for mobile users.

Team **Innovatrix** -- [Aman Keshari](https://github.com/amanRajKeshari), [Md.khushtar Ali](https://github.com/Kaif2684)

`2026-03-08`

---

### Medicore
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medicore-a95b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryan0416/medicore) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Full-Stack hospital management platform with AI-po

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Antigravity](https://img.shields.io/badge/Antigravity-333333?style=flat-square)

**The problem it solves**

Modern hospitals manage large volumes of patient data, clinical records, lab results, and administrative workflows, but these systems are often fragmented across multiple tools. This fragmentation makes it difficult for healthcare staff to efficiently access patient information, manage hospital operations, and make timely decisions. As a result, hospitals face operational inefficiencies, increased administrative burden, and delays in clinical decision-making.

At the same time, clinicians must constantly refer to medical guidelines, research papers, and treatment protocols to make evidence-based decisions. Manually searching through these sources during busy clinical workflows is time-consuming and can lead to information overload or missed insights.

This project addresses both challenges by combining a hospital management platform with an AI-powered clinical knowledge system. The platform centralizes hospital operations such as patient management, encounters, billing, and reporting, while the AI system uses Retrieval-Augmented Generation (RAG) to retrieve relevant medical guidelines and research documents before generating responses. This enables healthcare professionals to quickly access operational data and evidence-based medical insights in one integrated system, improving efficiency and supporting better clinical decision-making.

**Challenges we ran into**

Integrating Multiple Technologies
The system combines Next.js, Express, Supabase, FastAPI, and AI components, which required careful design of APIs and communication between services. Ensuring smooth interaction between the frontend, backend, and AI service was one of the main architectural challenges.

Designing the RAG Pipeline
Building the Retrieval-Augmented Generation (RAG) pipeline required handling document ingestion, text chunking, embeddings generation, and vector retrieval. Ensuring that the AI retrieves relevant clinical context before generating responses was critical to reduce hallucinations.

Managing Structured and Unstructured Data
The project had to handle structured hospital data (patients, encounters, billing) and unstructured medical documents (guidelines, research papers). Designing a system that could efficiently process and query both types of data required careful schema and storage decisions.

Security and Access Control
Since healthcare systems handle sensitive information, implementing secure authentication and role-based access control (RBAC) was important. Ensuring that only authorized users could access certain actions or data required middleware and permission checks.

Building Scalable Architecture
The project was designed to simulate a 200-bed hospital environment, which required thinking about modular architecture, database migrations, and scalable service separation between the hospital platform and the AI system.

Ensuring Reliable AI Responses
One of the key challenges was preventing AI hallucinations. The solution was to design the system so that answers are generated only after retrieving evidence from trusted clinical documents, and sources are included with responses.

Team **Syntax Flux Frontiers** -- [Danishmeet Singh](https://github.com/danishmeet), Riya Maan, [Aryan Dahiya](https://github.com/aryan0416), Miss Priyanka

`2026-03-08`

---

### SwayamShield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/swayamshield-caf6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Lovish00/SwayamShield---Copy.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XLiyDfdnkkk?si=Ok0c_uEOS1091TI2) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Empowering your healthcare journey.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

SwayamShield addresses the critical problem of delayed medical response during emergencies, especially in areas where patients struggle to quickly connect with hospitals, ambulances, and doctors. In many situations, people do not know which hospital has available beds, ambulances, or doctors, leading to wasted time that can cost lives. The platform provides a centralized healthcare emergency system where patients can instantly request an ambulance, track its arrival in real time, and connect directly with the hospital that is responding to the emergency.

At the same time, hospitals and administrators gain a city-level view of healthcare resources, including available beds, doctors, ambulances, and emergency ward capacity across registered hospitals. This helps improve resource allocation, coordination, and faster medical decision-making. By combining real-time tracking, hospital connectivity, and intelligent health assistance in one platform, SwayamShield makes emergency healthcare faster, more organized, and more accessible for both patients and healthcare providers.

**Challenges we ran into**

While developing SwayamShield, we encountered several technical and design challenges. One of the main challenges was implementing real-time features, such as ambulance tracking and emergency status updates, because it requires proper synchronization between the patient interface, hospital panel, and backend data. Another difficulty was managing and displaying healthcare data effectively, such as hospital resources (beds, doctors, ambulances, and emergency wards) across different hospitals in a city while keeping the interface simple and understandable.

We also faced challenges in designing a clean and responsive user interface, ensuring that the dashboard, hospital panels, and emergency sections remained visually clear while presenting multiple types of information. Integrating location-based features to detect the user's city and show relevant hospital data was another technical challenge. Additionally, implementing secure login and role-based access for patients, doctors, and admins required careful handling to prevent incorrect access (such as a patient logging into a doctor dashboard).

Overall, balancing functionality, real-time healthcare needs, and user-friendly UI/UX while building a reliable system was one of the key challenges during the development of the platform.

Team **The404s** -- Loveleen Dutta, Sourav Pandey, Lavisha Guglani, Lovish Bansal

`2026-03-08`

---

### ArogyaAi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/arogya-ai-d330) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aarush0008x/arogya) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://arogya-bice.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> ai health companion

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Healthcare access remains a major challenge globally.

People often face difficulties such as:

• Lack of quick medical guidance
• Difficulty understanding health symptoms
• Delayed doctor consultation
• No organized personal health tracking
• Limited awareness of preventive healthcare

Additionally, many individuals search for medical advice online but encounter unverified or confusing information, which can lead to incorrect self-diagnosis.

As a result:

• Minor health issues may escalate
• Patients become anxious
• Healthcare resources are inefficiently used

**Challenges we ran into**

1️⃣ Integrating AI with the Web Application 🤖

One of the biggest challenges was connecting the AI model with our web application.
We had to design a proper prompt structure so that the AI could understand the user’s symptoms and return useful results like possible conditions, risk level, and advice.

How we solved it:
We created a structured prompt and formatted the AI response into JSON so it could be easily displayed on the frontend.

2️⃣ Handling Natural Language Symptoms 🧠

Users can describe symptoms in many different ways. For example, someone might write “head pain” while another person writes “headache”. This makes symptom analysis challenging.

Solution:
We used an AI language model that can understand natural language and interpret different ways of describing symptoms.

3️⃣ Designing a Simple and User-Friendly Interface 🎨

Healthcare platforms can easily become complex, but we wanted ArogyaAI to be very simple and easy to use.

Solution:
We focused on a clean UI using Next.js and TailwindCSS, and designed the workflow as simple as possible:
Login → Enter symptoms → Get AI results.

4️⃣ Managing Health Data Securely 🔒

Since the platform stores health-related information, data security and privacy were important concerns.

Solution:
We implemented JWT authentication and structured database storage so users can only access their own reports.

5️⃣ Making the System Scalable 📈

Another challenge was designing the system so it can handle more users in the future.

Solution:
We used a modular architecture separating frontend, backend, AI processing, and database, which allows the system to scale easily.

6️⃣ Ensuring Responsible AI Usage ⚠️

AI in healthcare must be used carefully because incorrect suggestions could mislead users.

Solution:
We added a clear disclaimer and designed the AI to provide general guidance instead of medical diagnosis, encouraging users to consult doctors when necessary.

Team **Coffeebyte** -- Aarush Singh, Angel Verma, Renuka Saini

`2026-03-08`

---

### CarePath
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carepath-0336) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/satyajitmishra-dev/carepath) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://carepath-sandy.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Your health Your route

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![MERN stack](https://img.shields.io/badge/MERN%20stack-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

CarePath is a web app that helps users identify the right medical specialist based on their symptoms and **locate nearby clinics** on an **interactive map**. It provides **clear recommendations, urgency indicators, directions to clinics, and an emergency helpline button,** making healthcare navigation faster, safer, and more efficient. The app is especially useful for first-time patients or anyone seeking quick, reliable medical guidance.

**Challenges we ran into**

We faced several issues while building the app: **the UI initially had rendering problems, and API calls were not fetching data properly.** Additionally, our Over pass turbo dataset of 255 clinics was not in the correct GeoJSON format, so map markers displayed incorrectly or not at all. To overcome these challenges, **we debugged the frontend, corrected API endpoints**, and wrote a preprocessing script to transform the dataset into the required schema. These experiences taught us the importance of frontend-backend integration, data consistency, and thorough debugging.

**AI / ML**

For the MVP, we focused on delivering a fully functional end-to-end symptom-to-specialist system, so we implemented rule-based logic combined with the Gemini API to analyze symptoms and suggest specialists. This allowed us to validate the core workflow and user experience. While we haven’t integrated a full ML model yet, the project is designed to support AI/ML enhancements, such as using machine learning or NLP to analyze free-text symptoms, predict conditions, and detect urgency levels in future iterations.

Team **NexAura** -- [Medha Parul](https://github.com/medhaparul8-wq), [DEBOJYOTI BAIN](https://github.com/DEBOJYOTI-BAIN), [Rupam Manna](https://github.com/nope6901), [Satyajit Mishra](https://github.com/satyajitmishra-dev)

`2026-03-11`

---

### medimap
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medimap-a1af) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Subhojeetacharjee/Exibit-hackathon-Code-x-.git) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Find the Right Medical Specialist

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

People often experience health symptoms but do not know which medical specialist they should consult. This confusion can lead to visiting the wrong doctor, wasting time, and delaying proper treatment. Additionally, finding nearby and affordable clinics quickly can be difficult. The project solves this by helping users input symptoms and instantly discover the appropriate specialist along with nearby clinics.

**Challenges we ran into**

While building this project, I faced several challenges.

One challenge was accurately mapping symptoms to the correct medical specialist, since many symptoms overlap across different conditions. To solve this, I implemented a simple symptom-to-specialist mapping system using keyword detection.

Another challenge was integrating map services to display nearby clinics. Setting up APIs like Google Maps required proper configuration and API keys. I resolved this by carefully configuring the API and testing it with sample location data.

I also faced difficulty in obtaining reliable data about affordable clinics, since consultation fee data is not always publicly available. To address this in the prototype, I used sample clinic data with estimated consultation fees.

Finally, designing a user-friendly interface was important. I focused on creating a clean and simple UI with clear inputs, results, and map visualization so users could easily understand the recommendations.

**AI / ML**

The project uses basic symptom analysis and keyword detection to recommend the correct medical specialist. This involves simple AI/ML or NLP-based logic to interpret user input and map symptoms to specialists.

Team **CODE-X** -- [Subhojeet Acharjee](https://github.com/Subhojeetacharjee), [Dhiman Nath](https://github.com/nathdhiman005-svg), [Esha Parvin](https://github.com/Esha-Parvin)

`2026-03-11`

---

### symptIQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/symptiq-d7e0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://69b14e44ad50010837aabc3c--heroic-shortbread-e231b9.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Everyone should use this for you health

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square)

**The problem it solves**

This is a project for your health

Team **Shadow Coders** -- [Deboparna Ghosh](https://github.com/deboparna-XC), [Rohan Majumdar](https://github.com/RohanxCodec), [Srijit dam](https://github.com/srijitxc), [Arpita Paul](https://github.com/arpita167paul)

`2026-03-11`

---

### The "Wellness Nudge" Web
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/the-wellness-nudge-web-89e7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://team-dataflow-4ei8.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Health First

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Netlify](https://img.shields.io/badge/Netlify-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

1. Long Continuous Screen Time

Many people (students, developers, office workers) sit for hours without breaks.

Problems caused:

Eye strain 👀

Neck & back pain

Poor posture

Solution:
The app reminds users to take micro-breaks like stretching or looking away from the screen.

2.Dehydration During Work

People often forget to drink water when focused on work.

Problems caused:

Headache

Fatigue

Reduced concentration

Solution:
The app sends hydration reminders during work sessions.

3. Mental Stress & Burnout

Continuous work without rest leads to:

Mental fatigue 🧠

Stress

Low productivity

Solution:
The app suggests breathing exercises or short relaxation breaks.

4. Lack of Healthy Work Routine

Many users do not follow a structured work–break cycle.

Solution:
The app uses a work timer + gamification to build healthy habits.

Example:

Work 25 minutes

Take a 2–3 minute break

Get points for completing breaks 🎮

5. Low Motivation to Follow Healthy Habits

People ignore reminders if they are boring.

Solution:
Gamification:

Points 🏆

Streaks 🔥

Progress bar

Rewards for healthy behavior

Team **TEAM DATAFLOW** -- [Shambhu Pradhan](https://github.com/Shambhu721426), [Aritra Mandal](https://github.com/aritracoder-435), [Bubai Das](https://github.com/coded-by-bubai), [Argha Dey](https://github.com/mrarghadey-commits)

`2026-03-11`

---

### Health-Tech and Wellbeing Project
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthtech-and-wellbeing-project-b28e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mamun-9t3.github.io/Health-and-Wellbeing/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/kVoT1R8bBU4) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Wellness Nudge website

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Health Companion is a web-based health assistance platform that helps users manage wellness and access quick medical guidance. It includes a wellness timer, symptom checker that suggests appropriate specialists, an AI-powered doctor chatbot, and a GPS-based hospital finder. The system also detects potential emergencies and provides navigation to the nearest hospital.

**Challenges we ran into**

Integrating the AI chatbot

Team **The repo bloomers** -- [Bristi Santra](https://github.com/slyrn-star), [MdMamun Alam](https://github.com/Mamun-9t3), [RAMIZ ALI](https://github.com/aliramij), [Aryan Goldar](https://github.com/agoldar649-dev)

`2026-03-11`

---

### MediNova
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medinova-4be8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RajanyaMondal/Health-Analyze) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Smart Health, Better Care

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Many people struggle to understand their health symptoms and often do not know which specialist doctor they should consult. This leads to delays in getting proper treatment and unnecessary hospital visits.

Medinova solves this problem by allowing users to enter their symptoms and receive guidance about possible health issues and the appropriate medical specialists. The platform simplifies the process of finding the right doctor and enables users to easily book consultations online.

It also reduces the time spent searching for healthcare information by providing a centralized platform where users can check symptoms, discover recommended doctors, and schedule appointments in one place. This makes healthcare access faster, more convenient, and more organized for patients.

**Challenges we ran into**

While building **Medinova**, I faced several technical and design challenges. One major challenge was implementing the **symptom input system** so that users could easily describe their health issues and get relevant suggestions. Mapping symptoms to possible medical specialties required careful logic and structuring of the data.

Another challenge was integrating **secure user authentication and appointment booking functionality**. Ensuring that users could register, log in, and book consultations smoothly without errors required proper backend validation and database handling.

I also faced difficulties while designing a **clean and user-friendly dashboard**, where users could view doctor recommendations, manage bookings, and track their health information. Balancing functionality with a modern UI required several iterations.

To overcome these challenges, I researched documentation, tested different approaches, debugged errors, and improved the system step by step. This process helped me strengthen my understanding of **full-stack development, API integration, and user-centered design**.

**Sustainability**

it solve peoples health issues

Team **Cuties** -- [Rohit Patra](https://github.com/ROHIT123-rr), [Rohit Mandal](https://github.com/rohitmandal2004), [Debjyoti Das](https://github.com/Deb911), [Rajanya Mondal](https://github.com/RajanyaMondal)

`2026-03-11`

---

### Wellness Nudge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wellness-nudge-9fde) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AmritaChakraborty217/WellNudge-Pro) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://well-nudge-pro.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> "Work smarter. Break better. Feel the difference."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Most people who work on computers know they should take breaks — but they don't. Not because they're lazy, but because no tool reminds them in a way that actually fits their rhythm.Existing solutions are either too generic (a simple timer), too aggressive (constant popups), or too complicated (enterprise wellness platforms). Nothing learns from you. Nothing adapts.
**NudgeWell fixes that.**
**NudgeWell doesn't just remind you to take a break. It knows which break you need, why you need it right now, and makes sure you actually want to take it.**

**Challenges we ran into**

🐛 Challenges I Ran Into

1. SVG Ring Not Rendering on Load
The timer ring was invisible on every page load. Cause: strokeDasharray was set after updateDisplay(). Fixing the order of two lines in init() solved it instantly.

2. Double XP Bug
Every break awarded +20 XP instead of +10. The completeBreak() function was firing twice — from the button click and the interval hitting zero simultaneously. Fixed with a simple breakCompleted boolean guard flag.

3. Daily Counter Never Resetting
Break counts carried over across days. Added a wn_break_day key in localStorage that compares today's date on every load and resets all daily counters when the date changes.

4. Confetti Invisible on Screen
Confetti pieces vanished immediately. The cause was using vw as an inline CSS unit — which browsers silently reject. Changing one character from 'vw' to '%' fixed it.

5. AI Pill Getting Pushed by the Panel
The Wellness AI pill shifted position whenever the chat panel opened. Pill and panel were flex siblings, so the hidden panel still occupied layout space. Fixed by giving both independent position: fixed values and making the wrapper a zero-height ghost element.

6. Streak Not Saving
Streak reset to 1 on every refresh. The saveState() function was saving everything except streak. One missing localStorage.setItem('wn_streak', streak) line was the entire bug.

7. Guided Audio Cutting Off
Speech synthesis cut off mid-sentence on Chrome. Chrome silently kills long utterances. Fixed by splitting audio into short sentences and chaining them through the onend callback instead of firing simultaneously.

**Health & WellBeing**

🏥 Health & Wellbeing Track
NudgeWell directly addresses one of the most overlooked health crises of the modern age — sedentary desk work and digital burnout.
The average knowledge worker sits for 8–10 hours a day, skips water for hours at a time, and never stops to breathe intentionally. Over time this leads to chronic back pain, dehydration, eye strain, anxiety, and cognitive fatigue. Most people know this. Most people do nothing about it — because no tool makes it easy enough.
NudgeWell sits at the intersection of behavioral science and preventive wellness. Every feature is rooted in a real health outcome:

🤸 Stretch breaks → prevent musculoskeletal strain from prolonged sitting
💧 Hydration nudges → combat the 15% cognitive drop caused by mild dehydration
🌬️ Breathing exercises → reduce cortisol levels and manage workplace stress
😊 Mood tracking → builds self-awareness around emotional patterns during work
🤖 AI personalization → ensures the right intervention reaches the user at the right moment, not at a fixed arbitrary time

What makes NudgeWell uniquely suited to this track is that it doesn't just inform — it intervenes. It doesn't show you a wellness dashboard and hope you act on it. It actively learns your behavior, detects risk windows like hydration gaps and post-lunch slumps, and delivers a targeted micro-intervention before the health impact compounds.
The gamification layer — XP, streaks, quests, and a virtual plant — is not cosmetic. It is a deliberate behavioral design choice based on habit formation research. Small rewards at the moment of the healthy action are proven to increase long-term compliance far more effectively than guilt or generic reminders.

**NudgeWell doesn't treat wellness as a feature. It makes wellness the entire product — personalized, proactive, and built into the rhythm of how people already work.**

Team **The Three Musketeers** -- [Sk Shahanjum](https://github.com/shahanjumsk-maker), [Siddhartha Ghosal](https://github.com/Siddhartha-Ghosal), [Amrita Chakraborty](https://github.com/AmritaChakraborty217)

`2026-03-11`

---

### wellness nudge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wellness-nudge-1f99) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/majisoumya/wellness-nudge.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://wellness-nudge.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/6O_ZhsyoJhQ?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> This is helpfull for work life balence.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Wellness Nudge is a smart, non-intrusive web application designed to balance deep focus with essential wellness breaks. It acts as a calm companion that reminds you to breathe, stretch, hydrate, and rest your eyes—without breaking your flow or adding to the noise.

**Challenges we ran into**

1. Accurate Presence Detection
Detecting whether the user is actually present or distracted using webcam-based AI can be difficult due to lighting conditions, camera angle, or movement.

2. Privacy Concerns
Users may feel uncomfortable allowing webcam access for monitoring presence.

3. False Alerts
The system may incorrectly send reminders even when the user is focused.

4. Balancing Notifications
Too many wellness nudges can interrupt productivity instead of helping it.

5. Browser Permission Issues
Many users may deny camera permission, limiting AI presence detection.

6. Performance Overhead
Running TensorFlow.js models in the browser may increase CPU/GPU usage and slow down the system.

7. Accurate Wellness Tracking
Hydration, stretching, and breaks often rely on user input, which may not always be accurate.

8. Cross-Browser Compatibility
Different browsers handle Web APIs and camera access differently.

9. 3D UI Performance
Interactive 3D backgrounds can reduce performance on low-end devices.

10. Data Security
User activity and health data must be stored securely to prevent privacy risks.

**Web3**

1. HealthTech & Wellbeing
Focuses on improving physical and mental health through technology.
Your app helps reduce burnout, eye strain, and sedentary lifestyle, making it a strong fit.
2. Al / Machine Learning
Your project uses TensorFlow.js for presence detection, which applies Al to monitor user focus and
attention.
3. Future of Work / Productivity
Targets tools that improve how people work in the digital era.
Wellness Nudge helps maintain healthy productivity habits.
4. Human-Centered Technology
Focuses on building technology that prioritizes user wellbeing and experience rather than just
efficiency.
5. Web Innovation
Your app uses modern web technologies such as React, TypeScript, Vite, WebGL, and Supabase,
showcasing advanced web development.
6. Digital Wellness
Focuses on solving issues like screen addiction, digital fatigue, and work-life balance.
7. Smart Lifestyle / Lifestyle Tech
Technology solutions that improve everyday life habits, such as health tracking and daily productivity

Team **NeuroX** -- [Soumyadip Maji](https://github.com/majisoumya), [SAYAN PAUL](https://github.com/Sayan-Official-32/), [Rohan Roy](https://github.com/Rohan-SDE), [SUKHENDU PAL](https://github.com/RohanGit-497)

`2026-03-11`

---

### Health-Mate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthmate-6e56) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sarniva/health-mate) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/O0ITIUQTNMs?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Your daily wellness companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# Health-Mate: What Problem Does It Solve?

## The Problem
Modern workers struggle with sedentary lifestyles, dehydration, and lack of exercise motivation. Tracking health goals manually is tedious, and without accountability, habits rarely stick.

## What Health-Mate Solves

### 1. **Sedentary Work Lifestyle**
- Automatically reminds users to take breaks during work sessions
- Tracks break compliance and rewards consistency
- Gamification makes break-taking fun, not a chore

### 2. **Dehydration & Health Neglect**
- Smart reminders for hydration throughout the day
- Logs water intake and celebrates daily goals
- Tracks BMI and personal health metrics in one place

### 3. **Exercise Motivation**
- Gamification system awards points for workouts
- Achievements unlock (e.g., "Exercise Enthusiast" after 10 sessions)
- Global leaderboards create friendly competition

### 4. **Smoking Cessation**
- Tracks smoke-free streaks (starting at 7 days, up to 100+ days)
- Logs craving levels to understand triggers
- Rewards with high-value achievements and points

### 5. **Habit Accountability**
- Global leaderboards show user rankings by tier (Bronze → Platinum)
- Local peer challenges let friends compete
- Streaks motivate consistency (longer streaks = more points)

## How It Makes Tasks Easier/Safer

✅ **Easier** - Single app to track health, work sessions, and activities  
✅ **Safer** - Automatic reminders prevent health neglect during work  
✅ **Motivating** - Points, achievements, and leaderboards drive engagement  
✅ **Data-Driven** - Clear metrics on BMI, points, streaks, and tier progress  
✅ **Social** - Peer challenges create community and accountability  

## Use Cases

- **Office Workers** - Take healthy breaks, stay hydrated, maintain fitness
- **Smokers Quitting** - Track smoke-free days with celebration milestones
- **Fitness Enthusiasts** - Log workouts, compete on leaderboards
- **Remote Teams** - Create peer challenge groups for wellness accountability

**Challenges we ran into**

# Challenges & Bugs Encountered

## 1. **Clerk → JWT Migration**
**Problem:** Initially implemented Clerk for authentication, but it added unnecessary complexity and vendor lock-in.

**Solution:** Migrated to JWT + bcrypt for self-managed authentication:
- Removed `@clerk/express` dependency
- Implemented custom JWT token generation/verification
- Added bcrypt password hashing with pre-save hook
- Updated all middleware to use JWT instead of Clerk
- **Result:** Simpler, lighter, fully controlled authentication ✓

---

## 2. **Mongoose Pre-Save Hook Issue**
**Problem:** Password hashing pre-save hook was calling `next()` parameter, causing incompatibility with Mongoose 9.3.

**Solution:** 
- Removed `next()` parameter call from async pre-save hook
- Mongoose 9.3 handles async hooks differently than older versions
- Hook now completes naturally without next callback
- **Result:** Password hashing works correctly ✓

---

## 3. **Zod Date String Parsing**
**Problem:** `z.date()` doesn't automatically parse ISO 8601 date strings from JSON requests, causing validation failures.

**Solution:**
- Replaced `z.date()` with `z.coerce.date()` across all schemas
- Applied to: Activity, WorkSession, HealthProfile models
- Now accepts both Date objects and ISO date strings
- **Result:** Flexible date input handling ✓

---

## 4. **Achievement Badge Type Enum Mismatch**
**Problem:** Achievement model enum had 10 values, but `ACHIEVEMENTS_CONFIG` constants defined 21 achievement types. Caused validation errors when awarding achievements.

**Solution:**
- Updated Achievement model enum to include all 21 badge types
- Aligned with constants: `first_steps`, `kickstarter`, `water_master`, `smoking_slayer`, etc.
- Fixed: `badgeType: 'first_steps' is not a valid enum value` error
- **Result:** All achievements can be awarded correctly ✓

---

## 5. **Request Body Validation vs JWT Extraction**
**Problem:** Zod schemas required `userId` in request body, but controller extracted it from JWT token. Caused "Invalid request body" errors.

**Solution:**
- Made `userId` optional in all request schemas
- Schemas now accept data without userId (extracted from JWT by controller)
- Applied to: HealthProfile, Activity, WorkSession, Achievement models
- **Result:** Cleaner API requests, token-based user identification ✓

---

## 6. **Missing Optional Field Defaults**
**Problem:** Activity and WorkSession endpoints failed because required fields weren't set when not provided in requests.

**Solution:**
- Made `date` optional in activity schemas (defaults to current date)
- Made `sessionId` optional for break logging (allows manual breaks)
- Set `workDuration` default to `duration` in controller
- **Result:** Flexible input, sensible defaults ✓

---

## Key Learnings

- **JWT + bcrypt > Clerk** for control and simplicity
- **z.coerce.date()** over z.date() for API flexibility  
- **Optional request fields** with JWT extraction is cleaner UX
- **Enum mismatches** between models and configs cause runtime errors
- **Mongoose 9.3** has different async hook behavior than older versions

All issues resolved. API fully functional with 38+ endpoints tested ✓

Team **Ad Astra** -- [Mehedi Hasan](https://github.com/mehedihasan-coder), [Imran Ali](https://github.com/imranali5), [Sarniva Das](https://github.com/sarniva), [Aparup Santra](https://github.com/Aparup321)

`2026-03-11`

---

### Cura-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/curaai-7361) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rahulkadvasara/cura-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/178JHoAzw5gA9Wcm2eOdtBBtgWjut4qrm/edit?usp=sharing&ouid=100442616736790137201&rtpof=true&sd=true) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/pTr2wxVyHyg?si=Gb2dtM59Tw0ibkX2) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> A Safety-Aware Multi-Agent Healthcare Assistant

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SHA-256 Hashes](https://img.shields.io/badge/SHA--256%20Hashes-333333?style=flat-square)

**The problem it solves**

Healthcare information is often **difficult for patients to understand and manage**. Medical reports contain complex terminology, drug interactions can be dangerous if unnoticed, and patients frequently forget to take medications on time. Additionally, many AI health tools do not consider **safety, context, or privacy**, which is critical when dealing with sensitive medical data.

**Cura AI addresses these challenges by making healthcare guidance more accessible, safe, and personalized.**

People can use Cura AI to:

- **Understand medical reports easily** – Upload a lab report or medical image and receive a simple explanation in everyday language.
- **Check drug interactions before taking medicines** – The system analyzes potential risks between medications and warns users if interactions may occur.
- **Manage medication reminders** – Users can set reminders using natural language (e.g., *“Remind me to take Aspirin at 8 PM”*).
- **Get symptom guidance** – Users can describe symptoms and receive structured advice including possible causes, urgency level, and recommended actions.
- **Interact through voice** – Users can ask health questions or set reminders using voice input.
- **Protect sensitive medical data** – The system uses encryption and access control to secure user health information.

By combining **AI reasoning, safety checks, and privacy protection**, Cura AI helps users make **safer and more informed healthcare decisions** while simplifying everyday health management.

**Challenges we ran into**

### 1. Handling Medical Data Security
One major challenge was ensuring that **sensitive medical data was stored securely**. Since the system stores medicines, reminders, and report summaries, we implemented **encryption using Fernet** to protect stored health data. However, after adding encryption, older records stored in plain text caused decryption errors.  
To solve this, we implemented **safe decryption handling**, allowing the system to work with both encrypted and previously stored data.

### 2. Formatting AI Responses for Better UX
Initially, AI responses were returned as **long unstructured text**, which made them difficult to read. For example, drug interaction results and symptom explanations appeared in a single line without proper sections.  
We solved this by **parsing structured keywords** like Risk, Summary, Urgency, etc., and converting them into **formatted UI blocks with colors and sections** to make the output easier to understand.

### 3. Managing Multi-Agent Coordination
The project uses multiple specialized agents (Symptom, Report, Reminder, Drug Interaction). Coordinating them correctly through a **central routing system** was challenging.  
We solved this by implementing a **Coordinator Agent** that detects the user's intent and routes the request to the correct agent, ensuring modular and scalable architecture.

### 4. Handling Context and Memory
Maintaining **user context (medicine history and conversation memory)** was necessary for accurate responses like drug interaction analysis. Designing a system that combines **session memory and persistent memory** required careful structuring to avoid duplicate or inconsistent data.

These challenges helped improve the system’s **security, reliability, and user experience**, making the final product more robust and safe for healthcare use.

**Best Use of Gemini API**

Cura-AI is designed as a **multi-agent healthcare assistant powered by large language models**. The system architecture is model-agnostic, allowing us to easily integrate and run **Google’s Gemini API** for medical reasoning tasks.

In our project, Gemini is used to power several critical healthcare intelligence modules:

### 1. Medical Report Understanding
Users can upload medical reports (lab reports, blood test results, etc.).  
The system extracts text using OCR and sends it to the Gemini model, which generates **simple, patient-friendly explanations** of complex medical data along with a **risk assessment level (Low / Moderate / High)**.

### 2. Symptom Analysis and Guidance
Gemini helps analyze user-described symptoms and produces structured responses including:
- Possible causes
- Urgency level
- Recommended actions
- Emergency guidance

This allows users to receive **quick preliminary health guidance** before consulting a medical professional.

### 3. Drug Interaction Safety Analysis
When users set medicine reminders, Gemini analyzes the **interaction risk between multiple medications** and generates safety warnings when potentially harmful combinations are detected.

### 4. Natural Language Health Interaction
Gemini enables users to interact with Cura AI using **natural language queries**, allowing the system to understand intent such as:
- setting medicine reminders
- asking about symptoms
- requesting report explanations

### Why Gemini is Valuable for This System
Healthcare queries require **contextual reasoning, safety awareness, and structured responses**. Gemini’s strong language understanding capabilities allow Cura AI to:

- Interpret complex medical text
- Generate clear explanations for non-medical users
- Provide structured safety guidance
- Support conversational healthcare assistance

By integrating Gemini into a **multi-agent architecture**, Cura AI demonstrates how Gemini can power **intelligent, safe, and accessible healthcare assistants**.

![image](https://assets.devfolio.co/content/75613629feac4b59bbc3202eed1021c0/2a07fa52-6e89-4401-9fe4-d49f1fcbdb66.png)

**Best Use of Auth0**

Cura-AI handles **highly sensitive healthcare data**, making secure authentication and identity management a critical part of the system. Our architecture is designed to integrate with modern authentication platforms like **Auth0** to ensure secure user identity verification and controlled access to medical data.

### Secure User Authentication
Users must authenticate before accessing the healthcare assistant. Each user account is uniquely identified, and all interactions with the system are tied to that identity. This ensures that **medical history, reminders, and reports are securely linked to the correct user**.

### Access Control for Medical Data
Every backend API request includes the authenticated user's identity. The backend verifies that the requesting user is allowed to access the requested resources before processing the request. This prevents unauthorized access to sensitive healthcare information such as:
- medical reports
- medication reminders
- health conversation history

### Protection of Sensitive Health Information
Healthcare data is extremely sensitive. To ensure privacy and security, the system enforces:
- **identity verification for every API request**
- **user-level data isolation**
- **encrypted storage for medical records**

By combining **secure authentication, identity verification, and access control**, Cura AI ensures that users maintain full control over their personal healthcare data.

### Why This Matters
Healthcare applications require strong identity protection to prevent data misuse. Integrating authentication platforms like **Auth0** enables Cura AI to provide **secure, scalable, and privacy-first healthcare assistance**, ensuring that personal medical information is protected at every interaction.

![image](https://assets.devfolio.co/content/75613629feac4b59bbc3202eed1021c0/6dd69436-3850-40b9-b09e-68b71698686c.png)

**Best Hack Built with Google Antigravity**

Google Antigravity was used as our primary **AI-native development environment** while building Cura AI. It significantly accelerated development by helping us design, iterate, and debug different parts of our multi-agent healthcare system.

### Rapid AI Prototyping
Using Antigravity’s AI-assisted coding capabilities, we quickly prototyped multiple healthcare agents including the **Symptom Agent, Report Analysis Agent, Drug Interaction Agent, and Reminder Agent**. This allowed us to experiment with different prompt structures and response formats efficiently.

### Faster Debugging and Iteration
While integrating multiple APIs, OCR processing, and backend routing, Antigravity helped us **debug issues faster**, suggest improvements to our Python and JavaScript code, and optimize our architecture during the hackathon.

### Multi-Agent System Development
Our system required coordinating several specialized AI agents through a **central coordinator architecture**. Antigravity helped us iterate on this architecture rapidly and test different routing strategies for symptom analysis, report summarization, and medication safety checks.

### Productivity During the Hackathon
Because hackathons require rapid development under tight time constraints, Antigravity enabled us to:
- write and refactor backend logic faster
- test AI prompts and workflows quickly
- iterate on UI and API integrations efficiently

This allowed our team to focus more on **building meaningful healthcare functionality** rather than spending excessive time on debugging and repetitive coding tasks.

By using Google Antigravity as our development environment, we were able to **accelerate the creation of a complex AI-powered healthcare assistant within the hackathon timeframe**.

Team **Aurix** -- [Rahul Kumar](https://github.com/rahulkadvasara)

`2026-03-08`

---

### EcoRoute
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecoroute-dd67) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Alman8904/EcoRoute) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1171435707?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Healthy Route Navigation

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Every navigation app today answers one question: "How do I get there fastest?" But for the 400+ million people worldwide with respiratory conditions — and for children, seniors, and urban commuters breathing polluted air daily — how clean the air is along the route matters just as much as travel time.EcoRoute solves the invisible danger of air pollution during daily commutes.Most people have no idea that two routes of similar length can differ by 30–40% in PM2.5 exposure. They don't know whether to leave now or wait 30 minutes for rush-hour pollution to clear. They have no concept of how much pollution they've already inhaled today, or how close they are to the WHO's safe daily limit.What people can use it for:
Asthma/allergy sufferers can pick the route that minimises airway irritants, using a dedicated health profile with a 35% sensitivity multiplier that adjusts every recommendation.
Parents can use the "Child" profile to plan school commutes and outdoor activities with tighter daily exposure budgets.
Urban cyclists and joggers who breathe harder and inhale more pollution per kilometre than car passengers can compare up to 3 alternative routes side-by-side and pick the cleanest one.
Senior citizens can benefit from personalised departure timing advice — the AI card tells them whether to leave now, wait 30 minutes, or wait an hour based on a real 12-hour air quality forecast.
Anyone commuting in polluted cities can track their daily and weekly pollution "budget" with a visual radial meter, build streaks of healthy days, and get alerted when they're approaching the WHO daily PM2.5 limit.
Health-conscious commuters get a lung visualiser that fills like a tank — showing exactly how many micrograms of PM2.5 they'll inhale on a given route, expressed as a percentage of the WHO daily safe limit.

**Challenges we ran into**

1. Getting truly different alternative routes from ORS
OpenRouteService's alternative_routes API was finicky — in many city geographies it returned only 1 route even when 3 were requested. We had to tune weight_factor (how much longer a route could be) and share_factor (how different it had to be in waypoints) iteratively. We also had to gracefully handle the case where ORS returns a FeatureCollection vs a plain route object, since the shape of the response changed depending on the endpoint variant we used.
2. AQI data sparsity crashing the scoring pipeline
WAQI only has stations in certain locations. When sampling 3 GPS points along a route, we'd frequently get null or undefined AQI back for rural or mid-route points. This caused NaN health scores and broken UI states. We fixed it with defensive averaging — filtering out nulls before computing the mean, and falling back to AQI-based scoring (instead of the more accurate PM2.5-based formula) when real PM2.5 data was unavailable. The mock fallback mode ([45, 120, 72]) was added to unblock demos entirely.
3. Leaflet + React StrictMode double-initialization
React 19 with StrictMode runs useEffect twice in development, which caused Leaflet to initialize two map instances on the same DOM node, breaking the map with a silent white screen. The fix was lazy-loading Leaflet via import('leaflet') inside useEffect and tracking a mapInitialized ref — so the second StrictMode call was a no-op.
4. LLM API reliability under hackathon time pressure
The Gemini and OpenAI keys both had rate-limit or latency issues during testing. Rather than let a failed AI call break the whole departure card, we built a 3-tier cascade: Gemini → OpenAI → deterministic rule-based fallback. Each tier has an 8-second timeout. This meant the Decision Card always rendered something useful even under zero-key demo conditions.
5. PM2.5 dose formula calibration
The lung visualiser only makes sense if the numbers feel medically grounded. We had to research WHO guidelines (25 μg/m³ daily safe limit), breathing rates for light walking (~18 L/min), and inhalation fraction to arrive at a formula that produced intuitive results — low numbers for clean short routes, alarming numbers for long rush-hour commutes. Getting the BREATHING_RATE_FACTOR and duration scaling right took several iterations of sanity-checking against real-world exposure studies.

**Best Use of Gemini API**

You've selected the "Best Use of Gemini API" track. Here's what to write in the explanation box:

EcoRoute uses the Gemini 1.5 Flash API as the primary AI reasoning engine for its departure decision card — one of the app's most distinctive features.
When a user plans a route, EcoRoute doesn't just show air quality data — it uses Gemini to synthesise real-time AQI readings, PM2.5 levels, the user's health profile (General / Asthma / Child / Senior), and a 12-hour Open-Meteo forecast into a plain-language, actionable recommendation: leave now, wait 30 minutes, or wait an hour.
The Gemini prompt is tightly constrained to 150 tokens and given rich context — current AQI, predicted future AQI, time of day (rush hour vs off-peak), and the user's medical sensitivity multiplier. This ensures responses are personalised, concise, and medically grounded rather than generic.
Gemini is the first tier in a 3-tier AI cascade (Gemini → OpenAI GPT-4o-mini → rule-based fallback), with an 8-second timeout per tier — guaranteeing the feature always works even under API instability during a live demo.

Team **MetaMinds** -- [Rishikesh Dhote](https://github.com/rishikeshdhote29), [Rohit Singh](https://github.com/rohit663), [Alman Khan](https://github.com/Alman8904), [Piyush Ray](https://github.com/Piyush0631)

`2026-03-08`

---

### AI-based smart queue system for hospital
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aibased-smart-queue-system-for-hospital-ff17) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/manya-upadhyay/hospital-queue-system) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Prioritizing Patients Intelligently.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Hospitals often face long waiting queues and inefficient patient prioritization, which can delay treatment for patients who need urgent care. In many hospitals, patients are treated on a first-come, first-served basis, without properly considering the severity of their symptoms. This can result in critical patients waiting longer while less urgent cases are treated earlier.
Additionally, hospital staff manually managing queues can lead to human errors, miscommunication, and inefficiency, especially during peak hours or emergencies. Patients may also misreport symptoms or mark their case as an emergency, making it difficult for hospitals to identify genuine urgent cases.
Our system addresses these challenges by providing an AI-powered smart queue management system that analyzes patient symptoms and assigns priority levels automatically, ensuring that emergency cases receive faster medical attention while maintaining a fair and efficient queue system.

**Challenges we ran into**

During the development of this project, we faced several technical and design challenges. One of the main difficulties was designing a fair and accurate patient prioritization system, ensuring that emergency patients are identified correctly without allowing misuse of the emergency option.

Another challenge was handling incorrect or incomplete symptom inputs from users, which could affect the accuracy of the queue prioritization. We also worked on creating a system that can balance both emergency and normal cases efficiently so that the queue remains fair for all patients.

From a technical perspective, integrating the database with the backend system and ensuring smooth data flow between the frontend interface and backend logic required careful implementation. Additionally, designing a simple and user-friendly interface for patient registration and queue tracking was important so that the system can be easily used in real hospital environments.

Despite these challenges, we were able to build a functional AI-based smart queue system that improves patient prioritization and reduces waiting time in hospitals.

**Best Use of Gemini API**

Our project integrates the Gemini API to enhance the intelligence of the hospital queue management system. When a patient enters their symptoms during registration, the system sends the symptom data to the Gemini API, which analyzes the medical context and determines the severity level of the condition.

Based on this AI-driven analysis, the system assigns a priority score to the patient. Emergency or high-risk cases are automatically moved to the top of the queue, ensuring that critical patients receive faster medical attention. This helps hospitals reduce waiting times and improve patient care.

By using the Gemini API’s natural language understanding, our system can interpret symptom descriptions provided by patients, even if they are written in simple or non-technical language. This makes the queue prioritization process more accurate, intelligent, and efficient compared to traditional first-come-first-serve systems.

Thus, the Gemini API plays a key role in enabling AI-powered symptom analysis and smart patient prioritization in our hospital queue system.

Team **Mindspark** -- [Kashish Chaudhary](https://github.com/KashishCh02), [Sneha Chaudhary](https://github.com/chaudharyhimani402-debug), [Manya Upadhyay](https://github.com/manya-upadhyay)

`2026-03-08`

---

### MedAi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medai-1905) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Lucifer-ipynb2/MedAi/tree/main) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nT4_Pen8ckE) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Diagnose Smarter, Live Healthier.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

## 🩺 What is MedAI?

**MedAI** is an AI-powered healthcare assistant designed to help users quickly understand their symptoms and access reliable medical information. It uses advanced AI models to analyze user input and provide helpful insights related to possible health conditions, precautions, and general medical guidance.

---

## 🚀 What Can People Use MedAI For?

### 1️⃣ Quick Symptom Analysis
Users can describe their symptoms (e.g., fever, headache, cough), and MedAI analyzes them to suggest possible conditions and provide basic medical insights.

This helps users:
- Understand what their symptoms might indicate
- Decide whether they should seek medical attention
- Get preliminary health information instantly

---

### 2️⃣ Instant Medical Information
MedAI acts as a **medical knowledge assistant** where users can ask questions such as:

- "What causes migraines?"
- "What are the symptoms of dengue?"
- "How to reduce fever at home?"

The AI provides clear explanations in an easy-to-understand format.

---

### 3️⃣ Early Awareness and Preventive Guidance
Many people ignore early symptoms due to lack of information. MedAI helps by providing:

- Possible health explanations
- Preventive tips
- Basic safety precautions

This can encourage users to take early action for their health.

---

### 4️⃣ 24/7 AI Health Assistant
Unlike traditional healthcare consultation which may require appointments, MedAI is available **anytime and anywhere**, allowing users to quickly get health-related insights.

---

## 💡 How MedAI Makes Existing Tasks Easier

### ⚡ Faster Access to Health Information
Instead of searching multiple websites for medical information, users can get **structured answers instantly** from MedAI.

### 🧠 Simplifies Medical Knowledge
Medical terms can be confusing. MedAI explains symptoms, diseases, and precautions in **simple and understandable language**.

### ⏱ Saves Time
Users can quickly understand their symptoms without spending hours researching online.

### 📚 Consolidated Medical Guidance
MedAI combines medical information, symptom analysis, and guidance into a **single AI-powered platform**.

---

## ⚠️ Important Disclaimer

MedAI is designed for **educational and informational purposes only**.  
It does **not replace professional medical advice, diagnosis, or treatment from a licensed healthcare provider**.

Users should always consult a qualified doctor for serious medical concerns.

---

## 🌍 Potential Impact

MedAI can help improve **health awareness and accessibility to medical information**, especially for people who need quick guidance before consulting a healthcare professional.

**Challenges we ran into**

## 🐞 Challenges & Bugs Faced During Development

### 1️⃣ API Integration Errors
One of the biggest hurdles during the development of **MedAI** was integrating the AI model through the OpenRouter API. Initially, the application frequently returned **"Server Error" responses** when users tried to send messages to the AI chatbot.

#### 🔍 Problem
The issue occurred because:
- The API key was not correctly loaded from environment variables.
- The request headers and body format required by the OpenRouter API were slightly different from the default configuration.

This resulted in failed API requests and prevented the chatbot from generating responses.

#### 🛠 Solution
To fix this issue:
- The API key was moved to a `.env` file and accessed using `import.meta.env` in the React application.
- Proper headers were added to the request, including:
  - `Authorization`
  - `Content-Type`
- The request body was structured according to the **chat completion format required by the AI model**.

After correcting the API request format and environment variable configuration, the AI responses started working correctly.

---

### 2️⃣ Rendering AI Responses Properly
Another challenge was displaying the AI-generated responses in a **clean and readable format**.

#### 🔍 Problem
The AI often returned responses containing:
- Markdown formatting
- Bullet points
- Headings

Without proper rendering, these responses appeared as **plain text**, making them difficult to read.

#### 🛠 Solution
To solve this problem, the following libraries were integrated:

- `react-markdown`
- `remark-gfm`

These libraries allowed the application to render AI responses with proper formatting, including lists, headings, and structured content.

---

### 3️⃣ Managing Chat State in React
Maintaining the chat history between the user and the AI was another technical challenge.

#### 🔍 Problem
Initially, new messages were not properly appended to the existing chat history, which caused messages to disappear or overwrite previous responses.

#### 🛠 Solution
This was solved by implementing **React state management** using the `useState` hook to store and update the message history dynamically. Each user message and AI response was pushed into a messages array, ensuring the chat conversation remained intact.

---

## 🎯 Key Learning

Overcoming these challenges helped improve understanding of:

- API integration with AI services
- Environment variable management in React (Vite)
- State management in React applications
- Rendering dynamic AI-generated content

These improvements ultimately made **MedAI more stable, user-friendly, and reliable.**

**Best Use of Gemini API**

## 🏆 How MedAI Fits into the Major League Hacking Track

**MedAI** aligns well with the **Major League Hacking (MLH)** track because it focuses on building an innovative, real-world solution using modern technologies such as **Artificial Intelligence, React, Python, and APIs**.

### 🚀 Innovation Through Technology
MLH encourages developers to build creative solutions that solve real-world problems. MedAI does exactly that by using **AI-powered medical assistance** to help users understand their symptoms and access reliable health information quickly.

### 🧠 AI-Powered Problem Solving
This project integrates **Large Language Models (LLMs)** through the OpenRouter API to analyze user symptoms and provide intelligent responses. This demonstrates how modern AI tools can be used to build practical applications that improve everyday life.

### 💻 Full-Stack Development
MedAI showcases a **full-stack development approach**, combining multiple technologies:

- **Frontend:** React.js for an interactive and responsive user interface
- **Backend:** Node.js / Flask for handling API communication
- **AI Integration:** OpenRouter AI models for generating medical insights
- **Markdown Rendering:** For structured and readable responses

This reflects the kind of **technical experimentation and learning** encouraged in MLH hackathons.

### 🌍 Real-World Impact
MLH projects often focus on solutions that create a meaningful impact. MedAI contributes to this by improving **health awareness and accessibility to medical information**, allowing users to quickly understand potential health concerns before consulting a medical professional.

### 📚 Learning and Exploration
Building MedAI involved exploring several important development concepts such as:

- AI API integration
- State management in React
- Handling asynchronous requests
- Designing user-friendly interfaces for AI systems

These learning experiences align strongly with the **MLH mission of empowering developers to build, learn, and innovate.**

---

## 🎯 Conclusion
MedAI demonstrates how modern web technologies and AI can be combined to build a **practical, impactful, and innovative solution**, making it a strong fit for the **Major League Hacking track**.

**Best Hack Built with Google Antigravity**

## 🏆 How MedAI Fits into the Major League Hacking Track

**MedAI** is a strong fit for the **Major League Hacking (MLH)** track because it demonstrates innovation, technical complexity, and real-world impact by combining modern web development with AI technology.

### 🚀 Innovative and Practical Solution
MedAI addresses a real-world problem: **quickly understanding medical symptoms and accessing reliable health information**. By leveraging AI, it automates tasks that typically require research or a medical consultation, making healthcare information **faster, safer, and more accessible**.

### 💻 Full-Stack Development
The project showcases strong technical implementation:
- **Frontend:** React.js for a responsive and interactive user interface
- **Backend:** Node.js / Flask for API handling and AI integration
- **AI Integration:** OpenRouter API for generating medical insights
- **Markdown Rendering:** `react-markdown` and `remark-gfm` for clean and readable AI responses

This demonstrates proficiency in building **full-stack applications** that integrate multiple technologies seamlessly.

### 🧠 AI-Powered Impact
MedAI uses AI to:
- Analyze symptoms and provide potential diagnoses
- Offer preventive guidance and early warnings
- Make medical knowledge understandable and accessible to everyone

This aligns with MLH’s focus on **using technology to solve meaningful problems**.

### 🌍 Real-World Relevance
By providing 24/7 AI-driven health assistance, MedAI:
- Improves **health awareness**
- Encourages **early preventive action**
- Offers a **safe platform for educational medical guidance**

This shows how hackathon projects can **directly impact users’ daily lives**.

### 🎯 Learning and Growth
Developing MedAI required overcoming challenges like:
- API integration errors
- Chat state management in React
- Rendering dynamic AI responses properly

These experiences reflect **MLH’s goal of fostering technical learning and creative problem-solving**.

---

**In summary:** MedAI exemplifies how hackathon projects can combine **innovation, AI, and full-stack development** to create a **practical, impactful, and user-focused solution**, making it an ideal fit for the Major League Hacking track.

[Divyang Jain](https://github.com/Lucifer-ipynb2)

`2026-03-08`

---

### HealthLinke
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/healthlinke-a429) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://healthlike.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Prescription Insights. Smarter Choices

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

1.Misreading prescription details or medical terminology.

2.Forgetting medication schedules or dosages.

3.Navigating multiple platforms to order medicines safely.

4.Lack of accessible guidance for health decisions.

**Challenges we ran into**

1.The server was not responding correctly, and we couldn’t figure out where it was running or why some API calls were failing.

2.This caused delays in connecting the frontend with the AI assistant and prescription analysis functionalities.

**Best Use of ElevenLabs**

We integrated Eleven Labs’ API to power our AI assistant’s voice capabilities. This allows the platform to read prescriptions aloud, give spoken suggestions, and interact naturally with users. By combining voice AI with prescription analysis and online ordering, the experience becomes more humanized, accessible, and engaging, making healthcare guidance feel personal and easy to follow.

Team **Error_99** -- [harsh prajapati](https://github.com/hp750746-ai), [Narendra Prajapat](https://github.com/mrnarendra3211-bit), [Abhishek Lama](https://github.com/abhisheklama12)

`2026-03-08`

---

### AHAR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ahar-618c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kapil-singh18/AHAR) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://food-waste-management-iota.vercel.app/consumption) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/-x_UFLvezvo?si=EXrO3PBVcXXk_j-n) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> AI based hospitality analytics and resource optimi

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

# What Problem I Solved Using AHAR

AHAR addresses a critical issue in the hospitality industry: food waste management and resource optimization. The problem I solved involves multiple interconnected challenges that restaurants and food service businesses face daily.

## The Core Problem
Food waste is a significant global issue, with hospitality businesses contributing substantially to it through inefficient inventory management, inaccurate demand prediction, and poor donation coordination. Traditional methods rely on manual processes that are time-consuming, error-prone, and lack real-time insights.

## Key Problems Addressed

### 1. Inefficient Inventory Management
- Manual tracking of ingredients and menu items
- Difficulty in predicting expiration dates
- Lack of real-time stock visibility
- Over-purchasing leading to waste

### 2. Inaccurate Demand Prediction
- Reliance on historical data without AI assistance
- Inability to factor in external variables like weather and events
- Over-production of food leading to surplus

### 3. Poor Donation Coordination
- Lack of streamlined process to connect surplus food with NGOs
- Manual coordination efforts
- Limited visibility of donation opportunities

### 4. Lack of User Authentication and Payment Processing
- No secure user management system
- Absence of monetization features for premium services
- Difficulty in managing user access and subscriptions

## The Solution
I developed a comprehensive web application called "AHAR" (AI-based Hospitality and Resource Optimizer) that integrates:

- **AI-powered demand prediction** using machine learning models
- **Real-time inventory management** with automated tracking
- **Smart donation locator** for connecting surplus food with NGOs
- **User authentication** using Clerk for secure access
- **Payment gateway integration** with Razorpay for monetization
- **Responsive UI** with integrated branding and logo

## Impact
This solution helps restaurants reduce food waste by up to 30%, optimize resource utilization, and create a sustainable food ecosystem. AHAR provides actionable insights that enable data-driven decision making, ultimately contributing to environmental sustainability and social good through better donation management.

The project demonstrates how technology can transform traditional hospitality operations into efficient, sustainable, and profitable businesses.

**Challenges we ran into**

# What Challenges I Encountered Developing AHAR

Developing AHAR, a food waste management application, presented several technical and implementation challenges that required creative problem-solving and persistence. Here are the main challenges I faced and how I overcame them.

## Technical Challenges

### 1. Authentication Integration
**Challenge:** Implementing secure user authentication was complex, especially with changing package dependencies.
- Initially used deprecated `@clerk/clerk-react` package which caused build failures
- Had to research and switch to compatible versions
- Required updating multiple import statements across the codebase

**Solution:** Downgraded to a working version (4.32.5) of the Clerk package and updated all imports consistently. This resolved the build errors and maintained authentication functionality.

### 2. Payment Gateway Implementation
**Challenge:** Integrating Razorpay payment gateway required careful handling of:
- Dynamic script loading for the payment SDK
- Proper error handling for payment success/failure
- Security considerations for API keys
- Cross-browser compatibility

**Solution:** Implemented a robust payment component with useEffect for script loading, comprehensive error handling, and secure key management through environment variables.

### 3. Build and Dependency Management
**Challenge:** Frequent build failures due to:
- Deprecated packages
- Version conflicts
- Node modules corruption
- PowerShell command execution issues in Windows environment

**Solution:** Systematically cleared node_modules, updated package.json with correct versions, and used proper command syntax for Windows PowerShell.

### 4. Logo Integration
**Challenge:** Adding the logo to the AHAR header while maintaining responsive design and proper styling.
- Needed to position logo alongside existing text
- Ensure it works across different screen sizes
- Maintain the existing design aesthetic

**Solution:** Modified the Layout component to use flexbox layout, added proper styling for the logo image, and ensured it integrates seamlessly with the existing UI.

### 5. Route Protection and User Experience
**Challenge:** Implementing authentication-based route protection without disrupting the user experience.
- Needed to redirect unauthenticated users to sign-in
- Maintain smooth navigation flow
- Handle authentication state properly

**Solution:** Used Clerk's SignedIn/SignedOut components to wrap routes, implemented proper redirects, and added user profile management through UserButton.

## Development Environment Challenges

### 6. Windows Development Environment
**Challenge:** Working with Windows PowerShell presented command syntax issues and path handling problems.
- Directory navigation commands failed with certain path formats
- Command chaining with && didn't work as expected

**Solution:** Used quoted paths and alternative command structures, learned Windows-specific npm and build tool behaviors.

### 7. Package Version Compatibility
**Challenge:** Keeping up with rapidly changing package versions and deprecation notices.
- Many packages get deprecated quickly
- Finding compatible versions for React 18 and Vite

**Solution:** Researched package documentation, checked npm registry for available versions, and tested builds iteratively.

## Learning Outcomes

These challenges taught me valuable lessons about:
- Staying updated with package ecosystems
- Proper error handling and debugging techniques
- Cross-platform development considerations
- The importance of version pinning and dependency management
- Building resilient applications that can handle external service integrations

Despite these challenges, each problem solved contributed to a more robust and feature-complete application. The experience significantly improved my problem-solving skills and understanding of modern web development practices.

Team **DevNinjas** -- [Krishnpal Vishwakarma](https://github.com/Krishna1129), [Arijeet Panchotia](https://github.com/Arijeet005), [Keshav Gehlot](https://github.com/keshavgehlot18), [Kapil Songare](https://github.com/kapil-singh18)

`2026-03-08`

---

### Protector
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/protector-98b4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/S2006-prog/Protector) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Health That matters just for 1 second

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Our system solves the critical problem of delayed health emergency detection by providing continuous Ai powered monitoring ,real time alerts, and centralized safety intelligence

Team **Creation 2.0** -- [Sayan Samanta](https://github.com/S2006-prog), [Sayan Patra](https://github.com/sayanpatra3097-art), [Debayan Das](https://github.com/Debayan-3110)

`2026-03-08`

---

### VOXGUARD
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/voxguard-df1c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://turbooovox.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co)

> A HEALTHBUDDY FOR SINGER PERFORMANCE

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square)

**The problem it solves**

SMART MIC is designed to make live concerts safer and more controlled for performers. During high-energy shows, singers often push their vocal limits without realizing the strain. SMART MIC monitors heart rate and SpO₂ in real time while analyzing pitch and volume to detect excessive vocal effort.

If a performer sings at very high pitch or volume for too long, or if physical stress increases beyond safe levels, the system provides an instant alert through the dashboard. This helps prevent vocal cord damage, breathlessness, and performance fatigue during long concerts.

For large stage performances, where adrenaline and crowd energy are high, artists may overexert themselves. SMART MIC acts as a silent health guardian, ensuring the singer stays within a safe vocal range while still delivering a powerful performance.

Sound engineers can also monitor the data backstage, helping them adjust sound levels or suggest short breaks when needed.

Unlike a regular microphone, SMART MIC supports both performance quality and artist safety, making live concerts smarter, safer, and more sustainable for professional singers.

**Challenges we ran into**

While building SMART MIC using Arduino Uno, MAX30100 and a dynamic microphone, a major issue appeared: audio noise and unstable sensor readings.

When the Arduino was powered via USB and simultaneously:
	•	Reading MAX3010 biometric data
	•	Sending data to Firebase
	•	Capturing microphone audio

There was:
	•	Low-frequency humming in the mic output
	•	Fluctuating SpO₂ and heart rate values
	•	Random spikes in sensor readings
	•	Inconsistent vocal strain detection

The issue happened because the analog microphone signal and digital sensor signals were sharing power and ground lines, causing interference and ground loop noise.

How It Was Solved
	1.	Power Stabilization – Added decoupling capacitors near the MAX3010 sensor.
	2.	Separate Grounding Layout – Reduced shared ground noise by careful wiring.
	3.	Shielded Audio Cable – Prevented EMI affecting the microphone signal.
	4.	Proper Wire Routing – Kept sensor wires away from audio lines.
	5.	Software Filtering – Applied smoothing algorithms before sending data to Firebase.

Result
	•	Clean audio signal
	•	Stable biometric readings
	•	Accurate real-time strain monitoring
	•	Reliable cloud data logging

When combining analog audio, biometric sensors, and cloud communication on Arduino, proper grounding, shielding, and filtering are essential to ensure accurate and noise-free performance.

**Gemini API**

The Problem We Are Solving with AI:

In live performances, raw sensor data is notoriously noisy. A singer hitting a powerful high note will naturally spike their vocal strain and heart rate. If a system only looks at hardcoded thresholds, it will constantly trigger false alarms ("crying wolf"), which ruins the performance and causes the crew to ignore actual emergencies.


Our Solution:  Gemini as the "AI Medical Supervisor"

We don't just trigger an alarm when a number goes high. Instead, we use Gemini 2.0 Flash as an intelligent, real-time supervisor to verify if an alert is a genuine medical emergency or just a normal part of the performance (or a sensor glitch).


How the Flow Works in Real-Time:

Trigger: The system continuously monitors the singer's Heart Rate, Blood Oxygen (SpO2), and Vocal Strain.
The Catch: If any metric breaches a critical threshold (e.g., vocal strain exceeds 0.58), the system catches it—but it doesn't panic yet.
The AI Hand-off: In a fraction of a second, the backend packages the exact current state of all three biometrics (HR, SpO2, Strain) and sends a structured prompt to the Gemini API.
The Analysis: We prompt Gemini to analyze the correlation between the data points.
The Verdict: Gemini responds instantly with a JSON payload containing:
A verdict (genuine, likely_false, or uncertain)
A risk level
A contextual explanation (e.g., "High vocal strain is present, but HR and SpO2 are completely normal. This is likely just safe, loud singing.")
An actionable recommendation for the crew.
Why Gemini? (The "Wow" Factor for the Judge)
Reasoning over Correlation: Gemini understands human physiology logic. It knows that a SpO2 drop combined with high vocal strain is a red alert, but high vocal strain with a normal heart rate is just a singer doing their job. Hardcoded if/else statements cannot do this reliably.
Speed: By using the Gemini 2.0 Flash model, the analysis happens in milliseconds. The crew gets an AI-verified medical context instantly, without interrupting the show for false alarms.
Actionable Output: Gemini doesn't just say "Warning." It gives the sound engineer or tour manager plain-English instructions on whether to cut the mic, bring water, or let the show go on.

Team **TEAM TURBOOO** -- [Srudyuti Dey](https://github.com/srudyuti16), [SUTAVRA MITRA](https://github.com/sutavrario), [Subhadeep Dolai](https://github.com/subhadeep0111)

`2026-02-28`

---

### MyHealthMate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resqverse-0c72) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AmishKumarJha/My_Health_Mate) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://my-health-mate-cqzg-45pupanlc-amishkumarjhas-projects.vercel.app?_vercel_share=HbAkFqIupxNVCDdSPJtWi4KX0wMSWefw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vegCspRi2ss?si=2rqCpUqgDDnl8q6w) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co)

> AI-Powered Preventive Healthcare Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

MyHealthMate is an AI-powered preventive healthcare platform that analyzes user health data to predict potential risks and provide personalized recommendations. It transforms medical metrics into simple insights, health scores, and smart alerts, helping users monitor and improve their well-being proactively.

Built using Next.js, FastAPI, and machine learning, MyHealthMate focuses on early detection and smarter lifestyle decisions.

**Challenges we ran into**

1 - Managing Large ML Model Files

The trained machine learning model file (`diet_model.pkl`) was approximately 787MB, which exceeded GitHub’s 100MB file size limit.  
We resolved this by:

- Removing the model file from Git history
- Using `.gitignore` to prevent tracking large model files
- Planning to host the model externally for production deployment

This helped me understand Git internals and best practices for handling large files.



2-  Git Branch & Merge Conflicts

While pushing the project, I encountered:
- Branch mismatch issues (`master` vs `main`)
- Merge conflicts in `README.md`
- Remote rejection due to unrelated histories

We resolved these by:

- Renaming branches properly
- Cleaning Git history
- Using `git filter-branch` to remove large files
- Force pushing after properly cleaning the repository

This improved my understanding of advanced Git workflows.

Key Learnings

- Proper Git repository management
- Handling large ML models in production
- Full-stack project structuring
- Backend–Frontend communication
- Debugging real-world deployment issues

Team **Floppy_Disk** -- [Prachi Jha](https://github.com/prachiijha), [Amish Kumar Jha](https://github.com/AmishKumarJha), [Barsha Panda](https://github.com/Barshapandaa), [Abhishek Seth](https://github.com/Abhishek-x23)

`2026-02-28`

---

### AI-Fitness-Trainer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aifitnesstrainer-cd1d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Kakumanu-Harshitha/Hack-SRM) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/S0YPtG0QnZ0?si=T4c9mTbDU9yYPfsU) [![Built at](https://img.shields.io/badge/Built%20at-HackSRM%207.0-0052CC?style=flat-square)](https://hack-srm26.devfolio.co)

> Your Personal AI Coach That Never Misses a Rep.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![random forest](https://img.shields.io/badge/random%20forest-333333?style=flat-square)

**The problem it solves**

The Problem It Solves:

Most people working out at home struggle with two major issues:

No real-time form correction, which increases injury risk.

Manual workout tracking, which is inaccurate and inconsistent.

Without a trainer present, users often perform exercises with incorrect posture, fail to count reps properly, and lack motivation or performance insights.

How AI Fitness Trainer Solves It

AI Fitness Trainer uses real-time computer vision and pose estimation to transform any webcam into a smart personal coach.

 Automatic Rep Counting – Detects complete movement cycles for exercises like squats and push-ups.

 Posture & Form Analysis – Tracks body landmarks and provides corrective feedback instantly.

 Smart Static Pose Timer – Automatically pauses or resets when form breaks during planks or yoga poses.

 Workout Analytics – Tracks performance, recovery rate, and joint stress.

 Gamification & Leaderboards – Keeps users motivated with XP, levels, and competition.

 Voice Coaching – Delivers real-time motivational and corrective guidance.

Impact

AI Fitness Trainer makes home workouts:

Safer through posture monitoring

Smarter with AI-driven tracking

More engaging through gamification

Data-driven with performance analytics

It brings the experience of a personal trainer into any room — powered entirely by AI.

**Challenges we ran into**

1. Real-Time Pose Accuracy & False Rep Counting

One of the biggest challenges was handling inaccurate or noisy landmark detection from MediaPipe. Small variations in joint angles sometimes caused false rep counts or missed reps.

How I solved it:

Implemented angle smoothing using moving averages.

Built a custom state machine with strict transition thresholds (START → DOWN → UP).

Added minimum hold durations to validate completed reps.

2. Handling Static Pose Break Detection

Tracking exercises like planks was tricky because minor posture shifts would reset the timer too aggressively.

How I solved it:

Introduced tolerance thresholds for acceptable angle variation.

Added a grace period before resetting the timer.

Used posture confidence scoring instead of binary detection.

3. WebSocket Real-Time Communication

Implementing live chat and notifications required stable WebSocket connections. Handling disconnects and reconnections was challenging.

How I solved it:

Implemented automatic reconnection logic on the frontend.

Added heartbeat/ping checks on the backend.

Used proper async handling with FastAPI WebSockets.

4. JWT Authentication & Protected Routes

Ensuring secure authentication across API routes and WebSockets required careful token validation.

How I solved it:

Created middleware for JWT verification.

Centralized API calls with automatic token injection.

Handled token expiration with proper logout flow.

5.Performance Optimization

Running pose detection at 30+ FPS while updating UI and state caused performance bottlenecks.

How I solved it:

Optimized re-renders using React memoization.

Moved heavy calculations outside render cycles.

Reduced unnecessary state updates.

**Grand Prize**

AI Fitness Trainer represents a complete, production-ready, end-to-end intelligent system that combines computer vision, real-time analytics, scalable backend architecture, and user-centric design into one impactful solution.

This project goes beyond a simple demo by delivering:

Real-time AI pose detection using computer vision for accurate movement tracking.

Custom-built state machines for intelligent rep counting and posture validation.

Full-stack architecture (React + FastAPI + PostgreSQL) with JWT authentication and WebSocket-based real-time features.

Gamification & performance analytics including XP, leaderboards, recovery rate, and joint stress monitoring.

Scalable backend infrastructure designed for real-world deployment.

The project solves a real and widespread problem — lack of accessible, real-time fitness coaching — by transforming any webcam into an AI-powered personal trainer.

It demonstrates:

Strong technical depth (AI + full-stack engineering)

Practical real-world usability

Scalability and production readiness

Clear user impact in health and wellness

AI Fitness Trainer is not just a prototype — it is a comprehensive intelligent platform designed to redefine how people train at home.

Team **nomotix** -- Navya Kedhari, Kakumanu Harshitha, Gunda Rahul Gupta, Mohnish Videla

`2026-02-26`

---

### Abhiraksha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/abhiraksha-2874) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kabir-fx/Abhiraksha) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1ioWrvoDRDG01G0VqprIiRFxOquSOhfGd/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co)

> Insurance Copilot for Indian Healthcare Facilities

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

**Abhiraksha**
Insurance Intelligence Copilot for Indian Hospitals

**Insight and Problem Origin**
Before building Abhiraksha, I worked in selling Hospital Management Software to Tier 2 and Tier 3 hospitals across South India. During on ground visits to independent hospitals and medical institutions, I observed how insurance claims are processed in real operational settings.

Most smaller hospitals use basic HMS systems but rely heavily on manual documentation, email chains, and WhatsApp coordination for insurance claims. Billing staff, often without formal insurance training, are required to interpret complex, English heavy policy documents and respond reactively to TPA queries.

Claims are frequently delayed due to documentation gaps, policy misinterpretation, and the absence of structured insurance validation within existing systems.

This firsthand exposure led to a clear realization. Hospitals in India do not lack software. They lack an intelligent insurance operations layer embedded into their workflow.

Abhiraksha is built from that insight.

**Problem Statement**
Insurance contributes approximately 65 percent of revenue for many Indian hospitals. However, insurance claim processing remains fragmented and inefficient.

For a hospital processing 100 claims per month, the average claim value is ₹80,000, resulting in monthly insurance revenue of ₹80,00,000. With an average deduction rate of 6 percent, hospitals lose approximately ₹4,80,000 per month. Around 70 percent of claims are delayed beyond 10 days and the working capital cycle averages 45 days. Typically, three staff members manage insurance operations.

Hospitals operate with thin margins and even a 2 to 3 percent deduction error significantly impacts profitability and liquidity. There is no structured pre submission validation layer in Indian healthcare insurance processing.

**Proposed Solution**

Abhiraksha is an Insurance Intelligence Plugin that integrates directly into existing Hospital Management Systems.

It functions as a pre submission validation engine that extracts structured data from discharge summaries and bills, applies insurer specific policy rules deterministically, calculates expected payouts and potential deductions, flags missing documents before submission, predicts common TPA queries, and provides CFO level dashboards for financial visibility.

The system transforms claim processing from reactive to predictive.

**Tech**

The architecture follows the flow HMS to Abhiraksha Plugin to Insurer or TPA.

The OCR module extracts structured data from unstructured bills and discharge summaries. The deterministic policy rule engine enforces room rent caps, sub limits, consumable exclusions, and documentation requirements. The deduction simulation engine calculates expected payout with transparent breakdown. The query risk detection module flags potential rejection triggers before submission.

All financial calculations are rule based and auditable to ensure trust and adoption.

**Innovation**

It introduces a structured insurance copilot layer embedded into hospital workflows. It combines AI based document extraction with deterministic financial policy enforcement and pre submission risk validation.

This infrastructure layer does not currently exist in the Indian healthcare ecosystem.

**Measurable Impact**

For a hospital with 100 claims per month, monthly revenue is ₹80,00,000 and average deduction at 6 percent results in ₹4,80,000 in losses.

If Abhiraksha reduces deductions by 25 percent, recovered revenue is ₹1,20,000 per month. Operational efficiency gain is estimated at ₹27,000 per month. Total measurable benefit is ₹1,47,000 per month.

With pricing at ₹200 per claim, cost would be ₹20,000 per month. This results in approximately 7 times return on investment with payback in less than one month.

Market Opportunity

India has approximately 20,000 hospitals with more than 30 beds. An estimated 8,000 hospitals process more than 30 insurance claims per month.


Go To Market Strategy

Phase 1 involves direct pilots with mid sized hospitals to measure deduction reduction and DSO improvement.

Phase 2 involves HMS vendor integrations where Abhiraksha is embedded as an Insurance Intelligence Module with revenue share.

Phase 3 involves deployment across regional hospital chains with centralized dashboards across branches.

Team **Owl Syndicate** -- [Saujas R](https://github.com/saujasrs), [Shivam Vats](https://github.com/kabir-fx)

`2026-02-15`

---

### DocAndAi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/docandai-bd7c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajni12071985-debug/DocAndAi) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/K47swMvt1tY?si=rxvbOO2hyYcgAVxD) [![Built at](https://img.shields.io/badge/Built%20at-HACK%20THE%20THRONE-0052CC?style=flat-square)](https://hack-the-throne.devfolio.co)

> Ai based patient management system

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Doc & AI helps people manage hospital visits more easily and safely.
Users can quickly check doctor availability, understand their health concern using AI guidance, and book OPD, pre-booking, or video consultations without standing in long queues.
The system reduces waiting time, avoids unnecessary hospital visits, and lowers crowding, making healthcare access faster, safer, and less stressful.
AI acts only as a support assistant, helping patients choose the right doctor while final decisions remain with medical professionals.

Team **SVIETIAN** -- [Prashant Sinha](https://github.com/prashantsinha), [Pragati Kesherwani](https://github.com/rajni12071985-debug), [sahiba sheikh](https://github.com/sahiba-sheikh), [Sudipta Chatterjee](https://github.com/sudiptachatterjee)

`2026-02-08`

---

### CareDetect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/caredetect-506e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://trialbreastcancerwebsite.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/L2NnE_vjGZg) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co)

> Early breast health screening using 3D and AI.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Blender](https://img.shields.io/badge/Blender-333333?style=flat-square) ![AR/VR](https://img.shields.io/badge/AR/VR-333333?style=flat-square) ![Keras CNN](https://img.shields.io/badge/Keras%20CNN-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

1 out of 8 women are at a certain risk of breast cancer, but detection at an early stage in India is often not possible due to the expensive nature of a mammography test, dependence on clinics, and geographical challenges such as rural and semi-urban scenarios. **CareDetect **provides an opportunity for a risk assessment test to be conducted at a very early stage, at a person’s own place, which is cost-effective, convenient, and easy to use repeatedly. The biochemical sweat test, which is cost-effective, is analyzed by AI on the device. A fully digital solution uses symptoms, menstrual history, family history, lifestyle, and an interactive 3D model of the breast to better understand the problem, generate a personalized risk score with clear next steps, and provide optional user feedback to continuously improve the model over time.

**Challenges we ran into**

One major challenge was working with the 3D renderable model in an AR/VR environment. Initially, the model was heavy and caused lag, slow loading, and interaction issues, which affected the overall user experience.

To overcome this, I optimized the 3D assets by reducing mesh complexity and improving rendering efficiency, while still maintaining visual clarity. I also tested the model repeatedly to ensure smooth interaction across devices.

Another challenge was making the 3D visualization easy to understand rather than overwhelming. This was solved by simplifying the structure and designing the interaction flow in a more intuitive way, so users can explore the model without confusion.

**Emerging Technologies**

CareDetect comes under Emerging Technologies because it is an AR/VR-based application that uses an interactive 3D renderable model to visually understand and analyze breast cancer–related patterns. The use of immersive 3D visualization instead of traditional flat representations makes the approach modern, intuitive, and aligned with emerging AR/VR technologies.

Team **CodeDivas** -- [Aadhya Verma](https://github.com/aadhyaavermaa), [Archi Aggarwal](https://github.com/archiagg26), [Anushka Yadav](https://github.com/anushkayadav0901)

`2026-02-07`

---

### CareCompanion
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carecompanion-369f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHAjHB4SxI/5HLowWuFeC27Bmg8M-sf0g/view?utm_content=DAHAjHB4SxI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h41bcb5bf8e) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/b2sKQzxRG6U?si=wmGCVmd2Xy8sG659) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co)

> AI-Powered Preventive Healthcare & Caregiver

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🔍 **The Problem**

Healthcare today fails in one crucial area: daily consistency.

•⁠  ⁠Medicines are forgotten
•⁠  ⁠Health data is scattered
•⁠  ⁠Caregivers are informed too late
•⁠  ⁠Preventable conditions become emergencies

For elders, this is dangerous.
For families, this is stressful.
And for the healthcare system, this is costly.

At the same time, menstrual health, an important indicator of overall well-being, is still ignored or treated as a private inconvenience — especially in India.

💡 **Our Solution – CareCompanion**

CareCompanion is a smart healthcare companion designed for every individual with special focus on elders and women’s health.

It helps users:
•⁠  ⁠Take medicines on time
•⁠  ⁠Track health regularly
•⁠  ⁠Stay connected with caregivers and doctors

And for women, it provides a dedicated, optional menstrual health tracker
because periods are not separate from health, they are part of it.

**Challenges we ran into**

* **Understanding the problem statement**
  Since the problem statement was provided by the organizers, the key challenge was understanding its intent clearly and identifying areas where meaningful innovation could be added without deviating from the core objective.

* **Communicating feasibility without development**
  As this was an ideathon and not a development-based hackathon, the challenge was to present the idea in a way that felt realistic and implementable. This was addressed by creating detailed workflows and feature breakdowns.

* **Designing for multiple user groups**
  Aligning the solution to serve elderly individuals, caregivers, and women—while keeping the experience simple—required careful feature prioritization and user flow planning.

* **Deciding premium vs essential features**
  A key challenge was ensuring that premium features did not restrict access to critical healthcare needs. All core health and safety features were kept free, with premium limited to advanced insights and personalization.

* **Simplifying a complex healthcare idea**
  Healthcare systems can be complex, and the challenge was to present the solution clearly within limited time. This was managed by structuring the idea into clear, modular components.

**Beginner's track - Your first hack starts here!**

CareCompanion fits perfectly into the Hackathon Track as it directly addresses the organiser-defined problem of improving everyday healthcare accessibility and adherence. The project focuses on helping individuals—especially elders—stay consistent with medications through smart reminders, while also providing a dedicated menstrual cycle tracking feature for women, an often ignored yet critical health aspect in India. By combining preventive care, timely alerts, and simple health tracking in one platform, CareCompanion aligns strongly with the hackathon’s goal of building impactful, tech-driven solutions for real-world health challenges.

Team **Fusion Coders** -- [Riddhika Sachdeva](https://github.com/Riddhika-Sacheva), [Mannat Wadhwa](https://github.com/mannatwadhwa1009-ship-it), [Prabhjot Singh](https://github.com/explore), [Hemank Aggarwal](https://github.com/hemankagg-hash)

`2026-02-07`

---

### PharmAssist
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pharmassist-194c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kshitiz510/hacktu-pharmassist) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> A million dollar R&D team

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

### The Problem It Solves

Access to affordable medicines remains a major challenge in underserved and remote regions, not due to lack of medical knowledge, but because **generic pharmaceutical companies struggle to identify which medicines to produce and scale efficiently**. High uncertainty around market demand, patent clarity, regulatory effort, and clinical feasibility discourages manufacturers from expanding into low-margin but high-impact drugs. As a result, many essential medicines remain unavailable or expensive where they are needed most.

### How This Project Helps

This platform enables **generic pharma companies to confidently expand their product portfolios** by automating early-stage research and decision-making. It replaces months of fragmented manual analysis with an AI-driven, multi-agent system that evaluates market demand, patent freedom, clinical activity, and supply feasibility in days.

By lowering the cost and risk of launching new generics, manufacturers are encouraged to enter underserved therapeutic areas—leading to **greater medicine availability, faster market entry, and lower prices for patients**. Ultimately, this improves healthcare access by ensuring essential, affordable medicines reach populations that are currently underserved, aligning directly with the goal of equitable and universal healthcare.

**Challenges we ran into**

### Challenges We Ran Into

One of the primary challenges was **integrating heterogeneous data sources with varying structure, reliability, and update frequency**. Market data, patent records, clinical trial information, and trade datasets all use different schemas and levels of granularity. Early versions of the system produced inconsistent insights because agents were operating on partially overlapping or outdated information.

To resolve this, we introduced a **standardized intermediate representation** that every agent had to conform to before passing data to the orchestrator. This ensured consistency, traceability, and easier debugging across the agent pipeline.

Another major hurdle was **balancing automation with explainability**. Fully automated outputs initially lacked transparency, which is critical in pharmaceutical decision-making. We addressed this by adding **confidence scoring and source attribution** to each agent’s output, allowing users to understand *why* a recommendation was made and what data supported it.

Finally, coordinating multiple agents without redundant computation was challenging. This was mitigated by implementing **task-level orchestration and caching**, which reduced unnecessary agent re-runs and improved overall system efficiency.

**MongoDB Atlas**

### Use of MongoDB Atlas

Our project uses a **MongoDB Atlas cluster as the central database layer** for all data storage and coordination needs. Outputs generated by each AI agent, such as market insights, patent evaluations, clinical signals, trade analysis, and confidence scores are stored as **JSON documents** in Atlas collections.

The flexible document-based schema allows us to efficiently manage **heterogeneous and evolving data** coming from multiple agents without rigid constraints. The orchestrator agent queries the Atlas cluster to aggregate these stored outputs and generate structured, explainable reports for decision-making.

By using a managed MongoDB Atlas cluster, we ensure **scalability, reliability, and fast access** to agent outputs and intermediate analysis states, enabling smooth multi-agent orchestration and future system expansion.

Team **PharmAssist** -- [Kshitiz Jain](https://github.com/kshitiz510), [Guransh Chugh](https://github.com/guranshchugh-9), [Vidyt Bhudolia](https://github.com/VidytBhudolia)

`2026-02-08`

---

### LifePulse-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifepulseai-8161) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryan-26-prog/LifePulse_AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1KgPW4Ull83XREt5tGIf17q8lJrhcpn1H/view?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> Community Health and Risk Management System

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

Community Health & City Risk Intelligence Platform

Transforming public health through AI-powered community monitoring and intelligent risk
assessment. Connecting citizens, NGOs, and city officials to prevent health crises before
they emerge.

**Challenges we ran into**

i faced challenges regarding timin issue

Team **Bruhgrammers** -- [Tarun Tarun](https://github.com/Txeim), [Aryan Dhiman](https://github.com/aryan-26-prog), [Mayank Kumar](https://github.com/mayankkumarlinghe-jpg)

`2026-02-08`

---

### PharmaInnovate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pharmainnovate-37f2) [![Built at](https://img.shields.io/badge/Built%20at-KnowCode%203.0-0052CC?style=flat-square)](https://knowcode-3.devfolio.co)

> Bimaari Nayi, Drugs Wahi.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![crewai](https://img.shields.io/badge/crewai-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square)

**The problem it solves**

# PharmaInnovate AI – Technical Overview

- **Modular Platform**: Pharmaceutical research and drug repositioning system designed for evidence-based analysis.
- **Unified Data Integration**: Aggregates biomedical, regulatory, scientific, and commercial data sources into a single analytical workflow.
- **Multi-Agent Architecture**: Central coordination layer decomposes complex queries into well-defined subtasks.
- **Parallel Execution**: Domain-specific agents run concurrently across clinical trials, regulatory intelligence, patent analysis, scientific literature, market data, and chemical evaluation.
- **Evidence Synthesis**: Normalizes, cross-validates, and correlates multi-source outputs with confidence assessment.
- **Repositioning Insights**: Identifies potential alternative drug indications using structured analytical reasoning.
- **Scalable Backend**: Asynchronous Python stack based on FastAPI and LangGraph ensures low latency and deterministic workflow control.
- **Interactive Frontend**: Real-time dashboard for visualization, exploration, and report generation.
- **Structured Outputs**: Generates publication-ready exports to support downstream analysis and decision-making.
- **Operational Efficiency**: Reduces manual research effort while improving traceability, reproducibility, and analytical reliability for research, clinical, and early-stage innovation environments.

**Challenges we ran into**

# Challenges faced

1. **API Usage Limits**  
   Manage and monitor API usage limits to ensure system reliability, prevent service interruptions, and maintain compliance with provider constraints.

2. **AI Agent Coordination and Parallel Execution**  
   Ensure that all AI agents operate cohesively, with proper orchestration to enable parallel execution while maintaining consistency, data integrity, and inter-agent communication.

3. **Transformation of JSON Data into Human-Readable Language**  
   Convert structured JSON outputs into clear, natural language representations that are easily understandable by end users without losing semantic accuracy.

4. **Adherence to Time Constraints**  
   Design and optimize workflows to guarantee that all processes execute within defined time limits, meeting performance and delivery requirements.

Team **Meow Meow** -- [Tisha Patel](https://github.com/tishapatel2109), [Pushya Singh](https://github.com/Push900?tab=overview&from=2025-04-01&to=2025-04-03), [Siddhant Shukla](https://github.com/Siddhantshukla1657), [Raunak Kumar Gupta](https://github.com/Raunakg2005)

`2026-01-25`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
