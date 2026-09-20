# Social Impact and Education

![Projects](https://img.shields.io/badge/Projects-196-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### HORCRUX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/horcrux-d677) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shreyascode11/horcrux-arena) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://horcrux-arena.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/E5T2s69Xkb0) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-57-FF6B6B?style=flat-square)

> Gamified STEM Learning • Real-Time Duels

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Framer Motion](https://img.shields.io/badge/Framer%20Motion-333333?style=flat-square)

**The problem it solves**

**The Problem it solves**

Traditional STEM education suffers from a massive engagement crisis. Students are often subjected to static, repetitive quizzes and one-size-fits-all curricula that fail to spark curiosity. The material is dry, question banks run out of fresh content, and students often feel lost regarding how their current studies connect to a future career.
**Horcrux** solves this by transforming passive study into a high-stakes, multiplayer Wizarding World adventure.

**It addresses three core problems:**

The "Static Content" Problem: unlike standard quiz platforms that rely on fixed databases, Horcrux uses Generative AI (Groq + Llama 3) to generate unique, context-aware questions instantly from any topic or uploaded PDF. This means the learning material is infinite and never repetitive.

**The "Boredom" Problem:** We replaced solitary revision with social competition. By using Socket.io for real-time 1v1 Duels and Squad Battles, we turn learning into an active, competitive sport where speed and accuracy determine the victor.

**The "Directionless" Problem:** Students often don't know what to do with their skills. Our AI Career Guidance acts as a multi-agent system that analyzes a student's grades, interests, and quiz performance to generate personalized career roadmaps, bridging the gap between today's lessons and tomorrow's jobs.

In short: We make education addictive by replacing boredom with magic.

**Challenges we ran into**

**Challenges I ran into**
Building a real-time multiplayer platform with generative AI integration as a beginner.

**Synchronizing Game State via WebSockets:** One of the hardest parts was ensuring that both players in a 1v1 duel saw the exact same question at the exact same time. Early on, we faced race conditions where one player would see the next question while the other was still on the previous one. We solved this by centralizing the game clock on the server (Node.js) and broadcasting "state snapshots" to clients rather than letting clients manage their own timers.

**Taming the AI (Prompt Engineering):** Initially, the Llama-3 model would sometimes return questions with broken JSON formatting or hallucinations, which crashed our frontend. We had to iterate extensively on our "System Prompts" to enforce strict JSON schemas and added a robust error-handling layer that cleans and validates the AI's output before sending it to the game engine.

**Persisting User Progress Without a Database:** To keep our architecture lightweight for the hackathon, we avoided setting up a heavy database like MongoDB. However, we still wanted users to track their monthly progress. We implemented a persistent local storage strategy that syncs seamlessly with the React state, allowing the "Monthly Progress" bar and battles "History" to update dynamically and survive page refreshes.

**The "Merge Conflict" Nightmare:** Collaborating on the same React components (like Dashboard.js and App.js) simultaneously led to some intense merge conflicts. We learned the hard way to communicate better before pushing changes!

These challenges ultimately pushed us to write cleaner, more modular code and gave us a deeper understanding of real-time architecture.

Team **1-A** -- [Rajdeep Shaw](https://github.com/rajdeep-pixel), [shreyas .](https://github.com/shreyascode11), [Aarush Gupta](https://github.com/aarx4real), [MANAV NAYAK](https://github.com/manavtarashnayak)

`2026-01-24`

---

### TLE Terminator: The Student Success Engine
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tle-terminator-the-student-success-engine-ec3d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prasoonpateldpsjkp2199-star/lms-by-tle-terminators) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lms-by-tle-terminator.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=DbHakW41MMk) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-26-FF6B6B?style=flat-square)

> Vision, Labs & AI: The Future of EdTech

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Redux](https://img.shields.io/badge/Redux-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**LMS by TLE Terminator bridges** the "Implementation Gap" in modern education—the disconnect between teaching content and students actually understanding it. It solves critical inefficiencies in online and resource-constrained learning environments:
1. Online teachers often feel like they are "teaching to the void" with no visibility into student engagement. Our Attention Engine acts as a **digital invigilator, providing real-time feedback on student focus** (gaze/head pose), enabling teachers to pivot instantly when the class zones out.

2.  Millions of students in underfunded or rural schools learn science **theoretically because they lack physical laboratories.** Our Virtual STEM Ecosystem brings Physics, Chemistry, and CS labs directly into the browser, allowing students to experiment safely and practically without expensive infrastructure.

**3.Eliminates "Revision Burnout" & Repetitive Doubts** Students waste hours re-watching lectures for notes, and teachers answer the same doubts repeatedly. Our AI Layer solves this by:

- Auto-Summarizing
 Lectures: Generating instant, structured revision notes from audio.
- Context-Aware
 Tutoring: Handling routine doubts instantly (chatbot support)

**4.Provides "360° Student Guidance"**
Most platforms stop at academic content. We solve the "Directionless Student" problem by integrating Personalized Career Guidance, ensuring students don't just learn what to study, but understand why it matters for their future.

**Challenges we ran into**

## Challenges We ran into:
----

### 🔴 Problem
- Initial **WebRTC peer-to-peer (mesh) setup** only supported 1-to-1 communication and did not scale.
- High **bandwidth and CPU usage** with multiple participants.
- Complex signaling logic and frequent **sync & connection drops**.
- **tldraw whiteboard** updates were not syncing correctly, causing latency and inconsistent board states.
- During deploying to production, faced issues with license limits for tldraw.

### 🛠 Solution
- Migrated to **Stream.io SFU architecture** for scalable multi-user video streaming.
- Optimized whiteboard sync using **incremental event updates, batching, and throttling**.
- Reduced latency and ensured **real-time board consistency** across users.
- Made temporary license arrangements for tldraw ,planning to build a custom whiteboard or move to open source solution in the future.

---

## 2. PDF Upload & Lecture Notes System

### 🔴 Problem
- Broken download links, duplicate file overwrites, and inability to **directly download PDFs from Cloudinary**.

### 🛠 Solution
- Implemented **Multer-based upload pipeline** with validation.
- Used **timestamp + UUID naming** for uniqueness.
- Uploaded PDFs in **Cloudinary raw format** for direct downloads.

---

## 3. Video → Audio Differentiation (Cloudinary Streams)

### 🔴 Problem
- Incorrect audio extraction, multi-channel mismatches, transformation failures, and **high streaming latency**.

### 🛠 Solution
- Used **explicit Cloudinary audio transformations** with fixed codecs and sampling rates.
- Added **format validation, retry logic, and optimized delivery endpoints**.
- Built a stable pipeline for **AI transcription & summarization**.

---

## 4. AI-Based Lecture Summarizer

### 🔴 Problem
- Converting **long lecture videos into accurate transcripts**.
- Handling **large audio files** without blocking the main application.
- Preventing system slowdowns during peak uploads.

### 🛠 Solution
- Implemented **OpenAI Whisper** for high-accuracy speech-to-text transcription.
- Designed an **asynchronous queue-based processing pipeline** to handle heavy transcription jobs without blocking the server.
- Used **pooling and rate-limiting** to manage concurrent requests and maintain system responsiveness.

---

## 5. Attention Engine

### 🔴 Problem
- **Model Accuracy vs Speed Trade-off**:
High-accuracy models reduced speed, while lightweight models reduced reliability. Finding the right balance for hackathon constraints was tough.

- **Inconsistent Lighting Conditions**
: Different lighting environments (low light, backlight, shadows) affected face detection accuracy, leading to false attention drops.
- **Real-Time Webcam Performance**:
Processing live webcam frames caused lag and high CPU usage, especially on low-end devices. Optimizing frame rate without losing accuracy was challenging.

### 🛠 Solution
- **Reduced frame rate** (processed every nth frame) and **resized frames** before processing and moved heavy computation to backend and used lightweight CV pipelines
- Used **lightweight pretrained models** optimized for real-time inference and applied **threshold-based attention** scoring instead of complex deep models
- Balanced accuracy by combining **multiple simple signals** (face presence + head pose)

---

**Duality AI — Offroad Semantic Scene Segmentation**

LMS by TLE Terminator fits this criteria through our proprietary "Attention Engine." We utilize advanced Computer Vision techniques (OpenCV & MediaPipe) and Deep Learning models to process live video feeds in real-time. Our system performs complex face detection, gaze estimation, and head-pose analysis to quantify student focus. This demonstrates a practical, high-impact application of visual data processing and ML inference, directly aligning with the track's focus on advanced AI/ML solutions.

![image](https://assets.devfolio.co/content/3bbbf1a777704493ae70048e634d83ff/21699144-9ddc-4f51-8d69-3b3bfee9f9b6.png) 

![image](https://assets.devfolio.co/content/3bbbf1a777704493ae70048e634d83ff/31c19d0d-5ecc-4031-a342-45524ec8a21c.png)

![image](https://assets.devfolio.co/content/3bbbf1a777704493ae70048e634d83ff/a860ff50-301e-4097-9ef5-34655e45d77b.png)

Team **TLE TERMINATORS** -- [Abhas Nath](https://github.com/abhas20), [Abhinav Neema](https://github.com/AbhinavNeema), [Prasoon Patel](https://github.com/Prasoon52), [Pranav Panmand](https://github.com/pranavpanmand)

`2026-01-25`

---

### Node-It-All
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nodeitall-d2a5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kavishbasole17/hackSRM) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hack-srm-one.vercel.app/login) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BXEsUhr4m9k) [![Built at](https://img.shields.io/badge/Built%20at-HackSRM%207.0-0052CC?style=flat-square)](https://hack-srm26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-14-FF6B6B?style=flat-square)

> Your personalised learning roadmap engine

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Have you ever wanted to learn something new but didn’t know where to start? You open YouTube, Google a few things, save some links… and suddenly you’re overwhelmed. That’s exactly the problem Node-It-All was built to solve.

Node-It-All is like a smart friend who takes a big, confusing goal and breaks it down into small, clear steps. Instead of throwing random information at you, it organizes everything into simple “nodes”. small chunks of knowledge that connect logically to each other. So if you want to build an app, learn a new skill, or prepare for a hackathon, it shows you what to learn first, what comes next, and how everything fits together.

Think of it as Google Maps. but for learning.
You enter your destination, and Node-It-All creates the route.

It doesn’t just list topics. It structures your journey in a way that feels achievable. You don’t feel lost. You don’t feel stuck. You just keep moving forward, one clear step at a time.

Our goal was simple: make learning feel less chaotic and more connected. Because when knowledge is organized properly, confidence naturally follows.

**Challenges we ran into**

One big challenge was making something powerful feel simple. Behind the scenes, there’s complex logic organizing everything — but for users, it had to feel effortless.

Another challenge was time. Building, testing, and refining the experience within a hackathon deadline pushed us to think fast and work smart.

Most importantly, we had to constantly ask ourselves:
“Is this actually helping someone feel less confused?”

And that question guided every decision we made.

**Grand Prize**

Node-It-All is a standout contender for the grand prize because it tackles a universal pain point cognitive overload with a sophisticated yet intuitive solution. While many tools simply aggregate data, Node-It-All innovates by applying a "GPS for Learning" logic that transforms chaotic information into structured, actionable pathways.

The project demonstrates high technical execution by managing complex backend dependencies while maintaining a seamless, user-centric interface. By focusing on the psychological aspect of learning building confidence through logical progression it transcends being just an app and becomes a scalable educational framework. Its ability to turn daunting goals into clear "nodes" showcases both creative vision and practical utility, making it a high-impact tool ready for real-world application.

Team **Team K Means Nothing** -- Kavish Basole, Nishik Kalidindi, Sai Darahaas Reddy Yerasi, Navya Nair

`2026-02-26`

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

### Bhoj Ki Khoj (Food App)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bhojkikhoj-5fd1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/immortalfoodie/TeamJugaadu-Bhoj-ki-Khoj-AWSTrack) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://medium.com/@foodieme1000/bhoj-ki-khoj-keeping-the-50-lunch-at-50-3e90015d9bf5) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/qTrIWtp7uxU) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Home-Cooked Food, Powered by Community.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Mapbox API](https://img.shields.io/badge/Mapbox%20API-333333?style=flat-square) ![HTML/CSS](https://img.shields.io/badge/HTML/CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

## ❗ The Problem It Solves

* 🍛 **Inflated Food Prices**
  A ₹50–₹60 home-cooked meal often becomes ₹140–₹160 on major food delivery platforms due to high commissions, delivery fees, and taxes.

* 🏠 **Limited Digital Reach for Local Kitchens**
  Local tiffin services and small bhojnalayas struggle to go digital because existing platforms are expensive and margin-heavy.

* 🚫 **Unhealthy Default Choices**
  With affordable home food being hard to access, people often rely on fast food or highly processed meals.

* 📉 **Unsustainable Model for Small Vendors**
  High platform fees make it difficult for home kitchens to earn fairly, discouraging them from scaling.

---

✨ **Bhoj Ki Khoj addresses these challenges by enabling direct discovery of local, affordable, home-cooked meals, keeping prices fair for both users and vendors.**

**Challenges we ran into**

## 🚧 Challenges I Ran Into

* ⏳ **Time Constraints**
  Building a meaningful solution within a hackathon timeline meant prioritizing only the most impactful features.

* 🎯 **Scope Management**
  There were many ideas, but not all could be implemented. The challenge was deciding *what not to build* and staying focused on the core problem.

* 💰 **Designing for Affordability**
  Most food-tech solutions assume high margins. Creating a system that works with **low-cost meals** required rethinking pricing, delivery, and vendor onboarding.

* 🧠 **Structuring the Idea Quickly**
  Turning a real-world problem into a structured product flow (users, vendors, delivery) in limited time was challenging.

* ⚖️ **Avoiding Overengineering**
  The goal was to keep the solution scalable yet simple enough to realistically work for small local vendors.

**Best Innovation**

# 🏆 Why Bhoj Ki Khoj Deserves Best Innovation

## 🍱 Project Overview

**Bhoj Ki Khoj** is a local food discovery and ordering platform built to keep affordable meals affordable. The app connects users directly with **local tiffin services, home kitchens, and small bhojnalayas** that serve fresh, home-cooked food at prices below ₹100.

Unlike traditional food delivery platforms where a ₹50 meal turns into ₹150 due to high commissions and delivery fees, Bhoj Ki Khoj focuses on **fair pricing and local reach**. Menus are updated daily based on what vendors actually cook, and deliveries are optimized through **collaborations with dabbawalas**, ensuring low cost and high reliability.

The goal of Bhoj Ki Khoj is to provide a **healthy, home-made alternative to fast food**, support local food providers, and make good food accessible to people living away from home without unnecessary markups.

---

## 🌟 Solving a Real and Overlooked Problem

Affordable home-cooked meals are widely available, yet difficult to access digitally without inflated prices. Existing platforms prioritize high commissions, making them unsuitable for small vendors and home kitchens.

Bhoj Ki Khoj bridges this gap by enabling direct discovery and fair access for both customers and food providers.

---

## 💡 Innovation Through Simplicity

The innovation of Bhoj Ki Khoj lies in its clear and focused approach.

- Prioritizes affordability over convenience-first pricing
- Highlights nearby local food providers
- Enables daily menu updates based on actual cooking capacity
- Reduces digital barriers for small vendors

Instead of adding complexity, Bhoj Ki Khoj simplifies food discovery.

---

## 🔗 Leveraging Existing Local Systems

By building around dabbawala-style delivery networks, the platform leverages a proven and efficient system rather than reinventing logistics. This keeps costs low while maintaining reliability and scalability.

---

## 🧠 Purpose Driven Use of Technology

Technology is used to structure and support the solution, not overcomplicate it.

- Planned and structured using Kiro IDE
- Modular and scalable by design
- Focused strictly on solving the core problem

This thoughtful use of technology strengthens the project’s real-world feasibility.

---

## 🎯 Strong Social Impact

Bhoj Ki Khoj creates impact across multiple dimensions.

- Affordable and healthy meals for students and working professionals
- Sustainable income opportunities for home kitchens
- Support for local food ecosystems
- Promotion of healthier eating habits

---

## 🏁 Conclusion

Bhoj Ki Khoj represents innovation that is practical, inclusive, and impactful. By solving a real problem with simplicity, fairness, and local focus, it challenges the current food delivery model and offers a better alternative.

This balance of social value, thoughtful design, and real-world applicability makes Bhoj Ki Khoj a strong contender for **Best Innovation**.

**AWS**

## ☁️ AWS Track Fit Focus on Kiro IDE

**Bhoj Ki Khoj** fits perfectly into the AWS Track through its use of **Kiro IDE** as the core development and planning tool.

Instead of jumping straight into coding, Kiro IDE was used to:
- 🧠 Break a real-world problem into clear and structured features
- 👥 Define user roles such as customers, vendors, delivery partners, and admin
- 🔄 Plan end-to-end workflows like menu updates, ordering, and delivery
- 🎯 Stay focused on the core goal of affordability and local reach

Kiro IDE helped convert scattered ideas into a well-organized product flow, enabling faster decision-making during the hackathon. Its context-aware guidance made it easier to avoid overengineering while still keeping the project scalable and realistic.

By using Kiro IDE throughout the lifecycle of Bhoj Ki Khoj, we were able to design and build a solution that solves a real problem efficiently, making it a strong fit for the AWS Track.

Team **Team Jugaadu** -- [Deepkumar Das](https://github.com/deepdas2607), [Pranav Shirke](https://github.com/PranavShirke), [Vishal Gowda](https://github.com/VishalGowda23), [Gideon Mire](https://github.com/GideonMire), [Yash Naik](https://github.com/Immortalfoodie)

`2025-12-30`

---

### BlindUnfold
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/blindunfold-b0ea) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajeet-04/BlindUnfold) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://piik.me/xthxr/hackxios-yt) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3ciUBsc0flI) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> A Realtime Vision for Visually Impaired Students

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Tesseract OCR](https://img.shields.io/badge/Tesseract%20OCR-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

For the 2.2 billion people globally with vision impairment, interacting with physical information remains a daily challenge. Screen readers solve digital accessibility, but physical accessibility is often left behind.

Common struggles include:
1.  **Sorting Mail & Documents:** Distinguishing between a utility bill and junk mail without asking for sighted help.
2.  **Navigating New Spaces:** Understanding the layout of a room or spotting obstacles at eye level.
3.  **Deciphering Handwriting:** Most OCR tools fail on handwritten notes (like birthday cards or post-its).
4.  **Locating Text:** Knowing *where* to point the camera to get a clear shot of a document.

## How BlindUnfold Helps

BlindUnfold transforms a smartphone into an intelligent audio describer. It prioritizes **latency, battery safety, and accessibility standards** over flashy UI, ensuring it is a reliable tool for daily independence.

### Key Capabilities

#### 1. Instant Text-to-Speech (OCR)
The app creates a "hold-to-scan" experience. Users simply point their phone and hold their finger on the screen. The app detects text in **English, Hindi, Urdu, or Bengali** and reads it aloud instantly. It uses intelligent filtering to ignore gibberish and only speak meaningful sentences.

#### 2. Audio Guidance Mode ("The Geiger Counter")
Finding text on a blank page is difficult if you cannot see it.
*   **The Solution:** The app emits a rhythmic clicking sound (Audio Guidance).
*   **How it works:** The clicking gets faster and higher-pitched as the camera detects denser text. It remains silent on blank walls. This allows users to center their camera on a document purely through sound.

#### 3. AI Scene Description
Users can ask "What am I looking at?"
*   Using **Gemini 3 Pro**, the app analyzes the camera feed and provides a detailed, safety-focused description of the environment (e.g., "A kitchen counter with a sharp knife near the edge and a spilled cup of coffee").

#### 4. Handwriting Recognition
Standard OCR struggles with cursive. BlindUnfold includes a specific mode to decipher handwritten notes, allowing users to read personal letters, doctor's notes, or whiteboard scribbles.

#### 5. Voice Control
To assist users with limited motor control or those who prefer hands-free operation, the entire app can be controlled via voice:
*   *"Read"* / *"Stop"*
*   *"Describe Scene"*
*   *"Faster"* / *"Slower"* (Adjusts speech rate)
##  Real-World Use Cases

| Scenario | How BlindUnfold Makes it Easier |
| :--- | :--- |
| **Grocery Shopping** | Quickly scan product labels to identify cans or boxes without picking every single one up. |
| **Sorting Mail** | Rapidly scan envelopes to separate bills from advertisements. |
| **Classrooms** | Students can snap a photo of a whiteboard or handout and hear the content immediately. |
| **Travel** | Read street signs, menu boards, or safety notices in multiple languages. |
| **Social** | Read handwritten holiday cards or letters from family members independently. |

##  Accessibility-First Design

*   **High Contrast UI:** Uses a Yellow (#FACC15) on Black theme, the standard for maximum visibility for low-vision users.
*   **Massive Touch Targets:** The UI is split into huge interaction zones that are impossible to miss.
*   **Haptic Feedback:** The phone vibrates to confirm actions (scanning started, text found, error), providing non-visual confirmation.
*   **Silence Threshold:** The audio guidance system is intelligent enough to stay silent when looking at blank surfaces, preventing sensory overload.

---

## Technical Stack

*   **Frontend:** React 19, TypeScript, Tailwind CSS
*   **AI/LLM:** Google Gemini 3 Pro & Flash Lite (via `@google/genai`)
*   **OCR:** Tesseract.js (WASM based)
*   **Audio:** Native Web Audio API (Oscillators for guidance) & Web Speech API (Voice commands)
*   **Platform:** PWA (Works offline, installable on Android/iOS)

**Challenges we ran into**

# BlindUnfold – Challenges & Solutions

Building **BlindUnfold** meant balancing real time OCR, camera and audio access, and strict accessibility needs.

## Key Challenges & How They Were Solved

### 1. OCR Jitter & Performance
Running OCR on every frame froze the UI and drained battery.  
Solution: Motion detection on a downscaled video grid triggers OCR only when the phone is steady, creating a natural point, pause, read flow.

### 2. Audio Overload
Continuous sound feedback caused sensory fatigue.  
Solution: A silence threshold plus non linear audio intervals that scale with text density, quiet when empty, informative when text appears.

### 3. Garbage Text vs Multi Language Support
Strict English filters broke Hindi, Urdu, and Bengali support.  
Solution: Dual

**Best Innovation**

# BlindUnfold – Why This Is a Top-Tier Innovation

BlindUnfold is not just a text reader. It is a **sensory-augmented accessibility system** designed to remove the real friction points faced by blind users.

## 1. Hybrid Edge–Cloud Intelligence
VisionAssist uses a tiered AI model. Printed text is processed locally with Tesseract.js (WASM) for instant, offline results, while complex tasks like handwriting and scene understanding are routed to Gemini 3 Pro in the cloud. This balances speed and intelligence instead of sacrificing one for the other.

## 2. Sensory Substitution Through Audio
Text density is converted into spatial audio cues using a non-linear “Geiger Counter” model. Silence when no text exists and accelerated clicks when text appears guide the user’s hand before reading begins. This turns vision into sound rather than guessing where text might be.

## 3. Battery-Aware Computer Vision
A custom motion detection engine gates OCR execution. Heavy processing only runs when the phone is stable below a 5 percent motion threshold, preventing blurry hallucinations and enabling all-day usability on mobile devices.

## 4. Intelligent Speech Control
Fuzzy string matching using Levenshtein distance suppresses repeated or near-identical speech output. The system speaks only when meaningful new information appears, producing calm, human-like feedback instead of noise.

## 5. Accessibility-First Interaction Design
The interface removes traditional visual UI in favor of interaction zones, high-contrast yellow-on-black visuals, and haptic confirmation. The app is fully operable without sight or screen attention.

## 6. Zero-Friction Distribution
Built as a high-performance PWA, BlindUnfold installs instantly from a link, runs on low-cost phones, updates automatically, and avoids app store barriers. It proves modern web technologies are powerful enough for real-time assistive vision.

Team **HOLA AMIGO** -- [Ankit Singh](https://github.com/Iankitsinghak), [ATHAR AKRAM](https://github.com/xthxr), [Rajeet Ash](https://github.com/rajeet-04)

`2025-12-30`

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

### Hope Foundation
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hope-foundation-5857) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lavaygarg/OOC-Project-2.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ooc-project-2-2.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uKp-U0NoRrM?si=ucaiK3jPvd2L11kl) [![Built at](https://img.shields.io/badge/Built%20at-Out%20Of%20Context'26-0052CC?style=flat-square)](https://out-of-context-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Empowering underprivileged children with education

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Traditional NGOs often struggle with manual record-keeping, lack of transparency in fund utilization, and inefficient volunteer coordination. Our website solves these problems by providing:

A secure, transparent donation system with instant receipts.
Streamlined volunteer management and event participation.
Real-time impact tracking and reporting.
Bilingual accessibility and modern user experience.
This ensures that resources reach those in need efficiently, builds donor trust, and enables NGOs to maximize their positive impact.

**Challenges we ran into**

Integrating Payment Gateways: Setting up and testing secure online donations (e.g., Razorpay) and handling payment callbacks reliably.
Ensuring Data Security: Implementing authentication, authorization, and protecting sensitive donor/volunteer data.
Database Design: Structuring MongoDB schemas for donations, events, volunteers, and ensuring data consistency.
Real-Time Updates: Displaying live donation stats and event updates without page reloads.
Bilingual Support: Managing seamless language switching (English/Hindi) across all UI and content.
Responsive UI: Making sure the site works well on all devices and screen sizes.
Deployment: Deploying both backend and frontend, configuring environment variables, and handling CORS issues.
Team Collaboration: Coordinating tasks, merging code, and resolving merge conflicts during the hackathon timeframe

Team **Pathway** -- Jatin J, Bhaskar Sarate, Lavay Garg, Riya Ghoshi

`2026-01-25`

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

### Polygo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/polygo-f3a2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/decodewithdeepak/polygo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://polygo-acehack.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Every Language , One Conversation !

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Auth0](https://img.shields.io/badge/Auth0-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square) ![Convex](https://img.shields.io/badge/Convex-333333?style=flat-square) ![sarvam ai](https://img.shields.io/badge/sarvam%20ai-333333?style=flat-square)

**The problem it solves**

Real-time group communication breaks down the moment people speak different languages. Teams, communities, and families are forced to manually translate messages using external tools — losing tone, idioms, and cultural context in the process. In fast-moving group chats, this friction makes collaboration nearly impossible.

Polygo solves this by acting as an invisible translation layer inside the chat itself:

- A single message in Spanish is instantly delivered as Hindi to one member, Japanese to another, and Bengali to a third — all in parallel, with no extra steps from the sender.
- Indic language pairs are handled by Sarvam AI for speed and colloquial accuracy across 22 Indian languages; global pairs are routed to Google Gemini for high-fidelity translation.
- Cultural nuances, honorifics, and idioms are preserved and explained - users see a short AI insight alongside each translated message so they learn as they chat.
- Sentiment-aware text-to-speech lets users listen to messages in their language with the correct emotional pacing, so the feeling behind a message is never lost.

**Who benefits:**

- **Remote teams** across countries can hold fluid discussions without a shared language.
- **Open source communities** can onboard contributors from any region without communication friction.
- **Students and educators** in multilingual classrooms can collaborate and learn simultaneously.
- **Families and friend groups** separated by borders can stay connected in their own languages.

**Challenges we ran into**

Building Polygo surfaced several hard technical problems that were not obvious at the start.

**Bridging Auth0 with Convex**

Auth0 and Convex both have their own identity systems. Getting Auth0 JWTs validated inside Convex required a custom auth adapter with exact token claim mapping — any mismatch silently rejected all authenticated requests.

**Parallel multicast translation**

A single message can need 8-10 simultaneous translations for a large group. The challenge was firing all jobs in parallel inside a single Convex mutation so a failure in one language does not block the rest.

**Dual-routing between Sarvam and Gemini**

- Sarvam is faster for Indic pairs but fails silently on unsupported languages.
- Gemini handles everything but is slower and more expensive.
- Mixed-script messages like Hinglish often confused the language detector.

We built a fallback layer where Sarvam failures automatically re-route to Gemini without the user noticing.

**Best Use of Gemini API**

Gemini is the backbone of Polygo's translation and intelligence layer. Here is how we use it:

**1. Six-Model Cascade for Zero-Downtime Translation**
We do not just call one Gemini model. We built a smart fallback chain — Gemini 3.1 Flash Lite Preview, 3.1 Flash Preview, 2.5 Flash Lite, 2.5 Flash, 2.0 Flash Lite, and 2.0 Flash. If one model hits a quota limit (429), we instantly try the next one. The user never sees a failure. Translation just works, every single time.

**2. Hybrid Routing with Sarvam AI**
For Indian language pairs (Hindi to Tamil, Bengali to Gujarati, etc.), we route through Sarvam AI for speed. But for any foreign language — Japanese, Chinese, French, Korean — Gemini handles the translation. This gives us the best of both worlds: Sarvam's speed for Indic pairs, Gemini's reliability for everything else.

**3. Cultural Nuance and Learning Tips**
Beyond translation, we use Gemini to generate short language learning tips that explain grammar, cultural context, or idiomatic meaning behind a message. For example, if someone sends "Jai Hind", the tip explains the historical weight behind the greeting — not just the literal words.

**4. Low-Latency Prompt Design**
Every Gemini call uses a tight prompt with `maxOutputTokens: 200` and `temperature: 0.1` to get fast, deterministic, translation-only responses. No reasoning tags, no explanations — just the translated text. This keeps response times low enough for real-time chat.

Gemini is not a bolt-on feature for us. It is the engine that makes multilingual communication actually feel natural.

**Best Use of Auth0**

Polygo uses **Auth0** for secure, enterprise-grade authentication. We implemented role-based mutation guards in Convex to ensure that only authorized participants can read or send messages in a conversation.

**1. One-Click Google Login**
Users sign in with Google via Auth0. No passwords, no signup forms. The Auth0 Next.js SDK handles the full OAuth flow — login, callback, logout, session management — out of the box.

**2. Custom Token Bridge for Convex**
Convex (our real-time backend) does not natively support Auth0. So we built a custom bridge endpoint (`/api/convex/v1/token`) that extracts the Auth0 ID Token from the server-side session and passes it to the Convex client. Every Convex query and mutation verifies this JWT before executing. No token, no access.

**3. Server-Side Session Security**
We use the Auth0 Next.js SDK v4 with server-side sessions — the token never touches the browser's local storage. The session is managed entirely on the server using `auth0.getSession()`, and the ID token is only exposed through our secure bridge endpoint.

**4. Identity-Linked User Profiles**
On first login, we sync the Auth0 profile (name, email, picture) into our Convex users table using the Auth0 `sub` claim as the external ID. This links every message, reaction, and conversation back to a verified identity. No anonymous users, no spoofing.

**5. Role-Aware Backend**
Every Convex mutation checks that the authenticated user is actually a participant of the conversation they are trying to access. Auth0 provides the verified identity, and our backend enforces the access rules on top of it.

Auth0 gives us production-grade authentication without us having to build or maintain any of it ourselves.

**Best Hack Built with Google Antigravity**

This project was developed entirely within the **Google Antigravity** environment. Antigravity served as a pair-programmer, handling:

- **Complex Architecture Design**: Mapping out the Convex-Sarvam-Google hybrid routing.
- **Natural Language Refactoring**: Generating utility hooks and complex UI components through speech and text commands.
- **Context-Aware Debugging**: Instantly identifying and fixing race conditions in the Convex live-subscription logic.
- **Rapid Documentation**: Generating this comprehensive README and product documentation based on the full codebase context.

Team **The Meowsters** -- [Abhinesh Jha](https://github.com/Abhineshhh), [Deepak Modi](https://github.com/decodewithdeepak), [Sumit Jha](https://github.com/SumitWiki)

`2026-03-08`

---

### CampusPitch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campuspitch-001f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Neha-Vaghela/Campus-Pitch) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> From student ideas to funded projects

![PHP](https://img.shields.io/badge/PHP-333333?style=flat-square) ![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square) ![phpMyAdmin](https://img.shields.io/badge/phpMyAdmin-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Students often struggle to turn ideas into reality due to:

No structured platform for idea pitching

Limited access to early feedback

Lack of seed funding opportunities

Weak student–alumni collaboration


Campus Pitch addresses these challenges by offering a centralized, transparent, and student-focused solution.
Solution

Campus Pitch enables:

Structured idea submission and discovery

Peer and alumni feedback through comments and votes

Micro-funding to support promising ideas

Admin moderation to ensure quality and relevance

**Challenges we ran into**

One of the major challenges during the development of Campus Pitch was designing a secure and reliable role-based access system using PHP and MySQL. Since the platform has different user roles (Student, Alumni/Investor, and Admin), ensuring that each role could only access its intended features was initially tricky.
This caused issues such as unauthorized access to admin pages and inconsistent session handling.
How I overcame it:
I implemented proper session management in PHP and added role checks at both the backend and database levels. Admin routes were protected using middleware-like checks, and sensitive actions (such as approving or rejecting pitches) were restricted strictly to authorized users. This improved security and stabilized user flows across the platform.
Another challenge was handling real-time pitch engagement features like votes, comments, and funding updates. Initially, duplicate votes and inconsistent funding values appeared due to missing validation and race conditions in database queries.
How I overcame it:
I solved this by enforcing unique constraints in the MySQL database, validating actions on the backend, and using transactional queries to ensure data consistency. This made interactions more reliable and prevented data duplication.
Finally, data organization and scalability became challenging as the number of pitches increased. Queries for trending and top-funded pitches started to slow down.
How I overcame it:
I optimized SQL queries, added proper indexing, and separated logic for leaderboard calculations. This significantly improved performance and prepared the platform for future growth.
These challenges helped me gain hands-on experience in backend validation, database optimization, and secure role management, making the overall system more robust and production-ready.

Team **KNEXUS** -- [Urvashi Sanpara](https://github.com/urvashisanpara), [Krishna Vala](https://github.com/krishnavala2602), [Riddhi Vadhaiya](https://github.com/Abc), [Neha Vaghela](https://github.com/Neha-Vaghela)

`2026-01-25`

---

### Student Placement Readiness
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/student-placement-readiness-e8be) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rudraprajapati2005/student-placement-readiness) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=lGVZbpUYBVc) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Empowering students to assess themself

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square)

**The problem it solves**

Student Placement Readiness is essentially about the gap students face when preparing for campus placements. The idea is to empower students to assess and enhance their readiness for recruitment by identifying skill gaps, providing actionable insights, and making the preparation process more structured and transparent .

**Challenges we ran into**

The dataset we obtained may not reflect the actual criteria of the placement nowadays also many aspects other than multiple datasets we used are still has not been used in the ML .

Other error we faced was getting huge bunches of error in the backend as we used the spring boot . The problem was solved as soon as the pom.xml was analyzed  and necessary version changes were applied in each dependencies.

Team **DIGITAL DYNAMITE** -- [Jaimin Raval](https://github.com/Jaiminjraval), [RUDRA PRAJAPATI](https://github.com/rudraprajapati2005), [Meet Prajapati](https://github.com/meetprajap), [Tarang Patel](https://github.com/TarangPatel19273)

`2026-01-25`

---

### Apni Disha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/apni-disha-d129) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pranay-code24/ApniDisha) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20This%20Fall%202025%20--%20Milestone%20Edition-0052CC?style=flat-square)](https://hackthisfall.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Personalized Career and Education Advisor

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

AI-driven aptitude & interest quiz, gamified assessment, and career path simulator provide tailored career recommendations. Dynamic roadmap builder + college/course matching engine prioritizing government institutions and relevant skill pathways. Scholarship guidance module integrated in the platform with alerts for eligibility and deadlines. Regional language support (English + Hindi + other vernaculars planned) and offline mode for low-connectivity areas. Parent dashboard & family engagement features (progress reports, comparative insights) ensure inclusivity. Proposed API/data integration with NCS, UDISE, and state-level admission portals for real-time updates. Automated feeds for admissions, placement opportunities, and alumni success cases embedded into the system. Offline-first microservices + edge caching — scalable, low-cost delivery to Tier-2/3 areas; target: 10–20% govt-college enrolment uplift.

[Pranay Gumashta](https://github.com/pranay_code24)

`2025-11-11`

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

### EqualEd
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/equaled-dcf8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wheresachin/equaled-ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.equaled.online) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Equal Learning. Equal Opportunity.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Google Text to Speech](https://img.shields.io/badge/Google%20Text%20to%20Speech-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Speech API](https://img.shields.io/badge/Speech%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

1. Many students with disabilities face difficulties using traditional digital learning platforms. Most websites are designed for standard users and do not support accessibility features needed by visually impaired, hearing impaired, or motor-impaired students.
 
2. EqualEd solves this problem by providing an AI-powered inclusive learning platform that adapts to different abilities. Students can use voice commands, text-to-speech, speech-to-text, captions, eye tracking, and adjustable interfaces to interact with learning content.

3. This makes digital education more accessible and allows students to learn independently without barriers. EqualEd helps create equal learning opportunities for everyone, regardless of physical or cognitive limitations.

**Challenges we ran into**

1. Implementing voice command functionality was challenging because speech recognition sometimes misunderstood commands due to noise or pronunciation. We solved this by improving command detection logic and adding clear feedback for unrecognized commands.

2. Integrating multiple accessibility features like text-to-speech, speech-to-text, and eye tracking while keeping the interface smooth required modular design. We structured the system so each feature could be enabled or disabled independently.

3. We also faced deployment and API configuration issues while connecting the frontend and backend. These were resolved by correctly setting environment variables and testing API communication.

Team **AURA** -- [Aditya kumar Singh](https://github.com/Rajputaditya), [SACHIN KUMAR](https://github.com/wheresachin), [Nisha Kumari](https://github.com/nishapandey8009-max)

`2026-03-08`

---

### Campus Connect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-connect-84e4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saurabhpal2363/Campus-Connect) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Connecting like minded students across campuses.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

Problem -->

Many students struggle to:

1.Find teammates for hackathons
2.Connect with students having similar skills
3.Discover project collaborators
4.Build a productive peer network
5.Most colleges rely on WhatsApp groups or random connections, which are inefficient.

CampusConnect solves this by creating a dedicated platform for campus collaboration.

Solution -->

CampusConnect allows students to:

1.Create a profile with skills and interests
2.Post project ideas or skill requirements
3.Discover students with relevant skills
4.Connect and collaborate on projects
5.Share posts and project opportunities
6.The platform builds a skill-based collaboration network inside the campus.

**Challenges we ran into**

1.Handling backend integration with Firebase, including authentication and database structure.

2.Managing user data, posts, and real-time updates between frontend and backend.

3.Designing a clean and intuitive UI/UX so students can easily navigate and use the platform.

Team **Let's Solve** -- Saurabh Babu, Saurabh Kumar, Ansh Saini, Saurav Kumar

`2026-03-08`

---

### EduVoice
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eduvoice-9152) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ankit2061/Eduvision) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Inclusive Education for everyone

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Voiceflow](https://img.shields.io/badge/Voiceflow-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Every classroom in India has students with varied learning abilities — from visual learners and auditory learners to students with blindness, deafness, autism, dyslexia, stammering, ADHD, and physical disabilities. Yet all content is prepared in one format, designed for one kind of student.

Teachers who want to create inclusive content for all their students spend an additional 8–10 hours per week manually converting lessons. Given their already packed schedules, this is simply not sustainable. The result: students with disabilities are left behind, not because teachers don't care, but because the system doesn't help.

EduVoice solves this by being the invisible bridge between any content a teacher creates and any format a student needs. The teacher creates once. The platform delivers to everyone.

**Challenges we ran into**

-CORS Error Fixation
-UI/UX Fixes
-Various Other minor bugs here and there

**Gemini API**

Gemini is the brain of EduVoice.
Every piece of intelligence in the app runs through Gemini:

Converts a teacher's lesson into simplified, grade-level, and advanced versions
Reformats content for each disability — literal language for autism, chunked for ADHD, simplified for dyslexia
Transcribes and analyses student speech, scoring grammar and pronunciation
Evaluates test answers equitably based on the student's disability profile
Interprets voice commands from specially abled teachers
Generates adaptive test questions per disability type
Summarises live class content every 2 minutes for ADHD students

**Snowflake API**

Snowflake is the central data layer of EduVoice — it stores everything the platform needs to personalise content for every student.
When a student is onboarded, their disability profile and accessibility preferences are stored as JSON in Snowflake's VARIANT column. When a teacher publishes a lesson, all the generated variants — the autism version, the dyslexia version, the blind version — are stored in the same lesson row as a single VARIANT column, so one query fetches everything.
Every time a student practices or takes a test, their scores, transcripts, and the accessibility settings they had active during that session are written to Snowflake. This is the key part — we store which accessibility tool was on alongside what score the student got.
This lets us run a single SQL query that JOINs structured scores with nested JSON accessibility state to produce the teacher's analytics dashboard — showing things like "students who had dyslexia font enabled scored 12 points higher on grammar than those who didn't." That kind of insight is only possible because Snowflake's VARIANT type lets you query inside JSON the same way you query a regular column.
In short — Snowflake is not just our database. It is what makes our personalization engine and impact analytics both possible in the same system. Sonnet 4.6

**ElevenLabs**

ElevenLabs is the voice of EduVoice — it is the reason blind students and dyslexic students get a learning experience that actually works, rather than a robotic text-to-speech fallback.
Every time a teacher publishes a lesson, ElevenLabs narrates each difficulty tier — Foundation, Grade-Level, and Advanced — at a natural, human-quality voice. The audio is generated once at publish time and cached in DigitalOcean Spaces, so every student who needs it streams the same file instantly without calling the API again.
For dyslexic students, ElevenLabs powers the synchronised read-aloud — the text highlights word by word as the audio plays, so the student is never lost between what they see and what they hear.
For blind students, ElevenLabs narrates not just the lesson text but also the AI-generated audio descriptions of any visual elements — diagrams, images, or anything a sighted student would see on screen.
For non-verbal students, ElevenLabs is their classroom voice. When a student taps a phrase on the AAC grid, ElevenLabs speaks it aloud in the room in real time — allowing a student who cannot speak to say "I have a question" in class like everyone else.
After a practice session, ElevenLabs delivers the spoken feedback — warm, encouraging, never mentioning the student's disability — so even the feedback loop is accessible to students who learn better by hearing than reading.
In short — ElevenLabs is what separates EduVoice from a tool that is technically accessible and one that is genuinely usable by the students who need it most.

**Auth0**

Auth0 handles every aspect of identity in EduVoice — who you are, what role you have, and what you are allowed to see.
When a user logs in, Auth0 authenticates them and issues a JWT token. The critical part is that we injected a custom role claim into every token at login time — so the token itself carries whether the user is a teacher, student, or admin. Every single API request to our FastAPI backend is verified against this token, and the role is extracted without a single extra database lookup.
This role is what drives the entire routing logic of the platform. A teacher logging in sees the content creation dashboard. A student logging in sees their personalised lesson feed. An admin sees the institution management panel. Same login screen, three completely different experiences — all decided by the Auth0 role claim.
For EduVoice specifically, this mattered beyond just access control. The student's role token is what the backend uses to identify which disability profile to fetch from Snowflake — so the moment a student logs in, the entire personalisation chain starts from their Auth0 identity.
In short — Auth0 is the front door of EduVoice. It decides who enters, what they carry with them, and ensures that a student never accidentally sees a teacher's dashboard and a teacher never accidentally edits another teacher's content.

**Best Beginners' Team**

This is our first time building with multiple AI APIs chained together, working with Snowflake's VARIANT columns, and deploying a full-stack app with a live backend. We picked a hard problem on purpose — inclusive education in India affects millions of students — and built something that actually demonstrates the idea end to end.

Team **ByteDrops** -- [Arnab Chaudhuri](https://github.com/Arnab-dot), [Ankit Talukder](https://github.com/ankit2061)

`2026-02-28`

---

### EQUALED-Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/equaledai-8c2e) [![Built at](https://img.shields.io/badge/Built%20at-Prompt%20The%20Future-0052CC?style=flat-square)](https://promptthefuture.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Education

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **AURA** -- [SACHIN KUMAR](https://github.com/wheresachin), [RAUNAK Azim](https://github.com/ranuak20), [Anita Kumari](https://github.com/anita-kumari-2207362a2), [Rajiya khatoon](https://github.com/rajiya2007)

`2026-02-20`

---

### Growdex
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/growdex-b3ff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ayushkumar2601/HELLCODERS_AMUHACKS5.0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://growdex-7.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/qhC-7o6Upzs) [![Built at](https://img.shields.io/badge/Built%20at-AMUHACKS%205.0-0052CC?style=flat-square)](https://amuhacks-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> One stop for Student Success

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

### The Problem It Solves

Students today juggle academics, career prep, skills, deadlines, and mental health across scattered platforms. Nothing talks to each other. As a result, performance tracking becomes reactive instead of proactive. You only realize there’s a problem when your GPA drops or deadlines pile up. Institutions face the same issue — they rely on static reports instead of real-time insights to detect at-risk students early.

### What It Can Be Used For

With this platform, students can monitor their GPA trends, track tasks, analyze stress levels, and see predictive insights like placement probability or burnout risk — all in one dashboard. It acts like a data-driven academic co-pilot, helping users make smarter study and career decisions instead of guessing.

Admins can view department-wide analytics, identify struggling students early, and make informed interventions using structured data rather than spreadsheets.

In short, it makes academic growth structured, measurable, and safer.

And yes, you should totally read this whole text because I wrote it (definitely not AI).

**Challenges we ran into**

### Challenges I Ran Into

One major hurdle was implementing **role-based authentication** with Supabase in a Next.js App Router environment. Handling sessions correctly on both the client and server side was tricky, especially when protecting routes like `/admin` and `/student`. At first, users could manually navigate to restricted pages because the middleware wasn’t validating the session properly.

I solved this by implementing Supabase’s SSR helpers, configuring secure cookie-based sessions, and adding middleware checks that verify both authentication status and user role before allowing access. This ensured proper redirection and secure route protection.

Another challenge was replacing mock dashboard data with real database queries without breaking the UI. Some components were tightly coupled with static data structures, which caused type mismatches after integrating Supabase. I refactored the components to use properly typed async server functions and introduced consistent data models across the app.

Lastly, redesigning the UI into a neo-brutalist system required restructuring reusable components rather than patching styles individually. Creating shared primitives like buttons and cards helped maintain consistency and scalability.

Each obstacle forced better architecture decisions — which ultimately made the project more robust and production-ready.

Team **HELL CODERS** -- [ATUL JHA](https://github.com/ATULJHAgh), [AYUSH KUMAR](https://github.com/ayushkumar2601), [ayush kumargour](https://github.com/AYUSHKUMAR0401), [Sayan Ghanty](https://github.com/SayanGhanty09)

`2026-02-11`

---

### Students' Finance Tracker
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/students-finance-tracker-dda1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Krish-26/Hackathon_fin_prjct) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1qe7Yr_ZNqEGMGlndldIb-AGi2t3oLYQF/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HACK%20THE%20THRONE-0052CC?style=flat-square)](https://hack-the-throne.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Spendwiser

![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

Young adults are not the most financially literate or responsible, so we decided to help bring a change to that.

Here's a simple finance tracker tailored for student usage, which is simple to use, not intimidating, and light.

The goal is to inculcate healthy spending habits in young adults by tracking the spendings and providing key insights.

**Challenges we ran into**

The savings tab turned out to be quite tricky and buggy, the logic was not as sound and needs to be thought out through again.

Rolling over months also took quite a few tries 😬.

Team **The Predator** -- Kshitiz Thakur, Krrish Dogra, Krishiv Guleria, Abhay Sharma

`2026-02-08`

---

### GameED
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gameed-950b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tanishjain101/GameED--Gamefied-Education-for-Rural-Development) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sRlY4BSHMno) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Gamefied Education for Rural Development

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Vanilla JS](https://img.shields.io/badge/Vanilla%20JS-333333?style=flat-square) ![LocalStorage](https://img.shields.io/badge/LocalStorage-333333?style=flat-square)

**The problem it solves**

Transforming Rural Education Through Gamification GameEd is an innovative web-based platform that transforms traditional education into an engaging, gamified experience specifically designed for rural communities. By leveraging game mechanics like XP, achievements, badges, and leaderboards, we make learning addictive and fun while addressing educational challenges in underserved areas.

**Challenges we ran into**

One of the biggest hurdles was building a reactive state management system without using frameworks like React or Vue. Since we rely on Vanilla JS, keeping the UI (progress bars, XP counters, badges) in perfect sync with the underlying data required writing custom helper functions to manually update the DOM every time a user’s state changed

**Open Innovation**

- EdTech (Education Technology)
- Gamification
- SocialImpact

Team **Taskforce 141** -- [Harjas Singh](https://github.com/harjasbuddy), [Tanish Jain](https://github.com/tanishjain101), [Siya Sharma](https://github.com/siyasharma1022007-ctrl), [Utkarsh Walia](https://github.com/utkwalia)

`2026-02-08`

---

### Learnify
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/learnify-bcc8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BHUVI-SHIP-IT/learnify) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://learnify3.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sW0rO1iPp1E) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Learnify is an AI-powered, accessibility-first lea

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![OAuth](https://img.shields.io/badge/OAuth-333333?style=flat-square) ![WebRTC](https://img.shields.io/badge/WebRTC-333333?style=flat-square) ![WebSOC](https://img.shields.io/badge/WebSOC-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

The challenge that Learnify addresses is the fragmentation, impersonalization, and lack of access to a complete learning system. Currently, learners are using multiple unrelated applications to learn, plan, code, collaborate, and track their progress; therefore, their overall learning is inefficient and frustrating. Most learning platforms use a standardized method that does not consider each learner's different pace for learning, skills that are lagging or missing, and what the learner wants to achieve, as well as considering the accessibility needs of each learner.

The result is low levels of engagement, prolonged delays in obtaining feedback, unpreparedness for use of skills, and inequity in obtaining quality education for many disabled or diverse-learning-needs learners. Moreover, institutions are having little real-time visibility into their learners' progress or the effectiveness of the learning experiences.

To help solve this problem, Learnify has created an all-inclusive and secure, AI-integrated learning experience that brings together all learning processes into a solution. With a personalized route to success through learning, AI support is always available, as are accessibility tools. Because of this, learners can learn more effectively, be more engaged, and continually develop new skill sets.

**Challenges we ran into**

Developing an AI Learning Solution that’s adaptable is a tough job because personalization includes individual learning speeds, goals, and accessibility needs without adding complexity and inaccuracies to the solution itself. Finding the right combination of AI-recommendations and reliable learning structures was very challenging.

Accessibility features — like dyslexia-friendly layouts, keyboard navigation, and inclusive design — presented major design challenges while also providing clear, responsive, and usable interfaces.

Time constraints also added to our rapid prototyping project as we were integrating artificial intelligence (AI) APIs, and analytic tools with many features onto one united platform.

To overcome these obstacles, we developed a modular architecture to focus on delivering a functional version of the product; we prioritized defining the appropriate core functions; and we tested through iteration to improve the AI-prompts and workflows. Rather than treating accessibility as an added feature, it became a critical part of the project's requirements. Rather than creating complex functional features, we will be delivering a basic and functional MVP.

**Open Track**

Learnify is a strong fit for the Open Track as it is a flexible, multi-domain AI-powered learning solution that does not fit into a single specific category. The project tackles several real-world problems like personalized education, accessibility, skill-building, and adoption of digital learning solutions in a single system.

Developed as an AI-powered, accessibility-focused learning operating system, Learnify integrates adaptive learning paths, AI-powered real-time support, peer-based learning, and support for learners with learning disabilities in a single, scalable solution. The modular design of the solution enables it to be adaptable to various use cases such as student education, inclusive learning, and future workforce upskilling, making it a strong fit for open-ended problem statements.

The Open Track allows Learnify to showcase innovation, impact, and scalability without being limited to a specific vertical, demonstrating the use of AI to revolutionize learning solutions in various domains.

[BHUVANESWAR M](https://github.com/BHUVI-SHIP-IT)

`2026-01-31`

---

### Prof Review app
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hjj-247b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anjali121234/mdg-project-app.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mdg-project-app.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ucvBThIuTt0?si=qF9fut4tkzfwdsPq) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> "Student-driven professor reviews"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Students often lack a reliable and structured way to share feedback about professors.

Currently:

Feedback is informal (WhatsApp, word of mouth)

Reviews are unstructured and biased

New students have no data to choose professors or subjects

Institutions lack transparent student insight

**Challenges we ran into**

Challenges we ran into 
1-Making review constraints 
2- Data mapping between frontend and back-end

**Open Track**

Our project is suitable for the open track because it solves a real-world problem using a scalable, full-stack solution without being limited to a specific domain.

Team **HAD H YRR** -- HARSH RISHI, Anjali .

`2026-02-01`

---

### DOMinator.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dominatorai-82c1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shaikh-Ibrahim-Mohammed-Rashid/KNOWCODE-3.0-THE-DOMinators/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/S3FnyPePl_g) [![Built at](https://img.shields.io/badge/Built%20at-KnowCode%203.0-0052CC?style=flat-square)](https://knowcode-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-POWERED STUDENT GUIDANCE & SCAM DETECTION SYS

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ML Classifier](https://img.shields.io/badge/ML%20Classifier-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

PROBLEM STATEMENT 1: STUDENT GUIDANCE SYSTEM USING MACHINE LEARNING
Diploma students often struggle to find colleges that provide Direct Second-Year admission because admission rules, eligibility criteria, and seat availability are not clearly available in one unified platform. This lack of proper guidance leads to confusion, uninformed decision-making, and the loss of valuable time during the critical admission process.


PROBLEM STATEMENT 2: SCAM DETECTION SYSTEM USING ARTIFICIAL INTELLIGENCE
With the exponential growth of online recruitment, there has been a rapid increase in fake internship and job offer letters targeting students and freshers. These fraudulent offers closely resemble genuine documents, making it difficult for candidates to verify their authenticity. This often results in significant financial loss and career insecurity for vulnerable job seekers.

**Challenges we ran into**

Challenges we ran into
Since our project targets two distinct problems Academic Guidance and Fraud Protection we faced unique technical hurdles in both domains while integrating them into a single platform.

1. Data Unavailability & Unstructured Formats (Guidance System) The primary challenge for the college predictor was that admission rules, seat matrices, and cutoff lists were scattered across disparate websites and unstructured PDF files. There was no ready-to-use API or dataset.

How we got over it: We had to build our own dataset from scratch. We wrote custom Python scripts to scrape data from official portals and utilized Pandas to clean and standardize the unstructured data into a machine-learning-friendly format.

2. Reducing False Positives (Scam Detection) For the scam detection module, the model initially struggled to distinguish between genuine offer letters from early-stage startups (which often lack formal formatting) and sophisticated fake offers created by scammers.

How we got over it: We shifted from simple keyword matching to a Context-Aware NLP approach. We also integrated OCR (Optical Character Recognition) to extract and analyze text from image-based offer letters, which significantly improved our detection accuracy.

Team **The DOMinators** -- [Shaikh Mudassir](https://github.com/ShaikhMudassir7), [Ibrahim Shaikh](https://github.com/Shaikh-ibrahim)

`2026-01-25`

---

### Proposal For Kornia and Fossia
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vlm-for-transcribeit-f825) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1KRb_Pq-xNRQUNOSbLO3-Zdrw7pe9xp-C/edit?usp=sharing&ouid=115132867771070245916&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> VLM and Robot Learning

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Ray](https://img.shields.io/badge/Ray-333333?style=flat-square)

**The problem it solves**

## Proposal 1: Data & Fine-Tuning API + Model Expansion for VLMs (Kornia)

Vision-Language Models (VLMs) enable tasks such as **Visual Question Answering, Image Captioning, and multimodal reasoning**, but fine-tuning them is still fragmented and difficult.

Today, users must:
1. Write custom multimodal dataset loaders  
2. Maintain model-specific training scripts  
3. Manually integrate logging, evaluation, and scaling tools  

This increases development time and makes experiments **hard to reproduce and easy to break**.

##### How this project helps

This project extends Kornia into a **first-class vision-language training platform** by:

- Providing a **standardized multimodal dataset API**  
- Integrating modern VLM architectures behind a **unified interface**  
- Offering a **robust fine-tuning workflow** with validation, logging, and scalability built in  

This allows researchers and developers to **focus on ideas instead of infrastructure**, making experimentation faster and safer.

## Proposal 2: VLM for TranscribeIt (Fossia)

Online video content remains inaccessible to large groups of users due to **three major barriers**:

1. Sensory barriers – visually impaired users miss on-screen actions, charts, or text  
2. Context barriers – transcripts lack visual cues and non-verbal information  
3. Language barriers – content is often locked to a single spoken language  

Most transcription tools only convert speech to text. They fail to capture **visual context**, making videos incomplete or confusing for many users.

##### How this project helps

This project transforms TranscribeIt into a **comprehensive accessibility engine** by:

- Adding **visual understanding** using lightweight Visual Language Models (VLMs)  
- Generating **timestamped visual descriptions** (e.g., “A chart appears on screen”)  
- Merging visual context with audio transcripts into a **unified, accessible output**

This makes video content **easier to understand, safer to consume, and more inclusive**, especially for visually impaired users and people consuming content asynchronously.

## Proposal 3: Robot Learning (Advanced) – Kornia

Robot learning systems require close coupling between **perception, spatial reasoning, data collection, and action**, yet most pipelines are fragmented and difficult to reproduce.

Common issues include:
1. Unstructured sensor logs  
2. Non-differentiable perception pipelines  
3. Datasets that are hard to replay or reuse  
4. Learning systems tightly coupled to specific robots  

This makes robot learning **slow to iterate and difficult to scale**.

##### How this project helps

This project extends Kornia into robotics by:

- Expanding bubbaloop for **real or simulated robot integration**  
- Introducing **structured, MCAP-based robot learning datasets**  
- Enabling **differentiable perception-to-action pipelines** using Kornia  

This supports safer experimentation, reproducibility, and future **imitation learning and Vision-Language-Action (VLA)** research.

**Challenges we ran into**

## Proposal 1: Data & Fine-Tuning API + Model Expansion for VLMs (Kornia)
**1. Inconsistent multimodal datasets**
Image–text datasets often contain missing captions, corrupted images, or extreme length variations.

**How I addressed it:**  
I designed the dataset API with **early validation, strict vs. permissive modes, and diagnostic summaries**, ensuring issues are detected before training.

**2. Model–dataset compatibility issues**
Different VLMs expect different image resolutions, tokenizers, and input formats.

**How I addressed it:**  
I introduced **standardized configuration objects and compatibility checks**, with descriptive error messages to prevent silent misconfiguration.

## Proposal 2: VLM for TranscribeIt (Fossia)
**1. Balancing accuracy with performance**
VLMs are typically large and resource-intensive, which conflicts with TranscribeIt’s goal of being **self-hostable and lightweight**.

**How I addressed it:**  
I evaluated optimized models such as Moondream2 and NanoLLaVA, and designed the pipeline around **quantized inference (4-bit / 8-bit)** and configurable frame sampling to keep resource usage predictable.

**2. Avoiding blocking the transcription pipeline**
Running VLM inference synchronously would significantly slow down audio transcription.

**How I addressed it:**  
I designed the system to run VLM inference as an **asynchronous background task**, ensuring the primary transcription flow remains fast and responsive.

## Proposal 3: Robot Learning (Advanced) – Kornia
**1. Sensor synchronization**
Precise alignment between camera data, robot state, and actions is critical.

**How I addressed it:**  
I designed the dataset structure around **timestamp-based validation and synchronization checks**, detecting misalignment early.

**2. Unstructured robotics data**
Robotics datasets are often difficult to reuse due to inconsistent formats.

**How I addressed it:**  
I adopted **MCAP as a first-class storage format** and defined a clear schema for observations, actions, and annotations.

[Dhruv Bhrasadiya](https://github.com/Dhruv-D-Bhrasadiya)

`2026-01-19`

---

### E-Rickshaw Connect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/erickshaw-connect-64c7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://e-rickshaw-870c6.web.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ySahd_LPMxw) [![Built at](https://img.shields.io/badge/Built%20at-Weekend%20of%20Code%202026-0052CC?style=flat-square)](https://weekendofcode2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Ride-sharing grid exclusively for MNNIT students.

![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square) ![canvas api](https://img.shields.io/badge/canvas%20api-333333?style=flat-square) ![OSRM](https://img.shields.io/badge/OSRM-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square) ![Cloud Firestore](https://img.shields.io/badge/Cloud%20Firestore-333333?style=flat-square)

**The problem it solves**

MNNIT Allahabad students often struggle with coordinating e-rickshaw rides to city destinations (like Civil Lines or the Junction) and outstations (like Lucknow or Varanasi). This results in high individual costs and safety concerns.

E-Rickshaw Connect solves this by:

Cost Efficiency: Facilitating seat-sharing among peers to split fares.

Verified Security: Restricting access strictly to @mnnit.ac.in email addresses to ensure users only share rides with verified campus peers.

Precision Coordination: Providing a live HUD with real-time road mapping and automated ETA calculations to remove the guesswork from campus transit.

**Challenges we ran into**

Map Route Overlapping: A significant hurdle was visualizing multiple rides on the same road without them overlapping and becoming unreadable. I solved this by implementing a coordinate offset algorithm that shifts parallel routes by a small fraction so each path is distinct.

Real-Time Data Integrity: Ensuring that the "Live Feed" stayed synced without unnecessary re-renders was challenging. I utilized Firestore's onSnapshot listeners to manage real-time updates while implementing auto-expiry logic to purge rides that have already departed.

Glassmorphism Performance: Maintaining a high-performance UI with blurred backgrounds and a particle engine on mobile devices required careful CSS and Canvas optimization.

Team **PowerKing** -- [Adarsh Hanji](https://github.com/adarsh-hanji), [Faizal Ameer](https://github.com/faizal0624), [Aatmik Ramachandran](https://github.com/CharterADz), [Vishal Ganesh](https://github.com/visgan2007-lgtm)

`2026-01-24`

---

### ALTRA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/altra-dbff) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jas212-on/adaptive-learning-agent) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_iE9wEINltY) [![Built at](https://img.shields.io/badge/Built%20at-Code%20Kalari-0052CC?style=flat-square)](https://code-kalari.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Adaptive learning and Tracking Agent

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tesseract OCR](https://img.shields.io/badge/Tesseract%20OCR-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

Online learning has never been more accessible — yet learners still struggle with lack of structure, unclear next steps, and poor progress tracking. People watch videos, read PDFs, and browse tutorials daily, but most of this learning remains unorganized, untracked, and difficult to measure. This leads to wasted time, repeated content, and incomplete mastery.

ALTRA solves this by transforming passive content consumption into an organized learning journey.

What People Can Use It For - Automatic Learning Tracking
No need to manually note what you studied. ALTRA detects learning content from YouTube, PDFs, websites, and docs in real time.

Instant Roadmap Creation
Get a clear step-by-step learning path for any detected topic.

Resource Recommendation
Discover the best videos, articles, and practice materials for each sub-topic.

Progress Visualization
View your mastery through interactive knowledge graphs.

Smart Revision
Auto-generated quizzes reinforce weak areas.

Personalized Learning History
Keep a lifelong record of everything you’ve learned.

**Challenges we ran into**

OCR Detection 
Accuracy in analyzing the text from screenshots

Gemini Limit
Use of LLM call via API is limited due to the token limit in their free-tier API's

Multilingual Support
Weak support offered by TesseractOCR for languages other than english

Team **VioniX** -- [Abhinandh A](https://github.com/a6hinandh), [Aniketh S](https://github.com/anikethdjz), [Sajish Sajan Varghese](https://github.com/Sajish06), [Jason Bobby](https://github.com/jas212-on)

`2026-01-18`

---

### Sharpner
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sharpner-e617) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sharpner.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/D_iGZ2HR__s?si=h_OkU5Iqpa8mnfBa) [![Built at](https://img.shields.io/badge/Built%20at-GenAI%20Hackathon%20--%20Chandigarh%202025-0052CC?style=flat-square)](https://genai-hackathon-chandigarh-2025.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Sharpner - Advanced Online Code Editor & Learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![gemini](https://img.shields.io/badge/gemini-333333?style=flat-square)

**The problem it solves**

# Sharpner  
**Advanced Online Code Editor & Learning Platform**

Sharpner is a modern, web-based integrated development environment (IDE) that bridges the gap between **learning to code** and **building real-world applications**. It combines a powerful code editor, cloud execution, AI assistance, real-time collaboration, and integrated learning resources—everything in one place.

---

## 🌟 Why Sharpner?

Learning and coding today often means juggling multiple tools:
- Code editor
- Documentation
- YouTube tutorials
- AI chat tools
- Collaboration platforms

This constant context switching breaks focus and slows productivity.

**Sharpner solves this by unifying the entire development and learning workflow into a single, distraction-free interface.**

---

## ❗ The Problem It Solves

- Fragmented learning and development experience  
- Frequent tab switching that breaks flow  
- Complex local setup (SDKs, compilers, environments)  
- Poor collaboration experience for remote learning  
- Beginners struggling to connect theory with practice  

---

## ✅ What You Can Use Sharpner For

- **Learn programming faster**
  - Read tutorials and write code side-by-side
  - Ideal for beginners and self-learners

- **Write & run code instantly**
  - Execute code in 10+ languages with zero setup
  - Cloud-based, secure, and isolated execution

- **Debug and understand code with AI**
  - Context-aware explanations
  - Learn *why* your code fails, not just the fix

- **Collaborate in real time**
  - Pair programming and remote classrooms
  - Live cursors, instant code sync

- **Prototype quickly**
  - Test algorithms, logic, and ideas in seconds
  - Useful for interviews, hackathons, and demos

---

**Challenges we ran into**

##  Git Conflict Challenge 

During development of **Sharpner**, we frequently ran into **Git merge conflicts**, especially when multiple contributors were working on the same core files (editor logic, Socket.io handlers, and API routes).

### The Issue
- Parallel feature development caused conflicts in shared files  
- Rebase and merge operations occasionally overwrote important changes  
- Conflicts became harder to resolve as the codebase grew  

### How We Solved It
- Broke large files into **smaller, modular components**
- Followed a **feature-branch workflow** instead of committing directly to `main`
- Used **clear commit messages** and rebased frequently
- Manually reviewed conflicts line-by-line to avoid silent bugs

### What We Learned
- Good Git practices scale just as much as good code
- Modular architecture drastically reduces merge conflicts
- Frequent syncing prevents painful late-stage conflicts

This experience helped us improve both our **collaboration process** and **codebase structure**.

---

##  AI System Instruction Challenge 

While integrating the **AI assistant** in Sharpner, one major hurdle was **designing effective system instructions** that kept responses helpful, consistent, and safe.

### The Issue
- Early prompts produced **generic or overly verbose answers**
- The AI sometimes ignored context from the editor
- Inconsistent tone and formatting across responses

### How We Solved It
- Created a **strict system instruction layer** that defined:
  - Role (pair programmer + tutor)
  - Response format (Markdown + syntax highlighting)
  - Behavior rules (explain *why*, not just *what*)
- Injected **editor context (current code, language, error output)** into each request
- Iteratively refined prompts by testing real user queries

### What We Learned
- Prompt design is as important as model choice
- Clear constraints lead to more reliable AI behavior
- Context-aware instructions drastically improve learning outcomes

This refinement turned the AI from a basic chatbot into a **true coding assistant** inside Sharpner.

Team **SharpVision** -- Gobind Singh, Ashish Yadav, [Ansh Sharma](https://github.com/CodeCrafter-c), Ratan Singh

`2025-12-24`

---

### Smart ML Model Trainer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-ml-model-trainer-ee93) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anushka-Gurav/Tech_Titans_ML_Model_Trainer) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ml-model-trainer.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Turning ML mistakes into learning moments.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**The Core Problem**

Students and early-stage ML learners often struggle to move from theory to a working, trained model. While tutorials explain algorithms, real-world ML workflows involve many hidden complexities that are difficult for beginners to manage independently.

Common challenges include:

- Selecting the right algorithm for a given dataset
- Understanding why a model fails or produces poor results
- Debugging silent errors, crashes, or compatibility issues
- Manually handling data preprocessing, validation, and format mismatches
- Successfully reaching the final goal: a trained and reusable model file (.pkl)

Most existing ML tools assume prior expertise and focus only on execution, without explaining what went wrong, why it happened, or how to fix it. As a result, beginners are left confused, discouraged, and unable to learn from their mistakes.

**Identified Gap in Existing Solutions**

Current ML training tools prioritize performance and flexibility over guidance. While powerful, they:

- Do not explain model failures in simple terms
- Provide minimal feedback when errors occur
- Expect users to already understand preprocessing, metrics, and debugging

This creates a learning gap where beginners can run code but cannot reason about outcomes.

**Challenges we ran into**

Challenge :
As requirements evolved, changes in training and evaluation logic began introducing silent errors and inconsistent model comparisons.

How Kiro helped:
Using Kiro’s spec-driven development, autopilot, and invariant-based tests, I locked correctness guarantees upfront. Kiro continuously validated changes against the spec, catching inconsistencies early and preserving reliability across training, evaluation, and comparison.
Challenge  Handling large, noisy real-world datasets caused memory spikes and slow training, impacting user experience.
How it was solved: I optimized data loading and preprocessing manually by batching datasets, reducing in-memory operations, and tuning preprocessing steps to balance performance and accuracy.

**AWS**

1. Planning-First Development: The project was built using Kiro’s spec-driven workflow, where system requirements, constraints, and invariants were defined before writing code, aligning perfectly with Kiro’s focus on planning and ideation.

2. Authentic Use of Kiro Features: Kiro was actively used for autopilot execution, architecture generation, flow diagrams, and invariant-based test planning, not just for code generation.

3. Traceable Execution: Every major feature (model training, evaluation, comparison, export) is traceable from spec → design → tests → implementation, demonstrating structured and disciplined use of the Kiro platform.

4. Well-Documented HERO Folder: The repository includes a dedicated ./kiro/ (HERO) folder containing planning notes, design decisions, specs, and diagrams, making the build process easy to review.

5. Clear Demo of Kiro in Action: The demo video showcases how Kiro guided decisions and evolution of the system, highlighting planning depth and execution clarity rather than just the final output.

Team **Tech Titans** -- [Shraddha Mane](https://github.com/Shraddha-mane-011), [Tasnim Shaikh](https://github.com/Tasnim-Shaikh), [Anushka Gurav](https://github.com/Anushka-Gurav), [Aishwarya Anekar](https://github.com/aishwaryanr)

`2025-12-30`

---

### SANKALP-BBZ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sankalpbbz-cb70) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vizsUEcYJFY) [![Built at](https://img.shields.io/badge/Built%20at-Calcutta%20<Hacks/>-0052CC?style=flat-square)](https://calcutta-lesshacksgreater.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The commitment to reduce hunger,poverty, education

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square)

**The problem it solves**

Sankalp is an AI-powered civic engagement platform that enables citizens to report real-world community issues like potholes, garbage, and broken infrastructure, while ensuring only genuine and high-priority problems are addressed.
It uses AI verification (Gemini + YOLO) to validate images, assess severity, prevent spam, and protect privacy through automatic face and number-plate blurring. Issues are geo-tagged, tracked in real time, and resolved transparently using proof-based before/after verification.
Sankalp encourages participation through gamification—points, leaderboards, and rewards—while providing dedicated dashboards for citizens, NGOs, and governments to collaborate efficiently.
In essence: Sankalp combines AI, transparency, and community participation to make civic problem-solving faster, fairer, and more trustworthy.

**Challenges we ran into**

- While building the AI powered validation system, we faced a problem that the model tends to categorize issue incorrectly. We changed out input prompts to strictly output categories amongst a set of categories.

- Privacy was a big concern while handling sensitive datas like images and faces of people in public places. To counter this, we added a feature to hide private details which blurs faces and license plates.

**All Participants**

Attendance Notification Automation

Team **buri buri zaemon** -- [BIDHAN SUREKA](https://github.com/Bidhan1811), [Debmalya Paul](https://github.com/debmalya123-debug), [gaurav munshi](https://github.com/harigaurav), [Aditya Chaudhary](https://github.com/adityachaudharycode)

`2025-12-28`

---

### SupremeClassroom
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/supremeclassroom-6aaf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/KingSahil/campus-app-new) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=XU51zkP3XgI) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20Hacks%203.0-0052CC?style=flat-square)](https://pechacks3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI based peer learning and attendance system

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

🧩 The Problem It Solves

Modern campuses suffer from fragmented systems.
Students use multiple apps for attendance, learning materials, food, notices, and discussions.
Admins rely on manual work, paper registers, or unsafe proxy-based attendance.

This causes:

❌ Wasted time

❌ Low student engagement

❌ Attendance fraud (proxy)

❌ Poor peer learning

❌ Scattered information

💡 What Campus Super App Does

Campus Super App brings everything into ONE secure Android app, making campus life simpler, safer, and smarter.

🎯 Core Use Cases (From First Principles)
1️⃣ Peer Learning (Knowledge Grows Together)

First principle:
Students learn better when they teach, discuss, and validate ideas together.

How the app helps:

Students ask doubts

Other students answer

Answers get upvoted by peers

Best explanations rise to the top

✔️ Encourages active learning
✔️ Builds confidence & communication skills
✔️ Reduces dependency on teachers for small doubts

2️⃣ AI-Based Help (Instant Support)

First principle:
Help should be available anytime, not only during class hours.

How the app helps:

AI explains concepts

AI gives hints, summaries, and clarifications

Helps students revise faster

✔️ Saves time
✔️ Personalized learning
✔️ Reduces stress before exams

3️⃣ Smart Attendance (Location-Based Verification)

First principle:
Attendance should verify physical presence, not just a name.

How it works:

Attendance opens only in class time

Student must be inside campus/class location

GPS + session timer verifies presence

Automatic notifications remind students

✔️ Prevents proxy attendance
✔️ Fully digital & secure
✔️ No manual registers

4️⃣ Centralized Campus Services

First principle:
One identity → many services.

Students can:

Order food 🍔

Access library 📚

View learning materials 🎓

Participate in discussions 💬

Buy/sell items 🛒

✔️ One app, one login
✔️ Faster access
✔️ Less confusion

🛡️ Safety & Reliability

Location-based attendance → no fake presence

Role-based access (Student / Admin)

Real-time sync → accurate data

Notifications → fewer missed classes

🚀 Why It’s Better Than Existing Systems
Existing Systems	Campus Super App
Multiple apps	One unified app
Manual attendance	Location-verified attendance
Passive learning	Peer + AI learning
No feedback loop	Upvotes & discussions
Delayed help	Instant AI support
📱 Platform

Android App

Built using React Native + Expo

Designed for Indian campuses

🏁 Final Impact

Campus Super App makes campus life:

Smarter → AI + analytics

Safer → Location-based verification

Faster → One platform

More engaging → Peer learning & upvotes

💬 It turns a passive campus system into an active digital ecosystem.

**Challenges we ran into**

🚧 Challenges I Ran Into (and How I Solved Them)

While building Campus Super App, I faced several real-world development challenges. These weren’t just coding issues, but system-level and time-management problems.

⏱️ 1. Adding Many Features in Limited Time

Problem (first principle):
Time is a finite resource, but features grow non-linearly.

I was building:

Peer learning system

AI help

Attendance with location verification

Admin dashboards

UI + navigation

Trying to build everything at once caused:

Feature overlap

Bugs due to rushed integration

Mental overload

How I solved it:

Broke features into core vs optional

Focused first on attendance + dashboard (core value)

Added AI and peer learning incrementally

Reused components instead of rewriting UI

✅ Result: Working MVP first, polish later

🔑 2. Gemini API Key Errors (AI Integration)

Problem (first principle):
APIs require correct authentication + environment setup.

I faced:

Invalid API key errors

Requests failing silently

API working in browser but not in app

Root cause:

API key not exposed correctly in Expo environment

Incorrect use of .env variables

How I solved it:

Stored the API key using Expo environment variables

Restarted Metro bundler after changes

Added proper error logging instead of silent failures

✅ Result: Stable AI responses inside the app

🗄️ 3. Supabase Errors (Auth & Data Sync)

Problem (first principle):
Backend systems are state-dependent (auth state, session, permissions).

I faced:

Auth state not updating correctly

Data not syncing in real time

Permission denied errors

Root cause:

Incorrect Row Level Security (RLS) policies

Auth listener not cleaned up properly

Navigation triggering before session was ready

How I solved it:

Fixed RLS policies for user roles

Used onAuthStateChange carefully with cleanup

Delayed navigation until session was confirmed

✅ Result: Reliable login and real-time data flow

🧠 Key Learnings

Build core logic first, features later

APIs fail silently unless logged properly

Backend security rules matter as much as frontend code

Debugging is a skill, not a mistake

🏁 Final Takeaway

These challenges taught me how real applications break — and how to fix them systematically.

💡 Writing code is easy. Making systems work together is the real engineering.

**Creative Use of Kiro**

Kiro helped me turn a complex campus idea into a working app within limited time.

Specifically, it helped by:

Structuring features (attendance, peer learning, AI help) into clear modules

Planning user flows for students and admins before coding

Prioritizing core features so the app remained usable even under time pressure

Refining AI prompts used with the Gemini API for better explanations

Reducing rework by clarifying logic before implementation

👉 In short: Kiro acted as a planning and reasoning layer that made development faster, cleaner, and more focused.

**Requestly**

🔧 How Requestly Fits Into This Track

Requestly fits into this project as a developer debugging and testing tool that helped me build faster and safer under time pressure.

🧠 First Principle: Why a Tool Like Requestly Is Needed

When building a real app, your frontend depends on APIs (AI, Supabase, attendance services).
If an API breaks, the entire feature stops.

So we need a way to:

Inspect requests

Modify responses

Debug without touching backend code

👉 That’s exactly where Requestly comes in.

🧪 What I Used Requestly For
1️⃣ Debugging API Requests (AI + Supabase)

Problem:
Some requests were failing, but the error wasn’t clear in the app.

How Requestly helped:

Viewed actual HTTP requests

Checked headers, tokens, payload

Verified if API keys were being sent correctly

✔️ Found missing headers
✔️ Detected wrong request formats

2️⃣ Testing Without Breaking the Backend

Problem:
Backend wasn’t always ready or stable.

How Requestly helped:

Mocked API responses

Returned fake success responses

Continued frontend development independently

✔️ Frontend progress didn’t stop
✔️ Saved a lot of time

3️⃣ Handling Gemini API Errors

Problem:
Gemini API failed due to key / environment issues.

How Requestly helped:

Intercepted requests

Confirmed whether the key was actually sent

Helped isolate frontend vs API issue

✔️ Faster root-cause detection

4️⃣ Safe Experimentation

Problem:
Changing live backend code is risky.

How Requestly helped:

Tested different request structures

Tried alternate endpoints

No backend redeploy needed

✔️ Safe testing
✔️ No data loss

🧩 Why Requestly Matters in This Track

This track focuses on:

Full-stack apps

AI integration

Real users

Time constraints

Requestly supports all of this by acting as a control layer between app and internet.

🏁 Final Summary

Requestly helped me:

Debug faster

Build frontend independently

Understand API behavior clearly

Reduce backend dependency

💡 In short: Requestly didn’t add features — it made building features possible.

**DigitalOcean**

was used as a reliable cloud backbone for deploying and testing backend services of the Campus Super App.

From first principles, any real app needs:

Stable servers

Fast deployment

Scalable infrastructure

How DigitalOcean fit in:

Hosted backend services securely

Enabled quick testing of APIs used by the app

Allowed smooth iteration without local-server limitations

Made the project feel production-ready, not just a demo

**Cloudflare**

This was hosted on cloudflare

**InsForge**

nsforge helped me move faster by simplifying backend setup and integration.

From first principles, a mobile app needs:

Auth

Data storage

APIs

Reliability

How Insforge fit in:

Reduced backend boilerplate so I could focus on features

Made connecting frontend → backend faster and cleaner

Helped test real app flows instead of mock demos

Saved time during rapid iteration in the hackathon

👉 In short: Insforge acted as a backend accelerator, letting me build more features in less time without sacrificing stability.

**Best Blog Post**

https://medium.com/p/7bcf3d165172/edit


this is our blog post made with kiro of our project

**Top Feedback**

https://airtable.com/appMDBZdtlySFAUZv/pagDf9CJykFLUjT7k/form

submited the form good!

**Social Engagement Prize**

added it on my instagram

www.instagram.com/supreme__sahil

**Gemini API**

Our project uses the Gemini API as a core intelligence layer inside the Campus Super App.

From first principles, Gemini acts as a real-time academic assistant that:

Explains concepts in simple language

Helps students resolve doubts instantly

Supports peer learning by improving answer quality

Instead of being a separate chatbot, Gemini is deeply integrated into the app’s learning flow, making help context-aware and always available.

This fits the Gemini API track because:

AI is used for real user problems, not demos

It enhances learning, productivity, and engagement

It is embedded inside a production-style Android app

👉 In short, Gemini transforms the app from a static system into an intelligent campus assistant.

Team **Tech Nerds** -- [Karamjit Singh](https://github.com/karampb02), [Sawal Pushkarna](https://github.com/sawal612), [Manpreet Dhir](https://github.com/Manpreetdhir), [Krishna Kumar](https://github.com/krishna212-3), [Sahil Gupta](https://github.com/kingsahil)

`2025-12-28`

---

### ArthaGuide
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/arthaguide-f5fd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dollaransh17/Artha_Guide_Code_Red_with_Rag_VectorDB) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://frontend-2feh32hnn-dollaransh17s-projects.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=wj-YyH70sCc) [![Built at](https://img.shields.io/badge/Built%20at-Technocrats%20Hackathon-0052CC?style=flat-square)](https://technocrats-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Your Money. Your Language. Your Guide

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

**The problem ArthaGuide solves**
ArthaGuide is an all-in-one financial assistant designed specifically for India’s 77 million gig workers. It helps users track their money effortlessly, understand their financial health, and access loans safely — all in English, Hindi, and Kannada.

At its core, ArthaGuide solves the biggest gap in the gig economy:
gig workers earn daily, but have no tools to manage irregular income, no access to regional-language financial advice, and face frequent loan rejections due to non-traditional earnings.

ArthaGuide brings everything into one simple platform:

SMS-powered auto-tracking: Paste any bank SMS → it becomes a categorized transaction instantly.

Smart Dashboard: Real-time financial health score, charts, insights, and spending patterns.

Multilingual AI Loan Advisor: Personalized loan guidance and financial advice in 3 languages.

Micro-loan Marketplace: Compare 5+ lenders with instant eligibility scoring and EMI calculations.

WhatsApp Bot Demo: A familiar chat interface for quick actions like adding expenses or checking balance.

With a clean UI, regional language support, and AI-powered insights,
ArthaGuide empowers gig workers to understand, manage, and improve their financial life — one SMS at a time.

**Challenges we ran into**

1. Accurate SMS Parsing Across 20+ Banking Formats

Bank SMS messages have no fixed structure — some use “INR”, some use “Rs”, some use “₹”, and dates vary across formats like DD-MM-YYYY, YYYY/MM/DD, etc.
This caused early failures where the parser would detect the wrong amount or skip transactions entirely.

How I solved it:

Built a regex-based multi-pattern parser

Normalized currency symbols

Added fallbacks for unknown patterns

Tested with 50+ real SMS samples

2. Making the Dashboard Update Instantly

When a new transaction was added, the charts (donut + bar) weren’t updating automatically due to React state timing issues.

Fix:

Centralized all financial data in a single state store

Triggered chart updates via useEffect watchers

Ensured transactions, balance, and score recompute in one pipeline

3. Multilingual Support Without Breaking the UI

Switching languages (especially Hindi/Kannada) increased text length and caused
UI breaks — buttons overlapped, chart labels overflowed.

Fix:

Implemented react-i18next with auto-resize

Added dynamic font scaling

Used flexible Tailwind classes (min-w, flex-wrap)

4. Loan Eligibility Engine Miscalculations

Our eligibility score depends on income, expenses, and savings.
Initially, minor changes in input caused huge jumps in score.

Fix:

Redesigned scoring formula

Introduced caps and smoothing functions

Created test cases for multiple financial profiles

Team **Hackistanis** -- [Gaurav Durge](https://github.com/gauravdurge-2332), [Swayam S](https://github.com/SwayamS123), [Shreyas Naik](https://github.com/shreyasNaik0101), [Anshul Vaibhav](https://github.com/dollaransh17)

`2025-12-06`

---

### ShikshaFlow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shikshaflow-c832) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://shikshaflow.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4M1zOiEw8gg) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20This%20Fall%202025%20--%20Milestone%20Edition-0052CC?style=flat-square)](https://hackthisfall.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Changing Our Education System

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

🚀 The Problem It Solves

Learning today is often passive and boring — students watch videos, read notes, and lose motivation. There’s no reward, no engagement, and no consistency.
shikshaflow fixes this.

🎮 Gamified Learning

Students earn XP, levels, achievements & coupons, and can compare progress globally.
Studying becomes fun, habit-forming, engaging — especially for long or difficult subjects.

🔗 Everything in One Place

Most platforms separate videos, quizzes, notes & progress tracking.
shikshaflow combines all of it:

📺 Video learning

🤖 AI-powered tutoring

🧠 Auto-generated quizzes

📊 Progress + reward tracking

No jumping between tools — learning becomes smooth and unified.

🏫 For Teachers & Institutions

Managing courses, tracking students and assessments is time-consuming.
shikshaflow offers a dashboard for educators with:

Course/content management

Authentication & registration

Real-time student progress tracking

Administration becomes easy & efficient.

🧩 Flexible for Self-Learners

Structured by subjects → topics → subtopics, but still self-paced.
AI-generated quizzes help learners test understanding without external exams.

⭐ In Short

shikshaflow bridges the gap between traditional education and self-learning, making study more engaging, rewarding, and effective — just like how you study with theory + PYQs + revision.

**Challenges we ran into**

🔥 Challenges I Ran Into

Building shikshaflow wasn’t straightforward — I hit multiple real-world hurdles while developing core features.

1. ⚠ Authentication & Session Handling

Managing secure login + registration with role-based access (student/teacher) initially caused session inconsistencies and redirect loops.
I resolved it by restructuring auth logic, implementing JWT-based validation, and adding proper protected routing.

2. 🎞 Video + Quiz Syncing

Syncing video progress with auto-generated quizzes was tricky — quizzes had to unlock only after the student completed or reached a certain timestamp.
I solved this using percentage-based video tracking and linking it to an AI-triggered quiz generation workflow.

3. 🤖 AI Quiz Quality

Early quiz generation produced repetitive or low-quality questions.
The fix was adjusting prompt-engineering, adding context awareness, and filtering output to ensure coverage of subtopics — resulting in more meaningful assessments.

4. 🗄 Database Structure

Designing a database schema flexible enough to support subjects → topics → subtopics, user progress, coupons, achievements and global rankings was complex.
After multiple iterations, I shifted to a more modular schema with relational mapping, making scaling easier.

5. 🎨 UI & Performance Balancing

Gamification meant lots of UI elements — XP bars, badges, streaks, etc.
Optimizing rendering and animations required lazy-loading, code splitting, and caching to keep performance smooth.

[Sahil Gupta](https://github.com/kingsahil)

`2025-11-27`

---

### Rural Learn
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rural-learn-9683) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ABHISHEKABHI52/rural-learn) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://rural-learnerhack.mgx.world/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/K4XB8VUJw4k?si=szmAZFTrSR206RNI) [![Built at](https://img.shields.io/badge/Built%20at-Hack--a--Sol%202025-0052CC?style=flat-square)](https://hackasol-4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Offline-first. Human-powered. Future-ready.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🚨 The Problem It Solves
📉 Teacher Shortage

Thousands of rural schools in Chhattisgarh have only one teacher, or none at all.

Children risk falling behind without proper guidance.

🌐 No / Low Internet

Streaming‑based EdTech fails in villages with poor connectivity.

Rural Learn is 100% offline‑first, ensuring continuity of education.

🖥️ Low Digital Literacy

Many students are first‑time users of digital tools.

The platform uses icon‑based, voice‑enabled UI in local languages to make learning intuitive.

🔋 Irregular Power Supply

Devices cannot rely on constant charging.

Rural Learn runs on lightweight, low‑power architecture that resumes progress instantly.

💡 What People Can Use It For
👩‍🏫 Facilitators (Teachers)

Use dashboards to track student progress and identify who needs help.

Gain “superpowers” to manage large classrooms more effectively.

🎓 Students

Learn at their own pace with an AI cognitive tutor that gives real‑time hints.

Stay motivated through gamification and AR demos (badges, points, 3D models).

🌍 Volunteers & Mentors

Connect remotely with rural learners for doubt‑clearing and mentorship.

Bridge the human connection gap with scheduled sessions.

🛡️ How It Makes Tasks Easier & Safer
✅ Offline‑First Learning → No dependency on internet, so education never stops.

✅ Affordable Deployment → Runs on Raspberry Pi for under ₹5,000, making it scalable.

✅ Inclusive Design → Voice + local language support ensures accessibility for first‑time learners.

✅ Resilient Architecture → Saves progress instantly, syncs when online, and works even with power cuts.

**Challenges we ran into**

🚨 The Problem Rural Learn Tackles
Massive Teacher Shortage

# In Chhattisgarh alone:

6,800+ single-teacher schools

212 schools with no teacher at all

# This leaves thousands of children without proper guidance, creating a deep learning gap.

Connectivity Barriers

Many villages have no or low internet.

# Streaming-based EdTech solutions fail here — continuity of education breaks down.

Low Digital Literacy

Students are often first-time users of digital tools.

Complex interfaces discourage learning instead of enabling it.

# Irregular Power Supply

Devices cannot rely on constant charging.

Learning tools must be lightweight, resilient, and offline-first.

**Web3 Revolution**

🌐 **How Rural Learn Fits Into Each Track
Web
**
Built as a Progressive Web App (PWA) using React.js..

Runs offline with IndexDB for local storage.

Facilitator dashboards and volunteer portals are accessible via browser, ensuring inclusivity across devices.

**Android**

Students in rural areas often have access to low‑cost Android phones.

The PWA installs like a native app, with voice input (Web Speech API) and gamified UI for first‑time users.

Offline caching ensures continuity even without mobile data.

**iOS**

Extends reach to urban volunteers and mentors who use iPhones/iPads.

Remote doubt‑clearing sessions and dashboards are accessible seamlessly.

Ensures cross‑platform collaboration between rural learners and urban supporters.

**macOS**

University students and professionals can use laptops for volunteer mentoring.

Facilitator dashboards and analytics tools run smoothly on macOS browsers.

Supports content creation and monitoring in real time.

**Others (Raspberry Pi / Local Server)**

A Raspberry Pi 4 acts as the “Rural‑Learn Box,” hosting the app offline.

**Creates a local WiFi hotspot for schools without internet.
**
Ultra‑affordable deployment (< ₹5,000) makes it scalable across villages.

Team **Solution Squad** -- [ABHISHEK KUMAR](https://github.com/ABHISHEKABHI52), [Biswajeet Tarasia](https://github.com/biswajeettararasia_622)

`2025-11-15`

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

### campus lost and found
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-lost-and-found-a94e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Amrinder-Singh-Sandhu/Lost-and-found-) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> a project to help students find their belongings

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

Team **CodeSlingers** -- [Amrinder Sandhu](https://github.com/Amrinder-Singh-Sandhu), Sneha Grover, [Ankit Sharma](https://github.com/Ankit007-gif), Nandini Thakur

`2026-03-08`

---

### LanguaChat
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/languachat-dfae) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ZunedKhan07/LinguaChat) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Breaking Language Barriers in Real-Time Chat

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **Zuned_Khan** -- [Juned Khan](https://github.com/ZunedKhan07)

`2026-03-08`

---

### TeacherOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/teacheros-dbdb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kabillanta/teacherosv2/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8svGTrnnx9E) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A teacher companion

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Replit](https://img.shields.io/badge/Replit-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square) ![Lyzr](https://img.shields.io/badge/Lyzr-333333?style=flat-square)

**The problem it solves**

The real reason we built TeacherOS is because we realized that the education revolution in India isn't struggling in the policy meetings. It is struggling in the classrooms.

We looked at what is happening in schools in smaller towns and villages. Teachers there are managing huge classes of sixty or more students. On top of that, the government introduced the new NCF 2023 standards. While the policy itself is brilliant, for a teacher on the ground, it is just a dense 600 page document that they do not have the time to decode.

We did not want to build just another chatbot. We wanted to build a bridge. We wanted to create a tool that takes those complex government standards and automatically translates them into simple, daily actions for the teacher.

That is also why we obsessed over the voice feature. We put ourselves in the shoes of a teacher in a chaotic classroom. If a fight breaks out or the noise level gets too high, they do not have the luxury of stopping to type a long prompt on a small screen. They need help immediately. By making TeacherOS voice controlled, we ensured that high quality pedagogical support is accessible even to teachers who might not be very tech savvy.

At the end of the day, we saw that our teachers are burning out from administrative work. We built TeacherOS to handle the planning and the compliance so that teachers can get back to the one thing AI cannot do, which is connecting with their students.

**Challenges we ran into**

Honestly, our biggest headache was just trying to fit a production-level architecture into a cloud IDE environment. We were pretty ambitious—we wanted a React frontend, an Express backend, and a Python WebSocket server all running simultaneously.

The environment just wasn't happy about that. We spent a long night debugging port conflicts where the mobile preview simply refused to handshake with our backend because the container kept putting the services to sleep or blocking the WebSocket protocol. It felt a bit like trying to park a truck in a compact space; we really had to fight the default configuration to get all three services talking to each other without crashing the container.

Then there was the AI layer. We used the Lyzr agent for our RAG system, but initially, it was a little too creative. We didn't want creativity; we wanted strict compliance with the 600-page NCF document. Taming the agent to stop hallucinating general advice and actually stick to the specific government PDF we uploaded was a real wrestling match. We had to rewrite the system prompts about twenty times before it finally understood that it wasn't just a chatbot, but a strict compliance officer.

Team **Hackoverts** -- [Prince Gupta](https://github.com/pr1ncegupta), [Kabillan TA](https://github.com/kabillanta/)

`2026-02-15`

---

### SmritiAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smritiai-8ad7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ashutosh887/SmritiAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://smriti-ai.replit.app/) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> LLM reliability across Indian languages

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**SmritiAI addresses the critical gap in LLM reliability across Indian languages.**

Test, diagnose, and fix LLM reliability across Indian languages with prompt DNA extraction and evolution.

### Problem Statement
Current LLMs show **dramatic performance drops** when serving India's 1.4B population:
- English: 87% accuracy
- Hindi: 44.8% accuracy (50% drop)
- Tamil: 38.5% accuracy (56% drop)
- Bengali: Similar degradation

**No existing tools** help developers:
1. **Test** prompts across Indian languages systematically
2. **Diagnose** where comprehension breaks down
3. **Fix** prompts with language-specific optimizations

### What SmritiAI Does

**For Product Teams:**
- Test customer support prompts across Hindi, Tamil, Bengali, Marathi, Telugu before deployment
- Catch "phantom recall" failures where LLMs ignore critical instructions in regional languages
- Generate evolved prompt variants optimized for SOV grammar (Hindi/Tamil/Bengali)

**For AI Developers:**
- Identify which prompt structures mutate dangerously during translation
- Get segment-level diagnostics showing exactly where instructions fail
- Compare model performance (Claude vs GPT-4o vs Gemini) across languages

**For Enterprises:**
- Ensure compliance prompts work equally in all official languages
- Reduce token costs (Indic scripts cost 4× more tokens)
- Avoid reputational damage from culturally inappropriate responses

### Real-World Use Cases

1. **Banking**: Test loan disbursement prompts across languages to ensure equal treatment
2. **Government**: Verify citizen service chatbots maintain accuracy in all 22 official languages
3. **E-commerce**: Ensure product recommendations don't degrade for Tamil/Bengali users
4. **Healthcare**: Test medical advisory prompts for consistent safety across languages

### Making Existing Tasks Easier & Safer

**Before SmritiAI:**
- Manual testing across languages (weeks of work)
- No visibility into what breaks during translation
- No way to systematically improve cross-language reliability
- Risk of launching products that discriminate by language

**With SmritiAI:**
- Analyze any prompt across 4-22 languages in 30-45 seconds
- Visual "Smriti Score" showing health per language
- Automatic prompt evolution with language-specific fixes
- DNA extraction showing structural mutation risks

### Impact

**Market Size:**
- 886M Indian language internet users
- $18B+ TAM for Indic LLM tooling
- 0 existing solutions for multilingual LLM reliability

**Technical Innovation:**
- First tool for prompt DNA extraction (structural analysis)
- First segment-level "phantom recall" detection for Indic languages
- First automated SOV grammar adaptation for Hindi/Tamil/Bengali

**Challenges we ran into**

### 1. **Claude API Authentication with .env Files**

**Bug:** FastAPI/Uvicorn wasn't loading environment variables from `.env` file, causing authentication errors:
```
"Could not resolve authentication method. Expected api_key to be set"
```

**Root Cause:** FastAPI doesn't automatically load `.env` files - requires explicit `python-dotenv` integration.

**Solution:**
- Added `from dotenv import load_dotenv` at top of `app/main.py`
- Called `load_dotenv()` before any environment variable access
- Verified API key loading with test endpoint

**Learning:** Always explicitly load environment files in Python frameworks, never assume automatic loading.

**Hackathon Prizes**

I have used Claude / Anthropic APIs, Claude Code and Replit for coding.

Team **DevSapiens** -- [Ashutosh Jha](https://github.com/ashutosh887)

`2026-02-15`

---

### Stax-AI Tutor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/staxai-tutor-b75f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aakriti1613/Stax-AI_Tutor) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/SYiEK8xdygc) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Because solving isn’t the same as learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Judge0 API](https://img.shields.io/badge/Judge0%20API-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Today, learning Computer Science often feels fragmented and overwhelming for students. Most platforms push learners directly into competitive problem-solving without ensuring strong fundamentals in **DSA, programming languages, OOPS, and DBMS**. As a result, students memorize solutions, rely on walkthroughs, and lose confidence when they get stuck, without truly understanding *why* their code fails. The absence of structured guidance, personalized feedback, and engaging learning paths turns what should be an exciting journey into a stressful race.

This project solves that problem by transforming learning into a **gamified, guided journey**. Instead of jumping straight to hard problems, learners begin with **AI-generated theory**, followed by **interactive MCQs** that ensure conceptual clarity before moving forward. Only after proving understanding do they unlock **coding challenges**, carefully structured into **Basic, Medium, and Hard** levels. When learners struggle, the platform adapts—assignments are dynamically generated by AI and validated using **DeepSeek**, reinforcing weak concepts without revealing solutions.

Beyond individual learning, the platform introduces **contests, marathons, duels, and standoffs**, making practice social, motivating, and competitive in a healthy way. Leaderboards reward consistency and mastery rather than speed alone. By unifying theory, practice, personalization, and competition into one immersive ecosystem, this platform bridges the gap between learning and application, helping students build confidence, clarity, and long-term problem-solving skills instead of short-term rankings.

**Challenges we ran into**

* Designing a **balanced gamified learning journey** without overwhelming beginners
* Ensuring **personalized AI guidance** without revealing full solutions
* Managing **dynamic content generation** for theory, MCQs, and coding
* Maintaining **fair validation** for AI-generated assignments
* Integrating **contests, duels, and marathons** smoothly with learning flow

Team **WhatTheHack** -- [Akriti Jha](https://github.com/aakriti1613), [Suparna Lahiri](https://github.com/Suparnalahiri4), [Sakshi Chaudhary](https://github.com/sakshiigdtuw)

`2026-02-07`

---

### SARTHI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sarthi-4775) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sarthi-x-jdmh.vercel.app/?_vercel_share=UTB0agb5KXTLLKf6QgtvyE6KlOyVtfq5) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Rural care within reach

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Rural healthcare faces geographic isolation, severe specialist shortages, and a widening digital divide. Patients struggle with long travel distances, lack of internet, and low health literacy, making a human-centric mediator essential to bridge the gap to life-saving care.

**Challenges we ran into**

-connectivity issues and device       shortage in rural area
- iliteracy rate is high
- high api cost because of real time mapping
- the privacy factor

Team **Solvers Pro** -- [Hardik Aggarwal](https://github.com/hardik26127-lab), [Divyansh Goyal](https://github.com/divyanshgoyal1607), [Tanmay Bansal](https://github.com/tanmai-dev), [Aradhya Sharma](https://github.com/Aradhya13042007), [Pratyaksh Gupta](https://github.com/pratyaksh6907)

`2026-02-08`

---

### Federated learning model
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/federated-learning-model-c9cb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gaurav-0707a/federated_model) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/H9x6cMnRaPk) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Training ML models while maintaining data security

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Socket Programming](https://img.shields.io/badge/Socket%20Programming-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Pillow](https://img.shields.io/badge/Pillow-333333?style=flat-square) ![pickle](https://img.shields.io/badge/pickle-333333?style=flat-square) ![Federated Learning](https://img.shields.io/badge/Federated%20Learning-333333?style=flat-square)

**The problem it solves**

The core of federated learning revolves around data security, for example : suppose 2 Hospitals have 100 and 300 patients of a rare disease , they have created a ML model that predicts if a person has it or not , but cant improve it further as its rare , they cant simply upload their data to a cloud server and train on it as its illegal and most developing and developed countries have laws around this. Federated learning model can be used in these cases as the data never leaves the hospital!
Another example , suppose 3 startups have a dataset of its user of around 10k,20k,30k and a ml model to train but the market is being led by a company with 50-100k users dataset. The startups can collaborate using federated learning as their data isn't even exposed to each other , let alone the tech giant(democratized ai-ml) , cant sabotage each other , though they will have to agree on common features as well.
It can also be used to train open sourced ml model , as the users wont be exposing their training data and will get to use a more efficient ml model.

**Challenges we ran into**

the first issue i ran into connecting sockets , one will have to play with their fire wall(disable it) to deploy it over multiple devices. This still persists. it was my first introduction with ML (time constrained) as well and had to use multiple reference books as i couldn't afford overspending. The Maths around machine learning was complicated and had to spend hours in debugging. Connecting zip files to a directory is another headache as i used my path and didn't take input for the path(time up before i could change this)so to change this  kindly change directory and path joining. Finally last hurdle was how is python interpreting images? I will leave this for the reader , really interesting stuff (Note : Computer understands intensity). If you want to change ml model , change the model file and data_loader as well , depending on the data (use pandas for csv) , i finalized my model based on reading a paper. Next comes UI ,i didn't have the time to make a webpage and create frontend , backend , that would have made it so cool , i also wanted to use cryptography but didn't get the time to learn that , will learn that as well! I can write a book on the problems i faced that will end with : "it actually runs".

**Open Track**

its open for all submissions

**Fresher's Track**

i am a fresher

Gaurav Singh

`2026-02-01`

---

### HandsFreeWeb
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/handsfreeweb-418b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyanshuharshbodhi1/Hands-Free-Web) [![Built at](https://img.shields.io/badge/Built%20at-HackJNU4.0-0052CC?style=flat-square)](https://hackjnu4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Democratising Web Accessibility

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Nanotechnology](https://img.shields.io/badge/Nanotechnology-333333?style=flat-square) ![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-333333?style=flat-square) ![STT](https://img.shields.io/badge/STT-333333?style=flat-square)

**The problem it solves**

## The Core Problem
The internet is designed for mouse and keyboard users. For millions of people with mobility impairments, this creates an invisible barrier that locks them out of the digital world.

**Who struggles today?**
- People with ALS, cerebral palsy, paralysis, or spinal injuries who cannot use standard devices
- Professionals suffering from Repetitive Strain Injury (RSI) who need to rest their hands
- Anyone seeking a more natural, hands-free browsing experience

**Why current solutions fail:**
- Commercial eye-tracking devices cost ₹5,00,000+ (£8,000+)
- Require specialized hardware you don't own
- Many send facial data to cloud servers, compromising privacy

## What HandsFreeWeb Enables

**🎯 Mouse-Free Navigation**
Move the cursor with head movements. Click by opening your mouth. Our "Magnetic Snap" technology auto-locks onto buttons within 45px radius for effortless precision.

**🎤 Voice-Powered AI**
Ask questions about any webpage using just your voice. Get instant AI-generated answers without typing a single character.

**📄 Instant Summaries**
Preview articles before clicking. Summarize YouTube videos without watching them. Save time and cognitive energy.

## The Impact
- Replaces ₹5,00,000 hardware with a **free** Chrome extension
- Works with your existing laptop webcam — no extra devices
- 100% on-device processing — your data never leaves your computer
- Helps prevent RSI by letting users browse without touching keyboard or mouse

**Challenges we ran into**

## 1. Head Tracking Jitter
**Problem:** Raw webcam face-tracking data was extremely shaky, making the cursor unusable for clicking small buttons.

**Solution:** Implemented a **1€ (One Euro) Filter** — an adaptive algorithm that smooths slow movements while allowing fast movements through. Combined with linear interpolation for buttery-smooth cursor transitions.

## 2. Audio Recording Failures
**Problem:** MediaRecorder sometimes produced empty audio files, causing transcription to fail with "corrupted file" errors.

**Solution:** Added minimum 1.5-second recording duration before allowing stop. Used chunked recording (250ms intervals) to ensure data capture. Added blob size validation before API calls.

## 3. API Rate Limits During Testing
**Problem:** Exhausted Gemini's free-tier quota during intensive testing, breaking Q&A functionality right before demo.

**Solution:** Built a multi-tier fallback system: Groq API (primary, ultra-fast) → Gemini Cloud → Gemini Nano (local, offline-capable). Ensures reliability even when one service fails.

## 4. Accidental Mouth Clicks
**Problem:** Users talking or yawning triggered unwanted clicks, making the extension frustrating.

**Solution:** Added dynamic mouth calibration that learns each user's neutral position. Required mouth to stay open for 450ms before triggering click. Eliminated false positives completely.

## 5. Performance vs. Battery Life
**Problem:** Running face-tracking at 60fps drained laptop batteries in under an hour.

**Solution:** Optimized inference parameters and moved heavy processing to offscreen canvas. Reduced CPU usage by 40% while maintaining smooth cursor movement.

Team **Byte Masters** -- [Priyanshu Harshbodhi](https://github.com/priyanshuharshbodhi1/), [Anushttha Shrivastava](https://github.com/Anushttha)

`2026-01-31`

---

### Loan_Approval-prediction
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/loanapprovalprediction-ae05) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/JUil4eS9Q98) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Fast and Fair Loan Approval with Machine Learning

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Jupyter](https://img.shields.io/badge/Jupyter-333333?style=flat-square) ![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat-square) ![ML Classifier](https://img.shields.io/badge/ML%20Classifier-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

This project solves the problem of slow, manual, and sometimes biased loan approval processes in banks by using machine learning to make fast and data-driven predictions about whether a loan should be approved or not. It reduces the workload on bank staff, minimizes human error and bias, helps in identifying risky applicants early, and ensures that deserving customers get quicker access to financial services. Overall, the system improves efficiency, accuracy, and fairness in loan approval decisions.

[Yash singh](https://github.com/yashsingh-tech99)

`2026-01-24`

---

### Smart Path Buddy
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartpath-buddy-7711) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/coddingjatin/DU-Hacks-5.0-Submission) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1h0QTQBnCdnMGSW2AMh-qzvxA33bKeUy_/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XWOytblwVDQ) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your personalized AI roadmap for smarter learning!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

## 🧩 The Problem It Solves

In today’s digital learning ecosystem, learners are surrounded by thousands of online courses, videos, articles, and tutorials. However, this abundance creates **confusion rather than clarity**. Learners often struggle to decide **what to learn, in which order, and how deeply**, based on their individual goals and current skill levels.

Most existing learning platforms follow a **static and generic approach**, offering the same learning path to all users. They lack:

- Personalization based on individual learning styles and pace  
- Continuous assessment and real-time feedback  
- Clear visibility into progress and learning gaps  

As a result, learners waste time on irrelevant content, lose motivation, and frequently drop out before achieving meaningful outcomes.

----

## How Smart Path Buddy Solves the Problem

Smart Path Buddy addresses these challenges by transforming learning into a **structured, adaptive, and learner-centric experience**.

### Personalized Learning Paths
- Uses AI to analyze a learner’s goals, prior knowledge, learning style, and preferences  
- Generates a **custom learning roadmap** with ordered checkpoints, resources, and timelines  
- Continuously refines the roadmap as the learner progresses  

### Intelligent Assessment & Feedback
- Integrates **adaptive quizzes and assessments** to evaluate understanding at each stage  
- Identifies knowledge gaps and adjusts content difficulty accordingly  
- Provides instant explanations and feedback to reinforce learning  

### Clear Progress Tracking & Motivation
- Offers a **comprehensive dashboard** showing learning progress, quiz performance, streaks, achievements, and time spent  
- Uses **gamification elements** such as points, badges, and streaks to keep learners engaged and consistent  

### Always-On Learning Support
- Includes an **AI-powered chatbot** that acts as a virtual learning mentor  
- Helps learners clarify doubts, receive recommendations, and navigate the platform efficiently  

### Organized & Safe Learning Experience
- Integrates calendars, reminders, and workflows to help learners plan and manage study time effectively  
- Enables collaboration through meetings and group learning while maintaining data security and privacy  

----

##  What People Can Use It For

- Creating **structured learning journeys** for skills like programming, data science, AI, or academics  
- Preparing for **exams, certifications, interviews, or career transitions**  
- Tracking learning habits and improving productivity and consistency  
- Learning complex topics using **visual diagrams, quizzes, and guided workflows**  
- Institutions and educators can use it to **monitor learner progress and personalize instruction at scale**

----

## Overall Impact

By combining **AI-driven personalization**, **continuous assessment**, **progress analytics**, and **interactive support**, Smart Path Buddy significantly reduces learning confusion and effort. It enables learners to **learn faster, stay motivated, and achieve their goals efficiently**, making learning **smarter, safer, and more outcome-focused**.

----

### Project Screenshots:

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/0e4c0e50-2429-424b-9201-ffbb031c755f.png)

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/70bb0046-a3f4-4216-b9a1-c4658a4fb236.png)

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/19d3ce9c-c19d-48f6-9182-94edcb0cac34.png)

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/77b19787-9f06-4e38-a7f7-bf0e911a7441.png)

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/33d4c1a1-cc66-41df-bc54-8ee475b78623.png)

![image](https://assets.devfolio.co/content/24b69d141a6640f6ae31d51d6b6730a7/30c0b930-2cad-487e-a6a9-f9859f0ca196.png)

**Challenges we ran into**

## Challenges I Ran Into

Building an AI-powered personalized learning platform involved several technical and design challenges. Below are some key hurdles faced during development and how they were addressed:

### Designing Accurate Personalization Logic
**Challenge:**  
Creating learning paths that truly adapt to individual users was challenging due to diverse learning styles, skill levels, and goals. Initial recommendations were either too generic or overly complex.

**Solution:**  
We introduced a **learning style survey**, adaptive quizzes, and continuous progress tracking. By combining user inputs, quiz performance, and clustering-based insights, the system was able to generate and refine personalized roadmaps effectively.

-----

### Integrating AI Without Overusing It
**Challenge:**  
One major hurdle was deciding where AI was genuinely needed versus where traditional logic was sufficient. Overusing AI risked increasing latency and complexity.

**Solution:**  
AI was carefully applied only to high-impact areas such as **quiz generation, learning roadmap creation, chatbot assistance, and user clustering**, while standard backend logic handled authentication, scheduling, and progress tracking.

---

### Managing Real-Time Progress & Dashboard Sync
**Challenge:**  
Keeping the dashboard updated in real time with quizzes, streaks, achievements, and roadmap progress caused data consistency issues between frontend and backend.

**Solution:**  
We implemented **well-structured REST APIs** with event-based updates and optimized database queries, ensuring accurate and near real-time synchronization of learning data.

---

### Handling Diverse Learning Data
**Challenge:**  
User data included quizzes, surveys, progress logs, timelines, and preferences, making data modeling complex.

**Solution:**  
Using **MongoDB’s flexible schema**, we designed modular collections for users, quizzes, roadmaps, and analytics, allowing the platform to evolve without breaking existing data.

---

### Ensuring Security While Maintaining Usability
**Challenge:**  
Balancing strong authentication with a smooth user experience was difficult, especially for password resets and session handling.

**Solution:**  
We used **JWT-based authentication**, **bcrypt password hashing**, and secure token-based password recovery to ensure data safety without compromising usability.

---

### Scaling Features Within Limited Time
**Challenge:**  
Implementing multiple modules (AI, quizzes, dashboard, chatbot, calendar) within hackathon time constraints was a major challenge.

**Solution:**  
We followed a **modular development approach**, prioritizing core features first and integrating additional components incrementally, ensuring a stable and functional end-to-end solution.

---

## Key Takeaway

Each challenge helped improve the system’s design and scalability. By focusing on modular architecture, selective AI usage, and continuous testing, the project evolved into a robust, personalized, and user-centric learning platform.

Team **Squad_404** -- [Jatin Vishwakarma](https://github.com/coddingjatin), [Siddhi Savji](https://github.com/siddhisavji24-cell), [Om Akiwate](https://github.com/Om1807), [Mustafa Shikalgar](https://github.com/Mustafa-shikalgar)

`2026-01-25`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-eaca) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1VV2UYrOsjIV_0ckL3FPgnU7Hm-UHcm06/edit?usp=sharing&ouid=118397144886047654677&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Quizora – Real-Time Quizzes, Real Learning.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Traditional learning and assessment systems often rely on static quizzes and delayed feedback, which limits student engagement and reduces active participation. Many existing platforms fail to create an interactive environment that motivates learners to participate consistently. As a result, assessments become routine tasks rather than meaningful learning experiences, leading to lower retention and reduced interest in the subject matter.

Quizora addresses these limitations by introducing a real-time, gamified quiz platform that transforms assessments into engaging and competitive learning experiences. Through features such as live quizzes, time-based challenges, instant feedback, leaderboards, and relay-based quiz modes, Quizora encourages students to participate and stay focused actively. The platform promotes healthy competition, improves motivation, and supports faster learning by providing immediate performance insights. By combining technology, gamification, and real-time interaction, Quizora creates a more effective, engaging, and modern approach to digital learning and assessment.

**Challenges we ran into**

Developing Quizora involved several technical and design challenges, particularly in building a reliable real-time quiz experience. One of the key challenges was managing real-time data updates, such as synchronised timers, live score calculations, and leaderboard updates, while ensuring consistency across all users. Handling multiple users simultaneously without performance degradation required careful backend planning and optimisation.

Another challenge was designing the system to be scalable and maintainable for future enhancements. Features such as authentication, relay modes, advanced quiz types, and analytics needed to be planned from the beginning to avoid major refactoring later. Additionally, balancing UI responsiveness with backend performance was critical to delivering a seamless user experience. Ensuring smooth quiz transitions, accurate timing, and minimal latency across different devices required continuous testing, debugging, and refinement. Overcoming these challenges helped strengthen both the technical foundation and overall usability of the platform.

[Gunjan Kumari](https://github.com/Gunj08)

`2026-01-16`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-0ccc) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1MKZ3PV7eiKhepzxrx_loavlmjkGoFzLu/edit?usp=sharing&ouid=109924878108727075703&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Turning Quizzes into Competitive Learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

[Meghna Chatterjee](https://github.com/fun-geek)

`2026-01-17`

---

### Winter of Code 5.0
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wallgodds-web-eb87) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/18NX2bVmoTxTvHFWgYeNF9Hts8M6-5Fe_JiiDhdXhoIk/edit?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Open source learning through real projects

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

[Ravindra Yadav](http://github.com/ravindra-y)

`2026-01-19`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-5022) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1-Umxuu4Y4vCE4nNOZryOIEoyTWDMQHeD/edit?usp=sharing&ouid=114504768581022299956&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Fast-paced quizzes that make learning competitive.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

[Padmalochan Sahoo](https://github.com/Padmalochan-812/)

`2026-01-19`

---

### Vidhyapatha:One stop career and education advisor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vidhyapatha-one-stop-personalized-career-and-education-advisor-58a6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Amirthavarshini05/Pec_Hacks.git) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20Hacks%203.0-0052CC?style=flat-square)](https://pechacks3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Guiding Your Career, Shaping Your Future

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Turns student confusion into a personalized roadmap from career → course → college.
Smarter choices, reduced dropouts, and a better future.

**Gemini API**

We use Gemini Flash to power our Interest & Career Recommendation Engine:

Students answer a short interest test

We send their responses (skills, interests, goals) to Gemini

Gemini maps the student profile to:

Career options they are likely to enjoy

Required courses/streams for those careers

Skill gaps they may need to improve

The results are then combined with our database to suggest:

Colleges that offer those courses

Relevant exams & scholarships

Team **VoltQuana** -- [Chandni MN](https://github.com/Chandni59), [Amirthavarshini R.U](https://github.com/Amirthavarshini05), [Aravindan SG](https://github.com/ARAVINDAN855), [Arul Jothi](https://github.com/aruljothi19)

`2025-12-28`

---

### Tower Of Learning
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tower-of-learning-a939) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ansh245/TOWER-OF-LEARNING) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/PikvXzJqEN8) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20Hacks%203.0-0052CC?style=flat-square)](https://pechacks3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Adhd Friendly Learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

This project solves the problem that traditional learning systems are not designed for ADHD brains. Most education systems expect students to sit quietly and focus for long periods. But students with ADHD get distracted easily not because they are lazy, but because their brains work differently.
As a result:
Learning becomes stressful and boring.
Students lose motivation.
Their creativity and potential are ignored.
They are often misunderstood or judged unfairly.
Our system solves this by adapting learning to the student’s attention span instead of forcing attention.
Using AI and gamification, we provide:
Short, engaging lessons
Personalized learning paths
Instant rewards that boost motivation
Stress-free and enjoyable learning
In short, we turn learning from punishment into play for ADHD and neurodivergent students.

**Challenges we ran into**

The main challenge was designing a system that keeps ADHD students engaged without overwhelming them, while also delivering meaningful learning in a limited time. We solved these challenges by keeping lessons short, design minimal, AI adaptive, and by continuously testing engagement instead of forcing focus.

Team **Smocky_coderz** -- [Ashpreet Kaur](https://github.com/ashpreet11), [Aman Sinha](https://github.com/amansinha0706), [Keerti Rao](https://github.com/Keertiiiii), [Ansh GiriGoswami](https://github.com/Ansh245), Rajeev Ransingh

`2025-12-28`

---

### UniLink (College Bazzar)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/unilink-college-bazzar-0aae) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NIVION-HUB/Unilink-college-market) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://unilink-college-bazaar-nivion.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://user-images.githubusercontent.com/77540753/197020778-9bb78963-4498-43f7-9ddc-423d0c6dbbc9.mov) [![Built at](https://img.shields.io/badge/Built%20at-Technocrats%20Hackathon-0052CC?style=flat-square)](https://technocrats-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The hyperlocal campus network for student success

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**The crisis of ‘Educational resource utilization’**. *Sustainable resource sharing.*

![image](https://assets.devfolio.co/content/e4ccc77c1425461597ec44ed9ebb7292/b93eacdc-6746-42c1-aa2a-410147d3f9fd.png)
*[College Bazaar](https://unilink-college-bazaar-nivion.vercel.app/)*  is  a dedicated, sepcific market place web app connecting students within the same  college to buy, sell and rent academic essentials (Batch-specific, tools, solved  PYQs, Geometry Kit).

• Books and materials that usually lie unused get a second life with someone who    really needs them.
• between seniors and juniors, not the usual awkward distance.

• Reduces academic waste: fewer resources are left unused or in the trash.

• Promotes a campus culture of sustainability, where the resources remain within the college loop.

• They start valuing their assets more, knowing they can help someone next year.

• The reputation improves in a student-driven, self-sustaining ecosystem.

• It helps juniors score better because they get battle-tested books seniors actually succeeded with.

• Makes the campus feel more connected, helpful, and collaborative.

**Key features:**

• Id verification – sign-up is limited to valid emails or college ID card OCR.
• Smart privacy – Students can chat and negotiate without revealing their phone numbers.
•Trust score – Buyers and sellers earn “UniLink points” for successful, honest exchanges which reflect their trust value.

**Challenges we ran into**

**The Challenge:**
Designing a database schema for College Bazaar that efficiently handled "Batch-specific" filtering was complex. Since items like books are relevant only to specific semesters or streams, a standard search wasn't enough. We also had to figure out how to handle the state of a product—ensuring that once a student agrees to sell an item, it doesn't appear available to others immediately, preventing[ race conditions](https://stackoverflow.com/questions/34510/what-is-a-race-condition) where two people try to buy the same book.

**The Solution:**
I used [MongoDB's flexible schema](https://www.mongodb.com/docs/manual/core/schema-validation/) to tag items with metadata for Year, Branch, and Subject. I also implemented an "Order Status" state in the backend that temporarily locks an item during negotiation, ensuring the inventory displayed to users is always real-time and accurate.

Team **NIVION** -- [Anshika Awadhiya](https://github.com/aawadhiya79-cloud), [Bikash Patel](https://github.com/NIVION-HUB), [Arman Bhardwaj](https://github.com/arman-12-codes), [Anmol Dubey](https://github.com/mranmoldubey1-code)

`2025-12-06`

---

### Education on why privacy is needed
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/education-on-why-privacy-is-needed-944f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/oS57wZspMJw?si=gG9VEav8gs4i5CCU) [![Built at](https://img.shields.io/badge/Built%20at-Zypherpunk-0052CC?style=flat-square)](https://zypherpunk.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> It’s a right to have privacy over your affairs

![Writing](https://img.shields.io/badge/Writing-333333?style=flat-square) ![Capcut](https://img.shields.io/badge/Capcut-333333?style=flat-square) ![video editing](https://img.shields.io/badge/video%20editing-333333?style=flat-square)

**The problem it solves**

Educate the masses on why the present state of blockchain is not as secured as they think and how all data is available for all to see

**General Bounty**

Showcase I can create content for founders and tell their stories in a convincing manner

**Privacy-Focused Content & Media**

Video content educating everyone on why they need privacy transacting with crypto and the blockchain

**Privacy-Focused Content & Media**

My content educates around the importance of privacy not only for individuals but institutions also

[Edidiong Uwemedimo](https://github.com/nimrid)

`2025-12-04`

---

### YouLearn AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tubetrends-ai-4c90) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sufiyancode/youtube-agent-fe) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GIUahPbQoo8) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20This%20Fall%202025%20--%20Milestone%20Edition-0052CC?style=flat-square)](https://hackthisfall.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Generates personalized learning paths

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-333333?style=flat-square) ![YouTube Data API](https://img.shields.io/badge/YouTube%20Data%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

YouLearn AI helps learners discover the best YouTube playlists for any topic and generates a personalized step-by-step learning roadmap — saving hours of research and reducing overwhelm.

**What makes your project unique?**
- Unlike generic search or AI chat responses:
- It uses YouTube data, not random guesses
- It ranks playlists based on quality, relevance & structure
- It generates a step-by-step roadmap, not just recommendations
- It is interactive + displayed on UI, not just text

**Challenges we ran into**

- Integrating AZURE OPENAI api was quite difficult
- Guardrails adding was also kind of difficult
- Handling the Nodes and Edges and creating the Roadmap on the Frontend.

Team **Codebaseai** -- [Rohit Deokate](https://github.com/anaconda-01/), [Sufiyan Shaikh](https://github.com/sufiyancode)

`2025-11-06`

---

### Setu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/setu-7110) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Krishna9879/hack-a-sol) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/muFb-IYCvyU) [![Built at](https://img.shields.io/badge/Built%20at-Hack--a--Sol%202025-0052CC?style=flat-square)](https://hackasol-4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The Learning Bridge for Every Village

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![DynamoDB](https://img.shields.io/badge/DynamoDB-333333?style=flat-square)

**The problem it solves**

The Problem It Solves (Detailed, Clear English)

Rural regions, especially in states like Chhattisgarh, face a serious education crisis:

Over 6,800 schools have only one teacher

212 schools have no teacher at all

One teacher handles multiple classes → quality drops

When teachers are absent, learning completely stops

Families cannot provide academic support

Internet and resources are very limited

Students fall behind every year, creating a long-term learning gap

🎯 This platform is designed to ensure that “learning never stops” — even when a teacher is not present.

🚀 What People Can Use It For (Detailed Usage Explanation)
✔ 1. Continuity of Learning Without a Teacher

When there is no teacher in the school:

The AI tutor explains lessons

Students get guided learning anytime

Lessons are broken down simply

They can study independently without supervision

👉 The platform becomes a virtual teacher for rural children.

✔ 2. Instant Doubt Solving

In rural schools:

Teachers are overloaded

Students often don’t get doubt clearance

On this platform:

Students type or speak their questions

The AI immediately responds with explanations

It can give steps, examples, diagrams, and summaries

👉 No more waiting for a teacher — doubts are cleared instantly.

✔ 3. Simplified Notes and Easier Explanations

Most rural students struggle with:

Difficult textbooks

English content

Long chapters

The platform automatically:

Summarizes long notes

Explains concepts in simple English

Converts difficult text into child-friendly language

Highlights key points

👉 Self-learning becomes easy and understandable.

✔ 4. Personalized Learning Paths

Every student learns differently.
But in rural schools, one teacher cannot give personal attention.

The platform’s AI:

Analyzes the student’s speed

Detects weak areas

Suggests what to study next

Builds a daily learning plan

👉 Like having a personal coach for every child.

✔ 5. Voice-Based Learning for Younger Kids

Many rural students:

Cannot type

Struggle with English

Prefer audio learning

This platform supports:

Voice-based questions

Voice instructions

Audio explanations

Bilingual/Hinglish support

👉 Perfect for students who cannot read or type confidently.

✔ 6. Home Learning When School Is Closed

Rural schools often remain closed due to:

Rain

Festivals

Teacher leave

Government duties

This platform ensures:

👉 Education continues even when the school is closed.

Students can study from home with structured guidance.

✔ 7. Curriculum-Aligned, Localized Content

The platform provides:

State-board aligned lessons

Simple examples

Region-friendly learning style

Easy language understandable for rural kids

👉 Content truly fits the rural student’s background and educational level.

-> How It Makes Learning Easier, Safer & More Consistent
-> Easier

Very simple interface

Designed for first-time or low-tech users

Works even on low internet

Voice + multimedia support

Clear and interactive explanations

-> Safer

No ads

No irrelevant content

Child-safe environment

Secure login

Data fully encrypted

-> More Consistent

Learning continues with or without a teacher

AI gives daily personalized support

Doubts cleared instantly

Students stay on track even in teacher-absent schools

-> One-Line Summary

“This platform provides a virtual teacher for rural children — ensuring learning continues every day, even when no human teacher is available.”

**Challenges we ran into**

###  1. Slow Internet + Rural Device Optimization

Challenge:
The platform needed to work smoothly even in areas with low-speed internet (2G/3G) and on low-end smartphones.
But our initial pages were heavy, loading slowly.

How I solved it:

Reduced frontend code size

Removed unnecessary libraries

Used lightweight Alpine.js instead of heavy frameworks

Compressed images and lazy-loaded content

Enabled caching & CDN delivery

Result: Platform now loads smoothly even on weak networks.

###  2. Getting AI Models to Explain in Simple Rural-Friendly Language

Challenge:
AI models (GPT-OSS, Tongyi) were giving complex explanations.
Rural students need simple language + step-by-step clarity.

How I solved it:

Created a custom prompting format

Added constraints like:

“Explain in simple English”

“Use real-life rural examples”

“Break into small steps”

Added a post-processing filter to simplify responses

Result: AI explanations became easy, child-friendly, and highly understandable.

###  3. Making Voice Features Work Accurately with Indian Accents

Challenge:
Generic STT (speech-to-text) struggled with rural Hindi/Hinglish accents.

How I solved it:

Integrated Sarvam AI, which is optimized for Indian accents

Tuned microphone sensitivity

Used confidence-score threshold to reject incorrect transcriptions

Added a retry mechanism:
“Sorry, I didn’t hear that clearly. Please repeat slowly.”

Result: Voice detection accuracy improved drastically.

###  4. Securing Firebase Auth with AWS Backend

Challenge:
Firebase gives tokens, but AWS Lambda backend must verify each token securely.
Early attempts caused authentication failures.

How I solved it:

Implemented Firebase Admin SDK on Lambda

Added token expiry check

Used proper IAM roles to protect endpoints

Tested with multiple token scenarios

Result: Authentication became reliable and secure.

###  5. Structuring Data in DynamoDB Without Relational Joins

Challenge:
DynamoDB is NoSQL — no joins.
We had to design a structure that works for:

Notes

Progress

AI outputs

Student profiles

How I solved it:

Used single-table design

Created composite keys like UserID#NoteID

Used GSIs for fast lookups

Stored large content in S3, not the DB

Result: Fast, clean, scalable database performance.

### ⚙ 6. Handling Long AI Responses Without Lambda Timeout

Challenge:
Tongyi DeepResearch sometimes takes longer to generate long, multi-step career plans.
Lambda 15-second timeout caused failures.

How I solved it:

Added asynchronous processing

Lambda sends the task to a queue

EC2 worker processes it

User receives the result when ready

Result: No timeouts, smoother user experience.

###  7. Designing a UI Usable by First-Time Internet Users

Challenge:
Rural students often:

Don’t know English

Haven’t used learning apps

Have limited digital literacy

How I solved it:

Used big buttons, simple colors

Added voice instructions

Kept screens clean (no clutter)

Local-language labels

Child-friendly icons

Result: A clean, intuitive interface even for new users.

- Summary (1-liner for judges)

“The biggest challenges were speed, AI complexity, voice accuracy, and security — but by using lightweight frameworks, optimized prompting, Indian-language models, and AWS best practices, we overcame every hurdle.”

**Web2.0 Track**

How My Project Fits the Problem Statement

The problem statement says:

Rural Learn — The Education Continuity Platform for Remote Villages
Thousands of schools have only one or no teacher. Learning stops when teachers are absent. The goal is to build a web platform that ensures continuous learning using AI, cognitive tutoring, and simple UI/UX—especially for rural children.

Now let’s map exactly how your project solves this problem.

- 1. Teacher Shortage → Virtual AI Teacher
Problem:

Rural areas have very few teachers, and many schools have 0 teachers.

How my project solves it:

My platform acts like a virtual teacher using AI:

Students get explanations instantly

Doubts are solved anytime

Lessons are broken down simply

AI can teach, guide, and support without needing a human teacher

-> Even if no teacher is available, learning continues.

- 2. Inconsistent School Attendance → Always-On Learning
Problem:

Teacher leaves, festivals, weather, or government duties = school closed → padhai band.

How my project solves it:

The platform is web-based, so:

Students can study at home

They get daily learning plans

They can learn anytime, at their own pace

-> School band ho ya teacher absent ho — padhai kabhi nahi rukti.

- 3. Difficult Concepts → AI-Based Simple Explanations
Problem:

Rural students struggle with textbooks and English-language content.
Teacher busy hota hai, detail explain nahi kar paata.

How my project solves it:

AI simplifies chapters

Converts tough text into easy English/Hinglish

Creates summaries, examples, diagrams, steps

Gives child-friendly explanations

-> Complex topics become easy to understand.

- 4. Lack of Personalized Teaching → Adaptive Learning
Problem:

A single teacher cannot give personal attention to every child.

How my project solves it:

AI identifies weak areas

Builds personalized learning paths

Adjusts difficulty according to the student’s speed

Tracks progress automatically

-> Har baccha apne level ke hisaab se seekhta hai.

- 5. Limited Digital Skills in Rural Areas → Simple UI/UX
Problem:

Rural children and parents are not tech-savvy.

How my project solves it:

Very simple interface

Large icons, clear buttons

Minimal English

Voice instructions available

Works smoothly on low-end phones

-> Even first-time learners can easily use it.

- 6. Poor Internet Connectivity → Lightweight Platform
Problem:

Many villages have slow 3G/2G internet.

How my project solves it:

Lightweight frontend (HTML + CSS + Alpine.js)

Fast loading

Low data usage

Content caching

Works even on weak networks

-> Rural connectivity problems do not stop learning.

- 7. Need for Cognitive Assistance → AI + Voice Support
Problem:

Young students can't type or read comfortably.

How my project solves it:

Using Sarvam AI (voice) + LLMs:

Students can speak their questions

AI replies with voice or simple text

Very natural conversation experience

Supports Hindi/Hinglish

-> The platform becomes a friendly cognitive assistant.

- 8. Requirement: Web Innovation + AI + Cognitive Tutoring
How my project directly fits the theme:

Web Innovation:
Low-bandwidth optimized web app, extremely simple design

AI:
GPT-OSS + Tongyi DeepResearch for tutoring, notes, learning paths

Voice AI:
Sarvam for Indian accent STT/TTS

Cognitive Assistance:
Adaptive learning, instant doubt solving

UI/UX:
Rural-friendly, child-friendly interface

-> The project exactly matches every keyword of the problem statement.

Team **Techions** -- [krishna paridwal](https://github.com/Krishna9879), [Veer Modi](https://github.com/Veer-Modi), [Aashish Tejwani](https://github.com/Aashish-gif), [Khushi Rajput](https://github.com/KhushiRajput18007)

`2025-11-15`

---

### MARG AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/marg-ai-3ae0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://adarshsuman34.github.io/byte-busters/) [![Built at](https://img.shields.io/badge/Built%20at-Hacknauts-0052CC?style=flat-square)](https://hacknauts.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Start learning with AI, from scratch.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

The platform addresses a critical gap in career guidance for Indian students after Class 10 and 12. Specifically:

Core Problem: 87% of Indian students lack access to quality career guidance after completing Class 10 or 12, leading to decision fatigue and misinformation as they navigate post-secondary education choices.

**Challenges we ran into**

1.) Our biggest challenge was a major user privacy bug. After connecting our Supabase database, we realized that every user who visited the app could see the exact same chat history.
**The Hurdle:**
This happened because our database queries were 'public'—they fetched all chats, not just the current user's. Since we wanted to avoid a full login system for this project, we needed a way to uniquely identify each device anonymously.
**How We Got Over It:**
We solved this by creating a helper function (`getOrCreateAnonymousId`) that runs when the app first loads.
1.  This function checks the browser's `localStorage` for a unique `user_id`.
2.  If an ID doesn't exist, it generates a new UUID (`crypto.randomUUID()`) and saves it in `localStorage` for future visits.
3.  We then updated *all* our Supabase queries (`fetchChatHistory`, `createChatSession`, `deleteAllChats`) to filter the data based on this unique `user_id`.
This effectively gave every user their own private, persistent chat history without forcing them to create an account.

2.) Our most frustrating bug was a "White Screen of Death" that crashed the app. Our app worked perfectly locally, but after deploying, it was completely blank.
**The Hurdle:**
The browser console showed a cryptic error: **"Invalid hook call. Hooks can only be called inside... you might have two copies of React in the same app."** This was confusing because our `package.json` only listed React once.
**How We Got Over It:**
After debugging, we found the culprit in the `index.html` file. The AI Studio boilerplate included an `<script type="importmap">` block that was loading React from an external CDN. This was conflicting with the copy of React being loaded from our `node_modules` by Vite.
We fixed it by **completely deleting the `importmap` block from `index.html`** and then running `rm -rf node_modules package-lock.json && npm install` to ensure only one clean copy of React was used. This immediately solved the crash.


3. Our  hurdle was getting the frontend app to correctly communicate with the Supabase database. At first, our app failed to load or save any data, just showing a generic "An error occurred" message.
**Debugging the Hurdles:**
We used the browser's "Network" tab and found several problems:
1.  **401 Unauthorized Error:** Our app couldn't connect at all. We fixed this by ensuring our Supabase keys in `.env.local` were being correctly passed to the app by our `vite.config.ts` file.
2.  **Column Does Not Exist Error:** After fixing the connection, the app still failed. The console showed a `column "text" does not exist` error.
**How We Got Over It:**
We realized our code (`supabaseService.ts`) was trying to save data to columns named `text` and `image`, but our database schema (`schema.sql`) had defined them as `text_content` and `image_url`. We had to meticulously check every function (like `fetchChatHistory` and `addMessageToSession`) and align all the column names in our code to match the database schema. This taught us how important it is for the frontend and backend to use the exact same data contract.

Team **Byte busters** -- [Danish Meraj](https://github.com/Danish-labs), [Aadarsh Suman](https://github.com/adarshsuman34), [Abhishek Goswami](https://github.com/abhishekgoswammi7645-create), [Abhinay Ranjan](https://github.com/abhinay1872)

`2025-11-16`

---

### UniVerse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/universe-2389) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/starnger-1000/Uni-Verse/tree/main) [![Built at](https://img.shields.io/badge/Built%20at-Hacknauts-0052CC?style=flat-square)](https://hacknauts.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A Student-Teacher Dashboard

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OCR](https://img.shields.io/badge/OCR-333333?style=flat-square) ![Chart.js](https://img.shields.io/badge/Chart.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

🚨 The Problem UniVerse Solves

Students and teachers use too many disconnected platforms — ERP, Google Sheets, WhatsApp, notice boards, and paper registers.
This creates confusion, missed updates, and no single place to track academic progress.


---

🎯 What People Use UniVerse For

🧑‍🎓 Students

View profile, attendance, marks, activities

Get AI-based attendance proof

Track lost & found items

See performance graphs in one place


🧑‍🏫 Teachers

Upload attendance & marks photos

AI extracts roll numbers + present/absent

Manage class records easily

Update data that syncs instantly to students



---

📦 How UniVerse Makes Logistics Easier

Paperless attendance: Teacher uploads photo → AI extracts → student sees instantly

Auto marks extraction: No manual typing

One platform instead of many: No more ERP + WhatsApp + Google Sheets confusion

Real-time updates: Students get changes immediately

Transparent & organized: No disputes, no lost data



---

⭐ In One Sentence

UniVerse centralizes attendance, marks, activities, and lost & found into one smart dashboard, reducing confusion and making campus management faster and paperless.

Team **Blaze** -- [Tarandeep Singh](https://github.com/tarantanuldh), [Yuvraj Singh](https://github.com/starnger-1000), [Navneet Singh Panesar](https://github.com/-)

`2025-11-16`

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

### Laser interactive white board
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/laser-interactive-white-board-b5cb) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1Bx7FH48PTih-jgTLWv98rjakUzGLw9Cc) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/98qYrv3u6x4) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Smart Education Made Affordable.

![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![Sensors](https://img.shields.io/badge/Sensors-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Abstract

Introduction
Classrooms need better tools for interactive learning. Current whiteboards are costly and hard to use without touching. The Laser Interactive Whiteboard (LIWB) fixes this. It is a new, low-cost idea no one has built exactly like this before. It turns any wall into a smart, touch-free board.

Objectives
Our goal is to make interactive teaching easy and cheap. We want teachers to draw and control lessons with a laser. Students should join in by pointing lasers too. The full 6x4 feet board should cost just ₹1500—much less than ₹50,000 store models.

Methods/Approach/Proposed Solution
We use an ESP32 chip as the brain. It links a grid of light sensors (LDRs and photodiodes with multiplexers). These track a laser pointer like a cursor on screen. Code fixes light changes and wall bumps for over 95% accuracy (proven by t-tests and graphs). Bluetooth connects to laptops. Teachers draw notes or quizzes. Students zoom, drag, and vote with lasers.

Conclusion/Implications
LIWB makes classes fun and active. Teachers save time; students learn more. At ₹1500, schools can buy many. It logs data for reports. Future adds: AI handwriting read and moving parts. This changes education for all.

**Challenges we ran into**

One major challenge we faced while building the Laser Interactive Whiteboard was accurately detecting the laser position on the 8×10 LDR sensor matrix. Even though the sensors were directly connected, different LDRs responded slightly differently to the same light intensity, and ambient room lighting sometimes affected the readings. This made it difficult to reliably determine which sensor was actually being hit by the laser. To solve this, we implemented a calibration step where the system measures the ambient light level for each LDR at startup and stores it as a baseline value. During operation, the real-time readings are compared with this baseline to calculate the corrected brightness, allowing the system to detect the laser spot more accurately. We also added a minimum laser detection threshold so that normal light changes are ignored and only strong laser hits are detected. This calibration approach significantly improved the precision and stability of the cursor tracking on the whiteboard.

Team **Zudos** -- Ansh Aggarwal, [Raj Aryan](https://github.com/Rajaryan), [Judah Ezekiel](https://github.com/Judahezekiel)

`2026-03-07`

---

### GlassBoxAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/glassboxai-c0d6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bhartendulakhanpal-create/GlassBoxAI-project.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MB3FB0vTZkA) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Opening the Black Box of Machine Learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Many machine learning systems act as black boxes, where users receive predictions but cannot understand how the model made that decision. Our goal is to transform machine learning from a black-box process into a transparent and responsible decision-making system. Our platform provides an interactive environment where users can train, analyze, and interpret machine learning models, making AI more transparent and understandable. This helps developers, students, and organizations build trustworthy and responsible AI systems.

**Challenges we ran into**

1. optimization issues, as we were trying to train 3 ML models simultaneously, there was a little lag being experienced by us. so we worked on optimization and also lighted the UI to optimize further.
2. testing issues, as we tested our backend on different parameters, sometimes the predictions were totally random, so we tightened the code, cleaned it, removed any unnecessary addition.
3. common frontend problems, there were man problems in the making of frontend, like animations being redered twice or thrice, over crowding, integration issues, but we debugged them all.

Team **Bit.Cartel** -- [Deewakar Singh](https://github.com/DeewakarSingh), [Dilrose Hothi](https://github.com/Dilrose112), [Maninder Singh](https://github.com/immaninder)

`2026-03-08`

---

### nexus ai (learning companion)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexus-ai-learning-companion-f155) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PRIYA-7814/nexus-ai-learning-companion-) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-study-buddy--pihu781474.replit.app) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> EdTech

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Students often struggle with understanding complex topics, finding reliable study materials, and getting instant academic help. Traditional learning systems do not provide personalized guidance or real-time support. Nexus AI solves this by offering an AI-powered learning companion that explains concepts, generates study materials, and answers questions instantly. It helps students learn more efficiently, saves time searching for information, and provides personalized support anytime during their learning process.

**Challenges we ran into**

while doing backend

Team **Life hackers** -- [Pawanpreet Kaur](https://github.com/Pawan-235), [Navdeep kaur](https://github.com/navdeep313), Karanpreet Kaur, [Priya .](https://github.com/PRIYA-7814)

`2026-03-08`

---

### Voice banking - accessibility first
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/voice-banking-accessibility-first-afbe) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyanshuraj-debug/voicebanking) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://voicebanking.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Bank with your voice

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square)

**The problem it solves**

Over 40% of India's population struggles with modern banking apps — elderly users find complex UI overwhelming, rural users face literacy barriers, and non-English speakers are completely left out. Traditional banking apps are built for the tech-savvy, not for Bharat.

**Challenges we ran into**

Bugs & Technical Challenges
1. CORS Errors
Frontend and backend were running on different origins — every API call was blocked. Took time to realize CLIENT_URL env variable wasn't set correctly in production, causing all requests to fail silently.
2. File Name Case Sensitivity
Developed on Windows where LoginOtp.jsx and LoginOTP.jsx are the same. But Linux (Render's server) is case-sensitive — entire build failed at deployment. Had to hunt down every import and fix casing.
3. JWT Session Issues
Access token was expiring in 5 minutes but frontend had no refresh logic — users were getting randomly logged out. Built an auto-logout timer with session expiry detection.
4. MongoDB Connection
IP whitelist was blocking Render's dynamic IPs. Had to set 0.0.0.0/0 to allow all IPs. Also faced URI formatting issues with special characters in passwords.
5. SMS OTP — Fast2SMS Failed
Fast2SMS returned error 999 — requires ₹100 minimum recharge before API works. Mid-hackathon we had to pivot, evaluated Twilio, MSG91, Textbelt. Finally switched to Twilio for reliability.
6. Deployment Hell 😅

Railway — free tier already used
Render — first attempt failed, server folder not found
Cyclic.sh — platform not working
Glitch — started asking for card details
Finally got Render working after fixing root directory config and static file serving order

7. Environment Variables — Build Time vs Runtime
VITE_ variables are injected at build time, not runtime. Render's env variables are only available at runtime — so frontend was still hitting localhost:5000 in production. Fixed by creating client/.env.production.
8. API Route Order Bug
app.get('*') for React routing was placed before API routes — every /api/user/profile call was returning index.html instead of JSON. Classic Express middleware order issue.

Team **Stack Overlords** -- Hiten Thakur, Aditya Akash, Priyanshu Raj

`2026-03-08`

---

### AssessmMate AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/assessmmate-ai-b00b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shivamrny/AssessMateAI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BaijGrDaw84?si=BMY6DsqY0pZQB2Wl) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Al Powered Exams with Teacher Control.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![API3](https://img.shields.io/badge/API3-333333?style=flat-square)

**The problem it solves**

Traditional examination systems are often time-consuming, difficult to manage, and lack meaningful performance insights. Teachers spend significant time manually checking descriptive answers, calculating marks, and preparing results. Managing online exams for large numbers of students can also be complex, while students often receive delayed feedback on their performance.

AssessMate AI simplifies this process by introducing AI-assisted evaluation and automated exam management. Teachers can easily create and manage exams, while the platform automatically evaluates theory responses using AI and generates instant feedback.

The system also provides performance analytics and dashboards that help teachers understand student progress and identify learning gaps. This makes the evaluation process faster, more efficient, and data-driven.

**Challenges we ran into**

During the development of AssessMate AI, we faced several technical and implementation challenges.

1. AI Evaluation Accuracy
One challenge was integrating the Google Gemini API to evaluate theory answers accurately. Initially, the AI responses were inconsistent in scoring. We solved this by improving the prompt structure and evaluation criteria, ensuring the AI graded answers based on clear guidelines.

2. Authentication & Login Errors
While implementing authentication with Supabase, we encountered login errors and session issues. This was resolved by properly managing JWT tokens and authentication state in the frontend using React context.

3. Frontend-Backend Integration
Connecting the React frontend with the Node.js/Express backend required careful API handling. Some API calls failed due to incorrect request formats. We fixed this by standardizing API responses and improving error handling.

4. UI and Dashboard Bugs
There were layout issues in the analytics dashboard such as inconsistent card sizes and hover effects. These were solved using Tailwind CSS utility classes and responsive design adjustments.

These challenges helped us improve the stability, usability, and performance of the platform

**Requestly – Creative Use Challenge**

Our project AssessMate AI is submitted under the Requestly Track, as Requestly was used during development to simplify API testing and debugging.

Requestly helped us intercept, modify, and debug API requests and responses between the frontend and backend. This allowed us to quickly identify issues in API calls, test different request scenarios, and ensure smooth communication between the React frontend and Node.js backend.

By using Requestly, we were able to speed up debugging, test API behavior efficiently, and improve the overall development workflow of the platform.

Team **VictoryVerse** -- tarun tarun, Shivam Rauniyar, [Dilip Kumar](https://github.com/dilipsharma0607), Tanish Chauhan

`2026-03-08`

---

### EduNova
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/krishaksarthi-815c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/omsohom01/EN) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://edunova1.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co)

> Where Learning Meets Fun

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Whatsapp API](https://img.shields.io/badge/Whatsapp%20API-333333?style=flat-square)

**The problem it solves**

Our platform offers personalized, interactive learning for children aged 3–12 and also for high school and college students, helping working parents overcome time constraints without compromising their child’s development. Through gamified, play-based content and voice-guided navigation, kids can learn independently in a safe, engaging environment. Parents save time, reduce stress, and gain peace of mind knowing their child is meaningfully engaged. With minimal supervision required, families can enjoy more quality time together, while our platform bridges the gap between screen time and effective early education. For high school and college students, we provide them career guidance and a path to reach their career aspirations. We give these students direction for their dream careers. We give them specialized guidance tailored to only them according to their interests and expertise. We also provide the students actual industry insight of their desired career making them keep up with the professional world.

**Challenges we ran into**

RAG queries took 30+ seconds, exceeding Twilio's hard limit
Solution: Implemented async job queue with polling mechanism—respond immediately to Twilio, process in background, caller polls for result
Audio Processing Pipeline

WhatsApp Integration Challenges
Multi-Turn Conversation State

Keeping conversation context across multiple message exchanges for crop planning
Handling WhatsApp message retries (duplicate IDs)
Solution: Redis-based session storage with auto-expiration
Language Support (Hindi/English Mix)

WhatsApp media upload constraints (file size limits)
Proper multipart form-data formatting for PDF uploads
Solution: PDF generation with size optimization and chunked delivery
Rate Limiting & Quota Management

Handling API rate limits from multiple providers simultaneously
Managing quota exhaustion gracefully
Solution: Multiple API key rotation and fallback models

Team **DAZZLING DUO** -- [Ankit Karmakar](https://github.com/davy-anii), [Sohom Roy](https://github.com/omsohom01)

`2026-03-11`

---

### Campus++
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/campus-a134) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sahil-Hode/CampusPP-app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/S9yhTgmcEpM?si=VFuvBgaQCpFCj0iA) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Campus++ bridges the gap between learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Unity](https://img.shields.io/badge/Unity-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

- Lack of Personalized Learning: Students often follow generic courses without structured learning paths tailored to their skills or goals.

- Fragmented Development Tools: Coding practice, learning resources, project building, and portfolio management exist on separate platforms.

- No Real-Time Performance Insights: Institutes and students lack predictive analytics to identify performance risks early.

- Limited Career Preparation: Students struggle to build real GitHub portfolios, prepare for interviews, and improve coding skills in a unified system.
 
- Lack of AI Mentorship: Most learning platforms provide static content instead of intelligent guidance and recommendations.

**Challenges we ran into**

1. GitHub OAuth Integration
While integrating GitHub OAuth for the in-platform code IDE, the GitHub access token was not persisting after authentication, which prevented repository access and code pushes.  
Solution: Fixed the OAuth callback flow, securely stored the token using JWT/session, and added middleware to attach the token for GitHub API requests.

2. Managing Multiple AI Services
The platform uses multiple AI services (Gemini, Mistral, Sarvam AI, ElevenLabs), which initially caused latency and inconsistent responses.  
Solution: Built a centralized AI service layer with async handling and fallback logic to ensure reliable responses.

3. Real-Time Voice Interaction
Implementing real-time voice interaction for mock interviews created synchronization issues between speech input and AI responses.  
Solution: Used Socket.IO for real-time communication and integrated Sarvam AI (STT) with ElevenLabs (TTS) for smooth voice interaction.

**Best Use of Gemini API**

Use gemini-2.0-flash for all code editor features (debug, explain, run, suggest) — fastest, cheapest, 1M context.
Only use gemini-2.5-pro for heavy refactoring or full file generation.

**Best Use of ElevenLabs**

For STT → ElevenLabs doesn't do STT. Use Whisper (OpenAI) or Deepgram instead.
For TTS → ElevenLabs is the best. Use:

Model: eleven_flash_v2_5 — fastest, lowest latency, best for real-time
Model: eleven_multilingual_v2 — best quality, multiple languages

Simple rule: flash for real-time speaking, multilingual_v2 for high quality output.

**Best Hack Built with Google Antigravity**

Campus++ is an AI-powered personalized learning platform that guides students through structured learning paths with AI-generated quizzes, progress tracking, and mentor-driven feedback — helping them master skills at their own pace

Team **FusionNova** -- [Shubham Alandkar](https://github.com/ShubhamAl), [Rakesh Kumar Singh](https://github.com/rakeshsingh157), [Omkar Keni](https://github.com/Omkarkeni7), [Sahil Hode](https://github.com/Sahil-Hode)

`2026-03-08`

---

### Language Bridge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/language-bridge-51d0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Byte-Mastering-Hub/Language-Bridge) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Break Language Barriers. Connect the World

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

In today’s digital world, people communicate across different countries and cultures using platforms like WhatsApp, Instagram, Facebook Messenger, and online meeting tools such as Google Meet or Zoom. However, **language barriers often make communication difficult**. Many users receive messages in languages they do not understand, which creates confusion and slows down conversations.

For example, a user might receive a message in Spanish, Tamil, or French but may only understand Hindi or English. Normally, the user has to **copy the message, open a translation website, paste the text, and then read the translation**. This process is slow and inconvenient, especially during real-time conversations or meetings.

**Language Bridge solves this problem by providing real-time translation directly inside the browser.** The extension automatically detects the language of incoming messages and instantly shows the translated version in the user’s preferred language. This allows users to understand messages immediately without leaving the chat platform.

### How It Helps Users

* **Real-time message translation:** Messages from different languages are automatically translated directly on chat platforms.
* **No need to switch apps:** Users don’t need to copy text to external translation tools.
* **Supports Indian regional languages:** The extension prioritizes Indian languages such as Hindi, Tamil, Telugu, Marathi, Gujarati, and others, making it useful for local communication.
* **Works across multiple platforms:** Users can read translated messages on WhatsApp Web, Instagram, Facebook Messenger, and other web-based chat applications.
* **Improves global communication:** People from different countries can communicate smoothly without worrying about language differences.

### Why It Is Useful

Language Bridge makes communication **faster, easier, and more inclusive**. It helps users understand conversations in real time and removes the friction caused by language barriers. Whether for personal chats, international collaboration, or online meetings, the extension allows users to communicate confidently with anyone, regardless of language.

**Challenges we ran into**

## The Problem It Solves

In today’s connected world, people communicate across different countries and cultures using platforms such as WhatsApp, Instagram, Facebook Messenger, and online meeting tools like Google Meet or Zoom. However, **language barriers still create major challenges in communication**. Many users receive messages in languages they do not understand, which can lead to confusion, delayed responses, and misunderstandings.

For example, a user might receive a message in Spanish, Tamil, or French but may only understand Hindi or English. Normally, the user has to **copy the message, open a translation website, paste the text, and then read the translation**. This process interrupts the conversation and makes real-time communication difficult.

**Language Bridge solves this problem by providing real-time translation directly inside the browser.** The extension automatically detects the language of incoming messages and instantly displays the translated version in the user’s preferred language. This allows users to understand messages immediately without leaving the chat platform.

### How It Helps Users

* **Real-time message translation:** Messages are automatically translated as soon as they appear in the chat.
* **No need to switch apps:** Users do not need to copy and paste messages into external translation tools.
* **Supports Indian regional languages:** The extension prioritizes Indian languages such as Hindi, Tamil, Telugu, Marathi, Gujarati, and others, making communication easier within diverse communities.
* **Works across multiple platforms:** Users can translate messages directly on platforms like WhatsApp Web, Instagram, Facebook Messenger, and other web-based communication tools.
* **Improves global collaboration:** People from different countries and language backgrounds can communicate smoothly without language barriers.

### Why It Is Useful

Language Bridge makes digital communication **faster, easier, and more inclusive**. By translating messages instantly within the chat interface, it removes the friction caused by language differences. Whether for personal conversations, international teamwork, or online meetings, the extension helps users communicate confidently with anyone, regardless of the language they speak.

Team **Hackaholics** -- [Vishal Kumar](https://github.com/Vishalsharma821042), [Sumit Tak](https://github.com/Byte-Mastering-Hub), [Ayekpam Prithiviraj](https://github.com/AyekpamPrithi), [Ayush Kumar](https://github.com/Ayush-kumar1930)

`2026-03-08`

---

### SamvadXR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/samvadxr-c50b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AaryanCode69/SamVadXR_Build_India_Hack_Context_Engine.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://sam-vad-xr-build-india-hack-context-engine--aaryanupadhyay.replit.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/DI7bSyamSU8) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co)

> Don't Just Learn the Language. Live the Culture.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Virtual Reality](https://img.shields.io/badge/Virtual%20Reality-333333?style=flat-square) ![C#](https://img.shields.io/badge/C#-333333?style=flat-square) ![Unity 3D](https://img.shields.io/badge/Unity%203D-333333?style=flat-square) ![Neo4j](https://img.shields.io/badge/Neo4j-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Replit](https://img.shields.io/badge/Replit-333333?style=flat-square)

**The problem it solves**

The Problem: The "Context Gap" in Language Learning
Millions of people use apps like Duolingo or textbooks to learn a new language, yet few can hold a confident conversation in the real world. Why? Because language is not just vocabulary and grammar-it is culture, context, and behavior.
Traditional methods fail to teach the critical "unspoken" rules of communication. A negotiation in Tokyo looks entirely different from one in Tamil Nadu or New York. The gestures, the polite indirectness, and the acceptable haggling strategies are all deeply cultural nuances that flashcards simply cannot teach.
Furthermore, corporate training for employees relocating abroad is currently expensive, unscalable, and often relies on static briefings rather than practical experience. Learners are left knowing what to say, but not how, when, or why to say it, leading to anxiety and "culture shock" when they finally travel.
The Solution: Samvad XR – Culturally Aware Immersion
Samvad XR bridges this gap by transforming language learning from rote memorization into a high-fidelity "flight simulator" for cultural interaction. We provide a safe, immersive VR environment where users learn by doing, not just reading.
How we make it easier & better:
Context Over Content: Instead of isolated words, users face real-world scenarios-starting with our MVP: Negotiating with a Street Vendor.
Cultural RAG Engine: Our backend doesn't just translate text; it understands culture. We use a Retrieval-Augmented Generation (RAG) system grounded in cultural etiquette data. If you are learning Japanese, the AI vendor expects politeness and indirect refusal. If you are learning a regional Indian language, the AI understands the energetic dynamic of street bargaining.
State-Aware Interaction: We utilize a GraphDB to track the "emotional state" of the conversation (e.g., INQUIRY → HAGGLING → DEAL) that influences the vendor’s behaviour. The AI vendor has a dynamic "Happiness Score" that reacts to your price offers, your tone, and your cultural adherence, forcing you to adapt your strategy in real-time.
Scalable Corporate Training: We democratize high-level cultural sensitivity training. Companies can deploy Samvad to train teams on global business etiquette-from a boardroom in Berlin to a market in Mumbai-without hiring expensive consultants.
By simulating the friction and flow of real human interaction, Samvad ensures that when users step off the plane, they aren't just translating words-they are communicating with confidence.

**Challenges we ran into**

Challenges I ran into
1. From Stateless Chatbot to Stateful Agent (The Neo4j Pivot)
Initially, our AI interaction was stateless with a simple simple request and response. We quickly realized this broke the immersion; the vendor would "forget" if you had insulted him or made a lowball offer just 10 seconds prior. The negotiation felt hollow.

The Fix: We implemented Neo4j (GraphDB) to track the conversation's "State of Mind." We now model the interaction as a graph (e.g., OPENING → HAGGLING → ANGER or DEAL). We also track a persistent "Happiness Score" for the vendor. This allows the AI to hold a grudge or warm up to you over time, making the negotiation feel emotionally real.

2. The "Culture" Hallucination Problem
We struggled with getting the LLM to consistently adhere to specific cultural norms without hallucinating stereotypes or reverting to a generic "AI assistant" personality. Hardcoding prompts for 60+ languages was unscalable.

The Fix: We built a specialized Cultural RAG (Retrieval Augmented Generation) pipeline. Before the agent responds, it queries a vector database for specific etiquette rules relevant to the user's current scenario and target language (e.g., "In India, refusing the first price is expected"). This context is injected into Claude's system prompt dynamically, ensuring accuracy without massive context windows.

3. Indic Language Tooling Gaps
While aiming for a global product, we wanted our MVP to shine in the Indian context. We found that major global LLM providers often struggle with the nuances, accents, and code-mixing (Hinglish) typical of Indian languages in their Speech-to-Text and Text-to-Speech offerings.

The Fix: We integrated Sarvam AI, a full-stack generative AI platform optimized for Indic languages. This allowed us to support high-fidelity, native-sounding speech interaction for Hindi, Tamil, and Kannada, making the "local market" scenario feel genuinely authentic.

**Hackathon Prizes**

Building for India, Scalable for the World.
Samvad XR fits perfectly into the core mission of Build India. We are leveraging frontier intelligence (Anthropic's Claude 3.5 Sonnet) and rapid deployment infrastructure (Replit) to solve a uniquely Indian problem: linguistic diversity, outdated language learning practices along with unscalable corporate training practices.

Anthropic Integration: We push the boundaries of Agentic AI by using Claude's tool-calling to bridge the gap between a language model and a 3D spatial environment.

Replit Deployment: Our entire backend orchestration - managing the flow between Unity, Sarvam AI, and Anthropic is "vibe coded" and hosted on Replit, demonstrating how quickly complex agentic workflows can be deployed.

Lightspeed Scale: We aren't just building an app; we are building a language-agnostic framework. With one config change and some more 3D models, our "Indian Market" becomes a "French Bakery," representing a massive global opportunity born in India.

Team **Cheese Maggi** -- [Raghav Sharma](https://github.com/rs0125), [Raghav Agrawal](https://github.com/raghavvag), [Aaryan Upadhyay](https://github.com/AaryanCode69)

`2026-02-15`

---

### Knot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/knot-073a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/siddarth2810/Knot) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co)

> Tying your learnings and social media

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

The fundamental problem Knot tries to solve is simple: **share what you learn**.

As a developer, I’ve been saved countless times by useful articles shared by complete strangers on the internet. That’s why I believe more people should share their learnings, experiments, and small discoveries..

So I built Knot, a small tool that works with a custom agent to draft social-media posts from what you’re learning. The idea is to reduce the friction: capture → draft → share, all just one click away.

**Challenges we ran into**

Setting up the open claw environment and figuring it out took longer than expected. Connecting the telegram to the open claw agent

Team **lighthouse** -- [Siddarth Gundu](https://github.com/siddarth2810/)

`2026-02-15`

---

### Study synch pro
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/study-synch-pro-ce1f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ParthAggarwal16/Warriors_AMUHACKS5.0) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/umNd83PhxQM?si=LMoiBFhsUYL2whWG) [![Built at](https://img.shields.io/badge/Built%20at-AMUHACKS%205.0-0052CC?style=flat-square)](https://amuhacks-5.devfolio.co)

> AI companion that won’t let students give up

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Personalized Study Plans: Automatically creates tailored schedules and learning paths based on the student’s current performance and goals.

Time Management Made Easy: Tracks study sessions, breaks, and productivity patterns, helping students stay consistent without feeling overwhelmed.

Instant Assistance: Multi-agent bots provide on-demand explanations, concept clarifications, and step-by-step problem-solving, reducing dependency on tutors or peers.

Progress Tracking & Recovery: Monitors missed topics, identifies weak areas, and recommends focused exercises to accelerate academic recovery.

Motivation & Engagement: Encourages consistent learning with reminders, gamified progress indicators, and personalized feedback.

**Challenges we ran into**

Qdrant Integration: Initially, searches were slow and results inconsistent. Solved by properly indexing user_id fields and testing queries step-by-step.

JWT Authentication: Token handling caused unexpected logouts and CORS issues. Fixed by using HTTP-only cookies, automatic token refresh, and proper CORS setup.

Multi-Agent Coordination: Bots sometimes gave conflicting guidance. Resolved by defining clear roles and a central orchestration system.

Team **Warriors** -- Nikhil Bisht, [nikhil kumar](https://github.com/Reaper4205), PARTH AGGARWAL, kamal gupta

`2026-02-11`

---

### SkillBridge-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skillbridgeai-ddc6) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jayesh2007-JS/LogiQ_AMUHACKS5.0) [![Built at](https://img.shields.io/badge/Built%20at-AMUHACKS%205.0-0052CC?style=flat-square)](https://amuhacks-5.devfolio.co)

> Bridging education to careers with AI.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

1. Academic Learning ≠ Career Readiness

Students spend years studying, but academic performance alone does not clearly indicate which career path suits them. Grades measure subject understanding — not industry alignment, skill depth, or job market relevance.

2. Hidden Skill Gaps

Many students believe they are “ready” for a role (e.g., Data Scientist, Cybersecurity Analyst), but:
They lack core industry-required skills
They don’t know what they’re missing
There is no clear roadmap to improve
This leads to job rejections, confusion, and wasted time.

3. No Clear Academic-to-Industry Translation

Students often ask:
“What job fits my degree?”
“Am I industry-ready?”
“What should I learn next?”
There is no intelligent system that translates:
Academic profile ➜ Skill assessment ➜ Industry demand ➜ Career match.

4. Rapidly Changing Job Market

Technology and industry demands evolve quickly:
New tools emerge
Old skills become outdated
Roles shift
Students struggle to align themselves with future-ready opportunities.

**Challenges we ran into**

1. Data Collection & Standardization

One of the biggest challenges was handling diverse academic data formats (CGPA, percentages, skill descriptions, certifications). Converting unstructured user input into structured, analyzable data required careful preprocessing and normalization.

2. Career Mapping Logic

Mapping skills to suitable career roles wasn’t straightforward.
Many skills overlap across domains (e.g., Python → Data Science, AI, Backend, Automation). Designing a weighted scoring model to determine the best-fit career required experimentation and tuning.

3. Avoiding Generic Recommendations

Basic rule-based systems give common suggestions like “Software Developer” for everyone.
Creating a system that produces personalized and differentiated outputs was challenging.

4. Skill Gap Detection

Identifying what a user lacks compared to industry standards required:
Defining role-based skill benchmarks
Comparing user skill intensity vs expected level
Generating meaningful improvement suggestions

5. Market Trend Integration
Career recommendations must align with real-world demand, not just user interest.
Balancing passion vs employability vs growth trends required intelligent ranking logic.

6. Confidence Scoring Model

Designing a fair and explainable confidence score was complex.
We had to ensure:
Transparency in scoring
Logical weighting
Avoiding bias toward one domain

7. Time Constraints (Hackathon Factor)

With limited time:
Backend logic
Frontend UI
Analytics layer
Testing & debugging
All had to be built efficiently and integrated smoothly.

8. Scalability & Future Expansion
Planning architecture in a way that allows:
Resume analysis
LinkedIn integration
AI interview simulation
Without breaking the core system.

Team **LogiQ** -- [Jayesh Singh](https://github.com/Jayesh2007-JS), [Aaditi Jaiswal](https://github.com/aaditijaiswalaj-coder), [Aryan Phadke](https://github.com/Rudra-cmd-dev), [Eshika Jasti](https://github.com/eshikajasti)

`2026-02-11`

---

### PredictMarket
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/predictmarket-e047) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://colab.research.google.com/drive/1Cu9W5wxFuePnEGBU63KA-XRBqNBhMrBc?authuser=1#scrollTo=nph-r98Mqia0) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/BZ23ZW3hJK8) [![Built at](https://img.shields.io/badge/Built%20at-PayLoad'26-0052CC?style=flat-square)](https://pay-load.devfolio.co)

> Leveraging Machine Learning and Quantitative Metri

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Problem 1: Market Noise vs. Real Risk

Description: Most investors only look at price. Our model uses Rolling Volatility to quantify "hidden" risk that isn't always visible in the price alone.

Solution: We provide a "Volatility-Adjusted" view of the market.

Problem 2: Guesswork in Portfolio Diversification

Description: Investors often buy stocks that move exactly the same way, increasing their risk.

Solution: Our K-Means Clustering automatically groups stocks based on their actual behavior (Risk/Reward), helping investors find truly diverse assets.

Problem 3: Predicting Market Direction (The "Downfall" Problem)

Description: Knowing when a trend is about to reverse is the hardest part of trading.

Solution: Using Logistic Regression and Moving Average Crossovers, we provide a directional signal to warn users of potential "Death Crosses" . (Risk mitigation)

**Challenges we ran into**

1. One of the primary challenges was the steep learning curve in domain-specific data. I had to develop a deep understanding of financial indicators like the Sharpe Ratio, Alpha/Beta, and Maximum Drawdown to ensure the model’s outputs were meaningful.

2. The transition from theoretical Machine Learning concepts to practical implementation required significant iteration. 

3. Identifying the optimal architectural balance was a key challenge to keep it easy as a beginner while maintaining the analytical rigor required for a competitive quantitative environment.

4. Ensuring logic retention required a disciplined approach to documentation.

**Quantifying the Markets - Machine Learning**

My project focuses on the mathematical quantification of market risk and the application of Machine Learning to predict asset direction. I implemented financial metrics like Volatility, Sharpe Ratio, and Alpha/Beta, alongside clustering algorithms to group stocks by risk-reward profiles.

[Ariba Waseem](https://github.com/ariba786966)

`2026-02-02`

---

### PocketSage: The Student CFO
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pocketsage-the-student-cfo-8996) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/adityabindal2006/PocketSage) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co)

> Spend with a Plan, Not a Prayer

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**The Problem: **Students face the "20th-of-the-Month Crash" because small, untracked expenses (like snacks) eat up 40% of their budget without them realizing it.

What You Use It For:
**Safe-to-Spend**: Shows exactly what you can spend today (Income - Bills - Savings), not just your total balance.
**Ghost Mode:** Stops impulse buys by showing the real cost (e.g., "Buying this = Your budget 89rupees/day for remaining 27 day of February").
**Squad Pots:** A pre-paid shared wallet for trips so nobody has to ask friends for money back later.

**Challenges we ran into**

1. The "Localhost" Trap (Mobile Testing)
Hurdle: The app worked on my laptop but refused to load on my phone because localhost is isolated to the computer.
Fix: I implemented Ngrok to create a secure tunnel, allowing me to test features like "Squad Pots" on multiple mobile devices instantly.

2. Coding the Psychology (Ghost Mode)
Hurdle: A simple subtraction calculator wasn't scary enough to stop impulse buys.
Fix: I engineered a "Reality Check Algorithm" that calculates your new daily budget (e.g., "₹30/day remaining"), instantly translating a purchase into the visceral feeling of being broke.

3. The "Infinite Debt" Glitch
Hurdle: Adding debt in the Khata tab didn't lower the Safe-to-Spend balance, making users feel richer than they were.
Fix: I overhauled the backend logic to treat Pending Debt as "Already Spent Money," ensuring the dashboard immediately reflects the true financial reality.

**Fresher's Track**

PocketSage is the ultimate "Fresher's Survival Kit" for finance, designed specifically to solve the problem students face living away from home for the first time: The 20th-of-the-Month Crash.

It fits the Fresher's Track because:
Hyper-Relevant Problem Statement: It targets the unique struggle of first-time financial independence, where small, unstructured expenses (like canteen chai, photocopies, and late-night snacks) drain 40% of a student's budget unnoticed.

Fresher-Friendly Tech Stack: Instead of complex enterprise frameworks, it is built on a clean, efficient, and accessible stack (Node.js, Vanilla JS, Tailwind CSS) that demonstrates a strong grasp of core web development fundamentals.

Campus-Centric Features: With "Squad Pots" for splitting trip costs and "Ghost Mode" to stop impulse buys (by translating costs into "days of Maggi"), it gamifies financial discipline in a way that resonates instantly with the university lifestyle.

Aditya Bindal

`2026-02-01`

---

### Chart-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/chartai-b05f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/codesoumya2006/Chart-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://chart-ai-rho.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1l5aOGMNXHE?si=ywBbPL6S2O6Rb6_v) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co)

> Turn Knowledge into AI Visual Learning Flows

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Sites API](https://img.shields.io/badge/Google%20Sites%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![IndexedDB](https://img.shields.io/badge/IndexedDB-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square)

**The problem it solves**

Modern learning, planning, and idea-building workflows are fragmented and inefficient.

Most users rely on plain AI chat tools that generate long, linear text, which makes it difficult to:

**❌ Visualize complex ideas
❌ Structure information logically
❌ Retain and revisit knowledge effectively**

**⚠️ Key Challenges Users Face**

🔹 Understanding complex topics step-by-step
🔹 Converting AI responses into actionable learning paths
🔹 Revisiting, editing, or extending previous AI outputs
🔹 Visualizing dependencies and relationships between ideas

**💡 How Chart-AI Helps**

Chart-AI transforms AI responses into **interactive visual charts** instead of static text blocks.

It bridges the gap between AI intelligence and human visual thinking.

**🚀 What Users Can Do with Chart-AI**

✅ Break down complex topics into clear, structured steps
✅ Visualize learning paths, workflows, and concepts
✅ Generate AI-powered explanations, tasks, and questions
✅ Maintain full context while iterating on ideas
✅ Use their own API key for better privacy and control

🎯 Impact

**Chart-AI makes learning and planning:**

**⚡ Faster
🧠 Clearer
🎨 More engaging
📊 Visually structured**

By combining Generative AI + visual workflows, Chart-AI turns AI from a chatbot into a thinking partner.

**Challenges we ran into**

1. **React Hook Order Error**

One major issue was a React Hooks order mismatch, which caused runtime warnings and unstable UI behavior.

**How I solved it:**

Refactored components to ensure hooks were always called in a consistent order
Removed conditional hook calls
Followed React’s Rules of Hooks strictly

**Agentic AI / ML**

Chart-AI is designed as an agentic system, not a simple AI chat interface. Instead of returning static text responses, it reasons, plans, and takes actions to help users achieve learning and planning goals.

1️⃣ Goal-Oriented Intelligence

Users provide a goal (a topic, concept, or uploaded file). Chart-AI interprets this goal and autonomously:
Breaks it into structured learning steps
Identifies dependencies between concepts
Builds a complete, actionable learning flow
This behavior aligns with agentic AI’s core principle of working toward a defined objective.

2️⃣ Autonomous Planning & Decision-Making

Chart-AI independently decides:
What type of node to create (lecture, task, quiz, summary)
The order in which concepts should be learned
How different ideas relate to one another
The AI performs multi-step planning, rather than waiting for individual prompts.

3️⃣ Action-Taking AI (Not Just Text Generation)

Once reasoning is complete, Chart-AI acts by:
Creating and modifying nodes on the canvas
Generating quizzes, explanations, tasks, and summaries
Automatically organizing layouts and relationships
This makes the AI an active participant in the workflow.

4️⃣ Context Awareness via RAG

Chart-AI continuously observes the current canvas state:
Reads visible nodes
Extracts relevant context
Answers questions based on existing relationships
This allows the AI to respond contextually, a key requirement for agentic systems operating within an environment.

5️⃣ Iterative Learning & Adaptation

Chart-AI maintains continuity across interactions:
Enhances existing content instead of restarting
Refines outputs based on user edits
Evolves learning flows over time

This reflects stateful reasoning and iterative improvement, both agentic traits.

[Soumyadeep Das Adhikary](https://github.com/codesoumya2006)

`2026-02-01`

---

### LMS by TLE Terminator
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lms-by-tle-terminator-cb1a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prasoonpateldpsjkp2199-star/lms-by-tle-terminators) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/DbHakW41MMk) [![Built at](https://img.shields.io/badge/Built%20at-Base%20Indonesia%20Hackathon%202025-0052CC?style=flat-square)](https://base-indonesia-hackathon-2025.devfolio.co)

> The Student Success Engine

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Redux](https://img.shields.io/badge/Redux-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

The problem TLE Terminator: The Student Success Engine solves
LMS by TLE Terminator bridges the "Implementation Gap" in modern education—the disconnect between teaching content and students actually understanding it. It solves critical inefficiencies in online and resource-constrained learning environments:

Online teachers often feel like they are "teaching to the void" with no visibility into student engagement. Our Attention Engine acts as a digital invigilator, providing real-time feedback on student focus (gaze/head pose), enabling teachers to pivot instantly when the class zones out.

Millions of students in underfunded or rural schools learn science theoretically because they lack physical laboratories. Our Virtual STEM Ecosystem brings Physics, Chemistry, and CS labs directly into the browser, allowing students to experiment safely and practically without expensive infrastructure.

3.Eliminates "Revision Burnout" & Repetitive Doubts Students waste hours re-watching lectures for notes, and teachers answer the same doubts repeatedly. Our AI Layer solves this by:

Auto-Summarizing
Lectures: Generating instant, structured revision notes from audio.
Context-Aware
Tutoring: Handling routine doubts instantly (chatbot support)
4.Provides "360° Student Guidance"
Most platforms stop at academic content. We solve the "Directionless Student" problem by integrating Personalized Career Guidance, ensuring students don't just learn what to study, but understand why it matters for their future.

**Challenges we ran into**

Challenges we ran into
Challenges We ran into:
🔴 Problem
Initial WebRTC peer-to-peer (mesh) setup only supported 1-to-1 communication and did not scale.
High bandwidth and CPU usage with multiple participants.
Complex signaling logic and frequent sync & connection drops.
tldraw whiteboard updates were not syncing correctly, causing latency and inconsistent board states.
During deploying to production, faced issues with license limits for tldraw.
🛠 Solution
Migrated to Stream.io SFU architecture for scalable multi-user video streaming.
Optimized whiteboard sync using incremental event updates, batching, and throttling.
Reduced latency and ensured real-time board consistency across users.
Made temporary license arrangements for tldraw ,planning to build a custom whiteboard or move to open source solution in the future.
2. PDF Upload & Lecture Notes System
🔴 Problem
Broken download links, duplicate file overwrites, and inability to directly download PDFs from Cloudinary.
🛠 Solution
Implemented Multer-based upload pipeline with validation.
Used timestamp + UUID naming for uniqueness.
Uploaded PDFs in Cloudinary raw format for direct downloads.
3. Video → Audio Differentiation (Cloudinary Streams)
🔴 Problem
Incorrect audio extraction, multi-channel mismatches, transformation failures, and high streaming latency.
🛠 Solution
Used explicit Cloudinary audio transformations with fixed codecs and sampling rates.
Added format validation, retry logic, and optimized delivery endpoints.
Built a stable pipeline for AI transcription & summarization.
4. AI-Based Lecture Summarizer
🔴 Problem
Converting long lecture videos into accurate transcripts.
Handling large audio files without blocking the main application.
Preventing system slowdowns during peak uploads.
🛠 Solution
Implemented OpenAI Whisper for high-accuracy speech-to-text transcription.
Designed an asynchronous queue-based processing pipeline to handle heavy transcription jobs without blocking the server.
Used pooling and rate-limiting to manage concurrent requests and maintain system responsiveness.
5. Attention Engine
🔴 Problem
Model Accuracy vs Speed Trade-off:
High-accuracy models reduced speed, while lightweight models reduced reliability. Finding the right balance for hackathon constraints was tough.

Inconsistent Lighting Conditions
: Different lighting environments (low light, backlight, shadows) affected face detection accuracy, leading to false attention drops.

Real-Time Webcam Performance:
Processing live webcam frames caused lag and high CPU usage, especially on low-end devices. Optimizing frame rate without losing accuracy was challenging.

🛠 Solution
Reduced frame rate (processed every nth frame) and resized frames before processing and moved heavy computation to backend and used lightweight CV pipelines
Used lightweight pretrained models optimized for real-time inference and applied threshold-based attention scoring instead of complex deep models
Balanced accuracy by combining multiple simple signals (face presence + head pose)

**Base Track**

How does this project fit within the track?

LMS by TLE Terminator fits this criteria through our proprietary "Attention Engine." We utilize advanced Computer Vision techniques (OpenCV & MediaPipe) and Deep Learning models to process live video feeds in real-time. Our system performs complex face detection, gaze estimation, and head-pose analysis to quantify student focus. This demonstrates a practical, high-impact application of visual data processing and ML inference, directly aligning with the track's focus on advanced AI/ML solutions.

Team **TLE TERMINATORS** -- [Pranav Panmand](https://github.com/pranavpanmand)

`2026-01-30`

---

### eyebro
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eyebro-4fcd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/monees007/eyebro) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAG_4LJdm3Q/0utenkxcZb8wjSnuWsa-ww/edit?ui=eyJEIjp7IlQiOnsiQSI6IlBCSnpHSlM2VzlIYm5QWWsifX19&utm_content=DAG_4LJdm3Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Built at](https://img.shields.io/badge/Built%20at-HackJNU4.0-0052CC?style=flat-square)](https://hackjnu4.devfolio.co)

> AI-Powered Visual Accessibility

![ML Kit](https://img.shields.io/badge/ML%20Kit-333333?style=flat-square) ![Android SDK](https://img.shields.io/badge/Android%20SDK-333333?style=flat-square) ![AR](https://img.shields.io/badge/AR-333333?style=flat-square) ![yolov8n](https://img.shields.io/badge/yolov8n-333333?style=flat-square)

**The problem it solves**

For a visually impaired person, even a short walk across campus can feel uncertain and stressful. There might be a low-hanging branch, an unexpected step, a slippery path after rain, or a crowded corridor — things that a normal **walking stick may miss**. Because of this, many people hesitate to move around alone and often need to rely on someone else, even for simple daily tasks.

**Eyebro** tries to change that feeling. It helps users “sense” obstacles through **voice** and **vibration**, giving them a little more confidence, safety, and freedom to move on their own.

**Challenges we ran into**

# 1. The Real-Time Latency Issue
Challenge: Cloud-based LMMs (like Gemini) have a 1–4 second latency, which is insufficient for high-speed navigation. A blind user needs a reaction time of <100ms to avoid immediate hazards.

Native Solution: We utilized a Tiered Processing Pipeline in Kotlin:

Immediate Tier: ARCore Depth API runs on the GL thread, providing obstacle alerts in ~15ms.

Fast Tier: On-device ML Kit and YOLOv8 (via TFLite) run locally for object labeling without network calls.

Context Tier: Gemini is only triggered manually for "Tell me what's around me" descriptions, where 2-second latency is socially acceptable.

# 2. The "Unknown Object" Blindspot
Challenge: Standard AI models only "see" what they are trained on (e.g., a "Chair" or "Person"). They are often blind to generic hazards like glass doors, thin poles, or curb drops.

Solution: We implemented MLKit and YOLOv8n models to identify the obstacle and alert the user more accurately.

# 3. Native Performance Optimization
Challenge: Accessing raw 16-bit depth buffers at 30 FPS involves processing over 2 million pixels per second, which can easily thermal-throttle a mobile CPU.

Solution: By moving to a pure Native Kotlin Module, we achieved:

Gradle Harmonization: We aligned the Kotlin version (1.9+) and TargetSDK (34+) to ensure compatibility with ARCore 1.40+, ensuring the app leverages the latest Depth API optimizations.

Team **NeuralNavigators** -- [Harsh Soni](https://github.com/harshsoni2357), [Manish Chandra](https://github.com/monees007), [Saransh Sood](https://github.com/specbeck)

`2026-01-31`

---

### MorphUI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/morph-ui-4351) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/S1ddheshh/ravenclaw-morphui) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Gv7RL493Fy8?si=48lYVomZcA5_Pqgx) [![Built at](https://img.shields.io/badge/Built%20at-KnowCode%203.0-0052CC?style=flat-square)](https://knowcode-3.devfolio.co)

> Generative UI Layer for Accessibility.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Currently, websites are cluttered, complex, and unreadable for millions of users with cognitive disabilities (ADHD, Dyslexia) or visual impairments. MorphUI eliminates this barrier by automatically redesigning any webpage in real-time to match the user’s specific needs—removing noise, simplifying language, and adjusting visuals instantly.

**Challenges we ran into**

​CSS Conflicts: The website’s styles were breaking our UI. Fix: Used Shadow DOM to create a sealed environment for our extension.
​AI Latency: The 3-second wait felt too long. Fix: Built an Optimistic UI with skeleton loaders and caching to give instant feedback.
​Bad AI Output: Gemini sometimes returned Markdown instead of JSON. Fix: Enforced a strict JSON Schema in the system prompt.
​The "Flashbang" Effect: The original page would flash before our UI loaded. Fix: Injected a temporary opacity: 0 style via Manifest V3 for smooth transitions.
​Quota Limits: We hit API rate limits during testing. Fix: Optimized payloads by stripping unnecessary HTML (scripts/SVGs), reducing token usage by 40%.

Team **Ravenclaw** -- [Sunnyy Kadam](https://github.com/Sunnyykadam), [Subhodip Mathur](https://github.com/subhodipmathur), [Sai Bagwe](https://github.com/saibagwe), [Siddhesh Achrekar](https://github.com/S1ddheshh)

`2026-01-25`

---

### eduNext
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edunext-f4d0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Smritiii29/eduNext_Learning_Platform) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/V5MAs3MdUgw?si=08LmCyeQvliySvoM) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> Adaptive Education with Real-Time Learner Analysis

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square)

**The problem it solves**

**1. Problem It Solves**

Online learning platforms today cannot determine whether a learner is truly engaged. They rely on surface-level metrics like video completion, clicks, or quiz scores, which fail to capture:

~Loss of attention during long video sessions

~Cognitive fatigue and emotional disengagement

~Learners passively watching content without comprehension

~One-size-fits-all difficulty levels for diverse cognitive states

As a result, students often:

~Complete courses without meaningful understanding

~Experience cognitive overload or boredom

~Perform poorly in assessments despite “completing” lessons

Educators also lack objective insight into how students interact with learning material beyond final scores.

**2. What EduNext Can Be Used For**

EduNext transforms passive online learning into an adaptive, learner-aware experience.

**For Students**

~Ensures learning content adapts to their real attention and emotional state

~Reduces burnout by dynamically adjusting quiz difficulty

~Improves knowledge retention by responding to disengagement in real time

~Provides personalized learning paths instead of rigid course structures

**For Educators**

~Offers measurable insight into learner engagement during lessons

~Enables review of recorded sessions to understand learning challenges

~Helps design better instructional content based on attention trends

~Supports fairer evaluation beyond exam scores

**For Institutions & Platforms**

~Improves course effectiveness and completion quality

~Reduces drop-out rates caused by disengagement

~Enables data-driven instructional design

~Strengthens academic integrity in online learning environments

**3. How It Makes Existing Tasks Easier & Safer**

- Smarter Learning, Not More Learning

Instead of forcing learners to adapt to content, EduNext adapts content to the learner, making education more efficient and humane.

- Early Detection of Disengagement

Loss of focus, fatigue, or emotional stress is detected before it affects performance, enabling timely intervention.

- Personalized Assessments

~Quizzes dynamically adjust difficulty, preventing:

~Cognitive overload

~Frustration from overly difficult questions

~Boredom from overly simple tasks

- Privacy-First Monitoring

~Webcam and EEG usage only with explicit consent

~No biometric data shared externally

~Designed for educational analytics, not surveillance

**4. Real-World Impact**

EduNext is applicable across:

Online universities & MOOCs

Remote classrooms

Corporate training platforms

Skill-based learning portals

Research in cognitive learning analytics

By bridging the gap between human cognition and digital education, EduNext makes online learning:

More engaging

More fair

More effective

More human-centric

**5. Summary**

EduNext solves a fundamental flaw in online education: the inability to understand learner attention.
By modelling cognitive and emotional engagement in real time, it enables adaptive learning that improves outcomes for students, educators, and institutions alike.

**Challenges we ran into**

**Critical Development & Version Control Challenges:**

**Database Schema Conflicts (src/lib/database.ts):** We encountered severe merge conflicts in our core database logic, involving over 17 distinct conflict points. This happened because two major features-Advanced Teacher Admin Tools and Blob-based Media Storage-were being developed simultaneously. Merging them required a complete overhaul of the IndexedDB schema to support complex FileObject types while maintaining backward compatibility for existing user data.

**Page-Level Integration Hazards:** Major UI components like 
CourseVideo.tsx and  TeacherDashboard.tsx faced massive conflicts. The challenge was merging high-level feature sets, such as real-time webcam emotion analysis and automated grading systems, into a single stable version without breaking the intricate React state management. 

**Dependency Hell (package-lock.json):** Simultaneous package updates in both the root and backend directories led to corrupt lock files and peer dependency mismatches. We had to perform internal 'dependency surgery' using --legacy-peer-deps to restore a clean, buildable environment.

**Deep Technical & Integration Issues:**

**Blob Lifecycle Management:** One of our biggest technical "real-world" issues was managing the lifecycle of Blob URLs for offline videos. We faced memory leaks where the browser would slow down because large video objects weren't being correctly revoked from memory after use, requiring a robust cleanup strategy.
**Instructional Tracking Calibration:** Integrating the Python-based AI analyzer with the React frontend was not straightforward. We struggled with "Data Jitter," where the emotion detection would fluctuate too rapidly, forcing us to implement a smoothing algorithm to make the attention reports readable and actionable for teachers.
**Transactional Integrity in IndexedDB:** Ensuring that student progress and "Points" were updated atomically was difficult. In a local-first environment, we had to ensure that if a browser was closed mid-lesson, the student's earned rewards and attention logs were safely committed to storage before the session terminated.
**Multilingual UI Overflow:** Translating the platform into Punjabi and Hindi caused unexpected "broken layouts" because Hindi text can be up to 30% longer than English. We had to refactor our styling system to use flexible, auto-scaling containers to ensure the dashboard remained premium-looking regardless of the chosen language.
**Hardware Access Permissions:** Handling webcam permissions across different browsers for our monitoring features proved tricky. We had to build a custom "Permission Bridge" to gracefully handle cases where students might deny access or where hardware was occupied by other recording software.

**Balancing Power with Performance:** Successfully integrated real-time emotion and attention tracking within the browser while maintaining high-performance, lag-free video playback across diverse hardware and lighting conditions.

**Engineering a Reliable "Offline-First" Ecosystem:** Overcame the technical hurdles of storing massive video and material Blobs in local storage, ensuring a seamless, high-speed learning experience even without internet connectivity.

**Adaptive Multilingual Content & Design:** Implemented context-aware support for Punjabi, Hindi, and English, resolving complex UI layout shifts and ensuring educational terminology remained culturally accurate.

**Collaborative Data Integrity:** Maintained a stable, unified database schema while rapidly iterating on diverse features like multi-modal doubt resolution (voice/text) and real-time student analytics.

**System Stability & Resource Management:** Optimized memory usage to prevent browser crashes, ensuring the platform could simultaneously handle high-resolution webcam streams, heavy file assets, and live tracking logs.

Team **Debug Duo** -- [Santhoshkumar R](https://github.com/santhoshkumar1204), [Smriti Sethu Narayanan](https://github.com/Smritiii29)

`2026-01-25`

---

### Student LeaderBoard
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/student-leaderboard-9599) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AdityaMehta226/DUHacks-5.0/tree/main) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> Press 'Start' on your journey.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

- Dashboard shows the hackathon which we have added.

- Submit can allow participants to submit github link or the project folder.

- Judge can allow to judges to give score, disqualify participants. Also bulk download option makes the download of folder easier as it download the project folder for each student

- Leaderboard give the rank with graphical representation.

**Challenges we ran into**

In creating the setting panel which has feature such as

- Preview of the uploaded profile picture.

- Delete of the uploaded picture.

- Showing the initials of the name again after deleting the profile picture.

Team **Syntax Pioneers** -- [HETVI KHAKHAR](https://github.com/hetvikhakhar), [Aditya Mehta](https://github.com/AdityaMehta226), [Shrushti Thummar](https://github.com/shrushtithummar307-glitch), [Vatsal Malaviya](https://github.com/Vatsal04201)

`2026-01-25`

---

### STEM Quest: AI & Gamification
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stem-quest-ai-and-gamification-4fcb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anirmay/gamified-stem-learning) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://legendary-squirrel.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> Gamifying STEM Education with Gemini AI.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![GSAP](https://img.shields.io/badge/GSAP-333333?style=flat-square)

**The problem it solves**

STEM Quest turns boring studying into an addiction. Instead of dry textbooks, students play an RPG game where solving math and physics problems unlocks XP, levels, and badges.

It uses Google Gemini AI to look at how a student plays and automatically generates a personalized career roadmap. If a student excels at logic puzzles, the AI mentors them on how to become a Data Scientist. It's education that feels like gaming.

**Challenges we ran into**

AI Integration: Connecting the Gemini 1.5 Flash API was tricky because it had to analyze complex user data (quest history, grades) in real-time without hallucinating. I solved this by building structured "Agent" prompts that force the AI to return clean JSON data for the charts.

State Management: Keeping the XP, Levels, and Badges synced instantly across the Dashboard and Leaderboard required switching from simple local storage to a real-time MongoDB + Socket.io backend.

[Anirmay Khan](https://github.com/Anirmay)

`2026-01-24`

---

### Stress Analyser
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stress-analyser-eb17) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tejaswikasula.github.io/SressAnalyser/) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> Analyze student stress and improve daily focus

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![CSS3](https://img.shields.io/badge/CSS3-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

Students today face increasing levels of stress due to academic pressure, long screen time, irregular sleep patterns, and tight deadlines.
Most students are unaware of their stress levels until it starts affecting their focus, productivity, and mental well-being.
Existing solutions are either:
Too complex or clinical
Require paid subscriptions or wearables
Do not provide quick, actionable insights

SOLUTION:

The Student Stress & Focus Analyzer is a lightweight, web-based software application that allows students to self-assess their stress levels using daily lifestyle inputs.
🔹 How it works:
The user enters basic parameters such as:
Sleep hours
Study hours
Screen time
Mood level
Deadline pressure
The system uses a rule-based analysis algorithm to:
Calculate a stress score (0–100)
Classify stress as Low, Moderate, or High
Provide simple focus and stress-management suggestions
Results are displayed instantly using visual charts for better understanding

**Challenges we ran into**

Challenges we faced:
1.Understanding the right parameters
Identifying which daily habits (sleep, screen time, deadlines) best represent student stress without using medical data.
2.Designing a simple yet meaningful algorithm
Creating a rule-based logic that is easy to explain, fast to compute, and suitable for a short hackathon timeline.
3.User-friendly UI design
Keeping the interface clean and simple so that users can complete the analysis in less than two minutes.

[Tejaswi Reddy](https://github.com/TEJASWIKASULA)

`2026-01-25`

---

### UniScope
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/uniscope-ebf8) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://prutha006.github.io/hackathon/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MPm8-0iCMGI) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> college reviews for students by the students

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square)

**The problem it solves**

Uni Scope – Real Voices, Real Campus Insights
Uni Scope is your go-to platform for honest, firsthand reviews from students of universities . Get the real scoop on campus life – from clubs and activities, canteen and library vibes, to placements and academics. No sugarcoating, no fluff – just genuine experiences to help you decide if a university is the right fit for you. Explore, compare, and make informed choices with Uni Scope.

**Challenges we ran into**

we are the team of first year students we dont know most of any of these stuff...we took part in this hackathon bare handed and in this one day we have gained so much knowledge technical stuff...even though we had much deep and applicable idea due to less skills we couldn't apply all of this but we have come far from our boundaries and i am really proud of that we learned this all by our self and made this...

Team **Revenclaw** -- [Riddhi Dabhi](https://github.com/RiddhiDabhi), [Niral Damor](https://github.com/niraldamor125-glitch), [Prutha Makwana](https://github.com/Prutha006), [Urvashiba Gohil](https://github.com/deadinside55)

`2026-01-25`

---

### Convolve
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codura-4e12) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/beingsage/Convolve) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1uuAdsiKPwrAeBajEHQq5AFEGqNGypMjO?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-DUHacks%205.0-0052CC?style=flat-square)](https://duhacks5.devfolio.co)

> Unified Artificial Intelligence Language System

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Artificial Intelligence research is experiencing exponential growth in models, algorithms,
papers, repositories, and informal knowledge. However, the underlying epistemic substrate
remains primitive: document-centric, embedding-driven, memoryless, and largely unverifiable.
This results in fragmentation, hallucinated authority, loss of negative knowledge, and continual
reinvention.

We introduce UAILS (Unified Artificial Intelligence Language System), a graph-
native, identity-first, formally verifiable, agent-governed knowledge infrastructure for AI. In-
spired by the role of the Unified Medical Language System (UMLS) in medicine, UAILS pro-
vides stable concept identity, explicit semantics, memory dynamics, conflict preservation, and

governance mechanisms. It unifies AI knowledge across text, mathematics, code, benchmarks,
and practice, while explicitly modeling time, uncertainty, decay, and verification.
UAILS combines a relational identity layer, a typed knowledge graph, vector-based semantic
memory, memory decay and consolidation algorithms, autonomous agents with game-theoretic
incentives, formal verification hooks, and a capture-resistant governance model. This paper

presents the full system architecture, data models, algorithms, incentives, and deployment strat-
egy, positioning UAILS as foundational infrastructure for future AI research, tooling, and lan-
guage models.

Team **Akatsuki** -- [Sujal Srivastava](https://github.com/beingsage)

`2026-01-25`

---

### InterviewPrep Hub
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/devconnect-5bf1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ssyaramwar/interview-prep-hub) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Learning focused

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Students preparing for technical interviews often struggle due to scattered learning resources, unstructured study material, and difficulty in quick revision across core Computer Science subjects such as DSA, DBMS, Operating Systems, Computer Networks, and OOP.

Most available resources are spread across multiple platforms, making preparation time-consuming and confusing, especially for beginners. Additionally, long notes make last-minute revision difficult, and there is a lack of a single centralized platform that organizes interview-oriented content in a simple and structured way.

This project solves these problems by providing:

1)A single web platform for all core CS interview subjects

2)Subject-wise and topic-wise structured notes

3)Machine Learning–based automatic summaries for quick revision

4)Easy access to important concepts in one place

5)A beginner-friendly interface for efficient interview preparation

**Challenges we ran into**

While building this project, I faced several challenges:
1)Designing a proper subject-wise structure:
Initially, organizing multiple Computer Science subjects and their topics in a clean and scalable way was challenging. I resolved this by planning a clear folder structure and breaking subjects into topic-wise modules.

2)Handling large notes content:
Managing lengthy study material and displaying it in a readable format required careful UI planning. I improved this by dividing content into sections and using a clean layout.

3)Integrating Machine Learning summarization:
Connecting the ML summarization model with the backend was challenging due to text extraction from notes and API response handling. I solved this by using pre-trained NLP models and creating a separate ML service integrated through the backend.

4)Backend and frontend integration:
Ensuring smooth communication between the frontend and backend initially caused errors. This was resolved by using REST APIs and proper request–response handling.

5)Time management and learning new concepts:
Balancing development while learning new technologies was difficult at times. I overcame this by working incrementally and focusing on one feature at a time.

These challenges helped me gain a deeper understanding of full-stack development and ML integration while improving my problem-solving skills.

**AOPS**

This project fits into the Hackathon track as it is a self-initiated idea developed independently to solve a real-world problem faced by students during technical interview preparation.

The project focuses on the Education (EdTech) domain, aiming to simplify learning and revision of core Computer Science subjects such as DSA, DBMS, Operating Systems, Computer Networks, and OOP.

By providing a web-based platform with structured subject-wise notes and integrating Machine Learning–based automatic summarization, the project enhances accessibility, reduces preparation time, and improves learning efficiency.

Since the idea, design, development, and implementation are entirely student-driven and not associated with any partner organization, it aligns perfectly with the Hackathon track, which encourages innovation, problem-solving, and independent project development.

[Sushant Yaramwar](https://github.com/ssyaramwar)

`2026-01-17`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-3c90) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1BAEde3-WxMbZtcdNI9_5dvjQIncrgVOz/edit?usp=sharing&ouid=104722655459715420851&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Turning learning into a game.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

[REDDY ManiSimha](https://github.com/Manisimha14)

`2026-01-15`

---

### Multi-Language Support for Indian Holidays
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/enhancing-the-python-holidays-framework-coverage-localization-and-usability-improvements-97e6) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://1drv.ms/w/c/5CB1F0E24B1F778B/IQA51lwxNZjPQ7yF_8Jz9oW3Aa1WrQjozIOf5VdzqF-TSlo?e=2WreZY) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Diversity in Code: Indian Holiday Localization

![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

[Rajyavardhan Mangali](https://github.com/rajyavardhan26)

`2026-01-19`

---

### AuthShield (Security System Design)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-062f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1dj4GgpgxyvJ3-Ta8802zJFYzbCMduooF/edit?usp=sharing&ouid=103371561003907731569&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Security that scales with the community

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Embedded Javascript (EJS)](https://img.shields.io/badge/Embedded%20Javascript%20(EJS)-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Compromised authentication is a common attack vector – 81% of hacking-related breaches involve stolen or weak passwords​. The importance of this project lies in the fact that authentication and authorization are core requirements for any application intended for real users as protecting data and resources of an individual is crucial.

[Tyra Javed](https://github.com/tyrajaved)

`2026-01-19`

---

### QUIZORA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-f10b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1irthpM6JAqGSxkwO5mzPWFSFf155NGH1/edit?usp=sharing&ouid=101484627888784704684&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Quizora – Making Learning Fun and Competitive

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**

Traditional quiz and learning platforms often face issues such as low user engagement, limited interactivity, and high entry barriers. Many platforms display features that are not fully functional, require users to follow complex steps to join quizzes, and lack motivation mechanisms like gamification. As a result, users lose interest and participation decreases.

**Quizora **solves these problems by improving usability, reducing access barriers, and making quizzes more interactive and competitive.

**What Can People Use It For**

- Participate in **real-time quizzes** for learning and assessment
- Compete with other users through a **score-based leaderboard**
- **Join or generate quizzes** with or without a quiz code
- Access** quiz features securely through registered user accounts**
- Navigate platform features easily using a clear and** functional homepage**


**How It Makes Existing Tasks Easier**

- **Easier onboarding**: Users can join quizzes without needing a code
- **Better usability**: Clickable features guide users clearly through the platform
- **Safer access**: Login and signup ensure secure and controlled participation
- **Higher engagement:** Gamification elements motivate repeated usage
-** Improved learning:** Fast feedback and competition enhance retention

**Challenges we ran into**

**Non-functional UI elements:**
Some homepage features were not clickable. I resolved this by identifying missing navigation logic and planning proper routing.

**Limited quiz access flow:**
Quizzes required a code to join. I addressed this by designing a flexible join flow that supports both code-based and code-free access.

**Documentation and template issues:**
Proposal tables were locked and not editable. I fixed this by removing content controls and recreating editable tables.

**AOPS**

Quizora fits well into the Annual Open Source Programs (AOPS) track as it focuses on continuous and meaningful contributions to an open-source project. The proposed work involves improving core features such as usability, authentication, gamification, and quiz accessibility, which are essential for the long-term growth and sustainability of the platform.

The project requires consistent development, incremental feature additions, and proper documentation, aligning with the goals of AOPS to encourage long-term engagement with open-source communities. By enhancing existing features and adding scalable improvements, this contribution supports ongoing maintenance and future extensions of the project.

Overall, the work on Quizora aligns with the AOPS track by promoting sustained open-source development, collaboration with mentors, and building features that benefit the community beyond a short-term contribution.

[ISHIKA .](https://github.com/Ishika-codeit)

`2026-01-19`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-e900) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1ho-yMYscQA7g3CLRHQaEThxQxwXQrCxG/edit?usp=sharing&ouid=101649645339248202245&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Fast-paced quizzes that make learning competitive.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

[Soumyadip Haldar](https://github.com/0xsoumyadip)

`2026-01-19`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-20d7) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1vK-qgEQSenEf_9jt0RmHQk9akOj-wQMJzKMCKzPAsOc/edit?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Fast-paced quizzes that make learning competitive.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

[Sneha Das](https://github.com/Sneha-Das457)

`2026-01-19`

---

### exoplanet detection using machine learning
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/exoplanet-detection-using-machine-learning-68d3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://colab.research.google.com/drive/14anlt5xDQPbk_OJQT268XBv8WVp8Tye-?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> exoplanet detection

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Data Science](https://img.shields.io/badge/Data%20Science-333333?style=flat-square) ![Data Visualization](https://img.shields.io/badge/Data%20Visualization-333333?style=flat-square)

**The problem it solves**

## Applications and Impact of Machine Learning–Based Exoplanet Detection

Machine learning (ML)–based exoplanet detection transforms how astronomers identify and study planets beyond our solar system by making the process faster, more accurate, and more scalable. This approach can be used in the following ways:

### 1. Automated Analysis of Large Astronomical Datasets
Modern space missions such as **Kepler, TESS, and PLATO** generate massive volumes of light-curve data. ML models can automatically scan these datasets to identify potential exoplanet signals, eliminating the need for time-consuming manual inspection by astronomers.

### 2. Improved Detection Accuracy
ML algorithms can learn subtle patterns in stellar brightness variations, enabling them to:
- Distinguish real exoplanet transits from noise and stellar activity  
- Reduce false positives caused by eclipsing binaries or instrumental errors  
- Detect smaller and Earth-like planets that traditional methods may miss  

### 3. Faster Discovery and Candidate Validation
By prioritizing high-probability exoplanet candidates, ML systems significantly reduce the time required for follow-up observations. This allows researchers to focus telescope time and resources on the most promising targets.

### 4. Enhanced Safety and Cost Efficiency
Automated ML pipelines reduce dependence on repeated human intervention, minimizing the risk of human error in data analysis. They also lower operational costs by optimizing the use of expensive space- and ground-based telescopes.

### 5. Support for Astrobiology and Habitability Studies
Accurate detection and classification of exoplanets help scientists:
- Identify potentially habitable worlds  
- Study planetary atmospheres and orbital characteristics  
- Narrow down targets in the search for extraterrestrial life  

### 6. Democratization of Astronomical Research
ML tools make exoplanet detection more accessible to:
- Early-career researchers and students  
- Smaller research institutions without large observational facilities  
- Citizen scientists participating in open astronomy projects  

### 7. Scalability for Future Space Missions
As future missions produce even larger and more complex datasets, ML-based methods provide a scalable solution that can continuously adapt and improve with new data.

**In summary**, machine learning enables safer, faster, and more reliable exoplanet detection, accelerating scientific discovery while making advanced astronomical analysis more efficient and widely accessible.

**Challenges we ran into**

## Challenges Encountered

While implementing machine learning for exoplanet detection, several challenges were encountered that affected model performance, reliability, and overall workflow:

### 1. Data Quality and Noise
Astronomical light-curve data is often noisy due to:
- Stellar variability
- Instrumental errors
- Missing or irregular observations  
Distinguishing genuine exoplanet transit signals from noise was a major challenge.

### 2. Class Imbalance
Exoplanet datasets are highly imbalanced, with **far fewer confirmed exoplanets than non-planet signals**. This caused models to:
- Bias toward the majority (non-exoplanet) class  
- Achieve high accuracy but poor real-world detection performance  

Special handling such as resampling or metric selection was required.

### 3. False Positives
Signals from eclipsing binaries, star spots, or background objects often resemble exoplanet transits. The model initially struggled to reliably differentiate these false positives from real planetary signals.

### 4. Feature Extraction and Representation
Choosing meaningful features from raw light curves was non-trivial. Poor feature selection led to:
- Loss of important transit characteristics  
- Reduced model generalization  

Balancing handcrafted features with automated feature learning was challenging.

### 5. Model Overfitting
Some models performed exceptionally well on training data but poorly on unseen data. This highlighted the difficulty of:
- Generalizing across different stars  
- Preventing the model from memorizing noise patterns  

Regularization and validation strategies were necessary.

### 6. Limited Labeled Data
Confirmed exoplanet labels are scarce and expensive to obtain, limiting supervised learning performance. This constrained model complexity and required careful dataset splitting.

### 7. Computational Constraints
Training models on large-scale astronomical datasets required significant computational resources, especially during hyperparameter tuning and cross-validation.

### 8. Interpretability of ML Models
Complex models such as deep neural networks acted as “black boxes,” making it difficult to:
- Explain predictions to astronomers  
- Validate results scientifically  

This posed challenges for trust and adoption in scientific research.

**Overall**, these challenges required careful preprocessing, model selection, and evaluation strategies to ensure reliable and scientifically meaningful exoplanet detection results.

**AOPS**

This project applies machine learning techniques to solve an open and research-driven problem in astronomy—automated exoplanet detection—aligning well with the AOPS track’s focus on AI-based open problem solving.

[Saachi Sawant](https://github.com/SaachiSawant)

`2026-01-20`

---

### Quizora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/quizora-c927) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1dgaAvJxvgG4zq4vcn0uEA7O8K13TVnfg/edit?usp=sharing&ouid=108344735832857542790&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Real-time relay quizzes with leaderboardd learning

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Traditional quiz/assessment platforms often feel boring and slow, which reduces student participation and motivation. They also provide delayed feedback and lack interactive features like live competition and real-time progress.

**Quizora (Rapid Quiz Relay)** solves this by introducing a **fast-paced, gamified quiz environment** where learners can compete under time constraints.

People can use it for:

Traditional quiz/assessment platforms often feel boring and slow, which reduces student participation and motivation. They also provide delayed feedback and lack interactive features like live competition and real-time progress.

Quizora (Rapid Quiz Relay) solves this by introducing a fast-paced, gamified quiz environment where learners can compete under time constraints.

People can use it for:

Conducting real-time quizzes for practice or assessment

Competitive learning through leaderboards and relay mode

Quick knowledge testing with timers (reduces passive learning)

Instant feedback, improving learning speed and engagement

Organizing quiz events in clubs/communities for students

Overall, it makes learning more interactive, engaging, and efficient by turning quizzes into a game-like experience. for practice or assessment

Competitive learning through leaderboards and relay mode

Quick knowledge testing with timers (reduces passive learning)

Instant feedback, improving learning speed and engagement

Organizing quiz events in clubs/communities for students

Overall, it makes learning more interactive, engaging, and efficient by turning quizzes into a game-like experience.

**Challenges we ran into**

✅ Challenges I ran into

While working on this project, I faced a few hurdles mainly related to setup, real-time logic, and smooth UI transitions:

Project setup & dependency issues:
Initially, some packages had version conflicts and the development server didn’t run smoothly.
✅ I resolved it by carefully checking the package.json, reinstalling dependencies, clearing cache, and using the correct Node/NPM version.

Real-time leaderboard updates:
Implementing a leaderboard that updates instantly for multiple users was challenging because it requires proper real-time syncing and avoiding inconsistent score data.
✅ I handled this by structuring the backend logic cleanly, ensuring updates were atomic, and testing with multiple sessions to verify correctness.

Relay timer & quiz flow bugs:
The relay timer sometimes desynced when users moved between questions quickly or when network delay occurred.
✅ I fixed it by improving state handling, centralizing timer logic, and ensuring transitions are controlled and predictable.

UI/UX smoothness during quiz transitions:
Switching between questions felt abrupt and sometimes caused rendering glitches.
✅ I improved this by refining component states, preventing unnecessary re-renders, and adding better transition handling for a smoother experience.

These challenges helped me understand the importance of clean state management, real-time consistency, and performance optimization in interactive applications.

[Aswin Mishra](https://github.com/swin01)

`2026-01-22`

---

### Juice Shop Learning Pathway
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/juice-shop-learning-pathway-3494) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1ELLKG-hT2oG5nT8_blJvgzJpGOQUXZgh/edit?usp=sharing&ouid=103688590782983703503&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> "Guided learning path for web security"

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AngularJS](https://img.shields.io/badge/AngularJS-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

[Shaik Arifa](https://github.com/arifashaik-bot)

`2026-01-25`

---

### WallGodds
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wallgodds-d020) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1oFaMwqKgz6FMz-UW4tO1ZSS7v9qMvmbFv-UFBC-gbjs/edit?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Built by the community, for every screen.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AJAX](https://img.shields.io/badge/AJAX-333333?style=flat-square)

[Keerthi Thalluri](https://github.com/ThalluriKeerthi)

`2026-01-25`

---

### Rapid Quiz Relay
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rapid-quiz-relay-1f00) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1n8Kk3PH4AiqzCFNCenZoUqoGnspjf69c/edit?usp=sharing&ouid=108440537576417973350&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Winter%20of%20Code%205.0-0052CC?style=flat-square)](https://winter-of-code-5.devfolio.co)

> Learning at the speed of competition.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

[HARSHIT Kumar](https://github.com/harshit521)

`2026-01-25`

---

### Codeblooded
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codeblooded-4803) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1CRSA8DBKR2eY6aOHOYDl5MpTASQ9Dq5W?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Out%20Of%20Context'26-0052CC?style=flat-square)](https://out-of-context-2026.devfolio.co)

> Risk Aware Machine Learning Trading Strategy

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

For problem statement 4:
Cryptocurrency prices, especially Bitcoin, are highly volatile and change rapidly at minute-level intervals. This makes it difficult for traders, analysts, and researchers to anticipate short-term price movements or evaluate future market behavior using raw historical data alone.

This project addresses that challenge by building a machine learning model that predicts future Bitcoin prices using minute-level historical data. By applying logarithmic scaling during training, the model stabilizes large price fluctuations and learns underlying patterns more effectively, resulting in more reliable predictions.

The solution can be used to:

Forecast short-term Bitcoin price movements

Support trading and investment decision-making

Analyze market trends and volatility more systematically

Reduce the manual effort of interpreting large volumes of high-frequency price data

Overall, this system makes price prediction safer and more efficient by transforming noisy, high-variance data into a form that machine learning models can learn from more accurately.

**Challenges we ran into**

One of the main challenges in this project was handling minute-level cryptocurrency data, which is extremely large and noisy. Training machine learning models on millions of data points often caused performance issues such as slow training times and memory constraints. To overcome this, I carefully optimized feature selection and used GPU-accelerated XGBoost with efficient tree construction methods.

Another significant challenge was choosing the correct way to apply logarithmic scaling. Initially, I experimented with predicting log-returns and reconstructing prices over long time horizons. This resulted in extremely large RMSE values due to exponential error accumulation when compounding minute-level predictions. After analyzing the issue, I corrected the approach by applying log scaling only to the target price during training and performing inverse transformation once during evaluation, which stabilized the error metrics.

I also encountered multiple data-related issues, such as inconsistent column names, missing values, and non-numeric data types (e.g., string-based volume columns). These caused model training failures until I implemented automatic column detection, type conversion, and safe preprocessing steps to ensure only valid numeric features were used.

Overall, these challenges improved the robustness of the final pipeline and helped me better understand the importance of data preprocessing, metric selection, and numerical stability when working with high-frequency financial data.

Team **HelloWorld** -- Ankit Pal

`2026-01-25`

---

### Bitcoin trading strategy and predictions
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bitcoin-trading-strategy-and-predictions-b4f3) [![Built at](https://img.shields.io/badge/Built%20at-Out%20Of%20Context'26-0052CC?style=flat-square)](https://out-of-context-2026.devfolio.co)

> Bitcoin trends analysis by machine learning

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![data analysis](https://img.shields.io/badge/data%20analysis-333333?style=flat-square)

**The problem it solves**

We've built a system that takes the 'guesswork' out of Bitcoin trading. By combining cutting-edge AI (Transformers) with classic risk controls, we make trading easier through automation and safer through disciplined volatility management.

**Challenges we ran into**

Prediction Loop Bottleneck: Backtesting was too slow because the model ran every single minute. We solved this by using Batch Prediction, which processed data in chunks and significantly increased simulation speed.
Cold Start Feature Bias: Indicators like vol_30 were initially NaN at the start of the test set, causing high errors. We fixed this by calculating all features on the full dataset before splitting to ensure continuous historical context.
Flat Equity Curve: The strategy initially made zero trades because the "Triple-Confirmation Logic" was too strict. We adjusted the entry thresholds and added a signal look-back window to capture valid opportunities.
Market Regime Overfitting: To prevent the model from only working in high-price environments like 2021, we switched our target to Log Returns. This normalized the data, allowing the model to generalize across various price levels.

**Ethereum Track**

​Multi-Asset Intelligence: Our Chronos-Bolt transformer model is designed for any high-frequency data, making it perfectly suited to predict ETH/USDT or other ERC-20 tokens with high accuracy.
​DeFi Risk Management: The "Triple-Confirmation Logic" (EMA, RSI, CCI) and Volatility Filters we built are essential for protecting capital in decentralized finance (DeFi) protocols.
​Liquidity Optimization: Our system helps users avoid "Impermanent Loss" by identifying high-volatility market regimes before they occur.
​Scalable Analytics: By using AutoGluon and LoRA, we provide an institutional-grade AI layer that can be integrated into Ethereum-based trading bots or smart contract oracles.

Shivam Bhatt

`2026-01-25`

---

### GYAAN-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gyaanai-945b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AlfinAby/GYAAN-AI.git) [![Built at](https://img.shields.io/badge/Built%20at-Code%20Kalari-0052CC?style=flat-square)](https://code-kalari.devfolio.co)

> "Where AI Meets Education "

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

## 🎯 The Problem

Traditional education uses a **one-size-fits-all** approach. Teachers with 30-50 students cannot provide personalized attention, causing many students to fall behind.

**Key Issues:**
- Students struggle when foundational concepts aren't addressed
- Teachers lack time for individual skill assessments
- No real-time visibility into each student's learning gaps
- Generic assignments that don't target specific weaknesses

---

## ✨ How GYAAN-AI Solves This

GYAAN-AI uses **5 specialized AI agents** to evaluate students in Reading, Comprehension, Vocabulary, Math, and Progress — creating a **personalized learning path** for each child.

**For Teachers:**
- ✅ Automated AI-powered student assessments
- ✅ Real-time dashboards with class analytics
- ✅ Smart task suggestions based on weaknesses
- ✅ Batch student & class management

**For Students:**
- ✅ Personalized learning based on skill level
- ✅ Visual progress map showing strengths/weaknesses
- ✅ Gamified experience with XP and achievements
- ✅ Multi-language support (English, Hindi, Malayalam)

---

> **"Every student deserves a personal tutor. GYAAN-AI makes that possible at scale."**

**Challenges we ran into**

## 🔧 Challenges Faced

### 1. Real-time State Synchronization
**Problem:** Student dashboard wasn't detecting when teachers approved accounts or assigned classes.
**Solution:** Implemented force-refresh mechanism that re-reads localStorage data with visual loading feedback, ensuring students see updates instantly when clicking "Check Status".

### 2. Multi-User Authentication Conflicts
**Problem:** Git credentials were cached for a different GitHub account, blocking pushes.
**Solution:** Used Windows Credential Manager to clear cached credentials and re-authenticate with the correct account.

### 3. Building 5 Independent AI Agents
**Problem:** Each agent (Reading, Comprehension, Vocabulary, Math, Progress) needed different evaluation logic while maintaining a consistent API interface.
**Solution:** Created a `BaseAgent` class that all agents inherit from, ensuring consistent methods while allowing specialized evaluation algorithms.

### 4. Premium UI Without Overwhelming First-Time Users
**Problem:** Balancing professional aesthetics with intuitive UX — too many elements confused users.
**Solution:** Designed a step-by-step onboarding flow with a visual "Learning Journey" tracker, showing users exactly where they are in the process.

### 5. Handling Multiple User Roles
**Problem:** Teachers and students have completely different dashboards and permissions.
**Solution:** Implemented role-based routing and conditional rendering, with auto-detection from user ID prefixes (PRC = Student, PCE = Teacher).

**Ethereum Track**

## 🔗 GYAAN-AI x Ethereum

GYAAN-AI integrates Ethereum blockchain for **verifiable education credentials** and **token-based incentives**.

### Key Ethereum Features:

**🎓 Soulbound NFT Certificates**
- Student achievements minted as non-transferable NFTs
- Immutable proof of skills on-chain

**💰 Learn-to-Earn Tokens**
- Students earn ERC-20 tokens for completing tasks
- Redeemable in educational marketplace

**🔐 Wallet-Based Identity**
- Self-sovereign student data ownership
- Login with Ethereum wallet

**📊 On-Chain Progress**
- Tamper-proof academic records
- Instantly verifiable by employers/schools

> Bringing Web3 to education — making learning verifiable, rewarding, and student-owned.

Team **TECHTONIC** -- [Alfin Aby](https://github.com/AlfinAby), [Abel K Sajan](https://github.com/Student), [Jiffson Paul](https://github.com/Jiffson)

`2026-01-18`

---

### Community Champions
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/community-champions-9b07) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://v0-community-hero-system.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Eleven's%20Code%20Surge-0052CC?style=flat-square)](https://elevens-code-surge.devfolio.co)

> what if everyone knew that they are heros

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Many people perform small but meaningful positive actions in their communities, such as helping others, volunteering, or supporting social causes. However, these actions often go unnoticed, which reduces motivation and long-term community engagement.

This project solves that problem by providing a simple platform where individuals can record their good deeds, track their impact, and receive recognition through credits and hero ranks. By making everyday positive actions visible and appreciated, the system encourages consistent good behavior and helps build a more responsible and connected community.

**Challenges we ran into**

One of the main challenges was managing user identity and state without using a full authentication system. Since this was a hackathon-style project, we avoided complex login mechanisms and instead implemented a lightweight username-based identity system. Ensuring that user data, credits, and profiles updated correctly across different pages required careful state handling.

Another challenge was deployment and testing across different platforms, as some platforms had limitations when running modern web frameworks. To overcome this, the project was designed to work reliably in a local environment while ensuring the core functionality remained stable and consistent.

Team **AURA** -- [Mohammed Arafath](https://github.com/No), [Nakul SKondattu](https://github.com/Nsknakul21), [Clement G](https://github.com/Clement), [Jovin Jacob](https://github.com/Jovin)

`2026-01-15`

---

### Hostel Community
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hostel-community-cb06) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hostel-community.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Eleven's%20Code%20Surge-0052CC?style=flat-square)](https://elevens-code-surge.devfolio.co)

> By Students, For Students

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Living in a hostel isn’t just about having a room. It’s about managing daily routines, staying informed, and feeling connected to the people around you.
However, hostel life often feels unorganized and confusing:

Important updates get buried in multiple WhatsApp groups

Menus, transport details, and schedules are spread across different places

Asking for help or sharing resources is not always easy

There is no single platform that truly represents the hostel community

Hostel Community addresses these issues by bringing everything into one simple, shared digital space for hostel residents.

**Challenges we ran into**

Managing multiple features in one project was difficult at first, as the site started to feel crowded. I solved this by splitting the project into smaller sections and building each part step by step.

Navigation became tricky as more pages were added, and broken links appeared. Organizing folders properly and regularly testing links helped fix this.

Keeping the design consistent across all pages was challenging. Reusing common styles and slowly refining the layout helped maintain uniformity.

Some layouts broke on smaller screens even though they looked fine on desktop. I resolved this by debugging CSS and improving responsiveness through repeated testing

Team **SPARK** -- [DINAKAR S](https://github.com/Dina3108), [Dharamveer A](https://github.com/Dharamveer-A/), [Deva TS](https://github.com/Devats266), [Aafridi Ansari](https://github.com/Aafridi-Ansari)

`2026-01-15`

---

### CalmEd
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/calmed-c59c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jeevansridharan/Stress-app) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.youtube.com/watch?v=vepGP33XC_g) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=vepGP33XC_g) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20Space%202025-0052CC?style=flat-square)](https://hack-space-1.devfolio.co)

> Supporting students with early stress awareness AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

Engineering students often face high levels of stress due to exams, academic pressure, skill development, career uncertainty, and personal issues. Many students hesitate to share their problems openly with friends, parents, or faculty due to fear of judgment or stigma.

As a result, stress remains unaddressed and can gradually lead to anxiety, burnout, poor academic performance, and mental health issues. Existing mental health solutions are often clinical, adult-focused, or intimidating for students, making early support inaccessible.

CalmEd addresses this gap by providing a simple, student-centric, and non-clinical platform for early stress awareness and support.

**Challenges we ran into**

One of the main challenges was designing the system in an ethical and responsible way. Since mental health is a sensitive area, I had to ensure that the platform does not provide medical diagnosis or treatment.

Another challenge was deciding how to keep the application simple while still meaningful. I solved this by starting with a basic version that focuses only on mood input and immediate stress relief, and then planning future upgrades incrementally.

Balancing simplicity, usability, and privacy was a key learning experience during this project.

**Generative AI**

CalmEd follows an incremental Gen AI approach.

The current version of the platform is a simple, rule-based MVP designed to validate student needs and ensure ethical, non-clinical mental wellness support. It focuses on usability, privacy, and early stress awareness.

In the next phase, Gen AI will be integrated to enhance the system by:
- Performing sentiment analysis on student text input to understand emotional tone
- Identifying stress patterns and trends over time
- Generating personalized, context-aware stress relief suggestions
- Adapting recommendations based on user behavior and feedback

By starting simple and progressively adding intelligence, CalmEd ensures responsible and human-centered use of Gen AI while avoiding over-reliance on automation in a sensitive mental health domain.

[JEEVAN S](https://github.com/jeevansridharan)

`2026-01-01`

---

### AuraShield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aurashield-67ce) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/IshanRastogi98/Aura-Shield) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aurashield.netlify.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co)

> AI-powered emotional awareness for students

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

## The Problem

Students frequently experience stress, emotional overload, and mental fatigue due to academic pressure, uncertainty, and constant digital engagement.  
However, these emotional states are often **unstructured, unclear, and hard to recognize early**.

Most students struggle with:
- Understanding what they are feeling at a given moment  
- Identifying negative emotional patterns over time  
- Converting vague thoughts into actionable self-awareness  

Existing solutions are either:
- Too clinical or heavy to use regularly  
- Focused on crisis response rather than early awareness  
- Not designed for simple, everyday reflection  

As a result, emotional distress often remains unnoticed until it starts affecting productivity, decision-making, or overall wellbeing.

---

## How AuraShield Helps

AuraShield makes emotional self-awareness **simple, fast, and accessible** by analyzing user-written text and converting it into clear emotional insights.

People can use AuraShield to:
- Reflect on their thoughts and understand emotional signals  
- Identify stress or negative sentiment early  
- Observe simple emotional trends across multiple entries  
- Receive clear, non-clinical guidance for next steps  

By transforming unstructured thoughts into meaningful insights, AuraShield helps users become more aware of their emotional state and make informed decisions before issues escalate.

**Challenges we ran into**

## Challenges Faced & How We Overcame Them

### 1. Sudden Change in Hackathon Requirements
Initially, the hackathon required the use of AWS services. After investing time in understanding and planning around AWS, the judging criteria were changed mid-hackathon, shifting the focus to the **Kiro IDE** instead.

**How we handled it:**  
Rather than panicking or discarding progress, we adapted quickly. We reframed our work around structured planning and documentation, which aligned well with Kiro’s strengths. This shift ultimately improved the clarity and organization of our project.

---

### 2. Learning a New IDE Under Time Pressure
None of us had prior experience with Kiro. A significant portion of the early hours was spent understanding how the IDE works, especially its spec-driven and AI-assisted workflows.

**How we handled it:**  
Although the learning curve felt intimidating at first, Kiro significantly accelerated development once we understood it. Its ability to generate structured specifications, documentation, and code reduced manual effort and helped us regain momentum.

---

### 3. Tooling & Platform Confusion
At one point, the tooling workflow started generating an application-style setup instead of a simple web-based interface, which did not align with our original intent.

**How we handled it:**  
By refining prompts, adjusting project configuration, and clearly defining our scope, we were able to realign the output with our requirement of a web-based solution.

---

### Key Takeaway
The biggest challenge was not technical complexity, but **adapting to change under time constraints**. Leveraging Kiro effectively turned an initial obstacle into a productivity boost and played a key role in completing the project successfully.

**Best Innovation**

## Why AuraShield Fits the Best Innovation Track

AuraShield addresses a real and widely experienced problem: the lack of simple, accessible tools for everyday emotional self-awareness among students.

The innovation lies not in complexity, but in **how emotional awareness is made lightweight, actionable, and usable on a daily basis**. Instead of focusing on clinical diagnosis or crisis intervention, AuraShield operates in the early-awareness space — helping users recognize emotional signals before they escalate.

Key aspects of innovation include:
- Converting unstructured user-written text into clear emotional insights
- Focusing on early detection and self-reflection rather than reactive solutions
- A clean, low-friction user experience that encourages regular use
- An MVP-first design that is realistic, scalable, and easy to extend

AuraShield demonstrates how AI can be applied thoughtfully to improve wellbeing without overengineering or overclaiming. Its simplicity, clarity of purpose, and real-world applicability make it a strong fit for the Best Innovation track.

**AWS**

## Why AuraShield Fits the AWS / Kiro Track

AuraShield makes meaningful use of the Kiro IDE throughout the project lifecycle, from ideation to execution. Instead of treating Kiro as a simple coding assistant, we used it as a **spec-driven development environment** to structure our thinking, define scope, and guide implementation.

Kiro was used to:
- Clearly define the problem and MVP requirements before writing code
- Create structured planning documents outlining included and excluded features
- Design a simple, scalable system architecture aligned with the project goals
- Break the project into executable tasks and iterate efficiently
- Generate and refine documentation directly within the IDE

This approach allowed us to adapt quickly to changing hackathon requirements and maintain clarity under time pressure. The `/kiro/` folder in our repository contains the planning and documentation artifacts generated during this process, demonstrating authentic and continuous use of the Kiro platform.

AuraShield aligns strongly with the AWS / Kiro track by showcasing how structured planning, clear documentation, and AI-assisted execution can significantly improve development efficiency and project quality.

Team **AuraForge** -- [Ishan Rastogi](https://github.com/IshanRastogi98), [Aditya Gupta](https://github.com/Aditya02032006), [Hardik Agrawal](https://github.com/builders-pride), [SANKALP PRAJAPATI](https://github.com/sankalp-stack)

`2025-12-30`

---

### Smart Solution for Students
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-solution-for-students-8911) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arpi2003ta/ml) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co)

> SSS

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Proposed Solution
•Core Idea / Concept SmartEdu System v1.0 is a unified AI-powered education platform that integrates learning, assessment, analytics, mentorship, and predictive guidance to deliver personalized, adaptive, and outcome-driven exam preparation.
•Key Features The platform offers AI-driven personalized learning paths, automated CBT and OMR evaluation, advanced analytics with adaptive study plans, real-time doubt resolution, AI-based college prediction, and immersive AR, voice navigation, and secure payment features.
•How It Addresses the Challenges SmartEdu replaces generic preparation with adaptive AI roadmaps, automates evaluation and analytics, provides real-time feedback, and centralizes all learning, testing, and communication within a single intelligent system.
•Why This Solution Is Better Than Existing Ones Unlike traditional platforms, SmartEdu delivers true AI personalization, faster feedback, integrated college guidance, higher engagement, and a scalable, future-ready digital learning ecosystem.

**Challenges we ran into**

Competitor Analysis
•Direct Competitors Platforms like Unacademy, Physics Wallah, and BYJU’S offer strong content and live classes but lack deep AI personalization, adaptive analytics, real-time mentoring, and college prediction capabilities.
•Indirect Competitors Tools such as Udemy, Coursera, and Google Classroom address only partial needs like content delivery or assignment management without intelligent assessment, personalization, or exam-focused analytics.
•Competitive Advantage of SmartEdu SmartEdu uniquely integrates AI-driven personalized learning, automated testing and analytics, real-time mentoring, and college prediction into a single unified platform—capabilities not offered together by existing competitors.

Team **Ai_nut** -- [Babarinde Johnson](https://github.com/Babarinde1), [Sahil Kumar](https://github.com/samarthyaveer), [arpita nath](https://github.com/arpi2003ta)

`2025-12-30`

---

### StudyBuddy AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/studybuddy-ai-e7aa) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryanrana-dev/StudyBuddyAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/17bhsyqID0-gxJj6ssM-fKmWL_xXJFXKL_IyGqj6SnVs/edit?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co)

> Learning, tuned to you.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Embedded Javascript (EJS)](https://img.shields.io/badge/Embedded%20Javascript%20(EJS)-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

Students today don’t struggle because of lack of study material — they struggle because of too much information and too little direction.
When a student searches a topic on Google, they are flooded with links, articles, videos, and playlists, making it difficult to decide what is actually important. This often leads to confusion, wasted time, and poor learning outcomes.
Similarly, while AI tools can generate answers, they require users to write well-structured prompts. Most students don’t know how to ask the right questions, and the conversational format often includes unnecessary explanations that disrupt learning flow.
StudyBuddy AI solves this problem by filtering information intelligently.
Instead of overwhelming users, it asks for:
the topic name
the desired difficulty level
the preferred type of content

Based on this, the platform generates only the relevant study material, tailored to the student’s needs, with no extra noise.
This helps students:
save time
stay focused
avoid information overload
study more effectively for daily learning and exams

StudyBuddy AI shifts the focus from searching and deciding to actually learning.

**Challenges we ran into**

Building StudyBuddy AI involved several technical challenges, especially around integrating and stabilizing AI responses in a production-like environment.

One major challenge was using the Gemini API via direct fetch calls instead of the official SDK. Most available documentation, examples, and community resources were SDK-based, which made debugging difficult. When AI responses failed or behaved unexpectedly, there were very limited references to rely on, requiring extensive manual debugging and experimentation.

Another significant challenge was frequent rate-limit issues. During development and testing, the application hit rate limits regularly, which forced continuous optimization of both the prompt structure and the expected output format. This required multiple iterations to minimize token usage while still maintaining content quality and reliability.

The most challenging part was handling inconsistent AI responses. Even when the model returned a logically correct answer, small issues like unnecessary syntax, formatting deviations, or missing fields would break server-side parsing and cause runtime errors. To solve this, I had to:

refine the prompt to enforce stricter output rules

optimize JSON parsing and validation logic

add safeguards to prevent server crashes on partial or malformed responses

These challenges pushed me to improve my understanding of prompt engineering, error handling, and building more resilient backend systems when working with AI models.

Overall, these difficulties played a key role in shaping a more stable and optimized implementation of StudyBuddy AI.

Team **Straw Hats** -- [Aryan Rana](https://github.com/aryanrana-dev), [Abhishek Rana](https://github.com/abhiahekrana345-blip)

`2025-12-31`

---

### CogniSkills
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cogniskills-795b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AQSA0925/CogniSkills-by-Ctrl-Creators) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.notion.so/CogniSkills-Hackathon-Project-Documentation-2d9bf9f390748052bb9df6314f1f5184?source=copy_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=Pip0oUEETWI) [![Built at](https://img.shields.io/badge/Built%20at-Hackxios%202K25-0052CC?style=flat-square)](https://hackxios2k25.devfolio.co)

> Skill Gap Analysis for Students

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Students often create resumes without knowing whether they are actually ready for a specific job role. 
While many learning resources exist online, students struggle to identify which skills they are missing and what they should focus on next.

This leads to unstructured learning, confusion, and wasted time preparing for roles without a clear direction.

CogniSkills addresses this problem by analyzing a student’s resume, comparing it with role‑specific skill requirements, and clearly identifying skill gaps. 
It then provides a simple and structured learning roadmap, helping students understand exactly where they stand and how to move forward.

**Challenges we ran into**

One of the main challenges we faced was extracting meaningful and consistent text from resumes with different formats and layouts. 
Some resumes contained varied section headings and formatting, which made skill detection less straightforward.

To solve this, we focused on building a simple and reliable text-based skill matching approach and tested it with multiple resume samples to ensure consistency.

Another challenge was managing time during the hackathon while balancing development and documentation. 
Using Kiro IDE helped us overcome this by clearly defining requirements, breaking the project into structured tasks, and keeping our execution focused on core features.

Overall, these challenges helped us understand the importance of planning, testing early, and building a clear MVP.

**Best Innovation**

CogniSkills fits into the Best Innovation track by addressing a common yet overlooked problem faced by students during career preparation.

Instead of providing generic learning resources, CogniSkills analyzes a student’s resume, compares it with role‑specific skill requirements, and clearly identifies skill gaps. It then provides a structured learning roadmap, helping students focus on what truly matters for their target role.

The innovation lies in combining resume analysis with actionable, role‑based guidance in a simple and accessible way. By focusing on clarity, personalization, and structured planning, CogniSkills offers a practical solution that improves how students prepare for jobs.

**AWS**

CogniSkills fits into the AWS track through its structured planning and execution using Kiro IDE, which is a core requirement of this track.

We used Kiro IDE to plan our project before development by defining the problem statement, solution approach, system workflow, and task breakdown using Spec mode. This helped us organize frontend, backend, and documentation work efficiently during the hackathon.

All planning and prototyping documents created using Kiro are included in the dedicated /kiro folder in our public GitHub repository, serving as clear proof of Kiro usage.

By focusing on structured thinking, documentation, and execution rather than ad-hoc coding, our project aligns well with the goals of the AWS / Kiro prize track.

Team **Ctrl+Creators** -- [Aqsa Behna](https://github.com/AQSA0925), [Tarik Khan](https://github.com/Tarik025)

`2025-12-30`

---

### Finsakhi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finsakhi-3830) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sreyamnambiar/finsakhi) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/UaZWG6HOH4Y?si=vALFQ8gyXFX9FYK-) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20Hacks%203.0-0052CC?style=flat-square)](https://pechacks3.devfolio.co)

> Bridges the gap between rural and investment.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Google Cloud Platform (GCP)](https://img.shields.io/badge/Google%20Cloud%20Platform%20(GCP)-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Rural and semi-urban women lack access to financial knowledge and guidance.
Low literacy and limited digital exposure make managing money difficult.
An AI-driven, inclusive platform is needed to simplify learning and empower financial decisions.

**Challenges we ran into**

One challenge I faced while building this project was handling calculation errors when users entered incomplete or unexpected inputs. At first, this caused incorrect budget totals and app crashes. I fixed this by adding proper input validation and testing different edge cases step by step. This helped make the calculator more stable and user-friendly.

**Requestly**

To mock and test APIs in rural areas which has low connectivity and failed UPI

**ELeven Labs**

We used ElevenLabs for speech-to-text functionality so users can speak instead of typing. This helps users who are not comfortable with keyboards or have low literacy. By converting voice input into text, the app makes budgeting and learning features easier, faster, and more accessible for everyone.

**InsForge**

we applied this track in our workflow, for finding the security in the API and URL endpoints, but we were not able to login

**Gemini API**

we used this for the chatbot

Team **Radiance07** -- Narmadha J, [Nanditha Lakshmanan](https://github.com/Nanditha-006), [Sreya M Nambiar](https://github.com/sreyamnambiar), [PARVEEN BEGUM T](https://github.com/Parveen2327), Amirthaa SK

`2025-12-28`

---

### Edura - AI Powered Study & Learning Companion
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eduniverse-aipowered-learning-platform-094f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/apurvakhangal/edura) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://devdaisy.gitbook.io/edura/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8C2bL4mlK-c?si=_b_MCqyvGAyAfWyA) [![Built at](https://img.shields.io/badge/Built%20at-CodeQuest%202025-0052CC?style=flat-square)](https://codequest-2025.devfolio.co)

> Where Learning, Focus, and AI Come Together.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Translation API](https://img.shields.io/badge/Translation%20API-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![FramerMotion](https://img.shields.io/badge/FramerMotion-333333?style=flat-square)

**The problem it solves**

# **Edura – AI Powered Study & Learning Companion**

---

## **Inspiration**

Students aren’t overwhelmed by subjects — they’re overwhelmed by the *system* around studying. Notes scattered across devices, PDFs lost in downloads, AI chats spread across 10 tabs, deadlines in different apps, and a constant feeling of “I’m missing something.”

I struggled with this chaos too:
messy notes → no schedule → no revision → burnout.

What I truly needed was:

* one place to collect all materials
* an AI tutor who explains simply
* quizzes when I upload PDFs
* a planner that adapts to my deadlines
* a calm focus environment
* accessibility for dyslexia/ADHD
* and a system that understands *my learning pace*

Edura was built from this need.
A tool not just for productivity — but for **clarity**, **structure**, and **peace** in the learning journey.

---

## **What Edura Does**

**Edura is an AI-powered, all-in-one learning companion** that generates courses, explains concepts, builds schedules, tracks progress, and keeps everything organized in one space.

---

## **✨ Core Features**

### **1. Ask Anything → Get Simple AI Explanations**

A friendly tutor that breaks down any concept with step-by-step clarity.
Supports 30+ languages and simplified explanations for beginners.

---

### **2. Upload Notes/PDFs → Get Automatic Revision Material**

Edura uses AI to extract meaning from documents and instantly generates:

* MCQs
* Flashcards
* Summaries
* Concept breakdowns
* Revision packs

Perfect for tight deadlines and quick exam prep.

---

### **3. AI Course Builder (Based on Prerequisite Questions)**

Students answer a few quick prerequisite questions about their level, goals, and timeline.
Edura generates:

* Complete personalized courses
* Lesson modules
* Practice tasks
* Flashcards
* Quizzes
* Time estimates

The AI adapts content difficulty based on the learner’s background.

---

### **4. AI Roadmap Generator**

Edura can create:

* Long-term roadmaps
* Goal-based learning paths
* Skill-level based progression
* Milestones with estimated time
* Weekly targets
* Progress trackers

Roadmaps are dynamic — they adjust as the student improves.

---

### **5. Smart Study Planner (Deadline-Aware)**

Students can:

* Add their own deadlines
* OR import tasks from **Google Classroom**

Edura then generates a personalized daily schedule:

* prioritized study blocks
* estimated hours
* spread-out workload
* urgency-based planning
* integrated tasks from assignments and courses

All schedules appear in list view *and* calendar view.

---

### **6. Study Materials Hub**

A single place to store:

* PDFs
* Notes
* Summaries
* AI content
* Flashcards
* Translated versions

Organized by subject, course, or tag.

---

### **7. Immersive Focus Mode**

Focus tools include:

* Pomodoro
* Ambient audio
* Visualizers
* XP rewards
* Streak tracking
* Distraction-free UI

Helps build consistency and reduce study anxiety.

---

### **8. Study VR Rooms (FrameVR)**

Students can study together in a virtual space with:

* avatars
* voice/video chat
* collaborative screens
* WASD navigation
* whiteboard support (coming soon)

Makes learning social and fun.

---

### **9. Learning Analytics & Gamification**

Track:

* XP
* Streaks
* Subject-wise progress
* Time spent
* Module completion
* Roadmap milestones
* Study session stats

Includes charts, insights, and mastery indicators.

---

### **10. Accessibility for All Learners**

Edura supports:

* **Dyslexia mode** (OpenDyslexic fonts, spacing tweaks)
* **ADHD-friendly focus settings**
* **Colorblind themes** (protanopia, deuteranopia, tritanopia)
* **Screen-reader friendly layouts**
* **Multilingual UI**

Built to be inclusive and neurodiversity-friendly.

---

## **How We Built It**

### **Architecture**

![Edura Architecture Diagram](https://github.com/apurvakhangal/edura/blob/main/public/final_architecture.png?raw=true)

**Challenges we ran into**

## **Challenges We Faced**

### 1. Unifying many tools into one seamless experience

Combining AI tutoring, planning, quizzes, VR, analytics, and translations required careful UX flow.

### 2. PDF processing & large document optimization

Chunking, summarizing, and generating quizzes efficiently was difficult.

### 3. Deadline-aware AI schedules

Balancing workload + deadlines + urgency needed strong planning logic.

### 4. Realtime XP & streak systems

Ensuring consistency across sessions and timezones.

### 5. Accessibility that doesn’t break design

Implementing dyslexia-friendly fonts & colorblind themes with aesthetic UI.

### 6. Embedding VR into React

Optimizing FrameVR inside the app without performance issues.

---

## **Accomplishments We’re Proud Of**

* Built a **complete AI learning ecosystem**, not just a chatbot
* Generated **quizzes, flashcards, and summaries** from PDFs instantly
* Created **AI courses & roadmaps** customized to learner prerequisites
* Added **deadline-aware planning + Google Classroom import**
* Integrated a **VR study room** for collaborative sessions
* Included **full accessibility modes** for neurodiverse learners
* Designed a clean, modern, aesthetic UI
* Achieved **subject-wise analytics** and real-time XP tracking

---

## **What We Learned**

* AI is powerful when it fits real workflows, not just chat
* Accessibility isn’t an add-on — it’s essential
* Students need *fewer* tools, not more
* Real-time systems require deliberate state design
* VR surprisingly increases remote study motivation
* A clear UX flow matters more than having many features

---

## **What’s Next for Edura**

* Mobile app (React Native)
* Offline mode for notes & flashcards
* AI-generated mind maps
* Voice-based AI mentor
* Better VR collaboration tools (shared Pomodoro, whiteboards)
* Weekly planner with time distribution
* Notion/PDF export
* Smart reminders & habits
* Analytics dashboard for teachers / institutions

[apurva k](https://github.com/apurvakhangal)

`2025-11-17`

---

### StudentX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/studentx-866f) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://patio-zipper-53334405.figma.site/) [![Built at](https://img.shields.io/badge/Built%20at-CodeQuest%202025-0052CC?style=flat-square)](https://codequest-2025.devfolio.co)

> Career Planner

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

Saves time and eliminates confusion

**Challenges we ran into**

I'm a FYE with no prior experiences. just exploring :)

[Jatin Choudhary](https://github.com/JatinChoudhary-07)

`2025-12-22`

---

### aws
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aws-fa54) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](http://9879574441jash.s3-website.eu-north-1.amazonaws.com) [![Built at](https://img.shields.io/badge/Built%20at-WinterSpark-0052CC?style=flat-square)](https://winterspark.devfolio.co)

> learning about devops using lambda, s3, api keys

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-333333?style=flat-square)

[KHUSHIL RUPAREL](https://github.com/KhushilKR15)

`2025-12-21`

---

### Donor Discovery for Ethiopian Community in Seattle
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/donor-discovery-for-ethiopian-community-in-seattle-9b70) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/QwTWpT2meCE?si=_IWtf2jZFQc-NEki) [![Built at](https://img.shields.io/badge/Built%20at-Mahiber%20Connect%20Hackathon-0052CC?style=flat-square)](https://mahiber-connect-hackathon.devfolio.co)

> Unlock opportunities & expand programs for ECS

![excel](https://img.shields.io/badge/excel-333333?style=flat-square)

**The problem it solves**

**Join the ECS Donor Discovery Team**
Help Build a Stronger Future for the Ethiopian Community in Seattle
ECS is entering an exciting new chapter—one focused on growth, sustainability, and expanding our impact in the Ethiopian community across Seattle. To achieve this, we are forming a special volunteer team that will help identify the private and institutional partners who can invest in our vision.
We are inviting passionate community members, leaders, and friends of ECS to join us in shaping the next stage of our organization’s journey.

**Why This Work Matters**
For decades, ECS has been sustained by community donations, partnerships with public agencies, and
the strength of our members. As our programs grow, so do the needs of our community—from youth
empowerment and cultural preservation to housing stability and community wellness.
To meet this moment, we must build a more diverse and sustainable base of supporters.
This is where you come in.
By helping identify major donors—from generous individuals to foundations and
corporations—you will be directly contributing to the long-term strength and resilience of ECS. Your
work will help unlock opportunities, expand programs, and uplift generations to come.
**What Volunteers Will Do**
As part of this team, you will:

- Explore and research potential donors whose values align with ECS’s mission
- Help classify and prioritize prospects across our key program areas
- Contribute to a fundraising roadmap that will guide donor outreach and engagement
- Work alongside other passionate volunteers and receive regular support from the Executive Director
- Your insights, connections, and curiosity will help uncover partnerships that can transform our community.

**What We Will Provide**

- ECS will give volunteers the tools and guidance needed to succeed, including:
- A clear overview of ECS’s priorities and three-year strategic vision
- Training and support in how to identify and evaluate donors
- Regular check-ins with leadership for strategy and collaboration
- You do not need fundraising experience—only a willingness to learn and a passion for uplifting your community.

**The Impact You Will Create**
By the end of this project, the team will produce a prioritized list of donor prospects across:

- Private Donors (individuals and families)
- Foundations
- Corporations

This list will become a cornerstone of ECS’s development strategy and a foundation for meaningful new
partnerships.

✨ Be Part of ECS’s Future
This is a unique opportunity to contribute your time, your voice, and your heart to an effort that strengthens our entire community. Together, we can build a sustainable future—one where ECS thrives and continues to serve as a home for connection, culture, and community support.
If you are ready to make a lasting impact, we welcome you to join us.
Your leadership today will help shape ECS for generations.

Betty Zelealem

`2025-11-22`

---

### EduPortal
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/eduportal-5975) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prince04kumar/technohack) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/YBNxy3doMNU) [![Built at](https://img.shields.io/badge/Built%20at-Technocrats%20Hackathon-0052CC?style=flat-square)](https://technocrats-hackathon.devfolio.co)

> Your all-in-one student portal

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

In today’s **fast-paced academic** environment, students often struggle to access personalized study resources and essential college information in one unified place. To solve this challenge, we developed a Retrieval-Augmented Generation **(RAG)–powered learning** platform designed specifically for our college ecosystem. This system acts as an intelligent academic companion, enabling students to learn in a personalized and efficient manner.

Our platform integrates **AI-driven study assistance, **centralized access to college documents, departmental resources, announcements, syllabus, and academic materials, all within a single interface. By combining retrieval-based search with **generative AI**, the system delivers precise, context-aware answers tailored to each student’s needs—whether they are preparing for exams, exploring subjects, or looking for college-related information.

This project not only **enhances the learning experience** but also reduces the friction students face when navigating scattered resources. Ultimately, it creates a ***smarter, more connected, and more accessible academic environment*** for every learner.

**Challenges we ran into**

**Challenges We Faced**
**1. Data Collection & Standardization**

College resources were scattered across PDFs, websites, notices, and departmental drives.
The biggest challenge was collecting, cleaning, and structuring this unorganized content so it could be indexed effectively for retrieval.

**2. Inconsistent Document Formats**

We encountered multiple formats—handwritten notices, scanned PDFs, outdated documents—leading to:

OCR accuracy issues

Misread text

Difficulty extracting structured information

**3. Building an Effective Retrieval Pipeline**

Creating a system that can fetch the most relevant content from thousands of documents was difficult.
We had to optimize:

Embeddings

Chunking strategies

Vector store design

Search accuracy

**4. Ensuring Response Accuracy
**
RAG systems sometimes generate irrelevant or partially correct answers.
We had to fine-tune prompts, improve filtering, and enhance retrieval quality to ensure the AI gives precise, context-aware answers to students.

**5. Handling Domain-Specific Academic Queries**

Students ask highly technical and subject-specific questions.
It was challenging to make the system consistently understand and respond accurately across different subjects and departments.

**6. Keeping the Information Updated**

College information changes frequently—timetables, notices, exam schedules.
Ensuring the system always reflects the latest data required robust update pipelines.

**7. Scalability & Performance**

The platform must support many students accessing it simultaneously.
We had to optimize latency, manage vector DB sizes, and ensure smooth performance even as data grew.

**8. Privacy & Access Control**

Some documents are restricted to certain student groups or departments.
Designing a permission system to ensure secure and role-based access was a major challenge.

**9. User Experience & Adoption**

Students expect simple, fast, and intuitive interfaces.
We faced challenges in designing a UI/UX that works for:

Quick queries

Long study sessions

Document browsing

Personalized learning paths

**10. Integrating Personalization**

To tailor content for each student, we had to work with:

User profiles

Learning patterns

Past interactions

Course preferences

Personalization without compromising speed or accuracy was a major technical challenge.

**Duality AI Track**

**How Our Project Fits Into the Duality AI Track**

Our project perfectly aligns with the Duality AI Track because it combines retrieval + generation (RAG) to solve a real student problem. It uses AI to deliver personalized learning, accurate answers, and centralized access to college information. The system demonstrates practical AI engineering, reduces hallucinations with verified retrieval, and has clear potential to scale across departments and institutions.

Team **cookerrors** -- [Prince Kumar](https://github.com/prince04kumar), [Aarya Khare](https://github.com/aaryakhare)

`2025-12-06`

---

### Hamro Community
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/hamro-community-7ec8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rockyffgod/Hamro-community) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%20School%20Edition-0052CC?style=flat-square)](https://deerhack-school-edition-1.devfolio.co)

> We are Special

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Spline](https://img.shields.io/badge/Spline-333333?style=flat-square)

**The problem it solves**

it is a website for the real ones in our community.
it helps the people from every block in the town to access benefits of being in a community

Team **Infinity Tech Warriors** -- Roshan Tamang

`2025-12-06`

---

### Community Connectivity
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/community-connectivity-934f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/K4us4i/HorizonX.git) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%20School%20Edition-0052CC?style=flat-square)](https://deerhack-school-edition-1.devfolio.co)

> Helpfulness

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square)

**The problem it solves**

It provides local events, disaster news.

Team **HorizonX** -- [Khushi Khatri](https://github.com/K4us4i)

`2025-12-06`

---

### ArthaGuide
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gvjvhhjvvhjv-24e7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dollaransh17/Artha_Guide_Code_Red_with_Rag_VectorDB) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/wj-YyH70sCc) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20This%20Fall%202025%20--%20Milestone%20Edition-0052CC?style=flat-square)](https://hackthisfall.devfolio.co)

> Your money. Your language. Your guide

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

ArthaGuide is an all-in-one financial assistant designed specifically for India’s 77 million gig workers. It helps users track their money effortlessly, understand their financial health, and access loans safely — all in English, Hindi, and Kannada.

At its core, ArthaGuide solves the biggest gap in the gig economy:
gig workers earn daily, but have no tools to manage irregular income, no access to regional-language financial advice, and face frequent loan rejections due to non-traditional earnings.

ArthaGuide brings everything into one simple platform:

SMS-powered auto-tracking: Paste any bank SMS → it becomes a categorized transaction instantly.

Smart Dashboard: Real-time financial health score, charts, insights, and spending patterns.

Multilingual AI Loan Advisor: Personalized loan guidance and financial advice in 3 languages.

Micro-loan Marketplace: Compare 5+ lenders with instant eligibility scoring and EMI calculations.

WhatsApp Bot Demo: A familiar chat interface for quick actions like adding expenses or checking balance.

With a clean UI, regional language support, and AI-powered insights,
ArthaGuide empowers gig workers to understand, manage, and improve their financial life — one SMS at a time.

**Challenges we ran into**

1. Accurate SMS Parsing Across 20+ Banking Formats

Bank SMS messages have no fixed structure — some use “INR”, some use “Rs”, some use “₹”, and dates vary across formats like DD-MM-YYYY, YYYY/MM/DD, etc.
This caused early failures where the parser would detect the wrong amount or skip transactions entirely.

How I solved it:

Built a regex-based multi-pattern parser

Normalized currency symbols

Added fallbacks for unknown patterns

Tested with 50+ real SMS samples

2. Making the Dashboard Update Instantly

When a new transaction was added, the charts (donut + bar) weren’t updating automatically due to React state timing issues.

Fix:

Centralized all financial data in a single state store

Triggered chart updates via useEffect watchers

Ensured transactions, balance, and score recompute in one pipeline

3. Multilingual Support Without Breaking the UI

Switching languages (especially Hindi/Kannada) increased text length and caused
UI breaks — buttons overlapped, chart labels overflowed.

Fix:

Implemented react-i18next with auto-resize

Added dynamic font scaling

Used flexible Tailwind classes (min-w, flex-wrap)

4. Loan Eligibility Engine Miscalculations

Our eligibility score depends on income, expenses, and savings.
Initially, minor changes in input caused huge jumps in score.

Fix:

Redesigned scoring formula

Introduced caps and smoothing functions

Created test cases for multiple financial profiles

Team **Hackistanis** -- [Gaurav Durge](https://github.com/gauravdurge-2332), [Anshul Vaibhav](https://github.com/dollaransh17), [Shreyas Naik](https://github.com/shreyasNaik0101)

`2025-11-30`

---

### Career Crest
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/career-crest-1c1d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aviisharma238/Career-Crest.git) [![Built at](https://img.shields.io/badge/Built%20at-HackBIOS%202K25-0052CC?style=flat-square)](https://hackbios2k25.devfolio.co)

> AI Career &Student Guidance System

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square)

**The problem it solves**

# CareerCrest – Personalized Career & Exam Guidance Platform

## The Problem It Solves

Students and career seekers often face challenges like:

- **Information Overload:** Finding accurate, up-to-date info on exams, deadlines, scholarships, and careers is difficult.  
- **Generic Guidance:** Most platforms provide one-size-fits-all advice without considering individual goals or streams.  
- **Inefficient Planning:** Without a clear roadmap, planning a career path or exam preparation can be overwhelming.  
- **Skill Gaps:** Students may not know which skills they need to focus on to succeed in their desired field.  
- **Scattered Resources:** Career advice, exam prep, and scholarship info are often fragmented across multiple websites.

## How CareerCrest Helps

- **Personalized Roadmaps:** Generates customized guidance for exams, careers, and skill-building.  
- **Centralized Platform:** Combines career advice, exam info, scholarships, and prep resources in one place.  
- **Time-Saving:** Reduces the need to search multiple sources or consult several mentors.  
- **Skill Gap Analysis:** Highlights areas for improvement before exams or applications.  
- **Real-Time Alerts:** Keeps users updated with deadlines, exam dates, and new opportunities.

## Use Cases

- Students looking for guidance on exams relevant to their stream.  
- Career seekers wanting a step-by-step roadmap to achieve their goals.  
- Individuals who want to track skill gaps and improve employability.  
- Users who need a single platform for exam schedules, scholarship info, and practice resources.

---

> CareerCrest makes career planning simple, personalized, and efficient!

**Challenges we ran into**

## Challenges I Ran Into

While building CareerCrest, I faced several challenges:  

1. **Integrating Firebase Authentication & Firestore**  
   - **Problem:** Setting up secure login and database rules to ensure users could only access their own data was tricky at first.  
   - **Solution:** I carefully studied Firebase security rules, tested different scenarios, and implemented rules that restrict access based on `request.auth.uid`.  

2. **Generating Personalized Roadmaps**  
   - **Problem:** Creating a system that gives tailored recommendations based on multiple user inputs was complex.  
   - **Solution:** I implemented a step-by-step logic flow that evaluates a student’s stream, skill level, and goals, and returns the most relevant exams, career options, and skill suggestions.  

3. **Handling Dynamic Data Updates**  
   - **Problem:** Keeping exam dates, scholarship info, and other resources up-to-date in real-time was challenging.  
   - **Solution:** I integrated Firestore’s real-time listeners and periodic data fetches to ensure users always see the latest info.  

4. **UI/UX Consistency**  
   - **Problem:** Ensuring the app was responsive and looked polished across devices required extra effort.  
   - **Solution:** I used Tailwind CSS with responsive design utilities and tested on multiple screen sizes to maintain a clean, user-friendly interface.  

> Each challenge taught me valuable lessons in full-stack development, real-time data handling, and building secure, user-focused applications.

Team **TechShastra** -- [Ayush Sharma](https://github.com/aviisharma238), [Ankita Mishra](https://github.com/ankitamishra1404), [manas gupta](https://github.com/Manas-gupta-04), [Deeksha Sahu](https://github.com/Deeksha131)

`2025-11-18`

---

### EduJusticeAi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edujusticeai-ed89) [![Built at](https://img.shields.io/badge/Built%20at-Hacknauts-0052CC?style=flat-square)](https://hacknauts.devfolio.co)

> AI-Powered Support for Student Justice.

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![XML](https://img.shields.io/badge/XML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

Students often face bullying, harassment, discrimination, or unsafe situations in and around educational institutions but hesitate to report due to fear, stigma, or confusion about process. When they do report, details are fragmented across chats, calls, and images with no standardized evidence, causing delays or dismissal. Many campuses lack accessible, always-available guidance or safe spaces to speak, and existing systems require internet, multiple apps, or manual steps—leading to under-reporting, poor follow-up, and limited accountability.

**Challenges we ran into**

EduJustice provides a single, student-friendly app to capture, analyze, and submit complaints quickly and safely. It lets students:

Speak to an AI Assistant for empathetic guidance, grounding steps, and next actions.
Record a voice complaint that is transcribed and emotion-checked to capture context clearly.
Scan or upload images; the app extracts text (OCR) and flags severity to standardize evidence.
Submit reports to Firestore with optional anonymity; profile details auto-fill to reduce friction.
Use a simple Firestore-based community Q&A for peer support without needing AI keys.
Benefit from offline-friendly fallbacks and local AI so help is available even with weak internet.
This turns scattered, high-friction reporting into a guided, consistent, and privacy-aware flow—making it easier to speak up, ensuring higher-quality evidence, and accelerating response by institutions.

Team **Kode-e-punjab** -- [Jasmeet Kaur](https://github.com/jasmeetk17), [Nisha Kanojia](https://github.com/nisha131), [Gagandeep Kaur](https://github.com/SKY-127/), [Suman .](https://github.com/suman512)

`2025-11-16`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
