a = int(input())
b = int(input())
c = int(input())

def solution(a: int, b: int, c: int) -> None:
    product = str(a * b * c)
    count = {}
    for i in range(10):
        count[i] = 0
    
    for i in product:
        count[int(i)] += 1
    
    for i in range(10):
        print(count[i])


solution(a, b, c)