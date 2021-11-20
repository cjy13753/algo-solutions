import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def isBipartite(graph: list) -> bool:
    col = {}
    def check(prevNode: int) -> bool:
        for newNode in graph[prevNode]:
            if newNode not in col: 
                col[newNode] = 1 - col[prevNode] # 컬러를 배정받지 못한 인접 노드의 경우 직전 노드와 반대되는 색을 배정해준 후 깊이 우선으로 다시 한 번 bipartite 체크에 들어간다.
                if not check(newNode):
                    return False
            else: 
                if col[newNode] == col[prevNode]: # 컬러를 배정받은 노드의 경우 직전 노드와의 색을 비교하여 같을 시 조건을 깨뜨리는 것으로 판단하여 False를 반환한다.
                    return False
        return True

    for i in range(1, len(graph)): # 비연결 그래프의 경우를 대비해서 graph에 존재하는 모든 노드 하나하나에 대해서 체크를 진행한다.
        if i not in col:
            col[i] = 0
        if not check(i): # 각 노드에 인접한 노드들에 깊이 우선으로 탐색하여 bipartite의 조건을 깨는지 체크한다.
            return False
    
    return True

if __name__ == '__main__':
    # 케이스가 돌기 시작하는 루프
    for _ in range(int(input())):
        numVertices, numEdges = map(int, input().split())
        graph = [[] for _ in range(numVertices + 1)]
        for _ in range(numEdges):
            v1, v2 = map(int, input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)

        if isBipartite(graph):
            print('YES')
        else:
            print('NO')