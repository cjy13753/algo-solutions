import sys
from collections import deque
from typing import List
input = sys.stdin.readline

def bfs(coins: List[int], threshold: int) -> int:
    queue = deque([(1, coin) for coin in coins])
    sumSet = set(coins)
    minNumTypes = int(10e10)

    while queue:
        count, sum = queue.popleft()
        if sum == threshold:
            minNumTypes = min(minNumTypes, count)
        for newCoin in coins:
            currSum = sum + newCoin
            if currSum > threshold:
                continue
            if currSum not in sumSet:
                sumSet.add(currSum)
                queue.append((count + 1, currSum))

    if minNumTypes == int(10e10):
        return -1
    else:
        return minNumTypes


if __name__ == '__main__':
    numCoins, threshold = map(int, input().split())
    coins = []

    for _ in range(numCoins):
        coins.append(int(input()))

    ans = bfs(coins, threshold)
    if ans == -1:
        print(-1)
    else:
        print(ans)