i1 = list(map(int, input().split()))
num_to_compare = i1[1]
num_list = list(map(int, input().split()))

def solution(num_to_compare: int, num_list: list) -> None:
    answer = []
    for num in num_list:
        if (num < num_to_compare):
            answer.append(num)

    print(*answer)

solution(num_to_compare, num_list)