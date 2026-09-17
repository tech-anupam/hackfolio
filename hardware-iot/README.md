# Hardware and IoT

![Projects](https://img.shields.io/badge/Projects-39-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### Chintu
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/max-e3ab) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ASAC44/chintu) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://max.3-110-105-33.sslip.io/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0w4cCR9zJCQ) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-8-FF6B6B?style=flat-square)

> AI orders it. Robot brings it upstairs.

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![ONDC](https://img.shields.io/badge/ONDC-333333?style=flat-square) ![prava](https://img.shields.io/badge/prava-333333?style=flat-square)

**Challenges we ran into**

## Challenges we ran into

### WE ALMOST ABANDONED THE IDEA BECAUSE THE COMMERCE LAYER KEPT FAILING

Our original plan depended on the Zepto MCP. We had already connected the robot, Telegram, and the Prava payment flow, but repeated product searches and order-status checks kept hitting rate limits. It was incredibly frustrating to watch almost the entire system work while the mission still failed at its very first commerce request.

For a while, we genuinely thought we might have to drop the whole idea.

Instead, we spent time testing different commerce options independently and comparing how they behaved under repeated searches and polling. After trying multiple paths, Swiggy Instamart was the one that held up. It gave Chintu the live product discovery, checkout, order correlation, and delivery tracking needed for the complete journey.

We also stopped treating every marketplace response as a command. Chintu now persists and normalizes each update, correlates it with the exact order being tracked, and dispatches the robot only after receiving the verified arrival state.

### OUR PULLEY ACTUALLY BROKE

The most chaotic moment of the build was completely physical: the pulley mechanism broke while we were testing it with Chintu.

There was a brief moment of panic because this was the robot we had spent all our time putting together. Thankfully, Chintu was secured inside the platform and nothing happened to it. The robot survived, but we had to stop everything and rebuild the pulley structure under serious time pressure.

The replacement needed better alignment, stronger attachment points, and repeated testing with Chintu’s real weight. It was a reminder that hardware does not care whether the software works perfectly—one weak knot or badly aligned section can still stop the entire mission.

That failure reinforced why the pulley needed its own safety system. The rebuilt setup uses normally-closed limit switches, keepalive messages, maximum-travel timeouts, emergency stopping, and latched faults. If communication disappears or the expected limit is not reached, the motor stops instead of continuing blindly.

### MAKING AUTONOMOUS NAVIGATION WORK IN OUR ACTUAL HOSTEL

Our corridor is not a controlled robotics lab. People walk through it, lighting changes, obstacles appear, wheels slip, and the robot never lands in exactly the same position twice.

We combined visual SLAM with measured wheel odometry, AprilTag checkpoints, obstruction handling, motor watchdogs, and emergency stopping. This lets Chintu follow the mapped route while still refusing to continue whenever its physical state is uncertain.

The biggest lesson was that Chintu could not be built as separate shopping, payment, and robot demos. Every failure, from marketplace rate limits to a broken pulley, had to be handled as part of one continuous mission. It was chaotic, but every setback made Chintu more reliable and made us understand the system much more deeply.

**The problem it solves**

## The problem it solves

Instant delivery is only instant until it reaches the gate.

Chintu started with a very real college-student problem: our hostel gate is far away, we order small things while working on classes, assignments, projects, and hackathons, and none of us wants to stop everything just to walk all the way down and wait for a delivery. Sometimes we are busy. Sometimes it is late, raining, or we are tired. And sometimes, honestly, we are simply too lazy to make another gate run.

We realised that ordering was already easy. The unfinished part was getting the order from the gate to our room. So we put together Chintu, a small autonomous robot that completes that missing physical last mile for us.

We message Chintu on Telegram with what we need. It understands the request, finds the item on Swiggy Instamart, presents the exact product and price, and sends a Prava approval link. After we approve that, it completes checkout, tracks the order, and keeps us updated. When Swiggy confirms that the rider has actually arrived, Chintu rides its pulley platform downstairs, autonomously navigates to the hostel gate, collects the package, returns to the pulley, and brings it back upstairs.

People can use Chintu to:

- Collect groceries, food, daily essentials, and packages without interrupting their work.
- Avoid repeated gate runs in hostels, apartments, offices, and campus buildings.
- Help people with limited mobility avoid unnecessary movement between floors.
- Serve buildings where a conventional elevator is unavailable or unsuitable for a robot.
- Turn shopping, payment, tracking, and physical pickup into one continuous request.

Because Chintu moves and spends money, we designed it to fail safely. Every purchase requires explicit Prava approval for the exact item and amount. A Telegram message or an uncertain delivery update cannot start the robot. Chintu moves only after a verified arrival event, while visual navigation, obstruction detection, emergency stopping, motor watchdogs, pulley limit switches, keepalives, and travel timeouts protect the physical journey.

Most commerce agents stop after recommending or ordering something. Chintu stays responsible until the product physically reaches us, the people who were too busy, too tired, or just too lazy to walk and do the entire annoying drill everyday.

**Best Visa Intelligent Commerce Implementation**

Chintu demonstrates the principles of Visa Intelligent Commerce through a meaningful Prava integration centred on permission, control, transaction completion, and user trust.

![image](https://assets.devfolio.co/content/b32836db2e814aa0a06e7ddb3c099543/b6284027-e362-4231-9ed5-a6947426f785.jpeg)

Prava is not an additional payment button placed at the end of our product. It is the authority boundary between what the AI may prepare and what it may actually purchase. Chintu can understand the request, search Swiggy Instamart, compare options, and construct an exact quote, but it cannot spend until the owner approves that specific item, quantity, and amount through Prava.

The approval link is delivered privately through Telegram. Approval, decline, timeout, and unknown results are persisted as separate outcomes. Only a confirmed approval allows checkout to continue; every other result stops the purchase safely. Payment credentials are never exposed to the language model, Telegram, the dashboard, or the robot.

After authorization, Chintu uses the approved transaction to complete the Swiggy checkout and shows the resulting order state. The integration therefore reaches a visible commercial outcome rather than ending after creating a payment session.

The same permission model continues after payment. A completed transaction does not automatically authorize physical movement. Chintu separately verifies the correlated order’s arrival before dispatching the robot, while the Raspberry Pi independently decides whether local motion is safe.

This makes Chintu a practical example of AI-initiated commerce where the agent is useful and autonomous within clear boundaries, while the owner retains understandable control over money and physical action.

![image](https://assets.devfolio.co/content/b32836db2e814aa0a06e7ddb3c099543/098ab4d0-ad21-49e5-9133-626e3936c4b7.jpeg)

**Most Startup-Ready Product**

Chintu begins with a narrow but frequent problem: people in hostels, campuses, apartments, and offices repeatedly leave their rooms or workspaces to collect deliveries from a gate or lobby.

This is already a real behaviour with existing demand. Residents regularly order groceries and essentials through instant-commerce platforms, but the final journey between the building entrance and their room remains manual. Chintu completes that missing step without requiring users to learn a new shopping interface. They simply send a Telegram message.

The product already combines the components needed for a deployable experience:

- A private Telegram interface for requests, approvals, and updates.
- Live Swiggy Instamart discovery, checkout, and delivery tracking.
- Prava-powered purchase authorization.
- A persisted backend and Mission Control dashboard.
- An autonomous Raspberry Pi robot with visual navigation and obstruction safety.
- An ESP32-controlled pulley system for movement between floors.
- A physically demonstrated request-to-pickup workflow.

Our initial market is hostels and campus residences, where many users share a gate, deliveries are frequent, and installing one system can remove the same repeated inconvenience for an entire building. From there, the model can expand to co-living spaces, apartment communities, offices, and other managed properties.

A practical business model is installation plus recurring software, support, and maintenance for each property. Distribution can happen through hostel operators, universities, property managers, and co-living companies rather than acquiring every resident individually.

We also demonstrated founder commitment during the build: when our original commerce provider became unreliable, we tested alternatives and migrated to Swiggy Instamart; when the pulley broke, we rebuilt it and continued physical testing.

Chintu is not only a weekend interface. It is the beginning of an embodied last-mile service that can be installed, operated, and improved building by building.

**Agentic Commerce Hackathon**

Chintu demonstrates agentic commerce as a complete journey from human intent to a physical result.

A user can message Chintu on Telegram with a request such as “get me milk under ₹300.” OpenAI interprets the intent, Chintu searches Swiggy Instamart, selects a suitable product within the constraints, presents the exact item and price, and creates a Prava approval session. Once the owner approves, Chintu completes checkout, tracks the correlated order, and reports every important update through Telegram and Mission 

Chintu does not stop when payment succeeds. When Swiggy confirms that the rider has reached the gate, the same mission dispatches a Raspberry Pi robot. The robot travels between floors using its pulley platform, navigates to the gate, collects the package, and returns it to the owner. 

This creates a new form of commerce in which the agent remains responsible for the outcome after checkout. Discovery, decision-making, authorization, payment, delivery tracking, and physical fulfilment are connected through one persisted workflow rather than separate demonstrations.

Trust is built into every stage. Chintu cannot spend without approval for the exact purchase, uncertain provider states cannot dispatch the robot, and local hardware safety checks can refuse movement even after the backend creates a job.

Chintu turns a message into a completed transaction and then carries the result home.

Team **ASAC44** -- [Aniket Yadav](https://github.com/Aniket2812), [Mohit Madan](https://github.com/Mmadan128), [Vansh Gaur](https://github.com/kymibuilds), [Snow Sadh](https://github.com/Electromagneticradiation)

`2026-08-02`

---

### GridLOCK
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gridlock-72f3) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://demo.a-str.com) [![Built at](https://img.shields.io/badge/Built%20at-DOMINION%202026-0052CC?style=flat-square)](https://dominion2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-7-FF6B6B?style=flat-square)

> Re-engineering Defense

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Leaflet](https://img.shields.io/badge/Leaflet-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square)

**Challenges we ran into**

Few problems we ran into-
1) Raspberry pi based nodes stopped functioning - Resolution: Moved all data to a VPS 
2) Prototype Code issues - All night debugging.
3) Firebase would not sync - Disable Locked mode
4) Prototype logic issues - Reworked entire architecture

**The problem it solves**

GridLOCK is a defense intelligence tool used to bridge the existential gap caused in Defense industry due to the ENNORMOUS amount of data generated and how its impossible for human judgement to react intime.

We also focus on decentralized Sovereign setup rather than a Cloud based which give the country full rights to its data without the risk of Data leakage.

SENTINEL is our AI engine that ensure only relevant data is communicated, used and accounted for. It also sits as a judgment analytics tools where any decision you make is studied recorded and later used when required.

Team **Team A-Star** -- [Johith Pranav](https://github.com/Na), [Shaaz Mohammed](https://github.com/H), [Aditya Singh](https://github.com/Na)

`2026-09-03`

---

### AstroSync AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/astrosync-ai-b713) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SudhanvSK/Citadel_InnovationIRL) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1VPT_cB8tbz8Bhy0UBqBULwLlcQZGFqkW/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/da8057fdf94747dd9b9e0529c2f35758) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-5-FF6B6B?style=flat-square)

> Autonomous Spacecraft Health Intelligence

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![MQTT](https://img.shields.io/badge/MQTT-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

Spacecraft fault protection is deterministic and reliable — hard limit checks, fault trees, Safe Modes. What isn't reliable is everything after the trigger: explaining what a fault is, retrieving the right response, and knowing what to do when the known response fails. Apollo 13's alarm storm, Chandrayaan-2's light-delay lockout, and modern flight tests drowning in telemetry are all the same failure — human operators expected to mentally map dependencies and recall playbooks under extreme time pressure.
AstroSync AI closes that gap. A deterministic threshold triggers detection (same as real flight systems). XGBoost classifies the fault. A FAISS-retrieval engine pulls the matching response from an authored playbook, sourced and ranked. When that known response fails to resolve the fault in time, an LLM proposes new mitigation hypotheses — and every single one is checked against a hardcoded safety policy before it can reach the operator. The flagship moment: the AI proposes firing the thrusters, and the safety layer visibly rejects it.
Built on real hardware — an ESP32 reading a DHT22, MPU6050, and HC-SR04 — not just a simulation.

**Challenges we ran into**

- The raw/effective override split: Getting manual override values and live sensor data to coexist without fighting each other was the highest-risk bug in the whole architecture, solved by tracking both values per channel and only letting the live sensor overwrite the "effective" value when no override was active.
- MPU6050 clone chip incompatibility: The Adafruit MPU6050 library refused to initialize because the board's chip was a clone that failed the library's WHO_AM_I check, switched to MPU6050_light, which skips that check, and converted its units (deg/s, g) to match our schema (rad/s, m/s²).
- Networking on a phone hotspot: A DHCP-assigned IP for the ESP32 kept changing between reboots, fixed by targeting the hotspot's fixed gateway IP directly instead of the laptop's reassignable address.

Team **InnovationIRL** -- [Sagar Narasannavar](https://github.com/Sagar-58), [Sudhanv Kulkarni](https://github.com/SudhanvSK), [Aniruddh Naik](https://github.com/alderido46), [Abhishek Kuri](https://github.com/abhishek-kuri)

`2026-07-12`

---

### Safe Streets
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safe-streets-eeda) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jessica-ops-star/safestreets2.0.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://safestreets-two.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/yX83UEGJyxE?si=FGWi0edlAhqn1dJG) [![Built at](https://img.shields.io/badge/Built%20at-DOMINION%202026-0052CC?style=flat-square)](https://dominion2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Predict . Detect . Protect . Escape

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-333333?style=flat-square) ![Force sensitive resistor](https://img.shields.io/badge/Force%20sensitive%20resistor-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**Challenges we ran into**

While developing our smart safety wearable, we faced several challenges involving hardware, sensors, communication, and integration.

1. GPS Signal Acquisition

Initially, the GPS module had difficulty obtaining location information. GPS requires a clear signal and may take time to connect to satellites.

We solved this by testing the GPS module in an open area and verifying the serial communication between the GPS module and ESP32.

2. Sensor Calibration

The MPU6050 and FSR sensors produce different values depending on movement and pressure.

A major challenge was determining the correct threshold values to differentiate between:

Normal hand movement.
Normal pressure.
Possible forceful movement or danger.

We addressed this by testing the sensors multiple times and adjusting the threshold values.

3. Reducing False SOS Alerts

A single sensor could accidentally trigger an SOS during normal daily activities.

For example:

Running could create sudden movement.
Holding an object tightly could create high pressure.

To reduce false alerts, we combined multiple sensor inputs instead of relying on a single sensor.

The system also includes a 45-second cancellation period before automatically sending the final SOS alert.

4. Hardware Integration

Connecting multiple components to the ESP32 required careful planning.

The system integrates:

GPS
MPU6050
FSR sensor
Buzzer
SOS button
Wi-Fi communication

We tested each component individually before integrating them into the complete system.

5. Power Management

Some components, especially the vibration motor, require more current than an ESP32 GPIO pin can safely provide.

Therefore, a transistor-based driver circuit was considered for controlling the motor safely.

6. Hardware and Software Communication

Another challenge was connecting the physical wearable system with the software platform.

The ESP32 needs to:

Collect sensor data.
Process possible danger conditions.
Obtain GPS location.
Connect to Wi-Fi.
Send information to the software platform.

We addressed this by testing the hardware modules and Wi-Fi connection separately before planning the complete integration.

**The problem it solves**

Personal safety remains a serious concern, especially for women and minors who may face situations where they cannot immediately contact family members, friends, or emergency services.

Recent incidents of violence against minors, including the recently reported case involving a minor connected with the Greater Noida region, highlight the importance of faster and more accessible personal safety and emergency-response systems. The case also demonstrates how a victim may be unable to immediately communicate or ask for help during a dangerous situation.

According to the latest available National Crime Records Bureau (NCRB) Crime in India 2024 data, 4,41,534 cases of crimes against women were registered in India during 2024. This is approximately 1,210 registered cases per day, highlighting the continuing need for improved personal safety and faster emergency response mechanisms. The 2024 report is currently the latest published NCRB Crime in India report.

In many emergency situations, a person may not have enough time or ability to:

Unlock a mobile phone.
Make an emergency call.
Send their location manually.
Speak or ask for help.

Our project addresses this challenge through a smart wearable personal safety system.

The system continuously monitors multiple possible danger indicators using sensors:

MPU6050 detects sudden or unusual hand movement and forceful pulling.
FSR pressure sensor detects excessive pressure or tight gripping.
Voice input from the mobile application acts as an additional safety indicator.
A physical SOS button allows the user to manually trigger an emergency.
GPS obtains the user's real-time location.
ESP32 with Wi-Fi communicates the emergency information with the connected software platform.

When multiple danger signals are detected, the system identifies a possible emergency situation. A 45-second confirmation period helps reduce false alerts. If the alert is not cancelled, the system can trigger an SOS and share the user's location with the connected software platform.

Our solution aims to reduce the time required to request help and communicate location information during a possible emergency, especially when the user may not be able to operate a phone normally.

Team **CY-X SENTINELS** -- Keerrthana M, [Jeba Joshua](https://github.com/joshua77-prog), [LOKESHWARAN S](https://github.com/Lokesh2728-crypto), [Jessica Benno](https://github.com/Jessica-ops-star)

`2026-09-03`

---

### Freshative
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/freshative-db3d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/k0sarthak/Fresh-ative) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI-powered freshness monitoring with simulated IoT

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Iot](https://img.shields.io/badge/Iot-333333?style=flat-square) ![Express](https://img.shields.io/badge/Express-333333?style=flat-square) ![GOOGLE GEMINI API](https://img.shields.io/badge/GOOGLE%20GEMINI%20API-333333?style=flat-square)

**Challenges we ran into**

**Getting the working interface right.** The shipment form has a lot of conditional state — fertilizer/pesticide toggles, tag-input fields for multiple entries, geolocation lookup — and keeping all of that in sync with a clean, readable UI while it fed into a live results dashboard took several iterations before it felt right.

**Frontend-backend integration.** Wiring the shipment form through to the Express API, and then getting the live results dashboard (`details.html`) to correctly fetch and render the same shipment's data — including the QR-code-driven flow, where scanning a code should instantly pull up the right shipment — needed careful work on the API routes and response shapes so the frontend and backend stayed in sync as fields were added.

**Upgrading the AI analysis.** Getting Gemini to produce genuinely useful output was an iterative process. Early prompts returned generic, repetitive text; we refined the prompt to feed in the actual sensor telemetry (temperature/humidity/ethylene history, risk events like door-opened or cooling-failure windows) so the model could generate a specific risk assessment plus concrete, actionable preservation recommendations rather than boilerplate advice.

**The problem it solves**

Food companies often rely on artificial preservatives because they lack a way to continuously monitor storage and transport conditions. Freshative closes that visibility gap instead of masking it: it simulates IoT sensors tracking a shipment from farm to consumer, computes a live freshness score, and uses AI to turn the sensor data into plain-language reports and natural preservation recommendations.

**Key features:**
- Guided form to log a shipment's crop, fertilizer, pesticide, and preservative data
- Simulated IoT sensor engine generating temperature, humidity, and ethylene telemetry across normal, door-opened, cooling-failure, and refrigeration-restored conditions
- Live freshness score, risk level, and a chart cycling between Temperature / Humidity / Ethylene
- Gemini-generated shipment analysis and natural preservation recommendations
- Auto-generated QR code linking to a shipment's live results dashboard
- Consumer-facing results page showing full shipment history and the AI report

Team **Smart Spoon** -- saksham manchanda, Keshav Sikka, Kunal Singh, Prateek Gupta, [Sarthak Gupta](https://github.com/k0sarthak)

`2026-08-16`

---

### Sprocket
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sprocket-fdee) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/spikonado/sprocket) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://spikonado.com) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> The AI agent for both hardware and software dev

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Rust](https://img.shields.io/badge/Rust-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![OpenAi](https://img.shields.io/badge/OpenAi-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Svelte](https://img.shields.io/badge/Svelte-333333?style=flat-square) ![Electron JS](https://img.shields.io/badge/Electron%20JS-333333?style=flat-square)

**Challenges we ran into**

### Who am I?

I am a **16 y/o** developer who loves building, learning about and using new things in tech.

### Hurdles I Faced

- **Best one:** Initially, the agent created very poor schematic drawings; to fix this, I told the agent what it was doing wrong and manually edited its schematic. I then told it to write its learning into a SKILL.md and repeated this loop.
- It was really hard to find good browser APIs to integrate with for the agent to shop on any website. After a lot of testing, I ended up going with Browserbase's stagehand.
- The agent being willing to order from fraudulent websites became a problem. I fixed this by explicitly telling it to check reviews of every supplier.

**The problem it solves**

### Short Description

Sprocket is an end-to-end agent for hardware and software development.
It allows anyone to take a hardware and/or software idea and turn it into a working prototype.

### Problem Solving For Devs

Similar to existing coding agents, but now hardware is also something that can be streamlined.

### Problem Solving For Normal Consumers

We often want very niche apps or electronics products in our daily lives that aren't available in the market at a low price. Sprocket solves that by allowing you to create those products with a single prompt.

### Differentiators from Other Products

- Sprocket conducts a thorough web search for every detail it could get wrong, decreasing hallucinations and increasing reliability.
- Sprocket is optimized for doing both hardware and software -> other agents only focus on one of these.
- Sprocket can pay for your SaaS subscriptions and hardware parts -> completing the loop.
- The product is fully open-source for users to hack on and change specific parts of it they don't like.

### Future Plans

- A LOT of custom benchmarks
- Cloud agents and cloud robotics simulation environments for training robot models using AI.
- Make a custom CAD software that is specifically made for AI and humans to work together.
- Train our own AI models for hardware.


### Re-use of Past Work

I wrote coding agent related code for the native rust client and the convex backend, alongside making an okay-looking UI before the hackathon.

All the work related to artifacts, hardware, prava integration, browser use, agentic checkout, etc., alongside a lot of UI rework was done during the hackathon.

**Best Visa Intelligent Commerce Implementation**

1. Created fully autonomous AI checkouts for any website that supports guest checkout.
2. Supports all types of mandate configurations.
3. Opens mandate approval in a new Prava/Visa page in a new tab in the user's browser, so that they can feel at ease entering card details.

![image](https://assets.devfolio.co/content/49d01e7949e84c988cf2133e0b7fe5b4/5723378d-1c81-422d-bfee-e6f14e039210.png)

![image](https://assets.devfolio.co/content/49d01e7949e84c988cf2133e0b7fe5b4/102f62cb-5548-4609-8e82-152b73fb74dc.png)

![image](https://assets.devfolio.co/content/49d01e7949e84c988cf2133e0b7fe5b4/3febb6ea-f1b2-431d-bf26-0ce677b37909.png)

**Most Startup-Ready Product**

- Sprocket is completely ready to be used by anyone (you can download it now and start using it).
- Every single one of its features works end-to-end with a very low failure rate.
- Depending on when you check the project, you should be able to pay for a Sprocket subscription right now. If not, it should be coming within 36 hours. The reason is a small delay in the approval process with our MoR.

### Multiple ways to make profits

 - SaaS subscriptions for Sprocket that give metered AI, browser tools, web tools, and Prava usage.
- Referral commissions from suppliers whenever Sprocket buys a product from them.
- Custom robotics hardware that will launch next month and be well-integrated with Sprocket.

### Real Users

These are hopefully going viral while I sleep:
1. https://x.com/amronos/status/2084020586750373939?s=20
2. https://news.ycombinator.com/item?id=49149322
3. https://github.com/spikonado/sprocket

We successfully got a few friends and teachers to become users of Sprocket.
They loved its web searching capabilities but wanted benchmarks for real validation of Sprocket being more efficient than the competition.
After the hackathon, this is our #1 priority.

### Future Plans

- A LOT of custom benchmarks
- Cloud agents and cloud robotics simulation environments for training robot models using AI.
- Make a custom CAD software that is specifically made for AI and humans to work together.
- Train our own AI models for hardware.

**OpenAI**

- We integrate the latest OpenAI GPT-5.6 models into Sprocket for handling all agentic tasks.
- GPT-5.6 Luna handles operating the browser and is operated by a smarter model the user chooses (ex., GPT-5.6 Terra or Sol).
- The user is presented with multiple options for which model they want to use, alongside what reasoning and token speed they want to use.
- The AI models are presented with a variety of tools, including command execution, asking questions, using a browser, web search, markdown web scraping, reading skills, etc. All of these tools were thought of from first principles to make the best engineering agent possible.

**Best Agentic User Experience**

- We offer a live view of the browser as the agent operates it
- We have a custom file/folder/project picker that doesn't rely on the operating system's poor-looking picker.
- We have a lot of nice-looking icons for all the tool calls the agent makes
- We have a very good-looking prompt composer with a nice UI for selecting skills
-  The right sidebar (in which the browser and artifacts live) has been crafted with hours of work on what the best UX can be. It features a proper full screen for artifacts, a new tab button for the agent browser view, and a way to full screen the right sidebar within the Sprocket UI.
- Some incredible settings pages with one made specifically for mandates. It provides multiple different mandate configurations, lists your current mandates for pausing/cancelling, etc.

To experience the full UI/UX described above, I encourage you to look at (fast-forward) this 6-min demo video: https://www.youtube.com/watch?v=E8KWO3Vh9YU or experience the product for yourself by downloading it from https://spikoando.com.

**Agentic Commerce Hackathon**

Fully integrated Prava end-to-end, including all types of mandates. The agent can use any website (that supports guest checkout) through its browser tools and complete checkout.

![image](https://assets.devfolio.co/content/49d01e7949e84c988cf2133e0b7fe5b4/5723378d-1c81-422d-bfee-e6f14e039210.png)

![image](https://assets.devfolio.co/content/49d01e7949e84c988cf2133e0b7fe5b4/bdc26bc4-8198-447f-b89e-a35760c296b4.png)

[Aarav Gupta](https://github.com/Amronos)

`2026-08-03`

---

### AEGIS Guardian
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aegis-guardian-fa15) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/somesh-opps/AEGIS-Guardian) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/ulVT6vnRfBk) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Code for everyone

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Dart](https://img.shields.io/badge/Dart-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**The problem it solves**

AEGIS Mission Control (also referred to as AEGIS Guardian) is a comprehensive, full-stack campus safety and infrastructure monitoring platform. The system is designed to provide real-time telemetry, threat detection (e.g., fire, gas leaks, unauthorized motion), and AI-driven insights to ensure campus security.

**Challenges we ran into**

1. I2C OLED Brownouts and Network Blocking

Challenge: The ESP32’s synchronous Firebase data pushes and heavy Wi-Fi radio current spikes were blocking the main execution loop and starving the I2C bus. This caused the Watchdog Timer to reset and the OLED display to randomly drop its internal memory and go blank.

Solution: Migrated the cloud architecture to use asynchronous Firebase uploads (setJSONAsync) to keep the main loop non-blocking. Increased the transmission interval to prevent memory fragmentation and implemented a brute-force software reboot of the OLED's charge pump (display.begin) on every refresh cycle to recover from microscopic voltage dips.

2. Phantom Sensor Triggers and Floating Pins

Challenge: The system initially locked into an "EMERGENCY" state due to false-positive fire alerts, followed by a delayed 5-second alarm trigger upon booting.

Solution: Traced the ghost readings to a combination of an inverted Active-LOW logic bug and a hardware floating pin issue. Migrated the flame sensor from an input-only pin (Pin 35, which lacks internal resistors) to a stable GPIO (Pin 26). Tuned the on-board LM393 potentiometer to ignore ambient infrared noise and corrected the boolean logic inversion in the sensor evaluation function.

3. BSSID Caching Wi-Fi Lockups

Challenge: The ESP32 would hang indefinitely on the boot screen when switching mobile hotspots, even when the SSID and password remained identical.

Solution: Identified that the ESP32 was caching the previous router's MAC address (BSSID). Implemented a forced cache-clearing protocol (WiFi.disconnect(true)) immediately preceding the WiFi.begin() command to ensure a clean connection state during field deployments.

**Best Use of Gemini API**

Our project, AEGIS, is a perfect fit for the Gemini track because the Gemini API serves as the central intelligence engine driving our system's autonomous decision-making and user interaction. We heavily leverage Gemini's advanced multimodal capabilities to process and analyze live camera feeds, enabling the architecture to perform complex visual reasoning and make real-time, context-aware safety assessments of the environment.

Furthermore, Gemini powers our interactive assistant chatbot, seamlessly translating raw building telemetry, emergency alerts, and visual insights into natural, conversational dialogue. By deeply integrating the Gemini API for both computer vision and natural language processing, we elevate AEGIS from a standard hardware sensor network into a proactive, intelligent AI safety assistant capable of sophisticated environmental analysis and intuitive human communication.

**Best Use of ElevenLabs**

Our project, AEGIS, is a strong fit for the ElevenLabs track because we have integrated an advanced voice assistant to serve as the primary communication and alert interface across our decentralized hardware network. By leveraging the ElevenLabs API, we transform raw environmental and safety telemetry into natural, high-fidelity audio broadcasts.

Instead of relying solely on physical buzzers or digital dashboards, AEGIS utilizes ElevenLabs' voice generation to communicate critical building-wide alerts, system statuses, and emergency notifications in real-time. This integration bridges the gap between hardware monitoring and human interaction, demonstrating how advanced voice AI can elevate physical infrastructure safety into an intuitive and highly accessible experience.

**Best Use of MongoDB Atlas**

Our project, AEGIS, is an ideal fit for the MongoDB track because MongoDB Atlas serves as the foundational data backbone for our entire decentralized IoT architecture. With multiple edge computing nodes continuously streaming high-frequency environmental telemetry and critical safety data, we rely entirely on MongoDB Atlas to seamlessly ingest, manage, and store this massive influx of information in real-time.

Beyond highly scalable storage, Atlas actively drives our system's intelligence and responsiveness. We utilize its robust querying and aggregation capabilities to fetch and classify complex sensor datasets on the fly, allowing us to instantly categorize data streams and distinguish between normal ambient conditions and critical emergencies. By leveraging MongoDB Atlas as our core data engine, AEGIS efficiently transforms raw hardware signals into a structured, highly accessible, and actionable database that powers our building-wide monitoring and alert ecosystem.\

**Best Use of ElevenLabs**

Our project, AEGIS, is a strong fit for the Elevenlabs track because we have integrated an advanced voice assistant to serve as the primary communication and alert interface across our decentralized hardware network. By leveraging the Elevenlabs API, we transform raw environmental and safety telemetry into natural, high-fidelity audio broadcasts.

Instead of relying solely on physical buzzers or digital dashboards, AEGIS utilizes Elevenlabs' voice generation to communicate critical building-wide alerts, system statuses, and emergency notifications in real-time. This integration bridges the gap between hardware monitoring and human interaction, demonstrating how advanced voice AI can elevate physical infrastructure safety into an intuitive and highly accessible experience.

**Open Innovation**

Our project, AEGIS Guardian, aligns with the Open Troy track because it is a highly adaptable, multi-domain IoT architecture designed to solve broad infrastructure challenges rather than fitting into a single, narrow use-case. We have engineered a scalable, decentralized edge-computing network of sensor nodes capable of real-time environmental telemetry and critical safety monitoring (including gas anomalies, fire detection, and high-current electrical loads).

Because the Open track champions cross-disciplinary innovation and versatile problem-solving, our system fits perfectly. It provides a robust, plug-and-play foundation that can be seamlessly deployed across diverse environments—from securing university laboratories and smart campuses to monitoring industrial or agricultural infrastructure—making it a universal, scalable solution.

Tip for the form: If they have a strict word limit, you can easily cut this down by just submitting the first paragraph, as it carries the heaviest technical impact!

Team **BitVerse** -- [Somesh Kumar Sahoo](https://github.com/somesh-opps), [Abhiraj SAHA](https://github.com/uvraj456), [Saudamini Roy](https://github.com/RoySaudamini), [Debopam Dutta](https://github.com/proxymaster356)

`2026-07-26`

---

### Project SANJAYA
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/project-sanjaya-fe60) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/darshanraj1909-jpg/Project-SANJAYA) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1u3iLTtgRn6cMzMgYcQLhh1OPcEIRe_QZ/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-Citadel%20Hackathon%20--%20Season%201-0052CC?style=flat-square)](https://citadel-hackathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> protecting lives beyond human vision

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Buzzer](https://img.shields.io/badge/Buzzer-333333?style=flat-square)

**The problem it solves**

SANJAYA is an AI-powered, real-time hospital safety and patient monitoring system designed to overcome the severe limitations of traditional, cloud-dependent surveillance. It addresses critical gaps in situational awareness, latency, and data privacy within healthcare environments by processing information directly at the edge

What people can use it for:

- Continuous Patient & Environment Monitoring: Automatically tracks hospital wards simultaneously for environmental hazards, patient distress, and posture changes.  

- Uninterrupted Emergency Detection: Operates reliably even during environmental obstructions like smoke, fire breakouts, or total darkness, ensuring situational awareness is never lost. 

- Immediate Local Alerting: Instantly flags critical events on a centralized GUI dashboard and logs them locally to ensure immediate action can be taken when every second matters.

How it makes existing tasks easier and safer:

- Eliminates Cloud Dependency & Latency: By deploying the system entirely as an Edge AI solution on a Raspberry Pi 5, it removes the lag of cloud processing and drastically protects sensitive patient privacy

- Reduces Medical Staff Workload: Automates the constant, exhausting task of manual ward monitoring, allowing doctors and nurses to focus on direct patient care while relying on automated, high-accuracy AI alerts ($92.68\%$ test accuracy)

- Multi-Modal Fall & Distress Safety: Instead of relying on a single visual stream, it runs a parallel architecture processing audio, text, and video simultaneously to catch patient falls (posture) or verbal/physical cries for help (distress) instantly.

- Highly Cost-Effective: Replaces expensive, complex infrastructure with a modular, scalable, and affordable edge-computing setup, making advanced tactical monitoring accessible to clinics, nursing homes, and rehabilitation centers alike.

**Challenges we ran into**

Optimizing Multi-AI Parallel Processing on the Edge: Running three independent AI services simultaneously (Hazard AI, Distress AI, and Posture AI) on different ports of a single Raspberry Pi 5 presented strict computational resource constraints. We had to optimize frame distribution and inference workflows to prevent thermal throttling or severe frame drops

Multimodal Data Aggregation: Designing an efficient Result Aggregation Service that cleanly merges predictions and confidence scores from separate audio, text, and visual streams in real time without creating data bottlenecks.

Balancing Accuracy vs. Real-Time Latency: Fine-tuning the underlying models to achieve highly reliable metrics ($92.68\%$ testing accuracy and $0.94$ recall) while keeping the system lightweight enough to render live video feeds and immediate alerts onto the frontend GUI seamlessly. 

Handling Environmental Obstructions: Ensuring the system's modular architecture could robustly handle edge cases—like sudden visibility loss from smoke or darkness—by relying on alternative parallel sensory inputs (like audio analysis) to maintain constant situational awareness

Team **The Shakuni Protocol** -- [Devjyoti Misra](https://github.com/Devjyoti1920), [Tuhin Dey](https://github.com/TuhinDey18), [Anshum Kumari](https://github.com/Anshum15), [Darshan Raj](https://github.com/darshanraj1909-jpg)

`2026-07-12`

---

### Anveshak
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anveshak-09ab) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/paimon-2005/anveshak-ugv.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sJU5azL8ApE) [![Built at](https://img.shields.io/badge/Built%20at-Hackrit-0052CC?style=flat-square)](https://hackrit2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-Powered Computer Vision & Visual Odometry

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Robotics](https://img.shields.io/badge/Robotics-333333?style=flat-square) ![Embedded Systems](https://img.shields.io/badge/Embedded%20Systems-333333?style=flat-square) ![Visual Odometry](https://img.shields.io/badge/Visual%20Odometry-333333?style=flat-square)

Team **Touch my stack** -- [Anit Nath](https://github.com/OrioRiko-09), [Parijat Majumdar](https://github.com/Macro6969), [Abhijit Mridha](https://github.com/paimon-2005), [Akshita .](https://github.com/Akshitakeshav)

`2026-09-12`

---

### GearUp AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/shoppingagnet-abda) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/xVFFQwB0smE) [![Built at](https://img.shields.io/badge/Built%20at-Agentic%20Commerce%20Hackathon-0052CC?style=flat-square)](https://agentic-commerce.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Automated hardware sourcing with human-in-the-loop

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**Challenges we ran into**

Integrating a dynamic AI agent loop with secure, multi-stage fintech gateways (like Prava) and real merchant adapters brought some fascinating
 engineering and integration challenges. Here are the main hurdles we faced and how we solved them:

  1. The Virtual Card Provisioning "Total Mismatch"
   * The Hurdle: Prava provisions virtual payment cards against the itemized product list provided in the purchase session.
   * The Bug: In early tests, we would create a session with an overall delivered total (e.g., ₹5,250), but only itemize the physical product in the
     line-item list (e.g., Keyboard = ₹5,000). Because shipping/tax (₹250) wasn't explicitly broken out, the gateway detected a balance mismatch
     between the sum of individual products and the session's overall total, causing card provisioning to fail upstream with a validation error.
   * How we got over it: We designed a robust _session_products() helper in our service layer. If the merchant's live quote includes shipping or any
     extra fees, the helper dynamically injects a virtual "Shipping" line item into the payload:

   1     shipping = float(quote.get("shipping") or 0)
   2     if shipping > 0:
   3         products.append({
   4             "description": "Shipping",
   5             "unit_price": f"{shipping:.2f}",
   6             "product_id": "shipping",
   7             "quantity": 1,
   8         })
      This aligned the itemized totals with the overall authorized session limit down to the penny, enabling flawless virtual card issuance.


  2. Browser Reloads & Single-Use Session Links
   * The Hurdle: Prava’s hosted cardholder collect and verification iframe links are single-use by design.
   * The Bug: The moment a user loads the checkout iframe, the token is exchanged. If the user experienced a network hiccup, closed the modal, or
     accidentally reloaded their tab, attempting to reload the page returned a SESSION_ALREADY_EXCHANGED error. Forcing the user to ask the AI agent
     to search, compare, and propose the purchase all over again was a terrible user experience.
   * How we got over it: We built a new_session() mechanism (a secure "session re-issuer") in our backend. When a retry is initiated, the backend:
       1. Calls Prava's session revocation API (prava.revoke_session) to cancel the active, defunct session.
       2. Runs an on-the-fly re-quote to make sure the price has not drifted past the user's approved spend cap.
       3. Issues a fresh, single-use Prava session token so the frontend can reload the checkout iframe instantly without requiring the user to start
          the procurement process from scratch.
  3. Gateway Uniqueness vs. Single-Purchase Auditing
   * The Hurdle: Gateway-level transaction deduplication.
   * The Bug: Prava requires the external_order_ref parameter to be strictly unique per merchant account. During payment retries (described in
     Challenge #2), reusing the purchase's unique database ID (e.g., pur_a2b3c4d5) returned a DUPLICATE_EXTERNAL_ORDER_REF error from Prava's API.
   * How we got over it: We wanted to keep all transaction history tied to a single unified purchase record for audit tracking, rather than generating
     fragmented rows. We solved this by counting the session creation events for that purchase and appending a retry suffix (e.g., -r1, -r2) to the
     external reference sent to Prava:

   1     attempt = 1 + sum(
   2         1
   3         for event in purchase.events
   4         if event.event in {"payment_session_created", "payment_session_reissued"}
   5     )
   6     # external_order_ref = f"{purchase.id}-r{attempt}"
      This satisfies the gateway’s unique reference requirement while keeping all retries linked back to the same parent purchase ID in our database.


  4. Desktop Operating System WebAuthn Compatibility Mismatch
   * The Hurdle: WebAuthn (FIDO2/Passkey) hardware reliance on desktop environments.
   * The Bug: During cross-platform testing, we noticed the passkey-based checkout flowed flawlessly on iOS and Android devices, but consistently
     failed or hung on Linux Chrome.
   * How we got over it: We researched the WebAuthn standard and realized this is a hardware and operating system mismatch. Mobile devices have
     native, built-in "Platform Authenticators" (Face ID, Touch ID, or Android Fingerprint scans mapped directly to Chrome/Safari). Linux desktops do
     not expose a unified, native platform authenticator to Chrome, causing it to fall back to physical USB security keys (like YubiKeys) and fail if
     none are connected. We resolved this by:
       1. Utilizing Hybrid WebAuthn during desktop testing—using Chrome's QR code pairing to authorize the biometric challenge on our mobile phones
          over Bluetooth.
       2. Activating Chrome DevTools' Virtual Authenticator environment during local development to simulate a biometric chip in software.

**The problem it solves**

The Procurement Shopping Agent

This project is a compatibility-first, human-in-the-loop AI Procurement Agent designed to automate the process of researching, verifying, and
  purchasing remote-work gear (such as keyboards, hubs, docks, chargers, and mice). 

  It bridges the gap between autonomous AI reasoning (discovering the best items) and enterprise-grade security & payment compliance (preventing
  unauthorized spend and securing payment details).


  What Can People Use It For?

  Users can leverage the Procurement Agent as a smart shopping companion that handles the end-to-end purchasing process within a secure framework:

   * Requirements-Driven Sourcing: Instead of manually searching multiple storefronts, users can state their goals in plain English (e.g., "I need a
     USB-C hub with at least 65W power delivery and macOS compatibility, delivered by Friday under ₹5,000").
   * Automated Specs Auditing: The agent automatically inspects product databases to verify critical hardware specifications (ports, connector types,
     operating system compatibility, and wattage) before making a suggestion.
   * Real-time Value Verification: The agent queries Google Shopping (via SerpAPI) to compare merchant prices against broader market listings,
     providing proof that a recommended deal is fair.
   * One-click Checkout Preparation: When the user picks a product, the agent tables a formal purchase proposal containing a comprehensive trade-off
     analysis, waiting only for user authorization.


  How It Makes Existing Tasks Easier

   1. Eliminates Search & Tab Fatigue: Rather than switching between search engines, technical spec sheets, and comparison tables, users interact with
      a single conversational interface that aggregates all of this context.
   2. No More Technical Mismatches: Purchasing peripherals is prone to compatibility errors (e.g., buying a dock that under-powers a laptop or lacks
      drivers for the OS). The agent ranks products by compatibility first, ensuring users never buy gear that does not work with their specific
      workspace.
   3. Objective Recommendation Matrix: The agent is instructed to present up to three options, clearly explaining the real trade-offs of each
      (delivery times, ports, price differences) rather than pushing a single sponsored link.

  
  How It Makes Purchases Safer (Security & Risk Safeguards)

  Standard AI agents capable of browser-automation or checkout pose massive security risks. This project employs a zero-trust capability boundary and
  strict financial guardrails to make agent-based commerce completely safe:

  1. Human-in-the-Loop Spending Boundary
  The agent itself has no permission to initiate payments or place orders. Its strongest possible action is the propose_purchase tool, which simply
  writes a pending proposal to the database and stops. Actual capital movement requires explicit human approval via the web UI.

  2. Live Dynamic Re-quoting (Anti-Exploit Protection)
  Prices fluctuate rapidly. When a user approves a proposed purchase, the backend immediately performs a real-time re-quote against the merchant's
  API. If the merchant has raised the price above the agent's original proposed spend ceiling (even by a fraction of a cent), the transaction is
  instantly blocked, failing safe before any payment session is initialized.

  3. Hard Backend Budget Ceilings
  Spend limits are strictly enforced at the database and service layer (e.g., a hard spend ceiling of ₹15,000). This ensures that even if the AI model
  is compromised or subjected to prompt-injection attacks, it is physically impossible for the agent to propose a transaction exceeding the
  administrator-configured budget.

  4. PCI-Compliant Prava payment gateway integration
   * Zero Cardholder Data Storage: The backend never stores, logs, or views sensitive card numbers or CVVs.
   * Hosted Payment Sessions: Payment collection and cardholder authentication are handled securely through Prava's hosted checkout sessions and
     secure iframe interfaces.
   * Scoped Virtual Credentials: Upon successful cardholder authorization, the system fetches a temporary, single-use, merchant-scoped credential to
     complete checkout, keeping the user's primary card details secure and isolated.

  5. Immutable Audit & Timeline Ledger
  Every purchase maintains an absolute audit history recording every state transition from proposed (by agent), to approved (by user), to
  payment_session_active, to checkout_completed (by merchant adapter). This guarantees total visibility and operational auditability for finance and
  IT teams.

Niranjana Ramesh

`2026-08-02`

---

### Synapse-X
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/synapsex-0841) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://siddhartha8406.github.io/nmit-cam/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/evH7qQUPjd0) [![Built at](https://img.shields.io/badge/Built%20at-NMIT%20HACKS%202026-0052CC?style=flat-square)](https://nmithacks26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> here for sensitive

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Servo Motor](https://img.shields.io/badge/Servo%20Motor-333333?style=flat-square) ![Piezoelectric sensor](https://img.shields.io/badge/Piezoelectric%20sensor-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**
The core challenge in remote robotics is the "Sensory Gap." Traditionally, controlling a robotic arm from a distance feels disconnected; you can see the robot moving on a screen, but you have no physical sense of what it is touching or how much pressure it is applying.

This system bridges that gap by providing a Human-Machine Interface (HMI) that prioritizes intuition and physical feedback.


**1. Eliminating the Learning Curve**
Most industrial or emergency-response robots are controlled via complex joysticks, gamepads, or specialized keyboards. These require hours of training and a high "cognitive load"—the operator has to think about which button moves which joint.

The Improvement: By using a haptic-integrated glove, the control becomes natural. If you want the robot to reach out, you move your hand. If you want it to grab, you flex your finger. This allows even untrained personnel to operate equipment during high-stress emergencies.


**2. Preventing Collisions and Equipment Damage**
When operating a robot in a hazardous or low-visibility environment (like a smoke-filled room or a deep-sea pipe), it is easy to accidentally smash the robotic arm into a wall or crush a delicate object.

The Solution: The integrated Piezo sensor acts as the robot's "nervous system." When the robot encounters resistance, the Haptic Feedback system sends an immediate vibration to the operator’s thumb.

The Impact: This physical alert is faster than a visual cue, allowing the operator to stop moving before damage occurs.


**3. Safety in Hazardous Environments**
There are many tasks where putting a human on-site is a death sentence, yet the task requires the dexterity of a human hand.

- Remote Handling: Whether it is defusing an explosive device, handling radioactive waste, or working in a chemically unstable lab, this system allows the operator to stay at a safe distance while maintaining the tactile "feel" needed for precision work.

- Tele-Presence: The use of HC-12/ESP-NOW wireless links means the operator can be hundreds of meters away, completely shielded from the danger zone.

**Challenges we ran into**

Building a high-precision haptic tele-operation system like SYNAPSE-X came with several "hidden" technical hurdles that only surfaced once the hardware was integrated. Here are the three most significant challenges I faced and the engineering solutions used to overcome them.

**1. The "Dancing Servo" Syndrome (Sensor Noise)**
**The Challenge:**
Initially, the robotic arm would jitter uncontrollably even when the glove was perfectly still. The MPU6050 is extremely sensitive, and tiny electrical fluctuations (noise) or hand tremors were being interpreted as commands to move 1 or 2 degrees back and forth constantly. This "dancing" was heating up the servos and making precise movement impossible.

**The Solution:**
I implemented a dual-layer filtering system:
**Moving Average Filter:** Instead of sending every raw reading, the ESP32 now averages the last 10 readings to smooth out spikes.
**Hysteresis (Deadzone):** I programmed a "threshold" logic. The robot only updates its position if the hand moves by more than 4 degrees. This locks the arm in place during minor tremors, resulting in rock-solid stability.


**2. Serial "Lock-up" and Buffer Flooding**
**The Challenge:**
During testing, the Arduino Nano would frequently freeze or "hang" after a few seconds of operation. I discovered that the HC-12 wireless module was sending data faster than the Nano could process and print it to the Serial Monitor. The 64-byte serial buffer was overflowing, causing the parseInt() function to wait forever for a "end of line" character that never arrived.

**The Solution:**
**Packet Markers:** I switched to a "Bounded Packet" format using < and > markers (e.g., <90,45,0>).
**Buffer Flushing:** I added logic to the Nano to "peek" at the serial data. If the buffer starts getting too full or finds "junk" data, it aggressively clears the buffer until it finds a new < marker. This ensured the robot always stayed synchronized with the glove.


**3. The Piezo Baseline & ADC Overflow**
**The Challenge:** The Piezo sensor (used for touch detection) was highly unpredictable. In the BIT lab environment, electrical noise from the servos caused the "idle" value of the Piezo to sit at 900/1023, leaving almost no room for a "squeeze" signal. Sometimes the signal would even "overflow" and wrap around to zero, triggering the haptic motor randomly.
**The Solution:**
**Dynamic Calibration:** I wrote a startup routine that samples the environment for 1 second when the robot powers on. It calculates a "Local Baseline."
**Relative Thresholding:** Instead of looking for a fixed number (like "1000"), the code now looks for a difference ($ \Delta $) from that baseline. This made the touch detection work perfectly regardless of whether the environment was electrically "noisy" or quiet.


**4. I2C Bus Hangs (The "Silent Freeze")**
The Challenge:
Sometimes the ESP32 would simply stop booting. I tracked this down to the MPU6050's I2C communication. If the SDA or SCL wires had even a slightly loose connection, the standard mpu.initialize() function would enter an infinite loop, "bricking" the glove.
**The Solution:**
I modified the setup sequence to include a non-blocking connection test. Now, the code checks if the MPU is responding before trying to initialize it. If it fails, the system prints a specific error to the Serial Monitor and continues running the other parts of the code (like the flex sensor) rather than freezing the entire system.

**Internet of Things**

**The Problem It Solves**
Traditional remote robotics suffer from a "Sensory Gap"—operators see the robot but cannot feel it. SYNAPSE-X bridges this by providing a natural, haptic-integrated interface.

**Intuitive Control:** Replaces complex joysticks with natural hand gestures.

**Tactile Feedback:** Uses vibration to alert operators of collisions, preventing damage.

**Safety:** Allows high-precision work (e.g., EOD, biohazards) from a safe distance.

**Challenges Faced**
**Sensor Jitter:** Solved with Moving Average and Hysteresis filters to stabilize movement.

**Serial Freezing:** Prevented "buffer floods" by using structured  markers and aggressive buffer flushing.

**Electrical Noise:** Overcame Piezo baseline shifts using Dynamic Calibration at startup.

**IoT Integration**: Edge Computing: Performs data filtering on-device (ESP32) to minimize latency.

**Wireless Connectivity:** Uses the HC-12 protocol for long-range, low-power communication.

**Cyber-Physical System:** Creates a bidirectional IoT loop where physical touch becomes digital data and vice versa.

**Best use of n8n**

**n8n (Workflow Automation)**
How you used it: n8n served as the "Logic Engine." You created a workflow that starts with a Webhook Trigger.  

**The Role:** When the robot's ESP32 detects a "Pick-up" via the button network, it sends an HTTP request to n8n. n8n then processes this data, logs the event, and triggers the next service to send a notification.

**Render (Cloud Hosting Platform)**
How you used it: You used Render as the infrastructure to host your n8n instance.  

**The Role:** Since n8n needs to be "always on" to listen for robot signals, hosting it on Render ensured your automation backend was live 24/7. This removed the need for a local server and made the system globally accessible.

**Google Gemini**

**How I Leveraged Gemini:**
**Architectural Decision-Making:** I consulted Gemini to pivot from a high-complexity 6-DOF model to a more reliable 3-DOF orientation system, focusing on industrial durability over mechanical complexity.

**Protocol Optimization:** Gemini helped me validate the transition from standard Wi-Fi to HC-12 (433MHz) for long-range telemetry and the implementation of I2C for streamlined sensor communication.

**Firmware & Logic Drafting:** I used Gemini to assist in writing and debugging the bidirectional communication code, ensuring near-zero latency between the controller and the robot.

**Cloud Orchestration:** Gemini was instrumental in designing the IoT logic track, helping me map the webhook integration between the ESP32 and n8n (hosted on Render) for automated mission logging.

**Professional Documentation:** I collaborated with the AI to refine technical descriptions and presentation narratives, ensuring the project was communicated with professional-grade clarity.

Team **PROTEGO** -- [Shreya Trambak Bhagwat](https://github.com/likhithakruthi), [Snehavalli K S](https://github.com/Siddhartha8406), [Yerasi Venkata Siddhartha Reddy](https://github.com/Siddhartha8406/)

`2026-05-10`

---

### (MINE-GUARD)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mineguard-f046) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hackolution-2026-minegaurd.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/mzvZyjQzHE8) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Intelligent IoT Real-Time Hazardous Environment

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![Package JSON](https://img.shields.io/badge/Package%20JSON-333333?style=flat-square)

**The problem it solves**

In the mining environment, the Critical Danger tier is the highest level of escalation. It indicates that environmental thresholds have been breached to a point where life and limb are at immediate risk.Trigger ConditionThresholdGas Level (Methane/CO)$> 2,500$ ppmTemperature$> 50$ °CWater Level (Flooding)$< 10$ cm (Distance from sensor to ground)Action: The system engages a High-Decibel Siren and a flashing "EVACUATE NOW" message on the LCD. Simultaneously, a high-priority JSON packet is pushed to the remote dashboard to alert surface command.🛠️ How MineGuard Empowers UsersMineGuard isn't just a collection of sensors; it’s a proactive safety partner. Here is how it transforms mining operations and safety management:1. For Underground Workers: Early Warning & SurvivalDetection of "Silent Killers": Workers cannot smell methane or carbon monoxide. MineGuard acts as a digital "canary in a coal mine," detecting these gases at parts-per-million (ppm) levels long before they become lethal.Hands-Free Monitoring: The 16x2 LCD Slideshow Logic allows workers to glance at environmental vitals while keeping their hands on their tools, ensuring they are always informed without distraction.Immediate Local Feedback: Because of Edge Computing, the device doesn't wait for a cloud response to scream. If a flood starts or a gas pocket is hit, the siren triggers instantly.2. For Surface Supervisors: Remote OversightReal-Time Data Visualization: Supervisors can monitor deep-mine conditions from a safe distance via the Web Dashboard. This removes the need for manual "safety check" walks into potentially hazardous zones.Incident Post-Mortem: Using the Historical Data Logging, safety officers can analyze the events leading up to a "near-miss" or accident, helping to improve future safety protocols and meet regulatory compliance.3. For Operations & Maintenance: Cost-Effective ReliabilityPredictive Maintenance: By tracking temperature and humidity trends, engineers can identify areas where ventilation systems are failing or where equipment might be overheating before a fire starts.Affordable Scalability: At a build cost of approximately ₹1,400 (~$17), MineGuard makes it financially feasible to deploy dozens of nodes throughout a mine, creating a comprehensive safety mesh that was previously too expensive for smaller mining operations.4. For Emergency Response: Informed RescueSituational Awareness: In the event of an evacuation, rescue teams can check the remote dashboard to see exactly which sector has the highest gas concentration or water levels, allowing them to plan the safest entry route.The MineGuard Edge: By bridging the gap between local hardware alerts and remote monitoring, we eliminate the "Information Vacuum" that often leads to mining tragedies. We don't just monitor hazards; we provide the seconds needed to save lives.

**Challenges we ran into**

HACKOLUTION-2026-MINEGAURD

🛡️ MineGuard — Intelligent IoT Real-Time Hazardous Environment Monitoring System
"Protecting Lives, One Pulse at a Time."

Hackathon Platform Framework License

MineGuard is an ESP32-powered IoT terminal that monitors atmospheric conditions and structural hazards in real-time — bridging local hardware alerts with remote web-based monitoring through a fail-safe dual-alert system. Built for multi-sensor fusion and proactive hazard mitigation in underground mining environments.

👥 Team — ERROR 404
#	Name	Role
1	Sounak Kumar Mondal	Team Leader
2	Rajashri Choudhuri	Member
3	Deepra Sarkar	Member
4	Krishanu Chakraborty	Member
📋 Table of Contents
The Problem
The Solution
Features
Tech Stack
Hardware Architecture
Dual-Tier Alert System
Remote Monitoring Dashboard
Why MineGuard
Roadmap
Getting Started
Project Structure
⚠️ The Problem
Mining is one of the world's most dangerous occupations.

Statistic	Figure
Global mining deaths per year	2,000+
Deaths caused by gas incidents	40%
Deaths preventable with real-time monitoring	60%
Key Challenges
Silent Killers — Colorless, odorless gases like CH₄ (Methane) and CO (Carbon Monoxide) cause explosions and asphyxiation with zero warning.

Environmental Instability — Sudden floods and extreme heat in deep mines go undetected until it's far too late.

Delayed Response — Conventional equipment lacks real-time remote visualization for surface supervisors.

💡 The Solution
MineGuard is an Integrated 360° Safety Ecosystem that provides:

Real-Time Sensing — Continuous multi-sensor sampling every 2 seconds
Dual-Tier Alerting — Graduated alert system from cautionary to critical
Remote Monitoring — Web-based command center accessible to surface supervisors
Edge Computing — All hazard decisions made locally on the ESP32; safe even when internet is unavailable
Metric	Value
Sensor Sampling Rate	2 seconds
Hazard Coverage	360°
Alert Layers	2 (Dual-Tier)
✨ Features
Multi-sensor fusion monitoring (gas, temperature, humidity, water level)
Intelligent dual-tier hazard grading system
16×2 I2C LCD display with automatic slideshow logic
High-decibel audio siren for critical alerts
JSON telemetry stream for web app integration
Real-time web dashboard for surface supervisors
Historical data logging for safety audits and compliance
Edge computing — fully operational without network connectivity
Modular, expandable hardware architecture
Affordable build cost (~₹1,400 in components)
🛠️ Tech Stack
Hardware
Component	Purpose
ESP32 (Dual-Core)	Main microcontroller & edge computing unit
MQ4 Sensor	Methane (CH₄) gas detection
MQ135 Sensor	Air quality & Carbon Monoxide (CO) detection
DHT22 Sensor	Temperature & Humidity measurement
HC-SR04 Sensor	Water level detection (flood monitoring)
16×2 I2C LCD Display	On-site visual readouts and alerts
Active Buzzer / Siren	High-decibel audio alert output
Software
Technology	Usage
C++ (Arduino Framework)	Firmware development for ESP32
JSON Telemetry	Structured sensor data serialization
HTML / JavaScript	Web-based real-time dashboard
Serial Communication	Data transfer between ESP32 and dashboard
🔩 Hardware Architecture
┌─────────────────────────────────────────────────────────┐
│                        SENSORS                          │
│   MQ4 (CH₄)  ·  MQ135 (CO)  ·  DHT22  ·  HC-SR04      │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              ESP32 (Dual-Core)                          │
│         Edge Computing & Hazard Classification          │
└──────────────────────┬──────────────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    ┌───────────┐ ┌─────────┐ ┌──────────────┐
    │  16×2 LCD │ │  Buzzer │ │ JSON Stream  │
    │  Display  │ │  Siren  │ │ → Web Dash   │
    └───────────┘ └─────────┘ └──────────────┘
Design Highlights
LCD Slideshow Logic — Automatically rotates between Temperature, Gas levels, and Water level readings for hands-free continuous monitoring without operator intervention.

Low Latency Response — All sensors are sampled every 2 seconds, providing near-instant hazard detection and alert triggering with minimal delay.

Edge Computing Safety — All hazard classification decisions are made locally on the ESP32 chip. Safety remains fully operational even when the web dashboard connection is lost.

Modular & Expandable — Hardware architecture supports seamless sensor additions and future wireless modules (LoRaWAN/WiFi) without redesign.

🚨 Dual-Tier Alert System
MineGuard uses an intelligent graduated hazard grading system:

⚠️ Tier 1 — Cautionary Alert (Yellow Zone)
Trigger Condition	Threshold
Gas Level	> 1,800 ppm
Temperature	> 40 °C
Humidity	Abnormality detected
Action: Visual warning displayed on LCD — notifies workers of rising environmental risks before reaching critical levels.

🚨 Tier 2 — Critical Danger

**BEST BEGINNER TEAM**

I am Sounak Kumar Mondal, a 2nd-year BCA student, and I am incredibly proud to lead this team of three talented first-year students. For their very first hackathon, we didn't want to build just another 'cool gadget'; we wanted to solve a problem where tech is a literal lifeline. We built MineGuard.

Mining is one of the world’s most dangerous jobs, with 60% of deaths being preventable through real-time monitoring. Our project addresses this head-on. What sets MineGuard apart from a typical beginner project is our focus on edge computing. Most IoT projects fail if the Wi-Fi drops, but in a deep mine, connectivity is never guaranteed. We designed MineGuard so that the ESP32 makes all critical safety decisions locally. If a hazard is detected, the alarm sounds instantly, regardless of the network status.

From a technical side, my team has worked hard on sensor fusion. We’ve integrated four different sensors—monitoring methane, carbon monoxide, temperature, and water levels—using a mix of I2C and analog protocols. This wasn't just about plugging in wires; my teammates, in their first semester, learned to calibrate these sensors to distinguish between a minor flicker and a life-threatening leak.

We also implemented a dual-tier alert system. We realized that in a high-stress environment, miners need a 'Caution' phase to prepare and a 'Critical' phase to evacuate. This level of safety logic, combined with a total build cost of just ₹1,400, makes MineGuard a professional-grade solution that is actually affordable for real-world mines.

Ultimately, this project represents the rapid growth of my freshmen teammates. They’ve moved from basic theory to building a complex, modular safety ecosystem in just a few days. We believe Team ERROR 404 deserves the Best Beginner Team title because we’ve balanced technical complexity with a deep sense of social responsibility.

Team **ERROR_404** -- [Deepra Sarkar](https://github.com/deeprasarkar007-glitch), [Rajashri Choudhuri](https://github.com/choudhurirajashri-code), [Krishanu Chakraborty](https://github.com/krishanu555), [SOUNAK KUMAR MONDAL](https://github.com/sounak286)

`2026-05-09`

---

### Aneebillin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/anebilin-95e4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arnab582004/Hactonix) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=DQohBJIrl_k) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Health is Wealth

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

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

Team **QBIT dynamics** -- [Saaraswata Roy](https://github.com/saaraswata), [Arnab Paul](https://github.com/Arnab582004), [Sarthak Sharan](https://github.com/sarthaksharan006), [Sayan Ghanty](https://github.com/SayanGhanty09)

`2026-04-19`

---

### Mukut-Smart coal miner helmet
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mukutsmart-coal-miner-helmet-7197) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kamanasis/MUKUT) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/19JHMU3Bv5PdjmeAiScJNGzLaCYrPftrx/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Protecting life beneath the surface

![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

Coal miners work in environments where gas leaks, accidents, poor visibility, and unreliable communication can turn emergencies into life-threatening situations.”

MUKUT addresses this by providing real-time hazard detection, underground location tracking, emergency SOS alerts, and long-range LoRa communication—even where GPS, mobile networks, and internet connectivity are unavailable

**Challenges we ran into**

Key Challenges

Unreliable Underground Connectivity
Conventional GPS, Wi-Fi, and internet connectivity cannot be assumed underground, so communication had to be designed around a LoRa-based multi-hop network.

Dynamic Network Failures
A relay node such as NODE02 can become unavailable, requiring the system to automatically discover and switch to an alternate route instead of losing communication.

Reliable Route Selection
The routing engine had to consider node/link availability and link quality while selecting a usable path and correctly handling NORMAL, FAILOVER, and NO_ROUTE states.

Real-Time State Synchronization
Safety, network, and routing information needed to update on the dashboard without page refreshes, requiring REST + WebSocket synchronization.
Simulator-to-Hardware Transition
We needed to develop and test the complete software system before physical hardware was ready, while ensuring simulator data and real hardware data could use the same backend pipeline.

LoRa Hardware Integration
Connecting the ESP32 and RA-02 modules introduced practical challenges around SPI configuration, LoRa communication, gateway reception, RSSI acquisition, and serial communication with the backend.
Limited Physical Hardware During Development

The complete multi-node underground network was not physically available for verification, so the failover network scenarios had to remain simulator-driven while the real hardware communication boundary was being developed.
Unverified Physical Sensors

Gas sensors and SOS hardware were not physically connected during Phase 4, so we had to avoid presenting simulated readings as genuine sensor measurements.
Maintaining Backward Compatibility
Every new phase had to preserve the functionality of previous phases—especially the safety engine, network model, routing engine, simulator, and existing dashboards.
Avoiding False Hardware Claims
A major challenge was clearly separating software-verified, simulated, and physically verified functionality so that the final demonstration remains technically honest.

Team **LORA-RX** -- [Aabir Manik](https://github.com/AabirManik), [Srijita Goswami](https://github.com/SrijitaGoswami), [Jayjit Dutta](https://github.com/jayjit-2025), [Sohan Sarkar](https://github.com/sohansarkar07), [Kamanasis Roy](https://github.com/kamanasis)

`2026-09-02`

---

### MineGuard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mineguard-ai-a971) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://splendorous-marshmallow-aecfbf.netlify.app) [![Built at](https://img.shields.io/badge/Built%20at-Dora%20Hack%202.0-0052CC?style=flat-square)](https://dora-hack.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Predict. Prevent. Protect.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Buzzer](https://img.shields.io/badge/Buzzer-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Sensors](https://img.shields.io/badge/Sensors-333333?style=flat-square)

**The problem it solves**

Underground mining workers face risks from hazardous gases, high temperature and humidity, falls, and collisions with obstacles. Existing safety systems often focus on detecting danger after conditions become critical. MineGuard AI aims to provide an early-warning safety layer by combining environmental and worker-motion data into an explainable risk score. It helps safety teams identify rising risks, warn workers before situations become more dangerous, and trigger an emergency response workflow when incidents such as falls are detected.

**Challenges we ran into**

One of our main challenges was converting the idea of predictive mining safety into a simple, understandable MVP. We had to design a dashboard that could clearly communicate sensor conditions, risk levels, worker zones, and emergency states. Another challenge was designing reproducible safety scenarios such as gas hazards, critical risk, proximity warnings, and worker falls so they could be demonstrated consistently during testing. We addressed these challenges by building a modular dashboard with separate Predict, Prevent, and Protect workflows and scenario-based testing.

Bhaskar Goswami

`2026-08-20`

---

### NexTrack-NariSuraksha
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nextracknarisuraksha-4324) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sumairasumaira648-svg/NariShakti) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://nari-shakti-phi.vercel.app/login) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> NexTrack — Because Safety Should Never Lose Signal

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![LoRa Alliance](https://img.shields.io/badge/LoRa%20Alliance-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![n8n](https://img.shields.io/badge/n8n-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**

Women in distress often face a critical gap between recognizing danger and being able to call for help. Conventional safety apps depend heavily on smartphones, cellular connectivity, battery, and active user interaction—exactly the things that may fail during an emergency.

NAARI SHAKTI addresses this gap through a discreet, wearable safety system designed to provide help even when a phone or cellular network is unavailable.

🚨 **Instant emergency activation**: A discreet SOS trigger allows the user to send an emergency alert without navigating a phone.
📡 **Off-grid communication**: The wearable can transmit emergency information without relying solely on cellular connectivity.
📍**Real-time location**: During an emergency, the user's location can be shared with trusted contacts/responders.
🛡️ **Multi-layer protection**: Beyond alerting, the system incorporates active deterrence mechanisms to help the user create distance and escape.
🎙️**Automatic distress detection**: Sensors can help identify abnormal movement, falls, or distress sounds, reducing dependence on manual interaction.
🗺️ **Safer navigation**: Risk-aware route information can help users avoid reported unsafe or high-risk areas.

In short, NAARI SHAKTI transforms women's safety from a phone-dependent emergency action into a discreet, multi-layer wearable safety network—designed to Detect, Alert, Locate, and Protect when it matters most.

**Challenges we ran into**

**Challenges We Ran Into**

Building **NAARI SHAKTI** involved several challenges because we wanted the system to remain useful even when the user's smartphone or cellular network becomes unavailable.

**Reliable emergency communication**: Our biggest challenge was designing an alert mechanism that does not depend entirely on cellular connectivity. We explored an off-grid communication approach so that an SOS can still be transmitted in low/no-network environments.
**Discreet SOS activation**: We had to make the emergency trigger quick and intentional without requiring multiple interactions with a phone. We refined the wearable interaction so that an SOS can be activated discreetly during a stressful situation.
**Hardware–software integration**: Connecting the wearable, location tracking, emergency alerts, and dashboard into one workflow required repeated testing and debugging of communication between the different components.
**Real-time location handling**: Maintaining accurate location information and passing it through the emergency pipeline while keeping the system lightweight was another challenge.
**Power and reliability**: Since a safety device needs to work when it is actually needed, we had to consider power consumption, response time, and reliable triggering rather than building a feature-heavy but impractical prototype.
Testing under realistic scenarios: We tested the complete flow—from *SOS activation → alert transmission → location sharing → response*—and iterated whenever one component introduced delays or failed to communicate correctly.

These challenges helped us move from a simple safety-app concept toward a multi-layer, wearable-first safety system designed around the realities of an emergency.

**Women Safety**

### Women Safety

**NexTrack is built around one simple idea: a woman’s safety should not depend on having her phone in her hand or a network on her screen.**

Our solution provides **protection before, during, and beyond an emergency**. It helps women identify potentially unsafe routes through **risk-aware safe-route intelligence**, discreetly trigger an SOS through a **wearable**, detect possible distress through **acoustic AI**, and share their **real-time or last-trusted location** with responders.

Most importantly, when cellular connectivity fails, NexTrack can use **LoRa-based communication** to keep emergency information moving beyond normal network coverage.

**From preventing risky situations to silently calling for help and guiding responders — NexTrack turns women’s safety from a reactive SOS into an intelligent, connected safety ecosystem.**

Team **NaariShakti** -- [Anuj Saini](https://github.com/anuj), [Shiny Dhingra](https://github.com/shinydhingra), [Sumaira .](https://github.com/sumairasumaira648-svg), [Nevid Alam](https://github.com/Nevid-786)

`2026-08-15`

---

### Outsurance
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/outsurance-9ad4) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vigneshbs33/outsurance/) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/DRa4v78j54U?si=y5bqvN58SEsBqPcJ) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/DRa4v78j54U?si=y5bqvN58SEsBqPcJ) [![Built at](https://img.shields.io/badge/Built%20at-MicroCraft%20--%20ArcNight-0052CC?style=flat-square)](https://microcarft-arcnight.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Health, Your Privacy, No Fine Print.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Framer](https://img.shields.io/badge/Framer-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

# The Problem Outsurance Solves

Buying health insurance in India is broken. For the average consumer, navigating the insurance landscape is a frustrating journey through deliberate jargon, hidden clauses, and high-pressure sales tactics. Outsurance re-engineers this experience from the ground up, turning a confusing financial chore into a transparent, secure, and hyper-personalized health strategy.

Here is exactly how Outsurance transforms the process, what people use it for, and how it makes existing tasks significantly easier, safer, and more accurate.

---

## 1. What Can People Use Outsurance For?

Outsurance serves as an autonomous, private digital insurance advisor. Users leverage the platform to:
* **Audit Existing or New Plans:** Evaluate whether a health insurance plan genuinely covers their unique pre-existing conditions (e.g., Diabetes, Hypertension) before buying.
* **Extract Vitals Automatically:** Upload complex medical reports, clinical PDFs, or lab blood tests to immediately extract critical health indicators without manually decoding medical terminology.
* **Run Financial Stress Tests:** Simulate real-world medical emergencies (e.g., *"How much out-of-pocket cost will I pay if I am hospitalized for a heart attack in Mumbai under Plan X?"*).
* **Interact with a Conversational Medical Agent:** Use natural language to query policy nuances, update health parameters on the fly, and ask follow-up questions like, *"What if I develop Asthma next year—how does that change my plan suitability?"*
* **Navigate in Native Languages:** Break down complex financial and medical jargon into over 15+ local Indian languages for family members who are non-native English speakers.

---

## 2. Making Existing Tasks Easier: Frictionless Insurance Discovery

Traditional insurance platforms operate like basic filtering directories. Outsurance replaces manual searching with data-driven automation.

| Traditional Process | The Outsurance Way | How It Makes It Easier |
| :--- | :--- | :--- |
| **Manual Data Entry:** Spending 20 minutes manually entering old prescription dates, blood sugar levels, and BP readings. | **Local AI Extraction:** Uploading a lab report triggers a local Small Language Model (SLM) to extract vitals instantly. | **Saves Time & Eliminates Error:** Users don't need to know what "HbA1c" or "Systolic" means; the system inputs the data perfectly in seconds. |
| **Deciphering Fine Print:** Reading 40-page policy PDFs to find waiting periods, co-pays, and disease-specific sub-limits. | **Structured Engine Matching:** Stage 2 & 3 matching algorithms cross-reference extracted health risks against a mapped database of insurance plans. | **Instant Clarification:** Zero scrolling through PDFs. The platform surfaces exact waiting periods and clauses relevant *only* to your conditions. |
| **Opaque Recommendations:** Platforms show a "Best Seller" badge with zero explanation of why that plan fits you. | **Explainable AI (XGBoost + SHAP + Gemma):** Visualizes exactly how metrics like BMI or Age impacted your score, backed by a plain-English explanation. | **Informed Decision Making:** Removes guesswork. Users see exactly *why* a specific plan scored an 8.5/10 versus a 5/10. |

---

## 3. Making Existing Tasks Safer: Privacy & Integrity by Design

The current insurance market carries significant risks regarding data privacy and predatory marketing. Outsurance establishes a secure framework to eliminate these threats.

### 🚫 Stopping Spam & Eliminating Aggregator Leaks
* **The Status Quo:** Entering your phone number on typical insurance aggregator sites instantly results in endless cold calls from aggressive brokers pushing high-commission plans.
* **The Outsurance Safety:** Built with a strict **Zero-Knowledge Design**. Clinical document parsing runs entirely in local memory on the client side. Only 10 anonymous numeric health vitals pass through the Machine Learning pipeline. Your sensitive medical documents never touch a third-party server, keeping your personal contact information secure from broker databases.

### 🧠 Mitigating the "Underwriter Rejection" Trap
* **The Status Quo:** Buying a plan without realizing a pre-existing condition is excluded can lead to claim rejections years later during a medical crisis.
* **The Outsurance Safety:** By running an advanced **4-Stage ML Recommendation Pipeline** (utilizing a custom XGBoost classifier trained on real hospital survey data), the platform calculates an accurate health risk tier (Low to Critical) beforehand. It proactively flags hidden policy traps, exclusions, and co-payment clauses before you pay a single rupee in premiums.

### 🔒 Secure Data Control
* Backed by rigid database **Row-Level Security (RLS)** and stateless JWT tokens, user sessions are completely isolated. For high-security environments, the entire ecosystem is packaged to deploy entirely offline on edge hardware (like a Raspberry Pi kiosk), ensuring sensitive medical queries can happ

**Challenges we ran into**

# Challenges We Ran Into

Building a production-ready, local-first intelligence engine that couples deterministic machine learning pipelines with non-deterministic small language models presented several technical hurdles. Because we chose to deploy on resource-constrained hardware (Raspberry Pi) and enforce absolute client-side data isolation, we could not rely on standard cloud infrastructure solutions. 

Here are the major technical challenges we encountered during development and how we engineered our way around them.

---

### 1. The Small Language Model Context Bloat & Multi-Agent Loop
* **The Hurdle:** Our conversational chatbot (`backend/app/agent.py`) handles complex tasks like tool orchestration, running out-of-pocket stress tests, and comparing plan specifications stored in `plans_db.py`. When we used local `gemma3:1b` via Ollama to evaluate conversational context alongside policy features for multiple plans, the context token count bloated immediately. This caused massive response latency (over 45 seconds per turn) on local hardware and occasionally led the model into an infinite loop of calling the same tool repeatedly.
* **How We Got Over It:** We engineered a **State-Throttled Tool Router**. Instead of passing raw, unstructured policy data or the entire chat history back to the model, we decoupled the execution layers:
  1. We used the local SLM strictly as a lightweight **Intent and Named Entity Recognition (NER) extractor** to pull parameters (e.g., condition names, localized budget ceilings).
  2. We passed these parsed parameters into deterministic, fast Python utility modules (`hospital_network.py` and `stress_test.py`).
  3. The structured responses from these modules were then injected into an optimized, minimal prompt template. This reduced the token payload by **78%**, dropping latency to under 3 seconds on standard local machines.

---

### 2. Feature Asymmetry & Normalization Breakdown in the XGBoost Pipeline
* **The Hurdle:** Stage 1 of our recommendation pipeline relies on a custom XGBoost classification model to assess a user's health risk tier based on real medical vitals (such as HbA1c, systolic blood pressure, and BMI). During testing, we noticed that when users had high qualitative medical risks (e.g., a history of severe kidney stones or a recent major surgical event) but otherwise perfect quantitative vitals (normal blood pressure, low BMI), the XGBoost model completely ignored the qualitative medical history and classified them as "Low Risk." This resulted in dangerous plan mismatches.
* **How We Got Over It:** We introduced **Stage 0: The Dynamic Condition Scorer** (`condition_scorer.py`). Before passing data to the XGBoost matrix, any text-based medical history or parsed clinical report details are processed through a local, aggressively cached risk-weight map (scoring conditions from `0.0` to `5.0`). We engineered a synthetic interaction feature—`metabolic_risk_score`—which cross-multiplies this condition score against quantitative biometric markers. By including this engineered feature in our training dataset, the XGBoost model learned to identify complex interactions, boosting classification accuracy to **85.0%** across all risk tiers.

---

### 3. RAM Swapping & Quantization Bottlenecks on Edge Deployments
* **The Hurdle:** One of our primary objectives was enabling the entire platform to execute entirely offline on a Raspberry Pi. During initial edge runs, launching the FastAPI backend alongside Ollama loading the `gemma3:1b` weights caused immediate memory starvation on the Pi's RAM. The operating system began aggressive memory swapping, which stalled the UI and caused the local AI document-extraction step to crash with out-of-memory (OOM) errors.
* **How We Got Over It:** We resolved this hardware bottleneck through aggressive resource optimizations:
  1. We switched to an aggressively quantized GGUF variant of the model, strictly limiting its execution footprint.
  2. We configured a strict memory-concurrency lock in the backend code, ensuring that the heavy extraction phase, the XGBoost inference matrix, and the chat agent never execute simultaneously in memory.
  3. We built a native **Soft-Fail Engine** that actively monitors hardware overhead. If local system resources cross a critical 92% RAM utilization threshold, the platform cleanly falls back to a high-speed regex-based medical parsing engine and static model matrix, preventing hardware lockups while preserving core platform features.

Team **CodeKrafters** -- [Vignesh B S](https://github.com/vigneshbs33), [Ishaan Gupta](https://github.com/Ishaan-Gpt), [Srujan Hiremath](https://github.com/srujanhiremath), [Keshav Agrawal](https://github.com/keshav-kr-agrawal)

`2026-06-13`

---

### Bharatshield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bharatshield-0567) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ANISHGHOSH763/Hacktonix2026-project.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/P71NKsUsxsM) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart Safety Helmet for Lone Industrial Workers

![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![LoRa SX1278 — Transmitter & Receiver](https://img.shields.io/badge/LoRa%20SX1278%20—%20Transmitter%20&%20Receiver-333333?style=flat-square) ![MPU6050 (6-Axis IMU)](https://img.shields.io/badge/MPU6050%20(6--Axis%20IMU)-333333?style=flat-square) ![MQ4 (Gas)](https://img.shields.io/badge/MQ4%20(Gas)-333333?style=flat-square) ![DHT22 (Temp & Humidity)](https://img.shields.io/badge/DHT22%20(Temp%20&%20Humidity)-333333?style=flat-square)

**The problem it solves**

Lone industrial workers in high-risk environments — mines, oil refineries, and factories — face life-threatening risks with no passive safety system:

- Workers collapse unconsciously (fall, gas exposure, cardiac arrest) with no way to call for help
- Dangerous gas levels go undetected until it's too late
- Extreme temperature and humidity levels go unmonitored, causing heat stroke and respiratory distress in workers
- Existing devices (panic buttons, dead man's switches) fail completely because they require the worker to consciously act
- Current solutions don't work in underground zero-connectivity zones
- Delayed rescue turns survivable incidents into fatalities

BharatShield solves this by:
- Passively detecting unconsciousness, dangerous gas levels, abnormal 
  temperature and humidity through sensors embedded in the helmet
- Automatically transmitting emergency alerts via LoRa radio from the worker's helmet (transmitter) to the supervisor's receiver unit — no internet, WiFi, or SIM required
- Alert reaches the supervisor instantly even kilometers underground with zero infrastructure

**Challenges we ran into**

1. LoRa Communication Stability-Struggled to get stable transmission between helmet and receiver.
   → Fixed by tuning frequency to 433MHz and adjusting spreading factor in Arduino code.

2. DHT22 & MQ4 Interference-MQ4 heat was affecting DHT22 temperature readings.
   → Resolved by adding read delays and spacing sensors apart on the circuit.

3. Multiple Sensor Fusion-Running MPU6050, MQ4 and DHT22 together caused board freezes.
   → Fixed using non-blocking millis() instead of delay() 
   to handle all sensors smoothly.

4. Power vs Range Tradeoff-High LoRa power gave better range but drained battery fast.
   → Balanced by finding minimum effective power setting and 
   adding sleep cycles between transmissions.

5. Hardware Stability-Loose jumper wires caused failures during testing.
   → Soldered critical connections before final demo.

Team **CtrlFreaks** -- [Ishita Dey](https://github.com/ishitadey955), [Aaditya Gupta](https://github.com/aadityagupta01), [Ayan Kar](https://github.com/Ayancoder1), [Anish Ghosh](https://github.com/ANISHGHOSH763)

`2026-04-19`

---

### BangleGuard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bangleguard-ai-09be) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/nayanip2001-max/BangleGuard-AI-sample) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Exposure Intelligence for Manufacturing.

![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![MQ5 gas sensor](https://img.shields.io/badge/MQ5%20gas%20sensor-333333?style=flat-square) ![DHT11](https://img.shields.io/badge/DHT11-333333?style=flat-square) ![RC522](https://img.shields.io/badge/RC522-333333?style=flat-square)

**The problem it solves**

BangleGuard AI solves the critical safety gap in traditional, small-scale manufacturing where hazardous workplace conditions build up over time unnoticed because conventional sensors only react after a single room metric crosses a dangerous limit.

Core Problems Solved

The "Cumulative Exposure" Blind Spot: Standard safety monitors measure room temperature or air quality in isolation. They fail to recognize that a moderate 38°C temperature combined with poor air quality over 4 continuous hours is far more dangerous to a worker than a temporary 42°C spike. BangleGuard tracks time-weighted, personalized exposure per worker.

Reactive Alerts vs. Predictive Prevention: Traditional systems ring alarms after a threshold is breached (when worker health is already compromised). BangleGuard analyzes environmental trends to predict rising risk and trigger interventions before dangerous levels are reached.

Unverified "Open-Loop" Safety: Standard setups notify supervisors of a problem but never verify if corrective actions worked. BangleGuard uses a closed-loop system (Sense → Associate → Analyse → Predict → Recommend → Verify) to continuously monitor whether risk actually drops post-intervention.

The Wearable Cost Barrier: Industrial safety wearables (like smartwatches or biometric monitors) cost $100–$200+ per worker, making them unaffordable for traditional bangle workshops. BangleGuard’s Hybrid Architecture places cheap $5 IoT sensors in workplace zones and gives workers $2 RFID badges, delivering personalized safety at a fraction of the cost.

**Challenges we ran into**

1. Gas Sensor Drift & Environmental Noise
The Challenge: The MQ-135 air quality sensor produced raw analog value spikes during initial warm-up and room airflow changes, triggering false escalation alarms in the risk model.
The Solution: Implemented a 5-sample moving average filter in the backend processing pipeline to smooth out transient noise while capturing genuine concentration trends.

2. Simulating Shift-Long Exposure in a 3-Minute Judge Demo
The Challenge: Cumulative exposure accumulation takes hours to reach unsafe levels, which is impossible to demonstrate live within a hackathon time limit.
The Solution: Built a backend Time Scaling Engine with a configurable multiplier (e.g., 1 real-world second = 1 simulated minute), allowing cumulative risk trajectories to play out dynamically during judging.

3. State Tracking Across Dynamic Zone Transitions
The Challenge: Workers shifting rapidly between zones caused edge-case exposure timer overflows and orphaned worker session records in backend state memory.
The Solution: Structured the backend around a strict finite-state machine (FSM). Swiping into a new zone automatically forces an explicit exit event on the previous zone, recalculating elapsed time ($\Delta t$) cleanly.

4. Power Bank Auto-Shutoff During Wi-Fi Idle
The Challenge: Standard power banks cut output after 30 seconds when ESP32 microcontrollers drop to low-power idle states between data transmission bursts.
The Solution: Kept the MQ-135 sensor heating element active to maintain a continuous load above 100 mA, and enabled low-current mode on the power source.

5. High-Frequency Web UI Chart Re-rendering
The Challenge: Streaming live sensor telemetry and dynamic risk updates over WebSockets caused dashboard line charts to lag when updating multiple worker profile cards simultaneously.
The Solution: Decoupled data ingestion from UI rendering by using state throttling on the dashboard, updating visible visual charts every 1 second while preserving sub-second backend analytical accuracy.

Team **DeBuggers** -- Vijay Aditya G K, Thrijagathi P, Thrinayani P, Aswin Ravikumar

`2026-09-02`

---

### Self bio fouling sensor skin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/self-bio-fouling-sensor-skin-1083) [![Built at](https://img.shields.io/badge/Built%20at-HackVerse:%20Into%20the%20Web-0052CC?style=flat-square)](https://hackverse-into-the-web.devfolio.co)

> Shake Off the Biofilm

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C](https://img.shields.io/badge/C-333333?style=flat-square)

**Challenges we ran into**

We had to connect an equivalent circuit for lm339 comparator since we couldn't acquire one

**The problem it solves**

This is a system to identify if a biofilm forms on top of a sensor and then removes it by vibrating

Team **fight club** -- Kanigha S, Mahathi Suresh, Aradhana V, Sheryl Achsha, Niranjana R

`2026-09-02`

---

### PhysioAssist AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/physioassist-ai-e236) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/watch?v=9yAM0jAbVsM&si=y7mgfXkrRayFXZsy) [![Built at](https://img.shields.io/badge/Built%20at-HyperFusion-0052CC?style=flat-square)](https://hyperfusion.devfolio.co)

> AI-Powered Physiotherapy for Smarter, Safer Recove

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

Physiotherapy exercises are often performed without proper supervision, making it difficult for patients to know whether they are performing movements correctly. Incorrect posture or joint movement can reduce the effectiveness of rehabilitation and may increase the risk of injury.

PhysioAssist AI addresses this problem by using computer vision and AI to analyze a patient's movements in real time. It tracks body keypoints, evaluates exercise form and provides immediate feedback so patients can perform rehabilitation exercises more safely and correctly. The system can also help physiotherapists monitor patient progress and make rehabilitation more accessible outside clinical settings

**Challenges we ran into**

One of our biggest challenges was achieving accurate real-time pose detection during physiotherapy exercises. Changes in lighting, camera angle, body position, and partial occlusion could cause keypoints to flicker or become inaccurate. We improved this by optimizing the pose-detection pipeline, adding validation and smoothing techniques, and continuously testing with different movements.

Another challenge was establishing reliable real-time communication between the frontend and backend. We solved this by using APIs and WebSockets to efficiently exchange exercise and movement data while keeping the user experience responsive.

We also faced challenges in designing meaningful exercise feedback. Instead of simply detecting movement, we had to define appropriate joint-angle thresholds and movement conditions so the system could provide useful guidance to the patient.

Team **NULL POINTER** -- ASHISH SHAW, [Harsh Jayswal](https://github.com/HarshJayswal-sudo), Devdeep Chakraborty, [SANAULLAH ANSARI](https://github.com/SimpleCoder26)

`2026-08-30`

---

### Braille Blast
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/braille-blast-079a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Meenachi27/Braille-Blast) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/PQQgvAb7dC4?si=ETHcjpJrXK6im-6R) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> wearable assistive technology

![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Embedded C](https://img.shields.io/badge/Embedded%20C-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square) ![Gemini API](https://img.shields.io/badge/Gemini%20API-333333?style=flat-square)

**Challenges we ran into**

Our biggest challenge was taking the idea from concept to a reliable working hardware-software prototype.

1.Hardware failures and rapid iteration: During initial prototyping, our soldering iron failed, interrupting assembly and requiring us to adapt our hardware workflow.

2.ESP32 instability: Our initial design used an ESP32, but when multiple components were integrated, we encountered brownout and watchdog timer (WDT) resets, largely related to power stability and load requirements. Rather than spending excessive time debugging an unstable prototype, we pivoted to an 3.Arduino Uno-based architecture for reliable demonstration.

Precise actuator integration: Connecting six tactile vibration actuators through the ULN2803A required careful soldering and debugging. Small wiring inconsistencies could result in incorrect Braille patterns, so we had to repeatedly verify the physical motor-to-Braille-dot mapping.

4.Power distribution: Providing stable power to the controller, HC-05 Bluetooth module, and multiple actuators was one of our major challenges. We experimented with battery supply, boost conversion, and common power distribution while ensuring sufficient current for simultaneous motor activation.
Braille pattern verification: The physical arrangement of motors did not initially perfectly match the logical Braille vectors. We had to remap the software lookup table according to the actual 3×2 tactile actuator arrangement.

5.End-to-end integration: Coming primarily from an ECE background, building the complete software pipeline—from a Streamlit interface and AI-based message compression to Python Bluetooth communication and Arduino-controlled tactile output—required us to work beyond our usual hardware-focused domain and integrate multiple software and hardware layers.

**The problem it solves**

According to the World Health Organization (WHO), at least 2.2 billion people worldwide are visually impaired and deaf , and accessing digital information is still a major challenge for people with visual impairment.
 Most smartphones and computers communicate information primarily through visual screens, while existing refreshable Braille displays costs more than 1 lakh and therefore difficult to access for many users.

Here comes our Solution  –  Braille Blast

Braille Blast is a low-cost  wearable tactile communication system that converts digital text into  Braille patterns represented through six vibration motors.

The system:

* Converts incoming text into a shorter, meaningful message using Gemini API.
* Maps each character to its corresponding 6-dot Braille pattern.
* Activates the appropriate vibration motors according to the Braille cell.
* Allows the user to feel the message through tactile feedback rather than relying entirely on a visual display.
* Provides a simpler and potentially more affordable approach to accessing digital notifications and messages.

The six coin  represent the standard Braille cell:

text is converted to 

●   ●
●   ●
●   ●


Each combination of vibrating motors represents a different character.

 Braille Blast aims to address two important barriers:

Accessibility + Affordability


This makes the project suitable for applications such as digital notifications, reminders, appointments, short messages, and other text-based information, providing users with a direct tactile way to receive information.

Braille Blast bridges the gap between digital communication and tactile accessibility by transforming text into compact, understandable Braille vibration patterns.

**Best Use of Gemini API**

### Best Use of Gemini API

**Braille Blast uses Gemini as an intelligent semantic compression engine for tactile communication.**

Long digital messages are difficult to consume through a tactile Braille interface because every additional character requires another Braille pattern. Instead of simply truncating text based on character count, Gemini understands the context and meaning of the complete message and generates a shorter version while preserving critical information.

Using the Gemini API, our system identifies and prioritizes essential details such as **dates, times, locations, names, deadlines, warnings, amounts, codes, status changes, and required actions**, while removing greetings, repetition, excessive formality, and unnecessary wording.

**Example:**

**Input:**
“Dear students, we would like to inform you that the internal assessment scheduled for August 30 at 10 AM has been postponed. The assessment will now be conducted on September 2 at 9:30 AM in Room 204. Students are requested to bring their record notebook.”

**Gemini Output:**
“Internal assessment postponed — Sep 2, 9:30 AM, Room 204. Bring record notebook.”

The compressed message is then passed through our **Python → Bluetooth → Arduino → Braille conversion pipeline**, where it is represented using six tactile actuators.

**Why Gemini?** Traditional summarization or keyword extraction can accidentally remove critical information. Gemini's contextual understanding allows Braille Blast to reduce message length while preserving the information the user actually needs, making tactile communication significantly faster and more practical.

Team **Dotmatrix Innovators** -- [Guna Vathy](https://github.com/gunavathyks652), [Mariammal M](https://github.com/manjusubbu04-cyber), [Meenachi M](https://github.com/Meenachi27), [Keerthana M K](https://github.com/Keerthana-M-K), [Sudharshana P S](https://github.com/sudharshana_ps)

`2026-08-30`

---

### ArogyaX
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/arogyax-e19c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anubhavsinha201/CONGNIVISTA) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtube.com/shorts/Fqv7-2qx9as?si=UGzQQZ1j6VG9DG0_) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/Fqv7-2qx9as?si=UGzQQZ1j6VG9DG0_) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Makkalai Thedi Maruthuvam

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Android SDK](https://img.shields.io/badge/Android%20SDK-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

# The problem ArogyaX solves

## The gap

Atrial fibrillation is one of the leading causes of stroke — and one of the quietest.
It's often completely asymptomatic; for many people, the first symptom is the stroke
itself. It's also cheap to catch: a 30-second single-lead ECG is enough to flag it.

None of that matters if the ECG never happens. In rural Tamil Nadu, a real ECG means a
clinic visit, dedicated equipment, and usually a network connection — three things a
doorstep doesn't have. So a condition that is genuinely easy to screen for goes
unscreened, not because the science is hard, but because the delivery is.

## Who it's for, and what they can do with it

ArogyaX is built for the **health worker already at the door** — specifically, the
Village Health Nurses working Tamil Nadu's *Makkalai Thedi Maruthuvam* (MTM) scheme,
who already visit households on a schedule to check blood pressure and blood glucose.

ArogyaX doesn't ask them to change that workflow. It adds one more 30-second step to a
visit that's already happening:

1. Attach two ECG electrodes and a fingertip pulse sensor — a ₹2,500 kit that clips to
   a phone the worker already carries.
2. Tap **Screen with ECG sensor**. The phone streams the recording live over Bluetooth,
   with a rolling trace on screen so the worker can see the signal is good before the
   30 seconds finish.
3. Get a result — not a diagnosis, a **referral priority**, spoken aloud in Tamil so the
   worker's eyes never have to leave the patient: *routine*, *see a doctor within 48
   hours*, *within 24 hours*, or *today*.

That result, and everything about the visit, is encrypted on the phone the moment it's
recorded and carries no name, phone number, or Aadhaar — only a salted, on-device ID.

At the other end, a **PHC clinician** opens a referral queue that's already sorted
worst-first, instead of a pile of raw recordings to triage themselves. A **district
health officer** gets an aggregated, de-identified view of where referral demand is
rising and where follow-ups aren't being completed — population-level signal that
doesn't exist today at all.

## What makes it safe enough to actually hand to a health worker

A screening tool used by someone who isn't a cardiologist has to be conservative about
what it's willing to say. Three design choices do that work:

- **It never diagnoses.** The output is a colour and a timeframe, decided by a fixed,
  auditable rule table — never a model-generated sentence, and never the words
  "atrial fibrillation" or "arrhythmia" on a worker-facing screen.
- **It refuses uncertain signal instead of guessing.** Bad electrode contact, patient
  motion, or even a single dropped Bluetooth data frame mid-recording gets the capture
  rejected and retaken — with a specific instruction on what to fix — rather than
  risking a confident wrong answer. A screening tool that always produces an answer is
  a screening tool that sometimes produces a wrong one.
- **It remembers.** Atrial fibrillation is often *paroxysmal* — it comes and goes, so a
  single clean reading proves very little. ArogyaX weighs repeat visits: a patient
  flagged once and clear the next time still reads as elevated risk, which is exactly
  the pattern a one-shot hospital ECG is structurally unable to see.

## What it's worth, in real numbers

On an independent, record-disjoint test set, the detector catches **95.2%** of AF
cases. At the scheme's real-world prevalence of AF (5.1%), that translates to, per 100
people screened:

| | |
|---|---|
| **True AF flagged** | ~4.9 people |
| **AF missed** | ~0.2 people |
| **False alarms** | ~27.9 people |

Roughly **1 in 7 referrals is real** — the honest cost of biasing hard toward catching
every case, stated plainly rather than dressed up as a better-sounding specificity
number. Every one of those ~5 real cases per 100 screened is someone whose stroke risk
is, today, found only by accident, if it's found at all.

## Why it's not just a gadget

The sensor and the model are the visible part. The part that makes this deployable is
that it runs **entirely offline** — the whole capture-to-result pipeline completes with
the radio off, and syncs to a district dashboard opportunistically whenever a network
happens to appear, never blocking a result on one. In a state where the last mile of
connectivity is exactly where the last mile of healthcare access is also missing, that
isn't a nice-to-have. It's the only way the rest of this works at all.

**Challenges we ran into**

# Challenges we ran into

Two hurdles stood out — one in the ML pipeline, one in the hardware integration. Both
were the kind of bug that doesn't announce itself: the system looks like it's working,
or looks like it's failing for an unrelated reason, until you trace it to the root.

---

## The technical hurdle: a quantized model that quietly became a different model

Our AF detector ships as an **INT8-quantized** CNN so it can run fast on a health
worker's own phone. The catch: full-integer quantization is not bit-reproducible run to
run. Retrain the exact same architecture on the exact same data, and you get a different
weight set — which means a different score distribution, which means the decision
threshold has to be *refit*, every time, or the model is being read with the wrong ruler.

**The symptom.** After a routine retrain, our evaluation script reported the CNN's
specificity had collapsed from a healthy operating point to **0.460**. Our first
instinct was the obvious one: *the new model regressed.*

**The real cause.** It hadn't. We'd retrained the model but left the *old* threshold
hard-coded in the decision policy:

```
old, correctly-fit threshold:  0.007812   (fit against the previous model)
new model's correct threshold: 0.1875     (fit against the retrained model)
                                ────────
                                24× apart, for a near-identical clinical
                                operating point
```

A number that looked exactly like "the model got worse" was actually "a threshold fit
for model A was silently pointed at model B." Nothing was broken — the two halves of
the system had just quietly drifted out of sync with each other, and the resulting
metric was consistent enough with a real regression that it took real digging to tell
the two apart.

**The fix.** We stopped treating "the model" and "its threshold" as two independent
things a human has to remember to keep in sync. `calibrate_threshold.py` now refits the
decision threshold directly from the quantized model's *own* score distribution as a
mandatory step of the release process — targeting a fixed sensitivity floor, never
inherited from FP32 or carried over from a prior build. Model and threshold move
together as one unit from now on, and the failure mode is documented explicitly in the
project's own engineering notes so a future retrain can't reintroduce it silently.

---

## The integration hurdle: "the sensor is paired, but the app can't find it"

A Bluetooth LE peripheral holds exactly **one** connection at a time, and it *stops
advertising itself* while that slot is occupied. Our sensor worked perfectly on the
bench. The moment we disconnected after a screening and tried to reconnect for the
next one, the app reported "no sensor unit found" — every time — even with the
hardware powered on, sitting right next to the phone.

**The symptom.** First connection: flawless. Every connection after that: invisible,
as if the hardware had failed, despite the LED still blinking.

**The real cause.** One line of ordering in our disconnect logic:

```kotlin
gatt.disconnect()   // asks the radio link to close...
gatt.close()        // ...but this releases the client IMMEDIATELY,
                     // before that request has actually finished
```

`close()` tears down the Android BLE client the instant it's called — it doesn't wait
for the link-layer disconnect to actually complete. So the ESP32 sensor never received
confirmation the phone had left. It kept holding its one connection slot open,
never resumed advertising, and became permanently invisible to every future scan —
not because anything was broken, but because we'd told our own side to stop listening
before the handshake that would have freed the peripheral had finished.

**The fix.** `close()` now *requests* the disconnect and waits for the peripheral to
confirm it (with a timeout as a backstop) before releasing the client. We also added
two fallback discovery paths for real-world reliability: reconnecting directly to an
already-bonded device, and a name-matched scan — because a device the phone has seen
before won't always be caught by a clean service-UUID filter alone.

---

## What both had in common

Neither bug looked like what it was. The threshold drift looked like a worse model; the
BLE failure looked like dead hardware. Both times, the fix wasn't a patch on the
symptom — it was removing a place where two parts of the system were allowed to fall
out of sync silently, and making that impossible instead of merely unlikely.

**Best Use of ElevenLabs**

ElevenLabs generates the spoken-Tamil layer of the app — but only at build time, never during an actual screening, because non-negotiable in this project is that a result must never depend on a live network call. We use it to pre-record two things once: the six fixed referral-outcome lines (RED/ORANGE/YELLOW/GREEN/RETAKE plus the "this is a screening, not a diagnosis" disclaimer), and a reusable vocabulary of individually-synthesized Tamil number words — Tamil number grammar is sandhi-heavy and irregular enough that splicing digits together doesn't work, so every whole number a result might need to speak (a heart rate, a signal-quality percentage) is pre-recorded once, the same way a railway station pre-records announcement vocabulary rather than composing speech from letters. Those number clips, plus a set of short fixed phrase segments, get stitched together on-device at runtime by our own sequence player to narrate all 33 dynamic explanation reasons with live per-patient values, with zero ElevenLabs calls happening in the field. In total we bundled 245 real, verified MP3 clips into the app this way — and every one of them is still flagged with an on-screen DRAFT marker, because machine-generated Tamil hasn't been reviewed by a native speaker or a clinician yet, and this project won't quietly let that pass as reviewed copy.

**Best Use of MongoDB Atlas**

MongoDB is the backbone of our sync service — the layer that lets a health worker's phone stay fully offline during a screening and still have every result reach a district dashboard the moment a network appears. Our Node service (server/src/mongo_repo.js) writes screenings to a screenings collection keyed by a unique index on recordId, so a retried upload from a spotty-connectivity phone upserts idempotently instead of creating duplicates or silently overwriting a clinician's referral acknowledgement — a real correctness requirement, not a nice-to-have, since a health worker's phone will retry uploads. A separate devices collection backs per-handset bearer-token auth, so a compromised phone can only ever write records attributed to itself. This isn't a local demo database — it runs against a live MongoDB Atlas cluster, and we proved it end-to-end by seeding 360 schema-validated synthetic screenings into it and reading them straight back out through the same PHC referral-queue API a real dashboard uses.

**Best Use of Snowflake API**

Snowflake is where individual screenings become district-level intelligence. server/scripts/export_to_snowflake.js reads new records out of MongoDB and merges them into a Snowflake screenings table using a stage-then-merge pattern — a bulk load into a temporary staging table followed by a single MERGE keyed on record_id, so re-running the export is always safe and never double-counts. On top of that table sits a district_tier_trends view that rolls screenings up by village, tier, and day — the query a district health officer would actually run to ask "where is referral demand rising, and where are follow-ups not happening?" The export is deliberately additive and privacy-preserving in the same move: it reads from Mongo and writes to Snowflake without ever touching the live app's request path, and only twelve non-identifying columns make the trip — no health-worker ID, no GPS coordinates, no raw ECG signal. We didn't just build this against a mock; we ran it against a real Snowflake trial account and confirmed it by pulling the same record back out of both MongoDB and Snowflake independently and diffing them.

Team **CONGNIVISTA** -- [Aadana K](https://github.com/aad-ana), [Anubhav Sinha](https://github.com/anubhavsin2020-web), [Niranjan JeyaSakthi](https://github.com/Niranjan-J01), [H Aadityaa](https://github.com/aadityaa0523), [Kshiti Prabhu](https://github.com/kshitiprabhu07)

`2026-08-30`

---

### Nayana
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nayana-smaart-tele-opthalmology-screening-assistant-def0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AnaghaBL/Nayana_PEC_v2) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1ye7eKEHN5L9YoUD9R0wpe1WSriKkcVkD/edit?usp=sharing&ouid=118131812239429296899&rtpof=true&sd=true) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_aoPZHcgPX8) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> Smart Tele Opthalmology Screening Assistant

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square)

**Challenges we ran into**

One of our biggest challenges was controlling corneal glare during front-eye imaging. Reflections from the illumination source could interfere with the eye image and affect the accuracy of our computer vision analysis. We experimented with the camera and illumination positioning and intensity to reduce reflections while maintaining sufficient image quality.

We also faced challenges integrating the different screening layers and ensuring that the hardware, image processing, and AI models worked together in a responsive pipeline. We addressed this through preprocessing, image-quality checks, and optimizing the processing workflow.

**The problem it solves**

Nayana addresses a critical gap in eye healthcare: millions of people develop vision-threatening conditions without timely access to screening or an ophthalmologist. Conventional eye screening can be expensive, equipment-dependent, specialist-dependent, and difficult to scale in rural and underserved communities, allowing preventable vision loss to go undetected until it becomes severe.

Nayana transforms eye screening into a rapid, AI-assisted, multi-modal assessment. It analyzes the retina, front of the eye, and pupillary response to identify potential abnormalities and generate an actionable screening report for healthcare professionals.

This enables:

* Early detection of potential eye abnormalities before significant vision loss occurs.
* Accessible screening in primary-care, rural, and resource-constrained settings.
* Faster triage, helping identify high-risk patients who should be referred to an ophthalmologist.
* Standardized assessment, reducing dependence on subjective initial screening alone.
* Scalable preventive eye care, allowing more people to be screened without requiring a specialist at every location.

Nayana does not replace the ophthalmologist—it extends the reach of the ophthalmologist. By bringing intelligent screening closer to the patient, Nayana aims to shift eye care from late-stage treatment to early detection and prevention.

Team **Bit by Bit** -- [Medha Balaji](https://github.com/medhabalaji), [Khushi Agarwal](https://github.com/khushia2608-afk), [Nisarga Hegde](https://github.com/hegdenisarga), [Anagha BL](https://github.com/AnaghaBL)

`2026-08-30`

---

### ZENVIBE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zenvibe-3a24) [![Built at](https://img.shields.io/badge/Built%20at-PEC%20HACKS%204.0-0052CC?style=flat-square)](https://pec-hacks.devfolio.co)

> IOT BASED SAFETY WRISTBAND

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square)

**Challenges we ran into**

![image](https://assets.devfolio.co/content/c7386443397d4e878c6aa498cb8dabb6/6c30fcbc-1863-49f5-bf5f-9a4a60b1a119.jpeg)

**The problem it solves**

![image](https://assets.devfolio.co/content/c7386443397d4e878c6aa498cb8dabb6/528b0771-e8bd-4a78-b228-23f9b6eefe3f.jpeg)

Team **ZENVIBE** -- [SHERIN FATHIMA](https://github.com/sherinfathimaqwe-spec)

`2026-08-30`

---

### Thervo - Sensor Free Predictive Cooling
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/thervo-sensor-free-predictive-cooling-5aea) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tanish0320/Thervo---Predictive-Cooling.git) [![Built at](https://img.shields.io/badge/Built%20at-RevengersHack-0052CC?style=flat-square)](https://revengershack.devfolio.co)

> Predict. Explain. Cool.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

One of the hardest parts was getting the model to behave the same way during training and when it was actually running. At one point, the training pipeline was processing the data differently from the live system. The model could look good on paper, but the moment we connected it to live telemetry, the numbers did not line up the way we expected.

We had to go back through the pipeline piece by piece and figure out where the mismatch was coming from. We eventually made the feature processing the same for both training and inference, including how CPU, GPU, memory, disk and network data were normalized and how the heat proxy was calculated.

Another challenge was the sensor free part. We could not simply look at a temperature sensor and say that a rack was getting hotter. We had to work out how much thermal pressure could be inferred from the workload itself. That led us to using CPU and GPU activity to build a heat proxy and then using neighboring racks to understand the wider thermal context.

The last thing we struggled with was explainability. Getting a model to output a risk score is one thing, but being able to answer an operator asking “why did the cooling just increase?” is much more useful. We built the XAI layer around the actual changes in workload, thermal risk and neighboring rack activity so the system can explain its decisions instead of just giving a number.

A lot of the work ended up being less about writing the model itself and more about making all the pieces behave consistently. We now have 34 automated tests covering the pipeline, inference, feature processing and XAI, and all 34 are passing.

**The problem it solves**

Every day, the digital world depends on thousands of servers working quietly behind the scenes. But keeping them running comes at a cost. Data centers use enormous amounts of energy to keep machines cool, often cooling systems react only after heat has already become a problem.

Thervo takes a different approach. It looks at the signals servers already generate, such as CPU, GPU, memory, disk and network activity, to understand how workloads are changing and predict thermal risk before it becomes critical. It does this without adding physical temperature sensors.

What makes Thervo different is that it does not simply make a cooling decision and leave operators wondering why. It explains what changed, why the risk increased or decreased, and what influenced the cooling decision.

This can help protect critical computing infrastructure, reduce unnecessary cooling, and give operators more confidence in AI driven decisions. It can also support the growing demands of AI workloads and modern data centers without requiring additional physical sensing infrastructure.

At its heart, Thervo is built around a simple idea.

Don't wait for machines to become hot to protect them. Understand what they are doing, anticipate what comes next, and act before it is too late.

**Trace Commons AI**

Thervo was developed iteratively with Gemini CLI across architecture, feature engineering, predictive modeling, testing, XAI, debugging, and validation. Our Trace Commons submission contains 12 authentic Gemini CLI sessions and 2,575 development steps, with reasoning excluded and the traces privacy-sanitized.

Team **GG** -- [Anshuman Panda](https://github.com/AnshumanPanda1), [Adithya K](https://github.com/AdithyaK3106), [Saqib Junaid](https://github.com/FlixonCoder), [Tanish Suragihalli](https://github.com/tanish0320)

`2026-08-22`

---

### TRUST3D
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trustd-691b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/9raveen/Trust3D-null-S3ntin3l5) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://trust3-d-null-s3ntin3l5-azure.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-Infinity%20Hacks%202026-0052CC?style=flat-square)](https://infinity-hacks.devfolio.co)

> When sensors lose sight, TRUST3D keeps its trust.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

One of our biggest challenges was integrating real nuScenes-derived data with a live API without making the demo dependent on the full nuScenes dataset at runtime. Initially, the live /scene endpoint was falling back to mock objects while our static fixtures contained the real 4-object scene, which caused a mismatch between the backend and dashboard.

We solved this by creating a frozen set of real demo objects from the nuScenes data and wiring both the live and static routes to the same source. This made the demo deterministic, reproducible, and independent of the nuScenes devkit during judging.

We also validated the trust/fusion pipeline across all three degradation scenarios, with our test suite passing 7/7 tests, including anomaly detection, trust degradation, fused-position accuracy, scene-confidence changes, and reproducibility.

**The problem it solves**

TRUST3D makes multimodal 3D perception safer and more resilient by continuously estimating how much each sensor should be trusted. When a sensor becomes unreliable, its influence on the fused scene is automatically reduced while healthier sensors carry more weight.

This can be used for:

1. Autonomous driving & ADAS — maintain reliable perception when a camera is obstructed or radar becomes noisy.
2.  Robotics — handle changing or unreliable sensing conditions without completely losing situational awareness.
3.  Safety-critical perception — identify anomalous sensors and expose confidence in the resulting scene instead of blindly trusting fused detections.
4.  Degraded environments — provide graceful degradation when individual sensing modalities become unreliable.


In short: TRUST3D turns sensor fusion from “trust everything equally” into “trust each sensor according to its current reliability.”

Team **NullS3ntin3l5** -- [Aprameya Goud](https://github.com/aprameyagoud), [V. Praveen](https://github.com/9raveen), [Manikanta Bojja](https://github.com/Manikanta-Bojja)

`2026-08-16`

---

### HelioTwin
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/heliotwin-2410) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://helio-twin.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-CodeStorm%202026%20#2-0052CC?style=flat-square)](https://codestorm-week2-2026.devfolio.co)

> Visualizing Sunlight for Smarter Urban Planning.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**Challenges we ran into**

HelioTwin is currently a working prototype, and one of the biggest challenges was integrating multiple GIS and solar analysis components into a single application. During development, we encountered issues with accurately detecting buildings inside custom-drawn boundaries, polygon selection, and maintaining consistent spatial analysis across different locations. Some features, such as precise building detection and certain analysis modules, are still being refined and do not yet perform reliably in every scenario.

Working with real-world OpenStreetMap data introduced inconsistencies that required extensive debugging, while optimizing sunlight and shadow calculations for interactive performance added further complexity. Although the prototype demonstrates the overall concept and workflow, improving the accuracy, robustness, and scalability of the analysis remains an ongoing part of development.

![image](https://assets.devfolio.co/content/c8561403d7ee4e3498070cc06cc72625/94961c7b-137d-47b8-8925-785fde3ac802.png)
currently it doesn't give exact measurements in the drawn area

**The problem it solves**

Urban planners, architects, homeowners, and solar installers often rely on expensive GIS software or manual site surveys to evaluate how sunlight interacts with buildings. Existing tools are either difficult to use, require specialized knowledge, or provide limited visualization.

HelioTwin simplifies this process by allowing users to select any location, analyze surrounding buildings, simulate sunlight throughout the year, and visualize shadows in an interactive 3D environment. Users can compare different dates and times, estimate solar exposure, and make informed decisions for rooftop solar installation, urban planning, energy optimization, and sustainable building design.

The platform makes advanced solar analysis accessible through a browser without requiring professional GIS expertise.

[Vihaan Goyal](https://github.com/VihaanGoyal12)

`2026-07-30`

---

### VisionAid
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vision-aid-767f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bipladipsaha/vision-aid) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/tFqWhtNfrQI?si=9uy54djaHUSKY4kZ) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Empowering Independence Through AI Vision

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![WebSOC](https://img.shields.io/badge/WebSOC-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Gradle](https://img.shields.io/badge/Gradle-333333?style=flat-square)

**The problem it solves**

VisionAid addresses the mobility and accessibility challenges faced by visually impaired individuals by providing real-time obstacle detection, AI-powered scene understanding, and voice-guided assistance. Unlike conventional solutions, it follows an offline-first hybrid approach that combines continuous ToF-based obstacle awareness with on-demand AI vision, ensuring low power consumption, enhanced privacy, affordability, and reliable operation without constant internet connectivity. This enables users to navigate their surroundings more safely, independently, and confidently.

**Challenges we ran into**

During development, we faced several technical challenges, including implementing reliable voice command recognition in noisy environments, optimizing AI inference on the Raspberry Pi within limited computational resources, and integrating Time-of-Flight sensors with the vision pipeline for accurate real-time obstacle detection. Maintaining low-latency communication between the Android application and Raspberry Pi over WebSockets while ensuring offline functionality was another key challenge. We addressed these issues through extensive testing, model optimization, asynchronous processing, sensor calibration, and a modular software architecture, resulting in a more reliable and efficient assistive system.

**Best Use of ElevenLabs**

VisionAid uses ElevenLabs to deliver clear, natural-sounding voice assistance, converting AI-generated responses into lifelike speech. This enables visually impaired users to receive real-time guidance, scene descriptions, and navigation instructions through an intuitive voice interface.

**Healthcare**

VisionAid fits the Healthcare track by improving the safety, mobility, and independence of visually impaired individuals. Using AI-powered computer vision, ToF sensors, and voice assistance, it provides real-time obstacle detection, scene understanding, and object identification through an affordable, offline-first wearable solution, making everyday navigation safer and more accessible.

Team **Binary Coded** -- [Anwesha Das](https://github.com/AnweshaDasAIeshaDasAI), [BIPLADIP SAHA](https://github.com/bipladipsaha), [ANISHA MAJUMDAR](https://github.com/Anisha1-AI), [Bittu Sharma](https://github.com/bittu7647)

`2026-07-26`

---

### BioArc Reactor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/bioarc-reactor-0029) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MindZed/mindzed-hexafall2.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://bioarc.mindzed.tech/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/dHcIAItFQ-8?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Smart tech for a greener earth.

![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![MQTT](https://img.shields.io/badge/MQTT-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Mosquitto MQTT Broker](https://img.shields.io/badge/Mosquitto%20MQTT%20Broker-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

## 🚨 The Global Problem & Industrial Bottleneck

Microalgae are biological superpowers: they absorb up to **400 times more atmospheric carbon dioxide ($CO_2$) per acre than terrestrial trees** and serve as the essential feedstock for renewable biofuels, pharmaceutical nutraceuticals, and sustainable protein. 

Despite this immense potential, industrial microalgae cultivation faces three critical roadblocks:
1. **High Biological Fragility & Culture Crashes**: Algae cultures are hyper-sensitive. Minor, unnoticed fluctuations in water temperature, pH, dissolved oxygen, or lighting schedules (photoperiods) can cause an entire culture tank to crash overnight, destroying weeks of progress.
2. **Exorbitant Hardware & Calibration Costs**: Currently, monitoring algal biomass density and determining the exact moment to harvest requires expensive laboratory equipment—such as **$5,000+ optical spectrophotometers** (measuring Optical Density at $OD_{680}$)—making automated bioreactors economically out of reach for small labs and decentralized clean-tech startups.
3. **Manual, Error-Prone Lab Labor**: Technicians must manually extract water samples daily, run chemical tests, and manually actuate dosing valves, air spargers, and grow lights. This creates a massive bottleneck for scaling up bio-solar carbon capture.

---

## 💡 How BioArc Solves It

**BioArc** transforms microalgae cultivation from a manual, high-risk lab chore into an **autonomous, AI-driven biophysical operating system**. We bridge the gap between industrial IoT hardware and intelligent web automation:

### 🧮 1. Algorithmic Biomass Tracking (Replacing $5,000 Spectrophotometers)
Instead of relying on expensive lab instruments, BioArc uses a low-cost RGB color sensor paired with our proprietary **Green Excess Index (GEI)** mathematical algorithm. 
* **Overcoming LED & Bubble Noise**: Standard sensors get blinded by intense purple/blue grow LEDs and aeration air bubbles. BioArc applies an automated **10-second "Quiet Sample Window"** that momentarily pauses aeration, lets bubbles settle, and computes a 5-sample trimmed moving average to calculate precise chlorophyll concentration.
* **Automated Harvest Triggering**: When cell density reaches optimal saturation (approx. $80\%$ density / OD 0.65), BioArc automatically alerts operators and initiates the harvest cycle.

### 🛡️ 2. Autonomous 24/7 Hardware Regulation (Zero Culture Crashes)
Powered by an **ESP32 microcontroller running an 8-state Finite State Machine (FSM)** (`IDLE`, `SAMPLING`, `DOSING`, `HARVESTING`, etc.), BioArc continuously regulates submerged water temperature ($^\circ C$), environmental humidity, nutrient intake valves, and grow light photoperiods 24/7 without human intervention.

### 🤖 3. Interactive AI Agency via Google Gemini Live
We eliminate complex, clunky dashboard interfaces by integrating **Google Gemini Live Bidi-Streaming AI with autonomous Tool Calling (`executeTool`)**. 
* Operators can literally converse with their bioreactor via voice or text: *"Gemini, check if water temperature is stable and enable manual override on the aeration pump."*
* The AI analyzes real-time telemetry, validates biological safety constraints, and directly actuates physical relays on the hardware!

---

## 🌍 What Can People Use It For?

* 🌿 **Decentralized Urban Carbon Capture**: Clean-tech startups and municipalities can deploy automated BioArc bio-solar trees or rooftop bioreactors to capture industrial exhaust $CO_2$ at a fraction of traditional infrastructure costs.
* 🧪 **Academic & Biotech Research Laboratories**: Researchers can automate tedious 24/7 culture logging, nutrient dosing, and environmental stabilization—freeing up thousands of hours of manual technician labor.
* 🚜 **Commercial Nutraceutical & Biofuel Farming**: Commercial growers of *Spirulina*, *Chlorella*, or lipid-rich biofuels can scale up production with automated harvest triggering and predictive machine learning growth models.

---

## ⚡ How BioArc Makes Existing Tasks Easier, Safer, and Faster

* 📉 **Slashes Equipment Costs by 90%**: Democratizes bioreactor automation by replacing lab-grade optics with algorithmic IoT sensors and edge computing.
* 🚨 **Proactive Alerting & Telegram Integration**: Instantly pushes real-time telemetry warnings and harvest-ready notifications directly to operators' phones via an automated Telegram bot.
* 🌐 **Fail-Safe Offline Operation (No Internet Required)**: If cloud Wi-Fi or MQTT connectivity drops, BioArc's local hardware FSM maintains all biological safety interlocks and automatically broadcasts an offline **Wi-Fi Captive Portal (`BioArc-AP`)**. Field technicians can connect via smartphone to view live sensor gauges and actuate valves offline from an embedded flash memory web dashboard!

**Challenges we ran into**

Building a synchronized biophysical hardware-to-cloud operating system pushed our full-stack engineering to the limit. When you interface physical biology, high-voltage microcontrollers, real-time web sockets, and streaming LLMs, things break in fascinating ways. 

Here are the four biggest bugs and hurdles we ran into, and exactly how we engineered our way out of them:

---

### 🔬 1. The "Purple Blindness" & Air Bubble Turbulence Hurdle (Optical Biomass Tracking)
* **The Bug**: To replace a $5,000 lab spectrophotometer, we submerged a low-cost RGB color sensor (Adafruit TCS34725) into our live microalgae tank to automate chlorophyll tracking. Our initial telemetry graphs were a complete disaster—raw data looked like violent, chaotic heartbeat spikes with zero correlation to actual algal growth! We discovered two culprits:
  1. **"Purple Blindness"**: The intense purple/pink LED grow lights flooded the RGB sensor, causing false-positive red/blue saturation.
  2. **Aeration Turbulence**: Micro-bubbles from the 24/7 $CO_2$ sparger scattered light randomly across the sensor lens.
* **How We Overcame It**: We realized raw RGB thresholding was mathematically impossible in a live tank. We abandoned it and engineered a proprietary normalization formula: the **Green Excess Index (GEI)** ($GEI = \frac{G - \alpha(R+B)}{R+G+B+\epsilon}$), which mathematically cancels out grow-light interference. To conquer the bubble scattering, we programmed our ESP32 FSM with an automated **"Quiet Sample Window"**: before taking an optical reading, the controller momentarily disengages the aeration pump and agitator motor for 10 seconds, lets the bubbles clear, takes 5 rapid samples for a trimmed moving average, and then resumes aeration. Instantly, our chaotic spikes transformed into smooth, lab-grade chlorophyll growth curves!

---

### ⚡ 2. The "Ghost Actuation" & WebSocket Desynchronization Bug (Hardware $\leftrightarrow$ Cloud Jitter)
* **The Bug**: We faced a frustrating race condition between our synchronous ESP32 microcontroller loop and our asynchronous Next.js 15 web dashboard. During field testing over cellular Wi-Fi, network jitter and Vercel serverless timeouts caused dropped MQTT packets. When an operator clicked "Toggle Aeration Pump" on the dashboard, the UI switch would toggle ON, but if the packet dropped, the physical hardware relay stayed OFF. This created a dangerous "Ghost Actuation" desynchronization where the web UI lied to the operator!
* **How We Overcame It**: We re-architected our communication layer with **Zustand Optimistic UI Hydration paired with a 3-Way Handshake Protocol**. Now, when an operator clicks a switch, the UI updates optimistically while broadcasting a command tag over Paho MQTT. If the ESP32 does not echo back the physical relay state confirmation within 2,000ms, our custom `useWebSocket` hook automatically rolls back the UI switch and alerts the operator. To make it bulletproof against Internet outages, we built an **Offline Wi-Fi Captive Portal (`BioArc-AP`) directly into ESP32 flash memory (`PROGMEM`)** so field technicians can always control relays locally!

---

### 🤖 3. The LLM Token Flood & Tool Execution Jitter (Gemini Live AI Streaming)
* **The Bug**: Integrating Google Gemini Live Bidi-Streaming AI over WebSockets brought unexpected latency and hallucination hurdles. Initially, feeding raw, high-frequency 1-second IoT telemetry JSON logs directly into Gemini’s context window caused severe token bloat, multi-second latency spikes, and context confusion—the AI copilot would get overwhelmed and misinterpret historical water temperature trends.
* **How We Overcame It**: We engineered a backend **Telemetry Normalizer** that aggregates 24-hour sensor streams into concise statistical snapshots (averages, deltas, and FSM runtime durations) before passing context to the LLM. Furthermore, when implementing custom **AI Tool Calling (`executeTool`)** to let Gemini physically control actuators, we programmed hardcoded biophysical safety interlocks: even if a user prompts Gemini to *"turn off the water cooling pump when temperature is 35°C,"* the local ESP32 FSM overrides unsafe AI commands, ensuring the AI has helpful agency without ever risking a culture crash!

---

### 💥 4. Strict Type Safety Across Dynamic IoT Telemetry Schemas
* **The Bug**: In our full-stack monorepo, data sources dynamically shift—switching between live Go backend MQTT telemetry, offline Captive Portal JSON, and fallback mock data during offline front-end development. This caused persistent TypeScript compilation errors, nullable field crashes, and Next.js client/server hydration mismatches during production builds.
* **How We Overcame It**: We established strict end-to-end domain contracts. We built comprehensive TypeScript interfaces (`TelemetryPayload`, `RelayStatus`, `SystemState`) shared across all hooks and server actions, and engineered a centralized fallback hydration normalizer (`mockData.ts`). By wrapping

**Best Use of Gemini API**

Used Google Gemini API for Chatbot, Voicebot and AI analytics.

**Best Use of DigitalOcean**

We use DigitalOcean VPS for our backend system.

Team **MindZed** -- [Abdul Kadir Jillani](https://github.com/mindzed), [Md Noor Hasan Ansari](https://github.com/NoorHasan92)

`2026-07-26`

---

### GESTURE VOCALIZER
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gesture-vocalizer-22d3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sayanghosh87/gesture_vocalizer) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/C55fP_SuE9w) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> GESTURhttps://devfolio.co/discoverE VOCALIZER

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**Challenges we ran into**

Building a real-time communication system required integrating multiple technologies into one seamless platform.

Major challenges included:

- Collecting and preprocessing sign language datasets for accurate model training.
- Achieving real-time gesture recognition with low latency.
- Reducing false predictions caused by different hand positions, lighting conditions, and backgrounds.
- Synchronizing hardware sensors, camera input, AI models, and the mobile application.
- Optimizing the machine learning model so it could run efficiently on limited hardware resources.
- Designing an intuitive interface for both sign language users and non-signers.
- Integrating speech synthesis and sign language animation into a single workflow.

To overcome these challenges, we combined computer vision, machine learning, hardware optimization, and continuous real-world testing. We validated the prototype with members of the deaf and mute community, incorporated their feedback, and improved recognition accuracy and usability. The project also received incubation support and was showcased before expert judges, strengthening both its technical and real-world impact.

**The problem it solves**

Millions of deaf and speech-impaired individuals struggle to communicate with people who do not understand sign language. This communication gap becomes even more critical in hospitals, public services, schools, workplaces, and emergency situations.

Gesture Vocalizer is an AI-powered wearable communication system that enables seamless two-way communication between sign language users and non-signers.

Our hardware prototype captures hand gestures using sensors and AI-based computer vision, instantly converting them into text and natural voice. Likewise, spoken or typed language is converted into sign language animations, enabling real-time conversations.

Key Features:
- AI-powered Sign Language → Text
- Sign Language → Natural Voice
- Speech/Text → Sign Language
- Real-time gesture recognition
- Portable wearable hardware prototype
- Mobile & display integration
- Works for healthcare, education, government offices, customer service, and daily communication.

The project empowers differently-abled individuals with faster, more natural, and inclusive communication while promoting accessibility for everyone.

**Healthcare**

### **Healthcare Track Justification**

Gesture Vocalizer addresses one of the most critical challenges in healthcare—effective communication between deaf or speech-impaired patients and healthcare professionals. Communication barriers can lead to misunderstandings, delayed diagnosis, incorrect treatment, and reduced quality of care.

Our solution enables seamless **two-way communication** by converting **Sign Language → Text/Voice** and **Speech/Text → Sign Language** in real time. This allows doctors, nurses, and caregivers to communicate directly with patients without requiring a sign language interpreter, ensuring faster and more accurate interactions.

The system combines a wearable smart glove, AI-powered gesture recognition, speech processing, and a mobile application to provide an accessible communication platform that is easy to use in hospitals, clinics, emergency departments, and telemedicine settings.

By improving accessibility, reducing communication gaps, and enabling inclusive healthcare services, Gesture Vocalizer enhances patient safety, supports better clinical decision-making, and contributes to more equitable healthcare for the deaf and speech-impaired community.

Team **BRAINY_BUNCH** -- [Sayan Ghosh](https://github.com/sayanghosh87), [SHANKAR DAS](https://github.com/shankarkmp), [SOUVIK MONDAL](https://github.com/mondalsouvik24827-ai)

`2026-07-26`

---

### EcoGrow Automation
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecogrow-automation-d482) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Sufiyaansari08/EcoGrow.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://hexafalls.surge.sh) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/uY6JatZWmv0) [![Built at](https://img.shields.io/badge/Built%20at-HexaFalls%202-0052CC?style=flat-square)](https://hexafalls2.devfolio.co)

> Iot based plant monitoring and automation

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square)

**Challenges we ran into**

1. Solving the Web Dashboard Localization Issue
The Problem: We needed dynamic language translation on the online web dashboard, but wanted to maintain a lightweight system without relying on heavy external cloud APIs or complex frontend scripting.

The Solution: We resolved this by storing all translation dictionaries locally in a highly organized JSON format. Because we deliberately engineered a streamlined frontend, we handled the localization logic entirely on the backend using the ESP32's C++ environment. The microcontroller parses the JSON file stored in its memory (via the ArduinoJSON library), matches the text keys to the user's selected language, and serves the dynamically populated HTML directly to the dashboard. This local-storage approach completely eliminated third-party API latency and ensured our Tailwind CSS bento-grid layout remained perfectly stable, all without requiring any heavy client-side processing.

2. Solving the Dual-Network (Offline/Online) Sync Issue
The Problem: The ESP32 needed to act as its own local offline router while simultaneously maintaining a connection to the global internet to update the remote dashboard, which initially caused network crashing and packet loss.

The Solution: We solved this by configuring the ESP32’s Wi-Fi radio to run in WIFI_AP_STA (Access Point + Station) dual mode. To prevent the system from freezing if the external internet dropped, we rewrote the connection logic to be completely asynchronous. By utilizing non-blocking C++ code (using timer intervals rather than standard delay functions), the microcontroller continuously manages the local offline dashboard and hardware sensors without pausing to wait for an internet response. If the global web connection drops, the system seamlessly falls back to the local Access Point without the user ever noticing a disruption in hardware control.

**The problem it solves**

Traditional plant care and agriculture often rely on manual monitoring, guesswork, and inconsistent routines, which can lead to poor plant health or crop failure. Furthermore, most modern "smart" agricultural solutions require a constant internet connection, making them useless in remote areas or during network outages.

EcoGrow Automation solves these issues by providing an autonomous, data-driven, and completely offline environment management system.

Specific Problems Solved:

Inconsistent or Improper Watering (Over/Under-watering):
Human error is the leading cause of plant death. By relying on real-time soil moisture sensors rather than a fixed timer or visual guessing, the system eliminates both drought stress and root rot. Plants are watered exactly when they need it, down to the optimal threshold.
Disrupted Plant Respiration & Light Deprivation:
Indoor setups or shaded greenhouses often suffer from poor lighting, but leaving artificial lights on 24/7 exhausts the plants and prevents cellular respiration. EcoGrow solves this by actively tracking ambient sunlight to supplement light only when necessary, while strictly enforcing a natural 6:00 AM to 6:00 PM circadian rhythm so plants can properly rest and respire.
Cloud Dependency in Remote Agriculture:
Most IoT systems break down without an active Wi-Fi connection to a cloud server. EcoGrow solves the "remote access" problem by utilizing an offline-first local server architecture. Farmers or plant owners can monitor metrics, actuate pumps, and download data completely independent of the internet.
Vulnerability to Environmental Hazards:
Sudden weather changes (like unexpected heavy rain) or emergencies (like electrical fires) can destroy a greenhouse in minutes. The system solves this lack of awareness by acting as an environmental sentry, providing immediate real-time alerts for fire and rain, alongside continuous air quality monitoring.
Lack of Actionable Historical Data:
Without data, cultivators cannot optimize their yield or troubleshoot seasonal issues. EcoGrow solves the "blind spot" in agricultural management by meticulously logging every sensor metric at one-hour intervals and allowing users to export the data as PDF reports for long-term trend analysis.

**Open Innovation**

EcoGrow Automation exemplifies Open Innovation by democratizing smart agriculture through an accessible, transparent, and decentralized architecture. Built on affordable ESP32 hardware and an adaptable HTML and Tailwind CSS frontend, it breaks away from closed-source proprietary systems and mandatory cloud subscriptions. By utilizing a dual-network setup for off-grid functionality and localized JSON-based translation, EcoGrow ensures that advanced automation and hourly data logging are available even in remote areas without internet access. Because the core logic is highly modular and data is openly shareable via PDF reports, the project empowers communities to easily adapt the technology for other domains like aquaponics or industrial monitoring, fostering collaborative, data-driven agricultural growth.

Team **BinaryBeasts** -- [Sufiya Ansari](https://github.com/Sufiyaansari08), [Shruti Raj](https://github.com/shrutiraj-student), [Joy Bhattacharjee](https://github.com/Joybhattacharjee6290-web)

`2026-07-26`

---

### VMS using AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vitals-monitoring-system-using-ai-983f) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gursingh-56/Vitals-Monitoring-System-Using-AI) [![Built at](https://img.shields.io/badge/Built%20at-HackVSIT7.0-0052CC?style=flat-square)](https://hackvsit-7.devfolio.co)

> Kanye Approves!

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**Challenges we ran into**

Man, we been thru a lot, it's an iot based project, we lowkey burnt 3 arduinos while making ts 🥀 and it was tuff getting the trusted data from da internet but we were successful in it

**The problem it solves**

Yo big Harv,
Ts piece of tech is extraordinary( Trust me on ts)
It helps a lot of peeps with their health and shi

Team **Team Vader** -- Gurkirat Singh, anmol singh, PARAM Parkash

`2026-07-25`

---

### Refreshable Braille display connected to mobiles
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/refreshable-braille-display-controlled-with-specific-software-dfb9) [![Built at](https://img.shields.io/badge/Built%20at-Devlynix%20Buildathon%202.0-0052CC?style=flat-square)](https://devlynix-buildathon-1.devfolio.co)

> The hardware reads and software translates

![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**Challenges we ran into**

- As it is a hardware project we are not able to get the minute magnets of size 1x0.5mm and ferrite rods of 1x10mm in time. 
- We also cannot provide the code as it is still in the early stage of patenting. Since the  projects theme wasn't specified I wasn't sure if hardware projects are accepted. Which is one of the reasons why I cannot provide the project link.

**The problem it solves**

It is a product being built by our company. This product is used by visually impaired people who can touch the pins tht come out of the hole. As shown in the images above the blind person moves along the dotes to read the characters. 
There are around 8 million people just in India who are completely blind. When a blind person or a child wants to learn the Braille characters/language, so he could understand the words and symbols put in any location for them. But to  learn it they have to turn to books or personal tutors which are really expensive. Visually impaired people also use mobiles but when they have to text someone they have to long press each key to hear what it is and then type it, surely it's time consuming and inefficient as there can still be errors. Let's move on to another scenario where a blind person wants to take notes in a meeting or a class, here he/she cannot even use voice mode or take notes with the paper and punch holes. All these are really inefficient as they won't even be able to keep up to the lecture.
The traditional Braille displays present are very expensive which is reduced upto 10 to 12 times by us. There is another american based company called orbit which uses has also made efforts to do the same but it still costs around 40k and can be only used for note taking.

[Mohamed Aamir Khan A](https://github.com/aamir214)

`2026-06-12`

---

### the god sensor
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/the-god-sensor-f297) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/guni7/proof-of-grass/tree/the-god-sensor) [![Built at](https://img.shields.io/badge/Built%20at-ETHPrague%202026-0052CC?style=flat-square)](https://ethprague2026.devfolio.co)

> sensors that do not lie

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square)

**The problem it solves**

In a world increasingly dependent on automated decision-making, we lack a Verifiable Truth Layer for real-world data. 
Centralization Risk: Current IoT and sensor networks rely on centralized APIs that can be manipulated.
Privacy vs. Utility: Proving a location or a climate reading shouldn't require exposing the exact device metadata.
DePIN Scalability: Current "Proof of Physical Resilience" systems are often clunky and expensive to settle on-chain.
GodEye solves this by generating ZK-Proofs at the edge, signing them via Orbitport Satellites for absolute timestamping, and settling them on Ethereum for sub-cent costs.

**Challenges we ran into**

Noir Integration: Compiling complex circuits for tiny edge devices required significant optimization of the ZK-pipeline to fit within enclave memory constraints.
Satellite Latency: Implementing a robust "retry" logic for the Orbitport KMS signing loop to handle transient satellite connectivity.
On-chain Settlement: Balancing the 5-minute uptime requirement with Ethereum's block times—we solved this by implementing a "batch verification" system in the manager contract.
Gas Optimization: Minimizing the cost of reward minting while maintaining a strict on-chain record of every verified proof.

**Ethereum Core**

We advance Ethereum’s foundational infrastructure by building a lightweight, trustless bridge between off-chain hardware and on-chain state. Our ZK-Weather pipeline demonstrates how Ethereum can scale to support millions of DePIN devices without sacrificing security or privacy

**Network Economy**

We implement a robust on-chain economic layer using the $SIGNAL token and ENS identity mapping. It creates a meritocratic economy where hardware operators are rewarded for verified uptime and data accuracy, managed entirely by smart contracts.

**Future Society**

it's a zk oracle for IoT device readings.

it converts normie sensors into god sensors. god sensors know it all. god sensors do not lie. CANNOT LIE*

step 1 - the iot device senses temperature and humidity. 
step 2 - iot device creates signatures containing device-id, firmware version, sensor readings, timestamps and sends it over wifi to system
step 3 - system verifies signatures with public key
step 4 - the system creates a zk proof, which can be system creates a merkle tree with a set of readings. it proves that the readings lie in a certain range of past readings (ie there are no sudden spikes in temperature), and also that the readings lie within a certain threshold(for trigger events).
step 5 - the proof is verified inside A minimal, standalone Ultra Honk ZK proof verifier targeting the USB Armory MK II -- a USB-stick-sized embedded device with an ARM Cortex-A7 @ 900 MHz (no NEON).

**SpaceComputer Bounty**

uses space computer to verify zero knowledge proof of sensor working correctly. 
-- we tried to use kms for cryptographic chip signature

Team **god-sensor** -- [Hiro .](https://github.com/laciferin2024/), [Gunit Malik](https://github.com/guni7/)

`2026-05-10`

---

### SafeBand
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safeband-8d19) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/suYfHGse1RE?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-Hackolution%202K26-0052CC?style=flat-square)](https://hackolution2k26.devfolio.co)

> To protect the ones you love

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

SafeBand is a smart emergency response and safety system designed to provide instant SOS communication even in situations where traditional internet or mobile network connectivity fails. Built using ESP32, GSM, GPS, BLE (Bluetooth Low Energy), and Firebase cloud integration, the system ensures that emergency alerts can still reach nearby devices and responders during critical situations.

The device continuously monitors connectivity conditions and intelligently switches between multiple communication layers depending on availability. In normal conditions, SafeBand uses Wi-Fi and Firebase cloud services to send real-time emergency alerts, GPS coordinates, and live status updates to connected users. If internet connectivity is unavailable, the integrated GSM module sends emergency SMS messages and phone calls containing the user’s live location. In situations where both Wi-Fi and GSM networks fail, SafeBand automatically activates a BLE-based fallback system that broadcasts SOS alerts and GPS coordinates directly to nearby devices through Bluetooth.

The BLE fallback architecture enables nearby phones, laptops, or relay devices to receive emergency notifications without requiring internet access. These devices can then relay the received information to the cloud or display emergency details locally, ensuring that communication is still possible during network outages, disasters, or isolated environments. The system broadcasts real-time SOS alerts for an extended duration to maximize reliability and improve discoverability during emergencies.

SafeBand also integrates live GPS tracking to provide accurate location data with every alert. Emergency notifications include a direct Google Maps link, enabling responders to quickly navigate to the user’s exact location. The web dashboard provides real-time monitoring, BLE notifications, emergency logs, and cloud synchronization for connected devices.

The project addresses major limitations of conventional emergency systems by introducing a multi-layer fallback communication model that prioritizes reliability, redundancy, and accessibility. SafeBand is designed for personal safety applications such as women’s safety, elderly care, disaster response, solo travel, remote area monitoring, and emergency communication in low-connectivity zones.

Key Features:

* Real-time SOS emergency alerts
* Automatic fallback communication system
* Wi-Fi + Firebase cloud integration
* GSM-based SMS and emergency calling
* BLE mesh-style emergency broadcasting
* Live GPS location tracking
* Google Maps emergency navigation
* Offline emergency communication support
* Smart web dashboard for monitoring and alerts
* Low-cost and scalable IoT architecture

**Challenges we ran into**

One of the biggest challenges during development was implementing a reliable fallback communication system when both Wi-Fi and GSM networks were unavailable. Traditional emergency systems heavily depend on internet or cellular connectivity, so creating an offline emergency communication workflow using BLE (Bluetooth Low Energy) required significant experimentation and debugging.

Another major challenge was ensuring stable communication between the ESP32 hardware and the web dashboard using Web Bluetooth APIs. Initially, BLE notifications were failing with GATT-related errors because browser-based Bluetooth communication requires additional BLE descriptors and proper notification handling. This was resolved by redesigning the BLE service architecture, implementing BLE2902 descriptors, and continuously broadcasting SOS packets for an extended duration instead of sending a single notification.

Power management and GSM stability also became critical hurdles. The SIM800L GSM module requires stable voltage and high burst current during SMS transmission and calling. During testing, unstable battery voltage caused random network disconnects and failed GSM registration. The issue was solved by redesigning the power setup using a Li-ion battery with TP4056 charging support and optimizing the module’s power delivery.

GPS integration introduced another layer of complexity, especially indoors where satellite fixes were inconsistent. To improve reliability during demonstrations and emergency conditions, a fallback coordinate system was implemented so the application could still demonstrate emergency routing and location-sharing features even when live GPS signals were temporarily unavailable.

Integrating multiple communication layers — Wi-Fi, Firebase, GSM, GPS, and BLE — into a single synchronized workflow while maintaining real-time responsiveness was another difficult aspect of the project. The final architecture was carefully optimized to dynamically switch between cloud communication and offline BLE fallback modes depending on network availability.

Overall, the project involved solving real-world IoT challenges related to connectivity redundancy, low-power embedded systems, BLE communication reliability, GSM stability, GPS integration, and real-time emergency alert synchronization.

Team **DevNova** -- [Srisanth Singh](https://github.com/sRiSaNtHsINgH)

`2026-05-09`

---

### AquaNode
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aquanode-7361) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://docs.google.com/presentation/d/1a_g2vovWEO2fPgkKlOSGWiDNaRMLEROn/edit?usp=sharing&ouid=103417196698712196611&rtpof=true&sd=true) [![Built at](https://img.shields.io/badge/Built%20at-HACKWAVE%202.0-0052CC?style=flat-square)](https://hackwave2.devfolio.co)

> Saaf paani Shudh paani

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![C](https://img.shields.io/badge/C-333333?style=flat-square)

Team **NextByte** -- [Prabhnoor Singh](https://github.com/PrabhnoorSingh-IITM), [Nilabh kalia](https://github.com/nilabh101), [JAISVEEN KAUR](https://github.com/jaisveenkaur), SIFT KAUR

`2026-05-05`

---

### CubeSat
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/cubesat-e8bf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PD-0707/Self-Healing-CubeSat-On-Board-Computer-with-Autonomous-Fault-Detection-and-Recovery.git) [![Built at](https://img.shields.io/badge/Built%20at-Locus'%20Paygentic%20Hackathon%20--%20#3-0052CC?style=flat-square)](https://paygentic-week3.devfolio.co)

> Self-Healing CubeSat On-Board Computer

![LoRa Alliance](https://img.shields.io/badge/LoRa%20Alliance-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Embedded C](https://img.shields.io/badge/Embedded%20C-333333?style=flat-square) ![Embedded Systems](https://img.shields.io/badge/Embedded%20Systems-333333?style=flat-square) ![I2C protocol](https://img.shields.io/badge/I2C%20protocol-333333?style=flat-square) ![Free RTOS](https://img.shields.io/badge/Free%20RTOS-333333?style=flat-square) ![SPI Protocol](https://img.shields.io/badge/SPI%20Protocol-333333?style=flat-square) ![Analog to Digital Conversion](https://img.shields.io/badge/Analog%20to%20Digital%20Conversion-333333?style=flat-square)

**The problem it solves**

**The Problem**

CubeSats operate in space where **no human intervention** is possible. Even small issues like voltage drops, overheating, or sensor failures can quickly escalate into complete mission failure.

**Existing systems are reactive they rely on ground stations, respond late, and suffer from communication delays.** In real missions, this delay can result in irreversible damage or data loss.

**Our Solution**

We built an Autonomous Self-Healing On-Board Computer (OBC) that:
**Continuously monitors system health (voltage, temperature, motion)
Detects faults in real time
Predicts failures early using a Digital Twin model
Automatically recovers from faults without human intervention
Uses adaptive LoRa telemetry to prioritize critical data**

Why It Matters

This system makes CubeSats:
**Autonomous → no constant ground dependency
Faster in response → milliseconds instead of minutes
More reliable → prevents cascading failures
Longer-lasting → early detection avoids permanent damage**

It shifts satellite systems from reactive → predictive and self-healing.

Impact 

CubeSat missions → improved survival and reliability
Deep space systems → works despite communication delays
Satellite constellations → reduces ground control load

What It Enables

Continuous health monitoring and fault prevention
Safer and more reliable space missions
Reduced risk of unexpected system failure
True autonomous satellite operation

**Challenges we ran into**

One major challenge was frequent **ESP32 crashes during flashing and runtime**, which led to unstable behavior and cases where **no LoRa packets were received at the base station.** This made debugging difficult since the issue could have been from software, hardware, or communication. After investigation, the problem was mainly due to improper SPI initialization, unstable power supply, and repeated flashing without clean resets. I resolved this by ensuring correct LoRa initialization, stabilizing power connections, adding debug logs, and restarting the ESP32 properly after flashing. This significantly improved system stability and ensured reliable telemetry transmission.

**Track: Checkout with Locus**

This project aligns with the **Open Innovation track** because it is not limited to a single platform or application domain like web, Android, or iOS. Instead, it focuses on building a **hardware-based intelligent system** that solves a real-world engineering problem in space systems.

Unlike platform-specific applications, this solution combines **embedded systems, real-time processing, and autonomous decision-making,** making it adaptable to multiple high-impact domains such as aerospace, remote monitoring, and autonomous systems.

The core idea is an **innovative onboard intelligence system for CubeSats** that can independently monitor, predict, and recover from faults. This goes beyond traditional software applications by integrating **hardware + firmware + real-time intelligence**, which is the essence of open innovation creating cross-domain solutions that are not restricted to a single ecosystem.

[Priyadarshini Thiagarajan](https://github.com/PD-0707)

`2026-04-29`

---

### Predictive Maintenance System using Sensor Data
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-predictive-maintenance-system-of-machine-using-sensor-data-85e1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/priyanshukanji-10/AI-Predictive-Maintenance-System-using-Sensor-Data) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/RKVSDBduSmE) [![Built at](https://img.shields.io/badge/Built%20at-Hacktonix%20'26-0052CC?style=flat-square)](https://hacktonix-26.devfolio.co)

> Predict. Prevent. Perform.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kaggle](https://img.shields.io/badge/Kaggle-333333?style=flat-square) ![Core ML](https://img.shields.io/badge/Core%20ML-333333?style=flat-square) ![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-333333?style=flat-square)

Team **Bonchito Bytes** -- [Tathagata Das](https://github.com/tatha730), [Madhurima Dutta](https://github.com/madhurimadutta1601-gif), [Priyanshu Kanji](https://github.com/priyanshukanji-10)

`2026-04-19`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
