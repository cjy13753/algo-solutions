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
    for i in range(2, numNodes + 1): # 각 노드에 대해서 parent를 구해준다
        if len(tree[i]) == 1:
            print(tree[i][0])
            continue
        if 1 in tree[i]:
            print(1)
            continue
        parent = -1
        for j in tree[i]: # 각 노드에 연결된 이웃 노드에 대해서 루트인 1로 이어지는 방향에 있는지 확인해준다.
            visited = set()
            stack = []
            stack.append((j, j)) # (next, candidate)
            flag = False
            while stack:
                next, candidate = stack.pop()
                visited.add(next)
                if next == 1:
                    parent = candidate
                    flag = True
                    break
                else:
                    for next in tree[next]:
                        if next not in visited:
                            stack.append((next, candidate))

            if flag == True:
                break
        print(parent)