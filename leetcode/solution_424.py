'''
Summary - Attempt #1

Time spent: 60m
Status: Failt due to wrong answer
failed case: s="ABBB", k=2
'''

import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "AABABBA"
        k = 1
        print(self.characterReplacement(s, k))

    def characterReplacement(self, s: str, k: int) -> int:
        if s == 1:
            return 1
        
        longest_windows_size = 0
        queue = deque()
        queue.append(0)

        while queue:
            diff_char_num = 0
            i = queue[0] + 1
            while i < len(s):
                if s[i] != s[queue[0]]:
                    if diff_char_num < k:
                        queue.append(i)
                        diff_char_num += 1
                    else:
                        queue.append(i)
                        break
                i += 1
            
            if i - queue[0] > longest_windows_size:
                longest_windows_size = i - queue[0]
            
            queue.popleft()
        
        return longest_windows_size
            
Solution()