import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

class Solution:
    def __init__(self) -> None:
        numCases = int(input())
        for _ in range(numCases):
            numCoinTypes = int(input())
            coinTypes = list(map(int, input().split()))
            targetAmount = int(input())
            cache = [0] * 10_001
            print(self.possibleCases(coinTypes, targetAmount, cache))

    def possibleCases(self, coinTypes: list, targetAmount: int, cache: list) -> int:
        if targetAmount <= coinTypes[-1]:
            if cache[targetAmount] == 0:
                count = 0
                for i in coinTypes:
                    if i <= targetAmount:
                        count += 1

                cache[targetAmount] = count

            return cache[targetAmount]
        
        sum = 0
        for i in coinTypes:
            if cache[targetAmount - i] == 0:
                cache[targetAmount - i] = self.possibleCases(coinTypes, targetAmount - i, cache)
            sum += cache[targetAmount - i]

        return sum

Solution()