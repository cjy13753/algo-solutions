import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = "wwwww"
        print(self.longestPalindrome(s))

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for left in range(length):
            dp[left][left] = True
        maxPalinLength = 1
        ans = [0, 0] # [left idx, right idx]

        # recur determines if s[left:right + 1] is palindromic
        def recur(left, right):
            if dp[left][right] == True:
                return True
            
            if left + 1 <= right - 1:
                if s[left] == s[right] and recur(left + 1, right - 1) == True:
                    dp[left][right] = True
                    return True
                else:
                    return False
            else:
                if s[left] == s[right]:
                    dp[left][right] = True
                    return True
                else:
                    return False

        for left in range(length):
            for right in range(left, length):
                if s[left] == s[right] and recur(left, right):
                    if right - left + 1 > maxPalinLength:
                        maxPalinLength = right - left + 1
                        ans[0], ans[1] = left, right

        return s[ans[0]:ans[1] + 1]


Solution()