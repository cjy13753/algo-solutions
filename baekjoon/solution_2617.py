import sys
input = sys.stdin.readline

def findImpossible(i: int, graph: list) -> int:
    count = 0

    def dfs(ball: int):
        cnt = 1

        for ball in graph[ball]:
            cnt += dfs(ball)
        return cnt

    for ball in graph[i]:
        count += dfs(ball)

    return count


if __name__ == '__main__':
    numBalls, numPairs = map(int, input().split())
    increasingGraph = [[] for _ in range(numBalls + 1)]
    decreasingGraph = [[] for _ in range(numBalls + 1)]
    for _ in range(numPairs):
        big, small = map(int, input().split())
        decreasingGraph[big].append(small)
        increasingGraph[small].append(big)
    
    ans = 0
    for i in range(1, numBalls + 1):
        if findImpossible(i, decreasingGraph) >= (numBalls + 1) // 2:
            ans += 1
        if findImpossible(i, increasingGraph) >= (numBalls + 1) // 2:
            ans += 1
        
    print(ans)