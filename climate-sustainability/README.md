# Climate and Sustainability

![Projects](https://img.shields.io/badge/Projects-164-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### crossx
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/crossx-9633) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fix-cli-web.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-13-FF6B6B?style=flat-square)

> Your AI Co-Pilot for Windows & Terminal

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Kubernetes](https://img.shields.io/badge/Kubernetes-333333?style=flat-square) ![langchain](https://img.shields.io/badge/langchain-333333?style=flat-square) ![Power shell 7+](https://img.shields.io/badge/Power%20shell%207+-333333?style=flat-square) ![Open telemetry](https://img.shields.io/badge/Open%20telemetry-333333?style=flat-square) ![Rag + chromadb](https://img.shields.io/badge/Rag%20+%20chromadb-333333?style=flat-square)

**Challenges we ran into**

**Challenges we ran into**

Building FixBot required solving several technical and security challenges.

- Reliable Windows diagnostics: Windows stores system information across Event Viewer, WMI, Performance Monitor, and PowerShell. Collecting and correlating this data into meaningful root-cause analysis was one of the biggest challenges.

- Safe AI execution: Allowing an AI to generate and execute terminal commands introduces security risks. We addressed this by implementing a permission gate where every generated command is previewed and requires explicit user approval before execution.

- Natural language understanding: Users describe the same issue in many different ways. We refined our prompts and system workflow so the AI could consistently interpret user intent and generate accurate troubleshooting steps.

- Git automation: Mapping conversational requests like "push my changes" or "fix this merge conflict" into the correct sequence of Git commands while handling errors gracefully required multiple iterations.

- Balancing automation with user control: We wanted FixBot to automate repetitive tasks without taking away control from the user. We solved this by keeping every critical action transparent, reviewable, and reversible.

These challenges helped us build a more reliable, secure, and user-friendly AI terminal assistant.

**The problem it solves**

**The problem it solves**

Windows troubleshooting is often frustrating, time-consuming, and requires technical expertise. Users frequently encounter cryptic error messages, driver failures, network issues, performance bottlenecks, and Git-related problems, but finding the root cause usually involves searching forums, reading documentation, and running complex terminal commands.

Many users end up executing scripts from untrusted sources without understanding the risks, while beginners often depend on IT support even for simple issues. Developers also struggle with Git commands, merge conflicts, and repository management.

FixBot solves these problems by acting as an AI-powered terminal copilot. Users can describe their issue in plain English, and FixBot:

- Diagnoses Windows system problems.
- Explains the root cause in simple language.
- Generates safe PowerShell/CMD commands.
- Requests user approval before execution.
- Automates Git workflows such as commit, push, branching, and merge assistance.
- Reduces troubleshooting time while making system maintenance safer and more accessible

.

This makes Windows administration and developer workflows faster, safer, and easier for both technical and non-technical users.

Team **SUDO** -- [Dinesh kumar As](https://github.com/dineshkumarAS-creator), [Poornima R](https://github.com/poornima2006188)

`2026-06-29`

---

### Fix Bot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fix-bot-c2ee) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dineshkumarAS-creator/fixbot-ai.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fix-cli-web.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-8-FF6B6B?style=flat-square)

> Live Windows monitor in your terminal. Real system

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PyPDF2](https://img.shields.io/badge/PyPDF2-333333?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-333333?style=flat-square) ![lang chain](https://img.shields.io/badge/lang%20chain-333333?style=flat-square) ![hugging face transformer](https://img.shields.io/badge/hugging%20face%20transformer-333333?style=flat-square) ![rich](https://img.shields.io/badge/rich-333333?style=flat-square) ![Lang graph](https://img.shields.io/badge/Lang%20graph-333333?style=flat-square) ![Lang smith](https://img.shields.io/badge/Lang%20smith-333333?style=flat-square)

**The problem it solves**

## Inspiration

Everyday PC problems are simple to *say* and hard to *fix*: slow Wi‑Fi, broken installs, “where is that file?”, “push this to GitHub.” Most tools either give static FAQ answers or dump raw terminal output. We wanted a **local AI support engineer** that understands plain English, reads the real machine state, and can act—with permission—instead of only chatting.

That idea became **FixBot**: a Windows CLI agent that diagnoses and repairs using live OS data, not memorized scripts.

## What it does

FixBot turns natural language into supervised actions across:

- **Network** — Wi‑Fi status, passwords, DNS/adapter repairs, speed tests  
- **Install / Update / Uninstall** — winget-driven package lifecycle with retries  
- **Files** — search (including typos), delete with shortcut cleanup  
- **Local RAG** — explain and answer questions over folders already on disk  
- **GitPilot** — guided + autonomous git (commit, push, recover from upstream errors)

Each serious action follows: **inspect → plan → permission gate → execute → verify → analyze errors → retry or escalate**.

## How we built it

- **Python** CLI with **Rich** for live agent streams and progress  
- **Gemini** for reasoning and plans; **Groq** for fast intent / classification  
- **LangGraph + LangChain** for multi-agent domain graphs (network, install, RAG, git)  
- **Windows APIs / CLI** — winget, netsh, git, psutil, WMI  
- **RAG stack** — loaders, chunking, embeddings, FAISS for local documents/code  
- **GitPilot** — allowlisted `git_ops` + tool registry so the LLM never gets free shell  

Architecture rule we stuck to: **the model plans; tools execute; the verifier decides success.**

## What we learned

- “Autonomous” only feels real when **failure is part of the loop** (e.g. push fails → no upstream → set upstream → push again).  
- **Permission gates** matter more than clever prompts for user trust.  
- Offline / rule-based fallbacks beat waiting forever on an LLM for network repair.  
- OAuth “localhost callback” auth is fragile; **PAT / SSH / a guided auth helper** is kinder to users.  
- Good UX is a **live stream of steps**, not walls of git tips.

## Challenges

1. **LLM hangs & timeouts** on network planning → offline telemetry ladders.  
2. **False verification** (e.g. DNS check fails while internet works) → softer health checks.  
3. **Install/uninstall edge cases** (user-scope apps, admin elevation, “already installed”).  
4. **LibreSpeed public servers** far from India → CDN fallback for speed tests.  
5. **Git auth UX** — browser redirected to dead `127.0.0.1` ports → auth helper + sanitized remotes (never show embedded tokens).  
6. Keeping **many domains** (network, install, RAG, git) isolated so one graph doesn’t break another.

## What’s next

Deeper Git conflict coaching, safer high-risk actions, richer speed-test UI, and tighter shared memory between FixBot and GitPilot—so the same repo context follows you from chat to coach menu.

**Challenges we ran into**

## Challenges we ran into

### Making a Windows monitor feel like a real TUI
We wanted a **btop-style** view in a Windows CLI (live CPU/RAM/net/process), not a one-shot “scan and print.” Rich tables and `Live` look fine in a fixed window, then break when the user **resizes**: rules span 200 columns, the prompt jumps to the far right, and the welcome panel stretches instead of wrapping.  
**Fix:** cap content width, `expand=False` on panels, and treat the terminal as a **column**, not “use every pixel.”

### Live graphs vs. shallow numbers
A speed/net panel that prints “12 Mbps” once is not monitoring. Public LibreSpeed servers from India were **1–3 s away**, so download/upload showed **0 Mbps** and random city names. A static bar also isn’t a graph.  
**Fix:** measure against a nearby edge (Cloudflare), multi-stream with warmup discarded, and drive the UI from **real callbacks / NIC counters** (`psutil.net_io_counters`) the way btop samples bandwidth—not random numbers.

### Process list that actually works on Windows
Listing processes with `psutil` + `open_files()` **hung** the CLI (had to Ctrl+C). Killing “everything” is dangerous (csrss, lsass, explorer).  
**Fix:** skip `open_files()`, sort by CPU/RAM quickly, then **close all (safe)** vs **close some by index** vs **close by name**, with a confirm step.

### Admin vs. real machine state
The tool needs adapter, storage, process, and registry access; skipping those at startup means the monitor is **blind**. Running as Administrator then breaks **user-scope** apps (install/uninstall).  
**Fix:** permission gate at boot, and treat “what Windows reports” (winget, netsh, taskkill) as the source of truth—not FAQ text.

### Don’t confuse chat with a dashboard
Natural language (`process running`, `my wifi`, `speed test`) kept falling into a **planner/LLM graph** instead of opening the live view. Gemini `function_call` with empty text crashed the planner.  
**Fix:** route monitor phrases **straight to the dashboard**, keep the LLM for diagnosis, and never block the live UI on a model timeout.

**Lesson:** a Windows monitor CLI is hard because the OS is slow, scoped, and inconsistent—the UI has to stay live, safe, and width-aware while numbers come from the machine, not the model.

Team **YONKOHS** -- [Poornima R](https://github.com/poornima2006188), [Dinesh Kumar](https://github.com/dineshkumarAS-creator)

`2026-08-23`

---

### RehabPulse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/rehabpulse-ai-safety-copilot-for-home-rehabilitation-c45d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://pulseforgecopilot.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/1b1f0f8daa9642f3b6288bd3f0da49a8) [![Built at](https://img.shields.io/badge/Built%20at-DOMINION%202026-0052CC?style=flat-square)](https://dominion2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Sense. Understand. Intervene. Recover.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![CanvasJS](https://img.shields.io/badge/CanvasJS-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Nodejs](https://img.shields.io/badge/Nodejs-333333?style=flat-square) ![Lucide](https://img.shields.io/badge/Lucide-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

The Care Gap in Home Rehabilitation
Physical therapy recovery heavily relies on home exercise programs. However, over 70% of patients demonstrate poor compliance or execute exercises with incorrect form at home. Without direct supervision, improper movement mechanics lead to secondary joint damage, compensatory habits, and delayed recovery. Clinicians remain blind to patient progress between weekly clinic visits.

How RehabPulse Transforms Physical Therapy
RehabPulse acts as a real-time AI Safety Copilot for home rehabilitation, converting any standard webcam or mobile camera into a clinical kinematic tracker.

Continuous Safety & Form Tracking: Calculates 3D joint angles, extension deficits, movement velocity drops, and bilateral asymmetry in real time without requiring physical wearable sensors or expensive hardware.
Deterministic Safety Kernel: Unlike unconstrained AI models that can hallucinate, RehabPulse uses an un-bypassable clinical safety kernel. When joint angles or velocity drops cross safe physiological limits, the platform automatically pauses the session to prevent injury.
Edge-First Data Privacy: Raw camera feeds are processed locally inside the browser using MediaPipe and WebGL. Only anonymized numerical kinematic vectors (angles and symmetry scores) leave the device, ensuring full privacy compliance by design.
Clinician Remote Telemetry: Telemetry data and safety breach logs stream directly to a provider dashboard, turning unmonitored home care into structured clinical data.

Startup & Industry Business Impact
RehabPulse provides immediate financial and operational value to physical therapy practices and health systems:

Unlocks Remote Therapeutic Monitoring (RTM) Billing: Enables providers to monetize home care using CMS reimbursement codes (CPT 98975 for setup, CPT 98977/98985 for device supply, and CPT 98979/98980 for treatment management).
Reduces Post-Operative Readmissions: Prevents joint re-injury following orthopedic procedures (such as total knee arthroplasty), lowering total care costs for hospital networks and value-based care providers.

**Challenges we ran into**

Challenges We Ran Into

1. Eliminating Latency for Real-Time Safety Enforcement

The Hurdle: Streaming high-resolution video frames to a backend server for pose estimation caused significant latency (200ms–500ms). In physical rehabilitation, delayed form correction renders safety intervention useless and increases injury risk during unsafe repetitions.
How We Solved It: We architected an edge-first pipeline using MediaPipe and WebGL directly inside the browser. Video frames are analyzed locally at 30+ FPS to extract coordinate landmarks. Only lightweight numerical vector payloads (~2 KB) are transmitted to the backend, reducing safety evaluation latency to under 15 milliseconds.

2. Guarding Against AI Hallucinations in Clinical Decision-Making

The Hurdle: Autonomous AI models and LLMs are non-deterministic and can hallucinate. Relying purely on an AI model to dictate whether a post-operative movement is safe introduces unacceptable clinical liability.
How We Solved It: We engineered a multi-agent architecture governed by a Deterministic Safety Kernel. While specialized AI agents handle qualitative reasoning (fatigue analysis and adaptive progression), the Safety Kernel enforces hard mathematical boundary rules. The Safety Kernel maintains strict override authority: if an AI agent suggests continuing an exercise that breaches safety parameters, the kernel instantly triggers an exercise auto-pause.

3. Maintaining Performance Across Low-Spec Consumer Devices

The Hurdle: Running computer vision models locally in web browsers degraded performance on older smartphones and laptops, causing dropped frames and distorted velocity calculations.
How We Solved It: We implemented dynamic canvas resolution scaling, downsampling camera feeds prior to landmark detection while maintaining spatial coordinate precision. We also integrated exponential moving average (EMA) smoothing algorithms to eliminate camera jitter and low-light artifacts.

Team **PulseForge** -- [Akshad Sarda](https://github.com/AkshadSarda23), [Mayank Chandrakar](https://github.com/Mayank-dev24), [Abhishek Kumar](https://github.com/abhi56singh), [Rahul v](https://github.com/rahul)

`2026-09-03`

---

### RECONNECT
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/reconnect-b9d8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anmol2627/RECONNECT) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://reconnect01.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-DOMINION%202026-0052CC?style=flat-square)](https://dominion2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Your Journey, Our support, Stronger together.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**Challenges we ran into**

Challenges We Ran Into & How We Overcame Them
1. The Stripe Checkout Loop (State Hydration)

Hurdle: After a user paid for a module via Stripe, redirecting them back to the exact spot they left off—while instantly unlocking the Google Meet link without a page refresh—caused state synchronization issues.
Solution: We passed a dynamic returnUrl during checkout creation. Post-payment, our backend intercepts the webhook and silently redirects the user back with hidden query parameters. A custom PaymentSuccessHandler then instantly hydrates the global context and auto-opens the module dialog, creating a flawless UX.
2. Dual-Actor Architecture & Privacy

Hurdle: Serving two distinct user types (individuals and organizations) without cluttering the UI or leaking sensitive data.
Solution: We used a strict Next.js Split-Auth architecture (/(participant) vs /(organization)). We secured data using Supabase Row Level Security (RLS) policies so organizations can only access analytics for their specific enrolled cohorts.
3. Vercel Build Crashes with SDKs

Hurdle: Our Vercel deployment repeatedly crashed because Next.js static collection was evaluating our top-level Stripe instantiations before production environment variables were loaded.
Solution: We refactored our code to instantiate SDKs lazily inside the API Route Handlers. This bypassed the static build evaluation phase completely and fixed the deployment.
4. A "Non-Punishing" Habit Tracker

Hurdle: We wanted a "LeetCode-style" daily check-in heatmap, but standard habit trackers feel punishing if you miss a day—the opposite of what reintegration requires.
Solution: We custom-built an SVG heatmap focusing heavily on color psychology. We used soothing sage/forest green gradients and tailored the logic to celebrate "streaks" of positivity, removing any negative visual indicators for missed days.

**The problem it solves**

The Problem RECONNECT Solves
Rehabilitation and reintegration into society are often overwhelming, lonely, and disjointed processes. Individuals leaving the justice system or intensive care programs frequently fall through the cracks due to fragmented resources, lack of accountability, and zero unified support.

RECONNECT acts as a centralized, supportive ecosystem that bridges the gap between individuals seeking a fresh start and the organizations dedicated to helping them.

For Participants (Individuals reintegrating):

Combats Isolation: Provides direct access to peer cohorts, one-on-one mentorship, and support groups so they never feel alone on their journey.
Builds Accountability: Features a gamified "Daily Check-in" system (with streaks and heatmaps) that turns daunting long-term goals into manageable, rewarding daily habits.
Centralizes Resources: Instead of navigating a maze of scattered websites and agencies, participants get personalized AI-driven recommendations for courses, jobs, and counseling right on their dashboard.
For Organizations (Non-profits, halfway houses, rehab centers):

Eliminates Blind Spots: Replaces messy spreadsheets with a powerful analytics dashboard to track participant engagement, milestone completion, and drop-off risks in real-time.
Streamlines Program Delivery: Allows orgs to easily host, manage, and even monetize (via Stripe) workshops, cohorts, and resources.
Scales Impact: Empowers case managers to support more individuals effectively by automating check-ins and progress tracking.
Ultimately, RECONNECT makes the daunting task of starting over manageable, measurable, and deeply supported.

Team **Mavericks** -- [Akshdeep Singh](https://github.com/its-akshdeep06), [Anmol Anmol](https://github.com/Anmol2627), [Ketan Saini](https://github.com/ketansaini-io), [Arnav Sinha](https://github.com/thebatmanbeginning)

`2026-09-03`

---

### TidyWindow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tidywindow-4d0a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/balatharunr/tidy-window) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHDkdaFujQ/iZ_2ATQhXhhqdbsVGtMCRA/view?utm_content=DAHDkdaFujQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h2adb407483) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/nfHyNJpjpQY) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Cleanup, diagnose, optimize and recover Windows

![.NET](https://img.shields.io/badge/.NET-333333?style=flat-square) ![C#](https://img.shields.io/badge/C#-333333?style=flat-square) ![wpf](https://img.shields.io/badge/wpf-333333?style=flat-square) ![Powershell 7](https://img.shields.io/badge/Powershell%207-333333?style=flat-square)

**The problem it solves**

## The problem it solves  
Windows maintenance is fragmented across command-line tools, scripts, and hidden utilities, making tasks error-prone, difficult to track, and risky due to the lack of proper safeguards, consistency, and rollback mechanisms.

---

## What people can use it for / How it makes tasks easier and safer  
- Manage installations, updates, cleanup, and diagnostics from a single interface  
- Execute system operations safely with validation, elevation checks, and restore points  
- Automate and repeat workflows using queues and presets  
- Monitor and audit actions through detailed logs and execution tracking  
- Replace complex terminal commands with a structured and controlled GUI experience

**Challenges we ran into**

## Challenges I ran into  

- **Reliable package manager detection (Winget/Chocolatey/Scoop)**  
  Detection was inconsistent due to environment differences and missing dependencies. Solved by combining PowerShell inventory scripts with fallback checks and clear state validation.

- **Handling elevation and permissions**  
  Many operations required admin rights, causing failures when not properly handled. Fixed by implementing controlled elevation flows and preserving state across restarts.

- **Sequential task execution without conflicts**  
  Running multiple operations in parallel caused instability. Resolved by designing a single-queue, sequential execution model with proper locking.

- **Ensuring safe rollback for critical actions**  
  Risky operations like registry edits and system tweaks needed recovery mechanisms. Addressed by enforcing restore points and maintaining structured backup states.

- **Parsing inconsistent script outputs (logs/JSON errors)**  
  PowerShell outputs were not always clean or predictable. Overcame this by adding robust parsing, error handling, and fallback messaging.

- **Maintaining UI responsiveness during long operations**  
  Long-running scripts blocked the UI. Fixed using async execution with background services and real-time streaming of logs.

- **Cross-feature state synchronization (logs, queue, status)**  
  Keeping UI components consistent was challenging. Solved by centralizing state management and event-driven updates across modules.

Team **Vibrant** -- [Arjjun S](https://github.com/Arjjun-S), Hariharan D, [Dhanush S](https://github.com/Cosmos-0118), [Bala Tharun](https://github.com/balatharunr)

`2026-03-17`

---

### Tinkerers.Space
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tinkerersspace-e385) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/qKitNp/tinker-cli) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tinkerers.space) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/5a156562332c42c6a8c1ada632a81270) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-6-FF6B6B?style=flat-square)

> Agentic Cloud Platform for Vibecoders who Shipfast

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

I have met a lot of intelligent people who are building amazing software, and they are non-technical. Some of them are product managers, and a few of them are college professors. They have just vibe-coded amazing software using Claude Code or Codex, but the biggest bottleneck they are currently facing is deploying it.

I met a professor who has made an entire OCR pipeline to convert books from English to native languages, but the real difficulty is that they simply don't understand how they are going to download the Hugging Face model onto a private server, provision GPUs, and so on. I think this is a sad case. **The real bottleneck today is not that people are unable to create software, but that they are unable to deploy it.**

I want to solve that. I want tinkerers.space to be the layer through which people will be able to deploy stuff. It's **a single platform that an AI agent can access and use to provision all kinds of cloud infrastructure.** I have made a CLI and a skill that the agent can use to deploy stuff, and Prava is basically the payment layer in between.

**Challenges we ran into**

One of the biggest challenges I ran into was actually integrating the Prava payments. I, for some reason, assumed there would be a webhook like with other payment services, but there wasn't. Thankfully, someone in the Discord channel faced a similar hurdle, and I got the solution from them.

Another problem I faced, which was not related to Prava or anything, was that my private server was acting up a bit because it's a bit unreliable right now. Thankfully, I got an Oracle VPS, and I am able to use it as a backup.

**Best Visa Intelligent Commerce Implementation**

The only way agents can grow is to acquire more infra, and to do that, they will need to pay for that infra. This is the future: agents automatically growing, training themselves, provisioning their own compute, buying their own compute. This is where we should focus right now, and I think tinkerer.space is trying to do that. It's the way agents are going to buy compute.

**Most Startup-Ready Product**

The biggest bottleneck for making a product right now is not actually developing the software. It's the deployment. If you make something fairly complex, you will actually need to scratch your head, look at the AWS console for hours, and figure out what's really going to happen. That, for a non-technical guy, is a nightmare. Even if they can somehow use skills to build cool frontends, vibe-code their backend, and integrate an ML model into their product, deployment is where the majority of the time is going to be spent. I want to reduce it all to almost zero. I want the agents to not just vibe-code but to vibe-deploy too, and I think this makes it a perfect startup-ready product.

**OpenAI**

OpenAI is the backbone of Tinkerers.Space. Every time someone sends a repo that doesn't have a Dockerfile we just use GPT-5.6 Luna to build it.

In fact, the example that I gave in the demo video does not have a Dockerfile. Even when someone tries to deploy on us, we don't actually know what tech stack they are using, right? To even determine the tech stack, whether it's Python or a Next.js app etc. we just use the OpenAI LLMs to read the repo and decide what actions we should take. OpenAI is the backbone of Tinkerers.Space.

**Best Agentic User Experience**

I think it's a really good UX because I have tried to reduce the hours' worth of DevOps and deployment tasks that a solo developer or a vibe coder would need to do to two minutes, if not seconds, in some cases. An agent is just going to do it for you, and you don't even have to worry about it.

**Agentic Commerce Hackathon**

Prava is actually the best fit for a payment provider here because the main interface for my users is going to be an agent. The agent is going to provision the cloud infrastructure required for it, which basically means the agent will be the buyer in a lot of cases. I don't think any other payment provider is providing this service.

Pranjal Pranjal

`2026-08-02`

---

### GreenStreet
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenstreet-7a6d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ASIKKANI/GreenStreet) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/kLTR9nePdno?feature=shared) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Don't just trash it. Cash it.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Image Processing - Open CV](https://img.shields.io/badge/Image%20Processing%20--%20Open%20CV-333333?style=flat-square)

**The problem it solves**

**The Problem**

Most people know they should segregate waste, but daily participation remains low because doing the right thing feels inconvenient, invisible, and completely unrewarded. At the same time, the recycling industry faces three major structural bottlenecks:

* **Contaminated Feedstock:** Industrial recyclers lose 30% to 40% of their operational margins sorting dirty, mixed garbage out of municipal waste streams.


* **The Corporate Compliance Gap:** Consumer brands (FMCG) are legally mandated under Extended Producer Responsibility (EPR) regulations to collect and recycle their packaging, but have no practical infrastructure to collect directly from individual households.


* **Inefficient Logistics:** Dispersed collection of small recyclable volumes from standalone homes is economically unviable for industrial collection trucks.



---

**How GreenStreet Solves It**

GreenStreet turns daily waste segregation into a simple, financially rewarding routine by connecting citizens directly to the industrial recycling supply chain:

* **For Everyday Individuals:** Users scan sorted plastic, cans, or dry waste using on-device camera verification to confirm purity. They drop off their tagged bag at a neighborhood grocery store (Kirana) or a community smart drop-pod. Within 30 seconds of weighing, they receive instant cash credited directly to their UPI account.


* **For Industrial Recyclers:** Recyclers receive clean, pre-sorted materials aggregated at neighborhood hubs, eliminating manual sorting overhead. The platform automatically groups local drop-offs into full-capacity collection routes for pickup vehicles.


* **For Consumer Brands:** FMCG companies fund citizen micro-payouts using their mandatory EPR compliance budgets. In exchange, they receive verified, auditable digital certificates proving regulatory plastic collection quotas.



---

**Key Impact**

* **Replaces Guilt with Tangible Value:** Gives households an immediate financial incentive to segregate waste daily, converting civic duty into a reliable micro-income stream.


* **Cuts Industrial Processing Overhead:** Keeps recyclable materials unadulterated before entering the recycling stream, reducing plant processing costs and diverting waste from landfills.


* **Verified Chain-of-Custody:** Provides end-to-end digital traceability from the citizen drop point to the recycling facility, making regulatory environmental compliance transparent and fraud-proof.

**Challenges we ran into**

**1. In-Browser Image Auditing & Model Latency on Mobile**

* **The Hurdle:** Running visual verification directly inside a mobile browser (PWA) caused memory spikes and slow response times, especially when users submitted images of crushed plastic bottles under dim or inconsistent lighting.


* **How We Overcame It:** We implemented an optimized client-side image compression step before passing frames to our vision classification endpoint. We added confidence-threshold validation to reliably score plastic types and detect obvious liquid or organic contamination in under 800ms.



---

**2. Synchronizing Real-Time State Between User and Merchant Portals**

* **The Hurdle:** Because the platform relies on local shopkeepers (Kirana partners) to verify the physical handover, both the resident's app and the merchant's dashboard required instant, two-way state reconciliation without manual page refreshes or inconsistent records.


* **How We Overcame It:** We built real-time WebSocket communication channels between both client interfaces. The second a merchant inputs the scale reading and scans the user's batch, the verified weight and updated wallet balance sync instantly across both screens.

---

**3. Preventing Double-Payouts and API Replay Exploits**

* **The Hurdle:** Triggering automated micro-payouts introduced the risk of replay attacks, where a user could attempt to reuse the same QR code or intercept the network call to trigger multiple payouts for one drop-off.


* **How We Overcame It:** We implemented an idempotency key framework paired with time-bound, single-use tokens. Each Bag ID auto-expires after 15 minutes and transitions through strict state stages (`CREATED` -> `VERIFIED` -> `SETTLED`), ensuring a payout executes exactly once on the backend.



---

**4. Geospatial Clustering for Fragmented Drop-Off Points**

* **The Hurdle:** Standalone household drop-offs were scattered randomly across the map, making individual pickup dispatches financially impractical and computationally heavy to calculate continuously on the server.


* **How We Overcame It:** We implemented density-based spatial clustering (DBSCAN) using PostGIS. The backend holds localized submissions in an aggregation queue until a geographic cluster hits a defined batch threshold, automatically generating an optimized multi-stop collection route for local pickup vehicles.

Team **Radioheads** -- [Asik kani](https://github.com/ASIKKANI), [Bharanidharan R](https://github.com/bharanidharanGit003), [Logesh R](https://github.com/Logesh-vr), [Divya Priya RK](https://github.com/divyapriya382006/)

`2026-09-02`

---

### DormSphere – AI-Powered Student Living Ecosystem
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dormsphere-cfae) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://priyansusamal.github.io/DormSphere/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=TnLyNSOVaxc) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> The Digital Hub for Hostel Living

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**The problem it solves**

The Problem DormSphere Solves

Hostel life is exciting, but it also comes with daily challenges that students struggle to manage efficiently.

Students often rely on multiple disconnected platforms and WhatsApp groups for important activities such as finding lost items, tracking expenses, organizing study groups, checking hostel notices, managing laundry, buying and selling essentials, and finding compatible roommates. This creates confusion, information overload, and wasted time.

DormSphere solves this problem by providing a single AI-powered platform that centralizes all essential hostel services in one place.

-How DormSphere Helps

1. DormAI Assistant
Provides instant guidance for common student concerns such as budgeting, study planning, food choices, roommate issues, and hostel-related queries.

2. Budget Buddy
Helps students track expenses and manage limited monthly budgets, reducing unnecessary spending and improving financial awareness.

3. MessMeter
Allows students to rate meals and view community feedback before visiting the mess, helping them make informed dining decisions.

4. Lost & Found
Creates a centralized space for reporting and recovering lost items, increasing the chances of successful item recovery.

5. Study Circles
Enables students to create and join collaborative study groups, making exam preparation and project work more effective.

6. Marketplace
Allows students to buy and sell books, calculators, lab coats, and other essentials within the hostel community, reducing costs and promoting reuse.

7. Notice Board
Provides a single location for hostel announcements, maintenance alerts, events, and important updates, eliminating the need to search through multiple chat groups.

8. Laundry Tracker
Helps students keep track of laundry submissions, pickup dates, and status updates, reducing misplaced or forgotten clothes.

9. Roommate Match
Suggests compatible roommates based on lifestyle preferences such as sleep schedules, cleanliness, study habits, and social behavior, helping create a more comfortable living environment.

 Impact

DormSphere transforms hostel management from a fragmented and stressful experience into a streamlined, organized, and student-friendly ecosystem. By combining community-driven features with AI assistance, it improves productivity, communication, convenience, and overall student well-being.

**Challenges we ran into**

Building DormSphere as a multi-feature web application came with several challenges.

1. Managing Multiple Features in a Single Project

One of the biggest challenges was integrating many independent modules such as Budget Buddy, MessMeter, Lost & Found, Study Circles, Marketplace, Notice Board, Laundry Tracker, and Roommate Match into a single cohesive platform.

As the number of features increased, keeping the code organized became difficult. To overcome this, I separated functionality into dedicated sections and created reusable UI patterns, allowing all modules to maintain a consistent design and user experience.

2. Debugging JavaScript Errors

As new features were added, some functions stopped working due to misplaced brackets, duplicate variables, and incorrect function execution order.

A major issue occurred when homepage statistics were being updated before the required helper functions were loaded. This caused runtime errors and prevented some dashboard elements from rendering correctly. I fixed this by restructuring the JavaScript file, organizing functions logically, and ensuring dependencies were loaded before execution.

3. Creating a Consistent User Interface

With multiple pages and modules, maintaining a professional and visually consistent design was challenging. I used a unified glassmorphism-inspired design system with shared colors, layouts, cards, animations, and responsive components to ensure a seamless experience across the platform.

4. Balancing Features and Performance

As the project grew, I had to balance adding new features with maintaining usability and responsiveness. Instead of continuously adding more modules, I focused on improving existing features, refining interactions, and enhancing the overall user experience.

Future API Integration Challenges

While building DormSphere, I designed the platform as a fully functional frontend prototype using browser-based storage. One challenge was planning how the system would scale into a production-ready application with real-time data and AI capabilities.

Several features are designed with future API integration in mind:

A. DormAI - can be connected to AI APIs such as Gemini or OpenAI to provide intelligent, personalized responses instead of rule-based suggestions.
B. Authentication - can be upgraded using Firebase Authentication for secure user management.
C. Marketplace, Study Circles, and Lost & Found can be connected to cloud databases such as Firebase Firestore or MongoDB to enable real-time updates across multiple users.
D. Notice Board can integrate with push notification services to instantly notify students about important announcements.
E. MessMeter can use backend APIs to aggregate ratings from all hostel residents and generate live analytics.
F. Roommate Match can leverage machine learning models to calculate compatibility scores using more advanced behavioral patterns and preferences.

Designing the application while keeping future API integration in mind was an important challenge because the structure had to remain modular and scalable. This experience helped me understand how frontend applications can evolve into full-stack, real-world solutions.

Key Learning

This project taught me the importance of modular development, debugging large codebases, UI consistency, and building scalable web applications. It also helped me understand how multiple independent systems can be integrated into a single user-focused platform.

[Priyansu Samal](https://github.com/priyansusamal/)

`2026-06-08`

---

### Greenoa
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenoa-1d8f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sai15-code/greenoa.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/111c0d325d6a4195992422415677b59d) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Travel Green. Earn Rewards. Make Impact

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square)

**The problem it solves**

Greenoa solves the problem of waste pollution in tourist places. Many travelers create plastic waste but don’t have a proper way or motivation to dispose of it responsibly.

Our platform makes it easier by allowing users to collect waste, upload proof, and earn rewards. This encourages people to take action and helps keep environments clean while traveling

**Challenges we ran into**

While building Greenoa, we faced some challenges.
We had difficulty managing the database and connecting Firebase with our frontend. Some errors occurred in setup and data handling.We also struggled to design a clear user flow for collecting waste, uploading proof, and giving rewards.
We solved these by fixing configuration issues, simplifying our features, and focusing on a basic working MVP.

[Sai Kumar](https://github.com/sai15-code)

`2026-04-20`

---

### EcoSentryx
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecosentryx-5814) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ecosentryx.pages.dev/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/IwoTSEFOFQo) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Multilingual eco-learning and mission tracking

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square)

**The problem it solves**

## The Problem EcoSentryx Addresses

EcoSentryx is an innovative platform designed to enhance environmental awareness and action among individuals, schools, and organizations.

### Problem

A significant barrier to effective environmental action is the fragmented nature of information available to the public. People often find themselves overwhelmed by scattered resources, making it difficult to engage meaningfully. Furthermore, verifying participation in various initiatives is complex, leading to ineffective campaigns that struggle to translate awareness into structured public action.

### Solution

EcoSentryx provides a seamless solution by creating a centralized platform where users can learn about environmental issues, participate in eco quizzes, and submit mission records through dedicated channels. This integrated system allows users to engage with environmental efforts without the hassle of managing multiple tools or sources.

### Features

- **Centralized Information Hub**: Access comprehensive resources on various environmental topics.
- **Engaging Eco Quizzes**: Interactive quizzes that educate users while encouraging further action.
- **Easy Participation Tracking**: Submit mission records for both personal and institutional involvement in a clear, organized manner.
- **Community Engagement**: Facilitate collaboration and organization of community-scale initiatives.

### Implementation

The EcoSentryx platform features a user-friendly interface that allows individuals to easily navigate and participate in awareness activities. We are actively showcasing our platform to demonstrate how users can leverage it to enhance their eco-friendly efforts.

### Impact

EcoSentryx significantly boosts visibility and organization in environmental awareness activities, helping users convert their knowledge into action. By streamlining the process of engaging with ecological issues, the platform empowers individuals and organizations to make a real impact on the planet.

### Challenges

As we continue to develop EcoSentryx, we recognize the need to optimize the user experience for a wider range of devices, ensuring that participation is easy and accessible regardless of the platform used.

### Links

- **Main Website**: [EcoSentryx Homepage](https://ecosentryx.pages.dev)  
- **Presentation**: [EcoSentryx PPT](https://gamma.app/docs/EcoSentryX-au5kd3kwpiqlcs0)  

By addressing these challenges, EcoSentryx stands ready to enhance environmental awareness and foster meaningful action across communities.

**Challenges we ran into**

In our endeavor to create a sophisticated system, we encountered several critical challenges that required our strategic focus and expertise.

## Integrating Education, Engagement, and Data Capture

A paramount challenge was seamlessly integrating education, engagement, and structured data capture into a unified frontend experience. To tackle this, we focused on:

- **Streamlined Interface Design**: We designed an interface that exudes simplicity, ensuring user comprehension while avoiding a fragmented experience.
  
- **Clear Flow Separation**: By distinctly separating participation flows, we provided users with a clear pathway through their interactions, thereby enhancing usability.

## Supporting Multilingual Content and Timed Features

Another essential challenge involved accommodating multilingual content and developing a timed fullscreen quiz flow. Our strategies included:

- **Dynamic Language Support**: We implemented a robust framework that enables the system to handle multiple languages effortlessly, ensuring inclusivity for a diverse user base.

- **Engaging Quiz Mechanics**: The design of the quiz flow was meticulously crafted to maintain user engagement while adhering to the timed requirements, fostering a dynamic learning environment.

## Maintaining Data Integrity Across Submission Pathways

Ensuring clean data writes across various submission pathways for individuals and institutions was critical. Our approach involved:

- **Organised Data Architecture**: We structured our backend data model around distinct record types, promoting clarity and consistency in data management.

- **Efficient Submission Processes**: By developing streamlined submission pathways, we ensured that data integrity remained intact, even with complex input scenarios.

## Prioritising Exceptional Design and User Experience

Recognising the pivotal role that design plays in user experience, we made key design principles a priority:

- **User-Centric Aesthetics**: Our design philosophy centered on creating an intuitive and visually appealing interface, enabling users to navigate seamlessly while accessing advanced functionalities.

- **Balancing Complexity and Usability**: Despite the intricate tasks being performed, we ensured that the system maintained an accessible and user-friendly feel.

## Embracing Continuous Improvement

To effectively navigate these challennsuring user comprehension while avoiding a fragmented experience.

- **Clear Flow Separation**: By distinctly separating participation flows, we provided users with a clear pathway through their interactions, thereby enhancing usability.

**Supporting Multilingual Content and Timed Features**

Another essential challenge involved accommodating multilingual content and developing a timed fullscreen quiz flow. Our strategies included:

- **Dynamic Language Support**: We implemented a robust framework that enables the system to handle multiple languages effortlessly, ensuring inclusivity for a diverse user base.

- **Engaging Quiz Mechanics**: The design of the quiz flow was meticulously crafted to maintain user engagement while adhering to the timed requirements, fostering a dynamic learning environment.

**Maintaining Data Integrity Across Submission Pathways**

Ensuring clean data writes across various submission pathways for individuals and institutions was critical. Our approach involved:

- **Organised Data Architecture**: We structured our backend data model around distinct record types, promoting clarity and consistency in data management.

- **Efficient Submission Processes**: By developing streamlined submission pathways, we ensured that data integrity remained intact, even with complex input scenarios.

**Prioritising Exceptional Design and User Experience**

Recognising the pivotal role that design plays in user experience, we made key design principles a priority:

- **User-Centric Aesthetics**: Our design philosophy centered on creating an intuitive and visually appealing interface, enabling users to navigate seamlessly while accessing advanced functionalities.

- **Balancing Complexity and Usability**: Despite the intricate tasks being performed, we ensured that the system maintained an accessible and user-friendly feel.

**Embracing Continuous Improvement**

To effectively navigate these challenges, we committed ourselves to a culture of continuous improvement:

- **Rigorous Testing and Iteration**: We embraced an iterative process, frequently updating the system based on performance metrics and user feedback to enhance its reliability.

- **Focused Interface Refinement**: Our dedication to a clean, distraction-free interface fostered enhanced user engagement and productivity.

By employing these proactive strategies and maintaining a resolute focus, we have successfully navigated the key challenges in developing a cohesive and efficient system, paving the way for future innovation and excellence.

**Track: Checkout with Locus**

**EcoSentryx: Transforming Environmental Engagement**

*Integrating Efforts with Locus Checkout*

1. **Enhancing Engagement**
   - EcoSentryx seamlessly integrates with the Locus Checkout system to foster environmental participation through a verifiable action flow.
   - This innovative approach not only motivates users but also ensures accountability in eco-friendly initiatives.

2. **Diverse Support Mechanisms**
   - **Paid Missions**: Participants can engage in various missions that support environmental causes while receiving tangible rewards.
   - **Sponsorship-Backed Campaigns**: Collaborate with organizations to create impactful campaigns funded through sponsorships, amplifying reach and effectiveness.
   - **Institution-Driven Eco Programs**: Partner with institutions to launch programs that target specific ecological goals, backed by their resources and networks.

3. **Seamless Payment Solutions**
   - Locus Checkout supports seamless USDC-based payments, simplifying transactions for participants and enhancing user experience.
   - Offers flexible payment options for:
     - **Campaign Access**: Easy entry into various environmental initiatives.
     - **Premium Institutional Participation**: Opportunities for deeper engagement with specialized programs.
     - **Reward-Linked Actions**: Encourages actions that benefit the environment, rewarding users for their commitment.

4. **Versatile Usage**
   - This platform serves not only human users but also automated agent-driven workflows, making it adaptable for various operational needs.
   - Significant potential for innovative applications in both individual and organizational contexts.

With EcoSentryx and Locus Checkout, we are paving the way for a more sustainable future through verified and engaging environmental actions. Join us in making a meaningful impact!

Team **EcoSentryx** -- Himanshu Kumar Singh

`2026-04-26`

---

### Waste hunter
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/waste-hunter-f111) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://eco-tracker-ruddy.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/J0UuxV3NhBA) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> AI That Turns Intentions Into Action

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AI](https://img.shields.io/badge/AI-333333?style=flat-square)

**The problem it solves**

## The Problem

Waste management is often reactive, inconvenient, and disconnected from everyday user behavior. People may notice litter in their surroundings but lack a simple way to identify, report, and take action on it. At the same time, sustainable habits can be difficult to maintain without motivation or feedback.

**Waste Hunter** addresses this by turning waste management into an interactive, AI-powered experience. Users can identify and report waste, build sustainable habits, complete challenges, maintain streaks, and track their environmental impact — all from one platform.

The goal is to make responsible waste management **simple, engaging, and actionable**, while encouraging people to take small actions that contribute to cleaner communities.

**Challenges we ran into**

Building Waste Hunter within the hackathon timeline came with a few technical and integration challenges.

1. AI/API limitations: We encountered API usage limits while testing AI-powered features. We optimized requests and focused on the core functionality needed for the demo.
2. Camera integration: The waste-detection camera feature required additional debugging to work reliably across different devices and browsers.
3. AI Assistant: Integrating the AI assistant with the rest of the application required troubleshooting API connectivity and frontend integration.
UI responsiveness: We had to refine the interface to ensure that the application remained usable across different screen sizes and handle issues such as dark-mode inconsistencies.
4. Time constraints: With a short hackathon timeline, we prioritized the most impactful features and focused on delivering a functional MVP rather than overloading the product with unfinished features.

Team **VYNEX** -- [Resham Afroz](https://github.com/reshamafroz222-collab), Mukesh Kamboj, Sameer Kumar, Nikhil Vats

`2026-08-25`

---

### WasteMatch AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wastematch-ai-f2cf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dishitasingh178-svg/Wastematch-Ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://waste-match-ai.ai.studio) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3QzaFxyD2Fk?si=Jw8vu11vFa_zrzA1) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Where Waste Meets Its Perfect Match

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square)

**Challenges we ran into**

One of the key challenges we faced while building WasteMatch AI was **integrating the Google Gemini API securely without exposing our API key in the frontend or publicly accessible code**. Since our application relies on Gemini for material understanding and AI-powered analysis, the API key was essential, but placing it directly in the client-side application would have created a serious security risk, especially if the project were deployed or shared publicly. To overcome this, we redesigned the integration so that the Gemini API is accessed through our **server-side Node.js layer**, keeping the credential away from the client. We stored the key securely using **environment variables** and provided a `.env.example` file containing only a placeholder for configuration. This allowed the application to communicate with Gemini while ensuring that the actual secret remained outside the source code and could be managed safely during development and deployment. This challenge taught us an important real-world lesson: **building an AI application isn't only about making the API work—it is also about integrating it responsibly and securely.**

**The problem it solves**

WasteMatch AI solves a major problem in the industrial sector: **valuable by-products are often treated as waste simply because businesses don't know where or how they can be reused**. At the same time, other industries may be purchasing new raw materials that could potentially be replaced by these available by-products. WasteMatch AI acts as a bridge between these two sides by providing an AI-powered platform where businesses can submit information about their industrial materials, including the material type, quantity, location, contamination details, and relevant characteristics. The platform then analyzes this information and identifies potential facilities that could reuse the material. Unlike a basic marketplace or keyword search, WasteMatch considers important real-world factors such as **material compatibility, contamination tolerance, facility capacity, required throughput, geographic distance, hazardous-material safety, economic value, and potential environmental impact**. This makes the process of discovering potential reuse opportunities faster, safer, and more practical for businesses. For example, consider a **steel manufacturing facility that generates steel slag** as a by-product. Instead of sending that material directly for disposal or storage, the manufacturer could submit its details to WasteMatch AI. Using Google Gemini for material understanding and normalization, the system can interpret the material information and then evaluate potential facilities, such as a cement-related facility, based on compatibility, quantity requirements, contamination limits, capacity, distance, and safety. WasteMatch can then rank suitable candidates and provide a **"Why Matched?"** explanation showing why a particular facility was recommended, along with potential economic value and CO₂ impact. In this way, WasteMatch changes the question from **"How do we dispose of this waste?"** to **"Who can use this material?"**—helping industries discover potential resource-sharing opportunities while supporting cost reduction, waste reduction, and a more circular industrial economy.

**Climate & Sustainability**

WasteMatch AI fits directly into the **Climate & Sustainability** track by helping industries turn waste into valuable resources. Instead of allowing industrial by-products to be discarded, our platform uses AI to find facilities that can potentially reuse those materials, reducing waste and the need for new raw materials. By connecting industries through **industrial symbiosis**, WasteMatch can help reduce disposal, lower associated emissions, create economic value, and promote a **circular economy** where resources stay in use for longer. Our goal is simple: **turn industrial waste into opportunity while building a more sustainable future.**

Team **Grok Is This True** -- [AKSHRA SRIVASTAVA](https://github.com/akshra-s), Vishesh Agrawal, [Dishita Singh](https://github.com/dishitasingh178-svg), Akshara Singh

`2026-08-15`

---

### DevShrink
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/devshrink-39e9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/shumaqueraza/devshrink) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://devshrink.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Understand any repo in seconds.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SSE](https://img.shields.io/badge/SSE-333333?style=flat-square)

**The problem it solves**

Every developer knows the feeling: you join a new team, inherit a legacy project, or want to evaluate an open-source library and you spend hours clicking through files, reading stale **READMEs**, and trying to figure out where anything lives.

**READMEs** are out of date. Wikis are empty. "*Just read the code*" isn't onboarding it's
archaeology.

DevShrink automates the first pass. Paste any **public GitHub URL** and get a structured onboarding report in under 60 seconds:

- 🏗️ **Architecture diagram** (Mermaid)
- 🚀 **Setup guide** with exact shell commands
- 📁 **Key files** what they do and why they matter
- 🧱 **Tech stack** with evidence
- ⚡ **Code quality assessment** what's good, what's missing
- 🧪 **Testing status**
- 🔒 **Security observations**
- 🎯 **First contribution** a specific scoped task
All streaming in **real-time** via Server-Sent Events. No polling, no waiting.
#### Use cases
- 👋 **Onboarding** understand a new team's codebase in minutes
- 🔍 **Evaluation** vet a library or tool before adopting it
- 📖 **Open source** give contributors a living onboarding document
- 🧐 **Code review prep** get the full picture before diving in
**Zero setup. No sign-up. No fluff.**

**Challenges we ran into**

### 1. SSE streaming vs response buffering

**Problem:** *fetch()* with *ReadableStream.getReader()* buffers the entire response body on most browsers before yielding to the reader. All AI tokens arrived at once when the connection closed, defeating the purpose of streaming.

**Fix:** Switched to native *EventSource* (Server-Sent Events). This required changing the endpoint from *POST* to *GET* (passing the repo URL as a query parameter), but now each event arrives in real-time with zero buffering.

**Key trade-off:** SSE is GET-only, so the URL is visible in server logs. Worth it for real-time streaming.

---

### 2. Gevent + SSL → RecursionError on deployment

**Problem:** Deploying with *gunicorn --worker-class gevent* caused infinite recursion in Python's *ssl* module:

*RecursionError: maximum recursion depth exceeded*

Root cause: gevent monkey-patches *ssl*, but *requests* / *urllib3* had already imported and cached SSL references before the patch ran. This is a [well-known issue](https://github.com/gevent/gevent/issues/1016) with gevent + SSL.

**Fix:** Moved *gevent.monkey.patch_all()* to the absolute first line of *app.py*, before any other import, including the standard library. This ensures SSL is patched before any library caches it:

```
import gevent.monkey
gevent.monkey.patch_all()
```

This single line fixed the entire deployment.

---

### 3. ES6 modules blocked by wrong MIME type

**Problem:** Hosting on Render.com served *.js* files as *Content-Type: text/plain* instead of *application/javascript*. Modern browsers strictly enforce *application/javascript* for *type="module"* scripts blocking the entire frontend from loading.

**Fix:** Python's *mimetypes* module on Linux was mapping *.js* incorrectly. Overrode it at app startup:

```
import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
```

---

### 4. Thread-safe rate limiting

**Problem:** Added IP-based rate limiting (2 requests per minute) with a sliding window. Flask's *threaded=True* (default since Flask 1.0) spawns a new thread per request. Two concurrent requests from the same IP could race past the check both seeing 0 timestamps.

**Fix:** Wrapped the timestamp read-modify-write cycle with *threading.Lock* and used *time.monotonic()* (immune to system clock changes) instead of *time.time()*.

[Shumaque Raza](https://github.com/shumaqueraza)

`2026-06-29`

---

### ResQ_link
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resqlink-9cc1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prith-2005/ResQ_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/7AfCwi8Ap0w?si=hV4SnYpPYuHagoPT) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Reducing response time when every second matters

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square)

**The problem it solves**

Emergency response is often slow and uncoordinated, especially in critical situations like accidents, fires, or crimes.
People struggle to quickly contact help or share their exact location during emergencies.
There is no centralized platform to report incidents and track their status in real time.
Lack of communication between users and responders leads to delays and confusion.
Existing systems do not provide real-time updates or transparency in handling incidents.
 Our Solution (ResQLink)
Provides a one-click SOS system that instantly alerts a trusted contact via WhatsApp with the user’s location.
Enables users to report incidents and disasters in real time, ensuring faster information flow.
Uses a centralized admin panel where authorities can:
Verify reports
Assign responders
Track progress (on the way, reached, resolved)
Offers real-time status updates, improving transparency and user confidence.
Integrates location-based reporting and GPS access, making response more accurate and faster.
Maintains live statistics and tracking, helping monitor system performance and efficiency.

**Challenges we ran into**

Designing a fast reporting system
Balancing speed and usability was difficult, as we needed a system that works in seconds without overwhelming the user with forms.
Real-time data flow between user and admin
Ensuring that reports instantly appear on the admin dashboard and update correctly required careful handling of APIs and backend logic.
Database transition (Local → Cloud)
Migrating from local MongoDB to MongoDB Atlas involved handling connection issues, authentication errors, and ensuring smooth data flow.
Managing multiple workflows
Handling different flows like SOS, incident reporting, and disaster reporting while keeping the system simple was challenging.
UI/UX optimization
Designing an interface that is both fast and intuitive under emergency conditions required multiple iterations.
Error handling and reliability
Ensuring the system works even when inputs are incomplete or when location access fails required robust validation and fallback logic.

**Best Use of MongoDB**

ResQLink heavily relies on MongoDB Atlas as its core database to manage real-time emergency data efficiently.
We use MongoDB Atlas (cloud database) to store user information, incident reports, and disaster data, enabling scalable and remote access.
The system handles dynamic and unstructured data such as different types of emergencies, locations, and user inputs, which fits perfectly with MongoDB’s flexible document model.
Each report is stored as a document containing fields like type, severity, location, and status, allowing easy updates and tracking throughout the response lifecycle.
MongoDB enables fast read/write operations, which is critical for real-time emergency reporting and admin monitoring.
Using Atlas allows our system to be accessible across multiple devices and environments, supporting future scalability.
We also utilize MongoDB to maintain live statistics and status updates, which are reflected instantly on the admin dashboard.

Team **Bugged Brains** -- [PRATYAY CHATTERJEE](https://github.com/PRATYAYCHATTERJEE), [PRIYANSHU MUKHERJEE](https://github.com/Priyanshumkjee), [Nileswar Dawn](https://github.com/Nileswar007), [PRITHWISH CHATTERJEE](https://github.com/Prith-2005)

`2026-04-05`

---

### EnvDiff
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/envdiff-32bd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abhi6537/EnvDiff) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Fix your environment. Not your entire system.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![GOOGLE GEMINI API](https://img.shields.io/badge/GOOGLE%20GEMINI%20API-333333?style=flat-square)

**The problem it solves**

Every developer has been here: you need a specific Python or Node version to run one project. You install it. Now three other projects are broken.

You paste the error into Claude or ChatGPT. It gives you five things to try. 
None of them work. Because the AI is guessing. It doesn't know what actually changed on your machine.

**EnvDiff fixes this two ways:**

***First,*** it tells you exactly what's wrong. It keeps a snapshot of your 
working environment and when something breaks, it shows you which change caused it. Not five possibilities. The actual cause.

***Second,*** before applying any fix, it saves your current environment as a 
restore point. Your app runs. When you're done, one click brings everything back to exactly how it was.

No Docker setup. No config files. No permanently broken system.

*It's like Time Machine for your dev environment.*

**Challenges we ran into**

Building EnvDiff wasn't just about calling an LLM our biggest challenges revolved around safety, determinism, and cross-platform execution. If an AI is going to automatically fix a developer's environment, it absolutely cannot break their machine in the process.

Here are the specific hurdles we faced and how we overcame them:

**1. The "Don't Break My Machine" Hurdle:** Safe Sandboxed Execution
The Challenge: Initial tests revealed a terrifying reality: the AI would frequently generate destructive or global-modifying scripts (e.g., curl | sudo bash, pyenv global, or writing to ~/.bashrc). We couldn’t just pipe raw LLM output into a user's terminal—that defeats the purpose of a helpful tool. The Solution: We engineered a Tangible, Project-Scoped Sandbox Environment. We built an execution interceptor in our VS Code extension that parses the AI's bash/PowerShell scripts before they run. It blocks system-modifying commands and automatically rewrites them into safe, local equivalents (e.g., forcing Python fixes into a .envdiff-sandbox/venv instead of the global interpreter). We made the sandbox visible and verifiable—creating an audit log (sandbox.log) of what was blocked vs. executed, alongside an auto-generated rollback.sh so developers can trust the tool completely.

**2. The "Hallucination vs. Action" Dilemma**
The Challenge: We found that a single LLM prompt trying to diagnose complex environment diffs (Node versions, OS differences, missing Env Vars, and package mismatches) simultaneously was prone to hallucinations. It would sometimes invent dependencies or suggest fixes that didn't align with the error stack trace. The Solution: We implemented a 3-Persona Consensus Engine. Instead of one generic prompt, the diff is analyzed by three distinct AI personas:

The Node/Frontend Expert
The Python/Backend Expert
The DevOps/Sysadmin Expert The backend aggregates their independently generated fixes, scores them based on the actual error trace, and only returns the highest-confidence, cross-verified solution to the VS Code extension.

**3. The "Observer Effect" in Version Detection**
The Challenge: We ran into severe cross-platform edge cases while capturing the "Golden" environment. For example, on Windows, querying Python versions using the py launcher inside spawned shell processes was failing due to complex quoting/escaping bugs ("py -3.11" vs py -3.11). This caused golden snapshots to record the wrong system defaults instead of the project-specific requirements. The Solution: We refactored our CLI detectors to act as "smart observers". Instead of blindly running shell commands, the CLI now proactively scans for project markers (like .python-version or .nvmrc) and dynamically restructures how it invokes sub-processes based on the host OS (win32 vs linux). This ensured that the golden snapshot perfectly matches the developer's intended project state, eliminating false-positive diffs across operating systems.

**Best Use of Gemini API**

We use the **Gemini API to power a 3-expert consensus engine.** 
Instead of asking one AI to figure everything out, we run three specialized Gemini instances in parallel, each with a different focus:

- **Infrastructure Expert:** looks at OS, runtime versions, system-level changes
- **Dependency Expert:** looks at package mismatches and version conflicts  
- **Configuration Expert:** looks at env vars, permissions, network config

All three analyze the environment diff and the error simultaneously. 
We then cross-validate their outputs using keyword overlap. If all three agree, we show a high confidence fix. If two agree, moderate confidence. If they diverge, we show all perspectives and let the developer decide.

The result is a diagnosis that is more reliable than asking a single model, because each expert is focused on exactly one layer of the environment.

Team **Jugaadu** -- [Piuli Biswas](https://github.com/iampiuli), [Kripasindhu Ghosh](https://github.com/kripa521), [Abhinandan Ghosh](https://github.com/Abhi6537), [AMRIT KAR](https://github.com/Amrit7679)

`2026-04-05`

---

### PlasticSense.ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/plasticsenseai-beab) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mjdevs27/Fantastic_Four_DJS_hn4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1S2G_z75vNdHM_dB4SGC6cAoHwHTlZFpY?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> helps users dispose of waste using real-time camer

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Waste sorting today is:

manual → slow, inconsistent, unsafe
error-prone → contamination reduces recyclability
inefficient → valuable recyclable material gets lost

There is no real-time intelligence layer that tells:

what material is present
how recyclable the batch is
how confident the system is
how much volume is being processed

**Challenges we ran into**

1. Dataset Imbalance (LDPE issue)
Problem: LDPE class had very few samples
Impact: Model biased toward majority classes, poor LDPE recall
Solution: Class-weighted loss + oversampling + augmentation
2. Dataset Mismatch
Problem: Combined datasets had different label structures (organic vs plastic-specific)
Impact: Inconsistent training signals
Solution: Unified label mapping + cleaned overlapping/ambiguous classes
3. Image → Video Generalization
Problem: Model trained on static images but deployed on live video
Impact: Performance drop due to motion blur, lighting, occlusion
Solution: Augmentation (blur, brightness, occlusion) + frame sampling
4. Real-Time Latency
Problem: Running detection + classification sequentially increased latency
Impact: FPS drop, non-smooth live feed
Solution: Mixed precision (FP16), threshold filtering, skipping redundant frames
5. Detection–Classification Pipeline Sync
Problem: YOLO outputs bounding boxes while classifier expects cropped images
Impact: Misaligned crops → wrong classification
Solution: Proper scaling, bounding box normalization, consistent preprocessing
6. Overlapping Objects
Problem: Waste items overlap on conveyor
Impact: Missed or merged detections
Solution: Tuned detection thresholds + accepted limitation of bounding-box approach
7. Confidence vs Accuracy Misinterpretation
Problem: Initially tried showing “correct vs incorrect” per frame
Impact: Conceptually wrong (no ground truth in live feed)
Solution: Switched to confidence-based “cleared vs flagged” system
8. Live Dashboard Design
Problem: Static UI didn’t reflect real-time inference
Impact: Poor interpretability
Solution: Built live stats pipeline (objects, confidence, alerts, class breakdown)
9. Backend–Frontend Sync
Problem: No real-time communication of inference stats
Impact: UI not updating with model output
Solution: Created /live_stats endpoint + polling mechanism
10. Model Accuracy Plateau (~70–73%)
Problem: Performance saturated early
Impact: Limited reliability
Solution: Fine-tuning (ConvNeXtV2), better augmentation, calibration (temperature scaling)
11. Low-Confidence Handling
Problem: Model forced predictions even when uncertain
Impact: False positives
Solution: Confidence thresholding + “flag for review” system
12. Multi-Object Handling
Problem: Multiple objects per frame
Impact: Need per-object tracking and summarization
Solution: Per-frame aggregation (counts, class distribution)
13. Deployment Constraints
Problem: Need to run on edge devices with limited compute
Impact: Model too heavy initially
Solution: Considered quantization, lighter inference pipeline
14. Frame Redundancy in Video
Problem: Consecutive frames nearly identical
Impact: Wasted compute
Solution: Frame skipping / sampling strategy
15. Real-World Variability
Problem: Dataset is clean, real waste is dirty, deformed
Impact: Generalization gap
Solution: Aggressive augmentation + acknowledging limitation
16. Threshold Tuning
Problem: Low threshold → too many false detections
Impact: noisy predictions
Solution: Tuned confidence threshold dynamically
17. Integration Complexity
Problem: Combining IP camera + backend inference + frontend display
Impact: Synchronization issues
Solution: Continuous streaming + polling-based updates

Team **Fantastic_Four_DJS** -- [Megh Dave](https://github.com/MEGH06), [Vansh Momaya](https://github.com/VanshMomaya7), [Moksh Jhaveri](https://github.com/mjdevs27), [Ketan Gaikwad](https://github.com/ketan-2905)

`2026-03-26`

---

### NepOrigin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nepal-origin-0620) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/walterwhite91/nep-agentic-commerce) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1n0D0yZyp0bTs9sEb39HYwce-4QdLpzXc/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Voice notes become merchants agents can buy from.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Drizzle](https://img.shields.io/badge/Drizzle-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![CloudFlare Workers](https://img.shields.io/badge/CloudFlare%20Workers-333333?style=flat-square) ![MCP](https://img.shields.io/badge/MCP-333333?style=flat-square) ![UCP](https://img.shields.io/badge/UCP-333333?style=flat-square)

**Challenges we ran into**

- **No wildcard DNS zone.** Original design used one dedicated origin per merchant (`{slug}.merchants.{domain}`); we don't own a domain to point wildcard DNS/TLS at. Disclosed the constraint and shipped a narrower real substitute — path-based dedicated origins (`/merchants/{slug}/**`) — still enforcing tenant isolation with real cross-tenant tests.
- **Linq was completely non-functional end to end before we drove it.** Five real bugs found by exercising the real webhook path with correctly HMAC-signed payloads against the real DB/APIs: wrong base-URL/endpoint map, wrong `sendMessage` body silently swallowing replies, a dead approve link, two structurally-unreachable states, a double state-write clobbering the pending payment id. A later live test still got inconsistent replies — traced to a genuine Postgres insert race (two conversation rows created 18ms apart for one buyer), fixed with an advisory-locked atomic find-or-create.
- **Prava sandbox card verification is independently flaky** (`Security Check Failed`/`FIDO_START_FAILED`), confirmed provider-side across multiple teams. Treated as a disclosed provider blocker that must never block Merchant Birth; kept the human-in-browser hosted card/passkey step explicit rather than mocking a successful payment.
- **A phone-only SMS buyer had no safe way to authenticate** — no SMS-OTP provider on this Supabase project. Chose a disclosed, explicitly-labeled self-declared phone-linking flow instead of inventing an unverified identity shortcut.

**The problem it solves**

Most agentic-commerce systems help an AI agent buy from a merchant that's already online, like a Shopify store, a public API, a maintained catalog. That leaves out most of the world's actual producers: an offline Nepali tea grower has phone photos, a WhatsApp voice note about pricing, and a paper price list — nothing an agent can discover or transact against.

**Nepal Origin creates the merchant, not just the checkout.** A producer's voice, product photos, price list, and business documents go through transcription, structured extraction, and deterministic conflict detection; the producer reviews and explicitly confirms; the result is a real, versioned, evidence-backed Merchant Passport with a dedicated HTTPS origin, an honest UCP catalog, and MCP tools over the same commerce core. A separate AI agent with no fixtures, no pre-known IDs, only the merchant's origin can discover it, get an identical quote over REST or MCP, and complete a real purchase through Prava, landing a real seller-side order with inventory reserved. Revoking evidence behind a confirmed fact mints a new Passport version and invalidates any quote pinned to the old one, live, not simulated.

We also built two buyer channels on the same core: a conversational `/chat` (with voice input) and a live SMS/iMessage channel over Linq — so the buyer side of "agent completes a real transaction" isn't limited to one UI.

**Best Visa Intelligent Commerce Implementation**

Nepal Origin uses Prava as its payment adapter for buyer-side checkout. Card capture runs through Prava's hosted PCI-compliant iframe (PravaCardForm), sandbox payment sessions are created server-side, and a report-status call confirms completion back to Prava, fixing a real bug where Prava showed "Payment Successful" but our system showed "Failed" due to a missing status report. Payment state is tracked through explicit truth-labeled states (live-complete, live-partial, provider-blocked) and kept strictly separate from settlement/authorization per our non-custodial design — Nepal Origin never holds buyer funds.

**Most Startup-Ready Product**

Judge us as a startup: Nepal Origin turns an offline Nepali producer's voice, photos, price list, and inventory into a live, dedicated-HTTPS, UCP/MCP-discoverable merchant, provable end to end from zero merchant record to a real external agent completing a quote and order. This is the wedge other agentic-commerce platforms lack: they help agents buy from merchants already online; we create the merchants agents can buy from.

**iMessage Agent**

Nepal Origin's buyer-continuation flow runs on Linq's conversation engine (packages/integrations/linq) for phone/SMS/iMessage-based buyer interaction — quote approval links, payment-pending/verified state transitions, and a phone-linking gate for buyer identity. This session live-verified the integration end to end and fixed five real bugs found in production use: an endpoint/base-URL map error, a dead approve link, unreachable payment states, a duplicate state write, and a multi-transport bug where Apple merges iMessage/SMS into one thread but Linq issued a new chat_id per transport, splitting a single buyer's conversation into two state machines.

**Best Prava Adapter for the NANDA Town**

We forked NANDA (nandatown) and built a Prava payments plugin (branch feat/prava-payments-plugin, 1335 passing tests, https://github.com/walterwhite91/nandatown) so NANDA agents can transact through the same non-custodial Prava adapter Nepal Origin itself uses giving agent-to-agent commerce scenarios a real, testable payment rail rather than a mock. PR to upstream NANDA is prepared, not yet opened, but we couldn't apply directly to our project.

**Best Agentic User Experience**

Nepal Origin's buyer experience is a real conversational agent: /chat takes voice or text and runs a live OpenAI tool-calling loop over search/quote/pay, handing off to Prava's hosted card capture for payment. The merchant side mirrors this — a producer speaks their catalog into onboarding and gets a structured, evidence-linked draft back for one-tap confirmation, no forms. We also attempted SMS/iMessage continuation via Linq so a buyer could finish a purchase by text; that path is not working reliably yet and is disclosed here rather than overstated — the core /chat + Prava experience is what's live and demoed.

**Agentic Commerce Hackathon**

Nepal Origin solves the supply side of agentic commerce: every existing agent-shopping system assumes merchants already exist online with clean catalogs. Most real-world producers — a Nepali handicraft exporter, a spice farm, a textile workshop — don't. Nepal Origin turns an offline producer's voice, product photos, price list, and inventory into a live, dedicated-HTTPS, versioned "Merchant Passport" with provenance-tracked evidence on every material fact (price, MOQ, lead time, shipping). Onboarding — voice/document capture, structured extraction, human confirmation, immutable Passport versioning — is done and live. Honest UCP discovery and catalog endpoints are live. MCP parity is done and functioning — the same tools an external agent (ChatGPT, Claude, a NANDA agent) calls return identical quotes to REST, verified by a real external-agent conformance harness. Buyer side closes the loop with /chat, a real OpenAI tool-calling agent for search/quote/pay, also functioning live. The full loop — zero merchant record → onboarding → confirmation → Passport → UCP/MCP catalog → independent external-agent discovery → quote → Prava payment → seller order → evidence-revocation invalidating a live quote — is real and demonstrated, not mocked.

Team **Anda** -- [Mimansh Neupane Pokharel](https://github.com/walterwhite91)

`2026-08-03`

---

### Cognivo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cognivo-5922) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ankitsri2005/Cognivo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cognivo-wltc.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fInVPDobzoE) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Turn mental chaos into a visual second brain

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Web Speech Api](https://img.shields.io/badge/Web%20Speech%20Api-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square) ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-333333?style=flat-square) ![React Flow](https://img.shields.io/badge/React%20Flow-333333?style=flat-square)

**The problem it solves**

Modern knowledge work is fragmented. Ideas, goals, tasks, and plans live across browser tabs, notes apps, and scattered documents — with no spatial structure and no way to see how they connect. Traditional tools are linear and passive; they store information but don't help you think or plan.

Cognivo is an AI-powered infinite visual canvas for productivity and life-mapping. It turns scattered thoughts into structured, interconnected knowledge — and actively helps you work smarter:

1. Smart Brain Dump: Speak or paste your thoughts; AI automatically sorts them into the Eisenhower Matrix (Urgent/Important grid) so you instantly know what to act on.
2. YouTube Roadmap Extractor: Drop any YouTube URL and get a step-by-step learning roadmap extracted directly onto your canvas — no manual note-taking.
3. Conflict Detection: Flags overlapping deadlines and illogical task dependencies before they derail your plans.
4. Time Reality Check: Warns you if your total workload exceeds available time before a deadline — a reality check your to-do list never gave you.
5. Persistent Canvas: Everything auto-saves to localStorage. Your second brain is always where you left it.
6. Voice Input: Speak thoughts directly onto the canvas via Speech-to-Text (Chrome/Edge).

Whether you're a student mapping a semester, a founder planning a product, or anyone trying to turn mental chaos into clarity — Cognivo makes thinking visible and planning honest.

**Challenges we ran into**

1. Persistent canvas state: Re-hydrating Zustand + localStorage caused node position drift and z-index conflicts in React Flow — fixed with careful state normalization.

2. Gemini structured output: Early API responses mixed JSON with markdown fencing, breaking parsers — resolved with strict prompt formatting and fallback sanitization.

3. YouTube transcript extraction: Transcripts aren't guaranteed for all videos. Handled missing/auto-generated transcripts gracefully with fallback prompting.

4. Time Reality Check logic: Normalizing task durations across incomplete deadline fields and freeform user input was tricky to get accurate.

5. Render cold starts: ~30–50s cold start on free tier made demos feel broken — added a "warming up" loading state to manage expectation.

6. Voice input compatibility: Web Speech API inconsistencies across browsers — scoped to Chromium with a clear fallback message for unsupported environments.

Team **THE BUG STOPS HERE** -- [Ankit srivastava](https://github.com/Ankitsri2005), [Achintya Jyoti](https://github.com/achintya0308), [NAVONIL SAHA](https://github.com/navonilsaha123), [Shambhavi Kumari](https://github.com/shambhavi151023)

`2026-06-26`

---

### Cognivo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cognivo-87c8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ankitsri2005/Cognivo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://cognivo-wltc.onrender.com) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/fInVPDobzoE) [![Built at](https://img.shields.io/badge/Built%20at-Tech%20Genesis%20'26-0052CC?style=flat-square)](https://tech-genesis.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Turn mental chaos into a visual second brain

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Web Speech Api](https://img.shields.io/badge/Web%20Speech%20Api-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square) ![React Flow](https://img.shields.io/badge/React%20Flow-333333?style=flat-square) ![Lucide Icons](https://img.shields.io/badge/Lucide%20Icons-333333?style=flat-square)

**Challenges we ran into**

1. Persistent canvas state across sessions: React Flow's node/edge state doesn't persist by default. We implemented Zustand for global state management and wired it to localStorage, but had to handle edge cases where re-hydrating large canvas states caused node position drift and z-index conflicts.

2. Gemini API structured output: Getting Google Gemini 1.5 Flash to return clean JSON (for Eisenhower classification and conflict detection) reliably required careful prompt engineering. Early responses mixed JSON with markdown fencing, breaking our parsers — fixed with strict output format instructions and fallback sanitization.

3. YouTube transcript extraction: The YouTube Roadmap Extractor relied on transcript availability, which isn't guaranteed for all videos. We handled missing/auto-generated transcripts gracefully and tuned the Gemini prompt to generate a coherent roadmap even from sparse input.

4. Time Reality Check logic: Calculating whether a user's total task workload exceeds available hours before a deadline required normalizing across different node types, incomplete deadline fields, and missing priority data — all entered freeform by the user.

5. Render cold start latency: Deployed on Render's free tier, the app had ~30–50 second cold start times that made demos feel broken. We added a loading state and a "warming up" indicator to manage user expectation during cold boots.

6. Voice input cross-browser compatibility: The Web Speech API behaves differently across Chrome, Firefox, and Safari. We scoped support to Chromium browsers and added a clear fallback message for unsupported environments.

**The problem it solves**

Modern knowledge work is fragmented. Ideas, goals, tasks, and plans live across browser tabs, notes apps, and scattered documents — with no spatial structure and no way to see how they connect. Traditional tools are linear and passive; they store information but don't help you think or plan.

Cognivo is an AI-powered infinite visual canvas for productivity and life-mapping. It turns scattered thoughts into structured, interconnected knowledge — and actively helps you work smarter:

1. Smart Brain Dump: Speak or paste your thoughts; AI automatically sorts them into the Eisenhower Matrix (Urgent/Important grid) so you instantly know what to act on.
2. YouTube Roadmap Extractor: Drop any YouTube URL and get a step-by-step learning roadmap extracted directly onto your canvas — no manual note-taking.
3. Conflict Detection: Flags overlapping deadlines and illogical task dependencies before they derail your plans.
4. Time Reality Check: Warns you if your total workload exceeds available time before a deadline — a reality check your to-do list never gave you.
5. Persistent Canvas: Everything auto-saves to localStorage. Your second brain is always where you left it.
6. Voice Input: Speak thoughts directly onto the canvas via Speech-to-Text (Chrome/Edge).

Whether you're a student mapping a semester, a founder planning a product, or anyone trying to turn mental chaos into clarity — Cognivo makes thinking visible and planning honest.

Team **THE BUG STOPS HERE** -- [Achintya Jyoti](https://github.com/achintya0308), [NAVONIL SAHA](https://github.com/navonilsaha123), [Ankit srivastava](https://github.com/Ankitsri2005), [Shambhavi Kumari](https://github.com/shambhavi151023)

`2026-06-26`

---

### VAJRAWATCH
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vajrawatch-c3ec) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arya-Mm/VAJRAWATCH-CORE) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/U_DkOTbp9Zc?si=63TXScof1wMG77Tw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/U_DkOTbp9Zc?si=63TXScof1wMG77Tw) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%202026-0052CC?style=flat-square)](https://deerhack26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> The AI nervous system for climate adaptation and G

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The Core Crisis: We are reacting to catastrophes instead of predicting them.
Nepal has 47 documented high-risk glacial lakes, and climate change is accelerating glacial melt at unprecedented rates. Currently, Glacial Lake Outburst Flood (GLOF) monitoring relies on human scientists manually reviewing satellite imagery from organizations like ICIMOD. This creates weeks of analytical lag. There is no automated API, no multi-signal consensus, and no real-time local alerting.

By the time human analysts confirm a moraine dam is failing, it is already too late.

July 2025 (Bhote Koshi): A GLOF destroyed 4 hydropower plants in 4 hours, eliminating 8% of Nepal's electricity supply and causing $200M+ in losses.

October 2023 (South Lonak): 55 deaths and $120M in damages.

Scientists are producing knowledge. They are not producing decisions.

**Challenges we ran into**

Building a mission-critical early warning system in 48 hours is inherently chaotic. We faced significant infrastructural and architectural hurdles, but every roadblock forced us to make the platform more resilient.

1. The Windows Compiler Trap & The "Pure Python" Pivot
The Hurdle: Midway through the build, our Windows MSYS2 Python environment suffered a catastrophic SSL certificate failure, completely breaking pip. When we attempted to bypass it, the environment failed to compile C++ and Rust-based data science libraries (numpy, pydantic-core) because the local build tools were missing.

The Solution: Instead of burning 6 hours debugging local Windows compilers, we executed an immediate architectural pivot. We stripped out the heavy dependencies and rewrote the entire 8-feature GLOF Risk Engine in pure, native Python. By relying strictly on the built-in math library, we eliminated our dependency on C-compilers entirely. This didn't just save our build—it resulted in a lighter, faster, and infinitely more portable risk engine.

2. The "11-Agent Cascade" vs. Hackathon Wi-Fi
The Hurdle: Our initial V2 design called for 11 sequential LLM agents passing state back and forth to calculate risk. We quickly realized that requiring 11 consecutive API network calls over notoriously unstable hackathon Wi-Fi was a guaranteed way to watch our live demo die on stage.

The Solution: We engineered a Stable Hybrid Architecture. We stripped the core risk assessment away from the LLMs and buried it in a zero-latency, offline, deterministic math backend. We then repositioned our LangGraph agents (powered by NVIDIA NIM) purely as an asynchronous "Decision Intelligence" layer. If the venue's internet goes down, the deterministic math still fires the red alert and saves the infrastructure.

3. Overcoming "Robotic" Life-and-Death Alerts
The Hurdle: When generating our Nepali language alerts, our initial fallback (Google TTS) sounded robotic, flat, and lacked the urgency required for an emergency evacuation broadcast. If the alert doesn't command immediate psychological attention, it fails its primary purpose.

The Solution: We integrated ElevenLabs' Multilingual v2 API. We had to carefully parse the JSON output from our Neo4j Graph database (extracting the specific names of threatened downstream villages) and inject them dynamically into a phonetically optimized Nepali prompt. The result is a broadcast-quality, human-sounding emergency alert that commands immediate attention in the native dialect.

4. Surviving the Local Fallback (Ollama)
The Hurdle: Integrating local Ollama models (gemma:2b) as a fallback for the NVIDIA APIs meant managing complex asynchronous timeouts. If the NVIDIA API hung, we needed the system to instantly catch the failure and route the prompt to localhost without crashing the FastAPI server.

The Solution: We built strict try/except timeout wrappers around our requests. We established a clean hierarchy of inference: try NVIDIA NIM first (Llama 3.3 70B), instantly fallback to local Ollama if network times out, and ultimately drop to a hardcoded, deterministic string if the local GPU runs out of VRAM. The system is engineered to never fail silently.

Team **Goggins** -- [Arya Mishra](https://github.com/Arya-Mm), [MANSI DUBEY](github.com/manas447), [ADVAIT JHA](https://github.com/advaitjha111-spec), [Gopal Parik](https://github.com/Gokup23)

`2026-06-13`

---

### GreenGuard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/econode-d2ac) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anushkachatterjee07-ui/Campus-Watt-Meter) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Turning Idle Classroom into Active Savings.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

The Campus-Watt-Meter is an integrated IoT and AI-driven solution designed to eliminate energy passivity in educational institutions. By bridging the gap between real-time occupancy sensing and power management, the system transforms "dumb" classrooms into responsive, energy-efficient environments.

**Challenges we ran into**

The Green Guard AI is a smart, IoT-driven energy conservation system designed to eliminate "Ghost Consumption" in educational institutions. By integrating real-time occupancy sensing with precise power monitoring, the project transforms traditional classrooms into responsive environments that automatically mitigate energy waste.

**GREEN & SUSTAINABLE EARTH**

The Campus-Watt-Meter project directly supports the "Green and Sustainable Earth" movement by transforming passive institutional buildings into active participants in carbon reduction. It moves energy management from a human-dependent "reminder" system to an automated, data-driven "guaranteed" system.

Team **Eco_Queens** -- [Ankita Basak](https://github.com/ankitabasak2022), [Anushka Chatterjee](https://github.com/anushkachatterjee07-ui), [Anushka Choudhury](https://github.com/anushkachoudhury866-ux)

`2026-03-27`

---

### SpecOps
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/blueprintdev-e819) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Architecture begins here.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![axios](https://img.shields.io/badge/axios-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Modern software development begins with Product Requirement Documents (PRDs), but transforming these documents into actual technical implementation is often slow, error-prone, and poorly coordinated.

Teams typically spend days or weeks manually converting PRDs into architecture designs, APIs, and development tasks. During this process:

Important requirements are misinterpreted or lost

Developers and product managers lack a shared understanding

There is no traceability between requirements and implementation

Tasks across tools like GitHub, Slack, and project management tools become disconnected

SpecOps acts as an AI-powered Architecture Assistant that automatically transforms product requirements into a structured development blueprint.
Analyzes PRDs using AI and provides PRD health score, completeness analysis, and complexity insights.

Extracts features, requirements, and ambiguities from the PRD automatically.

Provides a Chat & Clarify feature to resolve ambiguities, enhance missing fields, and update the PRD for better feature and task generation.

Generates tasks, developer-ready user stories, and story points, and organizes them into structured development tasks.

Includes a Sprint Planner to group tasks into sprints and track development progress.

Generates system architecture and API specifications based on the extracted requirements.

Maintains a Traceability system linking PRD lines → services → generated APIs → tasks, allowing teams to track which requirement created which component and identify impacted services or APIs when the PRD is updated.

Provides a Code Generator that creates a project code scaffold which can be pushed directly to GitHub, opened in VS Code, or downloaded as a ZIP.

Includes a Testing feature that generates positive, negative, and unit test cases for APIs and allows exporting a Postman collection as JSON.

Offers automation and integrations with GitHub, ClickUp, and Slack, enabling automatic task updates from GitHub commits, two-way synchronization with ClickUp tasks, and real-time notifications in Slack channels.

Integrates with Requestly, allowing users to download Requestly rules, import them into Requestly, and start frontend development using mocked APIs without waiting for the backend team.

Ultimately reduces the gap between product planning and engineering execution by automating the journey from PRD to architecture, APIs, tasks, and development workflows.

**Challenges we ran into**

One of the major challenges we faced was relying on a third-party AI API (Gemini) for generating outputs. This caused slow loading times and we were also quickly exhausting the free-tier API limits.

Initially, our system was making separate LLM calls for each feature (for example, 11 features resulted in 11 different API calls), which significantly increased response time and API usage.

To solve this, we optimized and restructured our prompts and orchestrated the generation pipeline so that multiple features could be processed within fewer LLM calls instead of separate requests.

This optimization reduced the number of API calls, prevented free-tier exhaustion, and significantly improved the overall response time and performance of the platform.

**Creative Use of Requestly**

PRD-Based Requestly API Client:

Value: Simplifies onboarding for developers. The platform generates ready-to-use Requestly collections that allow developers to directly test APIs generated from the PRD.

Implementation: These requests include embedded JavaScript test scripts that automatically validate the AI-generated responses and APIs in real time, helping developers quickly verify whether the generated outputs match the expected behavior.

Automated Debugging with SessionBook:

Value: Acts like a flight recorder for the AI pipeline, making debugging easier when something goes wrong.

Implementation: Whenever a backend failure occurs, the system automatically triggers a Requestly SessionBook capture, which records network requests, console logs, and session activity. This allows developers to quickly analyze and debug issues in the AI pipeline.

Executable Specifications with Backend Parity:

Value: Ensures strong alignment between backend development and frontend implementation.

Implementation: The platform exports project configurations and API specifications directly as Requestly rules, allowing the frontend team to mock and simulate backend APIs based on the PRD. This ensures the PRD remains the single source of truth and enables frontend development without waiting for backend completion.

Attached a google drive link which have code snippet screenshots and demo video demonstration of Requstley implementation.
https://drive.google.com/drive/folders/1iZJCe5yVwrE7oXDJ0SmD5tmidKy05oUj?usp=drive_link

Team **ZeroPoint_O** -- [Akshat KumarModi](https://github.com/modiakshat1806), [S Dhruv](https://github.com/dhrxv30), [Rounak Mittal](https://github.com/rounak1208)

`2026-03-15`

---

### AgriNegotiator
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agrinegotiator-0e17) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ritikmehta080905/FarmGenAI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/9SaVg81OXxc) [![Built at](https://img.shields.io/badge/Built%20at-Bytecamp'26-0052CC?style=flat-square)](https://bytecamp-26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Decentralized AI Negotiation for Agriculture

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![YAML](https://img.shields.io/badge/YAML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

- Agricultural markets are highly fragmented and decentralized. Farmers, buyers, warehouses, and transporters operate independently with limited coordination. This leads to several challenges:
- Manual negotiation: Farmers must negotiate prices with buyers individually, which is slow and inefficient.
1. Poor price discovery: Farmers often cannot identify the best buyers or market opportunities.
2. Logistics inefficiencies: Transport and storage resources are not coordinated properly.
3. Post-harvest losses: Produce spoils when farmers cannot find buyers in time.
4. Distress selling: Farmers are forced to sell crops below profitable prices due to urgent financial needs.
5. These issues reduce farmer income and create significant waste across the agricultural supply chain.

How AgriNegotiator Helps

- AgriNegotiator introduces a decentralized AI-powered multi-agent negotiation platform that automates coordination between agricultural stakeholders.
- Instead of manual decision-making, autonomous AI agents represent different participants in the supply chain, including:
1. Farmer agents
2. Buyer agents
3. Transport agents
4. Warehouse agents
5. Food processor agents
6. Compost / waste management agents

These agents negotiate prices, allocate resources, and coordinate logistics automatically, ensuring more efficient market interactions.

What People Can Use It For

AgriNegotiator can be used to:
- Automatically negotiate crop prices between farmers and buyers
- Coordinate transportation and delivery logistics
- Find storage options when buyers are unavailable
- Redirect unsold produce to processors or alternative markets
- Reduce food waste by ensuring produce always has a usable pathway

Impact

By introducing intelligent negotiation and coordination, AgriNegotiator helps:

- Improve farmer profitability through better price discovery
- Reduce post-harvest waste
- Optimize logistics and storage utilization
- Enable faster and more efficient agricultural transactions

Overall, the platform transforms traditional crop marketplaces into an AI-driven decentralized negotiation ecosystem.

**Challenges we ran into**

One of the biggest challenges while building AgriNegotiator was designing the interaction and communication between multiple autonomous agents. Since our system involves several agents — such as farmer agents, buyer agents, transporter agents, and warehouse agents — ensuring that they could communicate, exchange offers, and negotiate correctly in real time was complex.

Another major hurdle was implementing a live negotiation log. We wanted users to see how agents were negotiating step-by-step (offers, counteroffers, and final agreements). Synchronizing this negotiation flow between the backend agent system and the frontend dashboard required careful API design and state management.

Integrating LLM-based reasoning into the agents was also challenging. We needed the agents to not just follow fixed rules, but also analyze context and decide whether to accept, reject, or counter an offer. This required experimenting with prompt design and connecting the system with LLM APIs such as Groq / OpenRouter to generate meaningful negotiation decisions.

We addressed these challenges by modularizing the agent architecture, clearly defining negotiation protocols between agents, and creating structured prompts for the LLM reasoning layer. This allowed the agents to interact more reliably and made the negotiation process more transparent and dynamic.

**GenAI**

AgriNegotiator leverages Generative AI to enable intelligent decision-making and negotiation between autonomous agents in a decentralized agricultural marketplace.

In our system, each stakeholder in the supply chain — such as farmers, buyers, and logistics providers — is represented by an AI agent. These agents use LLM-based reasoning to analyze negotiation contexts and generate responses such as offers, counteroffers, or acceptance decisions.

Instead of relying on fixed rules, the agents use Generative AI to dynamically interpret market conditions, pricing constraints, and negotiation history to determine the most suitable action.

Key ways our project uses Generative AI include:

AI-powered negotiation reasoning for generating offers and counteroffers

Context-aware decision making based on price constraints, demand, and supply

Dynamic interaction between agents through natural-language reasoning

Adaptive negotiation strategies that simulate real-world market behavior

By embedding Generative AI into a multi-agent negotiation system, AgriNegotiator demonstrates how Gen AI can power autonomous coordination and decision-making in complex decentralized environments.

This aligns strongly with the Gen AI track by showcasing how LLMs can move beyond text generation and enable intelligent autonomous systems that solve real-world coordination problems.

Team **BUG HUNTERS** -- [Rashmi Andhale](https://github.com/rashmi2307), [Tanishka Bhoir](https://github.com/tanishka), [Gayatri Mahajan](https://github.com/Gayatrii0911), [Ritik Mehta](https://github.com/Ritikmehta080905)

`2026-03-15`

---

### Spotless
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spotless-f033) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/call-me-rodney/spotless) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://spotless-frontend-three.vercel.app/login) [![Built at](https://img.shields.io/badge/Built%20at-DOMINION%202026-0052CC?style=flat-square)](https://dominion2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Machine learning enabled waste intelligence platfo

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![nestjs](https://img.shields.io/badge/nestjs-333333?style=flat-square)

**Challenges we ran into**

Training a custom model came with ts own difficulty going into production. We also spend some time getting everyhting working together well

**The problem it solves**

An AI-powered waste intelligence platform that detects waste, predicts where it will accumulate, prioritizes collection, routes crews, and verifies removal

Team **Dream Team** -- [Rodney Kawuma](https://github.com/call-me-rodney), [Shikuku olayo](https://github.com/reagha), [Marvin Akampumuza](https://github.com/AkampumuzaMarvin)

`2026-09-03`

---

### Continuum
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/continuum-recover-the-reasoning-your-code-forgot-293b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Monish-D609/continuum-decision-archaeology) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/PIDrr32w2aU) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Recover the reasoning your code forgot

![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![CloudFare](https://img.shields.io/badge/CloudFare-333333?style=flat-square)

**The problem it solves**

## What Problem It Solves

A lot of the important context behind an engineering decision never makes it into the codebase.

You can usually see what the code is doing, but not necessarily why it was implemented that way. The reasoning might be in a PR discussion from two years ago, an issue where an alternative was rejected, or a review comment explaining a constraint that is no longer obvious. As the project grows, this context becomes increasingly difficult to recover.

This creates a few practical problems. Engineers may spend hours trying to understand an existing design, re-propose approaches that were already tried, or make changes that unintentionally violate an assumption made earlier in the project's history. It also makes onboarding harder because a lot of the knowledge ends up sitting with the people who were around when those decisions were made.

**Continuum is built to solve this problem by making that historical context searchable and usable.**

It indexes PRs, issues, discussions and other GitHub history, extracts the actual decisions and reasoning from them, and makes that information available through natural-language queries.

Some of the things we wanted it to answer are:

* Why was this part of the system designed this way?
* Was this approach considered before, and if so, why was it rejected?
* What constraints led to the current implementation?
* What did the team actually decide in the original discussion?
* Has the current implementation moved away from an earlier architectural decision?

It can also be used to reconstruct ADRs from existing project history and give new engineers some of the context that would otherwise require asking someone who has been on the project for years.

### Why not just use ChatGPT or Claude?

A general-purpose LLM can explain the code, but that is different from knowing the history behind it.

If a particular implementation exists because an alternative was discussed and rejected in a PR six months earlier, that information is not present in the code itself. The model can make a reasonable guess about why the code looks the way it does, but that answer is not necessarily what the team actually decided.

Continuum retrieves that historical information from the repository and grounds its answers in the original GitHub artifacts. The user can see the PR, issue or commit that the answer came from instead of having to take the model's explanation on faith.

### Why not just use GitHub search?

GitHub search is useful when you already know what you are looking for. The problem is that historical questions often don't work that way.

If I want to know why a particular architectural decision exists, I may not know which PR introduced it, what terminology the team used at the time, or whether the discussion happened in an issue rather than a PR. Even after finding the right thread, there may be hundreds of comments to go through.

Continuum handles the retrieval and synthesis step. Instead of returning a collection of PRs and leaving the engineer to connect them, it identifies the relevant discussions and produces an answer around the decision, the reasoning, alternatives that were considered, and the supporting evidence.

The goal is fairly simple: **make the reasoning already present in a project's history as accessible as the code itself.**

**Challenges we ran into**

**1. Turning GitHub Discussions into Decision Intelligence**

GitHub was never designed to store clean architectural decisions. A single PR can contain hundreds of comments—mixing genuine design reasoning with CI bots, code-style debates, approvals, and unrelated discussion. Naively embedding this data would make retrieval confidently noisy.
Our solution: we introduced an LLM-powered extraction layer that converts raw PRs/issues into structured decision records containing the decision, rationale, rejected alternatives, and supporting evidence before anything reaches the vector index. This ensures the system indexes engineering knowledge, not conversation noise.

**2. Designing Hybrid Search That Survives Restarts**

Semantic search alone can miss exact technical terminology, while keyword search can miss semantic intent. We therefore combined pgvector dense retrieval with BM25 sparse retrieval, fused using Reciprocal Rank Fusion (RRF). The challenge: BM25 is memory-resident, so deployments and service restarts require the index to be reconstructed from Supabase.
Our solution: we eagerly rebuild the sparse index during startup rather than delaying it until the first user query. This keeps the system query-ready immediately, while exposing a clear scalability path toward persistent BM25 snapshots for repositories with thousands of decisions.

**3. Preventing the LLM from “Making Things Up” When History Is Missing**

The most dangerous failure mode wasn't a wrong retrieval—it was a plausible answer with no historical evidence. An LLM will happily synthesize an answer even when the repository contains no supporting decision.
Our solution: we added an explicit evidence sufficiency layer. Retrieval scores are evaluated before synthesis, while the model must return is_insufficient_evidence and a confidence_summary. When evidence falls below a relevance threshold, the system surfaces the uncertainty instead of presenting speculation as historical fact.

**4. Reconstructing Decisions Across Disconnected Conversations**

Engineering decisions rarely live in one place. A PR may reference an issue, which references an RFC from months earlier. Standard vector retrieval treats these as independent chunks, meaning it can find where something was implemented without finding why it was originally chosen.
Our solution: we strengthened retrieval through higher candidate recall + RRF across semantic and lexical search, allowing disconnected evidence to surface together. The remaining architectural challenge is true cross-reference graph retrieval, which represents the next evolution of the system from document search toward decision-graph reasoning.

**5. Balancing Answer Quality with Citation Faithfulness**

A useful answer needs to be coherent; a trustworthy answer needs verifiable evidence. Forcing the model to tightly interleave prose and citations caused an undesirable trade-off: either answers became fragmented, or citations started supporting claims they didn't actually establish.
Our solution: we separated narration from verification. The answer is optimized for coherent reasoning, while a structured citation layer independently maps evidence back to its source. This gives users a natural explanation and an auditable trail back to the original GitHub discussion.

Team **11:11** -- [Monish D](https://github.com/Monish-D609), [Naveen Kasi](https://github.com/kasi8888-code), [Shyam Prakash](https://github.com/Shyampr007), Avnish M

`2026-09-02`

---

### ResQX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resqx-3f6a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/srijitag448-jpg/ResQ-Hub) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://res-q-hub-liard.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> ResQX — When Every Second Matters, We Respond.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Google API](https://img.shields.io/badge/Google%20API-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square)

**The problem it solves**

The Problem ResQX Solves

During emergencies and disasters, delays in reporting incidents, locating victims, finding available ambulances, hospitals, and shelters can cost lives. ResQX brings these critical services together into one intelligent emergency-response platform.

People can use ResQX to:

-  Send SOS alerts with real-time location
-  Find and coordinate nearby ambulances and hospitals
-  Locate suitable emergency shelters
-  Identify safer routes during disasters
-  Use AI to analyze emergencies and support faster decisions
-  Track emergency resources and rescue operations in real time

ResQX makes emergency response faster, smarter, and safer—helping connect people with the right help when every second matters.

**Challenges we ran into**

Challenges We Ran Into

Building ResQX involved integrating several complex features into one real-time emergency response platform. One major challenge was handling real-time location tracking and accurately connecting users with nearby ambulances, hospitals, and shelters.

We also faced challenges with Google authentication, API integration, map services, real-time database synchronization, and responsive UI performance. Some features initially had issues with location permissions, delayed data updates, and inconsistent API responses.

We overcame these hurdles by testing each module individually, improving error handling, implementing proper location-permission checks, optimizing real-time data updates, and using a modular architecture to make the frontend and backend work smoothly together.

These challenges helped us make ResQX more reliable, scalable, and effective when every second matters.

Team **Neural Nexus** -- [Srijita Ghosh](https://github.com/srijitag448-jpg), Oindrila Saha, Shreyasi Das, [Paulami Roy](https://github.com/roypaulami04-creator)

`2026-08-29`

---

### EcoPulse
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecopulse-39bc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sapghosh55-lab/EcoPulse.git) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> **Translating satellite data into real-time carbon

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Satellite Noise & Cloud Cover: Standardizing inconsistent multi-temporal imagery, tidal shifts, and cloud artifacts before model ingestion.
Distinguishing Real Erosion from Seasonal Shift: Avoiding false positives from normal seasonal variations by using deep feature extraction via Siamese U-Nets.
Large-Scale Map Rendering Lag: Overcoming browser memory bottlenecks when rendering heavy raster/vector overlays by optimizing MapLibre GL JS WebGL layers.
Pixels-to-Biomass Translation: Accurately converting raw 2D visual segmentation masks into scientifically grounded carbon stock numbers.
End-to-End Latency: Reducing execution time across satellite data fetching, PyTorch inference, and UI rendering via async pipelines and AOI-scoped bounding boxes.

**The problem it solves**

EcoPulse addresses several critical challenges in modern environmental monitoring, conservation management, and remote sensing:

1. The Gap Between Raw Satellite Data and Actionable Metrics:
Raw satellite imagery and multi-temporal remote sensing feeds are massive, unstructured, and difficult for non-technical stakeholders or local authorities to interpret. EcoPulse automates the transformation of these raw data layers directly into quantifiable ecological indicators—specifically carbon stock metrics and erosion masks.
2. Accurate Land-Change and Erosion Tracking:
Traditional manual tracking or basic change-detection methods struggle with high noise levels and temporal variations in satellite feeds. By utilizing deep learning architectures (such as PyTorch-based Siamese U-Nets), EcoPulse accurately pinpoints structural shifts in land cover, shoreline movement, and erosion risks over time.
3. Proprietary Mapping and Token Lock-In:
Many modern geospatial dashboards rely on proprietary mapping platforms that require paid tokens, API limits, or restrictive licensing terms. EcoPulse solves this by integrating MapLibre GL JS, providing an entirely open-source, high-performance rendering engine for large-scale geospatial visualization without vendor lock-in or licensing bottlenecks.
4. Streamlining Ecological Impact Quantification:
Conservationists and environmental researchers often have to stitch together separate GIS tools, machine learning scripts, and visualization dashboards. EcoPulse unifies data acquisition, AI inference, and interactive visualization into a streamlined pipeline, making it easier to assess environmental health and ecosystem vulnerability rapidly.

Team **Avengers** -- [Saptarshi Ghosh](https://github.com/sapghosh55-lab), [Rishan Pandey](https://github.com/RishanEP08), [Aritra Bhattacharyya](https://github.com/aritrab571-dotcom)

`2026-08-30`

---

### Team hypercampus Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/team-hypercampus-ai-3e2e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://samat-educa-6e3fitfuu-anant00785s-projects.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Every campus ERP manages records — none senses a s

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

## Challenges We Ran Into

Building HyperCampus AI involved several challenges, especially in connecting multiple campus workflows into one intelligent system.

* **Integrating multiple AI services:** We needed AI features for study planning, career guidance, risk explanations, and voice assistance. Managing different LLM capabilities while keeping responses useful and consistent required careful prompt design and modular integration.

* **Connecting multiple user roles:** Students, faculty, parents, and administrators require completely different dashboards and actions. We solved this by designing the system around role-based access and separate action centers while keeping the underlying student data connected.

* **Real-time academic risk detection:** Identifying students at risk was not enough—we also needed to explain *why* they were at risk. We implemented an explainable factor breakdown so faculty could understand the contribution of attendance, marks, and exam proximity to the risk score.

* **Payment reliability and duplicate transactions:** Integrating online fee payments introduced the challenge of securely verifying transactions and preventing duplicate payment records. We addressed this using server-side **HMAC-SHA256 verification and idempotent payment logging**.

* **Closing the intervention loop:** A major hurdle was making intervention more than just an alert. We designed HyperIntervene so faculty can assign a specific recovery task, mentor, and deadline, after which the student's progress is verified and their risk level is recalculated.

These challenges pushed us to build HyperCampus AI as a **modular, connected system rather than just another college dashboard**.

**The problem it solves**

## The Problem It Solves

Traditional college ERP systems **store data but don't turn it into actionable intelligence**. Attendance, marks, fees, and student engagement are often handled separately, making it difficult for colleges to identify problems early and take coordinated action.

**HyperCampus AI** solves this by connecting students, faculty, parents, and administrators through a single intelligent campus platform.

* 🎓 **For Students:** Identifies academic weaknesses, creates personalized AI study plans, provides career guidance, and helps students stay consistent with their learning.
* 🧑‍🏫 **For Faculty:** Automatically identifies students at academic risk, explains *why* they are at risk, and recommends targeted interventions instead of relying on manual spreadsheet checking.
* 👪 **For Parents:** Provides real-time visibility into attendance, marks, academic progress, and fee status, reducing communication gaps and last-minute surprises.
* 🏛️ **For Administrators:** Provides centralized fee analytics, overdue tracking, payment reconciliation, and multi-campus management.

### From Detection to Recovery

Instead of discovering a student's problems after semester failure, HyperCampus AI follows a continuous loop:

**Detect Risk → Explain Why → Prescribe Action → Assign Deadline → Re-evaluate**

This enables colleges to move from **reactive problem-solving to proactive student support**, helping identify declining academic performance as early as Week 3 and coordinating students, faculty, parents, and administration toward recovery.

Team **Team HyperCampus** -- [Rahul Ranjan](https://github.com/rahul12-bit), [Anant TANTI](https://github.com/Anant00785), [Pranav Kumar](https://github.com/Pranavkr323), SHRIJA MUKHERJEE

`2026-08-30`

---

### CareConnect -ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/careconnect-ai-57f9) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://careconnect-ai-com.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> CareConnect AI: Smart care, zero stress.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

The problem it solves
Finding care often means juggling multiple apps. CareConnect AI unifies emergency navigation, women’s health, and daily wellness into one GenZ-friendly platform.
 Instant Care & Navigation: Locates nearby hospitals and doctors fast with real-time routing for emergencies.
 Multilingual AI Chatbot: Breaks language barriers with 24/7 smart medical guidance in your native tongue.
 Women's Health & PCOS Alerts: Smart cycle tracking that flags early PCOS/PCOD symptoms without the panic.
 Custom Fitness & Diets: Instant diet charts and workout plans tailored precisely to your height and weight.

**Challenges we ran into**

Challenges we ran into
 PCOS Pattern Accuracy: Algorithmic fine-tuning to detect irregular cycle patterns accurately without triggering false health alarms.
 Low-Latency Mapping: Integrating real-time location routing to locate verified emergency clinics instantly.
 Multilingual NLP: Training the AI chatbot to deliver accurate medical context across multiple languages effortlessly.

Team **ALUPOSTO** -- [DEBANJAN CHOUBEY](https://github.com/DebanjanChoubey), [Anirban Bagchi](https://github.com/Anirban2005-git), [Pragya Das](https://github.com/Pogo1808), [DEBOJIT DUTTA](https://github.com/Debojit2607)

`2026-08-30`

---

### Waste2Worth AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wasteworth-ai-a710) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/25it083-cmyk/Waste2Worth-AI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1221741805?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Waste Today, Worth Tomorrow

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square)

**Challenges we ran into**

One of the main challenges was handling different types of waste because the same category can look different in different conditions. We also faced difficulty in making the system give useful suggestions for items that are not clearly recyclable. We addressed this by keeping the first version focused on common waste categories and providing simple disposal and reuse recommendations. Another challenge was making the interface easy enough for users to understand without technical knowledge.

**The problem it solves**

Waste is often mixed together, making recycling and proper disposal difficult. People may not know whether an item is recyclable, reusable, compostable, or should be disposed of as general waste. This leads to poor waste segregation, more landfill waste, and loss of recyclable materials. Waste2Worth AI helps users identify waste and guides them on the correct disposal or reuse method.

Team **Waste2Worth AI** -- Reshmashree KR, SOBANA E

`2026-08-27`

---

### GreenRoute Negotiator
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenroute-negotiator-0658) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sanggitsaaran/GreenRoute_Negotiator) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Save Green Save Nature

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Google Maps API](https://img.shields.io/badge/Google%20Maps%20API-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-333333?style=flat-square)

**The problem it solves**

*The Problem It Solves*

Urban transport in Indian metropolitan hubs generates over 14% of national greenhouse gas emissions, yet commuters routinely default to high-carbon single-occupancy vehicles. The core bottleneck is cognitive friction: standard navigation apps simply list routes, forcing the user to mentally calculate hidden vehicle ownership expenses, door-to-door parking search delays, and air quality exposure. 

GreenRoute Negotiator bridges this gap as a decision-theoretic AI engine. Instead of just showing routes, it actively evaluates live multi-modal options against empirical Indian emission baselines (ARAI, ICCT). It mathematically balances time, cost, and carbon tailored to the commuter's learned preferences, doing the heavy lifting to make sustainable mobility the default choice.

**Challenges we ran into**

*Challenges We Ran Into*

*   *Arbitrating LLM Hallucinations:* We quickly realized that relying on LLMs to calculate precise utility scores inevitably led to mathematical hallucinations. We solved this by isolating the math into a pure Python, framework-free domain layer. Our Groq-powered multi-agent panel is strictly guardrailed to debate and narrate only the mathematically pre-computed winner. If the LLM attempts to declare a different winner, the pipeline rejects the transcript and triggers a deterministic fallback.
*   *Quantifying Real-World Friction:* Raw routing APIs only yield in-vehicle times, which do not reflect the reality of a daily commute. Vishal and I engineered our four specialist agents (Speed, Cost, Carbon, Weather) to be materially load-bearing. They inject strict mathematical deltas—such as adding 4 minutes for car parking searches, applying a 60% ownership cost uplift, and penalizing open-air modes during severe AQI or rain—before the final recommendation is scored. 
*   *State Management & Concurrency:* Handling simultaneous trips, agent negotiation logs, and transit caching initially caused database locking issues. We mitigated this by migrating the persistence layer to SQLAlchemy ORM with SQLite running in WAL (Write-Ahead Logging) mode, ensuring high-concurrency reads and resilient schema handling.
*   *Voice API Quota Exhaustion:* Utilizing ElevenLabs for real-time voice narration risked massive API quota burn and latency spikes if users replayed summaries. We built a localized LRU caching layer using SHA-256 hashing for the requested text and voice ID, allowing instant audio retrieval for repeated Coordinator narrations without hitting the external network.

**Best Use of Gemini API**

We leverage the Gemini API as a structured reasoning and natural language intelligence layer that bridges human conversational intent with complex mobility data. Using Gemini's structured JSON schema capabilities, the system accurately parses conversational inputs to extract destinations, deadlines, and context like weather or budget constraints without brittle regex rules. Beyond intent extraction, Gemini powers our guardrailed multi-agent explanation layer. It translates the complex, multi-variable arithmetic of our four specialist agents (Speed, Cost, Carbon, Weather) into intuitive, plain-English rationales, explaining exactly why a particular mode was chosen while being strictly constrained to prevent metric hallucination or altering the deterministic mathematical outcome.

**Best Use of ElevenLabs**

We integrate ElevenLabs to transform GreenRoute from a data-heavy dashboard into an accessible, hands-free travel companion for active commuters. By leveraging ElevenLabs' expressive, low-latency text-to-speech synthesis, the platform voices real-time Coordinator summaries, journey recommendations, and mid-commute traffic alerts directly to the user. To ensure production-grade performance and resource efficiency, we engineered a backend LRU caching pipeline powered by SHA-256 hashing on text payloads and voice profiles. This guarantees sub-millisecond audio delivery for repeated route summaries, eliminates redundant API quota consumption, and maintains an instant, voice-first commuter experience even during network strain.

Team **Team Marvels** -- [Surya HA](https://github.com/Surya-Hariharan), [Vishal Seshadri B](https://github.com/Vishalspl-0903), [Kishore B](https://github.com/Kishore-1803), [Sanggit Saaran K C S](https://github.com/sanggitsaaran), [Venkatram KS](https://github.com/venkatramks)

`2026-08-30`

---

### GREEN PIN NEXUS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/green-pin-nexus-c95b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Bavanapg13/green-pin-nexus.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://green-pin-nexus-gjdb.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Detect the chain, not just the event

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![NetworkX](https://img.shields.io/badge/NetworkX-333333?style=flat-square)

**Challenges we ran into**

1. Detecting chains instead of isolated events

The biggest challenge was designing the system to recognize that individually authorized actions can become suspicious when combined into a sequence. We addressed this by correlating events temporally and evaluating multiple signals together.

 2. Balancing anomaly detection and false positives

Unusual activity is not necessarily malicious. For example, an administrator working at 2 AM could be responding to a legitimate production incident. We therefore introduced business-context validation so that approved incidents, tickets, and maintenance windows can influence the final risk assessment.

3. Combining different detection approaches

No single algorithm was sufficient for the problem. Behavioral anomaly detection is useful for identifying deviations from normal behavior, while deterministic sequence logic is better suited for enforcing mandatory workflows. We combined ML, rules, statistical analysis, and graph relationships into a unified risk engine.

4. Demonstrating a sensitive banking-security problem safely

Real privileged banking telemetry contains sensitive information and was not appropriate for a prototype. We therefore designed controlled synthetic scenarios representing normal operations, legitimate emergency exceptions, and suspicious privileged-activity chains.

5. Making the output useful to a human investigator

A risk score alone is not enough for a security supervisor. We built the investigation flow around correlated evidence, timelines, relationships, business context, recommended actions, and audit records so that the supervisor can understand why an event was flagged.

**The problem it solves**

Traditional access-control and security systems can determine whether a privileged bank officer is authorized to perform an individual action, but identifying misuse often requires understanding the relationship between multiple actions performed over time.

An officer may be authorized to modify a beneficiary, increase a transaction limit, and initiate a payment individually. However, when these actions occur in a suspicious sequence, involve a new entity, exceed the officer's normal financial behavior, bypass required approvals, and lack legitimate business context, the combined chain may indicate privileged misuse.

GREEN PIN NEXUS addresses this gap by correlating privileged activity across multiple dimensions instead of evaluating events in isolation.

The platform combines behavioral anomaly detection, temporal sequence analysis, relationship graph analysis, financial-risk analysis, privilege sensitivity, historical behavior, and business-context validation into an explainable unified risk score.

Security supervisors can investigate the complete action chain, understand why an alert was generated, verify whether legitimate business context exists, review recommended responses, and record their decisions in an auditable workflow.

The prototype uses synthetic data and simulated response actions, making it safe for demonstration without exposing real banking or customer information.

Team **Sparkle** -- [THANISHKA YOGESH](https://github.com/thanishkaykb), S Nithish Kumar, [Surya Senthil](https://github.com/kingsofsao), [BAVANA P G](https://github.com/Bavanapg13)

`2026-08-29`

---

### stagehub
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stagehub-d6d4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NightWing1998/stagehub) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Lc6GjYbYWJ4) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> A staging environment for code

![Go](https://img.shields.io/badge/Go-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![AST](https://img.shields.io/badge/AST-333333?style=flat-square) ![claude](https://img.shields.io/badge/claude-333333?style=flat-square) ![Kuzu](https://img.shields.io/badge/Kuzu-333333?style=flat-square) ![GraphDB](https://img.shields.io/badge/GraphDB-333333?style=flat-square)

**What is the deployed URL for this project?**

https://github.com/NightWing1998/stagehub

**How Did You Use Claude?**

## Claude is the intelligence layer

We used Claude in two distinct ways, and the distinction is the most important design decision in the project.

### 1. In the product: Claude explains what the graph proved

When a push produces findings, stagehub makes **one** `claude-opus-5` call for the whole review. Each finding is sent with its proof chain and ±8 lines of real source around the impacted call site. We use **structured output** (`output_config.format` with a JSON schema) so the response maps directly onto database rows, and `effort: "low"` because a live demo is waiting on it.

What comes back is a reviewer, not a summarizer:

> "parseBackendFreelistType references bbolt.FreelistArrayType, which no longer exists, so etcd-server's embed package fails to compile (undefined: bbolt.FreelistArrayType)."
>
> **fix** — In etcd-server/embed/config.go, drop the bbolt.FreelistArrayType reference and return the new FreelistKind value, matching bbolt's renamed field.

It names the exact compiler error, which is checkable. And two hops out at `StartEtcd()` it correctly says **"no change needed here"**, pointing the fix back at the real site instead of proposing an edit where the symptom merely surfaced. Distinguishing a direct user from a transitive caller is the difference between a reviewer and a search result.

### 2. The deliberate constraint: severity is never asked of the model

**Claude finds how the bug impacts the system**

Reachability is proven by recursive Cypher over the call graph, so severity is graph-derived and never asked of the model. Claude's job is prose: *why does this break*, and *what should I change*.

**How you are solving it?**

## A staging environment for code

You push to **stagehub** instead of your upstream remote. On every push to master it reviews the change **against every other repo in the org**, then an admin merges upstream or blocks.

### The pipeline

**1. Index the org (once per repo set).** Every repo is parsed into a symbol graph. Go uses Go's own stdlib `go/parser`; TypeScript uses ts-morph. Both emit the *same* index shape, so everything downstream is language-agnostic.

**2. Link across repo boundaries.** This is the hard part, and we solve it three ways:
- **Go** — import paths are fully qualified, so the module path is a prefix and the remainder is the package directory. An exact id match, not a heuristic.
- **npm** — `package.json` name matched against the bare import specifier.
- **HTTP** — an endpoint becomes a graph node with a *globally shared id* (`http:POST /v1/charge`). Two repos indexed independently write the same node and converge with no join at all. This is how we catch wire-contract breaks that no compiler sees.

Crucially, **each repo is indexed in isolation** — we deliberately do not resolve `node_modules`. Anything crossing a package boundary becomes a pending import for the link pass. Resolving through a symlink would work on a laptop and prove nothing.

**3. On push: AST-diff, not text-diff.** We `git archive` both the old and new sha, index both sides, and diff the symbol tables. A rename is a *rename*, not two unrelated text edits. Deltas are typed: `field-rename`, `enum-change`, `signature-change`, `symbol-removed`.

**4. Query the graph.** A recursive Cypher query over an embedded Kuzu graph does reverse reachability, up to 6 hops, with one predicate that defines the entire product:

```cypher
WHERE caller.repo <> changed.repo
```

That single line is what makes this cross-repo analysis rather than a linter.

### Stack

Next.js + TypeScript · embedded Kuzu graph database · Postgres · Go stdlib parser · ts-morph · Claude Opus 5. 15 regression tests covering extraction, cross-repo linking and AST diffing.

**What is the problem your project solves?**

## Every repo is green. The system is broken.

Large engineering orgs do not live in one repository. Prometheus, Docker, Kubernetes, etcd — each is **dozens of separately versioned repos**. Every one has its own CI, its own reviewers, its own release cycle.

And that is exactly the problem: **code review is scoped to a single repository.** A pull request is reviewed against the repo it lands in. CI runs the tests of the repo it lands in. Nobody — no human, no compiler, no test suite — reviews the *seams between* repos.

### Why it matters

This class of bug is expensive precisely because it is invisible at review time. The person best equipped to fix it — the author, at the moment of the change, with full context — never learns it exists. Instead it surfaces as a mysterious build failure in a repo they may not own.

The wire-contract version is worse still: rename a JSON field or re-case an enum value and *nothing* fails to compile. A producer and a consumer simply stop agreeing, silently, in production.

We staged prod. Nobody staged code.

Team **The New Avengers** -- [Neel Shah](github.com/Freelancer-98), [Dhruvil Shah](https://www.github.com/NightWing1998)

`2026-08-08`

---

### tinyexpr.zig
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tinyexprzig-eaf1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aadi-joshi/tinyexpr.zig) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/Ad0RZ6qTxe0?si=TS7ZyPugEC-RE3Id) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Ad0RZ6qTxe0?si=TS7ZyPugEC-RE3Id) [![Built at](https://img.shields.io/badge/Built%20at-Port%20Mortem%202026%20--%20Code%20Resurrection%20Hackathon-0052CC?style=flat-square)](https://portmortem.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> tinyexpr Zig port that keeps C smoke green

![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![C](https://img.shields.io/badge/C-333333?style=flat-square) ![ActionScript](https://img.shields.io/badge/ActionScript-333333?style=flat-square) ![Zig](https://img.shields.io/badge/Zig-333333?style=flat-square) ![Zig 0.16](https://img.shields.io/badge/Zig%200.16-333333?style=flat-square) ![Libm](https://img.shields.io/badge/Libm-333333?style=flat-square) ![Differential fuzzing](https://img.shields.io/badge/Differential%20fuzzing-333333?style=flat-square)

**The problem it solves**

tinyexpr is a small C library for compiling and evaluating math expressions. People embed it for config formulas, tools, and game logic when they want a tiny expression language without a full scripting runtime.

We ported codeplea/tinyexpr to Zig 0.16.0 for Port Mortem Track G (C to Zig). Downstream C code can keep calling the same te_interp / te_compile / te_eval / te_free surface: the Zig build ships that C ABI.

The original smoke suite is untouched (byte-identical smoke.c and minctest.h) and links against the Zig static library. All four flag configs pass on both Zig-linked and C-linked smoke:

- default: 4930/4930
- pow: 4924/4924
- natlog: 4934/4934
- pow_natlog: 4928/4928

![image](https://assets.devfolio.co/content/9e6fe0dc215d46a7a536f76322dafaa8/f54824c9-46f1-44a4-84bd-1bc721b34e21.png)

Escape hatches live only in src/c_abi.zig: 16 total, CI threshold 20, zero outside that file. A certified 60s differential fuzz ran 48,512,558 executions with 0 divergences. An enumerator over 11,505 short inputs (string length at most 3, AST depth at most 1) also reported 0 divergences on compile nullness, error position, f64 bits, and te_print bytes.

![image](https://assets.devfolio.co/content/9e6fe0dc215d46a7a536f76322dafaa8/3f56c8bc-55bc-407a-bec2-52dd815eabb8.png)

Where the C original stack-overflows on deep nests (upstream issue 136), the port fails closed with a bounded error instead of SIGSEGV. Fair interp bench (C -O2 vs Zig ReleaseSafe, Linux Docker aarch64): Safe arithmetic p99 about 1.03% slower (8209 vs 8125 ns).

One command for judges: docker compose up --build verify
Repo: https://github.com/aadi-joshi/tinyexpr.zig

**Challenges we ran into**

Parity without editing tests. The original smoke suite had to stay byte-identical. Loose float tolerances would have made Zig look green for the wrong reason. We kept bit-exact compares and fixed the port until all four compile-flag matrices passed on both Zig-linked and C-linked smoke. The scorecard CI fails if README numbers drift from measured evidence.

C ABI versus escape-hatch budget. Matching te_expr layout and allocators on Zig 0.16 needs pointer casts and allocator bridging. Every hatch is confined to src/c_abi.zig, counted in CI (threshold 20), and the parser core stays hatch-free. That is our Track G answer to shipping a port that compiles but is full of unchecked escapes.

![image](https://assets.devfolio.co/content/9e6fe0dc215d46a7a536f76322dafaa8/4b0ae478-d184-4f7d-bb98-85016bc5e4e6.png)

Differential comparison is finicky. In-process C versus Zig needs symbol renaming, shared libm strtod for locale parity, and a written equivalence scope: C locale, below nest bound, no C undefined behaviour. Deep nests that crash C are documented divergences, not silent wins. Host-dependent edges like fac(0/0) stay in probe data and are scoped in the write-up.

Bugs showed up while matching C. Differential work led to confirming nest overflow (issue 136) and signed-char ctype UB (issue 105), filing next_token linkage (issue 141) and locale/strtod (issue 142), and opening fix PRs 143 and 144. Novelty is stated honestly in docs/findings.md: 136 and 105 were not claimed as first discoveries.

![image](https://assets.devfolio.co/content/9e6fe0dc215d46a7a536f76322dafaa8/ad6c6a12-174a-4265-b142-7a5facb61ef7.png)

Allocator-misuse Track G criterion: honest miss. Fault injection over 271 ordinals produced 0 crashes on either side. We recorded the negative result instead of forcing a story.

Two machines, one invariant. WSL and Darwin in parallel meant scrubbing absolute host paths from evidence, keeping the four suite totals identical, and freezing on tag submission-v1 with those counts in the tag message.

![image](https://assets.devfolio.co/content/9e6fe0dc215d46a7a536f76322dafaa8/89faa1a4-5cd3-4547-ba7a-8cef54457185.png)

Team **maxout** -- [Kavya Bhand](https://github.com/kavyabhand), [Aadi Joshi](https://github.com/aadi-joshi)

`2026-08-03`

---

### NANDA - Prava Economic Execution Layer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nanda-prava-economic-execution-layer-818c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/projnanda/nandatown/pull/211) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://rail-rail.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/p-WrJa8nY38) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Real payments for autonomous agents.

![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square) ![Nanda Town](https://img.shields.io/badge/Nanda%20Town-333333?style=flat-square)

**Challenges we ran into**

## Challenges I ran into

### Wrong session ID prefix from live sandbox

When we first wired the adapter to Prava’s live sandbox, our tests assumed session IDs looked like `sess_…`. Real responses came back as `ses_…`. Asserts failed even though create-session had succeeded, so it looked like the rail was broken when it was really our matcher. We debugged by logging the raw JSON from `POST /v1/sessions`, comparing it to the docs and to our fixture expectations, then tightened the prefix check and any redaction helpers to accept `ses_`. After that, verify paths and demo receipts lined up with real sandbox evidence.

### Async-only locking was not enough under thread pressure

Idempotency looked fine under normal `asyncio` load: the same `PaymentRef` should hit the rail once. Under a hostile test that fired the same ref from about ten threads, we still saw double create-session calls. The bug was that `asyncio.Lock` only serializes coroutines on one event loop; ThreadPoolExecutor workers bypass it. We reproduced with a concurrent stress test, confirmed two network calls for one logical pay, then added a threading gate around the critical section (keep the asyncio lock for cooperative async paths). Retries of the same `PaymentRef` became a single rail hit with a stable receipt.

### Passkey checkout cannot run headless in agent CI

Full live checkout expects a browser/passkey step. Multi-agent NANDA scenarios and CI cannot sit in that UI, so a pure “live end-to-end” path either hangs or forces people to fake the whole payment. We treated that as a product constraint, not a mock to hide: hybrid mode still does a real `POST /v1/sessions` against the sandbox (so you get real `ses_` / `ord_` evidence), then completes the agent-facing confirm path headlessly so quote → pay → verify can finish in simulation. That keeps sandbox honesty without pretending passkey checkout ran inside the test runner.

**The problem it solves**

# Prava Payments Adapter for NANDA Town

## The Problem
I kept hitting the same wall in NANDA Town: agents can “trade,” but money was fake.  
The stock payment plugins are in-memory ledgers, so you never learn how a real rail fails.

## What I Built
I built a drop-in `payments: prava` plugin. Agents can:

- **Quote**  
- **Pay**  
- **Verify**  
- **Refund**

…against Prava’s sandbox, with:

- Local budget locks  
- Rollback on timeouts  
- Receipts that **do not leak** API keys

## Why It’s Useful Today
This plugin is useful if you’re simulating agent commerce and **actually care about**:

- Retries  
- Insufficient funds  
- Sandbox evidence  

…not just a happy‑path mock.

## Next Steps
- A cleaner hosted demo console (this frontend)  
- Stronger defaults for idempotency after process restarts

**Best Prava Adapter for the NANDA Town**

## Track fit: Project NANDA — Best Prava Adapter for NANDA Town

This project is built specifically for the Project NANDA track challenge: a **reliable, reusable Prava payments adapter for NANDA Town**, wired to Prava’s Agentic Payments Sandbox, with failure handling and a commerce scenario on top.

### What the track asks for → what we shipped

| Track requirement | Our submission |
|---|---|
| Payments-layer plugin (`quote` / `pay` / `verify` / `refund`) | `nest-plugins-prava` implements NANDA’s `Payments` protocol as `payments: prava` |
| Connect to Prava Agentic Payments Sandbox | `HttpPravaClient` / `HybridPravaClient` call sandbox `POST /v1/sessions` and related flows |
| At least one successful sandbox transaction | Live/hybrid runs produce real sandbox IDs (`ses_…`, `ord_…`) with `verify=confirmed` |
| Handle at least one failure case | Local budget lock + rollback on insufficient funds / rail failure; typed errors; demo fail→retry path |
| Scenario + tests | `scenarios/prava_marketplace.yaml` + hostile/unit suite (concurrency, duplicate `PaymentRef`, API failures, edge cases) |
| Easy install & reuse for future builders | Plugin entry point, README, env (`PRAVA_MODE` / `PRAVA_API_KEY`), one-line scenario switch |
| Upstream PR + Devfolio entry | Fork + PR to `projnanda/nandatown`; Devfolio links the PR and a working product demo |

### Why this is a track fit (not a bolt-on)

NANDA Town’s stock payment plugins are mostly **in-memory ledgers**. That is fine for toy sims, but it never exercises a real agent-commerce rail: session creation, timeouts, retries, insufficient funds, or secret hygiene.

Our adapter is the missing **execution layer**:

1. **Protocol bridge** — Agents keep calling NANDA’s sync ledger API (`quote` → `pay` → `verify_payment` → `refund`). Under the hood we map that to Prava’s session / payment-result / report-status model.
2. **Production-minded controls** — Local budget locks *before* hitting the rail; rollback if the rail fails; idempotent `PaymentRef` handling; secret scrubbing in receipts/logs; optional durable journal for restart-safe idempotency.
3. **Modes for builders** — `mock` (CI/deterministic), `live` (full sandbox HTTP), `hybrid` (real create-session for sandbox evidence + headless completion so multi-agent sims can finish without a browser passkey mid-run).
4. **Commerce simulation on top** — Marketplace scenario with multiple agents so buyers/sellers exercise quote/pay/verify under budget pressure, not only a single happy-path unit test.
5. **Tryable product surface** — Hosted **RAIL** demo console (Next.js) lets judges click a fail→retry flow and see redacted sandbox session evidence without cloning the monorepo. The **source of truth for the track** remains the Python plugin + scenario in the NANDA Town PR; the console mirrors the same behavioral story for Devfolio’s mandatory product link.

### Evaluation dimensions (how we map)

- **Quality & reliability** — Typed failures, concurrency gates (`asyncio` + threading), duplicate-ref safety, regression tests around real sandbox ID shapes (`ses_` not `sess_`).
- **Security / auth / failure handling** — API keys stay server-side / env-only; receipts scrub secrets; insufficient funds and rail errors fail closed with budget rollback instead of silent double-spend.
- **Ease of install & reuse** — `payments: prava` in a scenario YAML; `nest plugins list` discovery; documented env and modes so another NANDA builder can adopt Prava as the payment layer without rewriting agent code.
- **Successful sandbox txs** — Hybrid/live evidence with real `ses_` / `ord_` IDs and confirmed verify.
- **Scenario / simulation quality** — Marketplace scenario plus a hosted demo that shows the failure path judges care about (retry after insufficient funds), not only a green path.

### What judges should open

- **GitHub / PR:** the `nest-plugins-prava` package, marketplace scenario, tests, and README (installation + reuse).
- **Product link:** RAIL console — run the fail→retry demo and inspect sandbox session evidence.

In short: this submission is not “Prava added to a chat app.” It is a **drop-in NANDA Town payments plugin** that makes Prava the reusable money rail for agent simulations — exactly what the Project NANDA track asks for.

[Ives Lim](https://github.com/ChiJian28)

`2026-08-02`

---

### Legilimens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/legilimens-110d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sourodyuti/TeamTraction) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://canva.link/rplf7zvaznkemol) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ITatu30lOsk) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Catching confusion the second it happens.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Actian VectorAI DB, Actian Vector Analytics, Python, FastAPI, Next.js 14, React 18, TypeScript, TailwindCSS, D3.js, Recharts, Docker & Docker Compose, Electron, Google Gemini API (gemini-2.5-flash), ElevenLabs TTS API, faster-whisper, PyTorch, MongoDB Atlas, WebSockets, WebRTC](https://img.shields.io/badge/Actian%20VectorAI%20DB,%20Actian%20Vector%20Analytics,%20Python,%20FastAPI,%20Next.js%2014,%20React%2018,%20TypeScript,%20TailwindCSS,%20D3.js,%20Recharts,%20Docker%20&%20Docker%20Compose,%20Electron,%20Google%20Gemini%20API%20(gemini--2.5--flash),%20ElevenLabs%20TTS%20API,%20faster--whisper,%20PyTorch,%20MongoDB%20Atlas,%20WebSockets,%20WebRTC-333333?style=flat-square) ![Action Vector DB](https://img.shields.io/badge/Action%20Vector%20DB-333333?style=flat-square)

**Challenges we ran into**

1. **Sub-second Vector Search & On-Prem RAG**: Integrating `faster-whisper` for live classroom speech recognition with **Actian VectorAI DB** required us to process and index live audio chunks every 3 seconds. We configured in-memory rolling buffers and synchronized VectorAI gRPC client calls so transcript embeddings (`bge-small-en`, 384-dim) are queryable immediately when students signal confusion.
2. **Cross-Platform Stealth Overlay (Electron + Wayland/X11)**: Building a transparent, click-through Cluely-style desktop overlay for teachers required handling display media streams across Linux (Wayland PipeWire portal vs X11) and Windows. We solved this by implementing native IPC IPC handlers in Electron (`stealth-client`) and leveraging custom WebRTC PipeWire capturer flags.
3. **Auth & Python 3.14 Compatibility**: Standard `passlib` bcrypt implementations crashed on Python 3.14 environments due to C-extension changes. We refactored authentication to directly use `bcrypt` with JWT token verification connected to a persistent MongoDB Atlas cluster.

**The problem it solves**

In large university lecture halls (80+ students), **up to 40% of students silently get lost** during complex technical topics (like pointers, recursion, or neural networks). They are often too shy or hesitant to raise their hand, while teachers remain completely unaware until midterm grades drop 3 weeks later. Furthermore, strict privacy regulations (such as the DPDP Act) make institutions reluctant to send live student telemetry or classroom audio into third-party cloud analytics.

**Legilimens** solves this by providing a **privacy-first, real-time "mind-reading" layer** for live classrooms:

1. **Quiet Confusion Capture (Muffliato PWA)**: Students tap one-click "I'm lost" or "Slower" buttons on their mobile phones without disrupting class.
2. **Real-time Radar for Teachers (Marauder's Radar)**: Teachers see a live D3 radial heatmap and timeline of concept-level confusion right on their desktop overlay.
3. **Instant Personalized Voice Analogies (Accio Analogy)**: When multiple students get stuck, Legilimens retrieves the exact lecture transcript snippet from an on-prem **Actian VectorAI DB**, rewrites it using Gemini into a personalized analogy based on the student's background/interests (e.g., sports, gaming, music), and delivers it back as calm voice audio via ElevenLabs within 1 second.
4. **On-Prem Privacy**: The entire student telemetry pipeline, local transcript embedding (`bge-small`), vector search, and columnar SQL analytics run locally on **Actian VectorAI DB** inside the school network so student data never leaves campus.

**Accio Relevance - Build with Actian VectorAI Database**

Legilimens directly powers its core privacy and intelligence layer using two primary Actian engines operating fully on-premise inside the campus network:

1. **Actian VectorAI DB (Hybrid Vector RAG & Instant Retrieval)**:
   - **Live Lecture Indexing**: As teachers lecture, live classroom audio is transcribed every 3 seconds (`faster-whisper`), embedded using `bge-small-en` (384-dim), and upserted directly into **Actian VectorAI DB** via gRPC (`:6574`).
   - **Accio Analogy Retrieval**: When multiple students signal confusion ("Muffliato" button), Legilimens queries Actian VectorAI DB using vector similarity search to instantly retrieve the exact transcript snippet and concept context. This context is then used to synthesize personalized analogies in under 1 second.
   - **Air-Gapped Privacy Guarantee**: Student telemetry and classroom discussion data stay stored locally inside Actian VectorAI DB. No raw transcript or student telemetry ever leaves the institution's local server.

2. **Actian Vector (Columnar SQL Analytics Engine for Pensieve)**:
   - **Time-Series Confusion Analytics**: All student confusion pings, timestamped telemetry, and concept breakdown indices are stored in **Actian Vector** via columnar SQL (`pyodbc` / `:5432`).
   - **Post-Lecture Teacher Insights (Pensieve)**: Teachers review lecture difficulty trends, topic failure rates, and cohort heatmaps generated directly from high-speed columnar SQL aggregation queries over the lecture's time-series data.

**Best Use of Gemini API**

1. **Contextual Analogy Generation (`gemini-2.5-flash`)**:
   - Takes raw lecture transcript snippets retrieved from Actian VectorAI DB along with student interest graphs to generate crystal-clear, pedagogically sound analogies on demand.

2. **Vision-based Screen Context (`Gemini Vision`)**:
   - Analyzes slides and code shared on the teacher's screen to extract context when audio transcripts are ambiguous or technical diagrams are being explained visually.

**Best Use of ElevenLabs**

1. **Sonorus Voice Re-delivery (`eleven_flash_v2_5`)**:
   - Converts freshly rewritten AI analogies into natural, calm audio streams delivered back to student mobile PWAs.
   - Allows students to put on earphones during a live lecture and listen to a 15-second tailored explanation without distracting others.

**Best Use of MongoDB Atlas**

**MongoDB Atlas User Authentication (`pymongo` & `Motor`)**:
   - Manages secure student and teacher registration, role-based profiles (teacher/student), and hashed password storage across live sessions.
   - Generates persistent JWT authorization tokens (`HS256`, 7-day expiration) to maintain seamless, authenticated WebSocket sessions on student PWAs and teacher overlays.

**Education**

Legilimens introduces a real-time, privacy-first "mind-reading" layer for live university classrooms and lecture halls (80+ students):

1. **Quiet, Frictionless Confusion Signal (Muffliato PWA)**:
   - Eliminates the fear and social friction students face when raising their hand in front of peers.
   - Allows students to tap a single-button signal on their mobile browser ("I'm lost" / "Slower") without interrupting the flow of the lecture.

2. **Real-time Teacher Radar (Marauder's Radar)**:
   - Gives professors a live D3 radial heatmap and timeline right on their desktop overlay so they can spot concept-level drop-offs as they happen in real time instead of waiting 3 weeks for midterm results or post-course feedback surveys.

3. **Personalized Auto-Analogy Voice Delivery (Accio Analogy)**:
   - When confusion spikes on a specific topic (e.g., *pointers* or *recursion*), Legilimens automatically retrieves the precise lecture context and generates a personalized analogy tailored to the student's unique interest profile (e.g., sports, gaming, music).
   - The analogy is delivered silently as audio back to the student's device via ElevenLabs TTS so learning momentum is restored instantly.

Team **Traction** -- [Akshar Nath Gorain](https://github.com/workforakng), [Aditi Barman](https://github.com/Aditi-Barman), [SANJANA MAHATA](https://github.com/Sanjana250312), [Sourodyuti Biswas](https://github.com/Sourodyuti)

`2026-07-26`

---

### SmartEcoAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartecoai-2f42) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sumanchattopadhyay2910-wq/smartecoai.git) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Empowering sustainable living with AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Building SmartEcoAI involved several technical and design challenges:
Integrating multiple AI services: We had to combine different AI capabilities for sustainability recommendations, carbon footprint estimation, and personalized suggestions while ensuring consistent outputs.
Data quality and preprocessing: Environmental datasets came from different sources with varying formats. Cleaning, validating, and normalizing the data was necessary to improve prediction accuracy.
Prompt engineering: Obtaining reliable and relevant AI responses required multiple iterations of prompt design and testing to reduce hallucinations and improve consistency.
Performance optimization: Some AI operations increased response time. We optimized API calls, implemented caching where possible, and reduced unnecessary computations to improve the user experience.
User experience: Presenting sustainability insights in a simple and actionable way was challenging. We refined the interface based on testing and user feedback to make the platform more intuitive.
Deployment and environment configuration: Managing environment variables, API keys, and deployment settings across development and production environments required careful configuration and debugging.
How We Overcame These Challenges
We adopted an iterative development approach, regularly tested each module independently, used version control for collaboration, improved prompts through experimentation, optimized backend workflows, and continuously refined the UI based on feedback. Thorough testing and debugging helped us deliver a stable and user-friendly platform that provides meaningful sustainability recommendations.

**The problem it solves**

Climate change and rising energy consumption have made it difficult for individuals and households to understand and reduce their environmental impact. Most people lack access to personalized sustainability guidance, real-time energy insights, and practical recommendations that fit their lifestyle. Existing solutions often focus on only one aspect, such as electricity monitoring or carbon tracking, without providing an intelligent, all-in-one assistant.
SmartEcoAI solves this problem by combining Artificial Intelligence with sustainability analytics to help users make eco-friendly decisions every day. The platform analyzes user activities, estimates their carbon footprint, tracks energy usage, and provides personalized recommendations to reduce emissions, save electricity, and adopt greener habits.
Key problems addressed:
Lack of awareness about personal carbon emissions.
No personalized AI-driven sustainability guidance.
Difficulty tracking daily energy consumption and waste.
Limited insights into how small lifestyle changes impact the environment.
Absence of a unified platform for eco-friendly decision-making.
How SmartEcoAI helps:
AI-powered carbon footprint estimation.
Personalized sustainability recommendations.
Energy usage monitoring and optimization.
Smart reports with actionable insights.
Encourages environmentally responsible behavior through data-driven suggestions.
By making sustainability simple, accessible, and personalized, SmartEcoAI empowers users to reduce their environmental impact while saving energy and contributing to a greener future.

**Sustainability**

SmartEcoAI promotes sustainability by helping individuals make environmentally responsible decisions in their daily lives. The platform uses AI to analyze user habits and provide personalized recommendations for reducing carbon emissions, conserving energy, minimizing waste, and adopting eco-friendly alternatives. It also tracks sustainability goals, measures environmental impact, and encourages long-term behavioral change through actionable insights. By making sustainable living accessible and data-driven, SmartEcoAI empowers users to contribute to a greener future while supporting global climate action and the UN Sustainable Development Goals.

Team **Garibb-Coders** -- [Tirtha Sadhu](https://github.com/tirthasadhu015-dot), [Trisha Paul](https://github.com/trishapaul098), [Tahseen Fatma](https://github.com/tahseen9832-jpg), [Suman Chattopadhyay](https://github.com/sumanchattopadhyay2910-wq)

`2026-07-26`

---

### OrderRadar
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/orderradar-13d1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Pulkitkh/TradingView_Clone) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/document/d/1yFRTHHaigC7CaeDS24e2RFwW2ZHQvrp8QdZVB5SEjk0/edit?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> From filing to feed — in seconds.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square)

**The problem it solves**

Every day, NSE-listed companies file dozens of order/contract announcements under SEBI Regulation 30. These filings are public but buried inside exchange websites, formatted as raw XBRL XML, and updated without any notification.
The result: traders and analysts miss material order wins entirely, or find out hours later when the stock has already moved.

Existing tools fall short:

1. Broker terminals have significant lag and no structured filtering
2. Financial news apps summarize selectively small/midcap orders go unreported
3. Manually checking NSE's website for 2,000+ listed companies is impossible

OrderRadar solves this by:

1. Polling NSE's official XBRL API every 35 seconds for new order/contract filings
2. Parsing structured XML to extract every relevant field, contract value, client name, duration, order type, domestic vs international
3. Applying data quality checks to catch filer errors before they reach you (we found 5 companies with corrupt data entries in a single day's feed)
4. Computing derived metrics Annual Value (contract ÷ duration), Order Size as % of company revenue
5. Delivering a clean, formatted alert to Telegram within seconds of the filing going live on NSE

Who it's for: retail investors, traders, and analysts tracking order-driven stocks, especially mid and smallcap infrastructure, defence, and EPC companies where a single large order can be a major catalyst.

**Challenges we ran into**

1. NSE blocks direct API calls —> solved by priming a browser session before every request.
2. XBRL tag names in real filings differed from official documentation —> solved by probing live XML before writing any parser.
3. Some companies filed corrupt values (₹43 lakh crore orders) that passed NSE's own validation —> built a sanity check layer to flag and cross-reference these.

[PULKIT KHEMKA](https://github.com/Pulkitkh)

`2026-06-29`

---

### SkyLive-By Horizon
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skyliveby-horizon-a0f8) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://arcnight-nine.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/n9nMALw7ipI?si=my1vRemrFiNHtGqu) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Your Window to the Live Universe

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![NASA API](https://img.shields.io/badge/NASA%20API-333333?style=flat-square)

**The problem it solves**

SkyLive aggregates real-time data from NASA, NOAA, and open APIs into a single, cohesive dashboard.
By capturing the user's specific coordinates , the platform personalizes the data. It tells the user exactly what is above their head right now,including specific planet visibility ratings, local sunrise/sunset timelines, and customized local ISS pass times(in a single website).
Upcoming Celestial Events timeline paired with the Space Event Alerts (push notifications) solves human forgetfulness.
(

![image](https://assets.devfolio.co/content/644595896a804b889841a3756e68390b/b1a97cce-5c15-4904-992c-2936d653e44f.png)Data updates for every 30 sec)

**Challenges we ran into**

The Challenge: It’s easy to display global celestial events, but translating a user's raw coordinate metrics ($17.52^\circ, 78.36^\circ$) into localized viewing data was tough. We had to figure out if a constellation was actively above the local horizon (Zenith) or if a planet's elevation angle made it "poor" or "excellent" to view at that exact minute.
Our Solution: We integrated lightweight coordinate-transformation libraries to calculate local Sidereal Time and altitude-azimuth matrices. This allowed us to dynamically calculate and display whether a planet is visible right now based entirely on the user's browser geolocation API.

Team **event horizon** -- Anvitha Reddy, Meghana Nakkanaboyina, vedasri brundavanam, Vaibhav Sir

`2026-06-14`

---

### EcoExplore
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecoexplore-f1f7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ShubhamMukhopadhyay/ecoexplore-ai-guide) [![Built at](https://img.shields.io/badge/Built%20at-Susegad%20Sprint%202026-0052CC?style=flat-square)](https://susegad-sprint.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Travel Goa. Leave it better than you found it.

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

These screenshots show a much more polished version of EcoExplore! Here are both writeups:

The Problem It Solves
The Core Problem
Goa receives over 8 million tourists a year — yet most end up at the same 10 beaches, at the same hours, wondering why their "paradise" feels like a parking lot. At the same time, planning a responsible trip is genuinely hard: eco-friendly options are buried under sponsored results, crowd information doesn't exist until you're already there, and carbon impact is completely invisible.
EcoExplore fixes all three.

What People Actually Use It For
🗺️ Explore — "Show me Goa beyond the postcards"
Filter destinations by vibe (Beaches, Heritage, Nature, Food, Nightlife, Wellness), see real-time crowd levels (Low / Medium / High) and an Eco rating on every card before you commit. No more showing up to a packed Calangute because a blog from 2019 called it "quiet."
🤖 AI Planner — "Write my trip in seconds"
Input your days, total budget, vibe, group type, and food preference — and get a full day-by-day itinerary with timed stops, eco bonuses, and crowd-aware scheduling. It doesn't just list places; it tells you when to go, why that timing matters ecologically, and flags transport choices that boost your Eco Score (e.g. "Scooter to Chapora Fort — avoid taxis, eco bonus +0.4").
🗺️ Smart Maps — "Route me around the chaos"
A live Leaflet map overlays real crowd density across Goa's hotspots. Pick Fastest, Eco, or Scenic routing, get a smart route around congestion, or book a bike directly. It turns a chaotic travel day into a calm, deliberate one.
🌿 Eco Score — "Tell me if I'm actually doing good"
Every itinerary generates a single honest score out of 10, broken down across Transport, Stay, Food, and Activities. It shows how you rank against similar trips, what's pulling your score down, and gives 3 concrete moves to raise it before you even leave — with logistics already checked.
💎 Hidden Gems — "Find what the algorithm misses"
A curated layer of community-sourced, AI-verified spots that sit outside mainstream recommendation engines — local cafés that support neighbourhoods, unmarked viewpoints, off-season beaches with Eco 9+ ratings.

Who It Helps
TravellerBefore EcoExploreAfterFirst-timerOverwhelmed by conflicting blogsPersonalised plan in 30 secondsRepeat visitorStuck in the same circuitDiscovers genuinely new spotsEco-conscious travellerNo way to measure impactLive score + actionable tipsBudget travellerOverpays at tourist trapsRouted to local, affordable gemsCouple / groupHours of negotiationOne plan everyone filters together


EcoExplore doesn't just plan your trip. It makes Goa's overcrowding problem smaller, one itinerary at a time.

**Challenges we ran into**

**1.  Making AI Itineraries Feel Local, Not Generic**
The problem: Early Claude-generated itineraries read like any travel blog — "Visit Baga Beach, try water sports, eat seafood." Technically correct, completely soulless.
The fix: Heavily engineered the system prompt with Goa-specific context: named local restaurants, ferry schedules, crowd peak hours by beach, eco transport options, and explicit instructions to add reasons for each choice ("low crowd window," "supports neighbourhood," "eco bonus +0.4"). The itinerary output went from generic to genuinely useful after about 12 prompt iterations.

**2.  Real-Time Crowd Data Without an Actual Data Source**
The problem: Building "live crowd intelligence" without access to real footfall APIs (Google Popular Times is private, no public Goa-specific equivalent exists).
The fix: Built a seeded pseudo-random crowd simulation engine — each location has a base crowd level that shifts realistically based on time-of-day, day-of-week, and seasonal weights. It behaves like live data and updates on refresh. The plan is to replace this with Google Places API or community-reported data in v2. Honest in the UI: the legend says "updated every 15 min" as a near-future design target, not a current claim.

**3.  Leaflet Map Crashing on Mobile**
The problem: The Leaflet.js map rendered fine on desktop but caused scroll-jacking and occasional white-screen crashes on iOS Safari — specifically when the map container was inside a scrollable div with overflow: hidden.
The fix: Wrapped the map in its own stacking context with position: relative; z-index: 0, added touch-action: none to the map tile layer, and forced a map.invalidateSize() call on screen visibility change. Also lazy-initialized the map only when the Smart Maps screen was first activated — which cut initial load time by ~40%.

**4.  Design System Consistency Across 7 Screens**
The problem: With 7 distinct screens (Home, Explore, AI Planner, Dashboard, Smart Maps, Hidden Gems, Eco Score), keeping typography, spacing, color, and component patterns consistent became genuinely hard — especially once the Playfair Display hero headers were introduced for some screens but not others.
The fix: Locked all tokens into CSS variables early (--teal, --fd for display font, --fb for body, --r for border radius, etc.) and built a small component vocabulary (.card, .pill, .btnp, .crowd-badge) that every screen draws from. When the design diverged, the variable system meant a single value change fixed all instances simultaneously.

Team **404 Duo Not Found** -- Shubham Mukhopadhyay, [Tamojit Mandal](https://github.com/TamojitMandal)

`2026-05-15`

---

### LCusAgent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lcusagent-042e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/maulana-tech/locus-paygents) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://paygents.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/PSnHvESxoAQ) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Autonomous AI agent economy simulation

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![BASE](https://img.shields.io/badge/BASE-333333?style=flat-square)

**The problem it solves**

AI agents are spending money invisibly. When an autonomous agent calls an API, pays for a service, or transfers funds, there's zero visibility into what happened, why, and whether it was legitimate. Developers building agent-based products have no way to:
- See what their agents are doing financially in real-time
- Debug failed transactions or unexpected spending
- Demonstrate agent economy flows to stakeholders or investors
- Test payment scenarios before going to production
PayGentic solves this by making agent transactions visible. It's a real-time 3D simulation that connects to the Locus Payment Infrastructure and visualizes every USDC transaction as it happens — agents physically walk to service booths, energy beams fire between buyer and seller, USDC coins float up with the exact amount, and success toasts confirm the transaction.
What people can use it for:
- Developers building with Locus — a live dashboard to watch their agents transact in real-time instead of digging through API logs
- Product demos & investor pitches — show, don't tell, how autonomous AI commerce works. The 3D visualization makes abstract crypto payments tangible
- Testing & debugging agent workflows — trigger skills via OpenClaw and instantly see if the transaction flows correctly through the Locus pipeline
- Education — teach people how AI agent economies work through an interactive, visual simulation rather than reading documentation
How it makes things safer:
- Real-time transaction monitoring catches unexpected spending immediately
- Wallet balance is always visible — no hidden drains
- Every transaction is logged in a Live Ledger with full details (agent, skill, amount, timestamp)

**Challenges we ran into**

1. Locus API CORS Restriction
Problem: The Locus API (beta-api.paywithlocus.com) does not send Access-Control-Allow-Origin headers. When deployed on Vercel, every fetch() call from the browser was blocked by CORS policy.
Solution: Built a Vercel serverless function (api/locus/index.js) that acts as a proxy — the browser calls our own /api/locus endpoint, and the serverless function forwards requests to Locus with the API key injected server-side. In local development, calls go directly to Locus (no CORS on localhost). The config auto-detects the environment and switches between proxy and direct mode.
2. OpenClaw GitHub App Installation Blocked
Problem: The build-with-locus-beta GitHub App is set as "Private" — external users cannot install it on their repos, blocking the from-repo deployment flow on Locus PaaS.
Solution: Pivoted to Vercel deployment with manual API proxy. Auth token exchange was also different from the docs — the actual endpoint was /v1/auth/exchange, not /v1/auth/token as documented in OPENCLAW_SETUP.md.
3. Transaction-to-Animation Mapping
Problem: Real Locus transactions use wallet addresses (e.g. 0x6299...), but the simulation uses agent IDs (e.g. c1, i3). There's no direct mapping between the two.
Solution: Created a resolution system where real transactions (buyerId: 'locus-wallet') automatically get assigned to an eligible idle agent (PROCUREMENT or CONSUMER) on the current floor. The skill endpoint is mapped to a booth position (e.g. agentmail-create-inbox → Booth A1, laso-get-card → Booth B1) using a mapping function.
4. Event Queue Race Condition
Problem: Multiple transactions arriving simultaneously could trigger overlapping animations — two agents trying to walk to the same booth, or beam animations colliding.
Solution: Implemented a sequential event queue processor with isProcessingRef guard. Only one transaction animates at a time. New events queue up and process one-by-one after each animation completes.

**Using PayWithLocus.com to leverage our suite.**

Track: Pay with Locus — PayGentic is built entirely on the Locus Payment Infrastructure. Every transaction in the simulation goes through real Locus APIs:
- x402 Pay-per-Use Endpoints — AgentMail (create inbox, send email, list messages) and Laso Finance (auth, virtual card) are called directly, with USDC deducted from the Locus wallet
- Transaction Polling — GET /api/x402/transactions and GET /api/pay/transactions are polled every 5 seconds to detect new on-chain activity
- Wallet Balance — GET /api/pay/balance syncs the real USDC balance from Base chain
- Locus API Client — Custom locusRequest<T>() helper with Bearer token auth, used across the entire app
The project demonstrates how to leverage the full Locus suite: not just payments, but the entire x402 skill catalog, transaction history, wallet management, and real-time monitoring — all visualized in an interactive 3D simulation.

Team **Fivee-LCus** -- [Muhammad Firdaussyah](https://github.com/maulana-tech), [Catur Setyono](https://github.com/catursetyono)

`2026-04-16`

---

### Lumen
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lumen-a129) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sayak-code/Lumen) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Smart.Private.Green.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🔆 Lumen — The Problem It Solves

Campus buildings and institutional spaces hemorrhage energy every day - lights blazing in empty lecture halls, ACs running in vacant labs, fans humming in deserted corridors - simply because there's no intelligent system watching. Lumen solves this by repurposing the CCTV cameras already installed in these spaces, transforming them into a real-time occupancy intelligence layer using YOLOv11 AI person detection. Rather than requiring expensive smart-sensor retrofits or manual intervention from facility managers, Lumen continuously scans each room, detects whether people are actually present, and automatically triggers appliance ON/OFF commands (lights, fans, AC) through smart relays - all without storing or transmitting any identifiable footage, thanks to its privacy-first "Ghost Mode" that renders only skeletal stick-figure outlines. Facility admins get a live dashboard showing occupancy counts, appliance states, and a historical Waste Event Log that tracks every time energy was saved - turning invisible waste into measurable, actionable data. Whether it's a university trying to cut its electricity bill, a school aiming to reduce its carbon footprint, or a corporate campus optimizing after-hours energy use, Lumen makes energy efficiency automatic, auditable, and camera-agnostic - working with built-in webcams, USB cameras, or IP/RTSP streams right out of the box, with zero dependency on cloud services or external infrastructure.

**Challenges we ran into**

🧱 Challenges I Ran Into

One of the trickiest hurdles we hit early on was getting the CV microservice to reliably open camera sources across different hardware setups. OpenCV's VideoCapture behaves inconsistently depending on the backend (DSHOW vs FFMPEG vs ANY), and on some machines the webcam would silently fail to open — returning no error, just an empty frame — causing the entire audit cycle to crash silently. We solved this by implementing a backend waterfall strategy: the detector now tries CAP_FFMPEG, then CAP_DSHOW, then CAP_ANY in sequence, and if all fail, the backend gracefully falls back to mock occupancy data so the UI never breaks. Another significant challenge was decoupling the system from hard infrastructure dependencies — the original design required MongoDB and an MQTT broker, which made local demos nearly impossible without a full DevOps setup. We refactored the backend to auto-detect missing services at startup and switch to an in-memory mock mode, keeping every feature functional for demos while printing clear diagnostic logs. On the frontend, achieving a consistent glassmorphism dark-mode aesthetic across all pages (Live Auditor, Room Management, Analytics, Settings) without Tailwind utility conflicts required carefully authoring a custom CSS design system with CSS variables and backdrop-filter layers, since many Tailwind utilities don't compose cleanly with glassmorphic backgrounds. Finally, managing the "ghost feed" privacy pipeline — rendering MediaPipe skeletal overlays onto a canvas without leak

Team **Mango Byte** -- [Urjita Paul](https://github.com/urjitapaul06), [Sayak Adak](https://github.com/sayak-code), [Souptik Pal](https://github.com/palriju11234-del)

`2026-04-11`

---

### codebaseGPT
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/codebasegpt-9749) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SUBHAZIT/CODEBASE-GPT) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://codebasegpt-0.pages.dev/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/FfE8VMOqDN8) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The most complex codebases decoded in seconds.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**CodebaseGPT** is built to bridge the gap between complex source code and developer understanding. Whether you're a new engineer onboarding to a massive repository or a senior architect maintaining multiple systems, it provides the AI-powered "eyes" and "brain" you need to navigate efficiently.

### The Problems It Solves

*   **Cognitive Overload in Massive Repositories:** Large codebases (1,000+ files) are notoriously difficult to "grok." Developers spend hours manually tracing function calls and mapping dependency chains just to make a small change.
*   **The "Onboarding Tax":** New team members often take weeks to become fully productive as they wait for senior developers to guide them through the project's architecture and conventions.
*   **Security Gaps in Development:** Security is often treated as an afterthought or a "CI stage" issue. Manual reviews are slow, and vulnerabilities are frequently missed until they reach production.
*   **PR Review Fatigue:** Human reviewers are inconsistent. They get tired, miss subtle logic flaws, or overlook deviations from established architectural patterns in large Pull Requests.
*   **AI Context Limitations:** Standard AI assistants often fail with large repositories because they hit "token limits" or lose track of the broader project context.

---

###  What People Use It For

*   **Instant Technical Onboarding:** Use the **Architecture Narrative** to get a high-level overview of any repo instantly. Ask questions like: *"How does the auth flow work here?"* or *"Where is the data validation logic located?"*
*   **AI-Powered Code Reviews (PRGPT):** Integrate directly into GitHub workflows. **PRGPT** automatically reviews every commit, catching logic errors, suggesting improvements, and summarizing changes before a human even opens the PR.
*   **Automated Security Audits:** Run deep scans across the entire codebase to detect vulnerabilities, hardcoded secrets, and security anti-patterns tailored to your specific stack.
*   **Safe Repository Exploration:** Use the **Developer CLI** or **Dashboard** to index public and private repositories safely. The "skeleton-first" indexing engine handles huge repos without hitting AI context limits.
*   **Issue Resolution:** Fetch GitHub issues directly into the dashboard and let the AI propose solutions, complete with exact code changes and root cause analysis.

---

### How It Makes Development Easier & Safer

*   **Faster Velocity (Easier):** You no longer need to read every file to understand a system. The AI provides a searchable, interactive map that acts as a 24/7 Technical Lead.
*   **Proactive Security (Safer):** Integrated scanning shifts security "left" in the development lifecycle, identifying risks the moment they are introduced into the codebase.
*   **Consistent Quality (Safer):** PRGPT never misses a line of code. It acts as a tireless first-pass reviewer, ensuring that every merge meets a high baseline of quality and consistency.
*   **Scalable Intelligence (Easier):** The on-demand indexing engine allows you to work with 50,000+ file repositories just as easily as a 50-file script, fetching only what the AI needs to answer your question.

**Challenges we ran into**

Building **CodebaseGPT** was a journey of constantly fighting "scale." When you're feeding entire repositories to AI models, you hit limits immediately token limits, API limits, and even browser memory limits. 

Here are the three biggest hurdles we faced and how we engineered our way around them:

### 1. The "Big Repo" Context Overflow 
**The Challenge:** AI models like GPT-4 and Gemini have fixed context windows (e.g., 128k tokens). A repository like `facebook/react` or `grafana/grafana` can easily contain millions of tokens. Initially, our indexer would just crash or the AI would return a `400: Context too large` error.

**The Solution: Skeleton-First Indexing**
We moved away from "index everything" to a **Two-Tier Strategy**:
*   For small repos, we fetch everything.
*   For large repos (>300 files), we index only a **"Skeleton"** initially: directory structure, [README.md](cci:7://file:///Users/apple/Desktop/FULLSTACK%20GIT%20DEV%20TOOLS%20PLATFORM/README.md:0:0-0:0), [package.json](cci:7://file:///Users/apple/Desktop/FULLSTACK%20GIT%20DEV%20TOOLS%20PLATFORM/package.json:0:0-0:0), and root-level config files. 
*   We then implemented **On-Demand Loading**, where the system lazy-loads file contents only when specific questions are asked or when a user clicks a file. This kept our "structural map" intact while staying well within token limits.

### 2. The 60FPS Visualization Bottleneck 
**The Challenge:** We wanted an interactive dependency graph. Our first version used **D3.js with SVG**. It looked great for 50 files, but at 1,000 files, the browser DOM couldn't keep up. Dragging a node caused the entire UI to lag (dropping to 5-10 FPS) because hundreds of SVG elements had to be recalculated.

**The Solution: Canvas-Based Rendering**
We refactored the entire visualization engine to use **Canvas rendering** via `react-force-graph-2d`. By shifting the drawing logic from the DOM to the GPU-accelerated Canvas API, we achieved smooth 60FPS performance even for massive monorepos. We also added a **warmup period** (50 simulation ticks) before rendering to prevent nodes from "exploding" across the screen when first loaded.

### 3. GitHub API Rate Limits & "Throttling" 
**The Challenge:** Fetching thousands of files requires individual API calls. Even with high-limit Personal Access Tokens (PATs), we would frequently hit GitHub's secondary rate limits when indexing deeply nested repositories, leading to failed index jobs and "hanging" progress bars.

**The Solution: Smart Batching & Concurrency Control**
We built a specialized **Supabase Edge Function** (`repo-fetch-batch`) that acted as an intelligent proxy.
*   **Batching:** It pulls up to 10 files in a single request.
*   **Concurrency:** It limits internal fetch workers to a maximum of 3 concurrent requests to stay under GitHub's "abuse" triggers.
*   **Retries:** We implemented exponential backoff (starting at 1s) that automatically kicks in the moment we detect a `403` or `429` status code, ensuring index jobs always finish, even if they have to slow down.

### 4. Browser Quota limits (`localStorage`) 
**The Challenge:** We wanted the app to feel "instant" by caching repo data locally. However, caching the full file tree of large projects triggered the browser's `QuotaExceededError` in `localStorage` (which is often limited to ~5MB).

**The Solution: IndexedDB + Compressed Metadata**
We moved the heavy repository cache from `localStorage` into **IndexedDB** using a lightweight wrapper. We also started compressing our "Architecture Narratives" and metadata strings before storage, allowing us to store dozens of project indices on a single device without ever hitting a storage cap.

Team **0101 CREW** -- [SUBHAJIT PATHAK](https://github.com/SUBHAZIT), [Debasis Khamari](https://github.com/dev-debasis), [Neel Das](https://github.com/neeldas0032), [Souvik Kundu](https://github.com/Souvik-kundu-off)

`2026-04-11`

---

### GreenPlate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenplate-8197) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AkibDa/GreenPlate) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/oDBQInX6bGE?si=8dkYbubuEOrZzAHA) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> The timesaver that you need !

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# The problem it solves

GreenPlate solves one of the most common yet overlooked problems in colleges and campuses: **food waste and inefficient canteen ordering systems**.

Every day, campus food stalls face issues like:

* students waiting in long queues during rush hours
* cancelled orders leading to prepared food being wasted
* unsold meals at the end of serving hours
* no easy way to reuse safe leftover food
* lack of incentives for students to make sustainable food choices
* staff having no data on waste, performance, or demand trends

Traditional canteen systems only focus on ordering food, but they do not solve what happens **after cancellations**, **unsold inventory**, or **food surplus**.

GreenPlate transforms this process into a **closed-loop sustainable food ecosystem**.

## What people can use it for

Students can use GreenPlate to:

* browse live menus from verified campus stalls
* prepay and skip queues with secure pickup codes
* buy discounted surplus meals from the resale marketplace
* earn Eco Points for sustainable purchases
* redeem points for discounts on future meals
* avoid unnecessary cancellations through reward-based accountability

Staff and managers can use it to:

* manage menus quickly using AI-powered menu scanning
* handle pickup verification securely
* monitor stall and staff performance
* convert cancelled READY orders into discounted resale items
* donate unsold safe food to nearby shelters
* track waste reduction and sustainability impact

## How it makes existing tasks easier

GreenPlate makes campus food ordering faster, smarter, and more sustainable by:

* reducing queue time with digital ordering
* preventing edible food from being wasted
* automatically converting cancellations into resale opportunities
* creating a donation workflow for shelters
* rewarding responsible student behavior with Eco Points
* helping stalls recover revenue from cancelled orders
* giving managers better operational visibility

Instead of food being thrown away, it gets:
```bash
resold, rewarded, or rescued
```
This makes GreenPlate not just a food ordering app, but a **campus sustainability platform that reduces waste while improving convenience and affordability**.

**Challenges we ran into**

# Challenges I ran into

Building GreenPlate was exciting because the biggest challenge was not just creating a food ordering system, but making sure the **sustainability workflows remained reliable, fair, and abuse-proof**.

One of the toughest hurdles was designing the **order lifecycle architecture**.

A normal food app only needs:
```bash
order → payment → pickup
```
But GreenPlate had to support a much more complex real-world flow:
```bash
order → payment → cancellation → refund → resale → donation → eco rewards
```
Making all these states work together without breaking the user experience was one of the hardest engineering problems in the project.

## 1) Preventing race conditions in resale purchases

A major issue appeared in the **discounted resale marketplace**.

Multiple students could try to buy the same surplus meal at the same time, which created a risk of **double booking the same food item**.

To solve this, I implemented **Firestore transactional reservations with a timed lock window**, where an item becomes temporarily reserved for 5 minutes during payment.
This ensured only one student could complete checkout while keeping the system fair and scalable.

## 2) Keeping payments, refunds, and cancellations consistent

Another big challenge was integrating **Razorpay payments with Firestore order states**.

The difficult part was ensuring:

* payment success updates the correct order
* cancelled paid orders trigger refunds safely
* READY orders convert into resale items
* duplicate webhook/payment verification does not break the order state

I solved this by introducing:

* internal order IDs
* idempotent payment verification
* batch Firestore writes
* strict order status validation before every transition

This made the payment flow much safer and production-ready.

## 3) Designing Eco Points without loopholes

The **Eco Points reward economy** introduced a new challenge:
how to reward sustainable behavior **without letting users exploit the system**.

For example, users could repeatedly:
```bash
order → earn points → cancel → refund → repeat
```
To prevent this abuse, I added:

* eco point penalties on cancellation
* no negative point balances
* tier recalculation after penalties
* weekly cancellation limits
* discount caps during redemption

This turned gamification into a **fair sustainability incentive system instead of a loophole-prone rewards feature**.

## 4) Balancing features without making the app feel overloaded

Since GreenPlate includes:

* food ordering
* AI menu scanning
* resale marketplace
* donation rescue
* eco rewards
* analytics

…the hardest product challenge was ensuring the app still felt **simple and intuitive**.

I solved this by keeping the **core student flow minimal**:
```bash
menu → order → pickup
```
while advanced sustainability workflows only activate when needed in the backend.

This kept the user experience clean while still making the platform powerful.

## What I learned

This project taught me how to design **real-world backend systems where business logic, payments, sustainability, and gamification all interact safely**.

The biggest takeaway was learning how to think beyond CRUD APIs and build **state-driven systems that solve real operational problems at scale**.

**Best Use of Gemini API**

GreenPlate fits the **Best Use of Gemini API track** by using Gemini as a **real-world intelligence layer for campus food operations and waste reduction**.

One of the biggest operational problems in college stalls is that menu updates are usually manual, slow, and error-prone. To solve this, we integrated **Gemini API for AI-powered menu extraction from images**.

Staff can simply upload a photo of a handwritten or printed menu, and Gemini automatically extracts:

* food item names
* prices
* short descriptions
* structured JSON output ready for verification

This removes the need for staff to manually enter every menu item, making menu onboarding significantly faster and reducing human errors.

What makes our Gemini integration especially impactful is that it is **not just a demo feature**, but directly improves a real operational workflow used by stall staff every day.

We use Gemini to:

* process menu images in multiple formats
* normalize noisy price patterns like ```25/-```
* generate concise food descriptions
* return clean JSON for direct backend integration
* help non-technical staff digitize menus instantly

This AI-powered workflow makes GreenPlate highly scalable across multiple college stalls where menus frequently change.

By combining Gemini with our **FastAPI + Firestore backend**, we turned an otherwise repetitive manual task into an **intelligent one-click digitization workflow**, helping staff save time while improving menu accuracy.

This directly supports GreenPlate’s broader mission of making campus food systems **faster, smarter, and more sustainable**.

Team **Code Newbies** -- [Kushal Golder](https://github.com/KushDa), [Sk Akib Ahammed](https://github.com/AkibDa), [Susovan Chatterjee](https://github.com/suso-van), [Jeet Sarkar](github.com/StackUnderflow10)

`2026-04-05`

---

### Classpilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/classpilot-46a7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rocker1166/frosthacks_localhost) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://frosthacks-localhost.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Ai powered next gen classroom ecosystem.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![langchain](https://img.shields.io/badge/langchain-333333?style=flat-square) ![Convex](https://img.shields.io/badge/Convex-333333?style=flat-square)

**The problem it solves**

## Project Summary: ClassPilot  
ClassPilot is an AI-powered, next-generation classroom platform that reimagines Google Classroom with an intelligent tutor layer. Instead of focusing on narrow text-only retrieval, we use a multimodal RAG approach that understands and reasons across class notes, PDFs, images, diagrams, code, quizzes, and voice interactions to deliver personalized, context-grounded learning for students and actionable insights for educators.

---

## The Problem It Solves

Most classroom platforms are strong at content storage but weak at day-to-day learning support and teaching intelligence.

- Students get stuck outside class and wait too long for help.
- Teachers repeatedly answer the same doubts with limited automation.
- Course materials exist, but finding the exact relevant page is hard.
- Generic AI tools are often ungrounded and unsafe for academic use.
- Faculty visibility into confusion, risk, and engagement is delayed.

ClassPilot solves this by turning static class content into an always-available, context-grounded tutor and teacher assistant.

---

## What People Can Use It For

### Students
- Ask course-specific questions and get grounded answers with citations.
- Learn with adjustable tutoring style, from direct explanation to Socratic guidance.
- Personalize experience only for the students with long term memory .
- Request quizzes, code help, diagrams, tables, and document navigation inside one chat flow.
- Attach specific resources directly in chat for focused answers.
- Use interactive canvas experiences for visual and active learning.
- Continue context-aware learning with conversation memory and summarization.

### Teachers
- Upload and organize class resources, then make them instantly tutor-ready.
- View student performance insights with risk tagging and weak-topic signals.
- Monitor topic confusion trends, engagement, and learning behavior.
- Manage classwork quizzes with authored question banks, publish guards, and grading paths.
- Capability to customize student side ai tutor behavior to fine tune student experience.  

### Institutions
- Run a safer, more effective AI-supported learning layer on top of standard LMS workflows.
- Improve response speed, personalization quality, and academic support coverage.
- Enable scalable student help while preserving course-grounded behavior and auditability.

---

## Major Implemented Capabilities 

- Convex-native production agent pipeline with intent routing, retrieval, generation, citation mapping, and canvas directives.
- Personalized tutor profile prompts per user for adaptive tutoring style.
- Interactive classwork quiz system:
  - faculty authoring,
  - question management and ordering,
  - student attempts,
  - objective grading support.
- Resource attachment in tutor chat using mention-based selection.
- Memory-aware tutoring with resilient long-term memory write flow and policy checks.
- Reliable citations and page-sync behavior with improved resource ID resolution and fail-safe PDF handling.
- Dashboard-level productivity features including notifications, calendar, and to-do aggregation.
- Route and navigation hardening for consistency, canonical paths, and safer dynamic routing.
- Streaming quality improvements including reasoning/answer separation and robust response handling.

---

## How It Makes Existing Tasks Easier and Safer

- Faster doubt resolution through instant, course-aware support.
- Higher answer trust through retrieval grounding and source citations.
- Lower faculty repetition cost via tutoring and assistant automation.
- Better learning outcomes through adaptive Socratic teaching modes.
- Earlier intervention via confusion heatmaps and insight dashboards.
- Safer operations through role-based access checks, guarded workflows, and resilient backend handling.

---

## Why This Approach Matters

Many projects focus first on building custom RAG internals.  
Our approach is to use Convex’s reliable retrieval primitives and direct engineering effort toward higher-impact education outcomes:

- intelligent tutoring behavior,
- personalized learning pathways,
- teacher copilots and insights,
- interactive learning surfaces,
- classroom workflow integration.

ClassPilot is not just a chatbot over PDFs.  
It is an AI-powered operating layer for modern education.

**Challenges we ran into**

## ClassPilot — Key Technical Challenges

Building ClassPilot wasn’t about generating answers.
The core challenge was making AI **trustworthy, multimodal, and classroom-ready** under real constraints.

---

### 1. Reliable Multimodal RAG

**Problem:** Inconsistent retrieval across PDFs, images, and mixed notes → missing context

**Solution:**

* Clean ingestion + optimized chunking
* Page-aware context stitching
* Tuned retrieval ranking
* Standardized embeddings using *Gemini Embedding 2*

**Result:** Consistent, high-quality retrieval across all content types

---

### 2. Hallucination Prevention

**Problem:** Confident but incorrect answers beyond retrieved data

**Solution:**

* Strict **RAG-boundary enforcement**
* Faithfulness checks + response gating
* Explicit fallback when context is insufficient

**Result:** Reliable, evidence-grounded responses

---

### 3. Clean Streaming Output

**Problem:** Reasoning + final answer mixed during streaming

**Solution:**

* Separate reasoning and answer channels
* Delta-safe parsing + fallback completion
* Robust output assembly

**Result:** Clear, readable responses with no duplication

---

### 4. Voice–Text Consistency

**Problem:** Voice responses drifted from text behavior

**Solution:**

* Unified retrieval + tool-routing logic
* Injected live context into voice flows
* Session sync + refresh

**Result:** Consistent, grounded voice interactions

---

**EDUCATION**

## How Our Project Fits the Education Track

Our project, **ClassPilot**, is built specifically for the exact problem in this track: students need reliable, course-specific help after hours, and faculty need scalable support for repetitive academic queries.

We are not building a generic chatbot.
We are building an AI-powered learning system that is grounded in course materials, uses Socratic tutoring behavior, cites sources, and gives faculty real-time insight into student confusion.

---

## Problem-Solution Alignment

The track asks for a tutor that is context-restricted, pedagogically safe, and useful for both students and instructors.
Our implementation directly matches that goal.

* We provide a faculty workflow to upload and manage course resources.
* We process those resources into a multimodal RAG pipeline with vector retrieval.
* We use **Gemini Embedding 2** for semantic indexing quality across mixed educational content.
* We enforce strict retrieval grounding so answers stay within course evidence.
* We apply configurable Socratic tutoring behavior so the system guides learners instead of simply giving away solutions.

---

## Functional Requirement Coverage

### 1. Faculty material upload

We support structured resource ingestion for course content (PDF/text/image-based learning resources).

### 2. Vector indexing + RAG

We chunk, embed, index, and retrieve context before generation.
RAG is part of the core architecture, not an optional add-on.

### 3. Context-only answering

We enforce strict RAG boundaries and faithfulness controls so responses remain course-grounded and out-of-scope handling is explicit.

### 4. Student chat interface

We provide a full student chat experience with streaming, contextual continuity, and interactive learning surfaces.

### 5. Socratic tutor behavior

We implement adjustable Socratic levels so teaching style can shift from direct explanation to guided reasoning.

### 6. Source citations

We return citation-linked responses with source/page traceability for transparency.

### 7. Faculty dashboard insights

We provide topic confusion and performance-oriented analytics, including teacher-facing AI assistance flows.

---

## Expected Outcomes Match

Our system is designed to deliver the outcomes requested in the brief:

* Automated course-specific support without requiring constant faculty intervention.
* High context adherence through strict retrieval boundaries and grounding checks.
* Student-wise and topic-wise insight signals in near real time.
* Transparent assistance through citation-aware responses and evidence-linked outputs.

---

## Impact Fit

Our project supports the intended education impact:

* 24/7 personalized support for students.
* Reduced repetitive workload for faculty and TAs.
* Better academic integrity through guided learning behavior.
* Better teaching decisions through confusion and engagement visibility.

---

## Constraint Fit

We satisfy the listed constraints:

* Vector retrieval and RAG are mandatory and central in our system.
* We do not rely only on pretrained model knowledge; retrieval grounding is enforced.
* We maintain role-aware access patterns and controlled data handling to support student privacy expectations.

---

## Why Our Submission Stands Out

Many solutions stop at “chat with documents.”
Our team built a broader AI classroom system that combines:

* multimodal RAG,
* Socratic pedagogy,
* faithfulness and strict boundary controls,
* citation transparency,
* teacher intelligence and analytics.

That is why our project fits this track strongly, both technically and educationally.

Team **localhost** -- [sajal patra](https://github.com/sajalpatra), [Deep Rajak](https://github.com/DeepRajak/), [Surya Dey](https://github.com/Surya2005Dey), [Suman Jana](https://github.com/rocker1166)

`2026-03-28`

---

### TerraForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/terraforge-bbd0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DotSlash-9-0/Hell-Boys) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1xp3-ZZdFuDh1A1DtoKCyf04WK9N0X9Dp?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MPwrHHJqDtY?si=AY0mU3XFNeiZjFxn) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> TerraForge powers data-driven climate action

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![jspdf](https://img.shields.io/badge/jspdf-333333?style=flat-square) ![React-leaflet](https://img.shields.io/badge/React--leaflet-333333?style=flat-square)

**The problem it solves**

# 🌍 TerraForge: Environmental Intelligence OS  
**Bridging rural agricultural diagnostics with government-level climate policy using Hybrid Edge-AI**


---

## 📖 Overview

TerraForge is an **AI-driven Environmental Operating System** for **real-time environmental tracking and predictive policy simulation**, enabling governments and citizens to make proactive, data-driven climate decisions.

Unlike cloud-dependent AI systems (high latency, API costs, bandwidth-heavy), TerraForge uses a **Hybrid Edge-AI architecture** with **locally deployed, quantized 1.1B parameter LLMs**, ensuring:

- ⚡ Zero API costs  
- 🔒 Complete data privacy  
- ⚙️ Low-latency performance  

---

## 🚀 Core AI Pipeline (Local ML)

A tightly integrated pipeline of optimized models:

### 🧠 TinyLlama-1.1B (Core LLM)

**Dual LoRA adapters:**
- Agricultural Diagnostic LLM → Crop/Livestock issue detection  
- Policy Strategy LLM → 3-tier plans (Strict / Moderate / Advisory)  

👉 **Key Innovation: Real-Time Prompt Injection**  
Live API + ML outputs are injected into prompts before generation:
- ✔ No hallucinations  
- ✔ Context-aware outputs  
- ✔ Scientifically grounded explanations  

---

### 🌐 NLLB-200 (Translation Layer)

- Converts regional languages → English → back to native  
- Enables multilingual rural accessibility  

---

### 🎙️ Whisper (Speech Input)

- Voice-to-text for non-technical users  

---

### 🔊 gTTS (Speech Output)

- Converts responses into audio (`.mp3`)  

---

### 📊 Random Forest (Prediction Engine)

- Processes AQI, rainfall, feed, temperature, etc.  
- Predicts yield changes (e.g., milk/crop output)  
- Feeds results into LLM for explanation  

---

## 🖥️ Frontend Ecosystem

Built with **Next.js + React + TailwindCSS + Shadcn UI**

### 👨‍🌾 Farmer Dashboard

- 🌦️ Live weather & AQI (*Open-Meteo API*)  
- 📉 Yield prediction from real-time stress factors  
- 🎤 Multilingual voice assistant (speech + audio output)  
- 📡 Works in low/no internet environments  

---

### 🏛️ Government Dashboard

- 🗺️ Geospatial map (*react-leaflet*)  
- 🔥 NASA FIRMS fire hotspot overlay  
- 🤖 AI-generated policy recommendations  
- 🧪 “What-if” simulation sandbox  
- 📄 Auto PDF reports (*jsPDF*)  

---

## 🧠 Architecture (API + AI Flow)

Separated into **Training (Past)** and **Inference (Present/Future)**

### 🏗️ Phase 1: Offline Training

- Historical data (2021–2024)  
- **Granger Causality (statsmodels)** → discovers environmental relationships  
- Train **RandomForest regressors** → saved as lightweight models  

---

### ⚡ Phase 2: Live Inference

1. Fetch live APIs (Open-Meteo, OpenAQ, NASA FIRMS)  
2. Apply trained rules → instant predictions  
3. Inject results into TinyLlama prompt  
4. Generate explanation  
5. Translate (NLLB) + Voice output (gTTS)  

---

## 📊 Foundational Datasets

- 🔥 Fires & Emissions → NASA FIRMS, Climate TRACE  
- 🌫️ Air & Weather → OpenAQ, IMD  
- 💧 Water → Central Ground Water Board  
- 🌾 Agriculture → ISRO/USGS (NDVI), Animal Husbandry (Milk Yield)  
- 💰 Economy → Agmarknet, Census of India  

---

## 💻 Tech Stack & Deployment

**Frontend:**  
Next.js 14, React, TailwindCSS, Shadcn UI, React-Leaflet, jsPDF  

**Backend:**  
Python, FastAPI  

**ML Stack:**  
transformers, statsmodels, scikit-learn, pandas  

**Models:**  
TinyLlama, NLLB-200, Whisper  

**Database:**  
Supabase (PostgreSQL)  

---

## 🚀 Deployment Strategy

- 🌐 Frontend → **Vercel (Global CDN)**  
- 🧠 Backend → Local GPU execution  
- 🔗 Public Access → **Ngrok / Cloudflare Tunnels**  

---

## 💡 Core Value

- Offline-first AI  
- Zero API dependency  
- Real-time + predictive intelligence  
- Multilingual + voice-enabled  
- Scalable from farmers → government systems  

---


**Built for the future. Running locally. Healing globally. 🌱🚀**

**Challenges we ran into**

## ⚡ Challenges I Ran Into

### 🧠 Running LLMs Locally Without Crashes

One of the biggest challenges was running a **1.1B parameter LLM locally** with limited GPU/CPU resources. Initially, the model either crashed or had very slow inference times.

**How I solved it:**
- Used quantization techniques to reduce memory usage  
- Optimized inference with CPU fallback when GPU wasn’t available  
- Reduced token generation limits for faster responses  

---

### 🔄 Eliminating AI Hallucinations

The LLM initially produced **generic or incorrect answers** due to lack of real-time environmental awareness.

**How I solved it:**
- Implemented **real-time prompt injection**  
- Injected live API data + ML predictions directly into the prompt  
- Ensured outputs were **context-aware and fact-based**, not guessed  

---

### 🌐 Multilingual Pipeline Integration

Integrating **NLLB (translation) + TinyLlama (LLM) + Whisper (speech)** into a single pipeline caused latency and formatting issues.

**Problems faced:**
- Incorrect translations breaking prompts  
- Delays due to multiple model calls  

**Solution:**
- Standardized all inputs into **English before LLM processing**  
- Optimized pipeline flow:  
  `Speech → Translation → LLM → Translation → Audio`  
- Reduced token size to improve speed  

---

### 📡 Handling Real-Time APIs Reliably

Live APIs (weather, AQI, NASA FIRMS) sometimes returned **inconsistent or missing data**, affecting predictions.

**How I solved it:**
- Added fallback/default values  
- Implemented validation and error handling layers  
- Cached recent API responses to ensure reliability  

---

### 🗺️ Geospatial Map Performance

Rendering real-time data (fire hotspots, regions) using `react-leaflet` caused **UI lag and overlapping issues**.

**Solution:**
- Implemented marker clustering  
- Limited real-time refresh frequency  
- Filtered only relevant data points for rendering  

---

### 🔊 Voice Input/Output Sync Issues

There were delays and mismatches between **speech input (Whisper)** and **audio output (gTTS)**.

**Fix:**
- Added async handling and proper sequencing  
- Ensured text confirmation before generating audio  
- Optimized audio generation timing  

---

## 💡 Key Learning

> Building TerraForge showed that the hardest part of AI systems isn’t just the models—  
> it’s **orchestrating LLMs, APIs, ML models, and UI into a reliable real-time system**.

**GreenTech**

**🌱 Green Tech Track Justification**

TerraForge directly aligns with the Green Tech track by enabling data-driven environmental monitoring, prediction, and policy action.

Our platform tackles critical climate challenges such as air pollution, agricultural stress, and environmental degradation by combining real-time data with AI-powered insights.

**🌍 Environmental Monitoring:** Integrates live data from sources like weather APIs, AQI sensors, and satellite fire detection (NASA FIRMS) to track ecological conditions in real time.
**📊 Predictive Sustainability:** Uses machine learning models to forecast impacts such as crop yield loss or livestock stress due to environmental factors.
**🏛️ Policy Optimization:** Generates actionable government strategies (e.g., pollution control, resource allocation) through AI-based simulations and scenario testing.
**🌾 Sustainable Agriculture:** Helps farmers make informed decisions to reduce losses, optimize resources, and adapt to climate variability.
**🌐 Accessibility & Inclusion:** Works offline with multilingual voice support, ensuring rural communities can actively participate in sustainable practices.

👉 By bridging ground-level environmental data with high-level policy decisions, TerraForge enables faster, smarter, and more sustainable climate action.

Team **Hell Boys** -- [Aryan Buha](https://github.com/Aryanbuha890), [Neel Prajapati](https://github.com/Neel-2606), [Krushit Prajapati](https://github.com/krushit1307), Sumit Patel

`2026-03-22`

---

### MedConnect
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medconnect-b9b7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mridulsharma17/electrothon-8.0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://electrothon-frontend-a28k.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Connecting Help When Every Second Matters.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

MedConnect solves the critical problem of delayed assistance during emergencies.
In many situations such as medical emergencies, accidents, or when someone suddenly collapses, immediate help is often not available nearby. People around may be willing to help, but they are usually unaware that someone nearby needs urgent assistance.

Because of this delay in response, the victim may not receive timely first aid or support, which can worsen the situation and sometimes even lead to loss of life.

MedConnect addresses this problem by instantly connecting people in emergencies with nearby volunteers and responders. By sharing live location, medical information, and real-time alerts, the platform helps ensure that help reaches the victim as quickly as possible when every second matters.

**Challenges we ran into**

While building MedConnect, one of the main challenges was implementing real-time location sharing and alerts so that nearby volunteers could receive emergency notifications instantly. Ensuring that the system could accurately detect and notify the closest volunteers required proper integration with location services and backend databases.

Another challenge was designing a simple and reliable SOS interface that users can operate quickly during stressful emergency situations. We had to focus on making the UI minimal and intuitive so that users could trigger alerts with just a few actions.

We also faced difficulties in managing real-time data synchronization between users and volunteers, such as updating request status and responder information. This was addressed by using Firebase services for real-time updates and authentication, which helped us build a more responsive and scalable system.

**Electrothon 8.0 Winners**

Our project, MedConnect, directly aligns with the goals of Electrothon 8.0 by leveraging technology to solve a critical real-world problem — reducing emergency response time and improving access to healthcare assistance.

In many emergency situations, delays in communication and lack of immediate medical guidance can significantly worsen outcomes. MedConnect addresses this challenge through a platform that combines AI-powered health assistance, location-based hospital discovery, and a community-driven volunteer response network.

The system works in two main parts. First, our web platform allows users to quickly find nearby hospitals using their PIN code and interact with an AI health assistant that provides structured medical guidance and recommended actions based on symptoms. This helps users make informed decisions during uncertain health situations.

Second, our mobile application focuses on real-time emergency response. With a single SOS trigger, the platform notifies nearby registered volunteers who can quickly respond and assist the victim. Volunteers can accept the request and coordinate through an in-app group chat to ensure faster and more organized help until professional medical care is available.

By integrating AI, real-time communication, and location intelligence, MedConnect demonstrates how modern technology can be applied to build scalable, socially impactful solutions for emergency healthcare support.

Electrothon encourages innovation that addresses real societal challenges, and our project reflects that vision by focusing on practical implementation, accessibility, and community-driven emergency assistance.

**Google Cloud**

Our project, MedConnect, leverages the power of Google Cloud to build a scalable platform that improves emergency healthcare accessibility and response time.

The system consists of a web platform and a mobile application designed to assist users during health emergencies. The web platform allows users to find nearby hospitals using their PIN code and interact with an AI-powered health assistant that analyzes symptoms and provides structured medical guidance, risk assessment, and recommended next steps.

Google Cloud services play a key role in enabling this functionality. Our AI assistant is powered by models from Google Gemini, which allows us to process natural language health queries and generate helpful responses. We also use cloud-based infrastructure to ensure that the system is reliable, scalable, and capable of handling real-time requests during emergency situations.

In addition to the AI assistant, our mobile application includes an SOS feature that notifies nearby registered volunteers when someone requires urgent assistance. Volunteers can accept the request and coordinate through an in-app group chat, helping reduce response time until professional medical help is available.

By using Google Cloud’s AI capabilities and scalable backend infrastructure, MedConnect demonstrates how cloud technology can support intelligent healthcare assistance, real-time coordination, and location-based services to improve emergency response and accessibility to medical support.

**ElevenLabs**

Our project, MedConnect, is an AI-powered emergency response and healthcare assistance platform designed to help users quickly access medical guidance and connect with nearby hospitals or volunteers during emergencies.
To improve accessibility and make the platform usable in real-world stressful situations, we integrated ElevenLabs text-to-speech technology directly into our AI health assistant. When a user asks a health-related question or receives guidance from the AI system, the response can be read aloud using natural, human-like voice synthesis. This allows users to receive information even if they cannot easily read their screen, such as during a medical emergency, while driving, or when assisting someone who is injured.
The ElevenLabs integration plays an important role in our system for several reasons:
Accessibility: Voice responses help visually impaired users or people in stressful situations quickly understand medical guidance.
Emergency usability: During urgent scenarios, listening to instructions is often faster and safer than reading text.
Human-like interaction: ElevenLabs provides realistic voice output, which makes the AI assistant feel more supportive and easier to interact with.
In our platform workflow, when the AI health assistant generates a response, the text is sent to the ElevenLabs text-to-speech API, which returns a natural voice output that can be played directly in the application. This transforms our assistant from a simple chatbot into a voice-enabled health companion capable of guiding users during critical moments.
By combining AI-generated medical guidance with ElevenLabs’ voice technology, MedConnect creates a more accessible, responsive, and human-centered emergency healthcare experience.

**Best Use of Gemini 3 [Google Deepmind]**

MedConnect leverages Gemini-powered AI to enhance emergency response and decision support.
We implemented a Retrieval-Augmented Generation (RAG) system that allows the AI to access relevant medical guidance and emergency response information in real time. When an emergency alert is triggered, the AI can analyze the situation and provide helpful suggestions or guidance to volunteers assisting the victim.

Additionally, the model is fine-tuned to understand emergency scenarios, enabling it to generate context-aware responses such as first-aid instructions, situational advice, or guidance based on available medical data.

By combining Gemini’s generative capabilities with RAG-based knowledge retrieval, MedConnect ensures that volunteers and responders receive accurate, reliable, and context-aware assistance during critical situations, helping reduce response time and improve the quality of emergency support.

Team **Devorbit** -- [Ayush Jha](https://github.com/itssAayush), [Shubham Singh](https://github.com/Shubham-singh112), [Ashish Gupta](https://github.com/Aashish-Op), [mridul sharma](https://github.com/mridulsharma17)

`2026-03-15`

---

### Aqua Check
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aqua-check-9675) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MugenSama-01/Aqua_Check) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aquacheck-vert.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/FjGDis5JqlU?si=J6-ekIeQdwCvb28P) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Groundwater & PreDrilling Hydrogeological Observer

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

Team **Beyond Syntax** -- [Koustav Das](https://github.com/koustavvd), [Tanishk Roychowdhury](https://github.com/MugenSama-01), [Neilanjan Sen Sharma](https://github.com/NEILANJAN-S-SHARMA), [Soumyajit Dewan](https://github.com/soumyajitdewan)

`2026-09-12`

---

### AI Food Waste Tracker
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-food-waste-tracker-ae83) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pratham-sinha-2007/AI-Food-Wastage-Tracker/tree/main) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/k4K8XxmZtM8?si=M_clL75n4RNPoTOw) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/k4K8XxmZtM8?si=M_clL75n4RNPoTOw) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Food Wastage - NOT COOL!

![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Google Teachable Machine](https://img.shields.io/badge/Google%20Teachable%20Machine-333333?style=flat-square)

**The problem it solves**

At retail sector food chains such as hostel mess, office mess, restaurants, etc, there is a lot of food waste because people just don't eat what they take. This project detects how much a food a person has wasted using computer vision, and rewards them if they have wasted no food thereby encouraging them and punishes them if they waste a lot of food. It rewards them by giving them a token that they can use in the same mess for an extra ladoo or rasgula and for punishing, it will click the photo  of the person as soon as it detects a lot of food wastage and upload it to the caterer's database so that they will get less food in the next serving.

**Challenges we ran into**

The biggest challenge in this project was training the ML model using Google's Teachable Machine and making it accurate enough for our project. Many times we gave it data, it worked, but predicted poorly for some other unseen data. Sometimes lighting conditions affected the result. Sometime the position of the plate affected the result. So we had to add those similar data points to into the dataset and redo the whole process of training the model and testing it.

Team **The Hackerz** -- Pratham Sinha, Revant Rai, AKSHAT CHAUDHARY

`2026-09-02`

---

### OurTales
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ourtales-c07d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ourtales.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/2a-93Df9yco?si=po34QzumqkZFIdT_) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Place where memories become stories worth keeping.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![expo.io](https://img.shields.io/badge/expo.io-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Photos preserve what happened, but they rarely preserve the story behind them.

The people who were there remember the details, the names, the jokes, the places and sometimes completely different versions of the same moment. That context often lives in someone's head, gets buried in group chats or disappears when the person who remembers it is no longer around.

OurTales lets people turn a photo into a shared memory. You add what you remember, invite the people who were there and they can contribute their own version through voice, photos or text.

Instead of forcing one "correct" story, OurTales keeps different memories, levels of certainty and disagreements together. Nothing is rewritten, invented or made public without approval.

It is built for families, friends, teams and communities who want to preserve not just their photos, but the stories that make them meaningful.

**Challenges we ran into**

Building the product was only part of the challenge. We also had to learn the hard way that getting a mobile app into production has its own timeline.

Because we were building OurTales within a very short launch window, we initially expected to be able to finish the app, submit it to the App Store and Google Play and have it publicly available in time for the launch. We quickly discovered that app store publishing has requirements and review processes that are outside our development timeline.

On iOS, the app needs to go through Apple's App Review process before public distribution. TestFlight gives us a way to distribute builds for beta testing, but it is not the same as having the app publicly available on the App Store. 

Google Play presented an even bigger timing constraint. For new personal developer accounts, Google requires a closed testing period before production access is available. That means a technically finished Android app can still be unable to go live immediately. 

At the same time, we were solving some difficult product and engineering problems:

Trust and AI: OurTales uses AI to help structure memories, but it must never invent names, dates, places or details. We had to design the system around preserving what people actually remember rather than generating a polished version of events.
Conflicting memories: Different people can remember the same moment differently. Instead of forcing the AI to choose a single "correct" story, we designed the experience to preserve different perspectives and levels of certainty.
Privacy: Memories are private by default, and access needs to be limited to the people invited to a specific memory. We enforce these rules at the database level with Postgres row-level security and constraints rather than relying only on the frontend.
Contributor friction: The product becomes more valuable when more people who were part of a memory contribute, but getting everyone to install and use a new app is a real adoption challenge, particularly for less technical family members.

The biggest lesson was that launching a mobile product means planning for both product readiness and platform readiness. We could build and iterate on the product quickly, but the App Store and Google Play have their own timelines that need to be accounted for from day one.

Team **Quad Core** -- Hafsa Hashmi, Zainul Abideen, Waqar Nawaz, Zohaib Ali

`2026-08-30`

---

### ECONETWORK AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/econetwork-ai-406c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JACK-444/ECONETWORK_AI.git) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "scan ,understand,prevent,impact."

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Camera API](https://img.shields.io/badge/Camera%20API-333333?style=flat-square) ![CSS3​](https://img.shields.io/badge/CSS3​-333333?style=flat-square)

**Challenges we ran into**

"One major challenge is ensuring reliable image classification because waste can appear in different shapes, sizes, lighting conditions, and backgrounds. Another challenge is preventing false or duplicate reports while keeping the application simple for users.”

**The problem it solves**

India generates a huge amount of waste, but a significant portion isn't properly segregated.

“Our project addresses the problem of improper waste segregation, recycling, and public waste dumping. Users often don't know what type of waste they have or whether it has recycling value. Our system uses AI to identify waste from an image, provides an estimated recycling value, and allows users to report publicly dumped waste with its location. We also use a reward system to encourage people to participate in responsible waste management.”

This causes:

Public spaces becoming polluted
Low recycling rates
Recyclable materials being lost
People not knowing how to segregate waste
Lack of simple reporting mechanisms
Loss of economic value from recyclable waste




Your project specifically identifies the lack of awareness, segregation, and public-waste reporting as key problems.

Team **phantom** -- [Mohammed Alyaan K H](https://github.com/mohammedalyaan1-kh), [JAGADEESH M.K](https://github.com/JACK-444), [rohan b](https://github.com/rohan-24-max), [aditya kanifnath mulay](https://github.com/AdityaMulay727), [BHUVANESHKANTH S K](https://github.com/bhuvaneshkanth)

`2026-08-30`

---

### Greenlight
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenlight-facf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VC444/greenlight) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1E9USUcnZ56X6dl4NW5FUseiFsaT74a9z/view?usp=drive_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8aVgPThk1Lc) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> I test your teammate's PRs so you don't have to.

![YAML](https://img.shields.io/badge/YAML-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**How Did You Use Claude?**

I used Claude to brainstorm my idea first. Then, I used plan mode and the /grill-me skill heavily to work out the details. Finally, Claude generated the code for the project. This process was not a one-time thing. I used it as a loop whenever a new big idea came to me in the project.

**What is the deployed URL for this project?**

https://github.com/VC444/greenlight

**What is the problem your project solves?**

Code generation is not the bottleneck anymore; reviewing it is. 

When you review a pull request, you can see whether the code looks right. You can't see whether it works. Only the second question matters to whoever uses the software. The AI review tools don't check it either because they read the same diff.

Finding out means pulling the branch and clicking through it, or asking for a demo. This takes time, so most people skip it and type LGTM. That's the problem. Nobody has made checking behavior as cheap as reading a diff.

**How you are solving it?**

I built a Github Action that turns a PR into a test plan and runs it in a real browser. It reports what worked and what didn't, with a recording of the entire session. 

I already built the browser and recording part before the hackathon, but the plan step was not working properly. That's what I focused on today. Even if there were mistakes in the plan, the browser would try to run them and crash. I made the plan step more robust, included Claude model support (which increased accuracy), and added a human-in-the-loop process where users can edit the plan before execution begins.

This is completely opensource.

Vignesh Chandrasekharan

`2026-08-08`

---

### Xutilize
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/civicos-acde) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OFFICIALHARI/Xutilize) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/XfbMwZzWtsI) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XfbMwZzWtsI) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Maximize resources. Minimize waste.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Radix UI](https://img.shields.io/badge/Radix%20UI-333333?style=flat-square) ![Zod](https://img.shields.io/badge/Zod-333333?style=flat-square) ![Tanstack Query](https://img.shields.io/badge/Tanstack%20Query-333333?style=flat-square)

**The problem it solves**

Communities already have valuable resources such as parking spaces, EV charging points, shared rooms, and local facilities. The problem is that these resources are often underutilized while people nearby struggle to find and access them when needed.

Most existing solutions only act as simple listing or booking platforms. They show available resources but do not intelligently coordinate supply and demand, optimize allocation, or help communities understand how their resources are being used over time.

Xutilize solves this by creating a centralized operating system for community resources. It enables resource owners to publish availability, allows users to request resources, and automatically identifies the best matches using a real-time allocation engine. The result is better utilization, reduced waste, improved accessibility, and a more efficient local ecosystem.

**Challenges we ran into**

One of the biggest challenges was designing a matching system that felt intelligent while remaining fast and easy to understand. A simple booking flow was not enough, so I developed a scoring-based allocation engine that evaluates factors such as availability, timing, location fit, priority, and resource compatibility before generating matches.

Another challenge was maintaining consistent state across the application. Actions such as creating resources, generating requests, running matches, updating bookings, and recording ledger entries all needed to stay synchronized. I solved this by using TanStack Query together with server functions to ensure reliable data updates throughout the platform.

Building a dashboard that could present resources, requests, analytics, and AI insights without overwhelming users was also difficult. Multiple layout iterations were required before arriving at a structure that balanced information density with usability.

Finally, integrating the AI insights layer required careful design. Instead of generating generic recommendations, I connected the insights system to actual platform activity so that recommendations and forecasts reflect real marketplace conditions.

[HARIKRISHNAN S](https://github.com/OFFICIALHARI)

`2026-06-17`

---

### Ecolife-ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecolifeai-ec42) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/harshitkr013/ecolife--ai) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ecolife-ai.vercel.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XMHQ_lqxlCg?si=LIvsmQn-pSLjPgwn) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> from Pantry to Planet

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

EcoLife AI is an all-in-one sustainability companion that helps users make smarter everyday decisions—for their health and for the environment.
People can use it to:
Identify waste correctly using AI and learn the proper disposal and recycling methods.
Reduce food waste by generating recipes from ingredients already available at home.
Follow personalised nutrition plans based on their age, health conditions, fitness goals, and dietary preferences.
Receive AI-powered sustainability advice on recycling, food storage, and eco-friendly habits.
Shop smarter with personalised grocery recommendations that minimise unnecessary purchases and waste.
Donate surplus food to nearby NGOs, reducing food waste while helping communities.
Stay motivated through EcoPoints and rewards for practising sustainable habits.
How Does It Make Existing Tasks Easier and Safer?
Instead of using multiple separate apps, EcoLife AI brings everything together in one platform.
It makes tasks easier by:
Eliminating the need to search the internet for recycling rules or recipe ideas.
Providing instant AI recommendations tailored to each user.
Helping users buy only what they need, reducing both costs and waste.
Simplifying the food donation process with location-aware matching.
Encouraging healthier lifestyles while promoting environmental responsibility.
This saves time, reduces confusion, and makes sustainable living much more accessible. 

 What Makes EcoLife AI Unique?
One integrated platform instead of several disconnected apps.
AI-driven personalisation across all major features.
Combines environmental sustainability and personal wellness, which most apps treat separately.
Encourages long-term behavioural change through EcoPoints and AI coaching.
Addresses multiple UN Sustainable Development Goals in a single solution, including Responsible Consumption, Zero Hunger, Good Health, and Climate Action.

**Challenges we ran into**

One of the biggest challenges was integrating the Google Gemini API across multiple features such as EcoScan, the AI Recipe Generator, the Sustainability Coach, and Nutrition Recommendations.
Initially, the application stopped generating responses because the Gemini model we were using had been deprecated. We also encountered API quota limits and inconsistent response formats, which caused some features to fail unexpectedly.
To solve this, we:
Updated the project to use the latest supported Gemini model.
Refactored the AI service so all features used a single, reusable API integration.
Added proper error handling and fallback messages to prevent the application from crashing when the API was unavailable.
Thoroughly tested each AI-powered feature after the migration to ensure consistent behaviour.
This experience taught us the importance of designing modular code, handling external API failures gracefully, and adapting quickly to changes in third-party services.

**Best Use of Gemini API**

yes

**Sustainability**

EcoLife AI directly addresses multiple sustainability challenges by using AI to reduce waste, promote responsible consumption, and encourage eco-friendly behaviour.
1. Reduces Food Waste
AI recipe generation uses ingredients already available at home.
Prevents edible food from being thrown away.
Food donation portal connects surplus food with nearby NGOs and people in need.
2. Improves Waste Management
EcoScan identifies different types of waste.
Guides users to dispose of waste correctly.
Encourages recycling and reduces landfill waste.
3. Encourages Sustainable Consumption
Smart shopping recommendations help users buy only what they need.
Personalised nutrition plans reduce over-purchasing and unnecessary food waste.
4. Promotes Environmental Awareness
AI Sustainability Coach educates users about recycling, composting, and eco-friendly habits.
Makes sustainability simple and accessible for everyone.
5. Builds Community Impact
Food donation system enables communities to redistribute excess food instead of discarding it.
Helps reduce hunger while minimising waste.
6. Drives Long-Term Behaviour Change
EcoPoints rewards users for sustainable actions.
Gamification motivates users to consistently adopt environmentally responsible habits.
Alignment with UN Sustainable Development Goals (SDGs)
EcoLife AI contributes to:
SDG 2: Zero Hunger (food donation)
SDG 3: Good Health and Well-being (nutrition guidance)
SDG 11: Sustainable Cities and Communities
SDG 12: Responsible Consumption and Production
SDG 13: Climate Action (reducing waste and emissions)


EcoLife AI leverages artificial intelligence to reduce food waste, improve recycling, promote healthier lifestyles, and empower communities to make sustainable everyday decisions—creating measurable environmental and social impact through a single integrated platform.

**Best Beginner's team**

Our team started this hackathon with limited experience in full-stack development and AI integration. Despite being beginners, we successfully designed, developed, and deployed a fully functional AI-powered sustainability platform within the hackathon timeline.
Throughout the project, we:
Learned and implemented React, TypeScript, and Vite for the frontend.
Integrated the Google Gemini API across multiple AI-powered features.
Solved real development challenges, including API integration, debugging, and deployment.
Successfully deployed our application on Vercel, making it publicly accessible.
Worked collaboratively by dividing responsibilities, learning new technologies, and supporting each other throughout development.
Instead of building a simple prototype, we created an integrated platform featuring AI waste detection, recipe generation, personalised nutrition, a sustainability coach, a food donation portal, smart shopping recommendations, and an eco-rewards system.
This project demonstrates our ability to quickly learn unfamiliar technologies, collaborate effectively, overcome technical challenges, and deliver a complete solution with meaningful social and environmental impact—qualities that embody the spirit of the Best Beginner's Team award.

Team **ERROR MINIONS** -- [Harshit Kumar](https://github.com/harshitkr013), [Indranath Sinha](https://github.com/indranathsinha4-cpu), [Nayonika Mukherjee](https://github.com/nayonikam25)

`2026-07-26`

---

### Nexus Voice AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexus-voice-ai-dabe) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Bring your AI Sales person on your online ecommerc

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

# Problem Statement

Modern e-commerce websites still rely on traditional search, filters, and manual browsing. Customers often struggle to find the right products because they don't know the exact product name or how to use filters effectively. As a result, they spend significant time comparing products, reading descriptions, and searching through multiple pages, leading to frustration and abandoned purchases.

At the same time, businesses receive thousands of repetitive customer queries such as product recommendations, order tracking, return policies, stock availability, and product comparisons. Providing instant, personalized assistance to every customer is expensive and difficult to scale.

Existing chatbots mainly answer predefined questions and lack the ability to understand customer intent, access live business data securely, or perform meaningful actions such as recommending products, adding items to the cart, or tracking orders.

There is a need for an intelligent, secure, and conversational AI shopping assistant that enables customers to interact naturally using voice or text while integrating seamlessly with existing e-commerce platforms. The solution should provide personalized recommendations, answer business-specific questions, execute shopping actions, and improve the overall customer experience without requiring businesses to expose their production databases.

**Challenges we ran into**

If this is for a hackathon, project report, or presentation, you can write:

### Challenges We Ran Into

* **Data Security & Privacy:** Convincing businesses to securely integrate their existing systems without exposing sensitive customer or business data.
* **Database Integration:** Designing a solution that works across different databases (MongoDB, MySQL, PostgreSQL) with varying schemas.
* **Schema Understanding:** Automatically identifying product-related tables and mapping them to a standard model despite different naming conventions.
* **Secure Data Access:** Avoiding direct database access by designing a connector-based architecture that keeps business data within the customer's infrastructure.
* **Real-Time Data Retrieval:** Ensuring inventory, pricing, and order information remain up-to-date while minimizing unnecessary data synchronization.
* **Natural Language Understanding:** Interpreting diverse customer requests and converting them into accurate product searches or business actions.
* **Voice Interaction:** Maintaining fast, natural, low-latency conversations using speech-to-text and text-to-speech technologies.
* **Cross-Platform Compatibility:** Building an SDK that can integrate seamlessly with different web frameworks and mobile applications.
* **Scalability:** Designing a multi-tenant architecture capable of serving multiple businesses while ensuring complete tenant isolation and high performance.
* **Trust & Adoption:** Creating an architecture that businesses feel comfortable adopting by prioritizing security, transparency, and minimal infrastructure changes.

These challenges shaped our decision to adopt a **connector-based architecture**, ensuring secure integration while providing real-time AI-powered shopping assistance.

**Best Use of ElevenLabs**

to generate the voice

**Best Use of MongoDB Atlas**

stored authentication data and database history

**Best Use of Gemini API**

to perform DB operations tools through MCV clients

Team **Pixel Pioneers** -- [Dipannita Chowdhury](https://github.com/lia-005), [Shahil Shaikh](https://github.com/Shahil-Shaikh), [Anik Dutta](https://github.com/anik0810), [Harshita Agarwal](https://github.com/Harshita2005-coder)

`2026-07-26`

---

### FoodBridge Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/good-bridge-ai-2925) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dhruvsoni83944-blip/FoodBridgeAi_HackVSIT7.0.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/8ouFrwFwj3E?si=qjSC415BS_S0VPzM) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Zero Food Waste Zero Hunger

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square)

**Challenges we ran into**

**Challenges We Ran Into**

**Live Syncing**: It was very hard to make the Donor screen update automatically the exact second a Volunteer clicks "accept". We had to fight with Firebase Firestore real-time listeners a lot to make it work.

**Too many user roles**: Making one single app work for 4 totally different people (Donor, NGO, Volunteer, Admin) without messing up the design was really tough. We had to build a complex Context state to handle who sees what.

**FSSAI Verification**: We wanted commercial restaurants to strictly upload license documents, but for normal home users we just wanted a fast OTP login. Handling both these flows together gave us many bugs initially.

**Live GPS Map**: Hooking up the browser's live location API so we can track the volunteer on a map with a countdown timer was very tricky, because it was making the app lag if we didn't manage the state perfectly

**The problem it solves**

**The Problem It Solves**

**Too much food waste**: Big hotels and wedding events are throwing away lots of good food everyday, but many people are still sleeping hungry because there is no way to connect them fast.

**Delivery problem:** NGOs want to take the food, but they don't have enough cars or live tracking to pick it up quickly before the food goes bad.

**Trust issues:** Restaurants are scared to donate because what if the food is bad and they get in trouble? There is no proper FSSAI checking.

**No single platform:** There is no one app where the donor, volunteer, and NGO can connect instantly and see the live status of the food delivery.

Team **Tech-Dal** -- Dhruv Soni, [Jaiveer Singh](https://github.com/Jaiveer18-Ai), [Lavesh Saini](https://github.com/laveshsaini), Rohit Sharma

`2026-07-25`

---

### RecoverX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/recoverx-977c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dacg13/Kinova-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://kinova-ai-zeta.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uyzQVLnL9iE) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Recover Smater. Move Better.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

**1. Real-time pose estimation was accurate, but not *fast enough* to feel real-time**

Our first pass used a standard pose estimation pipeline running frame-by-frame inference, but on a typical laptop webcam this introduced 200-300ms of lag between the actual movement and the feedback appearing on screen. For a rehab tool, that lag is the difference between "this feels like a mirror" and "this feels broken." We fixed it by downsampling frame resolution before inference, running detection on a fixed interval rather than every frame, and interpolating joint positions between detections — which got us under 80ms without losing accuracy on the joint angles that actually matter for form correction.

**2. Defining "wrong form" turned out to be a much harder problem than detecting joints**

Detecting a skeleton is the easy part. Deciding *when a movement crosses from "acceptable variation" into "actually wrong"* is genuinely hard — every body moves slightly differently, and a threshold that's too strict flags correct reps as wrong, while one that's too loose misses real mistakes. We ended up building exercise-specific tolerance ranges based on joint angle deltas rather than a single global threshold, and tuned them by recording and reviewing dozens of our own reps — both correct and deliberately incorrect — to find where the line should sit.

**3. Building the Digital Twin without it looking like a glitchy stick figure**

Our first attempt at the live biomechanical visualization just connected raw landmark points with straight lines, and because pose estimation isn't perfectly stable frame-to-frame, the result jittered constantly and looked unconvincing in a live demo — a serious risk given how much this feature matters to our pitch. We added smoothing across a short rolling window of frames and constrained joint movement to realistic biomechanical ranges, which stabilized the rendering enough to hold up under live camera conditions.

**The problem it solves**

Millions of people are prescribed home rehabilitation exercises after surgery or injury, and **66%** of them perform these exercises **incorrectly**, without ever knowing it. A wrong rep doesn't just slow recovery down. It can cause re-injury, increase pain, and push the patient right back to the clinic they were trying to graduate from.

The core failure isn't motivation — it's supervision. Once a patient leaves the clinic, no one is watching how they move. Existing rehab apps are just video libraries with reminders bolted on. They tell you *what* to do, but they have no idea *how* you're actually doing it.

**Kinova AI fixes this by turning any standard camera into a real-time physiotherapist.**

Using computer vision and AI pose estimation, Kinova watches every rep as it happens:

- Detects incorrect posture and joint misalignment **the instant it occurs**, not after the fact
- Gives real-time corrective feedback — the same cue a therapist would give standing in the room
- Builds a live **Digital Twin** of the patient's movement, visualizing joint angles, symmetry, and range of motion that a video call could never show
- Tracks recovery over time and turns raw movement data into a personalized recovery score and next-session recommendation

No wearables. No sensors. No extra hardware — just a camera and an internet connection.

**Who it's for:**
- **Patients** recovering from surgery, sports injuries, or chronic conditions who need guidance between appointments
- **Physical therapists** who currently have zero visibility into how patients perform exercises at home, and rely on patients self-reporting accurately
- **Healthcare systems** trying to reduce re-injury rates and unnecessary follow-up visits caused by improper home exercise execution

Physical therapy shouldn't stop when the appointment ends. Kinova AI makes sure it doesn't.

Dhruv Agrawal

`2026-06-30`

---

### Construction Projects predictor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/construction-projects-predictor-8e0c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://dapper-taffy-7c00ac.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/jhWgLVpC4ak) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Predict the risk. Before it becomes the cost."

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Construction projects blow past budgets and deadlines constantly — and most teams find out only after it's too late to fix anything.
This tool flips that around. Feed it a project's details — budget, planned duration, location, type, phase — and it predicts the probability of delay and cost overrun, estimates the expected delay in days and cost overrun amount, and breaks down the top risk factors behind that prediction, paired with actionable recommendations to reduce them. Risk gets surfaced before the project is locked in, not after the damage is done.
It's built around two roles sharing the same data, with completely different views:

Admins / project managers get a full portfolio view across every project they oversee — run new assessments, compare risk across dozens of sites side by side, and stay in control from a single dashboard.
Clients / contractors get a focused view of only their own project(s) — their risk score, their recommendations, with zero clutter from anyone else's data.

A contractor can sanity-check a project's risk before bidding on it. A PM managing a portfolio of projects across multiple sites can instantly see which one needs attention first. An investor gets an objective, data-backed read on project health instead of a gut feeling or a status update that's already stale by the time it lands.

**Challenges we ran into**

The hardest part wasn't the prediction model — **it was access control at scale.**
I needed one login screen to produce two completely different experiences across a growing portfolio of projects: admins see everything, clients see only their own, and that boundary had to hold even against someone hitting the API directly — not just hiding a button in the UI. I built this with Supabase Row Level Security, enforcing the rule at the database itself, so it can't be bypassed from outside.
Then I hit a bug that genuinely had me stuck: logins worked, but the wrong dashboard and wrong data started showing up. No error, no crash — just quietly wrong. The cause: a project's ownership column had been called user_id in some migrations and owner_id in others, so the newer role-based policies were silently filtering against a column that didn't match the live schema. Postgres doesn't complain about this — it just returns nothing, or the wrong rows, which made it look like a logic bug when it was actually a naming mismatch hiding across dozens of policies.
The fix was refusing to trust anything I hadn't personally verified against the live database — querying information_schema.columns and pg_policies directly instead of trusting what earlier code claimed. Once the real column name was confirmed, I rewrote every policy consistently, added a single is_admin() function so admin-override logic lived in exactly one place, and stress-tested it properly across multiple simulated clients and projects — confirming each client could only ever see their own project, while admins saw the entire portfolio, with zero leakage either way.
The lesson that stuck: a **security feature** isn't done when the plan reads correctly — it's **done when you've proven it against the real system, with real data, at real scale.**

[Gautham Poolakkal](https://github.com/Gautham-0824)

`2026-06-29`

---

### Clenzo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/clenzo-ff1c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BALASURIYA290506/clenzo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://clenzo-ten.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI-Powered Waste Reporting for Smarter Cities.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

Urban waste management still relies heavily on manual complaints, delayed inspections, and fragmented communication between citizens and municipal authorities. As a result, untreated waste often remains unattended for long periods, causing environmental pollution, health risks, and reduced public trust in civic services.

Citizens currently have no simple and rewarding way to report waste issues, while municipal teams struggle to prioritize complaints due to the lack of structured information. Existing reporting systems rarely verify the quality of reports or encourage active community participation.

CLENZO solves this by creating an AI-powered bridge between citizens and municipalities. Citizens can instantly report waste by uploading a photo, while Google Gemini Vision analyzes the waste, GPS captures the location, and municipal authorities receive structured reports for faster verification and resolution. A reward-based system further motivates citizens to actively contribute towards building cleaner and smarter cities.

**Challenges we ran into**

Building CLENZO within a hackathon timeframe required us to integrate multiple technologies into a seamless workflow.

One of our biggest challenges was implementing reliable AI-powered waste detection using Google Gemini Vision while ensuring that the analysis remained fast enough for a smooth user experience. Integrating Firebase Firestore for real-time report management and synchronizing updates across citizen and municipal dashboards also required careful planning.

Another challenge was designing role-based access, ensuring that municipal features remained accessible only to administrators while providing citizens with a simple and intuitive reporting experience.

During deployment, we also encountered issues related to environment variables and Firebase authentication on Vercel. After debugging the deployment configuration and securely managing API keys, we successfully deployed the application and connected all services in production.

These challenges helped us gain valuable experience in full-stack development, cloud deployment, and AI integration under tight deadlines.

[Balasuriya M](https://github.com/BALASURIYA290506)

`2026-06-29`

---

### RepoMind AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/repomind-ai-8401) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sahildk/RepoMind-AI/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://repo-mind-ai-vd9i.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Reconstruct Codebase Architecture Instantly. Over

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![REST API](https://img.shields.io/badge/REST%20API-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

1. **Mermaid.js Syntax Formatting:** LLMs often generate flowchart syntax with special characters (like dots in file extensions package.json or slashes in directory paths src/app) which cause Mermaid.js to crash when parsing. We solved this by developing a strict JSON validation prompt instructing Gemini to wrap all labels with special characters in double quotes and avoid any hanging nodes.

2. **GitHub API Rate Limits:** GitHub limits public API requests to 60 per hour for unauthenticated users. We optimized this by filtering out binary files, asset folders, and build noise (e.g. node_modules, .next, dist, .git) before processing, and allowing users to pass their own GitHub Personal Access Token directly from the frontend React state (stored securely in localStorage).

3. **Responsive Flow Canvas:** Making SVG charts responsive, zoomable, and pannable in Next.js required custom wrapper components around Mermaid.js to handle fullscreen views, SVG exports, and dynamic size recalculations on window resize.

**The problem it solves**

Traditional codebase analysis tools require downloading gigabytes of source code, setting up local Docker environments, or performing resource-heavy vector database indexing before they can explain how a project is structured. This creates massive latency, high token costs, and security risks by storing raw proprietary source code.

RepoMind AI solves this by reconstructing developer workspace architectures in seconds using a metadata-first approach. By querying public repository trees and dependency manifests on demand, it parses the topology, filters out binaries and build noise, and passes only the structural context to Gemini 2.5 Flash. Gemini then compiles the relationships into interactive, fully zoomable and pannable Mermaid.js flowcharts and generates maintainability dashboards. No heavy cloning, no indexing, and minimal token usage.

Sahil Deore

`2026-06-30`

---

### MemoSphere-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/memosphereai-ef6d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MuhammedMazinMH/memosphere-ai-build) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://memosphere-ai-build.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Hk-IjVe4vY4) [![Built at](https://img.shields.io/badge/Built%20at-Tech%20Genesis%20'26-0052CC?style=flat-square)](https://tech-genesis.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Second Brain for Smarter Learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Amazon Web Services (AWS)](https://img.shields.io/badge/Amazon%20Web%20Services%20(AWS)-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![DynamoDB](https://img.shields.io/badge/DynamoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![clerk authentication](https://img.shields.io/badge/clerk%20authentication-333333?style=flat-square)

**Challenges we ran into**

The biggest challenge was designing a system that could transform unstructured PDF documents into meaningful knowledge without losing important context.

Another challenge was generating a clean knowledge graph without showing irrelevant or duplicate concepts. We solved this by improving our AI prompt design, validating the AI responses using structured schemas and storing only clean data.

Integrating AWS DynamoDB with the application while maintaining user-specific knowledge was another learning experience. We also optimised document processing so that uploaded files, generated concepts, quizzes and analytics remained properly connected.

Finally, ensuring smooth synchronisation between all modules after every upload required careful handling so that the knowledge graph, search, AI coach and learning analytics always reflected the latest data.

**The problem it solves**

Students today study from multiple sources like lecture notes, PDFs, assignments and project documents. As the number of documents increases, finding important information becomes difficult and time consuming. Most students spend more time searching for notes than actually learning.

MemoSphere AI solves this problem by converting uploaded study material into a searchable knowledge base. It automatically extracts important concepts, generates a visual knowledge graph, provides AI-powered summaries, creates quizzes and helps students understand their weak areas through learning insights and exam readiness analysis.

Instead of reading the same documents again and again, students can quickly search, revise and learn from their own knowledge in one place.

Team **ChaiPeCode** -- MOHAMMED SAHIM, Poorna D Shetty, Muhammed Mazin MH, Abdul Basith

`2026-06-26`

---

### SKILLBRIDGE AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/skillbridge-ai-5217) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://skillbridge-three-eosin.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/kv9vlqvn9cU?si=U6SM7dg2xgUSaNho) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> SKILLBRIDGE AI Your Career. Decoded.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Students and fresh graduates often struggle to understand whether they are truly prepared for their desired careers. While job portals help users find opportunities, they rarely explain why a candidate is not a good fit or what specific skills they need to improve. As a result, many students apply blindly, receive rejections without feedback, and spend time learning skills that may not align with industry expectations.
How SkillBridge AI Helps
SkillBridge AI acts as a personalized AI career mentor that helps students make informed career decisions.
Users can:
Upload their resume and select their target role
Analyze their career readiness for a specific job
Identify skill gaps and missing competencies
Receive personalized learning roadmaps
Get recommendations for relevant projects and courses
Interact with an AI career mentor chatbot for guidance and support
Benefits
Eliminates guesswork from career planning
Provides actionable feedback instead of generic resume scores
Helps students focus on the most relevant skills and projects
Makes career guidance accessible, affordable, and available 24/7
Increases employability by aligning learning with industry requirements

**Challenges we ran into**

Challenges We Ran Into

One of the biggest challenges we faced was integrating and managing multiple API calls efficiently. Since SkillBridge AI relies on AI-powered resume analysis, skill-gap detection, roadmap generation, and chatbot interactions, we encountered issues with API response delays, inconsistent outputs, and handling large amounts of resume data.

Another challenge was ensuring that the information generated by different API calls remained consistent across the platform. For example, the identified skill gaps needed to align with the recommended courses, projects, and roadmap suggestions.

To overcome this, we optimized our API workflow, improved prompt engineering, implemented proper error handling, and structured the data flow so that outputs from one stage could be reliably used by the next. Through continuous testing and debugging, we were able to create a smoother and more reliable user experience.

This challenge taught us the importance of efficient API integration, data consistency, and building resilient systems when working with AI-powered applications.

Team **assasinJFK** -- [Humaira Aisha.U](https://github.com/humairaaishau2025-wq), Rathna Teja, [Peeyush Agnihotri](https://github.com/idontlikecoughsyrups)

`2026-06-14`

---

### MOLE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mole-4e5e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sarangchaudhari635-oss/MOLE_Nepal) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mole-nepal.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=Hn-GVic1KFg) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%202026-0052CC?style=flat-square)](https://deerhack26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Transforming Industrial Waste into Economic Value

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-333333?style=flat-square) ![Markdown](https://img.shields.io/badge/Markdown-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

In the traditional Linear Economy ("Take, Make, Waste"), industrial production faces critical bottlenecks:

    High Operational Cost: Factories pay enormous landfill tipping and waste disposal fees to discard secondary products and byproducts.
    Procurement Scarcity: Purchasing virgin raw materials is highly volatile, carbon-intensive, and expensive. Sourcing recycled materials is highly fragmented, rely on offline brokers, and suffers from a lack of quality control.
    Logistical Inefficiencies: Transporting waste over long distances is cost-prohibitive and contributes heavily to scope-3 emissions. Freight costs often kill the economics of recycling.
    Compliance & Audit Gaps: Companies struggle to track, compute, and report audit-ready ESG metrics (CO2 avoided, landfill diversion percentages, circularity indexes) required by regulators.

✨ The Circular Solution

MOLE bridges the gap between waste generators (Sellers) and recyclers/manufacturers (Buyers) through:

    AI-Powered Material Matching: Deterministically pairing compatible chemical and physical byproducts with exact buyer criteria.
    Proximity & Logistics Sorting: Prioritizing localized trade connections using geolocation distance sorting to minimize freight overhead.
    Predictive Waste Forecasting: Anticipating future waste outputs using scheduling and historical data to match streams before they even exit the assembly line.
    Circularity & ESG Analytics: Auto-calculating corporate circularity scores, tracking carbon emissions saved (compared to virgin material processing), and outputting audit-ready reports.
    Interactive Trade Connections Map: Visualizing localized industrial networks and tracking verified trade relationships over time.

**Challenges we ran into**

The Netlify Deployment "White Screen" (Vite Assets Path & SPA Routing Redirects)
The Hurdle: After deploying the frontend code to Netlify, users were greeted with a blank white screen, and the browser console showed 404 Not Found errors for all compiled JS and CSS bundles.
The Cause: In 

vite.config.ts
, the base property was set to '/MOLE/' (likely optimized for a GitHub Pages project path). However, on Netlify, the application is deployed under the root domain, causing Vite to request assets from /MOLE/assets/... instead of /assets/.... Additionally, typing a route directly in the address bar (e.g., /app/dashboard) bypassed the single-page React router and returned a standard server-side 404.
The Fix:
Adjusted the base property in 

vite.config.ts
 to '/' to resolve assets from the root.
Configured Netlify's build variables directly inside 

netlify.toml
 and added a standard SPA fallback redirect rules block (/* to /index.html with a 200 status code) to let React Router handle all path navigation.

**Environment**

MOLE (Circular Economy B2B Marketplace) is engineered from the ground up to solve critical environmental bottlenecks, making it a perfect fit for the Environment & Sustainability Track.

The platform addresses the core failures of the traditional Linear Economy ("Take, Make, Waste") by providing the software infrastructure needed to scale Industrial Symiosis—the practice of feeding one factory's byproducts and waste streams back into another factory's production line as raw materials.

Here is how the project directly impacts and fits into the Environment Track:

1. Landfill Diversion & Waste Optimization (Industrial Symiosis)
The Problem: Millions of tons of industrial byproducts, scrap materials, and manufacturing waste are dumped into landfills annually because factories lack visibility into who could reuse them.
MOLE's Solution: The marketplace actively tracks and categorizes material streams. Through the Impact Analytics dashboard, companies monitor their Waste Diversion Breakdown across four vectors:
Recycled: Processing waste into new raw materials.
Reused: Direct reintegration of byproducts.
Recovered: Energy or material recovery.
Landfill: Minimized to target a absolute zero-waste footprint.
Circularity Index: Companies are scored on a scale of 0 - 100 comparing their recycled-to-landfill ratios against industry percentiles to gamify and drive corporate environmental accountability.
2. Carbon Footprint Reduction (CO₂ Savings Trajectory)
MOLE achieves carbon reduction in two distinct ways:

Virgin Material Substitution: Manufacturing virgin raw materials (like primary plastics, steel, or chemicals) is highly energy-intensive. Sourcing secondary (recycled/reused) materials requires a fraction of that energy. The platform calculates CO₂ saved using Life Cycle Assessment (LCA) coefficients: $$\text{CO₂ Saved} = \sum \Big(\text{Volume} \times (\text{Virgin Material Factor} - \text{Recycled Process Factor})\Big)$$
Proximity Logistics & Haversine Distance Sorting: Transportation is a primary driver of Scope-3 emissions. MOLE's smart matching engine uses the Haversine formula to calculate the geolocation distance between buyers and sellers, factoring Proximity heavily into the match score (worth up to 25 points out of 100). By prioritizing localized trade networks, it minimizes freight emissions.
3. Real-World Impact Translation
To make environmental impacts tangible for business stakeholders and auditors, MOLE translates abstract metric tons of carbon and waste into relatable, real-world equivalencies in the 

ImpactAnalytics.tsx
 page:

🌳 Trees Saved: Translates carbon avoided into the number of mature trees needed to absorb that amount of carbon per year.
⚡ Coal Avoided: Represents the tonnes of coal that were not burned to generate the energy saved during extraction and processing.
💧 Water Conserved: Computes the liters of water saved by using recycled processes instead of water-intensive primary resource extraction.
🚗 Cars Off the Road: Measures the equivalent annual emissions of passenger vehicles removed from highways.
4. Direct Support for ESG Reporting & Green Compliance
As environmental regulations tighten globally, corporations struggle to compile clean, auditable ESG (Environmental, Social, and Governance) data. MOLE automates this process by tracking every transaction's carbon footprint, water footprint, and landfill diversion rate. This provides companies with exportable, audit-ready data to claim carbon credits, qualify for green tax incentives, and meet regulatory reporting standards.

Team **Krazy K0ders** -- [Sarang Chaudhari](https://github.com/sarangchaudhari635-oss), Harsh Prabhu

`2026-06-13`

---

### “AyurTrace”
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ayurtrace-e082) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://psychic-waffle-pjw767wrg9jjf9wx6-5173.app.github.dev/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> “From Forest to Formula — Transparent. Trusted"

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

“The biggest challenge was integrating blockchain transparency with a user-friendly system that rural farmers and consumers can both use easily.”

**The problem it solves**

“AyurTrace solves the problem of counterfeit, untraceable, and non-transparent Ayurvedic herb supply chains using blockchain-based geo-tagged traceability.”

Team **Hackops** -- [Dipendu Samanta](https://github.com/jitu318)

`2026-05-17`

---

### Geo tracking of waste
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/geo-tracking-of-waste-3728) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/varsha28-code/Geo-Tracking-of-Waste) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> A smart waste management system

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AngularJS](https://img.shields.io/badge/AngularJS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Built a full-stack web application for real-time smart waste monitoring, improving tracking efficiency by 30% using YOLOv3 and geolocation.

**Challenges we ran into**

One major hurdle I faced while building the "Geo-Tracking Waste Management System" was handling inaccurate real-time location updates from waste collection vehicles.

During testing, the GPS coordinates sometimes showed incorrect positions or delayed updates because of weak network connectivity and inconsistent sensor data. This created problems in route tracking and made the dashboard display unreliable vehicle movements.

[Srivarsha Akula](https://github.com/varsha28-code)

`2026-05-22`

---

### VoiceCoach
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/voiceagent-d144) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prateek-Wayne/voice-agent) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://voice-agent-coach.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Learn speaking through live AI conversations.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Natural Language Processing](https://img.shields.io/badge/Natural%20Language%20Processing-333333?style=flat-square)

**Challenges we ran into**

# Challenges I Ran Into

One of the main challenges was experimenting with the traditional voice pipeline:

`Speech → Speech-to-Text → LLM → Text-to-Speech`

Connecting all these parts together in real time was more difficult than expected. I faced several issues while working with the `AudioContext` graph pipeline, especially around audio streaming, playback timing, and handling microphone/speaker audio correctly.

Another challenge was managing the flow between speech input, sending data to the LLM, and receiving streamed responses back smoothly without noticeable delay.

After experimenting with different approaches, I realized the pipeline could be simplified significantly by using Google Gemini Live APIs, which provide built-in voice-to-voice interaction instead of manually handling separate speech-to-text and text-to-speech stages.

**The problem it solves**

# The Problem It Solves

This project is a demo real-time AI speaking practice platform that helps users improve conversation, pronunciation, and listening skills using live voice interactions. Users can speak directly with an AI tutor and receive spoken responses instantly without typing or complex setup.

## What People Can Use It For

- Conversation practice for interviews, travel, or daily communication.
- Pronunciation and listening practice using natural AI voice responses.
- Learning/demo purposes to showcase real-time voice interaction with AI models.

## How It Helps

- Makes speaking practice simple and interactive.
- Removes the need to type messages during practice.
- Gives quick spoken responses for a more natural conversation experience.
- Supports multiple languages for basic conversational learning.

## Supported Languages

- English (US) — `en-US`
- English (UK) — `en-GB`
- Spanish — `es-ES`, `es-MX`
- French — `fr-FR`
- German — `de-DE`
- Japanese — `ja-JP`
- Korean — `ko-KR`
- Chinese — `zh-CN`
- Hindi — `hi-IN`
- Portuguese — `pt-BR`

Prateek Verma

`2026-05-24`

---

### Lumen
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lumen-2397) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/isjustabhi/Lumen--Your-Focus-Alive) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lumen-your-focus-alive.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Watch your discipline become a place.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![WebGL](https://img.shields.io/badge/WebGL-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

**Weather transitions that felt like weather, not a state machine.**
The first cut snapped between clear, rain, and storm instantly — it read as "state changed" instead of "the sky is closing in." I fixed it by crossfading cloud darkness, rain particle density, color saturation, and sun intensity over a 2-second window, each on its own eased curve. Now the storm rolls in rather than appearing.

**Browser audio gating across Chrome and Safari.**
Tone.js needs a real user gesture to start, and the rules differ between browsers. Calling Tone.start() in a useEffect or on mount silently fails in Safari. The fix was strict discipline: Tone.start() runs only inside the Begin button's onClick and the audio toggle's onClick. Never anywhere else. The audio toggle in settings also re-validates the context on every flip.

**Bundle weight from R3F + Tone.js + MediaPipe.**
The naive bundle was huge and Vite was warning about chunk size on every build. I solved it three ways: manualChunks in vite.config.ts splits three, R3F, drei, postprocessing, and tone into named chunks for parallel loading. Tree instances and flower instances use InstancedMesh so 100 plants is one draw call instead of a hundred. MediaPipe is lazy-loaded — the FaceDetector only ships if the user enables webcam attention in settings, which is off by default.

**Making the completion cinematic feel like a reward, not a modal.**
Early versions just popped a success card. It felt like a tax form. The breakthrough was an 8-second silent celebration before any UI appears — the aurora unfurls, 200 fireflies rise from the island, bloom warms, a I-V-vi-IV chord progression resolves over 6 seconds — and only then does the stats card slide up from the bottom. The world celebrates first. The UI is a footnote.

**Persistence + the demo URL.**
The whole premise ("your island grows over weeks") collapses if a hard refresh wipes everything. I wired Zustand to localforage so the ecosystem, history, streak, and seed all survive. Same user gets the same island forever. For the demo, a ?demo=showcase query param hydrates a mock state of 47 sessions and 32 trees so judges see a mature island the moment they land — without me having to actually focus for 19 hours before the submission.

**The problem it solves**

Every focus app punishes you when you slip.

Streaks you'll inevitably break. Timers that turn red. Trees that wilt and die. A trail of guilt notifications that pile up until you delete the app three days in.

The honest data: shame-based productivity tools work for about a week. Then they become another source of stress, one more thing demanding performance from people who downloaded a focus app because they were already struggling.

Lumen solves this with the opposite model: intrinsic reward instead of extrinsic punishment.

You open Lumen and you see your island, a procedurally generated, low-poly 3D world that's yours forever. You pick a duration (15, 25, 45, 60, or 90 minutes) and hit Begin. While you focus, the world responds in real time. Trees sprout. Flowers bloom. The sun arcs across the sky. Butterflies drift. A generative ambient soundtrack, built live in your browser, not a static loop, breathes underneath it all.

When you get distracted and switch tabs, the sky darkens, rain falls, color drains from the world, lightning flashes. When you return, the sun breaks through, the storm lifts, and the world heals. Visibly. In real time. No modal pops up to scold you. No streak resets. The world reacting is the feedback.

When the session ends successfully, an aurora ribbon unfurls across the sky, 200 fireflies rise from the island, a chord progression resolves, and a card slides up: "Today you grew 2 trees and 4 flowers." Your island is now slightly richer, forever.
![image](https://assets.devfolio.co/content/1227a16dadd248bf8e85992b7ae6713f/50cd503b-d9bd-4394-87b9-4259fdb5eb51.jpeg)
Use Lumen for:
- Deep work sessions where you need a beautiful, non-distracting environment
- Studying that feels rewarding instead of punishing
- Replacing Pomodoro apps that have made you feel like garbage
- Building a visible, weeks-long record of the discipline you've put in

Built entirely on the web. No download, no sign-in, no backend, no data leaves your browser. Open the link, hit Begin, and watch your discipline become a place.

[Abhiram Varma Nandimandalam](https://github.com/isjustabhi)

`2026-05-26`

---

### Mela
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mela-a2fb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sarinsanyal/godsofdev-synchronocity-s2) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/OQ_8Rf21Avk) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI Event Recommendation App with Map and Swiping

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

Mela is a AI Powered Community Event Discovery and Management Platform that is graphically and Maps. It acts as a centralized hub for locals, creators, and organizers to bring people together.

**Challenges we ran into**

Integrating the Mobile (react native) with the AI and Clerk Auth and Supabase DB.

Making the UI/UX Intuitive.

**AI/ML**

We had to design a Recommendation Engine which evolves over time with the user interaction and the event data. It personalizes according to their choices.

**Open Innovation**

This was completely using AI and App Dev with an Express Backend. So this is Open Innovation.

Team **GodsOfDev** -- [Sarin Sanyal](github.com/sarinsanyal), [Debshuvra Sarkar](https://github.com/Synapse-CodeX), [Arghadip Dutta](https://github.com/devop123-glitch), [Soham Nandi](https://github.com/SohamNandi06)

`2026-05-31`

---

### AgentFoundry
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agentfoundry-f9d8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VladBosovets/AgentFoundry) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agentfoundry-production.up.railway.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Launch an AI-powered micro-business in 30 seconds

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square)

**The problem it solves**

Starting a service business takes weeks: writing a pitch, figuring out pricing, building a checkout, delivering the work. AgentFoundry collapses all of that into one text field.

You describe an idea — "resume optimization service" or "cold email writer" — and AgentFoundry:

1. **Generates the business** — Claude writes the name, tagline, service description, and a specialized AI fulfillment prompt
2. **Creates a live storefront** — instant public page with a working Locus payment checkout
3. **Fulfills every order automatically** — when a customer pays, the AI agent delivers the output in seconds
4. **Adapts without you** — a Lifecycle Intelligence engine watches every order and autonomously adjusts pricing, evolves the AI's prompt through iterative optimization, and regenerates the entire business concept if performance tanks

It's not a template builder. Every business is a live AI agent that self-improves over time — lower success rates trigger price cuts and prompt rewrites; sustained high demand raises prices and refines the agent's behavior. No code, no ops, no manual intervention.

**Challenges we ran into**

**Claude cutting off mid-JSON** — The business generator occasionally hit the token limit inside a nested string, producing truncated JSON that failed to parse. We fixed this with a three-layer extraction strategy: direct parse → code fence extraction → brace-boundary regex, plus increasing `max_tokens` and tightening the prompt to keep the fulfillment prompt concise.

**Making the lifecycle engine testable** — The adaptation logic touches pricing, prompt evolution (which calls Claude), and business regeneration (which also calls Claude) all in one run. Getting Jest mocks to intercept the right module boundaries required careful ordering — mocking `@anthropic-ai/sdk` before `require('../src/lifecycle')` is evaluated, so the Haiku call inside `evolvePrompt` never fires in tests.

**Keeping state sane across the store layer** — We needed the same codebase to run with an in-memory store in tests and Postgres in production with zero conditional logic in business code. We solved this with a factory pattern: `store.js` exports whichever implementation `DATABASE_URL` points to, and both satisfy the same async interface. TDD drove the Postgres implementation — 15 store tests written before a single SQL line.

**Secret scanning blocking the first push** — An `.env` file with a live API key had been committed in the root commit before `.gitignore` was in place. GitHub rejected the push. We rewrote history with an orphan branch and force-pushed to clear it from all reachable commits.

Team **vladb** -- Vlad Bosovets

`2026-05-21`

---

### GreenScore
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greenscore-f697) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AtharvGunda/GREENSCORE) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/TV51VRNxwVQ?si=1WAQ4pxiUik9cHFR) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Generates Carbon Score For SME's

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

The climate economy is growing rapidly, and billions of rupees are being allocated for green financing. But there’s a major infrastructure problem: banks still have no simple way to identify which SMEs are genuinely environmentally responsible, while SMEs have no standardized way to prove their sustainability performance.
As a result, green capital exists, businesses need it, regulators are pushing it but the system remains disconnected. This slows down climate action, delays sustainable industrial growth, and leaves a massive green financing gap in the SME sector.

**Challenges we ran into**

Building GreenScore in 48 hours meant navigating real-world complexity — no verified SME emission benchmarks existed in India, so we built the methodology ourselves using CEA, MoEFCC, and SEBI's own data, which means we're not dependent on anyone else's dataset. Self-reported data creates trust questions, which we've already identified as our next product — utility bill integration and third-party verification. The two-sided market cold start is a sequencing challenge we've solved by targeting SIDBI first, who has an active incentive to send us deal flow. And being unregulated today means we move faster than any regulated incumbent — by the time SEBI's ESG Rating Provider framework is notified, we'll already have the largest green SME dataset in India. Every challenge we ran into turned out to be a gap nobody else had filled — and that's precisely why GreenScore exists.

**Open Innovation**

GreenScore is an open-innovation platform because it transforms publicly available government climate and sustainability data into a practical financial intelligence system.
The green finance ecosystem already exists — banks want to give green loans, regulators are pushing sustainability, and SMEs want cheaper capital — but the system lacks a trusted environmental verification layer connecting both sides. GreenScore bridges that gap by converting complex environmental data into a simple, standardized sustainability score that financial institutions and SMEs can actually use.”
![image](https://assets.devfolio.co/content/cf58490859994bcaaa7f9e0f61c7e5df/b5747c46-b582-49c5-9b98-f19445dfe10b.png)

![image](https://assets.devfolio.co/content/cf58490859994bcaaa7f9e0f61c7e5df/2e75b45e-e9e5-4577-b31f-5b7ed5f49dd4.png)

![image](https://assets.devfolio.co/content/cf58490859994bcaaa7f9e0f61c7e5df/04fa10a0-58f9-496d-ad0e-ffef5a815818.png)

Team **VIBE CODERSS** -- [Atharv Gunda](https://github.com/AtharvGunda), [Varun chiniwalar](https://github.com/Varun12252004), [Ramprasad Kulkarni](https://github.com/ramklk), [Ajit Shetti](https://github.com/AjitShetti)

`2026-05-10`

---

### PrivaSense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/privasense-11a1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://priva-sense-rho.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=yA_hH1sVGCA) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Detecting Cognitive Drift Before It Become Decline

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![LibROSA](https://img.shields.io/badge/LibROSA-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Whisper](https://img.shields.io/badge/Whisper-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Millions of elderly individuals experience gradual cognitive decline, but early symptoms of conditions like Alzheimer’s and Dementia often go unnoticed until they become severe and irreversible. Traditional clinical assessments are expensive, infrequent, inaccessible in many regions, and usually capture only a single snapshot of a patient’s condition.

PrivaSense solves this by providing a privacy-first, AI-powered cognitive health monitoring platform that continuously tracks cognitive changes using speech, motor, and behavioral analysis. It enables early detection of cognitive drift through non-invasive assessments, helping caregivers and clinicians intervene sooner.

The platform makes cognitive monitoring more accessible, affordable, and safer by:

* Allowing remote assessments from home
* Providing multilingual support for wider accessibility
* Offering explainable AI insights clinicians can trust
* Sending real-time caregiver alerts during sudden decline
* Processing sensitive audio data locally without sending it to external AI services

PrivaSense ultimately helps families monitor elderly loved ones with dignity, transparency, and complete control over their data.

**Challenges we ran into**

One of the biggest challenges we faced was implementing reliable audio processing while maintaining complete user privacy. Since we wanted all speech analysis to happen locally without relying on third-party APIs, optimizing Whisper-based transcription and feature extraction on limited hardware became difficult. We overcame this by redesigning parts of the pipeline to use lightweight preprocessing with Librosa and asynchronous FastAPI workflows for smoother performance.

Another major hurdle was managing real-time cognitive scoring and explainability together. Integrating SHAP explanations with dynamically generated risk scores initially caused inconsistent outputs and slow inference times. We solved this by refining our feature engineering pipeline, caching intermediate results, and simplifying the explainability layer for faster and more interpretable insights.

We also encountered deployment issues related to environment variable exposure, MongoDB authentication, and frontend-backend synchronization during cloud deployment. Through iterative debugging, secure `.env` handling, and restructuring our API configuration, we stabilized the deployment pipeline successfully during the hackathon.

**AI & ML**

PrivaSense belongs specifically to the **Applied AI/ML Healthcare domain**, with strong foundations in:

* **Speech Intelligence**
* **Behavioral Signal Processing**
* **Explainable AI (XAI)**
* **Predictive Healthcare Analytics**
* **Human-Centered AI Systems**

The core intelligence of PrivaSense is built around analyzing cognitive biomarkers from speech and motor behavior using machine learning pipelines. Instead of using manually programmed rules, the platform leverages AI-based feature extraction and inference mechanisms to identify subtle neurological patterns associated with early Alzheimer’s and Dementia progression.

From a domain perspective, the project integrates several specialized AI areas:

### 🧠 1. Speech AI & Audio Intelligence

PrivaSense uses Whisper and Librosa for:

* Speech transcription
* Pause-duration analysis
* Speech fluency tracking
* Vocal variance and rhythm analysis
* Temporal speech feature extraction

These are commonly used techniques in computational paralinguistics and cognitive speech analysis.

### 📊 2. Predictive Machine Learning

The platform generates a **Progressive Decline Index (PDI)** using extracted behavioral and audio features. This transforms raw multimodal data into predictive cognitive risk scores capable of identifying longitudinal decline trends.

### 🔍 3. Explainable AI (XAI)

Healthcare AI systems require transparency and interpretability. PrivaSense integrates SHAP-based Explainable AI to break down how each feature contributes to a patient’s risk score, improving clinician trust and reducing black-box decision making.

### 🧬 4. AI-Driven Digital Health Monitoring

The project functions as an intelligent digital biomarker system that continuously monitors cognitive wellness remotely. This places it within the rapidly growing domain of AI-assisted preventive healthcare and remote patient monitoring systems.

### 🔐 5. Privacy-Preserving AI

Unlike many cloud-based healthcare AI tools, PrivaSense performs local audio processing to preserve sensitive patient data. This aligns with emerging research areas in privacy-first and edge AI systems for healthcare applications.

Because the platform performs multimodal feature extraction, predictive inference, explainability, and adaptive cognitive monitoring using AI models, PrivaSense is a domain-specific AI/ML healthcare solution rather than a conventional healthcare management application.

**Google Gemini**

Google Gemini is well-suited for PrivaSense because it enables advanced multimodal AI capabilities, including contextual reasoning over speech-derived cognitive patterns, behavioral summaries, and patient interaction data. Its strong natural language understanding can support adaptive wellness recommendations, conversational healthcare assistance, multilingual interaction, and intelligent report summarization while integrating efficiently with healthcare-focused AI workflows.

**MongoDB Atlas**

MongoDB Atlas is ideal for PrivaSense because the platform generates heterogeneous and evolving healthcare data such as speech features, cognitive scores, longitudinal assessments, caregiver mappings, and explainability outputs. MongoDB’s flexible document-based schema allows efficient storage of semi-structured multimodal patient data while Atlas provides scalable cloud deployment, secure access control, high availability, and seamless FastAPI integration for real-time AI-driven healthcare applications.

Team **NoByte** -- [AYUSH CHOUDHARY](https://github.com/aice18), [Ashish Sharma](https://github.com/ashisharma06), [Dhanush N](https://github.com/dhanush-n8n), [Jyotsna G](https://github.com/jyotsnag-l)

`2026-05-10`

---

### agenttollgate
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agenttollgate-9169) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/janneh2000/agenttollgate) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ZSpPK4O5GWs) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The 60-second paywall for AI agents.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![USDC](https://img.shields.io/badge/USDC-333333?style=flat-square)

**The problem it solves**

AI agents are about to spend money on the open web — but the payment infra they need doesn't exist yet. Stripe was designed for humans clicking "Buy now," not autonomous agents calling APIs at machine speed. The result: every API team that wants to sell to agents has to roll their own paywall, key rotation, abuse limits, and reconciliation — or just give up and stay free.

AgentTollgate is a drop-in paywall layer that wraps any HTTP API behind a CheckoutWithLocus toll. You point it at your upstream URL, set a price, and you get a tollgated endpoint that:

- Returns HTTP 402 Payment Required with a Locus pay URL when an agent calls without payment
- Settles the payment in USDC on Base via CheckoutWithLocus
- Replays the original request upstream once paid, returning the real response with x-locus-receipt
- Comes with a policy DSL (per-agent spend caps, geo rules, allow/deny lists) and reputation-based dynamic pricing (good agents pay less, brand-new or flaky agents pay a multiplier)
- Exposes itself over MCP so any Claude/GPT/Anthropic agent can discover and pay for tollgates the same way it discovers tools

A merchant goes from "I have an API" to "AI agents can pay me in USDC" in under 60 seconds. No custom auth, no Stripe Connect, no chargebacks.

**Challenges we ran into**

1. The 402 replay loop under concurrent retries. An agent that gets 402'd will retry. If the retry lands before the webhook confirms payment, we'd either double-charge or serve a stale response. We solved this by keying every session by Locus's session_id directly, so retries with the same x-locus-receipt are O(1) idempotent lookups, and we re-confirm with Locus on every replay rather than trusting our local cache.

2. Designing reputation scoring that doesn't punish new agents permanently. A naive score-based multiplier locks new agents out forever. We landed on a 0–1000 score with a 1.6 - score/1000 multiplier — new agents start at 500 (1.1× price), good agents drift toward 1× over time, and abusive agents climb toward 1.6× before policy hard-caps them out.

3. Locus's API surface is still evolving. We wrote a thin client (src/lib/locus.ts) with a mock-mode fallback so the proxy, dashboard, and MCP server all develop against a stable interface. Swapping in production keys is a one-line change.

4. better-sqlite3 native bindings across Node versions. The prebuild for Node v22 darwin-arm64 wasn't downloading on `npm install --omit=optional`. Lazy-initializing the DB in `src/lib/db.ts` (so the binding only loads on first call, not at import time) plus a documented `npm rebuild better-sqlite3 --build-from-source` step in the README fixed it.

5. Making the 402 flow legible in a pitch deck. Sequence diagrams in pptxgenjs are painful. We ended up drawing it slide-by-slide as vertical lifelines with widely-spaced arrow rows so the agent ↔ Tollgate ↔ Locus ↔ Upstream interaction reads at a glance.

**Track: Checkout with Locus**

AgentTollgate is built entirely around CheckoutWithLocus — it's the payment rail that makes the whole proxy work.

How we use it, end to end:

1. Session creation (preflight) — Every 402 response mints a fresh CheckoutWithLocus session via `preflight()` in `src/lib/locus.ts`, with the tollgate ID, price in USDC micros, agent ID, and a client-reference for reconciliation. The returned pay_url and approval_url go straight into the 402 body so the agent can pay.

2. Receipt verification (confirm) — When the agent retries with x-locus-receipt: <session_id>, we re-confirm with Locus on every replay (not just at webhook time) so refunded or disputed sessions can't replay a paid response.

3. Webhook handling — src/app/api/webhooks/locus/route.ts HMAC-verifies the Locus webhook and updates session state, so the dashboard reflects real-time settlement.

4. USDC on Base — All settlement happens in USDC on Base, with the merchant's payout address attached at tollgate-creation time.

5. Production-ready abstraction — The entire Locus integration is encapsulated in src/lib/locus.ts. Production API keys swap in without touching the proxy, dashboard, or MCP server. We ship with a mock-mode for local dev so the demo works without live keys.

The result is the simplest possible CheckoutWithLocus surface for an entire new category of buyer: AI agents paying for API calls in real time. Any developer with an HTTP endpoint can wire it up in under a minute and start accepting agent payments through Locus.

ALIE JANNEH

`2026-04-26`

---

### ZEARCH
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zearch-d3a4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XZNON/ZEARCH) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.loom.com/share/fd5724b567dd413185b1af251f7e795f) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/fd5724b567dd413185b1af251f7e795f) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Zearch — Doubt? → Live Application in Seconds

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square)

**The problem it solves**

Have you ever searched online for a WHAT IF scenario but don't quite get what you asked for? Wont it be super cool if you searched for something and you could get an answer visually, be able to manipulate according to your will. 
WHAT IF is exactly that, it takes your what if scenarios and gives you a live working dynamic website, still not quite what you wanted well no worries, you can prompt further until you're satisfied.  Its a SEARCH but better, its a ZEARCH.

Every time we search for something whether it’s a financial calculation, data analysis, or a decision we get information, not tools.

**You search:**

“If I invest ₹10k/month for 10 years at 12% return?”

And you get blog posts, static answers, or generic calculators that don’t quite fit your needs. Even AI only gives you answers in text.

**We asked:**

What if instead of searching for tools, you could generate them instantly?

That’s where LiveAnswer came from.

**What it does?** 

LiveAnswer turns natural language into fully functional, live web applications.

**Instead of returning text, it:**

generates a complete interactive app
deploys it instantly using Locus
returns a live URL in seconds

Every prompt becomes a working product.

**Key Features**
- Prompt → App Generation 
- Converts user input into a React-based interactive application
- Instant Deployment via Locus
- Automatically provisions infrastructure (project, service, deployment)

 **Modify & Redeploy**
Users can evolve apps with follow-up prompts

With the help of buildWithLocus platform and APIs, we were able to generate applications , get live and factual data, whip up a container on the spot.

**BuildWIthLocus is the core of the project as this is where you live applications are created, hosted and destroyed. **

***What you can do:***

1) **Data **→ **Interactive Insight**

(Turn raw data into a mini SaaS dashboard)

2)**Simulators & Calculators**

3)**Learning by Doing**

“Visualize how quicksort works”
→ animated sorting app
“Teach me binary trees”
→ drag & build tree
“Projectile motion simulation”
→ change angle, velocity

4)** Dev Tools as Apps**

“Create a JSON formatter + validator”
“Regex tester with live matches”
“SQL query playground”
“API tester like Postman”

5)**“What-if” Explorers**

“What if I save 20% more every year?”
“What if CAC increases 2x?”
“Population growth simulation”
“Business profit scenarios”

**Challenges we ran into**

**1. CDN timing issues (Recharts crash)**

Generated apps relied on CDN libraries like Recharts, which don’t always load before execution.

This caused runtime errors like:

window.Recharts is undefined

*Solution:*

implemented runtime readiness checks
delayed rendering until libraries loaded
added fallback UI

**2. Making AI-generated apps reliable**

LLM outputs are not always production-safe:

missing guards
unsafe assumptions
runtime crashes

*Solution:*

built a post-processing layer
patched generated HTML before deployment
enforced safe patterns

**3. Dynamic deployment orchestration**

Each request required:

project creation
service provisioning
git push deployment
polling status

Managing this in real time with low latency was challenging.

*Solution:*

optimized deployment pipeline
efficient polling
scheduled teardown system

**Track: Using BuildWithLocus to leverage our suite.**

The core of the project relies on BuildWithLocus's platform and its APIs, it uses the API wrappers to generate applications on spot and uses containers created by BWL to host that appliation. With the ability also to destroy the applications built on spot or after a set time using BWL's APIs.

Team **Dhurandar** -- [Shivalik Singh](https://github.com/XZNON)

`2026-04-22`

---

### FinGuard-Nexus
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/finguardnexus-7242) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shubhang-8/FinGuard-Nexus) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://finguard-nexus-auaxvwumaeekxkdybquvz7.streamlit.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XGH2pn1TPi0) [![Built at](https://img.shields.io/badge/Built%20at-DAYZERO%202.0-0052CC?style=flat-square)](https://dayzero2o.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> 6-Hour Audits into 60-Second AI Insights

![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![pathlib](https://img.shields.io/badge/pathlib-333333?style=flat-square) ![Claude 3.5 Sonnet](https://img.shields.io/badge/Claude%203.5%20Sonnet-333333?style=flat-square)

**The problem it solves**

FinGuard-Nexus addresses the critical "AI Trust Gap" in the financial sector. Currently, compliance teams are forced to choose between slow, manual audits—taking up to 6 hours per report—or "Black Box" AI systems that often hallucinate regulatory data, creating massive legal liabilities.

FinGuard-Nexus solves this by:


Eliminating Hallucinations: Our proprietary Hallucination Shield cross-references every AI-generated claim against raw Ledger Row IDs, ensuring 100% data grounding.


Drastic Velocity Gains: We transform the manual 6-hour SAR generation process into a 60-second automated workflow.


Mathematical Integrity: An autonomous Integrity Agent performs vectorized reconciliation to catch "fat-finger" errors and ledger mismatches that humans often overlook.


Regulatory Defensibility: Every decision is backed by a timestamped Multi-Agent Decision Timeline, providing a clear audit trail for regulators and auditors.Multi-Agent Synchronization: One of the biggest hurdles was ensuring that the Forensic Agent and the Governance Agent could communicate without losing context. I solved this by implementing a centralized state management system where each agent contributes to a shared "Decision Timeline".

Zero-Hallucination Enforcement: It was difficult to force the LLM to stick strictly to the ledger data. I overcame this by building the Hallucination Shield—a post-processing layer that uses Python to parse the AI's narrative and verify every name and amount against the source CSV.

Environment Agnostic Pathing: I ran into issues with file pathing when moving from local development to Streamlit Cloud. I fixed this by utilizing the Pathlib library to ensure the system handles regulatory rule-sets correctly across different operating systems.

**Challenges we ran into**

Multi-Agent Synchronization: One of the biggest hurdles was ensuring that the Forensic Agent and the Governance Agent could communicate without losing context. I solved this by implementing a centralized state management system where each agent contributes to a shared "Decision Timeline".

Zero-Hallucination Enforcement: It was difficult to force the LLM to stick strictly to the ledger data. I overcame this by building the Hallucination Shield—a post-processing layer that uses Python to parse the AI's narrative and verify every name and amount against the source CSV.

Environment Agnostic Pathing: I ran into issues with file pathing when moving from local development to Streamlit Cloud. I fixed this by utilizing the Pathlib library to ensure the system handles regulatory rule-sets correctly across different operating systems.

Team **Horcrux** -- [Shubhang Kedia](https://github.com/Shubhang-8), [Yash Saxena](https://github.com/yashsaxena2209), [Riya Baliyan](https://github.com/Riyab15)

`2026-04-16`

---

### ICD Decoder
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/icd-decoder-8948) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yuvrajai1234-work/ICD-Decoder.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://icd-decoder.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/Bl5bivcKZyQ?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-DAYZERO%202.0-0052CC?style=flat-square)](https://dayzero2o.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Demystifying diagnostics

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Manual ICD-10 Coding Burden 🏥

Medical coders manually read clinical documents (discharge summaries, operation notes, triage logs) and assign ICD-10 diagnosis/procedure codes
Time-consuming, error-prone, and expensive for healthcare organizations

Insurance Claims Delays 💰

Incorrect or delayed ICD-10 coding directly impacts claim processing and reimbursement
Wrong codes = denied claims, revenue loss, or overpayments
Current manual process creates bottlenecks in claims submission

Healthcare Research Data Quality 📊

Researchers need accurately coded medical data for epidemiology, quality studies, and outcome analysis
Manual coding inconsistencies introduce errors in research datasets

Real-World Value:
For Insurance Companies: Faster claims processing, reduced denials, better fraud detection
For Healthcare Providers: Reduced coding staff burden, faster billing cycles, improved cash flow
For Researchers: Consistent, audit-able coded datasets for quality studies and outcome analysis
For Compliance: Full traceability for medical coding audits and regulatory requirements
Technical Implementation:
Uses TF-IDF + machine learning (not just rule-based) trained on mtsamples.csv medical records
Maps medical specialties → ICD-10 code ranges + keyword matching
Live deployment at https://icd-decoder.vercel.app
This is a productivity multiplier for healthcare's most tedious administrative task while maintaining human oversight for quality assurance.

**Challenges we ran into**

1. Multi-Service Architecture 
Complexity

Challenge: The system spans 3 layers (Next.js frontend, Node.js API, Python Flask ML service)

Issue: Services must communicate reliably, especially with cold start delays on Render

Evidence: Code shows 60-second timeout handling for ML API:
TypeScript
export const maxDuration = 60; // Allow for Render's cold start

2. ML-Backend Communication & Deployment

Challenge: Python Flask backend (ML service) deployed separately on Render, which has cold starts

Impact:
Predictions fail if ML service is unresponsive or starting up
Graceful error handling needed throughout (see error responses with fallbacks)
Environment variable ML_API_URL must be correctly configured

3. Missing ICD-10 Ground Truth Data

Challenge: mtsamples.csv contains clinical text but NO actual ICD-10 codes

Workaround: Had to create manual specialty → ICD-10 mapping (essentially rule-based)

Limitation: This reduces model accuracy vs. supervised learning with real labels
Code note: Implementation uses TF-IDF + keyword matching as proxy for true medical coding

Team **Snipe Coders** -- [Akshat Singh](https://github.com/Akshat-Singh-SRM), [LAKSH NAGORI](https://github.com/Lakshnagori1508), YuvRaj Thakur

`2026-04-17`

---

### Revenue Recovery Engine
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/revenue-recovery-engine-be32) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pranavghuge/AI-Revenue-Recovery-Engine.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai-revenue-recovery-engine.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#1-0052CC?style=flat-square)](https://paygentic-week1.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Turn cold leads into real commissions.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

Real estate agents don’t lose deals due to lack of leads — they lose them due to poor timing and inconsistent follow-ups.

High-intent buyers often go cold because agents fail to respond at the right moment or forget to follow up after key actions like site visits or price discussions. These missed interactions result in significant revenue leakage, often worth lakhs in lost commissions.

Existing tools focus on lead management, not revenue recovery.

This project solves that by identifying stalled conversations, quantifying the revenue at risk, and automatically re-engaging leads with context-aware AI follow-ups — ensuring that potential deals are actively recovered instead of silently lost.

**Challenges we ran into**

One of the main challenges was shifting the system from a traditional lead management mindset to a revenue-focused recovery engine.

Instead of just tracking leads, I needed to design a system that could:
- Identify when a conversation is “cooling off”
- Infer buyer intent from partial chat context
- Estimate potential deal value and prioritize accordingly

Another challenge was designing a clear and intuitive user experience. The goal was to ensure that within seconds, a user (or judge) can understand where revenue is at risk and what action should be taken.

Balancing AI intelligence with simplicity was also critical — making sure the system feels smart without becoming complex or overwhelming.

Finally, creating a realistic demo environment (with seeded data, chat flows, and recovery moments) was essential to effectively communicate the product’s value in a short time.

Pranav Ghuge

`2026-04-15`

---

### VERDANTIX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/verdantix-5b83) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Aayush9-spec/Verdantix) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://verdantix-ebon.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tRT_y7rDMXc) [![Built at](https://img.shields.io/badge/Built%20at-Off--Grid-0052CC?style=flat-square)](https://offgrid.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> EARN FROM EVERY GREEN MOVE

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Kaggle](https://img.shields.io/badge/Kaggle-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Farmers lack access to simple tools to **understand their carbon impact**, as existing systems are complex and not designed for small-scale use. This is especially challenging in rural areas with poor internet connectivity.

Verdantix solves this by providing AI-powered carbon score predictions, actionable recommendations, and a multilingual assistant. It also works offline, storing data locally and syncing automatically when connectivity returns.

This makes sustainable farming easier, more accessible, and data-driven, helping farmers improve practices and potentially benefit from carbon credits without needing advanced technical knowledge.

**Challenges we ran into**

A key challenge was handling offline functionality. When users were offline, API requests failed and data was lost.

I solved this by implementing a localStorage-based queue system, storing inputs locally and syncing them via a /sync API once connectivity returned.

Another challenge was the lack of real carbon datasets, which I addressed by using a Kaggle dataset and engineering a realistic carbon scoring model.

**Winners**

Verdantix fits into AgriTech, Climate Tech, and Rural Innovation by using AI to help farmers make smarter, sustainable decisions. It works even in low-connectivity areas and translates complex carbon data into simple, actionable insights for real-world use.

Team **CoderX** -- [amitesh kumar shukla](https://github.com/amiteshkrshukla), [Arpit Tiwari](https://github.com/arpitjr7-hub), [Aayush Singh](https://github.com/Aayush9-spec)

`2026-04-11`

---

### SolarAnalysis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/solaranalysis-41c5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Divyapriya382006/SolarAnalysis-Devshouse.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/dViISvEozNE?si=ysUMESEugUD3Pb4Z) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> "Turn Your Rooftop into a Smart Energy Source”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Many people want to install solar panels but don’t know where to start. They struggle to understand how much energy they will generate, how much money they will save, and whether their roof is even suitable. Existing solutions are either too complex, require manual input, or don’t provide real-time, personalized insights.

Our project solves this by providing a simple, interactive platform that helps users plan solar installation easily. It uses simulation and smart analysis to show energy output, cost savings, and optimal panel placement based on location and conditions.

This makes solar planning:

Faster –>no need for manual calculations
Easier – >visual and user-friendly interface
More accurate –> data-driven predictions
More accessible –> anyone can use it without technical knowledge

Ultimately, it helps users make better and more confident decisions about switching to solar energy.

**Challenges we ran into**

One of the main challenges we faced was integrating multiple features like maps, simulation, and real-time updates into a smooth and responsive interface. Since different components depended on each other (like location data affecting energy prediction), managing state and ensuring everything updated correctly was initially difficult.

We also faced issues with development environment differences. For example, some commands and configurations behaved differently in PowerShell compared to standard terminal environments, which caused errors during setup.

Another challenge was handling realistic data. Since we did not rely fully on external APIs, we had to simulate weather conditions and energy calculations in a way that still felt accurate and meaningful.

To overcome these challenges:

We structured the project into modular components to manage complexity
Used TypeScript to reduce bugs and improve code reliability
Debugged environment issues step-by-step and adapted commands accordingly
Designed fallback logic and simulations to ensure smooth functionality even without real APIs

These challenges helped us improve both the technical robustness and usability of the project.

**Environmental Sustainability**

Our project directly contributes to environmental sustainability by making solar energy adoption easier, more accessible, and more efficient. Many people hesitate to switch to solar due to lack of clarity around energy output, cost savings, and feasibility.

By providing a platform that simulates solar energy generation, predicts efficiency based on location and conditions, and visualizes optimal panel placement, we help users make informed decisions about adopting renewable energy.

This reduces dependency on non-renewable energy sources and encourages the use of clean energy. By simplifying the transition to solar power, our solution supports lower carbon emissions and promotes a more sustainable and eco-friendly future.

Team **MARGHERITA** -- [Kushagra Kalra](https://github.com/kushxgr), [Giridharan RE](https://github.com/dharanre/-Blockchain-Explorer), [Aanya Malhotra](https://github.com/aanyamalhotra2024-source), [Divya Priya RK](https://github.com/divyapriya382006/)

`2026-03-29`

---

### WasteIQ - Predictive Waste Intelligence Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wasteiq-predictive-waste-intelligence-platform-9920) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DotSlash-9-0/Team-Vertex) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a84IsBTLPs8) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Waste intelligence for sustainable cities

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

# ♻️ WasteIQ  
**Smart Waste Intelligence & Diversion Platform**

WasteIQ is a data-driven platform designed to transform how waste is predicted, collected, and utilized. It bridges critical gaps in municipal waste management by combining predictive analytics, real-time matching, and inclusive data collection.

---

## 🚀 Problem Statement

Current waste management systems are largely **reactive**, **inefficient**, and **data-blind** in key areas:

- Overflow issues are addressed only after complaints  
- Usable waste ends up in landfills due to missed timing  
- Informal workers contribute massively but remain invisible in data systems  

---

## 💡 Our Solution

WasteIQ tackles these challenges through three core innovations:

---

### 📊 1. Collection Intelligence Engine  
**Problem:** No system predicts waste surges in advance  

**Solution:**  
We use predictive analytics to forecast waste spikes **24–72 hours in advance** by correlating:

- Festival calendars  
- Weather forecasts  
- Market schedules  
- Construction permits  

**Outcome:**  
- Proactive waste collection  
- Reduced overflow incidents  
- Optimized resource allocation  

---

### 🔄 2. Surplus Diversion Matching Engine  
**Problem:** Usable waste reaches landfills due to missed connections  

**Solution:**  
A **time-constrained matching system** connects waste generators with receivers such as:

- NGOs  
- Biogas plants  
- Recycling units  
- Animal farms  

**Outcome:**  
- Maximum utilization of waste  
- Reduced landfill dependency  
- Circular economy enablement  

---

### 📱 3. Informal Sector Integration  
**Problem:** Informal waste workers generate no structured data  

**Solution:**  
We design for real-world constraints:

- Offline-first mobile logging  
- Works on low-end Android devices  
- Opportunistic data sync  

**Outcome:**  
- Inclusion of informal sector in data ecosystem  
- Better decision-making with real ground data  
- Empowerment of waste workers

**Challenges we ran into**

## ⚠️ Challenges I Ran Into

Building WasteIQ involved solving multiple real-world and technical challenges:

---

### 🔌 1. Handling Low Connectivity (Offline-First Design)

**Challenge:**  
Many waste workers operate in areas with poor or no internet connectivity, making real-time data syncing unreliable.

**Solution:**  
We implemented an **offline-first architecture** using IndexedDB in a PWA. Data is stored locally and synced automatically when even minimal connectivity (e.g., 2G) is available. This ensured uninterrupted data collection in all environments.

---

### 📊 2. Accurate Waste Prediction Without Sensors

**Challenge:**  
Most existing systems rely on IoT sensors, but our goal was a **hardware-free solution**.

**Solution:**  
We used **time-series forecasting (Prophet)** combined with **XGBoost** and external signals like weather and events. This allowed us to predict waste surges without deploying any physical infrastructure.

---

### 🚛 3. Dynamic Route Optimization

**Challenge:**  
Traditional waste collection uses fixed routes, but we needed dynamic routing based on predicted demand.

**Solution:**  
We implemented a **Vehicle Routing Problem (VRP)** solver using OR-Tools to optimize routes in real time, prioritizing high-waste zones and improving efficiency.

---

### 🔄 4. Real-Time Matching for Surplus Waste

**Challenge:**  
Surplus resources (like food) have a **very limited usability window**, making matching time-critical.

**Solution:**  
We designed a **constraint-based matching engine** that filters receivers based on type, distance, and capacity, and sends instant alerts via SMS and push notifications.

---

### 👥 5. Integrating the Informal Sector

**Challenge:**  
A large portion of recycling is handled by informal workers who are not part of any digital system.

**Solution:**  
We built a **simple, low-barrier interface** that works on basic smartphones, requires minimal input, and supports offline usage, ensuring inclusivity and better data coverage.

---

### 🚀 Conclusion

These challenges pushed us to design a system that is not only technically robust but also practical, scalable, and usable in real-world conditions.

**GreenTech**

## 🌱 How WasteIQ Fits the GreenTech Track

WasteIQ is a predictive waste intelligence platform designed to improve sustainability, optimize resource usage, and reduce environmental impact using a **software-only approach**.

---

### ♻️ 1. Predictive Waste Management

WasteIQ uses data sources such as:
- Weather forecasts  
- Festival and event calendars  
- Historical waste generation data  

to **predict waste surges 24–72 hours in advance**.

This enables:
- Proactive waste collection  
- Reduced bin overflows  
- Optimized truck routes  
- Lower fuel consumption and emissions  

---

### 🔄 2. Surplus Diversion & Circular Economy

WasteIQ introduces a **real-time matching system** that connects:
- Waste generators (restaurants, markets, factories)  
- Waste receivers (NGOs, recyclers, biogas plants)  

This ensures:
- Food and recyclable materials are utilized before expiry  
- Reduced landfill dependency  
- Promotion of a circular economy  

---

### 📱 3. Inclusion of Informal Waste Sector

The platform includes an **offline-first mobile system** for informal workers:
- Works on low-end Android devices  
- Stores data offline and syncs when connectivity is available  
- Captures previously untracked recycling activity  

This improves:
- Data completeness  
- Recycling efficiency  
- Social and economic inclusion  

---

### ⚙️ 4. Software-Only, Scalable Solution

WasteIQ:
- Requires **no IoT sensors or additional hardware**  
- Works with existing infrastructure  
- Is scalable across cities and rural areas  
- Functions even in low-connectivity environments  

---

### 🌍 5. Environmental Impact

With WasteIQ:
- Waste overflow is predicted instead of reacted to  
- Fuel usage and emissions are reduced  
- Recyclables and surplus materials are efficiently utilized  
- Sustainability metrics and accountability are improved  

---

### 🚀 Conclusion

WasteIQ transforms waste into actionable intelligence, enabling smarter decisions, reducing environmental impact, and building a more sustainable and efficient waste management ecosystem.

Team **Team Vertex** -- [Kunj vaghani](https://github.com/kunjvaghani), [Vansh Patel](https://github.com/VanshPatel2010), [Mit Keraliya](https://github.com/keraliya07), [Neel Patel](https://github.com/Neel-001)

`2026-03-22`

---

### FlyWaySafe
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/flywaysafe-5f72) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DotSlash-9-0/Medhavi) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uBWCBxJERNo?si=oCcUVeGQwRk2-hia) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart Wind Turbine for Bird Migration Safety

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

We're trying to maximise the efficiency of wind turbines along with trying to save lives of migratory birds. Both of these problem are closely linked as Wind turbine plants loose around $200-250 million in revenue due to being hauted to allow the safe movement of migratory birds. Annually 400-600k birds die because of colliding with these wind turbines. We aim to solve both these problems.

**Challenges we ran into**

Challenges Faced 
Dataset Integration: Combined three datasets into a single, consistent training set.
Class Imbalance: Handled uneven class distribution to avoid biased predictions.
Data Engineering: Performed preprocessing and feature engineering to improve model performance.

**GreenTech**

There are 2 types of things which comply with the PS
1) Energy Production increase as less time for shut down.
2) Community is now able to use more green energy.

Team **Medhavi** -- [Vatsal Bateriwala](https://github.com/Vatsal565), [Deep Das](https://github.com/THE-DEEPDAS), [Sneha kumari](https://github.com/Sneha25-bit), [Vikram Singh](https://github.com/VikramSingh138)

`2026-03-22`

---

### EcoGo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecogo-1736) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Nishanth773/EcoGo) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nishanth773.github.io/login) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Sustainability in Logistics

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The logistics sector contributes significantly to CO₂ emissions and fuel consumption due to inefficient route planning, traffic congestion, poor road conditions, and unnecessary engine idling

Existing solutions like Google Maps provide eco-routing, but they are primarily designed for individual users and do not consider logistics-specific challenges such as truck load, driver behavior, idle fuel wastage, and road conditions like potholes

Our solution EcoGo, addresses these issues by providing an AI-powered eco-routing system tailored for logistics fleets. It analyzes real-time traffic, weather, road conditions, and vehicle data to recommend the most fuel-efficient routes instead of just the shortest or fastest ones

Additionally, it promotes sustainable driving through driver behavior tracking, idle detection, and a gamification system that rewards eco-friendly driving, ultimately reducing fuel consumption, operational costs, and environmental impact

**Challenges we ran into**

One of the major challenges we faced was integrating map functionality into our application. Embedding and customizing map services for route optimization required handling APIs and ensuring proper configuration, which initially led to errors like 404 issues during deployment.

Another challenge was accessing real-time data such as traffic, fuel consumption, and road conditions. Since we did not have access to real fleet data, we had to simulate data for our prototype.

To overcome these challenges, we used available APIs, simplified our routing logic for the prototype, and focused on building a working model that demonstrates the concept effectively.

Team **Code Crafters** -- [Nishanth P](https://github.com/Dnj), [Akshaya Saravanan](https://github.com/Akshaya-csbs), [Roshan Ganesh M](https://github.com/ROSHAN-456), [Merwin O](https://github.com/merwin27)

`2026-03-17`

---

### NeuroRoute
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/neuroroute-da0e) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://neuroroute-03-k74k-kradftmjq-jeevitha3shetty-9221s-projects.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Optimize Intelligence, Minimize Waste

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves :**

Today, most AI systems follow a “one-size-fits-all” approach — every query, whether simple or complex, is processed by large, resource-heavy models.

This leads to several **critical issues:**

**Unnecessary Energy Consumption**
Simple queries like “summarize this paragraph” still trigger powerful models, wasting computational resources.

**High Carbon & Water Footprint**
Large-scale AI inference consumes significant electricity and water for cooling, contributing to environmental impact.

**Increased Latency**
Users experience slower responses because heavy models are used even when not needed.

**Inefficient Resource Utilization**
Systems fail to optimally use available CPU/GPU resources, leading to poor cost-performance balance.

**Lack of Transparency**
Users have no visibility into how much energy their queries consume or what impact they create.

**No Data for Optimization**
Current systems don’t systematically log usage patterns to improve efficiency or train better routing strategies.

**What People Can Use It For?**

NeuroRoute transforms how users interact with AI by making it intelligent, efficient, and sustainable.

**Everyday Use Cases**

**Instant Summarization**
Quickly summarize articles, PDFs, or selected text directly from any webpage. No page switching required .

**Smart Q&A and Explanations**
Get answers or simplified explanations without overloading heavy AI models unnecessarily.

**Context-Aware Research**
Analyze selected content and generate insights tailored to the complexity of the query.

**Content Simplification**
Convert complex information into easy-to-understand language instantly.

How It Makes Tasks Easier, Faster, and Safer

**Dynamic Model Routing**
Automatically selects the most efficient AI model based on query complexity (LOW → small model, HIGH → large model).

**Faster Response Times**
Lightweight queries are handled by smaller models, reducing latency significantly.

**Green AI Optimization**
Tracks and minimizes energy, carbon, and water usage, promoting sustainable AI usage.

**CPU → GPU Escalation (Smart Compute Shift)**
Only uses GPU-heavy computation when necessary, ensuring optimal hardware utilization.

**Plug-and-Play Architecture**
New models can be added easily without modifying core system logic which boosts the economy of the company.

**Dataset Generation for Research**
Logs anonymized query data, enabling future improvements in AI efficiency and routing strategies.

**Privacy-Conscious Design**
Stores only necessary metadata (not sensitive user data), ensuring safer usage.

**Works Anywhere (Browser Extension)**
Seamlessly integrates into any webpage — no need to switch apps or workflows.

**Why It Matters ?**

NeuroRoute shifts AI from being power-hungry and inefficient to smart, adaptive, and environmentally responsible — making advanced AI accessible while reducing its global impact.

**Challenges we ran into**

One of the biggest challenges we faced was ensuring reliable **real-time routing** of AI queries through our middleware layer. Initially, incoming requests were not being properly captured due to mismatches between expected and actual API request patterns. This made it difficult to verify whether the system was functioning correctly. We resolved this by **analyzing live network traffic** using browser developer tools, identifying the exact request structures, and refining our routing conditions to ensure accurate interception and forwarding.

Another key challenge was establishing **stable communication between the browser extension and the middleware server**. We encountered issues related to **permissions and cross-origin restrictions**, which prevented requests from reaching the backend. This was addressed by configuring the correct access permissions and request headers, enabling seamless and secure interaction between the frontend and backend components.

We also faced difficulties in debugging and validating the routing pipeline, since the system operates across multiple layers. To overcome this, we built dedicated monitoring endpoints such as /neuroroute/queries and /neuroroute/stats that log every request, including the selected model and performance metrics. This provided clear visibility into the system’s behavior and helped us ensure that routing decisions were accurate and consistent.

Finally, designing an effective dynamic model selection strategy was challenging. We needed to **balance performance, cost, and efficiency** while handling queries of varying complexity. Through iterative testing and refinement, we developed a reliable classification and routing mechanism that consistently maps queries to the most appropriate model, resulting in an optimized and scalable system.

**Creative Use of Requestly**

We used **Requestly **in a highly unconventional and impactful way by transforming it from a simple API redirection tool into a **real-time AI routing layer**. Instead of modifying applications or integrating SDKs, we leveraged Requestly to intercept outgoing AI requests and **dynamically reroute** them through our NeuroRoute middleware. This allowed us to introduce an **intelligent decision-making layer** into existing systems without requiring any changes to their code, effectively turning Requestly into a zero-code AI infrastructure enabler.

This approach is powerful because it removes the biggest barrier in AI optimization- integration complexity. Any application making AI calls can instantly benefit from our system. Once intercepted, each query is analyzed based on its complexity and routed to the most efficient model, ensuring that simple queries do not consume expensive or energy-intensive resources. This **transforms static AI usage into a dynamic**, optimized pipeline that improves both performance and cost efficiency.

What makes our implementation especially unique is its focus on sustainability. By routing queries intelligently, we reduce unnecessary compute usage and actively track environmental metrics such as energy consumption, carbon emissions, and water usage. In our testing, we successfully routed **100+** queries across multiple models while continuously monitoring their environmental impact. This demonstrates how Requestly can act not just as a network tool, but as a gateway for enabling greener AI systems.

Overall, we reimagined Requestly as a foundational layer in an AI architecture - one that enables real-time optimization, sustainability, and universal compatibility. This approach has the potential to evolve into a platform-level solution where any AI-powered application can become smarter, more efficient, and environmentally responsible without requiring redevelopment.

Team **CodeWin** -- [Neha Reddy](https://github.com/Neha20-git), [Jeevitha Shetty](https://github.com/JeevithasHetty), [Srividisha MS](https://github.com/Vidishams), [Jeevitha R](https://github.com/JeevithaR3)

`2026-03-18`

---

### Heart Guard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/heart-guard-ai-4305) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Skyhitman/project-1-----) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHDci8ruAM/upR93WLeToby806EvJTS7w/view?utm_content=DAHDci8ruAM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h683aaf9c0d) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/8608f654acd24d2fae3153ed4547ce2d) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Every heart deserves a second chance

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square)

**The problem it solves**

The project addresses the critical challenge of early and accurate detection of Myocardial Infarction (MI) using real-time ECG signal analysis, as delayed diagnosis of heart attacks remains a leading cause of preventable deaths globally. Traditional ECG interpretation requires trained cardiologists and hospital infrastructure, making it inaccessible in remote areas or emergency situations outside clinical settings. This project aims to build a portable, low-cost IoT-based system using an ESP32 microcontroller paired with an AD8232 ECG sensor that continuously monitors a patient's heart activity and streams the data wirelessly to a machine learning backend. The backend employs an ensemble of three deep learning models that collectively analyze the ECG signal and predict the likelihood of MI in real time, with the results displayed on a web interface for immediate visibility. The core challenge being solved is bridging the gap between raw biosignal acquisition from affordable hardware and reliable clinical-grade MI detection, enabling faster intervention in time-critical cardiac events outside of hospital environments.

**Challenges we ran into**

One of the most frustrating challenges encountered during this project was the ESP32 consistently producing a false positive MI detection on a completely healthy patient, with the ensemble model confidently outputting 86.3% probability despite the subject having no cardiac condition. After extensive debugging, the root cause was traced to the AD8232 ECG sensor operating at too high a gain, causing the R-peaks in the QRS complex to clip at the ADC's maximum value of 4095 repeatedly. This clipped flat-top waveform closely resembles an ST-segment elevation pattern in ECG morphology, which is one of the primary indicators of MI that the models were trained to detect from the PhysioNet dataset. Compounding this was an irregular sampling rate issue where multiple samples were being logged with identical timestamps due to the WebSocket transmission batching on the ESP32, meaning the signal reaching the model was unevenly spaced rather than the consistent 360Hz the models expected. To diagnose this, a session recording feature was built directly into the backend that captured and saved the raw live ESP32 data as JSON, which was then visualized and analyzed to reveal the clipping and baseline drift problems clearly. The fix involved adjusting the electrode placement to standard Lead I configuration, tuning the AD8232 gain, adding a bandpass filter between 0.5–40Hz in the firmware, and fixing the timestamp logging to ensure uniform sampling before the signal reaches the inference pipeline.

Team **TEAM SOLVIX** -- [Saurav Karunakaran](https://github.com/Skyhitman), [Santhoshkumar R](https://github.com/santhoshkumar1009), Vishwanathan S, [Shreethrudhi B](https://github.com/shreethurdhi)

`2026-03-17`

---

### CreatorInsight
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/creatorinsight-8290) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sahilalamshaikh/CreatorInsight-Syntax-Erroz-) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://presenti.ai/app/share/CAE.IAEqEH7yotn_X4r02FgflKvmKukwAUABSgoxNzczNzU3ODY4?invite_code=ZHAs0cZ9%EF%BC%8C) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XWRwB-f6WFU) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart recommendations for creators

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![fast.ai](https://img.shields.io/badge/fast.ai-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

The main objective of our project is to develop a centralized analytics platform that combines data from multiple social media platforms and presents it in a single dashboard.

The system aims to help creators:

Monitor their follower growth and engagement trends

Analyze the performance of their posts

Understand audience demographics and behavior

Receive intelligent insights about their content performance

By providing all analytics in one place, CreatorInsight helps creators save time and gain a clearer understanding of their overall social media presence.

To address the problem, we developed CreatorInsight, a platform that collects and analyzes social media data and presents it through an interactive dashboard.

The system aggregates information such as post metrics, engagement rates, reach, impressions, and follower growth. Using these metrics, the platform generates insights that help creators understand how their content performs across different platforms.

One important feature of CreatorInsight is its AI-based analysis system, which evaluates the performance of posts and identifies patterns in engagement. This allows creators to recognize which content is performing well and what type of content resonates most with their audience.

The platform also generates alerts for important events, such as when a post becomes viral or when engagement increases significantly.

**Challenges we ran into**

Obstacles Faced During the Project
1. Integrating Data from Multiple Platforms

One of the major challenges was designing a system that can handle data from multiple social media platforms. Each platform provides analytics in different formats, so we had to create a unified data structure to store and process this information.

2. Designing the Database Structure

Another challenge was designing the database schema to efficiently store analytics data such as posts, metrics, alerts, milestones, and brand deals. We needed a well-structured database to ensure the system could handle large amounts of analytics data.

3. Handling Real-Time Analytics

Displaying live updates for post engagement and analytics required implementing real-time communication between the backend and frontend. Ensuring smooth data updates without performance issues was a technical challenge.

4. Authentication and Security

Implementing secure user authentication using JWT tokens was another obstacle. We had to ensure that only authorized users could access their analytics dashboards and data.

5. Creating Realistic Data for Testing

Since we were not directly connected to real social media APIs, we had to generate realistic analytics data for testing and demonstrating the system. Designing a seed script that simulates real creator analytics was a challenge.

6. UI and Data Visualization

Designing a dashboard that clearly presents complex analytics data in an easy-to-understand way was also difficult. We had to carefully structure charts, tables, and metrics so users could quickly understand their performance.

Team **Syntax Erroz** -- Sahil Sahikh, Prikshit Kaswan, Chris Juvin, Vignesh Swain

`2026-03-17`

---

### Stellar_Sync
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stellarsync-7957) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/codehubasa/Stellar_Sync) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/VS3HVBvq5Xk) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/VS3HVBvq5Xk) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co)

> AI-Driven Signal Recovery for Deep-Space Telemetry

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **OJAMAJO DOREMIS** -- [Asmita Banerjee](https://github.com/codehubasa), [Isha Chakraborty](https://github.com/isha09-code)

`2026-09-12`

---

### FairShake
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fairshake-c97c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tamizholiyan/FairShake.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/_ZsC0ScyTQ8?si=Mq7SzZGKLMihXAxu) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Secure escrow for gig-economy payments.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

India’s freelance economy runs on trust nobody can verify.No safety net in India’s freelance sector. Freelancers risk non-payment after delivering; clients risk ghosting or poor quality after paying an advance.Upwork and UrbanCompany offer protection, but charge 20–30% commission and lock users into rigid workflows.Most deals happen informally over WhatsApp and UPI. UPI is instant, but once money is sent, it’s gone — no way to verify delivery.

Our solution:
No marketplace, no rigid workflow.Fairshake is a bilateral escrow platform that secures funds directly between a Client and a Service Provider.Funds move only on delivery. The Client locks funds before work begins; they’re released only once work is submitted and verified against agreed milestones.Disagreements go to review, not auto-refund. If either side disagrees, the deal moves into review — neither side has unilateral control over the outcome

**Challenges we ran into**

It was very hard to deal with all the different logics and keeping them from breaking each other.

Team **Ragnarok** -- Tamizholiyan R K, Yadhavi K, Sadhana G, Thejas R

`2026-09-02`

---

### Found@VIT
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/foundvit-24de) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gurucharan-a/Found-VIT.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MuH78pcKx6s?si=hEtZpsborrqKn4ha) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Lost something in VIT? Find it in seconds.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**Challenges we ran into**

We originally used Gemini Vision as our AI but we found that it had a low rate limit and was incredibly inaccurate at identifying features from images. So, instead we used Qwen via Groq which gave much higher accuracy and reliable results.

**The problem it solves**

Our web app solves the problem of existing lost & found platforms for VIT being too  cluttered in the form of WhatsApp groups, as these groups have a member limit, get overrun with messages, and new members cannot see old messages. Found@VIT is the solution for that - a hyperlocal web app that allows lost & found items on the VIT Chennai campus to be viewed in the form of posts, similar to social media platforms. Using AI categorization and moderation, it ensures that the app remains a safe and relevant community for finding and relinquishing lost items. An easy tag-based search system allows for easy identification of lost objects.

Team **Thunderbolts** -- Harshith Venkataraman, GuruCharan A, Sivanee R, Rishwanth Kumar Senthil Kumar, Sahana Balaji

`2026-09-02`

---

### AgriSentinel
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agrisentinel-b6f8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AgriEssentials/agrisentinel-v1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://agrisent.onrender.com) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> We Build the Future of Indian Agriculture

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Jinja2](https://img.shields.io/badge/Jinja2-333333?style=flat-square)

**Challenges we ran into**

MQTT was not set up in the backend
As a result, the .env file had an empty MQTT_HOST
and
the backend was not able to establish any connection to HiveMQ,
which resulted in the console showing MQTT: NOT CONFIGURED.
The backend and the ESP32 listened to different MQTT topics.
The web console sent messages to agri/pump/control topic, while the ESP32 subscribed to agri/pump/mix. Therefore, the ESP32 did not receive any commands to start the pump.
It is similar to when someone calls from Room A, while you are waiting for the call in Room B.
The ESP32 firmware was controlling a wrong type of motor driver.
The pumps require an H-bridge (L298N chip), which requires two complementary IN pins for each motor/pump (active-HIGH control). However, the firmware was using a simple relay driver, which utilizes one active-LOW GPIO pin for controlling the motor. Therefore, even if MQTT communication was fixed, the ESP32 would still not be able to turn on the pump due to incorrect electrical control signal.

**The problem it solves**

The product AGRI-SENTINEL turns precision-farming technology into something that a small-time farmer can employ, without the requirement of an agronomy degree, or even complicated apps that may be unfamiliar to users.
Problems addressed by the product:
Crop disease loss due to lack of surveillance and proper medication
Changes in soil pH and moisture that are not monitored or acted upon in a timely manner
Inappropriate or excessive use of chemical fertilizers and pesticides
Disease recognition and appropriate medication requires expertise and time, while incorrect medication poses health risks, especially when done manually, without proper equipment. Additionally, chemical dosing is difficult to measure, and is a hazardous task when done incorrectly.
How does the product solve these problems?

AI-Based Leaf Diagnosis: diagnosis of leaf diseases, pathogens, and severity percentage (0%-100%). Customized chemical treatment recipes can be made based on the diagnosis, removing the need for an agronomist's help
ESP32-S2 pH and Moisture Sensor: allows for automated irrigation and fertilization, which cuts down on resource waste and removes the need for repeated field visits
Automated Mixing and Spraying System (Using L298N Motor Driver): allows for automated and accurate mixing of chemicals according to the recipe, which means that the user is not exposed to the harmful effects of the chemicals, and also provides accurate dosing, removing the need for hazardous manual dosing
Satellite Monitoring of Field Polygons: allows the uploading of field polygons to the system, which allows for vegetation and NDVI analysis, providing insight into the whole field's status at a glance
Weather and Market Info, Voice Assistant: provides weather and market info in local languages, along with a voice assistant (Sarvam AI) for ease of use.

**Hardware**

Custom embedded control system . the project involves implementing real-time control logic on an ESP32 (WiFi + MQTT + state machine) that drives physical actuators through an L298N driver . A textbook embedded systems task focused on the implementation of control logic over GPIOs and the physical layer (driver communication, timing-sensitive dosing algorithms), as opposed to simulation.
Sensor integration . the use of an ESP32-S2 development board for implementing the core logic that interprets the analog and digital signals from sensors is another strength in terms of hardware-related competencies. Interfacing with real-world sensors and condition hardware-specific signals (pH, ground humidity) is a fundamental skill in embedded systems development.
Actuation and control  the implementation of the mixing/spraying system is a strong example of a “hardware track” competency in the mix of automation and control. It demonstrates the ability to implement a closed-loop control system that takes an action (mixing ratios, spraying) based on a condition (AI diagnosis result). The project involves developing the control logic for the mixing ratios (time-dependent actuation), multiplexer-controlled motor drivers, and a relay control circuit for the spraying system. In a hardware-focused challenge, such “sense-decide-act” pipelines are common, and one’s ability to demonstrate proficiency in building them is a strong point.
Systems-level hardware expertise — working with cloud/AI-based systems (leaf diagnosis, satellite NDVI visualization) presents an interesting systems-level challenge in terms of bringing these high-level systems down to the hardware layer through a series of communications (MQTT). Power delivery (ground references), power stability (brownout protection), and timing are all critical in such systems, and the fact that the project requires the implementation of these lower-level system hardware features is a strong validation of systems-level experience.

Team **AgriEssentials** -- [Ibhan Mukherjee](https://github.com/ivanho-git), Ramya CM, Rahul M, Anusha Vinod, KIRTHIK SUDHARSAN

`2026-09-02`

---

### Spidersense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/spidersense-9d97) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gnanaharoid/HackVerse) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> One wristband, one second ahead

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Embedded C](https://img.shields.io/badge/Embedded%20C-333333?style=flat-square) ![HTML/CSS](https://img.shields.io/badge/HTML/CSS-333333?style=flat-square)

**The problem it solves**

SPIDER-SENSE is a smart safety wristband that predicts and detects potential emergencies using physiological, motion and environmental data then automatically alerts the responsible person and stores the event for timely intervention.

**Challenges we ran into**

Integrating hardware and software, converting our prototype into actual real world product

**Hardware**

We have made the prototype of the spidersense which is a wristband which solely takes inputs on hardware components

Team **Cybersync** -- Srinitha S, Gnana Harish, Mithun Shanker, Suhael FK, Bhagyasri B

`2026-09-02`

---

### Career spider sense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/career-spider-sense-d70a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sachin-b487/Career_Spider_Sense_Final) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://career-spider-sense-final.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ftOmcCilorU) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> “Know Your Gap. Choose Your Path. Become Job-Ready

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![NLP](https://img.shields.io/badge/NLP-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Students often don't know what skills their target job requires, which skills they already have, what skills they are missing, or what they should learn first.

This leads to career confusion, random course selection, unnecessary certifications, and unclear career planning.

Our solution identifies the gap between a student's current skills and their target job requirements, then provides a clear, priority-based roadmap to become job-ready.

**Challenges we ran into**

Challenges We Ran Into

- Resume data extraction: Converting different resume formats into structured skills and information was challenging.
- Skill matching: Mapping a student's existing skills accurately against the requirements of a target job was not straightforward.
- Skill prioritization: Deciding which missing skill the student should learn first required considering importance, proficiency, and dependencies.
- AI accuracy: Making sure the AI-generated recommendations were relevant and not generic was challenging.
- Time constraints: Building and integrating multiple features within the hackathon's limited time was a major challenge.
- Integration & debugging: Connecting the frontend, backend, AI analysis, and database while keeping the application stable required continuous testing.
- Readiness scoring: Designing a meaningful and explainable score instead of an arbitrary percentage was another challenge.

Team **Micro Titans** -- Lokeshkumar Balamurugan, Rudhraa V, Advaith Kirankumar, Nishanth Kumar, Sachin B

`2026-09-02`

---

### Nirvana
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nirvana-73eb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jaaiwanth/Nirvana) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nirvanaai-coral.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/kLJi83ej1CY) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> “From Distress to Dispatch, in Seconds.”

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

One of our biggest challenges was orchestrating multiple AI agents while validating their outputs against live geospatial and rescue-resource data. The Incident Analysis Agent generates structured emergency information, but this information then had to flow correctly through H3/Haversine filtering, live resource availability, OSRM routing, and finally the Decision Agent. We encountered cases where AI-generated information did not completely align with the available live dataset, resulting in invalid resource matches or inconsistent dispatch decisions.

To solve this, we introduced an additional AI Validation Agent between the Incident Analysis Agent and the resource-selection pipeline. This agent cross-checks the extracted incident details against the available resource capabilities, location data, and routing information, identifies inconsistencies, and refines the incident state before it reaches the Decision Agent. We also added strict Zod schema validation to ensure the AI outputs remain structured and predictable. This created a more reliable multi-agent pipeline where each agent has a specific responsibility and the final dispatch decision is grounded in validated, real-world resource and routing data.

**The problem it solves**

During disasters and emergencies, critical information is often unstructured, incomplete, and constantly changing, while rescue resources are distributed across different locations. Emergency coordinators must manually interpret distress reports, identify suitable teams, check availability, calculate realistic routes, and decide what resources to dispatch—creating delays and increasing the risk of sending the wrong team or route.

NIRVANA automates this entire coordination process. Its multimodal AI intake can understand text, audio, and images, fusing information such as victim counts, injuries, hazards, and infrastructure damage into a structured emergency incident. Our Incident Analysis Agent then extracts and validates the incident details, while the Decision Agent evaluates rescue-team capabilities, specialization, and real road ETA to select the optimal primary and secondary responders. H3 and Haversine provide rapid spatial filtering, OSRM calculates actual road-network routes, and SSE provides live dispatch and vehicle telemetry to the command dashboard. A deterministic fallback engine ensures the critical workflow can continue even when AI inference fails.

We have also tested the system against live/current routing and emergency-response scenarios, validating the end-to-end flow from incident intake through resource selection, routing, dispatch, and live tracking. The project includes standardized disaster scenarios and benchmark tooling for latency and throughput testing.

Ultimately, NIRVANA makes emergency response faster, safer, and more coordinated by turning fragmented multimodal distress information into an actionable rescue decision—helping responders understand faster, decide smarter, and rescue sooner.

Team **Duck Squad** -- [Hari Aswath](https://github.com/HariAswath), [SaiAmirthesh Muthukumar](https://github.com/SaiAmirthesh), [JAAIWANTH K](https://github.com/Jaaiwanth)

`2026-09-02`

---

### SmartWasteGrid
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartwastegrid-6ef4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/varunns2007/SmartWasteGrid) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/s3H5m-dP6ss?si=-FqwWd0coRcj0G7S) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> AI-Powered Closed-Loop Waste Intelligence

![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Convolutional neural network (CNN)](https://img.shields.io/badge/Convolutional%20neural%20network%20(CNN)-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square)

**Challenges we ran into**

Our first version of this system used YOLOv11 for per-object detection and classification directly on the conveyor — identifying and classifying each individual piece of waste as it moved past the camera.

During review, we got direct, specific pushback: real municipal waste doesn't arrive as neatly spaced, distinguishable objects. It's bulk-poured and overlapping, and factors like occlusion, motion blur, and wet waste visually staining or coating nearby plastics all degrade per-object detection accuracy in ways that don't show up in a clean demo dataset. In other words, our model looked great on curated test footage but wouldn't hold up against a real conveyor's actual mess.

How we resolved it: we reframed the vision layer's job from "detect and classify every individual object" to "estimate the overall composition of a batch," combining camera output with other sensor signals (load cell, and conceptually NIR/metal detection for material identification) instead of relying on vision alone. This was both a more honest claim about what the CV model can actually deliver at bulk-waste scale, and a better architectural fit — our downstream routing decisions only ever needed whole-batch composition, not item-level identity, so we were solving a harder problem than the system actually required.

What people can use it for

Facility operators (compost yards, biomethanation plants, MRFs)

See real-time composition of incoming batches instead of discovering what arrived only after it's dumped — lets them plan processing capacity for the day instead of reacting to it.
Get a live feed showing when a nearby ULB has overflow they could absorb, turning idle capacity into utilized capacity without manual coordination calls.
Generate an auditor-ready record of exactly how much waste they diverted from landfill and processed, usable to actually apply for carbon-credit revenue — something most plants currently have no reliable paper trail to support.

Municipal commissioners / ULB officials

View a ward-level segregation compliance heatmap instead of relying on spot checks — makes it easy to see which wards or collection routes consistently send contaminated batches, so enforcement or education can be targeted instead of citywide and blanket.
Track a district-level diversion rate over time as a concrete, defensible sustainability metric for reporting up to the state, instead of an estimate.

State-level planners (CMA / Tamil Nadu Urban Infrastructure)

Get cross-ULB visibility into which treatment plants are underused and which are overloaded — a coordination gap no single ULB dashboard currently solves — and act on it without approving new construction, since it works with capacity that already exists.
Use accumulated multi-city historical composition data to decide where new shared cluster facilities should actually be sited, based on real feedstock volume and transport distance rather than guesswork.

Citizens and informal waste pickers

Get visibility into where their segregated waste actually ends up, and fair, transparently logged valuation for material an informal picker recovers — data that's currently invisible to the formal system entirely.

How it makes existing tasks safer or easier

Replaces guesswork with measurement — "how much of our waste is actually recyclable" is currently usually an assumption based on area or demographic, not a measured fact. This makes it a real-time number.
Makes landfill diversion provable, not just claimed — a tamper-evident, hash-chained record means a diversion or emissions-avoided number can't be quietly inflated after the fact, which is the missing piece keeping most Indian composting/biomethanation plants out of the carbon-credit market today.
Turns a manual coordination problem into an automatic one — cross-ULB routing that currently doesn't happen at all (because no one is watching two neighboring ULBs' capacity at once) happens automatically, with zero new physical infrastructure required.
Moves accountability upstream, where it's cheaper to fix — instead of only sorting waste after it's already mixed, it surfaces exactly where source segregation is failing, so the problem can be addressed at the household/ward level, where it's far cheaper to fix than downstream.

**The problem it solves**

Municipal solid waste in Tamil Nadu (and India broadly) mostly arrives at transfer stations and treatment plants already mixed, and segregation compliance varies wildly between cities — some report near-100%, others under 50%. On top of that, treatment infrastructure that already exists — compost yards, biomethanation plants, MRFs — often sits underused in one ULB while a neighboring ULB's plant is overloaded, purely because there's no system connecting real-time waste arrivals to available capacity. The result: recoverable waste ends up in landfill not because treatment doesn't exist, but because nothing is coordinating supply with it.

SmartWasteGrid closes that loop end-to-end:

At intake — camera and sensor-fusion detection estimates each batch's Wet / Dry / Recyclable composition in real time, logged to a tamper-evident, hash-chained ledger so the record can't be silently altered later.
At the city level — a ward-level segregation compliance heatmap gives municipalities a data-backed view of where source segregation is failing, instead of relying on spot inspections.
Across the state — a cross-ULB matching engine routes excess recoverable waste to the nearest facility with available capacity instead of defaulting to landfill when the local plant is full, using infrastructure the state already operates rather than requiring new construction.
For accountability and funding — a diversion-rate dashboard turns "we help the environment" into a measurable, trackable number per district, and a carbon-credit MRV export packages that same tamper-evident data into an audit-ready format plants can use to actually apply for carbon-credit revenue.    Facility operators (compost yards, biomethanation plants, MRFs)

See real-time composition of incoming batches instead of discovering what arrived only after it's dumped — lets them plan processing capacity for the day instead of reacting to it.
Get a live feed showing when a nearby ULB has overflow they could absorb, turning idle capacity into utilized capacity without manual coordination calls.
Generate an auditor-ready record of exactly how much waste they diverted from landfill and processed, usable to actually apply for carbon-credit revenue — something most plants currently have no reliable paper trail to support.

Municipal commissioners / ULB officials

View a ward-level segregation compliance heatmap instead of relying on spot checks — makes it easy to see which wards or collection routes consistently send contaminated batches, so enforcement or education can be targeted instead of citywide and blanket.
Track a district-level diversion rate over time as a concrete, defensible sustainability metric for reporting up to the state, instead of an estimate.

State-level planners (CMA / Tamil Nadu Urban Infrastructure)

Get cross-ULB visibility into which treatment plants are underused and which are overloaded — a coordination gap no single ULB dashboard currently solves — and act on it without approving new construction, since it works with capacity that already exists.
Use accumulated multi-city historical composition data to decide where new shared cluster facilities should actually be sited, based on real feedstock volume and transport distance rather than guesswork.

Citizens and informal waste pickers

Get visibility into where their segregated waste actually ends up, and fair, transparently logged valuation for material an informal picker recovers — data that's currently invisible to the formal system entirely.

Team **CATALYST CREW** -- [RUBIKHA M](https://github.com/rubikha4407), [Gokul N](https://github.com/gokulpn2025aiml-beep), [Nicksan Raj N U](https://github.com/nicksan-17), [Varun N S](https://github.com/varunns2007), [rashmika manikandan](https://github.com/rashmikashamara-dotcom)

`2026-08-30`

---

### Aquabot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aquabot-d21d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prithika-gv/aquabot-rl.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1q0I0JqFC2f4ViPc4kxUGQGbsr3d98x0b/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4XBwIPghyXc) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> AI Powered Robot for Waste Collection & Monitoring

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Water bodies face two connected challenges: floating waste and gradual sediment accumulation. Floating plastic requires continuous cleanup, while siltation silently reduces reservoir and tank capacity and is typically assessed through infrequent, expensive surveys.

AquaBot is a low-cost autonomous platform that detects, pursues and collects floating debris using edge AI, while simultaneously collecting GPS, water-quality and environmental data. Its ultrasonic sensing capability provides a foundation for measuring the sediment-water interface and tracking sediment accumulation. The platform combines autonomous navigation, waste collection and environmental monitoring into a single modular system, enabling more frequent and data-driven water-body assessment.

**Challenges we ran into**

Building AquaBot required integrating AI, embedded electronics, mechanical collection, environmental sensors and a live dashboard into one working system.

One major challenge was running YOLO-based debris detection directly on the Raspberry Pi 5 while also handling navigation and communication. We optimized the AI pipeline for edge deployment and achieved approximately 5.5 FPS, allowing the robot to detect floating debris without depending on cloud processing.

Another challenge was coordinating the Raspberry Pi and ESP32. The Raspberry Pi handles AI detection and navigation, while the ESP32 handles real-time motor and conveyor control. We established UART communication between them to reliably transfer navigation commands and separate computational tasks from time-critical hardware control.

We also had to convert AI detection into actual autonomous movement. Instead of simply detecting waste, we implemented a Search → Pursue → Collect workflow, where the robot searches for debris, navigates toward the detected target and activates the conveyor for collection.

Integrating multiple sensors was another hurdle. GPS, pH, water temperature, ambient temperature, humidity and ultrasonic sensing had to work together while providing reliable real-time telemetry.

Team **Phoenix Horizons** -- [Rayhan Hameed](https://github.com/Ray-5106), [Prithika G](https://github.com/prithikag), [Kaviya Sree](https://github.com/kaviyasrees)

`2026-08-30`

---

### Sorter G - AI Powered Waste  Sorting Robot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-autonomous-waste-sorting-robot-sorter-g-709c) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/gnskPPD5WBQ) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Turning Waste into Resources with AI-Powered Robot

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The world generates enormous amounts of waste, but a significant portion of recyclable material is still lost because mixed waste is difficult, expensive, and unsafe to sort manually , less efficiently.

When recyclable materials such as PET, HDPE, metals, cardboard and other recoverable materials are mixed with general waste, they can be contaminated or missed during manual sorting. Valuable materials are then sent to landfills or incineration instead of being recovered and reused.

At the same time, waste-sorting workers often perform repetitive, physically demanding and potentially hazardous picking operations, particularly when handling contaminated or sharp waste.

This creates a chain of problems:

 - More waste reaches landfills because recoverable materials are not separated effectively.
 -Valuable recyclable materials are lost, reducing material recovery and recycling rates.
- Environmental pollution increases through landfill growth, potential soil and groundwater contamination, and greenhouse-gas emissions.
 -More virgin resources are extracted when recyclable materials that could replace raw materials are lost.
 -More energy and fossil resources are consumed to produce new materials instead of recovering existing ones.
 Workers face repetitive and hazardous tasks, increasing physical strain and exposure to contaminated waste.
 Waste-management costs increase when facilities depend heavily on manual sorting and disposal.
 Inconsistent manual sorting can reduce recovery efficiency, especially in high-volume mixed waste streams.
How SorterG Addresses It

SorterG uses AI-based computer vision + a Cartesian X/Y/Z robotic system + vacuum end-effector to identify and automatically pick targeted recyclable materials from a mixed waste stream and route them to designated bins.

This enables:

Mixed Waste → AI Identification → Robotic Picking → Material Separation → Higher Recovery → Less Landfill

The Impact

SorterG is designed to contribute to:

Higher material recovery — recover valuable materials that may otherwise be lost.

Landfill reduction — divert recyclable materials away from disposal.

Lower environmental impact — support recycling and reduce the need for continuous disposal and virgin-material production.

Resource conservation — keep materials in circulation instead of extracting additional raw resources.

Potential energy & fossil-resource savings — recycling many materials can require less energy than producing them from virgin resources.

 -Safer work environments — reduce workers' exposure to repetitive picking and potentially hazardous waste.

-More efficient waste facilities — automate a key bottleneck while potentially integrating with existing conveyor systems.

 -New and upgraded jobs — shift human roles toward robot supervision, maintenance, quality control, system operation and facility management.

**Challenges we ran into**

Building SorterG required integrating AI vision, mechanical motion, electronics and robotic control into one reliable system. Our biggest challenge was making all these components work together accurately and safely.

🤖 1. Precise Robotic Positioning

The robot needed to move accurately to different positions for picking and depositing materials. Small positioning errors could cause the vacuum to miss the object.

How we solved it:
We implemented controlled X/Y/Z motion, homing using limit switches, calibrated movement positions and predefined pick-and-place coordinates to improve repeatability.

👁️ 2. AI Detection → Robot Movement

Detecting an object with AI was only half the problem. We had to convert the detected object's position into coordinates that the robot could actually reach.

How we solved it:
We developed a communication pipeline between the computer vision system and the robotic controller, converting detected objects into actionable pick locations.

🌀 3. Reliable Picking

Different waste materials have different shapes, surfaces and weights. A vacuum system that works well on one object may fail on another.

How we solved it:
We integrated a vacuum end-effector with controlled suction timing, allowing the robot to pick, hold and release objects at designated locations.

🔌 4. Hardware–Software Integration

We encountered issues coordinating the Arduino/RAMPS controller, stepper motors, limit switches, vacuum system and AI computer.

How we solved it:
We separated the system into controllable modules and tested each subsystem individually before integrating them into the complete workflow.

🛑 5. Homing & Safety

The robot needed a reliable starting position every time. Without accurate homing, the same coordinates could result in different physical positions.

How we solved it:
We implemented limit-switch-based homing and defined a known reference position before allowing the sorting cycle to begin.

⚙️ 6. Real-World Reliability

A system that works in a demonstration is not automatically ready for a real waste facility. Objects can be misplaced, detection can fail, or a pick can be unsuccessful.

How we solved it:
We designed the system around repeatable motion, defined operating positions and modular control, allowing individual components to be calibrated and improved without redesigning the entire system.

🚀 What We Learned

The biggest challenge wasn't building the individual components—it was making AI, robotics and waste handling work together as one reliable system.

We moved from “a robot that can pick objects” to a complete AI-assisted material recovery system.

**Track Commons AI**

AI is central to SorterG. Our computer-vision model identifies recyclable materials in mixed waste, and its predictions directly drive the robotic picking and sorting process. This creates a real-world AI application with measurable environmental, operational, and safety impact.

Team **Green Warming** -- [Boaz K](https://github.com/boazk0515-bot), [DONSINTO SAJI](https://github.com/dinsintosaji)

`2026-08-30`

---

### Smart Energy Management
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-energy-management-predictive-alerts-and-fault-detection-using-ai-8ba2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ai.studio/apps/c42b2b0a-74e7-4444-adaf-79f4a11fb7fc) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> AI-driven optimization for sustainable energy grid

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

During the development of our project, we faced several challenges, particularly in designing a compact retrofit system that can reliably collect data from different motor parameters. Initially, we used simulated sensor inputs in Wokwi to test our ESP32-based system, but we realized that real machine data would be necessary to validate the fault-detection approach. We also had to consider how to detect sudden electrical abnormalities quickly while minimizing unnecessary data transmission and power consumption. Another challenge was designing the system to scale from a single machine to multiple machines while maintaining a centralized dashboard. These challenges helped us refine our architecture by introducing local edge processing, wireless communication, cloud-based monitoring and AI-assisted analysis.

**The problem it solves**

Industrial motors can develop faults such as overload, overheating, abnormal vibration and electrical abnormalities. In many existing machines, these conditions are not continuously monitored, and manual inspection is difficult when machines are located far apart. This can result in delayed fault detection, unexpected breakdowns, production downtime and energy wastage.

Team **GreenGrid AI** -- [rakshana s](https://github.com/rakshana2503111), [Preethi M](https://github.com/preethi2503109), [PRISHA S](https://github.com/singaiprisha-stack), [Manimozhi Rajendran](https://github.com/manimozhi2505103)

`2026-08-30`

---

### FlowCapital
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/flowcapital-7607) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rohit1638/FlowCapital) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Where production evidence becomes credit

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-333333?style=flat-square)

**The problem it solves**

Manufacturers who need working capital to fund a production run (raw materials, labor, WIP) usually have to prove to a lender that the order is real and progressing — but that proof today is scattered across POs, GST filings, production plans, and warehouse counts, with no single verifiable trail. Lenders end up underwriting on incomplete, unverifiable information and slow manual back-and-forth.

FlowCapital AI turns that evidence into a structured, auditable financing workflow:

For manufacturers: a single portal to request production financing backed by real documents (purchase orders, production plans, collateral), track the physical goods lifecycle (PO → Raw Material → Production → Finished Goods → In Transit → Invoiced → Settled), and get an AI assistant that explains why their confidence score is what it is and what would improve it.
For lenders: a decision workspace that surfaces a deterministic confidence score, collateral coverage, and any conflicts (e.g. a quantity mismatch between what was planned and what's actually in the warehouse) — so they can approve, reject, or conditionally approve exposure with a full audit trail instead of a black-box judgment call.
Makes it safer by keeping AI explanations backend-only (Gemini key never touches the browser) and falling back to deterministic finance rules if the AI is unavailable, so a lending decision is never blocked on — or silently altered by — an LLM being flaky

**Challenges we ran into**

A few hurdles that show up directly in the project's own troubleshooting notes (worth mentioning if the real story matches one of these, or as a starting point to expand on):

CORS / "failed to fetch" between frontend and backend — since the frontend (Next.js) and backend (FastAPI) run on separate ports, requests failed until NEXT_PUBLIC_API_BASE_URL in .env.local was pointed at the exact backend port. Fixed by allowing all localhost ports in dev on the backend CORS config and double-checking the env var matched.
Document upload silently failing — file uploads (PO/GST/production plan evidence) wouldn't go through until python-multipart was installed in the backend virtual environment, since FastAPI needs it to parse multipart form data.
Port collisions — port 3000 was often already taken, so the dev flow had to tolerate Next.js falling back to another port (e.g. 3005) without breaking anything downstream.
Keeping the AI safe to depend on — since lending decisions can't hang on a third-party API being up, a deterministic fallback engine had to mirror what Gemini would produce (confidence bands, financeable value, risk explanations) so the underwriting flow degrades gracefully instead of breaking.

Team **ARAM** -- [Sachit Ram](https://github.com/sachit-17), [SriDhanvanth P](https://github.com/sridhanvanth07), [Rohit Ram](https://github.com/Rohit1638), [Adhithya Ilayaraja](https://github.com/Astraxz)

`2026-08-29`

---

### A2A
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aa-6f83) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Naghul03/Vit_PixelPirates.git) [![Built at](https://img.shields.io/badge/Built%20at-Origins-0052CC?style=flat-square)](https://origins.devfolio.co)

> Autonomous Finance for Agent to Agent Economy

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

Our biggest challenge was turning a complex problem statement into a real, working prototype. Building and integrating multiple AI agents, connecting their workflows, and implementing key features like escrow, collateral, verification, settlement, and reputation required several iterations. We also spent significant time researching the problem deeply to identify the core requirements and make them practical within the hackathon. Through continuous testing and debugging, we gradually brought the complete A2A workflow together.

**The problem it solves**

AI agents are becoming capable of performing tasks autonomously, but they still lack a reliable economic infrastructure to safely work and transact with other agents. Today, agents cannot easily determine whom to trust, agree on fair economic terms, protect payments, verify whether work is genuinely completed, or handle failures and disputes without human or centralized intervention. This creates a fundamental trust and accountability gap in agent-to-agent commerce.

A2A addresses this gap by providing an autonomous financial layer that makes agent-to-agent transactions verifiable, accountable, and economically secure.

Team **Pixel Pirate** -- [naghul varshan](https://github.com/naghul03), SAHITH M, [Vigneshwaran S](https://github.com/vickyy2424), [Rahul S](https://github.com/ZenitsuAckerman)

`2026-08-29`

---

### Precursor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/precursor-ff34) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Anagha-Hebbale/Precursor) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://precursor-organiser.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/HOsaTAEY5_k) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co)

> See small problems before they become incidents.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Integrating three independently-built pieces (AI/ML, backend, frontend)
Preventing report volume from drowning out severity*
Early in scoring design we realized a widely-reported minor issue could out-rank a rarely-reported serious one under a simple count-based formula — a real design flaw, not just a demo bug, that needed explicit fixing (severity weighting, per-user/per-location report caps) rather than trusting the naive math.
No photo hosting infrastructure*
Locally-selected photos only exist as browser-local blob URLs — the backend/AI literally can't fetch them over the network. Fixed by sending images as base64 directly, avoiding a dependency on any third-party hosting service that could fail mid-demo.
Merge conflicts and environment drift across a distributed team*
Parallel branches (AI/ML, backend, frontend) hit real git conflicts when merged, plus classic environment issues (Windows vs Mac terminal differences, PATH/venv setup) that ate real time close to the deadline.

**The problem it solves**

THE PROBLEM

Many physical-world problems begin as small, isolated signals:

A flickering light
A water leak
An overflowing bin
A damaged staircase
Increasing crowding
A minor safety hazard
Individually, these observations may not appear urgent. However, when similar observations start appearing from multiple people in the same area, they can indicate a developing problem.

Traditional reporting systems generally react after an incident is recognized.

Precursor aims to detect the pattern before the incident.

💡 Solution
Precursor allows users to submit lightweight observations containing:

📝 Description
📷 Optional photo
📍 Location
👤 User ID
The system then:

Receives the observation through FastAPI
Uses Gemini's multimodal AI to identify issue tags and severity
Stores the observation in PostgreSQL
Groups related observations using issue similarity and geographic proximity
Calculates an Emergence Score
Generates alerts when a cluster crosses a defined threshold
Displays observations and alerts through the dashboard

Team **Committed.** -- [Anagha Hebbale](https://github.com/Anagha-Hebbale), [Ann Gracia](https://github.com/anngracia07), [Anoushka Pramanik](https://github.com/anoushka3047), [Arushi Sinha](https://github.com/arushisinha12)

`2026-08-23`

---

### CrashAid-An AI-Powered Road Safety Ecosystem
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/crashaidan-aipowered-road-safety-ecosystem-49ec) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VengalaAbhinay/CrashAid-2.0) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1218619693?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co)

> CrashAid – Predict. Prevent. Protect

![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![OSRM](https://img.shields.io/badge/OSRM-333333?style=flat-square)

**Challenges we ran into**

⚠️ Challenges We Ran Into

During the development of CrashAid, we faced several technical and design challenges while trying to build a real-time, reliable emergency-response system.

 🔧 1. Sensor-Based Crash Detection

One of the biggest challenges was accurately detecting crashes using mobile sensors like the **accelerometer, gyroscope, and GPS**.
It was difficult to differentiate between actual accidents and normal sudden movements like braking or speed breakers.

**How we solved it:**
We implemented a **multi-factor approach**, combining speed changes, motion patterns, and a **confirmation countdown** to reduce false positives.

---

📱 2. Real-Time Location Tracking

Maintaining **accurate and continuous GPS tracking** was challenging, especially with fluctuating network conditions and device limitations.

**Solution:**
We optimized location updates and ensured that **last known location** is always available, even in low-connectivity scenarios.

---

🗄️ 3. Offline Data Availability

Emergency situations often occur in areas with poor internet connectivity, making it difficult to fetch nearby services.

**Solution:**
We integrated a local **SQLite database (`places.db`)** containing emergency service data, allowing the app to function **offline**.

---

🗺️ 4. Map Integration & Routing

Integrating maps, showing routes, handling markers, and visualizing real-time updates was complex.

**Solution:**
We used optimized mapping libraries and focused on **clear route visualization, markers, and efficient updates** for better performance.

---

🚦 5. Traffic Signal Priority (Simulation)

Implementing real-world traffic light control is not feasible in a hackathon environment.

**Solution:**
We designed a **simulation-based approach** that identifies signals along the route and demonstrates an **emergency priority corridor**, making the concept practical and demo-friendly.

---

🤖 6. Lightweight AI Implementation

Running AI features like **driver monitoring and first-aid assistance** on mobile devices without heavy processing was challenging.

**Solution:**
We used **lightweight and optimized AI approaches**, focusing on feasibility and performance rather than complex models.

---

🔄 7. System Integration

Combining multiple features like **crash detection, SOS, routing, AI, and offline data** into one smooth workflow was difficult.

**Solution:**
We designed a **modular architecture**, ensuring each component works independently but integrates seamlessly into the overall system.

---

🎯 Conclusion

These challenges helped us improve CrashAid into a **more practical, reliable, and scalable solution**, ensuring it performs effectively even in real-world emergency situations.

**The problem it solves**

🚨 The Problem It Solves

Road accidents remain one of the major causes of fatalities and serious injuries worldwide, largely due to **delayed emergency response, lack of real-time information, and poor coordination between victims, responders, and hospitals**.

In many real-life situations:

* Accident victims are **unable to call for help** due to unconsciousness, panic, or severe injuries
* Emergency responders **do not receive accurate location or critical medical details in time**
* Ambulances **lose valuable minutes due to traffic congestion and inefficient routing**
* Drivers are **unaware of potential dangers such as potholes, hazardous roads, or fatigue**
* Internet connectivity may be unreliable, making it difficult to locate nearby emergency services

While existing solutions offer features like navigation, emergency calling, or crash detection, they operate in isolation and **fail to provide a unified, end-to-end emergency response system**.



💡 Our Solution — CrashAid

CrashAid is an **AI-powered road safety and emergency response platform** designed to bridge the gap between **accident occurrence and timely medical assistance**.

It combines **prevention, detection, and response** into one integrated system:

🚗 Prevention

* Detects **driver drowsiness and distraction** using a smart dashcam
* Allows users to report **potholes and road hazards**, helping prevent future accidents

💥 Detection

* Uses mobile sensors (accelerometer, gyroscope, GPS) for **automatic crash detection**
* Evaluates crash **severity** and reduces false alerts with a confirmation countdown

🚨 Response

* Automatically triggers **SOS alerts with live GPS location**
* Shares critical information with emergency contacts
* Provides **offline access to emergency services** using a local SQLite database (`places.db`)
* Identifies and recommends the **most suitable hospital**, not just the nearest

 🚑 Intelligent Emergency Coordination

* Generates **fastest, traffic-aware ambulance routes**
* Identifies traffic signals along the route and simulates an **emergency priority corridor**
* Reduces delays in reaching medical facilities

🤖 Assistance

* Includes an **AI First-Aid Assistant** to guide users or bystanders during the critical waiting time


🎯 Impact

CrashAid transforms emergency response by:

* Reducing dependency on manual actions during critical situations
* Improving **speed, accuracy, and coordination** in emergency handling
* Enhancing **road safety awareness and prevention** through real-time data



🏁 In Summary

CrashAid is not just an SOS application — it is a **complete road safety ecosystem** that works **before, during, and after an accident**.

By connecting **driver monitoring, crash detection, emergency response, smart routing, and road intelligence**, CrashAid aims to **save lives by making emergency response faster, smarter, and more reliable**.

**Road Safety**

🚗 How CrashAid fits into Road Safety

CrashAid directly aligns with the Road Safety track by addressing all three critical aspects: **accident prevention, real-time detection, and faster emergency response** using AI and data.

🛡️ Prevention

CrashAid improves road safety before accidents happen by:

* Monitoring drivers using a **Smart Dashcam** to detect drowsiness and distraction
* Enabling **crowd-sourced pothole and hazard mapping**, helping identify dangerous roads
* Alerting drivers about nearby risks to reduce accidents

💥 Detection

* Uses mobile sensors (accelerometer, gyroscope, GPS) for **automatic crash detection**
* Identifies severity and triggers alerts without requiring manual input

🚨 Response

* Instantly sends **SOS alerts with live GPS location**
* Helps locate **nearby hospitals and emergency services**, even offline
* Provides **AI-assisted first aid guidance** during critical moments

 🚑 Smart Mobility & Emergency Routing

* Generates **fastest routes for ambulances** using real-time data
* Identifies traffic signals along the route and simulates an **emergency priority corridor**
* Reduces delays in reaching medical care

---

🎯 In Summary

CrashAid uses **AI, mobile sensors, and real-time data** to create a complete road safety solution that not only **reduces accidents** but also ensures **faster and smarter emergency response**, perfectly aligning with the goals of the Road Safety track.

Team **RESURGENCE** -- M Jyothika, [Vengala Abhinay](https://github.com/VengalaAbhinay), Srikeerthi Mandadi

`2026-08-16`

---

### incimin.io
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/incimin-0cb4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vivonk/incimin) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://incimin.ngrok.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/g4cUC-qv_No) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon:%20Building%20at%20the%20Frontier-0052CC?style=flat-square)](https://pushtoprod-india.devfolio.co)

> Autonomous AI SRE: root cause in 60 seconds

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Anthropic](https://img.shields.io/badge/Anthropic-333333?style=flat-square) ![Qdrant](https://img.shields.io/badge/Qdrant-333333?style=flat-square) ![Clickhouse](https://img.shields.io/badge/Clickhouse-333333?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-333333?style=flat-square) ![Memgraph](https://img.shields.io/badge/Memgraph-333333?style=flat-square)

**What is the deployed URL for this project?**

https://incimin.ngrok.app

**What is the problem your project solves?**

## The Problem

When a production incident fires, the L1 on-call engineer spends **15–45 minutes** manually correlating signals across service topology maps, distributed traces, raw logs, and runbooks before forming a single hypothesis.

This is:
- **Expensive** — senior engineers paged at 2 AM, pulled away from deep work
- **Error-prone** — high cognitive load under pressure leads to wrong initial hypotheses and wasted investigation time
- **Slow** — every minute of MTTR is lost revenue and eroded customer trust

The L1 triage role — *"what broke, why, and what should I do?"* — is entirely pattern-matching across structured data: the service dependency graph, telemetry signals, and past runbooks. It requires speed and breadth of signal, not uniquely human judgment. Humans are the bottleneck in a loop that a machine can close faster and more accurately.

**The impact is real:** In a mid-size enterprise with a microservices architecture, a single P1 incident can cost $50K–$500K in engineering time and customer churn. The L1 triage step alone accounts for 40–60% of time-to-resolve.

**How you are solving it?**

## The Solution

incimin.io is an autonomous AI SRE agent that, the moment an alert fires, does what an L1 engineer does — but in under 60 seconds.

### Architecture

A **LangGraph state machine** with Bayesian belief updating drives the investigation loop. Three fully deterministic tools own the critical path:

1. **Cypher BFS (Memgraph)** — traverses the live service dependency graph to find which upstream services could have caused the observed symptoms, ranked by graph distance and failure probability
2. **ClickHouse SQL (SigNoz)** — queries correlated distributed traces and logs against the candidate services to find error spikes, latency outliers, and crash signals in the exact time window of the incident
3. **Qdrant semantic search** — retrieves the most relevant operational runbook from the pre-embedded knowledge base, matched by incident description and affected service

Zero LLM reasoning in the critical path — hallucination risk is eliminated where it matters most.

### Human-in-the-Loop Safety Gates

The agent proposes; humans decide. Before any remediation executes, the agent **pauses and records** exactly what it wants to do and why. Approved actions are drawn from a **fixed allowlist** — never LLM-composed commands. Approval decisions are durable, surviving API process restarts (backed by Postgres + LangGraph checkpointer).

### Demo Scenario

OpenTelemetry Astronomy Shop (14 real microservices) as the victim application. Deterministic chaos injection: `paymentservice` crash → checkout latency spike → alert fires → agent runs. Memgraph Lab shows the live graph traversal on split-screen as the agent navigates from the alerting service to the root cause node in real time.

### Stack

- **Agent orchestration**: LangGraph 1.2 + Claude (Anthropic) for synthesis
- **Graph DB**: Memgraph + MAGE (BFS/DFS Cypher algorithms)
- **Telemetry**: SigNoz + ClickHouse (OTel-native traces and logs)
- **Vector store**: Qdrant + fastembed (fully local, no API key required)
- **Backend**: FastAPI + Postgres (durable incident state + HITL approval gates)
- **Frontend**: React dashboard with live SSE step graph
- **Infra**: Full Docker Compose local stack — zero cloud dependencies

*This project was built from the ground up during the hackathon sprint. The OTel Astronomy Shop is an open-source reference app used as the incident simulation target.*

**How Did You Use Claude?**

## How We Use Claude

Claude serves as the **synthesis layer at the tail of the investigation pipeline** — the one place where LLM reasoning is safe, appropriate, and genuinely valuable.

### What Claude Receives

After the deterministic retrieval pipeline assembles structured evidence, Claude receives an evidence package containing:
- **Graph traversal result**: the BFS path from the alerting service to the suspected root cause node, with edge weights and service metadata
- **Telemetry findings**: correlated error rates, latency percentiles, and crash logs from ClickHouse — structured rows, not free text
- **Runbook match**: the most semantically relevant operational playbook from Qdrant, matched by incident description and affected service
- **Bayesian posteriors**: confidence scores for each root cause hypothesis after the investigation loop converges

### What Claude Produces

1. A **root cause statement** with a confidence level (grounded in Bayesian posteriors, not intuition)
2. A **cited explanation** of the evidence chain — which signals pointed where and why
3. **Operator-readable remediation steps** drawn from the retrieved runbook, adapted to the specific incident context

### The Key Design Decision

Claude is explicitly *not* used for topology reasoning, SQL generation, or any step where a hallucination would send an on-call engineer in the wrong direction at 2 AM.

**Design principle: deterministic retrieval + Claude synthesis = fast, trustworthy incident response.**

This means Claude's output is always grounded — it cannot invent a root cause that isn't backed by a real graph path and real telemetry signals. Claude adds the human-readable narrative layer that turns structured evidence into an actionable incident report.

Team **Capillary** -- [Nirmal Sarswat](github.com/vivonk), Sanjay Kumar

`2026-08-08`

---

### MemoSphere-AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/memosphereai-1c0f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MuhammedMazinMH/memosphere-ai-build) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://memosphere-ai-build.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Hk-IjVe4vY4) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Your Second Brain for Smarter Learning

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![AWS](https://img.shields.io/badge/AWS-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![DynamoDB](https://img.shields.io/badge/DynamoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![clerk authentication](https://img.shields.io/badge/clerk%20authentication-333333?style=flat-square) ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-333333?style=flat-square)

**The problem it solves**

Students today study from multiple sources like lecture notes, PDFs, assignments and project documents. As the number of documents increases, finding important information becomes difficult and time consuming. Most students spend more time searching for notes than actually learning.

MemoSphere AI solves this problem by converting uploaded study material into a searchable knowledge base. It automatically extracts important concepts, generates a visual knowledge graph, provides AI-powered summaries, creates quizzes and helps students understand their weak areas through learning insights and exam readiness analysis.

Instead of reading the same documents again and again, students can quickly search, revise and learn from their own knowledge in one place.

**Challenges we ran into**

The biggest challenge was designing a system that could transform unstructured PDF documents into meaningful knowledge without losing important context.

Another challenge was generating a clean knowledge graph without showing irrelevant or duplicate concepts. We solved this by improving our AI prompt design, validating the AI responses using structured schemas and storing only clean data.

Integrating AWS DynamoDB with the application while maintaining user-specific knowledge was another learning experience. We also optimised document processing so that uploaded files, generated concepts, quizzes and analytics remained properly connected.

Finally, ensuring smooth synchronisation between all modules after every upload required careful handling so that the knowledge graph, search, AI coach and learning analytics always reflected the latest data.

Muhammed Mazin MH

`2026-06-26`

---

### Prompt2Site
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/promptsite-aa64) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Vasu-uu/Prompt2Site) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> From prompt to production-ready page — in seconds.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

A major challenge was balancing structure with variety. The AI needed to return strictly typed, predictable JSON for the renderer to work with — but predictable structure tends to produce repetitive-looking sites. Getting genuinely varied layouts, colour palettes, and typography across generations, without breaking the schema the renderer depended on, took a fair amount of prompt tuning.

The other challenge was the export pipeline — taking a site that exists as live, dynamically rendered React state and reliably converting it into a single self-contained HTML file with all styling embedded, while keeping it visually identical to the live preview.

**The problem it solves**

Building a website usually means writing code, making design decisions, sourcing images, and repeating that whole process every time something needs to change. That's a real barrier for non-technical users, and a slow grind even for developers who just want to prototype an idea quickly.

Prompt2Site AI removes that friction. You describe the site you want in plain language, and it generates a complete, structured, responsive layout — theme, copy, and components included. Changes happen the same way: just ask, and the AI updates the existing design instead of starting over. And because it exports real, production-ready HTML/CSS, it's not just a mock up tool — what you build is usable.

[Vasudev V](https://github.com/Vasu-uu)

`2026-06-29`

---

### EcoTrace
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecotrace-beb4) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

[Anushka Tyagi](https://github.com/AnuTyagi-1306)

`2026-07-30`

---

### ExpiryGuard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/expiryguard-ai-an-agentic-platform-for-intelligent-expiry-management-and-waste-prevention-dd0b) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Save Products Before They Become Waste

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Businesses such as supermarkets, retailers, warehouses, distributors, and other expiry-sensitive organizations manage large numbers of products across different batches, each with its own expiry date. In many cases, expiry tracking still depends on manual shelf checks, spreadsheets, or basic date reminders. This makes the process time-consuming, error-prone, and reactive. Products are often discovered only when they are very close to expiry—or after they have already expired—resulting in preventable waste, financial losses, unnecessary disposal, and inefficient inventory management.

ExpiryGuard AI solves this problem by transforming expiry management from a manual checking process into a proactive, intelligent workflow. Users can scan a product's barcode, register its batch, quantity, and expiry information, and continuously track inventory through a centralized dashboard.

The platform goes beyond simply asking, “When will this product expire?” It also asks, “Is this stock likely to remain unsold before it expires, and what action should be taken now?”

Using factors such as remaining shelf life, available stock, sales velocity, and estimated demand, the system generates an Expiry Risk Score to identify products that are at high risk of becoming waste. It also applies the FEFO (First-Expired, First-Out) principle to help businesses prioritize the correct batches for sale or movement.

When a risk is detected, the system can recommend actions such as:

Prioritizing a batch for immediate sale
Applying an early discount
Transferring stock to a location with higher demand
Reducing or postponing unnecessary replenishment
Initiating a supplier return where applicable
Flagging suitable surplus products for redistribution or donation

Instead of ending with an alert, ExpiryGuard AI is designed as an agentic system that follows a Detect → Predict → Recommend → Approve → Act workflow. With Prava integrated as the action and transaction layer, approved workflows can progress toward real-world actions such as purchases, payments, or other supported transactions.

This makes expiry management easier for businesses by reducing repetitive manual checks, helping staff focus on the most urgent inventory first, and enabling earlier intervention while products still have value. The broader impact is reduced preventable waste, lower financial losses, smarter procurement, and more efficient use of available products.

**Challenges we ran into**

One of the biggest challenges was designing the project as more than a simple expiry-date reminder. A basic system could send an alert a fixed number of days before expiry, but that would not account for the fact that different products have different stock quantities, sales rates, demand patterns, and shelf lives. We addressed this by designing an Expiry Risk Score that considers multiple factors such as remaining shelf life, available quantity, sales velocity, and estimated demand. This allows the system to prioritize products based on actual risk rather than only the expiry date.

Another challenge was batch-level inventory tracking. The same product can have multiple batches with different manufacturing and expiry dates, so storing only one expiry date per product would produce incorrect results. We solved this by separating product information from batch information and tracking each batch independently. This also enabled us to implement the FEFO (First-Expired, First-Out) approach.

Barcode data was another hurdle. A barcode can help identify a product, but it does not always contain batch-specific information such as manufacturing date and expiry date. To handle this, we designed a hybrid workflow where barcode scanning identifies the product, while missing batch-specific details can be captured separately and stored for future tracking.

We also faced the challenge of deciding when the AI agent should act automatically and when the user should remain in control. Actions involving purchases, payments, stock transfers, or other business decisions should not be executed without appropriate authorization. We therefore designed a human-in-the-loop workflow: the system detects the risk, explains why the product is at risk, recommends an action, and asks for approval before proceeding with a supported action through Prava.

Finally, integrating multiple components—barcode scanning, inventory management, expiry monitoring, risk scoring, AI recommendations, alerts, and transaction workflows—into one coherent system was challenging. We addressed this by dividing the application into modular layers and building the workflow incrementally:

Scan → Track → Predict → Recommend → Approve → Act

These challenges helped us move from the idea of a basic expiry tracker toward a more practical, scalable, and action-oriented solution for preventing product waste.

[G Sanjay](https://github.com/sanjay-hub07)

`2026-07-13`

---

### Build a wardrobe
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/build-a-wardrobe-31e4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/archisman-codex/fashion-recommender) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fashion-recommender-7tuxhuhea9gxrfzxmgx85u.streamlit.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/TgCIdatyXes) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> A fashion recommendor that suggests clothing.

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Package JSON](https://img.shields.io/badge/Package%20JSON-333333?style=flat-square) ![Pillow](https://img.shields.io/badge/Pillow-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**Challenges we ran into**

.

Challenges I ran into
**Solo build** : With only one person, I had to make less time taking software so couldn't use live ML-based skin tone detection and live web scraping in favor of a manual swatch-based undertone picker and a curated, hand-built product dataset, so I could show a functional project.
**Store locator reliability****-:The first choice for real-world store lookup was using google maps api but it needed payment authorization, which I wasn't comfortable with, so I switched to OpenStreetMap's free Nominatim + Overpass APIs — then had to work around the free Overpass server's frequent timeouts by building in automatic fallback across three mirror servers.
**Balancing precision with coverage**: The recommender often could not find recommendations for unusual colours and kept returning no outputs. solved this with a fallback system that filters step-by-step (season → occasion → color-only) instead of showing a dead end.
**Tooling from scratch**: Setting up Git, GitHub, and the Python/Streamlit environment for the first time mid-hackathon, and debugging real deployment issues (PATH errors, nested folder structure, API 504s) live under time pressure.

**The problem it solves**

Picking outfits that actually suit you based on  your skin tone, the occasion, the season, and budget is a decision most people often find difficult to make. Existing shopping apps recommend based on browsing history or generic trends, not on you. Our app closes that gap: upload a photo, tell it your budget, location, season, and occasion, and it recommends clothing and accessories chosen to flatter your specific skin undertone, then shows where to actually buy them, both online (direct product links) and offline (nearby stores), so the recommendation turns into a purchase in one step.

Archisman Datta

`2026-07-27`

---

### Second Brain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/second-brain-80f5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/b1uerayy/second-brain) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://open.substack.com/pub/reh4n/p/your-save-folder-is-where-ideas-go?r=6n65hc&utm_campaign=post-expanded-share&utm_medium=post%20viewer) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> The Future of Personal Knowledge Management

![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

We live in an era where information is abundant, but knowledge is not. Every day, we save articles, research papers, videos, social media posts, and notes with the intention of revisiting them later. Over time, these resources pile up in bookmarks, note-taking apps, and read-later lists, rarely being opened again. This phenomenon, often referred to as **information hoarding**, creates a gap between consuming information and actually learning from it.

Most existing tools focus on storing information or helping users retrieve it through search. They don't actively organize knowledge, identify relationships between ideas, or help users build upon what they have already learned. Likewise, AI chatbots are excellent at answering questions but generally lack a persistent understanding of a user's personal knowledge base.

Second Brain addresses this problem by transforming scattered information into an evolving, interconnected knowledge system. Instead of simply storing information, it reads, organizes, updates, and connects knowledge automatically, allowing users to make better use of everything they save.

### Use Cases

* **Students** – Build a long-term knowledge base from lecture notes, research papers, and study material while automatically connecting related concepts.
* **Researchers** – Organize papers, discover relationships between topics, and retrieve relevant information using semantic search instead of exact keywords.
* **Developers** – Store documentation, tutorials, code snippets, and technical articles in a system that understands how they relate to one another.
* **Content Creators & Writers** – Maintain a searchable repository of ideas, references, and inspiration that can be recalled naturally during the writing process.
* **Lifelong Learners** – Continuously capture and organize knowledge from books, videos, articles, and online courses without letting valuable information become forgotten.
* **Professionals** – Build a personalized AI assistant that understands company documentation, project notes, and work-related knowledge to provide contextual assistance.

### How It Improves Existing Workflows

* Eliminates information hoarding by turning saved content into usable knowledge.
* Automatically updates and organizes notes instead of creating duplicate information.
* Retrieves information based on meaning using semantic search rather than exact keywords.
* Maintains long-term context by grounding responses in your personal knowledge base.
* Connects related ideas automatically, helping users discover relationships they may not have noticed themselves.
* Runs locally, ensuring privacy while giving users complete ownership of their data.
* Reduces the time spent searching through notes, allowing users to spend more time applying what they have learned.

The long-term vision is to evolve Second Brain from a terminal-based application into a fully featured web application and productivity platform. Rather than being just another note-taking app or chatbot, it aims to become a modern AI-powered productivity tool that actively helps users think, learn, and manage knowledge. The goal is to provide an intuitive, polished user experience through a dedicated web interface while preserving the powerful AI capabilities running behind the scenes. Ultimately, Second Brain is intended to become a personal AI system that continuously grows with its user, making knowledge management as seamless and intelligent as possible.
I have also written an article why such information management systems are necessary-

**Challenges we ran into**

## Challenges I Ran Into

Building Second Brain presented a number of interesting technical challenges, especially because the project combines LLMs, semantic search, and knowledge management into a single system.

One of the biggest challenges was designing a workflow where the AI **updates existing knowledge instead of repeatedly creating new notes**. Simply asking an LLM to summarize content wasn't enough; I needed a reliable pipeline that could determine where new information belonged, maintain consistency across the knowledge base, and avoid duplication over time.

Another challenge was implementing **semantic search**. Traditional keyword search isn't sufficient for a knowledge management system because related concepts may use completely different wording. To solve this, I integrated sentence embeddings and vector similarity search so that information could be retrieved based on meaning rather than exact keywords. This significantly improved the relevance of retrieved context and laid the foundation for Retrieval-Augmented Generation (RAG).

Running everything **locally** also introduced its own set of challenges. Local LLMs have limited context windows, consume more system resources than cloud APIs, and require careful optimization to keep response times reasonable. I had to design the system so that only the most relevant pieces of information were retrieved and passed to the model instead of loading the entire knowledge base.

Keeping the project modular was another hurdle. As the project grew, adding new features directly into a single script quickly became difficult to maintain. Refactoring the code into separate components for ingestion, embeddings, retrieval, and querying made the codebase much easier to extend and debug.

Overall, these challenges shaped the architecture of the project and reinforced the importance of building systems that are modular, scalable, and capable of growing as new AI capabilities are added.

[Rehan Bangar](https://github.com/b1uerayy)

`2026-07-26`

---

### SolarWise
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/solarwise-b2e5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/amananshukumar/solarwise) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://solarwise-kappa.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/J5r1cT9NyBM?si=TLl3iwj6tXDBROye) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> SolarWise: Your Rooftop, Powered by AI

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square)

**Challenges we ran into**

## 🚩 Challenges & Solutions

### 1. CORS Issue (Render + Vercel)
**Challenge:** Production API requests failed due to CORS errors after deployment.  
**Solution:** Normalized allowed origins by removing trailing slashes before comparison, ensuring consistent origin matching.

### 2. Password Re-hashing on Admin Approval
**Challenge:** Promoted admins couldn't log in because passwords were unintentionally hashed again.  
**Solution:** Replaced `user.save()` with `findByIdAndUpdate()` to bypass the Mongoose `pre('save')` hook and preserve existing password hashes.

### 3. Hidden Form Validation
**Challenge:** Sign-in submission was blocked because a hidden "Full Name" field still had required validation.  
**Solution:** Applied conditional validation only during registration and cleared validation errors when switching tabs.

### 4. GPS to DISCOM Mapping
**Challenge:** Needed offline reverse-geocoding for Indian electricity tariff mapping without paid APIs.  
**Solution:** Implemented a custom **Haversine Distance Algorithm** to map user coordinates to the nearest supported city/state within a 75 km radius, with a fallback message for unsupported locations.

**The problem it solves**

# ☀️ SolarWise India — AI-Powered Rooftop Solar Intelligence & Subsidy Engine

## 💡 Problem Statement
Adopting rooftop solar in India is often complicated due to inaccurate cost estimates, subsidy confusion, manual roof inspections, and state-specific electricity tariffs. Property owners lack a fast, reliable way to assess installation costs, savings, ROI, and government incentives before investing.

## 🚀 Solution
SolarWise India streamlines the entire solar assessment process into an AI-powered experience, providing accurate rooftop analysis, financial insights, and subsidy calculations within seconds.

### ✨ Key Features

- **🤖 AI Rooftop Analysis:** Uses **Google Gemini 2.5 Flash Vision** to analyze satellite roof images, detect roof type, identify shade obstructions, and estimate usable installation area.

- **⚡ Energy Generation Forecast:** Predicts daily, monthly, and annual solar energy generation based on regional solar irradiance.

- **💰 Subsidy & ROI Calculator:** Calculates installation cost, **PM Surya Ghar** subsidy eligibility (up to **₹78,000**), net investment, monthly savings, and estimated payback period.

- **🗺️ Smart Location-Based Estimates:** Auto-detects the nearest supported Indian city using GPS and a custom Haversine algorithm to apply state-specific DISCOM tariffs and solar radiation data.

- **📈 25-Year Impact Dashboard:** Visualizes lifetime savings, ROI, CO₂ emissions reduced, coal savings, and tree-equivalent environmental benefits.

- **🛡️ Admin Management Portal:** Secure dashboard for managing electricity tariffs and approving administrator access requests.

**Best Use of Gemini API**

# 🤖 Google Gemini AI Integration

SolarWise India leverages **Google Gemini 2.5 Flash Vision** via the **@google/genai SDK** to perform AI-powered rooftop solar feasibility analysis from satellite imagery.

## 🔍 How It Works

1. User selects their rooftop location on the map.
2. Uploads a satellite image.
3. The backend sends the image to **Gemini Vision** for analysis.
4. AI returns structured data used directly in the solar calculator.

## 📊 AI Analysis Output

Gemini extracts key rooftop insights, including:

- 🏗️ Roof type (RCC, Tile, or Metal)
- 🌳 Shade obstruction level
- 📐 Estimated usable roof area
- ⚡ Maximum solar capacity (kW)
- 🎯 Solar feasibility score
- 📝 Key observations and AI summary

## ⚙️ Integration

The structured JSON response automatically populates the Solar Calculator, enabling accurate energy generation, subsidy, ROI, and feasibility calculations while displaying an AI-powered rooftop scorecard to the user.

**Best Use of MongoDB Atlas**

# 🍃 How SolarWise India Uses MongoDB

SolarWise India uses **MongoDB Atlas** with **Mongoose ORM** as its primary cloud database to securely manage users, solar reports, and regional DISCOM data.

## 🗄️ Database Collections

### 👤 `users`
- Stores user profiles and **Bcrypt-hashed** passwords.
- Supports **role-based access** (`user` / `admin`).
- Manages the **admin request & approval workflow**.

### 📊 `calculationresults`
- Saves complete solar assessment reports.
- Stores user inputs, AI analysis, energy estimates, subsidy calculations, ROI, and environmental impact metrics.
- Linked to users via **MongoDB ObjectId** for report history.

### 🌍 `statedatas`
- Maintains **state-wise DISCOM tariffs**, solar irradiance, and supported cities.
- Updated through an **Admin Dashboard** for accurate regional calculations.

## ⚙️ MongoDB Features

- 🔒 **Secure Authentication:** Passwords are automatically hashed using Mongoose middleware and Bcrypt.
- 📄 **Flexible Schema:** Efficiently stores complex AI analysis and financial calculation data.
- ☁️ **Scalable Cloud Database:** MongoDB Atlas provides reliable, scalable storage for users and solar reports.
- 🛡️ **Fault-Tolerant Design:** In-memory fallback ensures uninterrupted calculations during temporary database connectivity issues.

**Sustainability**

# 🌿 Sustainability Impact

## 🌍 Supporting Sustainable Development
SolarWise India accelerates rooftop solar adoption by combining AI, geospatial intelligence, and financial modeling to make clean energy accessible, affordable, and data-driven.

### 🌐 UN Sustainable Development Goals (SDGs)

| SDG | Contribution |
|------|--------------|
| **SDG 7 – Affordable & Clean Energy** | Simplifies solar adoption with AI-powered energy and subsidy estimates. |
| **SDG 11 – Sustainable Cities & Communities** | Promotes decentralized renewable energy across urban and rural India. |
| **SDG 13 – Climate Action** | Helps users measure and reduce their carbon footprint through solar adoption. |

## 📊 Environmental Impact

- 🌱 **CO₂ Reduction:** Estimates annual carbon emissions avoided through solar energy generation.
- ⚫ **Coal Savings:** Calculates thermal coal displaced by renewable electricity.
- 🌳 **Eco-Equivalencies:** Converts environmental impact into easy-to-understand metrics such as **trees planted** and **cars removed from the road**.

## 🇮🇳 Supporting India's Clean Energy Goals

- Aligns with **India's Net-Zero 2070** vision and renewable energy targets.
- Simplifies access to the **PM Surya Ghar: Muft Bijli Yojana**, including subsidy calculations of up to **₹78,000**.

## 💰 Economic Sustainability

- Reduces electricity bills by up to **90%**.
- Estimates a **2.5–3.5 year** payback period.
- Projects **25 years** of clean energy generation with strong long-term ROI.

Team **Code debuggers** -- [Aman Kumar](https://github.com/amananshukumar), [Akanksha Raj](https://github.com/Akanksharaj409), [Saloni Kumari](https://github.com/salonishri101)

`2026-07-26`

---

### SolarShare
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/solarshare-fed4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://solarshare-gq9c.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co)

> A Peer-to-Peer Solar Energy Trading Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Firestore](https://img.shields.io/badge/Firestore-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was understanding how peer-to-peer energy trading would work in practice. Initially, we assumed electricity could be transferred directly from one house to another. However, we learned that electricity always flows through the existing power grid and cannot be physically routed between two specific households.

To solve this, we redesigned our approach. Instead of transferring electricity directly, we implemented a virtual energy trading model. Using smart meter data, our platform records the amount of surplus energy exported by a producer and the amount consumed by a nearby buyer. Based on these verified readings, SolarShare handles buyer-seller matching, transaction records, and secure financial settlement while the existing grid continues to deliver the electricity.

We also faced challenges in designing a fair pricing mechanism. To address this, we introduced a marketplace model where producers earn more than the government feed-in tariff while consumers still pay less than the regular grid price, creating a win-win situation for both.

**The problem it solves**

Millions of rooftop solar owners generate surplus electricity that is either underutilized or sold back to the government at a low fixed tariff. At the same time, nearby households without solar panels purchase electricity from the grid at a much higher price.

This creates three major problems:

Solar producers earn less for the clean energy they generate.
Consumers pay higher electricity bills, even when renewable energy is available nearby.
Clean energy is not utilized efficiently, increasing dependence on the traditional power grid and causing higher transmission losses.

SolarShare solves this problem by creating a peer-to-peer energy marketplace where rooftop solar owners can securely trade their surplus electricity with nearby consumers using verified smart meter data.

This allows producers to earn more, consumers to save on electricity costs, and communities to make better use of locally generated renewable energy while reducing pressure on the power grid.

Team **Code Masters** -- [Aaditya .](https://github.com/aaditya2305-beep), [Shivi Goel](https://github.com/itsmehshivi123-dot), [Yash Sharma](https://github.com/ysharma2777-source), [Saniya Goel](https://github.com/Saniya-codes07)

`2026-07-25`

---

### DECODEX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/decodex-179f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ADITYAMITTAL1604/DECODEX) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://decodex-five.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1212876831?fl=ip&fe=ec) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co)

> AI Diagnostic Reading & Dyslexia Intervention Plat

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Whisper](https://img.shields.io/badge/Whisper-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square)

**The problem it solves**

Reading difficulties often go unnoticed until they begin affecting a child's confidence, academic performance, and future opportunities. Introducing Decodex—an AI-powered dyslexia screening and reading intervention platform designed to help students, teachers, and parents identify reading challenges early and take meaningful action.

Decodex combines speech recognition, AI-powered error analysis, personalized practice generation, and classroom analytics into a single intelligent ecosystem. Our mission is simple: make dyslexia detection faster, more accessible, and more effective for every learner.

As users enter the platform, they are welcomed through a secure role-based authentication system designed for students, teachers, and parents. Each stakeholder receives a personalized experience while maintaining privacy, security, and controlled access to learning data.

Once logged in, students arrive at their personalized dashboard. Here they can track their reading health score, monitor progress, view achievements, and access AI-generated learning recommendations tailored specifically to their reading profile. Every interaction helps the platform better understand the learner and adapt accordingly.

To begin an assessment, the student selects a reading passage. These carefully designed exercises evaluate reading fluency, pronunciation accuracy, decoding ability, and overall literacy development. The student then reads the passage aloud while Decodex records the audio in real time.

Behind the scenes, the recording is securely processed through our AI pipeline. Using advanced speech recognition and sequence-alignment algorithms, Decodex compares the spoken response against the original passage to identify substitutions, omissions, insertions, mispronunciations, and other reading difficulties with high precision.

Within seconds, the student receives a comprehensive reading report. The platform evaluates reading speed, accuracy, fluency, and overall performance while visually highlighting individual errors. Each mistake is categorized using dyslexia-focused reading patterns inspired by evidence-based literacy intervention frameworks, helping uncover the root causes behind reading struggles.

Based on these results, Decodex automatically generates a personalized learning pathway. Instead of assigning generic exercises, the platform creates targeted interventions designed specifically around the student's weaknesses. This ensures that every learner receives support tailored to their unique reading needs.

The identified weaknesses are then transformed into focused practice activities. Students can revisit challenging words, understand phonetic patterns, practice pronunciation, and strengthen decoding skills through structured exercises. This approach turns assessment into immediate intervention, enabling continuous improvement after every session.

Because Decodex works with children's educational data, parental consent and verification are built directly into the platform. Parents can securely authorize participation and remain actively involved in their child's learning journey while ensuring transparency and responsible data usage.

Parents also gain access to detailed progress dashboards where they can monitor reading development, identify strengths and improvement areas, review assessment history, and receive actionable recommendations. Rather than discovering issues after significant academic impact, parents receive early insights that enable timely support.

For educators, Decodex provides powerful classroom analytics. Teachers can instantly identify struggling readers, analyse class-wide literacy trends, monitor student progress, and uncover common learning gaps through intuitive visual dashboards. This significantly reduces manual analysis and allows educators to focus on intervention rather than administration.

The platform also generates AI-assisted screening insights that help teachers prioritise support where it is needed most. By transforming reading assessments into actionable intelligence, Decodex enables data-driven educational decisions at both the individual and classroom levels.

Decodex is more than a reading assessment tool. It is a complete AI-powered ecosystem that combines speech processing, intelligent screening, personalised intervention, parental engagement, and classroom analytics to ensure that every child receives the support they need to become a confident reader.

Because every child deserves to be understood, every reading challenge deserves early attention, and every learner deserves the opportunity to succeed.

Decodex — Understanding How Every Child Reads, Powered by AI.

**Challenges we ran into**

Registration was failing in production with a generic 'Invalid URL' error. We traced it through the frontend's URL-construction logic, then to a Postgres connection string that had unencoded special characters in the password, then to an IPv6-only hostname our host couldn't route to, and finally to a build step that wasn't copying our SQL schema files into the compiled output. Four distinct root causes stacked on top of each other — We diagnosed each one by reading actual server logs rather than guessing.

Team **TeraBytes** -- [Aditya Mittal](https://github.com/ADITYAMITTAL1604), [Ashmeet Singh](https://github.com/Singh4Ashmeet)

`2026-07-25`

---

### NullTrace
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nulltrace-2979) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AnubhavRoy007/NullTrace) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1hRfLBIvIkWoxeQdY6ZTCd7WpcOYZpIVi?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co)

> USE NULLTRACE, BECOME UNTRACEABLE

![Cryptography](https://img.shields.io/badge/Cryptography-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![Networking](https://img.shields.io/badge/Networking-333333?style=flat-square) ![HTML/CSS](https://img.shields.io/badge/HTML/CSS-333333?style=flat-square) ![Cybersecurity](https://img.shields.io/badge/Cybersecurity-333333?style=flat-square)

**The problem it solves**

Most of the internet users today are typically first generation internet users. The people who are well accustomed with the internet, can protect their privacy very well by using the norms of the internet. But ain't the privacy of those new people important ? 

So we designed a web extension that can secure the users internet searches , use VPN and Proxy Server, and use a local server to do the searches keeping them safe and secure.

**Challenges we ran into**

The first challenge i ran into was the problem statement. Thinking that the problem was small but even none cared to solve it. 
Second thing was upgrades most probably. Cause the entire project can be made in less than 10 hours but we need something more to add on.

Team **VOID_Walkers** -- [Soumyajit Dutta](https://github.com/BO-Saber), [Anubhav Roy](https://github.com/AnubhavRoy007), [Ritam Das](https://github.com/rdx-exe)

`2026-07-12`

---

### EcoLint
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecolint-6e00) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AnitSarkar123/EcoLint/tree/master) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1HVcZWq0hZsGRHP-SXjoJSNInvavmgFQ5/edit?usp=drivesdk&ouid=117033107470314773838&rtpof=true&sd=true) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/f2c4f7248dde480da06d0703400c99e9) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co)

> #codecarbon

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

# EcoLint 🍃

**AI-Powered FinOps Optimizer, Security Scanner, & VS Code Extension**

EcoLint is a comprehensive suite of tools designed to drastically reduce the computational footprint of your code. By acting as an advanced FinOps engine, it intelligently analyzes your source code to optimize performance (speed, RAM, CPU cycles), calculate carbon and cost savings, and apply automated cybersecurity patches.

The EcoLint project is divided into two primary interfaces:
1. **The VS Code Extension** (`/ecolint` & `/backend`)
2. **The Terminal CLI Tool** (`/ecolint-cli`)

---

## 💻 1. EcoLint for VS Code

The EcoLint VS Code extension brings our AI-powered code analysis, benchmarking, and optimization directly into your IDE. It communicates with a dedicated backend language server to provide real-time suggestions and automated refactoring.

### ✨ Extension Features
- **Analyze (`ecolint.analyze`)**: Analyzes the current code for performance bottlenecks and structural issues.
- **Benchmark (`ecolint.benchmark`)**: Runs simulated performance benchmarks on the active file.
- **Optimize (`ecolint.optimize`)**: Automatically optimizes the selected code inline.
- **Generate Pull Request (`ecolint.generatePullRequest`)**: Generates a summary PR containing the analysis results and optimization justifications.
- **Interactive UI**: Integrates directly into the VS Code Activity Bar with dedicated views for *Analysis Results*, *Benchmarks*, and *Optimizations*.

### 🛠️ Extension Setup
The VS Code extension requires the backend server to be running:
1. **Start the Backend:**
   ```bash
   cd EcoLint/backend
   npm install
   npm run start # (or equivalent dev script)
   ```
2. **Install the Extension:**
   ```bash
   cd EcoLint/ecolint
   npm install
   # Press F5 in VS Code to launch the Extension Development Host
   ```
*(Note: Ensure `ecolint.apiEndpoint` in your VS Code settings points to your running backend).*

---

## 🚀 2. EcoLint CLI

The EcoLint CLI is a lightweight, terminal-based alternative for fast, pipeline-friendly optimizations.

### ✨ CLI Features
- **🧠 Multi-Mode AI Optimization:**
  - **Maximum Performance**: Strips formatting and readability to compress variables and maximize raw computational speed. *(C/C++ Aware: Replaces heavy includes with lightweight forward declarations).*
  - **Balanced Production**: Achieves high performance while adhering strictly to clean architectural principles.
  - **Educational Mode**: Provides a JSON-formatted technical breakdown explaining the complexity shifts (e.g., $O(N^2) \rightarrow O(N)$).
- **🔒 Intelligent Security Scanner (SOLID Design):** Scans entire files for severe vulnerabilities (SQL Injections, XSS) and offers 1-click automated security patches.
- **📊 Eco Metrics Telemetry:** Simulates the real-world impact of your code optimizations (Latency, RAM, Carbon Reduction, Cost Savings).
- **💬 Dynamic Custom Directives:** Override the engine with natural language rules (e.g., *"Do not remove comments"*).

### 🛠️ CLI Setup & Usage
1. **Installation:**
   ```bash
   cd EcoLint/ecolint-cli
   npm install
   ```
2. **Configuration:** Add your AI provider API Key to `ecolint-cli/.env`:
   ```env
   NVIDIA_API_KEY=your_api_key_here
   ```
3. **Usage:**
   ```bash
   npm run build
   
   # Optimize and secure a specific file
   npm start -- --file ../test.c
   
   # Optimize a specific line range
   npm start -- --file ../test.c --lines 10-25
   ```

---

## 📚 Documentation
For more in-depth architectural details, API documentation, and contribution guidelines, please refer to the `/docs` directory.

## 🧪 Testing the Pipeline
You can test the core AI engine using the provided test files at the root of the repository:
- **`vulnerable_test.py`**: Contains `O(N^2)` loops and glaring security flaws (Hardcoded Secrets & SQL Injection). Tests both the FinOps optimizer and the Security Scanner.
- **`test.c`**: Contains standard C code. Tests the C/C++ specific include optimizations.

**Challenges we ran into**

Here are the major technical problems and roadblocks we encountered (and successfully solved!) while building the EcoLint project:

1. The AST web-tree-sitter Module Crash
The Problem: When we first tried to implement Abstract Syntax Tree (AST) parsing to deeply analyze code structure, we hit a hard crash: SyntaxError: The requested module 'web-tree-sitter' does not provide an export named 'default'.
The Solution: This happened because our project uses modern ESM (ECMAScript Modules, type: "module"), but the library was built for older CommonJS environments. Since it blocked the build, we pivoted, ripped out the AST logic, and shifted our focus entirely to LLM-based parsing and optimization instead.
2. The AI Ignoring the "Don't Remove Comments" Rule
The Problem: You passed a custom directive saying "don't remove comments", but the AI kept deleting them anyway.
The Solution: The underlying Maximum Performance system prompt was so aggressive ("Ignore code readability, documentation... at all costs") that it overpowered your custom instruction. We solved this by wrapping your custom instructions in a CRITICAL USER DIRECTIVE block, explicitly telling the AI that your instructions strictly override its default system behavior.
3. DeepSeek Minifying and Squashing Code
The Problem: When you switched to the DeepSeek AI model and ran it on test.c, it output the code as a giant, unreadable block of text squashed onto a single line.
The Solution: The AI took our instruction to "optimize for token constraints at all costs" far too literally and deleted all spaces and line breaks to save tokens. I updated the system prompt to explicitly command it: "CRITICAL: You must preserve standard code formatting, indentation, and line breaks. Do not minify or squash the code."
4. Git Submodule & Push Failures
The Problem: When you tried to push the code to GitHub, Git threw warnings about an "embedded git repository" and later failed with fatal: 'ecolint_cli' does not appear to be a git repository.
The Solution: Because ecolint-cli had its own hidden .git folder inside it, Git treated it as a detached submodule, meaning it wasn't actually saving your files to the main EcoLint repo. We solved this by deleting the inner .git folder, clearing the cache, and re-adding it so the main repository could properly track all your code.
5. Architectural Bloat (SOLID Principles)
The Problem: When you asked to add a full-file Security Vulnerability Scanner on top of the FinOps optimizer, the main AI engine and orchestration file were at risk of becoming a massive, unmaintainable "spaghetti" script.
The Solution: We applied SOLID principles (specifically the Single Responsibility Principle) by entirely separating the cybersecurity logic into a brand new securityController.ts. This kept the optimization engine fast and clean, while allowing the security scanner to run as an independent layer just before saving the file.

Team **BlitzHacker** -- [Anit Sarkar](https://github.com/AnitSarkar123), [Debaditya Saha](https://github.com/NeatSleep), [Roushan Singh](https://github.com/roushan-code), [Muberser Hossain](https://github.com/Mubashir2611)

`2026-07-12`

---

### ResQMesh
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resqmesh-fb43) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/madhesh935/vibathon) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/tIi0y2dHLJ4?si=jAkez4f0M1r_Ko3a) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20Vibeathon-0052CC?style=flat-square)](https://microcraft-vibeathon.devfolio.co)

> Every Second Counts Every Connection Saves Lives.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

**The Problem ResQMesh Solves**

Natural disasters such as **floods, earthquakes, cyclones, landslides, wildfires, and building collapses** often destroy critical communication infrastructure, including mobile towers, internet networks, and power systems. During the **Golden Hour**, when rapid communication is essential for saving lives, victims are frequently unable to contact emergency services, while rescue teams lose access to real-time information required for effective decision-making. Most existing disaster management systems depend on **internet connectivity, cloud services, and centralized infrastructure**, making them unreliable when they are needed the most.

### Key Challenges

### 1. Communication Infrastructure Failure

Damaged communication networks prevent victims from sending SOS alerts and sharing their location, leaving affected communities isolated and disrupting coordination between victims and rescue teams.

### 2. Delayed Emergency Response

Without timely and accurate information, rescue teams cannot quickly identify critical incidents or locate victims. Manual verification of emergency reports increases response time and reduces the chances of successful rescue.

### 3. Information Overload

Emergency operation centers receive large volumes of information from phone calls, GPS data, CCTV feeds, drones, and citizen reports. Processing this unstructured data manually makes it difficult to identify genuine emergencies and prioritize rescue efforts.

### 4. Lack of Intelligent Prioritization

Most existing systems process emergency requests in the order they are received rather than by severity. As a result, life-threatening emergencies may not receive immediate attention, leading to inefficient resource allocation.

### 5. Poor Situational Awareness

Rescue teams often lack a complete view of victim locations, disaster severity, available resources, evacuation routes, and team positions, making rescue planning slower and less effective.

### 6. Dependence on Cloud Infrastructure

Most AI-enabled emergency response platforms require internet connectivity and cloud services. During disasters, these services often become unavailable, causing critical decision-support systems to fail.

### 7. High Deployment Cost

Traditional emergency communication solutions rely on specialized hardware and dedicated infrastructure, making them expensive to deploy and difficult to scale, especially in remote or resource-constrained regions.

---

# Solution – ResQMesh

ResQMesh is an **offline-first, AI-powered decentralized disaster response platform** designed to maintain communication and rescue coordination even when traditional infrastructure fails. It transforms **smartphones, Raspberry Pi relay nodes, and laptops** into a **self-healing mesh communication network** that enables reliable device-to-device communication using **Wi-Fi Direct, Bluetooth, and LoRa**, eliminating the need for internet or cellular connectivity.

Victims can send **SOS alerts, emergency messages, GPS locations, and voice inputs**, which are securely relayed across nearby devices until they reach the **Rescue Command Center**. A lightweight **Edge AI Triage Engine**, powered by **Qwen 2.5 1.5B running locally through Ollama**, analyzes emergency requests, classifies incidents into **Critical, High, Medium, or Low** priority levels, and provides first-aid guidance using a local **RAG knowledge base** without relying on cloud services.

The **Rescue Command Dashboard** provides real-time incident monitoring, live victim tracking, AI-assisted priority ranking, resource allocation, disaster mapping, and rescue team coordination. Its **self-healing mesh architecture** automatically reroutes messages through alternative devices whenever a network node fails, ensuring uninterrupted communication throughout the disaster zone.

---

# Key Benefits

* Enables emergency communication without internet or cellular networks.
* Uses affordable existing devices such as smartphones, Raspberry Pi, and laptops.
* AI-powered emergency prioritization for faster rescue decisions.
* Provides offline first-aid and disaster guidance through local AI.
* Improves situational awareness with real-time dashboards and live maps.
* Self-healing mesh network ensures reliable communication during infrastructure failure.
* Cost-effective, scalable, and suitable for deployment from rural communities to smart cities.

**Challenges we ran into**

# Challenges Faced

Building **ResQMesh** involved several technical and architectural challenges, especially because the platform is designed to operate **without internet connectivity** while still providing intelligent disaster response.

## 1. Designing a Reliable Offline Communication Network

One of the biggest challenges was enabling communication when conventional infrastructure is unavailable. Since internet and cellular networks cannot be assumed during disasters, we had to design an offline communication workflow using **Wi-Fi Direct, Bluetooth, and LoRa**. We addressed this by adopting a **mesh networking architecture**, allowing nearby devices to relay messages until they reach the rescue command center.

## 2. Running AI on Resource-Constrained Devices

Running an AI model on edge devices such as Raspberry Pi is challenging due to limited CPU power and memory. To overcome this, we selected a lightweight **Qwen 2.5 1.5B** model running locally through **Ollama** and combined it with a **Retrieval-Augmented Generation (RAG)** knowledge base. This reduced computational overhead while still providing reliable emergency triage and first-aid guidance.

## 3. Reliable Message Delivery

In a disaster environment, devices may move out of range or disconnect unexpectedly. Ensuring that emergency messages are not lost required implementing a **store-and-forward mechanism**, local buffering, acknowledgements, and automatic retries. The mesh network also supports **self-healing**, automatically rerouting messages through alternative nodes when a device becomes unavailable.

## 4. Balancing Performance and Accuracy

We needed fast AI responses without compromising the quality of emergency recommendations. Instead of using a large cloud-based model, we optimized inference by combining a compact local LLM with curated emergency knowledge through RAG, reducing latency while maintaining accurate responses.

## 5. Integrating Multiple Technologies

The project combines a modern web application, backend services, real-time communication, edge AI, local databases, and multiple communication technologies. Ensuring smooth integration between the victim application, relay nodes, AI engine, and rescue dashboard required careful API design, modular architecture, and extensive end-to-end testing.

## 6. Building a Scalable Architecture

Another challenge was designing a system that could work for both a small village and a large urban disaster. We addressed this by using a modular, decentralized architecture where additional smartphones, Raspberry Pi relay nodes, and command devices can join the mesh network without major configuration changes.

---

### Outcome

By addressing these challenges, we built a disaster-response platform that is **offline-first, AI-powered, scalable, fault-tolerant, and deployable using affordable hardware**. The experience reinforced the importance of designing resilient systems that continue operating even when traditional communication infrastructure fails.

[MADHESH B](https://github.com/madhesh935)

`2026-06-30`

---

### Recon
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/recon-038c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NAS-24/devlynix-buildathon-vuln-scanner/tree/main) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://devlynix-buildathon-v-git-22590e-naman-sinhas-projects-e2a7b18d.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=I7PluyvVpVw) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> Identify. Remediate. Deploy.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

## Why Recon Audit?

Most security tools are built for experts. They're often slow, expensive, and generate massive reports full of technical jargon that require hours of research to understand.

**Recon Audit** is designed to make website security simple, fast, and actionable.

###  No More Guessing Games

Instead of waiting hours for a lengthy scan, simply enter your website URL and get a **real-time security health score**.

Think of it as a quick health check-up for your website.

### Actionable Fixes, Not Just Warnings

Most security scanners only tell you what's wrong.

Recon Audit goes a step further by using **AI-powered recommendations** to show you exactly how to fix issues—often with a simple one-line configuration change.

Spend less time researching and more time patching vulnerabilities.

###  Instant Verification

Fixed a security issue but unsure whether it actually worked?

With our **Verify Fix** feature, you can instantly re-check specific vulnerabilities without running a full scan again.

Just click **Verify**, wait a second, and watch the status change to **PASS**.

### Security for Everyone

Whether you're:

- A student building a hackathon project
- A developer managing a startup website
- A small business owner maintaining an online presence

Recon Audit helps you identify and fix security issues quickly, so you can focus on building great products instead of chasing vulnerabilities.

**Challenges we ran into**

**Infinite Fetch Loop** (ERR_INSUFFICIENT_RESOURCES): The report page spammed API requests on client-side re-renders, crashing the network. Fixed by moving data fetching to a native Next.js Server Component.

**Client/Server Directive Conflict**: Putting 'use client' on a page with top-level async data fetching broke the Next.js runtime. Fixed by removing it from the parent and isolating interactivity in the child BentoGrid.

**Fragile Live Event Stream: **A single scanner crash or timeout would kill the entire active stream_scan process. Fixed by wrapping individual scanners in try/except blocks to gracefully skip errors.

**Artificial Stream Throttling:** Leftover asyncio.sleep delays in the backend generator threatened production timeouts. Fixed by removing them so results stream instantly.

**Database Schema Rejection:** MongoDB inserts failed because the database strictly required an explicitly structured radar_scores object. Fixed by writing a utility to map and weigh category data dynamically before saving.

[Naman Sinha](https://github.com/NAS-24)

`2026-06-15`

---

### Buildfolio
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/proofforge-3148) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://buildfolio-tech.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1201337417?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> Where code becomes credibility

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was working with different GitHub profiles, since every developer has a unique set of repositories, technologies, and activity levels. We also spent time making sure the portfolio looked good on both desktop and mobile devices, generating clean PDF exports without formatting issues, and keeping all themes visually consistent while providing a smooth user experience.

**The problem it solves**

Many developers struggle to create and maintain professional portfolios. Traditional portfolios require constant manual updates and often become outdated, failing to reflect a developer's latest skills and projects. Buildfolio solves this by automatically generating a portfolio from GitHub activity, ensuring that a developer's work is always represented accurately and professionally.

Team **Team Vertex** -- [Bhargav ram](https://github.com/bhargavram-06), [Ankitha Sahukari](https://github.com/ankitha102), [KEERTHILATIKA YELURI](https://github.com/keerthilathika777-creator)

`2026-06-15`

---

### LifeOS- AI-Powered Visual Second Brain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lifeos-aipowered-visual-second-brain-8c51) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ananthakumarbCSE/lifeOS) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://life-os-hia8.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=mqxfSexk7YU) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> From brain dumps to roadmaps, powered by AI.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

###  The Problem It Solves

Traditional productivity tools usually force users into linear lists or rigid calendars, which fall short in several key areas:
1. **Chaotic Raw Ideas:** When users have a "brain dump" of aspirations, projects, and tasks, translating them into concrete steps is a manual, cognitively demanding task.
2. **Missing Dependency Context:** Normal todo lists do not show connections. You cannot easily visualize that *Task A* (e.g., "Build Backend API") cannot start until *Task B* (e.g., "Design Database Schema") is completed.
3. **Planning Conflicts & Overload:** People regularly set overlapping events, schedule tasks that exceed their actual daily working limits, or set deadlines too close together without realizing it.
4. **Passive Learning Material:** Educational resources (like YouTube tutorials or lectures) require users to pause, take notes, and manually create tasks to actually apply what they learned.

#### How **LifeOS** Solves This:
*   **Natural Language Brain Dump:** Users can dump unstructured thoughts, notes, and raw ambitions. The built-in **Gemini AI** engine automatically structures them into high-level goals and granular, actionable tasks.
*   **Interactive React Flow Canvas:** Visualizes tasks, goals, projects, and events as custom draggable nodes. Relationships and dependencies are mapped dynamically through visual edges.
*   **Hybrid Conflict Detection:** A dual-engine analyzer flags planning conflicts:
    *   *Deterministic Rules:* Checks for overlapping events, tasks exceeding daily configured work hours, and deadlines less than 48 hours apart.
    *   *AI Cognitive Analysis:* Gemini flags logical prerequisites (e.g., scheduling a complex task before its prerequisite learning roadmap is complete).
*   **YouTube Action Extractor:** Converts any learning tutorial URL into a step-by-step interactive roadmap directly on the canvas by parsing the transcript with Gemini.
*   **Automated Weekly Planner:** Respects daily work hour configurations and maps out a balanced 7-day schedule automatically.

**Challenges we ran into**

### Challenges We Ran Into

#### 1. React Flow Performance and State Sync Lag
*   **The Hurdle:** Saving the canvas state to MongoDB Atlas on every node drag, connection, or modification caused visual lag, UI freezing, and excessive API calls.
*   **How We Resolved It:** We implemented an **automatic debounced state-saving system (500ms)** using **Zustand** and **Axios**. Dragging nodes updates the frontend UI instantly in local state, while network synchronization requests are debounced to ensure we only write to MongoDB when the user stops interacting.

#### 2. Unreliable AI Mutations & Database Pollution
*   **The Hurdle:** Directly inserting AI-generated items (from Brain Dumps or YouTube roadmaps) into the live production database was risky. Formatting errors, hallucinations, or misaligned dependencies could corrupt the user's canvas.
*   **How We Resolved It:** We created a **Staging Lifecycle (Pending ➡️ Approved)**. All AI analysis outputs are first saved in a temporary `AIAnalysis` schema. The client renders this as a staging preview, giving the user the ability to review, edit, or reject the nodes before committing them to the live visual board.

#### 3. Concurrent Auth Token Refresh Race Conditions
*   **The Hurdle:** Using short-lived (15m) JWT access tokens in memory and secure (7d) HttpOnly refresh cookies caused race conditions. When a page loaded with multiple concurrent API calls, multiple refresh requests were triggered simultaneously, causing token rotation invalidation errors.
*   **How We Resolved It:** We built a centralized queue within our Axios interceptors (`api-client.ts`). When an access token expires, the interceptor pauses outgoing requests, triggers a single refresh token request, updates the token, and then flushes the queued requests with the new token.

#### 4. Hard Rate Limits Hindering Local Development
*   **The Hurdle:** Implementing strict API and AI rate-limiters on the backend is crucial for production security and cost control, but it frequently blocked the team during rapid feature testing.
*   **How We Resolved It:** We created environment-aware middleware on the Express server that dynamically bypasses rate-limiting blocks whenever `NODE_ENV === 'development'`, providing an uninterrupted local development experience.

Team **Innovex** -- [Anantha Kumar](https://github.com/ananthakumarbCSE), [Ananya Sridhar](https://github.com/ananyasridharcse2024)

`2026-06-14`

---

### Forgefolio
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/forgefolio-804c) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://forgefolio.lovable.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/M6LWcGReDmg?si=oO0-rD6pQ3-I1N50) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> “Turn GitHub into a job-ready portfolio in seconds

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

**Problem It Solves**

Developers often have strong GitHub projects, but they are poorly presented and hard for recruiters to evaluate quickly. This leads to good work being overlooked.

ForgeFolio fixes this by converting GitHub repositories into a clean, structured portfolio with clear project descriptions, skills, and highlights—removing the need to manually design or organize a portfolio.

**Use Cases**

- Job and internship applications with a professional portfolio.
- Quick portfolio creation without frontend/design effort.
- Better personal branding by showcasing projects clearly.
- Making GitHub work readable and recruiter-friendly.

**Challenges we ran into**

**GitHub API Rate Limits**

Repeated profile fetches quickly hit GitHub’s rate limit (403). This broke data loading during testing.
Fix: reduced API calls, added basic caching, and batched requests.

**Inconsistent GitHub Data**

Some profiles lacked fields like bio, pinned repos, or language stats, causing UI errors.
Fix: added null checks and fallback UI states.

**Slow Rendering for Large Profiles**

Users with many repos caused noticeable lag due to heavy client-side processing.
Fix: limited repo count, moved processing to backend, and reduced recomputation.

[Pooja Borole](https://github.com/Po952)

`2026-06-15`

---

### synaptic
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/synaptic-cfd4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://synaptic-eight.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/632e6c50c5bb4fac981e891e321c9079) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> Where thoughts become structured

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Advanced Encryption Standard (AES)](https://img.shields.io/badge/Advanced%20Encryption%20Standard%20(AES)-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Anthropic Claude API](https://img.shields.io/badge/Anthropic%20Claude%20API-333333?style=flat-square) ![React Flow (@xyflow/react)](https://img.shields.io/badge/React%20Flow%20(@xyflow/react)-333333?style=flat-square)

**The problem it solves**

Modern students and developers are drowning in chaos — assignments, side projects, learning goals, deadlines, and random ideas all living in different apps, notes, and their heads.

**Synaptic** is an infinite AI-powered visual canvas that turns mental chaos into structured clarity:

-  **Smart Brain-Dump** — type everything on your mind in one go. AI (Claude Sonnet) instantly categorizes each task into the **Eisenhower Matrix** (Do Now / Schedule / Delegate / Eliminate) and places them as visual nodes on your canvas
-  **YouTube Action-Extractor** — paste any tutorial or course URL and Synaptic extracts the transcript and converts it into a **connected roadmap of actionable steps** on the canvas
-  **Visual Conflict Detection** — automatically detects when two deadlines are within 24 hours of each other and flags both nodes with a warning
-  **Infinite Canvas** — drag, connect, zoom, and organize nodes freely. Everything persists across sessions via localStorage
-  **Silent Coder aesthetic** — deep charcoal + forest green, bento-grid inspired layout built for developers

**Challenges we ran into**

## 1. React Flow SSR Conflict
Next.js tried to server-render React Flow, which uses browser-only APIs and crashed the build. Fixed it by dynamically importing the Canvas component with `ssr: false`.

## 2. YouTube Transcript Extraction Without an API Key
YouTube's official Data API requires OAuth and quota limits. We reverse-engineered the captionTracks field embedded in YouTube's HTML response to fetch raw caption XML directly — no API key needed.

## 3. Claude API JSON Parsing
Claude occasionally wraps JSON responses in markdown code fences (json ). I added a regex fallback to strip fences before parsing, making it robust in all cases.

## 4. TypeScript Strict Mode vs React Flow's Node Types
React Flow's NodeProps types conflict with Zustand's persisted state shape under strict TypeScript. Resolved by loosening the node data type to any for render components while keeping strict types in the store layer.

## 5. Deadline Conflict Detection Across Dynamic State
Running conflict detection synchronously after every node add caused stale state reads. Fixed with a `setTimeout(() => detectConflicts(), 100)` pattern to let Zustand flush state before scanning.

[sadhana s](https://github.com/sadh-ana)

`2026-06-15`

---

### Visual Second Brain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/visual-second-brain-4577) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mittai17/SudoShift) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://spadevity.tech/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/S7sbuJj84gc) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> Think. Plan. Execute. All in One Brain.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Socket.IO](https://img.shields.io/badge/Socket.IO-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square) ![Reactflow](https://img.shields.io/badge/Reactflow-333333?style=flat-square)

**The problem it solves**

We noticed that most people use multiple tools for different purposes — one app for notes, another for tasks, another for project management, another for learning resources, and so on. This often makes information scattered and difficult to manage.

With Visual Second Brain, we wanted to bring everything together into a single visual workspace. Users can plan goals, manage projects, track habits, organize resources, create tasks, schedule events, and collaborate with others without constantly switching between applications.

The platform helps users turn ideas into action by visually connecting information and workflows. Whether someone is preparing for an exam, managing a startup, planning a hackathon project, or organizing personal goals, they can do everything inside one collaborative canvas. AI-powered features further help by generating roadmaps, summaries, learning materials, and workflow suggestions, making the overall process faster and more organized.

**Challenges we ran into**

One of the biggest challenges was designing a flexible node system. Since our platform contains many different node types such as Goals, Projects, Tasks, Habits, Resources, Milestones, Events, Formulas, and Integrations, it was difficult to make them all work consistently while still keeping the interface simple for users.

Another challenge was implementing real-time collaboration. Multiple users can edit the same canvas simultaneously, so we had to carefully handle synchronization and state updates to ensure everyone sees changes instantly without conflicts.

Integrating external services such as GitHub, Notion, Jira, Slack, Discord, Google Sheets, and other platforms was also challenging because each service has different APIs, authentication methods, and data formats. We solved this by creating reusable integration patterns that made the system easier to extend.

We also spent considerable time improving how AI interacts with our node ecosystem. Instead of giving generic responses, we wanted the AI to understand the purpose of each node and generate structured workflows that users could directly build on the canvas. Achieving this required multiple iterations of prompt design and workflow planning logic.

Despite these challenges, overcoming them helped us create a more powerful and unique platform that combines knowledge management, productivity, collaboration, automation, and AI assistance into a single visual workspace.

Team **SudoShift** -- [Dinesh D](https://github.com/Dinesh-2007), [DHAARINI T](https://github.com/tdhaarini032), [Giridharan M](https://github.com/mittai-17)

`2026-06-15`

---

### Second Brain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/second-brain-31a8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Hotrodminers/SecondBrain) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://second-brain-nine-mocha.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/3siIhW-hSyQ) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> You tell us what to do. We'll tell you when

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Auth0](https://img.shields.io/badge/Auth0-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**The problem it solves**

Second Brain removes the organizing burden entirely. Instead of carefully filing tasks one by one, you just dump everything on your mind in plain language — deadlines, goals, worries, half-formed ideas — and the app does the structuring for you, in seconds.

1. From raw text to a prioritized board.
The moment you submit a brain dump, AI reads every line, extracts each distinct task, and places it on an infinite canvas sorted by the Eisenhower Matrix — separating what's urgent from what's important: Do Now, Schedule, Delegate, or Drop. No forms, no tagging, no dragging. Thoughts in, structure out. This instantly surfaces the trap most people fall into — living in "urgent" mode while the important-but-not-urgent work that builds their future gets ignored.

2. Automatic, reliable grouping.
Real life has themes, so related tasks (three health goals, everything tied to one project, all your coursework) are automatically clustered into colored groups — even across separate brain dumps and across quadrants. Crucially, this grouping is deterministic, not an AI guess: we combine the category the model assigns with a classic graph-theory algorithm (Union-Find) to build clean, non-overlapping groups every single time. That makes the experience dependable rather than flaky.

3. Dependencies you can see.
Grouping shows what belongs together; directional arrows show what to do first. The AI detects prerequisite relationships — "submit the application" after "get approval," "deploy" after "build" — and draws them automatically, so your board reflects the real order of operations, not just a list.

4. A second brain that builds on itself.
Thoughts don't arrive all at once, so neither does the board. Each new brain dump links into everything already on the canvas — new tasks join existing groups and connect to prior tasks — so your second brain grows and reorganizes itself over time instead of starting from scratch.

5. You stay in control.
The AI does the heavy lifting, but it's your brain: drag to create your own connections (groups recompute live), rename or delete tasks, and start fast with ready-made templates.

6. Beyond tasks — learning, too.
Drop in any YouTube tutorial link and the app extracts the transcript and turns it into a step-by-step roadmap — a connected chain of milestones laid right onto your canvas. A 40-minute video becomes a plan you can actually follow.

Under the hood, it's built on Next.js and React Flow, with secure authentication (email + OTP verification and Google sign-in), a PostgreSQL database, and a triple-fallback AI pipeline (Groq → Claude → Gemini) so it stays fast and never goes down.

The outcome: in seconds, a midnight mess of obligations becomes a calm, connected, prioritized map. You bring the chaos — Visual Second Brain brings the order.

**Challenges we ran into**

**Challenges We Ran Into**

Defining the AI schema was one of the earliest and most debated decisions. We had to figure out exactly what the model should be responsible for versus what the server should handle — whether classification logic lived in the prompt, in post-processing, or split between both. Getting the output shape right (quadrant labels, task labels, notes, relationships) took multiple iterations because an ambiguous schema meant the model would return inconsistent structures that broke the frontend unpredictably.

Managing multiple AI calls was another challenge. The brain dump and YouTube roadmap features both hit the Groq API, and we had to think carefully about what happens when one call is slow, times out, or returns malformed JSON. We added fallback handling so a failed API call wouldn't silently break the canvas, and structured the server responses so the frontend always got a predictable shape even in error cases.

The YouTube transcript issue was a significant blocker. Vercel's serverless functions run from shared IP ranges that YouTube actively blocks for transcript scraping, so our initial approach of reading transcripts directly failed completely in production even though it worked locally. We found a workaround using Supadata.ai as a middleware layer to fetch the transcript data, which got the YouTube roadmap feature working reliably on Vercel.

Designing the data schema for nodes and edges went through several revisions. We debated whether relationships between tasks should be inferred by the AI, computed algorithmically, or drawn manually by the user — and ended up building all three. The Union-Find algorithm groups related tasks into colored clusters by merging nodes that share a category or are connected by an edge, using path compression for efficiency. Topological sort informed how we ordered YouTube roadmap steps into a directed learning chain, ensuring the sequence was always valid and cycle-free before rendering edges.

React Flow had a steeper learning curve than expected. Custom node types, edge handling, state synchronization with `useNodesState` and `useEdgesState`, and the `onConnect` callback all had subtle behaviors that weren't obvious from the docs. Getting the canvas to feel smooth while also being reactive to AI responses arriving asynchronously required careful state management.

Vercel's continuous deployment actually became an asset during debugging. Every push to main triggered a fresh deployment, which meant we could test fixes in a real serverless environment quickly instead of guessing why something worked locally but failed in production — which was especially useful for catching the YouTube IP blocking issue and the localStorage key mismatch.

Keeping the canvas state consistent across sessions without a real-time database was trickier than expected. We used localStorage but ended up with two conflicting storage schemas during development — one using split keys and one using a unified key — which caused stale edges to persist across refreshes and took time to track down and migrate cleanly.

Team **Hotrodminers** -- [Rajat Upadhyay](https://github.com/HotrodminerJr), [Surabhi Agarwal](https://github.com/jewel-surabhi), [Darsh Verma](https://github.com/DarshEllisd)

`2026-06-15`

---

### Altair
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/altair-0347) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prince-predeep/altair67) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://altair67-three.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1201127839?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Decoding the Universe

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![HTML/CSS](https://img.shields.io/badge/HTML/CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**Challenges we ran into**

One of the biggest challenges was integrating multiple space-related features into a single cohesive platform while maintaining a consistent user experience. Altair combines real-time ISS tracking, AI-powered research tools, an interactive knowledge hub, sky visualization, gamification systems, and educational games, each with different data requirements and UI patterns.

Another challenge was working with external APIs and real-time data sources. Some APIs had rate limits, inconsistent responses, or missing data, which required us to implement fallback handling and optimize how data was fetched and displayed.

We also spent significant time refining the user interface to balance functionality with engagement. Since our goal was to make space exploration feel exciting and accessible, we iterated on layouts, visual design, and navigation multiple times to ensure users could easily move between educational content, tracking tools, AI features, and games.

Finally, coordinating development across multiple modules within a limited hackathon timeframe was a challenge. We addressed this by dividing responsibilities among team members, maintaining clear communication, and continuously integrating each module to ensure that all parts of Altair worked together as a unified platform.

**The problem it solves**

Space exploration data is often scattered across multiple platforms, making it difficult for students, enthusiasts, and casual users to discover, understand, and interact with information about space. Real-time events such as ISS passes, celestial phenomena, active missions, and astronomical discoveries often go unnoticed because they are presented in technical formats that are not easily accessible to the general public.

Altair solves this problem by bringing space exploration, education, and discovery into a single interactive platform. Users can learn through a structured knowledge hub, track live space activity such as the International Space Station, explore the night sky, access AI-powered research tools, and engage with educational games that make complex concepts easier to understand.

By combining real-time space data, gamification, visualization, and AI-assisted learning, Altair transforms space from something distant and difficult to understand into an experience that is interactive, engaging, and accessible to everyone.

Team **Bankai** -- Sadwik G, Kavin Kadmiel, prince predeep, Aryan Nalla

`2026-06-14`

---

### ExecutiveOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/executiveos-bb2d) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://theexecutiveos.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/GTJmVnBqVEM) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co)

> Where Business Decisions Become Data-Driven.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Package JSON](https://img.shields.io/badge/Package%20JSON-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

## Challenges We Ran Into

### 1. Orchestrating Multiple AI Agents

One of the biggest challenges was coordinating multiple AI agents to behave like a real executive team rather than a collection of independent chatbots.

Initially, agents would produce overlapping recommendations, contradict one another, or lose context from previous discussions. This reduced the realism and usefulness of the boardroom simulation.

**How we solved it:**
- Designed a structured agent workflow with clearly defined responsibilities.
- Implemented a shared context layer so every agent had access to the same business information.
- Added a moderation and synthesis stage that consolidated viewpoints into a unified executive recommendation.

**The problem it solves**

ExecutiveOS is an AI-powered digital executive advisor designed to help entrepreneurs, startups, business owners, consultants, and decision-makers evaluate ideas, analyze opportunities, identify risks, and make smarter business decisions faster.

Instead of relying on fragmented research, expensive consultants, or guesswork, ExecutiveOS simulates the expertise of an entire executive team—bringing together strategic, financial, operational, market, and risk perspectives in one intelligent platform.

---

## What Can People Use It For?

### 🚀 Business Idea Validation
- Evaluate new business ideas before investing time and money.
- Identify strengths, weaknesses, opportunities, and risks.
- Receive structured feedback similar to an investor or advisory board review.

### 📊 Strategic Decision Making
- Compare multiple business strategies.
- Analyze expansion opportunities.
- Evaluate partnerships, acquisitions, or new product launches.

### 💰 Financial Planning
- Generate financial projections and forecasts.
- Assess profitability and growth potential.
- Identify potential financial risks before execution.

### 🎯 Market Research & Competitive Analysis
- Understand market opportunities.
- Analyze competitors and industry trends.
- Discover differentiation strategies and competitive advantages.

### ⚠️ Risk Assessment
- Identify operational, financial, market, and execution risks.
- Simulate worst-case and best-case scenarios.
- Improve preparedness before making critical decisions.

### 📈 Growth Planning
- Create actionable roadmaps for scaling businesses.
- Prioritize initiatives based on impact and feasibility.
- Receive strategic recommendations for sustainable growth.

### 🤝 Business Consulting & Advisory
- Serve as a 24/7 virtual advisory board.
- Help consultants and agencies accelerate client analysis.
- Provide executive-level insights without requiring expensive consulting engagements.

---

## How Does ExecutiveOS Make Existing Tasks Easier?

### Traditional Approach
A business owner often needs to:
- Conduct market research manually.
- Analyze competitors separately.
- Build financial models from scratch.
- Consult multiple experts.
- Consolidate information from numerous sources.

This process can take days or weeks.

### With ExecutiveOS
- Centralizes research, analysis, and strategic evaluation.
- Produces executive-level insights within minutes.
- Reduces repetitive research and manual analysis.
- Helps users focus on decision-making rather than information gathering.

---

## How Does It Make Decisions Safer?

### Risk-First Thinking
ExecutiveOS actively identifies:
- Financial risks
- Market risks
- Operational risks
- Execution challenges
- Competitive threats

### Multi-Perspective Evaluation
Instead of providing a single opinion, the platform evaluates decisions from multiple executive viewpoints, helping users uncover blind spots and challenge assumptions before acting.

### Scenario Simulation
Users can explore:
- Best-case outcomes
- Worst-case outcomes
- Potential bottlenecks
- Alternative strategies

This enables more informed and resilient decision-making.

---

## Key Benefits

- Faster business analysis
- Better-informed decisions
- Reduced research effort
- Earlier risk detection
- Executive-level strategic insights
- Scalable and accessible advisory support
- Improved confidence in business planning and execution

---

## Vision

ExecutiveOS aims to democratize high-quality business intelligence by making executive-level strategic guidance accessible to everyone—from solo entrepreneurs and small businesses to growing companies and enterprise teams.

Team **The Lumos League** -- Viswasainath Vijayakumar, [Sreeja Kotra](https://github.com/Sreejaavilla), [Varsha Ashok](https://github.com/varshaashok2104-art), [Raghav Aravind](https://github.com/hecker-go-brrr)

`2026-06-14`

---

### MOLE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mole-00e9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sarangchaudhari635-oss/MOLE_Nepal) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mole-nepal.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Hn-GVic1KFg?si=PJtM-ESjb1d272iJ) [![Built at](https://img.shields.io/badge/Built%20at-DeerHack%202026-0052CC?style=flat-square)](https://deerhack26.devfolio.co)

> Transforming Industrial Waste into Economic Value

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

In the traditional Linear Economy ("Take, Make, Waste"), industrial production faces critical bottlenecks:

    High Operational Cost: Factories pay enormous landfill tipping and waste disposal fees to discard secondary products and byproducts.
    Procurement Scarcity: Purchasing virgin raw materials is highly volatile, carbon-intensive, and expensive. Sourcing recycled materials is highly fragmented, rely on offline brokers, and suffers from a lack of quality control.
    Logistical Inefficiencies: Transporting waste over long distances is cost-prohibitive and contributes heavily to scope-3 emissions. Freight costs often kill the economics of recycling.
    Compliance & Audit Gaps: Companies struggle to track, compute, and report audit-ready ESG metrics (CO2 avoided, landfill diversion percentages, circularity indexes) required by regulators.

**Challenges we ran into**

The Netlify Deployment "White Screen" (Vite Assets Path & SPA Routing Redirects)
The Hurdle: After deploying the frontend code to Netlify, users were greeted with a blank white screen, and the browser console showed 404 Not Found errors for all compiled JS and CSS bundles.
The Cause: In 

vite.config.ts
, the base property was set to '/MOLE/' (likely optimized for a GitHub Pages project path). However, on Netlify, the application is deployed under the root domain, causing Vite to request assets from /MOLE/assets/... instead of /assets/.... Additionally, typing a route directly in the address bar (e.g., /app/dashboard) bypassed the single-page React router and returned a standard server-side 404.
The Fix:
Adjusted the base property in 

vite.config.ts
 to '/' to resolve assets from the root.
Configured Netlify's build variables directly inside 

netlify.toml
 and added a standard SPA fallback redirect rules block (/* to /index.html with a 200 status code) to let React Router handle all path navigation.

**Environment**

MOLE (Circular Economy B2B Marketplace) is engineered from the ground up to solve critical environmental bottlenecks, making it a perfect fit for the Environment & Sustainability Track.

The platform addresses the core failures of the traditional Linear Economy ("Take, Make, Waste") by providing the software infrastructure needed to scale Industrial Symiosis—the practice of feeding one factory's byproducts and waste streams back into another factory's production line as raw materials.

Here is how the project directly impacts and fits into the Environment Track:

1. Landfill Diversion & Waste Optimization (Industrial Symiosis)
The Problem: Millions of tons of industrial byproducts, scrap materials, and manufacturing waste are dumped into landfills annually because factories lack visibility into who could reuse them.
MOLE's Solution: The marketplace actively tracks and categorizes material streams. Through the Impact Analytics dashboard, companies monitor their Waste Diversion Breakdown across four vectors:
Recycled: Processing waste into new raw materials.
Reused: Direct reintegration of byproducts.
Recovered: Energy or material recovery.
Landfill: Minimized to target a absolute zero-waste footprint.
Circularity Index: Companies are scored on a scale of 0 - 100 comparing their recycled-to-landfill ratios against industry percentiles to gamify and drive corporate environmental accountability.
2. Carbon Footprint Reduction (CO₂ Savings Trajectory)
MOLE achieves carbon reduction in two distinct ways:

Virgin Material Substitution: Manufacturing virgin raw materials (like primary plastics, steel, or chemicals) is highly energy-intensive. Sourcing secondary (recycled/reused) materials requires a fraction of that energy. The platform calculates CO₂ saved using Life Cycle Assessment (LCA) coefficients: $$\text{CO₂ Saved} = \sum \Big(\text{Volume} \times (\text{Virgin Material Factor} - \text{Recycled Process Factor})\Big)$$
Proximity Logistics & Haversine Distance Sorting: Transportation is a primary driver of Scope-3 emissions. MOLE's smart matching engine uses the Haversine formula to calculate the geolocation distance between buyers and sellers, factoring Proximity heavily into the match score (worth up to 25 points out of 100). By prioritizing localized trade networks, it minimizes freight emissions.
3. Real-World Impact Translation
To make environmental impacts tangible for business stakeholders and auditors, MOLE translates abstract metric tons of carbon and waste into relatable, real-world equivalencies in the 

ImpactAnalytics.tsx
 page:

🌳 Trees Saved: Translates carbon avoided into the number of mature trees needed to absorb that amount of carbon per year.
⚡ Coal Avoided: Represents the tonnes of coal that were not burned to generate the energy saved during extraction and processing.
💧 Water Conserved: Computes the liters of water saved by using recycled processes instead of water-intensive primary resource extraction.
🚗 Cars Off the Road: Measures the equivalent annual emissions of passenger vehicles removed from highways.
4. Direct Support for ESG Reporting & Green Compliance
As environmental regulations tighten globally, corporations struggle to compile clean, auditable ESG (Environmental, Social, and Governance) data. MOLE automates this process by tracking every transaction's carbon footprint, water footprint, and landfill diversion rate. This provides companies with exportable, audit-ready data to claim carbon credits, qualify for green tax incentives, and meet regulatory reporting standards.

[Ashveth Pawar](https://github.com/Ashveth)

`2026-06-13`

---

### food waste data analysis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/food-waste-data-analysis-d069) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026-0052CC?style=flat-square)](https://codestorm-week1-2026.devfolio.co)

Vaibhav Tripathy

`2026-05-31`

---

### Nexus AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nexus-ai-6a7b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/2308partha/event_recommendation_ai) [![Built at](https://img.shields.io/badge/Built%20at-Synchronicity%20S2.0-0052CC?style=flat-square)](https://synchronicity-s-2.devfolio.co)

> AI based recommendation and digital marketing

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![chromadb](https://img.shields.io/badge/chromadb-333333?style=flat-square)

**The problem it solves**

The platform solves the fragmented event management ecosystem by bringing organizers, attendees, venues, vendors, and sponsors into one unified marketplace. Organizers often struggle to find reliable service providers, suitable venues, and sponsorship opportunities, while users find it difficult to discover events relevant to their interests. Our AI recommendation system delivers personalized event suggestions, increasing engagement and participation. The RAG-powered chatbot provides instant support and event-related information. Social networking features help attendees connect with like-minded people, fostering communities around events. The bounty-based work system creates opportunities for volunteers and freelancers, making event execution more efficient, cost-effective, and scalable.

**Challenges we ran into**

Gemini API key issue like it is not able to take heavy data load, Sometimes Database fetching issue

Team **Async Nexus** -- Sourav Sen, [Aritro Biswas](https://github.com/aritrob543-jpg), [Partha Rana](https://github.com/2006partha), [Debmalya Das](https://github.com/DebmalyaDas-007)

`2026-05-31`

---

### Saferide Guardian
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/saferide-guardian-79f7) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> An AI Powered Lost Item Recovery

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![React Native](https://img.shields.io/badge/React%20Native-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **Gryffindors** -- [Divyadharshana P](https://github.com/Divyadharshana5), [Vairamuthu M](https://github.com/vmmuthu31)

`2026-05-14`

---

### Smart-mobile-recommender
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smartrecruitmentsystem-8bb9) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mobile-recommender-geobx9ru9a7kdx7mqenmrq.streamlit.app/) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Choose Better. Buy Smarter.

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

Many users struggle to choose the right smartphone because there are hundreds of options available with different specifications, brands, prices, and features. Most people do not fully understand technical details like processor performance, RAM requirements, camera quality, battery optimization, or which phone is best for their specific usage such as gaming, photography, content creation, studying, or daily multitasking. Existing e-commerce platforms often overwhelm users with too many choices and generic filters, making the selection process confusing and time-consuming.

This project solves that problem by providing a personalized mobile phone recommendation system based on user preferences and requirements. Users can enter their budget range, preferred brands, and intended usage or application type, and the system intelligently recommends the most suitable smartphones. By using content-based recommendation techniques with Python and scikit-learn, the project analyzes smartphone features and matches them with user needs to generate relevant suggestions. The Streamlit-based interface makes the experience simple, interactive, and user-friendly.

The system helps users save time, avoid unsuitable purchases, and make better buying decisions without needing deep technical knowledge about smartphones.

**Challenges we ran into**

Some of the major challenges I ran into while building this project were collecting and cleaning smartphone data from multiple sources, handling missing or inconsistent specifications, and preparing the dataset in a structured format suitable for machine learning. Since different phones have varying feature formats such as processor names, camera specifications, battery details, and pricing, preprocessing the data accurately was an important challenge.

Another challenge was designing an effective recommendation logic that could provide relevant results based on multiple user inputs like budget, preferred brands, and usage type. Implementing content-based filtering using scikit-learn required proper feature selection and similarity calculations to ensure accurate recommendations.

I also faced difficulties in balancing recommendation accuracy with performance and usability. Making the Streamlit UI interactive, user-friendly, and responsive while integrating the backend recommendation model smoothly required several iterations and testing. Additionally, ensuring that the recommendations remained meaningful even when users provided limited preferences was another challenge during development.

Kalp Mundra

`2026-05-15`

---

### VigilAI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vigilai-60d4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/webgo-oss/vigilai) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/YI0pYCjGOIE) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> AI-Powered Autonomous Payment Recovery Platform

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![SMTP](https://img.shields.io/badge/SMTP-333333?style=flat-square) ![flask-mail](https://img.shields.io/badge/flask--mail-333333?style=flat-square) ![API](https://img.shields.io/badge/API-333333?style=flat-square)

**The problem it solves**

**VigilAI** helps businesses reduce revenue loss caused by **failed payments, declined subscriptions, incomplete transactions, and delayed customer recovery workflows**. Many subscription-based platforms and online services lose significant revenue because payment recovery processes are often **manual, slow, repetitive, and difficult to scale efficiently**.

The platform automates the entire failed payment recovery lifecycle using **AI-driven operational workflows**. Businesses can use VigilAI to intelligently analyze failed transactions, trigger **adaptive retry strategies**, automate customer communication, monitor recovery performance, and track operational insights through a centralized dashboard.

Instead of relying on manual follow-ups and static retry systems, VigilAI enables a more **autonomous and scalable recovery process**. The system helps businesses:

* **improve payment recovery efficiency**
* **reduce manual operational workload**
* **automate customer engagement workflows**
* **monitor recovery analytics in real time**
* **identify high-risk payment patterns**
* **improve subscription retention and revenue recovery**

The platform is especially useful for **SaaS businesses, subscription services, fintech platforms, and digital products** that handle recurring transactions and large-scale payment operations.

By combining **AI-powered decision systems** with **workflow automation**, VigilAI transforms payment recovery from a reactive manual task into an intelligent operational process.

**Challenges we ran into**

One of the biggest challenges while building **VigilAI** was designing a **realistic autonomous payment recovery engine** capable of handling multiple workflow states simultaneously. Failed payments are not simple binary events — they involve **retry timing, customer risk behavior, transaction patterns, recovery prioritization, and communication sequencing**. Creating a system that could intelligently simulate these operational decisions required careful **workflow orchestration** and **state management**.

Another major challenge was implementing **adaptive retry logic**. Different payment failure scenarios required different recovery strategies, and building a flexible system that could dynamically adjust retry attempts and recovery actions without breaking the workflow pipeline was complex. Early implementations often caused **conflicting recovery states** and **duplicate processing events**.

Generating **contextual AI-driven customer communication** was also difficult. The platform needed to create recovery emails that reflected **transaction status, retry history, and customer risk levels** while maintaining realistic operational behavior. Building logic that dynamically adjusted communication flows based on changing recovery conditions became a key technical challenge.

Managing **real-time recovery analytics** was another core hurdle. Since multiple recovery actions could occur simultaneously, ensuring accurate synchronization between **transaction states, recovery metrics, activity logs, and dashboard analytics** required restructuring the backend flow into a more centralized **event-driven architecture**.

Another significant challenge was the lack of access to **real-world payment recovery datasets** and actual customer transaction behavior. Since production financial data is highly sensitive and difficult to obtain, realistic customer profiles, transaction histories, payment failures, retry patterns, and recovery behaviors had to be **simulated manually using structured JSON datasets**. Considerable effort went into designing these datasets to closely mimic realistic operational scenarios so the platform could demonstrate believable AI-driven recovery workflows and analytics behavior.

**Using LocusFounder to Build a Business!**

VigilAI aligns with the Locus Founders track by demonstrating how AI-powered systems can transform real-world business operations through intelligent automation. The platform autonomously handles failed payment recovery workflows by analyzing transaction behavior, generating adaptive recovery strategies, automating customer communication, and providing real-time operational insights through a centralized dashboard.

Built as a scalable SaaS-style solution, VigilAI reduces manual intervention, improves operational efficiency, and helps businesses recover lost revenue more effectively. The project highlights the practical application of AI agents, workflow orchestration, and enterprise automation within modern fintech ecosystems.

Hamza Shaikh

`2026-05-18`

---

### Food waste analysis
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/food-waste-analysis-1cb0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tripathy25scs1003005357-dev/FOOD-WASTE-ANALYSIS.git) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#4-0052CC?style=flat-square)](https://paygentic-week4.devfolio.co)

> Smart AI system to reduce food wastage

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Excel.js](https://img.shields.io/badge/Excel.js-333333?style=flat-square)

**The problem it solves**

Food wastage is a major issue in homes, restaurants, hostels, and cafeterias. Large amounts of edible food are wasted daily due to poor monitoring and lack of awareness. This leads to financial loss, resource wastage, and environmental problems.

Our project helps users analyze food waste patterns, track wasted food quantities, and generate insights to reduce unnecessary waste. By using data analysis and smart recommendations, the system encourages better food management and sustainability

**Challenges we ran into**

Collecting and organizing food waste data accurately.
Designing a simple and user-friendly interface.
Managing large datasets and generating meaningful insights.
Integrating analysis features while keeping the system lightweight and fast.
Handling inconsistent data inputs during testing.

We solved these challenges by improving data preprocessing, simplifying the UI, and optimizing the analysis workflow.

**Using LocusFounder to Build a Business!**

Sustainability & AI — Using data analysis and smart monitoring to reduce food wastage and promote efficient resource management.

Vaibhav Tripathy

`2026-05-26`

---

### Waste Management AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/waste-management-ai-6444) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rahul-dev-cmd/WasteWise-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://waste-wise-ai-rouge.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co)

> Predict Today. Feed Tomorrow

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square)

**The problem it solves**

What WasteWise AI Does For You

 For Restaurant Owners
-Stop guessing how much food to cook— get an AI prediction every morning before kitchen prep starts
Run smarter promotions— use the Marketing ROI simulator to know if a discount campaign will actually bring more people before spending money on it
Never over-order ingredients— predicted footfall tells you exactly how much raw material to buy that day
- **Automatic surplus handling** — instead of throwing leftover food in the bin at closing time, NGOs are notified automatically

---

For Hostel Wardens & Mess Managers
-Exam season?** The model already knows footfall drops — it adjusts predictions automatically
-Festival holidays?** Same — no more cooking 300 meals when only 60 students stayed back
Daily headcount without manual counting** — just click predict and get today's expected number
Reduce monthly food budget waste** — less overcooked food = direct cost savings

 For NGOs
No more cold calling hostels asking for leftovers** — WasteWise AI alerts you automatically when surplus is predicted
Plan your pickup logistics in advance** — you know by morning how many meals are coming tonight
- **Structured, reliable food supply** instead of random donations

---

 For Management & Decision Makers
- **Data-driven kitchen operations** — replace gut feeling with ML predictions
Track surplus trends** — see which days/seasons waste spikes and plan accordingly
One dashboard** for all your branches/entities in one place

 The Core Value In One Line Before WasteWise AI — kitchens cook based on yesterday's guess.
 After WasteWise AI — kitchens cook based on tomorrow's prediction.

**Challenges we ran into**

## Challenges we Ran Into

---

### 1. The Model Kept Breaking on New Inputs
Okay so this one genuinely frustrated me for a while. When you train XGBoost it creates like 40+ columns after one-hot encoding. But when a new user hits the API, their request is just 7 simple fields. The model would just crash or give garbage output because the columns didn't match.

we had to figure out how to save the exact column list from training and then reshape every incoming request to match it perfectly before passing it to the model.

---

### 2. The Demo Kept Dying Because of Weather API
Every time we tested the predict endpoint, if the OpenWeatherMap key was wrong or the internet was slow, the whole thing would crash. Not great when you're about to demo in front of judges.

So we just wrapped it in a try/except and said — if anything goes wrong with weather, just assume it's Clear and keep going. Simple fix but took me a moment to think of it.

---

### 3. Render Refused to Deploy Because of Pandas
Spent a good chunk of time staring at a red build log that just said `metadata-generation-failed`. Turns out my requirements.txt had exact version numbers pinned like `pandas==2.2.2` which conflicted with Render's environment.

The fix was embarrassingly simple — just remove all the version numbers and let Render figure it out itself.

---

### 4. XGBoost Was Silently Getting Wrong Data
After one-hot encoding, some columns were staying as `True/False` boolean instead of `1/0` integers. XGBoost didn't throw an error — it just gave weird predictions and I couldn't figure out why for a while.

Eventually caught it by printing the dtypes and added one extra loop to force everything to int.

---

### 5. Wrong Target Column Name
This one would have been embarrassing. we almost trained the entire model on the wrong column because I assumed it was called `Footfall`. The actual dataset had it as `Expected_Footfall`.

Caught it only because we actually read the dataset generator script line by line before writing the training code.

Team **#include <errors.h>** -- [Ankush Saha](https://github.com/ankushsaha2006), [Rahul Agarwal](https://github.com/rahul4172), [Rahul Dev](https://github.com/rahul-dev-cmd)

`2026-05-09`

---

### VibeCoder AI – Voice Based Coding Assistant
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vibecoder-ai-voice-based-coding-assistant-7996) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/teenojc/VibeCoder-AI) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%201.0-0052CC?style=flat-square)](https://devlynix-buildathon.devfolio.co)

> Build apps using your voice with AI — no typing ne

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**Challenges we ran into**

One of the main challenges was integrating voice input with AI-generated code output in a smooth workflow. Initially, handling speech recognition accuracy and converting natural language into structured programming instructions was difficult. I resolved this by breaking the system into smaller modules: voice-to-text processing, AI prompt generation, and code output formatting. Testing and iteration helped improve accuracy and usability.

**The problem it solves**

Many beginners struggle with writing code manually, debugging errors, and understanding programming syntax. VibeCoder AI solves this by allowing users to build and generate code using voice commands. It makes coding faster, more accessible, and beginner-friendly by using AI to convert spoken ideas into working code. This reduces learning barriers and improves productivity for developers and students.

[Teenoj bajini](https://github.com/bajiniteenoj)

`2026-05-06`

---

### Email triage and response environment
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/email-triage-and-response-environment-6fc3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saisatwik-hue/OpenENV-1) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://huggingface.co/spaces/saisatwik1234567/Email-triage-and-response-environment) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> enterprise email through reinforcement learning

![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![LoRa Alliance](https://img.shields.io/badge/LoRa%20Alliance-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![HUGGING FACE SPACES](https://img.shields.io/badge/HUGGING%20FACE%20SPACES-333333?style=flat-square) ![pydantic](https://img.shields.io/badge/pydantic-333333?style=flat-square)

**The problem it solves**

Managing email takes 28% of every knowledge worker's day. A missed P0 alert, 
an ignored legal deadline, a phishing email that slipped through — these are 
real problems with real consequences.

This project is a complete training environment where a language model can 
learn to handle enterprise email through trial and feedback. The model reads 
emails, decides what action to take, receives a reward signal after every 
decision, and gradually improves.

**Challenges we ran into**

50 realistic enterprise emails span 6 categories — from production database 
outages that need immediate escalation, to customer refund requests that need 
empathetic responses, to phishing attempts that need to be archived without 
engaging.

Three tasks of increasing difficulty:
- Task 1 (Easy): Sort and prioritise 20 emails correctly
- Task 2 (Medium): Draft professional responses — scored with synonym-aware 
  grading so natural paraphrasing counts as much as exact keywords
- Task 3 (Hard): Process all 50 emails in the right priority order within 
  a step budget

Three innovations that make this environment different from anything else in 
the registry:

1. Synonym-aware keyword grading — "reimbursement" scores the same as 
   "refund" because they mean the same thing
2. Kendall tau prioritisation scoring — measures whether urgent emails were 
   handled before low-priority ones, not just whether everything got done
3. Dense shaped rewards — feedback arrives after every single action, not 
   just at the end of the episode

Verified scores: 0.9999 on Easy, 0.889 on Medium, 0.891 on Hard. 
Average 0.927. All tasks passing. Phase 1 and Phase 2 validation cleared.

sai satwik Vavilala

`2026-04-29`

---

### AI-Powered Knee MRI Diagnostic with Explainable AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aipowered-knee-mri-diagnostic-assistant-with-explainable-multiview-intelligence-092d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Swapnil-2005/kneeMRI_XAI/blob/main/app.py) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/4074e37e53e7438b8aaff2597f087a39) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co)

> "Precision MRI analysis in seconds."

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Deep Learning](https://img.shields.io/badge/Deep%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Deep Neural Networks](https://img.shields.io/badge/Deep%20Neural%20Networks-333333?style=flat-square) ![Keras CNN](https://img.shields.io/badge/Keras%20CNN-333333?style=flat-square) ![Neural Network](https://img.shields.io/badge/Neural%20Network-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

**The problem it solves**

Today, getting an MRI scan is not the hardest part — understanding it is.

In many cases, patients receive their MRI reports but struggle to interpret them. The reports are often highly technical, filled with medical terminology, and require expert knowledge to fully understand. This creates confusion, anxiety, and delays in taking the right medical decisions.

In rural and semi-urban areas, the problem becomes even bigger. Patients may not have immediate access to orthopedic specialists, which means they have to wait days — sometimes weeks — just to understand what their scan actually shows.

On the other hand, most AI solutions in medical imaging focus only on prediction. They detect abnormalities, but they don’t explain them in a meaningful or user-friendly way. This limits their real-world usefulness.



**How our solution helps**

Our system focuses on making MRI analysis faster, clearer, and more understandable.

- Instant MRI Analysis  
  The system analyzes knee MRI scans and detects ACL/PCL conditions using a trained object detection model.

- Clear Visual Understanding  
  It highlights the affected areas directly on the scan, helping users see where the issue is instead of just reading about it.

- Deep Learning-based Classification  
  A classification model further evaluates the scan and provides an additional layer of analysis.

- Risk Assessment  
  Based on the findings, the system categorizes the condition into different risk levels (LOW / MEDIUM / HIGH), helping users understand the seriousness of the injury.

- Simple and User-Friendly Output  
  Instead of complex medical jargon, the results are presented in a clean and easy-to-understand format.



**Impact**

This solution helps make medical analysis:

- Faster → Immediate results without waiting for expert review  
- Accessible → Useful in areas with limited specialist availability  
- Understandable → Converts complex medical data into simple insights  
- Supportive → Helps patients make informed decisions earlier  

Overall, it reduces confusion, saves time, and brings clarity to a process that is often overwhelming for patients.

**Challenges we ran into**

### Challenges I ran into

Building this project involved several practical and technical challenges, especially while working under time constraints.

One of the main challenges was handling the **dataset quality and imbalance**. The number of normal MRI scans was much higher compared to torn ACL/PCL cases, which made the model biased initially. To overcome this, I used data augmentation techniques and carefully monitored training performance to improve generalization.

Another challenge was **model integration**. Combining object detection (YOLO) with a classification model in a single pipeline required proper preprocessing, resizing, and consistent data handling. Initially, mismatches in image formats and dimensions caused incorrect predictions, which were resolved by standardizing input pipelines.

I also faced issues with **file paths and environment setup**, especially while managing virtual environments and organizing model files. Errors like missing model files or incorrect directories slowed down development, but restructuring the project and maintaining a clear folder hierarchy helped fix this.

On the backend side, integrating everything with FastAPI required debugging multiple runtime issues such as image encoding, API response formatting, and handling large files efficiently.

Finally, building a smooth connection between the backend and frontend was another hurdle. Ensuring that API calls, image uploads, and responses worked correctly in real time required multiple iterations and testing.

Despite these challenges, each issue helped improve the system's robustness and gave a deeper understanding of building end-to-end AI applications.

Team **Gijutsu no Bushi** -- [Samrat Chatterjee](https://github.com/cmdX-samrat), [Swapnil Banerjee](https://github.com/Swapnil-2005), [Debjit Roy](https://github.com/LOrd-Debjit)

`2026-04-19`

---

### AuditPilot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/auditpilot-4637) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ckasidis/audit-pilot) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://audit-pilot-eight.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/PIHYTngaaAM) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> See everything. Miss nothing. Recover faster.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square)

**What is the deployed URL for this project?**

https://audit-pilot-eight.vercel.app/

**Use of Genspark**

Used for UI prototyping before implementation

**Use of Claude**

- Genspark → Claude Code workflow: We generated the initial UI prototype and the per-agent system prompts in Genspark, then handed both off to Claude Code as a reference spec for production implementation.
  - Claude Code Skills: Leveraged official skills (vercel:nextjs, vercel:ai-sdk, neon-drizzle, shadcn) to avoid hallucinated APIs and stay aligned with current best practices.
  - Plan → Review → Implement loop: Every non-trivial change ran through Plan Mode for architectural alignment, a review pass, then implementation — with deliberate context clears between cycles to keep
  the agent sharp.
  - Structured output everywhere: Every LLM step uses generateObject with Zod schemas so outputs land directly in typed DB tables (no regex JSON extraction).

**How you are solving it**

User upload required files -> Run parser -> Fraud Detection Subagent -> Risk Ranking Subagent -> Data ingested to PostgreSQL database so it will be available for querying in. a chat based conversational UI

**The problem your project solves**

Description: AuditPilot is an AI intelligence layer that transforms Singapore Airlines'  Audit from a manual, cycle-driven process into a proactive fraud detection and revenue recovery system. Built on Anthropic Claude , it deploys a pipeline of specialist agents —  Parser, Fraud Detector, Risk Scorer, and Audit Assistant — against audit data sources: HOT files, DCS no-show feeds, eDA discount reports, and AGM group booking extracts. 
The problem AuditPilot solves is real: fraud patterns that cross HOT Files and DCS no-show records go undetected until the billing cycle closes, AGM PDFs require manual monthly extraction, eDA completeness checks block audit from starting. AuditPilot collapses this into a single weekly AI-generated digest — cutting query resolution time by 80%, surfacing 3× more fraud cases than end-of-cycle manual review, and auto-generating every ADM notice with zero manual drafting.
Genspark was used to generate the base UI which the team then further enhanced with Claude Code.

Team **SIA Pilots** -- Christine Choy, [ARUNKUMAR THANGARAJU](https://github.com/na), [Kasidis Chantharojwong](https://github.com/ckasidis)

`2026-04-24`

---

### Push & Pray
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/push-and-pray-c26d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kittypurrnaz/push-and-pray) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/K4Do2PLhmQg) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> Post-event reports in 60 seconds, not 8 hours

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![powerpoint](https://img.shields.io/badge/powerpoint-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![Anthropic Claude](https://img.shields.io/badge/Anthropic%20Claude-333333?style=flat-square)

**Use of Genspark**

## Genspark Integration

We make **two Genspark API calls** per report run:

### Call 1 — Quantitative Benchmarks (`fetch_benchmarks`)
Searches for industry-average metrics for the event type and region:
- Average attendance rates and no-show percentages
- Typical NPS score ranges
- Conversion and engagement benchmarks

This gives Claude real numbers to benchmark the client's data against, rather than just reporting raw figures in isolation.

### Call 2 — Audience Intelligence (`fetch_event_context`)
Searches for qualitative context specific to the event:
- What this type of audience typically expects
- Common feedback themes from similar events
- Key success and failure factors

This grounds the AI-written narrative in genuine industry knowledge, making the recommendations specific and credible rather than generic.

Both calls fall back to sensible mock data if no API key is provided, so the pipeline always produces a complete report.

**The problem your project solves**

link: https://sudoku-calamity-abnormal.ngrok-free.dev

## The Problem

Every event — conferences, product launches, company offsites — generates a mountain of data: attendance CSVs, survey exports, check-in logs. Someone has to turn all of that into a polished post-event report for the client or leadership team.

That someone spends **5–8 hours** doing this by hand:
- Cleaning dirty spreadsheets (duplicate rows, blank columns, inconsistent date formats)
- Computing NPS scores, attendance rates, and demographic breakdowns manually
- Googling industry benchmarks to give the numbers context
- Writing the same sections over and over: exec summary, venue commentary, recommendations
- Formatting everything into a presentable PowerPoint

The result is always late, always inconsistent, and never uses the full depth of the data.

**How you are solving it**

## Our Solution

**Push & Pray** is a Post-Event Report Auto-Generator. Upload your CSV/XLSX files, set the event brief, and receive a polished PowerPoint report in under 60 seconds.

### How it works

1. **Data Ingestion** — Upload attendance and survey files. A `DataCleaner` module normalises formats, deduplicates rows, and infers column roles automatically.

2. **Deep Analytics** — A `DataAnalyst` module computes NPS scores, rating distributions, demographic breakdowns, check-in curves, and data quality scores. Results are persisted in a local SQLite `ContextMemory` database so the system learns from every event run.

3. **AI Enrichment (Genspark)** — Two Genspark calls fetch real-world context:
   - Quantitative benchmarks (industry-average attendance rates, NPS, conversion)
   - Qualitative audience intelligence (expectations, feedback themes, success factors)

4. **Report Writing (Claude)** — Claude Sonnet writes the full narrative: headline, exec summary, conversion commentary, venue notes, demographics, voice-of-attendee synthesis, and 3–5 actionable recommendations — grounded in the actual numbers.

5. **PowerPoint Export** — A custom `ReportGenerator` builds a branded, visually polished `.pptx` with a dark navy/indigo theme, ready to send to the client.

**Use of Claude**

## Claude Integration

Claude does three jobs in the pipeline:

### 1. Dataset Profiling (Claude Haiku — fast)
On upload, Haiku classifies column roles (`attendee_name`, `check_in_time`, `rating`, `nps_score`, etc.), identifies data quality issues, and confirms the analytical plan — all in a single fast call before the heavier work begins.

### 2. Report Narrative (Claude Sonnet — deep)
Sonnet receives the cleaned data, computed statistics, Genspark benchmarks, and audience context, then writes the full report in one structured JSON response:
- `headline` and `subheadline`
- `exec_summary` (3–5 bullet points)
- `conversion_commentary`, `venue_commentary`, `demographics_commentary`
- `voice_of_attendee` synthesis
- `recommendations` (3–5 actionable next steps)

The tone is configurable (professional, casual, bold) per client brief.

### 3. React Frontend Commentary API (Claude Sonnet — via Flask)
The React/Vite frontend calls a Flask endpoint (`/api/commentary`) that hits Claude Sonnet directly, enabling real-time AI commentary generation in the browser UI — powered by the Anthropic SDK with prompt caching on the system prompt for efficiency.

Team **Push & Pray** -- [Sarah Ahmad](https://github.com/kittypurrnaz), [Estelle Teh](https://github.com/Builtbyest)

`2026-04-24`

---

### Q2 Economic Report Automation
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/q-economic-report-automation-3c7b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/JoozKelly/q2-automation-webapp) [![Built at](https://img.shields.io/badge/Built%20at-Push%20to%20Prod%20Hackathon%20with%20Genspark%20&%20Claude-0052CC?style=flat-square)](https://push-to-prod.devfolio.co)

> AI-powered quarterly reports for FTZ tenants

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![TailWindCSS](https://img.shields.io/badge/TailWindCSS-333333?style=flat-square) ![Zustand](https://img.shields.io/badge/Zustand-333333?style=flat-square) ![Recharts](https://img.shields.io/badge/Recharts-333333?style=flat-square) ![Claude API](https://img.shields.io/badge/Claude%20API-333333?style=flat-square) ![Genspark](https://img.shields.io/badge/Genspark-333333?style=flat-square) ![XLSX](https://img.shields.io/badge/XLSX-333333?style=flat-square)

**Use of Claude**

## Use of Claude

Claude (via the Anthropic SDK) powers four distinct API routes in the application:

### 1. `/api/ingest` — Economic Data Synthesis
After Genspark returns raw search results, Claude structures them into a typed JSON schema covering 8 data categories: dashboard KPIs, GDP timeseries, investment inflows, inflation trends, macro indicator grid, sector summaries, infrastructure projects, and geopolitical events. A custom brace-counting extraction algorithm handles reliable JSON parsing from Claude's streaming output.

### 2. `/api/analyze-files` — Multimodal File Ingestion
Uploaded Excel, PDF, and image files are sent to Claude's multimodal API. Claude extracts structured economic data from charts, tables, and text — even from scanned documents or slide decks — and maps it to the same typed schema.

### 3. `/api/generate` — Report Copywriting
Claude takes the structured dashboard data and writes the executive narrative sections of the quarterly report: macroeconomic commentary, sector analysis, infrastructure progress summaries, and geopolitical risk assessments.

### 4. `/api/ceo-brief` — Q3 Strategy Generation
Users upload their Q2 report document, and Claude generates a forward-looking **5-chapter Q3 storyline** for the CEO:
1. Macroeconomic Foundation
2. Infrastructure & Policy Enablers
3. Geopolitical Tailwinds
4. Sector Momentum
5. H2 Setup & Outlook

Claude is the core intelligence layer — Genspark feeds it data, and Claude transforms that data into actionable business intelligence.

**The problem your project solves**

## The Problem

Batam Free Trade Zone (FTZ) tenant-relations teams produce a **Quarterly Economic Report** every three months for investors, government liaisons, and C-suite stakeholders. The process today looks like this:

- Analysts manually pull macroeconomic data from BPS (Indonesia's national statistics bureau), news sites, and internal trackers
- Data is copy-pasted into Excel to build charts, then charts are manually placed into PowerPoint or Word
- A copywriter produces the executive narrative from scratch
- Design is re-done from scratch each quarter to maintain branding consistency
- The whole cycle takes **3–5 business days** per report

**Why it matters:** Delays in quarterly intelligence mean that investment decisions, tenant conversations, and policy responses all happen on stale data. The manual process also introduces transcription errors and inconsistent framing across quarters, undermining credibility with senior stakeholders.

**How you are solving it**

## Our Solution

We built a full-stack **Next.js web application** that automates the entire quarterly reporting pipeline:

### 1. Data Ingestion (`/ingestion`)
- Users upload Excel, CSV, PDF, or image files — or trigger a **live Genspark web search** to pull the latest macroeconomic data automatically
- BPS-targeted search mode fetches official Indonesian statistics directly
- Files are parsed with the XLSX library; images and PDFs go through Claude's multimodal API

### 2. AI Synthesis (`/api/ingest`)
- Claude synthesises raw data into a structured JSON payload covering: GDP timeseries, investment inflows, inflation trends, sector momentum, infrastructure projects, geopolitical events, and a Batam FTZ news feed
- A custom brace-counting JSON extraction algorithm ensures reliable parsing of Claude's responses

### 3. Interactive Dashboard (`/`)
- KPI cards, historical GDP line charts, stacked area investment charts, and inflation bar charts — all rendered with Recharts and driven by Zustand state

### 4. Report Builder (`/report-builder`)
- Section-by-section report composition with infrastructure trackers, geopolitical impact ratings, and sector momentum summaries
- One-click **PDF export** with professional layout via react-to-pdf

### 5. CEO Brief (`/ceo-brief`)
- Upload the current Q2 report and Claude generates a forward-looking **5-chapter Q3 strategy narrative** for the executive team

**Result:** Report turnaround drops from 3–5 days to under 2 hours.

**Use of Genspark**

## Use of Genspark

Genspark is the **live data backbone** of the ingestion pipeline.

### How it's integrated
- The `/api/ingest` route calls Genspark via its CLI interface to perform real-time web searches for macroeconomic indicators (GDP growth, FDI inflows, inflation, BPS publications, sector news)
- A dedicated **BPS search mode** targets Indonesia's national statistics bureau specifically for official quarterly figures
- Search results stream back in real time, with logs displayed in the UI so users can see exactly what data was retrieved and from where
- Genspark also powers the **Batam FTZ news feed**, fetching and categorising recent articles by topic (FDI, infrastructure, policy, geopolitics, sector activity)

### Why Genspark
Instead of maintaining brittle scrapers for dozens of government and news sources, Genspark acts as an intelligent web research layer — returning structured, relevant results that Claude can immediately synthesise into the dashboard schema. This means the app always has access to the **latest published data** without any manual refresh.

**The problem it solves**

Quarterly economic reporting for Batam Free Trade Zone (FTZ) tenants is slow, fragmented, and highly manual. Economic data is scattered across government portals (BPS), news feeds, and internal spreadsheets — requiring analysts to spend days aggregating figures, building charts, writing narratives, and designing polished PDFs before a single report reaches a stakeholder.

**Challenges we ran into**

Reliable JSON extraction from Claude's streaming responses required a custom brace-counting algorithm instead of greedy regex, which broke on nested structures. Multimodal ingestion (PDF, Excel, images in one pipeline) needed careful schema design so the AI output always mapped cleanly to typed TypeScript interfaces. Streaming Genspark search logs in real time while simultaneously synthesising the data into a structured dashboard required careful async orchestration across Next.js API routes.

**Hackathon Prizes**

This project directly addresses the hackathon's core theme: eliminating invisible, painful internal workflows with AI. Quarterly economic reporting is a real internal process experienced at trade-zone management companies — hours of manual data collection, Excel charting, and PowerPoint design that this app replaces end-to-end with Claude and Genspark.

[Kelly Tayong](https://github.com/JoozKelly)

`2026-04-24`

---

### MarginMind
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/marginmind-abb9) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rohan5commit/marginmind-paygentic) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://marginmind-paygentic.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#2-0052CC?style=flat-square)](https://paygentic-week2.devfolio.co)

> AI Agent finds SaaS waste and saves teams cash now

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![Nvidia Nim](https://img.shields.io/badge/Nvidia%20Nim-333333?style=flat-square) ![Locus API](https://img.shields.io/badge/Locus%20API-333333?style=flat-square)

**The problem it solves**

Startups and solo builders lose money every month to SaaS waste: duplicate tools, underused subscriptions, rising vendor costs, and missed refund/negotiation opportunities.

Most people can spot waste, but they don’t take action because the follow-through is manual and slow.

MarginMind solves this by acting like a finance operations agent:
  - Ingests spend data from CSV/demo transactions
  - Detects duplicate subscriptions, pricing outliers, underused tools, and refund/negotiation candidates
  - Prioritizes actions by expected monthly/annual savings
  - Uses NVIDIA NIM for concise, founder-ready reasoning
  - Uses a Locus-native action layer (wallet context, wrapped API planning, and task escalation logic) to move from analysis to execution

 The result is practical: less monthly burn, higher savings capture, and an agentic workflow that is focused on money saved, not just dashboards.

**Challenges we ran into**

A major challenge was making the product truly agentic instead of a generic analytics dashboard.

I had to redesign the flow so each finding maps to an executable next step (cancel, downgrade, refund request, negotiate, replace, or monitor), then connect that to a Locus-first action model.

 Other hurdles:
  - Deployment reliability on Vercel: I hit failed production deploys and fixed build/runtime issues, then validated with GitHub Actions + production checks.
  - AI output reliability: NIM responses needed strict JSON handling, schema validation, retry logic, and deterministic fallbacks.
  - Security hardening: Public AI endpoints needed payload validation, rate limiting, and safer error handling to prevent abuse.
  - Locus clarity in demo: I added explicit live/simulation state, redacted sensitive wallet fields, and surfaced Locus capability checks so judges can clearly see what is live now vs guarded in MVP.

These fixes made the app more robust, safer, and demo-ready under real judging conditions.

**Track: Using BuildWithLocus to leverage our suite.**

MarginMind is built specifically for the Week 2 BuildWithLocus track: it is an agentic spend-optimization product where Locus is part of core execution, not branding.

The system ingests startup SaaS spend, detects waste duplicates, underused tools, pricing outliers, rising costs, refund/negotiation candidates), and maps each finding to an actionable agent decision. It then routes these decisions through a Locus-native layer: wallet-aware policy guardrails, wrapped API planning, app capability discovery, and ROI-based task escalation logic.

This directly matches “Hack an Agent to Make You Money” because MarginMind is designed to reduce real monthly burn and recover money, not just visualize data. NVIDIA NIM is used for structured strategy/explanation outputs, while deterministic heuristics keep decisions grounded and auditable for demo and judging.

Rohan Santhosh

`2026-04-19`

---

### LIVECollab
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/livecollab-96ad) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://fork-yeah-three.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Ctrl%20+%20Build-0052CC?style=flat-square)](https://ctrl-build.devfolio.co)

> Collaborate. Create. Sync — in real time

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

## ❗ Problem Statement

Modern collaboration is fragmented.

Teams often rely on multiple disconnected tools for:
- brainstorming (whiteboards)
- communication (voice & chat)
- decision-making (polls, data tools)

This constant context switching:
- breaks workflow  
- slows down productivity  
- causes loss of ideas and clarity  

There is no single platform that seamlessly combines real-time visual collaboration, communication, and interactivity.

---

## 💡 Solution

LiveCollab solves this by providing a unified, real-time collaborative environment where teams can:

- Draw and brainstorm together on a shared canvas  
- Communicate via voice, chat, and live captions  
- Use interactive tools like polls and graphs  
- Stay fully synchronized without switching platforms  

All in one place — fast, intuitive, and built for real-time teamwork.

**Challenges we ran into**

## ⚔️ Challenges I Ran Into

Building LiveCollab came with several real-world engineering challenges:

---

### 🔄 Real-Time State Synchronization
Keeping multiple users in sync on a shared canvas was difficult.  
Issues like:
- duplicate events  
- out-of-order updates  
- inconsistent canvas states  

**Solution:**  
Implemented event-based synchronization using Socket.IO with controlled state broadcasting and idempotent updates to ensure consistency across all clients.

---

### 🎨 Canvas Performance (React-Konva)
Handling continuous drawing events caused performance drops and lag, especially with multiple users.

**Solution:**  
- Optimized re-renders by minimizing state updates  
- Batched drawing events  
- Used refs and efficient layer updates in React-Konva  

---

### 🧩 Draggable Widget Sync (Graphs & Polls)
Keeping widget positions, resizing, and data synchronized across users was tricky.

**Solution:**  
- Centralized widget state on the server  
- Synced position + data changes via socket events  
- Used controlled components with React-Rnd  

---

### 🎙️ Voice Chat + Live Captions
Integrating real-time speech-to-text with live updates on the canvas introduced latency and accuracy issues.

**Solution:**  
- Used browser Speech-to-Text APIs  
- Streamed partial transcripts instead of waiting for full sentences  
- Optimized UI updates for smoother caption rendering  

---

### 🔐 Google OAuth + Session Handling
Managing authentication across frontend and backend caused session persistence issues (especially with CORS).

**Solution:**  
- Configured proper CORS with credentials  
- Used Express sessions with secure cookies  
- Ensured consistent session handling across requests  

---

### 🌐 Handling Late Joiners
New users joining a room weren’t seeing the existing canvas state initially.

**Solution:**  
- Implemented state persistence on the server  
- Sent full canvas snapshot on join  
- Synced chat history and widgets on connection  

---

## 🚀 Key Takeaway

The biggest challenge was not building features individually, but making them **work together in real-time without breaking synchronization or performance**. Solving this required careful event design, state management, and optimization.

Team **Fork yeah** -- Ayush Thakur, Vedant Sharma

`2026-04-16`

---

### RoadRakshak
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/roadrakshak-c7b8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pulkit1245/RoadRakshak.git) [![Built at](https://img.shields.io/badge/Built%20at-Off--Grid-0052CC?style=flat-square)](https://offgrid.devfolio.co)

> Har second pe nazar, Har jaan ki fikar

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Vite](https://img.shields.io/badge/Vite-333333?style=flat-square) ![Ultralytics](https://img.shields.io/badge/Ultralytics-333333?style=flat-square) ![YOLOv8](https://img.shields.io/badge/YOLOv8-333333?style=flat-square) ![Base64Encoding](https://img.shields.io/badge/Base64Encoding-333333?style=flat-square) ![OlaMap](https://img.shields.io/badge/OlaMap-333333?style=flat-square)

**The problem it solves**

Today traffic infrastructure is not good enough. It only reacts to things after they have already happened. For example cameras just record what is happening. People only do something about it after they notice that something has gone wrong. When there are car accidents this delay is not a waste of time. It can cost people their lives. When someone has an accident emergency services still have to wait for someone who saw it happen to call them which can take 15 to 20 minutes. This is a long time especially when every minute counts.

We are trying to fix this problem. The problem of not being able to respond enough when something happens.

Our system is different from what's already out there. We use intelligence to make traffic cameras smarter. Of just watching what is happening we understand what is going on. If someone has an accident our system knows away and sends out emergency alerts in just a few seconds. It does all of this without needing anyone to get involved.

What really makes our system special is that it does not just stop at seeing that something is wrong. Most other systems just identify the problem. Then stop. Our system does everything. It sees the problem figures out what is happening. Then does something, about it. From looking at the details of what happened to getting emergency services to respond our system does it all automatically. There are no delays, no need to wait for someone to do something and no bottlenecks.

Basically we are not just building a system that can detect problems. We are changing the way that cities respond to emergencies.

We are taking traffic infrastructure, which used to record what was happening and turning it into a system that can actually save lives. Our system does not just see accidents happen. It responds to them away.

**Challenges we ran into**

One of the hardest challenges we faced was not building detection, but building reliable detection. 

In real-world traffic, vehicles are constantly moving close to each other. If you rely on just one signal like bounding box overlap, the system starts detecting ‘accidents’ everywhere, which makes it unusable in practice. 

So instead of thinking like developers, we started thinking like people in the real world.

We designed a multi-layer intelligence system where no single parameter can trigger an accident. We combine spatial signals like overlap, temporal signals like motion patterns, and physical indicators like sudden velocity changes. Only when multiple independent signals align do we confirm a collision. 

This shift from single-condition detection to multi-signal validation was the key to making our system reliable, not just functional.

The second major challenge was real-time performance. Deep learning models are powerful, but they are also costly in terms of computation. We had to balance speed and accuracy, optimizing our pipeline so that detection happens instantly without sacrificing performance.

We also had to handle real-world unpredictability, such as low-light conditions, varying camera angles, and inconsistent environments. Instead of ignoring these issues, we engineered around them using adaptive image enhancement techniques to maintain consistency.

But the real challenge wasn’t technical; it was conceptual. 

Building a model is easy. Building a system that works reliably in the chaos of the real world is where the real engineering begins. 

And that’s exactly what we focused on.

**Winners**

We have designed our project at the crossroads of Smart Cities, AI & Machine Learning, and Public Safety & Mobility.

In terms of Smart Cities, our approach involves turning traditional traffic infrastructure into a smart network that does not simply monitor but also reacts to traffic conditions in real time.

In the area of AI & Machine Learning, our project uses the capabilities of computer vision in real time for traffic analysis and decision-making. In this context, the speed of our model is vital because each second can mean the difference between life and death.

Finally, it is crucial to emphasize the connection of our project with Public Safety. Road accidents are one of the leading causes of mortality, but the issue here lies in emergency response time. Our model significantly decreases the time between detecting an accident and sending an alert.

The power of our AI technology should be seen in its practical application to create a more responsive and safe city environment.

In other words, we are not limited to any particular path; on the contrary, we embrace various domains to solve a real-life problem that benefits from technological advancements.

Team **Mahaveera** -- [Pulkit Verma](https://github.com/pulkit123459), [Anupriya Saxena](https://github.com/AnupriyaSaxena28), [Shreyasvi Srivastava](https://github.com/Shreyasvi25)

`2026-04-11`

---

### GoSustain
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gosustain-0971) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/pragga9876/GoSustain) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20Storm%202.26-0052CC?style=flat-square)](https://hack-storm.devfolio.co)

> Your Carbon. Your Control

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Embedded Javascript (EJS)](https://img.shields.io/badge/Embedded%20Javascript%20(EJS)-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![Charts.js](https://img.shields.io/badge/Charts.js-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square) ![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-333333?style=flat-square)

**The problem it solves**

In the fight against climate change, we introduce GoSustain — a smart energy optimization platform that transforms sustainability into everyday action. It collects real-time device data, uncovers consumption patterns, and delivers hyper-personalized recommendations through interactive dashboards. Powered by anomaly detection and predictive AI, GoSustain automates savings, slashes wastage and carbon emissions, and empowers households and organizations to live greener — efficiently and affordably.

**Challenges we ran into**

Developing GreenLane, the ecofriendly route finder, we needed to tackle the traffic on routes, travelling modes chosen by user, etc

Team **Humein Select Bilkul Mat Karna** -- [Sonam Das](https://github.com/squirtlenotgangster), [Pragga Mukherjee](https://github.com/pragga9876), [Abhirup Nandi](https://github.com/Abhirup-261004)

`2026-04-09`

---

### Energy Consumption Optimizer
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/energy-consumption-optimizer-0f36) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/agamonighosh6-prog/Energy-Consumption) [![Built at](https://img.shields.io/badge/Built%20at-Hack%20Storm%202.26-0052CC?style=flat-square)](https://hack-storm.devfolio.co)

> Reduce energy wastage

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square)

**The problem it solves**

• Our hardware project model is an energy conservation system using ESP 32 ,DHT 11 sensor 
• It measures temperature and humidity .
• Machine learning analyzes data to find unusual changes and possible energy waste.
• If probable expected event does not occurs then the system since alerts to a mobile phone and activate a buzzer.
• These helps maintain stable environmental conditions, reduces and necessary energy used and improves smart monitoring.

**Challenges we ran into**

I face the device capacity issue.Our ESP32 have 2mb capacity.But if we deploy human detection Ml model ,it can't process due it's low capacity .So ,if we have the raspberry pi device then ,we can develope it.

Team **Hackops** -- Agamoni Ghosh, [Pritam Ghosal](https://github.com/pritamghosal), [Aritro Dey](https://github.com/Aritro-2005)

`2026-04-09`

---

### ClaimGuard Ai
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/claimguard-ai-dadb) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/rajsingh62/ClaimGuard-AI.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1lqgseI1cahDcCSYWwo3vLlod9nVEEv28/edit?usp=drive_link&ouid=116213143042471078316&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> From policy confusion to payout clarity-in seconds

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

## 💡 The Problem It Solves

ClaimGuard AI is designed to solve a very real and frustrating problem that almost everyone faces with insurance—**confusion and lack of trust**. Most people don’t fully understand their insurance policies because they are filled with complex terms and hidden conditions. When it comes time to file a claim, they often don’t know what will actually be covered, which leads to unexpected rejections, delays, and stress.

This project makes that entire process much simpler and more transparent. Instead of manually reading long policy documents or relying on agents, users can just upload their policy and bill, and the system clearly tells them what is payable, what is not, and most importantly—**why**. This saves time, reduces confusion, and helps users make better decisions.

It also makes the process safer and more trustworthy. By storing a proof of the result on blockchain, users can be confident that the decision hasn’t been altered or manipulated. This is especially important in cases where disputes happen between customers and insurance providers.

In simple terms, ClaimGuard AI turns a complicated, uncertain process into something **clear, fast, and reliable**, helping users feel more in control of their insurance decisions.

**Challenges we ran into**

## ⚠️ Challenges I Ran Into

One of the biggest challenges I faced while building ClaimGuard AI was handling **unstructured PDF data, especially insurance policies and bills. Every document had a different format—some were scanned images, some had complex tables, and others had inconsistent wording for the same clauses. Initially, the OCR output was messy and the AI was giving incorrect or incomplete results because it couldn’t clearly understand the structure.

To solve this, I didn’t rely on a single approach. I improved the pipeline step by step—first by cleaning the OCR output, then by introducing basic preprocessing like removing noise and standardizing text. After that, I built a rule-based layer alongside NLP so that even if the AI model missed something, the system could still make logical decisions based on keywords and patterns. This hybrid approach significantly improved accuracy.

Another challenge was integrating the blockchain layer using Solana. At first, I tried storing too much data directly, which made things inefficient. After researching and experimenting, I realized that storing only the hash of the result was the right approach—it reduced cost and improved performance while still ensuring data integrity.

Overall, these challenges taught me an important lesson: building real-world systems is not about perfect models, but about combining multiple techniques and iterating until the system becomes reliable.

**Best Build on Solana**

ClaimGuard AI fits perfectly into the “Built on Solana” track because it uses blockchain in a meaningful, real-world way rather than just as an add-on. In our system, AI analyzes insurance policies and bills to generate a claim decision, but the key innovation is what happens next—we convert that result into a secure hash and store it on Solana. This ensures that once a decision is made, it cannot be altered, creating a transparent and tamper-proof record. In an industry like insurance, where trust and disputes are major issues, this adds a powerful layer of credibility. So, while AI handles the intelligence, Solana guarantees the integrity of the outcome, making the entire system reliable, verifiable, and aligned with the core purpose of blockchain technology.

Team **Shadow Solver** -- [Yogesh Prasad](https://github.com/yogeshHax), [Sunny Kumar](https://github.com/Sunny25052005), RAJ SINGH, [Nitesh Barnwal](https://github.com/Nitesh0986)

`2026-04-05`

---

### Smart Waste Segregation(Team Beta)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-waste-dustbin-6590) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Priya342-gif/Beta) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1BUxQgbarub_6qSpunt78DjLqs2DWb4oR/edit?usp=drive_link&ouid=104871653029729584555&rtpof=true&sd=true) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/gpFGEkUT2qI?feature=shared) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Clean & Green Technology

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![MQTT](https://img.shields.io/badge/MQTT-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

This project is an AI powered smart waste segregation system designed to automate and improve waste management. It uses an ESP32, IR sensors, and a camera to detect and capture waste images. A Tensor Flow Lite model classifies the waste into organic, recyclable, and hazardous categories in real time. Based on the result, servo motors automatically direct the waste into the correct bin, eliminating manual sorting.
A secondary IR sensor monitors the bin level and triggers an alert when it becomes full, displaying a message on the LCD and sending a notification via MQTT for timely action.
Benefits
Automation: Eliminates manual waste segregation
Safety: Reduces human exposure to hazardous waste
Efficiency: Improves accuracy of waste classification
Real-time Monitoring: Detects bin overflow instantly
Scalability: Can be deployed in smart cities and campuses
Cost-effective: Reduces long

**Challenges we ran into**

Servo Power Issues: Servos caused instability and ESP32 resets due to low power
Solution: Used external 5V supply with common ground
Camera Connection Failure: Camera stream failed due to network restrictions
Solution: Switched to mobile hotspot for same network access
TensorFlow Compatibility: Installation failed on newer Python versions
Solution: Downgraded to Python 3.12 and used virtual environment
LCD Not Displaying: No output due to wrong I2C address and pin conflicts
Solution: Fixed address and reassigned SDA/SCL pins
MQTT Delays: Delay in receiving classification results
Solution: Improved message handling and added timeout
Dataset Limitations: Model accuracy affected by limited data
Solution: Combined datasets and used preprocessing and augmentation

Team **Beta** -- [Priya Chauhan](https://github.com/Priya342-gif), [Urvi Gupta](https://github.com/UrviGupta8124), [Akarshi Srivastava](https://github.com/Akarshi27), [Ayush Pandey](https://github.com/aayuk003)

`2026-04-04`

---

### Aarogya_sos
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aarogyasos-c212) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aarogyasos.netlify.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1180043712?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> “From SOS to Solution in Seconds"

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

AarogyaSOS is an intelligent, integrated emergency healthcare platform that enables instant medical assistance through a single action — no complex steps, no delay. Unlike standalone emergency calling apps, AarogyaSOS combines real-time location intelligence, medical profile sharing, AI assistance, and a community helper network — all in one unified platform.

**Challenges we ran into**

Problem 1: Getting accurate user location was inconsistent, and sometimes the browser denied location access.

Solution: We implemented:
enableHighAccuracy: true in Geolocation API
Proper error handling (permission denied, timeout, etc.)
User prompts to allow location access
This improved reliability and user experience.

Problem 2: The biggest challenge was ensuring SOS works without internet, since web apps rely heavily on connectivity.

Solution: We designed an offline fallback system:

Detect network status using navigator.onLine
Store SOS requests in localStorage
Trigger SMS/call fallback mechanism
Auto-sync data when internet reconnects

This made the system more real-world reliable.

Team **Titans** -- [VIVEK Vivek](https://github.com/Vitalvon), [Nishant Goel](https://github.com/Nishant121002), [Abhishek Goswami](https://github.com/Abhi001199), [Amira .](https://github.com/amira7289)

`2026-04-04`

---

### Blood Help
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/blood-help-2cf5) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/FqjC8rKTnTQ?si=amqnMiTP0pH_D_tJ) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Made by ECOSHIELD love for India

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

Provides instant, AI-powered matching

Enables real-time emergency alerts

Uses GPS to find nearest donors

Ensures verified and trusted requests

 Motivates donors through rewards & recognition

Predicts demand using AI/ML



“Our project solves the problem of delayed and unorganized blood access by creating a real-time, AI-driven network that connects donors and patients instantly.”

![image](https://assets.devfolio.co/content/8a5ec7863e644dd99760e87160716d56/e6b76c22-c1c7-4468-b988-19faac10473b.jpeg)

**Challenges we ran into**

“Our main challenges were real-time matching, scalability, and ensuring secure, reliable communication — which we solved through optimized backend design and AI-driven logic.”

Team **EcoShield** -- [Anushka Sharma](https://github.com/anushka658), [Krishna Yadav](https://github.com/raokrishna4455-debug), [Krishna Sagar](https://github.com/krishnasagarg10), [Anushka Singh](https://github.com/anushkaasingh26)

`2026-04-04`

---

### Greencred
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greencred-b599) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prakharsi055-netizen/greencred2) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> Strava for eco actions

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![Cloudinary](https://img.shields.io/badge/Cloudinary-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

GreenCred is solving the lack of a trusted, social, and rewarding platform for environmental action, turning eco work from an invisible private habit into a visible, verified, and celebrated public identity.

**Challenges we ran into**

Can't host  the website because free scription of firebase can only host static site but we are using django which is dynamic and we are unable to use Google vision API due to lack of resources. Profile window in our site is not fully loading

**Fresher’s Track: The Rising Lanterns**

All team members are in first year this is our first hackathon before this, we have no prior experience .

Team **Dead Neurons** -- [Amit Singh](https://github.com/amitsingh005), [dhruv singh](https://github.com/ru-dhruv)

`2026-03-29`

---

### DanishRecon- Advance Vulnerability Platform
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/danishrecon-advance-vulnerability-and-reconnaissance-analysis-platform-9c08) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/DanishDhanjal15/DanishRecon.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1178120914) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> Cybersecurity project

![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![PyQt](https://img.shields.io/badge/PyQt-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![NetworkX](https://img.shields.io/badge/NetworkX-333333?style=flat-square) ![Cybersecurity](https://img.shields.io/badge/Cybersecurity-333333?style=flat-square) ![Python3.11](https://img.shields.io/badge/Python3.11-333333?style=flat-square)

**The problem it solves**

DanishRecon solves the problem of slow, manual, and error-prone cybersecurity reconnaissance by automating the entire process of discovering exposed services, vulnerabilities, and misconfigurations across networks and web applications.

For penetration testers and security teams: It dramatically reduces the time and expertise needed to perform comprehensive assessments, enabling even small teams to scan multiple targets in parallel and receive professional, actionable reports.
For organizations: It helps identify security gaps before attackers do, making it easier and safer to secure digital assets.
For students and researchers: It provides a hands-on, all-in-one platform to learn and practice real-world security testing techniques.
By integrating advanced detection, AI-powered analysis, and compliance mapping in a single tool, DanishRecon makes security assessments faster, more thorough, and accessible to a wider audience.

**Challenges we ran into**

Integrating Multiple Tools:
Combining Nmap, Nikto, and custom scripts into a single workflow was challenging due to differences in output formats and error handling. I overcame this by writing robust parsers and standardizing the data models.

Handling False Positives:
Some vulnerability checks (especially WAF detection and secret scanning) produced false positives. I improved accuracy by adding cross-verification steps and allowing manual review in the reports.

Performance Optimization:
Scanning multiple targets in parallel caused high memory and CPU usage. I optimized the threading model and implemented resource limits to ensure stable performance even on modest hardware.

User Experience (UX):
Designing an intuitive GUI with real-time feedback and export options required several iterations and user feedback. I used PyQt5’s features to add progress bars, dark/light themes, and easy report exports.

AI Integration:
Integrating Gemini AI for advanced analysis required learning new APIs and handling asynchronous responses. I solved this by modularizing the AI components and providing clear fallbacks if the AI service was unavailable.

Team **CYBERKNIIGHTS** -- [Danish Dhanjal](https://github.com/DanishDhanjal15), [AINESH CHAKRAVARTI](https://github.com/Darthvader)

`2026-03-29`

---

### PhantomCut
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wattwatch-b716) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/LeonDae/PhantomCut) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1I6M3TSICMa8vxF-k48eXM_Y6EtVJjSvC?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> #Command your energy. Cut the phantom.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![YOLOv8](https://img.shields.io/badge/YOLOv8-333333?style=flat-square)

**The problem it solves**

We tackled something really common but often overlooked appliances like lights, ACs, and screens being left running in empty rooms. The tricky part is that regular motion sensors just can't tell the difference between "no one's here" and "someone's sitting quietly." Our system repurposes CCTV cameras that are already installed everywhere and turns them into smart energy monitors that can actually catch these situations and act on them automatically.

![image](https://assets.devfolio.co/content/9334cca562a842d4979c94025ac91572/39cc6484-56dd-47fd-ac8d-d19a732d2d00.jpeg)

**Challenges we ran into**

We ran into a few real ones — someone sitting still might not get detected, so our system could wrongly think a room is empty. Figuring out whether a light or screen is genuinely on, just from a camera feed, turned out to be harder than it sounds. Running all of this in real time also puts a heavy load on basic hardware. And of course, having cameras watching people constantly raised some obvious privacy concerns that we had to think carefully about.



![image](https://assets.devfolio.co/content/9334cca562a842d4979c94025ac91572/8a172900-3df7-4435-a5a4-2112aea2bc9f.jpeg)

**GREEN & SUSTAINABLE EARTH**

This fits squarely under a sustainability/green tech track, since the whole project is about reducing energy waste in buildings using smart AI-powered monitoring.

Team **Team Resolve** -- [Dhritiman Roy](https://github.com/d-r-o-y), [Rudrakshee Banerjee](https://github.com/Rudrakshee), [Ditsu Kundu](https://github.com/LeonDae), [Jishnu Roy](https://github.com/Jishnu1618)

`2026-03-28`

---

### Watt-Watch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wattwatch-033b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/reashav7/Watt-Watch.git) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> Turning Every Camera into an Energy Guardian

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Twilio Rest API](https://img.shields.io/badge/Twilio%20Rest%20API-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

An AI-powered system that transforms existing CCTV cameras into smart energy auditors by detecting room occupancy and active appliances in real time. It identifies “empty but active” spaces, ensures privacy through anonymization, and delivers actionable insights to reduce energy waste and carbon footprint.

**Challenges we ran into**

One of the key challenges we faced was accurately detecting ceiling fans using computer vision. Unlike common objects, fans are not well-represented in standard datasets and often appear small, blurred, or partially visible in CCTV footage—especially when rotating, which caused frequent false negatives in our system. To overcome this, we created a custom dataset with fan images in different conditions (angles, lighting, ON/OFF states) and fine-tuned a YOLOv8 model specifically for fan detection. We also applied data augmentation (blur, brightness changes) and adjusted detection thresholds, which significantly improved accuracy and made our “empty but active” energy detection more reliable.

**GREEN & SUSTAINABLE EARTH**

Our solution directly supports the theme of Green and Sustainable Earth by reducing unnecessary energy consumption through intelligent monitoring. By using AI to detect “empty but active” spaces in real time, it helps eliminate phantom energy waste from lights, fans, and other appliances. This leads to lower electricity usage, reduced carbon emissions, and cost savings for institutions. Additionally, by leveraging existing CCTV infrastructure and ensuring privacy through anonymization, the system promotes sustainable innovation without requiring extra hardware, making it both environmentally and socially responsible.

Team **Byte Dunes** -- [Rajobrata Mukherjee](https://github.com/rajobrata1201), [REASHAV DE](https://github.com/reashav7), [Snehan Maity](https://github.com/Snehan-Maity)

`2026-03-28`

---

### Watt-Watch
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wattwatch-7167) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/alitacodes/Watt-Watch) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/vQ6Ko7n3V8s) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> Save Energy, Save your Money

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![MySQL](https://img.shields.io/badge/MySQL-333333?style=flat-square)

**The problem it solves**

Watt-Watch is an AI-driven system that transforms passive CCTV feeds into "smart" energy auditors. By distinguishing between active occupancy and empty, power-draining rooms, it eliminates the "phantom energy" traditional sensors miss—without disrupting quiet students.

Facilities managers can use it to automate lighting adjustments in real-time, cutting costs and carbon footprints without expensive retrofits. It simplifies building oversight by providing actionable data, making campus operations more efficient, sustainable, and less reliant on manual energy checks.

**Challenges we ran into**

One of the most significant technical hurdles was establishing a seamless, low-latency synchronization between the edge IoT devices and our centralized server. Initially, the automation pipeline suffered from data bottlenecks and inconsistent state updates, where the system struggled to trigger real-time energy cut-offs based on rapidly changing visual metadata.
We overcame this by integrating this with a Flask-SocketIO backend, we established a dedicated "live pipe" between the vision-processing server and the edge devices.

This architecture solved the synchronization bottleneck by enabling the server to push state changes (e.g., "Room 402 is now empty") directly to the IoT controllers the millisecond the AI detected a change. This transformed a manual, high-latency process into an automated, event-driven pipeline that ensures the power grid responds at the speed of the visual data.

**GREEN & SUSTAINABLE EARTH**

Our project bridges the gap between infrastructure and ecology by repurposing existing visual data into "intelligent energy audits." By converting standard CCTV feeds into real-time occupancy detectors, we eliminate phantom energy loads without the high cost of hardware retrofits. This creates a scalable Smart City framework that achieves massive carbon reduction and quantifiable financial savings, proving that AI-driven "Ethical Surveillance" can prioritize resource optimization while strictly respecting individual privacy.

Team **NanoDevs** -- [Jyotipriya Biswas](https://github.com/noob-master-jpb), [Sneha Mandal](https://github.com/alitacodes), [Subham Majumdar](https://github.com/Linux56ax), [Sayani Rana](https://github.com/Sayani966)

`2026-03-28`

---

### TraceFlow
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/traceflow-b125) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abhishek222983101/Paradigm_hn4) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> AI-powered traceability for recycled materials.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

The recycling industry is a cornerstone of global sustainability, but its supply chain is notoriously opaque. Tracking a plastic bottle from a local scrap vendor, through the washing and shredding process, all the way to becoming a finished recycled pellet usually involves messy spreadsheets, manual data entry, and siloed software. 
This lack of transparency causes three massive problems:
1. It is incredibly difficult to calculate actual material yield and pinpoint where physical losses are happening on the factory floor.
2. It is easy for fraudulent or non-compliant materials to slip into the supply chain.
3. Companies struggle to prove their compliance for sustainability certifications and Extended Producer Responsibility (EPR) audits.
TraceFlow AI solves this by providing an intelligent, end-to-end traceability platform specifically built for recycled materials. 
We make the existing workflow significantly easier by allowing warehouse managers and floor workers to log inventory using natural language. Instead of navigating complex drop-down menus, a worker can simply type or speak, "Received 500kg of PET plastic from Vendor A and sent it to washing." Our NLP engine automatically extracts the entities and updates the database.
We make the process safer and more transparent for plant operators by visualizing the exact journey of all materials using interactive Sankey diagrams. If a batch of plastic loses an unusual amount of weight during the washing phase, our integrated Machine Learning models (Isolation Forest and XGBoost) instantly flag the anomaly, allowing quality control teams to catch inefficiencies or theft in real-time.

**Challenges we ran into**

💥 The D3.js Sankey Crash
The Bug: Our material flow visualization broke during backend integration. d3-sankey strictly requires numeric indices, but our database uses string-based IDs (like "INV-S4"), causing the canvas to crash with cryptic errors.

The Fix: Instead of building fragile data-mapping dictionaries, we configured D3 natively to accept strings using .nodeId((d) => d.id). We paired this with a pre-render sanitization script to strip out circular loops and orphaned nodes. It rendered flawlessly on the first compile.

🧠 Taming Unstructured Jargon
The Hurdle: We wanted natural chat interactions, but parsing factory jargon with Regex was too brittle, and sending every message to a massive LLM was too slow and expensive.

The Fix: We built a two-tier NLP pipeline. A lightweight, local DistilBERT model handles rapid intent classification (e.g., logging vs. querying). Only then do we ping Featherless API LLMs to extract specific entities. This architectural split slashed latency and made the bot highly accurate.

Team **Paradigm** -- [Bhoomika Surve](https://github.com/bhoomisurve), [Abhishek Tiwari](https://github.com/Abhishek222983101)

`2026-03-26`

---

### ERTH
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/erth-f625) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lokesh-3s/Kabo_hn4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1ZBwF1pI5s5QzFmocKumZ4nH4ckm4sBzY/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> Classify. Recycle. Sustain.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Convolutional neural network (CNN)](https://img.shields.io/badge/Convolutional%20neural%20network%20(CNN)-333333?style=flat-square)

**The problem it solves**

This AI-powered pipeline tackles one of recycling's most persistent failures the misidentification and inconsistent sorting of plastic waste at scale. By combining an EfficientNet-B3 classifier (plastic type), CLIP-based recyclability grading (A/B/C condition scoring), and monocular depth estimation for volume measurement, the system transforms a single image of plastic waste into a structured, actionable output telling operators what the plastic is, whether it's worth recycling, and how much is there automatically replacing the slow, dangerous, and error-prone manual sorting that causes millions of tonnes of recyclable plastic to end up in landfills every year.

**Challenges we ran into**

The main hurdle was bridging the domain gap between lab photos and real conveyor footage. We tackled this with Focal Loss, WeightedRandomSampler, and SAM optimizer to find flatter loss minima that generalize better to unseen conditions. Inconsistent dataset labels required building a normalization pipeline, while the small conveyor dataset pushed us toward efficient architectures like YOLOv8-nano. Three-phase progressive training preserved pretrained knowledge while adapting to plastic classification, and confidence thresholding let us gracefully handle uncertainty. While the initial clean-test performance was excellent at 98.8%, the real-world gap taught us invaluable lessons about the importance of domain-specific data and robust optimization strategies, challenges we successfully addressed through principled engineering rather than shortcuts.

Team **kabo** -- [Kashish Mandhane](https://github.com/KashProgramming), [Lokesh Sahuji](https://github.com/lokesh-3s), [Durvi Bangera](https://github.com/durvibangera), [Ishita Singh](https://github.com/ishitahq)

`2026-03-26`

---

### EcoScan
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecoscan-8dc4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SwarikaaM/CodeRescue_hn4) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> AI-driven plastic recognition.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

Plastic waste is one of the most critical environmental challenges due to its non-biodegradable nature and long-lasting ecological impact. Efficient recycling relies on correctly identifying plastic types, but most recycling facilities still depend on manual sorting, which is:

**Slow** – processing large volumes of waste takes significant time.
**Labor-intensive** – requires continuous human effort for inspection.
**Error-prone** – dirt, deformation, or visually similar plastics often cause misclassification.

Consequences of incorrect sorting include contamination of recycling streams, lower-quality recycled materials, and reduced economic value of plastics.

Our project provides an AI-powered system that automatically classifies plastic waste from images, delivering:

- Faster and more accurate recycling
- Reduced human effort and errors
- Improved quality of recycled materials
- A scalable solution for sustainable waste management


This system leverages computer vision and machine learning to handle real-world conditions like dirt, deformation, and lighting variations, making recycling safer, smarter, and more efficient.

**Workflow:**

![image](https://assets.devfolio.co/content/f9e2b9be261c46dc89e1cae9fc107a60/6f4800d7-68e1-46db-97f7-6a84ba99efa0.png)

**Challenges we ran into**

**1. Low accuracy on real-world images**
- Model performed well on clean dataset images but struggled with dirty, deformed, or poorly lit waste.
- Solution: Applied data augmentation (rotation, brightness, noise) and used transfer learning to improve generalization.

**2. Visually similar plastic types**
- Categories like PET and HDPE were hard to distinguish, leading to misclassification.
- Solution: Fine-tuned model architectures and optimized hyperparameters for better feature extraction.

**3. Model overfitting**
- The model started memorizing training data instead of learning patterns.
- Solution: Used regularization techniques, validation checks, and improved dataset diversity.

**4. Backend integration issues**
- Difficulty in connecting the trained model with the frontend for real-time predictions.
- Solution: Built a FastAPI backend and created efficient API endpoints for image uploads and inference.

Team **CodeRescue** -- [Sharanya Pillai](https://github.com/sharanyaa23), [Swarika Maurya](https://github.com/SwarikaaM), [Nikita Mulam](https://github.com/NikitaMulam2005)

`2026-03-26`

---

### AaharIQ
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aahariq-7d93) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SarveshTikekar/SAASukeClan_hn4) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> Market noise to restaurant moves, decoded.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Django](https://img.shields.io/badge/Django-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

In the current landscape, a single viral Reddit thread or a sudden dip in Google Maps ratings can determine whether a restaurant thrives or closes. While most owners are flooded with data, they lack the time to translate "social chatter" into a winning business strategy.
**AaharIQ** acts as a bridge between fragmented digital noise and decisive physical action. People can use it to:

- **Exit "Reactive Mode"**: 
Instead of panicking after a negative trend goes viral, owners use Real-Time Social Listening to detect early warning signals and address service "defects" before they escalate

- **Automate Professional Consulting**: 
It eliminates the need for expensive manual audits by instantly populating 8 Strategic Frameworks (like SWOT, PESTEL, and the BCG Matrix) using live data from Google Reviews, Zomato, Magicpin, and niche foodie communities.

- **Master the Hyperlocal Market**: 
Managers can stop guessing what the competition is doing. The platform provides Competitor Benchmarking, allowing a side-by-side performance comparison against local rivals to identify exactly where they can reclaim market share.

- **Bridge the Boardroom Gap**: 
For enterprise-level hospitality groups, it transforms messy web data into "Boardroom-Ready" PDF reports. These reports use coordinate-based precision to present high-contrast visuals that justify strategic pivots to stakeholders.

**AaharIQ** takes the "guesswork" out of hospitality. It makes the task of market analysis faster, competitive positioning sharper, and reputation management effortless, allowing restaurateurs to focus on what they do best: serving great food and providing a quality experience.

**Challenges we ran into**

Building a high-fidelity platform like **AaharIQ** in the 2026 hospitality climate came with significant technical and strategic hurdles. Here are the primary challenges we navigated to ensure the platform met the rigorous "Restaurant Oracle" requirements:

- **The "Cold Start" Data Problem**: 
We encountered severe review scarcity for newer or niche suburban restaurants. To overcome this, we implemented a Triangulated Delta Mapping engine that compensates for low volume by analyzing the broader "hyperlocal mean" of the sector.

- **API Volatility (Featherless.ai)**:
 During the integration of the required unique AI features, we faced the expiry of the provided Featherless.ai API key. We pivoted by building a modular intelligence layer that allowed us to swap in temporary inference mocks to maintain the "Insight-to-Action" flow until the enterprise credentials were restored.

- **Meta’s Walled Gardens**: 
Extracting clean data from Facebook and Instagram proved impossible without risking account bans due to gated models and aggressive anti-scraping measures. We made the strategic decision to exclude Meta sources to protect account integrity, instead deepening our integration with Zomato and Swiggy APIs to ensure "Traceable" and "Audit-Ready" intelligence.

- **The Global vs. Hyperlocal Paradox**:
 Balancing broad market trends with "street-level" signals was a perilous balancing act. We resolved this by engineering a Strategic Intelligence Matrix that filters macro-environmental data (PESTEL) through a hyperlocal discovery engine, ensuring the "Offensive Tactics" remained relevant to the restaurant's specific zip code.

- **Framework Complexity**:
 Populating 8 distinct strategic frameworks (like VRIO and Six Sigma) from fragmented social chatter was a massive logic hurdle. We moved beyond simple word clouds by using MECE Problem Architecture to ensure every customer complaint was deconstructed into mutually exclusive, actionable categories.

Team **SAASukeClan** -- [Sarvesh Tikekar](https://github.com/SarveshTikekar), [Ketan Shelke](https://github.com/ketanshelke97), [Mangesh Gautam](https://github.com/Gautammangesh), [Arkaprabha Ghosh](https://github.com/Hrickthegeek)

`2026-03-26`

---

### AI-BASED PLASTC WASTE TYPE AND GRADE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aibased-plastc-waste-type-and-grade-identification-28c8) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/103Chj6MahjKxdfADAdpv0F-iftarRQlN?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> Turning Waste into Wisdom

![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

1. Smart Recycling 
Automatically identifies plastic types (PET, HDPE, LDPE, PP, PS, Others) in real time.

Reduces human error in manual sorting.
Ensures cleaner, higher-quality recycled materials.

2. Environmental Monitoring 
Detects plastics in rivers, beaches, and public areas.

Tracks plastic pollution quickly.
Helps plan clean-up and recycling strategies.

3. Education & Awareness 
Shows how different plastics are recycled.

Useful for schools, colleges, and workshops.
Teaches proper segregation in an interactive way.

4. Industrial Automation & Safety 
Integrates with conveyor systems to sort plastics automatically.

Prevents contamination in production lines.
Makes handling hazardous plastics safer.

Team **404 Error Not Found** -- [Soundarya Kolte](https://github.com/SoundaryaKolte?tab=repositories), [Shreya Chavan](https://github.com/Shreyachavan15), [Vaishnavi Nagane](https://github.com/nagane09)

`2026-03-26`

---

### WasteLens
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wastelens-345b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hi-karanb/TSM_Entity_hn4) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> clean india green india

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square)

**The problem it solves**

WasteLens AI is an intelligent recycling and waste management platform that simplifies complex operations through automation and AI. It helps industries, recycling units, and vendors efficiently track materials from purchase to processing and dispatch, reducing manual errors and improving transparency.

The platform makes tasks easier by enabling natural language input, where users can simply type or speak data instead of filling long forms. Its multi-step workflows guide users through processes like tracking processed and lost material, ensuring accurate calculations and validation.

With AI-powered analytics, users gain real-time insights into efficiency, loss percentage, and vendor performance, making decision-making faster and data-driven. The multi-agent system automates tasks like data extraction, analysis, and anomaly detection.

Additional features like image-based waste classification, QR-based batch tracking, and a marketplace for trading materials enhance usability and traceability. Overall, it improves operational efficiency, reduces waste loss, and supports sustainable practices.

**Challenges we ran into**

so there were deployment issues on the vercel when i was deploying and there was connection of backend and frontend issues which we later resolved

Team **TSM Entity** -- [Karan Banerjee](https://github.com/hi-karanb), [Faiz Moulavi](https://github.com/faizzz11), [Aaditya Mourya](https://github.com/mouryaaditya20), [SHREY MISHRA](https://github.com/SHREY275)

`2026-03-26`

---

### mergeinfinity
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mergeinfinity-ba16) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EmaadAkhter/MergeInfinity_hn4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://frontend-inky-gamma-68.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackNiche%204.0-0052CC?style=flat-square)](https://hackniche4-0.devfolio.co)

> AI-Based Plastic Waste Type & Grade Identification

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Vercel](https://img.shields.io/badge/Vercel-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Render](https://img.shields.io/badge/Render-333333?style=flat-square)

**The problem it solves**

Plastic waste is rarely sorted correctly — most people can't identify plastic types (PET, HDPE, PP, etc.)
Recyclers lose value due to mixed/misgraded plastic inputs
No accessible tool exists for real-time plastic identification at the consumer level
Leads to increased landfill waste and lost recycling revenue

**Challenges we ran into**

Training a lightweight CNN (MobileNetV3) with high accuracy on limited plastic image data
Balancing model size vs accuracy — final model is only 5.9MB at 80.87% accuracy
LLM API reliability — implemented Featherless AI → Qwen fallback chain
MongoDB async integration with FastAPI without blocking inference
Deploying model on Render with cold start latency issues

Team **MergeInfinity** -- [Ayaan Shaikh](https://github.com/Ayaanshaikh12243), [Emaad Ansari](https://github.com/EmaadAkhter)

`2026-03-26`

---

### emission-watchdog
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/emissionwatchdog-1917) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://emission-watchdog-codex-frontend.onrender.com/) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co)

> From AQI number to guilty party — automatically.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Leaflet.js](https://img.shields.io/badge/Leaflet.js-333333?style=flat-square)

**The problem it solves**

Millions breathe toxic air daily in Delhi. Tools like IQAir show you a number. 
Nobody tells you *who caused it, when it will happen again, or what it's doing to your body.*


### What's missing from existing tools

- *IQAir / AQI Now* — shows current AQI, no history, no attribution
- *CPCB Dashboard* — raw sensor data, no pattern detection
- *Google Maps* — eco-routing for cars, nothing for pedestrians
- *None of them* identify which industry is responsible

### Who suffers

- *Residents* — don't know why pollution spikes or when it will happen
- *Parents* — can't decide when it's safe for children to go outside
- *Regulators* — no automated system to catch repeat industrial violators
- *Journalists* — no tool to investigate environmental accountability

### What Emission Watchdog does

We built an *accountability engine*, not a monitoring dashboard.

- Detects anomalous pollution spikes using rolling Z-score analysis
- Proves spikes follow a weekly schedule using chi-squared statistical testing
- Attributes spikes to nearby industries using 4 signals: distance, wind direction, pollutant profile, and operating hours
- Predicts next spike up to 24 hours in advance
- Translates AQI into human terms — "breathing this air = smoking 15 cigarettes today"
- Tracks how many days per month each area violated CPCB legal limits
- Sends automated email alerts to regulators when a severe spike is detected


### The core discovery

*Pollution spikes in Delhi follow weekly schedules.*

- Mundka: every Wednesday 8pm
- Siri Fort: every Wednesday 4am  
- Delhi city-wide: every Sunday 3am

Statistically proven on real CPCB data (p < 0.001). A 4am Wednesday spike is not 
traffic. It is not weather. *It is a scheduled industrial activity — and now we can prove it.*

**Challenges we ran into**

### 1. No free historical AQI data existed

Our entire project depends on detecting patterns over time — but WAQI's free API 
only gives current readings. We tried three sources before finding one that worked:

- *WAQI historical API* → requires paid plan. Dead end.
- *OpenAQ API* → changed to require API keys mid-build, then rate-limited us. 
  Pulling 1 year of hourly data for 13 stations would have taken 6+ hours.
- *Kaggle CPCB Dataset* → finally found 219,125 real hourly readings from 5 NCR 
  cities. Free, official government data.

We wrote a custom importer to load it into our database — and the Sunday 3am spike 
pattern we discovered is a genuine statistical finding on real CPCB data.

### 2. Attribution was scientifically weak

Our first version attributed spikes using only proximity — "closest factory is 
responsible." A mentor pointed out this is guesswork, not evidence.

*Fix:* Rebuilt attribution with 4 independent signals:
- *Distance* (25%) — GPS proximity via Haversine formula
- *Wind alignment* (30%) — is the facility upwind at spike time?
- *Pollutant fingerprint* (25%) — does the chemical profile match the facility type?
- *Schedule match* (20%) — does spike timing match known operating hours?

Four converging signals is evidence. One signal is guesswork.

**GreenTech**

The GreenTech track asks for software solutions that improve **sustainability, 
environmental awareness, and efficient resource usage.** Emission Watchdog 
addresses all three directly:

- **Environmental awareness** — we don't just show AQI numbers, we prove *who* 
  is causing pollution, *when* they do it, and *how often* — turning passive 
  awareness into actionable accountability
- **Sustainability** — by identifying repeat industrial violators with statistical 
  proof, we create a tool that can drive real regulatory action and force polluters 
  to clean up operations
- **Resource usage** — regulators currently spend enormous time manually reviewing 
  sensor data to identify violations. Our system automates this entirely — one API 
  call delivers a statistically proven case for inspection

Team **codex123** -- Kunal Maka, [Nishant Sharma](https://github.com/Nishant-NITG)

`2026-03-22`

---

### GreenO
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/greeno-ccfb) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1CFHUhSmxoOEWhH29c88z5MoY9SV8WhTB/view?usp=drive_link) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/wEKyCYb84_0) [![Built at](https://img.shields.io/badge/Built%20at-DotSlash%209.0-0052CC?style=flat-square)](https://dotslash-9.devfolio.co)

> Orchestrate your energy

![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Prism.js](https://img.shields.io/badge/Prism.js-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square) ![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Razorpay API](https://img.shields.io/badge/Razorpay%20API-333333?style=flat-square) ![Reinforcement learning](https://img.shields.io/badge/Reinforcement%20learning-333333?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-333333?style=flat-square)

**The problem it solves**

GreenO solves a critical challenge facing modern manufacturing: **how to maximize renewable energy utilization while optimizing operational costs and minimizing carbon footprint in real-time**.

**For factory operators and energy managers:**
- **Real-time Energy Routing**: Intelligently directs solar power to HVAC systems, essential machinery, and battery storage based on instantaneous grid prices and carbon intensity
- **Automated Optimization**: Eliminates manual energy scheduling guesswork with RL-driven agents that continuously learn and adapt to operational patterns
- **Cost Savings**: Arbitrage opportunities between battery storage and grid pricing can reduce energy costs by 20-30%
- **Carbon Accountability**: Tracks grid carbon intensity and prioritizes renewable consumption, supporting ESG reporting and regulatory compliance
- **Subscription-Protected Analytics**: Enterprise-grade analytics dashboards with real-time SSE streaming, protected subscription verification, and audit trails for compliance

**Without GreenO**: Factories either overspend on grid energy, underutilize solar capacity, or rely on static rule-based systems that can't adapt to market changes. With GreenO, energy decisions become **intelligent, data-driven, event-driven, and continuous**.

**Challenges we ran into**

### **Challenge 1: RL Model Training for Time Series Data & Data Leakage Prevention**

**Problem**: Training RL agents on factory energy time series introduced critical data leakage:
- **Future Information Leakage**: Agents saw future grid prices and solar output, making decisions unrealistically perfect
- **Temporal Dependencies**: During training the timeseries data is continues in timestamp but in our system the infranceing of RL agent is uneven.
- **Distribution Shift**: Training on 2023 data vs. 2026 production patterns with different renewable penetration
- **Episode Boundaries**: Day/night cycles and factory operating hours were ignored

**Solution**: Strict temporal validation framework:

1. **Time-Aware Data Splitting**: 
   - Training: Jan-Aug 2023 | Validation: Sep-Oct 2023 | Test: Nov-Dec 2023 (sine of temporal features)
   - Temporal boundaries enforced in `greeno_orchestrator.onnx`

2. **Causal Windowing**:
   - Agent observes only current window
   - Future features (solar_forecast, grid_price) explicitly excluded
   - Realistic 3-5 ms action latency

3. **Episode Segmentation**:
   - Split trajectories at midnight (reset battery assumptions)
   - Separate training for peak (06:00-22:00) vs. off-peak (22:00-06:00) hours
   - Stratified sampling across seasons

4. **Distribution Shift Mitigation**:
   - `norm_stats.npz` stores 2023 mean/std with monthly retraining triggers
   - Novelty detection for out-of-distribution states (>80% solar penetration)

5. **Validation Metrics**:
   - Leakage detector: Evaluate on shuffled future timesteps (performance should drop)
   - Causality check: Mask future features and measure reward degradation
   - Production sim: Test on 2026 data with distribution shifts

---

### **Challenge 2: Real-time RL Orchestration with Event-Driven Architecture**

**Problem**: Integrating ONNX-based RL models with real-time decision-making across a distributed event bus required careful orchestration. The RL agent needed to:
- Process streaming telemetry data without blocking
- Generate optimized decisions within <100ms
- Propagate decisions through Kafka for async consumption
- Handle variable input states (weather, grid prices, battery SOC)

**Solution**: Implemented an **event-driven orchestration pipeline**:
1. Telemetry events trigger RL inference via FastAPI
2. Decision events published to Kafka topic
3. Express backend consumes decisions from Kafka consumer group
4. Real-time decision streaming to frontend via SSE

Used ONNX Runtime for sub-10ms inference and normalized state preprocessing (SB3 epsilon clipping) to handle edge cases.

---

### **Challenge 3: Kafka Integration for Decision Propagation**

**Problem**: Kafka consumer lag and exactly-once semantics were critical since energy decisions can't be missed or duplicated.

**Solution**: Implemented consumer groups with offset management:
- Each RL decision assigned unique monotonic timestamp
- DuckDB stores decision outcomes for idempotency checks
- Graceful handling of late-arriving events (within 5-minute window)
- Monitoring dashboard tracks Kafka lag across producers/consumers

This ensured **100% decision delivery** without duplication across concurrent streams.

**GreenTech**

GreenO is a **real-time RL-driven energy orchestration platform** that directly addresses the GreenTech challenge of optimizing renewable energy utilization in manufacturing.

### Environmental Impact
- **Carbon Reduction**: Maximizes solar/wind consumption during generation peaks, reducing reliance on grid carbon-intensive power
- **Demand-Side Management**: Smart battery/load orchestration shifts heavy operations to renewable-rich periods, cutting facility carbon footprint
- **Grid Stabilization**: By predictably consuming renewable energy, GreenO reduces wind/solar curtailment waste

### Core Innovation
Our ONNX-based RL agent learns optimal energy routing decisions by observing:
- Real-time solar/wind generation
- Grid carbon intensity (time-varying mix)
- Battery state & thermal inertia
- Factory operating patterns

The system maximizes **renewable energy utilization**.

Team **Concurrents** -- [Devan Chauhan](https://github.com/Devan019), [Zeel Javia](https://github.com/ZeelJavia), [Milan Bhadarka](https://github.com/milanbhadarka), [Manil Modi](https://github.com/ManilModi)

`2026-03-22`

---

### JunkIn
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/junkin-12f5) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sajeed69/JunkIn) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://junkin-seven.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co)

> AI-Powered Recycling & Resale,Turn Junk Into Value

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JWT](https://img.shields.io/badge/JWT-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

JunkIn is a production-ready, scalable hybrid platform that maximizes the value of unwanted items through a dual-mode approach: Reuse (Marketplace) and Scrap (Recycling).
Powered by an AI Decision Engine, JunkIn analyzes every item to recommend whether it should be sold to a neighbor or professionally recycled for its material value.
🚀 Key Features
AI-Driven Decision Engine: Instantly analyzes items (images/text) to provide resale and scrap value estimates.
Rare Item Detection: AI-powered rarity analysis that performs web searches to identify high-value/limited-edition items for collectors.
Collector Bidding Marketplace: Dedicated auction-style platform where verified collectors can bid on rare items detected by AI.
Eco Rewards Gift Card System: Gamified incentive system where users earn Eco Points for sustainable actions and unlock scratch cards for digital gift cards.
Dual-Mode Marketplace:
Reuse Mode: Peer-to-peer marketplace for functional items.
Scrap Mode: Scheduled professional pickups for recyclables with transparent pricing.
Kabadiwala Interface: Dedicated dashboard for scrap collectors with real-time request tracking and digital receipts.
Admin Control Panel: Full platform monitoring, commission management, and scrap rate configuration.
Digital Receipts: Automated PDF generation for every scrap transaction.
Environmental Impact Tracking: CO2 savings calculation for every item diverted from landfills.
Requestly API Client Integration: Built-in API interception tool for real-time market simulation and dynamic recommendation testing.

**Challenges we ran into**

For the JunkIn hybrid reuse–scrap platform, the three major challenges you can mention are:

1. AI Decision Engine Accuracy

The biggest challenge was designing the AI model that decides whether an item should be reused (sold) or scrapped.

Many items have uncertain conditions from images.

Some items have both resale and scrap value, making classification difficult.

Limited datasets for training models on second-hand or waste items.

2. Real-Time Price Estimation for Scrap Materials

Scrap values depend on dynamic market prices of metals, plastics, and electronics.

Prices change frequently across locations.

Maintaining accurate and updated scrap rates required building an admin system to configure rates dynamically.

Incorrect pricing could affect user trust in the platform.

3. Integration of Dual Marketplace System

The platform combines two completely different workflows:

Peer-to-peer resale marketplace

Scrap pickup and recycling logistics

Building a system where the AI automatically routes items to the correct mode while maintaining a smooth user experience was technically complex.

**Creative Use of Requestly**

Requestly API Client — Feature & Usage
JunkIn integrates a built-in Requestly-inspired API Client that allows real-time interception and modification of backend API responses. This enables dynamic market simulation without changing any backend code.

🎯 Purpose
The Requestly API Client demonstrates how real-time market data changes directly affect JunkIn's AI recommendation engine. By intercepting API responses, users can simulate scenarios like scrap price surges or demand crashes and watch the AI recommendation update live.
📖 How to Use
Step 1: Open AI Analysis Page
List an item on JunkIn → Navigate to the AI Analysis results page.
You'll see the Live Market Rates card showing current scrap prices.
Step 2: Enable Simulation Mode
Toggle the "Simulation Mode" switch in the top-right header.
This reveals the Future Value Simulator panel with 3 scenario buttons.
Step 3: Run a Scenario
Click any scenario (e.g., "Scrap Market Price Surge").
Watch the Today vs Future Scenario comparison appear instantly.
The AI recommendation dynamically recalculates based on modified prices.
Step 4: Use the Requestly API Client (Advanced)
From the AI Analysis page (with Simulation Mode ON), click "OPEN API CLIENT".
This opens the full Requestly API Client interface at /requestly-client.
Select an endpoint from the sidebar (e.g., Scrap Prices).
Edit the JSON response body with custom values.
Click "Save & Intercept" to mock the API response.
Return to the AI Analysis page — your custom data is now active.
Step 5: Observe Reactive Changes
Open your browser DevTools Console (F12 → Console tab).
Look for green [REQUESTLY DEMO] and [REQUESTLY CLIENT] log messages.
These show exactly how intercepted data flows through the recommendation engine.

![image](https://assets.devfolio.co/content/c0cfa8de67bd4bebb9692b010b3e36a4/d5abe9f0-94f7-4b6f-a808-1e1cc512d5a6.png)

![image](https://assets.devfolio.co/content/c0cfa8de67bd4bebb9692b010b3e36a4/6e6afcb9-585c-4268-959c-cd7d305ce81c.png)

Team **Kaizen** -- [Divyanshu Raj](https://github.com/divyanshuraj1095), [Sajeed Ahmed](https://github.com/sajeed69), [Sankalp Suman](https://github.com/s8sankalp)

`2026-03-16`

---

### EcoLedger
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecoledger-f6dc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hrishitashenvi144/Team_Smash) [![Built at](https://img.shields.io/badge/Built%20at-Hack--Nocturne%202.O-0052CC?style=flat-square)](https://hack-nocturne-2.devfolio.co)

> Scrap to Supply

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

ScrapToSupply

Turning industrial waste into opportunity.
A platform that connects businesses with surplus materials to businesses that can reuse them, while calculating the environmental and economic impact of that reuse.

Problem:
Industries generate large amounts of surplus and waste materials every year.
Most of this waste ends up in landfills even though many of these materials could still be useful to other businesses.

There is currently no simple system that helps industries discover, exchange, and evaluate the impact of reusing these resources.

Solution:

ScrapToResource is a platform that enables businesses to:

- List surplus or waste materials
- Discover usable resources from other businesses
- Exchange these materials instead of discarding them
- Calculate the environmental and economic impact of reuse

The system promotes industrial symbiosis and circular economy practices.

Key Features

Waste / surplus material listing
Resource discovery between businesses
Environmental impact estimation
Economic value estimation
Landfill reduction tracking
Dashboard visualization of impact metrics
Impact Metrics Calculated

The platform estimates three key sustainability indicators:

1.CO₂ Emissions Saved
Estimated emissions avoided by reusing waste instead of producing new raw materials.
2.Landfill Reduction
Amount of waste diverted from landfills through reuse.
3.Economic Value Generated
Estimated market value created by converting waste into usable material.

How It Works

A business lists a surplus resource (type, quantity, location).
Other businesses can view and request the resource.
When the material is reused, the system calculates:
CO₂ saved
landfill reduction
estimated economic value

These values are calculated using resource-specific impact factors.

Tech Stack

Backend:
Python
FastAPI

Frontend:
React

Database:
MongoDB

AI / Data Component:
Python-based impact estimation model

Example Scenario:

A furniture manufacturer generates 500 kg of wood scrap.
Instead of sending it to a landfill:
A packaging company claims the material.

The system estimates:
CO₂ emissions saved
landfill waste avoided
economic value generated

This transforms waste into a usable resource.

Future Improvements:

Real-time industry matchmaking
Logistics optimization
Verified environmental impact datasets
AI-based waste-resource matching
Industry-specific material marketplaces

Team **SMASH** -- [Hrishita S](https://github.com/hrishitashenvi144), [MAMTHA D](https://github.com/dmamtha9468-sudo), [P Saranya](https://github.com/SaranyaPadala), [Samiksha Singi](https://github.com/Samikshagit-07)

`2026-03-16`

---

### S.A.R.A.
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sara-8693) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/johanesronin22/SARA) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAHEMqbkwRE/14zdBI_o4OLMIxcdyAXfPA/edit?utm_content=DAHEMqbkwRE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/76d7675a463c4b77a0abb92005f4ecdc) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Stock Analysis and Recommendation AI

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Beginners often struggle to invest in stocks due to confusion, fear, and lack of proper guidance, and this is exactly where SARA steps in. The stock market can feel overwhelming, filled with complex terms, data, and charts that are difficult to understand without prior knowledge. Many people don’t know how to choose the right stocks or even grasp basic financial concepts, creating a strong barrier to entry. On top of that, the fear of losing money discourages them from starting, while those who do invest often make emotional decisions, buying at high prices out of excitement or selling during market drops out of panic. Most available advice online is generic and not tailored to individual needs, leaving users without personalized direction based on their budget, goals, or risk tolerance. Additionally, beginners usually lack the time and expertise to research companies and market trends, making informed decision-making even harder. There is also no clear strategy for when to buy, sell, or hold investments, and trust issues arise when users are asked to rely on random tips without proper explanations. SARA solves all of these problems by acting as an intelligent, beginner-friendly financial companion, simplifying complex information, offering personalized recommendations, reducing emotional bias with data-driven insights, and making the entire investing process easy, transparent, and accessible for everyone.

**Challenges we ran into**

Building SARA came with a few key challenges, such as simplifying complex financial data for beginners, ensuring the AI gives accurate and personalized recommendations, and designing a clean, easy-to-use interface. We also had to be careful to provide responsible insights without misleading users, all while working within tight hackathon time constraints.

Team **FinNova** -- Anagha Mithra, Sravan Salimkumar, amodini A, Johanes Aryo Noegroho

`2026-03-17`

---

### Waste Wise
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/waste-wise-5eb7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Natansh11/WasteSort) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://waste-wise1.vercel.app/insights) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/f2e797ba7e2e44d6bef7f1eee41f7fb8) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> identifies recyclable materials and contamination

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

Team **TP306** -- C Vaishnavi, Natansh Natansh

`2026-03-17`

---

### FocusTube
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/focustube-debc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Vanshika490/FocusTube/tree/pr-changes) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Optimized YouTube Learning Environment

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

The Problem:
Students use YouTube to learn but YouTube is built to keep you watching, not learning. There's no study mode, no intent tracking, no accountability. A student opens YouTube to study DSA and 40 minutes later they're watching Silicon Valley or The Imitation Game — not because they're lazy, but because the platform has no concept of their goal.

What FocusTube Solves:
A focused study companion that sits on top of YouTube — you set a goal, it finds the best educational content, tracks your session timer, detects the moment you drift off topic using AI, and quizzes you at the end to reinforce learning

**Challenges we ran into**

1. Stateless backend losing goal context
The biggest one. Every search request was stateless so goal and session_id were undefined on the backend. Gemini had nothing to compare against so classification never fired. Fixed by persisting goal server-side in sessionGoals{} and generating a UUID session_id in localStorage on the frontend.
2. Gemini analysis silently failing
The catch block only logged err.message — when Gemini returned malformed JSON the error was swallowed completely with no visibility. Fixed by logging the raw Gemini response before parsing and making the JSON extraction non-greedy.
3. Zero results blocking Gemini
When a query like "taylor swift" returned 0 educational results after filtering, the condition finalResults.length > 0 prevented Gemini from running at all — so off-topic searches never got flagged. Fixed by moving Gemini analysis before the YouTube fetch entirely, making it query-based not result-based.
4. buildQueryWithGemini polluting searches
An earlier version appended suffixes like "lecture explained tutorial" to every query via Gemini. This hurt result quality and added unnecessary API latency. Removed entirely — raw query now goes straight to YouTube.
5. MODULE_NOT_FOUND crash on startup
@google/generative-ai was used in quiz.js but not installed in the Backend's node_modules. Fixed with npm install @google/generative-ai in the Backend folder.

**Google Cloud**

FocusTube uses Gemini API as its core intelligence in two ways:
1. Real-time Rabbit Hole Detection
Every search query is sent to Gemini along with the user's study goal and session history. Gemini classifies intent as on_topic, related_educational, rabbit_hole, off_topic, or entertainment. This isn't a keyword filter — it's contextual reasoning. Gemini understands that "the imitation game" is a Turing biopic and a rabbit hole for a DSA student, while "turing machine tutorial" is on topic. No hardcoded rule could make that distinction. Session history is passed with every call so Gemini gets smarter about repeat offenses within the same session.
2. Dynamic Quiz Generation
After each session Gemini generates a fresh 5-question quiz tailored to exactly what the user watched — not a static question bank.
Why it fits the Gemini track:
The entire product value depends on Gemini being right. It's not a feature — it's the reason the product works. Without Gemini, FocusTube is just a YouTube search bar.

Team **Nullptr** -- [Vanshika Sharma](https://github.com/Vanshika490), [Rakhi Badhan](https://github.com/Rakhi-web579), [Zulikha Banoo](https://github.com/zulikha-star)

`2026-03-15`

---

### VanDoot
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vandoot-b3a0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mansi249/Vandoot_project) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a5oWSf7bEqA?si=gNKIsYsC1BSv-9Mc) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Messenger of Forest

![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

**The problem it solves**

Forests are difficult to monitor continuously due to their large geographical areas and limited connectivity. Traditional monitoring systems often rely on a single detection source such as cameras or smoke sensors, which frequently produce false alarms caused by environmental conditions like lighting changes, animal movement, or natural smoke sources. These false alerts waste valuable time and resources for forest rangers and can delay responses to real threats such as wildfires or illegal human activities.

Additionally, raw monitoring data collected from remote sensing systems is difficult to interpret at scale. Rangers and monitoring teams require tools that not only detect events but also help them understand long-term patterns in forest activity. There is a need for a system that can combine edge detection, sensor verification, and intelligent analysis to provide reliable alerts and meaningful insights for forest monitoring

**Electrothon 8.0 Honors Track**

BEST HARDWARE TRACK
VanDoot is fundamentally a hardware-driven system designed for real-world deployment in remote forest environments. The core detection layer runs directly on an ESP32-CAM microcontroller, where a lightweight TinyML MobileNet model performs on-device image classification to detect events such as fire, human presence, or animal activity. Running the model at the edge allows the system to operate in areas with limited or no internet connectivity while maintaining low power consumption.

In addition to the vision module, the system integrates multiple environmental sensors such as smoke, thermal, PIR motion, and audio sensors. These sensors provide additional environmental signals that help verify visual detections. A Random Forest model performs sensor fusion using these inputs to reduce false alarms and improve detection reliability.

By combining embedded AI inference, physical sensor integration, and edge-based decision making, VanDoot demonstrates a complete hardware-software monitoring pipeline. The hardware layer performs real-time detection and logging, while the cloud-based analytical layer uses Gemini to interpret long-term monitoring data and generate actionable environmental insights.

**Best Use of Gemini 3 [Google Deepmind]**

VanDoot uses the Gemini API as an intelligence layer that analyzes monitoring data generated by the edge detection system. The primary detection pipeline operates on hardware using an ESP32-CAM running a TinyML MobileNet model that classifies images into categories such as fire, human, animal, or empty scenes. In addition, environmental sensors such as smoke, thermal, PIR motion, and audio provide supporting signals. These inputs are combined using a Random Forest classifier to perform sensor fusion and verify potential threats while reducing false alarms.

The system logs significant monitoring events over time. Instead of presenting these logs as raw data, the Gemini API is used to analyze aggregated monitoring summaries and convert them into natural language ecological reports. Gemini processes the structured event statistics and generates explanations describing patterns such as wildlife movement trends, potential human intrusion, or indicators of wildfire risk.

The Streamlit dashboard serves as the interface where users upload or select monitoring logs, which are then summarized and sent to Gemini for analysis. By leveraging Gemini’s reasoning and natural language generation capabilities, VanDoot transforms low-level detection logs into actionable insights that can help forest rangers better understand environmental activity and respond to threats more effectively.

Team **VanDoot** -- [Hardik Matta](https://github.com/Hardikmatta), [Mansi Sangwan](https://github.com/Mansi249), [Aadrit Kuthialia](https://github.com/Aadrit-sys), [Gaurav .](https://github.com/gaurav2175)

`2026-03-15`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
