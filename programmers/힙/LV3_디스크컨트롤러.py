""" 
Attempt #1: PASS
Time spent: 41m
My own answer: Yes

Time Complexity:
Sorting에 O(NlogN) 소용, N은 job의 개수
각 job은 최대 한 번 heappush되고, 최대 한 번 heappop되기 때문에
O(2NlogN) -> O(NlogN)
따라서 총 O(NlogN)

Space Complexity:
O(N)
"""

import heapq

def solution(jobs):
    currentTime = 0
    minHeap = []
    totalProcessTime = 0 # totalProcessTime = wait time + work time
    totalJobs = len(jobs)
    doneJobs = 0

    jobs.sort(key=lambda x: (-x[0]))
    
    while doneJobs < totalJobs:
        while jobs and jobs[-1][0] <= currentTime:
            requestPoint, worktime = jobs.pop()
            heapq.heappush(minHeap, (worktime, requestPoint))
        if len(minHeap) == 0:
            currentTime = jobs[-1][0]
        else:
            worktime, requestPoint = heapq.heappop(minHeap)
            currentTime += worktime
            totalProcessTime += currentTime - requestPoint
            doneJobs += 1
    
    return int(totalProcessTime / totalJobs)

print(solution([[0, 3], [1, 9], [2, 6]]))