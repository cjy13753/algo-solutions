import sys

size = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
ptr = len(towers) - 2
ans = [0] * size
stack = []

stack.append([size - 1, towers[-1]])

if len(towers) == 1:
    print(0)

while ptr >= 0:
    while stack and towers[ptr] >= stack[-1][1]:
        i, h = stack.pop()
        ans[i] = ptr + 1
    stack.append([ptr, towers[ptr]])
    ptr -= 1

print(*ans)