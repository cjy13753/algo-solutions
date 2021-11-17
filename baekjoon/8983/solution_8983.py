import sys

def num_hunts(hunters_x:list, birds_xy: list, gun_range: int) -> None:
    hunters_x.sort()

    count = 0
    for bird_xy in birds_xy:
        bird_x, bird_y = bird_xy[0], bird_xy[1]
        start = 0
        end = len(hunters_x) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if abs(hunters_x[mid] - bird_x) + bird_y <= gun_range:
                count += 1
                break

            if hunters_x[mid] > bird_x:
                end = mid - 1
            elif hunters_x[mid] == bird_x:
                break
            else:
                start = mid + 1
    print(count)

n_hunters, n_birds, gun_range = list(map(int, sys.stdin.readline().split()))
hunters_x = list(map(int, sys.stdin.readline().split()))
birds_xy = []
for _ in range(n_birds):
    birds_xy.append(list(map(int, sys.stdin.readline().split())))

num_hunts(hunters_x, birds_xy, gun_range)