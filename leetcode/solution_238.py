import sys
from typing import List
input = sys.stdin.readline

# initial attempt, took 40 minutes
# approach keywords: two pointers with prefix product array and suffix product array
# time complexity: O(n), 248 ms
# space complexity: O(n), 22.4 MB

class Solution:
    def __init__(self) -> None:
        nums = [-1,1,0,-3,3]
        print(self.productExceptSelf(nums))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i - 1]

        suffix = [0] * len(nums)
        suffix[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i + 1]

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]

        return ans

Solution()