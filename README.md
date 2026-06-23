# Multi-Verse Optimizer (MVO) Hyperparameter Analysis on Hypersphere Function

An in-depth research and engineering project analyzing the convergence, computational complexity, and structural dynamics of the **Multi-Verse Optimizer (MVO)** algorithm applied to a continuous 10-dimensional **Hypersphere benchmark function**. 

The project leverages automated **Grid Search** optimization to investigate how critical hyperparameters—such as population size, maximum epochs, and Wormhole Existence Probability (WEP)—impact optimization precision and stability compared to traditional bio-inspired metaheuristics like Genetic Algorithms (GA).

---
<p align="center">
  <img width="760" height="678" alt="image" src="https://github.com/user-attachments/assets/07623dbf-ffc2-4119-9a0a-3354f61206a8" />
  <br>
  <em>Figure 1: 3D Visualization of the MVO algorithm on a Hypersphere function (Note: "Wartość funkcji celu" translates to "Objective Function Value", and "Wymiar" means "Dimension").</em>
</p>

## Key Features

- **Theoretical Benchmarking**: Evaluation of the MVO astrophysics-based multi-verse model (White/Black holes for exploration, Wormholes for exploitation) versus traditional Genetic Algorithms (GA).
- **Automated Grid Search**: Systematic evaluation of **18 unique configuration pairs** across varying ecosystem sizes and epoch counts.
- **Multi-Criteria Analytics**:
  - **Convergence Analysis**: High-resolution log-scaled trajectory and convergence curve plotting.
  - **Pareto Efficiency Frontier**: Cross-examination of time complexity (execution time in seconds) versus optimization accuracy (final objective function error).
  - **Trajectory Inspection**: Highlighting structural behavior patterns such as smooth down-slope rolling versus the complex "orbiting effect" caused by aggressive wormhole teleportation.
- **Interactive Visualization**: Extensive usage of multi-dimensional plotting frameworks to chart performance matrices and 3D objective spaces.

---

## Tech Stack & Libraries

- **Language**: Python 3
- **Optimization Framework**: `MealPy` (Multi-Verse Optimizer Implementation)
- **Data Engineering**: `NumPy`, `Pandas`
- **Data Visualization**: `Matplotlib` (3D Projection & Lineplots), `Seaborn` (Dark-grid matrices and regression facets)

---

## Experimental Setup & Grid Search Parameters

The optimization domain was bound within $[-5.0, 5.0]$ for a 10-dimensional space, testing combinations of:
1. **Population Size (Number of Universes)**: `30`, `60`, and `100` individuals.
2. **Evolutionary Lifespan (Max Epochs)**: `50` and `150` generations.
3. **Wormhole Existence Probability (WEP Dynamics)**:
   - **Low ("Mało tuneli")**: Geared towards steady, exploratory paths with smooth convergence.
   - **Standard**: The default balanced configuration.
   - **High ("Dużo tuneli")**: Aggressive exploitation focused heavily around the best-known local/global optimum.

---

## Summary of Key Engineering Insights

- **The Wormhole Paradox (WEP)**: Low WEP ("Mało tuneli") proved to be the most reliable and stable baseline option for low-to-mid population tiers, preventing chaotic spatial disruptions. Conversely, High WEP ("Dużo tuneli") yields a highly erratic "orbiting" path but functions as a **Premium Strategy**—outperforming all setups and hitting the absolute global minimum ($5.7 \times 10^{-5}$) *only* when backed by a massive population pool of 100 universes.
- **The Stagnation of "Standard"**: The default balanced configuration suffered severe stagnation at higher resource scales, proving the absolute necessity of targeted hyperparameter tuning.
- **Pareto Front Optimality**: 
  - *Compute-Efficient Path*: 30 universes + Low WEP (Sub-second execution with satisfactory error reduction).
  - *Max-Precision Path*: 100 universes + High/Low WEP (Highest CPU investment yielding absolute convergence).

---

## Structure of the Project

- `wyniki_mvo_raport.csv` — Contains raw logs and historical data from the 1800 experimental iterations.
- `Sprawozdanie_MVO_projekt4.ipynb` / `.html` — Comprehensive Jupyter notebook containing analytical reports, mathematical deductions, and plotting blocks.

---
*Developed as part of a deep-dive into advanced evolutionary computing and metaheuristic optimization algorithms for Evolutionary Computation course.*
