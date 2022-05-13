'''
Summary

Leetcode 767. Reorganize String (Medium)

Attempt #2: PASS
Your unique answer?: No
Idea from: https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue

Time Complexity: O(nlogn) due to using heap tree, where n is the length of the given string
Space Complexity: O(n) to hold each character and its frequency in the given string
Runtime: 61 ms, faster than 21.61% of Python3 online submissions for Reorganize String.
Memory Usage: 13.9 MB, less than 28.94% of Python3 online submissions for Reorganize String.
'''

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        container = []
        for character, freq in Counter(s).items():
            container.append((-freq, character))
        maxHeap = []
        for item in container:
            heapq.heappush(maxHeap, item)
        
        temp_char = ''
        temp_freq = 0

        while maxHeap:
            item = heapq.heappop(maxHeap)
            freq, character = -item[0], item[1]
            ans += character
            freq -= 1
            if temp_freq != 0:
                heapq.heappush(maxHeap, (temp_freq, temp_char))
            temp_char = character
            temp_freq = -(freq)

        if temp_freq != 0:
            return ""
        else:
            return ans
        

testcases = ["ccb", "cccb", "vvvlo"]
solution = Solution()
for testcase in testcases:
    print(solution.reorganizeString(testcase))