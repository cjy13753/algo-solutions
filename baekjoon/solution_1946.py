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
        candidates.sort(key=lambda x: abs(x[1] - x[0]), reverse=True)
        possible = []
        for candidate in candidates:
            flag = True
            for i in possible:
                if (candidate[0] < i[0] and candidate[1] < i[1]) or (candidate[0] > i[0] and candidate[1] > i[1]):
                    flag = False
                    break
            if flag == True:
                possible.append(candidate)
        print(len(possible))

Solution()