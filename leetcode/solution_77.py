'''
Summary

Attempt #2
Your own answer?: No (https://leetcode.com/problems/combinations/discuss/27002/Backtracking-Solution-Java)
Approach: backtracking

Time Complexity: O(n Combination k)
Runtime: 452 ms, faster than 68.91% of Python3 online submissions for Combinations.
Space Complexity: O(k)
Memory Usage: 15.7 MB, less than 53.46% of Python3 online submissions for Combinations.
'''


import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        n = 3
        k = 2
        print(self.combine(n, k))


    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start, tmp, remainder):
            if remainder == 0:
                ans.append(list(tmp))
                return

            for i in range(start, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp, remainder - 1)
                tmp.pop()

        backtrack(1, [], k)

        return ans


Solution()