import sys
import heapq

leftMaxHeap = []
rightMinHeap = []

for _ in range(int(sys.stdin.readline())):
    val = int(sys.stdin.readline())
    if len(leftMaxHeap) == len(rightMinHeap):
        heapq.heappush(leftMaxHeap, (-val, val))
    else:
        heapq.heappush(rightMinHeap, (val, val))
    if len(rightMinHeap) > 0 and rightMinHeap[0][1] < leftMaxHeap[0][1]:
        max = heapq.heappop(leftMaxHeap)[1]
        min = heapq.heappop(rightMinHeap)[1]
        heapq.heappush(leftMaxHeap, (-min, min))
        heapq.heappush(rightMinHeap, (max, max))
    print(leftMaxHeap[0][1])