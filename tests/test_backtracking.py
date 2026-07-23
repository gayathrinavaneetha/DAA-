import pytest

from daa.backtracking import (
    combination_sum,
    combination_sum_ii,
    n_queens,
    permute,
    solve_sudoku,
    subsets,
    subsets_containing_element,
)


def _norm(list_of_lists):
    return sorted(tuple(x) for x in list_of_lists)


def test_permute_three_distinct():
    result = permute([1, 2, 3])
    assert len(result) == 6
    assert _norm(result) == _norm(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )


def test_permute_single_and_pair():
    assert permute([1]) == [[1]]
    assert _norm(permute([0, 1])) == _norm([[0, 1], [1, 0]])


def test_permute_does_not_mutate_input():
    data = [1, 2, 3]
    permute(data)
    assert data == [1, 2, 3]


def test_subsets_lexicographical():
    assert subsets([1, 2, 3]) == [
        [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
    ]


def test_subsets_count_is_power_of_two():
    assert len(subsets([1, 2, 3, 4])) == 16


def test_subsets_skips_duplicates():
    assert subsets([1, 1]) == [[], [1], [1, 1]]


def test_subsets_containing_element():
    result = subsets_containing_element([2, 3, 4, 5], 3)
    assert _norm(result) == _norm(
        [[3], [2, 3], [3, 4], [3, 5], [2, 3, 4], [2, 3, 5], [3, 4, 5], [2, 3, 4, 5]]
    )
    assert all(3 in subset for subset in result)


def test_combination_sum_reuses_elements():
    result = combination_sum([2, 3, 6, 7], 7)
    assert _norm(result) == _norm([[2, 2, 3], [7]])


def test_combination_sum_no_solution():
    assert combination_sum([5, 10], 3) == []


def test_combination_sum_ii_unique():
    result = combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
    assert _norm(result) == _norm(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )


# One queen is placed per column, so a solution needs cols <= rows and the
# number of occupied rows equals the number of columns.
@pytest.mark.parametrize("rows, cols", [(4, 4), (1, 1), (3, 2), (10, 8)])
def test_n_queens_returns_solution(rows, cols):
    result = n_queens(rows, cols)
    assert len(result) == cols
    assert result == sorted(result)
    assert len(set(result)) == len(result)
    assert all(1 <= r <= rows for r in result)


@pytest.mark.parametrize("rows, cols", [(3, 4), (2, 5), (8, 10)])
def test_n_queens_impossible_board(rows, cols):
    # More columns than rows means one-queen-per-column cannot use distinct rows.
    assert n_queens(rows, cols) == []


def test_n_queens_default_8x10_has_no_solution():
    # The coursework driver uses an 8x10 board, which is unsolvable.
    assert n_queens() == []


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
    # No empty cells remain.
    assert all(cell != "." for row in board for cell in row)
    # Every row, column and 3x3 box is a permutation of 1-9.
    digits = set("123456789")
    for r in range(9):
        assert set(board[r]) == digits
    for c in range(9):
        assert {board[r][c] for r in range(9)} == digits
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = {board[br + i][bc + j] for i in range(3) for j in range(3)}
            assert box == digits
