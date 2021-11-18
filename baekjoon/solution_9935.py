import sys

target = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())
bombSize = len(bomb)
lastBombChar = bomb[-1]

stack = []

for c in target:
    stack.append(c)
    if stack[-1] == lastBombChar:
        if stack[-bombSize:] == bomb:
            del stack[-bombSize:]
if not stack:
    print('FRULA')
else:
    print("".join(stack))