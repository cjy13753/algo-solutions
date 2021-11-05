a = input()
b = input()

def solution(a: int, b: int) -> None:
    ones = b%10
    tens = b%100//10
    hundreds = b//100

    print(a * ones, a * tens, a * hundreds, a * b)

solution(int(a), int(b))