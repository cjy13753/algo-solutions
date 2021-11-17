import sys

def remn_matrix(matrix: list, power: int) -> list:
    if power == 1:
        modulo(matrix)
        return matrix

    sub_matrix = remn_matrix(matrix, power // 2)
    squared = multiply(sub_matrix, sub_matrix)
    if power % 2 == 1:
        product = multiply(squared, matrix)
        modulo(product)
        return product
    else:
        modulo(squared)
        return squared
    
def multiply(matrix1: list, matrix2: list) -> list:
    size = len(matrix)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            row = matrix1[i]
            col = [matrix2[k][j] for k in range(size)]
            res[i][j] = sum([row[k] * col[k] for k in range(size)])
    
    return res

def modulo(matrix: list) -> None:
    for i in range(size):
        for j in range(size):
            matrix[i][j] = matrix[i][j] % 1000

size, power = list(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(size):
    matrix.append(list(map(int, sys.stdin.readline().split())))

res = remn_matrix(matrix, power)
for row in res:
    print(*row)