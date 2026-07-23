"""Shared utilities for the DAA algorithm exercises.

Several exercises in this repository re-implemented the same algorithms with
identical (copy-pasted) code. This module collects a single implementation of
each recurring pattern so the individual exercise scripts can import it instead
of duplicating the logic.

The functions keep the exact behaviour of the original snippets so the expected
outputs recorded alongside each exercise remain unchanged.
"""

import sys


# --- Disjoint Set (Union-Find) --------------------------------------------
# Duplicated across the Boruvka's / Kruskal's minimum-spanning-tree exercises.

def find(parent, u):
    """Return the representative of u's set, applying path compression."""
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]


def union(parent, rank, u, v):
    """Merge the sets containing u and v using union by rank."""
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    elif rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        rank[root_u] += 1


# --- Prim's minimum spanning tree -----------------------------------------
# Duplicated between the "prims algorithm" exercises.

def prims_mst(graph):
    """Return the MST edges ``(u, v, weight)`` of a weighted adjacency matrix.

    A ``0`` entry in ``graph`` means "no edge" between the two vertices.
    """
    num_vertices = len(graph)
    selected_nodes = [False] * num_vertices
    selected_nodes[0] = True
    edges = []
    for _ in range(num_vertices - 1):
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(num_vertices):
            if selected_nodes[i]:
                for j in range(num_vertices):
                    if not selected_nodes[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        edges.append((x, y, minimum))
        selected_nodes[y] = True
    return edges


def print_weighted_edges(edges, header="Edges in the Minimum Spanning Tree:"):
    """Print a list of ``(u, v, weight)`` edges in a readable form."""
    print(header)
    for u, v, weight in edges:
        print(f"{u} - {v} with weight {weight}")


# --- Sudoku solver ---------------------------------------------------------
# Duplicated between the two "Sudoku solver" exercises.

def solve_sudoku(board):
    """Solve a 9x9 Sudoku board in place using backtracking.

    Empty cells are ``'.'`` and filled cells are the characters ``'1'``-``'9'``.
    Returns ``True`` if the board was solved.
    """
    def is_valid(num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = '.'
                    return False
        return True

    return solve()


# --- N-Queens --------------------------------------------------------------
# Duplicated between the "8 queens" / "restricted position" exercises.

def queen_is_safe(board, row, col):
    """Return True if a queen can sit at ``board[row][col]`` given a
    column-by-column placement (checks the row and the two left diagonals)."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board, col):
    """Place queens column by column starting at ``col``; True on success."""
    if col >= len(board[0]):
        return True
    for i in range(len(board)):
        if queen_is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def place_n_queens(rows, cols):
    """Attempt to place queens on a ``rows`` x ``cols`` board.

    Returns the 1-based row numbers that hold a queen, or ``[]`` if there is no
    valid placement.
    """
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    if solve_n_queens(board, 0):
        return [i + 1 for i in range(rows) if 1 in board[i]]
    return []


# --- Optimal Binary Search Tree -------------------------------------------
# Duplicated across the "OBST" / "optimal cost" exercises.

def optimal_bst(keys, freq):
    """Build the optimal binary-search-tree cost and root tables.

    Returns ``(cost, root)`` where ``cost[0][n-1]`` is the optimal cost and
    ``root[i][j]`` is the chosen root for the sub-range ``keys[i..j]``.
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
            total_freq = sum(freq[k] for k in range(i, j + 1))
            for r in range(i, j + 1):
                current_cost = (cost[i][r - 1] if r > i else 0) + \
                               (cost[r + 1][j] if r < j else 0) + total_freq
                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost
                    root[i][j] = r

    return cost, root
