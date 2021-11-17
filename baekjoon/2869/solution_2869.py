import math

up, down, target = map(int, input().split())

def solution(up: int, down: int, target: int) -> None:
    print(math.ceil((target - up) / (up - down)) + 1)

solution(up, down, target)