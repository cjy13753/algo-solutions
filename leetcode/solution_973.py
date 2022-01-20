'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 13m

Time complexity: O(NlogN)
Runtime: 948 ms, faster than 27.26% of Python3 online submissions for K Closest Points to Origin.
Space complexity: O(N)
Memory Usage: 19.8 MB, less than 61.82% of Python3 online submissions for K Closest Points to Origin.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        points = [[1,3],[-2,2]]
        k = 1
        print(self.kClosest(points, k))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        for point in points:
            store.append([point[0]*point[0] + point[1]*point[1], point])
        store.sort()
        
        return [item[1] for item in store[:k]]

Solution()