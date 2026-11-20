"""
Load the email-Eu-core networks following the group's construction rules.

Put the two SNAP files (still .gz, no need to unzip) in a folder called
`data` next to this file:
    data/email-Eu-core.txt.gz
    data/email-Eu-core-department-labels.txt.gz

Rules: directed, unweighted (u -> v if u sent >= 1 e-mail to v),
self-loops removed, isolated nodes kept, department stored as node attribute "dept".

Department networks: for each of the N_DEPTS largest departments, the subgraph
induced by its members (only e-mails where sender AND receiver belong to that
department). Node IDs are the same as in the whole network.
"""
import gzip
from collections import Counter
from pathlib import Path

import networkx as nx

DATA = Path(__file__).parent / "data"
SEED = 42
N_DEPTS = 4  # number of largest departments analysed as separate networks


def _open(path):
    path = Path(path)
    return gzip.open(path, "rt") if path.suffix == ".gz" else open(path)


def load_whole():
    """Whole institution network with department labels."""
    G = nx.DiGraph()
    with _open(DATA / "email-Eu-core-department-labels.txt.gz") as f:
        for line in f:
            if line.strip():
                node, dept = map(int, line.split())
                G.add_node(node, dept=dept)
    with _open(DATA / "email-Eu-core.txt.gz") as f:
        for line in f:
            if line.strip():
                u, v = map(int, line.split()[:2])
                G.add_edge(u, v)
    G.remove_edges_from(list(nx.selfloop_edges(G)))
    return G


def largest_departments(G, k=N_DEPTS):
    """IDs of the k largest departments (ties broken by department ID)."""
    sizes = Counter(d for _, d in G.nodes(data="dept"))
    return [d for d, _ in sorted(sizes.items(), key=lambda x: (-x[1], x[0]))[:k]]


def dept_network(G, dept):
    """Subgraph induced by the members of one department."""
    members = [n for n, d in G.nodes(data="dept") if d == dept]
    return G.subgraph(members).copy()


def load_all():
    """Dict with the whole network plus the N_DEPTS largest department networks."""
    G = load_whole()
    nets = {"whole": G}
    for dept in largest_departments(G):
        nets[f"dept{dept}"] = dept_network(G, dept)
    return nets


if __name__ == "__main__":
    # Quick check: run `python load_networks.py`
    for name, H in load_all().items():
        print(f"{name:7s}  nodes={H.number_of_nodes():5d}  edges={H.number_of_edges():6d}")
