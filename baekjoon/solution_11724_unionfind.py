import sys
from collections import Counter

def unionFind(parent: list, src: int, dst: int) -> None:
    src = findParent(parent, src)
    dst = findParent(parent, dst)

    if src != dst:
        if src < dst:
            parent[dst] = src
        else:   
            parent[src] = dst

def findParent(parent: list, vertex: int) -> int:
    if parent[vertex] != vertex:
        parent[vertex] = findParent(parent, parent[vertex]) # path compression logic applied
    return parent[vertex]

if __name__ == '__main__':
    numVertices, numEdges = map(int, sys.stdin.readline().split())
    parent = [i for i in range(numVertices + 1)]
    
    for _ in range(numEdges):
        src, dst = map(int, sys.stdin.readline().split())
        unionFind(parent, src, dst)
    
    for i in range(1, numVertices + 1):
        findParent(parent, i)

    print(len(Counter(parent)) - 1)