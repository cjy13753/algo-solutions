import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = list(input().strip())
        self.reverseString(s)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        

Solution()