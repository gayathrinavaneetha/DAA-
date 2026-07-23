"""Backtracking problems (permutations, subsets, combination sum, N-queens, sudoku)."""

from itertools import combinations
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """Return all permutations of the distinct integers in ``nums``."""
    result: List[List[int]] = []
    nums = list(nums)

    def backtrack(start: int) -> None:
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def subsets(s: List[int]) -> List[List[int]]:
    """Return all subsets of ``s`` in lexicographical order (duplicates skipped)."""
    s = sorted(s)
    result: List[List[int]] = []

    def backtrack(start: int, path: List[int]) -> None:
        result.append(path)
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            backtrack(i + 1, path + [s[i]])

    backtrack(0, [])
    return result


def subsets_containing_element(elements: List[int], x: int) -> List[List[int]]:
    """Return every subset of ``elements`` that contains ``x``."""
    result: List[List[int]] = []
    n = len(elements)
    for r in range(1, n + 1):
        for subset in combinations(elements, r):
            if x in subset:
                result.append(list(subset))
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """All combinations of ``candidates`` (reusable) summing to ``target``."""
    result: List[List[int]] = []

    def backtrack(remaining: int, combination: List[int], start: int) -> None:
        if remaining == 0:
            result.append(list(combination))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()

    backtrack(target, [], 0)
    return result


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """Combinations of ``candidates`` (each used once) summing to ``target``."""
    candidates = sorted(candidates)
    result: List[List[int]] = []

    def backtrack(start: int, remaining: int, combination: List[int]) -> None:
        if remaining == 0:
            result.append(list(combination))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            combination.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], combination)
            combination.pop()

    backtrack(0, target, [])
    return result


def _is_safe(board: List[List[int]], row: int, col: int) -> bool:
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


def _solve_n_queens(board: List[List[int]], col: int) -> bool:
    if col >= len(board[0]):
        return True
    for i in range(len(board)):
        if _is_safe(board, i, col):
            board[i][col] = 1
            if _solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def n_queens(rows: int = 8, cols: int = 10) -> List[int]:
    """Return the 1-indexed rows that hold a queen in a ``rows`` x ``cols`` board."""
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    if _solve_n_queens(board, 0):
        return [i + 1 for i in range(rows) if 1 in board[i]]
    return []


def solve_sudoku(board: List[List[str]]) -> bool:
    """Solve a 9x9 sudoku ``board`` in place. Empty cells are ``'.'``."""

    def is_valid(num: str, row: int, col: int) -> bool:
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve() -> bool:
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
