'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 3m
Time Complexity: O(nlogn) due to using sort function
Runtime: 91ms
Space Complexity: ?, it depends on what sorting algorithm python built-in sort function uses.
Memory Usage: 15 MB, less than 93.80% of Python3 online submissions for Kth Largest Element in an Array.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        print(self.findKthLargest(nums, k))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

Solution()