'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 35m

Time complexity: O(NlogN) where N is the length of INTERVALS due to sorting algorithm
Runtime: 140 ms, faster than 33.97% of Python3 online submissions for Merge Intervals.
Space complexity: O(1)
Memory Usage: 18.8 MB, less than 9.12% of Python3 online submissions for Merge Intervals.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        print(self.merge(intervals))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        ans = []
        left = intervals[0][0]
        right = intervals[0][1]
        i = 1
        while i < len(intervals):
            if right >= intervals[i][0]:
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                ans.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            
            if i + 1 == len(intervals):
                ans.append([left, right])
            
            i += 1
        
        return ans

Solution()