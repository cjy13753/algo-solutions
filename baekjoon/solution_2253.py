import sys
input = sys.stdin.readline
INF = sys.maxsize

class Solution:
    def __init__(self) -> None:
        numStones, numSmallRocks = map(int, input().split())
        smallRocks = set()
        for _ in range(numSmallRocks):
            smallRocks.add(int(input()))
        
        self.minimumLeaps(numStones, smallRocks)

    def minimumLeaps(self, numStones: int, smallRocks: set):
        dst = numStones 
        # dp[prev][now]의 의미: prev에서 now로 왔을 때 목적지(dst)까지 필요한 최소 점프 수(만약 목적지 도착이 불가능하다면 INF)
        dp = [[INF] * (numStones + 1) for _ in range(numStones + 1)]

        def dfs(prev: int, now: int) -> int:
            if dp[prev][now] != INF:
                return dp[prev][now]
            elif now == dst:
                dp[prev][now] = 0
                return 0
            else:
                prevLeap = now - prev
                for leap in range(prevLeap - 1, prevLeap + 2):
                    if leap >= 1 and now + leap <= numStones and (now + leap) not in smallRocks:
                        dp[prev][now] = min(dp[prev][now], dfs(now, now + leap) + 1)
                return dp[prev][now]
        
        if dfs(1, 2) == INF:
            print(-1)
        else:
            print(dp[1][2] + 1)

Solution()