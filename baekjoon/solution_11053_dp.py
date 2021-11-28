import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        sequenceSize = int(input())
        sequence = list(map(int, input().split()))

        self.dpBottomUp(sequenceSize, sequence)
        self.dpTopDown(sequenceSize, sequence)

    def dpBottomUp(self, sequenceSize: int, sequence: list) -> None:
        # dpTable의 ith element가 의미하는 바: 0th element에서 시작해서 ith element까지의 수열에서 
        # ith element를 포함한다고 했을 때 가장 긴 증가하는 수열의 길이 저장
        dpTable = [1] * sequenceSize 

        ans = 0
        for i in range(sequenceSize):
            for j in range(i):
                if sequence[j] < sequence[i]:
                    dpTable[i] = max(dpTable[i], dpTable[j] + 1)
            ans = max(ans, dpTable[i])
            
        print(ans)

    def dpTopDown(self, sequenceSize: int, sequence: list) -> None:
        # dpTable의 의미는 위와 동일하다.
        dpTable = [-1] * sequenceSize
        def recur(start) -> int:
            if dpTable[start] != -1:
                return dpTable[start]
            
            dpTable[start] = 1
            for i in range(start + 1, sequenceSize):
                if sequence[start] < sequence[i]:
                    dpTable[start] = max(dpTable[start], recur(i) + 1)
            
            return dpTable[start]

        recur(0)
        print(max(dpTable))

Solution()