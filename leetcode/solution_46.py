'''
Summary

Your own answer?: Yes
Time spent: more than 60m(due to interrupts, couldn't accurately track)
Time complexity: (N!)
Runtime: 72 ms, faster than 5.36% of Python3 online submissions for Permutations.
Space complexity: O(N)
Memory Usage: 14.5 MB, less than 14.70% of Python3 online submissions for Permutations.
'''

import sys
import copy
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [1,2,3]
        print(self.permute(nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(carry: list, remainder: list) -> None:
            if not remainder:
                ans.append(carry)

            for n in remainder:
                new_carry = copy.deepcopy(carry)
                new_remainder = copy.deepcopy(remainder)
                new_carry.append(n)
                new_remainder.remove(n)
                dfs(new_carry, new_remainder)

        dfs([], nums)
        return ans

Solution()