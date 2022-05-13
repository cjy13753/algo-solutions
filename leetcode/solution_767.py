'''
Summary - Attempt #1 FAIL

Difficulty: Leetcode Medium
Time spent: 50m
FAIL type: Wrong Answer
FAIL reason: started off with completely wrong idea
'''

from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        counterTuple = list(counter.items())
        counterTuple.sort(key=lambda x: -x[1])
        counterList = []
        for e in counterTuple:
            counterList.append(list(e))

        if len(s) == 1:
            return s
        elif len(counterList) == 1:
            return ans
        elif counterList[0][1] - counterList[1][1] > 1:
            return ans
        else:
            for i in range(counterList[0][1]):
                for i in range(len(counterList)):
                    if counterList[i][1] != 0:
                        ans += counterList[i][0]
                        counterList[i][1] -= 1
            return ans

testcases = ["ccb", "cccb"]
solution = Solution()
for testcase in testcases:
    print(solution.reorganizeString(testcase))
