import sys

def shortestDistance(start: int, end: int) -> int:
    if end - start + 1 < 4:
        return brute(start, end)

    mid = start + (end - start) // 2
    sdOnLeft = shortestDistance(start, mid)
    sdOnRight = shortestDistance(mid + 1, end)

    minDist = min(sdOnLeft, sdOnRight)

    sdOnMiddle = getMiddle(start, mid, end, minDist)

    return min(minDist, sdOnMiddle)

def brute(start: int, end: int) -> int:
    minDist = 3_200_000_000
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            minDist = min(minDist, dist(points[i], points[j]))
    return minDist

def dist(a: list, b: list) -> int:
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)

def getMiddle(start: int, mid: int, end: int, minDist: int) -> int:
    xCandidates = []

    for i in range(start, end + 1):
        if pow(points[i][0] - points[mid][0], 2) < minDist:
            xCandidates.append(points[i])
    
    xCandidates.sort(key = lambda x: x[1])

    for i in range(len(xCandidates) - 1):
        for j in range(i + 1, len(xCandidates)):
            if  pow(xCandidates[i][1] - xCandidates[j][1], 2) < minDist:
                minDist = min(minDist, dist(xCandidates[i], xCandidates[j]))
            else:
                break

    return minDist

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))
points.sort(key=lambda x: x[0])
print(shortestDistance(0, len(points) - 1))