import sys

def num_hunts(hunters_coordinates:list, birds_coordinates: list) -> None:
    hunters_coordinates.sort()

    count = 0
    for bird_coordinate in birds_coordinates:
        bird_x_coordinate = bird_coordinate[0]
        min_x_diff = find_min_diff(bird_x_coordinate, hunters_coordinates)
        bird_y_coordindate = bird_coordinate[1]
        if min_x_diff + bird_y_coordindate <= gun_range:
            count += 1

    print(count)

def find_min_diff(bird_x_coordinate: int, hunters_coordinates: list) -> int:
    start = 0
    end = len(hunters_coordinates) - 1
    min_diff = float('inf')

    while start <= end:
        mid = start + (end - start) // 2
        x_diff = hunters_coordinates[mid] - bird_x_coordinate
        if x_diff > 0:
            end = mid - 1
            min_diff = min(min_diff, abs(x_diff))
        elif x_diff == 0:
            return x_diff
        else:
            start = mid + 1
            min_diff = min(min_diff, abs(x_diff))
    
    return int(min_diff)

num_hunters, num_birds, gun_range = list(map(int, sys.stdin.readline().split()))
hunters_coordinates = list(map(int, sys.stdin.readline().split()))
birds_coordinates = []
for _ in range(num_birds):
    birds_coordinates.append(list(map(int, sys.stdin.readline().split())))

num_hunts(hunters_coordinates, birds_coordinates)