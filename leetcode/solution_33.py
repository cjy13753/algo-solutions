'''
Summary - Attempt #2

Your own answer?: No
Reference: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple

Time complexity: O(logn)
Runtime: 51 ms, faster than 40.62% of Python3 online submissions for Search in Rotated Sorted Array.
Space complexity: O(1)
Memory Usage: 14.6 MB, less than 80.84% of Python3 online submissions for Search in Rotated Sorted Array.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [4,5,6,7,0,1,2]
        target = 0
        print(self.search(nums, target))

    def search(self, nums: List[int], target: int) -> int:
        INF = int(1e10)
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = int((left + right) / 2)
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num_at_mid = nums[mid]
            else:
                if target < nums[mid]:
                    num_at_mid = -INF
                else:
                    num_at_mid = INF

            if target < num_at_mid:
                right = mid - 1
            elif target > num_at_mid:
                left = mid + 1
            else:
                return mid
            
        return -1

Solution()