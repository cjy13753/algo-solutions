'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 35m

Time Complexity: O(N^2) because although it traverses the list only once, popping and inserting element may take O(N)
Runtime: 62 ms, faster than 9.37% of Python3 online submissions for Sort Colors.
Space Complexity: O(1)
Memory Usage: 14.1 MB, less than 91.84% of Python3 online submissions for Sort Colors.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [2,0,2,1,1,0]
        self.sortColors(nums)
        print(nums)

    def sortColors(self, nums: List[int]) -> None:
        idx = 0 
        tracking = -1
        while idx < len(nums):
            if tracking == idx:
                break
            if nums[idx] == 0:
                nums.pop(idx)
                nums.insert(0, 0)
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums.pop(idx)
                nums.append(2)
                if tracking == -1:
                    tracking = len(nums)
                tracking -= 1

Solution()
