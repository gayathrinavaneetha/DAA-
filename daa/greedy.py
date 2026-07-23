"""Greedy / optimisation problems: OBST, vertex cover, assignment, Huffman codes."""

from itertools import permutations
from typing import Dict, List, Tuple


def optimal_bst(keys: List, freq: List[float]):
    """Optimal binary search tree cost/root tables via dynamic programming.

    Returns ``(cost, root)`` matrices; the optimal cost is ``cost[0][n-1]``.
    """
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            sum_freq = sum(freq[k] for k in range(i, j + 1))
            for r in range(i, j + 1):
                current = ((cost[i][r - 1] if r > i else 0)
                           + (cost[r + 1][j] if r < j else 0) + sum_freq)
                if current < cost[i][j]:
                    cost[i][j] = current
                    root[i][j] = r
    return cost, root


def vertex_cover(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """2-approximation vertex cover: add both endpoints of each uncovered edge."""
    cover = set()
    covered_edges = set()
    for u, v in edges:
        if (u, v) not in covered_edges and (v, u) not in covered_edges:
            cover.add(u)
            cover.add(v)
            covered_edges.add((u, v))
            covered_edges.add((v, u))
    return sorted(cover)


def vertex_cover_max_degree(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """Greedy vertex cover repeatedly picking the maximum-degree vertex."""
    cover = set()
    edge_set = set(edges)
    while edge_set:
        degree: Dict[int, int] = {}
        for u, v in edge_set:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        max_vertex = max(degree, key=degree.get)
        cover.add(max_vertex)
        edge_set = {edge for edge in edge_set if max_vertex not in edge}
    return sorted(cover)


def assignment_problem(cost_matrix: List[List[int]]) -> Tuple[Tuple[int, ...], int]:
    """Brute-force assignment problem. Returns ``(best_assignment, min_cost)``."""
    num_workers = len(cost_matrix)
    min_cost = float('inf')
    best_assignment: Tuple[int, ...] = ()
    for perm in permutations(range(num_workers)):
        current = sum(cost_matrix[i][perm[i]] for i in range(num_workers))
        if current < min_cost:
            min_cost = current
            best_assignment = perm
    return best_assignment, min_cost


def build_huffman_codes(characters: List[str], frequencies: List[int]) -> Dict[str, str]:
    """Assign codes to characters ordered by frequency (as in the coursework)."""
    ordered = sorted(zip(characters, frequencies), key=lambda x: x[1])
    return {char: bin(i)[2:] for i, (char, _) in enumerate(ordered)}


def decode_huffman(encoded_string: str, code_dict: Dict[str, str]) -> str:
    """Decode ``encoded_string`` using the mapping produced above."""
    reversed_dict = {v: k for k, v in code_dict.items()}
    decoded_message = ""
    current_code = ""
    for bit in encoded_string:
        current_code += bit
        if current_code in reversed_dict:
            decoded_message += reversed_dict[current_code]
            current_code = ""
    return decoded_message
