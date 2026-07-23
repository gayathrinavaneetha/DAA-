import random

import pytest

from daa.divide_and_conquer import count_tuples, k_closest, median_of_medians


def test_k_closest_basic():
    result = k_closest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2)
    assert sorted(map(tuple, result)) == [(-2, 2), (0, 1)]


def test_k_closest_returns_k_points():
    result = k_closest([[1, 1], [2, 2], [3, 3], [4, 4]], 3)
    assert len(result) == 3
    assert [1, 1] in result


def test_count_tuples():
    assert count_tuples([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_count_tuples_all_zero():
    assert count_tuples([0, 0], [0, 0], [0, 0], [0, 0]) == 16


def test_count_tuples_none():
    assert count_tuples([1], [1], [1], [1]) == 0


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([12, 3, 5, 7, 19], 1, 5),
        ([12, 3, 5, 7, 19], 0, 3),
        ([12, 3, 5, 7, 19], 4, 19),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 6),
    ],
)
def test_median_of_medians(arr, k, expected):
    assert median_of_medians(arr, k) == expected


def test_median_of_medians_matches_sorted():
    rng = random.Random(99)
    for _ in range(30):
        arr = [rng.randint(0, 100) for _ in range(rng.randint(1, 40))]
        k = rng.randint(0, len(arr) - 1)
        assert median_of_medians(arr, k) == sorted(arr)[k]


def test_median_of_medians_does_not_mutate_input():
    arr = [12, 3, 5, 7, 19]
    median_of_medians(arr, 2)
    assert arr == [12, 3, 5, 7, 19]
