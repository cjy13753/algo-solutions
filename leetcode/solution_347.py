'''
Summary

Attempt #1
Your own answer?: Yes
time spent: 15m
Time complexity: O(nlogn) because of sorting
Runtime: 96 ms, faster than 88.92% of Python3 online submissions for Top K Frequent Elements.
Space complexity: O(n)
Memory Usage: 18.8 MB, less than 39.10% of Python3 online submissions for Top K Frequent Elements.
'''

import sys
from collections import defaultdict
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [1]
        print(self.topKFrequent(nums, 1))

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        for num in nums:
            nums_freq[num] += 1

        dict_items = list(nums_freq.items())
        dict_items.sort(key=lambda x:x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(dict_items[i][0])

        return ans

Solution()