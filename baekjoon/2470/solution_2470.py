import sys

def print_couple_with_sum_closest_to_zero(num_solutions: int, solutions: list) -> None:
    solutions.sort()

    pt_front = 0
    pt_back = num_solutions - 1
    min_abs_sum = float('inf') # 애매하게 1,999,999,999 했다가 로직 에러로 실패
    couple = [0, 0]

    while pt_front < pt_back:
        front_num, back_num = solutions[pt_front], solutions[pt_back]
        sum = front_num + back_num
        if sum > 0:
            pt_back -= 1
        elif sum == 0:
            print(f"{front_num} {back_num}")
            return
        else:
            pt_front += 1
        
        if abs(sum) < min_abs_sum:
            min_abs_sum = abs(sum)
            couple[0], couple[1] = front_num, back_num
    
    print(f"{couple[0]} {couple[1]}")

num_solutions = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

print_couple_with_sum_closest_to_zero(num_solutions, solutions)