n, t_row, t_col = map(int, input().split())

def searchZ(n: int, t_row: int, t_col: int, base_quad: list) -> int:
    if n == 1:
        return base_quad[t_row][t_col]
    
    t_prime_row = t_row%pow(2,n-1)
    t_prime_col = t_col%pow(2,n-1)

    prev_quad_size =  pow(2, 2*(n - 1))

    base_quad_row = t_row//pow(2, n-1)
    base_quad_row = t_col//pow(2, n-1)

    return searchZ(n-1, t_prime_row, t_prime_col, base_quad) \
            + prev_quad_size * base_quad[base_quad_row][base_quad_row]

base_quad = [[0,1], [2,3]]
print(searchZ(n, t_row, t_col, base_quad))