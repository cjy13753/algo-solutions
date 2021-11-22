import sys
from collections import defaultdict, deque
input = sys.stdin.readline

if __name__ == "__main__":
    numCities, numRoads, distance, start = map(int, input().split())
    roads = defaultdict(list)
    for _ in range(numRoads):
        src, dst = map(int, input().split())
        roads[src].append(dst)
    
    queue = deque()
    queue.append((start, 0)) # start, total
    visited = set()
    visited.add(start)

    atExactDistance = []
    while queue:
        city, total = queue.popleft()

        if total == distance:
            atExactDistance.append(city)
        
        for i in roads[city]:
            if i not in visited:
                visited.add(i)
                queue.append((i, total + 1))
    
    atExactDistance.sort()
    if len(atExactDistance) == 0:
        print(-1)
    for i in atExactDistance:
        print(i)
        

