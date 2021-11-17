num = int(input())

def solution(num: int) -> int:
    if num == 0:
        return 1
    
    return num * solution(num - 1)


print(solution(num))