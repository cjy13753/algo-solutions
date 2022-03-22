""" 
Attempt #1
성공, 49m 소요
"""

from collections import deque

def convertToAlphabet(num):
    return ['A', 'B', 'C', 'D', 'E', 'F'][num - 10]

def numberToBase(num, base):
    if num == 0:
        return '0'
    digits = deque()
    while num:
        q, r = divmod(num, base)
        if r >= 10:
            r = convertToAlphabet(r)
        digits.appendleft(str(r))
        num = q
    return ''.join(digits)

def solution(n, t, m, p):
    fullString = ''
    num = 0
    while len(fullString) < m * (t - 1) + p:
        fullString += numberToBase(num, n)
        num += 1
    
    answer = ''
    count = 0
    i =  p - 1
    while count < t:
        count += 1
        answer += fullString[i]
        i += m
    
    return answer