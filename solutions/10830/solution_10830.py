import sys

def remn_matrix(matrix: list, power: int) -> list:
    size = len(matrix)
    if power == 1:
        return modulo(matrix)

    sub_matrix = remn_matrix(matrix, power // 2)
    if power % 2 == 1:
        return modulo(multiply(multiply(sub_matrix, sub_matrix), matrix))
    else:
        return modulo(multiply(sub_matrix, sub_matrix))

    
def multiply(matrix1: list, matrix2: list) -> list:
    size = len(matrix)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            row = matrix1[i]
            col = [matrix2[i][j] for i in range(size)]
            product = sum([row[i] * col[i] for i in range(size)])
            res[i][j] = product
    
    return res

def modulo(matrix: list) -> list:
    size = len(matrix)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            res[i][j] = matrix[i][j] % 1000
    
    return res

size, power = list(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(size):
    matrix.append(list(map(int, sys.stdin.readline().split())))

res = remn_matrix(matrix, power)
for row in res:
    print(*row)