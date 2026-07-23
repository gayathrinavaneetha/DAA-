from daa.strings import find_substrings


def test_find_substrings_basic():
    assert find_substrings(["mass", "as", "hero", "superhero"]) == ["as", "hero"]


def test_find_substrings_none():
    assert find_substrings(["abc", "def", "ghi"]) == []


def test_find_substrings_deduplicates():
    assert find_substrings(["a", "a", "aa"]) == ["a"]


def test_find_substrings_empty_input():
    assert find_substrings([]) == []
