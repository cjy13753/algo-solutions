import sys

def find_remn(num: int, power: int, div: int) -> int:
    if power == 1:
        return num % div
    
    remn = find_remn(num, power // 2, div)

    if power % 2 == 1:
        return remn ** 2 * num % div
    else:
        return remn ** 2 % div
    

num, power, div = list(map(int, sys.stdin.readline().split()))
print(find_remn(num, power, div))