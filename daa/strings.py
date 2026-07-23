"""String problems: brute-force substring membership across a word list."""

from typing import List


def find_substrings(words: List[str]) -> List[str]:
    """Return words that occur as a substring of some other word in ``words``."""
    result = set()
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.add(words[i])
    return sorted(result)
