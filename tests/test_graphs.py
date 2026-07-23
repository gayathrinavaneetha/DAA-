import pytest

from daa.graphs import (
    DisjointSet,
    boruvka,
    floyd_warshall,
    kruskal,
    min_colors,
    prims_mst,
)

GRAPH_MATRIX = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

WEIGHTED_EDGES = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]


def test_prims_mst_total_weight():
    edges = prims_mst(GRAPH_MATRIX)
    assert len(edges) == len(GRAPH_MATRIX) - 1
    assert sum(w for _, _, w in edges) == 16


def test_kruskal_mst():
    mst, cost = kruskal(4, list(WEIGHTED_EDGES))
    assert cost == 19
    assert len(mst) == 3
    assert (2, 3, 4) in mst


def test_boruvka_matches_kruskal_cost():
    _, kruskal_cost = kruskal(4, list(WEIGHTED_EDGES))
    mst, cost = boruvka(list(WEIGHTED_EDGES), 4)
    assert cost == kruskal_cost
    assert len(mst) == 3


def test_disjoint_set_union_find():
    ds = DisjointSet(5)
    assert ds.find(0) != ds.find(1)
    ds.union(0, 1)
    ds.union(1, 2)
    assert ds.find(0) == ds.find(2)
    assert ds.find(3) != ds.find(0)
    # Union is idempotent.
    ds.union(0, 2)
    assert ds.find(0) == ds.find(2)


def test_floyd_warshall_shortest_paths():
    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    dist = floyd_warshall(n, edges)
    assert dist[2][0] == 5
    assert dist[0][3] == 5  # 0 -> 1 -> 4 -> 3 = 2 + 2 + 1
    for i in range(n):
        assert dist[i][i] == 0
    # Symmetric for an undirected graph.
    for i in range(n):
        for j in range(n):
            assert dist[i][j] == dist[j][i]


def test_floyd_warshall_disconnected():
    dist = floyd_warshall(2, [])
    assert dist[0][1] == float("inf")


@pytest.mark.parametrize(
    "edges, n, expected",
    [
        ([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 4, 3),
        ([(0, 1), (1, 2), (2, 3)], 4, 2),
        ([], 3, 1),
        ([(0, 1), (1, 2), (2, 0)], 3, 3),
    ],
)
def test_min_colors(edges, n, expected):
    assert min_colors(edges, n) == expected
