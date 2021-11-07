n = int(input())

def count_hanoi(n:int) -> int:
    if n == 1:
        return 1
    return 2 * count_hanoi(n-1) + 1

paths = []
def paths_hanoi(n: int, src: str, aux: str, dst: str) -> None:
    if n == 1:
        paths.append(f"{src} {dst}")
        return
    paths_hanoi(n-1, src, dst, aux)
    paths.append(f"{src} {dst}")
    paths_hanoi(n-1, aux, src, dst)
    
print(count_hanoi(n))
if n <= 20:
    paths_hanoi(n, "1", "2", "3")
    print('\n'.join(paths))