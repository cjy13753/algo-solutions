import sys
import heapq

total = 0
decks = []
for _ in range(int(sys.stdin.readline())):
    decks.append(int(sys.stdin.readline()))

if len(decks) == 1:
    print(0)
else:
    heapq.heapify(decks)
    while len(decks) > 0:
        a = heapq.heappop(decks)
        b = heapq.heappop(decks)
        tmp = a + b
        total += tmp
        if len(decks) != 0:
            heapq.heappush(decks, tmp)

    print(total)