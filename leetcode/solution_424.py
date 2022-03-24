'''
Summary - Attempt #3 (PASS)

Slight change to the previous attempt after referring to leetcode discussion.
The key is to subtract the frequency of the most frequent charact in the window of the from the window size.

Runtime: 146 ms, faster than 76.11% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14 MB, less than 64.50% of Python3 online submissions for Longest Repeating Character Replacement.
'''

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        start_idx = 0
        end_idx = 0
        max_size = 0

        while end_idx < len(s):
            counter[s[end_idx]] += 1
            if (end_idx - start_idx + 1) - max(counter.values()) <= k:
                max_size = max(max_size, end_idx - start_idx + 1)
                end_idx += 1
            else:
                counter[s[start_idx]] -= 1
                start_idx += 1
                end_idx += 1

        return max_size