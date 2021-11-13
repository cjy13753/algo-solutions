import sys
from typing import List

def lengthOfLIS(nums: List[int]) -> None:
    n = len(nums)
    dp = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    
    print(max(dp))
            
input()
nums = list(map(int, sys.stdin.readline().split()))
lengthOfLIS(nums)