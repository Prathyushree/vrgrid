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
