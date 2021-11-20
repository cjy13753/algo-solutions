import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
    numNodes = int(input())
    tree = defaultdict(list)
    for _ in range(numNodes - 1):
        node1, node2 = map(int, input().split())
        tree[node1].append(node2)
        tree[node2].append(node1)

    parent = [0] * (numNodes + 1)

    stack = []
    visited = set()
    stack.append(1)
    parent[1] = 1
    while stack:
        popped = stack.pop()
        visited.add(popped)
        for i in tree[popped]:
            if i not in visited:
                parent[i] = popped
                stack.append(i)
    
    for i in range(2, numNodes + 1):
        print(parent[i])