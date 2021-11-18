import sys
import heapq

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(list(map(int, sys.stdin.readline().split())))

events = [(left, -height, right) for left, height, right in buildings]
events += list({(right, 0, 0) for _, _, right in buildings})
events.sort() # sorting order가 아주 중요. left 기준으로 오름차순, height 기준으로 내림차순(-height 기준 오름차순)

res = [[0, 0]] # [turning position, -negHeight]
alive = [(0, float('inf'))] # max_heap [negHeight, ending position]. 
                            # 참고로 [0, float('inf')] 더미 값을 안 넣어주면 step 3에서 중간에 빌딩이 전부 사라지는 시점의 변곡점과 높이 0을 담지 못하게 됨

for curPos, negHeight, endingPos in events:

    # step 1: event 시점의 pos보다 좌측으로 ending position을 가진 alive building들이 존재한다면 해당 building들 삭제
    while alive[0][1] <= curPos:
        heapq.heappop(alive)
    
    # step 2: 시작점의 빌딩이라면 heap에 추가
    if negHeight:
        heapq.heappush(alive, (negHeight, endingPos))
    
    # step 3: 지난 turning position에서의 height와 현재 시점의 가장 높은 height와 서로 같지 않다면 또다른 변곡점으로 res에 추가
    if res[-1][1] != -alive[0][0]:
        res.append([curPos, -alive[0][0]]) 

for point, height in res[1:]:
    print(point, height, end = ' ') 