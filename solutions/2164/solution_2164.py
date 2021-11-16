import sys

i = 0
queue = list(range(1, int(sys.stdin.readline()) + 1))

while i < len(queue) - 1:
    if i % 2 != 0:
        queue.append(queue[i])
    i += 1

print(queue[i])