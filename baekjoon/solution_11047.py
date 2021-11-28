import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numCoins, target = map(int, input().split())
        coins = []
        for _ in range(numCoins):
            coins.append(int(input()))
        self.minimumUseOfCoins(coins, target)

    def minimumUseOfCoins(self, coins: list, target: int) -> None:
        cnt = 0
        coins.sort(reverse=True)

        for coin in coins:
            dividend = target // coin
            if dividend > 0:
                cnt += dividend
                target -= coin * dividend

        print(cnt)

Solution()