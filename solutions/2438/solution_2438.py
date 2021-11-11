num = int(input())

def solution(num: int) -> None:
    for i in range(1, num + 1):
        print("*" * i)

solution(num)