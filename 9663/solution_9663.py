import copy

n = int(input())

def solution(n: int) -> None:
    count = 0
    board = [[True for _ in range(n)] for _ in range(n)]
    for i in range(n):
        count += n_queen(n-1, i, copy.deepcopy(board), n)
    
    print(count)


def n_queen(row: int, col: int, board: list, size: int) -> int:
    count = 0
    
    # Trivial case 처리
    if board[row][col] == False:
        return 0
    
    if row == 0:
        return 1
    
    # Queen이 다니는 길 모두 False 처리
    for i in range(size):
        board[row][i] = False
    
    up = row - 1
    while up >= 0:
        board[up][col] = False
        up -= 1
    
    upper_left = [row - 1, col - 1]
    while upper_left[0] >= 0 and upper_left[1] >= 0:
        board[upper_left[0]][upper_left[1]] = False
        upper_left[0] -= 1
        upper_left[1] -= 1
    
    upper_right = [row - 1, col + 1]
    while upper_right[0] >= 0 and upper_right[1] < size:
        board[upper_right[0]][upper_right[1]] = False
        upper_right[0] -= 1
        upper_right[1] += 1
    
    # 바로 윗줄 셀들에 대해서 recursive call
    for i in range(size):
        count += n_queen(row-1, i, copy.deepcopy(board[:-1]), size)

    return count

solution(n)