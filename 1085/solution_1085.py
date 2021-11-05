i = input().split()

def solution(x: int, y: int, w: int, h: int) -> None:
    print(min(x, y, h-y, w-x))

solution(*map(lambda x: int(x), i))