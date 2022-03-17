import math

def solution(n):
    temp = []
    q = 0
    r = 0
    ans = 0
    while n >= 3:
        q, r = divmod(n, 3)
        temp.append(r)
        n = q
    temp.append(n)
    for i in range(len(temp)):
        ans += math.pow(3, i) * temp[len(temp) - i - 1]
    return ans