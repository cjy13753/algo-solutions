import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        self.fib(int(input()))

    def fib(self, n: int) -> None:
        if n == 0:
            print(0)
            return
        elif n == 1:
            print(1)
            return

        idx = 2
        prev = 1
        prevBeforePrev = 0
        while idx <= n:
            res = prevBeforePrev + prev
            prevBeforePrev = prev
            prev = res
            idx += 1

        print(res)

Solution()