import pytest

from daa.dynamic_programming import (
    climbing_stairs,
    full_justify,
    rob,
    unique_paths,
    word_break,
)


@pytest.mark.parametrize(
    "n, expected",
    [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13)],
)
def test_climbing_stairs(n, expected):
    assert climbing_stairs(n) == expected


@pytest.mark.parametrize(
    "m, n, expected",
    [(7, 3, 28), (3, 7, 28), (1, 1, 1), (3, 3, 6), (2, 2, 2)],
)
def test_unique_paths(m, n, expected):
    assert unique_paths(m, n) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1], 1),
        ([], 0),
        ([2, 7, 9, 3, 1], 11),
        ([5, 5], 5),
    ],
)
def test_rob_circular(nums, expected):
    assert rob(nums) == expected


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a"], True),
    ],
)
def test_word_break(s, words, expected):
    assert word_break(s, words) is expected


def test_full_justify_line_widths():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    result = full_justify(words, 16)
    assert result == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]
    assert all(len(line) == 16 for line in result)


def test_full_justify_single_word_line():
    result = full_justify(["word"], 10)
    assert result == ["word      "]
    assert len(result[0]) == 10
