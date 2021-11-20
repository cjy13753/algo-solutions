import sys
from collections import defaultdict
input = sys.stdin.readline


if __name__ == '__main__':
    # 케이스가 돌기 시작하는 루프
    for _ in range(int(input())):
        numVertices, numEdges = map(int, input().split())
        graph = defaultdict(list)
        verticesCol = {}
        for _ in range(numEdges):
            v1, v2 = map(int, input().split())
            verticesCol[v1] = 0
            verticesCol[v2] = 0
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()
        flag = True
        col = 1
        for vertex in verticesCol: # 각 vertex에서 시작해서 이분 그래프가 성립되는지 확인한다.
            if vertex in visited:
                continue
            
            stack = []
            stack.append(vertex)
            while stack:
                popped = stack.pop()
                if verticesCol[popped] == 0:
                    verticesCol[popped] = col
                    col *= -1
                visited.add(popped)
                for neighbor in graph[popped]:
                    if verticesCol[neighbor] == verticesCol[popped]:
                        flag = False
                        break
                    if neighbor not in visited:
                        stack.append(neighbor)
                if flag == False:
                    break
                
        if flag == True:
            print('YES')
        else:
            print('NO')






            