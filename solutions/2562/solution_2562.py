num_list = []
for i in range(9):
    num_list.append(int(input()))

def solution(num_list: list) -> None:
    max_num = 0
    index = 0
    for i in range(len(num_list)):
        if (num_list[i] > max_num):
            max_num = num_list[i]
            index = i
    print(max_num)
    print(index + 1)

solution(num_list)