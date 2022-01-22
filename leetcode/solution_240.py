'''
Summary - Attempt #2

Your own answer?: No
Reference: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution

Time complexity: O(m + n)
Runtime: 232 ms, faster than 36.19% of Python3 online submissions for Search a 2D Matrix II.
Space complexity: O(1)
Memory Usage: 20.5 MB, less than 73.62% of Python3 online submissions for Search a 2D Matrix II.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        target = 19
        print(self.searchMatrix(matrix, target))

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = 0
        n = len(matrix[0]) - 1

        while m < len(matrix) and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                m += 1
            else:
                n -= 1

        return False

Solution()