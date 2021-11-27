import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        firstStr = input().strip()
        secondStr = input().strip()
        self.lcs(firstStr, secondStr)

    def lcs(self, firstStr: str, secondStr: str) -> None:
        m = len(firstStr) # row
        n = len(secondStr) # col

        dpTable = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if firstStr[i - 1] == secondStr[j - 1]:
                    dpTable[i][j] = dpTable[i - 1][j - 1] + 1
                else:
                    dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])
        
        print(dpTable[m][n])

Solution()