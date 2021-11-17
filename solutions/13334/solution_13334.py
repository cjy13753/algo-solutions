import sys
import heapq

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    person = list(map(int, sys.stdin.readline().split()))
    if person[0] > person[1]:
        person[0], person[1] = person[1], person[0]
    people.append(person)
people.sort(key=lambda x: x[1]) # 끝점 기준 정렬
d = int(sys.stdin.readline())
minHeap = []
count = 0

for person in people:
    house = person[0]
    office = person[1]
    threshold = office - d
    if threshold <= house:
        heapq.heappush(minHeap, house)
    while minHeap and minHeap[0] < threshold:
        heapq.heappop(minHeap)
    count = max(count, len(minHeap))

print(count)

