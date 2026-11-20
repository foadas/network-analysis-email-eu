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
load_networks.py                  shared loader: everyone uses it to build the same networks
notebooks/
  NA_01_structure_RQ1.ipynb       RQ1 (Section 5.1): network structure, small-world, degree distribution
report/
  main.tex                        report (LaTeX, official template, 3cm margins)
  degree_distribution.png         Figure 1
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

## How to use the shared loader (Google Colab)

Put this in the first cell of your notebook:

```python
# Download the data and the shared loader
!mkdir -p data
!wget -q -P data https://snap.stanford.edu/data/email-Eu-core.txt.gz
!wget -q -P data https://snap.stanford.edu/data/email-Eu-core-department-labels.txt.gz
!wget -q https://raw.githubusercontent.com/foadas/network-analysis-email-eu/main/load_networks.py
```

Then, in the next cell:

```python
from load_networks import SEED, load_all, load_whole

nets = load_all()      # {"whole": G, "dept4": ..., "dept14": ..., "dept1": ..., "dept21": ...}
G = nets["whole"]      # whole network, department of node n: G.nodes[n]["dept"]
```

Expected sizes: `whole` 1,005 nodes / 24,929 edges; `dept4` 109 / 1,167; `dept14` 92 / 1,506; `dept1` 65 / 502; `dept21` 61 / 601.

## Tools

Python with [NetworkX](https://networkx.org/) (measures), pandas, matplotlib; Gephi (figures).
