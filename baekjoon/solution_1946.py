import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numCases = int(input())
        for _ in range(numCases):
            numCandidates = int(input())
            candidates = [] # documentScore, interviewScore
            for _ in range(numCandidates):
                candidates.append(list(map(int, input().split())))
            self.maximumEmployees(candidates)



    def maximumEmployees(self, candidates: list) -> None:
        candidates.sort(key=lambda x: x[0])
        cnt = 1
        prevInterviewRank = candidates[0][1] # 서류 1등의 interviewScore
        
        for i in range(1, len(candidates)):
            if candidates[i][1] < prevInterviewRank:
                cnt += 1
                prevInterviewRank = candidates[i][1]

        print(cnt)

Solution()