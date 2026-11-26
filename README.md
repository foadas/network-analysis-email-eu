# Formal Departments and Informal Communication

Group project for the **Network Analysis** course (University of Bologna, Prof. Saverio Giallorenzo).

We analyse the e-mail network of a European research institution
([SNAP email-Eu-core](https://snap.stanford.edu/data/email-Eu-core.html)) to compare
its official departments with the way people actually communicate.

## Research questions

- **RQ1:** What is the overall structure of the e-mail network, and do departments differ structurally?
- **RQ2:** Who are the central actors, and who bridges departments?
- **RQ3:** Are departments real boundaries of communication?

## Repository structure

```
load_networks.py                    shared loader: everyone uses it to build the same networks
notebooks/
  NA_01_structure_RQ1.ipynb         RQ1 (Section 5.1): structure, degree-preserving tests, triad census
  NA_02_RQ2.ipynb                   Section 3 dataset table + RQ2 (Section 5.2): centrality, bridges
  NA_03_RQ3.ipynb                   RQ3 (Section 5.3): departments as communication boundaries
report/
  report_full.tex / .pdf            the report (official template, 3cm margins) - MAIN FILE
  *.png                             figures
  main.tex, person2_sections.tex,
  person3_sections.tex              older drafts (merged into report_full.tex)
```

Data is **not** stored in the repo: the notebooks download it from SNAP.

## Network construction rules

| Rule | Choice |
|---|---|
| Nodes | members of the institution (1,005), with attribute `dept` (42 departments) |
| Edges | u → v if u sent at least one e-mail to v |
| Direction / weights | directed, unweighted |
| Self-loops | removed |
| Isolated nodes | kept |
| Undirected version (when needed) | OR rule: `G.to_undirected()` |
| Department networks | 4 largest departments (IDs 4, 14, 1, 21), each = subgraph induced by its members |
| Random seed | 42 |

## Tools

Python with [NetworkX](https://networkx.org/) 3.7 (measures, null models), scikit-learn (NMI, ARI), NumPy and pandas, matplotlib (figures).

## Hypothesis labels: report vs notebooks

| Report | Notebook |
|---|---|
| H1.1 small-world vs degree-preserving null | `NA_01_structure_RQ1.ipynb`, Step 10 |
| H1.2 reciprocity vs degree-preserving null | `NA_01_structure_RQ1.ipynb`, Step 10 |
| H3.1 members prefer their own department | `NA_03_RQ3.ipynb`, H1 |
| H3.2 departments more closed than chance (E–I) | `NA_03_RQ3.ipynb`, H3 |
| H3.3 communities vs departments | `NA_03_RQ3.ipynb`, H2 (+ H2b stability/resolution) |
| H3.4 reciprocity within vs between departments | `NA_03_RQ3.ipynb`, H5 |
| Members outside department LCC (in 5.1) | `NA_03_RQ3.ipynb`, H4 |
| Department pairs (descriptive) | `NA_03_RQ3.ipynb`, department pairs cell |
