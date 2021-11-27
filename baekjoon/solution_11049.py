import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numMatrices = int(input())
        rows = []
        cols = []
        for _ in range(numMatrices):
            row, col = map(int, input().split())
            rows.append(row)
            cols.append(col)
        
        self.minimumMultiplication(rows, cols, numMatrices)

    def minimumMultiplication(self, rows: list, cols: list, numMatrices: int):
        dp = [[0] * (numMatrices) for _ in range(numMatrices)]
        
        for col in range(1, numMatrices):
            for row in range(col - 1, -1, -1):
                minMult = int(2**31)
                for k in range(row, col): # 내가 실수한 부분 for k in range(col)이라고 해서 계산이 잘못 이루어짐
                    minMult = min(minMult, dp[row][k] + dp[k + 1][col] + rows[row] * rows[k + 1] * cols[col]) # 내가 실수한 부분 rows[row] * rows[k] * cols[col]이라고 했음
                dp[row][col] = minMult
        
        print(dp[0][len(cols) - 1])

Solution()