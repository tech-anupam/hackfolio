# Social Impact and Education

![Projects](https://img.shields.io/badge/Projects-51-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

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

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
