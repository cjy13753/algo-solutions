import sys

numDigits, numRemoval = map(int, sys.stdin.readline().split())
s  = sys.stdin.readline().split()[0]
stack = []

i = 0
while numRemoval > 0 and i < numDigits:
    while stack and numRemoval > 0 and stack[-1] < s[i]:
        stack.pop()
        numRemoval -= 1
    stack.append(s[i])
    i += 1

while numRemoval > 0:
    stack.pop()
    numRemoval -= 1

while i < numDigits:
    stack.append(s[i])
    i += 1

print("".join(stack))