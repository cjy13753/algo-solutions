import sys
input = sys.stdin.readline
INF = sys.maxsize

class Solution:
    def __init__(self) -> None:
        numCities = int(input())
        weights = [list(map(int, input().split())) for _ in range(numCities)]

        self.minimumCost(numCities, weights)

    def minimumCost(self, numCities: int, weights: list):
        # dp[now][visited]가 의미하는 바: 현재 now에 있고 now를 포함해서 visited에 있는 모든 도시들을 방문했다고 했을 때 최초 시작점까지 가기 위해 남은 비용
        # visited가 의미하는 바: 이진수이며 0의 자리가 1이면 0번 도시를 방문했고, 2**1 자리는 1번 도시, 2**2 자리는 2번 도시, ..., 2**k 자리가 1이면 k번 도시를 방문했음을 의미함
        dp = [[INF for _ in range(1<<numCities)] for _ in range(numCities)]

        def dfs(now: int, visited: int) -> int: # 현재 now에 있고 visited를 방문한 상태일 때 최초 시작점인 0까지 도달하는 데 남은 비용
            if dp[now][visited] != INF: # memoization을 이용한 연산 작업 최소화
                return dp[now][visited]
            
            if visited == (1<<numCities) - 1: # 모든 cities를 다 방문했고 마지막으로 최초 시작점인 0으로 돌아오기 직전인 상황
                if weights[now][0] != 0:
                    dp[now][visited] = weights[now][0]
                    return dp[now][visited]
                else:
                    return INF

            # 아직 방문하지 않은 도시들만 골라서 해당 도시(next)에 도착했을 때 최초 시작점 0까지 도달하는 데까지 남은 비용과
            # 현재 있는 도시(now)에서 next 도시로 가는 비용을 합하는 조합들 중 최솟값을 dp[now][visited]에 갱신
            for next in range(1, numCities):
                if weights[now][next] != 0 and 1<<next & visited == 0: # weights[now][next] != 0 생각 못해서 한참 고생. 모든 도시가 연결되지 않았을 수 있음
                    dp[now][visited] = min(dp[now][visited], dfs(next, visited | 1<<next) + weights[now][next])

            return dp[now][visited]
        
        print(dfs(0, 1<<0))

Solution()