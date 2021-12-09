# Referred to discussion solution by GraceMeng(https://leetcode.com/problems/trapping-rain-water/discuss/178028/Stack-with-Explanation-(Java-Python-Scala))
# time: O(n)
# space: O(n)

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        height = [4,2,0,3,2,5]
        print(self.trap(height))

    def trap(self, height: List[int]) -> int:
        leftBoundIdxStack = []
        totalTrappedWater = 0

        for rightBoundIdx, rightBoundHeight in enumerate(height):
            while leftBoundIdxStack:
                buttomHeight = height[leftBoundIdxStack[-1]]
                if buttomHeight < rightBoundHeight:
                    buttomHeight = height[leftBoundIdxStack.pop()]
                    if not leftBoundIdxStack:
                        break
                    leftBoundIdx = leftBoundIdxStack[-1]
                    leftBoundHeight = height[leftBoundIdx]
                    heightDiff = min(leftBoundHeight, rightBoundHeight) - buttomHeight
                    width = rightBoundIdx - leftBoundIdx -1
                    totalTrappedWater += heightDiff * width
                else:
                    break
            
            leftBoundIdxStack.append(rightBoundIdx)
        
        return totalTrappedWater


Solution()