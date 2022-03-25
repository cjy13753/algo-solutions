""" 
Attempt #1
Time spent: 45m
My own answer: yes
"""

def solution(triangle):
    dpTable = [[-1] * (i + 1) for i in range(len(triangle[-1]))]
    dpTable[0][0] = triangle[0][0]

    def recur(r, c):
        if dpTable[r][c] != -1:
            return dpTable[r][c]
        
        if c > r - 1:
            dpTable[r][c] = recur(r - 1, c - 1) + triangle[r][c]
        else:
            if c - 1 < 0 :
                dpTable[r][c] = recur(r - 1, c) + triangle[r][c]
            else:
                dpTable[r][c] = max(recur(r - 1, c - 1), recur(r - 1, c)) + triangle[r][c]
        return dpTable[r][c]

    for i in range(len(triangle[-1])):
        recur(len(dpTable[-1]) - 1, i)

    return max(dpTable[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))