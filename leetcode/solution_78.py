'''
Summary

Attempt #1
Your own answer?: Yes
Time spent: 27m

Time Complexity: O(nC0 + nC1 + nC2 + ... + nCn)
Runtime: 62 ms, faster than 5.45% of Python3 online submissions for Subsets.
Space Complexity: O(N)
Memory Usage: 14.5 MB, less than 18.52% of Python3 online submissions for Subsets.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [1,2,3]
        print(self.subsets(nums))

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(curr: int, path: list):
            if curr == len(nums):
                return

            if curr == -1:
                ans.append([])
                for i in range(curr + 1, len(nums)):
                    dfs(i, path + [])
            else:
                ans.append(path + [nums[curr]])

                for i in range(curr + 1, len(nums)):
                    dfs(i, path + [nums[curr]])

        dfs(-1, [])
        return ans


Solution()