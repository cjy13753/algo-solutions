'''
Summary

Attemp #1
Your own answer?: Yes
time spent: 16m
Time Complexity: O(m * n) where m is the number of rows and n is the number of columns.
Runtime: 316 ms, faster than 63.68% of Python3 online submissions for Number of Islands.
Space Complexity: O(1)
Memory Usage: 16.7 MB, less than 84.79% of Python3 online submissions for Number of Islands.
Approach: Breadth First Search
'''

import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        grid = grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
        print(self.numIslands(grid))

    def numIslands(self, grid: List[List[str]]) -> int:
        rSize = len(grid)
        cSize = len(grid[0])
        ans =  0

        for r in range(rSize):
            for c in range(cSize):
                if grid[r][c] == "0":
                    continue

                grid[r][c] = "0"
                ans += 1
                queue = deque()
                queue.append((r,c))

                while queue:
                    oldR, oldC = queue.popleft()

                    for dR, dC in [0, 1], [1, 0], [0, -1], [-1, 0]:
                        newR = oldR + dR
                        newC = oldC + dC

                        if 0 <= newR < rSize and 0 <= newC < cSize and grid[newR][newC] == "1":
                            grid[newR][newC] = "0"
                            queue.append((newR, newC))
        
        return ans

Solution()