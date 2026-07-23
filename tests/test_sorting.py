import random

import pytest

from daa.sorting import bubble_sort, insertion_sort, quick_sort

SORTERS = [bubble_sort, insertion_sort, quick_sort]


@pytest.mark.parametrize("sorter", SORTERS)
@pytest.mark.parametrize(
    "data",
    [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        [-2, -5, 0, 3, -1],
    ],
)
def test_sorters_match_builtin(sorter, data):
    assert sorter(list(data)) == sorted(data)


@pytest.mark.parametrize("sorter", SORTERS)
def test_sorters_on_random_data(sorter):
    rng = random.Random(1234)
    for _ in range(20):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 30))]
        assert sorter(list(data)) == sorted(data)


def test_in_place_sorters_return_same_object():
    data = [3, 2, 1]
    assert bubble_sort(data) is data
    data2 = [3, 2, 1]
    assert insertion_sort(data2) is data2


def test_quick_sort_does_not_mutate_input():
    data = [3, 1, 2]
    quick_sort(data)
    assert data == [3, 1, 2]


def test_quick_sort_keeps_duplicates():
    assert quick_sort([2, 2, 2, 1]) == [1, 2, 2, 2]
