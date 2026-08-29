# Research Log

Append-only. Newest entries at the bottom. One entry per finding, with who and when.

Format:

```
## YYYY-MM-DD — <name>
**Module:** <research module>
**Finding:**
**Source:**
**So what:** what this changes in the build, if anything.
```

---

## 2026-08-28 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Multi-Level Surface (MLS) maps store multiple height intervals (ground surface and overhead clearance/ceiling) per 2D grid cell column to handle overhanging obstacles and multi-level structures.
**Source:** Triebel, R., Pfaff, P., & Burgard, W. (2006). "Multi-Level Surface Maps for Outdoor Terrain Mapping and Loop Closing." *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.
**So what:** Confirms our ground+ceiling two-layer representation is an MLS-style map. We must explicitly cite Triebel et al. (2006) as prior art and phrase our architecture as adopting "MLS-style two-layer cells", avoiding any claim of inventing multi-level 2.5D cells.

## 2026-08-28 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Nested egocentric multi-resolution grids with interlaced ring buffers and constant-time toroidal shifts were developed for 3D laser scanners on MAVs. Cell resolution decreases with range, justified by LiDAR beam divergence and measurement density.
**Source:** Droeschel, D., Stückler, J., & Behnke, S. (2014). "Local Multi-Resolution Representation for 6D Motion Estimation and Mapping with a Continuously Rotating 3D Laser Scanner." *IEEE International Conference on Robotics and Automation (ICRA)*; and *Journal of Field Robotics (JFR)* 33(4):451–475, 2016.
**So what:** Gives Aakash (D1) and Shrestha (D3) the validated precedent for $O(1)$ toroidal shift indexing on ring buffers. Identifies our exact novelty gap: Droeschel did not include 2.5D elevation Kalman fusion, semantic-driven refinement, variance-honest split/merge under a fixed memory budget, or plan-regret validation.

## 2026-08-28 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Geometry clipmaps maintain a set of nested regular grids centered on the observer for terrain rendering, updating only newly exposed boundary regions in $O(\text{perimeter})$ time upon viewer movement rather than $O(\text{area})$.
**Source:** Losasso, F., & Hoppe, H. (2004). "Geometry Clipmaps: Terrain Rendering Using Nested Regular Grids." *ACM SIGGRAPH 2004*, pp. 769–776.
**So what:** Confirms Shrestha's toroidal shift kernel must implement the $O(\text{perimeter})$ boundary-only clear rather than clearing entire ring buffers upon shift.

## 2026-08-28 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Recursive 1D Kalman filter elevation updates per cell with range-dependent measurement variance $\sigma_m^2(r) = \sigma_0^2 + c \cdot r^2$ provide statistically optimal terrain height tracking for mobile robots.
**Source:** Fankhauser, P., Bloesch, M., Gehring, C., Hutter, M., & Siegwart, R. (2014). "Robot-Centric Elevation Mapping with Uncertainty Estimates." *International Conference on Climbing and Walking Robots (CLAWAR)*.
**So what:** Confirms that the Kalman elevation measurement variance model in `docs/sih-math.md` §3 matches canonical robotics literature.

## 2026-08-29 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Radial ground beam spacing grows quadratically with range ($s_{\text{rad}}(r) = \frac{r^2 \Delta\phi}{h_s}$), reaching $10.8\text{ m}$ at $50\text{ m}$. Consequently, a uniform $5\text{ cm}$ grid at $50\text{ m}$ is $99.87\%$ empty in a single frame. Far rings are populated over time via vehicle ego-motion ("Ring-Sweep Filling"). Potholes ($30\text{ cm}$) are physically undetectable beyond $r_{\max} \approx 8.3\text{ m}$.
**Source:** Derivation from LiDAR beam trigonometry on KITTI HDL-64E parameters; formalized in `docs/memo-r1-sensor-physics-and-ring-justification.md`.
**So what:** Provides the physical proof that coarsening far rings is not merely a memory optimization, but a physical necessity matching LiDAR sampling density. Sets the hard $8.3\text{ m}$ scope limit for negative obstacles.

## 2026-08-29 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Compiled an 8-way comparative taxonomy contrasting `vrgrid` against OctoMap (2013), MLS (2006), Droeschel (2014), Elevation Mapping (2014), Adaptive Patched Grid (2023), PCT (2024), and Wavemap (2023).
**Source:** `docs/prior-art-taxonomy-matrix.md`.
**So what:** Formally isolates `vrgrid`'s three defensible novelty claims: (1) joint range+semantic foveation under compile-time 8.94 MB SoA bounds, (2) variance-honest split/merge via Law of Total Variance, and (3) validation via downstream Plan Regret $R(S)$.

## 2026-08-30 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Point Cloud Tomography (PCT) slices 3D point clouds into parallel 2.5D elevation layers for GPU-accelerated traversability planning. While PCT represents a modern revival of MLS maps, its core contribution is parallel GPU planning rather than foveated spatial compression.
**Source:** Yang, T., Cheng, K., Xue, J., Jiao, J., & Liu, M. (2024). "Efficient Global Navigational Planning in 3D Structures based on Point Cloud Tomography." *IEEE/ASME Transactions on Mechatronics*, arXiv:2403.07631.
**So what:** Validates our critique that PCT is MLS reframed. Positions `vrgrid` as solving the orthogonal problem: foveated spatial compression under hard memory bounds rather than uniform tensor slicing.

## 2026-08-30 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Adaptive Patched Grid Mapping dynamically alters 2.5D cell patch sizes for automotive LiDAR, but merges child cells using naive inverse-variance averaging ($1/\sigma_p^2 = \sum 1/\sigma_i^2$). This drops the spatial between-cell variance term ($\sum w_i (\mu_i - \mu_p)^2$), creating artificial high confidence where cells straddle elevation steps (e.g., curbs).
**Source:** Wodtko, T., Griebel, M., & Buchholz, M. (2023). "Adaptive Patched Grid Mapping." *arXiv:2308.03416*, Ulm University.
**So what:** Identifies the critical mathematical error in modern adaptive grids. Proves why Aakash's (D1) implementation of the Law of Total Variance in `sih-math.md` §4 is mathematically necessary for obstacle safety.

## 2026-08-30 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Wavemap implements 3D multi-resolution volumetric mapping via Haar wavelets. While memory-efficient for 3D aerial robots, tree traversal creates irregular memory lookups and branch divergence on GPUs. For ground vehicles, $O(1)$ flat 2.5D ring buffers maximize memory bandwidth and provide planner-native queries.
**Source:** Reijgwart, V., Cadena, C., Siegwart, R., & Ott, L. (2023). "wavemap: Efficient Volumetric Hierarchical Occupancy Mapping." *Robotics: Science and Systems (RSS)*, arXiv:2306.01279.
**So what:** Supplies the formal justification for why `vrgrid` deliberately uses 2.5D foveated rings rather than 3D wavelet trees for autonomous driving.

## 2026-08-30 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Maximum Mipmaps build hierarchical max-reduction pyramids over height fields for fast ray-stepping in terrain rendering.
**Source:** Tevs, A., Ihrke, I., & Seidel, H.-P. (2008). "Maximum Mipmaps for Fast, Accurate, and Scalable Dynamic Height Field Rendering." *ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D)*.
**So what:** Confirms the graphics lineage for Shrestha's (D3) conservative pyramid (§7.2), providing guaranteed zero-false-negative traversability ray-stepping for safety.

## 2026-09-01 — Srinivas
**Module:** R1 — Representation & prior art
**Finding:** Formulated the definitive architectural comparison between 2.5D foveated ring grids and 3D volumetric hierarchies (OctoMap, Wavemap). Proved that for ground robots operating on 2D surface manifolds, 3D trees waste memory on empty air ($>98\%$), introduce GPU warp divergence via tree pointer chasing, and lack deterministic compile-time memory bounds. Flat 2.5D ring arrays deliver $O(1)$ indexing, 100% coalesced GPU memory access, and native 2D traversability bitfields under an 8.94 MB compile-time bound (~286x smaller than 3D voxels).
**Source:** `docs/memo-r1-day4-rings-vs-octree.md`.
**So what:** Unblocks the Day 4 justification milestone and provides the submission-ready defense text for the report.
