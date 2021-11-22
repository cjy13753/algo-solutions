import sys
input = sys.stdin.readline

def dfs(n: int, res: int, sequence: list, ans: list, add: int, sub: int, mul: int, div: int) -> None:
    if n == len(sequence) - 1:
        ans[0] = max(ans[0], res)
        ans[1] = min(ans[1], res)
    
    if add:
        dfs(n + 1, res + sequence[n + 1], sequence, ans, add - 1, sub, mul, div)
    if sub:
        dfs(n + 1, res - sequence[n + 1], sequence, ans, add, sub - 1, mul, div)
    if mul:
        dfs(n + 1, res * sequence[n + 1], sequence, ans, add, sub, mul - 1, div)
    if div:
        if res < 0:
            res = (-1) * (abs(res) // sequence[n + 1])
        else:
            res = res // sequence[n + 1]
        dfs(n + 1, res, sequence, ans, add, sub, mul, div - 1)


if __name__ == '__main__':
    sizeSequence: int = int(input())
    sequence: list = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    ans = [-1_000_000_000, 1_000_000_000] # [max, min]
    dfs(0, sequence[0], sequence, ans, add, sub, mul, div)
    print(ans[0])
    print(ans[1])