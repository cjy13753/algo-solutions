'''
Summary

Attempt #2
Your own answer?: No(https://leetcode.com/problems/subsets/discuss/122645/3ms-easiest-solution-no-backtracking-no-bit-manipulation-no-dfs-no-bullshit)

Runtime: 39 ms, faster than 20.08% of Python3 online submissions for Subsets.
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
        ans = [[]]

        for n in nums:
            tmp_ans = []
            for subset in ans:
                tmp_ans.append(subset + [n])
            ans += tmp_ans

        return ans


Solution()