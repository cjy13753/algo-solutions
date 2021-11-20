import sys
input = sys.stdin.readline


def calPaths(graph: list, col: list) -> int:
    count = [0]
    def dfs(vertex: int) -> None:
        for i in graph[vertex]:
            visited = set()
            visited.add(vertex)
            stack = []
            stack.append(i)

            while stack:
                popped = stack.pop()
                visited.add(popped)
                if col[popped] == 1:
                    count[0] += 1
                else:
                    for j in graph[popped]:
                        if j not in visited:
                            stack.append(j)

    for vertex in range(1, len(graph)):
        if col[vertex] == 0:
            continue
        dfs(vertex)
    
    return count[0]


if __name__ == '__main__':
    numVertices = int(input())
    col = list(map(int, list("0"+input().strip())))

    graph = [[] for _ in range(numVertices + 1)]
    for _ in range(1, numVertices):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(calPaths(graph, col))