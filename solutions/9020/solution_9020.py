from collections import OrderedDict

num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcases.append(int(input()))

def solution(testcases: list) -> None:
    prime_num_list = OrderedDict()
    prime_num_list[2] = None

    for num in range(3, max(testcases)):
        is_prime = True
        for prime_num in prime_num_list:
            if (num % prime_num == 0):
                is_prime = False
                break
        if (is_prime == True):
            prime_num_list[num] = None
    
    for testcase in testcases:
        find_combination(testcase, prime_num_list)

def find_combination(testcase: int, prime_num_list: OrderedDict) -> None:
    possible_combination = ()
    smallest_difference = 10000
    for prime_num in prime_num_list:
        if (prime_num > testcase):
            break
        
        other_prime_num = testcase - prime_num
        if other_prime_num in prime_num_list:
            difference = abs(other_prime_num - prime_num)
            if difference < smallest_difference:
                smallest_difference = difference
                possible_combination = (prime_num, other_prime_num)
    
    print(f"{possible_combination[0]} {possible_combination[1]}")
    

solution(testcases)

