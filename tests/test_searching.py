import pytest

from daa.searching import binary_search, find_kth_positive


@pytest.mark.parametrize(
    "arr, key, expected_index",
    [
        ([5, 10, 15, 20, 25, 30, 35, 40, 45], 20, 3),
        ([10, 20, 30, 40, 50, 60], 50, 4),
        ([21, 32, 40, 54, 65, 76, 87], 32, 1),
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 3, 2),
    ],
)
def test_binary_search_found(arr, key, expected_index):
    index, comparisons = binary_search(arr, key)
    assert index == expected_index
    assert comparisons >= 1


def test_binary_search_not_found():
    index, comparisons = binary_search([1, 2, 3, 4, 5], 99)
    assert index == -1
    assert comparisons >= 1


def test_binary_search_empty():
    assert binary_search([], 1) == (-1, 0)


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3, 4], 2, 6),
        ([], 1, 1),
        ([], 5, 5),
        ([2, 3, 4, 7, 11], 1, 1),
    ],
)
def test_find_kth_positive(arr, k, expected):
    assert find_kth_positive(arr, k) == expected
