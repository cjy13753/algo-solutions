'''
Summary

Your own answer?: No. Reference(https://leetcode.com/problems/daily-temperatures/discuss/109832/Java-Easy-AC-Solution-with-Stack)
Time Complexity: O(n), Runtime: 1964 ms, faster than 5.00% of Python3 online submissions for Daily Temperatures.
Space Complexity: O(n), Memory Usage: 25.3 MB, less than 60.94% of Python3 online submissions for Daily Temperatures.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        temperatures = [73,74,75,71,69,72,76,73]
        print(self.dailyTemperatures(temperatures))

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                i = stack.pop()
                ans[i] = idx - i
                
            stack.append(idx)
        
        return ans

Solution()
