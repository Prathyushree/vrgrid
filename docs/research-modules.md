# Research Modules — Reading Assignments

*Three modules, one owner each. Each module is paired to a developer (see execution plan). You are not writing a literature review at the end; you are delivering **decision memos** on a fixed cadence that unblock your paired dev.*

---

## How research works on this project

**The failure mode to avoid:** three people read forty papers, produce a bibliography on 4 September, and none of it changed a single line of code. That is worse than not reading at all, because it consumed three people for eight days.

**The rule:** every paper you read must terminate in one of three outcomes.

| Outcome | Action |
|---|---|
| **Changes a decision** | Write a ≤1-page memo. Hand to your paired dev *the day you find it*, not at the end. |
| **Confirms a decision** | One line in the module log. Cite it in the report. Move on. |
| **Neither** | Stop reading. Log the title and why it didn't apply. |

**Deliverable cadence — every 48 hours, per module:**
1. **Decision memo** (≤1 page): what we should change, why, what it costs, what happens if we don't.
2. **Positioning paragraph**: 3–5 sentences of related-work prose, submission-ready. By 4 September these three sets of paragraphs *are* the related-work section. Nobody writes it from scratch at the end.
3. **Number harvest**: any figure from a paper we can benchmark against, with its exact conditions (dataset, sequence, hardware). Numbers without conditions are useless.

**Verify every citation before it reaches a slide.** Plan v2 already caught one hallucinated model ("RangeBlock," 74.5% mIoU — no such paper; the number matches SphereFormer's 74.8%, a sparse-voxel transformer, not a range-view method). If you cannot find the PDF, the paper does not exist. Assume nothing.

**Priority key:** 🔴 read first, blocks a decision · 🟠 read this week · 🟡 read if time · ⚫ know it exists, cite it, don't read it

---

# Module R1 — Representation, Prior Art & Positioning
### Paired with D1 (grid engine). Owner: ______

**Your job in one sentence:** make sure we do not claim as novel anything that was published in 2004, 2006 or 2014, and make sure we *do* claim what is actually ours.

**This is the highest-stakes research module.** A panel member who recognises our ring diagram as a 2014 paper we didn't cite will discount everything else we say. Your first 48 hours matter more than anyone else's.

### 🔴 Tier 1 — read before D1 freezes the cell struct (Day 1–2)

| Paper | Why |
|---|---|
| **Triebel, Pfaff & Burgard, "Multi-Level Surface Maps for Outdoor Terrain Mapping and Loop Closing," IROS 2006** | **Our ground+ceiling scheme is a two-layer MLS map.** Twenty years old. Read it, cite it, and rewrite our claim so it says "we use MLS-style two-layer cells" rather than implying we invented them. Non-negotiable. |
| **Droeschel, Stückler & Behnke, "Local Multi-Resolution Representation for 6D Motion Estimation and Mapping with a Continuously Rotating 3D Laser Scanner," ICRA 2014** — and the JFR 2016 extension (*J. Field Robotics* 33(4):451–475) | **This is our foveated ring grid, in 2014.** Interlaced ring buffers, resolution decreasing with distance, constant-time ego-motion shift, justified by sensor measurement density. Extract: (a) exactly how their ring buffers work — D1 can steal the implementation approach; (b) what they *didn't* do (no semantics, no 2.5D elevation, no uncertainty handling on resolution change) — that gap is our contribution statement. |
| **Losasso & Hoppe, "Geometry Clipmaps: Terrain Rendering Using Nested Regular Grids," SIGGRAPH 2004** | The graphics origin of nested toroidal LOD rings. Gives us a lineage to cite and one implementation idea D1 should know: **incremental boundary-only update, O(perimeter) not O(area)**. |
| **Fankhauser, Bloesch, Gehring, Hutter & Siegwart, "Robot-Centric Elevation Mapping with Uncertainty Estimates," CLAWAR 2014** | The canonical Kalman-per-cell elevation map with range-dependent measurement variance. Our §3 measurement model comes from here. Confirm we've got the variance propagation right. |

### 🟠 Tier 2 — read Day 3–4

| Paper | Why |
|---|---|
| **Yang, Cheng, Xue, Jiao & Liu, "Efficient Global Navigational Planning in 3D Structures based on Point Cloud Tomography," arXiv:2403.07631, IEEE/ASME T-Mech 2024** | The closest modern multi-layer 2.5D work. **Important finding to verify:** PCT's representation is substantially MLS reframed; its real contribution is GPU-parallel traversability evaluation + cross-slice planning. Confirm this and state it — it's a fair, informed critique that shows we read past the abstract. |
| **Wodtko, Griebel & Buchholz, "Adaptive Patched Grid Mapping," arXiv:2308.03416, Ulm University** | **Closest prior art on range-adaptive automotive grids.** Layered grid with dynamically changing cell sizes, novel spatial cell fusion, memory reduction for automotive perception. Position against it explicitly: what do they do on split/merge uncertainty? On semantics? Their detailed tables are paywalled — get what you can. |
| **Reijgwart, Cadena, Siegwart & Ott, "wavemap: Efficient Volumetric Hierarchical Occupancy Mapping," RSS 2023, arXiv:2306.01279** | The hierarchical-3D alternative we are deliberately *not* using. Haar wavelet MRA, adaptive resolution, uncertainty-aware sensor model. Need one paragraph on why 2.5D + rings beats octree + wavelets for a ground vehicle (answer: dense array, coalesced GPU access, planner-native query — but verify). |
| **Tevs, Ihrke & Seidel, "Maximum Mipmaps for Fast, Accurate, and Scalable Dynamic Height Field Rendering," I3D 2008** | The source of our conservative pyramid (§7). Max instead of mean, hierarchical ray-stepping. Confirm the construction and check whether anyone has already imported it to traversability — if they have, we cite them; if not, that's a contribution. |

### 🟡 Tier 3 — if time

- **Greene, Kass & Miller, "Hierarchical Z-Buffer Visibility," SIGGRAPH 1993** — the occlusion-culling ancestor of the max pyramid. One paragraph of lineage.
- **Tang et al., "ML-SkiMap: Path Planning on Multi-level Point Cloud with a Weighted Traversability Graph," arXiv:2504.21622, 2025** — SkipList tree with vertical levels; curvature-driven point retention (28,579 → 2,771 points, 9.6%). The retention idea is adjacent to our refinement policy.
- **Einhorn, Schröter & Gross,** Nd-tree adaptive occupancy mapping — the classic split/merge-on-measurement-statistics lineage. Background only.
- ⚫ **OctoMap** (Hornung et al., Autonomous Robots 2013) — cite as the standard 3D baseline. Do not read.

### R1 deliverables

1. **Day 2:** "Prior art we must cite" memo — the list, with one sentence each on what they did and what we do differently. This becomes the report's positioning section.
2. **Day 2:** Verified answer to *"has anyone built a toroidal-addressed LOD pyramid over a 2.5D elevation map with semantic refinement?"* If yes, we reposition immediately. If no, that's the claim.
3. **Day 4:** One paragraph justifying rings-over-octree, with a citation.
4. **Day 6:** Related-work section, assembled, ~600 words.

---

# Module R2 — Dynamics, Segmentation & Ghost Removal
### Paired with D2 (perception front-end). Owner: ______

**Your job in one sentence:** make sure our ghost-removal numbers are comparable to published ones, and that D2 never implements something a repo already does better.

### 🔴 Tier 1 — Day 1–2

| Paper | Why |
|---|---|
| **Xu, Kong, Shuai & Liu, "FRNet: Frustum-Range Networks for Scalable LiDAR Segmentation," IEEE TIP 2025, arXiv:2312.04484** | Our segmenter. Verify before D2 depends on it: Apache 2.0 licence ✓, published checkpoints ✓, 73.3% mIoU SemanticKITTI / 82.5% nuScenes, ~5× faster than comparable SOTA, MMDetection3D-based. **Confirm the checkpoints are 19-class and confirm exactly which config to load.** Also check the Fast-FRNet variant (~7.5M params) in case we need headroom. |
| **Chen, Li, Mersch, Wiesmann, Gall, Behley & Stachniss, "Moving Object Segmentation in 3D LiDAR Data: A Learning-based Approach Exploiting Sequential Data," RA-L 2021 (LMNet)** | The residual-image approach D2 implements in Phase 2. Extract the exact residual construction, the number of residual channels, and how they handle ego-motion compensation. |
| **Zhang, Duberg, Pinto Afonso et al., "A Dynamic Points Removal Benchmark in Point Cloud Maps," KTH-RPL, ITSC 2023** | The benchmark we report against. **Critical: understand that it evaluates offline whole-map cleaning while we run an online rolling local map.** Extract the exact metric definitions so our numbers are directly comparable, and get the baseline table (Removert, ERASOR, Octomap, Dynablox, DUFOMap, BeautyMap). |
| **Lim, Hwang, Oh & Myung, "ERASOR: Egocentric Ratio of Pseudo Occupancy-based Dynamic Object Removal," RA-L 2021** | Cheapest strong baseline. The egocentric-ratio idea may be directly usable as a fallback if our visibility cleanup underperforms. |

### 🟠 Tier 2 — Day 3–5

| Paper | Why |
|---|---|
| **Duberg, Jia, Zhang et al., "DUFOMap: Efficient Dynamic Awareness Mapping," RA-L 2024** | Ray-casting free-space classification, online, **one parameter set across all scenarios**. Our visibility cleanup (§10.4) is the cheap version of this idea. Compare the mechanisms honestly and get their numbers. |
| **Jia, Chen, Zhang et al., "BeautyMap: Binary-Encoded Adaptable Ground Matrix for Dynamic Points Removal," RA-L 2024** | Binary ground matrix, coarse-to-fine z-axis segmentation, range-visibility static restoration. The **static restoration** idea is directly relevant — it's the mechanism that stops over-clearing from eating fences. |
| **Xu et al., "FLARES: Rethinking Range-View Representation," arXiv:2502.09274, Bosch, Feb 2025** | Argues for *lower* azimuth resolution + sub-clouds (64×512, not 64×2048), better on both speed and accuracy. D2 needs this before fixing the range-image config. Verify the claim holds at our resolution. |
| **Lim, Oh & Myung, "Patchwork++: Fast and Robust Ground Segmentation," IROS 2022** | Use as-is; do not reimplement. Confirm licence and check whether it handles our slope/kerb cases. |
| **Vizzo, Guadagnino, Mersch, Wiesmann, Behley & Stachniss, "KISS-ICP: In Defense of Point-to-Point ICP," RA-L 2023** | Runs in parallel with GT poses from Day 1 (B5). Extract expected drift on KITTI so D3 knows what gap to expect in the GT-vs-odometry metric. |

### 🟡 Tier 3

- **Kim & Kim, "Remove, then Revert" (Removert), IROS 2020** — multi-resolution range-image visibility. Baseline.
- **Lim et al., "HeLiMOS"** — moving-object labels across four LiDAR types. Only relevant if we claim cross-sensor generalisation, which we probably won't in eight days.
- **Behley et al., "SemanticKITTI," ICCV 2019** — for the exact multi-scan (25-class) label semantics and the `learning_map` structure. ⚑ **Verify the specific claim in master v4 §3.6: that `moving-*` IDs 250–259 are present in the raw `.label` files and the 19-class collapse happens only in config.** If that's wrong, our entire training-avoidance plan collapses and D2 must know on Day 1. **This is your single most urgent task.**

### R2 deliverables

1. **Day 1, before anything else:** confirm or refute the raw-label claim above. One line, sent immediately.
2. **Day 2:** FRNet setup memo — exact config, checkpoint URL, class mapping, known gotchas.
3. **Day 3:** DynamicMap metric definitions, written so D3 can implement them without reading the paper.
4. **Day 5:** Baseline number table (method, DR, SP, runtime, dataset, hardware) for the comparison slide.
5. **Day 6:** Related-work paragraphs on segmentation and dynamic removal.

---

# Module R3 — Traversability, Evaluation & the Plan-Sensitivity Claim
### Paired with D3 (evaluation + dashboard). Owner: ______

**Your job in one sentence:** establish that plan-regret evaluation is genuinely unpublished, and give D3 the metric definitions to implement.

**This module owns the headline novelty claim.** If it turns out someone already published resolution-vs-plan-quality, we need to know by Day 3, not on 5 September.

### 🔴 Tier 1 — Day 1–3

| Paper | Why |
|---|---|
| **Psomiadis, Maity & Tsiotras, "Communication-Aware Map Compression for Online Path-Planning," ICRA 2024, arXiv:2309.13451** — and the iterative version, arXiv:2503.10843 | **The closest prior art to our headline claim.** Sequentially selects optimal map compression guided by the robot's path, balancing resolution against communication cost. Read very carefully. Their objective is **information-theoretic**; ours is **plan-regret**. If you cannot articulate that difference in three sentences, our novelty claim is in trouble — escalate immediately. |
| **Larsson, Maity & Tsiotras, "Information-Theoretic Abstractions for Planning in Agents with Computational Constraints," RA-L 6(4):7651–7658, 2021** | The information-bottleneck formulation of resolution allocation. Same lineage. Establishes exactly what "information gain" allocation means so we can contrast it. |
| **Tsiotras et al., "Q-tree search," IEEE T-RO 36(6):1669–1685, 2020** | Multiresolution planning with distance-from-agent LOD. Confirms that "refine near the agent" is old; our refinement is near-the-*decision*, which is different. |
| **Cowlagi & Tsiotras, "Multiresolution Motion Planning for Autonomous Agents via Wavelet-Based Cell Decompositions," IEEE T-SMC-B 42(5):1455–1469, 2012** | Earliest form of the idea. Background, one citation. |

### 🟠 Tier 2 — Day 3–5

| Paper | Why |
|---|---|
| **Patel et al., "RoadRunner M&M: Learning Multi-range Multi-resolution Traversability Maps," RA-L 2024, arXiv:2409.10940** | **Directly comparable, and the numbers are usable.** Predicts elevation + traversability at two range/resolution levels: ±50 m at 0.2 m, ±100 m at 0.8 m, reporting up to 50% improvement on elevation and 30% on traversability over RoadRunner. Note it is a *learned* end-to-end map, not an online-refined data structure — that's our differentiator. Get their resolution schedule for our comparison table. |
| **Sivaprakasam et al., "SALON: Self-supervised Adaptive Learning for Off-road Navigation," ICRA 2025, arXiv:2412.07826** | Rapid online traversability adaptation. Relevant to our traversability-as-bitfield design; check what conditions they decompose into. |
| **Cai et al., "EVORA: Deep Evidential Traversability Learning"** | Uncertainty-aware traversability. Relevant to our confidence bit and the fail-safe rule. |
| **Nuss et al., "A Random Finite Set Approach for Dynamic Occupancy Grid Maps with Real-Time Application," IJRR 2018** | The DOGMa lineage — particle-based evidential grids with per-cell velocity. We are *not* doing this; know why (cost), and have the one-sentence answer ready. |

### 🟡 Tier 3

- **Verti-Bench, arXiv:2502.11426, RSS 2025** — off-road mobility benchmark, 100 environments / 1000 tasks. ⚑ **Verify the venue and year before citing.** Possible testbed for the plan-regret study if SemanticKITTI proves awkward for planning.
- **Multi-resolution 3D mapping with explicit free space, arXiv:2010.07929** — uses **multi-resolution maximum occupancy queries** for coarse-to-fine collision checking. This is the closest existing thing to our conservative pyramid. If it covers what §7.3 claims, we cite it and narrow our claim to the 2.5D-traversability specialisation.
- **Dempster–Shafer / evidential occupancy background** — only if a judge asks why log-odds instead.

### R3 deliverables

1. **Day 3, hard deadline:** verdict on the plan-regret novelty claim. *"Unpublished as framed, closest is Psomiadis 2024 which optimises information not plan cost"* — or an escalation. **This gates our headline slide.**
2. **Day 3:** metric definitions handed to D3 as pseudocode: plan regret, Fréchet distance, ρ = IL/spread, DR/SP/F.
3. **Day 4:** comparison table skeleton — which published numbers we can sit next to, under what conditions.
4. **Day 6:** related-work paragraphs on traversability and evaluation, plus the "why not DOGMa" paragraph.

---

## Shared reference — verify-before-citing list

Every one of these appeared in earlier planning docs and must be confirmed against a real PDF before it reaches a slide:

- ❌ **"RangeBlock," 74.5% mIoU** — no such paper found. Number matches SphereFormer (74.8%, CVPR 2023), a sparse-voxel transformer, not range-view. **Do not cite.**
- ⚠ **PCT "three orders of magnitude" scene-evaluation speedup** — author-reported, own dataset. Quote with attribution and conditions.
- ⚠ **ML-SkiMap 9.6% point retention** — author-reported on one test cloud.
- ⚠ **Verti-Bench venue (RSS 2025)** — confirm.
- ⚠ **Any arXiv preprint stamped 2026** — check whether a final published version exists.

## Module log format

One shared file, `research-log.md`, three sections. Append-only:

```
[R1] 2026-08-29 | Triebel IROS 2006 (MLS maps) | READ
  → DECISION: ground+ceiling is MLS. Reword master v4 §2.3 claim. Cite.
  → COST: none, wording only.
  → POSITIONING: "Our two-layer cell follows the Multi-Level Surface
    formulation of Triebel et al. (2006); our contribution is not the
    representation but the resolution policy over it."
```

If a paper produced no line in this log, you should not have read it.
