import sys

def snowwhite(dwarfs: list) -> None:
    total_of_nine = sum(dwarfs)
    for i in range(len(dwarfs) - 1):
        for j in range(i + 1, len(dwarfs)):
            if total_of_nine - dwarfs[i] - dwarfs[j] == 100:
                heights = []
                for k in range(len(dwarfs)):
                    if k != i and k != j:
                        heights.append(dwarfs[k])
                heights.sort()
                for height in heights:
                    print(height)
                return

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

snowwhite(dwarfs)