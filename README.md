# BurstBeam: Near-Optimal Real-Time 3D Path Planning

**Author:** Arka Brahma, Age 16, Class 10, India  
**Algorithm:** Polynomial Beam Search + Short + Delayed

## Overview
BurstBeam is a deterministic 3D pathfinding algorithm designed for dense urban grids (e.g., drone navigation).  

- 100% success rate in dense 3D grids  
- Only +0.8% longer than optimal paths (A*)  
- 44 ms average runtime (100x100x30 grid)  
- Memory-efficient (~110 MB)

BurstBeam uses:
1. Early parallel bursts (`sub_beams`) to escape urban canyons  
2. Delayed pruning (`prune_delay`) for convergence  
3. Fully deterministic behavior without training

---

## Installation
```bash
git clone https://github.com/arkakly128-hub/BurstBeam.git
cd BurstBeam
