"""Lightweight self-tests for the shared utilities in ``daa_utils``.

Run with ``python3 test_daa_utils.py`` (no external test runner required).
"""

from daa_utils import (
    find,
    union,
    prims_mst,
    solve_sudoku,
    place_n_queens,
    optimal_bst,
)


def test_union_find():
    parent = list(range(5))
    rank = [0] * 5
    union(parent, rank, 0, 1)
    union(parent, rank, 1, 2)
    assert find(parent, 0) == find(parent, 2)
    assert find(parent, 3) != find(parent, 0)


def test_prims_mst():
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    edges = prims_mst(graph)
    assert edges == [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
    assert sum(w for _, _, w in edges) == 16


def test_solve_sudoku():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solve_sudoku(board) is True
    assert board[0] == ["5", "3", "4", "6", "7", "8", "9", "1", "2"]
    for row in board:
        assert sorted(row) == list("123456789")


def test_place_n_queens():
    # Classic 8x8 board has a solution.
    assert place_n_queens(8, 8) == [1, 2, 3, 4, 5, 6, 7, 8]
    # The 8x10 variant used in the exercises has no column-by-column placement.
    assert place_n_queens(8, 10) == []


def test_optimal_bst():
    keys = [10, 12, 16, 21]
    freq = [4, 2, 6, 3]
    cost, root = optimal_bst(keys, freq)
    assert cost[0][len(keys) - 1] == 26
    assert root[0][len(keys) - 1] == 2


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for test in tests:
        test()
        print(f"{test.__name__}: ok")
    print(f"\nAll {len(tests)} tests passed.")


if __name__ == "__main__":
    main()
