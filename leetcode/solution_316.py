'''
Summary
Attempt number: #1
Your own answer?: No (Reference: https://www.youtube.com/watch?v=nsnpeb_0Hfw&ab_channel=TimothyHChang)
Time complexity: O(n), Runtime: 32 ms, faster than 91.77% of Python3 online submissions for Remove Duplicate Letters.
Space complexity: O(n), Memory Usage: 14.3 MB, less than 49.97% of Python3 online submissions for Remove Duplicate Letters.

Memo:
    - Greedy algorithm with utilizing index for last occurrence of each character is very interesting
'''

import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "cbacdcbc"
        print(self.removeDuplicateLetters(s))

    def removeDuplicateLetters(self, s: str) -> str:
        last_occr = {c: idx for idx, c in enumerate(s)}
        stack = []
        seen = set()

        for idx, c in enumerate(s):
            if not stack:
                stack.append(c)
                seen.add(c)                
            else:
                if c in seen: continue

                while stack and c < stack[-1] and last_occr[stack[-1]] > idx:
                    seen.remove(stack.pop())
                
                stack.append(c)
                seen.add(c)
        
        return "".join(stack)


Solution()