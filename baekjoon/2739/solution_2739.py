num = int(input())

def solution(num: int) -> None:
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")

solution(num)