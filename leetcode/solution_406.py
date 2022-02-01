'''
Summary - Attempt #1

Your own answer?: Yes
Status: Fail due to Time Limit Exceeded

Time complexity: At least O(n^2)
Space complexity: O(n)
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        print(self.reconstructQueue(people))

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        INF = int(1e10)
        people.sort()

        queue = [[INF, 0] for _ in range(len(people))]
        
        for person in people:
            for i in range(person[1], len(people)):
                if queue[i][0] != INF:
                    continue
                cnt = 0
                for j in range(0, i):
                    if queue[j][0] >= person[0]:
                        cnt += 1
                
                if cnt == person[1]:
                    queue[i] = person
                    break
        
        return queue

Solution()