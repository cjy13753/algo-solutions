""" 
소요시간: 
43m, 성공

시간복잡도: 
O(N), N은 문자열의 길이
while문이 2개 있기 때문에 O(N^2)로 보일 수 있지만, 
start 포인터가 계속 end 포인터로 갱신되기 때문에
nested된 while문의 시간복잡도만 보면 된다.
nested된 while문의 경우 end가 1씩 증가하기 때문에
문자열의 길이 만큼 loop를 돌게 된다.

공간복잡도:
일단 O(N) 안으로는 무조건 들어올텐데, 얼마나 더 낮을지를
현재 내 실력에서 생각해낼 수가 없다.
"""


def solution(msg):
    dictionary = {}
    answer = []
    nextIdx = 1
    start = 0
    end = start
    
    for i in range(ord('Z') - ord('A') + 1):
        dictionary[chr(ord('A') + i)] = nextIdx
        nextIdx += 1
        
    while start < len(msg):
        idxToAdd = 0
        while end < len(msg) and msg[start : end + 1] in dictionary:
            idxToAdd = dictionary[msg[start : end + 1]]
            end += 1
        answer.append(idxToAdd)
        if end < len(msg):
            dictionary[msg[start : end + 1]] = nextIdx
            nextIdx += 1
        start = end
        end = start
            
    return answer