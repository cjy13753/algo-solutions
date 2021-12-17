import sys
from collections import deque
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        temperatures = [73,74,75,71,69,72,76,73]
        print(self.dailyTemperatures(temperatures))

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 1
        cur = 0
        queue = deque()
        ans = [0] * len(temperatures)

        while i < len(temperatures):
            queue.append(temperatures[i])
            if queue[-1] > temperatures[cur]:
                ans[cur] = len(queue)
                queue.popleft()
                cur += 1
            i += 1
        queue.popleft()
        ans[cur] = 0
        cur += 1
        
        while cur < len(temperatures):
            if queue and queue[-1] > temperatures[cur]:
                ans[cur] = len(queue)
            if queue:
                queue.popleft()
            cur += 1
        
        return ans

Solution()