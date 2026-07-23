"""Sorting algorithms (bubble sort, insertion sort, quick sort)."""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort ``arr`` in place using bubble sort with an early-exit optimisation."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """Sort ``arr`` in place using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    """Return a new sorted list using (non in-place) quick sort."""
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
