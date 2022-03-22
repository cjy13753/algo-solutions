""" 
Attempt #1
성공, 49m 소요

시간 복잡도:
대략 O(m*t)가 될 것 같다. m: 게임에 참가하는 인원, t: 미리 구할 숫자의 개수
solution 함수에 있는 첫 번째 while loop에 의해 결정될 것 같다.
numberToBase의 경우 num을 계속 base로 나눠주기 때문에
logarithmic한 시간 복잡도를 가질 것 같고, while loop을 돌아도
linear * logarithmic이라서 무시해도 될 수준일 것 같다.

공간 복잡도:
아쉬움 남는 부분은 전체 문자열을 미리 구해놓지 않고 iterator로 만들었으면
공간 복잡도를 낮출 수 있지 않았을까?
다른 사람들 풀이도 참고했으나 일단 먼저 전체 문자열 구해놓고 답을 구함.
"""

from collections import deque

bigNums = ['A', 'B', 'C', 'D', 'E', 'F']

def numberToBase(num, base):
    if num == 0:
        return '0'
    digits = deque()
    while num:
        q, r = divmod(num, base)
        if r >= 10:
            digits.appendleft(bigNums[r - 10])
        else:
            digits.appendleft(str(r))
        num = q
    return ''.join(digits)

def solution(n, t, m, p):
    fullString = ''
    num = 0
    while len(fullString) < m * t:
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