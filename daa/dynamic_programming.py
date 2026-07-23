"""Dynamic-programming problems."""

from math import comb
from typing import List


def climbing_stairs(n: int) -> int:
    """Number of distinct ways to climb ``n`` steps taking 1 or 2 at a time."""
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def unique_paths(m: int, n: int) -> int:
    """Number of unique top-left to bottom-right paths in an ``m`` x ``n`` grid."""
    return comb(m + n - 2, m - 1)


def _rob_linear(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


def rob(nums: List[int]) -> int:
    """Maximum money robbed from houses arranged in a circle (no two adjacent)."""
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    return max(_rob_linear(nums[:-1]), _rob_linear(nums[1:]))


def word_break(s: str, word_dict: List[str]) -> bool:
    """Return True if ``s`` can be segmented into words from ``word_dict``."""
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]


def full_justify(words: List[str], max_width: int) -> List[str]:
    """Format ``words`` into fully justified lines of width ``max_width``."""
    result: List[str] = []
    current_line: List[str] = []
    num_of_letters = 0
    for word in words:
        if num_of_letters + len(current_line) + len(word) > max_width:
            spaces_to_add = max_width - num_of_letters
            if len(current_line) == 1:
                result.append(current_line[0] + ' ' * spaces_to_add)
            else:
                num_spaces = len(current_line) - 1
                even_space = spaces_to_add // num_spaces
                extra_space = spaces_to_add % num_spaces
                line = ''
                for i in range(num_spaces):
                    line += current_line[i]
                    line += ' ' * (even_space + (1 if i < extra_space else 0))
                line += current_line[-1]
                result.append(line)
            current_line = []
            num_of_letters = 0
        current_line.append(word)
        num_of_letters += len(word)
    last_line = ' '.join(current_line)
    last_line += ' ' * (max_width - len(last_line))
    result.append(last_line)
    return result
