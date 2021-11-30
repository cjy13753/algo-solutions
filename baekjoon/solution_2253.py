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
        maxJump = int((2 * numStones) ** (1/2)) + 1

        dp = [[INF] * (maxJump + 1) for _ in range(numStones + 1)]
        dp[1][0] = 0

        for stone in range(2, numStones + 1):
            if stone in smallRocks:
                continue
            
            currMaxSpeed = int((2 * stone - 2) ** (1/2))

            for jump in range(1, currMaxSpeed + 1):
                dp[stone][jump] = min(
                    dp[stone - jump][jump - 1], 
                    dp[stone - jump][jump], 
                    dp[stone - jump][jump + 1]) + 1

        minJump = min(dp[numStones])
        if minJump == INF:
            print(-1)
        else:
            print(minJump)

Solution()