
## Lisbon VS Portugal — How does the capital compare to the national network?

Lisbon is a **subset of the national dataset** (same 16,989-contract source, filtered to the 16 Lisbon-region municipalities), so the national notebook is our natural reference point. The question is whether the capital *amplifies* or *softens* the national patterns.

| Metric | **Lisbon** | **Portugal (national)** | Reading |
|---|---|---|---|
| Nodes (N) | 1,824 | 6,436 | Lisbon ≈ 28% of all players |
| Edges (L) | 2,432 | 10,995 | Lisbon ≈ 22% of all relationships |
| Density | 0.000731 | 0.000265 | **Lisbon ~2.8× denser** |
| Avg degree ⟨k⟩ | 2.67 | 3.42 | Slightly lower in Lisbon |
| Avg path length ⟨d⟩ | 4.97 | 5.07 | Almost identical (small-world holds) |
| Clustering C | 0.000 | 0.000 | Bipartite in both |
| Components | 48 | 113 | Fewer absolute, similar share |
| Largest CC | 93.8% | 96.0% | One giant market in both |
| Public entities | 299 | 1,109 | — |
| Companies | ~1,525 | ~5,327 | — |
| Gini — companies | 0.742 | 0.769 | Suppliers slightly **less** unequal in Lisbon |
| Gini — public entities | 0.809 | 0.750 | Buyers **more** unequal in Lisbon |
| Top 20% companies → value | 77.6% | 80.5% | Similar, slightly lower in Lisbon |
| Top 20% buyers → value | 85.5% | 78.6% | **Higher buyer concentration in Lisbon** |
| Power-law α (in-degree) | 2.54 | 2.97 | — |
| Power-law α (out-degree) | 2.26 | 1.92 | National buyer tail even heavier |
| Co-contracting projection | 1,487 nodes / 48.4k edges | 5,232 nodes / 247.5k edges | — |
| Avg clustering (projection) | 0.872 | 0.831 | Lisbon supplier cliques slightly tighter |
| Louvain communities | 19 | 32 | — |
| **Modularity Q** | **0.673** | **0.553** | **Lisbon is more cleanly segmented** |
| Random Q (Z-score) | 0.105 (Z≈269) | 0.090 (Z≈371) | Both far above chance |
| Largest community | 426 — **IT, Claranet** (€169.9M) | 1,133 — construction, "waste to me" (€486M) | Capital's biggest cluster is IT, not construction |
| #1 bridge company | claranet ii solutions | claranet ii solutions | Same firm leads both |


## **Structure**

- **Denser, equally navigable.** Lisbon holds ~28% of the national nodes but is **~2.8× denser** (0.00073 vs 0.00027). Even so, the average path length is essentially the same (**4.97 vs 5.07**) and the giant component is comparable (93.8% vs 96.0%) — the small-world, single-marketplace structure is a national property that the capital reproduces faithfully.
- **Same bipartite fingerprint.** Clustering is 0 in both, and in both cases the empirical ⟨d⟩ is far below the Erdős–Rényi reference (Lisbon 4.97 vs 7.49; Portugal 5.07 vs 7.19) — hub buyers and bridge firms compress distances at every scale.

## **Concentration & Dominance**

- **A revealing asymmetry.** On the **supplier** side Lisbon is *slightly less* concentrated than the country (Gini 0.742 vs 0.769; top-20% = 77.6% vs 80.5%) — the capital's larger pool of IT/services firms spreads value a little more. But on the **buyer** side Lisbon is *more* concentrated (Gini 0.809 vs 0.750; top-20% buyers = 85.5% vs 78.6%): a handful of big municipalities and institutions dominate demand in the capital even more than nationally.
- **Same faces at the top.** **Claranet II Solutions and MEO are dominant in both networks** — Claranet leads bridge-betweenness nationally *and* in Lisbon, and roughly **half of Claranet's national contract value (€8.7M of €16.9M) is concentrated in the Lisbon region**. The capital is where these IT champions consolidate their structural power.
- **Sector mix differs.** Nationally the heaviest single-firm winners include telecoms (MEO €28M), transport (Yutong) and energy (Iberdrola/Petrogal); in Lisbon the dominant *structural* players are squarely IT/software, with construction and medical equipment as the big value sectors.

## **Community Structure**

- **Lisbon is more cleanly segmented.** Despite being a quarter of the size, the Lisbon co-contracting network has **higher modularity (Q = 0.673 vs 0.553)** and tighter supplier cliques (avg clustering 0.872 vs 0.831). Filtering to one metropolitan region removes some of the cross-regional noise, leaving sharper sector-based communities.
- **The dominant cluster flips sector.** Nationally the largest community is construction ("waste to me", 1,133 firms, €486M); in **Lisbon the largest community is IT/software, led by Claranet II Solutions (426 firms, €169.9M)** — the capital is disproportionately an IT procurement hub.
- **Same connective tissue.** In both networks the top bridge companies are dominated by the IT cluster (Claranet, Timestamp, Exitus, Inetum, MEO), confirming that IT firms link otherwise-separate market segments at *every* geographic scale.

## **Key Takeaway**
*Lisbon = more concentrated buyers + more dominant IT suppliers + sharper communities (higher Q) than the country as a whole*