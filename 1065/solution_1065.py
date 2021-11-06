num = int(input())

def solution(num: int) -> None:
    if (num < 100):
        print(num)
        return
    
    count = 99
    for n in range(100, num + 1):
        n_str = str(n)
        diff = int(n_str[1]) - int(n_str[0])
        is_equal = True
        for i in range(1, len(n_str) - 1):
            if (int(n_str[i + 1]) - int(n_str[i]) != diff):
                is_equal = False
                break
        
        if (is_equal == True):
            count += 1
    
    print(count)

solution(num)