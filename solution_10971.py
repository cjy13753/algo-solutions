import sys

def find_min_cost(cities: list, res: list, cost_matrix: list, end: list = []) -> None:
    if (len(cities) == 0):
        total_cost = 0
        end = end + end[0:1]
        for i in range(len(end) - 1):
            cost = cost_matrix[end[i]][end[i+1]]
            if cost == 0:   
                return
            total_cost += cost
        res[0] = min(res[0], total_cost)

    else:
        for i in range(len(cities)):
            find_min_cost(cities[:i] + cities[i+1:], res, cost_matrix, end + cities[i:i+1])

n = int(sys.stdin.readline())
cities = []
for i in range(n):
    cities.append(i)
cost_matrix = []
for _ in range(n):
    cost_matrix.append(list(map(int, sys.stdin.readline().split())))

res = [10_000_000]
find_min_cost(cities, res, cost_matrix)
print(res[0])