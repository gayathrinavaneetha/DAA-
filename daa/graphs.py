"""Graph algorithms: MST (Prim, Kruskal, Boruvka), Floyd-Warshall, colouring."""

import sys
from itertools import count
from typing import Dict, List, Tuple

INF = float('inf')


def prims_mst(graph: List[List[int]]) -> List[Tuple[int, int, int]]:
    """Prim's MST from an adjacency matrix. Returns ``(u, v, weight)`` edges."""
    num_vertices = len(graph)
    selected = [False] * num_vertices
    selected[0] = True
    edges: List[Tuple[int, int, int]] = []
    for _ in range(num_vertices - 1):
        minimum = sys.maxsize
        x = y = 0
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j] and minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x, y = i, j
        edges.append((x, y, minimum))
        selected[y] = True
    return edges


class DisjointSet:
    """Union-Find with path compression and union by rank."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


def kruskal(n: int, edges: List[Tuple[int, int, int]]):
    """Kruskal's MST. Returns ``(mst_edges, total_cost)``."""
    ds = DisjointSet(n)
    mst: List[Tuple[int, int, int]] = []
    total_cost = 0
    for u, v, weight in sorted(edges, key=lambda x: x[2]):
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
    return mst, total_cost


def boruvka(edges: List[Tuple[int, int, int]], num_vertices: int):
    """Boruvka's MST. Returns ``(mst_edges, total_cost)``."""
    ds = DisjointSet(num_vertices)
    mst_edges: List[Tuple[int, int, int]] = []
    total_cost = 0
    num_components = num_vertices
    while num_components > 1:
        cheapest: List = [-1] * num_vertices
        for u, v, weight in edges:
            set_u, set_v = ds.find(u), ds.find(v)
            if set_u != set_v:
                if cheapest[set_u] == -1 or cheapest[set_u][2] > weight:
                    cheapest[set_u] = (u, v, weight)
                if cheapest[set_v] == -1 or cheapest[set_v][2] > weight:
                    cheapest[set_v] = (u, v, weight)
        progressed = False
        for entry in cheapest:
            if entry != -1:
                u, v, weight = entry
                if ds.find(u) != ds.find(v):
                    ds.union(u, v)
                    mst_edges.append((u, v, weight))
                    total_cost += weight
                    num_components -= 1
                    progressed = True
        if not progressed:
            break
    return mst_edges, total_cost


def floyd_warshall(n: int, edges: List[List[int]]) -> List[List[float]]:
    """All-pairs shortest paths on an undirected graph via Floyd-Warshall."""
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def _adjacency_list(edges: List[Tuple[int, int]], n: int) -> List[List[int]]:
    graph: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def _is_safe(graph: List[List[int]], color: List[int], v: int, c: int) -> bool:
    return all(color[neighbor] != c for neighbor in graph[v])


def _color_util(graph: List[List[int]], m: int, color: List[int], v: int) -> bool:
    if v == len(graph):
        return True
    for c in range(1, m + 1):
        if _is_safe(graph, color, v, c):
            color[v] = c
            if _color_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False


def min_colors(edges: List[Tuple[int, int]], n: int) -> int:
    """Minimum number of colours needed for a proper colouring of the graph."""
    graph = _adjacency_list(edges, n)
    for m in count(1):
        if _color_util(graph, m, [0] * len(graph), 0):
            return m
    raise AssertionError("unreachable")
