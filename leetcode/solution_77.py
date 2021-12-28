'''
Summary

Attempt #1
Your own answer?: Yes
Time spent: 35m

Time Complexity: O(n Combination k)
Runtime: 512 ms, faster than 39.75% of Python3 online submissions for Combinations.
Space Complexity: O(k)
Memory Usage: 15.7 MB, less than 53.46% of Python3 online submissions for Combinations.
'''


import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        n = 5
        k = 2
        print(self.combine(n, k))


    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(start: int, path: list):
            if len(path) == k:
                ans.append(path)
                return

            for newStart in range(start + 1, n + 1):
                dfs(newStart, path + [newStart])

        for start in range(1, n + 1):
            dfs(start, [start])

        return ans

Solution()