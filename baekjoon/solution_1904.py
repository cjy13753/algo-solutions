import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        n = int(input())
        self.possibleTiles(n)

    def possibleTiles(self, n: int):
        if n == 1:
            print(1)
            return
        if n == 2:
            print(2)
            return
        
        twoBefore, oneBefore = 1, 2
        curr = -1
        nth = 3

        while nth <= n:
            curr = (oneBefore + twoBefore) % 15746
            twoBefore, oneBefore = oneBefore, curr
            nth += 1

        print(curr)

Solution()