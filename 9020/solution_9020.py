num_testcases = int(input())
testcases = []
for i in range(num_testcases):
    testcases.append(int(input()))

def solution(testcases: list) -> None:
    for testcase in testcases:
        find_combination(testcase)

def find_combination(testcase: int) -> None:
    prime_num_list = {2}
    
    for num in range(3, testcase):
        is_prime = True
        for prime_num in prime_num_list:
            if (num % prime_num == 0):
                is_prime = False
                break
        if (is_prime == True):
            prime_num_list.add(num)
        
    possible_combination = ()
    smallest_difference = 10000
    for prime_num in prime_num_list:
        other_prime_num = testcase - prime_num
        if other_prime_num in prime_num_list:
            difference = abs(prime_num - other_prime_num)
            if difference < smallest_difference:
                smallest_difference = difference
                possible_combination = (prime_num, other_prime_num)
    
    print(f"{min(possible_combination)} {max(possible_combination)}")
    

solution(testcases)

