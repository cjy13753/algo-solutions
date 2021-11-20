import sys
from collections import Counter

def unionFind(parent: list, src: int, dst: int) -> None:
    srcParent = findParent(parent, src)
    dstParent = findParent(parent, dst)

    if srcParent != dstParent:
        if srcParent < dstParent:
            parent[dst] = srcParent
        else:
            parent[src] = dstParent

def findParent(parent: list, vertex: int) -> int:
    if parent[vertex] == vertex:
        return vertex
    
    return findParent(parent, parent[vertex])

if __name__ == '__main__':
    numVertices, numEdges = map(int, sys.stdin.readline().split())
    parent = [i for i in range(numVertices + 1)]
    
    graph = []
    for _ in range(numEdges):
        src, dst = map(int, sys.stdin.readline().split())
        graph.append([src, dst])
    graph.sort() # 여기서 잘못 됐음. 입력 되는 데이터가 u < v일 것이라고 가정했기 때문. 하지만 (3, 4), (4, 2), (6, 2)와 같이 들어오면 문제 발생.
    for src, dst in graph:
        unionFind(parent, src, dst)

    print(parent)
    print(len(Counter(parent)) - 1)
