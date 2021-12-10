import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
        print(self.threeSum(nums))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        if len(nums) < 3:
            return []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                
                    while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                        left += 1
                    while right - 1 > -1 and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(ans)

Solution()