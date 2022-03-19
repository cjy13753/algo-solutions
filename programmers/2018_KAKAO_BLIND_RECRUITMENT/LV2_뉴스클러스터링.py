""" 
총 57m 소요해서 성공

1. 시간이 많이 걸린 부분
일단 문제 자체를 이해하는 데 오랜 시간이 걸림.
문자열 관련 문제가 나오면 문제를 이해하는 것 자체에 시간이 지나치게 오래 걸림.
교집합과 합집합에 대한 처리를 어떻게 해야 할지로 오래 걸림.

2. 실수
예외 케이스에서 두 집합이 모두 공집합인 경우 1로만 처리.
하지만 문제 조건에서 모든 답은 65536을 곱한 후 정수부분만 남겨서 반환하라고 했음.
답을 하나의 변수에 넣고, 그 답에 대한 처리는 마지막에 통일해서 처리하는 게 좋겠음.

3. 내 추론 시간 복잡도와 공간 복잡도
- 시간 복잡도
N은 str1 문자열의 길이 그리고 M은 str2의 문자열의 길이
str1을 다중집합으로 만드는 데 O(N), str2를 다중집합으로 만드는 데 O(M)
str1을 counting 하는 데 O(N), str2를 counting 하는 데 O(M)
교집합의 길이를 구하는 데 O(N), 합집합의 길이를 구하는 데 O(N+M)
결론적으로 O(N+M)

-공간 복잡도
list와 Counter 객체 사용으로 O(N+M)
"""

from collections import Counter

def solution(str1, str2):
    store1 = []
    for i in range(len(str1) - 1):
        if not (str1[i].isalpha() and str1[i+1].isalpha()):
            continue
        store1.append(str1[i:i+2].upper())

    
    store2 = []
    for i in range(len(str2) - 1):
        if not (str2[i].isalpha() and str2[i+1].isalpha()):
            continue
        store2.append(str2[i:i+2].upper())

    
    nomi = 0
    denomi = 0
    counterStore1 = Counter(store1)
    counterStore2 = Counter(store2)

    answer = 0
    
    if len(counterStore1) == 0 and len(counterStore2) == 0:
        answer = 1
    
    elif len(counterStore1) == 0 or len(counterStore2) == 0:
        answer = 0
    
    else:
        for key in counterStore1.keys():
            if key in counterStore2:
                nomi += min(counterStore1[key], counterStore2[key])
        
        for key in counterStore1.keys():
            if key in counterStore2:
                denomi += max(counterStore1[key], counterStore2[key])
                del counterStore2[key]
            else:
                denomi += counterStore1[key]
        
        for val in counterStore2.values():
            denomi += val

        answer = nomi / denomi

    return int(answer * 65536)