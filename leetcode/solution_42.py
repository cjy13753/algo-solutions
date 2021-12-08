import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        height = [5,4,1,2]
        print(self.trap(height))

    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = height[0]
        maxRight = height[-1]
        left = 1
        right = n - 1
        ans = 0

        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1

        return ans

Solution()