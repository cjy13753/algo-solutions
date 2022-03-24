'''
Summary - Attempt #2

Time spent: 50m
Status: Failed due to wrong answer
failed case: s="ABBB", k=2
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
            if (end_idx - start_idx + 1) - counter[s[start_idx]] <= k:
                max_size = max(max_size, end_idx - start_idx + 1)
                end_idx += 1
            else:
                counter[s[end_idx]] -= 1
                counter[s[start_idx]] -= 1
                start_idx += 1

        return max_size