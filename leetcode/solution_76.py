'''
Summary - Attempt #1

Memo: Failed due to wrong answer
Time spent: 1h40m
'''

import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "bba"
        t = "ab"
        print(self.minWindow(s, t))

    def minWindow(self, s: str, t: str) -> str:
        def is_valid(judge, store):
            for i in range(len(judge)):
                if store[i] < judge[i]:
                    return False
            return True
        
        judge = [0] * (ord('z') + 1)
        for c in t:
            judge[ord(c)] += 1
        store = [0] * (ord('z') + 1)
        
        must_have = set(t)
        minWindow_length = 1e10
        minWindow = ""
        queue = deque()

        for idx, c in enumerate(s):
            if c in must_have:
                queue.append(idx)
                store[ord(c)] += 1
            if is_valid(judge, store):
                left_most_idx = queue[0]
                right_most_idx = queue[-1]
                if right_most_idx - left_most_idx < minWindow_length:
                    minWindow_length = right_most_idx - left_most_idx + 1
                    minWindow = s[left_most_idx:right_most_idx + 1]
                popped_idx = queue.popleft()
                store[ord(s[popped_idx])] -= 1

        while queue:
            if is_valid(judge, store):
                left_most_idx = queue[0]
                right_most_idx = queue[-1]
                if right_most_idx - left_most_idx < minWindow_length:
                    minWindow_length = right_most_idx - left_most_idx + 1
                    minWindow = s[left_most_idx:right_most_idx + 1]
            popped_idx = queue.popleft()
            store[ord(s[popped_idx])] -= 1

        return minWindow

Solution()