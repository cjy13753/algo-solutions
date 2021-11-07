n = int(input())

def solveNQueens(n: int) -> list:
    res = [0]
    dsf([-1] * n, 0, res)
    return res

def dsf(queens: list, curr_row: int, res: list) -> None:
    if curr_row == len(queens):
        res[0] += 1
        return
    
    for col in range(len(queens)):
        queens[curr_row] = col
        if check_valid(queens, curr_row):
            dsf(queens, curr_row + 1, res)

def check_valid(queens, curr_row):
    for prev_row in range(curr_row):
        if abs(queens[curr_row] - queens[prev_row]) == curr_row - prev_row or queens[curr_row] == queens[prev_row]:
            return False
    return True

print(solveNQueens(n)[0])