import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        s = input().strip()
        print(self.isPalindrome(s))

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        left = 0
        right = len(s) - 1

        flag = True
        while left <= right:
            if (s[left].isalpha() or s[left].isnumeric()) and (s[right].isalpha() or s[right].isnumeric()):
                if s[left].lower() != s[right].lower():
                    flag = False
                    break
                else:
                    left += 1
                    right -= 1
                    continue
            
            if not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            
            if not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
        
        return True if flag else False


Solution()