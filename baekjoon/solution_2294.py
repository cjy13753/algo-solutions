import sys
input = sys.stdin.readline

def bfs(types: list, threshold: int, sum: int, count: int) -> int:
    if sum == threshold:
        return count
    if sum > threshold:
        return int(10e10)

    minCount = int(10e10)
    for i in types:
        minCount = min(minCount, bfs(types, threshold, sum + i, count + 1))
    return minCount


if __name__ == '__main__':
    numTypes, threshold = map(int, input().split())
    types = []

    for _ in range(numTypes):
        types.append(int(input()))

    ans = bfs(types, threshold, 0, 0)
    if ans == int(10e10):
        print(-1)
    else:
        print(ans)