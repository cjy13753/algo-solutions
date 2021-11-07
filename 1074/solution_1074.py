arr = [[0,1], [2,3]]

n, r, c = map(int, input().split())
def searchZ(n: int, r: int, c: int) -> int:
    if n == 1:
        return arr[r][c]
    return searchZ(n-1, r%pow(2,n-1), c%pow(2,n-1)) + pow(2, 2*(n-1)) * arr[r//pow(2, n-1)][c//pow(2, n-1)]

print(searchZ(n, r, c))