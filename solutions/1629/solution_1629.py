import sys

def find_remn(num: int, power: int, div: int, cache: dict = {}) -> int:
    if power == 1:
        res = num % div
        cache[power] = res
        return res
    
    first_half = power // 2
    second_half = power - power // 2

    first_half_remn = cache[first_half] if first_half in cache else find_remn(num, first_half, div, cache)
    second_half_remn = cache[second_half] if second_half in cache is not None else find_remn(num, second_half, div, cache)

    res = (first_half_remn * second_half_remn) % div
    cache[power] = res

    return res

num, power, div = list(map(int, sys.stdin.readline().split()))
print(find_remn(num, power, div))