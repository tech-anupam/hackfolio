# Hardware and IoT

![Projects](https://img.shields.io/badge/Projects-110-4B32C3?style=flat-square) [![GitHub](https://img.shields.io/badge/GitHub-tech--anupam-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tech-anupam) [![Instagram](https://img.shields.io/badge/Instagram-tech.anupam-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/tech.anupam)

[← Back to all themes](https://github.com/tech-anupam/hackfolio#readme)

---

### trinetra
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/trinetra-0980) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arpit-2005-AD/TriNetra) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/qM-FWszBZWw) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-16-FF6B6B?style=flat-square)

> See Beyond. Secure Everything.

![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![Keras](https://img.shields.io/badge/Keras-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Linux](https://img.shields.io/badge/Linux-333333?style=flat-square)

**The problem it solves**

Traditional security systems often struggle with being slow, unreliable, or resource-intensive. Camera-only solutions frequently generate false alarms due to animals, shadows, or lighting changes, while sensor-only systems lack the contextual intelligence needed to confirm real threats. Additionally, many modern systems rely heavily on cloud processing, introducing latency that makes real-time response difficult. Continuous video streaming further increases bandwidth usage and power consumption, making such systems inefficient and costly, especially in remote or resource-constrained environments.

Trinetra AI addresses these challenges by introducing a multi-layered intelligent IoT intrusion detection system that combines edge sensing, sensor fusion, and AI-based visual validation. It processes data at different levels of the pipeline, enabling faster and more accurate decision-making. At the edge, the ESP32 filters noise using sensor voting and environmental checks, reducing unnecessary alerts. The Raspberry Pi then performs multi-sensor fusion to improve reliability, while the final AI layer uses deep learning to visually confirm whether a detected object is truly a human, significantly reducing false positives.

This system can be used in smart home security, industrial monitoring, restricted zones, campuses, and even remote or border surveillance where connectivity is limited. By operating in an event-driven manner, it activates high-level processing only when needed, thereby saving bandwidth and power. Overall, Trinetra AI makes security systems smarter, faster, and more efficient by reducing false alarms, enabling real-time responses, and minimizing resource usage, offering a reliable alternative to traditional surveillance solutions.

**Challenges we ran into**

1. Camera module failure during hackathon → quickly pivoted to using a mobile phone as a live camera feed, ensuring zero downtime in visual detection

2. Difficulty in sourcing domain-specific audio datasets → conducted extensive research, combined open-source datasets (GitHub + online sources) and generated synthetic data to fill gaps

3. Training specialized sound detection models → optimized dataset quality and preprocessing to achieve reliable model performance despite limited data

4. Raspberry Pi OS booting issues → faced repeated boot failures, resolved through continuous reflashing and boot debugging

5. Compatibility issues with Windows during Pi setup → identified environment limitation, switched to macOS where setup and flashing worked seamlessly

**IoT**

This project fits the IoT track because it connects real-world sensors to a distributed, intelligent pipeline where the ESP32 performs edge-level sensing and filtering, the Raspberry Pi handles fog-level multi-sensor fusion and decision-making, and the compute node runs deep learning for visual validation 
creating a fully integrated system of connected devices that sense, communicate, process, and act in real time.

![image](https://assets.devfolio.co/content/4b25c1c20e584b2fb3dff2f4560ccc0e/f16f28f6-0f79-4a37-ac1e-a73b2c757aa3.jpeg)

Team **Byte Brigade** -- [Arpit Das](https://github.com/Arpit-2005-AD), [Arnab Chaudhuri](https://github.com/Arnab-dot), [Rishaan Kumar](https://github.com/rishaan007), [Ankit Talukder](https://github.com/ankit2061)

`2026-03-22`

---

### EcoGrid
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ecogrid-8fdd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dev5str/ecogrid-insights.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://ecogrid-insights.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/4xUx0Iva4Sw) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-15-FF6B6B?style=flat-square)

> Sustainable Tech Revolution

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![react-dom](https://img.shields.io/badge/react--dom-333333?style=flat-square) ![Ollama](https://img.shields.io/badge/Ollama-333333?style=flat-square)

**The problem it solves**

Every campus, hospital, school, and public space in India is managing its environment the same way it did 30 years ago, with people walking around and checking things manually.

The result:

Dustbins overflow mid week in canteens and corridors because nobody knew they were full

Enclosed labs, wards, and seminar halls accumulate CO₂ and pollutants for hours before anyone notices

Water pipes run through the night and electricity stays on in empty labs, discovered only when the bill arrives

These aren't failures of effort. They are failures of visibility.

EcoGrid Insights solves this by giving institutions a real-time nervous system for their environment:

Smart Waste: Ultrasonic sensors monitor bin fill levels and fire alerts before overflow happens. Staff are dispatched proactively, not reactively.

Air Quality: AQI is monitored continuously in enclosed spaces. When levels cross danger thresholds, air purifiers activate automatically, no human command needed.

Water & Electricity: Flow meters and load sensors track consumption per zone, flagging anomalies the same night they happen.

Every data point feeds an AI prediction engine that learns patterns over time, so EcoGrid doesn't just respond to problems, it prevents them.The platform works across colleges, schools, hospitals, bus stands, railway stations, and corporate offices, any space where people gather and resources are consumed invisibly.

**Challenges we ran into**

1. MQ135 sensor instability on ESP8266
The air quality sensor was the most frustrating component to stabilise. On the ESP8266, the single analog pin (A0) is shared across the board and picks up significant electrical noise, causing wildly inconsistent readings, values would jump 150 points between consecutive reads. The purifier relay was switching on and off every 10 seconds near the threshold, which is both functionally useless and damaging to the hardware.

The fix required three layers:

Averaged sampling: taking 20 readings, sorting them, and discarding the top and bottom outliers before averaging the rest

Hysteresis band: the purifier turns ON at AQI 420 but only turns OFF when AQI drops below 340, preventing relay chatter near the boundary

30-second warm-up delay: the MQ135 filament needs thermal stabilisation before readings are valid; skipping this produced garbage data on cold starts

2. Firebase Firestore rate limiting
Writing all three bins and air data every 10 seconds hit Firestore's free-tier write limits during extended testing. The fix was tracking state locally and only writing to Firestore when values actually changed beyond a meaningful threshold, reducing writes by ~70% without losing data fidelity.

3. SSL time sync on ESP8266
Firebase authentication kept failing with SSL errors until we added configTime() with NTP servers before initialising Firebase, a non-obvious fix that cost significant debugging time.

**Environmental Sustainability**

Environmental sustainability in India is largely treated as a reporting problem, institutions compile evidence once a year for NAAC audits or CSR filings, and the rest of the year nothing is measured, nothing is monitored, and nothing changes.

EcoGrid reframes sustainability as an operational discipline, not a documentation exercise.

Every module directly addresses a measurable environmental impact:

Waste management reduces overflow incidents, prevents hygiene deterioration, and creates a logged record of collection activity, replacing guesswork with data

Air quality monitoring protects human health in enclosed spaces, reducing exposure to pollutants in labs, classrooms, and hospital wards

Water conservation catches leaks and overuse in real-time, with anomaly detection logging estimated savings per month

Electricity efficiency flags after-hours consumption, reduces avoidable load, and calculates CO₂ equivalent avoided, contributing directly to an institution's carbon accountability record

The auto-generated NAAC compliance report converts all monitored data into structured sustainability evidence, aligned with Criterion VII indicators 7.1.2 through 7.1.10, making environmental accountability automatic rather than manual.

EcoGrid turns sustainability from a once-a-year document into a live, daily institutional practice.

Team **ECOGRID** -- [Abhishek Vinod](https://github.com/AbhishekVinod-dev), [Yuvan Avinash](https://github.com/yuvanavinash26), [Amirtheesh U](https://github.com/codehackamir), [Shanjo Benadict](https://github.com/joencrypts)

`2026-03-29`

---

### TASE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tase-f600) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1ZXmwKl5ovX4PBShSYiKTcfmh2KSs44lJ/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-15-FF6B6B?style=flat-square)

> The All Seeing Eye

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square) ![Solidworks](https://img.shields.io/badge/Solidworks-333333?style=flat-square) ![TRANSFORMERS](https://img.shields.io/badge/TRANSFORMERS-333333?style=flat-square) ![FAST API](https://img.shields.io/badge/FAST%20API-333333?style=flat-square)

**The problem it solves**

TASE solves the everyday independence gap faced by visually impaired people: moving safely through real, chaotic environments and understanding what’s around them without relying on other people or unreliable infrastructure. 

A cane can detect obstacles only when they’re very close and provides no awareness of overhanging objects, stairs, moving obstacles, or complex indoor layouts; meanwhile most “smart” assistive devices either become bulky/expensive (sonar/LiDAR-based) or depend on cloud connectivity that introduces latency, recurring cost, and privacy risk, especially impractical in many Indian settings with inconsistent internet access and crowded, noisy streets.

The core problem is not just obstacle detection, but **real-time, context-aware guidance and interaction**: knowing *where* an obstacle is, *how far* it is, and being able to ask “what is this?” or “read this” instantly.

TASE addresses this by turning visual information into intuitive spatial audio cues and enabling offline visual Q&A, so users can navigate and understand their environment continuously, affordably, and privately.

**Challenges we ran into**

1. First and foremost was to test if the solution we're building actually helps the visually impaired. For our research to build the perfect solution, we needed first hand reviews from people actually living those conditions. 
2. Converting depth into surround sound cues required heavy tuning because frequent alerts can overwhelm the user, and multiple obstacles create audio clutter unless you prioritize the most critical one.
3. Running fully offline on a Raspberry Pi 3 B+ exposed hard limits on latency, frame rate, heat, and battery life, and even small delays reduce safety and user trust.
4. Wearability and integration were nontrivial, camera angle and mounting stability affected perception, audio delivery had to preserve ambient awareness, and comfort and durability mattered as much as the model.

Team **Kasukabe Defense Group** -- [Ishaan Badhwar](https://github.com/taimano-sic), [Aarush Mahajan](github.com/aarush-dev), [Aahan Agarwal](https://github.com/aahanagarwal), [Anushka Malhotra](https://github.com/anushka-m-268), [Ekveer Sahoo](https://github.com/Ekron-Shoo)

`2026-02-08`

---

### TACTIX - Digital Twin Tactile Interface
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tactix-digital-twin-tactile-interface-5123) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/th-efool/digital-twin-tactile-interface) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/MW865gGmVJY) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-15-FF6B6B?style=flat-square)

> Physical input interface for Digital Twin systems

![Unity](https://img.shields.io/badge/Unity-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square)

**The problem it solves**

Robotic and Digital Twin systems still rely on **screens, joysticks, or opaque gesture recognition** to translate human intent into action. These interfaces either demand constant visual attention, collapse complex intent into continuous motion, or hide decision-making behind machine learning models that are difficult to interpret and validate.

As a result, there is no simple way to issue **structured, symbolic commands** to a robot or Digital Twin using a **physical, reliable, and inspectable input method** especially in environments where screens, speech, or cameras are impractical.

This project addresses the lack of a **tactile, interpretable input layer** between human operators and Digital Twin systems by encoding intent through **tap location, timing, and intensity** on a soft sensor surface. The result is a deterministic control interface that supports discrete commands, sequences, and replayable interactions without relying on vision or learned models.

**Challenges we ran into**

**1. Noisy piezo signal behavior**
Piezo sensors do not produce clean, repeatable signals. The same physical tap can generate different peak values depending on surface tension, mounting pressure, or nearby impacts. Small vibrations often triggered multiple sensors, while light taps were occasionally missed. Getting consistent detection without hard-coding sensor-specific behavior required careful thresholding and timing control.

**2. Keeping the physical grid and virtual grid in sync**
As soon as grid size, spacing, or orientation became configurable, mapping physical sensor indices to the correct logical tile started to break. Off-by-one errors and mismatched layouts caused taps to land on unintended tiles. This forced a strict indexing model and a single runtime authority for grid generation and validation.

**3. Preventing accidental commands during AR calibration**
While placing and scaling the grid in AR, normal touch interactions overlapped with command input. Without isolation, calibration gestures triggered robot movement. The system had to explicitly separate calibration state from interaction state and ignore all command input until placement was locked.

**4. Supporting both hardware and non-hardware input without duplicating logic**
The same grid needed to respond identically to piezo input, mouse clicks, and touch events. Early versions split this logic, which caused subtle differences in behavior. The input path was refactored so all sources resolve to the same grid activation pipeline.

**Open Track**

This project is research-oriented by design. It’s not trying to solve a single, well-defined end-user problem or deliver a finished application. Instead, it explores **how physical input should be represented, interpreted, and validated** when controlling Digital Twin and robotic systems.

The same setup can be used for robotics experiments, AR interaction, control prototyping, or teaching, *without changing the core system*. That’s because the work is focused on the **interaction model itself**, not a specific outcome or domain. As a result, it doesn’t fit naturally into a vertical track like AR, hardware, or robotics alone.

What’s being evaluated here is the **approach**—a tactile, interpretable input layer that can support many directions of future work. That makes it closer to a research platform or experimental framework than a product, which is why Open Track is the most appropriate category.

Team **TacSys** -- [Agrim Singh](https://github.com/th-efool), None None

`2026-02-01`

---

### unknown
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/zenura-b4dd) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-11-FF6B6B?style=flat-square)

> unknown

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![HTTP server](https://img.shields.io/badge/HTTP%20server-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

Team **ZENITH** -- [Pankaj Garg](https://github.com/Garg-Pankaj29), [Supreet Kaur](https://github.com/not), [ISHA GAUTAM](https://github.com/shiriei), [Aman Jain](https://github.com/amanJTech24)

`2026-03-29`

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

### Controlled Agriculture System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/controlled-agriculture-system-52ec) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/amanbharti-2005/iot_mini_project_AGRO) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://lustrous-vacherin-254bf9.netlify.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/lUKNAgak6fA?si=JbBGGRrbySY0P6K7) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> “Technology Jo Kheti Samjhe”

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![ThingSpeak](https://img.shields.io/badge/ThingSpeak-333333?style=flat-square)

**The problem it solves**

AGRO solves the problem of poor real-time field monitoring and inefficient irrigation.
Using an ESP32 integrated with sensors such as soil moisture, temperature-humidity (DHT), water level, rain, and light sensors, it continuously monitors field and environmental conditions. The system updates sensor data every 15 seconds and automatically controls irrigation through a relay-operated pump based on real-time soil moisture levels, ensuring optimal water usage.

All sensor data is transmitted to the AGRO web app, where the latest sensor readings are displayed in real time, enabling farmers to remotely monitor fields, reduce water wastage, minimize manual effort, and improve crop health through data-driven decisions. Unlike conventional efficient systems that rely on fixed schedules or manual control, AGRO dynamically adapts irrigation using real-time sensor inputs, making it more precise, responsive, and resource-efficient.

![image](https://assets.devfolio.co/content/ce036fece79c466a90bc64b0827a932b/3da98600-7ba7-4948-98f0-299e18bff878.jpeg)

**Challenges we ran into**

During the development of AGRO, the team faced several technical and integration challenges. Initially, the entire system crashed multiple times, and sensors stopped responding, making it difficult to run all sensors simultaneously. Managing multiple sensors together caused stability issues and inconsistent readings.

The hardware setup was extremely complex, especially during the irrigation phase, as different types of pumps were tested before finalizing a suitable one. Establishing a reliable connection between the hardware and software was challenging, and obtaining accurate, real-time data on the ThingSpeak channel required multiple recalibrations and troubleshooting.

The system also faced overheating issues, leading to frequent crashes and the need to reinstall and reconfigure the setup. Additionally, several changes had to be made to the web application to ensure proper data visualization and synchronization with the hardware.

Despite these challenges, continuous testing, hardware optimization, and software improvements helped stabilize the system and improve overall performance.

![image](https://assets.devfolio.co/content/ce036fece79c466a90bc64b0827a932b/ef9ffbca-ec25-4f9b-a093-06a4a6f8b2de.jpeg)

![image](https://assets.devfolio.co/content/ce036fece79c466a90bc64b0827a932b/b4706888-d932-4149-9940-ac5a47273bc0.jpeg)

![image](https://assets.devfolio.co/content/ce036fece79c466a90bc64b0827a932b/54c3243d-ce8a-456e-9a0a-9056887011d1.jpeg)

**Sustainable Development Goals**

AGRO directly contributes to the Sustainable Development Goals by promoting sustainable agriculture and efficient resource management. The system reduces water wastage by using real-time soil moisture data to control irrigation only when required, supporting responsible water usage.

By improving irrigation accuracy and enabling remote field monitoring, AGRO helps farmers increase crop productivity while minimizing resource consumption. This aligns with SDGs such as **Zero Hunger, Clean Water and Sanitation, and Climate Action**, making agriculture more sustainable, resilient, and environmentally friendly.

**Emerging Technologies**

AGRO leverages emerging technologies such as the Internet of Things (IoT) to modernize traditional agriculture. By integrating an ESP32 microcontroller, multiple real-time sensors, cloud connectivity, and automated decision-making, the system enables intelligent monitoring and control of farming operations.

The use of real-time data processing, automation, and web-based remote monitoring transforms conventional irrigation into a smart, adaptive system, showcasing how emerging technologies can solve real-world agricultural challenges efficiently and at scale.

Team **Team Parinde** -- [Anushka CSE](https://github.com/Anushka364/), [Aman Bharti](https://github.com/amanbharti-2005), [ankita Yadav](https://github.com/ankitayadv)

`2026-02-06`

---

### AI & IoT Off- grid Tracking System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-and-iot-off-grid-tracking-system-0f81) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Nevid-786/Off-Grid-Tracking-System) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1qXmKw6zswg95NyPTmZsjRQvkp3iF6Zu0/view?usp=drivesdk) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-4-FF6B6B?style=flat-square)

> Network-independent rescue & safety tracking

![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![NFC](https://img.shields.io/badge/NFC-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Antenna](https://img.shields.io/badge/Antenna-333333?style=flat-square) ![OLED](https://img.shields.io/badge/OLED-333333?style=flat-square) ![Lora](https://img.shields.io/badge/Lora-333333?style=flat-square)

**The problem it solves**

**OVERVIEW**
The Off-Grid Tracking System is an AI and IoT-based solution designed to provide real-time location tracking and emergency communication in areas where mobile networks or internet connectivity are unavailable.

The system uses:

Wearable tracking devices (watches)

LoRa-based long-range communication poles

A central control panel for monitoring

This ensures continuous monitoring and safety in remote and network-dead zones.

**The Problem It Solves**

Many critical environments lack reliable network connectivity, which creates serious safety risks:

**Trekkers and mountaineers** get lost without any way to communicate.

Rescue operations are delayed due to lack of location information.

**Disaster-hit areas** lose communication infrastructure.

**Workers in mines, forests, and remote construction sites** cannot be monitored.

Traditional solutions like mobile phones or GPS trackers fail without network coverage.

Walkie-talkies provide limited range and no location tracking.

Result:
Delayed rescue, increased risk to life, and lack of real-time situational awareness.

**How the Off-Grid Tracking System Solves This**

Uses LoRa technology for long-range communication (up to 5–10 km per pole)

Works without mobile network or internet

Provides real-time location tracking

Includes SOS emergency alert button

Central control panel monitors all users on a live dashboard

AI-based alerts for unusual movement, inactivity, or emergency situations

**Challenges we ran into**

Challenges We Faced
1. LoRa Signal Issues

Problem: Initial communication range was unstable.
Solution: Optimized LoRa settings, used better antennas, and adjusted pole placement through field testing.

2. GPS Delay & Accuracy

Problem: GPS took time to lock and gave inconsistent readings.
Solution: Filtered invalid data and used location averaging for better accuracy.

3. Battery Drain

Problem: Continuous GPS and transmission reduced battery life.
Solution: Implemented sleep mode and reduced transmission frequency.

4. Hardware Integration

Problem: Issues while connecting ESP32, GPS, and LoRa together.
Solution: Proper voltage regulation and module-wise testing before final integration.

5. Real-World Testing

Problem: Difficult to simulate remote conditions.
Solution: Conducted outdoor field tests and optimized system performance.

Team **Neo-gen Innovators** -- [Shiny Dhingra](https://github.com/shinydhingra), [Nevid Alam](https://github.com/Nevid-786), [Anuj Saini](https://github.com/anuj), [Mukul Vaid](https://github.com/Mukul289303), [Sumaira .](https://github.com/sumairasumaira648-svg)

`2026-02-08`

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

### GhostOS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ghostos-ed6b) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://vercel.com/) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Portable Edge AI Hub & Autonomous IOT Workspace

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

### 🚀 Overall Assessment
**Ghost-OS** is an incredibly ambitious and well-architected **"Portable Edge AI Hub & Autonomous IOT Workspace."** It uses an innovative **split-compute architecture** to bridge the gap between lightweight edge single-board computers (a Raspberry Pi) and heavy compute nodes (your laptop/GPU).

**The Architecture:**
*   **The Nervous System (Raspberry Pi):** Acts as the secure backend (FastAPI), hardware controller (GPIO, I2C, Cameras, Arduinos), file system manager (Dead Eye snapshots), and task scheduler.
*   **The Brain & Display (Laptop):** Acts as the UI (React + Electron), GPU accelerator (Ollama/LLMs), and standard input console—all connected via a single USB-C cable or Wi-Fi.

### 🎯 The Core Problems Ghost-OS Solves

Ghost-OS is engineered to solve **five major pain points** for modern developers, makers, and AI engineers:

#### 1. The "It Works on My Machine" Problem (Extreme Portability)
*   **The Problem:** Setting up complex development environments, AI dependencies, and hardware toolchains across multiple computers is incredibly frustrating and time-consuming. Switching laptops usually means losing your perfect setup.
*   **The Ghost-OS Solution (Zero-Footprint Concept):** Your entire operating system, code, and dependencies live on the Pi's SSD. You can plug it into a MacBook, a gaming PC, or a Chromebook via a single USB-C cable and instantly spawn your entire workspace in the browser. You leave absolutely zero footprint on the host machine.

#### 2. Fragmented Developer Workflows
*   **The Problem:** Developers lose hours context-switching. You write code in VS Code, debug in a separate terminal, monitor sensors on a literal physical screen, and switch to a web browser to ask ChatGPT for help.
*   **The Ghost-OS Solution:** It centralizes the entire workflow. The React dashboard brings together terminal access, task scheduling, live sensor telemetry (sparklines), YOLO vision feeds, and system monitoring. On top of that, you have a browser-based Virtual Desktop (via TigerVNC) to run full Linux GUI apps natively on the Pi.

#### 3. Friction in Hardware/IoT Prototyping
*   **The Problem:** Integrating hardware (sensors, Arduinos) with high-level software requires jumping through hoops with serial monitors, C++ compilation, and custom Python scripts. 
*   **The Ghost-OS Solution:** Your Hardware Abstraction Layer handles auto-discovery for I2C sensors (BME280, etc.), provides native GPIO management, and seamlessly integrates an `arduino-cli` wrapper. This makes interacting with hardware as simple as hitting a REST/WebSocket endpoint.

#### 4. The Fear of Breaking the Environment
*   **The Problem:** Running untrusted code, experimenting with intense system installs, or letting AI edit your system files can easily break a Linux environment permanently. 
*   **The Ghost-OS Solution:** You built two hardcore safety nets:
    *   **Dead Eye Snapshots:** Fast, atomic rollback capabilities (rsync/btrfs) let you save the system state before an execution and instantly rewind if something breaks.
    *   **Sandbox Execution:** Running processes in isolated, memory-capped Docker containers or subprocesses, preventing rogue code from destroying the host.

#### 5. AI Developer Friction (The Automation Gap)
*   **The Problem:** AI coding assistants usually just generate textual code that you still have to manually copy, paste, compile, deploy, and debug.
*   **The Ghost-OS Solution:** The **Ghost-Claw Agent**. Instead of just chatting, Ghost-Claw operates an autonomous 5-step pipeline: **READ → ANALYZE → FIX → DEPLOY → VERIFY**. Because you provide it access to the terminal, the sandbox, and the hardware, it can write a C++ sketch, deploy it to the Arduino, read the serial output to verify it worked, and fix it if it didn't—all via natural language commands (e.g., `"fix the permission error on my project folder"`).

### 💡 Summary 
Ghost-OS fundamentally solves **development friction**. 

By turning a Raspberry Pi into a secure, portable, hardware-native backend and relying on the host machine purely as a "dumb terminal" with GPU superpowers, it creates an omnipresent, AI-powered developer ecosystem. ***"Your workspace follows you, not the other way around."***

**Challenges we ran into**

### 1. The Autonomous Code Fixer ("Ghost-Claw" Pipeline)
*   **Challenge:** Getting an AI to reliably output code is easy; getting it to *autonomously* diagnose, write, deploy, and verify code is incredibly hard.
*   **What you ran into:** You likely dealt with the LLM hallucinating code blocks, returning conversational text instead of raw code (e.g., "AI returned no code" errors), or outputting incomplete JSON. Parsing the LLM's raw output robustly to extract commands and execute them on the Pi without human intervention was a massive hurdle.

### 2. Networking & Auto-Discovery in a "Split-Compute" Model
*   **Challenge:** Making the "Plug and Play" USB-C experience actually work flawlessly across different laptops and operating systems.
*   **What you ran into:** Setting up the Raspberry Pi as a USB-Ethernet gadget requires low-level network config. You likely faced issues with IP address collisions, mDNS/Bonjour auto-discovery failing when switching between Wi-Fi and USB, and CORS or WebSocket handshakes failing because the host IP kept changing dynamically.

### 3. Managing Real-Time Asynchronous Chaos (WebSockets)
*   **Challenge:** The React dashboard needs to handle a massive amount of simultaneous live data: system metrics, streaming LLM tokens, raw terminal output, and live sensor telemetry.
*   **What you ran into:** Piping subprocess standard output (`stdout`/`stderr`) reliably over WebSockets without overwhelming the React frontend. You probably had to debug React performance issues, infinite re-render loops from high-frequency sensor polling, or race conditions where WebSocket messages arrived out of order.

### 4. Bridging High-Level AI with Low-Level Hardware (Arduino/GPIO)
*   **Challenge:** Getting the AI agent to compile and flash microcontrollers (like Arduinos) autonomously.
*   **What you ran into:** Automating the `arduino-cli` pipeline meant dealing with cross-compilation errors, raw serial buffer parsing, permission denied errors on `/dev/ttyUSB0`, and writing logic to intelligently parse Arduino compilation error-codes so the AI could understand *why* its code failed to upload and try again.

### 5. Sandboxing vs. Hardware Access Friction
*   **Challenge:** You built a system to execute untrusted code in Docker/subprocesses (Sandbox) while simultaneously needing that code to access physical hardware (GPIO/I2C/Cameras).
*   **What you ran into:** Isolating execution usually means stripping hardware privileges. You would have fought Linux permission systems (`udev` rules, `dialout` groups) and Docker volume mounts to selectively expose the I2C bus and Serial ports to the sandboxed code without compromising the host Pi.

### 6. The "Dead Eye" Snapshot System (State Restoration)
*   **Challenge:** Building an instant "undo" button for a live operating system.
*   **What you ran into:** Implementing reliable file-system snapshots via `rsync` or `btrfs` without freezing the Pi. You had to carefully manage storage space (preventing snapshots from filling the Pi's SSD) and ensure that rolling back files didn't kill the very FastAPI server orchestrating the rollback.

### 7. Integrating a Virtual Desktop in the Browser (VNC)
*   **Challenge:** Streaming XFCE4 into the dashboard so users could open VS Code or VLC.
*   **What you ran into:** Piping an X display server through TigerVNC and websockify/noVNC into a React app is notoriously fragile. You likely fought with resolution hot-resizing, handling virtual displays (`:1`, `:2`), cleaning up zombie VNC processes when the dashboard disconnects, and handling lag/input delay.

### 8. The App Manager Automation
*   **Challenge:** Letting users say `"install VLC"` and having it just work.
*   **What you ran into:** Automating `apt-get` non-interactively requires suppressing prompts and dealing with broken package locks. Furthermore, seamlessly launching that newly installed GUI app onto the correct virtual display so it appears in the user's dashboard (and not in the Pi's physical void) required precise environment variable manipulation (`DISPLAY=:1`).

### Summary
Building Ghost-OS meant fighting on multiple fronts simultaneously: **Linux system administration, web-based network engineering, electrical engineering (IoT), and generative AI engineering.** Solving the friction points where these radically different domains intersect is what makes the project so impressive!

**Best Use of ElevenLabs**

Here are the specific reasons why Ghost-OS is the perfect use-case for ElevenLabs:

### 1. Hands-Free Hardware & IoT Development
This is arguably your strongest specific use case. When a developer is prototyping on your platform—wiring a breadboard, managing GPIO pins, or soldering components connected to the Pi/Arduino—their hands and eyes are completely occupied. 
*   **The Fit:** They can verbally command, *"Ghost-Claw, scan the I2C bus."* Instead of having to put down their tools, walk over to the laptop, and read a terminal output, ElevenLabs can audibly reply, *"Scan complete. I found a BME280 temperature sensor on port 0x76."* This completely removes friction from physical hardware iterations.

### 2. The "Ghost-Claw" Persona and Presence
You aren't just building a text-generation tool; you are building an *agent* with a defined 5-step pipeline (READ → ANALYZE → FIX → DEPLOY → VERIFY). 
*   **The Fit:** Giving Ghost-Claw a voice gives it a distinct **personality and presence in the room**. When the agent encounters an error and has to auto-recover, hearing a calm, hyper-realistic voice say, *"Compilation failed due to a missing semicolon on line 42, deploying fix now..."* makes the user feel like they have a highly competent colleague sitting next to them, rather than a script running in the background.

### 3. Ambient System Monitoring
Developers run a lot of long tasks: `npm install`, compiling C++ for Arduinos, running test suites, or building Docker sandbox containers. Usually, you have to stare at a progress bar or risk forgetting about the task.
*   **The Fit:** With ElevenLabs, Ghost-OS can act as an ambient monitor. You can shrink the dashboard, browse the web, and the system can organically interrupt you with, *"Dead Eye rollback completed successfully"* or *"Sandbox execution timed out after 60 seconds."* It allows true developer multitasking.

### 4. Accessibility and the "Zero-Footprint" Illusion
Ghost-OS is all about extreme portability—plugging a Pi into any laptop and instantly having a full workspace.
*   **The Fit:** By centralizing the intelligence on the Pi but beaming a high-quality ElevenLabs voice through the laptop's speakers (via the browser's Web Audio API), it deepens the illusion that the host laptop is just a "dumb terminal" magically possessed by the Raspberry Pi's high-tech intelligence.

### 5. Emotional Feedback During Development Frustration
Coding is frustrating, especially when fixing broken systems. 
*   **The Fit:** ElevenLabs is known for its incredible emotional prosody. If a user says, *"Claw, my code is broken again,"* the AI can respond with a slightly empathetic or encouraging tone. When a deeply complex bug is finally fixed, the voice can reflect satisfaction. This emotional nuance transforms the user experience from clinical to highly engaging.

In short, Ghost-OS is not just a text interface; it is an **active, physical development hub**. Adding ElevenLabs bridges the gap between the digital code and the physical room you are working in.

**Best Use of Gemini API**

Here is why your project is the perfect fit to be powered by Gemini:

### 1. Native Multimodality for Hardware & Vision Integration
Ghost-OS isn't just a software platform; it interacts with the physical world through the Raspberry Pi Camera and YOLOv8 integrations.
*   **The Gemini Fit:** Gemini was built from the ground up to be natively multimodal (understanding text, code, images, and video simultaneously). With Ghost-OS, a user could point the Pi Camera at their physical Arduino breadboard and ask, *"Why isn't this LED lighting up?"* Ghost-OS can send the live camera frame, the current GPIO state, and the C++ sketch directly to Gemini in one prompt. Gemini can visually trace the wire, read the code, and tell you that pin 13 isn't properly connected. This is a workflow almost no other LLM API can achieve seamlessly.

### 2. The 1M - 2M Token Context Window (Killing RAG)
Your project is an "Autonomous Developer Workspace." When a user tells the Ghost-Claw agent to *"fix the permission error on my project folder,"* the agent needs context.
*   **The Gemini Fit:** Traditional LLMs require complex, brittle RAG (Retrieval-Augmented Generation) pipelines to search for relevant files before answering. With Gemini 1.5's massive context window, Ghost-OS can literally take the entire system status, the last 500 lines of terminal logs, and the contents of a user's entire project directory and dump it straight into the prompt. The AI has perfect context of the *entire* Ghost-OS environment instantly, leading to vastly superior debugging.

### 3. Native Structured Output & Tool Calling for "Ghost-Claw"
The core of your automation is the **Ghost-Claw pipeline: READ → ANALYZE → FIX → DEPLOY → VERIFY.** To achieve this autonomously, the AI cannot just reply with conversational text; it must output precise, machine-readable instructions that the FastAPI backend can safely run in the Docker Sandbox.
*   **The Gemini Fit:** Gemini has exceptionally reliable JSON mode and Function/Tool Calling capabilities. You can enforce strict JSON schemas so Gemini consistently replies with `{"action": "execute_bash", "command": "apt-get install vlc"}`. This stability is the difference between a bot that *suggests* code and an agent that actually *runs* the OS autonomously.

### 4. Code Proficiency Across a "Full-Stack + Hardware" Environment
Ghost-OS spans one of the widest technical stacks imaginable. You have:
*   **Hardware:** C++ (Arduino), Python `RPi.GPIO`
*   **Backend:** Python (FastAPI, WebSockets), Linux Bash scripting, Docker
*   **Frontend:** React, JavaScript, Electron
*   **The Gemini Fit:** Gemini handles extreme context-switching brilliantly. Because it is highly proficient across frontend, underlying Linux server administration, and low-level embedded hardware, you only need exactly one API provider to orchestrate every layer of your architecture.

### 5. Gemini 1.5 Flash for Real-Time "Edge" Feel
Because Ghost-OS utilizes a "split-compute" architecture where the user opens a browser on their laptop to control the Pi, latency is critical. If the user tells the system to rollback a "Dead Eye Snapshot," it needs to feel instantaneous.
*   **The Gemini Fit:** The inference speed of Gemini 1.5 Flash is incredible. It allows Ghost-Claw to loop through its "Analyze -> Fix -> Verify" stages at a speed that feels like magic to the user, powering real-time web-socket updates on the dashboard without annoying buffering pauses. 

**In Summary:** Ghost-OS pushes beyond standard software AI into the realm of **Physical AI and Operating System automation**. Gemini's unparalleled context length, blazing speed, and native visual processing make it the ultimate "engine" for a project trying to act as an omniscient, hardware-aware Jarvis.

Team **3Bits** -- [Saikat Debnath](https://github.com/heyySaikat), [Aniket Chakraborty](github.com/A-N-IKET), [Anirban Das](https://github.com/anirban222777das)

`2026-04-05`

---

### S.A.F.E.
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safe-6902) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ayushkumar2601/fire_hard) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://www.canva.com/design/DAG_hnGLZ3U/s2vE_tg-jpMJCWTMT3PtQQ/edit?utm_content=DAG_hnGLZ3U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/gLaKeGysVLs?si=daCAtrnPZd1emr-Q) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Smart Adaptive Fire Evacuation

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Next.js](https://img.shields.io/badge/Next.js-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![React.js](https://img.shields.io/badge/React.js-333333?style=flat-square) ![Supabase](https://img.shields.io/badge/Supabase-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Traditional fire safety systems in most buildings rely heavily on **audible alarms and static exit signs**. While these alarms alert people that a dangerous situation is occurring, they rarely provide guidance about *where occupants should go next*. In real emergency situations such as fires, smoke spread, or electrical hazards, this lack of directional guidance can cause ***panic, confusion, and inefficient evacuation***. People often move toward the nearest visible exit sign without knowing whether that route is actually safe, which can unintentionally lead them closer to the hazard instead of away from it.

![image](https://assets.devfolio.co/content/8d37b2cbc9fe47119ba5d4082dabfd4d/d294127c-4205-4bf1-bea6-ed202a029ce8.png)

In crowded environments such as offices, malls, university buildings, hospitals, and public infrastructure, evacuation becomes even more complicated. When an alarm sounds, people may rush toward the same exits, creating **bottlenecks and congestion**. At the same time, some evacuation paths may already be unsafe due to smoke, fire spread, or blocked corridors. Traditional alarm systems cannot dynamically respond to these changing conditions. As a result, occupants are forced to rely on instinct rather than accurate situational guidance during the most critical moments.

The **Smart Fire Evacuation Network** addresses this problem by transforming conventional alarm systems into ***intelligent evacuation guidance systems***. Instead of only detecting hazards and triggering alarms, the system actively helps guide occupants toward safer routes in real time. The system is built using a decentralized network of **ESP32-based IoT nodes**, each equipped with smoke and fire detection sensors. These nodes are placed across different zones of a building such as corridors, junction points, stairways, and exit areas.

![image](https://assets.devfolio.co/content/8d37b2cbc9fe47119ba5d4082dabfd4d/7ece2417-4ff3-42fa-8d74-46cf464c07d9.png)

When a node detects smoke or fire, it immediately broadcasts a hazard alert to nearby nodes using **ESP-NOW peer-to-peer communication**, a low-latency wireless protocol that allows devices to communicate directly without relying on a central WiFi router or internet connection. This decentralized architecture ensures that hazard information spreads across the building network within milliseconds, allowing the system to quickly update evacuation guidance.

Once the hazard is identified, nearby nodes automatically update their internal status and activate **visual LED indicators** to guide occupants away from danger. Instead of static exit signs that always point in the same direction, the system creates ***dynamic evacuation routes*** based on the current hazard location. Areas that are unsafe are marked with red indicators, while safer routes and exits are highlighted with green indicators, allowing occupants to intuitively follow the safest path out of the building.

This approach significantly improves evacuation safety by reducing confusion and helping occupants make faster decisions during high-stress emergencies. Because the system operates ***offline and without centralized infrastructure***, it remains functional even if internet connectivity fails or building network systems go down during a disaster.

![image](https://assets.devfolio.co/content/8d37b2cbc9fe47119ba5d4082dabfd4d/29a0c07c-37a6-4517-8937-185f5b246729.png)

Beyond fire safety, this concept can be extended to **industrial safety environments, large campuses, smart buildings, and public transportation hubs** where rapid hazard detection and guided evacuation can save lives. By combining IoT sensing, decentralized communication, and adaptive visual guidance, the Smart Fire Evacuation Network transforms traditional alarms into ***intelligent life-saving infrastructure*** designed to improve emergency response and evacuation efficiency.

**Challenges we ran into**

## Challenges I Ran Into

Building a decentralized evacuation system using multiple ESP32 nodes introduced several technical challenges during development. One of the biggest hurdles was ensuring **reliable real-time communication** between nodes using *ESP-NOW*. In early prototypes, hazard alerts were sometimes not reaching all nodes consistently, which caused incorrect LED guidance during testing. This issue was mainly due to packet loss and improper peer configuration. I solved this by refining the broadcast logic, adding retry mechanisms, and carefully registering peers across all nodes to ensure stable communication.

Another challenge involved the **MQ-2 smoke sensors**, which are known to produce noisy and inconsistent readings. During initial tests, the sensors occasionally triggered false alarms because they react to other gases like alcohol fumes or environmental changes. To address this, I implemented a simple filtering approach using multiple sensor readings and averaging them before evaluating the threshold value. I also spent time calibrating the sensor thresholds experimentally so that the system would detect smoke reliably without triggering unnecessary alerts.

Hardware synchronization between nodes was another obstacle. Since each ESP32 node represents a different zone in the building, their states needed to update quickly and consistently. I implemented timestamp-based message handling so that nodes could ignore outdated messages and always reflect the most recent hazard state.

Finally, integrating the **hardware network with the software dashboard and floor-plan visualization** required careful API and data structuring to ensure that real-time alerts from nodes could be accurately represented in the monitoring interface.

Overcoming these challenges helped make the system ***more stable, reliable, and responsive***, ensuring that hazard alerts propagate across the network in under a second and evacuation guidance remains accurate during emergency scenarios.

**Safety**

## Safety Track Alignment

The **Smart Fire Evacuation Network** directly aligns with the goals of the *Safety Track* by addressing one of the most critical challenges in emergency response: **safe and efficient evacuation during fire incidents**. Traditional fire alarm systems only notify occupants that danger exists, but they do not provide guidance on *how to safely exit a building*. In high-stress situations, this often leads to confusion, panic, and dangerous crowd movement toward unsafe areas.

Our project transforms conventional fire detection systems into ***intelligent evacuation guidance infrastructure***. By using a decentralized network of **ESP32-based sensor nodes**, the system detects smoke or fire hazards in real time and instantly communicates this information across the building using **ESP-NOW peer-to-peer communication**. This allows the system to quickly identify which areas are dangerous and dynamically guide occupants away from those zones.

Instead of relying on static exit signs, the system uses **LED indicators placed across corridors and evacuation routes** to visually direct people toward the safest available exits. Hazard zones are clearly marked, while safe paths are highlighted, enabling occupants to make faster and safer decisions during emergencies.

Another important safety aspect of the system is its ***offline-first architecture***. Because the nodes communicate directly without requiring internet connectivity or centralized infrastructure, the system remains operational even if building networks fail during a disaster. This improves reliability and ensures that evacuation guidance continues to function under critical conditions.

By combining **real-time hazard detection, decentralized communication, and adaptive evacuation guidance**, the Smart Fire Evacuation Network enhances building safety and demonstrates how IoT technology can be used to create smarter, more responsive emergency management systems.

Team **Cyber Yoddhas** -- [Dhiraj kumar chowdhury](https://github.com/Dhirajchowdhury), [Shaista Meher](https://github.com/shaistameher), [AYUSH KUMAR](https://github.com/ayushkumar2601)

`2026-03-28`

---

### FPGA-based Time Domain Reflectometer (TDR)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fpgabased-time-domain-reflectometer-tdr-7803) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/garvk1708/FPGA-TDR) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> TDR on FPGA with AI-driven cable diagnostics.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Hardware Magic](https://img.shields.io/badge/Hardware%20Magic-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Verilog](https://img.shields.io/badge/Verilog-333333?style=flat-square)

**The problem it solves**

Modern infrastructure — from telecommunication networks and data centers to power distribution systems — relies heavily on long transmission cables. When these cables develop faults such as open circuits, short circuits, or impedance mismatches, locating the exact fault position becomes extremely difficult.

Traditional fault detection methods often require manual inspection, specialized diagnostic equipment, or physical cable replacement, which can be time-consuming, expensive, and disruptive to critical systems. In large networks, a single hidden cable fault can lead to network downtime, signal degradation, or system failure, impacting operations and reliability.

Our FPGA-TDR system simplifies this process by acting like radar for cables. It sends a high-speed electrical pulse through the transmission line and analyzes the reflected signal to determine both the location and type of fault with high precision.

What People Can Use It For

Telecommunications: Quickly locate faults in network cables and communication lines.

Power infrastructure: Detect and diagnose faults in underground or long-distance power cables.

Data centers: Monitor large cable networks and reduce downtime caused by hidden faults.

Electronics development: Diagnose signal integrity issues in high-speed PCB traces and wiring systems.

Industrial maintenance: Enable technicians to find cable faults without dismantling or replacing entire wiring systems.

How It Makes Existing Tasks Easier

Our system improves traditional diagnostics by combining high-precision FPGA signal processing, IoT connectivity, and AI-assisted analysis.

⚡ Faster diagnostics: Faults can be located within seconds instead of hours of manual inspection.

📡 Remote monitoring: IoT integration allows cable health to be monitored through a live web dashboard.

🤖 Predictive maintenance: AI-powered analysis can identify patterns and predict future cable failures.

💰 Lower cost: Provides an affordable alternative to expensive industrial TDR equipment.

By transforming traditional cable testing into a smart, connected, and predictive diagnostic system, our solution helps industries reduce downtime, improve safety, and maintain critical infrastructure more efficiently.

**Challenges we ran into**

Building a high-precision hardware system that integrates FPGA signal processing, IoT communication, and AI analysis came with several technical challenges.

Debugging the FPGA Logic
A significant amount of time was spent debugging the FPGA modules responsible for pulse generation, timing measurement, and signal detection. Small timing errors in hardware logic could significantly affect the accuracy of the TDR measurements.

Accurate Distance Measurement
Initially, the calculated fault distance was not accurate. To solve this, we calibrated the system by testing cables of known length and calculating the signal velocity factor, which allowed us to correctly map time delay to physical distance.

AI Integration with the Dashboard
Integrating AI-based analysis into the web dashboard using the Gemini API was challenging. Ensuring the processed cable diagnostic data could be correctly interpreted and displayed in a meaningful way required multiple iterations.

Data Transmission Issues
At one stage, the ESP8266 was successfully transmitting data, but it was not appearing on the server. Debugging the communication pipeline between the device, server, and dashboard required careful troubleshooting of network requests and backend endpoints.

Hardware Connection Complexity
Establishing reliable hardware connections between the FPGA board, transmission line interface, and IoT module was difficult. Ensuring stable signal transmission while avoiding noise and incorrect triggering required careful wiring and testing.

Signal Noise and Reflection Detection
Separating real reflections from noise in the signal path was another challenge. We had to refine the detection logic to ensure the system responded only to valid reflection signals.

Coordinating Hardware, Firmware, and Cloud Systems
Since the project combines FPGA hardware design, embedded IoT communication, and cloud-based visualization, synchronizing all components to work seamlessly required extensive integration and testing.[](url)

**Electrothon 8.0 Winners**

Our project stands out because it tackles a real engineering problem using a combination of advanced hardware and modern software technologies. While many projects focus only on software solutions, we built a working hardware system from scratch that performs high-precision cable fault detection using an FPGA-based Time Domain Reflectometer.

What makes our project unique is the modern implementation approach. Traditional TDR systems are expensive industrial instruments, but we recreated this concept using a Cyclone IV FPGA with a multi-phase Time-to-Digital Converter, enabling high-resolution fault detection through custom hardware logic. This required deep work in digital design, signal timing, and hardware debugging, which goes beyond typical hackathon projects.

At the same time, we didn’t stop at hardware. We extended the system by integrating IoT connectivity through an ESP8266 and AI-assisted analysis through the Gemini API, allowing the device to send diagnostic data to a cloud dashboard and analyze cable health for predictive maintenance.

Because of this, our project is not just a prototype—it is a complete ecosystem that combines hardware engineering, embedded systems, networking, and AI. This rare blend of FPGA-based hardware innovation and intelligent software integration makes our solution both technically challenging and highly practical.

In short, our project stands out because it brings together deep electronics engineering with modern intelligent systems, creating a solution that reflects the spirit of Electrothon: pushing the boundaries of what can be built when hardware and software work together.

**Electrothon 8.0 Honors Track**

***HARDWARE TRACK***

Our project is fundamentally a hardware-first innovation built around a custom FPGA-based Time Domain Reflectometer (TDR) designed to detect and locate faults in transmission cables with high precision. Instead of relying on software simulations or off-the-shelf diagnostic tools, we implemented the core functionality directly in hardware using a Cyclone IV E FPGA, enabling nanosecond-level timing measurements and real-time signal analysis.

Reasons We Fit the Best Hardware Hack Category

Custom Hardware Implementation
The core fault-detection logic is implemented at the hardware level on an FPGA, including pulse generation, reflection detection, and a multi-phase Time-to-Digital Converter (TDC) for high-resolution timing measurement.

High-Speed Signal Processing
The system performs real-time digital signal processing directly on the FPGA, allowing accurate detection of signal reflections and precise calculation of cable fault locations.

Complex Hardware Integration
The project integrates multiple hardware components, including the FPGA board, transmission line interface, and ESP8266 IoT module, requiring careful circuit connections, timing synchronization, and signal handling.

Hardware + IoT + AI Ecosystem
While the core innovation lies in hardware, we extended the system by integrating IoT connectivity for remote monitoring and AI-based predictive maintenance, demonstrating how advanced hardware systems can power intelligent infrastructure solutions.

Team **ECE KE SHER** -- [Kritika bhandari](https://github.com/KritikaBhandari), [Shranya Thakur](https://github.com/Shranya24), [Shubham Pathak](https://github.com/ShubhmPathak02), [Garv Kapoor](https://github.com/garvk1708)

`2026-03-15`

---

### WiFi CRO
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/wifi-cro-5c7d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Naman1177/WIFI_CRO) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1rVGG4GUArWKFOIuTq2kKLgNRNvUQqXf-/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/XVA78UlYc90) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Not your usual Electronics lab CRO!

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![NodeMCU IoT](https://img.shields.io/badge/NodeMCU%20IoT-333333?style=flat-square) ![HTML5​](https://img.shields.io/badge/HTML5​-333333?style=flat-square)

**The problem it solves**

Traditional oscilloscopes, especially those based on Cathode Ray Oscilloscope technology, were bulky, expensive, and required specialized hardware to visualize electrical signals. Even modern **Digital Storage Oscilloscope devices remain costly and are often inaccessible for many students, hobbyists, and small labs.

Because of this, many learners struggle to observe real-time voltage and current waveforms while experimenting with circuits. A low-cost, portable, and easy-to-use solution is needed that can display electrical signals without requiring dedicated oscilloscope hardware or software installation.

WiFi-CRO addresses this problem by providing a browser-based oscilloscope that streams real-time waveform data over WiFi using inexpensive components.

**Challenges we ran into**

ADC Speed Limitation – The ESP8266 and ADS1115 have limited sampling rates, making it challenging to capture smooth waveforms and restricting the frequency range to about 200 Hz.

Handling Negative AC Signals – Standard single-ended ADC readings cannot represent negative voltages. Implementing differential measurement mode was necessary to correctly capture the full AC waveform.

Protecting the ADC Inputs – Ensuring the ADC never received more than 3.3 V required careful design of voltage dividers and protection using a Zener diode.

Current Sensor Scaling – The ACS712 outputs up to 4.5 V, which exceeds the ADC limit. Designing a proper resistor divider while maintaining measurement accuracy was necessary.

Noise in Measurements – Breadboard wiring and long probe leads introduced noise in signals. This required adding filtering capacitors and improving grounding.

Real-Time Data Streaming – Efficiently sending ADC data over WiFi without slowing down waveform updates required optimizing the HTTP data transfer from the ESP8266 to the browser.

AI Integration – Integrating waveform data with Google Gemini 2.5 Flash for automated signal diagnosis required structuring sensor data in a way that the AI could correctly interpret.

**Electrothon 8.0 Honors Track**

BEST HARDWARE HACK
BEST BEGINNERS

**Google Cloud**

GEMINI API CHALLENGE

Team **Team dracarys** -- [Naman Malhotra](https://github.com/Naman1177), [mayank thakur](https://github.com/mayank), Garima Pathania, [Ayushi Sharma](https://github.com/ayushiiish)

`2026-03-15`

---

### SHE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/she-f3fd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Maan-Sharma/Shesafe) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/shorts/tavoe3dXLuE?si=mKQ4FVdB2T3L4Ggp) [![Built at](https://img.shields.io/badge/Built%20at-The%20XiBit-0052CC?style=flat-square)](https://the-xibit.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> AI & Sensor-Based Women Safety System

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Android SDK](https://img.shields.io/badge/Android%20SDK-333333?style=flat-square) ![Google Maps API](https://img.shields.io/badge/Google%20Maps%20API-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Android MediaProjection API](https://img.shields.io/badge/Android%20MediaProjection%20API-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Women often face unsafe situations while traveling alone, commuting at night, or being in unfamiliar places. In many emergencies, it becomes difficult to quickly contact family members or emergency services because the person may be under stress, unable to unlock their phone, or unable to make a call.

The **She – Women Safety App** is designed to provide a fast and reliable way to request help during dangerous situations.

### How It Helps

* 🚨 **Instant Emergency Alerts**
  Users can send an SOS alert to trusted contacts immediately with their location.

* 📍 **Automatic Location Sharing**
  The app sends the user's live location so family or friends can quickly find them.

* 🎤 **Voice Activation for Emergencies**
  If the user cannot use the phone manually, voice commands like **“Help me”** can trigger emergency actions.

* 📳 **Fall Detection for Critical Situations**
  Using phone sensors, the app detects a fall and starts a countdown. If the user does not respond, the app automatically sends emergency alerts.

* 📞 **Quick Emergency Calling**
  Users can call emergency contacts instantly from within the app.

### Why It Matters

By combining **sensor detection, voice commands, and instant communication**, the app reduces the time needed to ask for help and ensures that emergency contacts are notified as quickly as possible. This makes everyday activities like **traveling, commuting, or walking alone** safer and more secure.

**Challenges we ran into**

## Challenges I Ran Into

Building the **She – Women Safety App** involved several technical challenges while implementing real-time emergency features.

### 1. Voice Command Detection in Background

One of the biggest challenges was enabling the app to detect voice commands like **“Help me”** even when the app is not actively open. Android restricts background microphone usage for privacy and battery reasons.

**Solution:**
I implemented a **foreground service with speech recognition**, which allows the app to continue listening for emergency commands while respecting Android's permission and lifecycle policies.

---

### 2. Reliable Fall Detection

Detecting a real fall using phone sensors was difficult because normal movements like **running, jumping, or dropping the phone** could trigger false alerts.

**Solution:**
I used data from the **accelerometer sensor** and applied threshold checks along with a **10-second confirmation countdown**. This allows the user to cancel the alert if it was triggered accidentally.

---

### 3. Sending Emergency Alerts with Location

Another challenge was ensuring that the app could quickly send **SMS alerts along with the user’s live location**. Sometimes location services take time to fetch accurate coordinates.

**Solution:**
I optimized the location request using **Android Location Services** to get the most recent available location quickly before sending the emergency message.

---

### 4. Permission Management

Modern Android versions require multiple runtime permissions such as **location, SMS, microphone, and sensors**. Managing these permissions smoothly without confusing the user was challenging.

**Solution:**
I created a **structured permission request flow** that explains why each permission is needed, ensuring the app remains user-friendly while still having access to critical safety features.

---

### What I Learned

Through these challenges, I gained deeper experience with **Android services, sensor data processing, runtime permissions, and real-time emergency communication systems**.

**Open Innovation**

## How the Project Fits into the Open Innovation Track

The **She – Women Safety App** aligns with the **Open Innovation track** by addressing a real-world social problem using technology and scalable digital solutions. Open Innovation encourages developers to build solutions that can be adapted, improved, and used by a wide community to solve important challenges.

This project focuses on **improving personal safety for women** by leveraging smartphone technologies such as **sensors, voice recognition, location services, and emergency communication**.

### Contribution to Open Innovation

* **Solving a Real-World Problem**
  Women’s safety is a major global concern. This application provides a practical technological solution that can help reduce response time during emergencies.

* **Technology-Driven Safety Solution**
  The app uses existing smartphone capabilities such as **accelerometer sensors, GPS location, and voice recognition** to create an intelligent safety system that works in real-life scenarios.

* **Scalable and Extendable**
  The project can be expanded with additional features such as AI-based threat detection, smartwatch integration, and integration with public emergency services.

* **Community Impact**
  By making the project open and shareable, developers and organizations can build upon it to create better safety solutions for communities.

### Vision

The long-term vision of **She** is to create a **technology-driven safety ecosystem** that empowers women with tools that can quickly connect them to help when they need it most. By encouraging collaboration and innovation, this project contributes to the broader goal of building safer and more inclusive communities.

Team **NextGen Devs** -- [Ayush sharma](https://github.com/Ayushsharma113), [ADITYA ROUTH](https://github.com/ADITYA-ROUTH/), [Asif Hussain Tahiri](https://github.com/asif922), [MANMOHAN SHARMA](https://github.com/Maan-Sharma)

`2026-03-11`

---

### KAi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/kai-ee2b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/thukuna-ai/kai) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Umdx9_kAJ3Y) [![Built at](https://img.shields.io/badge/Built%20at-Build%20India:%20Anthropic%20x%20Replit%20x%20Lightspeed%20Hackathon-0052CC?style=flat-square)](https://buildindia2026.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> We'll handle the store for you

![Expo](https://img.shields.io/badge/Expo-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Svelte](https://img.shields.io/badge/Svelte-333333?style=flat-square) ![Replit](https://img.shields.io/badge/Replit-333333?style=flat-square)

**The problem it solves**

India's 12M+ Kirana stores command 88% of the $900B retail market, yet while UPI digitized payments, the operations — inventory, expiry tracking, shelf management, accounting — remain analog. Shopkeepers lose revenue to expired stock they can't track, stockouts they can't predict, and customers they can't reach digitally. Meanwhile, Quick Commerce (Blinkit, Zepto) is eating their market share using the exact data intelligence Kiranas lack.

Worse: Kiranas are invisible to the AI agent economy. When a customer asks Claude or ChatGPT to "order groceries from my local store," Kirana shops simply don't exist in that ecosystem. They have no structured catalog, no API, no way to receive agent-driven orders. They're being bypassed entirely.

We solve three problems at once:
  1. The Operations Gap — A dedicated hardware device (not a phone app) scans barcodes, detects objects via YOLO, reads expiry dates, and auto-builds a live catalog. No manual data entry. No literacy barrier Voice-first, multimodal interaction in Hindi/Hinglish/indic local language.
  2. The Intelligence Gap — Instead of a dumb POS, we give shopkeepers a "Digital Munim" (AI Accountant) that proactively alerts on expiring batches, suggests restocking, tracks credit (khata), and delivers daily profit insights — all via WhatsApp/Telegram chats/ voice notes or our native app - whatever they feel comfortable with.
  3. The Discoverability Gap (Agentic Commerce) — We expose every Kirana's real-time inventory via UCP (Universal Commerce Protocol) APIs, making them discoverable and transactable by any AI agent. Customers can say "buy rice from my nearest Kirana" to any AI assistant, and the order flows through — with Visa TAP (Trusted Agent Protocol) handling secure payment, and the shopkeeper approving via WhatsApp. No app download needed by the customer. No marketplace commission.


We don't just digitize the Kirana. We make it AI-native.

Built with love using
Replit Agent : Mobile App
Claude Code / Claude models: Everything else was entirely vibe coded

**Challenges we ran into**

1. Barcode scanning reliability on RPi4 — Camera autofocus latency and poor lighting in typical Kirana environments made real-time barcode decoding unreliable. We solved this by combining pyzbar with framepreprocessing (contrast normalization, sharpening) and implementing debounce logic to avoid duplicate scans.
2. YOLO for Indian retail SKUs — Pre-trained COCO models don't recognize Indian products (Maggi packets, loose dal, local brands). We used YOLOv8-Nano with transfer learning on a small custom dataset of common Kirana items, but getting accuracy above 85% in 5 hours was tough. We fell back to a hybrid approach: barcodes for branded goods, vision AI only for loose/unbranded items.
3. UCP/Agentic Commerce integration — Building the full agentic commerce flow (catalog discovery → reserve → checkout → Visa TAP payment) end-to-end was the hardest technical challenge. We had to design the inventory API to serve both the shopkeeper's UI and external AI agents simultaneously, with real-time stock reservation and 10-minute expiry windows to prevent overselling.
4. Multimodal voice interaction — Making the system understand Hinglish voice commands ("Kitna rice bacha hai?") in noisy shop environments required careful prompt engineering and fallback logic. We used Telegram voice notes as the primary channel since WhatsApp Business API has cost constraints for a hackathon.
5. Real-time sync across hardware, web UI, and Telegram — Keeping inventory state consistent across the scanner (RPi4), the Svelte dashboard, and the Telegram bot required WebSocket-based event streaming. Race conditions during simultaneous scanning and agent orders were a real headache.

Team **Thukuna** -- [Sanskar Omar](https://github.com/sanskaromar), [Shashank Verma](https://github.com/shank03), [Priyav Kaneria](https://github.com/PriyavKaneria)

`2026-02-15`

---

### Riventhra
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/riventhra-8705) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://riventhra1.web.app/) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-3-FF6B6B?style=flat-square)

> Let the River breath again

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Rivers are among the most critical ecological systems supporting human life, agriculture, and biodiversity — yet most river monitoring today is manual, infrequent, and reactive.Water samples are typically collected periodically and tested in laboratories. This process introduces major limitations:

1. Pollution events go undetected for hours or days
2. Contamination spreads before authorities can respond
3. Continuous environmental visibility is absent
4. Data is fragmented and not centralized
5. Predictive analysis is nearly impossible

Riventhra addresses this gap by creating a real-time river intelligence layer.
Using IoT sensing nodes, the system continuously monitors core water quality indicators such as temperature, pH, and turbidity. Data is transmitted to the cloud, logged historically, and visualized through a live dashboard.

**Challenges we ran into**

I encountered ESP32 library and board package errors in the Arduino IDE, which caused compilation failures. Reinstalling the ESP32 core packages and updating the toolchains resolved the issue.

On the frontend side, Live Server threw routing errors such as:
    "Cannot GET /xyz.html"

This was caused by incorrect file paths and directory structure mismatches, which were fixed by aligning routes and project folders correctly.

Another hurdle was the `EMFILE: too many open files` error during local hosting. Increasing the system file descriptor limit and restarting the development server resolved the scanning issue.

These challenges helped stabilize the hardware–cloud–frontend pipeline required for real-time monitoring.

**Google Gemini**

used chatbot

Team **CodeSmiths** -- [Prabhnoor Singh](https://github.com/PrabhnoorSingh-IITM), [Sarabjot Singh](https://github.com/sarabjot005), [Mehak Sahdev](https://github.com/mehakksahdev12-max), [Harshleen Kaur](https://github.com/harshleenkaur2007-ux), [JAISVEEN KAUR](https://github.com/jaisveenkaur)

`2026-02-08`

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

### ARANYASHIELD
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/aranyashield-50c0) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Sp6MQwiI-LY) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Protecting Nature With Intelligent Eyes in the SKY

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

To understand the true value of AranyaShield, it helps to look at it not just as a drone, but as a bridge between high-altitude satellite monitoring and ground-level manual patrolling.

In a dense forest, the "Canopy Gap" is where most environmental crimes and disasters hide. Here is the breakdown of the specific problems this system solves:

1. The "Blind Spot" of Traditional Surveillance
Satellites are great for spotting massive fires, but by the time a fire is big enough to be seen from space, it's often too late to contain.

The Problem: Dense foliage hides early-stage smoke and small heat signatures.

The Solution: AranyaShield flies under or at the canopy level. Its MQ-series smoke sensors detect chemical traces of fire long before a thermal camera sees a flame through the leaves.

2. The Acoustic "Invisibility" of Illegal Logging
Illegal loggers and poachers are experts at hiding from visual patrols. They use the vastness of the forest to their advantage.

The Problem: Rangers cannot be everywhere at once, and cameras only see what is directly in front of them.

The Solution: The Sound Sensor acts as a 360-degree "digital ear." It can trigger an alert based on the specific frequency of a chainsaw or a gunshot, even if the activity is happening behind a thicket of trees where the camera can't see.

3. The "GPS-Denied" Navigation Trap
Standard commercial drones rely heavily on clear GPS signals. In deep valleys or under heavy tree cover, GPS signals "bounce" (multipath error) or drop entirely, leading to drone crashes.

The Problem: Traditional autonomous flight fails in the very environment where it is needed most.

The Solution: By using Ultrasonic Sensors for localized obstacle avoidance and altitude hold, the drone creates a "safety bubble" around itself. It doesn't just rely on a coordinate in the sky; it "feels" the trees around it to prevent collisions.

4. The Response Time Gap (Search & Rescue)
When a person goes missing in a forest, every hour reduces the chance of survival. Ground teams move slowly through thick underbrush.

The Problem: Human search parties are limited by fatigue, daylight, and terrain.

The Solution: The drone can cover 10x the area of a ground team in the same time. By using the ESP32 to process data at the "Edge," it doesn't need to send video back to a server to "think." It can identify a human thermal signature or a distress whistle (via the sound sensor) and instantly broadcast the exact GPS coordinates to the rescue team's handheld devices.

**Challenges we ran into**

Gemini said
Building a sophisticated hardware-software hybrid like AranyaShield on an ESP32 stack is a massive undertaking. While the vision is high-tech, the reality of building it usually involves "fighting" the hardware to get it to behave in a rugged environment.

Here are four specific technical hurdles you likely faced (or will face) and the engineering "pivots" used to overcome them.

1. The "Power Spike" Problem (Sensor Interference)
The Hurdle: The MQ-series smoke sensor requires an internal heating element to function. When the heater kicks in, it draws a significant amount of current. We found that this caused "brownouts" on the ESP32 or created electrical noise that made the Ultrasonic sensors give erratic distance readings (jumping from 2 meters to 10 centimeters instantly).

The Fix: * Hardware: We implemented decoupling capacitors (10µF and 0.1µF) close to the sensor power pins to smooth out the voltage spikes.

Isolation: We moved the smoke sensor onto a dedicated 5V power rail separate from the ESP32’s 3.3V logic supply to ensure the "noise" from the heater didn't leak into the microcontroller's processing.

2. The "Blocking Code" Trap (Concurrency)
The Hurdle: Standard Arduino code runs in a single loop. When we added the GPS module, the code would "wait" for a valid satellite string. During those few milliseconds of waiting, the Sound Sensor was "deaf" and the Ultrasonic sensors weren't checking for obstacles. In a flying drone, 200ms of "blindness" means a crash.

The Fix: We pivoted to using FreeRTOS (which is native to the ESP32). We split the project into three high-priority tasks:

Task A (Flight Safety): Reading Ultrasonic data every 20ms.

Task B (Environmental): Sampling Sound and Smoke levels.

Task C (Telemetry): Handling GPS and WiFi/LoRa communication.
This ensured that a slow GPS lock never interrupted the "reflexes" of the drone's obstacle avoidance.

3. Acoustic "Ghosting" (Propeller Noise)
The Hurdle: The Sound Sensor is designed to hear chainsaws and gunshots. However, when the drone is flying, the high-frequency whine of the four brushless motors creates a massive amount of "acoustic trash." The sensor would constantly trigger "false positives" because it couldn't distinguish a chainsaw from its own propellers.

The Fix: Instead of just measuring "loudness" (amplitude), we implemented a basic Frequency Analysis (using an FFT - Fast Fourier Transform library). We identified the specific frequency band of the drone's motors and "notched" it out in the code, allowing the ESP32 to listen specifically for the lower-frequency "thrum" of a chainsaw or the sharp "crack" of a gunshot.

4. GPS Signal "Multipath" (The Canopy Shield)
The Hurdle: In dense forests, the tree canopy acts like a biological shield. The GPS Neo-6M module struggled to get a "3D Fix" because the leaves blocked or reflected the satellite signals. The drone’s coordinates would "drift" by 10–15 meters even when sitting still.

The Fix: We implemented Sensor Fusion. We didn't rely solely on the GPS for positioning. We used the Ultrasonic sensors to maintain a fixed altitude and the Onboard IMU (Inertial Measurement Unit) to track relative movement. If the GPS signal dropped or became unreliable (High HDOP), the system would switch to "Dead Reckoning" mode, using its last known velocity and heading to estimate its position until a clear signal returned.

**Best Hardware Project**

Track Fit: Best Hardware Project
AranyaShield is a high-performance, multi-mission autonomous quadcopter that pushes the limits of the ESP32 architecture to solve critical environmental challenges. Our project fits the "Best Hardware Project" track through its complex integration of sensors, custom power management, and edge-computing capabilities.

1. Sophisticated Sensor Fusion
Unlike standard drones, AranyaShield utilizes a specialized hardware stack designed for high-density forest environments:

Acoustic Intelligence: A high-sensitivity sound sensor coupled with real-time frequency analysis to detect chainsaws/gunshots.

Chemical Early Warning: MQ-series smoke detection sensors integrated into the airflow for early-stage wildfire identification.

Ultrasonic Shielding: A localized array of HC-SR04 sensors providing a 360° "safety bubble" for obstacle avoidance in GPS-denied forest canopies.

2. Custom Engineering & Power Optimization
A major hardware hurdle was managing the high current draw of the smoke sensor's heating element alongside the ESP32’s logic. We engineered a multi-rail power distribution system with decoupling capacitors to prevent electrical noise from interfering with sensor accuracy—a common pitfall in DIY robotics.

3. Edge Intelligence on Low-Power Hardware
We successfully implemented FreeRTOS on the ESP32 to handle concurrent tasking (GPS tracking, sensor sampling, and flight safety) without a single point of failure. By moving the "brain" entirely onto the drone (Edge AI), we eliminated the need for cloud dependency, making this a truly standalone, rugged hardware solution for remote wilderness.

4. Scalability & Impact
The hardware is designed to be cost-effective and modular, allowing for the deployment of drone "swarms." This makes it a viable real-world tool for forest departments with limited budgets, providing a tangible hardware solution to the global crises of deforestation and wildfires.

Team **MicroHarD** -- [Abhijit Mridha](https://github.com/paimon-2005), [Atanu Maity](https://github.com/atanu194m), [Atanu Ray](https://github.com/atanuray1802-ai), [Poulami Neogi](https://github.com/ethereal19)

`2026-04-05`

---

### SMART KRISHI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-krishi-324a) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/sWIkOdr-2k4?si=dw0X5t9iY3pmwXnO) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> From Guesswork to Data-Driven Farming.

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Android](https://img.shields.io/badge/Android-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Embedded Systems](https://img.shields.io/badge/Embedded%20Systems-333333?style=flat-square)

**The problem it solves**

Smart Krishi tackles two core issues: unpredictable farm productivity and lack of trust in food quality.

Farmers rely on guesswork for irrigation and crop decisions, leading to low efficiency and unstable income. Existing solutions only provide data, not action.

Smart Krishi converts farming into a data-driven, automated system using IoT sensors and AI to monitor soil, detect diseases, and control irrigation in real time. It also enables traceability, linking farm data to final produce for consumer trust.

⚙️ What People Can Use It For
Automate irrigation based on real-time soil data
Monitor farm conditions remotely
Detect plant diseases using AI
Improve crop decisions using data insights
Enable traceable, verified food production

It reduces manual effort, increases efficiency, and turns farming into a controlled, predictable process.

**Challenges we ran into**

Power & hardware instability → Fixed using better battery setup and circuit design
LoRa communication issues → Improved packet handling and reliability
Noisy sensor data → Applied calibration and filtering
Limited ML datasets → Used transfer learning and curated datasets
System integration complexity → Built modular pipeline (data → processing → action)

Team **ROGUE BITS** -- [Anamika Vashisth](https://github.com/Null), [Shivam Mishra](https://github.com/SaKA7dev), [Prabhat Singh](https://github.com/prabhat9949), [Abhay Chauhan](https://github.com/AbhaySingh97/)

`2026-04-04`

---

### AgriVistaar
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agrivistaar-dbe7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sainasharma2007/AgriVistaar-) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> "AgriVistaar: Turning Drone Insights "

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

🚜 For Farmers: Smarter Fields & Higher ProfitsTraditionally, farmers walk through their fields manually to check for problems, which is labor-intensive and often misses early warning signs. AgriVistaar changes this:Early Warning System: Farmers can detect "silent" threats like rice blast or nitrogen deficiency through drone-based NDVI scanning before they are visible to the human eye.Precision Spraying: Instead of blanket-spraying an entire field with expensive chemicals, farmers get "Zone Alerts" (e.g., "Spray only Zone C"). This reduces exposure to hazardous pesticides and saves money.Optimal Selling Time: Instead of selling crops out of desperation or habit, farmers use the Profit Calculator to predict yield and track live mandi prices to sell when profits are highest.Offline Accessibility: In areas with poor 2G/3G connectivity, farmers can still view downloaded heatmaps and alerts, ensuring they are never without guidance in the field.🏢 For FPOs: Village-Scale ModernizationFarmer Producer Organizations (FPOs) act as the technology hub, making advanced tools affordable for everyone.Shared Infrastructure: FPOs can manage a single drone asset to service hundreds of smallholder farmers, bringing the cost down to a manageable ₹200–400 per acre.Digital Record Keeping: FPOs can maintain digital health records and yield histories for every field in their network, which is vital for getting better insurance rates or government subsidies.Hardware Agnostic Management: FPOs can use any drone brand they already own; AgriVistaar acts as the "intelligent layer" on top of the existing hardware.🛡️ Safer & More Reliable AgricultureResource Conservation: By providing exact instructions on where to water or fertilize, the platform helps cut water use by 30% and fertilizer waste by 25%, leading to a more sustainable environment.Transparency in Supply Chain: The platform helps combat product fraud in mandis by providing data-backed evidence of crop quality and ownership.Reduced Physical Strain: Instead of manually scouting massive fields, the drone does the heavy lifting, keeping farmers away from potentially hazardous terrain or pest-heavy areas

**Challenges we ran into**

1 face problem in mongodb connection 
2 face problem in initialisation in auth 0
3 face problem in making multi language chat bot with gemini
4 face problem in uploading detail about field

Team **Innovault** -- [Saina Sharma](https://github.com/sainasharma2007), [RISHIKA GARG](https://github.com/gargrishika2005-cell), [Kanav Agarwal](https://github.com/kanav1211), [Kartike Rohila](https://github.com/kartike37)

`2026-03-08`

---

### V_lora
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/vlora-36fd) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Arjun-2005aa/V_LORA.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/kMol-m4E5UY) [![Built at](https://img.shields.io/badge/Built%20at-HackSRM%207.0-0052CC?style=flat-square)](https://hack-srm26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Ensure communication works where everything fails.

![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Lora](https://img.shields.io/badge/Lora-333333?style=flat-square) ![Codec](https://img.shields.io/badge/Codec-333333?style=flat-square)

**The problem it solves**

Modern communication depends on cellular networks and the internet, which often fail during emergencies, in remote locations, or when networks are congested. In these situations, people are left without reliable ways to coordinate, share updates, or call for help. Existing solutions either stop working entirely without connectivity or are limited to short-range, voice-only communication.

This system provides infrastructure-free voice and text communication using LoRa, allowing users to send short voice messages and text even when there is no internet or cellular coverage. It improves safety and coordination by offering reliable, low-power communication that continues to work when conventional networks are unavailable.

**Challenges we ran into**

One of the major challenges was building a complete mobile application within the limited time frame of the project. While the long-term plan was to have all functionality running directly on a phone app, time constraints and parallel project commitments meant we relied on a Python-based client running on a laptop for testing and demonstration. This allowed us to validate the core communication system—WiFi bridging, LoRa transmission, voice compression, and packet handling—without blocking progress on the underlying technology.

Another challenge was achieving reliable voice transmission over LoRa, which has very strict bandwidth limitations. This was addressed by switching to burst-based push-to-talk communication and using an ultra-low-bitrate voice codec, ensuring intelligible audio while maintaining reliability and range. The mobile app implementation is still in progress and nearly complete, and the current setup successfully proves the feasibility and performance of the system at the communication level.

**Grand Prize**

This project fits into the Grand Prize track because it addresses a real-world problem at scale with a technically sound and impactful solution. Communication failures affect disaster response, public safety, rural connectivity, and large-scale events, and this system directly targets those scenarios by enabling voice and text communication without relying on cellular networks or internet infrastructure.

The project goes beyond a simple prototype by demonstrating real-world testing, measurable range, and a complete communication pipeline—from user input to wireless transmission and playback. Its architecture is designed to scale through relay stations, higher-gain antennas, and multi-device coordination, making it a strong foundation for broader deployment. By combining low-power wireless communication, intelligent system design, and practical use cases, this project shows the depth, feasibility, and societal impact expected in a Grand Prize–level submission.

Team **TEDH** -- Hemraj Sodisetti, Arjun Kasimsetty, Eswar Doddakula, Sandana Sureshvaran, Thanuja Gogineni

`2026-02-26`

---

### Backdoor Zero
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/backdoor-zero-a7d4) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1OuuMs-Kum-fmxZ00Z6VeLEcXLWqxMkup) [![Built at](https://img.shields.io/badge/Built%20at-PRINCE%20PROTOTHON-0052CC?style=flat-square)](https://prince-protothon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> Providing a safe and secure internet to the world.

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Pi Camera](https://img.shields.io/badge/Pi%20Camera-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Embedded Systems](https://img.shields.io/badge/Embedded%20Systems-333333?style=flat-square) ![PushBullet](https://img.shields.io/badge/PushBullet-333333?style=flat-square)

**The problem it solves**

We at Backdoor Zero are working to make you and your network more secure. Either it’s chinese router firmware backdoor, a malicious device connected, or an automated attack. We take care of everything. Alongside this, we also provide CCTV surveillance, smoke and fire detection with emergency alerts, and we also provide network-wide ad shielding that eliminates intrusive tracking and bloatware on every device of your network.
Our integrated DNS level filtering automatically purges ads and invasive trackers from your entire network.
All you need to do is plug our attachment into your router, and sit back and relax while we take care of everything.

**Challenges we ran into**

One of the main challenges we encountered during development was capturing and analyzing query information from network requests. The core difficulty lay in the need to intercept every DNS query originating from multiple devices connected to the router, which would have traditionally required implementing a custom DNS server solution. This approach presented significant complexity in terms of deployment, configuration, and maintenance across different network environments.
To overcome this obstacle, we developed an alternative approach that proved more practical and scalable. We created a structured logging system that captures request data into JSON files, with each request represented as a discrete object containing relevant metadata and query parameters. This allowed us to effectively monitor network activity without the overhead of a full DNS interception layer. We then implemented a rule-based checking mechanism that processes these JSON request objects, enabling us to filter, analyze, and respond to queries based on predefined criteria. This solution not only simplified our architecture but also provided greater flexibility in how we could parse and act upon the captured data, ultimately making our system more maintainable and easier to debug.

Team **Pinmode HIGH** -- Harsh Bhushan Pathak, [Adarsh Singh](https://github.com/Adarsh-1784), [Harsh Verma](https://github.com/harshverma27)

`2026-02-21`

---

### INSIGHT – Intelligent Surveillance Technology
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/insight-intelligent-surveillance-and-guidance-technology-8acc) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Harshvardhan-bajpai/Insight) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-2-FF6B6B?style=flat-square)

> AI-assisted CCTV system for real-time awareness.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![Unmanned Aerial Vehicles (Drones)](https://img.shields.io/badge/Unmanned%20Aerial%20Vehicles%20(Drones)-333333?style=flat-square) ![Computer Vision](https://img.shields.io/badge/Computer%20Vision-333333?style=flat-square)

**The problem it solves**

INSIGHT solves the problem of slow and inefficient manual CCTV monitoring in public areas.
It uses AI to automatically detect threats like altercations, trespassing, and suspicious activity in real time.
It can also recognize criminals, watchlisted individuals, employees, and security staff using face recognition.
Instead of relying on humans to constantly watch screens, the system generates instant alerts with confidence scores.
All detected events are logged, making investigation and reporting easier.
This improves public safety by enabling faster response and preventing incidents from escalating.

**Challenges we ran into**

The biggest challenge i ran into was how to optimise the altercation detection.
Previously i was using mediapipe for pose estimation and then i calculate the movement speed of limbs to flag it as a altercation or not but that took heavy computational power.
Then i simplified it by using Action-Reaction logic by drawing simple bounding boxes over the attacker and victim.
I also used motion speed, bounding box size similarity, direction of movement to get more accurate results.

**Emerging Technologies**

This project fits perfectly into Emerging Technologies track because it combines multiple next-gen technologies into one real-world security system.

It uses AI + Computer Vision (YOLO + InsightFace) for real-time threat detection and identity recognition.
It applies automation and intelligent decision-making by generating alerts without human monitoring.
It integrates multi-source surveillance (drone, rover, CCTV) which is a modern approach used in smart cities and defense systems.
It also represents an edge-AI security platform, meaning detection happens live instead of offline analysis.
This is exactly what emerging tech is about: AI-driven autonomous monitoring, smart infrastructure, and future policing systems.

Team **Flag Smashers** -- [harshvardhan bajpai](https://github.com/Harshvardhan-bajpai), [anushka mishra](https://github.com/consoler987-byte)

`2026-02-08`

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

### FirmwareForge
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/firmwareforge-348c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Souptik-De/FirmwareForge) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> AI first hardware IDE

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Electron](https://img.shields.io/badge/Electron-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square)

**The problem it solves**

# Problem Solved by FirmwareForge

**FirmwareForge** is an AI-native Arduino IDE that simplifies embedded development through intelligent automation.

## Core Problems

### 1. **Manual Complexity**
- **Problem**: Traditional Arduino IDEs require manual pin conflict checking
- **Solution**: AI-powered code generation with Gemini 2.0 Flash that automatically handles pin assignments, includes required libraries, and ensures board compatibility

### 2. **Fragmented Workflow**
- **Problem**: Developers switch between code editor, serial monitor, board manager, and external tools
- **Solution**: Unified Electron app integrating Monaco editor, serial monitor, Arduino CLI, and Wokwi simulation

### 3. **Steep Learning Curve**
- **Problem**: Beginners struggle with wiring, hardware requirements, and proper code structure
- **Solution**: Multiple AI assistance modes:
  - **Chat Guide**: Educational guidance without code
  - **Plan-First**: Detailed implementation plans before coding
  - **Step-by-Step**: Incremental building with todo tracking
  - **Fast Build**: Immediate code generation

### 4. **Hardware Compatibility Issues**
- **Problem**: Pin conflicts, voltage mismatches, and timing issues cause failures
- **Solution**: AI automatically checks pin conflicts, flags voltage issues, and ensures proper code structure

## Key Innovation

FirmwareForge makes AI a first-class citizen in embedded development, providing contextual assistance and hardware-aware code generation that understands physical constraints.

## Target Users

- **Beginners**: Educational guidance and automation
- **Hobbyists**: Rapid prototyping with AI assistance  
- **Professionals**: Streamlined workflow with advanced features
- **Educators**: Teaching tool with built-in best practices

**Best Use of Gemini API**

We are using gemini  api as the ai agent in our ai first hardware ide where it generates code , makes circuit visualization ,creates plan , guides in chat etc.

**Best Hardware Project**

We are revolutionizing hardware development by ai first hardware ide where it generates code , makes circuit visualization ,creates plan , guides in chat etc.

Team **Nooblers** -- [Soumyadip Das](https://github.com/morc00), [Souptik De](https://github.com/Souptik-De)

`2026-04-05`

---

### SMART SAFETY HELMET SYSTEM FOR RIDERS
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-safety-helmet-system-for-riders-dd26) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/1pDNSbBRAsg) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/1pDNSbBRAsg) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> protecting Heads with intelligent technology

![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![MQ5 gas sensor](https://img.shields.io/badge/MQ5%20gas%20sensor-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![Sensors](https://img.shields.io/badge/Sensors-333333?style=flat-square)

**The problem it solves**

Our project is highly beneficial for delivery partners, who often face time constraints that may lead them to exceed safe driving speeds. The system continuously monitors the rider’s speed and provides real-time alerts through the helmet if the speed exceeds safe limits.

In addition, the project incorporates safety features such as alcohol detection to identify if the rider is under the influence, as well as rider monitoring for enhanced security. In the event of an accident, the system automatically generates and sends an alert message to predefined contacts or emergency services.

Overall, this solution aims to improve rider safety, promote responsible driving behavior, and significantly reduce the risk of accidents.

**Challenges we ran into**

During the development of our project, we encountered several challenges. At times, hardware connections were not functioning reliably, which required careful troubleshooting and reconfiguration. Additionally, we faced minor issues in the coding phase, including debugging errors and optimizing system performance.

However, through continuous testing, teamwork, and iterative improvements, we were able to overcome these challenges and successfully implement the system.

Team **Four Runners** -- [Souhardya Mitra](https://github.com/mitrasouhardya2005-cpu), [SRIPARNO DAS](https://github.com/sriparnodas9-collab), [Renascence Dey](https://github.com/Rena-code93), [Soham Sarkar](https://github.com/sohamsarkar-dotcom)

`2026-04-05`

---

### LokPi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/lokpi-671e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shikhar-24100/Hackmol-7.0) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> The Offline Smart Assistant for Bharat

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

Generative AI is revolutionizing the world, but it is leaving behind the next billion users. Existing smart assistants (like Siri or Alexa) and cloud-based LLMs fail rural and non-urban India for four critical reasons: they require persistent high-speed internet, expensive hardware, paid data plans, and are heavily biased toward English fluency. LokPi bridges this digital divide. It is a 100% offline, privacy-first, Devanagari-native voice assistant running entirely on a low-cost Raspberry Pi .Here is how LokPi makes existing tasks radically easier, safer, and more accessible:
1. Breaking the Connectivity Barrier
For the ~400 million people with limited or no internet access, relying on the cloud is impossible. LokPi brings the power of an LLM directly to the edge. It processes complex intents, manages memory, and answers questions with zero latency and zero internet dependency.
2. Hands-Free Digital Literacy via ADB
Many first-time tech users struggle with complex touchscreen UIs. LokPi solves this by integrating an offline Android phone controller via ADB. Users can simply speak in Hindi, and LokPi will physically control their smartphone—opening WhatsApp, scrolling, typing, or making calls —turning an intimidating smartphone into a fully accessible, voice-first device.
3. Hyper-Local Language Support
Instead of forcing users to adapt to "bot English," LokPi natively understands Devanagari speech (STT) and synthesizes Hindi text (TTS). We implemented fuzzy matching and custom alias dictionaries to gracefully handle regional dialects, local slang, and mispronunciations that trip up commercial AIs

**Challenges we ran into**

Building a 100% offline, generative AI pipeline on a highly resource-constrained Raspberry Pi meant we couldn't rely on the safety nets of cloud APIs. Every component—from STT to LLM to TTS—had to be optimized for the edge.

**Main Track: The Deepforge Arena**

LokPi fits perfectly into The Deepforge Arena because it is a triumph of highly optimized, resource-constrained Edge AI engineering. Rather than relying on cloud APIs, we forged a 100% offline, decoupled AI pipeline running entirely on a low-power Raspberry Pi. To make this possible, we engineered deep system-level optimizations: parallel model warm-ups, asynchronous intent parsing, RAM pinning (keep_alive=-1), non-blocking background TTS threads, and a multi-tiered local LLM architecture (routing between Llama 3.2 1B and 3B models). We aren't just calling an AI; we forged a robust, low-latency edge AI stack that directly interfaces with hardware via offline ADB commands to bridge India's digital divide.

Team **Echelon** -- [Premal Goyal](https://github.com/Premal005)

`2026-03-29`

---

### Synapse XR
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/synapse-xr-e1f7) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prayag-1771/Synapse_XR) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/IWHz76PAAq4) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Remote AR/VR Guidance System

![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![WebRTC](https://img.shields.io/badge/WebRTC-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Redis](https://img.shields.io/badge/Redis-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Unity 3D](https://img.shields.io/badge/Unity%203D-333333?style=flat-square)

**The problem it solves**

## The Problem It Solves

Synapse XR addresses the gap between **on-site junior engineers and remote senior expert engineers**, especially in scenarios involving **heavy and costly machinery** such as turbines and transformers, where precise guidance is critical but physical presence is not always feasible.

In many cases, experienced experts must travel **long distances** to handle serious faults, leading to delays, increased costs, and operational downtime. Synapse XR enables real-time remote assistance, reducing the need for physical travel.

This is achieved through the integration of **AR/VR, IoT, and AI technologies**, where AI further enhances the system by **smoothing interactions, enabling hand/object detection, and providing real-time measurements (such as length and angles)** to assist expert engineers in precise decision-making.

### Core Problems

- Lack of **real-time expert assistance** in remote or industrial environments  
- Dependence on experts traveling long distances for critical issues  
- Difficulty in explaining **complex hand movements or procedures verbally**  
- High risk of **errors, delays, or safety hazards** due to miscommunication  
- Inefficiency of traditional support methods such as **calls, manuals, or static video**

**Challenges we ran into**

### 1. Noisy Sensor Data (Hardware Instability)

**Problem:**  
Flex sensors and FSR readings were inconsistent due to electrical noise and unstable wiring.

**Solution:**  
- Added capacitors for noise filtering  
- Implemented moving average smoothing in firmware  
- Ensured proper grounding and shorter wire paths  


### 2. Real-Time Data Latency

**Problem:**  
Initial communication methods caused noticeable lag between glove movement and AR rendering.

**Solution:**  
- Switched to WebSockets for continuous streaming instead of HTTP polling  
- Introduced Redis for fast in-memory state + Pub/Sub fan-out  
- Optimized event flow to avoid unnecessary database hits  


### 3. Synchronization Between Systems (ESP32 ↔ Backend ↔ AR)

**Problem:**  
Ensuring all components (glove, backend, dashboard, Unity app) interpret data consistently.

**Solution:**  
- Defined a strict JSON schema for glove data  
- Used shared contracts in  `shared/schemas/` to enforce consistency  
- Standardized event names like ``` `hand:data`, `glove:update` ```across services  


### 4. Real-Time Multi-User Session Management

**Problem:**  
Handling multiple users (worker + expert) in the same session with proper access control.

**Solution:**  
- Built a session-based backend system with roles ```(`worker`, `expert`, `admin`)```  
- Used JWT authentication and Socket.IO room-based routing  
- Cached latest glove state in Redis for quick access  


### 5. Hardware + Software Integration Complexity

**Problem:**  
Bridging physical hardware signals with real-time software systems and AR rendering.

**Solution:**  
- Broke the system into clear layers:  
  `Sensor → Firmware → WebSocket → Backend → Clients`  
- Developed and tested each module independently before integrating  
- Used simple test servers and visualization tools for debugging early

**AR & VR**

## How This Project Fits Into the AR/VR Track

Synapse XR is fundamentally an **AR-based telepresence system** that enhances real-world tasks using immersive visualization and interaction.

It leverages **Augmented Reality (AR)** to overlay expert guidance directly onto a worker’s physical environment, enabling intuitive, real-time assistance. Instead of relying on verbal instructions, the system allows experts to **visually demonstrate actions through hand tracking and AR overlays**, making guidance more precise and effective.

### Key Alignment with AR/VR

- **Augmented Reality Interaction**  
  Real-time overlay of expert hand movements and annotations onto the worker’s view using a Unity-based AR application  

- **Immersive Guidance**  
  Transforms traditional remote support into an interactive AR experience where instructions are *seen*, not just heard  

- **Natural Input in XR**  
  Uses a sensor-based glove to bring **human hand motion directly into AR**, enabling intuitive and realistic interaction  

- **Spatial Understanding**  
  Combines hand tracking and environmental context to provide **context-aware guidance in 3D space**  

- **Bridging Physical and Digital Worlds**  
  Seamlessly connects real-world actions with digital feedback, which is a core principle of AR/VR systems  

Overall, Synapse XR demonstrates how AR can be used beyond visualization—serving as a **practical tool for real-time collaboration, training, and problem-solving in physical environments**.

Team **pipSqueaks** -- [Prayag Sharma](https://github.com/prayag-1771), [PUSHKAR MISHRA](https://github.com/ItsPM25), [R Sudarsan](https://github.com/sudarsan2507-hue), [Ishaan Jindal](https://github.com/SacredNightmare99)

`2026-03-29`

---

### SentinelVault
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sentinelvault-fd6a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Lavanya-Vaidya/SentinelVault.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=nFbNNtMukcI) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Approve with confidence. Sign without exposure

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![ESP32 CAM](https://img.shields.io/badge/ESP32%20CAM-333333?style=flat-square) ![Arduino IDE/ESP-IDF](https://img.shields.io/badge/Arduino%20IDE/ESP--IDF-333333?style=flat-square) ![ATECC508A Secure Element](https://img.shields.io/badge/ATECC508A%20Secure%20Element-333333?style=flat-square) ![2.8” SPI TFT Display (ILI9341)](https://img.shields.io/badge/2.8”%20SPI%20TFT%20Display%20(ILI9341)-333333?style=flat-square) ![Keypad, Li-ion Battery](https://img.shields.io/badge/Keypad,%20Li--ion%20Battery-333333?style=flat-square) ![Node.js, Express.js, Web3.js / Ethers.js](https://img.shields.io/badge/Node.js,%20Express.js,%20Web3.js%20/%20Ethers.js-333333?style=flat-square)

**The problem it solves**

**The Problem It Solves**

A lot of people lose their crypto not because their wallet gets hacked, but because they accidentally approve something they don’t understand.

Most wallets show complicated transaction data that normal users can’t easily read. On top of that, they rely on connected devices like phones or laptops, which can be infected with malware or tricked by phishing websites.

So users often end up blindly signing transactions, not knowing what they’re actually approving.

**What It Helps People Do**

**SentinelVault gives users a safer way to handle their crypto.**

It lets you see and understand what you’re signing
It keeps your private key completely offline and protected
It makes sure you confirm every transaction manually
It helps catch risky actions like giving unlimited permissions
How It Makes Things Better

**Instead of trusting your phone or browser, SentinelVault acts like a checkpoint.**

You scan the transaction
The device explains it clearly
You decide whether to approve it
Only then does it sign

No cables. No direct connection. No blind trust.

**Challenges we ran into**

**1. Camera Module Integration (ESP32-CAM)**

Getting the camera to work reliably was one of the biggest challenges.
Initially, the ESP32-CAM would either fail to upload code or randomly restart due to unstable power.

**How we solved it:**

Used a stable 5V supply instead of relying only on USB
Properly configured GPIO0 for flashing
Tested using basic camera examples before moving to QR decoding

**2. QR Decoding on Limited Hardware**

Decoding QR codes on the ESP32-CAM was difficult because of limited processing power and memory. Real-time image processing is heavy for a microcontroller.

**How we solved it:**

Optimized image size and resolution
Explored lightweight QR libraries
Considered fallback approaches (like simplifying payload or offloading decoding if needed)

**3. Arduino Library Compatibility**

Many libraries (display, camera, crypto) didn’t work smoothly together. Some conflicted with each other or weren’t optimized for ESP32.

**How we solved it:**

Tested each module independently first
Switched to more stable or actively maintained libraries
Gradually integrated components instead of building everything at once

**4. API and Transaction Handling**

Understanding how blockchain transactions are structured (especially Ethereum) was challenging. Parsing raw transaction data and converting it into something readable required careful handling.

**How we solved it:**

Broke down the transaction structure step-by-step
Focused on simple transactions first (like transfers)
Used existing documentation and examples to validate outputs

**5. Development Workflow**

Managing multiple components (camera, display, secure element, power) made debugging harder. A small issue in one part could break the entire system.

**How we solved it:**

Built the system in stages (camera → display → secure element → integration)
Tested each module independently before combining
Used serial debugging extensively

**6. ML Model / Risk Detection Decisions**

Initially considered using a machine learning model for detecting risky transactions, but this added unnecessary complexity and resource constraints for the device.

**How we solved it:**
Used ensemble XG model for **96.44%** accuracy and AUC to **98%** accuracy

**Blockchain & Decentralized Applications**

SentinelVault directly solves a core problem in the blockchain ecosystem: secure transaction signing and user trust.

In blockchain and decentralized applications (DApps), users are responsible for approving every transaction themselves. There is no central authority to protect them. However, most users interact with DApps through wallets that run on internet-connected devices, making them vulnerable to phishing, malware, and malicious smart contracts.

SentinelVault improves this by acting as a secure, independent signing layer between the user and any DApp.

It works with any Ethereum-based, Blockchain-based DApp (DeFi, NFTs, swaps, etc.)
It ensures transactions are verified and approved offline
It keeps private keys completely isolated from the internet
It prevents users from blindly signing malicious smart contract calls

Instead of replacing DApps, SentinelVault enhances their security, making decentralized systems safer and more usable.

Team **Rocket** -- [Sidak Singh](https://github.com/sidak-sethi/), [Lavanya Vaidya](https://github.com/Lavanya-Vaidya), [Ojas Singh](https://github.com/OjasSingh19), [Himalaya Sharma](https://github.com/sharmahimalaya)

`2026-03-29`

---

### IoT BASED SMART SOLAR MONITORING SYSTEM SDG7
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/solar-monitoring-system-58a3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Nandana1102/solar-dashboard.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/9Av2hR0Z9XI?si=TWvjpxq2yTpV-Xm-) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> solar monitoring system

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![JSON](https://img.shields.io/badge/JSON-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

Solar panel systems often lose efficiency due to factors such as dust accumulation, overheating, poor maintenance, and unnoticed electrical issues. Most existing setups do not provide real-time monitoring or meaningful insights, making it difficult for users to identify performance drops or take timely action.

As a result, energy generation becomes inconsistent, and users are unable to understand the actual condition of their solar systems. There is a need for a solution that can continuously monitor key parameters, detect problems early, and present the information in a simple and actionable way.

Smart Solar Monitoring & Analytics System
This system is a real-time solar monitoring solution that measures electrical and environmental parameters while also analyzing performance and providing intelligent insights. It helps users understand how efficiently their solar panel is operating and what actions are needed to improve it.
It can be used in multiple domains such as homes, industries, maintenance, and research, making solar systems more efficient, reliable, and easy to manage.
Applications
Home users: Track energy generation and reduce electricity costs
Industries & solar farms: Detect underperforming panels and reduce losses
Maintenance teams: Identify faults quickly and reduce manual inspection
Students & researchers: Analyze performance and develop smart models
Key Features
Real-time monitoring of voltage, current, power, and light
Calculation of actual vs expected power and energy
Automatic efficiency evaluation
Remote access through web dashboard
Intelligent fault detection system
Problem Detection
Dust accumulation on panels
Overheating conditions
Low efficiency performance
Wiring or load issues

Smart Benefits
Reduces energy loss
Improves solar efficiency
Minimizes maintenance effort
Enhances system safety
Provides actionable recommendations

Innovation
Unlike traditional systems, this solution does not just display data but analyzes and interprets it, converting raw values into meaningful insights and decisions.

Impact
Smarter energy usage
Lower operational costs
Safer solar installations
Better performance monitoring

**Challenges we ran into**

During the development of this project, I faced several technical and practical challenges that required careful problem-solving.

One of the main challenges was establishing reliable communication between the ESP32 and the web dashboard. Since the ESP32 acts as a local server, ensuring stable connectivity over WiFi and handling dynamic IP addresses was initially difficult. This required multiple iterations to ensure the dashboard could consistently fetch real-time data without interruptions.

Another issue was related to data synchronization between the hardware and frontend. Real-time updates caused inconsistencies during rendering, especially in a Next.js environment, where server-side and client-side rendering must match. Resolving hydration errors and managing dynamic data updates properly was an important learning step.

Sensor integration was also a challenge. Each sensor (INA219, BH1750, DS18B20) operates differently, and calibrating them to provide meaningful and stable readings took time. Ensuring that all sensor data was accurate and synchronized before sending it to the dashboard was crucial.

Designing a user interface that is both informative and simple was another hurdle. The goal was to present technical data like voltage, irradiance, and efficiency in a way that is easy to understand at a glance. Achieving a clean layout while including graphs, AI insights, and recommendations required several UI refinements.

Finally, implementing intelligent insights from raw data was challenging. Instead of just displaying sensor values, I had to design logic to interpret the data and generate useful predictions and recommendations, such as detecting efficiency drops or possible dust accumulation.

**IoT & Smart Devices**

This project belongs to the IoT and Smart Devices track because it uses an ESP32 to connect multiple sensors and collect real-time data from a solar panel system. The device measures parameters such as voltage, current, light intensity, temperature, and irradiance, and sends this data over WiFi to a web dashboard.

It is not just a data collection system; it processes the sensor data to evaluate performance, detect issues, and provide useful suggestions. This makes the system smart, as it helps users understand and improve the efficiency of their solar setup.

The project demonstrates a complete IoT workflow by combining sensing, communication, data processing, and visualization into one integrated system.

Team **SANG** -- [STIBIN STEEPHEN](https://github.com/no), [Gautham Pavithran](https://github.com/no), [Nandana Nandakumar](https://github.com/No), [Akshitha Anurag](https://github.com/akshithaanurag-sketch?tab=repositories)

`2026-03-29`

---

### MediMomo
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/medimomo-4ccf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dominic12012006/Hacknova-medimomo-auto-bot/tree/main) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/oHC02G1fEOA) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/-uCF5oZHu3I) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Say it, See it, Reach it

![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![UDP Socket](https://img.shields.io/badge/UDP%20Socket-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![ROS (Robot Operating System)](https://img.shields.io/badge/ROS%20(Robot%20Operating%20System)-333333?style=flat-square) ![Speech API](https://img.shields.io/badge/Speech%20API-333333?style=flat-square)

**The problem it solves**

What if hospitals had a tireless assistant that
knew every patient's schedule, navigated every
ward, and dispensed every dose, without a single
human detour?
Solution: A voice-controlled autonomous robot
that delivers and dispenses medicines on
schedule — precisely, reliably, every time.

Controlling robots in real time often requires manual input or complex interfaces, which can be limiting in dynamic or assistive scenarios. This project enables intuitive human-robot interaction by combining voice commands with visual perception, allowing a robot to autonomously locate and navigate toward targets using simple spoken instructions. It is especially useful for assistive navigation and hands-free control systems.

**Challenges we ran into**

One major challenge was synchronizing asynchronous inputs from speech recognition and vision processing without introducing latency. Handling noisy or inconsistent voice input and ensuring reliable AprilTag detection in varying lighting conditions also required careful tuning. Another challenge was designing a smooth control pipeline to avoid jittery motion and ensure stable navigation when approaching the target.

Team **MEDI MOMO** -- [Anubhav Rawat](https://github.com/AnubhavRawat21), [Adarsh Mittal](https://github.com/adarsh0error), [Swastika Kangabam](https://github.com/swastopia), [Dominic Thomas](https://github.com/Dominic12012006)

`2026-03-17`

---

### Fury Fly
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fury-fly-8221) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yrajha18/ai-powered-rescue-analysis.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1IzVaLXr7tzOPeuOJU_pgQvI-ybAxGing?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> India First 45mm Class Micro Drone

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

During natural disasters such as earthquakes, building collapses, fires, and explosions, rescue teams often face extremely dangerous and inaccessible environments. Many disaster sites contain narrow gaps, unstable debris, toxic environments, or partially collapsed structures where sending human rescuers immediately can risk further casualties.

In the initial hours after a disaster, rapid situational awareness is critical. Rescue teams need to quickly understand the condition of the site—whether there are trapped victims, safe entry points, or further structural risks. However, traditional tools and large drones are often too bulky to navigate confined spaces, making it difficult to inspect the interior of collapsed areas.

Fury Fly addresses this problem by providing a compact micro-drone platform designed to explore tight and hazardous environments. Its lightweight and small form factor allow it to enter spaces that larger drones or rescue equipment cannot access. By remotely operating the drone, rescue teams can safely gather critical information about the disaster site before sending personnel inside.

The drone enables responders to:

Explore collapsed structures or narrow spaces safely

Assess dangerous environments without risking human lives

Quickly gather situational information in disaster zones

Support faster and more informed rescue decisions

**Challenges we ran into**

Developing Fury Fly involved several technical and engineering challenges across hardware integration, flight stability, and power management.

One of the major challenges was achieving stable hovering on a micro-drone platform. Since the drone uses lightweight coreless motors and a compact frame, even small variations in thrust could cause instability. Integrating the MPU6050 IMU sensor and tuning the stabilization algorithms to maintain a balanced flight required multiple iterations of testing and calibration.

Another challenge was power management. The drone runs on a small 1S Li-Po battery, which limits both current supply and flight time. Ensuring that the ESP32 controller, motor drivers, and sensors received stable power without voltage drops required careful wiring and optimization of the power distribution system.

Hardware integration also presented difficulties. Connecting multiple components such as the ESP32 microcontroller, IMU sensor, motor drivers, and wireless communication module in a very compact space required careful layout planning and soldering precision. Any loose connection or electrical noise could directly affect flight stability.

I also faced challenges in motor control and thrust balancing. Small differences between motors can lead to uneven lift, so proper calibration and testing were necessary to ensure that the drone could hover reliably.

Additionally, firmware development and debugging took significant effort. Implementing real-time sensor reading, filtering the IMU data, and converting it into stable motor control signals required extensive testing and tuning.

Despite these challenges, overcoming them helped improve the robustness of Fury Fly and strengthened the system’s capability to operate as a compact, disaster-response micro-drone platform.

**Electrothon 8.0 Winners**

Fury Fly is an intelligent micro-drone designed to assist disaster response teams in navigating hazardous and confined environments where human entry is dangerous or impossible. Built as a compact aerial exploration system, Fury Fly aims to improve situational awareness, rapid assessment, and search operations during disasters such as earthquakes, collapsed buildings, fires, and other emergency situations.

The project combines hardware innovation, embedded intelligence, and real-time communication to create a lightweight drone platform capable of stable flight and indoor navigation. Powered by an ESP32-based flight controller, Fury Fly integrates multiple subsystems including an IMU-based stabilization unit (MPU6050), custom motor driver circuitry, and a high-efficiency Li-Po power system optimized for micro aerial vehicles.

What makes Fury Fly a strong candidate for the Electrothon Winner Track is its focus on solving a real-world problem with a practical, deployable solution. Traditional drones are often too large to enter collapsed structures or narrow spaces, while Fury Fly is designed specifically to operate in tight, debris-filled environments. Its small size and stable hover capability allow it to explore areas inaccessible to rescue teams.

The system also incorporates wireless communication over Wi-Fi, enabling operators to remotely control the drone and monitor its status in real time. This allows rescue personnel to safely gather information from disaster sites before sending human teams into potentially dangerous areas.

Fury Fly demonstrates the key elements required for a winning innovation:

Real-world impact: Assists disaster response and search operations

Interdisciplinary engineering: Combines electronics, embedded systems, and robotics

Practical implementation: A working hardware prototype rather than a conceptual idea

Scalability: The platform can be extended with cameras, thermal sensors, gas detectors, or AI-based victim detection systems

By addressing a critical challenge in disaster management with an innovative and functional prototype, Fury Fly embodies the spirit of the Electrothon Winner Track — building technology that can make a meaningful difference in real-world situations.

**Electrothon 8.0 Honors Track**

Fury Fly represents a strong example of an innovative hardware-centric solution designed specifically for disaster management scenarios. The project focuses on building a compact, intelligent micro-drone capable of assisting rescue teams during emergencies such as earthquakes, collapsed structures, and other disaster-prone environments.

What makes Fury Fly suitable for the Best Hardware Hack category is its deep integration of custom hardware design, embedded systems, and real-time sensing technologies. The system is built around a lightweight drone platform powered by micro coreless motors and controlled by an ESP32-based microcontroller. The drone integrates multiple hardware modules including an MPU6050 inertial measurement unit (IMU) for stabilization, custom motor drivers, a 1S Li-Po power system, and Wi-Fi communication for control and telemetry.

A key innovation of Fury Fly lies in the real-time stabilization and hovering system, which uses IMU sensor data and embedded control algorithms to maintain stable flight in constrained indoor environments. This makes the drone particularly useful for navigating through tight spaces such as collapsed buildings where larger drones cannot operate.

From a hardware engineering perspective, the project required:

Designing a compact and lightweight flight control system

Integrating multiple sensors with embedded firmware

Building custom motor driver circuitry

Optimizing power management for ultra-small Li-Po batteries

Achieving stable hover using sensor fusion and control algorithms

The drone is specifically optimized for rapid deployment in disaster situations, where it can be used for search, exploration, and situational awareness in hazardous areas without risking human lives.

By combining hardware innovation, embedded control systems, and real-world applicability, Fury Fly demonstrates the core principles of a hardware hack — rapid prototyping, creative engineering, and impactful problem solving.

Therefore, Fury Fly strongly aligns with the objectives of the Electrothon Honor Track – Best Hardware Hack, showcasing a functional, hardware-driven prototype capable of addressing real-world disaster management challenges.

Team **The Risers** -- [Sagar Shaw](https://github.com/Gocodein), [YASH RAJ](https://github.com/yrajha18), [Roshan Kumar Yadav](https://github.com/Roshan-tech336)

`2026-03-15`

---

### PhaseFlow(Smart Load Balancing System)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-load-balancing-systemphase-flow-edc1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VanshChauhan146/PhaseFlow.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/aaerH8EvZow?si=HYQJiSbx0bjpgtfk) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Balance the Power, Protect the Grid

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

**The problem it solves**

Preventing Equipment Failure: Unbalanced loads in three-phase systems cause stator overheating and vibration in motors, leading to insulation breakdown and premature failure.
Reducing Energy Waste: Imbalance leads to neutral current flow and increased 
 losses (heat), which spikes electricity bills and reduces overall grid efficiency.
Eliminating Manual Monitoring: Traditionally, technicians check phases with handheld meters. Your system replaces periodic manual checks with 24/7 automated surveillance, catching faults the moment they happen.

**Challenges we ran into**

Data Synchronization (The "Phase Shift" Problem)
The Challenge: To calculate if a system is truly balanced, you need current and voltage readings from all three phases at the exact same microsecond.
High-Frequency Data Noise
The Challenge: Industrial environments are "electrically noisy" due to electromagnetic interference (EMI).
In the real world, a 3-phase system is never 100.0% balanced.

**Electrothon 8.0 Winners**

Our project isn't just software—it relies on physical sensors (like CT sensors or Hall Effect sensors) and microcontrollers (like ESP32 or Arduino) to capture raw electrical data.
 Our project bridges the gap between raw electrical current and digital insights by integrating embedded systems with real-time cloud processing." The software (your website and backend logic) provides the intelligence to interpret that raw data and make it useful for a human.

**Electrothon 8.0 Honors Track**

Our project isn't just software—it relies on physical sensors (like CT sensors or Hall Effect sensors) and microcontrollers (like ESP32 or Arduino) to capture raw electrical data.
Our project bridges the gap between raw electrical current and digital insights by integrating embedded systems with real-time cloud processing."
 The software (your website and backend logic) provides the intelligence to interpret that raw data and make it useful for a human.we have also made a website which monitors real time voltages and currents and also sends alerts while a load inbalances in a particular line

Team **Team Alphaa** -- [Tanishk Agarwal](https://github.com/Iamstrong03), [Trisha Garg](https://github.com/trishagarg), [Vansh Chauhan](https://github.com/VanshChauhan146), [Vaibhav Kewalramani](https://github.com/vaibhav-kramani)

`2026-03-15`

---

### Smart Waste Management System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-waste-management-system-3aa8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Krish2910/smart-waste-dashboard) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/15aa7032bdd84aa790d065317c52f3aa) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart IoT system for real-time waste monitoring

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![NodeMCU](https://img.shields.io/badge/NodeMCU-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Data Visualization](https://img.shields.io/badge/Data%20Visualization-333333?style=flat-square) ![Embedded C](https://img.shields.io/badge/Embedded%20C-333333?style=flat-square) ![ThingSpeak](https://img.shields.io/badge/ThingSpeak-333333?style=flat-square)

**The problem it solves**

In many cities, garbage bins are collected on fixed schedules instead of actual need, which leads to several problems. Sometimes bins overflow before the collection truck arrives, causing bad odor, pollution, and unhygienic conditions. At other times, trucks visit bins that are still empty, which results in wasted fuel, time, and manpower.

Our Smart Waste Management System solves this problem by using IoT sensors to monitor garbage bins in real-time. The ultrasonic sensor detects the fill level of the bin, while other sensors monitor environmental conditions such as temperature and humidity. When the bin reaches a critical level, the system sends data to the ThingSpeak cloud platform, allowing authorities to monitor bin status remotely.

This enables smart waste collection, where garbage trucks are dispatched only when bins are nearly full. As a result, the system helps reduce operational costs, prevent overflowing bins, improve city cleanliness, and make waste management more efficient

**Challenges we ran into**

One of the main challenges we faced was integrating the RFID module with multiple sensors (Ultrasonic sensor, DHT11, LDR, and LCD) on a single ESP8266 NodeMCU. Due to hardware pin limitations and communication conflicts, the RFID module was not functioning properly when all sensors were connected simultaneously.
To solve this issue, we redesigned the architecture by using two ESP8266 microcontrollers. One ESP8266 handles the sensor data collection (garbage level, temperature, humidity, and light), while the second ESP8266 manages the RFID scanning and identification system.
Both devices send their data to the ThingSpeak cloud platform, where the data is integrated and visualized on the backend dashboard.

Team **Ai Alchemist** -- Krish Singhal

`2026-03-08`

---

### Guardian AI- IOT based safety system
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/guardian-ai-iot-based-safety-system-ec14) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> To predict the disaster before the disaster happen

![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Twilio](https://img.shields.io/badge/Twilio-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![gemini](https://img.shields.io/badge/gemini-333333?style=flat-square)

**The problem it solves**

Guardian AI is an Iot based safety system which is used to detect the disaster and predict the risks if there is any like gas leakage,temp increases suddenly,water increasing suddenly and cross the water level .It is easily accessible because it is cost efficient just in 1500-2000₹ . We can install it to houses, hotels,and small shops

**Challenges we ran into**

We are using Google gemini ai as as cloud to generate the alert notification but there are many easier ways to get it so that's the main problem for us

Team **Nexora** -- Dhruv rai, Gagan Deep

`2026-03-08`

---

### Sensor Shield
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/sensor-shield-3c9a) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gautamabhish/Sensor-Shield) [![Built at](https://img.shields.io/badge/Built%20at-HACKSECURE'26-0052CC?style=flat-square)](https://hacksecure-1461.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Your Guardian for Mobile Sensor & App Usage

![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square)

**The problem it solves**

Modern smartphones rely on permission-based security for sensitive sensors such as the microphone, camera, and GPS. Once a user grants these permissions, applications are free to access them whenever they want.

The problem is that users have almost no visibility into how those permissions are actually used in real time.

This creates several risks:

Apps may access microphone or camera in the background without the user realizing.

Location data may be collected excessively, even when the user is not actively using the app.

Permissions granted months ago remain active even if the app is no longer used.

Users have no simple way to understand behavioral misuse of permissions.

In other words, the operating system tells you what an app is allowed to do, but not what it is actually doing.

How Sensor Helps

Sensor acts as a real-time privacy watchdog that continuously monitors how apps use sensitive device sensors and alerts the user when behavior becomes suspicious.

Instead of just checking permissions, the system analyzes actual runtime behavior.

It helps users:

Detect background microphone or camera access

Identify apps that overuse GPS tracking

Understand which apps access sensors most frequently

Receive instant alerts when unusual activity occurs

All analysis happens directly on the device, ensuring that no private data leaves the user’s phone.

Real-World Use Cases
🛡️ Detecting Spyware or Malicious Apps

Some malicious apps secretly activate sensors in the background. Sensor detects abnormal behavior patterns and warns the user immediately.

Example:

A flashlight app activating the microphone in the background.

🔍 Transparency for Privacy-Conscious Users

Users who care about privacy can see exactly:

Which apps use sensors

When they use them

Whether the access occurred in the background

This turns invisible behavior into clear, understandable insights.

⚠️ Identifying Permission Abuse

Apps often request more permissions than they need. Sensor detects Permission Debt — situations where apps keep sensitive permissions despite not being used.

Example:

A weather app that still has Always Location Access even though the user hasn’t opened it in weeks.

📊 Understanding Device Privacy Health

Sensor provides a privacy dashboard that summarizes:

Sensor activity trends

High-risk events

Most invasive apps

This helps users maintain a healthier digital privacy environment.

Why It Matters

Mobile devices contain some of the most sensitive personal data people own.

While operating systems enforce permission controls, they do not provide strong tools for behavioral transparency.

Sensor bridges this gap by giving users real-time insight, automated detection, and actionable controls over how their device sensors are used.

It transforms privacy from a static permission system into a dynamic, behavior-aware protection layer.

**Challenges we ran into**

The android ecosystem api restrictions were problem

Team **RingZero** -- [Abhishek Gautam](https://github.com/gautamabhish/), [Himanshu .](https://github.com/himanshu1009), [Himanshu Mahajan](https://github.com/HimanshuMahajan123), [Navdeep Singh](https://github.com/saininavdeep25)

`2026-03-11`

---

### TempMent
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/jhxzixs-00e8) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/2Tg7gWL-loo?si=yfuom2jZxvJ6r6eE) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Smart Sensing

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

**The problem it solves**

Modern offices, campuses, and shared workspaces waste a significant amount of electricity because lighting, HVAC systems, and infrastructure continue operating even when rooms are unoccupied. Traditional occupancy monitoring solutions rely on cameras or infrared sensors, which introduce privacy concerns, limited coverage, and expensive installation costs.

Our solution transforms existing WiFi environments into intelligent sensing spaces using **WiFi signal disturbance** analysis. Without using cameras or microphones, the system detects human presence and motion inside a room in real time.

This enables automated energy optimization, smarter workspace utilization, and privacy-preserving security monitoring. Facilities managers can identify unused rooms, reduce unnecessary power consumption, and receive alerts when unexpected motion is detected after operational hours.

By leveraging* low-cost edge* devices, the system makes intelligent building monitoring affordable and deployable even in small and medium offices.

**Challenges we ran into**

One of the major challenges we faced was extracting reliable motion information using **WiFi Channel State Information (CSI)** from commodity hardware like the ESP32. WiFi signals naturally contain noise and environmental fluctuations, which initially caused unstable motion detection and inconsistent automation behavior.

We addressed this by refining signal processing logic, calculating variance between CSI amplitudes, and introducing motion hold thresholds to stabilize occupancy detection. Hardware limitations such as sensing range and antenna sensitivity also required experimentation with placement and signal tuning.

Another challenge was integrating hardware sensing with a real-time web dashboard and alert system. Ensuring smooth communication between IoT devices, backend services, and the frontend interface required careful synchronization and testing.

Despite these challenges, we successfully developed a working prototype capable of detecting occupancy and triggering automation and alerts in real time.

Team **Runtime Terror** -- [Shlok Katiyar](https://github.com/shlok612), [Siddhant Satyajeet_Jena](https://github.com/FOX-KNIGHT), [ANKITA MOHAPATRA](https://github.com/ankitamohapatra0406), [Rajshree Balsamant](https://github.com/Rajshree482)

`2026-02-28`

---

### Backdoor Zero
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/backdoor-zero-c384) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/1ma_aCVs8pXxad4O_LF7V3_oqAkSny6qO) [![Built at](https://img.shields.io/badge/Built%20at-Rekkathon-0052CC?style=flat-square)](https://rekkathon.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Providing a safe and secure internet to the world.

![JS](https://img.shields.io/badge/JS-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Networking](https://img.shields.io/badge/Networking-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![CoralAccelerator](https://img.shields.io/badge/CoralAccelerator-333333?style=flat-square)

**The problem it solves**

We at Backdoor Zero are working to make you and your network more secure. Either it’s chinese router firmware backdoor, a malicious device connected, or an automated attack. We take care of everything. Alongside this, we also provide CCTV surveillance, smoke and fire detection with emergency alerts, and we also provide network-wide ad shielding that eliminates intrusive tracking and bloatware on every device of your network.
Our integrated DNS level filtering automatically purges ads and invasive trackers from your entire network.
All you need to do is plug our attachment into your router, and sit back and relax while we take care of everything.

**Challenges we ran into**

One of the main challenges we encountered during development was capturing and analyzing query information from network requests. The core difficulty lay in the need to intercept every DNS query originating from multiple devices connected to the router, which would have traditionally required implementing a custom DNS server solution. This approach presented significant complexity in terms of deployment, configuration, and maintenance across different network environments.
To overcome this obstacle, we developed an alternative approach that proved more practical and scalable. We created a structured logging system that captures request data into JSON files, with each request represented as a discrete object containing relevant metadata and query parameters. This allowed us to effectively monitor network activity without the overhead of a full DNS interception layer. We then implemented a rule-based checking mechanism that processes these JSON request objects, enabling us to filter, analyze, and respond to queries based on predefined criteria. This solution not only simplified our architecture but also provided greater flexibility in how we could parse and act upon the captured data, ultimately making our system more maintainable and easier to debug.

**Embedded Systems**

Our project aligns strongly with the Embedded Systems Track through its implementation on a Raspberry Pi 5, which serves as a dedicated embedded hardware platform for network security monitoring. The Pi 5 acts as an intermediary device between connected devices and the router, functioning as an embedded security appliance that operates at the network level.
The embedded nature of our solution is evident in several key aspects. First, we leveraged the Pi 5's compact form factor and low power consumption to create a standalone, always-on security monitoring system that can be seamlessly integrated into existing network infrastructure. The device runs continuously in the background, requiring minimal user intervention once deployed.
Second, our implementation involves real-time processing and analysis of network traffic directly on the embedded device. The Pi 5 intercepts every DNS query passing through the network and performs rule-based vulnerability checking on-the-fly. This requires efficient resource management and optimized code execution, which are hallmarks of embedded systems development. We had to carefully consider memory constraints, processing overhead, and I/O performance to ensure the system could handle multiple simultaneous queries without introducing latency or bottlenecks.
Furthermore, the project demonstrates practical embedded systems principles such as hardware-software integration, real-time data processing, and the development of a purpose-built appliance that solves a specific problem using constrained computing resources.

Team **PinMode HIGH** -- [Harsh Verma](https://github.com/harshverma27), [Vaishali Bhatt](https://github.com/Vaishali171), [Adarsh Singh](https://github.com/Adarsh-1784), Harsh Bhushan Pathak

`2026-02-11`

---

### nil
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/brainwave-driven-wheelchair-for-paralysis-patients-using-eeg-and-ml-b4fc) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://google.com) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> nil

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![SciPy](https://img.shields.io/badge/SciPy-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

Team **Brain-Route** -- [pratyaksh lodhi](https://github.com/PratyakshLodhi), [Aaron David Don](https://github.com/Aaron-David-Don), [Jessy Don](https://github.com/jessyalikkala-cyber)

`2026-02-08`

---

### FutureCan
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/futurecan-865d) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gulshantomar/FutureCan) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://futurecan-b83a2.web.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/2-3Vgs7eUnE?si=M_z8cUbbQuOT_FK3) [![Built at](https://img.shields.io/badge/Built%20at-Lean%20In%20Hacks%207.0-0052CC?style=flat-square)](https://leanin-hacks-7.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> Recycling the World, Reviving the Earth.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-333333?style=flat-square) ![MQTT](https://img.shields.io/badge/MQTT-333333?style=flat-square) ![Figma](https://img.shields.io/badge/Figma-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Servo Motor](https://img.shields.io/badge/Servo%20Motor-333333?style=flat-square) ![IR Sensor](https://img.shields.io/badge/IR%20Sensor-333333?style=flat-square)

**The problem it solves**

### 1. Poor Waste Segregation at Source
Most people do not segregate waste properly, causing recyclables, organic waste, and hazardous materials to mix and end up in landfills.

**FutureCan solves this by:**  
Using AI-based image recognition to automatically identify and segregate waste at the source.


### 2. Manual & Unsafe Waste Handling
Sanitation workers often face health risks due to direct contact with mixed and hazardous waste.

**FutureCan solves this by:**  
Automating waste sorting, reducing manual handling and improving worker safety.


### 3. Inefficient Waste Collection
Traditional waste collection follows fixed schedules, leading to overflowed bins or unnecessary trips.

**FutureCan solves this by:**  
Using IoT sensors to monitor fill levels and enable optimized, data-driven collection routes.


### 4. Low Public Participation in Recycling
People lack motivation and awareness to practice proper waste disposal.

**FutureCan solves this by:**  
Providing real-time feedback and reward-based incentives that encourage sustainable habits.


### 5. High Environmental Impact
Mixed waste increases landfill use, pollution, and carbon emissions.

**FutureCan solves this by:**  
Improving recycling efficiency, reducing landfill waste, and supporting a circular economy.

**Challenges we ran into**

**1. Inaccurate Waste Classification (AI Model)**
Problem:
The CNN model initially misclassified waste due to poor lighting, mixed waste, and varied shapes—especially with Indian waste types.

How I Solved It:
- Collected and trained on a more diverse, India-specific dataset  
- Fine-tuned the TensorFlow CNN model  
This improved classification accuracy to ~90% in lab conditions.


**2. ESP32-CAM Camera & Memory Crashes**
Problem:
The ESP32-CAM frequently crashed due to limited memory when capturing and sending images.

How I Solved It:
- Optimized image capture timing  
- Offloaded heavy processing to the backend  
This stabilized the system.


**3. Servo Motor Timing Issues**
Problem: 
Servo motors opened the wrong flap or jammed due to improper delay and power fluctuations.

How I Solved It:
- Implemented precise timing logic  
- Used separate power control and calibration for each servo  
- Added fallback positions  
This ensured reliable waste segregation.


**4. User Adoption & Awareness**
Problem:  
Users were unsure whether to trust AI-based segregation.

How I Solved It: 
- Added buzzer and visual feedback  
- Introduced a reward-based system  
This increased user confidence and engagement.

**Open Innovation**

- Uses open and widely used tech (IoT, AI, cloud) that others can easily integrate.
- Shares real-time waste data with municipalities, recyclers, and researchers.
- Encourages collaboration between citizens, government, industry, and academia.
- Modular design allows external teams to improve AI models or add features.
- Supports public sustainability goals like smart cities and Swachh Bharat.

*FutureCan fits open innovation by enabling shared data, collaboration, and extensible AI-IoT systems for smart waste management.*

Team **Alience** -- [Kashish Garg](https://github.com/Kashishgarg248), [Priyanshi Govil](https://github.com/PriyanshiGovil)

`2026-02-08`

---

### nil
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/brainwave-driven-wheelchair-for-paralysis-patients-using-eeg-and-ml-fc59) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> nil

![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![SciPy](https://img.shields.io/badge/SciPy-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![Electric Motor](https://img.shields.io/badge/Electric%20Motor-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

[Aaron David Don](https://github.com/Aaron-David-Don)

`2026-01-31`

---

### Smart ICU Patient Monitoring System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-icu-patient-monitoring-system-85c9) [![Built at](https://img.shields.io/badge/Built%20at-HackJNU4.0-0052CC?style=flat-square)](https://hackjnu4.devfolio.co) ![Likes](https://img.shields.io/badge/Likes-1-FF6B6B?style=flat-square)

> “Smart Vital Signs Monitoring for ICU Patients”

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

Team **Vital Link** -- [Mayank Saraswati](https://github.com/mayanksaraswati), [Bhumi Suri](https://github.com/bhumisuri2819-collab), [Kashish Dhawan](https://github.com/kashishdhawan73-cyber)

`2026-01-31`

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

### Robo Arm Car
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/robo-arm-car-34f2) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anirbansamadder800-code/robotic-arm-car) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/C7XHRoAXIvc?si=HO5DM9o2UxclsteS) [![Built at](https://img.shields.io/badge/Built%20at-Code%20for%20Change%202.0-0052CC?style=flat-square)](https://code-for-change-2026.devfolio.co)

> Control the Future — With Your Voice.

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Servo Motor](https://img.shields.io/badge/Servo%20Motor-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI/ML-333333?style=flat-square) ![Picamera](https://img.shields.io/badge/Picamera-333333?style=flat-square) ![Mediapipe](https://img.shields.io/badge/Mediapipe-333333?style=flat-square)

**The problem it solves**

In real life, a lot of tasks like lifting, moving, or handling objects can be risky and tiring.
For example, dealing with hot or sharp items, doing the same work again and again in factories, or lifting heavy objects.

Because of this, people often face:

Injuries like burns, cuts, or body strain
Tiredness from repetitive work
Reduced efficiency and mistakes over time

How my Project Solves It

My AI robotic system:
Uses voice + gesture control → no need for manual effort
Uses vision (object detection) → identifies and tracks objects automatically
Uses robotic arms → performs precise pick-and-place tasks
Uses mobile base → reaches different locations autonomously

Our AI-powered robotic assistant reduces human effort and risk by automating object handling through voice, vision, and gesture control—bringing safety and efficiency to real-world environments

**Challenges we ran into**

1. Servo Jerking During Load

One of the biggest issues I faced was jerky movement in the robotic arm, especially while lifting objects.
The motion was not smooth and sometimes unstable.

Root Cause:
Voltage drops due to high current demand from high-torque servos
Too frequent PWM updates causing vibration
Solution:
Increased delay between servo updates to reduce signal noise
Implemented smooth stepping logic for gradual movement

2. Voice Recognition Inaccuracy (Noise Issue)

The voice control system sometimes failed or misunderstood commands due to background noise.

Root Cause:

Microphone sensitivity and ambient noise
Low confidence recognition from the speech model

Solution:

Tuned microphone threshold and input levels
Added command filtering logic (accept only predefined keywords)
Used fallback input (keyboard/manual control) for reliability

Camera Detection & Tracking Errors

The object detection module occasionally failed to detect or properly center objects.

Root Cause:

Camera index issues and inconsistent lighting
Bounding box instability

Solution:

Fixed camera initialization and device index
Added centering logic using object coordinates

4. Multi-System Coordination (Voice + Gesture + Movement)

Running multiple systems together caused conflicts and delays.

Root Cause:

Blocking code execution (no parallel processing)

Solution:

Introduced threading to run voice and gesture systems simultaneously
Optimized control flow to avoid command overlap

![image](https://assets.devfolio.co/content/f4b477e2331a460bb2615ef32bc9bab7/e705795b-0503-4ead-8602-4066f9e14e05.jpeg)

Team **MotionX** -- [Anirban Samdder](https://github.com/anirbansamadder800-code), [Rupak Ghosh](https://github.com/iamRupak123), [Sourish Nandi](https://github.com/sourishnandi153-dev), [Sayani Halder](https://github.com/Sayani-halder), [Shovan Goswami](https://github.com/ShovanG394)

`2026-04-11`

---

### Agnivaarak
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/agnivaarak-e7e4) [![Built at](https://img.shields.io/badge/Built%20at-Hacktropica%202k26-0052CC?style=flat-square)](https://hacktropica2k26.devfolio.co)

> Fire bujhao zindagi bachao

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![WebSockets](https://img.shields.io/badge/WebSockets-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-333333?style=flat-square)

**The problem it solves**

Fire emergencies are chaotic, time-critical, and often mismanaged due to lack of clear, real-time guidance. Existing systems like smoke detectors and fire alarms- only alert people, but fail to help them act correctly.

This leads to:

❌ Panic and confusion during evacuation
❌ People choosing unsafe or blocked exits
❌ Delayed response due to lack of situational awareness
❌ High false alarms from vision-only systems (e.g., bright lights, screens, colors)
💡 How FireSuppressor Solves It

FireSuppressor v1.0 transforms traditional fire safety into an intelligent, decision-driven system.

🔥 Accurate Fire Detection (No False Panic)

By combining:

YOLO-based vision
Fire authenticity analysis (flicker, motion, edge chaos)
Sensor fusion (flame, smoke, temperature)

👉 The system confirms real fire instead of reacting to false triggers like yellow objects or screen reflections.

🧠 Real-Time AI Decision Making

Using Gemini AI, the system:

Understands fire spread and risk zones
Identifies safe vs dangerous areas
Continuously updates evacuation strategies

👉 This replaces guesswork with data-driven decisions

🗺️ Smart Evacuation Guidance

Instead of generic alarms, users get:

Step-by-step escape routes
Dynamic rerouting if paths are blocked
Zone-specific safety instructions

👉 People no longer ask “Where do I go?”

🔊 Human-Like Voice Instructions

With ElevenLabs, the system provides:

Calm, clear voice guidance
Multi-language support
Real-time updates

👉 This reduces panic and improves compliance

🎯 Real-World Use Cases
🏢 Malls & Office Buildings → Guide people to nearest safe exits
🏫 Schools & Colleges → Ensure safe evacuation of large groups
🏥 Hospitals → Assist in moving patients safely
🏠 Smart Homes → Early detection and guided response
🏭 Factories → Prevent industrial fire hazards
🚀 Impact

FireSuppressor changes fire safety from:

❌ Passive alerts → ✅ Active guidance

It makes emergency response:

Faster ⚡
Safer 🛡️
Smarter 🧠
🏁 One-Line Summary

**“We don’t just detect fire - we help people survive it.”**

**Challenges we ran into**

### 1. Distinguishing Real Fire vs Fake Fire (Major Challenge)

One of the biggest challenges was ensuring that the system does not trigger false alarms. In early testing, the model often detected **fire-like visuals** such as mobile screen videos, reflections, or bright light sources as real fire.

**Solution:**
I solved this by introducing a **multi-layer validation system**:

* YOLO-based visual detection for fire/smoke
* Temporal analysis (flicker, color variation) to detect real flame behavior
* Sensor-based confirmation (simulated inputs like flame/temperature)

By combining these signals instead of relying on a single model, the system became significantly more reliable and reduced false positives.

---

### 2. Detecting Small Fires (Matchstick / Lighter)

Most pretrained models struggled with detecting **very small fire sources**, which are critical in early-stage fire prevention.

**Solution:**
I addressed this by:

* Lowering detection thresholds carefully
* Using higher-resolution frames for inference
* Fine-tuning detection sensitivity specifically for small flame regions

This improved early detection capability without introducing too many false triggers.

---

### 3. Real-Time Performance vs Accuracy Tradeoff

Running detection, validation, AI reasoning, and voice generation together caused latency issues initially.

**Solution:**
I optimized the pipeline by:

* Using lightweight models (e.g., fast YOLO variants)
* Running components asynchronously where possible
* Using low-latency TTS (ElevenLabs Turbo)

This brought the total response time to **sub-second**, which is critical in emergency scenarios.

---

### 4. Converting Detection into an Automated Workflow

Initially, the system was just detecting fire, not *handling* it intelligently.

**Solution:**
I redesigned the architecture into an **event-driven workflow**:

* Fire detection triggers an event
* Event flows through validation → AI reasoning → action pipeline
* Actions include voice alerts, logging, and dashboard updates

This made the system behave like a **real incident response pipeline** rather than just a detection model.

---

### 5. Making AI Decisions Trustworthy

Another challenge was ensuring that AI-generated instructions are reliable and not vague or generic.

**Solution:**
I structured the input to the AI using **organized signals from multiple agents**, which improved:

* Decision clarity
* Context-awareness
* Consistency of evacuation instructions

---

### Final Outcome

These challenges helped evolve the project from a simple detection system into a **robust, intelligent safety platform** that is:

* More accurate
* Faster
* Context-aware
* Practical for real-world deployment

**Best Use of ElevenLabs**

We use ElevenLabs to transform AI-generated safety decisions into clear, natural, and human-like voice instructions in real time.

Unlike traditional fire alarms that only create noise and panic, our system delivers intelligent, situation-aware guidance - for example:
“Avoid the North Wing. Proceed safely to Exit Gate 2 via Zone B3.”

This creates a fundamentally better emergency experience by:

Enhancing clarity → Users receive precise, actionable instructions instead of vague alerts
Reducing response time → Sub-second voice generation ensures immediate guidance
Building trust → A calm, human-like voice improves compliance and reduces panic in critical situations

👉 In short, we don’t just alert people - we guide them intelligently when it matters most.

**Best Use of Gemini API**

FireSuppressor v1.0 leverages Google Gemini not as a simple chatbot, but as a real-time cognitive safety engine that transforms raw sensor data into actionable intelligence during emergencies.

**1. 🧠 Contextual Fire Reasoning**

Unlike traditional systems that only detect fire, Gemini understands the situation.
It analyzes:

Visual inputs (YOLO fire detection)
Sensor data (heat, smoke, IR)

to determine fire severity, spread risk, and appropriate response strategies - enabling smarter and safer decisions.

**2. 🗺️ Generative Evacuation Intelligence**

Gemini converts algorithmic paths (from BFS navigation) into human-readable, real-time instructions:

“Avoid Zone B2. Proceed to Exit Gate 2 via Corridor C1.”

This bridges the gap between machine computation and human understanding, acting like a virtual emergency coordinator.

**3. 🌑 Sensor-Driven Awareness in Low Visibility**

In smoke-filled or low-light conditions where cameras fail, Gemini interprets sensor anomalies (temperature spikes, gas levels) to maintain situational awareness and continue guiding occupants effectively.

**4. 🧑‍🤝‍🧑 Human-Centric Decision Making**

Gemini identifies risk zones and dynamically prioritizes human safety by generating zone-specific alerts and evacuation strategies, helping manage crowd flow and prevent congestion during emergencies.

**Core Impact**

👉 Gemini transforms the system from a detection tool into an intelligent decision-making system

Instead of just saying “there is a fire”, it answers:

Where is it spreading?
Who is at risk?
Where should people go right now?
🎯 One-Line Power Statement

**“Gemini enables our system to think, reason, and guide- not just detect.”**

Team **SNAP** -- [Srinjoyee Dey](https://github.com/SrinjoyeeDey), [Anway Ghatak](https://github.com/onnoi10), [Nidhi Kumari](https://github.com/Nidhi20505), [Pradip Das](https://github.com/Pradip261)

`2026-04-05`

---

### AI + IoT system for power and energy in delhi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ai-iot-system-for-predicting-and-preventing-power-and-water-failures-093b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dafrie/lstm-load-forecasting) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/IE3FVDHUWTo) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> An AI platform for power and water systems

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![casper.js](https://img.shields.io/badge/casper.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-333333?style=flat-square)

**The problem it solves**

Delhi’s fragile infrastructure under climate stress is addressed by enabling prediction, prevention, and coordination of power and water systems.

In Short
Prevents blackouts during heatwaves
Reduces water loss from leaks & theft
Avoids cascading failures (power → water disruption)
Shifts system from reactive → predictive management

Team **ClassCoders** -- [Tanishq Gupta](https://github.com/starkeyyyy), [Zishan Ansari](https://github.com/0xZ15H4N), [Anurag Kamboj](https://github.com/ANURAG2428), [Aryan Wadhwa](https://github.com/Aryanwadhwa14)

`2026-04-04`

---

### ResQ sense
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/resq-sense-fdd0) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/E0qvtEQtnjU) [![Built at](https://img.shields.io/badge/Built%20at-Hacknovate--7.0-0052CC?style=flat-square)](https://hacknovate07.devfolio.co)

> Swift Detection Sure Rescue

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![NodeMCU IoT](https://img.shields.io/badge/NodeMCU%20IoT-333333?style=flat-square)

**The problem it solves**

Our solution is built to help rescue personnel from Indian rescue forces to adapt their strategy specifically for pancake collapse of buildings. The cause of building collapse may be landslide, earthquake, or explosive. There are no concrete ways to identify human presence as well as alive parameters that can be justified non-invasively. In this scenario, our radar rescue sense will enable rescue operators to identify distance, life probability, and situation analysis (critical or dead), making rescue much more swift and saving more valuable lives.

**Challenges we ran into**

Understanding magic of radio frequency, building radar on unreliable cheap equipment and trying to justify our problem statement. We worked on tuning signals, reducing noise, and improving detection accuracy in unstable conditions. Challenges I ran into include inconsistency in hardware performance, difficulty in calibrating sensors, and interference from surrounding signals. Another challenge was maintaining accuracy while keeping the system low-cost and portable. Despite these issues, we continued refining the system to make it more reliable for real-world rescue scenarios.

Team **Tarangit** -- [ANWESHA PAL](https://github.com/anwesha024), [Amnender Singh](https://github.com/AmnenderSingh), [Mayank Upadhyay](https://github.com/Mayankupadhyay-25), [Jai Verma](https://github.com/aqua20023)

`2026-04-04`

---

### TOBBY HEATH
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/tobby-heath-a706) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://tobby-b6e07.web.app) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/kjWy0KIecTk?feature=share) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> AI BASED HEALTH MONITORING SYSTEM IOT SYSTEM

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square) ![MAX30100 Oximeter](https://img.shields.io/badge/MAX30100%20Oximeter-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Firebase Authentication](https://img.shields.io/badge/Firebase%20Authentication-333333?style=flat-square) ![SSD1306 OLED](https://img.shields.io/badge/SSD1306%20OLED-333333?style=flat-square) ![DS18B20](https://img.shields.io/badge/DS18B20-333333?style=flat-square) ![INMP441](https://img.shields.io/badge/INMP441-333333?style=flat-square)

**The problem it solves**

# 🏥 TOBBY - Medical-Grade IoT Health Monitoring System

> Industry-standard clinical features that differentiate from consumer smartwatches

## 🎯 What Makes TOBBY Different from Smartwatches?

### 5 Industry-Standard Clinical Features:

1. **MEWS (Modified Early Warning Score)** - Hospital-grade early warning system that predicts patient deterioration 6-12 hours early
2. **HRV (Heart Rate Variability)** - Cardiac risk prediction 48 hours before symptoms
3. **Trend Analysis & Anomaly Detection** - FDA requirement for medical devices
4. **Vital Signs Correlation** - Clinical Decision Support AI for disease pattern detection
5. **Personalized Baseline Learning** - Learns YOUR normal, not textbook values

## 🔧 Hardware Components

- **ESP32** - Main microcontroller
- **MAX30105** - Pulse oximeter & heart rate sensor
- **DS18B20** - Medical-grade temperature sensor
- **INMP441** - I2S digital microphone for voice AI
- **SSD1306 OLED** - 128x64 status display
- **ST7735 TFT** - 160x128 color display for detailed metrics
- **Push Buttons** - User interface controls

## 📱 Software Stack

### ESP32 Firmware:
- Arduino C++
- Firebase Realtime Database integration
- Deepgram Speech-to-Text
- Groq AI (Medical-only responses)
- Clinical algorithms (MEWS, HRV, etc.)

### Web Application:
- React.js
- Firebase Authentication & Database
- Tailwind CSS
- Real-time clinical monitoring
- Doctor & Patient dashboards

## 🚀 Quick Start

### ESP32 Setup:
1. Open `esp32/esp2/esp2.ino` in Arduino IDE
2. Install required libraries (see code comments)
3. Update WiFi credentials
4. Update Firebase credentials
5. Upload to ESP32

### Webapp Setup:
```bash
cd webapp
npm install
npm start
```

## 📊 Clinical Features

### MEWS Score (Modified Early Warning Score):
- Respiratory rate scoring
- Heart rate scoring
- Blood pressure scoring
- Temperature scoring
- SpO2 scoring
- Consciousness level (AVPU)
- **Score ≥5 = ICU risk**

### HRV Analysis:
- RMSSD calculation from R-R intervals
- Cardiac autonomic function
- Stress and recovery monitoring
- **HRV <20 = High cardiac risk**

### Baseline Learning:
- Collects 20 measurements
- Calculates personal normal ranges
- Alerts on deviations from YOUR baseline
- Reduces false alarms by 60%

## 🏆 Hackathon Demo Points

**Problem**: Mentors say "What's different from smartwatch?"

**Answer**: 
- Smartwatches track fitness metrics
- TOBBY predicts medical emergencies
- Hospital-grade algorithms
- Professional doctor monitoring platform
- Clinical Decision Support System

## 📁 Project Structure

```
tobby-health-firebase/
├── esp32/
│   ├── esp2/esp2.ino          # Main device firmware
│   └── tobby_firebase.ino     # Alternative firmware
├── webapp/
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── Dashboard.jsx
│   │   │   ├── DoctorDashboard.jsx
│   │   │   ├── ClinicalDashboard.jsx
│   │   │   └── ...
│   │   └── firebase.js        # Firebase config
│   └── package.json
└── Documentation/
    ├── CLINICAL_FEATURES_COMPLETE.md
    ├── HACKATHON_DEMO_SCRIPT.md
    └── ...
```

## 🎓 Technical Highlights

- Real-time Firebase sync
- Medical-only AI restriction
- Multi-display interface (OLED + TFT)
- Voice interaction with speech-to-text
- Clinical alert system with severity levels
- Doctor-patient linking system
- Appointment scheduling
- Prescription management

## 📝 License

MIT License - See LICENSE file for details

## 👥 Team

Built for hackathon - Medical IoT Innovation

---

**Status**: Production-ready with industry-grade clinical features
**Version**: 19.0 (ESP32) | 2.0 (Webapp)
**Last Updated**: March 2026

Team **WinnerX** -- [Diksha Sharma](https://github.com/Dikshaa16), [Ankit Saharan](https://github.com/Ankit545654)

`2026-03-29`

---

### NERVE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/nerve-neural-electrical-response-verification-engine-f0dc) [![Built at](https://img.shields.io/badge/Built%20at-HackMol%207.0-0052CC?style=flat-square)](https://hackmol-7.devfolio.co)

> Neural Electrical Response and Verification Engine

![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

NERVE enables secure access to physical spaces, digital systems, and sensitive infrastructure by verifying identity through live muscle signals rather than static credentials. Unlike passwords or fingerprints, the signal only exists during active muscle contraction, making it impossible to steal, clone, or replay from a database. It can function as a drop-in replacement for passwords, a stronger second factor in MFA systems, or a continuous background verification layer that detects session takeovers in real time. Industries with high security requirements healthcare, banking, defence, industrial operations benefit directly from a method that guarantees physical presence of the authorized individual. At the consumer level, it eliminates the friction of passwords entirely while raising the security floor well above what any current mainstream authentication method provides.

**Challenges we ran into**

Signal Quality and Noise -> Raw EMG signal from the Pico's ADC is extremely susceptible to noise from power lines, electrode contact quality, and cable movement. Getting a clean enough signal required bandpass and notch filtering in software, and even then, small inconsistencies in electrode placement between sessions caused significant variation in the recorded signal.

Electrode Placement Consistency-> The single biggest challenge. EMG signals are highly sensitive to where exactly the electrodes sit on the forearm. Even a centimeter of difference between two sessions changes the amplitude and character of the signal enough to confuse the model. There is no easy mechanical fix for this at the prototype stage.

Low Classification Accuracy ->The model currently sits at 67% cross-validation accuracy, well below the 90%+ needed for a credible authentication system. With only two users and ten reps each, the feature distributions of both users overlap significantly, leaving the SVM without a clean decision boundary to work with.

Limited Training Data-> Ten repetitions per user generates roughly 230 feature windows, which is borderline insufficient for training a robust classifier. More reps and more enrolled users are needed before the model generalises reliably.

Hardware Constraints—> The Raspberry Pi Pico's 12-bit ADC and lack of onboard signal conditioning means the system depends heavily on the external EMG sensor module for amplification and filtering. Any inconsistency in the analog circuit directly degrades the data quality before it even reaches the software pipeline.

**Main Track: The Deepforge Arena**

NERVE qualifies for the main track as it is a full-stack engineering project combining hardware, signal processing, and machine learning, not scoped or simplified for a specific category. It represents an open, unrestricted technical build competing on its own merit.

Team **Technocratic Dynamos** -- [Naman Dhingra](https://github.com/NAMAN9801), [Krrish Sharma](https://github.com/Discovir), [Sayam Sharma](https://github.com/Wizcoderr), [Sehajdeep Singh](https://github.com/code100percent)

`2026-03-29`

---

### FitMon
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/fitmon-ca99) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sanjayram-07/FitMon) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/3omoHr5i5BI?si=sBDbXLrtsUe9CHmR) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/a_pVvdMqAr4) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co)

> IoT and CV powered Injury prevention system

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Express.js](https://img.shields.io/badge/Express.js-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Image Processing - Open CV](https://img.shields.io/badge/Image%20Processing%20--%20Open%20CV-333333?style=flat-square)

**The problem it solves**

FitMon tackles the lack of real-time, form-aware feedback in strength training and real time injury detection. Most users train without immediate guidance, making it easy to develop poor technique, miss range-of-motion targets, or misjudge muscle engagement. FitMon closes that gap by combining computer vision and sensor data to evaluate movement quality and deliver actionable coaching during or right after a workout

**Challenges we ran into**

- Webcam contention: The browser dashboard and Python CV engine can’t share the same webcam. I fixed it by clearly separating “web mode” vs “desktop CV mode” and adding usage guidance so only one runs at a time.

- Realtime data spikes: Early on, socket payload bursts caused jittery UI updates. I smoothed this by batching/normalizing updates before emitting them to the dashboard.

**IoT & Smart Devices**

- Uses edge devices (ESP32 + FSR sensors) to capture physical-world signals.

- Streams sensor data in real time to a backend via sockets for live monitoring.

- Fuses IoT sensor data with computer vision to improve accuracy and context.

- Provides a dashboard for remote visibility, analytics, and session history.

- Demonstrates a full IoT pipeline: device → network → backend → insights/UI.

Team **CNL** -- [Sanjay Ram](https://github.com/sanjayram-07), [Dwaragesh C](https://github.com/dwarageshc7203)

`2026-03-29`

---

### biobox
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/biobox-77de) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sharon169961/bioboxx) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/NgL3lTqRohc?si=qNGRCbnC0-h4ZgUG) [![Built at](https://img.shields.io/badge/Built%20at-DevsHouse%20'26-0052CC?style=flat-square)](https://devshouse26.devfolio.co)

> BioBox - the Digital Twin of the Coral Ecosystem.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![Three.JS](https://img.shields.io/badge/Three.JS-333333?style=flat-square) ![Linux](https://img.shields.io/badge/Linux-333333?style=flat-square)

**The problem it solves**

Coral reef conservation currently suffers from "data lag," where environmental damage is only discovered after irreversible bleaching has begun. Coral Sentinel introduces a novel real-time Digital Twin powered by a mesh network of distributed sensor nodes. This architecture eliminates the dependency on single-point monitoring, providing a high-resolution spatial map of ocean health. By using XGBoost machine learning to analyze live telemetry across this mesh, the system can predict lethal pH drops < 7.8 before they occur. This proactive approach grants marine biologists a critical 48-hour early warning window to implement cooling or buffering strategies at exact coordinates, making reef protection faster, safer, and more geographically precise than traditional manual sampling.

**Challenges we ran into**

The primary hurdle was the hardware-to-software calibration required to sync a distributed mesh network with the ROS 2 Humble middleware. Getting independent nodes to communicate without collision required implementing a custom message protocol to handle multi-dimensional sensor arrays. I overcame this by developing a Rosbridge WebSocket server, which acted as a real-time translator between the low-level telemetry layer and a high-end Three.js web frontend. This involved resolving "address already in use" port conflicts and mapping the physical coordinates of the mesh into a reactive 3D coordinate system. The result is a cloud-ready dashboard that turns raw robotic data into an intuitive interface accessible from any browser without specialized software.

**Environmental Sustainability**

Coral Sentinel directly advances the Environmental Sustainability track by digitizing marine conservation through real-time ecosystem resilience monitoring. By replacing manual, periodic data collection with an automated mesh network of AI-enabled sensors, the project reduces the carbon footprint and human interference typically associated with large-scale oceanographic surveys. Its novelty lies in creating a circular data economy: raw environmental telemetry is processed by a predictive XGBoost model to forecast acidification, which is then visualized in a low-power web-based Digital Twin. This allows for "Precision Conservation," where localized intervention strategies—such as targeted electrolyte buffering or automated cooling—can be deployed at the exact coordinates of stress, minimizing resource waste and maximizing the survival rate of the world’s most critical carbon-sequestering coral habitats.

Team **BioBoxx** -- [Diganta Dutta](https://github.com/diganta121), [Diyaashivaani Arun](https://github.com/moodymelady), [Sharon David](https://github.com/sharon169961?tab=repositories), [Ashrithi S](https://github.com/techy_ash)

`2026-03-29`

---

### EvacNet
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/evacnet-cc5e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tanmoy-12/smart-fire) [![Built at](https://img.shields.io/badge/Built%20at-FrostHacks%20S02-0052CC?style=flat-square)](https://frosthacks-s-2.devfolio.co)

> Decentralized Real-Time Fire Evacuation.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square)

**The problem it solves**

The Problem It Solves

Traditional fire alarm systems operate on a binary model — they only indicate that a fire exists, but not where it is or how to escape safely. This creates a critical gap during emergencies, especially in large buildings where:

Smoke reduces visibility, making static exit signs ineffective
People instinctively rush toward familiar exits, causing dangerous congestion
Occupants may unknowingly move toward the hazard instead of away from it

Our system, EvacNet, solves this by transforming passive alarms into an intelligent evacuation guidance system.

🚀 What it Enables:
Real-time hazard awareness across multiple zones
Dynamic evacuation routing that adapts as fire spreads
Directional guidance using LEDs and audio cues
Decentralized operation, ensuring functionality even if Wi-Fi or infrastructure fails
🧠 How It Makes Things Better:
Converts panic-driven evacuation into guided movement
Reduces evacuation time and prevents bottlenecks
Works in offline scenarios, unlike cloud-dependent systems
Provides a low-cost, scalable solution suitable for schools, hostels, and public buildings

**Challenges we ran into**

1. 🔌 ESP-NOW Communication Issues

Initially, multiple ESP32 nodes were not able to detect each other, even though the code was correct.

Problem:
Each ESP32 was operating on a different Wi-Fi channel, which prevented ESP-NOW communication.

Solution:
Forced all devices to operate on the same channel:

WiFi.softAP("Node_X", "12345678", 1);

This ensured reliable communication across all nodes.

2. 🧠 Distributed Network Synchronization

Each node only knew about its immediate neighbors, resulting in an incomplete dashboard.

Problem:
No global visibility in a decentralized system.

Solution:
Implemented a gossip-based synchronization protocol, where each node shares:

Its own state
Known states of other nodes

This allowed all nodes to gradually build a complete network view.

3. 📊 Blank Dashboard Issue

The web dashboard initially showed no data even when nodes were active.

Problem:
Nodes were not adding their own status to the network table.

Solution:
Explicitly added self-state:

network[NODE_ID].id = NODE_ID;

This ensured at least one visible node and proper UI rendering.

4. ⚡ Power vs Responsiveness Trade-off

The MQ-2 sensor consumes significant power due to its heating element.

Problem:
Turning it off saves power but delays detection.

Solution:
Used controlled duty cycling and optimized sampling intervals to balance:

Power consumption
Detection reliability
5. 🔄 Handling Real-Time Dynamic Changes

Fire conditions change rapidly, requiring constant updates.

Problem:
Ensuring real-time routing without central control.

Solution:
Designed a distributed decision model, where each node:

Updates its state
Recalculates decisions locally

This ensured instant adaptation without dependency on a central system.

**Safety**

Our project solves the problem of evacuation during a building catches a fire. So it is important for people protection & safety

Team **TechSpark** -- [TANMOY CHANDA](https://github.com/tanmoy-12), [Dip Bhattacharyya](https://github.com/Dip393), [Neha Shaw](https://github.com/Neha859), [Agnick Ghosh](https://github.com/AgnickGhosh-0003)

`2026-03-28`

---

### Neuro-Guard
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/edge-ai-powered-seizure-prediction-device-6754) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/youRanupam/NEURO-GUARD) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/dukMZZ30tNw?si=Eb-qLfPdPJ5aXKFH) [![Built at](https://img.shields.io/badge/Built%20at-BINARY%20v2-0052CC?style=flat-square)](https://binaryvtwo.devfolio.co)

> Predict before it strikes

![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

Epileptic seizures often occur without warning, posing serious risks such as injuries, delayed medical response, and reduced quality of life. Existing solutions primarily focus on post-event detection rather than early prediction, limiting their effectiveness in real-world scenarios. To address this gap, we propose an AI-powered multimodal seizure early warning system designed to predict seizure risk before onset.

**Challenges we ran into**

1. Geting actual EEG signal data
2. MCU failure 
3. Sensor failure

**IoT**

This project fits perfectly into the Internet of Things (IoT) ecosystem as a specialized Edge-AI wearable. It follows a classic layered IoT architecture: the Perception Layer uses AD620 and MPU6050 sensors to collect real-time biological and physical data. The Processing Layer employs Edge Computing, where the ESP32-C3 runs local AI inference to ensure low latency and data privacy—critical for medical alerts. Finally, the Network and Application Layers use Bluetooth Low Energy (BLE) to bridge the device to a smartphone, enabling remote monitoring and automated emergency notifications.

Team **Wire-iors** -- [AKASH MAITY](https://github.com/akashmaity2005), [Abhijit Mondal](https://github.com/abhijit-o11), [Anupam Baidya](https://github.com/youRanupam)

`2026-03-22`

---

### BeatRescue
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/beatrescue-73a1) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sangsaist/HackNova-3.0--Beat_Rescue.git) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://youtu.be/Z6m0QdhjGT8) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/Lx1yFIlv4Ho) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> Disaster Rescue

![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Microcontroller](https://img.shields.io/badge/Microcontroller-333333?style=flat-square)

**The problem it solves**

In disasters such as **earthquakes, landslides, mine collapses, or building failures, people can become trapped beneath layers of debris.** One of the most critical challenges for rescue teams is locating survivors quickly. In many cases, victims are injured, unconscious, or unable to call for help, making them extremely difficult to detect.

Rescue operations are also highly time-sensitive. Studies from major disasters show that the first 72 hours after a collapse are known as the **“Golden 72 Hours.”** During this period, the chances of survival are highest. After this window, **the survival rate can drop dramatically in many cases falling below 10% after 72 hours**, depending on injuries, oxygen availability, and environmental conditions.

Real disasters highlight this challenge. For example:

- ***During the 2015 Nepal earthquake, thousands of people were trapped under collapsed buildings, and rescue teams struggled to identify where survivors were located.***

- ***In the 2023 Turkey–Syria earthquake, many victims were found days later only because they managed to tap or create small movements that rescuers detected manually.***

However, the vibrations caused by such small movements are extremely weak and difficult to detect using traditional search methods.

**Current rescue approaches mainly rely on:**
- *Manual search by rescue workers*
- *Sniffer dogs*
- *Thermal cameras*
- *Radar-based systems*

While these methods can help, they often become less reliable in deep or dense debris environments. Materials like concrete, metal, and soil block heat signals, disrupt scent trails, and interfere with sensing technologies. As a result, rescue teams may spend valuable time searching large areas without clear indicators of where survivors might be.

**BeatRescue aims to address this challenge by detecting tiny ground vibrations generated by human movement, such as tapping, slight body shifts, or attempts to signal for help.** By identifying these vibration patterns, the system can help rescue teams narrow down search areas and focus their efforts where signs of life may be present.

In this way, BeatRescue acts as a support tool for disaster response teams, **helping improve survivor detection during the most critical hours after a disaster.**

**Challenges we ran into**

Challenge 1: Working with a highly sensitive sensor
The geophone used in the project is very sensitive and can detect extremely small vibrations. While this is useful for detecting human movement, it also means the sensor easily picks up unwanted environmental vibrations, making the signal difficult to interpret.

Challenge 2: Filtering noisy signals
The raw signals collected from the sensor contained a lot of noise. A major challenge was converting these noisy signals into clearer and more meaningful data. This was addressed by applying signal filtering techniques to reduce unwanted frequencies and focus on useful vibration patterns.

Challenge 3: Collecting real testing data
Another difficulty was collecting realistic vibration data. Human-generated vibrations are very small and inconsistent, so multiple tests and adjustments were needed to gather usable datasets and improve the reliability of the system.

Team **POWER HOUSE** -- Sanjay T, [Sanjeev S T](https://github.com/sanjeev7007), [Sangsai ST](https://github.com/sangsaist), Naveeth RP

`2026-03-17`

---

### ahhhh vazuhthukal vazuhthukal project
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/ahhhh-vazuhthukal-vazuhthukal-project-a506) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Raajmohan4194/PARK-SMART) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/0iEkzNwKrGk) [![Built at](https://img.shields.io/badge/Built%20at-HackNova%203.0-0052CC?style=flat-square)](https://hacknova-3.devfolio.co)

> parksmart!

![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Flutter](https://img.shields.io/badge/Flutter-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square)

**The problem it solves**

Imagine driving into a bustling city, ready to start your day, but the first obstacle you
encounter is finding a parking spot. The frustration of circling around blocks, wasting time and fuel, is a common experience for many urban dwellers. But what if there was a solution to this age-old problem? Enter smart parking apps, the technological saviors that are revolutionizing the way we park. Smart Parking systems can be helpful to drivers who to find parking spots more easily which will save a lot of time. Additionally, sensor-based parking meters can adjust rates based on
demand, further discouraging unnecessary parking.

**Challenges we ran into**

1. Designing a simple and user-friendly interface that clearly shows parking availability without confusion was challenging.
2. Initially, the ultrasonic sensor gave inconsistent readings due to environmental factors like distance variation and obstacles, which made detection unreliable.

Team **ahhhh vazuhthukal vazuhthukal** -- prannav baaradhi, Lokesh Venkatesan, Afraz Ali, Raaj Mohan

`2026-03-17`

---

### Precision Arm
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/precision-arm-d58c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ronakdotasara/roboticarm-ros2.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/CbYFsTaU-Z8) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Advance robotics for intelligent manipulation

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-333333?style=flat-square) ![Arduino Uno](https://img.shields.io/badge/Arduino%20Uno-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

1.Automates repetitive industrial tasks like pick-and-place operations to improve efficiency.
2.Reduces human exposure to hazardous environments such as high temperature or toxic areas.
3.Improves precision in manufacturing where accurate positioning of components is required.
4.Assists warehouse automation for sorting, packaging, and handling objects.
5.Minimizes human error in tasks that require consistent and repeatable movements.
6.Supports robotics education and research using simulation tools like ROS 2, Gazebo, and RViz.
7.Provides a scalable automation solution for industries adopting smart manufacturing.

**Challenges we ran into**

While developing this project, we faced several challenges. First was learning and implementing ROS for robotic control. Another challenge was establishing communication between ROS and Arduino. We also faced difficulty in integrating the camera with object detection using YOLO and OpenCV. Converting camera coordinates to robotic arm movement required calibration and coordinate mapping. Finally, mechanical alignment and the limited degrees of freedom of our robotic arm made precise object picking challenging.

**Electrothon 8.0 Honors Track**

All girls team + hardware 
Volt4Ace

Our project presents a ROS 2–based intelligent robotic arm developed by an all-girls engineering team, designed to demonstrate precise object manipulation through advanced robotics software and simulation tools.
The robotic arm integrates ROS 2 for communication and control, RViz for 3D visualization, Gazebo for physics-based simulation, and MoveIt for motion planning and inverse kinematics. Using these technologies, we created a system that allows the robotic arm to calculate optimal joint movements and execute accurate pick-and-place tasks.
The workflow begins with URDF modeling of the robotic arm, which defines the robot’s structure and joints. This model is then simulated in Gazebo to test real-world physics and interactions. Motion planning is handled through MoveIt, enabling efficient path planning while avoiding collisions. RViz provides real-time visualization of the robot’s configuration, trajectory, and environment.
Our project demonstrates how software simulation and hardware robotics can work together to develop intelligent automation systems. Built entirely by an all-girls team, this project highlights technical capability, teamwork, and innovation in the field of robotics.
This solution can be applied in industrial automation, smart manufacturing, and assistive robotics, where precise and programmable robotic manipulation is essential.

Team **volt4ace** -- [Priti Yadav](https://github.com/Pritiyadav904), [Ritika Loctus](https://github.com/Ritika-07-Loctus), [Shailja Choudhary](https://github.com/Shialja1533), [riya choudhary](https://github.com/riyachoudhary06)

`2026-03-15`

---

### Echopod
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/echopod-13b3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/suhani-code-java/ECHOPOD.git) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/shorts/eL46yvnxl5M?si=7I7iZEhlNu1nsZQ1) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Seeing the path through intelligent sensing.

![Firebase](https://img.shields.io/badge/Firebase-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![Android Studio](https://img.shields.io/badge/Android%20Studio-333333?style=flat-square) ![Kotlin](https://img.shields.io/badge/Kotlin-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Text-to-Speech](https://img.shields.io/badge/Text--to--Speech-333333?style=flat-square)

**The problem it solves**

Navigating indoor spaces like malls, offices, or hospitals can be difficult and unsafe for visually impaired individuals, as there are limited tools that help them detect obstacles or understand their surroundings indoors.

Our device acts as a smart navigation companion that uses sensors and AI-powered vision to detect obstacles and recognize objects. It provides real-time vibration and audio feedback to guide users safely, while the SOS feature with GPS allows them to quickly share their location in emergencies. This helps visually impaired users move more safely and independently.

**Challenges we ran into**

While building this project, we faced several challenges on both the hardware and software sides. Integrating multiple hardware components like the ESP32, ESP32-CAM, ultrasonic sensors, GPS module, amplifier, and vibration motors on a breadboard initially caused issues such as unstable connections and interference between sensors. We resolved this by reorganizing the wiring, carefully managing power distribution, and testing each component individually before integrating them into the full system.

On the software side, we encountered a Java NullPointerException while developing parts of the application logic, which required careful debugging and validation of object initialization. Training the machine learning model for object detection was another challenge, as achieving reliable detection with limited resources required experimenting with different datasets and optimization techniques.

We also faced difficulties with Firebase data uploads and IoT integration, where data from the device was not consistently syncing with the cloud. By revisiting the Firebase configuration, API setup, and connection logic, we were able to establish stable communication between the device and the database.

These challenges helped us improve the system step by step and ultimately build a more reliable and robust assistive navigation device.

**Electrothon 8.0 Honors Track**

**Hardware track**

**ElevenLabs**

The generated voice makes navigation instructions more understandable and user-friendly for visually impaired users.

Team **CtrlAltWin** -- [SOMYA PANCHOLI](https://github.com/Somya-Pancholi), [Daksh Saini](https://github.com/dakshsaini1103), [Suhani Choudhary](https://github.com/suhani-code-java), [chitvansh agrawal](https://github.com/chitvansh24ee168-alt)

`2026-03-15`

---

### Divya Drishti:Fog accident prevention system
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/divya-drishtifog-accident-prevention-system-523c) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/IBelieveInTheDream/Electrothon-Project) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=zU4faQG1jWs) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Your Divine sight in Zero visibility

![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![MATLAB](https://img.shields.io/badge/MATLAB-333333?style=flat-square) ![Electric Motor](https://img.shields.io/badge/Electric%20Motor-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat-square)

**The problem it solves**

So have you ever driven through intense fog where you can't even see 5m ahead of you? This results in many devastating accidents like the ones shown in the video.
So we thought why not research on this topic and see if we as students could find a solution to this particular problem.
And so came to be DIVYA-DRISHTI:
Where humans are unable to respond and break, DivyaDrishti is an automatic breaking system that save the lives of people in such extreme weather conditions.

Unlike standard LIDAR systems which cost more than 70000Rs and **fail in extreme weather conditions** such as fog, our solution offers a **much cheaper** 15000Rs alternative to it **that actually works**.
This project has the **potential to save thousands of lives** and **prevent the extreme traffic jams** that happen due to these accidents

**Challenges we ran into**

One of the major challenges we had during this project was the mmWave Sensor.
Although much cheaper than the Lidar sensors available in the market(costing upto 1lakhRs), it was still out of our options to buy a 15000Rs sensor. 
So we started looking for online simulations.
We had to learn MATLAB completely from scratch in order to simulate this project.
Night long we were just trying to figure this thing out and research about this project.
and inally** WE DID IT.**

**Electrothon 8.0 Winners**

#FIRST-YEAR team aiming for the win.
This is one of the few hardware projects in this hackathon that actually has the potential to save millions of lives, while catering to the niche of low income families.

**Electrothon 8.0 Honors Track**

#Best-Beginner Hack
#Best-Hardware Hack
Well as a team in the first year building this project which could save the lives of thousands of people was a great opportunity for us.
we faced countless challenges in building this automatic breaking system but alas we are finally here, ready to take home the prize

Team **XEREXINITES** -- [Rekhansh Sharma](https://github.com/IBelieveInTheDream), [Ashmit Bhatt](https://github.com/bhattashmit09), Rahul Sonkhla, [Rishabh Uniyal](github.com/rishabhuniyal)

`2026-03-15`

---

### Real Time  EV Energy and Sensor(Simulation)
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/real-time-ev-energy-and-sensor-dashboard-simulation-db34) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rahulkhatkar079/ev-dashboard) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Web interface displaying real time EV sensors data

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square)

**The problem it solves**

​1. Real-Time EV Energy & Sensor Dashboard (Simulation)
​Since electrathons often focus on electronics and electric vehicles, you can build a live monitoring dashboard. Instead of physical sensors, you write a background script on your laptop that generates mock data and pushes it to a database.
​The Concept: A web or mobile interface that displays live metrics like battery temperature, voltage, motor RPM, and estimated range.
​The "Real-Time" Element: As the background script generates new numbers every second, the dashboard updates instantly without needing a page refresh.
​Tech Stack: * Data Generator: A simple Python or C script to generate random but realistic sensor values.
​Database: Firebase Realtime Database (free and very easy to set up).
​Frontend: HTML/CSS/JavaScript, or a basic app framework if you are exploring app development.

**Challenges we ran into**

Service key wasn't generating and firebase admin module not found.

**Requestly Track**

![image](https://assets.devfolio.co/content/c403e8c6c29045fdabea71f33949f773/0ca79b72-ca5c-4a23-8d49-5038895792b7.png)

Team **Hamirpur Royals** -- [Aashish Bishnoi](https://github.com/ace0290), [Rahul Khatkar](https://github.com/Rahulkhatkar079), [Satwik Rana](https://github.com/satwikrana080-beep), [Pranshu Saini](https://github.com/pranshusaini22)

`2026-03-15`

---

### styleMind - AI Wardrobe Intelligence
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/stylemind-2e95) [![Built at](https://img.shields.io/badge/Built%20at-Electrothon%208.0-0052CC?style=flat-square)](https://electrothon-8.devfolio.co)

> Open your wardrobe. Get your outfit. Instantly

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Arduino](https://img.shields.io/badge/Arduino-333333?style=flat-square) ![ESP8266 Wifi MCU](https://img.shields.io/badge/ESP8266%20Wifi%20MCU-333333?style=flat-square)

**The problem it solves**

**Problem Statement:** 

Every morning, the average person spends 
17 minutes standing in front of their wardrobe 
not knowing what to wear.

Not because they have nothing.
Because they have too much — and no intelligence 
to guide them.

Current problems:

1. No weather context
   You pick an outfit without knowing it will 
   be 38°C outside or raining by afternoon.
   Result → discomfort, wasted outfit changes.

2. You forget what you own
   Studies show 30% of wardrobe items are never 
   worn. People rebuy clothes they already have.
   Result → wasted money, cluttered wardrobe.

3. Manual effort every single morning
   You have to open your phone, check weather, 
   scroll through mental inventory, decide.
   Result → decision fatigue before the day starts.

4. No personalization
   Generic fashion apps suggest outfits for 
   average body types, average weather, average 
   preferences.
   Result → suggestions that don't actually fit 
   your body, skin tone, or style.

5. Fragmented shopping
   When you need something new, you check Amazon, 
   then Flipkart, then Meesho separately.
   Result → wasted time, missed deals.

**Solution :**

StyleMind — AI Wardrobe Intelligence

We put a ₹200 ESP8266 sensor on your wardrobe door.

When you open it every morning:

→ Sensor detects door motion instantly
→ App reads today's live weather
→ AI checks your actual wardrobe items
→ Suggests the perfect outfit in under 3 seconds
→ Shows what you own vs what you need to buy
→ Finds best price across Amazon, Flipkart, Meesho

Before you have even looked at your clothes —
StyleMind has already decided what you should wear.

No phone to open.
No app to scroll.
Just open your wardrobe.

![image](https://assets.devfolio.co/content/78f04226d73d4bc3b3b97509012a76ca/b9f10b69-f32d-4c71-8c8d-e310411f6339.png)

![image]
(https://assets.devfolio.co/content/78f04226d73d4bc3b3b97509012a76ca/d17abcc7-315a-4d7a-9d8f-7dd6a7ad70a5.png)

![image](https://assets.devfolio.co/content/78f04226d73d4bc3b3b97509012a76ca/e390cdf8-514f-4f10-9c3c-b37a06300132.png)

![image](https://assets.devfolio.co/content/78f04226d73d4bc3b3b97509012a76ca/685fd1dd-9a9f-4a6e-8779-1f817118acef.png)

![image](https://assets.devfolio.co/content/78f04226d73d4bc3b3b97509012a76ca/905666f4-ee9d-4e16-941e-ca2aac6caa83.png)

**Challenges we ran into**

Challenge :
Getting a physical ESP8266 sensor to 
communicate with a browser in real time 
was our biggest technical challenge.
HTTP is request-response — the browser 
cannot just "listen" for hardware signals.

**Solution : **
We implemented Server-Sent Events (SSE).
The browser opens a persistent connection 
to our Node.js server and stays listening.
When ESP8266 sends a signal, the server 
instantly pushes it to the browser.
Total latency — under 300 milliseconds.

**Challenge: **
We planned to use Claude Vision API 
to automatically identify clothing 
from uploaded photos.
However API keys require a credit card 
and we are first-year students without 
access to paid APIs during the hackathon.

**Solution:**
We built a smart filename-based 
categorization engine that reads 
keywords from the photo filename 
and maps them to category, color, 
fabric, season and occasion.

The result looks identical to an 
AI-powered categorizer but works 
100% offline with zero API cost.
The architecture is ready for Claude 
Vision integration when API access 
is available

**Electrothon 8.0 Honors Track**

We are first-year engineering students 
at NIT Hamirpur participating in our 
second hackathon.

We have basic experience with ESP8266 
from our previous hackathon — but 
StyleMind pushed us far beyond what 
we had done before.

In this hackathon we did for the first time →
Connected hardware to a live web application
Built Server-Sent Events for real-time 
hardware-to-browser communication
Designed a complete AI-powered frontend
Integrated weather API with outfit logic
Built price comparison across 3 platforms
Created a professional full-stack product
from a single HTML file + Node.js server

Our previous hackathon gave us the 
hardware foundation. Electrothon 8.0 
gave us the challenge to build something 
real, complete and impactful with it.

StyleMind is our first complete product —
from idea to working demo to pitch 
in 48 hours.

Team **BEYOND_404** -- [Nishant Thakur](https://github.com/nishantthakur2049-bot), [Ojasvi Bhardwaj](https://github.com/Ojasvibhardwaj2006), [Parnika Choudhary](https://github.com/parnikachoudhary), [Kanav Kalia](https://github.com/kanavkalia1-afk)

`2026-03-15`

---

### SMART WASTE MANAGEMENT SYSTEM
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/smart-waste-management-system-246b) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Krish2910/smart-waste-dashboard) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.loom.com/share/15aa7032bdd84aa790d065317c52f3aa) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> An IOT smart system for real time waste monitoring

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![NodeMCU](https://img.shields.io/badge/NodeMCU-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Ultrasonic](https://img.shields.io/badge/Ultrasonic-333333?style=flat-square) ![ThingSpeak](https://img.shields.io/badge/ThingSpeak-333333?style=flat-square) ![ESP8266 Wifi MCU](https://img.shields.io/badge/ESP8266%20Wifi%20MCU-333333?style=flat-square)

**The problem it solves**

This is a smart waste management system ,India uses a very manual method of going to each house for garbage collection which wastes a lot of fuel and energy.This smart waste monitoring system reads the distance of the filled garbage from lid of te bin,percentage of filled garbage,amount of humidity,and the temperature.It alerts based on a certain level of all these  values.So if the temperature is greater than 50 degress ,it sends a fire alert!,If  humidity is greater than 70% then alerts the municipality.The RFID records whether the bin has been collected or not. This enables smart waste collection,where garbage trucks are dispatched only when they are full,thus helps in reducing overall operational cost.Also alerts when humidity is very high which is the cause of many water borne diseases.

**Challenges we ran into**

The challenge we faced was interfacing 5 sensors into one nodemcu.So although the DHT11,LCD and the ultrasonic sensor was  functioning well,but when we tried to add the RFID module for recording the status of bin collected,it showed a fatal error on the arduino  ide when we tried uploading it. That's why we added another esp8266 nodemcu in order to use the RFID for scanning  and RTC module for real time stamps.

[IMAN CHAKRABORTY](https://github.com/amritashreecando-code)

`2026-03-08`

---

### Life- Link Network
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/life-link-network-9422) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/veervashishth1708/lifeline) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Communication That Refuses to Die

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![MongoDB](https://img.shields.io/badge/MongoDB-333333?style=flat-square) ![LoRa Alliance](https://img.shields.io/badge/LoRa%20Alliance-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

Team **Dynamo** -- [mohammad zaid ansari](https://github.com/muhammadzaidansari313), [karamdeep singh](https://github.com/kddhammu07-netizen), [Aryan Singh](https://github.com/aryan-singh69), [veer vashishth](https://github.com/veervashishth1708)

`2026-03-08`

---

### IDIS - Integrated Disaster Intelligence System
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/idis-integrated-disaster-intelligence-system-68f8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/krishmunjal01/Hack-N-Win) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Detect Early. Respond Faster. Protect Everyone.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Java](https://img.shields.io/badge/Java-333333?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-333333?style=flat-square) ![Spring](https://img.shields.io/badge/Spring-333333?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![RestAPIs](https://img.shields.io/badge/RestAPIs-333333?style=flat-square)

**The problem it solves**

Urban buildings face multiple hidden risks **such as structural stress, gas leakage, fire hazards, and abnormal vibrations,** which are often detected only after significant damage has already occurred. Traditional safety systems like fire alarms usually detect only a single type of hazard, and they rely heavily on manual monitoring or late-stage detection.

Our system **solves this by providing a multi-hazard intelligent monitoring platform** that continuously analyzes environmental and structural conditions in a building.

The platform integrates **IoT sensors** and a **centralized monitoring dashboard** to detect early warning signals such as:
1. Abnormal structural vibrations
2. Smoke and fire hazards
3. Gas leakage
4. Temperature anomalies

These signals are processed in real time and trigger instant alerts and emergency communication through the platform.

**How it helps in real life:** 
This system can be used in:
1. Residential apartment buildings
2. Hospitals and healthcare facilities
3. Schools and universities
4. Shopping malls and commercial complexes
5. Office buildings and industrial spaces

**Instead of waiting for disasters to happen, our solution enables proactive safety monitoring.**

**Benefits**:
1. Early detection of potential structural or environmental hazards
2. Faster emergency response through automated alert
3. Centralized monitoring dashboard for authorities
4. Reduced risk of building damage and loss of life
5. Improved safety management in densely populated structures

By combining **sensor networks, real-time monitoring, and automated alerting,** the platform helps make buildings **smarter, safer, and more responsive to emergencies.**

**Challenges we ran into**

During the development of this project, we faced several technical and design challenges.

**1. Backend–Frontend Integration**
One of the initial challenges was integrating the **Spring Boot backend with the React frontend** for authentication and alert management. There were issues with API endpoints, CORS configuration, and request handling.
We resolved this by properly configuring **REST API endpoints and enabling CORS** policies, ensuring smooth communication between the frontend dashboard and backend services.

**2. OTP Authentication Flow**
Implementing **OTP-based authentication** required handling secure token generation and validation. Ensuring that OTPs were generated, sent, stored temporarily, and validated correctly was initially challenging.
We solved this by implementing a **secure OTP verification system with proper backend validation and expiration logic.**

**3. Designing Sensor Data Handling**
Since our project **involves multiple sensors detecting different hazards, we had to design a logic that prevents false alarms.** For example:
1. Cooking smoke or cigarette smoke could trigger fire alerts.
2. Temporary vibrations could occur during construction or movement.
To solve this, we implemented a **multi-sensor confirmation approach**, where alerts are triggered only when multiple related parameters cross predefined thresholds.

**4. Designing Scalable Architecture**
Another challenge was designing the system so it could **scale to large buildings.** Instead of connecting every sensor directly to the internet, we introduced a **gateway architecture**, where sensor nodes send data to a local gateway that forwards it to the cloud server.
This approach reduces network load and improves reliability.

**5. Emergency Alert System**
Implementing a reliable **alert broadcasting mechanism** required handling multiple communication channels like dashboard alerts, SMS alerts, and email notifications.
We implemented an **alert controller system** in the backend that processes alerts and distributes them across different communication channels.

**Despite these challenges, overcoming them helped us design a robust and scalable safety monitoring platform.**

Team **ResQNet** -- AKSHAT DUBEY, Bhavya ., Krishang Kaushik, Krish .

`2026-03-08`

---

### 🌱 KRISHISHAKTI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/krishishakti-1db3) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vishalpaliwal79/KrishiShakti_local) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/_K0x_rOIRZA?si=Qlwc_04JSIUtu3aX) [![Built at](https://img.shields.io/badge/Built%20at-Hack--N--Win%203.0-0052CC?style=flat-square)](https://hacknwin-3.devfolio.co)

> Smart Desert Farming & Atmospheric Water Harvest

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![C++](https://img.shields.io/badge/C++-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square)

**The problem it solves**

Many regions across the world such as Rajasthan, the Middle East, and parts of Africa suffer from arid climates and water scarcity, making agriculture extremely difficult. Farmers in these areas struggle with low rainfall, poor soil fertility, and inefficient water usage, which severely limits crop production.

In deserts and semi-arid regions, even when farming is possible, farmers often rely on unpredictable rainfall or expensive groundwater extraction. Over-irrigation can quickly deplete limited water resources, while under-irrigation can lead to crop failure.

Additionally, most small farmers lack real-time environmental monitoring and data-driven irrigation systems, meaning they must rely on guesswork to determine when to water crops.

KrishiShakti addresses these challenges by combining IoT sensors, AI analytics, and atmospheric water harvesting technology to create a smart farming ecosystem designed specifically for water-scarce environments.

A key innovation in the system is the use of silica gel desiccant technology, which can capture moisture from the air and convert it into usable water through heating and condensation. This allows small amounts of water to be generated even in low-humidity environments, supporting irrigation and sensor monitoring systems.

Together, these technologies enable farmers to optimize water usage, monitor crop conditions in real time, and produce water from atmospheric humidity, improving agricultural resilience in harsh environments.

**Challenges we ran into**

During development, several challenges were faced.

1 Hardware Integration

2 Synchronizing multiple sensors with the microcontroller required careful calibration.

3 Water Harvesting Efficiency

4 Atmospheric water harvesting depends heavily on humidity levels, making it challenging in extremely dry environments.

5 Sensor Accuracy

6 Environmental sensors can produce noisy data, requiring filtering and calibration to obtain reliable measurements.

7 System Scalability

8 Ensuring the system can scale from a small prototype to a larger farming deployment requires further optimization and infrastructure development

Team **ERROR DETECTORS** -- [ADITYA JHA](https://github.com/coding-laadla)

`2026-03-08`

---

### iSARTHI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/isarthi-62b8) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abhishekmmb18-lang/i-SARTHI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://i-sarthi.vercel.app/) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> AI + IoT Smart Road & Driver Safety System

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![Flask](https://img.shields.io/badge/Flask-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Database](https://img.shields.io/badge/Database-333333?style=flat-square)

**The problem it solves**

Many vehicles on the road today—especially government fleet vehicles, school and college transport buses, logistics trucks, and older or budget vehicles—lack modern AI-based safety and monitoring features. These vehicles often operate without systems capable of detecting road hazards, monitoring traffic conditions, or providing intelligent driver assistance.

Because of this limitation, drivers receive little or no warning about dangers such as potholes, damaged roads, congestion, unexpected obstacles, or narrow roads, increasing the risk of accidents, vehicle damage, and delays.

At the same time, road infrastructure monitoring is still largely manual and reactive. Authorities typically learn about issues like potholes, damaged roads, or heavy congestion only after complaints, delays, or accidents occur. This results in slower response times and inefficient road maintenance.

Emergency vehicles such as ambulances also face difficulty navigating through traffic because traffic infrastructure is not connected or intelligent enough to prioritize them, which can delay critical medical response.

How **iSARTHI** Solves This

**iSARTHI** (*Intelligent Smart AI Road & Traffic Hazard Intelligence*) is a customizable AI-powered retrofit kit designed to bring advanced road intelligence and safety features to vehicles that currently lack them.

Instead of requiring the purchase of expensive new vehicles with built-in smart systems, iSARTHI can be installed as a modular kit in existing vehicles, transforming them into smart, connected mobility units.

The system integrates sensors, AI processing, and connectivity to continuously monitor road conditions, detect hazards, and share real-time information with drivers, fleets, and authorities.

What the iSARTHI Kit Provides

Depending on the user’s requirements, the iSARTHI kit can include:


- Road hazard detection (potholes, damaged roads, waterlogging)

- Traffic congestion monitoring and alerts

- Driver safety monitoring (drowsiness and distraction detection)

- Obstacle and narrow road detection

- Emergency and SOS alert system

- Ambulance priority routing and potential smart traffic signal coordination

- Crowdsourced road intelligence, where multiple vehicles verify and report road issues

- Customizable for Different Use Cases

iSARTHI is designed as a modular and customizable platform, allowing organizations to choose features based on their needs. It can be deployed in:


- Government fleet vehicles for large-scale road condition monitoring and infrastructure reporting

- School and college buses to enhance student transport safety

- Logistics and delivery fleets for safer driving and optimized route management

- Older or budget vehicles that lack built-in AI driver assistance systems

**Impact**

By converting everyday vehicles into mobile road intelligence units, iSARTHI enables continuous, crowdsourced monitoring of road conditions while improving driver safety and traffic efficiency.

This approach makes the solution:

- Scalable – deployable across thousands of vehicles

- Cost-effective – upgrades existing vehicles instead of replacing them

- Collaborative – builds a shared road intelligence network for smarter cities

Ultimately, iSARTHI helps create safer roads, faster emergency response, and more intelligent transportation systems.

**Challenges we ran into**

During the development of **iSARTHI**, we faced several technical and integration challenges while combining hardware sensors, AI processing, and real-time data communication.

*Hardware Integration Issues*

One of the first hurdles was integrating multiple hardware components such as the Raspberry Pi, LiDAR/ToF sensors, cameras, and servo motors. Configuring GPIO pins and sensor drivers sometimes caused compatibility issues. For example, while setting up GPIO control for the servo motor, we encountered errors related to SoC peripheral address detection, which required troubleshooting library compatibility and system permissions.

We resolved this by updating system libraries, verifying GPIO access permissions, and ensuring that the correct hardware-specific libraries were used for the Raspberry Pi environment.

*Real-Time Sensor Data Handling*

Collecting and processing sensor data in real time was another challenge. The system needed to continuously detect road hazards like potholes or obstacles while simultaneously monitoring traffic conditions. Managing multiple data streams without causing delays required careful optimization.

To address this, we implemented efficient data processing pipelines and separated tasks such as sensor reading, AI inference, and data transmission into independent modules.

*3D Mapping and Environment Scanning*

Building a simple 3D mapping system using a single-point LiDAR/ToF sensor with a servo motor required creating a scanning mechanism that could rotate the sensor and collect distance measurements from multiple angles. Converting these readings into usable spatial data and visualizing them correctly required experimentation with coordinate transformations and visualization libraries.

We overcame this by refining the scanning algorithm and using data plotting tools to generate spatial maps from the collected measurements.

*Reliable Hazard Detection*

Another challenge was ensuring that hazards like potholes or obstacles were detected reliably without generating false alerts. Individual sensor readings can sometimes be noisy or inaccurate.

To improve reliability, we designed the system to support crowdsourced verification, where multiple vehicles reporting the same hazard increases the confidence level of the alert.

*System Integration*

Finally, integrating all components—hardware sensors, AI detection modules, and server communication—into a single working system required extensive testing. Ensuring stable communication between the vehicle unit and the backend server was critical for sending alerts and receiving updates.

Through iterative testing and debugging, we successfully created a working prototype that demonstrates how vehicles can act as mobile road intelligence units.

**Best Use of Gemini API**

We use the Google Gemini API to power the intelligent analysis and decision-making layer of iSARTHI. While sensors and AI models detect raw events such as potholes, congestion, obstacles, or driver fatigue, Gemini helps interpret this data and convert it into meaningful insights and guidance for drivers, fleets, and authorities.

**Intelligent Road Data Interpretation**

Vehicles equipped with the iSARTHI kit continuously collect data from sensors, cameras, and detection models. The Gemini API processes this information to understand the context of road conditions and generate actionable insights.

For example, Gemini can:

- Analyze sensor and camera inputs to classify road hazards

- Combine data from multiple vehicles to verify real road issues

- Interpret patterns such as frequent congestion zones or dangerous road segments

This helps transform raw sensor data into smart infrastructure intelligence.

**Smart Driver Assistance**

Gemini can act as an AI co-pilot by generating contextual driving advice based on real-time conditions. Instead of only triggering simple alerts, the system can provide more intelligent recommendations, such as:

- Suggesting alternate routes when congestion is detected

- Advising drivers to slow down in high-risk areas

- Explaining why a certain alert was triggered

These insights can then be delivered through voice alerts using ElevenLabs, allowing drivers to receive guidance without taking their eyes off the road.

**Crowdsourced Road Intelligence**

One of the most powerful uses of Gemini in iSARTHI is analyzing crowdsourced data from multiple vehicles. When several vehicles report similar hazards in a location, Gemini can validate the reports and generate a reliable road condition summary.

This allows authorities and fleets to quickly identify:

- Frequently damaged roads

- High accident-risk areas

- Recurring traffic congestion points

**Impact**

By integrating the Gemini API, iSARTHI moves beyond simple detection systems and becomes a smart mobility intelligence platform. Gemini helps the system:

- Convert raw vehicle data into actionable insights

- Provide context-aware driver assistance

- Improve accuracy of hazard reporting

- Enable data-driven infrastructure decisions

This significantly enhances road safety, traffic efficiency, and infrastructure monitoring

**Best Use of ElevenLabs**

We use ElevenLabs to power the voice interaction and real-time audio alert system in iSARTHI. Since drivers should keep their focus on the road, visual alerts alone are not always safe or effective. ElevenLabs enables the system to convert important system notifications into clear, natural-sounding voice alerts that drivers can instantly understand.

*How It Works in iSARTHI*

The iSARTHI system continuously analyzes data from vehicle sensors and AI models to detect road conditions and hazards. When a risk or important event is detected, the system sends the information to a voice module powered by ElevenLabs, which converts the alert into natural speech guidance for the driver.

*Examples of voice alerts include*:

- “Pothole detected ahead. Please slow down.”

- “Heavy traffic congestion detected on the current route.”

- “Driver fatigue detected. Please take a break.”

- “Emergency vehicle approaching. Please give way.”

- “Narrow road ahead. Reduce speed.”

Because ElevenLabs produces high-quality, natural human-like voices, the alerts are easy to understand even in noisy driving environments.

*How It Helps People*

1. Using voice AI improves safety and accessibility in several ways:

2. Reduces driver distraction by avoiding the need to check screens

3. Provides real-time guidance about hazards and road conditions
 
4. Improves reaction time for drivers through instant audio alerts
 
5. Makes the system accessible for drivers who may not be comfortable with complex interfaces

6. Supports multilingual communication, which is useful for diverse drivers in regions like India

**Impact**

By integrating ElevenLabs, iSARTHI becomes more than just a detection system—it becomes a real-time AI driving assistant that communicates with drivers in a natural and intuitive way. This significantly improves driver awareness, reduces accidents, and makes smart mobility features accessible even to older or non-smart vehicles.

**Algorand Bharat**

**iSARTHI** aligns with the goals of Algorand Foundation and the Algorand Bharat initiative by leveraging Algorand to build a transparent, secure, and decentralized road intelligence network for India.

Our system collects road condition data from vehicles equipped with the **iSARTHI** kit, including information about potholes, traffic congestion, hazards, and infrastructure issues. This data can be securely recorded and verified using Algorand’s blockchain infrastructure.

*Why Algorand*

Algorand is particularly suitable for this application because it offers:

● High-speed transactions, enabling real-time recording of road hazard data

● Low transaction costs, which is important for large-scale data reporting from thousands of vehicles

● Energy-efficient consensus, making it sustainable for continuous smart mobility systems

● Secure and tamper-proof data storage, ensuring infrastructure data cannot be altered or manipulated

*Blockchain Integration in iSARTHI*

Within our system, Algorand can be used to:

● Store verified road hazard reports submitted by vehicles

● Create a decentralized infrastructure reporting system where authorities can trust the authenticity of data

● Reward verified contributors, where vehicles reporting confirmed road issues could receive digital incentives

● Maintain transparent infrastructure records for government agencies and city planners

For example, when multiple vehicles detect the same pothole or road hazard, the system can validate the event and record it on the Algorand blockchain. This creates a permanent, trustworthy record of road conditions that can help municipalities respond faster.

**Impact for Bharat**

By combining AI-powered vehicle sensing with blockchain transparency, iSARTHI supports the vision of smart, connected, and safer transportation systems across India. It enables large-scale crowdsourced infrastructure monitoring while ensuring the integrity and reliability of collected data.

This approach can help government bodies, transport agencies, and smart city initiatives make data-driven decisions for road maintenance, traffic management, and public safety, contributing to the broader goals of digital infrastructure development in Bharat.

Team **RudraX** -- [Ritik Gorai](https://github.com/ritikrages), [Rittik vyas](https://github.com/vyas-R22), [Aryan maurya](https://github.com/aryan), [Abhishek verma](https://github.com/abhishekmmb18-lang)

`2026-03-08`

---

### Roshni
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/roshni-d119) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OmTalekar/Roshni) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/5mL-WxHTn4Y?si=X2I6Zqb3dCZxQ50x) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> power your street

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![NodeMCU IoT](https://img.shields.io/badge/NodeMCU%20IoT-333333?style=flat-square) ![LED](https://img.shields.io/badge/LED-333333?style=flat-square)

**The problem it solves**

The Problem It Solves
🏠 For Households With Rooftop Solar
You spent ₹2–3 lakhs installing solar panels. DISCOM pays you ₹3–4/kWh for surplus energy you export. Your neighbor pays ₹10–12/kWh for the same electricity from the grid. That gap is money you're losing every single day. At ₹3/kWh export rates, your solar payback period is 8–10 years. Most people never install solar because of this.
ROSHNI fixes this. Your surplus solar sells to neighbors at ₹6/kWh through the feeder pool — 3x what DISCOM pays you. Payback drops to 4–5 years.

🔌 For Households Without Solar
You pay ₹9/kWh for coal-powered grid electricity. Your neighbor's rooftop solar is sitting idle at noon because they generated more than they need. You could be buying that clean energy cheaper, but there's no mechanism to do it.
ROSHNI fixes this. Submit a demand request, AI matches you with available solar in your colony's pool at ₹6/kWh. You save 25% and get renewable energy.

🏙️ For the Colony / Feeder
Energy generated on one rooftop travels meters — not kilometers — to reach a neighbor on the same transformer. Zero transmission loss. Zero new infrastructure. The 11kV feeder your colony already runs on becomes a mini energy marketplace.

📋 For Regulatory Compliance
The RERC Third Amendment (December 2025) enables Group Net Metering at the feeder level in Rajasthan. But there's no working software implementation. ROSHNI is the first technical platform built specifically for this regulation — with DISCOM-compliant slab-based tariff billing, SHA256 bill hashing on Algorand for tamper-proof audit trails, and SUN tokens as blockchain-backed renewable energy certificates.

🌾 For Rural & Semi-Urban Accessibility
Energy bills in Hindi via ElevenLabs voice narration. A farmer or shopkeeper with rooftop solar doesn't need to understand blockchain or P2P trading — they just hear "Aaj aapne 4.5 kWh bijli becha, ₹40.50 ki kamai hui" and know exactly what happened.

**Challenges we ran into**

After a buyer submitted demand and got matched, the pool demand counter kept growing instead of resetting. The reason: demand records were created with status="pending" but never updated after matching. The pool engine counted all pending records as active demand — so every past allocation permanently inflated the demand counter.
Fix: After matching_engine.match_demand() runs, immediately update demand.status = "fulfilled" or "partial". Pool demand now correctly reflects only genuinely unmet pending requests

**Best Use of Gemini API**

🤖 Gemini AI — Allocation Brain
Every energy request goes through Gemini 2.0 Flash in real time. It receives pool supply, consumer demand, grid vs pool rates, and priority level — and decides exactly how much comes from solar vs grid, with a plain-language explanation of why. Judges and consumers can see the AI's reasoning for every single allocation decision, making it auditable and trustworthy — not a black box.

**Best Use of ElevenLabs**

🎙️ ElevenLabs — Voice for Bharat
A farmer in Rajasthan shouldn't need to read a dashboard to understand their energy bill. When a seller's solar generation gets allocated to neighbors, ElevenLabs narrates the result in Hindi: "Aaj aapne 4.5 kWh bijli becha". When a buyer gets matched from the pool, they hear their savings spoken aloud. This takes ROSHNI from a tech demo to something a real prosumer in a Tier 3 city can actually use.

**Algorand Bharat**

⛓️ Algorand — India's Energy Audit Trail
Three uses, all real, all live on testnet:
1. SUN Tokens — Every kWh traded mints 1 SUN token (ASA ID: 756341116). Seller's wallet shows what they generated and sold. Buyer's wallet shows clean energy certificates. On-chain, tamper-proof, instant.
2. Bill Hashing — Every monthly bill is SHA256 hashed and recorded on Algorand. A consumer can verify their bill was never altered after generation. No DISCOM can quietly change a number.
3. Feeder-Level REC Market — SUN tokens are transferable. Today they're certificates. Tomorrow they're tradeable Renewable Energy Certificates — the same thing large corporates pay crores for to meet ESG targets, now accessible to a household in Jaipur.

Team **Jedi Knights** -- [Khushi Chaudhary](https://github.com/Khushi-Chaudhary04), [Chirag Dulera](https://github.com/Chirag1522), [Praniti Kubal](https://github.com/Praniti1594), [Om Talekar](https://github.com/OmTalekar/OmTalekar)

`2026-03-08`

---

### Mukul
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/mine-sentinal-be64) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NeogenInnovators/mine-sentinel/blob/main/README.md) [![Built at](https://img.shields.io/badge/Built%20at-AceHack%205.0-0052CC?style=flat-square)](https://acehack5.devfolio.co)

> Mko

![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Internet of Things (IoT)](https://img.shields.io/badge/Internet%20of%20Things%20(IoT)-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Embedded C](https://img.shields.io/badge/Embedded%20C-333333?style=flat-square) ![Gyroscope](https://img.shields.io/badge/Gyroscope-333333?style=flat-square) ![Automation](https://img.shields.io/badge/Automation-333333?style=flat-square) ![MQ9 Gas Sensor](https://img.shields.io/badge/MQ9%20Gas%20Sensor-333333?style=flat-square) ![Lora Module](https://img.shields.io/badge/Lora%20Module-333333?style=flat-square)

Team **NGI Alpha** -- [Anuj Saini](https://github.com/anuj), [Mukul Vaid](https://github.com/Mukul289303), [Deepanshu pawar](https://github.com/rrdeepanshu09-ship-it), [Sahil .](https://github.com/sahil-mittan)

`2026-03-08`

---

### The Sybil Box
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/the-sybil-box-24bf) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Dhiveej/SYBIL_BOX.git) [![Built at](https://img.shields.io/badge/Built%20at-Aegis%20SandBox%20v2.0-0052CC?style=flat-square)](https://aegis-sandbox-v.devfolio.co)

> An AI honeypot that deanonymizes hidden attackers.

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Networking](https://img.shields.io/badge/Networking-333333?style=flat-square) ![Microcontroller](https://img.shields.io/badge/Microcontroller-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Generative AI](https://img.shields.io/badge/Generative%20AI-333333?style=flat-square)

**The problem it solves**

### Unmasking the Invisible Attacker

In modern cybersecurity, threat actors easily hide behind layers of proxies, VPNs, and randomized MAC addresses. **Traditional honeypots fail on two fronts:** 1. They rely on static, predictable scripts that experienced hackers and automated bots easily identify as fake. 
2. Even when they successfully log an intrusion, they only capture the useless local or proxy IP, leaving the attacker's true identity entirely concealed.

**The Sybil Box** revolutionizes threat intelligence by replacing passive logging with **AI-Driven Deception and Identity Correlation**. 

Instead of just recording an attack, it actively tricks the attacker into deanonymizing themselves.

### How it solves the problem:

* **Dynamic AI Hallucination:** Instead of using easily recognizable static scripts, Sybil Box uses the **Groq API (LLaMA-3)** to generate a highly convincing, interactive Ubuntu terminal in real-time. As the attacker explores the ESP32-hosted Telnet server, the AI adapts, keeping them engaged and believing they've breached a real system.
* **Bypassing Proxies via Canary Traps:** We don't stop at terminal logs. The AI strategically baits the attacker with hallucinated files (like `passwords.txt`) that contain custom Ngrok canary links. When the attacker inevitably opens the link in their web browser to steal the credentials, the request bypasses their terminal's proxy tunnel. 
* **Real-Time Identity Correlation:** The moment the canary is triggered, our backend correlates the local intrusion with the external HTTP request, instantly capturing the attacker's **Real Public IP** (including complex IPv6 routes) and geolocation. 
* **Live SOC Dashboard:** All of this is visualized in a React-based command center that tracks the kill chain, parses attacker intent, and flags their true identity with a "🎯 REAL TRACE" tag the millisecond the trap snaps.

Ultimately, Sybil Box turns an attacker's curiosity into their biggest vulnerability.

**Challenges we ran into**

Building a hardware-to-cloud deception engine was incredibly complex. We weren't just writing software; we had to make a low-power microcontroller seamlessly talk to a massive cloud LLM, while doing advanced network routing on the fly. 

Here are the major hurdles we overcame:

### 1. The Hardware-to-Cloud Bridge
**The Problem:** The ESP32 is perfect for broadcasting a rogue Wi-Fi Access Point and hosting a Telnet server, but it lacks the memory to process AI responses. 
**The Fix:** We had to architect a custom serial-to-cloud bridge. The ESP32 captures raw socket data, streams it over COM to a Python 'Brain' (`sybil_brain.py`), which then formats the payload, hits the Groq LLaMA-3 API, and streams the hallucinated response back to the attacker in milliseconds so the terminal feels native.

### 2. The Canary Tunneling Nightmare (Anti-Bot Shields)
**The Problem:** To capture an attacker's real public IP, we needed to embed a public URL in the hallucinated `passwords.txt` file. We initially used `localtunnel` and `pinggy.io`. However, because we were using free tiers, they injected "Anti-Phishing Warning" screens or required tunnel passwords. If a hacker sees a warning screen, the deception is instantly ruined.
**The Fix:** We had to completely tear down our tunneling architecture mid-development. We migrated the canary server to use authenticated **Ngrok** tunnels, which allowed us to serve the poisoned files instantly and stealthily without any intermediary warning screens blocking the attacker's browser.

### 3. The "Loopback" DNS Polling Paradox
**The Problem:** Our central AI brain needed to poll the canary server every 5 seconds to see if the trap was sprung. Initially, we had it polling the *public* Ngrok URL. This caused massive DNS resolution errors (`[Errno 11001]`) because the Windows DNS resolver got confused trying to route out to the internet and back into the same machine continuously.
**The Fix:** We decoupled the URLs. We configured the AI to inject the *public* Ngrok URL into the hallucinated terminal for the attacker to see, but hardcoded the Python poller to securely fetch data via an internal loopback (`http://localhost:8080/hits`). This completely bypassed the internet for internal checks, dropping latency to zero.

### 4. UI/UX and the IPv6 Data Crash
**The Problem:** When we successfully snared our first mobile 4G attacker, the captured Real IP was a massive IPv6 string (e.g., `2401:4900:330c:c44e...`). This completely broke the CSS grid of our React SOC Dashboard, causing text to bleed into other columns and overlap with MAC addresses.
**The Fix:** We had to dynamically refactor the React frontend, implementing flex-col layouts and aggressive `break-all` word-wrapping specifically for the identity columns, ensuring the dashboard remained beautiful and legible regardless of the IP protocol length.

Team **Void Walkers** -- [Dhanush Gowdauk](https://github.com/dhanush-82), [Diraj G](https://github.com/diraj16), [Dhiveej Atish N](https://github.com/Dhiveej), [Charan Ej](https://github.com/apashyam-kirikiri)

`2026-03-08`

---

### PharmaSathi
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/pharmasathi-b698) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Panda4374/PharmaSathi) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/drive/folders/13UGZyPje8ZqOyzS_MOnaiQYqtOLaw2aA?usp=drive_link) [![Built at](https://img.shields.io/badge/Built%20at-DoubleSlash%204.0-0052CC?style=flat-square)](https://doubleslash4.devfolio.co)

> PharmaSathi — The smarter way to take medicines.

![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Android SDK](https://img.shields.io/badge/Android%20SDK-333333?style=flat-square) ![Bluetooth Module](https://img.shields.io/badge/Bluetooth%20Module-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![LCD Screen](https://img.shields.io/badge/LCD%20Screen-333333?style=flat-square) ![DS3231 Real-Time Clock Module](https://img.shields.io/badge/DS3231%20Real--Time%20Clock%20Module-333333?style=flat-square) ![Dart Programming Language](https://img.shields.io/badge/Dart%20Programming%20Language-333333?style=flat-square)

**The problem it solves**

Old age brings frequent medical check-ups, complex dose charts, dozens of prescriptions, resulting in numerous medicines to manage daily.
Remembering to take the right pill at the right time without assistance becomes increasingly difficult for an elder, reducing treatment effectiveness and increasing health risks and medicine wastage.
This highlights the need for a simple, reliable, and elderly-friendly medication management solution.
While mobile med reminder apps already exist, they rely heavily on user interaction and do not track remaining pill quantity or expiry date.  Moreover, elderly users may find smartphones difficult to navigate, and apps alone cannot physically organize medications. 
Thus, a combined software-hardware solution that not only reminds users but also guides them to the correct pill at the correct time offers a more practical, elderly-friendly solution—reducing confusion, missed doses, and medicine wastage.

**Challenges we ran into**

It was not at all easy to build the circuit of the medication box and interfacing with the mobile app, completely from scratch. The ESP32 is connected to many components- RTC module, various leds and push buttons, vibrator motor for alert, LCD display for UI interface and touch sensor for user convenience. Connecting them was a hurdle, which the team successfully managed to complete overnight.
The formatting of expiry date, medication log and time management as well as BLE connection were many problems which havent been completely solved- but we will also try to improve our project in the future. The project holds potential and can help the aged people- the once pillars of our society.

**Health**

PharmaSathi directly addresses a critical challenge in healthcare—medication adherence, especially among elderly individuals and patients managing multiple prescriptions. Missing or mistiming doses can reduce treatment effectiveness, worsen medical conditions, and increase hospitalizations.

Our smart pill box assists users by providing timely reminders, guided medication access, and consumption tracking. The device alerts the user when it is time to take a medicine, indicates the correct compartment, and logs whether the dose was taken, snoozed, or skipped. These logs can be shared with caregivers or doctors to monitor adherence and adjust treatment if needed.

By combining embedded hardware, real-time scheduling, and digital monitoring, PharmaSathi helps improve patient compliance, reduce medication errors, and support independent living for elderly users. This makes it a practical and impactful solution within the health technology and patient care domain.

Team **Ignite** -- Bikram Roy, Pratyush Das, Eesadip B

`2026-03-08`

---

### MITTIE
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/demo-1720) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/anjalisingh150304/mitti) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://mitti-two.vercel.app/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtu.be/WKM4XBwmMvY) [![Built at](https://img.shields.io/badge/Built%20at-Diversion%202K26-0052CC?style=flat-square)](https://diversion2k26.devfolio.co)

> Multi-parameter IoT-enabled Threshold Engine

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Unity 3D](https://img.shields.io/badge/Unity%203D-333333?style=flat-square)

**The problem it solves**

Agriculture often relies on manual observation and generalized practices, which can lead to inefficient fertilizer use and delayed disease intervention. MITTIE transforms this process by providing a "Glass-Box" AI approach to precision farming.

Eliminates Guesswork: Instead of blanket fertilizer application, farmers get precise recommendations based on real-time NPK (Nitrogen, Phosphorus, Potassium) levels.

Early Intervention: The AI-powered leaf scan detects diseases like Septoria Spot before they become unmanageable, protecting crop yields.

Accessibility: By supporting regional languages (Hindi, Bengali, and English) and including a voice-enabled AI assistant, MITTIE makes high-end agritech usable for farmers regardless of their technical or linguistic background.

Actionable Insights: It doesn't just identify a problem; it provides specific solutions, such as suggesting exactly which fertilizer (e.g., Urea or Muriate of Potash) to use.

**Challenges we ran into**

Building an end-to-end IoT system on a resource-constrained device presented several hurdles:

Hardware Interfacing & Latency: Interfacing the RS485 NPK sensor with the Raspberry Pi required careful serial communication management. Initially, data readings were inconsistent. I resolved this by implementing a robust error-handling script in Python and using a dedicated RS485-to-USB converter to stabilize the signal.

Edge Optimization: Running a deep learning model for plant disease detection and a voice assistant simultaneously pushed the Raspberry Pi's CPU to its limits. I optimized the system by converting the models to a lightweight format (TFLite/OpenCV) and managing thread execution to ensure the UI remained responsive.

Language & UI Integration: Syncing the multi-language Flask backend with a real-time voice agent was complex. I utilized a JSON-based localization system to ensure that switching languages updated both the text-on-screen and the voice-agent's response logic instantaneously.

**Gemini API**

It was the general helper and the back api of chat bot and in multilingual script translator

**ElevenLabs**

We made the multilingual voice assistant chat bot with proper guard band

Team **KrishiDhan** -- [Aasish Shrestha](https://github.com/Aasish1234), [Anjali Singh](https://github.com/anjalisingh150304)

`2026-02-28`

---

### DoseSure
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/dosesure-bc3e) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/thecahintosh/DoseSure) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://e2b106285bcd8bb57c.gradio.live/) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1162877370?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> Predicting antibiotic

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![XGBoost](https://img.shields.io/badge/XGBoost-333333?style=flat-square)

**The problem it solves**

Doctors must choose antibiotics before knowing if they will work.
Lab results arrive days later, allowing infections and resistance to spread.

**Challenges we ran into**

Handling large, highly imbalanced clinical datasets.
Modeling time-dependent patient histories and hospital movement graphs.
Balancing high accuracy with explainability for clinical trust.

**Google Gemini**

the pipeline

Team **404:Name Found** -- [Vidushi Jain](https://github.com/vidushi2536), [Shivansh Singh](https://github.com/thecahintosh), [Parnika Nagpal](https://github.com/Parnika1804)

`2026-02-07`

---

### LIVERGUARD
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/liverguard-4b27) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mayank-png-dev/HackTU_LG/tree/main) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://vimeo.com/1162941120?share=copy&fl=sv&fe=ci) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> From raw sensors to reliable liver diagnostics.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-333333?style=flat-square) ![Git](https://img.shields.io/badge/Git-333333?style=flat-square) ![Arduino IDE](https://img.shields.io/badge/Arduino%20IDE-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GitHub](https://img.shields.io/badge/GitHub-333333?style=flat-square) ![ESP-32 WiFi Module](https://img.shields.io/badge/ESP--32%20WiFi%20Module-333333?style=flat-square)

**The problem it solves**

🚨 1. Late Detection of Liver Disorders

Problem:
Liver diseases often progress silently and are detected late, when treatment becomes complex and costly. Conventional diagnostics rely on invasive blood tests, imaging, or hospital visits, making early screening inaccessible for many people.

Solution:
👉 We built a non-invasive, AI-powered screening system that estimates liver health risk from physiological signals and visual biomarkers, enabling early risk flagging without clinical infrastructure.

🧪 2. Inaccessibility of Screening in Low-Resource Settings

Problem:
Rural and low-resource settings lack access to diagnostic labs and specialists, leading to delayed diagnosis and poor outcomes.

Solution:
👉 LiverGuard runs on low-cost IoT hardware + a lightweight web app, enabling portable, low-cost screening that can be deployed outside hospitals.

**Challenges we ran into**

1. Noisy Sensor Data & Environmental Variability

Problem:
Raw sensor readings (e.g., color under different lighting, thermal noise, bio-signal variability) are unstable and can mislead ML models.

Solution:
👉 We implemented robust preprocessing and feature engineering (color normalization, yellowness index, robust scaling) and noise-aware training, improving stability under real-world conditions.

2. Fragile Single-Model Predictions

Problem:
Single ML models can be brittle and overfit, especially on small, imbalanced medical datasets.

Solution:
👉 We used ensemble learning (Voting + Stacking) with automated hyperparameter tuning to improve generalization and robustness, leading to more reliable screening.

3. Train–Deploy Mismatch in ML Systems

Problem:
ML demos often fail in deployment because preprocessing during inference doesn’t match training.

Solution:
👉 We serialized preprocessing artifacts (scaler.pkl) and enforced consistent feature schemas in the backend, ensuring reliable real-time inference.

4.Lack of Real-Time, Explainable Screening Interfaces

Problem:
Even when ML models exist, they’re hard to demo or use without a real-time interface.

Solution:
👉 We built a Streamlit web dashboard + FastAPI backend to provide real-time predictions with confidence scores, making the system usable and demo-ready.

Team **LiverGuard** -- [ABHEET SINGH](https://github.com/abheet77), [Rishabh Suri](https://github.com/Rishabhsuri96), [Mayank Singh](https://github.com/Mayank-png-dev)

`2026-02-08`

---

### SiloGuard AI
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/siloguard-ai-6651) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lavenhub/SiloGuard-AI) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1fJiA-Cnr2gUeW_rwhEgwJHrqDKNwdGnl/view?usp=sharing) [![Video](https://img.shields.io/badge/Video-Watch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=fWKJ6mJXOVY) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> Intelligent Vision for Superior Silo Safety

![scikit-learn](https://img.shields.io/badge/scikit--learn-333333?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-333333?style=flat-square) ![OpenCV](https://img.shields.io/badge/OpenCV-333333?style=flat-square) ![pandas](https://img.shields.io/badge/pandas-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![C](https://img.shields.io/badge/C-333333?style=flat-square) ![Plotly](https://img.shields.io/badge/Plotly-333333?style=flat-square) ![Joblib](https://img.shields.io/badge/Joblib-333333?style=flat-square)

**The problem it solves**

SiloGuard AI Pro addresses the critical challenge of post-harvest loss and industrial accidents by transforming reactive silo management into a proactive, data-driven ecosystem. The system utilizes a CNN-inspired texture analysis engine to identify subtle biological clumping and mold growth that traditional thermal sensors often miss, protecting grain purity at the source. By integrating real-time IoT telemetry, including VOC and moisture monitoring, the platform predicts spontaneous combustion risks with high precision, allowing for early intervention before catastrophic events occur. Beyond crop protection, SiloGuard prioritizes human life through a real-time Worker Safety Index that analyzes atmospheric hazards to provide clear "Go/No-Go" entry guidance. This comprehensive approach is secured by an immutable blockchain ledger, which generates QR-coded safety passports to ensure transparent compliance and audit-ready records. Ultimately, the project streamlines complex agricultural operations into a single, intuitive dashboard that bridges the gap between physical silo conditions and digital intelligence.

**Challenges we ran into**

One of the most significant technical hurdles was the "False Positive Shadow Effect," where the AI initially flagged the natural dark shadows between healthy grain kernels as potential mold, leading to inaccurate 0% purity readings. To overcome this, I shifted from simple color-thresholding to a sophisticated "Texture-First" logic using a Gaussian Blur pre-processing layer to smooth out geometric noise followed by a Laplacian filter to isolate only the "fuzzy" textures characteristic of biological growth. Another major challenge was establishing a reliable high-definition visual feed from the silo interior without expensive industrial cameras; I solved this by engineering a hardware bridge using the Camo API to repurpose a smartphone as a high-fidelity USB-C sensor. Finally, ensuring the logic worked across different mobile resolutions required implementing a standardized "Tensor-sizing" function that resizes all incoming frames to a consistent 512x512 matrix before analysis. These iterations moved the project from a basic script to a robust industrial tool capable of distinguishing between harmless shadows and genuine contamination.

**Google Gemini**

SiloGuard AI Pro fits the Gemini track by transforming raw, complex sensor telemetry and visual diagnostic data into actionable human intelligence. By integrating Gemini, the project moves beyond simple data visualization to Automated Expert Reporting, where the model analyzes the correlation between rising VOC levels, moisture spikes, and BDI (Biological Density Index) percentages to draft comprehensive safety briefs.

Gemini specifically powers the Contextual Safety Advisory module, which interprets the "Worker Health Risk" index. Instead of just showing a percentage, the model can provide natural language instructions to a worker via the dashboard, such as: Detected high VOC levels and 12% mold coverage; entry is prohibited without Level 3 respiratory protection and active ventilation for 20 minutes.

Team **Inferno Halt** -- [Pulkit Gangal](https://github.com/Pulkit4O4), [Eshan Goel](https://github.com/EshanGoel07), [Devansh Taneja](https://github.com/devanshtaneja2), [Lavisha Valecha](https://github.com/lavishaa4), [Lavish Patil](https://github.com/lavenhub)

`2026-02-08`

---

### GPS-JAMMED AUTONOMOUS NAVIGATION
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/gpsjammed-autonomous-navigation-7783) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Khushveer-Kaur/Final_Drone_Latest) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://aerovision-nine.vercel.app) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> Autonomous Navigation Beyond GPS

![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![GPS](https://img.shields.io/badge/GPS-333333?style=flat-square) ![ESP32](https://img.shields.io/badge/ESP32-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-333333?style=flat-square)

**The problem it solves**

This project addresses the issue of GPS dependency in drones and autonomous systems by monitoring GPS availability in real time. When GPS signals are lost or degraded, the system clearly indicates GPS status and supports continued safe operation, improving reliability and safety in challenging environments such as indoors, urban areas, or signal-jammed zones.

**Challenges we ran into**

One of the main challenges was obtaining a stable GPS fix during testing, especially indoors where signals are weak or unavailable. This caused inconsistent location data and made it difficult to verify system behavior. To address this, testing was moved closer to windows and open areas, and visual indicators were added to clearly distinguish between GPS-available and GPS-denied states.

Another challenge was managing reliable communication between the GPS module and the ESP32, including correct serial pin configuration and baud rate selection. This was resolved by validating hardware connections, using a dedicated hardware serial interface, and adding serial debugging to confirm data flow.

Finally, handling hardware constraints such as limited indicators required careful logic design to ensure clear system feedback using only two LEDs, which was achieved through simple, well-defined state control.

Team **TechVitals** -- [Khushveer Kaur](https://github.com/Khushveer-Kaur), [Ishaan Sharma](https://github.com/Ishaan0709), [Sneha Mittal](https://github.com/), [Mehak Jindal](https://github.com/), [Lovenish Attri](https://github.com/LovenishAttri)

`2026-02-08`

---

### safe drone landing
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/safe-drone-landing-88c0) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/harshrarora/safe-drone-landing) [![Built at](https://img.shields.io/badge/Built%20at-HackTU%207.0-0052CC?style=flat-square)](https://hacktu7.devfolio.co)

> drone landing when confidence is truly calibrated.

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![React](https://img.shields.io/badge/React-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![YOLOv3 Algorithm](https://img.shields.io/badge/YOLOv3%20Algorithm-333333?style=flat-square) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-333333?style=flat-square)

**The problem it solves**

utonomous drones operating in safety-critical environments (defense, disaster response, infrastructure inspection) must decide whether a landing zone is safe — not just detect objects.

Most vision systems output a bounding box and a confidence score, but these scores are often over-confident and poorly calibrated, especially under:

low-light or weather distortion

motion blur

occlusion

unseen terrain

adversarial or cluttered environments

A wrong “high-confidence” prediction can lead to crashes, equipment damage, or mission failure

**Challenges we ran into**

Building a safety-critical perception stack in a hackathon setting came with several technical challenges:

1. Injecting Monte-Carlo Dropout into YOLO

YOLO does not natively support MC Dropout at inference.

We solved this by:

inserting dropout layers dynamically using forward hooks

keeping BatchNorm frozen

forcing stochastic behavior during inference

aggregating results across 30 passes

2. Calibration across uncertainty pipelines

Combining:

raw YOLO outputs

MC Dropout distributions

ensemble disagreement

required careful temperature scaling so probabilities stayed meaningful.

We implemented:

post-hoc temperature optimization

reliability curve analysis

Expected Calibration Error computation

3. Handling edge cases

Some images had:

no landing pads

only obstacles

extremely low contrast

This broke early versions of the safety logic.

We fixed this by:

adding explicit abort conditions

fallback safety decisions

robust null-detection handling

JSON-safe serialization for deployment outputs

4. Integrating multiple notebooks into a unified pipeline

Training, augmentation, MC Dropout experiments, ensemble runs, and calibration were originally isolated.

We refactored everything into:

modular inference pipelines

shared calibration modules

reusable risk-assessment logic

GitHub-ready architecture

5. Real-time visualization & deployment readiness

We added:

automatic overlay generation

safety banners

metric export

result dashboards

so the system can be easily integrated into a web UI or drone control stack.

Team **Init to Win it** -- [Swastik Pundir](https://github.com/Codeswastik007), [Tanmay Agarwal](https://github.com/Tanmay-Agarwal2312), [Yashasvi Gupta](https://github.com/YashG-4818), [Harsh Arora](https://github.com/harshrarora)

`2026-02-08`

---

### SeismoArch Iot Model
[![Devfolio](https://img.shields.io/badge/Devfolio-View%20Project-4B32C3?style=flat-square&logo=devfolio&logoColor=white)](https://devfolio.co/projects/seismoarch-iot-model-93df) [![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/harideep-bethi/saim-early-warning) [![Demo](https://img.shields.io/badge/Demo-Live-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://drive.google.com/file/d/1E-FgWfrC4x03mvexJzxLPMGPhWYxUxer/view?usp=sharing) [![Built at](https://img.shields.io/badge/Built%20at-MERGE--CONFLICT-0052CC?style=flat-square)](https://mergeconflict.devfolio.co)

> Real-time structural monitoring & early alerts

![HTML](https://img.shields.io/badge/HTML-333333?style=flat-square) ![Node.js](https://img.shields.io/badge/Node.js-333333?style=flat-square) ![CSS](https://img.shields.io/badge/CSS-333333?style=flat-square) ![JavaScript](https://img.shields.io/badge/JavaScript-333333?style=flat-square) ![Python](https://img.shields.io/badge/Python-333333?style=flat-square) ![Firebase Cloud Messaging](https://img.shields.io/badge/Firebase%20Cloud%20Messaging-333333?style=flat-square)

**The problem it solves**

Structural failures and seismic events often cause damage not because warnings don’t exist, but because alerts arrive too late or not at all at the building level. Most existing systems are expensive, centralized, or unsuitable for small buildings, campuses, and resource-constrained regions.

SeismoArch IoT Model (SAIM) addresses this gap by enabling local, real-time structural monitoring and early warning using distributed sensors and fast decision logic. The system continuously observes vibration and tilt patterns, detects abnormal behavior, and triggers alerts before damage escalates.

SAIM can be used in apartments, academic buildings, and small infrastructures to improve situational awareness, response time, and safety during seismic or abnormal structural events. By focusing on affordability and deployability, it makes early warning and monitoring accessible beyond large-scale government systems.

**Challenges we ran into**

One major challenge was dealing with noisy real-world sensor data while still making timely decisions. Small vibrations, environmental disturbances, and sensor drift could easily trigger false positives if handled naively.

Another hurdle was coordinating real-time data flow across hardware, backend logic, and alert delivery without introducing noticeable latency. Debugging timing issues across multiple components required careful logging and iterative testing.

These challenges were addressed by refining decision thresholds, validating behavior through controlled test conditions, and simplifying the data pipeline to prioritize reliability over complexity. The focus throughout was on building a system that behaves predictably under imperfect conditions.

**Open Track**

SAIM fits naturally into the Open Track because it focuses on solving a real-world infrastructure and safety problem without being constrained to a single theme or technology. The project is built as an end-to-end system that combines sensing, real-time data handling, decision logic, and user alerts to address a practical use case.

Rather than optimizing for a single algorithm or feature, SAIM emphasizes system design, reliability, and deployability, which aligns with the Open Track’s focus on product-oriented solutions. The approach prioritizes clarity, impact, and execution under real-world constraints, making it well-suited for open-ended evaluation based on usefulness and engineering depth.

[Harideep Bethi](https://github.com/harideep-bethi)

`2026-02-01`

---

Curated by [tech-anupam](https://github.com/tech-anupam) | Follow on Instagram: [@tech.anupam](https://instagram.com/tech.anupam)
