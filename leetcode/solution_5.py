import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "wwwww"
        print(self.longestPalindrome(s))

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        longestPalindromicStart = 0
        maxPalinLength = 1

        for end in range(length):
            for start in range(end - 1, -1, -1):
                if end - start == 1 or dp[start + 1][end - 1] == True:
                    if s[start] == s[end]:
                        dp[start][end] = True
                        if end - start + 1 > maxPalinLength:
                            longestPalindromicStart = start
                            maxPalinLength = end - start + 1

        return s[longestPalindromicStart:longestPalindromicStart + maxPalinLength]


Solution()