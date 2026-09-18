# Social Impact and Education

![Projects](https://img.shields.io/badge/Projects-87-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### KnowGap
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/knowgap-bce4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ankitsri2005) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://knowgap-1-0bfh.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-10-FF6B6B?style=flat-square)

> Know What Students Know

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

Traditional assessment systems evaluate students only through final scores, making it difficult to identify why a student performed poorly or whether a correct answer was based on actual understanding or random guessing. Teachers often receive only marks, without insights into misconceptions, confidence levels, response behavior, or hidden knowledge gaps.
KnowGap solves this problem by providing AI-powered learning gap forensics. The platform goes beyond marks and analyzes:

Hidden Learning Gaps – Detects students who answer correctly but are actually guessing.
Misconceptions Detection – Identifies students who are confidently giving wrong answers, revealing deep conceptual misunderstandings.
Response Time Analysis – Uses answer timing to distinguish between mastery, low confidence, impulsive guessing, and confusion.
AI Confusion Detection – Automatically identifies weak topics after every assessment.
Personalized Remediation – Suggests targeted improvement areas and enables re-tests to measure gap closure.
Peer Comparison Insights – Shows how a student's topic-wise performance compares with class averages.
Parent Engagement – Generates AI-powered performance reports for parents.
Teacher Analytics Dashboard – Helps educators make data-driven decisions instead of relying solely on marks.
By combining Artificial Intelligence, Machine Learning, confidence-based answer tagging, and learning analytics, KnowGap transforms traditional assessments into an intelligent diagnostic system that helps teachers identify, understand, and close learning gaps more effectively.

**Challenges we ran into**

Building KnowGap involved several technical and research challenges.

1. Distinguishing Knowledge from Guessing

Traditional assessment systems only store whether an answer is correct or incorrect. Designing a system that could identify hidden learning gaps required combining answer correctness with confidence levels and response times. We developed a custom confidence-based tagging mechanism to classify students into meaningful learning profiles.

2. Collecting Meaningful Educational Data

Creating reliable learning analytics required designing a data structure that could capture quiz scores, confidence ratings, response latency, topic-wise performance, and remediation results while maintaining consistency across assessments.

3. AI-Based Gap Detection Logic

Developing algorithms that accurately identify misconceptions and weak concepts was challenging. We experimented with different approaches before combining classification, clustering, and performance prediction techniques to generate actionable insights.

4. Response Time Analysis

Students answer questions at different speeds due to multiple factors. Designing a system that could differentiate between mastery, hesitation, guessing, and confusion without generating misleading results required extensive testing and calibration.

5. Full-Stack Integration

Integrating the frontend, backend, database, authentication system, and AI analytics modules into a single platform created synchronization and data-flow challenges. These were resolved through modular architecture and API-based communication.

6. Deployment and Scalability

Deploying the project on a cloud platform while ensuring secure user authentication, database persistence, and smooth performance required multiple iterations and optimization efforts.

How We Overcame Them

We addressed these challenges through continuous testing, iterative model improvements, structured database design, modular development practices, and frequent validation of results using real-world educational scenarios. The final system successfully combines AI-driven analytics with an intuitive user experience to help educators identify and close learning gaps effectively.

Team **THE BUG STOPS HERE** -- [Achintya Jyoti](https://github.com/achintya0308), [Ankit srivastava](https://github.com/Ankitsri2005), [NAVONIL SAHA](https://github.com/navonilsaha123), [Shambhavi Kumari](https://github.com/shambhavi151023)

`2026-05-30`

---

### Learning Twin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/paper-learn-twin-d83a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://learningt.freebuff.app/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> An AI That Learns How You Learn

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square)

**The problem it solves**

Students have too much educational content but no personalized system to manage their learning. They often don't know what to study first, which topics they are weak in, what they have forgotten, whether they are actually exam-ready, or which resources are best for their needs. Existing tools usually provide generic explanations, notes, quizzes, or study plans but don't continuously understand the student's actual syllabus, knowledge gaps, mistakes, progress, and exam performance. Learning Twin AI solves this by creating a continuously updated learning profile that understands where the student is, identifies what they need next, and guides them toward exam readiness.

**Challenges we ran into**

One of our biggest challenges was turning unstructured student data, such as uploaded or pasted syllabi and notes, into reliable structured information that the AI could actually use. We also had to balance RAG accuracy and response quality, especially when generating answers from students' own notes. Another challenge was connecting multiple AI features, including the Learning Twin, Knowledge Graph, Exam Simulator, Smart Resources, and JARVIS, into one consistent learning workflow rather than making them feel like separate tools. Finally, we had to work within limited development time and API/resource constraints while making the application responsive, reliable, and easy for students to use.

Team **Mishti Minds** -- [Debraj Bhattacharjee](https://github.com/Debraj200534), [BIDISHA DAS](https://github.com/BidishaDas2006), [Dibyendu Chatterjee](https://github.com/dibyendu-coder), [DIBYANGANA BISWAS](https://github.com/dibyanganaaa)

`2026-08-29`

---

### MYTHOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sentinel-1228) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-moymlec3kdj0s0p9.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Built for the student figuring it out alone.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square)

**The problem it solves**

People spend a lot of time fetching out product ideas, do marketing, make a seo compatible website and add products to it!! so what i did was i created a pipeline where you hit discover trend button and then it finds out the top selling and trending products and shows you with their suppliers ( cj-dropshipping ) and then you can hit create website button and it will create a complete website with a 9 pharse pipline - 🗂️ PHASE 0 — Foundation & Decision Making
What happens:

all the info that is taken from the first claude hit when we use discover idea goes to claude with a prompt
Claude generates your Project Blueprint — a single document that every future phase references
Decisions locked in: tech stack, color palette, brand name, payment providers, hosting

Output: blueprint.md — your store's constitution

🗂️ PHASE 1 — Tech Stack Setup
What happens:

Claude gives you exact terminal commands to scaffold the project
Framework: Next.js (React, SEO-friendly, fast)
Database: Supabase (free tier, Postgres, auth built-in)
Styling: Tailwind CSS
Hosting: Vercel (free, auto-deploy from GitHub)

Output: Folder structure, config files, environment variable template

🗂️ PHASE 2 — Database Schema
What happens:

Claude designs all your database tables
Products, variants, inventory, orders, customers, cart, coupons, reviews
Supabase SQL scripts ready to paste and run

Output: Complete DB schema + seed data (dummy products to start)

🗂️ PHASE 3 — Frontend Pages
Claude builds each page in a sub-session:
Sub-phasePage3AHomepage (hero, featured products, trust section)3BProduct listing / collection page3CSingle product page (the full dropshipping page from before)3DCart + mini-cart drawer3ECheckout page3FOrder confirmation page3GUser account + order history
Output: Full Next.js page components, mobile-responsive

🗂️ PHASE 4 — Backend / API Routes
What happens:

Claude writes all server-side logic
Add to cart, update cart, place order, fetch products
Inventory checks, coupon validation, order status updates

Output: Next.js API routes + Supabase queries

🗂️ PHASE 5 — Authentication
What happens:

which ever auth is available, i have given my clerk keys in .env
Guest checkout flow
Protected routes (account page, order history)

Output: Auth context, login/signup pages, session handling

🗂️ PHASE 6 — Payment Integration
On the main mythos dashboard have a option to connect stripe account. now every time a new dropshipping store is created the stripe info will be used to setup checkout

🗂️ PHASE 7 — Supplier / Product Sourcing Integration
using the links on CJ dropshipping that claude gives in discover idea step we import the product to store

🗂️ PHASE 8 — Admin Dashboard
all the business info will be seen on the main mythos dashboard

🗂️ PHASE 9 — Email System
What happens:

Resend or Nodemailer integration (free tiers available)
Order confirmation email
Shipping update email
Abandoned cart recovery email (triggered after 1 hour)
Welcome email on signup

Output: Email templates + trigger logic   

And then we can link stripe payments and we are done, the website is live ready to sell!! and it would have a autonomous mode where if a business doesn't get sale within 3 days or is not profitable within 7 days the idea gets dropped agent takes learning improves itself and then makes a new business and once a business is profitable it assigns it to a subagent and runs and while the main agent makes another new business so we have multiple source of earnings!! PRICING - $10 to run one time workflow, and to run autonomous flow it would cost $10 per cycle + 5% profit share

**Challenges we ran into**

I first started with a Saas project and then shifted to MYTHOS, and it was working pretty good but then a week before deadline al my code got wiped out and now i am forced to explain my idea in words. it was a technical fault with locus please take that it account. the live url that u see is a old completely different project that has no link with my main project!

[ansh surana](https://github.com/Anshsurana123)

`2026-05-10`

---

### Hey Tappr
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tappr-d42d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shrit1401/tappr-ptp) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SVwo1mZt0vE) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Interface For Millions of Elders

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Android](https://img.shields.io/badge/Android-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![react-native](https://img.shields.io/badge/react--native-333333?style=flat-square) ![accessibility](https://img.shields.io/badge/accessibility-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square) ![Convex](https://img.shields.io/badge/Convex-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square)

**How Did You Use Claude?**

Claude is the reasoning core of the product, not a bolt-on feature. It powers:

- The voice conversation loop,  every user turn is reasoned about by Claude Opus before a response is spoken back
- The autonomous phone-control agent,  Claude picks and sequences the tool calls (tap, scroll, type, point, draw) needed to complete a task on the user's behalf, using an indexed description of the current screen
- Vision/UI understanding, Claude interprets accessibility-tree snapshots and screenshots to decide what's on screen and where to point

**What is the problem your project solves?**

Smartphones are hard for people who didn't grow up with them, especially older users. When they get stuck ("how do I book a Cab?", "where's the Settings App?"), they either give up or have to call someone. We can change that, LLMs are way powerful than ever before, we have to figure out the way we can help older generation with these new technologies.

**What is the deployed URL for this project?**

https://tappr-ptp-page.vercel.app/

**How you are solving it?**

Hey Tappr is an AI Buddy which lives on your phone. Tappr is a phone assistant that draws on your screen. Ask "where's WhatsApp?" and it circles the icon and tells you — then asks whether to guide you step by step or just do it for you.

It notices when you're stuck from real signals (going back in loops, tapping dead buttons) and offers help before you ask, while staying completely silent during films, books and calls. It also warns about the scams aimed at older people — OTP requests, remote-access installs — without ever crying wolf on genuine bank messages.

****Disclosure of prior work**** 
we have been working on mobile use agents for past 2 weeks, and have used the architecture to build the agents, rest proactive agents, widgets, proactive brain (markdown crawling) and making agents accessible just for elders in 5 hours

Team **Claude's Plan** -- Saumya Patel, Koppala Rishi Kanth, [Shrit Shrivastava](https://github.com/shrit1401)

`2026-08-08`

---

### SafeRAG
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saferag-7d06) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mouli-tech2025/Hexa_RAG.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/4gfuKnc5zMA?si=p_fwBVRVOvztEjKy) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Local RAG for learning: less weight, less memory

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Docling](https://img.shields.io/badge/Docling-333333?style=flat-square) ![Qwen3](https://img.shields.io/badge/Qwen3-333333?style=flat-square) ![Actian VectorAI DB](https://img.shields.io/badge/Actian%20VectorAI%20DB-333333?style=flat-square) ![RoBERTA-base-SQuAD2](https://img.shields.io/badge/RoBERTA--base--SQuAD2-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

When an aircraft lands with an active fault, maintenance engineers must manually cross-reference FAA manuals, historical incident reports, and inspection images across disconnected PDFs and legacy systems — often in hangars with no reliable Wi-Fi, and under ITAR/data-sovereignty rules that forbid sending sensitive maintenance data to the cloud. This manual context-switching eats into tight turnaround windows, and under FAA/EASA Part 145, any AI output that can't be traced back to real evidence is unusable.

Who Can Use It & How

Built for aircraft maintenance engineers, MRO technicians, and airline maintenance crews — especially operators who can't afford, or aren't allowed, cloud-dependent proprietary tools.

How to use it:

Start an investigation
Enter a fault code and a short description
Optionally upload an inspection image
Receive a full Investigation Summary in seconds — evidence, hypothesis, recommendation, and confidence rating — all traceable, all offline

How It Solves the Existing Problem

Instead of an engineer manually flipping through FAA manuals, old incident logs, and inspection photo archives one by one, AeroSage AI automates that correlation end-to-end:

Ingestion (offline): Real, public FAA AMT Handbook excerpts and Airworthiness Directives, plus historical incident reports, are embedded with Qwen3-Embedding; inspection images are embedded with DINOv2.
Storage: Stored in Actian VectorAI using named vectors (per modality) and metadata filters (Aircraft, Engine, ATA Chapter).
Retrieval: The query is filtered by metadata, searched across text + image named vectors in parallel, and fused server-side via Reciprocal Rank Fusion (RRF) — no custom fusion logic in the app layer.
Synthesis: A small local LLM, Qwen3-4B-Instruct (via Ollama), summarizes only the retrieved evidence — it never invents a procedure or diagnosis.
Output: An Evidence Used panel, a root cause hypothesis, a recommended action, and a Retrieval Confidence (High/Medium/Low) rating based on the number of corroborating sources — never a fabricated percentage — with every claim linked to a clickable citation.

Why size matters: Most RAG deployments assume a connection to a large hosted model. AeroSage AI runs its entire inference stack on a ~1.1-billion-parameter local model — a fraction the size of typical cloud-scale LLMs, which often run 100B+ parameters — small enough to run on local/edge hardware with zero data leaving the site. Cerebras is used only during setup, to generate non-safety-critical synthetic supporting content — never at inference time, and never for procedural content.

Net result: a slow, error-prone, multi-system manual search becomes a single evidence-first workflow that's faster, fully auditable, and safe for regulated, offline environments.

**Challenges we ran into**

1. Fusing text and image retrieval without custom logic
Correlating FAA documents, incident reports, and inspection images without writing brittle manual scoring code was a challenge. We solved this using Actian VectorAI's server-side RRF and named vectors, letting the database handle multimodal fusion instead of the app layer.

2. Preventing the LLM from inventing details
In a regulated maintenance context, a confident but unverified answer is worse than none. We fixed this with strict low-temperature RAG prompting and a hard fallback: if evidence is weak or missing, the system outputs "No supporting evidence found" instead of guessing.

3. Slow local document ingestion
Since everything runs offline for data-sovereignty compliance, embedding FAA manuals and incident reports through Qwen3-Embedding on local hardware was initially slow, making iteration painful. We fixed this by batching ingestion and caching embeddings so we didn't re-embed the same documents on every test run.

**Accio Relevance - Build with Actian VectorAI Database**

SafeRAG is built entirely around Actian VectorAI as its core retrieval engine — not as a bolt-on database, but as the system's central intelligence layer.

We use three of Actian's key capabilities directly:

Named Vectors: FAA documents, historical incident reports, and inspection images are each embedded separately (Qwen3-Embedding for text) and stored as named vectors within one logical record — keeping modalities isolated without needing separate databases.
Metadata Filtering: Every query is first narrowed by aircraft model, engine type, and ATA chapter before vector search runs, pruning irrelevant results and making retrieval both faster and more precise.
Server-side Reciprocal Rank Fusion (RRF): Instead of writing custom Python logic to merge text and image relevance scores, we rely on Actian's native RRF to fuse multimodal evidence server-side — the mathematically optimal combination, with zero custom fusion code in our app layer.

This directly matches the "Accio Relevance" track's focus: our entire value proposition depends on Actian solving the hard problem of multimodal evidence correlation. The LLM in our system never diagnoses or invents — it only summarizes what Actian's retrieval has already verified exists, with every claim traceable back to a source Actian retrieved. Without Actian's named vectors and native RRF, our core evidence-correlation workflow doesn't work.

**Open Innovation**

SafeRAG fits the Open Innovation track because it applies modern multimodal RAG and vector search techniques to a domain that's largely underserved by existing AI tooling: regulated, offline, safety-critical aircraft maintenance.

Most AI/RAG innovation today assumes cloud connectivity and optimizes for consumer or enterprise SaaS use cases. We took the opposite constraint set — no internet, no cloud, strict regulatory traceability (FAA/EASA Part 145), and zero tolerance for hallucination — and built a system that still delivers real evidence-correlation value under those conditions.

The innovation here isn't just "add AI to maintenance" — it's in the architecture:

Treating retrieval as the core intelligence, not the LLM, so the system can be fully audited and never originates unverifiable claims
Making multimodal correlation (text documents + inspection images) work entirely offline, on lightweight local infrastructure
Replacing fabricated confidence scores with an explainable, source-count-based confidence rating — a small but meaningful rethink of how AI systems should communicate certainty in high-stakes domains

This approach isn't limited to aviation — the same evidence-first, offline-first, non-hallucinating pipeline could extend to any regulated field (railways, power plants, oil rigs, defense) where engineers need traceable answers and can't rely on the cloud. That generalizable, constraint-driven approach to trustworthy AI is what makes this an Open Innovation fit rather than a narrow vertical tool

**Education**

SafeRAG fits the Education track through its role in technical knowledge transfer and on-the-job training for maintenance engineers — particularly junior technicians who haven't yet built up years of tacit institutional knowledge.

Aircraft maintenance expertise is traditionally passed down informally — senior engineers remember which past incidents resemble a current fault, junior engineers don't. SafeRAG turns that tacit knowledge into an accessible, explainable learning tool:

Every recommendation comes with citations back to the original FAA documentation, so instead of just getting an answer, a technician sees exactly which regulatory section or AD supports it — reinforcing correct procedural knowledge rather than replacing it.
The Evidence Used panel functions like a guided case study, showing a junior engineer how a fault code connects to a real historical incident and a real inspection finding, teaching pattern recognition that normally takes years of hands-on experience to build.
Because retrieval surfaces similar historical incidents and inspection images rather than final answers, it encourages engineers to compare and reason through evidence themselves rather than blindly trusting an output — building better diagnostic thinking rather than automating it away.

Team **Beta Ethical Developers** -- [Sayantan Biswas](https://github.com/sayantan0909), [Mouli Biswas](https://github.com/mouli-tech2025)

`2026-07-26`

---

### notesmarketplace
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/notesmarketplace-5ba6) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.noteshere.site/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> A secure peer-to-peer marketplace for studentsnote

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Nodemailer](https://img.shields.io/badge/Nodemailer-333333?style=flat-square)

**Challenges we ran into**

Building a platform with over 50,000 lines of code, real-time communication, and secure file sharing came with its fair share of hurdles. Here are the most significant challenges and how I overcame them:

1. Real-time Communication & Socket Synchronization

The Hurdle: Integrating instant messaging via Socket.io alongside Jitsi VoIP calling was tricky. Initially, managing active user states and handling disconnections caused duplicate notifications and "ghost" participants in voice calls.
The Solution: I implemented a robust heartbeat mechanism using Socket.io to track user presence accurately. I also centralized the WebRTC and Socket connections into a custom React Hook, which ensured that event listeners were properly mounted and unmounted, eliminating memory leaks and ghost calls.
2. Secure File Delivery & Access Control

The Hurdle: Notes Marketplace relies heavily on users sharing digital files (PDFs, images). I needed to ensure that previews were publicly accessible, but the actual high-quality note files were strictly locked behind authentication and successful payment/access verification.
The Solution: Instead of serving files directly from public URLs, I implemented a secure cloud storage solution. I configured the Node.js backend to generate Presigned URLs with short expiration times. This ensures that even if a user shares a direct download link, it will expire and become invalid for anyone else trying to bypass the system.
3. Complex State Management & Performance Optimization

The Hurdle: As the application grew, managing the state for real-time chat notifications, user authentication, and advanced search filters (University, Semester, Subject) started causing unnecessary re-renders in the React frontend, slowing down the UI.
The Solution: I restructured the global state using optimized context providers and Redux (or Zustand). By implementing React.memo, useMemo, and lazy loading for heavy components (like the PDF previewer and Jitsi wrapper), I significantly reduced the initial load time and achieved a buttery-smooth 60fps scrolling experience on both mobile and desktop.
4. Advanced Search & Database Query Optimization

The Hurdle: Allowing students to filter through potentially thousands of notes using multiple dynamic filters (Subject, University, Rating, Price) led to slow MongoDB query response times.
The Solution: I optimized the MongoDB database by creating Compound Indexes on the most frequently queried fields (e.g., university_id + semester + subject). I also implemented server-side pagination and caching for trending notes, which drastically reduced the database load and made the discovery page feel instantaneous.

**The problem it solves**

📚 Notes Marketplace

Traditional academic environments suffer from a major knowledge-sharing gap. Students often struggle to find reliable, organized, and high-quality study resources when they need them most.

🚨 Core Problems

1️⃣ Scattered & Unorganized Study Material

Important notes, exam summaries, and study guides are spread across WhatsApp groups, random Google Drive folders, Telegram channels, and personal devices. Finding the right resource for a specific semester or subject becomes frustrating and time-consuming.

2️⃣ No Incentive for Student Creators

Creating quality academic notes requires significant effort and consistency. However, students currently have no dedicated platform to showcase, distribute, or monetize their academic work, discouraging talented creators from contributing.

3️⃣ Unsafe Peer-to-Peer Sharing

Most note-sharing transactions happen through direct chats and social platforms, leading to payment fraud, contact leaks, corrupted files, and trust issues between buyers and sellers.

 4️⃣ Poor Communication Experience

Students often face difficulties while negotiating, asking questions, or discussing notes because communication systems are fragmented across multiple apps and platforms.

---

 🌟 Our Solution: Notes Marketplace

Notes Marketplace is a modern MERN-stack powered academic ecosystem designed to simplify, secure, and enhance student resource sharing.

Built with over **50,000+ lines of code**, the platform combines responsive UI, real-time communication, and secure peer-to-peer interactions into a single seamless experience.

---

 🎯 Key Features

 📖 Curated Academic Discovery

Students can browse notes using advanced filters such as:

* University
* Semester
* Subject
* Category

The platform provides a premium responsive experience with optimized layouts for both desktop and mobile users.

*(Insert Homepage Screenshot Here)*

---

 ⚡ Rich Interactive Note Previews

Every note listing includes immersive preview cards displaying:

* Subject information
* Seller details
* Ratings
* Price
* Download metrics

This allows students to evaluate resources before making purchases.

- ![image](https://assets.devfolio.co/content/fb224e9d3cc141179d6f9f0ba4294610/5253b9fc-1cd1-4711-b5f5-6cb96c963029.png)

---

 💬 Real-time Chat & Voice Communication

The platform includes:

* Instant messaging
* Real-time notifications
* Integrated Jitsi VoIP calling

Students can communicate securely without exposing personal phone numbers.

![image](https://assets.devfolio.co/content/fb224e9d3cc141179d6f9f0ba4294610/bb864d30-dc16-4706-8b09-15ebcf38a3e8.png)

---

  🚀 Vision

Our goal is to build a trusted digital ecosystem where students can:

* Access high-quality academic resources
* Monetize their knowledge
* Collaborate securely
* Improve learning accessibility

Notes Marketplace transforms fragmented academic sharing into a structured, safe, and scalable student-powered platform.

[Dev Kumar](https://github.com/DEVKUMAR9012)

`2026-05-20`

---

### UniDrop
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/unidrop-d6d6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/thiruvenkatam-cell/NMITHACKSdhayo.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/14d0bbc11d2448228019d539140c7b51) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Powered by Students, for Students.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square)

**The problem it solves**

1. Students waste time searching across campus for snacks, stationery, medicines, and essential items during busy schedules.
2. There is no trusted platform for students to borrow or lend useful items within the campus community.
3. Traditional delivery systems are slow and inefficient for short-distance campus deliveries.
4. Lack of real-time communication and tracking creates confusion during deliveries.
5. Campus vendors often struggle to reach students digitally in an organized way.
6. Students traveling along the same route cannot utilize their movement to assist  with deliveries and earn rewards.

**Challenges we ran into**

1. Implementing real-time delivery tracking and live location updates smoothly.
2. Managing instant communication using chat and Socket.IO connections.
3. Designing an efficient delivery partner assignment system based on nearby    routes and locations.
4. Ensuring secure OTP authentication and safe delivery verification.
5. Maintaining responsive and smooth UI animations across different devices.
6. Handling real-time database updates and synchronization using MongoDB Atlas.
7. Integrating Google Gemini AI for intelligent recommendations and assistance features.
8. Deploying frontend and backend services separately on Vercel and Render while maintaining proper API communication.

**Open Innovation**

> P2P Campus Connect fits into the Open Innovation Track because it solves real-world campus problems using smart technology, AI, and community-driven collaboration. The platform combines peer-to-peer commerce, real-time delivery, borrowing/lending, and intelligent route-based delivery matching into one scalable ecosystem.

> Its innovative and flexible approach can be expanded beyond campuses to hostels making it a practical and scalable real-world solution.

**Google Gemini**

1. Gemini AI enhances P2P Campus Connect by making the platform smarter, more personalized, and efficient. It helps analyze user behavior, preferences, and order patterns to provide intelligent recommendations such as popular snacks, frequently borrowed items, and personalized suggestions.

2. Gemini AI can also assist users through smart search, chatbot-style assistance, and faster query handling inside the platform. By improving user experience, optimizing interactions, and enabling AI-powered recommendations, Gemini adds innovation and intelligence to the overall campus commerce ecosystem, making the platform more modern and user-friendly.

**MongoDB Atlas**

1. MongoDB Atlas fits into P2P Campus Connect by providing a scalable and cloud-based database system to manage users, orders, delivery details, chat data, and transaction records efficiently.

2. Since the platform involves real-time updates, live tracking, and multiple users interacting simultaneously, MongoDB Atlas helps handle dynamic and rapidly changing data with high performance and reliability. Its cloud infrastructure also makes the platform easily scalable for larger campuses and future expansion into other communities, supporting the project’s innovative and real-world application goals.

Team **Jinn Coderzs** -- [TARUN KUMAR](https://github.com/tarun05108), [Somobrato Das](https://github.com/Somobrato2668?tab=repositories), [vikash kumar](https://github.com/vikash1551), [THIRUVENKATAM V](https://github.com/thiruvenkatam-cell)

`2026-05-10`

---

### Local Services
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/local-services-321f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/expertcoder06/localServices.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://local-services-q53h.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Connecting community with trusted providers

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Nodemailer](https://img.shields.io/badge/Nodemailer-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

![image](https://assets.devfolio.co/content/6d710d53b33149d0b20556d68abbb073/a589e261-4121-4da0-9411-0e39f83f63e5.jpeg)

🚨 The Problem It Solves
1. 🔍 Difficulty in Finding Reliable Service Providers

People struggle to find trusted local professionals like electricians, plumbers, or tutors.
➡️ Most options rely on:

Word-of-mouth
Unverified contacts

❌ Result: Low trust and poor service quality

2. 🛡️ Lack of Trust & Verification

There is no proper system to verify:

Identity of providers
Skill authenticity

➡️ This creates a high risk of fraud and fake profiles.

3. 💰 Unclear & Unpredictable Pricing

Customers often don’t know:

Final cost
Hidden charges

❌ Result: Disputes and hesitation in booking services

4. ⏱️ Time-Consuming Process

Finding and contacting providers involves:

Multiple calls
Waiting for responses

➡️ Leads to delays and frustration

5. 📍 Inefficient Local Matching

No efficient way to:

Find nearby providers
Compare options quickly

➡️ Results in wasted time and effort

6. 📉 No Performance Tracking

There is no system to track:

Provider reliability
Job completion rate
Response time

➡️ Users cannot make data-driven decisions

7. ❌ Poor Communication & Coordination

Lack of:

Real-time updates
Booking confirmations

➡️ Leads to miscommunication and missed appointments

**Challenges we ran into**

![image](https://assets.devfolio.co/content/6d710d53b33149d0b20556d68abbb073/fb2c308e-e0f8-4cc7-a9ca-b46ec6775328.jpeg)
🚧 Challenges We Ran Into
1. 🔍 Service Standardization Across Categories

We needed to support multiple services like electricians, tutors, and plumbers.
➡️ Each service has different workflows and pricing models, making it difficult to design a unified system architecture.

2. 🛡️ Provider Verification & Fake Profile Prevention

Ensuring that service providers are genuine was a major challenge.
➡️ We planned facial recognition-based authentication, but implementing accurate real-time face matching within the hackathon timeframe was complex.

3. 😓 Face Recognition Implementation Challenge (IMPORTANT)

We faced difficulties in:

Matching uploaded images with live camera input
Handling lighting, angles, and image quality
Achieving real-time performance in the browser

➡️ Due to these constraints, we implemented a face detection + alternative verification approach, while keeping the system ready for full face recognition integration in future.

4. ⏱️ Real-Time Booking & Response Handling

Users expect instant booking confirmations and provider responses.
➡️ Managing real-time updates, chatbot replies, and availability sync caused latency challenges.

5. 💰 Dynamic Pricing Complexity

We designed pricing based on:

Demand
Availability
Ratings

➡️ Creating a fair and understandable pricing model without confusing users was difficult.

6. 📍 Location-Based Matching

Matching users with nearby providers required:

Radius-based filtering
Efficient location queries

➡️ Balancing accuracy and performance was challenging.

7. 📅 Scheduling & Time Slot Conflicts

Implementing:

Provider availability
Booking slots
Conflict handling

➡️ Avoiding double bookings and overlapping schedules was a key issue.

8. 🤖 Chatbot Integration

We integrated a chatbot to assist users.
➡️ Challenge was making it:

Context-aware
Fast
Useful for booking decisions
9. 📧 Notification System

Sending booking confirmations via email required reliability.
➡️ Ensuring instant and consistent delivery was tricky during development.

10. ⚖️ Handling Cancellations & Penalties

We introduced penalties for both users and providers.
➡️ Designing a fair and logical penalty system for different scenarios was complex.

These challenges helped us design a more scalable and practical system, where we prioritized reliability, user experience, and future extensibility over incomplete implementations

**OPEN INNOVATION**

![image](https://assets.devfolio.co/content/6d710d53b33149d0b20556d68abbb073/ef44d6b0-7638-480f-935c-d2428e617c3e.png)

Our platform allows any local service provider (plumbers, electricians, tutors, etc.) to join and offer services.
➡️ This creates an inclusive and open marketplace, instead of a closed system.

🤝 2. Community-Driven Trust System

We don’t rely on a central authority only.
➡️ Trust is built using:

User ratings
Reviews
Completed jobs
Response time

👉 This means users themselves contribute to improving the platform, which is a core idea of open innovation.

🔄 3. Continuous Feedback Loop

Customers and providers both:

Give feedback
Rate each other
Influence visibility and trust score

➡️ The system evolves continuously based on real user input, not static rules.

🧠 4. Integration of AI & Open Technologies

We use:

Chatbots
Scalable MERN stack
Future-ready APIs (face recognition, etc.)

➡️ The system is designed to integrate new technologies easily, making it adaptable and innovative.

🌐 5. Solving Real Community Problems

Open Innovation focuses on real-world impact.
➡️ Our project:

Reduces search time for services
Increases income opportunities for local workers
Builds trust in the informal sector

👉 This directly benefits the local community ecosystem.

🔗 6. Modular & Extensible Architecture

Our system can easily expand to:

New service categories
New cities
New features (AI, verification, payments)

➡️ This makes it an open and scalable innovation platform, not a fixed product.

⚡ 7. Collaboration Between Multiple Stakeholders

The platform connects:

Customers
Service providers
AI systems
Admin dashboards

➡️ This creates a collaborative innovation environment, which is the essence of open innovation.

Instead of building a closed solution, we built an open system where innovation comes not just from us, but from every user interacting with the platform

Team **Decoders** -- [Swayam Prasad](https://github.com/Swayam-Was-Here), [Mohit Yadav](https://github.com/19-mohityadav), [Sanjay Sharma](https://github.com/expertcoder06)

`2026-03-28`

---

### digiGUIDE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/digiguide-f082) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/studentSS-code/digi_Guide.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/gMuMUMkBUso?si=9K3Kx2LB7PI-tm6x) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI LEARNING TWIN

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **PIXELTHINKERS** -- [SNEHA CHOWDHURY](https://github.com/SnehaChowdhur), [Sristy Singh](https://github.com/studentSS-code)

`2026-09-12`

---

### AutoNBA Mapper (Smart Education)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/autonba-mapper-smart-education-fc30) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=bXKIzAQZIVw) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Question paper analyser and setter

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

While building this project , so many bugs was created like not working a pdf extracted , memory was not saving, etc.

**The problem it solves**

Problem:- Time consuming work to filter out and analyze the question for a teacher. 
This project is usefull for a teacher of engineering colleges to analyse and filter out the questions automatically and manually.

Team **HUNGRYMATE** -- [Piyush Kumar](https://github.com/piyush-kumar-gurudev), [Pravat Choudhary](https://github.com/pravatchoudharyjee2025-sketch), [Priyanka Bhagat](https://github.com/priyankaCodes813), [Sagnik Chakraborty](https://github.com/CSagnik06)

`2026-08-30`

---

### AI-Based Child Safety System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aibased-child-safety-system-4552) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/somesh-opps/AI-Based-Child-Safety-System) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Making Schools & Childcares Safer with AI

![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square)

**Challenges we ran into**

Reliable child identification
Making sure the system correctly recognizes the right child every time, even with lighting changes, pose differences, or partial face occlusion.

RFID and face verification integration
Combining RFID-based check-in/check-out with camera-based validation so both parts work together smoothly.

Hardware–software communication
Connecting Python with the Arduino UNO R3 over serial communication without delays, disconnects, or data sync issues.

Image processing accuracy
OpenCV-based detection can struggle with poor lighting, motion blur, camera angle, and crowded environments.

False positives / false negatives
Avoiding cases where the system wrongly approves or rejects a child or guardian.

Real-time performance
Ensuring the system responds quickly enough for check-in/check-out without long waiting times.

LCD status feedback
Displaying clear and correct messages on the LCD while keeping it synchronized with the backend logic.

Sensor and device reliability
Handling RFID reader errors, camera failures, Arduino resets, or loose wiring.

Dataset / training limitations
If face recognition is used, collecting enough good-quality images for each child can be difficult.

Privacy and security concerns
Storing child identity data safely and preventing misuse of attendance or recognition data.

**The problem it solves**

This project appears to solve the problem of manual child check-in/check-out management in schools and daycare centers.

In practical terms, it likely addresses:

Poor attendance tracking for children
Unauthorized pickup risks by ensuring only approved people can check children in/out
Time-consuming manual logging by automating attendance and entry/exit records
Lack of real-time verification using tools like RFID, camera-based computer vision, and Arduino-driven hardware
Based on the repo description, the system is an automated child safety and attendance solution that combines:

Python + OpenCV for vision-based processing
Arduino UNO R3 for hardware control
RFID for identity verification
LCD screen for status display
So the core problem it solves is improving child safety and streamlining attendance/access control in educational or childcare settings.

Team **BitVerse** -- [Somesh Kumar Sahoo](https://github.com/somesh-opps), [Abhiraj SAHA](https://github.com/uvraj456), [Saudamini Roy](https://github.com/RoySaudamini)

`2026-07-30`

---

### Pudding
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pudding-7a7e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tasfia-17/Puddingext) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/SOuFOeRcN_E) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SOuFOeRcN_E) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI Cognitive Accessibility Browser Extension

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-333333?style=flat-square) ![i18n](https://img.shields.io/badge/i18n-333333?style=flat-square) ![accessibility](https://img.shields.io/badge/accessibility-333333?style=flat-square) ![Privacy](https://img.shields.io/badge/Privacy-333333?style=flat-square) ![GEMINI NANO](https://img.shields.io/badge/GEMINI%20NANO-333333?style=flat-square) ![Lingo.dev](https://img.shields.io/badge/Lingo.dev-333333?style=flat-square) ![ADHD](https://img.shields.io/badge/ADHD-333333?style=flat-square)

**The problem it solves**

Pudding helps people with dyslexia, ADHD, and reading challenges by using on-device AI (Chrome Gemini Nano) to simplify and restructure web content in real-time. Works 100% offline across 10 languages reaching 5+ billion people.

**Challenges we ran into**

Getting Chrome Gemini Nano to work reliably behind experimental flags, building privacy-safe cognitive tracking with local storage only, and adding RTL support for Arabic without breaking LTR layouts.

**The problem it solves**

Millions of people struggle to read online content. 8.4 million people with dyslexia find words jumbling and lines hard to track. 6.4 million people with ADHD lose focus in dense, distraction-filled pages. Non-English speakers face a double barrier: complexity AND language.

Existing tools are either cloud-based (privacy risk), one-size-fits-all (no adaptation), or English-only. No tool learns how YOU read and adapts content to YOUR cognitive style — in YOUR language.

Pudding solves this with a Cognitive Adaptation Engine that:
- Learns your personal reading patterns entirely on-device
- Adapts content complexity in real-time based on your behavior
- Works 100% offline — zero data leaves your device
- Supports 10 languages reaching 5+ billion people

**Challenges we ran into**

## Challenge 1: Chrome Gemini Nano API Instability
Chrome's built-in Prompt API (Gemini Nano) is still in experimental flags. Getting it to reliably trigger text simplification without falling back silently required careful feature detection and graceful degradation logic.

## Challenge 2: Cognitive Tracking Without Privacy Violation
Tracking scroll speed, reading pauses, and re-reads on any webpage is technically complex. We had to build a non-intrusive observer that works across dynamic content (infinite scroll, SPAs) while storing everything in Chrome local storage only — never touching any external server.

## Challenge 3: RTL Language Support
Adding Arabic (right-to-left) to the extension UI required overhauling the CSS layout system and testing across multiple text directions without breaking the existing LTR layouts.

## Challenge 4: Content Restructuring Without Breaking Page Layouts
Inserting structured bullet points and collapsible sections into arbitrary third-party webpages (Wikipedia, news sites, blogs) without breaking their DOM or CSS took significant iteration on the content.js injection approach.

Tasfia Chowdhury

`2026-06-28`

---

### FundMySkill
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fundmyskill-9b7b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/monojitgoswami69/FundMySkill) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/O75yYtLc-iI) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Bringing learning to the needy, one fund at a time

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![Pinecone](https://img.shields.io/badge/Pinecone-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square)

**The problem it solves**

***The problem it solves***

Crowdfunding for education sounds effective, but in reality, it often lacks transparency. Once money is donated, there’s usually no clear visibility into how it’s actually used. This creates doubt for donors and opens the door for partial misuse or inefficient allocation of funds.

At the same time, underprivileged students don’t just need financial support, they need a complete and structured learning environment. Many solutions either stop at funding or provide fragmented educational resources without continuity or accountability.

* ***Donors can’t clearly track how their contributions are used***
* ***Lack of transparency reduces trust in crowdfunding platforms***
* ***Students often receive incomplete or unstructured learning support***
* ***Credentials are easy to fake and hard to verify***

To address this, the platform not only ensures transparent fund management through escrow but also provides a full learning ecosystem.

* ***Structured courses with video lectures and guided curricula***
* ***Live interactive sessions for real time learning and doubt solving***
* ***Assessments and quizzes to track progress and understanding***
* ***On demand study materials and resources for flexible learning***
* ***AI based Socratic tutor for personalized, question driven learning***
* ***Verifiable on chain certificates that cannot be forged***

This connects funding directly to measurable learning outcomes, making the entire system more accountable and effective.

**Challenges we ran into**

***Challenges I ran into***

This project turned out to be harder than it looked on paper because it mixes a lot of moving parts, AI, payments, and a full learning platform.

The AI tutor was one of the biggest challenges. Getting the RAG system to actually give useful, relevant answers wasn’t easy. In the beginning, it either pulled the wrong context or gave very generic responses that didn’t really help students. I had to spend a lot of time improving how content was stored, how it was retrieved, and how the system understood what the student was actually asking.

Another tricky part was handling the escrow system. It’s not just about holding money safely, it’s about deciding when and where that money should go. Splitting funds across course providers, APIs, and platform costs while keeping everything transparent and fair took a lot of thought. Making it automated without making it unsafe was a constant balancing act.

* ***Making the AI tutor actually helpful instead of just technically correct***
* ***Improving how content is retrieved so answers stay relevant***
* ***Designing fund flow logic that prevents misuse but still works smoothly***
* ***Connecting spending (APIs, courses, infra) directly to real usage***
* ***Keeping everything stable while multiple systems interact together***

Most of this was solved through a lot of iteration, testing, and breaking things repeatedly until the system became more reliable.

**Web3**

The crowdfunding model is built around decentralized escrow, where funds are not blindly handed over but are programmatically controlled. This ensures that money is only released under predefined conditions, making misuse significantly harder and accountability much stronger.

* ***Funds are stored and managed through decentralized escrow instead of centralized control***
* ***Transactions are transparent and can be verified, improving donor trust***
* ***Fund distribution is tied to actual usage like course access and platform resources***

On the education side, Web3 is used to solve the problem of credential authenticity. Certificates are minted on chain, making them tamper proof and independently verifiable without relying on the platform.

* ***Course completion certificates are issued as on chain credentials***
* ***Eliminates forgery and enables instant verification of achievements***

Overall, Web3 enables this platform to move from a trust based system to a trustless one, where both funding and outcomes are transparent, enforceable, and verifiable.

**AI/ML**

The platform includes an AI powered Socratic tutor that guides students through concepts using questions, helping them think rather than just consume answers.

The system is built on a RAG pipeline, so responses are grounded in actual course material. This keeps explanations relevant to what the student is studying and avoids generic or incorrect outputs.

* ***RAG based architecture to retrieve and ground responses in course specific content***
* ***Reduces hallucination and improves answer reliability***
* ***Adapts explanations based on student queries and learning context***

Beyond tutoring, AI is also used to continuously evaluate understanding in real time.

* ***Generates on demand quizzes based on current topics***
* ***Tests student understanding instantly instead of delayed assessments***
* ***Adjusts difficulty dynamically based on performance***
* ***Provides immediate feedback to reinforce weak areas***

This turns the platform into an active learning system instead of a passive content delivery tool.

* ***Acts as a 24/7 personalized tutor***
* ***Combines teaching and testing in a continuous feedback loop***
* ***Scales high quality learning without increasing instructor load***

**Open Innovation**

***How this project fits into Open Innovation***

This project brings together ideas from multiple domains, Web3, AI, and education, and combines them into a single system focused on solving a real world problem. Instead of improving just one layer, it rethinks how funding and learning can work together in a more open and accountable way.

At its core, the platform is designed to be modular and extensible, making it possible to integrate different course providers, learning resources, and AI systems without being locked into a single ecosystem.

* ***Open integration with multiple course providers and content sources***
* ***Flexible infrastructure that can incorporate new tools, APIs, and learning modules***
* ***Decoupled architecture allowing independent improvement of funding, AI, and education layers***

The system also promotes transparency and verifiability, which are key aspects of open innovation.

* ***Fund flows are visible and auditable instead of being hidden behind centralized control***
* ***Learning outcomes and certifications are independently verifiable***
* ***Encourages trust between contributors, educators, and learners***

By making both the financial and educational components more open, composable, and accountable, the project creates a foundation that others can build on, extend, or adapt to different use cases beyond just this platform.

**Education**

***How this project fits into Education***

This project focuses on making quality education accessible, structured, and accountable for students who typically don’t have access to it. Instead of just providing content, it delivers a complete learning environment supported by both technology and funding.

The platform combines structured courses with continuous support, ensuring that students don’t just enroll, but actually learn and complete their journey.

* ***Well structured courses with video lectures and guided learning paths***
* ***Live sessions for interaction, doubt solving, and engagement***
* ***Assessments and quizzes to consistently track progress***
* ***On demand study materials for flexible learning***

AI plays a key role in improving how students learn, especially where teacher access is limited.

* ***AI powered tutor that helps students understand concepts step by step***
* ***On demand quizzes to test understanding in real time***
* ***Immediate feedback to help students improve continuously***

What makes this different from typical edtech platforms is the accountability layer tied to funding.

* ***Students’ learning is directly supported through transparent crowdfunding***
* ***Funds are tied to actual educational usage and outcomes***
* ***Certificates are verifiable, ensuring real value of completion***

This ensures that students are not only given access, but are supported through a reliable and complete learning system that leads to measurable outcomes.

Team **Nohara Family** -- [Monojit Goswami](https://github.com/monojitgoswami69), [Shubhadeep Biswas](https://github.com/sbr69)

`2026-03-22`

---

### Campus Connect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-connect-858b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/The-Blue-Pheonix/campusConnect) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://campus0connect.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/bT_vamRECCA) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The Next-Gen Real-Time Student Discovery & Network

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

Team **Blue_Pheonix** -- [Anirban Sarkar](https://github.com/AnirbansarkarS/), [Chirabrata Ghosal](https://github.com/CHIRABRATA), [Aryan Mishra](https://github.com/aryyann011)

`2026-09-12`

---

### VLA ( VISION LANGUAGE ACTION)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vla-vision-language-action-ee9b) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/_lShRIDO8zE?si=4q7nHTUSodigzet5) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> bringing Ai to physical intelligence

![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Integration of the custom yolo model designed and hardware arm

**The problem it solves**

So basically coding and bot to fold cloths is tougher but in case what if u can teach it through vison and text link an human. The technology know as VLA.

**Hardware**

Robotic arm and electronics

Team **Team 404 error** -- Steve Josh, Adnan Hanish, Hisham Shameer, [Aathitya Pandian](https://github.com/sd)

`2026-09-02`

---

### NextGen Edu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nextgen-edu-8cbc) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smarter Schools. Proactive Communication.

![PHP](https://img.shields.io/badge/PHP-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![CodeIgniter](https://img.shields.io/badge/CodeIgniter-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**Challenges we ran into**

One challenge we ran into was integrating external communication services with the main system. It wasn't enough to just have an SMS feature in the website — we had to understand how the provider's API, authentication and configuration worked and how the response should be handled by our backend.

We handled this by separating the integration from the main modules and testing the communication step by step instead of trying to connect everything at once. This also made it easier to troubleshoot when something didn't work as expected.

**The problem it solves**

Managing an institution involves a lot of separate tasks — student records, attendance, exams, fees, homework, communication, reports and more. When these things are handled through different systems, spreadsheets or manual work, information gets scattered and it becomes easy to miss updates or waste time on repetitive tasks.

NextGen Edu brings these day-to-day activities together in one platform. It helps staff manage information in one place, while students, teachers and parents can access the information that is relevant to them. The goal is simple: less manual work, fewer communication gaps and a more organized way of running the institution.

Team **Team Unravel** -- [Ayush Thakur](https://github.com/ayush8907), [Shyam Sundar Jha](https://github.com/ShyamSundarJha), [Alina Washim](https://github.com/alina01washim-aw)

`2026-08-30`

---

### AdLoop
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/adloop-7e59) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DV0x/adloop) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Self-learning ad engine with a truth layer

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![Agents](https://img.shields.io/badge/Agents-333333?style=flat-square) ![managed-agents](https://img.shields.io/badge/managed--agents-333333?style=flat-square) ![gpt-image-2](https://img.shields.io/badge/gpt--image--2-333333?style=flat-square) ![claude-code](https://img.shields.io/badge/claude--code-333333?style=flat-square)

**What is the deployed URL for this project?**

https://github.com/DV0x/adloop (local-first: python3 -m engine canvas godesi.in serves the live canvas on localhost:8787)

**How Did You Use Claude?**

Claude is the entire intelligence layer, on **Claude Managed Agents (CMA)** as the runtime:

- **One CMA session = one pipeline stage** (brand capture / batch / founder edit), each driven by a structured runbook. Our validated render + assembly scripts execute *inside* the CMA sandbox; the KIE render key lives in a **vault** and is substituted at egress, so the model never sees it. Per-session **budget caps** with pause/resume.
- **Memory stores as the product's moat**: the per-brand ledger and learned-rules files live in a CMA memory store, mounted read-write into every session — that's what makes the engine *self-learning* across sessions.
- **Multiagent roster (depth-1)**: cold-start capture fans three research lanes (facts, design guide, personas) out to parallel copies of the agent; the correctness QA gate is never delegated.
- **claude-opus-5** writes the art-direction briefs (structured tool calls against a pinned 8-slot schema) and runs the **vision verify pass** — reading rendered pixels and diffing every numeral on canvas against the fact bank.
- **Claude Code** built the whole thing today, including this submission via the Devfolio MCP.

**What is the problem your project solves?**

An Indian D2C brand loses money on its first sale (median: **−₹320 per new customer**; 78% of 6,000+ brands are unprofitable on order one). Survival means finding the ad that works before the money runs out — and creative drives **56% of sales ROI**, more than targeting or placement. But an ad fatigues in 3–6 weeks, agencies bill ₹40–80K/month and deliver 2–4 creatives, and ~4,000 brands sit below the ₹1L ad-spend floor agencies won't touch.

Existing AI ad tools are fast and structurally broken. We captured a competitor's full pipeline live before building: **it invents claims** — a "100% SATISFACTION GUARANTEE" seal for a brand with no guarantee, "Loved By 10,000+" with zero reviews scraped; roughly **40% of its claims wouldn't survive an audit**. Its 30-ad batches collapse into ~1 real message tested, and it has **no memory** — every run is day one, every brand gets the same scene skeletons.

A founder doesn't need 30 pictures. They need to find the one message that works — without their ad account making legal claims their brand never made. **We sell the search, not the assets.**

**How you are solving it?**

**AdLoop is a self-learning ad creative engine.** Give it a brand URL; it researches the brand, writes art-direction briefs, renders finished ads, verifies its own output by reading the pixels back, and learns from every batch and every founder edit.

- **Truth layer**: every fact is captured with its source URL into a number bank with an explicit FORBIDDEN list. Every ad carries `facts_used[]`; any numeral not traceable to the bank can't ship. A vision pass reads the finished image and diffs every number on canvas against the facts.
- **Probes, not pictures**: each ad is a distinct hypothesis keyed by angle × SKU × persona. Three ads test three things.
- **The ledger that learns**: every shipped ad is logged by cell and status. Winners repeat *deliberately* in new scenes; unproven cells never duplicate; every batch keeps an exploration slot. Founder edits become permanent brand rules (one edit = signal, two = rule).

**The loop closed live during the event, on godesi.in — receipts are tracked in the repo:**
1. Batch 2 shipped; the founder made two edits asking for "festival mela energy" (`brands/godesi.in/batches/002/edit-*/`).
2. The engine generalized both into one promoted rule in `brands/godesi.in/memory.md` — including which brand color the bunting takes per ground.
3. **Batch 3 applied the rule with zero new instructions** — all three briefs carry the mela-flag layout line (`batches/003/briefs.json`).
4. **The verify pass then FAILED all three batch-3 renders** — the image model had hallucinated numerals into the scene (sticky notes reading "Client call 3:30 PM") and the truth layer caught every one (`batches/003/verdicts.json`). Refusing to ship them IS the product.

The repo README maps every claim above to the exact file that proves it: https://github.com/DV0x/adloop

**Prior-work disclosure**: the prompt-grammar research (capturing a competitor pipeline, extracting its structure) and validation scripts predate the event window. Built during the hackathon: the full engine on Claude Managed Agents (capture/batch/edit stages, pinned schemas, ledger + memory promotion), the live canvas UI, and three live batches end to end (~$0.17/image, ~5 min warm).

[0xauser 0xauser](https://github.com/DV0x)

`2026-08-08`

---

### VillageWork
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/villagework-8ce0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saptarshi-bisoi/VillageWork) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://villagework.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Rural talent Need digital speed.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Lucide React](https://img.shields.io/badge/Lucide%20React-333333?style=flat-square)

**The problem it solves**

# 🧩 The Problem VillageWork Solves

> **500 million skilled hands. Zero digital presence. One broken connection.**

In every Indian village, there's an electrician with no clients, and a family with no electrician.
VillageWork ends that absurdity.

---

## The Gap Nobody Fixed

India digitized payments. India digitized education. India digitized food delivery.

**But the village carpenter still gets work by standing at the chai stall.**

---

## 6 Real Problems. One Platform.

| # | Problem | Reality |
|---|---------|---------|
| 🔍 | Skilled workers are invisible | No profile, no reach, no discovery beyond their street |
| 📵 | Customers can't find help | Asking 10 neighbors to find a plumber is still the norm |
| 🏙️ | Talent migrates needlessly | Youth leave villages not for lack of skill — but lack of platform |
| 🤝 | Trust doesn't scale | People only hire who they personally know. Strangers don't get hired |
| 💸 | Cash kills accountability | No receipts, no records, no financial identity for workers |
| 🌐 | Existing apps weren't built for Bharat | Urban Company needs English. Fiverr needs internet. Villages need neither |
---

> **VillageWork doesn't just connect workers to jobs.**
> **It gives rural India its first economic identity — digital, trusted, and local.**

**Challenges we ran into**

# ⚔️ Challenges I Ran Into

> Building for rural India sounds simple. It wasn't.
> Every assumption we had about users, devices, and connectivity got challenged — fast.

---

## 1. 🌐 Designing for 2G Without Killing the Experience

**The Hurdle**
Our first build was beautiful — smooth animations, high-res images, rich UI. Then we tested it on a 2G connection simulating rural network speeds.
It took **14 seconds to load.** That's a dead product in a village.

**How We Fixed It**
- Stripped all heavy animations and replaced with CSS-only transitions
- Compressed every image to WebP format under 30KB
- Lazy-loaded non-critical components
- Built an offline-first fallback screen so the app doesn't just die on slow networks

**Result:** Load time dropped from 14s → **under 3 seconds on 2G.**

---

## 2. 📱 WhatsApp Integration Kept Breaking

**The Hurdle**
WhatsApp Business API has strict message templates — you can't send free-form text without pre-approval. Every time we tried to notify a worker about a new job, the message either got blocked or delivered blank.

**How We Fixed It**
- Switched to pre-approved WhatsApp message templates with dynamic variables (`{{worker_name}}`, `{{job_title}}`, `{{customer_village}}`)
- Built a fallback: if WhatsApp fails, send an SMS via Twilio
- Added a delivery status tracker so workers aren't left in the dark

**Result:** Notification delivery rate went from ~40% → **92% across both channels.**

---

## 3. 🗺️ Hyperlocal Matching Was Harder Than Expected

**The Hurdle**
PIN codes in rural India are wildly inconsistent. Multiple villages share one PIN code. Some villages don't appear on Google Maps at all. Our location-based matching kept returning workers from 40km away as "nearby."

**How We Fixed It**
- Built a custom village name + PIN code database using government census data
- Added a manual village selector as a fallback when GPS or PIN code fails
- Used haversine distance formula between GPS coordinates instead of relying on PIN codes alone

**Result:** Match accuracy improved from 58% → **94% within actual 5km radius.**

---

## 4. 🔤 Multilingual UI Broke Our Entire Layout

**The Hurdle**
When we switched the UI to Hindi, every label overflowed its container. Hindi text is longer, denser, and wraps differently than English. Buttons broke. Cards overlapped. The nav bar collapsed.

**How We Fixed It**
- Rebuilt all UI components with `min-width` instead of fixed `width`
- Used flexible `flexbox` wrapping everywhere
- Tested every screen in both languages before finalizing any component
- Set Hindi as the default test language during development going forward

**Result:** Full Hindi UI now renders cleanly across all screen sizes.

---

## 5. 🔐 Trust — The Problem You Can't Just Code Away

**The Hurdle**
This wasn't a bug. It was a human problem. During our user research, villagers told us they would **never** hire someone they found on an app — no matter how good the profile looked. Trust in rural India is deeply personal, not digital.

**How We Fixed It**
- Introduced **neighbor vouching** — existing users can endorse a worker they personally know
- Added a **"Jobs Done in Your Village"** counter on each profile
- Built a **community verification badge** separate from the standard ID badge
- Designed the rating system to show the reviewer's village name — making reviews feel local and real

**Result:** A feature born from a human insight, not a technical requirement — and arguably our **strongest differentiator.**

---

## 💬 The Biggest Lesson

> We didn't just build software.
> We had to **unlearn every urban assumption** we carried into this project —
> about internet speed, about literacy, about trust, about what "simple" really means.
>
> **That unlearning was the hardest — and most valuable — part of building VillageWork.**

[SAPTARSHI BISOI](https://github.com/saptarshi-bisoi)

`2026-06-27`

---

### AI StudyMate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-studymate-6b20) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AmbujSingh012/AI-StudyMate.git) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Intelligent Learning Companion.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# AI StudyMate

AI StudyMate is a web-based learning platform that uses Artificial Intelligence to make studying easier, faster, and more interactive for students. While studying, many students spend a lot of time reading long PDFs, searching for explanations on different websites, creating notes, or preparing questions for revision. This process can be time-consuming and sometimes confusing. AI StudyMate aims to solve these problems by bringing everything together on a single platform.

With AI StudyMate, students can simply upload their class notes, lecture slides, or PDF books, and the application will automatically generate a short and easy-to-understand summary. If a student doesn't understand a particular topic, they can ask questions directly to the AI, which will answer based on the uploaded study material instead of giving unrelated information from the internet.

The platform also helps students prepare for exams by automatically generating quizzes, flashcards, and important questions from their notes. Instead of spending hours making revision material manually, students can focus more on understanding concepts and practicing them. AI StudyMate can also create a personalized study plan based on the student's available time, subjects, and exam schedule, helping them stay organized and avoid last-minute preparation.

Another important feature is the progress dashboard, where students can track completed topics, quiz scores, and their overall learning progress. This helps them identify weak areas and spend more time improving those topics before exams.

The main goal of AI StudyMate is to reduce the effort students put into organizing study materials so they can spend more time actually learning. It combines note summarization, AI-powered question answering, quiz generation, revision tools, and study planning into one simple and user-friendly platform.

This project is especially useful for college students, school students, competitive exam aspirants, and self-learners who want a smarter and more efficient way to study. By making learning interactive and personalized, AI StudyMate helps students save time, improve productivity, and build confidence in their preparation.

![image](https://assets.devfolio.co/content/9d7f85341b3341e6b18ad7bf5094835c/a78696e4-3572-4fe4-8cf6-82eecff1cf78.png)

**Challenges we ran into**

## Challenges We Faced

One of the biggest challenges while building **AI StudyMate** was getting the AI to provide answers that were based only on the uploaded study material. Initially, the AI sometimes generated generic responses instead of using the content from the student's notes. This could lead to inaccurate or irrelevant answers, especially when users asked topic-specific questions.

To solve this, we improved the document processing pipeline by extracting and organizing the text from uploaded PDFs before sending it to the AI. Instead of relying only on a general prompt, we provided the AI with the most relevant sections of the uploaded document as context. This significantly improved the accuracy and relevance of the responses.

Another hurdle was handling PDFs with complex layouts, such as tables, images, and multiple columns. Text extraction from these files was inconsistent, which affected the quality of summaries and quizzes. We experimented with different PDF parsing libraries and added preprocessing steps to clean and structure the extracted text before passing it to the AI.

We also faced challenges in generating quizzes that were balanced in difficulty. At first, the AI produced either very simple or overly complex questions. By refining the prompts and defining question formats (multiple choice, true/false, and short answer), we were able to generate more useful and exam-oriented quizzes.

Although these challenges took time to overcome, they helped us build a more reliable, accurate, and user-friendly learning assistant. The experience also gave us a better understanding of AI integration, prompt engineering, and document processing in real-world applications.

![image](https://assets.devfolio.co/content/9d7f85341b3341e6b18ad7bf5094835c/e1cd9ce7-7afd-40a0-b956-5a6599711936.png)

Ambuj Singh

`2026-06-28`

---

### EduSense AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edusense-ai-9d41) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Surekha2704/edusense-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://edusense-ai-netlify.netlify.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/k6O7MHdbRiM) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Spotting at-risk students before they fall behind.

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Chart.js](https://img.shields.io/badge/Chart.js-333333?style=flat-square) ![Netlify](https://img.shields.io/badge/Netlify-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

The Problem:
Teachers often realize a student is struggling only after they fail major exams, when it's too late to reverse course. Standard gradebooks show raw numbers, but they don't proactively spot warning trends like declining attendance or poor quiz scores early.

How EduSense AI Solves It:
EduSense AI acts as an early warning system for educators. By automatically analyzing attendance, quiz trends, and study hours, it flags at-risk students in real time and generates step-by-step intervention checklists so teachers can step in before final exams.

**Challenges we ran into**

1. Designing an Intuitive Early-Warning Metric:
Balancing attendance, quiz scores, and self-reported study hours into a meaningful risk assessment required fine-tuning the AI scan logic so it accurately flags "At Risk" students without generating false alarms.

2. Dynamic Data Visualization:
Integrating Chart.js to render real-time performance trend lines dynamically whenever new student data is submitted or selected was tricky to synchronize smoothly with the rest of the dashboard UI.

3. Seamless Netlify & GitHub CI/CD Deployment:
Ensuring continuous deployment from GitHub to Netlify worked without build path errors or missing assets required carefully organizing the static project directory structure.

![image](https://assets.devfolio.co/content/60f958995b924b36bc88410677b745e9/845723af-dcb9-46fc-a1c8-5212ae773387.jpeg)

![image](https://assets.devfolio.co/content/60f958995b924b36bc88410677b745e9/0355b433-c301-45b3-8834-2bc639855abb.jpeg)

surekha k

`2026-07-24`

---

### LearnVerse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/learn-verse-c409) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SayanDev156/LEARN_VERSE) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://learn-verse-black.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/z_FSn7R5244?si=mAs6GPGefaXAmdeG) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The AI-powered studio for smarter learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Learn Verse solves the problem of **generic, one-size-fits-all learning experiences** that don't adapt to how each person actually learns.

Most learners today juggle scattered resources—videos, articles, notes, PDFs—with no single place that understands their pace, gaps, or goals. This leads to:

- Wasted time searching for the "right" explanation
- Passive consumption instead of active understanding
- No personalized feedback on what to learn next

**Learn Verse** uses AI to turn any topic into a structured, interactive learning experience. People can use it to:

- Get **AI-generated explanations, summaries, and study material** tailored to their level
- **Ask questions** and get instant, contextual answers instead of searching endlessly
- Turn raw content (notes, docs, topics) into **organized learning paths**
- Track progress and revisit weak areas efficiently

In short, Learn Verse makes learning **faster, more personalized, and less overwhelming—acting as a smart study companion instead of a static content library.

**Challenges we ran into**

Building Learn Verse came with a few solid challenges:

- **Integrating AI responses smoothly into the UI** — Getting the AI-generated content (explanations, summaries, answers) to render cleanly and update in real time without janky reloads took some trial and error. We solved this by handling responses asynchronously and adding proper loading states.

- **Prompt design for consistent, useful output** — Early on, AI responses were sometimes too generic or off-topic. We iterated on our prompts and added context/constraints to make outputs more relevant and learner-friendly.

- **Managing API rate limits and latency** — Since the app relies on AI calls for core features, we had to think about response times and avoid hitting rate limits during testing. We addressed this by caching common queries and adding debouncing on user input.

- **Balancing simplicity with functionality—We wanted the interface to feel simple ("Add a tagline..." and clean write/preview toggle) while still packing in real learning features, so we had to be intentional about what to include in the first version vs. save for later.

Working through these taught us a lot about building AI-integrated products that feel fast and reliable, not just "smart."

**Best Use of MongoDB Atlas**

Learn Verse uses **MongoDB Atlas** as the core database powering our AI learning studio.

We store and manage key data such as:
- **User profiles and learning progress**, so the platform can adapt content to each learner over time
- **Generated learning material** (explanations, summaries, study paths) from AI responses, structured as flexible JSON documents — a natural fit for MongoDB's schema-less design
- **Chat/query history**, allowing users to revisit past questions and answers

MongoDB Atlas's flexibility let us

**Education**

Learn Verse fits squarely into the **Education** track because it directly reimagines how people learn, using AI as the core engine rather than as an add-on feature.

Instead of static courses or one-size-fits-all content, Learn Verse acts as an **AI-powered learning studio** — turning any topic into structured, personalized study material, answering learner questions in context, and helping people focus on what they actually need to understand next.

By making learning more adaptive, interactive, and efficient, Learn Verse addresses a core challenge in education: **most resources are built for the average learner, not the individual one**. This project aims to close that gap using AI.

**Best Use of Gemini API**

Learn Verse is powered at its core by the **Gemini API**, which drives the AI intelligence behind our learning studio.

We use Gemini to:
- **Generate personalized explanations and study material** from any topic a learner inputs, adapting tone and depth to their level
- **Answer learner questions in real time**, acting as an on-demand AI tutor instead of forcing users to search through scattered resources
- **Summarize and structure raw content** (notes, topics, documents) into organized, digestible learning paths

Gemini's strong reasoning and language capabilities let us build a genuinely adaptive learning experience rather than a static content library — the core promise of Learn Verse. Its speed and quality of responses were essential to making the AI feel like a real study companion, not just a chatbot bolted onto the product.

Team **Code breakers** -- [Sridipta Dutta](https://github.com/Sridipta2004), [Sayan Bhowmik](https://github.com/SayanDev156), [Abhay Kumar Deb](https://github.com/Abhay-krdeb), [Renascence Dey](https://github.com/Rena-code93)

`2026-07-26`

---

### SignVerse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/signverse-0c49) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/razaulshoaib/signVerse-Indian-Sign-Language-Interpreter.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sign-verse-sign-language-interprete-neon.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/mjdOMtuvWk8) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> sign language interpreter

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Mediapipe](https://img.shields.io/badge/Mediapipe-333333?style=flat-square)

**The problem it solves**

Communication barriers between the Deaf/Hard-of-Hearing community and non-sign language speakers remain a major daily obstacle in education, healthcare, workplaces, and public services. Most existing sign language tools are either text-only, clunky, or require specialized hardware.
**SignVerse** bridges this gap by providing an instant, browser-based **Indian Sign Language (ISL) to Text & AI Voice Interpreter**:
- **Real-Time Visual Recognition**: Uses webcam feed and 21-point MediaPipe hand landmark detection to translate sign gestures into text instantly without specialized gloves or depth sensors.
- **ElevenLabs AI Voice Output**: Automatically speaks out recognized signs in natural, human-like English voice so non-signers can listen effortlessly in real time.
- **Multi-Lingual Text Translator**: Live translation of recognized sign text into **Hindi**, **Bengali**, and **Urdu** to support diverse regional language requirements.
- **Zero-Barrier Accessibility**: Runs directly in standard web browsers on laptops, tablets, and mobile devices without installing native apps.

**Challenges we ran into**

⚡ Challenges We Ran Into
1. **Integrating Low-Latency ElevenLabs Text-to-Speech**:
   - *Challenge*: Calling third-party TTS APIs on rapid real-time gesture streams can cause speech overlapping, browser quota exhaustion, or CORS blocks.
   - *Solution*: Designed a dual-layer architecture featuring a Node.js Express proxy `/api/tts` with local fallback to Browser Web Speech API. Implemented sentence tracking so ElevenLabs speaks newly recognized phrases naturally without repeating previous words.
2. **Handling Frame Recognition when Gestures Stop**:
   - *Challenge*: Polling backend endpoints continuously every 2 seconds caused random demo predictions and 502 gateway errors when user hands left the camera frame.
   - *Solution*: Built a real-time client-side hand presence detector using MediaPipe `HandLandmarker`. Recognition requests automatically pause when no hands are in the camera view, keeping the console clean and voice output completely silent when hands stop.
3. **Hand Landmark Overlay & Video Alignment**:
   - *Challenge*: Scaling 21-point hand skeleton coordinates correctly across responsive camera aspect ratios (`object-cover`) on different screen sizes.
   - *Solution*: Developed a custom dynamic scaling offset formula in HTML5 2D Canvas to map MediaPipe normalized coordinates `(x, y)` onto the scaled video element smoothly at 60 FPS.

**Best Beginner's team**

As freshers, we started this hackathon with almost no prior experience in machine learning. From scratch, we collected our own dataset, trained a custom ML model, and achieved **84% accuracy**. Our project addresses a real-world challenge by helping deaf and mute individuals communicate through a **multilingual sign language interpreter**, while also enabling anyone to learn sign language interactively. More than just a technical project, it reflects our determination to learn, build, and create technology that makes a meaningful social impact.

Team **DORA** -- [Rafey KHAN](https://github.com/RAFEY-W), [Hasnain Raza](https://github.com/Na), [Razaul Shoaib](https://github.com/razaulshoaib), [Syed Tabrez](https://github.com/tabrezleo77)

`2026-07-26`

---

### Quickgig
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quickgig-bfdd) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vercel.com/adarsh-prasads-projects-a487a279/quickgigdemo/cxH761FyGT3SzzA1WBpT1FCrBdeG) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> an app dedicated to students to pay their bills

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

faced some bugs in the beginning and then corrected and improved the UI

**The problem it solves**

Quickgig is a web app designed to help students earn their own money to cover some of their collage/university expenses by letting them find part time job opertunities near them easier and faster.
The core idea is a hyper-local gig board where students find short-term work (catering, delivery, event help, retail, tutoring) near them, and small businesses/employers post shifts they need filled fast.

[ADARSH PRASAD](https://github.com/Adarsheey)

`2026-06-28`

---

### CivicEye AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/civiceye-ai-d835) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Piyush4801/CivicEye) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://civiceye-frontend-egxb.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/VU0slghJgWg?si=50XKI0WG3sAkEK6w) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Building Smarter Cities Through AI & Community

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

Building CivicEye AI required solving several technical challenges.

We designed a modular backend architecture capable of handling issue management, AI analysis, trust verification, gamification, and multiple user roles.

Integrating AI-based image analysis, implementing dynamic trust scoring, designing interactive dashboards, optimizing map performance, and ensuring scalability were some of the biggest challenges.

We solved these problems by following a service-oriented architecture, reusable components, optimized database models, and clean TypeScript code.

**The problem it solves**

Cities receive thousands of civic complaints every day, but existing systems suffer from poor transparency, duplicate reports, slow response times, and limited collaboration between citizens, government departments, and NGOs.

Citizens often lose trust because they cannot track the progress of their complaints or know whether any action has been taken.

CivicEye AI solves this by creating an AI-powered civic collaboration platform where issues are automatically detected using AI, verified through trust scoring, routed to the appropriate government departments, and tracked transparently until resolution. NGOs, volunteers, and citizens collaborate together to build smarter and safer cities.

Piyush Sarode

`2026-06-30`

---

### Multilingual Civic Chatbot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/multilingual-civic-chatbot-8f7b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://multilingual-civic-chabot.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> CivicAI: Bridging the language gap between citizen

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Tens of millions of residents face language barriers when trying to access vital local government services. Finding accurate information on applying for ration cards, reporting potholes, or paying utility bills often requires navigating complex, English-heavy government websites. CivicAI bridges this gap by providing an intuitive, multilingual chatbot that acts as a universal, localized civic assistant—democratizing access to real-world government knowledge by answering questions instantly in the user's native language.

**Challenges we ran into**

Initially, the chatbot was hardcoded to a fictional "Metro City" dataset with fake contacts, which completely broke down when users asked about real-world locations (like Tamil Nadu or London). Furthermore, older models were failing to authenticate with our specific API key setup.

How I got over it: I overcame the data limitation by fundamentally restructuring the AI's system prompt. Instead of relying on static local JSON data, I engineered the prompt to instruct the LLM to dynamically detect the user's location from their query and leverage its vast underlying knowledge to fetch real-world government portals and emergency numbers globally. To fix the API issues, I upgraded the backend integration to utilize the latest Gemini 2.5 Flash model, which restored stable API connectivity and drastically improved multilingual response times.

[Sudharson U](https://github.com/sudharson2007)

`2026-06-30`

---

### Cipher runner
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cipher-runner-c8a3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NxSesori/cipher-runner) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cipher-runner.space-z.ai/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/TMQNgW5c_wQ?is=aboba) [![Built at](https://img.shields.io/badge/Built%20at-Tech%20Genesis%20'26-0052CC?style=flat-square)](https://tech-genesis.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Cybersecurity vocabulary learning  game

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

This project helps with learning dry and repetitive technical cyber security vocabulary, while playing a game. This helps people to dive into the cybersecurity filed without boring studying and spending hours on research. By playing the game, they can learn basic terms and concepts, which makes their further research way more efficient, as they will already know basic terms and definitions. This game allows for building a solid base in an entertaining way.
It also worth noting, that the project is orientated more towards a younger demographic, as the game form keeps them engaged and sparks interest among them/

**Challenges we ran into**

We found out, that it is quite difficult to give terms a short definition, that will be both be accurate and easy to undersand and remember.
We had to find a balance between entertainment aspects and actual usefulness.

Team **PyCdez** -- Anton Denisov, Cristina Eimund, Никита Шевченко

`2026-06-26`

---

### CivicOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/civicos-9fef) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OFFICIALHARI/civicos-exchange) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://civicos-flax.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/pINOEvfsdjs) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The Operating System for Community Resources

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Radix UI](https://img.shields.io/badge/Radix%20UI-333333?style=flat-square) ![Zod](https://img.shields.io/badge/Zod-333333?style=flat-square) ![Tanstack Query](https://img.shields.io/badge/Tanstack%20Query-333333?style=flat-square)

**The problem it solves**

Communities already have valuable resources such as parking spaces, EV charging points, shared rooms, and local facilities. The problem is that these resources are often underutilized while people nearby struggle to find and access them when needed.

Most existing solutions only act as simple listing or booking platforms. They show available resources but do not intelligently coordinate supply and demand, optimize allocation, or help communities understand how their resources are being used over time.

CivicOS solves this by creating a centralized operating system for community resources. It enables resource owners to publish availability, allows users to request resources, and automatically identifies the best matches using a real-time allocation engine. The result is better utilization, reduced waste, improved accessibility, and a more efficient local ecosystem.

**Challenges we ran into**

One of the biggest challenges was designing a matching system that felt intelligent while remaining fast and easy to understand. A simple booking flow was not enough, so I developed a scoring-based allocation engine that evaluates factors such as availability, timing, location fit, priority, and resource compatibility before generating matches.

Another challenge was maintaining consistent state across the application. Actions such as creating resources, generating requests, running matches, updating bookings, and recording ledger entries all needed to stay synchronized. I solved this by using TanStack Query together with server functions to ensure reliable data updates throughout the platform.

Building a dashboard that could present resources, requests, analytics, and AI insights without overwhelming users was also difficult. Multiple layout iterations were required before arriving at a structure that balanced information density with usability.

Finally, integrating the AI insights layer required careful design. Instead of generating generic recommendations, I connected the insights system to actual platform activity so that recommendations and forecasts reflect real marketplace conditions.

[HARIKRISHNAN S](https://github.com/OFFICIALHARI)

`2026-06-15`

---

### Student Management
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/student-management-c0e7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://learn.microsoft.com/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A simple Python-based system for managing student

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Managing student records manually can be time-consuming and confusing. This project helps schools and students organize data like student details, attendance, and performance in one place. It makes record management faster, easier, and more efficient.

**Challenges we ran into**

While building this project, I faced challenges in designing the user interface and managing student data correctly. I also had some issues with Python logic and debugging errors, but I solved them by testing the code step by step and learning from online resources.

Pradeep Sahoo

`2026-05-24`

---

### Synap AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/synap-9998) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Kundan730/Synap) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://synap-five.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/2aed1d92cd6948b583a59642bd11e2fa) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Real-Time Visual Intelligence for Learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square)

**The problem it solves**

Most students experience education today as walls of static text, passive video lectures, and chatbots that forget them the moment the tab closes. Real one-on-one tutoring where someone actively draws while explaining, adapts to your confusion, and remembers your weak spots across weeks costs more than most families can afford. AI tutors today aren't a real substitute: they're text in, text out, and stateless.

**Challenges we ran into**

The realtime model would close the socket immediately after setupComplete, dropping the entire session. Diagnosis took several iterations because the same error code masked at least three different root causes: a Modal secret missing in the server environment, a barge-in interrupt that called truncate (which Gemini Live doesn't support), and an out-of-band chatCtx.append racing with generateReply. Fixed by setting realtimeInputConfig.activityHandling = NO_INTERRUPTION so interrupts become a no-op, switching the text-message handler to generateReply({ instructions: ... }) instead of mutating chat context, and adding an agentReady state that gates user actions until the agent's first speaking→listening transition completes.

[Kundan Kumar Sahu](https://github.com/Kundan730)

`2026-05-10`

---

### AskSenior
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/asksenior-5251) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.google.com) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Built by students for students

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

Team **Veer Di Code** -- [Aryan Kumar](https://github.com/Aryxn0608), [Saransh Suman](https://github.com/Saransh-Suman)

`2026-05-10`

---

### Life sync AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/life-sync-ai-054a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dineshpagadala7492/life-sync-ai) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your AI assistant for student life

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Students often struggle to balance academics, schedules, finances, career planning, and personal productivity using multiple disconnected apps. This causes poor time management, stress, and reduced efficiency.

Life Sync AI solves this by combining all essential student and daily life tools into one smart AI-powered platform.

**Challenges we ran into**

During development, we faced challenges in combining multiple modules such as task planning, reminders, finance tracking, and AI recommendations into one smooth workflow.

We solved this by dividing work among team members, creating a modular structure, and integrating features step by step.

**Track: Using BuildWithLocus to leverage our suite.**

Life Sync AI uses BuildWithLocus tools to create a smart productivity platform that combines planning, reminders, automation, and AI-powered assistance in one place.

Our project leverages the Locus ecosystem to build a seamless user experience for students and young professionals managing academics, career goals, finances, and daily tasks.

Team **LEO** -- [Rohit Raaj Anish Lanka](https://github.com/PhantomCoder1000), Aravind_sai_ Reddy, Dinesh Pagadala, Krishna Vamshi

`2026-04-22`

---

### Autopay Agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/autopay-agent-c17a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://svc-moabg1ducfxrqwdo.buildwithlocus.com/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Autonomous payments from natural language.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Cron Scheduler](https://img.shields.io/badge/Cron%20Scheduler-333333?style=flat-square)

**The problem it solves**

## The problem it solves

Sending crypto payments is still harder than it should be.

Even when someone knows exactly what they want to do, like sending a small payment to a wallet or repeating the same payment every week, they still have to go through a bunch of manual steps. They need to open the right wallet, enter the address carefully, type the amount, double-check everything, and remember to do it again later if it’s a recurring payment. That process takes time, creates stress, and leaves a lot of room for mistakes.

AutoPay Agent makes that experience feel much more natural. Instead of treating payments like a technical wallet task, it lets people describe what they want in plain language and have the system turn that into a clear payment action.

## What people can use it for

People can use AutoPay Agent for simple everyday payment tasks, like sending USDC to someone with a short instruction, or setting up recurring payments without having to remember them manually.

It’s especially useful for:

- sending one-time payments faster
- setting up repeat payments like daily, weekly, or monthly transfers
- reducing mistakes when entering payment details manually
- making crypto payments feel easier for people who are not deeply technical
- creating a more natural interface for AI agents that need to manage payments on someone’s behalf

## How it makes things easier

What makes this helpful is not just that it sends payments, but that it removes friction.

Instead of forcing users to think in wallet steps, addresses, forms, and repeated actions, it lets them think in intent. They can simply say what they want to happen, and the app handles the structured part for them.

That makes payments feel:

- easier to start
- easier to repeat
- easier to understand
- and safer to review before execution

In simple terms, AutoPay Agent helps turn crypto payments from a stressful manual process into something that feels closer to talking to an assistant.

**Challenges we ran into**

## Challenges I ran into

One of the biggest challenges was getting the deployment flow working correctly with Locus.

At first, the project would not deploy because the credential we had worked for the **PayWithLocus beta payment API**, but not for the default **BuildWithLocus production deployment API**. That created a confusing situation where payments were working in one environment, but deployment authentication kept failing in another. After digging through the docs and testing the different endpoint combinations, I found that the correct deployment flow for this project had to use the **beta BuildWithLocus endpoints**, not the default production ones. Once I switched the deployment flow to the beta environment, I was able to authenticate, create the project, create the service, and push the app successfully.

Another challenge was that the app kept showing this fallback response:

```json
{
  "success": true,
  "simulated": true,
  "message": "LOCUS_API_KEY is not set. Payment simulated for MVP."
}
```

At first this looked like the API key was missing completely, but the real issue was more subtle. The backend only checked `process.env.LOCUS_API_KEY`, so local runs without injected environment variables would always fall back to simulation even though a saved Locus credential existed elsewhere. I fixed that by improving configuration loading and adding `.env` support for local development, which made the behavior much clearer and removed the misleading “key is not set” path.

I also ran into a deployment timing issue after the app was pushed successfully. The deployment eventually became healthy, but the public service URL briefly returned:

```json
{
  "error": "Service unavailable or not found",
  "host": "...",
  "hint": "The service behind this hostname may be deploying, stopped, or not registered."
}
```

That turned out to be a service-discovery delay rather than a broken deployment. I verified the deployment logs, checked runtime status, and confirmed that the service container was healthy before the public route fully caught up.

On the product side, a separate challenge was the frontend itself. I went through multiple design passes because early versions looked too rough or too generic for a real demo. I rebuilt the UI several times using different frontend design skill directions until it felt clean, focused, and more presentable for a hackathon-quality demo.

Overall, the hardest part of the project was not the basic app logic, it was making sure the **payment environment, deployment environment, runtime configuration, and user-facing experience** all lined up correctly.

Ismail Abubakar

`2026-04-22`

---

### AI Study Planner
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-study-planner-3832) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://canva.link/9ccxqg9pnsug0ig) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-powered personalized study planner for students

![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

Students often struggle to manage their study time effectively and lack structured planning. This leads to poor time management, missed deadlines, and reduced productivity. Existing methods like manual timetables are rigid and not personalized to individual needs.

**Challenges we ran into**

One of the main challenges was designing a simple yet effective solution within a short time. Deciding how to structure the planner and present the idea clearly was difficult. I overcame this by focusing on a minimal approach and creating a basic prototype that demonstrates the core functionality.

**Track: Using BuildWithLocus to leverage our suite.**

AI / Machine Learning

Sindhu Saravanan

`2026-04-23`

---

### AI Academic Agent: Student Productivity System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-academic-agent-autonomous-student-productivity-system-569b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shashank-wd/ai-academic-planner) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-academic-planner-swart.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-DAYZERO%202.0-0052CC?style=flat-square)](https://dayzero2o.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI agent for planning, execution, and optimization

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

**What can people use it for?**

**1. Automated Study Planning**

*Converts syllabus and deadlines into structured study schedules*

**2. Smart Note Generation**

*Summarizes PDFs, lectures, and study materials into concise notes*

**3. Intelligent Reminders**

*Sends proactive alerts for deadlines, exams, and tasks*

**4. Performance Tracking**

*Analyzes study patterns and provides insights for improvement*

**5. Personalized Learning Support**

*Adapts study plans based on user behavior and progress*

___________________________________________________________________________

**How it makes tasks easier**

1. *Reduces manual planning effort*

2. *Eliminates information overload*

3. *Organizes scattered academic data into one system*

4. *Automates repetitive tasks (scheduling, reminders, summaries)*

___________________________________________________________________________
**“Transforms academic management from manual effort into an intelligent, automated workflow.”**
___________________________________________________________________________

![image](https://assets.devfolio.co/content/5df754da77ee4aadbfc70578c9f02ccd/b9cfac68-817f-4caf-914e-a6374766812d.png)

![image](https://assets.devfolio.co/content/5df754da77ee4aadbfc70578c9f02ccd/ef8620ca-5e1f-432a-88a6-ff0e98640db8.png)

**Challenges we ran into**

![image](https://assets.devfolio.co/content/5df754da77ee4aadbfc70578c9f02ccd/80ed777e-a8e0-4e3e-a742-0ec7d60d87b9.png)

![image](https://assets.devfolio.co/content/5df754da77ee4aadbfc70578c9f02ccd/c85d2873-f350-48d8-9187-73acf036d1db.png)

![image](https://assets.devfolio.co/content/5df754da77ee4aadbfc70578c9f02ccd/86f5a8df-0501-403c-b451-f8e0556ba06c.png)

___________________________________________________________________________

**1. ⚙️ Deployment Configuration Issues**
*Render couldn’t detect package.json due to wrong root directory
Build failed initially because backend wasn’t structured correctly for deployment*

**2. 🔌 Backend Runtime Failures**
*Server crashed with “Exited with status 1”
Root cause:
Missing or incorrect environment variables
MongoDB connection failure*

**3. 🗄️ Database Connectivity Issues**
*Incorrect MongoDB URI format
Missing database name in connection string
MongoDB Atlas not allowing external access (IP whitelist issue)*

**4. 🌐 CORS Errors (Frontend ↔ Backend)**
*Frontend hosted on Vercel couldn’t access backend on Render
Caused by:
Default cors() config (too open / not specific)
Missing CLIENT_URL setup*

**5. 🔑 Environment Variable Confusion**
*Confusion between:
Backend env variables (Render)
Frontend env variables (Vercel)
Initially unclear where to place VITE_API_URL*

**6. 🔗 Frontend–Backend Integration Issues**
*API calls still pointing to localhost
Required replacing with deployed backend URL*

**7. 🔒 Security Oversights**
*Sensitive data (MongoDB credentials) exposed during setup
Logging environment variables in production*

**8. 🧪 Debugging Challenges**
*Limited error logs initially made debugging harder
Needed to improve logging for MongoDB connection errors*

Team **Byte4Life** -- Shreyash Mishra, [Aditya Pandey](github.com/devSin8), [Shashank Bhadoriya](www.github.com/shashank-wd), [Aniruddha Verma](https://github.com/N0VACHR0NO)

`2026-04-17`

---

### Society help Page
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/society-help-page-f2ee) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://society-one-kohl.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "The Digital Backbone of Your Community."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square)

**The problem it solves**

Manually tracking who has paid maintenance and providing receipts is a common headache for society secretaries.

The Solution: The Member Portal allows residents to "pay maintenance" and "view notices" in real-time, creating a clear digital trail and reducing disputes over payment history.

**Challenges we ran into**

**. Architectural & Logic Challenges
Role-Based Access Control (RBAC): One of the biggest hurdles is ensuring a Member cannot access Admin routes (like /admin-panel) by simply typing the URL. You had to implement middleware or logic to check user roles before rendering pages.

State Management: Keeping the UI updated across two different panels. For example, when an Admin approves a request, the Member panel needs to reflect that "Approved" status immediately without a manual database refresh.

2. Technical Development (The "BCA Grind")
Frontend-Backend Integration: Since you've worked with Flask and HTML/CSS/JS before, connecting your Vercel-hosted frontend to a live database (like MongoDB or Firebase) and ensuring the API endpoints were secure and responsive was likely a challenge.

Responsive Design: Society members will use this on phones, while admins might use it on laptops. Making those complex tables (like maintenance logs) look good on a 6-inch screen is a classic CSS Flexbox/Grid struggle.

3. Data Integrity & Security
Input Validation: Dealing with "dirty data." You had to ensure that when a member raises a complaint, they can't inject malicious code (SQL injection or XSS) into your database.

Session Management: Handling logins so that a user stays logged in while browsing but gets logged out for security after a certain period of inactivity.

4. Feature-Specific Logic
Maintenance Calculation: Coding the logic for "pay maintenance." You had to handle scenarios like partial payments, late fees, or generating digital receipts, which requires precise math and date-handling in JavaScript or Python.

Broadcast Filtering: Ensuring that a broadcast sent by the Admin actually reaches the right "Members" and doesn't get lost or sent to other Admins by mistake.

[Dhairya Gulati](https://github.com/dgulati352-cpu)

`2026-04-11`

---

### SmartAid
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartaid-c73d) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-based app to help students study faster

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Students often struggle with managing study time, understanding concepts, and staying consistent. Many existing tools are complicated or not personalized, making learning inefficient.

**Challenges we ran into**

We faced challenges in designing a simple and user-friendly interface while integrating AI features. Managing time and planning features effectively was also difficult.

**Using PayWithLocus.com to leverage our suite.**

AI / Machine Learning
Or Productivity / Education

Aman Choudhary

`2026-04-12`

---

### LIBRE METRO
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/libre-metro-1a7c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://otzua.in) [![Built at](https://img.shields.io/badge/Built%20at-Matrix%203-0052CC?style=flat-square)](https://matrix-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A community driven METRO service

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![LocationServices](https://img.shields.io/badge/LocationServices-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Metro systems like Delhi Metro are widely used, but existing apps and websites only provide official routes, which are often not the most convenient in real-life situations. These routes may involve unnecessary interchanges, long walking distances, or crowded segments, making daily travel uncomfortable—especially for students, new commuters, and tourists.

A major gap is the absence of community-driven insights. Regular commuters often know better, more practical routes (for example, fewer interchanges or higher chances of getting a seat), but there is no platform where these optimized routes can be shared or accessed.

Additionally, current solutions lack:
	•	Personalized guidance for different users (students, tourists)
	•	Accurate “nearest metro” detection based on real location
	•	Clear step-by-step navigation including direction and platform details
	•	Fare comparison (smart card vs ticket, discounts, etc.)
	•	Discovery features like nearby food spots or useful stops

As a result, users rely on trial-and-error or word-of-mouth to find better routes.

Libre Metro solves this by combining official data with real user experience, creating a smarter, more practical metro navigation system focused on comfort, efficiency, and personalization.

**Challenges we ran into**

Building Libre Metro came with several practical and technical challenges.

One major issue was data inconsistency between APIs and our internal dataset. Metro station names were not always formatted the same (for example, spacing differences like “Vishwavidyalaya” vs “Vishwa Vidyalaya”), which caused route search failures. I resolved this by implementing a normalization system that ignores case, spaces, and special characters, ensuring consistent matching across the app.

Another challenge was accurate nearest metro detection. Initial implementations using browser geolocation were not precise enough and often returned incorrect stations. This was improved by comparing user coordinates with our own dataset of metro stations using distance calculations, making the results more reliable.

Designing the community-driven route builder was also complex. Allowing users to input custom routes while automatically filling intermediate stations required careful logic using ordered station data. This was solved by mapping station sequences and dynamically generating routes between selected points.

Additionally, implementing real-world navigation features like direction (towards terminal stations), interchanges, and platform guidance required structuring route data in a more meaningful way instead of just listing stations.

Finally, maintaining a consistent UI/UX using neo-brutalism design while continuously adding new features was challenging. Care was taken to enhance functionality without breaking the visual consistency of the application.

Overall, these challenges helped improve both the technical robustness and real-world usability of the project.

**Grand Cash Prize Pool – ₹50,000**

Libre Metro fits this track by addressing a real-world, large-scale problem faced by millions of daily metro commuters. It combines practical utility with modern technology to improve how people navigate public transport systems.

The project goes beyond traditional metro apps by introducing a community-driven layer, where users can share and discover more efficient and comfortable routes based on real experience, not just official data. This directly improves commuting efficiency, reduces travel friction, and enhances user comfort.

From a technical perspective, the project integrates:
	•	Real-time location-based features (nearest metro detection)
	•	Smart route processing and visualization
	•	Structured navigation guidance including direction and interchanges
	•	Dynamic UI/UX built for mobile-first usage

Additionally, Libre Metro focuses on scalability and real-world impact. While currently implemented for Delhi Metro, the system is designed to expand to other metro cities, making it adaptable and widely applicable.

By combining community intelligence, structured data, and intuitive design, Libre Metro aligns strongly with the goals of this track—building practical, impactful solutions using technology.

Team **NOOBS** -- [Krish singh](https://github.com/otzua), shubham .k

`2026-04-07`

---

### Learnova
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/learnova-a9cb) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://antara0619.github.io/LEARNOVA/) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> “Learnova – Where Learning Meets Innovation.”

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

Learnova is an AI-powered smart learning platform that solves the problem of scattered and inefficient studying by providing a personalized, interactive, and all-in-one learning experience. With features like smart recommendations, progress tracking, and gamified learning, Learnova transforms the way students learn—making it faster, smarter, and more engaging.
Learnova Solution
Learnova = One Smart Learning Hub.
 All-in-one platform for videos, PDFs, quizzes, and notes.
🧠 Personalized learning paths based on user goals.
📊 Progress tracking dashboard to monitor growth.
🔔 Smart reminders for consistency.
💬 Interactive chatbot for instant doubt solving.
Your personal learning assistant, anytime, anywhere.
From confusion to clarity in one platform.

**Challenges we ran into**

Challenges We Faced While Building Learnova
1. 🔄 Integrating Multiple Learning Resources
Bringing together videos, PDFs, and quizzes in one place was difficult.
Different formats required different handling (embedding, file storage, UI display).
Ensuring smooth loading without slowing the website was a challenge.
2. 🤖 Implementing AI Chatbot
Creating a smart chatbot was not straightforward.
Understanding user queries accurately was tough.
Maintaining fast response time while keeping answers relevant required optimization.
3. 🔐 Authentication & Login Issues
Handling user login/signup was one of the major problems.
Errors in authentication logic caused login failures.
Managing sessions and user data securely was complex.
4. 📊 Progress Tracking System
Tracking student performance in real time was challenging.
Needed to store and update user data dynamically.
Designing a simple yet meaningful dashboard took effort.
5. 🎨 UI/UX Design Balance
Making the website both attractive and user-friendly was tricky.
Too many features made the UI cluttered.
Simplifying navigation while keeping it modern required multiple redesigns.
6. ⚡ Performance Optimization
Website speed became an issue due to heavy content.
Large videos and files slowed down loading.
Required optimization techniques like lazy loading and compression.

Team **Learnova** -- [Aashtha Kumari](https://github.com/Aashtha2405), [Antra Srivastava](https://github.com/ANTRA123-STACK), [Antara Dutta](https://github.com/antara0619), [Ankita Chandra](https://github.com/Ankita-code77)

`2026-04-05`

---

### ThinkMate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/thinkmate-db9b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/itsmeayan45/ThinkMate2) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/6vrS7kj7idg) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-powered learning, designed to focus.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

The problem it solves:
Students and teachers often use disconnected tools for notes, doubt-solving, exams, and performance tracking. This leads to slow learning, repeated manual work, and poor visibility into student progress.

What people can use it for:
ThinkMate is an AI-powered learning platform where students can learn from uploaded study materials, ask instant doubts, and practice exams in one place, while teachers can manage content and track analytics.
It makes studying faster, revision more focused, and teaching workflows easier by combining everything into a single system.

**Challenges we ran into**

Challenges I Ran Into
One major hurdle was making the AI chat reliable with uploaded documents.
At first, responses were either too generic or missed context because the retrieval pipeline was not consistently returning the most relevant chunks.

What was going wrong
Document chunks were uneven, so important points got split badly.
Embedding/vector settings were sensitive, and small config mismatches hurt retrieval quality.
Network/API failures sometimes interrupted the flow and created inconsistent user experience.
How I fixed it
Tuned chunk size and overlap so context stayed meaningful during retrieval.
Standardized embedding + vector index configuration and re-indexed documents.
Added stronger error handling and fallback responses so chat didn’t break on transient failures.

**Best Use of MongoDB**

ThinkMate uses MongoDB as the core data layer for both application data and AI retrieval workflows, which directly aligns with the “Best Use of MongoDB” track.

Why MongoDB is a strong fit here
Flexible schema for evolving edtech data: Users, courses, documents, chat history, and exam records all have different shapes and change frequently during development.
Single database for product + AI context: MongoDB stores standard app entities and powers document-grounded AI through vector storage.
Fast iteration for hackathon speed: MongoDB Atlas let us quickly move from prototype to working cloud deployment without complex infra setup.
How MongoDB is used in this project
Core collections: student/teacher accounts, courses, uploaded document metadata, chat sessions, exam interactions, and analytics signals.
Vector search pipeline: processed document chunks are embedded and stored in a MongoDB vector collection, enabling semantic retrieval for course-aware Q&A.
Scalable cloud setup: Atlas provides managed hosting, indexing, and reliability needed for multi-user classroom-style usage.

Team **KernelPanic** -- [Rupsa Adhikary](https://github.com/Rupsa004), [Swapit Biswas](https://github.com/swapitbiswas/), [Swarnadip Sen](https://github.com/swarnadipsen/), [Ayan Guchhait](https://github.com/itsmeayan45)

`2026-04-05`

---

### SkillEx
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skillex-85ad) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VanshikaCharak/SkillExchange/tree/main) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://skill-exchange-riyn.vercel.app/dashboard) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A communal skill exchange community for learners.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Learners no matter the stage they are in,  face a constant issue of finding reliable and tried and tested resources for their learning journey. We try to solve that issue by building a community where learners can exchange high quality verified resources, teach other skills they are proficient in, build their resume and even get 1:1 mentorship. How it is different from the widely available free resources on the net is that, the resources are never ending, and our opinions are influenced mostly based on the people we interact with, but having someone experienced guide you in the skill you want to master, that they have themselves learned, narrows down the infinite resources present on the internet, to few reliable and trusted resources. Which is quite the headache among learners of all ages trying to master something new.

**Challenges we ran into**

So our team being fully comprised of first year students with little knowledge about actual deployment, our biggest hurdle was to deploy the app using Vercel. We built our repository quite fast on GitHub, but we faced numerous challenges during integration of different aspects of the project that were being handled by each teammate. Syncing the code across all the machines uniformly, was quite the headache. After integrating, we faced huge issues while deploying. Even after manually parsing through the whole repository and taking help of various resources, the deployment was challenging. As it was our first time integrating and deploying an actual project.

**Women Track: The Queen’s Vanguard**

All team members are females and belong to the First Year Batch at NITJ. Hence, this project is a perfect fit for the aforementioned track.

Team **Tech Gurlies** -- [Aruta Kochey](https://github.com/arutakochey-sketch), [Akashita .](https://github.com/akashita08), [Vanshika Charak](https://github.com/VanshikaCharak), [Sehaj Modi](https://github.com/SehajModi)

`2026-03-29`

---

### EduLite
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edulite-b3b6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/elambarathi-C/EduLite-OS) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/oOsOXlwwwbY) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Education for everyone

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Large Language Models usually require expensive GPUs and 16GB+ of RAM. Most donated or low-cost laptops in schools have only 2GB of RAM.
	EduLite Solution: Through extreme optimization and 4-bit quantization, it shrinks a massive AI brain to fit into a tiny ~700MB memory footprint, reviving older "e-waste" laptops into powerful tutoring stations.

Most modern AI tutors (like ChatGPT or Gemini) require a constant, high-speed internet connection. In rural or underserved areas, "digital learning" often stops the moment the signal drops.
	EduLite Solution: It runs 100% offline. All AI inference and textbook processing happen on the local hard drive, making education "signal-independent."

Generic AI models often make up facts or use curricula from different countries.
	EduLite Solution: By using RAG (Retrieval-Augmented Generation), the AI is "grounded" in local NCERT/CBSE PDFs. It doesn't just guess; it "reads" the specific textbook provided to give accurate, syllabus-aligned answers.

**Challenges we ran into**

Cubic silent failure on Ubuntu 24.04 was the first major hurdle — the sudo password dialog never appeared due to a policykit-1 vs polkitd incompatibility. Fixed it by installing a patched community .deb and launching with sudo cubic.

ChromaDB failed silently during pip install because the Ubuntu VM defaulted to Python 3.12, which was incompatible at the time. Resolved by installing Python 3.11 via the deadsnakes PPA and recreating the virtual environment.

EduLite service crashed on boot because systemd started Flask before Ollama finished loading. Fixed by adding After=ollama.service, Restart=on-failure, and RestartSec=5 to the service unit file — ensuring the app retried automatically.

Each bug taught us something real about Linux service management, dependency pinning, and OS-level deployment that no tutorial had covered.

**IoT & Smart Devices**

EduLite is a lightweight AI-powered education OS designed to run on low-cost, resource-constrained school computers — devices that share the same core challenge as IoT hardware: doing meaningful computation with minimal resources.

The system runs a locally deployed TinyLlama AI model via Ollama entirely on-device, with no cloud dependency. This mirrors the edge-computing model central to smart IoT deployments, where data is processed locally rather than sent to external servers — critical in schools with unreliable internet.

The OS is packaged as a custom bootable Ubuntu image, meaning any bare-metal machine can become a smart educational device simply by booting from a USB — essentially turning ordinary school PCs into purpose-built smart learning terminals.

Team **Exotic coders** -- [Adarshini Raju](https://github.com/adarshinimapraju), [Rokith Sathyamoorthy](https://github.com/rokithsathyamoorthy-prog), [Elambarathi C](https://github.com/elambarathi-c), [Haripriya Srinivasan](https://github.com/Haripriya-15-06)

`2026-03-29`

---

### Vidyarthi Saarthi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vidyarthi-saarthi-32d0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/monojitgoswami69/frosthacks) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> why keep learning exclusive to classrooms?

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![sentence-transformers](https://img.shields.io/badge/sentence--transformers-333333?style=flat-square) ![hugging-face](https://img.shields.io/badge/hugging--face-333333?style=flat-square)

**The problem it solves**

* Students frequently encounter course-specific doubts outside regular class hours when faculty or teaching assistants are unavailable.
* Existing general-purpose AI tools provide overly broad or context-agnostic responses, often relying on external knowledge instead of prescribed academic materials.
* These systems may directly provide answers without guiding the learning process, reducing conceptual understanding and encouraging passive learning.
* Lack of a structured, course-aware support system leads to repeated queries being handled manually by faculty, increasing their workload.
* Students do not have a reliable way to verify whether answers are grounded in their official lecture notes, textbooks, or curriculum.
* There is limited visibility for instructors into common areas of student confusion, making it difficult to adapt teaching strategies.
* Ensuring academic integrity and maintaining student privacy in digital doubt-solving systems remains a challenge.

**Challenges we ran into**

* Ensuring strict **context grounding** so the model answers only from uploaded course materials and does not rely on external knowledge.
* Designing a reliable **retrieval pipeline (RAG)** with accurate chunking, embeddings, and similarity search to minimize irrelevant results.
* Handling **edge cases in queries** where student questions are vague, multi-topic, or partially outside the provided context.
* Implementing **Socratic response behavior**, forcing the model to guide rather than directly answer, which conflicts with default LLM tendencies.
* Maintaining **high citation accuracy**, ensuring every response correctly references source documents (page, lecture, etc.).
* Balancing **latency vs accuracy**, especially when using vector search + LLM generation under real-time constraints.
* Managing **document preprocessing issues** (PDF parsing errors, inconsistent formatting, noisy text extraction).
* Preventing **hallucinations**, especially when relevant context is weak or missing.
* Designing a scalable system without **expensive infrastructure**, while keeping it responsive under load.
* Ensuring **student privacy** while still logging queries for analytics and faculty insights.
* Creating a flexible system that supports **dynamic filtering (course, semester, topic)** without degrading search performance.
* Integrating multiple components (LLM, vector DB, backend, frontend) into a **stable, production-ready pipeline**.

**EDUCATION**

***How It Fits the Education Track***

* Provides a **course-specific AI tutor** that delivers personalized academic support aligned strictly with official lecture materials and curriculum.
* Enhances **conceptual learning** by using a Socratic approach, guiding students through reasoning instead of giving direct answers.
* Enables **24/7 doubt resolution**, reducing dependency on faculty availability and improving learning continuity.
* Reduces **faculty workload** by automating repetitive queries while still maintaining academic rigor through grounded responses.
* Improves **learning transparency** by including citations from lecture notes and textbooks, helping students verify and trust answers.
* Generates **actionable insights for educators** by analyzing common student queries and identifying areas of confusion.
* Promotes **academic integrity** by preventing blind answer generation and ensuring responses are context-bound.

Team **Runtime Terrors** -- [Monojit Goswami](https://github.com/monojitgoswami69), [Prabrisha Das](https://github.com/Pdas2506), [PIYALI CHAKRABORTY](https://github.com/PIYALI2025)

`2026-03-28`

---

### RuralDev
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ruraldev-188d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ARPANkundu2404/RuralDev) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/S6bKmjLxMb4) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> From Village Roots to Global Routes

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

In rural areas, people have skills:
Pottery, Embroidery, Origami, Handicrafts
But they face major issues:
❌ No direction on how to earn
❌ No trust in buyers/sellers
❌ High fraud (fake workshops, low-quality products)
A trust-driven platform that transforms rural skills into sustainable income using AI-based job recommendations, verified workshops, and a fraud-resistant marketplace.

**Challenges we ran into**

The biggest challenges in our system are data scarcity, fraud detection complexity, and integrating AI recommendations with real-world rural economic behavior. We addressed these using hybrid approaches combining rule-based logic, machine learning, and admin verification.

Team **Electrocoders** -- [Anubhab De](https://github.com/anubhab1001), [Avrajit Dey](https://github.com/Avrajit-718), [Arpan Kundu](https://github.com/ARPANkundu2404)

`2026-03-22`

---

### voice first digital access for financial inclusion
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/voice-first-digital-access-for-financial-inclusion-8785) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yuvashree5806-hub/VoiceFirstDigitalAccessBanking) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vaaniaccess.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/7220b7512f374f03a5ec5f7e5c26b9b8) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> VoicePay: Speak to Spend, Speak to Save

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Voice-First Multilingual Financial Inclusion Platform

1. The Core Problem

Digital banking and government welfare systems today suffer from an Inaccessibility Gap. Most platforms are designed for the "average" user—someone who is literate, tech-savvy, and possesses full physical dexterity.
This excludes millions from the global financial ecosystem:
Literacy Barriers: 25% of the global population struggles with functional literacy, making text-heavy banking apps impossible to navigate.
Cognitive & Physical Hurdles: Elderly users and Persons with Disabilities (PwDs) often find complex menus, small buttons, and rapid-fire OTP/PIN entries stressful or physically impossible.
The "Middleman" Trap: Because these users cannot use digital tools independently, they rely on third parties (family, neighbors, or agents), which leads to financial exploitation, loss of privacy, and fraud.

2. What People Use It For
Our platform transforms the mobile phone into a Voice Companion that understands intent rather than just commands.

A. Independent Banking
Balance Inquiries: A user can simply ask, "How much money do I have left?" in their native dialect.
Money Transfers: Instead of typing account numbers, a user says, "Send five hundred rupees to my daughter for her school books."
Bill Payments: Making utility payments via voice without navigating nested service menus.

B. Welfare & Scheme Accessibility
Eligibility Checks: Users can ask, "What government schemes am I eligible for as a senior citizen?"
Enrollment: Applying for benefits by answering spoken questions rather than filling out complex digital forms.

C. Financial Literacy & Planning
Spending Insights: Users receive audio-based advice like, "You spent more on groceries this month than usual. Would you like to save some money for your medicine next week?"

**The Impact**

By moving the interface from the Eyes/Hands to the Voice/Ears, we achieve:
Dignity: Users manage their own money without asking for help.
Reach: Banks can serve rural populations without building physical branches.
Transparency: Direct-to-beneficiary transfers eliminate "leakage" in government welfare systems.

**Challenges we ran into**

Challenges & Hurdles

Building a voice-first fintech solution presented several unique technical and design obstacles:

A. Handling Intent Over Syntax
The Bug: Initial versions used rigid keyword matching. If a user said "Send money" instead of "Transfer funds", the system failed.
The Hurdle: Natural human speech is messy, especially in rural dialects.
The Fix: We integrated the Gemini API to act as a semantic interpreter. Instead of looking for words, the LLM extracts the intent and entities (Amount, Recipient) regardless of the phrasing or slang used.

B. The "Code-Switching" Problem
The Bug: Standard Speech-to-Text (STT) engines struggled when users mixed languages (e.g., mixing Hindi with English technical terms like "Transfer" or "Balance").
The Fix: We implemented a hybrid prompt engineering strategy with Gemini that explicitly instructs the model to recognize "Hinglish" and regional variations, ensuring the AI maintains context even when the language shifts mid-sentence.

C. Latency and User Trust
The Hurdle: In voice interfaces, a 2-second delay feels like an eternity. Users often wonder if the app crashed, leading to repeated commands and errors.
The Fix: We designed a "Cognitive Feedback" system. We added real-time visual waveforms and "Thinking" haptics/animations that trigger immediately upon voice detection, providing instant reassurance while the API processes the request.

5. The Impact

By moving the interface from the Eyes/Hands to the Voice/Ears, we achieve:
Dignity: Users manage their own money without asking for help.
Reach: Banks can serve rural populations without building physical branches.
Transparency: Direct-to-beneficiary transfers eliminate "leakage" in government welfare systems.

Team **falcon** -- [JAY CHANDRA](https://github.com/JC-29068), [Yuvashree M](https://github.com/Yuva-2006-del), [Tejeshwar p](https://github.com/teju-1024)

`2026-03-17`

---

### KinetixVerse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/kinetixverse-2c4e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ramanbansal1/KinetixVerse) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Making Robot learning easy

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SAM3D](https://img.shields.io/badge/SAM3D-333333?style=flat-square) ![RERUN](https://img.shields.io/badge/RERUN-333333?style=flat-square) ![MUJOCO](https://img.shields.io/badge/MUJOCO-333333?style=flat-square)

**The problem it solves**

Robotics systems trained in simulation often fail when deployed in the real world. This is known as the **sim-to-real gap**.

Traditional robotics development relies on controlled laboratory environments and manually created simulation scenes. These simulations rarely capture the variability and complexity of real-world environments.

Key limitations of current approaches:

* Training cycles typically take **6–12 months**.
* Building robotics lab infrastructure can cost **$500K–$2M+**.
* Only **~15% of universities** have access to advanced robotics facilities.
* Most simulations cover **less than 30% of real-world scenarios**.

At the same time, the internet contains **billions of videos showing real-world interactions**, but almost none of this data is used for robotics training.

This creates a massive opportunity to convert real-world video data into training environments.

**Challenges we ran into**

One major hurdle we encountered while building KinetixVerse was maintaining stable object tracking across video frames when converting videos into simulation environments. In our early pipeline using YOLO segmentation and tracking, we observed issues such as mask area spikes, sudden centroid jumps, and identity switches where the same object would be assigned different IDs across frames. These inconsistencies caused incorrect trajectories and made downstream modules like pose estimation and physics prediction unreliable. To overcome this, we implemented several stabilization techniques, including filtering out frames with abnormal mask area changes or large centroid movements, adding embedding-based re-identification using DINOv2 with FAISS to maintain consistent object identities, and storing tracking history in a lightweight database to preserve temporal context. These improvements significantly stabilized object trajectories and allowed us to generate reliable motion data for physics-aware simulation.

**Electrothon 8.0 Winners**

KinetixVerse fits strongly within the **AI/Robotics innovation track of Electrothon** because it addresses a real and well-known robotics challenge: the **sim-to-real gap**, where robots trained in simulation fail in real-world environments. The project introduces a novel pipeline that converts **real-world videos into physics-aware 3D simulation environments** using technologies like object detection, segmentation, scene reconstruction, pose estimation, and physics engines such as MuJoCo. This allows robotics developers to generate training environments in **hours instead of months**, significantly reducing cost and development time. The combination of **deep technical complexity, real-world impact, scalability, and a strong visual demo (video → simulation → robot training)** aligns well with the key judging criteria of Electrothon, making it suitable for the **innovation and advanced AI systems category that typically produces winning projects**.

**IQ AI**

In KinetixVerse, we used IQ-AI to estimate the physical behavior of objects directly from video, enabling the system to understand how objects move and interact in the real world. Modern AI systems can analyze video sequences and infer underlying physical dynamics such as motion, collisions, and object interactions, rather than only recognizing visual appearance. Research in video-based physics reasoning shows that AI models can learn to predict object trajectories and interactions by observing frames over time, effectively learning the rules of dynamics from visual data.For example, recent work on physics-aware video benchmarks demonstrates that AI systems must understand principles like solid mechanics, fluid dynamics, and motion to accurately predict what will happen next in a sceneUsing this idea, IQ-AI in our pipeline analyzes tracked objects in the video and predicts their physical properties—such as motion patterns, interactions, and dynamic behavior—which are then integrated into our simulation engine to produce physics-consistent environments for robotics training.

**Google Cloud**

We leveraged the Gemini API on Google Cloud and integrated it with ADK and IQ-AI to enhance physics estimation in our video-to-simulation pipeline. Gemini provides multimodal scene understanding that helps interpret object interactions, contextual relationships, and motion cues from video frames. This contextual intelligence is combined with IQ-AI’s physics inference module, allowing our system to estimate how objects behave and interact in the real world. By using Gemini’s reasoning capabilities alongside our computer vision and tracking pipeline, we were able to generate more accurate and physics-consistent simulations from real-world video data.

**Best Use of Gemini 3 [Google Deepmind]**

We used the Gemini API in combination with ADK and IQ-AI to enhance physics estimation from video by providing high-level scene understanding and reasoning about object interactions. While our computer vision pipeline detects, segments, and tracks objects, Gemini helps interpret the context of the scene—such as how objects interact, whether they are static or dynamic, and what type of physical behavior they exhibit. This contextual reasoning is passed to the IQ-AI physics module, which uses it to better estimate motion patterns and interaction dynamics. By integrating Gemini’s multimodal understanding with our physics inference pipeline, we were able to generate more realistic and physically consistent simulations from real-world video data.

Team **DEV.HUNTERS** -- [Khushvinder Thakur](https://github.com/thakursanju), [Mridul Ahluwalia](https://github.com/Mridul-Ahluwalia06), [Raman Bansal](https://github.com/ramanbansal1), [Pradyuman Sharma](https://github.com/its-me-meax)

`2026-03-15`

---

### Campus Link
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-link-d1f7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chetan208?tab=packages&repo_name=Electrothon-Backend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://campuslink-tawny.vercel.app/login) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/EXYAqNwiezI) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> your AI powered student network

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

College students today struggle with a fragmented experience — WhatsApp groups are chaotic, LinkedIn feels too corporate, and there's no platform built specifically for verified college students to connect, collaborate, and grow together.

**CampusConnect solves this by:**

- **Verified identity** — only students with college email domains can join, eliminating fake profiles
- **Smart connections** — an AI-powered recommendation engine suggests people based on mutual connections, shared skills, same college, and common interests — not just random people
- **Personalized AI assistant** — CampusBot answers any question like ChatGPT, but also fetches real student profiles when learning help is needed ("mujhe React sikhna hai" → roadmap + relevant students to connect with)
- **Daily opportunity alerts** — an AI agent scans the internet daily and sends each student a personalized notification for internships, hackathons, and fellowships matching their exact profile
- **Real-time feed** — post updates, ask questions, share projects — and get notified when your connections post something new
- **One platform** — profile, posts, connections, chat, search, and AI — all in one place built for students

**Challenges we ran into**

**1. Zod version conflict with ADK-TS**
ADK-TS internally uses Zod v4 but our project had Zod v3 installed. This caused a `Cannot read properties of undefined (reading 'def')` crash at runtime. Fixed by upgrading to `zod@4`.

**2. Gemini passing wrong userId to tools**
The AI agent was reading `Name: chetan` from the system prompt and passing `"chetan"` as userId to MongoDB queries instead of the actual ObjectId — causing `Cast to ObjectId failed` errors. Fixed by moving tools inside `getCampusAgent()` as closures so `userId` came from JavaScript scope, not from Gemini's interpretation.

**3. Duplicate AI responses**
Gemini would write the full answer, call the tool, then rewrite the entire answer again with tool results appended — resulting in duplicate content. Fixed with explicit `CRITICAL: Write everything ONCE` instructions in the system prompt.

**4. Daily agent suggesting same opportunity to all users**
The AI was defaulting to "Google Summer of Code" for every student regardless of their profile. Fixed by building profile-specific prompts using `preferredType` (hackathon/internship/open source) derived from each student's `openTo` field, and explicitly blocking generic suggestions unless they genuinely matched.

**5. Regex crashing on C++ skill**
MongoDB regex queries with `C++` caused `Invalid regular expression: /C++/i: Nothing to repeat` because `+` is a special regex character. Fixed with a `safeRegex()` function that escapes all special characters before building the regex.

**6. Stacking context blocking chatbot overlay**
The floating chatbot had `z-index: 9999` but was still appearing behind the navbar because a parent component created a new stacking context. Fixed using `createPortal` to render the chatbot directly into `document.body`.

**7. Real-time notification architecture**
Building a notification system that handled both friend post triggers (event-driven) and daily AI opportunity alerts (cron-based) while keeping the frontend in sync required combining `node-cron`, MongoDB `insertMany`, and a 30-second polling interval on the frontend.

**Requestly Track**

we have used  requestly to test our Apis

**IQ AI**

we have used IA ai to build ai chat bot

**n8n**

i have used n8n to build ai agents

**Best Use of Gemini 3 [Google Deepmind]**

we have user gemini api

Team **Team Phantom** -- [Anuj Keshri](https://github.com/anujkeshri7), [Abhishek .](https://github.com/abhishek1343), [Arpita Soni](https://github.com/arpita-1111), [CHETAN .](https://github.com/chetan208/)

`2026-03-15`

---

### Spindle AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spindle-ai-ce15) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/roshanr2902-cmyk/Parallax) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Solves every problem of a student

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Fixing bugs

**The problem it solves**

The problem:
During an emergency, people may panic, waste time figuring out whom to contact, or struggle to communicate their location and situation quickly.

Your project can solve this by providing:

🚨 One-tap SOS — quickly trigger an emergency alert.
📍 Location sharing — communicate the user's location to trusted contacts/responders.
👥 Nearby-person detection — identify people nearby who could potentially assist.
🕸️ Emergency dashboard — put critical information and actions in one place.
🤖 AI assistance — guide the user through appropriate next steps based on the situation.
📱 Simple interface — minimize the number of actions needed when someone is stressed.
The strongest one-line pitch

“Spider-Web is an AI-powered emergency assistance platform designed to connect people in distress with trusted contacts and nearby help as quickly as possible.”

Team **Parallax** -- Sanjey Vell, U ShrutilayaU, B Srusty, Rithuvarnikha S, Roshan R

`2026-09-02`

---

### Thiran AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/thiran-ai-aad8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VK210607/thiranAI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/maiHnuHorqA) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> BRIDGING GAP BETWEEN STUDENTS AND MARKET REALITY

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Data Acquisition and  Debugging LLMs.

**The problem it solves**

Most student career platforms push toxic leaderboards, comparative percentile rankings, and shallow progress bars that induce anxiety rather than fostering genuine mastery. Furthermore, milestone completion is typically an unchecked honor system where any link is blindly accepted.

ThiranAI re-engineers career preparation around pure personal mastery and verifiable proof of work:

Zero Peer Comparison: No public ranks, percentiles, or leaderboards. Every student competes only against their own previous milestone.
Adaptive Discovery: Discovers authentic domain alignment through scenario-based aptitude dilemmas rather than generic multiple-choice quizzes.
Real AI Proof Verification: Powered by Google Gemini 2.5 Flash, student project submissions (GitHub repositories and technical notes) are audited against expected deliverables before milestone credit is awarded.
Guilt-Free Diversion Detection: Intelligently detects if a student’s interests are naturally pivoting to another domain and offers friction-free roadmap realignment.

Team **Bugheads** -- Vishalini V, G VARSHA, [Udith Anand](https://github.com/no), Vethavarna S B, [Vijay Kiran](https://github.com/VK210607)

`2026-09-02`

---

### EduSight AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edusight-ai-9032) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/divyamanitiwaridmt94-rgb/EduSightAI) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co)

> An AI-powered mobile app that helps blind students

![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square)

**Challenges we ran into**

The biggest challenge was implementing a camera layout that a blind person could handle independently. Since they cannot see the viewfinder, making an automatic image frame lock based on edge boundaries and tuning the haptic vibration speeds in real-time was very tricky. I resolved this by utilizing asynchronous programming states in Flutter to handle constant view stream calculations smoothly without freezing the UI.

**The problem it solves**

Regular classrooms are completely visual. When teachers write notes or explain complex equations on the whiteboard, blind or visually impaired students face a huge learning barrier. They cannot see the board in real-time and have to constantly rely on friends or manual scribes to take notes for them.

EduSight AI solves this by turning visual boards into instant speech. It gives audio-vibrational guidance so blind users can frame their camera independently. Once the board is centered, it snaps the photo automatically, uses Google Gemini API to read the text/diagrams, and reads the notes aloud using a Text-to-Speech engine.

[Divyamani Tiwari](https://github.com/divyamanitiwaridmt94-rgb)

`2026-08-20`

---

### SpeakSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/speaksense-91b4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Zharif18/speak_sense) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/hWWZFKyCxmo) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> A students product for students

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Pinpointing Meaningful Differentiation: In a crowded landscape of basic transcription and speech-timer apps, our initial hurdle was moving beyond surface-level speech-to-text metrics. We realized that speaking effectively isn't just about what you say, but how your body and mind react under pressure. Deciding how to cleanly integrate distinct layers—low-latency voice processing, body language tracking, and wearable heart-rate metrics—without overwhelming the user was a delicate balancing act in product definition.  Articulating Our Core USP: It took deliberate iteration to crystallize our primary value proposition: moving away from generic, post-speech advice and delivering an explainable, multi-modal feedback engine. Rather than treating physiological stress, posture, and speech pacing as isolated silos, our breakthrough came from tying them into a unified, weighted scoring model and context-aware AI coaching that reflects real-world human communication.

**The problem it solves**

Most of us dread public speaking, and practicing alone in front of a mirror or a webcam doesn’t really help—you simply can't tell if you're talking too fast, slouching, overusing filler words, or visibly anxious until it's too late. NuEra (SpeakSense) solves this by acting as a personal, real-time speech coach. Instead of giving you vague advice, it looks at the whole picture: it listens to your words with low-latency speech recognition, tracks your posture and body language through your camera, and monitors your heart rate to catch moments of stress. By bringing all these cues together into a single, intuitive score and offering clear, actionable tips via Google Gemini, NuEra turns the guesswork of speech prep into practical, confidence-building practice.

**Best Use of Wolfram**

used in vocabulary enrichment of a student

Team **NuEra** -- [Sakthi S](https://github.com/Sakthi09-git), [sathurmugan K](https://github.com/sathur791), [Mohamed Zharif](https://github.com/Zharif18)

`2026-08-30`

---

### GapSens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gapsens-identifying-learning-gaps-before-students-falling-behind-df7d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Samitharani/GapSens---Identifying-Learning-Gaps-Before-Student-Falling-Behind) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1PdFHr69iZpz7pF9GEFoNd58DT5xl4Jdo/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/5MgeSpRIqUk) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Identifying Learning Gaps

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Traditional learning platforms mainly show marks, grades, and overall performance, but they often fail to explain why a student made mistakes, which concepts they have not understood, and what they should do next.

Teachers may have to manually review multiple answer sheets, identify repeated mistakes, find the underlying learning gaps, select appropriate study materials, and track whether the student improves in the next assessment. This becomes difficult and time-consuming, especially for a classroom with many students.

GapSens AI solves this by turning assessment data into evidence-based, personalized learning support.

What people can use GapSens AI for
Teachers can upload learning materials and student answer sheets and get question-level and concept-level insights instead of only aggregate marks.
Answer-sheet analysis identifies the student's answers, marks, correctness, and relevant concepts, with teacher verification when the extracted evidence is uncertain.
Learning-gap detection identifies concepts where the student is struggling based on actual assessment evidence.
Explainable feedback helps students understand what they got wrong, why the mistake happened, what the correct approach is, and which key points they should remember.
Material matching connects an identified learning gap with relevant learning materials uploaded by the teacher.
Personalized interventions suggest practical next steps such as reviewing a concept, studying examples, practicing questions, and reassessing.
Risk analysis helps teachers identify students who may need additional academic support.
Knowledge-graph-based analysis helps represent relationships between concepts and identify relevant prerequisite knowledge.
Test-to-test comparison allows teachers to compare assessments such as Test 1 and Test 2 to determine whether a learning gap has improved or persisted.
Students can access their authorized learning materials and receive understandable, evidence-based analysis of their own answers.
Multilingual support allows the interface to be used in English, Tamil, and Hindi, improving accessibility for diverse learners.

**Challenges we ran into**

Challenges We Ran Into
Handwritten OCR: Extracting accurate answers from handwritten sheets was challenging, so we added verification instead of blindly trusting OCR.
Concept Mapping: Some questions had no clear concept, so we marked them UNMAPPED instead of guessing.
Dynamic Analysis: We had to ensure learning gaps and interventions were based on actual student answers, not seeded data.
Firebase Permissions: Students initially couldn't access uploaded materials due to authorization/query issues, which we fixed without weakening security.
Multilingual Support: Added English, Tamil, and Hindi while keeping the existing data and application logic unchanged.

**Best Use of Render**

Render is used to deploy and host our GapSens AI application as a live web platform. It provides the cloud runtime for our application, allowing teachers, students, and administrators to access the system through the web without running it locally. Our application services run on Render, while Firebase manages authentication, Firestore data, and learning-material storage.

Team **Tech Crew** -- [Shona P](https://github.com/Shona05), [Samitha Rani](https://github.com/Samitharani), [Ramya S](https://github.com/ramyasuresh-1)

`2026-08-30`

---

### Saathi - AI Financial Copilot For Gig Workers
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saathi-4302) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dipakkr/financial-learning-game-for-blue-collars) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://financial-learning-game-for-blue-co-zeta.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> Financial confidence, by voice, any language

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![React-three-fiber](https://img.shields.io/badge/React--three--fiber-333333?style=flat-square) ![Web-Speech-API](https://img.shields.io/badge/Web--Speech--API-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square)

**What is the deployed URL for this project?**

https://financial-learning-game-for-blue-co-zeta.vercel.app/

**How you are solving it?**

## Saathi isn't a chatbot — it's a *dojo* where an AI runs a world you live in

Saathi meets workers where they are: **you talk, in your language, and an AI walks you through money and helps you get ahead.** Voice in, voice out, in Hindi, Tamil and English. Show a document to the camera and the AI reads it back to you.

The insight is that reading *about* money doesn't build confidence — **surviving consequences does**. So instead of lessons, Saathi is an AI that runs a world, plays an adversary you have to beat, and acts on your behalf:

- **🗣️ Talk to learn** — voice-first conversation in your own language. No forms, no English, no typing. Multimodal: point your camera at a bank letter or an insurance paper and the AI explains it.
- **🎮 Survive the Month** — an AI game master runs a 30-day money simulation. You *live* the consequences of saving vs. spending, insuring vs. going uncovered. An emergency hits — did past-you prepare?
- **🛡️ Fraudster Face-Off** — the AI role-plays an *adaptive* scammer that changes tactics based on how you respond. You practice refusing your PIN/OTP under pressure until you can beat it every time.
- **🤖 Do-it-for-me agent** — a tool-using agent checks your eligibility for real schemes (Jan Dhan, Ayushman Bharat, PM Suraksha Bima) and sets you up, instead of just telling you they exist.
- **📈 Financial Confidence score + streak** — progress you can feel, plus a **B2B intent-discovery dashboard** so banks and NGOs can see, in aggregate, what workers actually need and where they get stuck.

**How it's built:** `Next.js` + `React` front end; `React Three Fiber` / `Three.js` for the 3D and 2D worlds you walk through; `Web Speech API` for speech-to-text; `Smallest.ai` for natural text-to-speech; deployed on `Vercel` in `TypeScript`. Every AI layer has a **keyless fallback**, so the live demo never dies even if an API key or network hiccups.

**Prior work disclosure:** built during the hackathon. The repo scaffolding (Next.js app shell, the collaboration protocol) predates the event; the AI brain, the Survive-the-Month game master, the adaptive Fraudster Face-Off, the eligibility agent, and the B2B dashboard were built during the hackathon.

**What is the problem your project solves?**

## 400M+ workers are locked out of finance — by literacy and fear, not by lack of money

India's urban gig and blue-collar workforce — delivery riders, cab and auto drivers, Urban Company partners, office boys, security guards, house help — is **400M+ people strong**. They earn, they spend, they support families. Yet they are effectively locked out of the financial system, and not because they lack money.

They are locked out by two things:

- **Literacy.** Every bank app, every insurance form, every government-scheme portal assumes you can read English (or dense formal Hindi) and parse a form. If you can't, the entire system is a closed door.
- **Fear.** UPI scammers drain accounts every single day with a phone call: *"Sir, share your OTP to keep your account safe."* A worker who has never been taught how a scam works has no defence.

The result: people who could be saving, insuring their families, and claiming schemes they are legally entitled to (Jan Dhan, Ayushman Bharat, PM Suraksha Bima) instead stay one emergency away from disaster — and lose what little they have to fraud.

**Why it matters:** financial confidence for this segment isn't a nice-to-have. It's the difference between a medical emergency that wipes out a family and one that's covered; between a scam that takes a month's earnings and one that's refused at the door.

The existing default — download an app, read the forms, figure it out — **fundamentally does not work** for the next billion users. It needs a different interface entirely.

**How Did You Use Claude?**

## Claude is the entire intelligence layer — not a feature bolted on

Every piece of intelligence in Saathi is Claude. It plays four distinct roles:

1. **Multimodal brain.** Claude takes voice-transcribed input *and* images (a bank letter, an insurance form held up to the camera) and responds in the user's language — Hindi, Tamil or English — with plain, jargon-free explanations. This is what makes the voice-first, no-reading interface possible at all.

2. **Adaptive adversary (Fraudster Face-Off).** Claude role-plays a UPI scammer that *adapts its social-engineering tactics* to how the user responds — escalating pressure, switching pretexts — so practice feels real. It also judges, in-character and then out, whether the user successfully refused to share their PIN/OTP.

3. **Game master (Survive the Month).** Claude runs a stateful 30-day simulation: it narrates events, injects emergencies, and computes the consequences of the player's earlier saving/insuring choices — turning abstract financial advice into lived cause-and-effect.

4. **Agentic tool-use loop.** Claude drives a tool-using agent that checks real-scheme eligibility (Jan Dhan, Ayushman Bharat, PM Suraksha Bima) and takes setup actions on the user's behalf — an agent that *acts*, not just answers.

Claude also powers the **B2B intent-discovery dashboard**, distilling conversation signals into the aggregate needs banks and NGOs can act on. Because the product is voice-first and multilingual for a low-literacy audience, Claude's instruction-following and multimodal reasoning are what make the whole experience feasible — remove it and there is no product.

Team **Solo Scale** -- Deepak Kumar, Naman Goyal

`2026-08-08`

---

### College Companion
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/college-companion-your-allin-one-student-productivity-platform-6142) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://campus-success-tool.lovable.app) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Your All-in-One Student Dashboard

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

College Companion is a student productivity platform designed to help college students manage their academic life in one place.

Many students use different apps and notes to track attendance, CGPA, exams, and study tasks, which can be confusing and time-consuming. College Companion solves this problem by providing a single dashboard where students can:

• Track attendance percentage and monitor academic progress
• Calculate CGPA across semesters
• Manage upcoming exams with countdown tracking
• Create and organize study plans and daily tasks
• Improve productivity through a simple and user-friendly interface

The platform helps students stay organized, save time, and focus on their academic goals without switching between multiple tools.

**Challenges we ran into**

During the development of College Companion, we faced several challenges while combining multiple student productivity tools into a single platform.

One of the main challenges was designing a clean and user-friendly dashboard that could display attendance tracking, CGPA calculation, exam management, and study planning without overwhelming the user. We experimented with different layouts and improved the interface to make navigation simple and intuitive.

Another challenge was ensuring that all features worked smoothly together while maintaining a consistent design across the application. We also focused on making the platform responsive so that it could be used effectively on both desktop and mobile devices.

These challenges were overcome through continuous testing, UI improvements, and iterative development, resulting in a more polished and user-friendly student productivity platform.

Team **Tech Titans** -- Swathilakshmi V

`2026-06-12`

---

### AI Design Accessibility Auditor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/prj-c55a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yugpathak17/AI-Design-Accessibility-Auditor) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1bAda20X0mJtrbSBhxxwBDUTQo9dwUea9/view?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Empowering designs, enabling everyone

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**Challenges we ran into**

## Challenges I Ran Into

### 1. Extracting Website Accessibility Data
One of the biggest challenges was collecting accessibility information such as alt text, heading structure, forms, and links from different websites. Since websites are built differently, some elements were difficult to detect consistently.

**Solution:**  
I used HTML parsing techniques and created separate checks for images, headings, forms, and navigation elements to ensure accurate analysis across various websites.

---

### 2. Designing a Meaningful Scoring System
Converting multiple accessibility checks into a single accessibility score was challenging. A simple count of issues did not accurately reflect the overall accessibility of a website.

**Solution:**  
I developed a weighted scoring system where critical issues have a greater impact on the final score than minor issues.

---

### 3. Handling Invalid or Unreachable URLs
Users could enter incorrect URLs or websites that were temporarily unavailable, causing the analysis process to fail.

**Solution:**  
I added input validation, error handling, and user-friendly messages to ensure the application remained stable and informative.

---

### 4. Creating a Clean and User-Friendly Interface
Presenting technical accessibility data in a way that is easy to understand for both developers and non-technical users was challenging.

**Solution:**  
I organized the results into clear sections, included visual indicators, and used a simple dashboard layout to improve readability.

---

### 5. Generating Downloadable Reports
Exporting accessibility results into a well-structured PDF report required formatting dynamic content properly.

**Solution:**  
I implemented automated report generation and tested it with different website analyses to ensure consistent formatting.

**The problem it solves**

## The Problem It Solves

Many websites are not fully accessible to people with disabilities due to issues such as missing alt text, poor colour contrast, improper heading structures, and limited keyboard navigation. Identifying these problems manually requires expertise, time, and expensive accessibility audits.

### How AI Design Accessibility Auditor Helps

-  **Automatically detects accessibility issues** on any website.
-  **Improves accessibility** for users with visual, hearing, motor, and cognitive impairments.
-  **Provides AI-powered recommendations** to fix detected issues.
-  **Generates detailed accessibility reports** for developers and organizations.
-  **Reduces manual auditing time** and effort.
- **Helps achieve WCAG compliance** and accessibility best practices.
-  **Reduces legal and compliance risks** associated with inaccessible websites.
-  **Enhances overall user experience and design quality** for all users.

### Who Can Use It?

- Web Developers
- UI/UX Designers
- Startups and Businesses
- Educational Institutions
- Government Organizations
- Accessibility Consultants

### Impact

AI Design Accessibility Auditor makes web accessibility faster, easier, and more affordable, helping create a more inclusive internet that everyone can access and use effectively.

yug pathak

`2026-06-23`

---

### TabPilot: Focus Workspace for Students
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tabpilot-focus-workspace-for-students-d6f2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aniket01jan2008-svg/tabpilot) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://files.catbox.moe/oj2c4r.mp4) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Interactive focus workspace for study sessions

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Video.js](https://img.shields.io/badge/Video.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**Challenges we ran into**

The main challenge was turning TabPilot from a static landing page into a real MVP without overbuilding. A productivity app can quickly become too large with calendars, accounts, AI chat, teams, and extensions.

I solved this by narrowing the MVP to the core student workflow: create a session, add resource links, add three focus tasks, mark progress, and save the data locally in the browser.

Another challenge was making the project stand out from a normal todo app. I focused the experience around the real student problem of scattered tabs, links, notes, deadlines, and study resources before they become clean tasks.

**The problem it solves**

Students often work with scattered browser tabs, notes, links, PDFs, deadlines, coding tasks, and assignment reminders across multiple tools. This creates context switching, forgotten resources, and unclear priorities.

TabPilot solves this by giving students one focused workspace where they can create study/project sessions, capture useful resources, organize links into Focus, Research, and Later, and track the top three tasks for the current session.

Latest update: Added interactive TabPilot MVP with session, resources, and task tracking.

People can use TabPilot to:
- Create separate workspaces for assignments, exam prep, coding practice, or hackathon builds
- Save useful resource links in one place
- Track up to three focus tasks per session
- Mark tasks complete and see progress update
- Keep data saved in the browser with local storage

It makes studying easier by turning messy digital clutter into a simple, actionable workflow.

[Aniket Yadav](https://github.com/aniket01jan2008-svg)

`2026-06-29`

---

### ScholarAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scholarai-1fc6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/riyahardeepkaur-gif/ScholarAI/commits?author=riyahardeepkaur-gif) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> ScholarAI – AI-Powered Learning Assistant

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Natural Language Processing](https://img.shields.io/badge/Natural%20Language%20Processing-333333?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-333333?style=flat-square) ![Llama](https://img.shields.io/badge/Llama-333333?style=flat-square) ![Ollama](https://img.shields.io/badge/Ollama-333333?style=flat-square)

**Challenges we ran into**

## Challenges I Ran Into

While building ScholarAI, I faced several technical challenges while developing the AI-powered document learning system.

### 1. Building the RAG Pipeline
One of the biggest challenges was connecting PDF processing, embeddings, vector search, and the LLM together. Initially, the AI responses were not always based on the uploaded notes.

**Solution:**  
I implemented a Retrieval-Augmented Generation (RAG) pipeline using Sentence Transformers for embeddings and FAISS for similarity search. This allowed ScholarAI to retrieve relevant sections from the uploaded document before generating answers.

---

### 2. PDF Text Extraction Issues
Some PDFs contained scanned images instead of actual text, causing the text extraction process to return empty results.

**Solution:**  
I identified the difference between text-based and image-based PDFs and optimized the application to work reliably with text-based study materials for the hackathon version.

---

### 3. Vector Database Integration
While storing document embeddings in FAISS, I encountered errors related to embedding dimensions and data formatting.

**Solution:**  
I debugged the embedding generation process, ensured correct NumPy array formatting, and added validation before storing vectors in the FAISS index.

---

### 4. Structuring AI-Generated Quiz Output
The LLM initially generated quiz questions in inconsistent formats, making it difficult to create an interactive quiz interface.

**Solution:**  
I improved the prompting strategy and added JSON-based structured output handling, allowing ScholarAI to generate organized MCQs with answer validation.

---

### 5. Optimizing Performance
Running local LLM models for summaries and quizzes was slower for larger documents.

**Solution:**  
I optimized the workflow by limiting the context size sent to the model and using smaller document chunks while maintaining answer quality.

---

These challenges helped improve my understanding of AI application development, RAG systems, vector databases, and building reliable user-focused solutions.

**The problem it solves**

## Problem It Solves

Students often spend hours searching through lengthy notes, PDFs, and study materials to find specific information. Traditional methods require manually reading large documents, which can be time-consuming and inefficient.

ScholarAI solves this problem by transforming static study materials into an interactive AI-powered learning assistant.

Users can upload their study PDFs and:
- Ask questions directly from their notes
- Get instant answers based on their own study material
- Generate quick summaries for revision
- Create AI-generated quizzes for self-assessment

By using Retrieval-Augmented Generation (RAG), vector search, and AI language models, ScholarAI helps students understand concepts faster, improves learning efficiency, and makes exam preparation more personalized and accessible.

It reduces the effort required to search through large documents and provides a smarter way to learn from existing educational resources.

Ramandeep Kaur

`2026-07-20`

---

### Road accident prediction uing machine learning
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/road-accident-prediction-uing-machine-learning-43b1) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

Pandranki Sravani

`2026-07-30`

---

### NEXUS AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexus-ai-f149) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mithunkumar1604/NEXUS-AI) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Your AI-powered student operating system

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The Problem

Students today struggle to manage multiple aspects of college life at the same time academics, assignments, learning new skills, projects, and career preparation.

Important information is scattered across different apps, making it difficult to stay organized and productive. Students often lack personalized guidance for creating study plans, choosing projects, improving technical skills, and preparing for future opportunities How NEXUS AI Helps

NEXUS AI acts as a personal AI-powered student operating system that brings learning, productivity, and career support into one platform.

It helps students by:

- 🤖 Providing an AI assistant for instant guidance on coding, studies, and projects
- 📚 Creating personalized study plans based on goals and deadlines
- ✅ Managing tasks and assignments to improve productivity
- 📝 Organizing notes in one place for easier revision
- 🚀 Helping students plan their career roadmap and skill development

By combining AI assistance with productivity tools, NEXUS AI reduces student stress, saves time, and helps students make smarter decisions throughout their academic journey.

**Challenges we ran into**

Building NEXUS AI was both exciting and challenging because this was my first hackathon project.

One of the biggest challenges was connecting the Google Gemini AI model with my Flask backend. I ran into issues with API keys, model compatibility, and getting the AI to return responses. After a lot of debugging, reading documentation, and testing different solutions, I was able to get it working.

I also faced problems connecting the frontend and backend. At first, messages weren't being sent correctly, and the AI responses weren't appearing on the webpage. I fixed these issues by debugging my Flask routes, JavaScript fetch requests, and checking browser console errors.

Another challenge was handling Git and GitHub. I accidentally included my `.env` file, which caused GitHub to block my push because it detected my API key. I learned how to use `.gitignore`, remove sensitive files, and manage my repository properly.

Designing the UI was another hurdle. I didn't want it to look like a basic student project, so I spent time creating a clean dark-themed interface with a modern AI-inspired look.

Since this was my first hackathon, I was honestly nervous and wasn't sure if I'd be able to finish everything on time. I encountered many coding errors and bugs along the way, but instead of giving up, I kept debugging, learning from each mistake, and improving the project step by step.

Overall, this project taught me much more than just programming. It improved my debugging skills, problem-solving ability, Git/GitHub workflow, API integration, and gave me confidence to build larger AI projects in the future.

[Mithun s](https://github.com/mithunkumar1604)

`2026-07-28`

---

### Explainable AI for Diabetes Risk Prediction
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/httpsdevfoliocoprojectsexplainableaifordiabetesriskprediction-3b7a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kashish-alt0786/Medical-IT-Diabetes-AI-Project) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.kaggle.com/code/kashish0000000/explainable-ai-diabetes-risk-prediction-xgboost) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> An end-to-end Machine Learning web application

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![shap](https://img.shields.io/badge/shap-333333?style=flat-square)

**Challenges we ran into**

1. **Handling Biologically Impossible Zeroes:** The raw dataset contained hidden missing data encoded as `0` values for metrics like Blood Pressure, Glucose, and BMI. Simply dropping these rows would strip valuable training data. I resolved this by identifying biologically invalid zeroes and applying group-median imputation.
2. **Explaining Tree-Based Ensembles:** Complex models like XGBoost offer high accuracy but are inherently hard to interpret. Implementing SHAP TreeExplainer allowed us to bridge the gap between model accuracy and clinical transparency by computing exact feature contributions for every test instance

**The problem it solves**

Diabetes affects hundreds of millions of people worldwide, yet early risk assessment tools often operate as opaque "black-box" models. Healthcare providers and patients are hesitant to trust machine learning predictions when they cannot see the clinical reasoning behind them.

**How this project solves it:**
- **Transparent Risk Scoring:** Utilizes an XGBoost machine learning model trained on key medical metrics (Glucose, BMI, Age, Insulin levels) to predict diabetes risk.
- **Clinician-Centric Interpretability:** Integrates **SHAP (SHapley Additive exPlanations)** values to break down exactly *why* a specific prediction was made, highlighting which biometric factors contributed most to a patient's risk.
- **Actionable Insights:** Helps practitioners move from raw statistical predictions to actionable clinical decisions, making early intervention safer and more reliable

kashish khan

`2026-07-28`

---

### Studymate AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/studymate-ai-dd6b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://study-mate-ai.ai.studio/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> The student's saviour

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was getting the AI to give accurate and helpful answers consistently. I improved this by refining my prompts, testing different scenarios, and fixing API integration issues. I also worked on making the interface simple and easy for students to use.

**The problem it solves**

StudyMate AI is an intelligent AI-powered learning assistant built using Google's Gemini API to make studying faster, easier, and more personalized. It helps students understand complex concepts through detailed explanations, summarize lengthy notes and PDFs, answer academic questions, translate study materials into multiple languages, generate quizzes for self-assessment, and create personalized study plans based on individual learning goals. The platform also offers text-to-speech functionality, allowing students to listen to their study material anytime. By combining multiple AI-powered learning tools into one platform, StudyMate AI acts as a 24/7 personal tutor, helping students learn more efficiently, improve retention, and prepare confidently for exams.

Aishwarya Parida

`2026-07-29`

---

### saint-monica-students-community
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saintmonicastudentscommunity-675a) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://saint-monica-students-community.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> FOR INNOVATIVE 10TH STUDENTS

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

🎓 One Platform for Every Student – Brings students together in a single digital community for academics, communication, and collaboration.
📚 Easy Access to Study Resources – Notes, assignments, previous papers, and learning materials are available in one place, reducing time spent searching.
💬 Real-Time Student Interaction – Encourages discussions, doubt-solving, and peer-to-peer learning.
📢 Centralized Announcements – Important school notices, events, and updates reach every student quickly.
🤝 Better Collaboration – Students can work together on projects, competitions, and hackathons more efficiently.
🌐 Accessible Anywhere – Being web-based, it can be accessed from any device with an internet connection without installing software.
📱 Mobile-Friendly Experience – Designed to work smoothly on phones, tablets, and desktops.
🔒 Secure Student Environment – A dedicated platform for the school community helps keep discussions and resources organized and private.
⚡ Saves Time – Eliminates the need to switch between multiple apps for communication and study materials.
🎯 Improves Student Engagement – Interactive features encourage participation beyond the classroom.
🚀 Scalable Platform – New features such as AI study assistants, attendance, quizzes, clubs, events, and placement support can be added over time.
💡 Developed by Student, for Students – Built with the real needs of the student community in mind, making it practical and user-focused.

**Challenges we ran into**

## Challenges I Ran Into While Building Saint Monica Students Community

Developing the Saint Monica Students Community platform was an exciting journey, but it also came with several technical and design challenges that helped me grow as a developer.

* **Designing a user-friendly interface:** Creating a clean, modern, and easy-to-use interface that works well for students without making it feel cluttered.

* **Making the website responsive:** Ensuring that every page worked smoothly across desktops, tablets, and mobile devices required continuous testing and adjustments.

* **Managing application state:** Keeping data synchronized across different pages and features while maintaining a smooth user experience.

* **Performance optimization:** Reducing loading times, optimizing images and assets, and minimizing unnecessary rendering to improve website speed.

* **Debugging unexpected issues:** Fixing layout inconsistencies, broken components, navigation bugs, and browser compatibility problems throughout development.

* **Planning a scalable architecture:** Organizing the project structure so that future features can be added without requiring a complete redesign.

* **Balancing features and simplicity:** Choosing which features to implement while keeping the platform intuitive and not overwhelming users.

* **Learning new technologies:** Adapting to unfamiliar frameworks, libraries, and development tools during the project while continuing to make steady progress.

* **Testing across browsers:** Ensuring consistent functionality and appearance on different browsers and screen sizes.

* **Time management:** Balancing development, testing, bug fixing, feature implementation, and continuous improvements within limited time.

Despite these challenges, each obstacle became an opportunity to learn and improve. Building this platform strengthened my problem-solving skills, improved my understanding of full-stack development, and reinforced the importance of writing scalable, maintainable, and user-focused software. Every challenge made the final product stronger and prepared me for even more ambitious projects in the future.

swayam anarthe

`2026-07-29`

---

### Student Hub
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/student-hub-f969) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Student HubStudent HubStudent Hub

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

This project helps students and users by providing a simple, responsive, and user-friendly platform to access important features in one place.

It reduces manual effort, saves time, and improves the overall user experience with a clean interface and easy navigation.

The project is designed to:
- Make tasks faster and easier.
- Provide a responsive experience on desktop and mobile devices.
- Improve accessibility and usability.
- Reduce confusion with a simple and modern interface.
- Help users complete their work more efficiently.

**Challenges we ran into**

During the development of this project, I faced several challenges.

- Making the website fully responsive on different screen sizes.
- Fixing CSS layout and alignment issues.
- Implementing JavaScript functionality without errors.
- Managing the project structure and organizing files properly.
- Improving the website's performance and user experience.

To overcome these challenges, I used browser developer tools for debugging, referred to official documentation, tested the project on multiple devices, and continuously improved the code through practice and problem-solving.

Anand Banwari

`2026-07-30`

---

### EduMenter Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edumenter-ai-bd3f) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co)

> Empowering Students with Smart Career Guidance, Re

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Our project is designed to solve a common problem faced by students, which is the lack of proper career guidance, confusion about what skills to learn, and difficulty in tracking their learning progress in an organized way.”
“We have built a student career guidance platform that helps users explore different career paths, understand required skills, and follow a structured roadmap to achieve their goals step by step.”
“The system allows students to upload their resumes, which can be stored securely using Firebase cloud database, making it easy to access and manage their data anytime.”
“We also provide an interview practice section where students can answer common technical and HR questions, helping them improve their confidence and prepare better for real interviews.”
“The career roadmap feature guides users based on their selected field, such as web development, AI, or cybersecurity, and shows the step-by-step learning path they should follow.”
“Additionally, the course recommendation system suggests relevant skills and technologies that students should learn next based on their chosen career direction.”
“To make the system more effective, we have integrated Firebase as a backend solution to store user data, resume details, and progress tracking in a cloud database.”
“Overall, our project acts as a simple but powerful career guidance assistant that supports students throughout their learning journey from beginner level to job readiness.

**Challenges we ran into**

One improvement we identified in our project is ensuring proper validation for all user inputs, such as checking whether the resume file is uploaded correctly before processing it.”
“We noticed that some pages required better navigation consistency, so we standardized the linking between all pages to ensure smooth user experience.”
“Another enhancement we made is improving error handling in Firebase integration, so that any network or database failure is properly managed without breaking the application.”
“We also fixed an issue where empty form submissions were being accepted, and now proper validation messages are shown to the user before saving data.”
“To improve performance, we optimized the JavaScript code by reducing redundant function calls and organizing the logic into reusable components.”
“We addressed a UI alignment issue in mobile view by making the design fully responsive using CSS media queries.”
“We improved the resume upload feature by ensuring that only valid file types like PDF and DOC are accepted, which prevents incorrect data from being stored.”
“Overall, these fixes helped us make the application more stable, user-friendly, and suitable for real-world usage.

[Murali Parasuraman](https://github.com/muralimurali0147-lab)

`2026-06-29`

---

### MindMesh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mindmesh-0b08) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alonek007/hackathon-arcnight) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hackathon-arcnight-production-41c0.up.railway.app/login) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Hni9rBz_bRQ) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Shatter the PDF. Experience your learning.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square)

**The problem it solves**

Students drown in passive PDFs and dense notes that cause cognitive fatigue — they stare at screens but don't actually absorb information. Standard quizzes only tell you that you failed *after the fact*, with no real-time correction. And one-size-fits-all education completely ignores individual learning gaps and weak spots.

MindMesh fixes all three: upload any PDF or notes, and it instantly architects them into surgical summaries, adaptive flashcards, real-time quizzes, and personalized 24-hour study plans — all powered by Google Gemini. If you keep missing questions on one concept, the system automatically pivots your study route and generates an interactive 3D visualization of that topic so you understand it viscerally, not just memorize it.

**Challenges we ran into**

Integrating pgvector with PostgreSQL for high-dimensional semantic embeddings was non-trivial — setting up the vector similarity search to accurately map conceptual relationships (not just keyword matches) took significant tuning. Getting React Three Fiber to generate meaningful 3D visualizations dynamically from AI-generated descriptions (rather than pre-built models) was another major challenge. We also had to carefully architect the RAG pipeline so Gemini's responses stayed contextually grounded to the uploaded document rather than hallucinating off-topic content. Deploying the full stack (React frontend + Node/Express backend + PostgreSQL with pgvector) on Railway with proper environment config and cold-start handling was the final stretch challenge.

Team **MasterMavericks** -- Ayush Choudhary, Adarsh Agrawal, Shashi Kumar, Sanidhya Sriman

`2026-06-14`

---

### Orbit
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/orbit-4437) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pranavamurthyks/orbit) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://orbit-frontend-v2.vercel.app/index.html) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/26Y4ILfXSKY) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> The ultimate SpaceTech community

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

3d modelling for VR

**The problem it solves**

Space curiosity is everywhere but there's nowhere to take it further. Existing platforms are passive — no gameplay, no reward for going outside, no way to connect with others who share the same interest. People who want to stargaze together have no infrastructure to organise, split costs, or find local communities. Curiosity spikes and dies without a loop to sustain it.
Orbit turns space curiosity into a habit — real physics gameplay on live NASA data, a reward economy for going outside, and a community layer that gets people stargazing together in the real world.

Team **Macrocraft** -- [Haripriya Subbiah](https://github.com/haripriyasubbiah), [praanesh mb](https://github.com/pransh-py), [Pranavamurthy K S](https://github.com/pranavamurthyks), Jeff Herbert

`2026-06-14`

---

### Scholar
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scholar-scale-up-your-learning-40e7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AMAYKJHA/For-Nepal) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tOAjN94J8es?si=RAO_BFA-N53ZOWOG) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%202026-0052CC?style=flat-square)](https://deerhack26.devfolio.co)

> Scale up your learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**Higher Study Students & Researchers**

- Information overload from dense PDFs and textbooks, with no adaptive guidance on what to focus on
- No long-term memory of learning progress; every session starts from scratch
- Existing AI tools (ChatGPT, NotebookLM) answer questions well but don't retain learning history or build on past sessions
- Lack of research-integrated tools that connect new material with previously studied concepts
- **Knowledge graph** that suggest learners what to go for next without wasting time

**Younger Students (Grades 1–5)**

- Learning from books and PDFs is boring and passive, with no engagement layer
- Low retention - students forget quickly without targeted, timely revision
- Parents have no way to track what their child has actually learned or where they're struggling
- Existing tools (flashcard apps, traditional notes) lack any story-driven or emotional hook to keep kids motivated
- Our app provides game-based learning on the basis of topic given by user providing flexibility

**Challenges we ran into**

- Synchronizing React (UI/state) with Phaser (game engine) in real-time - getting HP bars, quiz results, and game events to stay in sync between the two systems required building a custom event bridge
- Getting the AI to reliably generate structured, valid JSON for 20 quiz questions across four difficulty tiers - needed careful prompt engineering and validation to avoid malformed or inconsistent output
- Working within free-tier API limits (Gemini, Groq) while supporting PDF parsing, embeddings, and chat - required fallback logic and rate-limit handling to keep the app usable
- Coordinating a 4-person team across frontend, ML, and backend roles under hackathon time pressure, especially integrating the RAG pipeline (PDF -> chunks -> embeddings -> pgvector) with the game and chat modules

**Ed-Tech**

This project gives scaled up learning for research, higher studies as well as interactive game-based learning for school going students

Team **ForNepal** -- [Sandeep Khadka](https://github.com/sandeepkhadk), [Rojin Dhami](https://github.com/Rojin-Dhami), Amay Jha, [Bishal Shrestha](https://github.com/BishalABPS52)

`2026-06-14`

---

### SkillBridge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skillbridge-ca24) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vaishnavi12162004.github.io/skillbridge/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

> Bridging the gap between students and career

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**Challenges we ran into**

Honestly, the biggest struggle was getting the JavaScript 
filter to work. The buttons weren't filtering the cards 
at all — turned out the data-type values in HTML didn't 
match what I was checking in JS. Spent way too long on 
that one small typo!

Making the UI look professional was also harder than 
expected. I kept tweaking colors, spacing and layouts 
until it finally felt right. The AI Career Advisor 
section was exciting to add but figuring out the API 
call structure was a new challenge for me.

Overall it pushed me to think like a real developer — 
debug, fix, repeat!

**The problem it solves**

Many students struggle to find internships, projects, mentorship opportunities, and learning resources that match their skills. Companies also face difficulty in finding candidates with verified practical skills. SkillBridge solves this gap by creating a platform where students can showcase their skills, connect with mentors, discover projects, and find relevant opportunities.

[Vaishnavi .](https://github.com/Vaishnavi12162004)

`2026-05-30`

---

### Mathgaze
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mathgaze-3154) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vishvakumar07/Mathgaze) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

> Turning Learning into a Fun-Filled Journey

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Building MathGaze was exciting, but it came with a few challenges. Our biggest challenge was finding the right balance between learning and fun. We didn't want the app to feel like a regular math worksheet, but we also wanted children to actually learn while playing. We spent time experimenting with different game ideas and question formats until we found a balance that felt engaging and educational.

Another challenge was deciding the difficulty level of the questions. During testing, some questions were too easy and became repetitive, while others were too difficult and could discourage young learners. We solved this by organizing questions into different levels so that children can gradually improve at their own pace.

We also faced some technical issues while implementing the scoring system and ensuring that game progress was tracked correctly. Through testing, debugging, and multiple revisions, we were able to fix these issues and make the experience smoother.

Overall, these challenges taught us a lot about both game development and educational design. By continuously improving the application based on feedback and testing, we were able to create a platform that makes learning math more enjoyable and accessible for children.

**The problem it solves**

MathGaze makes learning mathematics fun and interactive for children by turning problem-solving into engaging games. Many students find math difficult, boring, or intimidating, which can reduce their interest and confidence in the subject. MathGaze addresses this challenge by combining educational content with game-based learning.

Children can use MathGaze to practice mathematical concepts such as addition, subtraction, multiplication, division, logical reasoning, and problem-solving skills in an enjoyable environment. Through interactive challenges, rewards, and gamified activities, students stay motivated while improving their mathematical abilities.

Benefits
1. Makes learning math enjoyable through games and interactive activities.
 2.Improves problem-solving and logical thinking skills.
 3.Helps children practice and reinforce mathematical concepts.
 4.Increases confidence by encouraging learning through play.
 5.Makes math practice less stressful and more engaging than traditional methods.
 6.Supports both classroom learning and self-study at home.

MathGaze transforms mathematics from a challenging subject into an exciting adventure, helping children learn faster, stay motivated, and develop a strong foundation in math.

Team **Main characters** -- Reegan Ferdinand, Zidane Ashik, Vishva Kumar, Rithanya S, Nivethika M, [Sahanaa Kumar](https://github.com/Sahanaakumar)

`2026-05-30`

---

### Astra AI Campus Manager
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/astra-ai-campus-manager-f532) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://timely-torte-83d5c7.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> The Future of Student Management 💻

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![Speech API](https://img.shields.io/badge/Speech%20API-333333?style=flat-square) ![Netlify](https://img.shields.io/badge/Netlify-333333?style=flat-square) ![jspdf](https://img.shields.io/badge/jspdf-333333?style=flat-square) ![Electron JS](https://img.shields.io/badge/Electron%20JS-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

🚀 The Problem Astra AI Campus Manager Solves
📚 Problem Statement

Many schools, colleges, coaching centers, and educational institutes still manage student records manually using notebooks, registers, spreadsheets, or complicated software. This creates several problems such as:

❌ Time-consuming student data management
❌ Difficulty in calculating percentages and grades manually
❌ Poor organization of attendance and subject records
❌ Complicated PDF/report generation process
❌ Lack of smart search and filtering options
❌ No AI or voice assistant support
❌ Difficult user interface for beginners
❌ No offline-friendly lightweight solution for small institutes

Teachers and administrators often waste a lot of time maintaining records instead of focusing on teaching and student improvement.

💡 Our Solution — Astra AI Campus Manager

Astra AI Campus Manager is an AI-powered smart student management system designed to simplify educational administration using modern web technologies and automation.

This platform helps institutes manage student records in a faster, smarter, and more professional way.

🔥 What People Can Use It For
👨‍🏫 Teachers
Add and manage student records easily
Calculate percentage automatically
Generate professional PDF reports instantly
Search student records quickly
Print reports directly
🏫 Schools & Colleges
Maintain organized student databases
Store class-wise and section-wise data
Improve digital management system
Reduce paperwork and manual calculations
👨‍💻 Students / Developers
Learn AI-integrated web development
Experience desktop app development using Electron.js
Explore voice assistant integration in projects
🤖 Smart AI Features

The project includes a built-in AI Voice Assistant that can:

Accept voice commands
Fill student information using speech
Help users navigate features
Improve accessibility for beginners

This makes the application modern, interactive, and user-friendly.

⚡ How It Makes Existing Tasks Easier
Traditional Method	Astra AI Solution
Manual calculations	Automatic percentage calculation
Paper records	Digital smart records
Hard to search students	Instant live search
Separate software for reports	Built-in PDF generation
Time-consuming management	One-click operations
Basic UI systems	Modern AI-powered interface
🛡️ Safety & Reliability
💾 Offline local data storage support
🔒 No internet required for core features
📄 Secure PDF export system
🖥️ Lightweight desktop application
⚡ Fast and responsive interface
🌍 Future Scope

The project is currently available for:

✅ Windows Desktop Version

Future development includes:

📱 Android App
🍎 iOS App
☁️ Cloud Database Integration
🤖 Advanced AI Assistant
📊 Analytics Dashboard
🔐 Login & Authentication System
🧠 Technologies Used
HTML5
CSS3
JavaScript ES6
Node.js
Electron.js
Web Speech API
jsPDF
LocalStorage
🚀 Conclusion

Astra AI Campus Manager transforms traditional student management into a smart, AI-powered digital experience. It saves time, reduces manual work, improves organization, and provides an innovative solution for modern educational environments.

🚀 Powered By Astra AI
👨‍💻 Developed By Ishan Lal

**Challenges we ran into**

⚡ Challenges We Ran Into During Development

Building Astra AI Campus Manager was an exciting journey, but we faced several technical and design challenges while developing the project.

🐞 1. Electron & Node.js Setup Issues

One of the biggest challenges was configuring the desktop application environment using Electron.js and Node.js.

Initially, commands like:

npm start

and

node -v

were not working properly due to:

Missing environment variables
PowerShell execution restrictions
Incorrect Node.js installation setup
✅ Solution

We resolved this by:

Reinstalling Node.js correctly
Fixing PATH variables
Enabling PowerShell script execution permissions
Properly configuring Electron project files

This helped the application run successfully as a desktop app.

🎤 2. AI Voice Assistant Integration

Integrating the AI voice assistant was another major hurdle.

The assistant initially:

Could not recognize commands properly
Failed to fill input fields automatically
Had speech recognition delay issues
✅ Solution

We implemented:

Web Speech API
Real-time command processing
Dynamic field mapping
Improved voice command handling logic

This allowed users to interact with the system using voice commands like:

“Add student”
“Save PDF”
“Search student”
“Dark mode”
📄 3. Professional PDF Generation

Generating clean and professional PDF reports was difficult in the beginning.

Problems included:

Broken table alignment
Missing borders
Improper spacing
Unorganized student data formatting
✅ Solution

We redesigned the PDF layout using:

Structured table formatting
Dynamic row generation
Border alignment
Automatic spacing logic using jsPDF

The final result became much more professional and readable.

🎨 4. UI & Theme Design Challenges

Creating a modern UI that looked professional on both desktop and browser environments was challenging.

Issues faced:

Poor responsiveness
Inconsistent dark/light themes
Alignment problems
Font rendering issues
✅ Solution

We improved the design by:

Using modern CSS styling
Adding responsive layouts
Implementing dark/light mode support
Supporting Hindi & English fonts

This created a cleaner and more user-friendly interface.

💾 5. Local Data Storage Problems

Managing student data without a backend server was difficult initially.

Data was getting:

Lost after refresh
Not displaying correctly
Difficult to organize
✅ Solution

We implemented:

LocalStorage-based database logic
Automatic save and load functions
Dynamic table rendering

This enabled offline-friendly data management without requiring cloud storage.

🌐 6. Web Deployment Challenges

Deploying the project online using Netlify also created issues such as:

Missing file paths
Images not loading
CSS and JavaScript not linking properly
✅ Solution

We fixed:

Folder structure
File naming conventions
Relative asset paths

After deployment, the project became accessible through a public web link.

🚀 What We Learned

Through these challenges, we learned:

Desktop application development
AI voice assistant integration
PDF automation
UI/UX improvement
Real-world debugging techniques
Deployment and hosting

These experiences helped transform the project into a fully functional AI-powered student management system.

🚀 Powered By Astra AI
👨‍💻 Developed By Ishan Lal

**Using LocusFounder to Build a Business!**

• Artificial Intelligence (AI)
• Education Technology (EdTech)
• Productivity & Automation
• Web & Desktop Application Development
• Smart Student Management Systems

Ishan Lal

`2026-05-22`

---

### dealpilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dealpilot-725a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/WiceKiwi/DealPilot) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1cHmMBr-4HOTOeg2kMK2CJOZOiUOg-U4p/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> uni students

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square)

**Use of Genspark**

Genspark serves as the agentic workspace and orchestration layer for DealFlow AI's revenue agents. Rather than
  making a single LLM call that extracts fields, we use Genspark to run a coordinated team of specialized agents —
  each with a narrow responsibility and auditable output. The dashboard's Live Agent Console makes this pipeline
  visible: judges can watch each Genspark-powered agent complete its step in sequence, see what it produced, and
  understand why a deal was flagged, enriched, or saved. Genspark is not tucked away in the backend — it's the
  centerpiece of the demo and the reason the product feels like a revenue team rather than a chatbot.

**How you are solving it**

DealFlow AI turns one natural sentence from a sales rep into a full CRM workflow. A rep sends a casual update —
  via Telegram or the web dashboard — and six specialized AI agents handle the rest:

  - Intake Agent — normalizes the message and confirms it's CRM-relevant
  - Extraction Agent — pulls contact, company, deal stage, sentiment, next action, and date with field-level
  confidence scoring
  - Validation Agent — flags missing fields, ambiguous dates, and risk signals; decides if confirmation is needed
  - Enrichment Agent — adds deal risk level, manager summary, and next best action recommendation
  - Action Agent — generates a CRM payload and a follow-up email draft
  - Manager Intelligence Agent — updates the pipeline digest with at-risk deals and follow-up queue

  Confirmed deals are written to Airtable as live CRM records. The Next.js dashboard updates in real time via
  WebSocket so managers always have an accurate pipeline view — without chasing reps for updates.

**Use of Claude**

Claude (via the Anthropic API) powers the structured reasoning at the core of each agent. Every agent receives a
  tightly scoped system prompt and returns valid JSON — contact extraction with confidence levels, validation
  decisions with field-by-field reasoning, enrichment outputs with manager-readable summaries, and follow-up email
  drafts. Claude's instruction-following and JSON reliability are what make the multi-agent pipeline deterministic
  enough to trust for CRM automation. The backend routes through Genspark first and falls back to Claude
  automatically, so the pipeline stays live even under API instability.

**The problem your project solves**

Sales teams lose revenue because CRM data is late, incomplete, and untrusted. After every call or meeting, reps know exactly what happened, but updating the CRM means stopping to open a system, finding the right record, and filling multiple fields. Most reps skip it or do it hours later from memory. The result: managers are forecasting from stale data, follow-ups get missed, and deals slip without warning.                                           

The root cause isn't laziness, it's friction. DealFlow AI removes that friction entirely.

Team **U&C** -- [Angelina Jennings](https://github.com/jenningsk-ux), [Justin Wicent](https://github.com/WiceKiwi), [Pranav Krishna](https://github.com/nil)

`2026-04-24`

---

### SmartEdu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartedu-7c66) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/adityapandey97/smartEdu) [![Built at](https://img.shields.io/badge/Built%20at-Off--Grid-0052CC?style=flat-square)](https://offgrid.devfolio.co)

> Smart Learning. Fair Attendance. Better Outcomes.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

** The Problem It Solves**
Fragmented classroom management across multiple platforms (WhatsApp, Excel, notice boards)
Manual and error-prone attendance tracking
No mechanism to correct incorrect attendance records
Lack of real-time communication for updates (holidays, schedule changes, events)
Poor visibility into student performance and progress
Low classroom engagement and interactivity
Inefficient assignment and study material management
 **What People Can Use It For
 Students**
Track attendance and receive alerts for shortage (<75%)
Access study materials (PPTs, notes, PYQs) in a centralized system
Submit, edit, and manage assignments
Raise attendance disputes for incorrect marking
Attempt quizzes and receive instant feedback
View marks and monitor academic performance
Receive real-time notifications and announcements
 **Teachers**
Mark and manage attendance efficiently
Upload and organize study materials
Create and manage assignments with deadlines
Upload and update student marks
Conduct quizzes to improve engagement
Send notifications (holidays, substitute teachers, events)
Review and resolve attendance-related issues
 How It Improves Existing Systems
Centralization: Consolidates all classroom activities into a single platform
Accuracy: Reduces errors in attendance through validation and correction mechanisms
Transparency: Enables fair attendance management via dispute resolution
Efficiency: Automates repetitive tasks like mark calculation and notifications
Real-Time Communication: Ensures instant updates and reduces information gaps
Data-Driven Insights: Provides performance analytics for better decision-making
Enhanced Engagement: Integrates quizzes and feedback to improve learning experience
Scalability: Can be extended across multiple classes and institutions
 **Final Statement**
Provides a comprehensive, efficient, and transparent digital classroom ecosystem that improves both teaching and learning outcomes.

**Challenges we ran into**

Challenges Faced
The project was built in a new domain with limited prior experience in Flutter-based app development.
Initial setup and running the application were challenging due to environment configuration and device/emulator issues.
There were difficulties in properly rendering and visualizing the UI, which slowed down development.
Time constraints limited the ability to implement all planned features and full backend integration.
How We Addressed Them
Focused on learning the basics quickly and building the application step-by-step.
Used debugging tools like flutter doctor and tested on real devices to resolve setup issues.
Simplified UI design to ensure consistency and faster implementation.
Prioritized core features and ensured a working prototype for demonstration.
Key Takeaway

We adapted to a new technology stack under time constraints and delivered a functional solution that demonstrates the core concept effectively.

Team **Defeated coders** -- [Nandita Sahni](https://github.com/Nanditasahni), [ADITYA PANDEY](https://github.com/adityapandey97), [ANKU YADAV](https://github.com/anku2622)

`2026-04-11`

---

### Broke AF
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/broke-af-4b84) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/UzumakiNarutoX/Broke-AF) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://broke-af-sooty.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Matrix%203-0052CC?style=flat-square)](https://matrix-3.devfolio.co)

> Your CA Best Friend Who Grew Up Among Students.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Indian college students have always been broke but never had a tool built for them existing apps assume a salary and bank account, not a monthly allowance and a Zomato habit. Broke AF solves this by showing your exact broke date before it hits, holding you accountable through a brutally honest AI spending verdict, letting you log expenses just by speaking, and replacing the chaotic WhatsApp bill-split thread with a clean, one-tap system. It doesn't try to be a full financial suite it just fixes the four things that make student finances painful, in a way that actually fits how students live.

**Challenges we ran into**

The trickiest part was getting the voice logging to reliably parse natural, messy student speech people say "80 ka chai" as easily as "spent 80 on chai," and making the AI handle both Hinglish patterns consistently took a lot of prompt tuning. The AI Judge was another hurdle; early responses were either too generic to be useful or too harsh to be funny, so finding the right tone that felt honest but not discouraging required several iterations. The broke date prediction also had edge cases where mid-month allowance top-ups would throw off the burn rate calculation entirely, which needed careful logic to handle gracefully. On the UI side, getting the bill split flow to feel frictionless especially the OCR receipt scanning reliably extracting totals from crumpled or low-light photos was harder than expected and involved falling back to manual entry as a safety net

**Grand Cash Prize Pool – ₹50,000**

Broke AF sits squarely at the intersection of AI and personal finance, built ground-up for a demographic that existing tools have always ignored. It uses AI not as a gimmick but as the core engine powering voice expense parsing, spending pattern analysis, and personalized financial verdicts making it a strong fit for any track centered around practical AI applications, fintech innovation, or student-focused solutions.

Team **Vertex** -- Priyansh Bharti, Jiya chaddha

`2026-04-07`

---

### StudyBuddy
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/studybuddy-f190) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/monojitgoswami69/hacktropica) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Improving learning beyond and within classrooms

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square) ![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-333333?style=flat-square)

**The problem it solves**

Modern educational institutions operate in a highly fragmented digital environment, where learning resources, communication, and academic support are spread across multiple disconnected platforms such as WhatsApp, Google Classroom, shared drives, and informal notes. This fragmentation creates inefficiencies in accessing relevant study material and prevents students from having a consistent, structured learning experience.

At the same time, while AI-powered tools are increasingly used by students for doubt solving, they are **not aligned with institutional curricula**. These systems often generate responses that are either out-of-syllabus, lack contextual grounding, or directly provide answers without reinforcing conceptual understanding. This results in shallow learning and reduces academic reliability.

From an institutional perspective, the problem is more severe. Faculty members and administrators currently lack **granular visibility into student comprehension** at the module or topic level. There is no systematic way to identify:

* Which concepts students consistently struggle with
* Whether teaching methods are effective across different cohorts
* Where curriculum delivery is breaking down

As a result, education systems today function without a **closed feedback loop** between teaching, learning, and measurable outcomes. Decisions are often reactive rather than data-driven, and opportunities for timely academic intervention are lost.

---

### Our solution

We address these challenges by building a **curriculum-aware, AI-powered academic platform** that unifies learning, support, and analytics into a single system.

At the student level, the platform provides a **RAG-based AI tutor** that is strictly grounded in institution-specific content. This ensures that every response is:

* Contextually accurate
* Aligned with the prescribed syllabus
* Supported with citations for transparency and trust

In addition, students gain access to a **centralized repository of study materials**, eliminating the need to navigate multiple platforms, and a **flash quiz generation system** that enables continuous practice and reinforcement.

At the faculty and administrative level, the platform introduces a **data-driven analytics layer**. Faculty can structure curriculum and monitor engagement, while HODs and administrators gain access to:

* Module-level and subject-level performance insights
* Identification of commonly misunderstood topics
* Indicators of potential gaps in teaching effectiveness

This creates a **closed-loop academic system**, where student interactions and performance data continuously inform teaching strategies and curriculum improvements.

**Challenges we ran into**

Building a curriculum-aware AI system within a real academic workflow introduced multiple technical and architectural challenges:

---

#### 1. Ensuring strictly curriculum-bound AI responses

Generic LLMs tend to hallucinate or pull in external knowledge beyond the syllabus, which directly conflicts with our requirement of controlled, institution-specific answers.

**What we did:**

* Designed a **RAG pipeline with strict retrieval gating**, ensuring responses are generated only from approved academic sources
* Implemented **context filtering and chunk relevance scoring** to avoid noisy or low-quality retrievals
* Added **citation generation** to enforce transparency and allow users to verify sources

---

#### 2. Handling fragmented and unstructured academic content

Study materials came in inconsistent formats (PDFs, notes, slides), often poorly structured and not optimized for retrieval.

**What we did:**

* Built a preprocessing pipeline involving:

  * Text extraction and normalization
  * Semantic chunking instead of naive splitting
  * Metadata tagging (subject, module, topic) for filtered retrieval
* This significantly improved retrieval accuracy and response grounding

---

#### 3. Balancing retrieval accuracy with latency

High-quality semantic search (especially across multiple filters like subject/module) introduced latency, which negatively impacted user experience.

**What we did:**

* Optimized vector search using **index partitioning (by year/subject)**
* Used **lightweight pre-filtering before similarity search**
* Tuned embedding size vs speed trade-offs to maintain responsiveness

---

#### 4. Designing meaningful academic analytics

Raw interaction data is noisy and does not directly translate into actionable insights for faculty or HODs.

**What we did:**

* Defined **clear academic metrics**, such as:

  * Topic-level query frequency
  * Error concentration zones
  * Student performance clustering
* Aggregated this into **module-level and subject-level insights** to highlight weak areas in teaching or understanding

---

#### 5. Building a multi-role system (students, faculty, admin)

Each user type required different capabilities, access controls, and data visibility, increasing system complexity.

**What we did:**

* Designed a **role-based architecture** with scoped permissions
* Separated data layers to ensure:

  * Students see only learning tools
  * Faculty access structured insights
  * Admins get cross-cohort analytics

---

#### 6. Maintaining response quality under limited data

In early stages, limited academic content reduced the effectiveness of retrieval-based answers.

**What we did:**

* Introduced **fallback strategies**, including:

  * Confidence thresholds for responses
  * Prompt constraints to avoid speculative answers
* Focused on improving dataset quality rather than over-relying on the model

---

**Best EdTech Project**

Our project directly aligns with the **EdTech track** by addressing a core limitation in current digital education systems: the absence of **curriculum-aligned AI support and measurable learning feedback loops**.

Unlike generic AI tutoring tools, our platform is designed specifically for **institutional deployment**, where accuracy, syllabus adherence, and accountability are critical. By leveraging a RAG-based architecture constrained to institution-approved content, we ensure that student interactions remain **reliable, verifiable, and academically relevant**, which is a key requirement in real-world education environments.

Beyond student support, the platform extends into an often-overlooked area in EdTech — **teaching effectiveness and academic analytics**. Our system captures and processes student interaction data to generate **module-level and subject-level insights**, enabling faculty and administrators to identify:

* Frequently misunderstood concepts
* Gaps in curriculum delivery
* Patterns in student performance across cohorts

This shifts the role of EdTech from passive content delivery to **active academic optimization**, where both learning and teaching can be continuously improved using data.

Additionally, by consolidating study materials, doubt solving, and practice tools into a single platform, we reduce ecosystem fragmentation and create a **structured, unified learning environment**, which is essential for scalability in institutional settings.

**Best Use of MongoDB**

Our platform relies heavily on **MongoDB as a flexible, high-performance data layer** to support the dynamic and unstructured nature of educational data and AI-driven workflows.

Unlike traditional relational databases, our system deals with **heterogeneous data types**, including:

* Unstructured academic content (PDFs, notes, extracted text chunks)
* Semi-structured metadata (subject, module, topic hierarchies)
* User interaction logs (queries, responses, quiz attempts)
* Analytics data generated from student behavior

MongoDB’s document-based model allows us to store and query this data **without rigid schemas**, which is critical as curriculum structures and content formats evolve across institutions.

---

### Key use cases of MongoDB in our system

#### 1. Content storage and retrieval for RAG

We store processed academic content as **document chunks with rich metadata**, enabling:

* Fast filtering (by subject, module, topic)
* Efficient retrieval pipelines before vector search
* Seamless updates when curriculum changes

---

#### 2. User interaction tracking at scale

Student queries, AI responses, and quiz attempts are stored as **event-like documents**, allowing us to:

* Capture fine-grained learning behavior
* Build longitudinal learning profiles
* Support real-time analytics without complex joins

---

#### 3. Analytics and insights generation

MongoDB enables aggregation pipelines that power:

* Module-level performance metrics
* Identification of high-frequency doubt areas
* Cohort-based analysis for faculty and HOD dashboards

This allows us to transform raw interaction data into **actionable academic insights**.

---

#### 4. Role-based system design

We manage multiple user roles (students, faculty, admin) with different data access patterns. MongoDB’s flexible schema allows us to:

* Store role-specific data efficiently
* Adapt permissions and structures without costly migrations

---

### Why MongoDB was the right choice

* Schema flexibility for evolving academic structures
* High read/write throughput for real-time interactions
* Native support for nested and hierarchical data (ideal for curriculum modeling)
* Scalable architecture suitable for multi-institution deployment

---

**Best Use of Gemini API**

Our platform leverages the **Gemini API as the core intelligence layer** to deliver reliable, context-aware academic assistance within a controlled, curriculum-bound environment.

A key challenge in education-focused AI systems is ensuring that responses are not only accurate, but also **aligned with institutional content and pedagogical intent**. We address this by integrating Gemini within a **RAG-based architecture**, where the model is guided strictly by retrieved academic context. Gemini’s strong reasoning capabilities allow it to:

* Generate **context-grounded explanations instead of generic answers**
* Maintain coherence across multi-step academic queries
* Adapt explanations based on the complexity of the topic

---

### Key ways we utilize Gemini API

#### 1. Context-aware academic tutoring

Gemini processes retrieved content chunks and generates **structured, easy-to-understand explanations**, ensuring:

* No out-of-syllabus drift
* Concept-focused guidance instead of direct answer dumping
* Citation-backed responses for transparency

---

#### 2. Intelligent quiz and practice generation

We use Gemini to dynamically generate **flash quizzes and practice questions** from curriculum content, enabling:

* Rapid reinforcement of concepts
* Variation in question patterns
* Continuous student engagement

---

#### 3. Academic content transformation

Gemini helps convert raw academic material into:

* Simplified explanations
* Summarized notes
* Structured learning outputs

This improves accessibility of complex topics for students.

---

#### 4. Signal generation for analytics

Student interactions processed through Gemini (queries, misunderstandings, response patterns) act as **semantic signals**, which are later used to:

* Identify weak concepts
* Detect learning gaps
* Feed into higher-level academic analytics

---

### Why Gemini API was critical

* Strong **reasoning and contextual understanding**, essential for academic use cases
* Ability to generate **structured and pedagogically useful outputs**, not just raw answers
* Efficient handling of long-context inputs, improving performance in RAG pipelines
* Consistent output quality across varied academic subjects

---

Team **Nohara Family** -- [Monojit Goswami](https://github.com/monojitgoswami69), [Shubhadeep Biswas](https://github.com/sbr69)

`2026-04-05`

---

### FlowEval
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/floweval-1c3f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Agni-glitch/FlowEval_hacktropica) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Cognitive Grading System for Educational purposes

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Closing the Delayed Feedback Loop
In traditional settings, by the time students receive feedback, they have often moved on to new topics, making the corrections less useful.

Real-Time Intervention: FlowEval provides instant, actionable feedback while the learning is still fresh.

Data-Driven Insights: It automatically generates Sentiment Radar Charts (measuring Clarity, Fact Density, etc.), turning raw feedback into visual data that helps teachers identify class-wide learning gaps.
Overcoming Manual Grading Burnout and Inconsistency
Manual grading is mentally draining and prone to personal bias, fatigue, and inter-rater variability.

Sentiment Calibration: It addresses human subjectivity by allowing teachers to set an "Examiner Persona" (e.g., Harsh Critic vs. Lenient Mentor), ensuring consistent grading across hundreds of papers.

Scalability: It handles high-volume tasks (like grading long-form essays or complex flowcharts) that would typically take a teacher dozens of hours.
Eliminating the "Black Box" of Automated Grading
Most AI grading tools are "wrappers" that provide a score without explanation, leading to student distrust. FlowEval solves this through:

Logical Trace Analysis: Instead of a generic grade, it simulates the student’s logic and identifies the exact "Divergence Point" where an algorithm or math problem fails.

**Challenges we ran into**

API & Model Availability
Gemini deprecations — gemini-1.5-flash was deprecated mid-development, forcing a switch to gemini-2.0-flash. Then gemini-2.0-flash hit free tier quota limits (limit: 0), meaning the model wasn't available on the free tier in that region at all — not a rate limit, a hard wall.
Free tier exhaustion — Multiple Gemini API keys from multiple accounts all hit quota. This is because Google ties free tier limits to the project/billing account, not just the key. Creating new keys under the same Google account reuses the same quota pool.

**Best Use of MongoDB**

The "Polymorphic Schema" Advantage
MongoDB’s document model is the perfect fit for FlowEval 2.0 because it handles two vastly different data structures in one collection without complex SQL joins:

Mode-Agnostic Storage: Store a Graph-based HIR Map (for logic) and a Thematic Heatmap (for essays) within the same evaluation object.

Performance: All "Digital Red Pen" data (highlights, stats, and logic nodes) is nested in a single document, allowing the frontend to fetch everything in one database query.

Rapid Iteration: You can add new AI metrics (like "Sentiment Scores" or "Plagiarism") instantly without the "migration nightmare" of traditional databases.

Why Mongoose?
Data Integrity: It enforces strict validation for sentimentProfiles and strictness levels while keeping the database flexible.

Developer Speed: Built-in middleware (like pre('save') for password hashing) handles security automatically, letting you focus on the AI logic.

**Best Use of Gemini API**

For your project, FlowEval 2.0, the Gemini API acts as the "Cognitive Engine" that powers the transition from raw student input to structured, pedagogical feedback. You are using the Gemini 1.5 Flash/Pro multimodal capabilities to bridge the gap between human reasoning and digital data.

Here is exactly how the Gemini API key is being utilized in your workflow:

1. Multimodal Logic Extraction (The "Parser")
When a teacher or student uploads a file—whether it is a handwritten flowchart, a digital image, or a text-based essay—you use the Gemini API to "see" and "read" the content.

Logical Mode: Gemini analyzes the visual structure of flowcharts and converts them into a Hierarchical Intermediate Representation (HIR). This turns a picture into a JSON-based logic map consisting of nodes and edges.

Subjective Mode: Gemini performs Latent Semantic Analysis to identify key historical facts, literary themes, or geographical concepts within a written response.

2. Dual-Core Evaluation (The "Brain")
The API key allows your backend to send complex, persona-driven prompts that control how the AI "thinks":

Sentiment Simulation: In Subjective Mode, the API simulates specific Examiner Archetypes (e.g., "Harsh Critic" vs. "Lenient Mentor") to provide feedback that matches a specific grading tone.

Symbolic Execution: In Logical Mode, Gemini doesn't just look for keywords; it simulates the execution trace of the student's logic to find the exact "Divergence Point" where their algorithm fails.

3. Coordinate-Mapped Annotation (The "Digital Red Pen")
Rather than just giving a final score, you use Gemini’s structured output to generate point-of-interest feedback:

Visual Highlighting: The API returns specific snippets of text or node IDs that contain errors.

JSON Overlay: Your application takes this structured JSON response and overlays it as a "Red Pen" layer on the frontend, allowing students to see hover-able tooltips explaining their mistakes.

4. Quantified Data Visualization
You use the API to generate raw numerical scores for various criteria like Clarity, Strictness, Tone Positivity, and Fact Density. This data is then fed directly into your Recharts Radar Chart on the frontend, transforming "AI chat" into a professional data visualization.

Team **NameNotFoundExceptions** -- [Arpan Das](https://github.com/ArpanDasGitHub), [Agni Roybar](https://github.com/Agni-glitch), [Abhirup Saha](https://github.com/abhirup004)

`2026-04-05`

---

### Tropic Town
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tropic-town-626a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arnob-B/hacktropica-localhost) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1Z58HS0o1HQ) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Where education meets innovation

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Traditional Learning Management Systems (LMS) often suffer from a disconnect between effort and reward.
Low Engagement: Standard video-and-quiz formats often feel like a chore, leading to high drop-off rates (often as high as 90% in self-paced courses).
Abstract Rewards: Grades and digital certificates are "static" and lack immediate utility for the student.
Isolation: Virtual learning frequently lacks the "campus feel" where social interaction and spontaneous discovery occur.

**Challenges we ran into**

We are building a persistent 2D world where learning is an exploration, not a list of links.
Immersive Navigation: Using a Phaser.js engine integrated into a React frontend, students move an avatar through a virtual campus.
Contextual Classrooms: Entering a building leads to a corridor of classrooms. Each door represents a specialized module where users can initiate real-time video calls or submit tasks.
The Token Loop: We utilize Solana to issue utility tokens.
Earn: Complete assignments $\rightarrow$ Receive Solana-based coins.
Spend: Use coins in the "Game Map" area to unlock mini-games, customize avatars, or access premium social zones.
For Students: Provides Immediate Gratification. The "Learn-to-Earn" (L2E) model transforms academic milestones into tangible assets that have immediate value within the platform's ecosystem.
For Educators: Higher Retention Rates. Gamification has been shown to improve student motivation by over 71%.
For the Platform: The use of Solana ensures low transaction fees and sub-second finality, making the micro-reward system financially viable at scale.

Team **localhost:6767** -- [Asmit Deb](github.com/asmitdeb), [Aritra Sarkar](https://github.com/AritraS05), [Rahul Pandey](https://github.com/rahul-p19), [Arnob Bhakta](https://github.com/Arnob-B)

`2026-04-05`

---

### Resq-ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resqai-50fc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/harshchhabraa/Resq-AI-hacknovate) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://resq-ai-hacknovate-qtd1.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> An AI-Driven, Community-Powered, End-to-End

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Current disaster alert systems only notify users but don’t tell them what to do next.
Alerts are often generic, delayed, or unclear, leading to panic, poor decisions, and unsafe situations—especially for vulnerable groups.
This application converts alerts into personalized, real-time action plans.

- Uses location + quick survey to understand user context

- Generates step-by-step checklists for immediate action

- Suggests safe evacuation or stay strategies

- Updates guidance as conditions change

- Supports multiple languages + voice instructions

Impact:

- Reduces panic with clear, actionable guidance

- Enables faster and safer decision-making

- Makes disaster response accessible to everyone

**Challenges we ran into**

- Real-time data integration: Combining multiple data sources (weather, location, user inputs) reliably and quickly

- Personalization vs speed: Generating accurate, context-aware plans within seconds during emergencies

- Handling edge cases: Supporting users with no internet, no transport, or high-risk conditions

- UX under stress: Designing a simple, intuitive interface that works in panic situations

- Multilingual & accessibility support: Ensuring clarity across languages and adding voice guidance

- Dynamic updates: Continuously adapting plans as conditions (routes, risk levels) change

Team **kasukabe** -- [Harsh Chhabra](https://github.com/harshchhabraa), [Shivansh PrasadChaudhary](https://github.com/shivanshpc), [Tanishka Jayant](https://github.com/tanishkajayant), [Siya Satija](https://github.com/SiyaSatija)

`2026-04-04`

---

### EDUPATH-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edupathai-2182) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hemendra-opensource/HACKNOVATE-PROJECT) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> CENTRALIZED LEARNING DASHBOARD FOR STUDENTS

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

📚 Students don't know what to study next → solved by the AI Recommendation Engine that scores every unlocked skill
🧠 No way to measure what a student actually knows → solved by Bayesian Knowledge Tracing (BKT) that updates mastery after every answer
🗺️ No visual map of learning progress → solved by the interactive Knowledge Graph showing locked/unlocked/mastered skills
🤖 No personalised tutoring at scale → solved by the Gemini-powered AI Tutor that adapts its language to the student's mastery level
📋 No structured study plan → solved by the ML Plan Generator using topological sort + weighted gap analysis
🔁 Students forget what they've learned → solved by the Spaced Repetition System (SRS) with SM-2 algorithm scheduling
😴 No awareness of cognitive overload → solved by Intelligence Widgets (burnout detection, cognitive load, optimal study time)

Team **RESEARCH RADIANCE** -- [AMAN GUPTA](https://github.com/amangupta9454), [Anshu .](https://github.com/anshu2006288), [Hemendra Sharma](https://github.com/hemendra-opensource), [Himanshu Gupta](https://github.com/himanshu561hi)

`2026-04-04`

---

### Carevista
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/carevista-dc6f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mukundangopalachary/carevista-telemedicine-2) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ISjaf9eOUFg) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co)

> Rural first , consent driven offline capable

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![ngrok](https://img.shields.io/badge/ngrok-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Agora API](https://img.shields.io/badge/Agora%20API-333333?style=flat-square)

**The problem it solves**

our platform primarily solves the problem of doctors lacking structured and reliable patient information in rural telemedicine environments with limited internet access, which increases cognitive load and reduces the quality of consultations. In many low-resource settings, patients not only struggle to clearly describe symptoms due to language and literacy barriers, but also face poor or unstable internet connectivity, making real-time, smooth consultations difficult. This forces doctors to spend valuable time both understanding fragmented patient input and dealing with incomplete or interrupted communication. Our system addresses this by enabling low-bandwidth-friendly input methods(voice or text), converting unstructured data into concise, structured clinical summaries that can be reviewed asynchronously or with minimal connectivity. In addition, it improves efficiency and access by introducing basic triage to prioritize cases, ensuring urgent patients are seen first without requiring continuous online presence. Finally, it attempts to tackle the financial barrier to care by allowing patients to request anonymous support for treatment-related expenses, although this remains a secondary, independent feature.

In short, our system solves:

Unstructured + low-connectivity patient communication →converts messy, intermittent input into clear, doctor-ready summaries
High doctor cognitive load →reduces time spent gathering and reconstructing patient information
Poor internet access →supports asynchronous, low-bandwidth interactions instead of relying on continuous video calls
Inefficient consultation flow → enables prioritization through non-diagnostic triage
Financial drop-offs in care →provides optional, anonymous support for treatment costs (secondary feature)

**Challenges we ran into**

In a hackathon setting, we faced several challenges primarily related to scope, feasibility, and time constraints. Our initial idea combined multiple complex components such as telemedicine, AI-assisted intake, triage, and crowdfunding, which made it difficult to build a complete and functional system within a limited timeframe. We also lacked access to real medical datasets, making it challenging to implement a fully trained AI model, and had to consider practical constraints like low internet connectivity and the need for a simple, intuitive user experience. Additionally, clearly demonstrating the value of the system to judges without overcomplicating the prototype was a key challenge.

We overcame these challenges by strategically narrowing our focus to a core, high-impact feature—structured patient intake and doctor-ready summaries instead of attempting to build the entire system. We replaced complex AI models with rule-based or simulated logic to generate reliable outputs within the given constraints. To address feasibility, we designed a lightweight and low-bandwidth-friendly workflow, avoiding dependence on real-time heavy infrastructure. We also prioritized clear and effective user flows, ensuring that the transformation from patient input to doctor summary was easy to understand and demonstrate. More advanced components like AI learning and crowdfunding were presented as future extensions rather than fully implemented features, allowing us to deliver a working, focused prototype. Overall, we approached the hackathon by simplifying the system, focusing on usability, and ensuring a strong, end-to-end demonstration instead of trying to do everything at once.

**Open Innovation**

Our project fits the Open Innovation track because it presents a flexible, extensible platform that rethinks how patient-doctor interactions are structured using assistive AI, rather than being limited to a single narrow use case. While it is applied in rural telemedicine, the core innovation—converting unstructured human input into structured, decision-ready summaries—can be adapted across multiple domains such as urban healthcare, emergency response, or even other sectors that rely on expert decision-making. The system is designed with a modular architecture, where components like AI-assisted intake, triage, and support systems can evolve independently over time. Additionally, by emphasizing a human-in-the-loop approach, where AI assists but does not replace professionals, the solution aligns with sustainable and responsible innovation principles. This openness in design, scalability, and cross-domain applicability makes our project a strong fit for the Open Innovation track.

Team **Ctrl Alt Hacks** -- [Mukundan Gopalachary](https://github.com/mukundangopalachary), [Shriya Srinivasan](https://github.com/shriyasrinivasann), [Srividhya Parthasarathy](https://github.com/Srividhyapartha), [Shreya Kasi](https://github.com/Shreya10052006)

`2026-03-29`

---

### ScholarTrace
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scholartrace-74db) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/megha-muhuri06/ScholarTrace) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> For Students in Need

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The core 3 problems it solves is the direct answering learning trap. It provides socratic method of solving question of hallucination and accuracy problem. We use RAG system to generate every response mathematically. The blackbox for educators. It curator control dashboard provides real time frictional telementry.

**Challenges we ran into**

1. API Errors
2. System Deadlocks
3. Meta data sync
4. Startup Crashes
5. Motion Logic

Team **SkillSeedd** -- [Megha Muhuri](https://github.com/megha-muhuri06), [Priyanshu Das](https://github.com/dpriyanshu888-droid), [Sahina Mamtaj](https://github.com/Sm-2007-code)

`2026-03-28`

---

### EDUXA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eduxa-f81d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shrimant05/AI_TUTOR) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> Empowering Students to Think, Not Just Retrieve

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square)

**The problem it solves**

EDUXA: The Grounded Socratic Tutor "Guiding Minds, Not Just Providing Answers."🚀 

The VisionEDUXA was engineered from the ground up to solve a critical flaw in modern AI education: the "Answer Machine" crisis. While generic LLMs act as a shortcut for students, EDUXA acts as a Socratic Scaffold, using a Grounded RAG architecture to guide students toward understanding while staying strictly within the boundaries of faculty-verified material. 

🎯 Alignment with the Problem StatementWe didn't just build a chatbot; we designed a high-precision engine tailored to the specific requirements of the challenge:Grounded Accuracy: By implementing a Similarity Threshold (0.4) and hybrid search, we ensure a 95%+ query accuracy rate, strictly refusing out-of-scope questions.Mandatory Citations: Every response is dynamically linked to metadata, providing Page-Level and File-Name citations so students can verify logic in their physical notes.

Socratic Pedagogy: The system identifies misconceptions and responds with Level-based hints and guiding questions instead of direct solutions.Data Isolation: Using isolated vector namespaces, we ensure that Student A's private notes are never accessible to Student B, satisfying all privacy requirements.

🌟 Major Achievements & Extra FeaturesBeyond the core requirements, ByteHacks pushed the boundaries of multimodal learning:🖊️ Handwritten Notes Embedding (The Big Achievement): We successfully implemented an OCR-enhanced ingestion pipeline.  This allows EDUXA to process "messy" handwritten lecture notes, transforming scanned images into searchable vectors—a breakthrough for legacy academic archives.

🎙️ Voice-Activated Tutoring: For a more natural learning experience, we integrated a Voice Mechanism, allowing students to engage in Socratic dialogue hands-free, making the tutor accessible for diverse learning needs.

🖼️ Student-Side Image Support: Students can upload images of diagrams or handwritten problems. EDUXA "sees" the context and provides Socratic hints based on the visual input, bridging the gap between text and imagery.

📊 The Ripple EffectEDUXA creates a data-driven ecosystem for both ends of the classroom:For Students: 24/7 inquiry-based guidance that builds academic autonomy. For Faculty: Reclaims 70% of manual effort by automating FAQs and generating Real-Time Confusion Heatmaps to pinpoint curriculum "hotspots." 🛠️ 


Technical StackBackend: Spring Boot (Java) for high-concurrency API orchestration. RAG Engine: FastAPI (Python) using LangChain for recursive chunking and reranking.Vector Store: MariaDB & ChromaDB for high-precision metadata-driven indexing. LLM: Gemini 1.5 Flash for low-latency, multimodal Socratic reasoning.

**Challenges we ran into**

local llm ollama showed very high latency

Socratic "hint-ladder" constraints

OCR pre-processing layer to accurately transcribe and index non-digital academic archives

**EDUCATION**

Gemini said
EDUXA fits the education track by transforming AI from a direct-answer engine into a grounded Socratic partner that reinforces academic integrity through inquiry-based guidance. By anchoring responses strictly to faculty-verified materials with 95%+ query accuracy and mandatory page-level citations, the system creates a hallucination-free environment for deep learning. Our specialized RAG architecture achieves significant multimodal milestones, including a Voice Mechanism for natural dialogue, student-side image support for visual problem solving, and a breakthrough handwritten notes embedding pipeline that digitizes legacy academic archives. Furthermore, EDUXA empowers instructors with real-time confusion heatmaps, reclaiming 70% of faculty time from repetitive queries to allow for more impactful, data-driven mentorship.

Team **ByteHacks** -- [Shrimant Shaw](https://github.com/Shrimant05), [Anushka Shaw](https://github.com/anushkashaw951), [Aditya Kumar Shaw](https://github.com/Itadi02), [Akash Sadhukhan](https://github.com/IamAkashSadhukhan)

`2026-03-28`

---

### BEACON
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/beacon-d3c9) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://beacon-landing-page-one.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> AI-Powered Web Accessibility & Security Audits

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Lighthouse](https://img.shields.io/badge/Lighthouse-333333?style=flat-square) ![Featherless.ai](https://img.shields.io/badge/Featherless.ai-333333?style=flat-square)

**The problem it solves**

BEACON (Benchmarking & Evaluation of Accessibility Compliance Optimization Node) addresses the critical and growing accessibility gap in modern web applications, where dynamic, feature-rich websites often unintentionally exclude users with disabilities—such as those with visual impairments, motor limitations, or cognitive challenges. Despite established standards like WCAG 2.2, developers frequently lack practical, intuitive tools to identify, contextualize, and resolve accessibility issues across entire websites. Traditional auditing solutions typically deliver raw, overwhelming reports without meaningful visualization, historical tracking, or actionable guidance, making compliance feel like an afterthought rather than an integrated part of development workflows.

This results in:
- **Poor user experience** for millions of users who rely on assistive technologies.
- **Legal and reputational risks** from non-compliance with accessibility regulations (e.g., ADA, Section 508).
- **Inefficient development cycles** where accessibility is treated as a separate, burdensome task instead of a core quality metric.

BEACON transforms accessibility auditing from a reactive, manual chore into a proactive, automated, and insightful process. By combining rule-based scanning (axe-core, Lighthouse, custom WCAG checks) with AI-powered semantic analysis, it catches not just surface-level violations but also complex cognitive and contextual issues that rule engines miss. The platform enables users to:

- **Automate comprehensive audits**: Scan entire websites for accessibility, security, and performance issues with multi-page crawling and real-time monitoring.
- **Gain contextual insights**: Visualize issues directly on pages, track scores over time, and receive AI-generated explanations and code fix suggestions.
- **Integrate seamlessly**: Use browser extensions for live overlays, VS Code extensions for development-time checks, dashboards for project management, and CI/CD integrations (e.g., Lighthouse CI) for continuous compliance.
- **Achieve compliance effortlessly**: Generate branded PDF reports, compliance certificates, and even auto-create GitHub pull requests with AI-recommended fixes.

For developers, QA teams, and accessibility specialists, BEACON makes auditing **easier** by eliminating manual testing, providing clear guidance, and offering benchmarking against industry standards. It makes processes **safer** by ensuring inclusivity, reducing legal exposure, and fostering a culture of accessible design from the start. Businesses can use it to maintain compliance, improve user satisfaction, and demonstrate commitment to diversity—turning accessibility from a checkbox into a competitive advantage. Whether you're building inclusive web experiences or retrofitting existing sites, BEACON bridges the gap between identification and resolution, making the web more accessible for everyone.

**Challenges we ran into**

Building BEACON as a multi-layered, AI-enhanced accessibility auditing platform presented several significant hurdles, from integrating complex technologies to debugging runtime issues. As a full-stack project combining Python backends, React frontends, browser extensions, and AI systems, we encountered challenges that tested my problem-solving skills and forced me to deepen my understanding of web development, accessibility standards, and system architecture. Below, I'll detail some key bugs and obstacles, along with how we overcame them.

#### 1. **API Error Handling Leading to Cryptic Console Errors**
   - **The Hurdle**: During frontend development, API requests to the FastAPI backend were throwing generic `"[object Object]"` errors in the browser console. This occurred because the error response from the server contained a JSON object in the `detail` field (e.g., `{ "message": "Invalid URL", "code": 400 }`), but the frontend's error handling code was directly passing this object to `new Error()`, which converted it to a meaningless string representation.
   - **Impact**: Users saw unhelpful error messages, making debugging difficult and degrading the user experience during scans or project management.
   - **Solution**: We modified the error handling in `frontend/lib/api.ts` to check the type of `error.detail`. If it was a string, use it directly; otherwise, stringify the object with `JSON.stringify()`. This ensured meaningful error messages like `"{"message":"Invalid URL","code":400}"` or custom fallbacks. We also added logging to capture raw responses for better debugging. This fix improved error visibility and helped identify server-side issues faster.

#### 2. **JSX Parsing Errors in Complex Dashboard Components**
   - **The Hurdle**: A build error `"Expected '</', got '{'"` appeared in the Next.js dashboard (`app/dashboard/[projectId]/page.tsx`), pointing to a comment line. The root cause was an unclosed `<div>` tag in a grid layout containing conditional rendering for charts and auth-detected pages. The parser expected a closing tag but encountered the opening brace of a conditional block, causing the entire component to fail compilation.
   - **Impact**: The build process halted, preventing deployment and testing of new features like score history visualization.
   - **Solution**: We carefully audited the JSX structure, counting opening and closing tags. The issue was a missing `</div>` to close the grid container after the AI Analysis section. Adding the tag resolved the parsing error. To prevent future issues, we adopted stricter JSX linting rules and used tools like Prettier for auto-formatting, ensuring balanced tags in complex conditional renders.

#### 3. **Integrating AI-Powered RAG Semantic Analysis with Rule-Based Scanning**
   - **The Hurdle**: Combining Layer 1 (rule-based axe-core/Lighthouse scans) with Layer 2 (RAG-based semantic analysis) was challenging. The vector store (using NumPy and sentence-transformers) needed to filter out issues already caught by Layer 1, but initial implementations caused duplicate findings or missed nuanced problems like cognitive language complexity. Additionally, embedding generation for 86+ WCAG criteria was computationally intensive, leading to timeouts during scans.
   - **Impact**: Scans were slow, inaccurate, or failed entirely, undermining the platform's core value of comprehensive auditing.
   - **Solution**: We refactored the scan pipeline in `backend/services/scan_service.py` to run Layer 1 first, collect rule IDs, and pass them as filters to the RAG query. For performance, we implemented batch embedding and caching with a hybrid retrieval (70% semantic + 30% BM25). Testing with sample websites and profiling with Python's `cProfile` helped optimize query times. This hybrid approach ensured faster, more accurate results without sacrificing depth.

#### 4. **Browser Extension Development and Cross-Origin Issues**
   - **The Hurdle**: Building Chrome extensions (MV3) for live accessibility overlays required handling content scripts that inject into any webpage. Initial attempts to communicate between popup scripts and content scripts failed due to cross-origin restrictions and asynchronous message passing, leading to overlays not displaying or crashing on certain sites.
   - **Impact**: The extension, a key "multi-surface" feature, was unreliable, limiting real-time auditing capabilities.
   - **Solution**: We studied Chrome's extension APIs and implemented proper message passing using `chrome.runtime.sendMessage()` and listeners. For cross-origin issues, we used `chrome.scripting.executeScript()` to inject scripts safely. Testing across multiple sites (including those with CSP headers) and using the Chrome DevTools extension debugger helped isolate issues. This resulted in a stable overlay that highlights accessibility issues directly on pages.

#### 5. **PDF Report Generation and Template Rendering**
   - **The Hurdle**: Gener

Team **Localbros:3000** -- [David Porathur](https://github.com/41vi4p), [Swar Churi](https://github.com/SC136), [Sai Balkawade](https://github.com/WillyEverGreen), [Sherwin Gonsalves](github.com/SHERV22)

`2026-03-26`

---

### Scanable
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/scanable-bf87) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Yashpithwa/noobs_next_door_hn4) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/98gtnWBhLO4) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> Building the next standard of accessibility

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![npm](https://img.shields.io/badge/npm-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-333333?style=flat-square)

**The problem it solves**

Modern web applications are often not accessible to all users.

Many developers only check accessibility at the end of development, or sometimes not at all. This leads to websites that are difficult or impossible to use for:

Users with visual impairments
Keyboard-only users
Screen reader users

As a result, accessibility issues remain unnoticed and reach production

**Challenges we ran into**

Handling Dynamic Websites

Modern websites load content using JavaScript, so simple HTTP scraping was not enough.

Problem:
Some elements were not visible during scanning.

Solution:
I used Puppeteer to render the full page and wait for content to load before scanning.

2. Navigation Timeout Errors

Problem:
I often got navigation timeout errors while loading heavy or slow websites.

Solution:
I increased the timeout and switched to domcontentloaded instead of waiting for full network idle.
I also added fallback handling so the scan doesn’t crash.

3. False Positives in Detection

Problem:
Some elements were incorrectly flagged as issues (e.g., buttons with hidden labels).

Solution:
I improved rule logic to consider context like aria-label, alt, and inner text.

4. Detecting Keyboard Accessibility

Problem:
It was difficult to check whether elements were truly usable via keyboard.

Solution:
I used Puppeteer and custom logic to simulate focus and detect focusable elements.
5. Performance Issues with Multi Crawling

Problem:
Scanning multiple pages at once caused high memory usage and slow performance.

Solution:
I implemented controlled concurrency and avoided duplicate URL scans using a Set.

🟢 6. Integrating CI/CD

Problem:
Making the tool fail builds correctly inside GitHub Actions was tricky.

Solution:
I added exit codes (process.exit(1)) based on scan results to enforce accessibility.

7. Generating Useful AI Explanations

Problem:
Raw accessibility errors were hard to understand.

Solution:
I integrated an LLM to convert technical issues into simple explanations and fixes.

8. Designing Game Mode

Problem:
Making developers feel accessibility issues instead of just reading them.

Solution:
I created a keyboard-only mode with visual restrictions to simulate real user challenges.

Team **NOOB'S NEXT DOOR** -- [Yash Pithwa](https://github.com/Yashpithwa), [Vansh Jain](https://github.com/jvansh1204), [Rachit Chotalia](https://github.com/RachitChotalia), [Tanishk Sancheti](https://github.com/tanSan9869)

`2026-03-26`

---

### DevDiff
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/devdiff-23b6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DotSlash-9-0/Team-Garuda) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/60td4zLUMOE) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co)

> It is a learning PR intelligence engine

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

**DevDiff solves this by combining fast static checks + ML scoring + logic review + feedback learning.**

### What people can use it for
- Scan pull requests before merge for security and logic risks
- Get a **risk score** per PR instead of raw alert spam
- See findings in real-time during analysis (faster review loop)
- Track risk trends by project/developer (history, scorecard, heatmap)
- Reduce repeated false positives through feedback-based adaptation

### How it makes tasks easier/safer
- Makes code review **faster** (priority-first findings)
- Makes releases **safer** (critical issues surfaced early)
- Makes teams **smarter over time** (developer-specific learning profile)
- Makes demos/reviews **clearer** (explainable and visual analytics)

**Challenges we ran into**

### Challenge A: Analysis looked “empty” even when pipeline ran
- **Issue:** Users thought analysis failed if no findings were shown clearly.
- **Fix:** Added explicit analysis states (loading, streaming, completed, no-findings success message) and PR metadata visibility.

### Challenge B: ML/LLM appeared unreliable in real environments
- **Issue:** Python scorer process and optional LLM sometimes failed silently due to runtime/env differences.
- **Fix:** Added ML bridge resilience (python fallback candidates, timeout fallback score), clearer event handling for logic findings, and robust websocket state updates.

### Challenge C: Auth timeout confusion (“invalid token” vs network timeout)
- **Issue:** Temporary auth network errors looked like user token failures.
- **Fix:** Added retry + timeout-aware auth handling and returned graceful service-unavailable responses for transient failures.

### Challenge D: Repeated noisy alerts (same pattern keeps coming back)
- **Issue:** Same findings repeatedly distracted reviewers.
- **Fix:** Implemented staged false-positive lifecycle:
  - first feedback → tracked
  - next occurrence → low priority
  - repeated feedback → ignored/suppressed pattern in future scans

### Challenge E: Demo reliability (stale dev cache/process conflicts)
- **Issue:** Frontend chunk 404 / route errors from stale build artifacts and conflicting processes.
- **Fix:** Stabilized dev run flow (clean restart, cache clear, port hygiene) and validated critical routes/builds before demo.

**DevTech**

DevDiff is a strong DevTrack fit because it improves the complete developer workflow from PR creation to merge decision.

### Why it fits
- **Developer Productivity:** prioritizes real risks so reviewers spend time on high-impact issues.
- **Engineering Quality:** blends deterministic security rules with probabilistic ML confidence.
- **Operational Maturity:** project-scoped analytics, developer profiles, history, and feedback loops.
- **Human-in-the-loop AI:** not “black-box AI only”; reviewer feedback directly influences future behavior.
- **Adoption-ready:** dashboard + live stream + scorecard + heatmap makes it practical for real teams, not just research demo.

Team **Team Garuda** -- [kalpan kaneriya](https://github.com/kalpan2007), [Tapan Vachhani](https://github.com/Vachhani-Tapan), [Mohil Mundke](https://github.com/mundkes-tech)

`2026-03-22`

---

### Civic Service Radar
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/civictech-a234) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DotSlash-9-0/Runtime-Rebels) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/pZM5G9xiALk) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co)

> Bridging Language Gaps and Predictive AI Routing

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Traditional civic grievance systems are often fragmented, slow, and inaccessible to the common citizen. DotSlash solves these core problems:

1.Language Barriers: Most platforms require English or a specific regional language. We use NLLB-200 to allow citizens to report issues in 200+ languages (Hindi, Gujarati, Tamil, etc.), which are then automatically translated and unified for officials.
2,Manual Triage Overload: Municipal offices are buried under thousands of complaints. Our Semantic Centroid Model automatically classifies, validates, and ranks complaints by priority (0-100 score) based on severity and category, ensuring life-threatening emergencies are handled first.
Welfare Inaccessibility: Citizens often don't know which government schemes they qualify for. By utilizing Gemini 2.0 Flash, we extract profiles from uploaded identity documents and instantly match users with 700+ government schemes.
3.Information Asymmetry: People waste hours in queues at government offices. Our Computer Vision (YOLOv8) system provides real-time "Traffic Levels" and wait-time estimations for municipal centers, allowing for smarter resource routing.

**Challenges we ran into**

1.Model Optimization & Latency: Running heavy models like NLLB-200 (600M parameters) and Sentence Transformers while maintaining a responsive UI was a challenge. We solved this by architecting a dedicated FastAPI ML Microservice that runs independently of the Next.js frontend, allowing for asynchronous processing and better memory management.
2.The "Semantic Ambiguity" Problem: During testing, we found that generic text (like food recipes or casual chat) was sometimes incorrectly classified into civic categories with low confidence. We overcame this by implementing a Dual-Threshold filtering system and a Civic Confidence Guard (0.22 benchmark). Any input that doesn't strongly mathematically align with a known civic "centroid" is now accurately flagged as invalid.
Cross-Language Entity Extraction: Extracting specific entities (location, dates, names) from translated text required careful handling. We used a hybrid approach of NLLB-200 for translation and MiniLM-L6-v2 for semantic mapping to ensure the "meaning" of the complaint wasn't lost in translation.
3.E2E Multimodal Integration: Coordinating the flow of data—from a user uploading an Aadhaar image in Next.js to Gemini extracting JSON, and then persisting that profile to MongoDB Atlas—required a robust error-handling pipeline to deal with varying image quality and document formats.

**CivicTech**

1.Bridging the Linguistic Divide: By integrating NLLB-200, we ensure that language is no longer a barrier to justice. Every citizen can report grievances in their native dialect, ensuring that marginalized communities have an equal voice in municipal improvements.
2.AI-Driven Governance: Our Semantic Triage System replaces slow, manual sorting with an automated priority matrix (0-100 score). This ensures that critical infrastructure failures and emergencies are surfaced to the right department in seconds, not weeks.
3.Welfare Transparency: We simplify the overwhelming complexity of government welfare using Gemini 2.0 Flash. By automating eligibility matching from document uploads, we ensure that entitled citizens actually receive the benefits meant for them, reducing the "knowledge gap" in social security.
4.Real-Time Public Utility: Our Queue Prediction system (YOLOv8) and Live Map Alerts turn passive citizens into active data contributors, creating a real-time "Civic Radar" for the city's infrastructure health.

Team **Runtime Rebels** -- Samanvitha Bolisetty, Ansh Gupta, [Pratham Patadiya](https://github.com/Pratham722007), Naina Jain

`2026-03-22`

---

### Access ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/access-ai-d76d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HarshGupta492/ACCESSWAY-AI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/e7d571405be84f3eaa5ae1c16b7f4366) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Disability

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Current navigation systems like Google Maps are designed for the general population and focus primarily on finding the shortest or fastest route, without considering accessibility challenges. They do not account for real-world barriers such as stairs, broken sidewalks, steep slopes, or narrow pathways, which can make routes unsafe or completely unusable for wheelchair users, elderly individuals, and visually impaired people. Additionally, these systems lack real-time awareness of changing environments and do not provide personalized routing based on different user needs. As a result, over a billion people with mobility challenges face reduced independence, increased risk during travel, and limited access to public spaces. The core problem is that navigation today follows a one-size-fits-all approach, while accessibility requires adaptive, real-time, and user-specific solutions.

**Challenges we ran into**

## ⚠️ Challenges Faced During Development

While building AccessWay AI, several technical and practical challenges were encountered. One of the primary challenges was implementing real-time obstacle detection using YOLOv8 without causing performance issues, as continuous image processing can be computationally expensive. Integrating live camera input with the backend while maintaining low latency required careful optimization and asynchronous processing. Another major challenge was designing a dynamic accessibility graph using map data from OpenStreetMap and applying user-specific constraints such as slope, path width, and obstacle avoidance in routing algorithms like A*. Ensuring real-time synchronization across users using WebSockets and Redis was also complex, especially when handling frequent updates from both AI detection and crowdsourced inputs. Additionally, generating meaningful and context-aware voice navigation for visually impaired users using RAG and NLP required combining multiple systems effectively. Finally, managing a full-stack architecture involving React, FastAPI, ML models, and real-time communication within a limited development timeframe required careful planning, modular design, and prioritization of core features for the MVP.

Team **DevEyes** -- [Ashneet Jha](https://github.com/ashneetjha), Harsh Gupta, [SHLOK YAGNICK](https://github.com/Shlok0005), [Surbhi Kaushal](https://github.com/SurbhiKaushal)

`2026-03-17`

---

### VitalVoice
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitalvoice-b1af) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ashishkumarjaiswal999/vitalvoice-backend) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/10oaXEqFc7KIEpw-yG_SCpLeOdU18rZeh?usp=drive_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/Yr8NYIk_ciE?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Doctor in your pocket, in your language.

![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Camera](https://img.shields.io/badge/Camera-333333?style=flat-square) ![Room Database](https://img.shields.io/badge/Room%20Database-333333?style=flat-square)

**The problem it solves**

VitalVoice — Voice-First AI Healthcare Companion for Bharat
The Problem
700 million Indians live in rural areas with limited access to quality healthcare. Language barriers, lack of doctors, and health illiteracy make even basic medical guidance inaccessible. Most health apps are English-only and require strong internet — leaving the majority of India behind.
Our Solution
VitalVoice is a voice-first AI healthcare companion built specifically for India. It brings hospital-grade medical intelligence to anyone's pocket — in their own language, with their own voice.
What Makes Us Different
 Multi-Agent AI Pipeline
Built on CrewAI with a 2-agent architecture — an Intent Filter agent that blocks non-medical queries, and a Medical Analyst agent that provides accurate health guidance. Every response is grounded in a RAG (Retrieval Augmented Generation) pipeline using ChromaDB vector database with 18 medical knowledge documents sourced from WHO, CDC, and ICMR.


 10 Indian Regional Languages
VitalVoice speaks India's languages — Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi, and English. Users select their language and every AI response comes back in that language automatically.
🎤 Voice-First Design
Speak your symptoms in your language. VitalVoice listens, understands, and responds — making it accessible to users who cannot read or type.
11 Health Modules

Symptom Checker — AI-powered diagnosis assistance
Medicine Reminder — Never miss a dose
Mental Health — Daily emotional check-ins
Report Explainer — Scan and understand medical reports
Child Health — Growth and milestone tracking
Emergency First Aid — Instant guided emergency help
Rural Health Worker — Field-ready health assistance
Genetic Risk — Understand your genetic profile
Dental Health AI — Scan and analyze dental concerns
Accessibility Mode — Voice-first, high-contrast UI
FitFuel — AI fitness and nutrition coaching

Tech Stack

Android: Kotlin, Jetpack Compose, MVVM, Room DB, WorkManager
AI Backend: Python FastAPI + CrewAI multi-agent pipeline
Vector Database: ChromaDB with RAG pipeline
AI Model: Google Gemini (gemini-3-flash-preview)
Voice: ElevenLabs TTS + Android SpeechRecognizer
Knowledge Base: 18 medical documents (WHO/CDC/ICMR)

Impact
VitalVoice targets India's 700 million rural population who currently have no access to quality medical guidance. By supporting 10 regional languages and working on low-end Android devices, we make AI healthcare truly accessible to every Indian — regardless of language, literacy, or location.
GitHub

Android App: https://github.com/ashishkumarjaiswal999/vitalvoice-android
Backend: https://github.com/ashishkumarjaiswal999/vitalvoice-backend

**Challenges we ran into**

1. CrewAI Domain Blocking — App Answered Everything
The biggest early challenge was that our AI was answering non-medical questions like Python code, math problems, and general knowledge. Judges in our first review flagged this as "just calling APIs."
Fix: We built a 2-layer blocking system — a local keyword filter that runs before any API call, and a CrewAI Intent Filter agent that validates every query is health-related. Non-medical queries now get blocked instantly with zero API calls.

2. Gemini API Model 404 Errors
We kept getting 404 errors trying every Gemini model name — gemini-pro, gemini-1.5-flash, gemini-2.0-flash. None worked with our SDK version.
Fix: After extensive testing we found that gemini-3-flash-preview was the correct model string for our SDK version. One model name change fixed all AI calls across 11 modules.

3. Dependency Hell on Cloud Deployment
Deploying to Railway and Render failed repeatedly because our requirements.txt had loose version constraints. pip was trying hundreds of package combinations, timing out after 30+ minutes. CrewAI version conflicts with Python 3.13 made it worse.
Fix: We pinned exact package versions and added a .python-version file to force Python 3.11. For the hackathon demo we used a local backend with firewall rules configured for phone-to-PC communication over WiFi.

4.  SpeechRecognizer Crash on Android
Our voice input crashed on build because we used EXTRA_ONLY_RETURN_LANGUAGE_RESULTS — a constant that doesn't exist in the Android SDK.
Fix: Removed the non-existent constant and rewrote the SpeechRecognizer helper using only valid Android speech recognition APIs.

5. 15-20 Second AI Response — App Looked Frozen
When the CrewAI pipeline ran (Intent Filter → RAG retrieval → Medical Analyst → Response Writer), it took 15-20 seconds. Users thought the app crashed.
Fix: Built a full-screen loading overlay with a large animated spinner, "Vita is analyzing..." message, and "Running AI agents + medical knowledge base — this may take 15-20 seconds" so users understand the wait is intentional and valuable.

6. Regional Language Integration
Making AI respond in 10 Indian languages while maintaining medical accuracy was tricky. We couldn't fine-tune the model and ElevenLabs doesn't support Indian languages well on the free tier.
Fix: We appended language instructions to every CrewAI prompt — Gemini natively understands all Indian languages. For TTS we use ElevenLabs for English and Android's native TTS engine for regional languages, which actually has better Indian language support.

**Electrothon 8.0 Honors Track**

1) Best Beginner Hack

Team **Bitwise** -- [Nitin Tiwari](https://github.com/tiwari-nitin), [Ashish Jaiswal](https://github.com/ashishkumarjaiswal999)

`2026-03-15`

---

### self-learning AI agent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/selflearning-ai-agent-520d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KESHAV-CHANDEL-07/Self_learning_AI_agent) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> A self learning agent that organizes your workflow

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

This self-learning AI agent solves the problem of manual and static digital organization, where files are often scattered or mismanaged because traditional tools rely on rigid, hard-coded rules rather than user context.
It addresses the following specific pain points:

 * Static vs. Dynamic Organization: Traditional file sorters use shallow logic, such as moving all .pdf files to a single folder regardless of content. This agent uses context-aware perception to detect the specific workflow (e.g., Web Dev, App Dev, or ML) and organize files based on project-specific structures.

 * Manual Maintenance Fatigue: Users often spend significant time manually cleaning workspaces and repositories. The agent automates this via a daemon watcher that monitors the filesystem in real-time, handling organization tasks in the background without user intervention.

 * Information Decay and Code Changes: When a file's code or purpose changes, its current location may become obsolete. The agent utilizes content fingerprinting (SHA-256 hashing) and MIME-type inspection to detect internal changes and re-classify files even if their names remain the same.

 * Tool Rigidity: Most tools do not learn from their mistakes. By implementing Q-Learning, this agent adapts its behavior based on rewards and user corrections, effectively "learning" the specific organizational style preferred by the user over time.

 * Infrastructure Fragmentation: It bridges the gap between local development and remote collaboration. By supporting remote repository ingestion, the agent can clone and organize entire codebases before they are integrated into a local workflow, ensuring a consistent structure across distributed teams.

 * Reliability in Automation: It solves the issue of automation "crashes" through a robust daemon watcher with built-in error recovery and backoff logic, ensuring the organization process remains stable even when encountering system-level exceptions.

**Challenges we ran into**

1. State Space Explosion and Overfitting

 * The Challenge: Moving beyond simple file extensions to include content hashes, MIME types, and workflow anchors significantly increased the complexity of the "State Key".
 * The Impact: A state key that is too specific (e.g., including a unique file hash) prevents the agent from generalizing its learning to other files. This can lead to a Q-table that grows infinitely without ever "learning" a broad rule.
 * The Solution: We implemented a Hierarchical State Key where the agent first looks at the workflow_context and then the mime_type, treating the file hash only as a trigger for re-evaluation rather than a permanent part of the decision-making state.

2. Synchronization and Race Conditions

 * The Challenge: The DaemonWatcher uses the watchdog library to monitor file events in real-time.
 * The Impact: If a user is currently saving a large file, the agent might attempt to move it before the OS has finished writing, leading to "File in Use" or "Permission Denied" errors.
 * The Solution: We had to implement a Poll Interval and retry logic in the DaemonWatcher to ensure the agent waits for file stability before executing an action.

3. Reward Loop Fragility
 * The Challenge: Defining what constitutes a "successful" organization is subjective.
 * The Impact: If the reward function is hard-coded (e.g., only rewarding moves that match a static config), the agent stops being "intelligent" and simply becomes a complex mirror of an if/else statement.
 * The Solution: We shifted toward Dynamic Reward Shaping, where manual user overrides (moving a file back) are treated as heavy negative penalties, allowing the agent to learn the user's specific "Workflow Style" over time.

4. Dependency and Environment Management
* The Challenge: Shipping the tool as a CLI requires it to work across different operating systems (Windows, macOS, Linux) with various library requirements.
 * The Impact: Libraries like python-magic depend on external "libmagic" binaries, which can cause the tool to crash on systems where these aren't pre-installed.
 * The Solution: We standardized the environment using a requirements.txt and a setup.py entry point, and added crash-recovery logic in the DaemonWatcher to handle missing dependencies gracefully.

5. Remote Repository Ingestion Complexity
 * The Challenge: Integrating repo links required managing local clones, temporary directories, and cleanup cycles.
 * The Impact: Improper cleanup can quickly fill a user's /tmp directory with gigabytes of cloned data from different repo links.
 * The Solution: We developed the RepoManager to handle the lifecycle of remote data, ensuring that clones are isolated and deleted after the organization cycle is complete.

Team **Chaos & Order** -- [Tanishq Thakur](https://github.com/tanishqq00), [KESHAV CHANDEL](https://github.com/KESHAV-CHANDEL-07), [Sachin Thakur](https://github.com/sachinthakur4002), [Shubham kumar](https://github.com/Shubham00097)

`2026-03-15`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
