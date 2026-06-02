# 📓 Notebook Structured Summary
## Network Analysis Applied to Public Procurement (Contratação Pública)
**Source**: `02_network_fa82b024.ipynb` | Bachelor's in Data Science – NOVA IMS (2025/26)  
**Group B**: Beatriz Marques, Maria Inês Santos, Luís Soeiro, Rodrigo Silva  
**Research Question**: *Which companies have a dominant position in public procurement?*  
**Data Source**: Portal BASE (Portuguese public procurement registry)  
**Notebook stats**: 108 cells (62 markdown, 46 code) · 36 logical sections

---

# Preamble / Title

**📝 Overview:**  
The notebook investigates the Portuguese public procurement market using **network science**.
The central bipartite graph connects *adjudicantes* (public contracting entities / buyers) and
*adjudicatários* (supplier companies / awardees) via contract relationships.
The research seeks to identify structurally dominant companies through centrality measures,
community detection, and comparison against random reference models.

---

# 1. Imports

**⚙️ Code cell purposes:**  
- Loads standard Python libraries: `networkx`, `numpy`, `pandas`, `plotly`, `powerlaw`, `scipy`, `sklearn`  
- Configures auto-reload and working paths  
- Imports custom source modules from `../source` (helper functions for network construction, centrality, visualisation)

---

# 2. Data Integration

**⚙️ Code cell purposes:**  
- Loads the cleaned procurement dataset from file (`pd.read_*`)  
- Parses date column `dataPublicacao` into datetime  

**📊 Textual outputs / results:**

```
<class 'pandas.DataFrame'>
RangeIndex: 16,989 entries, 0 to 16,988
Data columns (total 22 columns):
  idcontrato                   16,989 non-null  int64
  tipoContrato                 16,989 non-null  str
  tipoFimContrato              16,972 non-null  str
  CPV                          16,989 non-null  str      ← EU procurement product code
  adjudicante                  16,989 non-null  str      ← buyer / contracting entity
  adjudicatarios               16,989 non-null  str      ← supplier / awardee
  concorrentes                 14,707 non-null  str      ← competing bidders
  precoBaseProcedimento        16,989 non-null  float64  ← base price
  precoContratual              16,989 non-null  float64  ← contract price
  PrecoTotalEfetivo            16,989 non-null  float64  ← actual total price
  dataPublicacao               16,989 non-null  str
  city                         14,215 non-null  str
  cpv_prefix / agg_cpv         16,989 non-null           ← aggregated CPV category
  adjudicante_clean /
  adjudicatarios_clean         16,989 non-null  str      ← normalised name fields
  dtypes: float64(5), int64(3), str(14)
  Memory usage: 2.9 MB
```
> **Key takeaway**: Dataset has **16,989 contracts** with full buyer, supplier, CPV category, price, and date information.

---

# 3. The Network

*(Umbrella section — analysis details in subsections 3.1–3.4)*

---

## 3.1 How is Public Procurement Distributed?

**📝 Explanatory text:**  
This section builds the core procurement network and characterises its basic structure.

**⚙️ Code cell purposes:**  
- Defines helper functions: `compute_weight()` (log-sum edge weighting), `_ensure_dataframe()`, `most_common()` (mode aggregation for CPV/city labelling)

---

### 3.1.1 Building the Network

**📝 Explanatory text:**  
> *Directed Graph → Bipartite Network (Companies ↔ Public Entities)*  
> **Nodes**: buyers (adjudicantes) + suppliers (adjudicatários)  
> **Edges**: directed from buyer → supplier, weighted by contract value  
> **Edge weight metric**: log-sum of contract values (dampens extreme outliers)

**⚙️ Code cell purposes:**  
- Constructs directed weighted NetworkX graph from the procurement DataFrame  
- Each edge represents a buyer-supplier contract relationship; edge attribute = aggregated contract value

---

### 3.1.2 Basic Properties

**⚙️ Code cell purposes:**  
- Computes standard network metrics: nodes, edges, density, average degree, average strength, average path length, clustering coefficient, transitivity, connected components

**📊 Textual outputs / results:**

| Metric | Value |
|---|---|
| **Nodes (N)** | **6,436** |
| **Edges (L)** | **10,995** |
| Density | 0.000265 (very sparse) |
| Avg Degree ⟨k⟩ | 3.42 |
| Avg Strength ⟨s⟩ (€) | 54 (log-weighted units) |
| Avg Path Length ⟨d⟩ | 5.074 |
| Clustering Coeff. C | 0.000000 |
| Transitivity | 0.000020 |
| Connected Components | **113** |
| Largest CC (%) | **96.0%** |

> **Key takeaway**: The network is **very sparse** (density ≈ 0.026%) but **well-connected** — 96% of all nodes belong to a single giant connected component. Near-zero clustering suggests **bipartite-like structure** (buyers connect to suppliers but suppliers rarely connect directly to each other).

---

### 3.1.3 Connectivity

**⚙️ Code cell purposes:**  
- Analyses connected components; identifies the giant component  
- Computes betweenness centrality for all nodes (buyers + suppliers combined)  
- Classifies top betweenness nodes by type (adjudicante vs. adjudicatário)

**📊 Textual outputs / results — Top-20 by Betweenness (full network, buyers + suppliers):**

| # | Node | Betweenness | Type |
|---|---|---|---|
| 1 | Guarda Nacional Republicana | 0.06954 | adjudicante (buyer) |
| 2 | Município de Leiria | 0.05379 | adjudicante |
| 3 | **Claranet II Solutions** | **0.04661** | **adjudicatário (supplier)** |
| 4 | **Exumas Consulting Group** | **0.04316** | **adjudicatário** |
| 5 | Centro Hospitalar Barreiro Montijo E.P.E. | 0.04210 | adjudicante |
| 6 | Município de Elvas | 0.03669 | adjudicante |
| 7 | Infraestruturas de Portugal | 0.03396 | adjudicante |
| 8 | Santa Casa da Misericórdia de Lisboa | 0.03361 | adjudicante |
| 9 | Unidade Local de Saúde do Arco Ribeirinho E.P.E. | 0.03322 | adjudicante |
| 10 | Município de Alcobaça | 0.03280 | adjudicante |
| 11 | Serviços Municipalizados de Água e Saneamento... | 0.03264 | adjudicante |
| 12 | Município de Vila Nova de Gaia | 0.02954 | adjudicante |
| 13 | Serviço de Saúde da Região Autónoma da Madeira | 0.02952 | adjudicante |
| 14 | CHBM - Centro Hospital Barreiro Montijo EPE | 0.02653 | adjudicante |
| 15 | Município de Almada | 0.02574 | adjudicante |
| 16 | Casa Pia de Lisboa I.P. | 0.02518 | adjudicante |
| 17 | **Petrogal** | **0.02414** | **adjudicatário** |
| 18 | **Base2** | **0.02347** | **adjudicatário** |
| 19 | Gebalis – Gestão do Arrendamento da Habitação Municipal | 0.02336 | adjudicante |
| 20 | **Planeta Vertical** | **0.02319** | **adjudicatário** |

> Top-20 split: **15 buyers / 5 suppliers** — buyers naturally dominate betweenness as structural hubs. Among suppliers, **Claranet II Solutions** and **Exumas Consulting Group** stand out with notably high betweenness.

---

### 3.1.4 Degree / Weight Distribution

**⚙️ Code cell purposes:**  
- Plots in-degree and out-degree distributions  
- Fits power-law model (CCDF) using the `powerlaw` library  
- Compares power-law fit against lognormal and truncated power-law alternatives  
- Provides interpretation guide for model selection

**📊 Textual outputs / results:**

```
==============================
POWER LAW FIT RESULTS (CCDF)
==============================
IN-DEGREE:  alpha = 2.97, xmin = 5.0,  p = 0.1866
OUT-DEGREE: alpha = 1.92, xmin = 6.0,  p = 0.0001

==============================
DISTRIBUTION COMPARISON
==============================
Power law α = 2.00, xmin = 1.0
Power vs Lognormal:   R = -22.203, p = 0.0000
Power vs Truncated:   R = -24.360, p = 0.0000
```

> **Interpretation**:
> - **In-degree (α ≈ 2.97, p = 0.19)**: Cannot reject power law → plausible scale-free distribution for the supplier-side (how many buyers a supplier serves).
> - **Out-degree (α ≈ 1.92, p < 0.001)**: Power law is rejected → buyer-side degree does NOT follow a pure power law.
> - Distribution comparison (R < 0, p → 0): **lognormal and truncated power law both outperform** the simple power law → the network has preferential attachment but is bounded by real-world constraints (budgets, regulations, capacity limits).

---

## 3.2 How Highly Concentrated Is The Network?

---

### 3.2.1 Pareto Principle + HHI

**📝 Explanatory text:**  
Measures overall market concentration using the Pareto principle, Gini coefficient, and the Herfindahl-Hirschman Index (HHI).

**⚙️ Code cell purposes:**  
- Computes cumulative share of contract value held by top 1%, 5%, 10%, 20% of supplier companies  
- Computes Gini coefficient (inequality of value distribution)  
- Computes HHI (sum of squared market shares × 10,000)  
- Generates Lorenz curve visualisation  

**📊 Textual outputs / results:**

```
===================================
PROCUREMENT CONCENTRATION
===================================

Top  1% of companies control  26.08% of total contract value
Top  5% of companies control  51.79% of total contract value
Top 10% of companies control  66.07% of total contract value
Top 20% of companies control  80.46% of total contract value

Gini coefficient: 0.7693
HHI:              20.65
```

> **Key takeaway**:
> - **Strong Pareto effect**: top 5% of suppliers capture ~52% of total value.
> - **Gini = 0.77** → high inequality in contract value distribution.
> - **HHI = 20.65** — very low on traditional scale (0–10,000), indicating **no single firm has monopolistic dominance** overall. However, high Gini shows significant skewness in favour of top players.
> - [chart/figure present — Lorenz curve]

---

## 3.3 Which are the Dominant Entities of the Network?

---

### 3.3.1 Compute Centrality Measures

**⚙️ Code cell purposes:**  
- Computes five centrality measures for all supplier nodes (adjudicatários): in-degree, total contracts, total contract value (€), PageRank, betweenness centrality  

**📊 Textual outputs / results:**
```
Centrality measures computed for 5,338 companies.
```

---

### 3.3.2 Top-10 Companies by Each Measure (Full Network — 6,436 nodes)

**📊 Textual outputs / results:**

**By In-Degree** (number of distinct buyers served):
| Rank | Company | In-Degree |
|---|---|---|
| 1 | Claranet II Solutions | 53 |
| 2 | Base2 | 39 |
| 3 | Exumas Consulting Group | 34 |
| 4 | Nautilus | 32 |
| 5 | Sogenave – Soc. Geral de Abastecimentos | 32 |
| 6 | Servisan Produtos de Higiene | 32 |
| 7 | MEO Serviços de Comunicações e Multimédia | 30 |
| 8 | Exitus Soluções Tecnológicas | 29 |
| 9 | Petrogal | 29 |
| 10 | Inetum España Sucursal em Portugal | 28 |

**By Total Contracts** (number of contracts won):
| Rank | Company | Contracts |
|---|---|---|
| 1 | Sogenave | ~132 |
| 2 | Claranet II Solutions | 118 |
| 3 | Exumas Consulting Group | 87 |
| 4 | B. Braun Medical | 76 |
| 5 | Vanibru Comércio de Produtos Alimentares | 73 |
| 6 | Base2 | 52 |
| 7 | Petrogal | 51 |
| 8 | MEO Serviços de Comunicações e Multimédia | 50 |
| 9 | TMLJ Facility Services | 46 |
| 10 | Medtronic Portugal | 45 |

**By Total Value (€)**:
| Rank | Company | Total Value |
|---|---|---|
| 1 | MEO Serviços de Comunicações e Multimédia | ~28M € |
| 2 | Yutong France | 23,430,000 € |
| 3 | SAS Yutong France | 22,518,600 € |
| 4 | Iberdrola Clientes Portugal Unipessoal | ~20M € |
| 5 | Claranet II Solutions | 16,863,405 € |
| 6 | Gertal – Companhia Geral de Restaurantes | ~16M € |
| 7 | Lactogal Produtos Alimentares | 15,323,406 € |
| 8 | Stellantis Portugal | 15,290,320 € |
| 9 | Petrogal | 14,691,034 € |
| 10 | Timestamp Sistemas de Informação | 14,368,687 € |

**By PageRank** (prestige/influence from contracting entity importance):
| Rank | Company | PageRank |
|---|---|---|
| 1 | Porto Editora | 0.0024 |
| 2 | Uniself – Soc. de Restaurantes Públicos | ~0.0022 |
| 3 | Claranet II Solutions | 0.0012 |
| 4 | BCN Sistemas de Escritório e Imagem | 0.0012 |
| 5 | Gertal | ~0.0011 |
| 6 | Euroessen Restauração e Serviços | 0.0009 |
| 7 | Nautilus | 0.0008 |
| 8 | MEO Serviços de Comunicações e Multimédia | ~0.0008 |
| 9 | Warpcom Services | 0.0008 |
| 10 | Crayon Software Licensing | 0.0007 |

**By Betweenness** (structural bridging between buyer clusters):
| Rank | Company | Note |
|---|---|---|
| 1 | Instituto Nacional de Saúde Dr. Ricardo Jorge | Public institution |
| 2 | Instituto Superior de Engenharia do Porto | Public institution |
| 3–10 | Universidades, INATEL, SUCH, INA | Public institutions / universities |

> *(Note: Betweenness top-10 in the full network is dominated by public institutions, reflecting their role as connectors. Supplier-side betweenness is better captured in the co-contracting projection — Section 6.)*

---

### 3.3.3 Dominant Companies: Multi-Ranking Analysis

**📝 Explanatory text (CENTRALITY DISCUSSION):**  
> *What makes a company "dominant" in public procurement?*  
> Dominance is assessed through a **multi-dimensional lens**:  
> 1. **Volume dominance** — high in-degree / many contracts (wins frequently)  
> 2. **Value dominance** — high total € (captures largest contracts)  
> 3. **Structural dominance** — high betweenness / high PageRank (bridges market segments, connected to important entities)  
>
> Companies appearing in multiple rankings are **structurally dominant** — they don't just win many contracts; they occupy critical positions in the procurement network. These firms:
> - Have diversified client portfolios (multiple public entities)
> - May have preferential access or specialised capabilities
> - Act as **gatekeepers** between different sectors of the market

---

## 3.4 Why Are Companies Specialised?

---

### 3.4.1 CPV – Company Network

**📝 Explanatory text:**  
Constructs a bipartite network linking **top companies** to their **CPV product/service categories** to reveal sectoral specialisation patterns.

**⚙️ Code cell purposes:**  
- Filters to top companies by contract volume  
- Builds CPV-company bipartite graph  
- Exports to Gephi format (`.gephi`)  

**📊 Textual outputs / results:**
```
Top companies selected: 1,067
Contracts retained:     7,761
Nodes: 1,098
Edges: 7,761
→ Exported: cpv_network.gephi
```

---

### 3.4.2 City – Company Network

**📝 Explanatory text:**  
Constructs a bipartite network linking **top companies** to **cities** (geographic locations of contracting entities) to reveal regional specialisation.

**⚙️ Code cell purposes:**  
- Builds city-company bipartite graph (top companies)  
- Exports to GEXF format for Gephi visualisation

**📊 Textual outputs / results:**
```
Top companies selected: 1,067
Contracts retained:     7,761
Nodes: 1,289
Edges: 6,418
→ Exported: city_company_network_top20.gexf
```

---

# 4. Random Reference Models

---

## 4.1 Generate Random Reference Models

**📝 Explanatory text:**  
To determine whether observed network properties are **statistically non-trivial**, the empirical network is compared to:
- **Erdős–Rényi (ER) random graph** — same N and L, random rewiring  
- **Configuration model** — same degree sequence as empirical, random wiring

**⚙️ Code cell purposes:**  
- Generates 5 realisations of ER and Configuration model graphs  
- Computes same metrics for each and averages across realisations  
- Tabulates empirical vs. random comparison

**📊 Textual outputs / results:**

| Metric | **Empirical** | ER Random (avg) | Config Model (avg) |
|---|---|---|---|
| N | 6,436 | 6,436.0 | 6,436.0 |
| L | 10,995 | 10,995.0 | 10,885.1 |
| Density | 0.0003 | 0.0003 | 0.0003 |
| Avg Degree | 3.4167 | 3.4167 | 3.3826 |
| **Avg Path Length** | **5.0737** | **7.1900** | **4.7978** |
| Clustering Coeff. | 0.0000 | 0.0004 | 0.0001 |
| Transitivity | 0.0000 | 0.0005 | 0.0001 |
| **Components** | **113** | **223.5** | **134.4** |
| **Largest CC (%)** | **95.96%** | **96.31%** | **95.42%** |

> **Key takeaways**:
> - **Path length (5.07)** is **notably shorter** than ER (7.19) → the real network has "small-world" efficiency that random graphs lack.
> - **Clustering ≈ 0** in all models — consistent with bipartite structure.
> - **Fewer components** in empirical (113) vs. ER (224) → real procurement network is **better integrated** than chance would predict.
> - [chart/figure present — comparison bar charts]

---

# 5. Community Detection & Modularity

---

## 5.1 Bipartite Projection → Company Co-Contracting Network

**📝 Explanatory text:**  
To study supplier-to-supplier relationships, the bipartite buyer-supplier graph is **projected** onto the supplier layer. Two companies are connected if they have **shared a common buyer** — i.e., they "co-contracted" with the same public entity.

**⚙️ Code cell purposes:**  
- Extracts giant component subgraph  
- Creates bipartite projection onto company (adjudicatário) nodes

**📊 Textual outputs / results:**
```
Entity nodes (adjudicantes + both roles): 129
Company nodes (adjudicatários):           435
Bipartite graph: 564 nodes, 565 edges
```

---

## 5.2 Company Projection (Co-Contracting Network)

**⚙️ Code cell purposes:**  
- Projects bipartite graph onto company layer (weighted by number of shared buyers)  
- Removes isolated nodes (no shared buyers)  

**📊 Textual outputs / results:**
```
Company co-contracting network:
  Nodes:                      412
  Edges:                    3,849
  Isolated companies removed:  23
  Density:                 0.04546   (much denser than bipartite)
  Avg clustering:          0.8762    (very high — dense cliques)
```

> **Key takeaway**: Avg clustering of **0.876** is very high — companies co-cluster tightly by buyer. If A and B both supply to entity X, and A also supplies to Y, then B very likely also supplies to Y.

---

## 5.3 Louvain Community Detection

**⚙️ Code cell purposes:**  
- Applies the Louvain algorithm to the co-contracting projection  
- Extracts partition and computes modularity Q  

**📊 Textual outputs / results:**
```
Louvain Community Detection Results:
  Number of communities: 28
  Modularity Q:          0.6464
  (Q > 0.3 suggests significant community structure)
```

> **Key takeaway**: **Q = 0.646** is well above the 0.3 threshold. The market is divided into **28 distinct communities** of co-contracting companies.

---

## 5.4 Modularity vs. Random Reference

**⚙️ Code cell purposes:**  
- Generates multiple random graph realisations  
- Applies Louvain to each and computes z-score vs. empirical Q

**📊 Textual outputs / results:**
```
Modularity Comparison:
  Empirical Q:              0.6464
  Random Q (mean ± std):    0.1984 ± 0.0039
  Z-score:                  114.13

  → Empirical modularity is SIGNIFICANTLY higher than random
```

> **Key takeaway**: Z-score of **114** — community structure is not a random artefact. The procurement market is **genuinely and strongly segmented** into distinct supplier groups.

---

## 5.5 Community Size Distribution

**📊 Textual outputs / results:**
```
Community size statistics:
  Largest community:  61 companies
  Smallest community:  2 companies
  Mean size:          14.7 companies
  Median size:         5.5 companies
```

> [chart/figure present — community size distribution]

---

## 5.6 Community Characterization

**⚙️ Code cell purposes:**  
- Labels each community with: size, top company, dominant CPV sector, dominant city, total contract value, internal density

**📊 Textual outputs / results — All 28 Communities:**

| Comm. | Size | Top Company | Dominant Sector (CPV) | Dominant City | Total Value (€) | Int. Density |
|---|---|---|---|---|---|---|
| 0 | 61 | Vneto Soluções | Alimentação, bebidas e tabaco | Lisboa | 4,703,400 | 0.968 |
| 1 | 4 | Caravela Cia. de Seguros | Finanças e seguros | Lisboa | 238,451 | 1.000 |
| 2 | 3 | Wavecom Soluções Rádio | Equip. escritório e informática | Oeiras | 186,301 | 1.000 |
| 3 | 50 | Contenur Portugal | Equipamento de transporte | Sintra | 7,749,412 | 0.242 |
| 4 | 44 | Megabarcelos Informática | Equip. escritório e informática | Lisboa | 9,571,314 | 0.206 |
| **5** | **52** | **Claranet II Solutions** | **Software e sistemas de informação** | **Lisboa** | **16,805,138** | **0.282** |
| **6** | **56** | **Papelprint** | **Equip. escritório e informática** | **Lisboa** | **10,054,670** | **0.168** |
| 7 | 4 | Sibafil | Construção | Amadora | 2,570,167 | 1.000 |
| 8 | 16 | Cosmotriangular | Construção | Lisboa | 1,633,183 | 1.000 |
| 9 | 15 | VWR International Mat. Lab. | Equip. médico e farmacêutico | Lisboa | 589,900 | 1.000 |
| 10 | 14 | Medline International Portugal | Equip. médico e farmacêutico | Cascais | 472,588 | 1.000 |
| 11 | 28 | JMC Cleaning Services | Construção | Lisboa | 3,211,881 | 0.413 |
| 12 | 3 | WRDN Serviços de Manutenção | Mobiliário e limpeza | Lisboa | 71,119 | 1.000 |
| 13 | 6 | NAN Audiovisuais | Equip. elétrico e iluminação | Lisboa | 668,664 | 0.733 |
| 14 | 9 | HCCM Consulting | Software e sistemas de informação | Lisboa | 3,013,030 | 0.667 |
| 15 | 3 | Meristema | Agricultura e serv. relacionados | Sintra | 308,408 | 1.000 |
| 16 | 8 | União para Acção Cultural e Juvenil | Transporte | Lisboa | 462,068 | 1.000 |
| 17 | 8 | Armasul – Dist. Mat. Elétricos | Software e sistemas de informação | Lisboa | 2,788,625 | 1.000 |
| 18 | 3 | Hewlett Packard | Software e sistemas de informação | Lisboa | 258,068 | 1.000 |
| 19 | 6 | Dragondisplay | Ambiente e resíduos | Lisboa | 381,657 | 1.000 |
| 20 | 2 | Litovale | Material impresso | Lisboa | 373,341 | 1.000 |
| 21 | 2 | Construções Pragosa | Construção | Sobral de Monte Agraço | 820,961 | 1.000 |
| 22 | 2 | Avia Travel & Events | Serviços auxiliares de transporte | Lisboa | 238,570 | 1.000 |
| 23 | 2 | Nortel Equip. Hoteleiros | Mobiliário e limpeza | Lisboa | 278,426 | 1.000 |
| 24 | 5 | Euphoric Flash | Telecomunicações | Alenquer | 323,202 | 1.000 |
| 25 | 2 | Oceano Franzino | Serviços auxiliares de transporte | Lisboa | 82,025 | 1.000 |
| 26 | 2 | Novo Corpo Exercício Físico | Equip. escritório e informática | Lisboa | 120,180 | 1.000 |
| 27 | 2 | RHMais | Finanças e seguros | Lisboa | 221,280 | 1.000 |

> **Key takeaways**:
> - **Community 5** (Claranet-led, IT/software, Lisboa, €16.8M) is the **highest-value community**.
> - Many small communities (size 2–3) have internal density = 1.0 (fully connected cliques) — tight niche groups.
> - **Lisboa dominates** geographically across almost all communities.
> - The 5 largest communities (0, 3, 4, 5, 6) account for the majority of aggregate contract value.

---

## 5.7 Inter-Community Connections & Bridge Companies

**⚙️ Code cell purposes:**  
- Identifies edges crossing community boundaries  
- Computes betweenness centrality on the co-contracting projection  
- Ranks top-10 companies by betweenness (bridge role)

**📊 Textual outputs / results — Top-10 Bridge Companies:**

| # | Company | Betweenness | Community |
|---|---|---|---|
| 1 | **Exitus Soluções Tecnológicas** | **0.1661** | 5 |
| 2 | Claranet II Solutions | 0.0979 | 5 |
| 3 | Avvale | 0.0970 | 3 |
| 4 | Planeta Vertical | 0.0932 | 5 |
| 5 | Inetum España Sucursal em Portugal | 0.0552 | 6 |
| 6 | Ohmtécnica Representações de Marcas | 0.0469 | 5 |
| 7 | MEO Serviços de Comunicações e Multimédia | 0.0451 | 5 |
| 8 | Código Azul | 0.0447 | 0 |
| 9 | Smile Viagens e Turismo | 0.0398 | 0 |
| 10 | Barraqueiro Transportes | 0.0345 | 3 |

> **Key takeaway**: **Community 5** (IT/software) provides 5 of the top 10 bridge companies. **Exitus Soluções Tecnológicas** is the #1 bridge (betweenness 0.166) — far ahead of the others — connecting otherwise distinct market segments.  
> [chart/figure present — inter-community heatmap]

---

## 5.8 Inter-Community Heatmap

**📝 Explanatory text (MODULARITY INSIGHTS & DISCUSSION):**

> **Expectation**: In a competitive market, we'd expect low modularity (Q < 0.3) — companies compete broadly. High modularity indicates **market segmentation** where groups of firms specialise in serving specific clusters of public entities.
>
> **Observations**:
> - Empirical Q **significantly exceeds** the random baseline (z = 114) → **real community structure exists**
> - Communities correspond to **market segments** — IT services, construction, food supply, medical equipment, transport
> - **Bridge companies** (high betweenness) operate across multiple segments → these are candidates for "dominant position"
> - Portuguese procurement is **segmented by sector and geography**, not uniformly competitive
>
> **Answer to RQ (partial)**:
> 1. **Dominate within** their community (high internal degree/strength)
> 2. **Bridge across** communities (high betweenness) — these have **diversified market access**

> [chart/figure present — inter-community edge heatmap]

---

# 6. Centrality Analysis

*(Repeats centrality analysis specifically on the **co-contracting projection** network — supplier-vs-supplier view of dominance, complementing Section 3.3 which used the full bipartite graph)*

---

## 6.1 Compute Centrality Measures

**⚙️ Code cell purposes:**  
- Computes in-degree, total contracts, total value (€), PageRank, and betweenness for all nodes in the co-contracting projection

**📊 Textual outputs / results:**
```
Centrality measures computed for 436 companies.
```

---

## 6.2 Top-10 Companies by Each Measure (Co-Contracting Projection — 412 nodes)

**By In-Degree** (co-contracting partners):
| Rank | Company | In-Degree |
|---|---|---|
| 1 | Claranet II Solutions | 14 |
| 2 | Exitus Soluções Tecnológicas | 7 |
| 3 | Inetum España Sucursal em Portugal | 6 |
| 4 | Ohmtécnica Representações de Marcas | 6 |
| 5 | Timestamp Sistemas de Informação | 5 |
| 6 | Papelprint | 5 |
| 7 | Claranet Portugal | 4 |
| 8 | Base2 | 4 |
| 9 | Planeta Vertical | 4 |
| 10 | Digiberia Information Technologies | 3 |

**By Total Contracts**:
| Rank | Company | Contracts |
|---|---|---|
| 1 | Claranet II Solutions | 21 |
| 2 | CPCEcho | 16 |
| 3 | Antero Lopes | 10 |
| 4 | Exitus Soluções Tecnológicas | 7 |
| 5 | Ohmtécnica Representações de Marcas | 7 |
| 6–9 | Timestamp / Digiberia / Inetum / Papelprint | 6 each |

**By Total Value (€)**:
| Rank | Company | Total Value |
|---|---|---|
| 1 | Paldata | 2,999,800 € |
| 2 | Claranet II Solutions | 2,867,339 € |
| 3 | Inetum España Sucursal em Portugal | 2,734,017 € |
| 4 | NOS Comunicações | 2,210,995 € |
| 5 | Warpcom Services | 2,201,029 € |
| 6 | MEO Serviços de Comunicações e Multimédia | ~2.1M € |
| 7 | HCCM Consulting | 1,566,521 € |
| 8 | Vodafone Portugal | ~1.17M € |
| 9 | Fujitsu Technology Solutions | 1,107,248 € |
| 10 | Reload Consultoria Informática | 964,522 € |

**By PageRank**:
| Rank | Company | PageRank |
|---|---|---|
| 1 | Claranet II Solutions | 0.00658 |
| 2 | Timestamp Sistemas de Informação | 0.00465 |
| 3 | Inetum España Sucursal em Portugal | 0.00437 |
| 4 | Ohmtécnica Representações de Marcas | 0.00368 |
| 5 | Multimac Hito Innovation | 0.00357 |
| 6 | Reload Consultoria Informática | 0.00346 |

---

## 6.3 Dominant Companies: Appearing Across Multiple Rankings

**📊 Textual outputs / results — 11 companies in Top-10 across 2+ measures:**

| Rank | Company | Appearances (of 5) | In-Degree | Contracts | Value (€) | PageRank | Community |
|---|---|---|---|---|---|---|---|
| **1** | **Claranet II Solutions** | **5 / 5** | 14 | 21 | 2,867,339 | 0.00658 | 5 |
| 2 | Inetum España Sucursal em Portugal | 4 / 5 | 6 | 6 | 2,734,017 | 0.00437 | 6 |
| 3 | Timestamp Sistemas de Informação | 4 / 5 | 5 | 6 | 749,051 | 0.00465 | 5 |
| 4 | Ohmtécnica Representações de Marcas | 3 / 5 | 6 | 7 | 21,285 | 0.00368 | 5 |
| 5 | Digiberia Information Technologies | 3 / 5 | 3 | 6 | 463,525 | 0.00276 | 6 |
| 6 | HCCM Consulting | 3 / 5 | 3 | 3 | 1,566,521 | 0.00337 | 14 |
| 7 | Papelprint | 2 / 5 | 5 | 6 | 82,710 | 0.00298 | 6 |
| 8 | Claranet Portugal | 2 / 5 | 4 | 4 | 461,788 | 0.00321 | 11 |
| 9 | Exitus Soluções Tecnológicas | 2 / 5 | 7 | 7 | 356,967 | 0.00227 | 5 |
| 10 | Warpcom Services | 2 / 5 | 3 | 5 | 2,201,029 | 0.00334 | 5 |
| 11 | Reload Consultoria Informática | 2 / 5 | 3 | 5 | 964,522 | 0.00346 | 5 |

> **Key takeaway**: **Claranet II Solutions** is the **only company in all 5 top-10 rankings** — unambiguously the dominant firm. **Inetum España** and **Timestamp** appear in 4/5. Top 3 are all IT companies in Communities 5/6.

---

# 7. Time Dependence

---

## 7.1 Temporal Evolution of N and L

**📝 Explanatory text (DISCUSSION):**

> The cumulative growth of nodes N(t) and edges L(t) reveals market dynamics:
> - **N(t) sub-linear, L(t) linear** → **concentration** (existing players accumulate contracts)
> - **Both grow proportionally** → **expansion** (new entrants compete)
> - **Rising L/N ratio** → denser, more interconnected network over time

**⚙️ Code cell purposes:**  
- Groups contracts by year, computes cumulative node and edge count over time  
- Plots N(t), L(t) trajectories and L/N ratio  

> [chart/figure present — temporal evolution of N and L]  
> *(No printed numerical table outputs — visual results only)*

---

# 8. Conclusions & Key Findings

*(Section header exists; markdown body and code cells are placeholder / not yet completed in the notebook. Substantive analytical conclusions are embedded in the discussion blocks of Sections 3.3.3, 5.8, and 6.3 above.)*

---

# 📌 Consolidated Key Findings for Business-Level Conclusions

| Theme | Finding |
|---|---|
| **Dataset** | 16,989 contracts; 6,436 unique entities (buyers + suppliers) |
| **Network size** | 6,436 nodes, 10,995 directed edges; 96% in one giant connected component |
| **Sparsity** | Density = 0.000265 (extremely sparse; bipartite structure) |
| **Concentration** | Top 5% of suppliers capture **51.8%** of contract value; Gini = **0.769** |
| **HHI** | 20.65 → no monopolist, but highly skewed distribution |
| **Scale-free?** | In-degree: α = 2.97 (consistent with power law); out-degree: rejected |
| **Random comparison** | Real network: shorter paths (5.07 vs 7.19 ER), fewer components (113 vs 224) |
| **Community structure** | **28 communities**, Q = **0.646** (z = 114 vs. random) — highly significant segmentation |
| **Market segmentation** | Communities cluster by sector (IT, food, construction, medical) and geography (Lisboa dominant) |
| **Most dominant company** | **Claranet II Solutions** — #1 in 5/5 rankings in co-contracting network; in-degree 53 in full network; €16.9M total value |
| **Top bridge companies** | Exitus Soluções Tecnológicas (betweenness 0.166), Claranet II Solutions, Avvale, Planeta Vertical |
| **IT sector dominance** | Community 5 (software/IT, Claranet-led, Lisboa) is highest-value community (€16.8M) and provides most cross-community bridges |
| **Raw value leaders** | MEO (~€28M), Yutong France (€23.4M), Iberdrola (~€20M) top by raw €, but less structurally central |
| **Temporal** | Cumulative growth of N vs L indicates market dynamics (visual — not printed); discussion suggests tracking concentration vs. expansion |