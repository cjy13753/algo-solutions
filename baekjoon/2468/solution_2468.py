import sys

def max_safe_area(area: list) -> None:
    max_rain_amount = 0
    for row in area:
        max_rain_amount = max(max(row), max_rain_amount)

    max_safe_count = 0
    for rain_amount in range(0, max_rain_amount + 1):
        area_width = len(area)
        masking = [[0] * area_width for _ in range(area_width)]
        
        for i in range(area_width):
            for j in range(area_width):
                if area[i][j] > rain_amount:
                    masking[i][j] = 1
        
        count = 0
        for i in range(area_width):
            for j in range(area_width):
                if masking[i][j] == 1:
                    count += 1
                    queue = []
                    queue.append((i, j))
                    while len(queue) > 0:
                        popped = queue.pop(0)
                        row = popped[0]
                        col = popped[1]
                        if row >= 0 and row < area_width and col >= 0 and col < area_width and masking[row][col] == 1:
                            masking[row][col] = 0
                            queue.append((row, col + 1)) # 동
                            queue.append((row, col - 1)) # 서
                            queue.append((row - 1, col)) # 남
                            queue.append((row + 1, col)) # 북
        
        max_safe_count = max(max_safe_count, count)
    print(max_safe_count)

n = int(sys.stdin.readline())
area = []
for _ in range(n):
    area.append(list(map(int, sys.stdin.readline().split())))

max_safe_area(area)