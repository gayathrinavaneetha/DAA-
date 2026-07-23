"""Searching algorithms (binary search, k-th missing positive integer)."""

from typing import List, Tuple


def binary_search(arr: List[int], key: int) -> Tuple[int, int]:
    """Search a sorted ``arr`` for ``key``.

    Returns a ``(index, comparisons)`` tuple where ``index`` is ``-1`` when the
    key is absent and ``comparisons`` is the number of element comparisons made.
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = left + (right - left) // 2
        comparisons += 1
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


def find_kth_positive(arr: List[int], k: int) -> int:
    """Return the ``k``-th positive integer missing from sorted ``arr``."""
    missing_count = 0
    current = 1
    index = 0
    while missing_count < k:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1
    return current
