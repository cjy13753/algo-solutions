a, b = input().split()

def solution(a: str, b: str) -> None:
    converted_a = ""
    for i in range(len(a) - 1, -1, -1):
        converted_a += a[i]

    converted_b = ""
    for i in range(len(b) - 1, -1, -1):
        converted_b += b[i]

    print(max(int(converted_a), int(converted_b)))

solution(a, b)