from collections import Counter

def unionParent(parent, v1, v2):
    v1 = findParent(parent, v1)
    v2 = findParent(parent, v2)

    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1

def findParent(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = findParent(parent, parent[vertex])
    return parent[vertex]

if __name__ == "__main__":
    numVertices = int(input())
    numEdges = int(input())
    parent = [i for i in range(numVertices + 1)]
    
    for _ in range(numEdges):
        v1, v2 = map(int, input().split())
        unionParent(parent, v1, v2)
    
    for i in range(1, numVertices + 1):
        findParent(parent, i)
    
    print(Counter(parent)[1] - 1)
