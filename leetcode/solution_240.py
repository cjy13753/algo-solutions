'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 40m

Time complexity: O(mlogn)
Runtime: 329 ms, faster than 8.34% of Python3 online submissions for Search a 2D Matrix II.
Space complexity: O(1)
Memory Usage: 20.6 MB, less than 73.62% of Python3 online submissions for Search a 2D Matrix II.
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
        # row_upper_limit, which is is the index of the array whose last element is the smallest among ones that are bigger than target
        row_upper_limit = len(matrix) - 1
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                row_upper_limit = min(row_upper_limit, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        # row_lower_limit, which is is the index of the array whose 0th element is the biggest among ones that are smaller than target
        row_lower_limit = 0
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target == matrix[mid][-1]:
                return True
            elif target > matrix[mid][-1]:
                row_lower_limit = max(row_lower_limit, mid)
                low = mid + 1
            else:
                high = mid - 1

        for i in range(row_lower_limit, row_upper_limit + 1):
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                mid = int((left + right) / 2)
                if target == matrix[i][mid]:
                    return True
                if target < matrix[i][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False


Solution()