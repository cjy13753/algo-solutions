import sys

def find_maximum_min_distance(houses_pos: list, req_routers: int) -> None:
    houses_pos.sort()
    start = 1
    end = houses_pos[-1] - houses_pos[0]
    max_min_len = 1

    while start <= end:
        min_len = start + (end - start) // 2
        prev_inst_house_pos = houses_pos[0]
        inst_routers = 1
        for i in range(1, len(houses_pos)):
            if houses_pos[i] - prev_inst_house_pos >= min_len:
                inst_routers += 1
                prev_inst_house_pos = houses_pos[i]
        
        if inst_routers >= req_routers:
            start = min_len + 1
            max_min_len = max(max_min_len, min_len)
        else:
            end = min_len - 1

    print(max_min_len)
        

num_houses, req_routers = map(int, sys.stdin.readline().split())
houses_pos = [int(sys.stdin.readline()) for _ in range(num_houses)]

find_maximum_min_distance(houses_pos, req_routers)