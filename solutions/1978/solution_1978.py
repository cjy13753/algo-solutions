given_nums = input()
nums_list = list(map(int, input().split()))

def solution(num_list: list) -> None:
    prime_num_list = {2}
    for num in range(3, max(num_list) + 1):
        is_prime = True
        for prime_num in prime_num_list:
            if (num % prime_num == 0):
                is_prime = False
                break
        if (is_prime == True):
            prime_num_list.add(num)
    
    count = 0
    for num in num_list:
        if (num in prime_num_list):
            count += 1
    
    print(count)

solution(nums_list)