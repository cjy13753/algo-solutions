import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numItems, maxWeight = map(int, input().split())
        weights = [0] * (numItems + 1)
        values = [0] * (numItems + 1)
        for i in range(1, numItems + 1):
            weight, value = map(int, input().split())
            weights[i] = weight
            values[i] = value

        self.maxValue(numItems, maxWeight, weights, values)

    def maxValue(self, numItems: int, maxWeight: int, weights: list, values: list) -> None:
        cache = [[-1] * (maxWeight + 1) for i in range(numItems + 1)] 
        def dp(n: int, c) -> int: # return the maximum value when you choose from n items with the weight constraint of c
            if cache[n][c] != -1:
                return cache[n][c]
            result = 0
            if n == 0 or c == 0: # if either no items are left to choose from or maximum weight capacity is zero
                result = 0
            elif weights[n] > c: # if nth item weighs more than the maximum weight capacity
                result = dp(n - 1, c)
            else: # if either choose the nth item or not
                result = max(dp(n - 1, c - weights[n]) + values[n], dp(n - 1, c))
            
            cache[n][c] = result
            return result

        print(dp(numItems, maxWeight))

Solution()