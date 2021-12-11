import sys
from typing import List
input = sys.stdin.readline

# 2nd attempt: referred to leetcode user hqpdash's answer
# memo: use special tactic to make space complexity more efficient from O(n) to O(1)
# time complexity: O(n), 236 ms
# space complexity: O(1), 21.2 MB

class Solution:
    def __init__(self) -> None:
        nums = [2, 3, 4, 5]
        print(self.productExceptSelf(nums))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            ans[i] = tmp
            tmp = ans[i] * nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1 , -1):
            ans[i] = ans[i] * tmp
            tmp = tmp * nums[i]
        
        return ans

Solution()