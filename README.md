# Network Analysis Course

## 📋 Overview

This project analyzes **Portuguese public procurement** as a network, using official public contract data from 2023–2026. Public buyers (entities) and suppliers (companies) form a bipartite buyer→supplier network, which is analyzed to identify dominant companies, dominant public entities, market structure, and community organization.

The analysis is carried out at two levels:
- **National level** (`02_network.ipynb`) — the full Portuguese public procurement market.
- **Lisbon level** (`03_network_lisbon.ipynb`) — a focused look at the capital, with a side-by-side comparison in `portugal_vs_lisbon_comparison.md`.

## 📚 Homeworks

- **Homework 1** — Network analysis of a *Game of Thrones* book character co-occurrence network.
- **Homework 2** — See `homeworks/homework2/Assignment02.ipynb`.

## 📁 Repository Structure

```tree
network-analysis/
│
├── homeworks/
│   ├── homework1/
│   │   ├── Assignment01_GroupB.ipynb   # Game of Thrones book co-occurrence network
│   │   ├── book_edges.csv              # Edge list dataset
│   │   ├── giant_component.gexf        # Exported giant component (GEXF)
│   │   ├── graph.gephi                 # Gephi project file
│   │   ├── got_book1_gephi.png         # Network visualization
│   │   └── got_book1_gephi_v1.png      # Network visualization (v1)
│   │
│   └── homework2/
│       └── Assignment02.ipynb
│
├── project/
│   ├── notebooks/
│   │   ├── 01_preprocessing.ipynb      # Data cleaning & preparation
│   │   ├── 02_network.ipynb            # National public procurement network analysis
│   │   └── 03_network_lisbon.ipynb     # Lisbon-level network analysis
│   │
│   ├── data/
│   │   ├── contratos2023_part01.csv    # Raw public contracts (2023)
│   │   ├── contratos2023_part02.csv
│   │   ├── contratos2023_part03.csv
│   │   ├── contratos2024_part01.csv    # Raw public contracts (2024)
│   │   ├── contratos2024_part02.csv
│   │   ├── contratos2024_part03.csv
│   │   ├── contratos2025_part01.csv    # Raw public contracts (2025)
│   │   ├── contratos2025_part02.csv
│   │   ├── contratos2025_part03.csv
│   │   ├── contratos2026.csv           # Raw public contracts (2026)
│   │   └── preprocessed_data.csv       # Cleaned dataset used by the notebooks
│   │
│   ├── figures/                        # Generated plots & visualizations
│   ├── graphs/                         # Exported graph files
│   ├── portugal_vs_lisbon_comparison.md # National vs. Lisbon comparison write-up
│   ├── presentation.pdf                # Project Final Presentation
│   └── project_description.pdf         # Project brief
│
├── .gitignore
└── README.md
```

## 👥 Team

**Group B**
- Beatriz Marques – 20231605
- Maria Inês Santos – 20231630
- Luís Soeiro – 20211536
- Rodrigo Silva – 20231602