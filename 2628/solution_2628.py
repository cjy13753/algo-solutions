width, height = map(int, input().split())
num_cut = int(input())
horizontal = [0, height]
vertical = [0, width]
for i in range(num_cut):
    type, num = map(int, input().split())
    (horizontal if type == 0 else vertical).append(num)
horizontal.sort()
vertical.sort()

def solution(horizontal: list, vertical: list) -> None:
    max_height = max(horizontal[i + 1] - horizontal[i] for i in range(len(horizontal) - 1))
    max_width = max(vertical[i + 1] - vertical[i] for i in range(len(vertical) - 1))
    print(max_height * max_width)

solution(horizontal, vertical)