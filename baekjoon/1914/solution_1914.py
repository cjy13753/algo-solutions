n = int(input())

def count_hanoi(n:int) -> int:
    if n == 1:
        return 1
    return 2 * count_hanoi(n-1) + 1

def paths_hanoi(n: int, src: str, aux: str, dst: str, res: list) -> None:
    if n == 1:
        res.append(f"{src} {dst}")
        return
    paths_hanoi(n-1, src, dst, aux, res)
    res.append(f"{src} {dst}")
    paths_hanoi(n-1, aux, src, dst, res)
    

print(count_hanoi(n))
if n <= 20:
    res = []
    paths_hanoi(n, "1", "2", "3", res)
    print('\n'.join(res))