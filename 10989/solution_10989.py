import sys

# counting sort
def countingsort() -> None:
    MAX = 10000
    size = int(sys.stdin.readline())
    count = [0] * (MAX + 1)

    input_max = 0

    for _ in range(size):
        n = int(sys.stdin.readline())
        if n > input_max:
            input_max = n
        count[n] += 1

    for i in range(1, input_max + 1):
        if count[i] == 0:
            continue
        
        for _ in range(count[i]):
            print(i)

countingsort()