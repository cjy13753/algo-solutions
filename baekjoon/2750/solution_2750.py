# Bubble sort
num = int(input())

num_ls = []
for _ in range(num):
    num_ls.append(int(input()))

def sort(num_ls: list) -> None:
    ls_size = len(num_ls)
    if ls_size < 2:
        return

    for i in range(ls_size - 1):
        front = 0
        back = 1
        for j in range(ls_size -1 -i):
            if num_ls[front] > num_ls[back]:
                swap(front, back, num_ls)
            front += 1
            back += 1

def swap(front: int, back: int, num_ls: list) -> None:
    tmp = num_ls[front]
    num_ls[front] = num_ls[back]
    num_ls[back] = tmp

sort(num_ls)
for i in range(len(num_ls)):
    print(num_ls[i])