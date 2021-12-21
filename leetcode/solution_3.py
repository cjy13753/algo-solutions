'''
Summary

Attempt #1
Your own answer?: No
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
Runtime: 48 ms, faster than 96.47% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 55.31% of Python3 online submissions for Longest Substring Without Repeating Characters.

Memo: I also came up with the idea of using one pointer pointing to the head of the range and another pointing to the iterater variable while keeping track of each value's latest index, 
but somehow failed to get the size out of the custom range.
'''

import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "abcabcbb"
        print(self.lengthOfLongestSubstring(s))

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        used = {}

        for idx, val in enumerate(s):
            if val in used and start <= used[val]:
                start = used[val] + 1
            else:
                maxLength = max(maxLength, idx - start + 1)
        
            used[val] = idx

        return maxLength

Solution()