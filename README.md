<!--
  skyv26 / profile README — dark neon glass system
  Artwork lives in ./assets and is regenerated with:  python3 assets/build_svgs.py .
  Every SVG carries its own dark background, so it reads the same in GitHub light and dark themes.
-->

<a name="top"></a>

<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Aakash Verma — Software Engineer, Full-Stack Developer, AI Systems & Product Architecture">
</p>

<p align="center">
  <a href="#introduction"><img src="./assets/nav/nav-00.svg" height="36" alt="00 Introduction"></a>
  <a href="#deployed-products"><img src="./assets/nav/nav-01.svg" height="36" alt="01 Deployed Products"></a>
  <a href="#product-explorations"><img src="./assets/nav/nav-02.svg" height="36" alt="02 Explorations"></a>
  <a href="#engineering-in-practice"><img src="./assets/nav/nav-03.svg" height="36" alt="03 Engineering in Practice"></a>
  <a href="#technology-stack"><img src="./assets/nav/nav-04.svg" height="36" alt="04 Stack"></a>
  <a href="#architecture"><img src="./assets/nav/nav-05.svg" height="36" alt="05 Architecture"></a>
  <a href="#community"><img src="./assets/nav/nav-06.svg" height="36" alt="06 Community"></a>
  <a href="#github-activity"><img src="./assets/nav/nav-07.svg" height="36" alt="07 Activity"></a>
  <a href="#writing"><img src="./assets/nav/nav-08.svg" height="36" alt="08 Writing"></a>
  <a href="#creative-work"><img src="./assets/nav/nav-09.svg" height="36" alt="09 Creative"></a>
  <a href="#contact"><img src="./assets/nav/nav-10.svg" height="36" alt="10 Contact"></a>
</p>

<br>

<!-- ═══════════════════════════════ 00 ═══════════════════════════════ -->

<a name="introduction"></a>
<img src="./assets/sections/section-00.svg" width="100%" alt="00 — Introduction">

> **I don't just write code. I understand problems, design systems, build products, and take them to deployment.**

I'm **Aakash Verma** — Software Engineer, Full-Stack Developer and Forward Deployed Engineer working in **AI systems and product architecture**. I work close to the business problem, in lead, senior-engineering and architecture roles, and carry products from requirements to production.

My path runs from **Electronics & Communication Engineering** and embedded hardware to full-stack platforms, backend and API architecture, SaaS, financial workflows and AI-powered applications. The products below run in **education, water resources, healthcare, astrology and professional services** — from Sierra Leone and Ethiopia to East Africa and India.

<table>
  <tr>
    <td width="50%" valign="top">
      <sub><b>WHAT I BRING</b></sub><br><br>
      ◆ Requirements → architecture → production<br>
      ◆ Frontend, backend, data and infrastructure<br>
      ◆ Domain fluency across regulated and specialist fields<br>
      ◆ AI systems that are useful, safe and explainable
    </td>
    <td width="50%" valign="top">
      <sub><b>HOW I WORK</b></sub><br><br>
      ◆ Understand the business before writing code<br>
      ◆ Build systems, not short-term hacks<br>
      ◆ Optimise for long-term maintainability<br>
      ◆ Teach while building
    </td>
  </tr>
</table>

<p align="center"><i>"Expectations lead to disappointments."</i> — my life's philosophy</p>

<img src="./aakash_cover.png" width="100%" alt="Aakash Verma — Disciplined intention. Relentless consistency. Absolute focus.">

<br><br>

<!-- ═══════════════════════════════ 01 ═══════════════════════════════ -->

<a name="deployed-products"></a>
<img src="./assets/sections/section-01.svg" width="100%" alt="01 — Deployed Products">

<div align="center">

| | Product | Domain | Live |
| :-: | :-- | :-- | :-- |
| **01** | [Edqio](#edqio) | Education technology · SaaS | [edqio.com ↗](https://edqio.com) |
| **02** | [Redwan HydroGeology](#redwan-hydrogeology) | Scientific software · water resources | [redwantcc.com ↗](https://www.redwantcc.com) |
| **03** | [Smile Medical Hospital](#smile-medical-hospital) | Healthcare · institutional | [smiledmi-sl.com ↗](https://www.smiledmi-sl.com) |
| **04** | [Horovista](#horovista) | Astrology · my own product | [horovista.com ↗](https://horovista.com) |
| **05** | [Genuine Consultancy Services](#genuine-consultancy-services) | Professional services | [genuineconsultancyservices.com ↗](https://genuineconsultancyservices.com) |

</div>

<br>

<!-- ─────────────── 01 EDQIO ─────────────── -->

<a name="edqio"></a>
<a href="https://edqio.com"><img src="./assets/projects/edqio.svg" width="100%" alt="01 — Edqio: school operating system for campuses and multi-school groups across East Africa. Live at edqio.com"></a>

**Edqio** brings admissions, timetables, attendance, fees, report cards and school-bus operations into one system for single campuses and multi-school groups, built around how East African schools run. A Daad Consulting product, developed with Purple Ocean FZE. **My role:** Forward Deployed Engineer — lead, senior engineering and architecture.

<details>
<summary><b>Case study</b> · role-based school operations</summary>
<br>

**The problem.** Schools run on registers, spreadsheets, fee books and phone calls. Each role needs a different slice of the same data, and money and grades need controls, not trust.

<table>
  <tr>
    <th align="left" width="33%"><sub>ACADEMICS</sub></th>
    <th align="left" width="33%"><sub>FINANCE &amp; CONTROLS</sub></th>
    <th align="left" width="34%"><sub>COMMUNITY &amp; TRANSPORT</sub></th>
  </tr>
  <tr>
    <td valign="top">Students, staff, guardians, classes, subjects, rooms<br>Enrollment &amp; admissions<br>Attendance, assignments, exams, grading<br>Timetables<br>Report cards with a <b>QR code</b> anyone can verify</td>
    <td valign="top">Invoices, payments, receipts, balances<br>Invoices sent only after staff review<br>Waivers &amp; scholarships need principal approval<br><b>Separation of duties</b> — no self-approval<br>Exportable audit trail</td>
    <td valign="top">Parent–teacher–student messaging with a kept record<br>Browser-based parent–teacher meetings<br>Live lesson streaming with attendance<br>Bus routes, stops, schedules &amp; <b>live location</b></td>
  </tr>
</table>

**What makes it technically interesting**

- **Authorisation is a product feature.** Six roles — principal, teacher, parent, student, finance officer, admission officer — each see only their own work; permissions are checked on every request and configurable per school.
- **Maker–checker finance.** The requester of a fee change can never approve it, and every approval lands in an exportable audit trail.
- **Integrity beyond the app.** QR-verifiable report cards let third parties check a document without an account.
- **Real-time operations** — live bus location for parents next to classic records management.

```mermaid
flowchart LR
    R["Six roles"] --> P{"Per-request<br/>permission check"}
    P --> A["Academics"]
    P --> F["Finance"]
    P --> T["Transport"]
    F --> M["Principal approval<br/>separation of duties"]
    M --> L["Audit trail"]
    A --> Q["QR-verified<br/>report cards"]
```

<sub>Drawn from publicly documented behaviour — not an internal architecture diagram. Stack observed on the live site: Next.js.</sub>

<!-- CONFIRM: modules you led; backend, database and hosting stack. -->

</details>

<br>

<!-- ─────────────── 02 REDWAN ─────────────── -->

<a name="redwan-hydrogeology"></a>
<a href="https://www.redwantcc.com"><img src="./assets/projects/redwan-hydrogeology.svg" width="100%" alt="02 — Redwan HydroGeology: digital platform of an Ethiopian water-resources consultancy with 3D terrain, project atlas and client portal. Live at redwantcc.com"></a>

**Redwan HydroGeology Solutions** is a water-resources consultancy based in Addis Ababa with a branch in Jigjiga. Its platform turns a technical practice — groundwater investigation, feasibility studies, design and construction supervision — into something clients can explore: interactive terrain, a project atlas and a secure client portal. **My role:** Forward Deployed Engineer — lead, senior engineering and architecture.

<details>
<summary><b>Case study</b> · scientific visualisation for a water-resources practice</summary>
<br>

**Audience.** Federal and regional government bodies, city administrations, universities, international organisations and private clients.

| Capability | What it does |
| :-- | :-- |
| **Interactive 3D terrain map** | Elevation from SRTM, boundaries from geoBoundaries and Natural Earth; auto-orbit and hover elevation readouts |
| **Elevation profile** | Cross-section of the terrain along the map |
| **Groundwater models** | A cross-section and a rotatable block model explaining aquifer systems |
| **Project atlas** | Assignments filterable by ongoing / completed, each with client, role, duration, location and outputs, linked to map locations |
| **Methodology** | Five stages — desk study, field investigation, drilling & testing, feasibility & design, supervision & administration |
| **Client portal** | Separate secure portal for reports, documents and progress updates |
| **Enquiry builder** | Collects organisation, location and services, then prepares a ready-to-send email |

**What makes it technically interesting.** Real geospatial data in the browser, 3D scientific diagrams that a non-specialist can rotate, and a domain vocabulary — strata, aquifers, pump tests, water balance — presented without dumbing it down.

<sub>Stack observed on the live site: Next.js. Data sources: SRTM, geoBoundaries, Natural Earth.</sub>

<!-- CONFIRM: 3D/map library, portal stack, hosting, and your scope. -->

</details>

<br>

<!-- ─────────────── 03 SMILE ─────────────── -->

<a name="smile-medical-hospital"></a>
<a href="https://www.smiledmi-sl.com"><img src="./assets/projects/smile-hospital.svg" width="100%" alt="03 — Smile Medical Hospital: web platform for a registered hospital in Freetown, Sierra Leone. Live at smiledmi-sl.com"></a>

**Smile Medical Hospital** is a registered hospital in Freetown, Sierra Leone. Its platform brings medical and dental services, a diagnostic laboratory, health and motor insurance, outreach and patient enquiries together on one site. **My role:** Forward Deployed Engineer — lead, senior engineering and architecture.

<details>
<summary><b>Case study</b> · one front door for a multi-service institution</summary>
<br>

<table>
  <tr>
    <td width="50%" valign="top">
      <sub><b>PATIENT JOURNEYS</b></sub><br>
      14 services — cardiology, paediatrics, surgery, laboratory, dental, dental CAD/CAM lab, internal medicine, maternity, radiology, pharmacy, wards, ICU, emergency, OPD<br>
      Laboratory test menu in four groups · book a test<br>
      Book an appointment · sign in · registration<br>
      Health and motor insurance cover · request a quote
    </td>
    <td width="50%" valign="top">
      <sub><b>PLATFORM</b></sub><br>
      Contact form with required fields and <b>Cloudflare Turnstile</b><br>
      About, medical, dental, laboratory, insurance, outreach, gallery, experts, FAQs<br>
      Privacy, terms and <b>patient-rights</b> pages<br>
      Media through Cloudinary and Next.js image optimisation
    </td>
  </tr>
</table>

Emergency contact and hours come first; every path then ends in a booking or enquiry action. Patients, families, insurance customers and charity partners each get their own route.

<sub>Stack observed on the live site: Next.js · Vercel · Cloudinary · Cloudflare Turnstile.</sub>

<!-- CONFIRM: what sits behind sign-in / registration / booking, and your scope. -->

</details>

<br>

<!-- ─────────────── 04 HOROVISTA ─────────────── -->

<a name="horovista"></a>
<a href="https://horovista.com"><img src="./assets/projects/horovista.svg" width="100%" alt="04 — Horovista: personalised Vedic astrology that turns a birth chart into a 14-chapter digital book. Live at horovista.com"></a>

**My own product and business.** Horovista turns a birth date, time and place into a personalised North Indian Vedic astrology **book** — read online or as a PDF, in English or Hindi. I designed, built and run it, and as a part-time astrologer I review the readings myself.

<details>
<summary><b>Case study</b> · from birth data to a personal book</summary>
<br>

<table>
  <tr>
    <td width="36%" valign="top"><sub><b>THE BOOK</b></sub><br>14 chapters<br>Dasha life timeline<br>Lal Kitab reading &amp; remedies<br>Gemstone guidance<br>3D page-turn reader<br>Standard + 8 designed editions</td>
    <td width="32%" valign="top"><sub><b>FREE TOOLS</b></sub><br>Daily horoscope<br>Panchang by city<br>Festival calendar · good-days finder<br>Moon sign · Kundli Milan<br>Lo Shu grid · planets · journal</td>
    <td width="32%" valign="top"><sub><b>BUSINESS</b></sub><br>Paid reports &amp; full book<br>Checkout with discount codes<br>Email sign-in, private charts<br>English / हिंदी<br>Add-to-home-screen web app</td>
  </tr>
</table>

- **Deterministic domain computation** — charts, Dasha periods, Panchang and matching must be reproducible from date, time and location.
- **Personalised content at scale** — every reading assembles into a two-language, 14-chapter book with a page-turn reader and PDF export.
- **Responsible scope** — no predictions of death or lifespan; no medical, legal or investment instructions.
- **Ask-your-book** — readers can ask their book questions. <!-- CONFIRM: AI-assisted? If yes, describe the approach. -->

<sub>Stack observed on the live site: Next.js · Cloudflare Turnstile · first-party analytics + Google Analytics with consent.</sub>

</details>

<br>

<!-- ─────────────── 05 GENUINE ─────────────── -->

<a name="genuine-consultancy-services"></a>
<a href="https://genuineconsultancyservices.com"><img src="./assets/projects/genuine-consultancy.svg" width="100%" alt="05 — Genuine Consultancy Services: client-facing business website. Live at genuineconsultancyservices.com"></a>

**Genuine Consultancy Services** — a deployed, client-facing business website that takes a visitor from positioning to services to enquiry. **My role:** Forward Deployed Engineer.

<!-- CONFIRM: services, page structure, contact workflow and stack — the site blocks automated readers, so none of this was verified. -->

<br>

<!-- ═══════════════════════════════ 02 ═══════════════════════════════ -->

<a name="product-explorations"></a>
<img src="./assets/sections/section-02.svg" width="100%" alt="02 — Product Explorations">

<img src="./assets/projects/ai-systems.svg" width="100%" alt="R&D — AI Assistants & Agents: LLM integration, RAG, tool calling, multi-step workflows, intelligent reporting, local and cloud models">

Ongoing R&D — not a released product. LLM integration · RAG and embedding pipelines · tool calling · multi-step agent workflows · contextual assistants · intelligent reporting · local (Ollama) and cloud model experimentation.

<br>

<!-- ═══════════════════════════════ 03 ═══════════════════════════════ -->

<a name="engineering-in-practice"></a>
<img src="./assets/sections/section-03.svg" width="100%" alt="03 — Engineering in Practice">

<img src="./assets/matrix.svg" width="100%" alt="Capability by product evidence matrix: verified on the live product, stated pending verification, or R&D">

<details>
<summary><b>Application Engineering</b> — frontend, backend, APIs, data, authentication</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| Role-based access, per-request authorisation | Edqio — six roles, every request checked |
| Authenticated accounts & portals | Horovista sign-in · Smile sign-in & registration · Redwan client portal |
| Multi-language product | Horovista — English and Hindi |
| Production web frontends | Edqio · Redwan · Smile · Horovista |

</details>

<details>
<summary><b>Fintech & Financial Applications</b> — payments, financial workflows, controls</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| Invoicing, payments, receipts, balances | Edqio — fee management |
| Maker–checker approvals, audit trail | Edqio — principal sign-off, separation of duties |
| Paid products and checkout | Horovista — paid reports, discount codes |

</details>

<details>
<summary><b>Education & Institutional Software</b> — administration and organisational workflows</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| School administration end to end | Edqio |
| Verifiable documents | Edqio — QR-verified report cards |
| Institutional platforms | Smile Medical Hospital · Redwan HydroGeology |
| Business web presence | Genuine Consultancy Services |

</details>

<details>
<summary><b>Scientific & Specialised Applications</b> — domain-specific software</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| Geospatial & terrain visualisation | Redwan — 3D terrain from SRTM, elevation profiles, project map |
| Scientific diagrams | Redwan — groundwater cross-section and rotatable block model |
| Deterministic domain calculations | Horovista — charts, Dasha timelines, Panchang, matching |

</details>

<details>
<summary><b>AI & Intelligent Systems</b> — LLMs, RAG, assistants, tool calling</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| Q&amp;A over personal content | Horovista — ask-your-book (approach to be documented) |
| RAG, tool calling, agents, reporting | AI R&amp;D lab |
| Local and cloud model serving | Ollama and cloud API experiments |

</details>

<details>
<summary><b>Infrastructure & Delivery</b> — hosting, delivery, protection</summary>
<br>

| Capability | Evidence |
| :-- | :-- |
| Five products in production | Edqio · Redwan · Smile · Horovista · Genuine |
| Edge hosting & media delivery | Smile — Vercel, Cloudinary |
| Bot protection | Smile and Horovista — Cloudflare Turnstile |
| Analytics with consent | Horovista |

</details>

<br>

<!-- ═══════════════════════════════ 04 ═══════════════════════════════ -->

<a name="technology-stack"></a>
<img src="./assets/sections/section-04.svg" width="100%" alt="04 — Technology Stack">

| Layer | Tools | Where it shows up |
| :-- | :-- | :-- |
| **Frontend** | <img src="https://skillicons.dev/icons?i=react,nextjs,redux,tailwind,sass,vite&theme=dark" height="34" alt="React, Next.js, Redux, Tailwind, Sass, Vite"> | Edqio · Redwan · Smile · Horovista (Next.js observed) · PWA, SSR/ISR, component systems |
| **Backend & APIs** | <img src="https://skillicons.dev/icons?i=nodejs,express,rails,django,graphql,postman&theme=dark" height="34" alt="Node.js, Express, Rails, Django, GraphQL, Postman"> | REST services, service layers, RBAC/JWT, rate limiting |
| **Data** | <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis&theme=dark" height="34" alt="PostgreSQL, MongoDB, Redis"> | Relational & document stores, caching, indexing |
| **AI** | <img src="https://skillicons.dev/icons?i=python,openai&theme=dark" height="34" alt="Python, OpenAI"> | LLMs, RAG, embeddings, vector DBs (Pinecone, Weaviate, pgvector), Ollama, OpenClaw |
| **Desktop** | <img src="https://skillicons.dev/icons?i=tauri,rust&theme=dark" height="34" alt="Tauri, Rust"> | Cross-platform desktop exploration |
| **Infrastructure** | <img src="https://skillicons.dev/icons?i=aws,docker,githubactions,vercel,netlify,cloudflare&theme=dark" height="34" alt="AWS, Docker, GitHub Actions, Vercel, Netlify, Cloudflare"> | Smile on Vercel · Turnstile on Smile and Horovista · Docker, CI/CD |
| **Embedded** | <img src="https://skillicons.dev/icons?i=c,cpp,arduino,raspberrypi&theme=dark" height="34" alt="C, C++, Arduino, Raspberry Pi"> | Firmware, sensor-to-cloud, hardware-to-API — my ECE roots |

<br>

<!-- ═══════════════════════════════ 05 ═══════════════════════════════ -->

<a name="architecture"></a>
<img src="./assets/sections/section-05.svg" width="100%" alt="05 — Architecture">

<img src="./assets/architecture.svg" width="100%" alt="Reference architecture: experience, edge, application, intelligence and data layers">

<details>
<summary><b>Same blueprint as a Mermaid diagram</b></summary>
<br>

```mermaid
flowchart LR
    subgraph EXP["Experience"]
        W["Web · PWA"]
        D["Desktop · Tauri"]
    end
    subgraph EDGE["Edge"]
        G["Auth · RBAC · rate limits · bot protection"]
    end
    subgraph APP["Application"]
        S["Domain services · approvals · audit"]
        J["Jobs · PDFs · notifications"]
    end
    subgraph AI["Intelligence"]
        O["Agent orchestration"]
        V["Retrieval · embeddings"]
    end
    subgraph DATA["Data"]
        P[("PostgreSQL / MongoDB")]
        R[("Redis")]
        F[("Object storage")]
    end
    W --> G
    D --> G
    G --> S
    S --> J
    S --> O
    O --> V
    S --> P
    S --> R
    J --> F
    V --> P
```

</details>

<br>

<!-- ═══════════════════════════════ 06 ═══════════════════════════════ -->

<a name="community"></a>
<img src="./assets/sections/section-06.svg" width="100%" alt="06 — Community">

<img src="./assets/impact.svg" width="100%" alt="Community impact: 100+ developers, top 40 global mentor, 1,000+ projects reviewed, 100+ engineers helped, 50+ web applications, 10+ IoT systems, 5,000+ contributions">

<table>
  <tr>
    <td width="50%" align="center"><img src="./profile.png" width="100%" alt="Frontend Mentor profile"><br><sub><b>Frontend Mentor performance</b></sub></td>
    <td width="50%" align="center"><img src="./progress-report.png" width="100%" alt="Learning progress"><br><sub><b>Continuous learning</b></sub></td>
  </tr>
</table>

<p align="center">
  <img src="./motm-1.webp" width="72" alt="Frontend Mentor — Mentor of the Month">
  <img src="./motw-1.webp" width="72" alt="Frontend Mentor — Mentor of the Week">
  <img src="./motw-2.webp" width="72" alt="Frontend Mentor — Mentor of the Week">
  <img src="./motw-3.webp" width="72" alt="Frontend Mentor — Mentor of the Week">
</p>

<br>

<!-- ═══════════════════════════════ 07 ═══════════════════════════════ -->

<a name="github-activity"></a>
<img src="./assets/sections/section-07.svg" width="100%" alt="07 — GitHub Activity">

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=skyv26&show_icons=true&count_private=true&include_all_commits=true&bg_color=0d0c12&title_color=E76F36&text_color=c9c6d3&icon_color=FF4D8D&border_color=2a2633&border_radius=16" width="49%" alt="GitHub stats">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=skyv26&layout=compact&langs_count=8&bg_color=0d0c12&title_color=E76F36&text_color=c9c6d3&border_color=2a2633&border_radius=16" width="49%" alt="Top languages">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=skyv26&background=0D0C12&border=2A2633&stroke=2A2633&ring=E76F36&fire=FF4D8D&currStreakLabel=E76F36&sideLabels=C9C6D3&currStreakNum=F5F3EE&sideNums=F5F3EE&dates=A9A6B5&border_radius=16" width="100%" alt="Contribution streak">
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=skyv26&bg_color=0d0c12&color=c9c6d3&line=E76F36&point=FF4D8D&area=true&area_color=8B5CF6&hide_border=false&radius=16" width="100%" alt="Contribution activity graph">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/skyv26/skyv26/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Contribution snake">
</p>

<br>

<!-- ═══════════════════════════════ 08 ═══════════════════════════════ -->

<a name="writing"></a>
<img src="./assets/sections/section-08.svg" width="100%" alt="08 — Writing">

| Essay | Theme |
| :-- | :-- |
| [**The Clockmaker's Dilemma**](https://skybrel.medium.com/the-clockmakers-dilemma-a-story-about-humans-in-the-age-of-ai-6133366a73fa) | Preserving humanity in automated systems |
| [**Friend or Foe?**](https://skybrel.medium.com/friend-or-foe-the-invisible-game-of-technology-c06987e6c2ac) | The hidden influence of technology |
| [**The Happy Developer**](https://skybrel.medium.com/how-to-be-the-happiest-software-developer-bcae8a663ca6) | Sustainable fulfilment in engineering |

<p align="center"><a href="https://skybrel.medium.com/"><img src="https://img.shields.io/badge/Read_the_full_archive-0d0c12?style=for-the-badge&logo=medium&logoColor=E76F36" alt="Full archive on Medium"></a></p>

<br>

<!-- ═══════════════════════════════ 09 ═══════════════════════════════ -->

<a name="creative-work"></a>
<img src="./assets/sections/section-09.svg" width="100%" alt="09 — Creative Work">

<a href="https://open.spotify.com/artist/2dGQpFvIvy3tANrmozUd1n"><img src="./assets/music.svg" width="100%" alt="skybrel — latest release 3 AM (2026)"></a>

<p align="center">
  <a href="https://open.spotify.com/artist/2dGQpFvIvy3tANrmozUd1n"><img src="https://img.shields.io/badge/Spotify-0d0c12?style=for-the-badge&logo=spotify&logoColor=1DB954" alt="Spotify"></a>
  <a href="https://www.youtube.com/@skybrel"><img src="https://img.shields.io/badge/YouTube-0d0c12?style=for-the-badge&logo=youtube&logoColor=FF0000" alt="YouTube"></a>
  <a href="https://push.fm/fl/bhyf4zmq"><img src="https://img.shields.io/badge/Listen_everywhere-0d0c12?style=for-the-badge&logo=applemusic&logoColor=FF4D8D" alt="Listen everywhere"></a>
  <a href="https://merch-studio.musixmatch.com/product/3504d0f9-0867-4acd-904a-9be5acd2c36c?source=embed"><img src="https://img.shields.io/badge/Merch-0d0c12?style=for-the-badge&logo=musixmatch&logoColor=E76F36" alt="Merch on Musixmatch Studio"></a>
  <a href="https://ko-fi.com/skybrel"><img src="https://img.shields.io/badge/Ko--fi-0d0c12?style=for-the-badge&logo=ko-fi&logoColor=FF5E5B" alt="Support on Ko-fi"></a>
</p>

<br>

<!-- ═══════════════════════════════ 10 ═══════════════════════════════ -->

<a name="contact"></a>
<img src="./assets/sections/section-10.svg" width="100%" alt="10 — Contact">

<p align="center"><b>Building something that has to work in the real world? Let's talk.</b></p>

<p align="center">
  <a href="mailto:dev.aakashv@gmail.com"><img src="https://img.shields.io/badge/Email-E76F36?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/skyv2022/"><img src="https://img.shields.io/badge/LinkedIn-0d0c12?style=for-the-badge&logo=linkedin&logoColor=0A66C2" alt="LinkedIn"></a>
  <a href="https://skybrel.medium.com/"><img src="https://img.shields.io/badge/Medium-0d0c12?style=for-the-badge&logo=medium&logoColor=white" alt="Medium"></a>
  <a href="https://twitter.com/devaakashv"><img src="https://img.shields.io/badge/X-0d0c12?style=for-the-badge&logo=x&logoColor=white" alt="X / Twitter"></a>
  <a href="https://www.frontendmentor.io/profile/skyv26"><img src="https://img.shields.io/badge/Frontend_Mentor-0d0c12?style=for-the-badge&logo=frontendmentor&logoColor=3F54A3" alt="Frontend Mentor"></a>
  <a href="https://horovista.com"><img src="https://img.shields.io/badge/Horovista-0d0c12?style=for-the-badge&logoColor=white" alt="Horovista"></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=skyv26&style=for-the-badge&color=E76F36&label=PROFILE+VIEWS" alt="Profile views">
</p>

<a href="#top"><img src="./assets/footer.svg" width="100%" alt="Systems with purpose — back to top"></a>
