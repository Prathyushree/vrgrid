# SIH 2026 — Hardest Problems & Low-Competition Problems, Domain by Domain

**Data:** all 226 published PS (172 Software / 54 Hardware, 30 organisations), snapshot 21 Aug 2026, sourced from sih.gov.in (CC BY 4.0) via the open mirror.
**Idea submission deadline:** 20 September 2026. Cap is 500 ideas per PS.

**Two caveats before you use this:**

1. The `Theme` field on the portal this year is badly mis-tagged — "Explainable AI for Diabetic Retinopathy" is filed under *Clean & Green Technology*, "Smart Scan for Electronic Warfare" under the same, "onion grading" under *Fitness & Sports*. **Do not filter by theme.** The grouping below is by actual subject matter.
2. At snapshot time every PS showed `0/500` ideas, so "nobody will take this" is my inference from barriers-to-entry, not from live counts. Re-check live counts on the portal before you lock in — that number is the single best signal you'll get.

**Hard ≠ unpopular.** They're different axes and you want the overlap:

| | Popular | Unpopular |
|---|---|---|
| **Easy** | Death zone. 300 teams, identical demo. | Boring but winnable. |
| **Hard** | Prestige trap (ISRO, DRDO). Still crowded. | **← This is where you want to be.** |

Only 42 of 226 PS ship a dataset link. For the other 184, "where does the data come from" is the question that kills most teams at the finale, and it's the question judges ask first.

---

## A. Weather, Climate & Atmospheric Science — MoES/IMD (~20 PS)

The single biggest cluster this year. MoES alone posted 30 PS.

**Hardest**
- **SIH26081 — Hybrid AI-NWP Multi-Model Forecast Blending System.** You're being asked to blend numerical weather prediction model outputs with learned corrections. This is an active research area at ECMWF-scale institutions. Doing it credibly needs GRIB/NetCDF handling, multi-model reanalysis data, and skill-score validation you probably can't do in 36 hours.
- **SIH26084 — Convective-scale nowcasting for thunderstorms, hail & cloudbursts (0–6 hr).** Convective initiation is genuinely unsolved. Radar + satellite fusion at convective scale, with an evaluation metric that punishes false alarms.
- **SIH26079 — AI-based Forecast Bust Detection for medium-range forecasts.** Meta-forecasting: predicting when the forecast will fail. Requires long forecast-verification archives most teams cannot obtain.
- **SIH26085 — Urban Flood Nowcasting (drainage + rainfall coupling).** Needs municipal storm-drain network data, which effectively does not exist in usable digital form for most Indian cities.

**Lowest competition**
- **SIH26073 — Anomaly detection for Automatic Weather Stations.** Unglamorous sensor-QC work. No pretty demo. But it's a well-scoped, tractable ML problem with a clear success metric, and IMD actually needs it. Strong sleeper.
- **SIH26076 — Personalised homepage for the 'Mausam' mobile app.** Looks trivial, so ambitious teams skip it and weak teams feel it's beneath a "hackathon". Real UX product problem with a live user base.
- **SIH26080 — Regime-aware AI post-processing of monsoon rainfall forecasts.** "Regime-aware" filters out ~95% of teams instantly because they don't know what a monsoon regime is.

---

## B. Ocean, Polar & Underwater Systems — MoES (~10 PS)

**This is the most under-contested domain in the entire hackathon.** Antarctic/deep-ocean instrumentation has almost no student pipeline in India.

**Hardest**
- **SIH26058 — Low-power real-time adaptive software-defined sonar transmitter payload for AUVs (Hardware).** Adaptive LFM chirp synthesis that retunes frequency/bandwidth to water turbidity, salinity and depth in real time, on a power budget. This is the hardest hardware PS on the board that isn't classified. You need acoustics, SDR, embedded DSP and a water tank.
- **SIH26064 — Low-cost deployable seafloor metal detection sensor (Hardware).** Detect polymetallic nodules and hydrothermal sulphides from a ship-deployed bottom sensor. Marine EM geophysics. Approximately zero undergraduate teams in India can validate this.
- **SIH26065 — Autonomous low-cost ocean observation platform for polar/Southern Ocean (Hardware).** Long-duration deployment in the worst environment on Earth. Materials, power, biofouling, satellite backhaul.
- **SIH26066 — OceanEmbed: satellite-embedding deep learning to reconstruct subsurface ocean temperature.** Inferring the 3D water column from 2D surface observations. Physically ill-posed; needs Argo float data.

**Lowest competition (and genuinely winnable)**
- **SIH26062 — Integrated Polar Expedition Logistics & Asset Management System.** It is inventory-and-scheduling software. Ordinary CRUD skills, extraordinary novelty framing — you're building for Bharati and Maitri stations. Almost nobody picks it because it sounds boring. It is the highest reach-the-finale-per-unit-effort PS on the entire list.
- **SIH26063 — Polar Science Outreach, Knowledge Repository & Media Portal.** Same logic. A content platform, dressed in Antarctica.
- **SIH26060 — Digital platform for remote management of Indian Antarctic Research Stations.** Constraint that makes it interesting: intermittent, very-low-bandwidth satellite link. Offline-first sync is a real engineering story.
- **SIH26057 — Marine debris detection from side-scan sonar imagery.** Sonar imagery is not RGB. Most CV teams take one look at a waterfall image and leave.

---

## C. Space & Remote Sensing — ISRO (11) + NTRO geospatial (5)

Crowded for prestige reasons despite being hard. Every college wants "ISRO" on the PPT.

**Hardest**
- **SIH26166 — Sun-angle and scale-invariant multi-modal image correspondence across Chandrayaan-2 OHRC / TMC-2 / IIRS.** Cross-sensor lunar image registration under wildly varying illumination, with no atmosphere, no vegetation and no texture priors. Classical feature matching fails; learned matching has no lunar training set. Dataset is marked TBD. This is the hardest software PS published this year.
- **SIH26169 — AI virtual camera tracking for coarse alignment of mobile Free-Space Optical Communication terminals.** Laser comms link acquisition on a moving platform. Milliradian pointing budgets.
- **SIH26168 — AI/ML intelligent dead-reckoning for seamless navigation.** Inertial drift correction without GNSS. Sounds approachable, is not.
- **SIH26142 (NTRO) — Deep-learning super-resolution mapping from medium-resolution satellite imagery.** Super-resolution that must remain *geometrically truthful*. Hallucinating a road is a failure, not a feature — and demonstrating that you haven't hallucinated is the whole problem.

**Lowest competition**
- **SIH26170 — AI anomaly detection in component burn-in & screening.** Semiconductor reliability testing. Zero glamour, ISRO badge, tabular time-series data. Very few takers.
- **SIH26174 — AI human activity recognition for on-board BAS experiments.** Niche enough that most teams won't understand the setup.
- **SIH26176 — ORCA: marine ecosystem reasoning with collaborative agents.** Sits awkwardly between ISRO, marine biology and agent frameworks — the ambiguity scares people off.

---

## D. Cybersecurity & Digital Forensics — NTRO (23) + AICTE (3)

NTRO is the second-largest poster and the most technically serious. Most PS here have no dataset, no contact, and terse descriptions.

**Hardest**
- **SIH26151 — Dark web threat actor de-anonymization.** Correlating Tor hidden-service footprints across marketplaces and forums to real-world identities. Legally fraught, ethically loaded, and the ground truth is unobtainable. You cannot validate your own system. Almost certainly the highest-risk PS on the board.
- **SIH26148 — 'JOCKY': new cross-platform programming language + compiler for forensic scripting that doesn't trip AV heuristics.** You are being asked to write a language and a compiler in 36 hours, with an evasion property as the acceptance criterion. Read this one carefully and think hard about what you're building before you commit.
- **SIH26147 — Automated analysis of .IQ and .wav files with signal parameter extraction.** RF baseband I/Q demodulation and blind parameter estimation. Requires SDR/comms theory that a CS syllabus does not cover.
- **SIH26150 — Multi-vendor DVR/NVR forensic analysis tool.** Reverse-engineering proprietary, undocumented filesystems from a dozen CCTV manufacturers. Pure grind, no shortcuts, no AI to hide behind.
- **SIH26164 — Enterprise Cryptographic Discovery & Analysis Tool.** Inventorying crypto usage across a heterogeneous estate — practically a post-quantum migration readiness tool.

**Lowest competition**
- **SIH26156 — Universal Log Pre-processing Framework.** Log normalisation. Sounds like homework. It's actually the thing every SOC needs and nobody builds well, and it's very demoable.
- **SIH26157 — Supervisory Analytics Tool for SOC Assessment (SAT-SA).** Vague title + unfamiliar acronym = instant skip by most teams.
- **SIH26163 — Security assessment of the World Monitor application.** Requires access to a specific NTRO application. Most teams assume they can't get it and move on.
- **SIH26159 / SIH26160 — Email cryptographic posture assessment / IPsec VPN protocol analyzer.** Protocol-level work with a hard correctness bar but a genuinely narrow, achievable scope. Underrated.

---

## E. Cryptocurrency & Financial Crime — MHA (4)

**Hardest**
- **SIH26182 — Automated attribution of unknown crypto wallets to the nearest VASP.** Graph heuristics on chain data, essentially rebuilding a slice of Chainalysis. Doable in principle, but "nearest VASP" ground truth is proprietary.
- **SIH26184 — Predictive analytics to forecast likely cash withdrawal locations from cybercrime complaints.** Needs real NCRP complaint data you will not have. You'll be building on synthetic data and judges will notice.

**Lowest competition**
- **SIH26183 — Real-time identification of fraud-linked exchanges from victim-reported wallet addresses.** Narrower and more tractable than 26182, and gets picked less because the title reads similar.

---

## F. Defence & Strategic Hardware — MoD, DRDO, BEL, MHA/NSG

**Hardest — and honestly, hardest on the board**
- **SIH26098 — Low-cost precision guidance kit with canard actuation and multi-mode electronic fuze for a 155 mm artillery shell (Hardware, MoD).** Guidance, navigation and control hardware that survives ~15,000 g setback shock, spin-stabilised, at a price point that beats existing PGKs. The only MoD PS this year. You cannot build or test this — you can only simulate and present a design. Consider it a design-competition PS, not a build PS.
- **SIH26050 — High-altitude performance optimization of anti-drone systems (Hardware, DRDO).** Environmental qualification engineering across RF, EO, mechanical and power subsystems at Ladakh conditions. No student team owns a climatic chamber.
- **SIH26185 — Helmet-mounted conformal antenna for urban CQB (Hardware, MHA/NSG).** Antenna design on a curved lossy surface next to a human head, in concrete-heavy multipath. Needs HFSS/CST and ideally an anechoic chamber. Extremely few teams have both the tooling and the RF fundamentals.
- **SIH26055 — Smart scan strategy for Electronic Warfare (DRDO).** RL-based receiver scheduling against frequency-agile emitters, with intercept-probability figures of merit. A synthetic radar dataset is provided, which makes it more tractable than it looks — but you must understand ES receiver theory first.
- **SIH26054 — Real-time digital twin for aero piston engines on MALE UAVs (DRDO).**

**Lowest competition**
- **SIH26049 — Reliability/lifespan modifications for electronics at sub-zero, low-pressure Ladakh conditions (Hardware).** The title is a 40-word paragraph. That alone kills its pickup rate. It's a materials-and-derating engineering study — very few teams, and a real problem.
- **SIH26051 — Software model for area-specific shelter thermal comfort design.** Building physics / thermal simulation. Sits in nobody's comfort zone: not CS, not quite mech.
- **SIH26052 — AI/ML adaptive noise cancellation for defence noise on embedded hardware.** Real-time DSP on an MCU. Impulsive noise (gunfire, rotor) breaks standard ANC. Hard, but scoped, and unfashionable enough to be quiet.

---

## G. Robotics, Drones & Autonomous Systems (~10)

**Hardest**
- **SIH26037 — Adaptive path planning and collision avoidance for autonomous vehicles on *unstructured Indian roads* (MathWorks).** "Unstructured Indian roads" is where every published AV planner falls over. MATLAB/Simulink toolchain requirement narrows the field further.
- **SIH26026 — Quadruped/handheld real-time narcotics and explosives detection for Indian Railways (Hardware).** You need a trace-detection sensor — IMS, or a validated e-nose array. The sensing physics, not the robot, is the wall. And you cannot legally obtain positive test samples.
- **SIH26158 — Single-pass drone video → accurate 3D model (NTRO).** "Single-pass" is the killer constraint: no loop closure, no multi-orbit overlap. Photogrammetry pipelines assume the opposite.
- **SIH26123 — Edge-AI distributed fleet coordination for AMRs (BEL).** Multi-agent coordination with no central planner, on edge compute.

**Lowest competition**
- **SIH26053 — Adaptive variable-resolution 2.5D LiDAR mapping (DRDO).** "2.5D" confuses people. It's a well-defined representation problem with a clear win condition.
- **SIH26126 — Vision-based autonomous navigation for outdoor UGV (BEL).** Loses teams to the flashier Qualcomm drone PS despite being more achievable.

---

## H. Mining, Metals, Coal, Oil & Gas (~18)

Industrial domain knowledge is the moat here. Very low pickup outside a handful of colleges.

**Hardest**
- **SIH26119 — Indigenous GPU-accelerated optimization solver: a sovereign alternative to CPLEX/Gurobi/Xpress (MRPL).** You are being asked to write a competitive MILP solver. Branch-and-cut, presolve, simplex/barrier, GPU-parallel — this is a decade of PhD work at IBM and Gurobi. Benchmarks are public (MIPLIB, Netlib, Mittelmann), so your gap will be measurable and large. **Do not pick this expecting to win on completeness.** Pick it only if you have a genuinely novel angle on one sub-problem (e.g. GPU-parallel cut generation) and can present it honestly as such.
- **SIH26120 — Digital twin for cyclic steam stimulation + sucker-rod pump optimization, Baghewala heavy oil field (Oil India).** Multiphase reservoir thermodynamics plus rod-pump dynamics. Needs petroleum engineering, not just ML.
- **SIH26117 — Sovereign on-premise agentic AI workbench on open-weight multimodal LLMs for confidential industrial work (MRPL).** Air-gapped agentic system with real security guarantees. The hard part is not the agent loop, it's the isolation and audit story.
- **SIH26025 — AI-enabled low-cost real-time mine subsidence monitoring & early warning (Hardware, Coal).** InSAR or GNSS/tiltmeter arrays at low cost. Geotechnical validation impossible in a hackathon.
- **SIH26009 — AI/ML + space tech to identify manganese reserves (Steel).** Mineral prospectivity mapping from hyperspectral/geophysical data. Real geology required.

**Lowest competition**
- **SIH26008 — Conveyor belt joint rupture detection in iron ore mining (Hardware, Steel).** Vibration/vision-based predictive maintenance. Genuinely tractable. Almost nobody picks it because "conveyor belt" doesn't sound like a hackathon.
- **SIH26007 — Safe operation of mine vehicles in fog / low visibility (Hardware, Steel).** Thermal + radar sensor fusion. Concrete, demoable, and quiet.
- **SIH26122 — Intelligent data capture & schedule-linking for infrastructure project progress (Oil India).** Construction-tech. Deeply unfashionable, real problem.
- **SIH26099 — AI-driven standardization of material codes across CPSEs (MoPNG).** Entity resolution on messy procurement catalogues. Boring name, extremely solvable, immediate operational value. Strong sleeper pick.

---

## I. Land Records & Geospatial Governance — MoRD (10)

Ten PS, all interlocking, all requiring you to understand ULPIN, cadastral survey and the SVAMITVA scheme. Domain barrier is high; competition is correspondingly low.

**Hardest**
- **SIH26011 — 3D ULPIN generation and vertical property mapping.** Extending a 2D parcel identifier system into the vertical dimension for apartments — this is an unsolved *policy plus data model* problem, not just a coding one. Nobody has done this in India at scale.
- **SIH26010 — Survey/resurvey of rural agricultural land in India (Hardware).** National-scale cadastral resurvey. Needs RTK GNSS or drone photogrammetry at survey-grade accuracy.
- **SIH26013 — Automated harmonization of multi-source geospatial data for urban land records.** Conflating cadastral maps, satellite imagery and revenue records that disagree with each other by design.

**Lowest competition**
- **SIH26017 — Predictive analytics for early detection of land acquisition delays.** A tabular ML problem wrapped in an intimidating governance context. Very few takers.
- **SIH26019 — National digital platform for land governance research and evidence-based policy.** Reads like a portal. It is a portal. Nobody wants it. It will reach the finale with a competent team.

---

## J. Health, MedTech & Ayush (~12)

The most crowded *category* overall — but the specific PS below are not.

**Hardest**
- **SIH26038 — Explainable AI for Diabetic Retinopathy screening (MathWorks).** Explicit numeric bar: >90% sensitivity, >85% specificity for referable DR, plus sub-pixel microaneurysm detection, plus Grad-CAM explainability, plus a Simulink throughput model. Four public datasets are provided (APTOS, IDRiD, DRIVE, Messidor-2) so you *can* validate — which is exactly why the bar is unforgiving. Best-specified PS on the whole board.
- **SIH26139 — Hybrid quantum machine learning for early disease detection (Egreen Quanta).** QML has no demonstrated advantage on clinical tabular data. You'd be building something you cannot honestly claim beats a gradient-boosted tree.
- **SIH26048 — iKwath: pod-based smart Kwatha maker (Hardware, Ayush).** A countertop appliance that performs pharmacopoeia-compliant decoction with controlled reduction ratios. Food-engineering hardware plus AFI/API standards compliance. Genuinely hard and completely unlike anything on the rest of the list.
- **SIH26113 — Human augmentation technologies (Hardware, Autodesk).** Scope is essentially unbounded, which is its own difficulty.

**Lowest competition**
- **SIH26047 — Patient case-taking software (Ayush).** Sounds like a CRUD form. Ayurvedic case-taking is genuinely structured differently from allopathic intake, which makes it an interesting data-model problem hiding behind a dull title.
- **SIH26046 — AIIA clinical trials dashboard (GCP-compliant CTMS).** "GCP-compliant" scares teams off. It's regulatory reading, not technical difficulty.
- **SIH26004 — AI-assisted early detection of osteoarthritis risk markers in NER (Hardware).** NER-specific health PS get very few teams.

---

## K. Agriculture, Dairy & Food (~12)

**Hardest**
- **SIH26109 — AI predictive modelling for early forecasting of bovine mastitis (Hardware, Fisheries/AH&D).** Predicting subclinical mastitis before somatic cell count rises. Needs longitudinal per-animal data from real dairy farms. Data acquisition is the whole problem.
- **SIH26111 — Rapid AI feed and silage quality testing (Fisheries/AH&D).** Effectively NIR spectroscopy chemometrics. Needs calibration against lab assays.
- **SIH26110 — Low-cost lightweight milk chilling can (Hardware).** Passive or low-power cooling that holds milk safe for hours, food-grade, cheap, and light enough to carry on a hill road. This is a hard thermodynamics-plus-cost-engineering problem disguised as a simple product.

**Lowest competition**
- **SIH26031 — Objective quality assessment and grading of onions.** Onion grading. Nobody's PPT dream. Clean CV problem with a real procurement use case.
- **SIH26021 — Honey Chain: blockchain traceability + smart beekeeping (MSME).** Beekeeping domain knowledge required. Very few takers.
- **SIH26005 — Solar-powered smart mini cold storage for NER vegetables (Hardware).** Same physics as 26110, same low pickup.

---

## L. Standards, Metrology & Test Automation — Consumer Affairs / BIS (10)

**The most systematically avoided domain on the board.** Every PS here requires reading an IS or IEC standard first. That single step eliminates most teams.

**Hardest**
- **SIH26029 — Automated high-current short-circuit test system for IEC 60898-1 MCB compliance (Hardware).** Generating and precisely controlling fault currents up to **10,000 A** with defined R and X_L. This is high-power lab equipment. You physically cannot prototype it as a student — you can only design and simulate it. Highest infrastructure barrier of any PS this year.
- **SIH26030 — Automated cable specimen preparation system for IS 10810 / IS 7098 (Hardware).** Mechanised cutting, straightening, slicing and dumbbell-shaping of PVC/XLPE/HDPE cable to standards tolerance. Real mechatronics.

**Lowest competition (and very winnable)**
- **SIH26035 — Software for generating test reports for non-automatic weighing instruments.** It's a form-and-report generator. It will get a handful of teams. A polished submission stands out enormously.
- **SIH26036 — Online verification system for weighing and measuring instruments.**
- **SIH26034 — Compliance checker for Legal Metrology (Packaged Commodities) Rules.** Rules-as-code. Tedious, tractable, and almost nobody will read the rules.
- **SIH26108 — Recommendation engine for applicable Indian Standards in procurement specs.** A retrieval problem over a well-defined corpus. Unsexy, very doable.

---

## M. MSME & Rural Livelihood Hardware (2)

Both are pure product-design problems with no AI hook, which is exactly why they'll be near-empty.

- **SIH26020 — Innovative hand-spinning equipment for Khadi artisans (Hardware).** Ergonomics, mechanism design, cost. Hard in a way engineering students are rarely trained for: you must actually improve on the New Model Charkha, and any real improvement has to be validated with artisans. Judges reward this heavily when done well.
- **SIH26022 — Solar-powered drying and packaging system for home-based agarbatti making (Hardware).** Thermal design plus humidity control plus a packaging mechanism, at rural-household price points.

---

## N. Education & Skilling (~8)

Mostly crowded and generic. Two exceptions.

**Hardest**
- **SIH26042 — Vernacular pedagogy and real-time translation for mother-tongue primary education (Jharkhand).** The target languages are tribal languages of Jharkhand — Santali, Ho, Mundari, Kurukh. These are genuinely low-resource: minimal parallel corpora, and Santali uses Ol Chiki script. Off-the-shelf translation APIs will not save you. Very hard, very few teams, very high impact.

**Lowest competition**
- **SIH26075 — 'CAPACITY CONNECT' LMS portal (MoES).** It is an LMS. Everyone knows it's an LMS. It will be nearly empty.
- **SIH26101 — AI learning platform for competency gap identification (MoSPI).**

---

## O. Governance & Citizen Platforms (~20)

Maharashtra, Jharkhand, MoSJE, MoSPI, Cooperation. Titles here are often written as a *problem sentence* rather than a solution brief — vague, which cuts both ways.

**Hardest**
- **SIH26129 — Interoperability across fragmented government digital platforms (Maharashtra).** This is an organisational problem being handed to students as a technical one. You cannot solve it; you can only demonstrate a credible integration layer. Judge it accordingly.
- **SIH26102 — Detecting anomalies, fraud and inefficiencies in MPLAD scheme implementation (MoSPI).** Fraud detection with no labelled fraud.
- **SIH26191 — Hazard-based red zones, carrying capacity assessment and relocation needs (MHA).** Carrying capacity is a contested concept with no agreed formula.

**Lowest competition**
- **SIH26056 — Real-time airfare price index via automated scraping for CPI augmentation (MoSPI).** A statistical index construction problem — Laspeyres/chained indices, sampling design — sitting behind a scraper. Very few teams will realise the index methodology *is* the deliverable. Excellent quiet pick.
- **SIH26095 — Smart real-time monitoring & inspection mobile app (MoSJE).** Generic-sounding, ministry-specific context.
- **SIH26089 — Cooperative gig services platform (Ministry of Cooperation).** Everyone assumes "another Urban Company clone" and skips it.

---

## P. Railways & Urban Transport (~8)

**Hardest**
- **SIH26027 — AI-powered automatic block planning to maximise asset availability on Indian Railways.** Maintenance block scheduling is a large constrained combinatorial optimisation over a live network, with safety constraints. Real operations research, and IR's actual timetable data is not public.
- **SIH26028 — Dynamic ETA forecasting for coaching trains.** Sounds easy. Indian Railways delay propagation is a network-cascade problem; naive regression will look fine on a demo and fail every judge question.
- **SIH26127 — City-wide multi-camera ANPR trajectory tracking (BEL).** Re-identification across non-overlapping cameras with Indian plate formats and poor camera quality.

---

## Q. Quantum-Inspired — Egreen Quanta (5)

Worth calling out as a block. **SIH26137–SIH26141.** "Quantum-inspired" here mostly means metaheuristics, not quantum hardware. These will get low pickup because the word "quantum" intimidates, and that makes them tactically attractive — but be careful: judges who know quantum computing will ask whether your "quantum-inspired" solver actually beats a classical baseline. Have that benchmark ready or don't pick these.

- **SIH26140 — Interactive quantum algorithm learning platform** is the safest of the five (it's an educational tool, no advantage claim needed) and will be nearly empty.

---

## R. CAD & Design — Autodesk (5)

- **SIH26116 — Mixed-use B+G+9 building in Revit.** This is an architecture assignment, not a software problem. CS teams will not touch it. If you have architecture students, this is the least-contested PS on the board relative to your skills.
- **SIH26114 — Smart city site planning in Autodesk Forma.** Same logic — tool-gated.

---

## S. Edge AI — Qualcomm (5, all Hardware)

**SIH26177–SIH26181.** All require on-device inference on Qualcomm silicon. Hardware-gated, so pickup depends entirely on whether kits are distributed.

- **SIH26177 — Autonomous SAR drone** will be the most contested of the five (drone + rescue is the classic hackathon fantasy).
- **SIH26179 — Retail intelligence platform** will be the least — retail analytics feels commercial rather than national-mission, so it gets skipped.

---

## T. Heritage & Culture (1 real PS)

- **SIH26096 — Digital heritage archive for memorials, manuscripts and Ambedkar-related collections (Hardware/MoSJE).** The only substantive heritage PS. Manuscript OCR for Indic scripts + AV archival + metadata standards. Reasonably hard, and heritage is historically the thinnest-competition track at SIH. Good asymmetric bet.

---

## U. Student Innovation — AICTE (34 open slots)

**SIH26193–SIH26226** are all titled just "Student Innovation" (~17 software, ~17 hardware) spread across themes. These are open-ended: you bring your own idea.

Reality check: the open track is *very* crowded at the internal-hackathon stage because weak teams default to it, but it's also where a genuinely original prototype has no incumbent to be compared against. Pick it only if you already have a working thing. Do not pick it to postpone deciding.

---

# Shortlist: the 10 hardest

1. **SIH26098** — 155 mm precision guidance kit + electronic fuze (MoD)
2. **SIH26166** — Chandrayaan-2 cross-sensor image correspondence (ISRO)
3. **SIH26119** — Indigenous GPU MILP solver vs CPLEX/Gurobi (MRPL)
4. **SIH26029** — 10,000 A automated MCB short-circuit test rig (BIS)
5. **SIH26058** — Adaptive software-defined sonar transmitter for AUVs (MoES)
6. **SIH26148** — New language + compiler for AV-evading forensic scripting (NTRO)
7. **SIH26151** — Dark web threat actor de-anonymization (NTRO)
8. **SIH26185** — Helmet-mounted conformal antenna, CQB (MHA/NSG)
9. **SIH26064** — Seafloor metal detection sensor for deep-ocean minerals (MoES)
10. **SIH26081** — Hybrid AI-NWP multi-model forecast blending (MoES/IMD)

# Shortlist: the 12 almost nobody will pick

Ordered roughly by *lowest effort-to-differentiation ratio* — these are the tactical picks, not the trophy picks.

1. **SIH26062** — Polar expedition logistics & asset management (MoES) — ordinary software, extraordinary framing
2. **SIH26099** — Material code standardization across CPSEs (MoPNG) — entity resolution, immediate real value
3. **SIH26056** — Airfare price index for CPI (MoSPI) — the index methodology is the deliverable
4. **SIH26035 / SIH26036** — Legal metrology test reports & verification (BIS)
5. **SIH26073** — AWS sensor anomaly detection (IMD)
6. **SIH26156** — Universal log pre-processing framework (NTRO)
7. **SIH26008** — Conveyor belt rupture prediction (Ministry of Steel)
8. **SIH26063** — Polar science outreach portal (MoES)
9. **SIH26031** — Onion quality grading (Consumer Affairs)
10. **SIH26116** — Revit mixed-use building (Autodesk) — if you have architecture students
11. **SIH26096** — Digital heritage archive (MoSJE)
12. **SIH26020** — Khadi hand-spinning equipment (MSME) — if you have mechanical design people

# The overlap — hard *and* quiet

If you want difficulty and low competition together, this is the intersection:

- **SIH26042** — Tribal-language pedagogy tool (Jharkhand). Low-resource NLP for Santali/Ho/Mundari. Hard, meaningful, and almost nobody is equipped for it.
- **SIH26058 / SIH26064 / SIH26065** — the MoES underwater/polar hardware trio.
- **SIH26049 / SIH26051 / SIH26052** — the three DRDO PS everyone skips because the titles are unreadable.
- **SIH26030** — Cable specimen prep automation. Real mechatronics, zero competition.
- **SIH26147** — I/Q signal parameter extraction (NTRO). RF theory gate keeps it empty.

---

## How to actually decide

1. **Check live idea counts on the portal now.** Everything above is a prior; the counter is evidence. A PS sitting at 30/500 on 10 September is worth more than any analysis here.
2. **For any PS without a dataset link (184 of 226), answer "where does my data come from" before you commit.** If the honest answer is "we'll synthesise it", expect that to be the first question at the finale.
3. **Check whether your SPOC has blocked the PS.** Your college must block a PS before your team can be nominated against it — a great PS your SPOC hasn't blocked is not available to you.
4. **Read the full description, not the title.** Several titles on this list are actively misleading in both directions.

_Full text of every PS: `ps_2026/SIH26XXX.md` in the open dataset, or sih.gov.in/sih2026PS._
