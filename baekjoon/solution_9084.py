import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numCases = int(input())
        for _ in range(numCases):
            numCoinTypes = int(input())
            coinTypes = list(map(int, input().split()))
            target = int(input())
            self.possibleCases(coinTypes, target)

    def possibleCases(self, coinTypes: list, target: int) -> None:
        cache = [0] * (target + 1)
        cache[0] = 1

        for coin in coinTypes:
            for i in range(coin, target + 1):
                cache[i] += cache[i - coin]

        print(cache[target])

Solution()