import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numItems, maxWeight = map(int, input().split())
        items = []
        for _ in range(numItems):
            items.append(list(map(int, input().split()))) # items: [weight, value]

        self.maxValue(items, maxWeight)

    def maxValue(self, items: list, maxWeight: int):
        items.sort()
        cache = [0] * (maxWeight + 1)
        for weight, value in items:
            cache[weight] = max(cache[weight], value)

        for weight, value in items:
            for i in range(weight, maxWeight + 1):
                cache[i] = max(cache[i], cache[weight] + cache[i - weight])
        
        print(cache[maxWeight])

Solution()