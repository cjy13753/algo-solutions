import sys

def find_maximum_height(minimum_length: int, trees_heights: list, highest: list = [0], start = 0, end = 2_000_000_000) -> None:
    if start > end:
        print(highest[0])
        return
    
    mid = start + (end - start) // 2
    timber_length = calculate_length(mid, trees_heights)
    if timber_length > minimum_length:
        highest[0] = max(highest[0], mid)
        find_maximum_height(minimum_length, trees_heights, highest, mid + 1, end)
    elif timber_length == minimum_length:
        print(mid)
        return
    else:
        find_maximum_height(minimum_length, trees_heights, highest, start, mid - 1)
        
    

def calculate_length(mid: int, trees_heights: list) -> int:
    length = 0
    for tree_height in trees_heights:
        remn = tree_height - mid
        if  remn > 0:
            length  += remn
    return length

num_trees, minimum_length = map(int, sys.stdin.readline().split())
trees_heights = list(map(int, sys.stdin.readline().split()))

find_maximum_height(minimum_length, trees_heights)