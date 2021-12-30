'''
Summary

Attempt #1
Your Own answer?: Yes
Time spent: 30m
Time Complexity: ?
Runtime: 145 ms, faster than 16.30% of Python3 online submissions for Combination Sum.
Space Complexity: O(N) where N is target
Memory Usage: 14.3 MB, less than 52.37% of Python3 online submissions for Combination Sum.
'''


import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        candidates = [2,3,6,7]
        target = 7
        print(self.combinationSum(candidates, target))

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        ans = []

        def dfs(start, path, goal):
            if goal < 0:
                return
            elif goal == 0:
                ans.append(path)
                return
            for i in range(start, size):
                dfs(i, path + [candidates[i]], goal - candidates[i])

        dfs(0, [], target)
        return ans

Solution()