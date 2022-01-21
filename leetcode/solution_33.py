'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 30m

Time complexity: O(nlogn) because in the worst case, you can do a logn search for every element in the list. This answer is worse than just one-passing search.
Runtime: 44 ms, faster than 64.39% of Python3 online submissions for Search in Rotated Sorted Array.
Space complexity: O(1)
Memory Usage: 14.4 MB, less than 93.57% of Python3 online submissions for Search in Rotated Sorted Array.
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
        INF = int(1e9)
        check = [INF]
        
        def recur(left, right):
            if (left > right):
                return

            mid = int((left + right) / 2)
            if nums[mid] == target:
                check[0] = mid
                return
            recur(mid + 1, right)
            recur(left, mid - 1)
        
        recur(0, len(nums) - 1)
        
        if check[0] == INF:
            return -1
        else:
            return check[0]

Solution()