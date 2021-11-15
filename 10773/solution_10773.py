import sys

n = int(sys.stdin.readline())
total = 0
stack = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        popped = stack.pop()
        total -= popped
    else:
        total += num
        stack.append(num)

print(total)