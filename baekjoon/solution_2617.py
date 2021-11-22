import sys
input = sys.stdin.readline

def countDfs(i: int, graph: list, count: int, visited: list) -> int:
    visited[i] = True
    for ball in graph[i]:
        if visited[ball] == False:
            count = max(count, countDfs(ball, graph, count + 1, visited))
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
        threshold = (numBalls + 1) // 2
        visited = [False] * (numBalls + 1)
        if countDfs(i, decreasingGraph, 0, visited) >= threshold:
            ans += 1
        visited = [False] * (numBalls + 1)
        if countDfs(i, increasingGraph, 0, visited) >= threshold:
            ans += 1
        
    print(ans)