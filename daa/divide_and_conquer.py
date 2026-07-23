"""Divide-and-conquer problems: k-closest points, 4-sum count, median of medians."""

import heapq
from collections import defaultdict
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """Return the ``k`` points closest to the origin (0, 0)."""
    max_heap: List = []
    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(max_heap, (-dist, [x, y]))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [point for _, point in max_heap]


def count_tuples(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Count tuples ``(i, j, k, l)`` with ``a[i]+b[j]+c[k]+d[l] == 0``."""
    ab_sum_count = defaultdict(int)
    for x in a:
        for y in b:
            ab_sum_count[x + y] += 1
    total = 0
    for x in c:
        for y in d:
            total += ab_sum_count[-(x + y)]
    return total


def median_of_medians(arr: List[int], k: int) -> int:
    """Return the ``k``-th smallest (0-indexed) element via median of medians."""

    def partition(values, pivot):
        less = [x for x in values if x < pivot]
        equal = [x for x in values if x == pivot]
        greater = [x for x in values if x > pivot]
        return less, equal, greater

    def select(values, rank):
        if len(values) <= 5:
            return sorted(values)[rank]
        chunks = [values[i:i + 5] for i in range(0, len(values), 5)]
        medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
        pivot = select(medians, len(medians) // 2)
        less, equal, greater = partition(values, pivot)
        if rank < len(less):
            return select(less, rank)
        elif rank < len(less) + len(equal):
            return equal[0]
        return select(greater, rank - len(less) - len(equal))

    return select(list(arr), k)
