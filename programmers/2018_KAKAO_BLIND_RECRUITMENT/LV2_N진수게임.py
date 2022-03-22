""" 
Attempt #1
성공, 49m 소요
"""

def solution(n, t, m, p):
    def convertToAlphabet(num):
        return ['A', 'B', 'C', 'D', 'E', 'F'][num - 10]
    
    def numberToBase(num):
        if num == 0:
            return '0'
        digits = []
        while num:
            digit = int(num % n)
            if digit >= 10:
                digit = convertToAlphabet(digit)
            digits.append(str(digit))
            num //= n
        return ''.join(digits[::-1])
    
    fullString = ''
    num = 0
    while len(fullString) < m * (t - 1) + p:
        fullString += numberToBase(num)
        num += 1
    
    answer = ''
    count = 0
    i =  p - 1
    while count != t:
        count += 1
        answer += fullString[i]
        i += m
    
    return answer