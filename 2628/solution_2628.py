width, height = map(int, input().split())
num_cut = int(input())
horizontal_cut_num = []
vertical_cut_num = []
for i in range(num_cut):
    cut = list(map(int, input().split()))
    if (cut[0] == 0):
        horizontal_cut_num.append(cut[1])
    else:
        vertical_cut_num.append(cut[1])

def solution(width: int, height: int, horizontal_cut_num: list, vertical_cut_num: list) -> None:
    pieces_height = []
    pieces_width = []

    if (len(horizontal_cut_num) > 0):
        horizontal_cut_num.sort()
        pieces_height.append(horizontal_cut_num[0])
        for i in range(len(horizontal_cut_num) - 1):
            pieces_height.append(horizontal_cut_num[i + 1] - horizontal_cut_num[i])
        pieces_height.append(height - horizontal_cut_num[-1])
    else:
        pieces_height.append(height)
    
    if (len(vertical_cut_num) > 0):
        vertical_cut_num.sort()
        pieces_width.append(vertical_cut_num[0])
        for i in range(len(vertical_cut_num) - 1):
            pieces_width.append(vertical_cut_num[i + 1] - vertical_cut_num[i])
        pieces_width.append(width - vertical_cut_num[-1])
    else:
        pieces_width.append(width)
    
    print(max(pieces_height) * max(pieces_width))
    

solution(width, height, horizontal_cut_num, vertical_cut_num)