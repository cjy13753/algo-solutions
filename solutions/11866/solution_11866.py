import sys

n, k = map(int, sys.stdin.readline().split())

queue = list(map(str, range(1, n + 1)))
res = []
i = 0
while i < len(queue):
    if i % k == k - 1:
        res.append(queue[i])
    else:
        queue.append(queue[i])
    i += 1

print("<" + ", ".join(res) + ">")