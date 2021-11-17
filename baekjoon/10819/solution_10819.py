import sys

def find_max(nums: list) -> int:
    results = []
    perm(nums,results)

    max_sum = 0
    for result in results:
        max_sum = max(max_sum, cal_sum_of_diff(result))
    
    return max_sum


def perm(start: list, res: list, end: list = []) -> None:
    if (len(start) == 0):
        res.append(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], res, end + start[i:i+1]) 

def cal_sum_of_diff(nums: list) -> int:
    sum = 0
    for i in range(len(nums) - 1):
        sum += abs(nums[i] - nums[i + 1])

    return sum

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(find_max(nums))