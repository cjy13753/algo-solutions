import sys

def print_presense(A: list, M: map) -> None:
    A.sort()

    for m in M:
        start = 0
        end = len(A) - 1
        flag = False

        while start <= end:
            mid = start + (end - start) // 2
            if m < A[mid]:
                end = mid - 1
            elif m == A[mid]:
                flag = True
                break
            else:
                start = mid + 1
        print(1) if flag else print(0)


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
M = map(int, sys.stdin.readline().split())

print_presense(A, M)