import sys

def find_wht_bl(mtrx: list, row_start: int, row_end: int, col_start: int, col_end: int, res: list) -> None:
    if row_start == row_end:
        if mtrx[row_start][col_start] == 0:
            res[0] += 1
        else:
            res[1] += 1
        return
    
    base_case = mtrx[row_start][col_start]
    flag = True
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if mtrx[i][j] != base_case:
                flag = False
                break
        if flag == False:
            break
    
    if flag == False:
        row_mid = row_start + (row_end - row_start) // 2
        col_mid = col_start + (col_end - col_start) // 2
        find_wht_bl(mtrx, row_start, row_mid, col_start, col_mid, res) # 1사분면
        find_wht_bl(mtrx, row_start, row_mid, col_mid + 1, col_end, res) # 2사분면
        find_wht_bl(mtrx, row_mid + 1, row_end, col_start, col_mid, res) # 3사분면
        find_wht_bl(mtrx, row_mid + 1, row_end, col_mid + 1, col_end, res) # 4사분면
    else:
        if base_case == 0:
            res[0] += 1
        else:
            res[1] += 1

mtrx = []
for _ in range(int(sys.stdin.readline())):
    mtrx.append(list(map(int, sys.stdin.readline().split())))

res = [0, 0] # res[0]: white - 0, res[1]: blue - 1
find_wht_bl(mtrx, 0, len(mtrx) - 1, 0, len(mtrx) - 1, res)
print(res[0])
print(res[1])