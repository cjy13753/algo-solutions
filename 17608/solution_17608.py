import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    stack.append(int(sys.stdin.readline()))

latest = stack.pop()
count = 1
while len(stack) != 0:
    popped = stack.pop()
    if popped > latest:
        count += 1
        latest = popped

print(count)