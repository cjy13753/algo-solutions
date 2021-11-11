year = int(input())

def solution(year: int) -> None:
    if (year % 4 == 0 and year % 100 != 0):
        print(1)
        return
    
    if (year % 400 == 0):
        print(1)
    else:
        print(0)

solution(year)