'''
Summary

Attempt #2
Your own answer?: No
Reference: https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained.
Time complexity: O(n) because of bucket sort
Runtime: Runtime: 108 ms, faster than 37.69% of Python3 online submissions for Top K Frequent Elements.
Runtime analysis: I think the reason why the actual runtime for O(n) bucket sort is slower than my original O(nlogn) solution is 
    probably because the given nums array size is limited to maximum 10^5.
Space complexity: O(n)
Memory Usage: Memory Usage: 19.9 MB, less than 6.61% of Python3 online submissions for Top K Frequent Elements.
'''

import sys
from collections import Counter
from itertools import chain
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [1,1,1,2,2,3]
        print(self.topKFrequent(nums, 2))

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        for num, freq in counter.items():
            buckets[freq].append(num)
        flattened = list(chain(*buckets))
        return flattened[::-1][:k]

Solution()