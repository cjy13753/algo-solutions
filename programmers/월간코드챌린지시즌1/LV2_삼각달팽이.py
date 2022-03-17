# 참고: https://amber-chaeeunk.tistory.com/61

def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]

    r = -1
    c = 0
    num = 1

    for direction in range(n):
        for _ in range(direction, n):
            if direction % 3 == 0:
                r += 1
            elif direction % 3 == 1:
                c += 1
            else:
                r -= 1
                c -= 1

            answer[r][c] = num
            num += 1

    return sum(answer, [])