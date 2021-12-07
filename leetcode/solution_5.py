import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "a"
        self.longestPalindrome(s)

    def longestPalindrome(self, s: str) -> str:
        store = defaultdict(list)
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                while i <= j and s[i] != s[j]:
                    j -= 1
                if s[i] == s[j]:
                    start = i
                    end = j
                    flag = True
                    while start <= end:
                        if s[start] != s[end]:
                            flag = False
                            break
                        else:
                            start += 1
                            end -= 1
                    if flag == True:
                        substring = s[i:j+1]
                        store[substring] = len(substring)

        maxValue = 0
        keyAtMaxValue = ''
        for key, value in store.items():
            if value > maxValue:
                maxValue = value
                keyAtMaxValue = key

        return keyAtMaxValue

Solution()