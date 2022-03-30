""" 
Attempt #1:PASS

My own answer: NO

Time complexity: O(nlogn)
while-loop takes O(logn) and for-loop takes O(n).
since for-loop is nested inside while-lopp,
the overall time complexity is O(nlogn)

Space complexity: O(1)
"""

def solution(n, times):
    min_time = 1
    max_time = max(times) * n
    ans = max_time
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        max_handle = 0
        
        for process_time in times:
            max_handle += mid_time // process_time

        if max_handle >= n:
            ans = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
        
    return ans

print(solution(6, [7, 10]))