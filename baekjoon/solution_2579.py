import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numSteps = int(input())
        points = [0] * (numSteps + 1)
        for i in range(1, numSteps + 1):
            points[i] = int(input())

        self.maxScore(numSteps, points)

    def maxScore(self, numSteps: int, points: list) -> None:
        # dp[i]가 의미하는 바: ith 계단에 올라왔을 때까지 누적된 최대 점수
        dp = [0] * (numSteps + 1)

        def recur(n: int) -> int: # dp[n]을 계산해주는 함수
            if dp[n] != 0:
                return dp[n]

            if n == 1:
                dp[1] = points[1]
                return dp[1]
            
            if n == 2:
                dp[2] = points[1] + points[2]
                return dp[2]
            
            if n == 3:
                dp[3] = max(points[1], points[2]) + points[3]
                return dp[3]
            
            dp[n] = max(recur(n-3) + points[n-1], recur(n-2)) + points[n]
            return dp[n]

        print(recur(numSteps))

Solution()