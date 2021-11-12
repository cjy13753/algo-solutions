import sys
from typing import List

def lengthOfLIS(nums: List[int]) -> None:
    sub = []
    for num in nums:
        if len(sub) == 0 or num > sub[-1]:
            sub.append(num)
        else:
            idx = bisect_leftmost(sub, num)
            sub[idx] = num
    
    print(len(sub))

def bisect_leftmost(sub: List[int], num: int) -> int:
    start = 0
    end = len(sub) - 1
    res = -1

    while start <= end:
        mid = start + (end - start) // 2
        mid_val = sub[mid]
        if mid_val > num:
            end = mid - 1
            res = mid
        elif mid_val == num:
            return mid
        else:
            start = mid + 1

    return res
            
input()
nums = list(map(int, sys.stdin.readline().split()))
lengthOfLIS(nums)