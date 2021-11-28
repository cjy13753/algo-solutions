import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        sequenceSize = int(input())
        sequence = list(map(int, input().split()))

        self.dpBottomUp(sequenceSize, sequence)
        # self.dpTopDown(sequenceSize, sequence)

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

    # def dpTopDown(self) -> int:

Solution()