import sys
import random

# Quick sort
def quicksort(nums):
    quicksort_core(nums, 0 ,len(nums) - 1)

def quicksort_core(nums: list, start: int, end: int) -> None:
    if len(nums[start:end + 1]) <= 1:
        return
    if start > end:
        return
    
    p = partition(nums, start, end)
    quicksort_core(nums, start, p - 1)
    quicksort_core(nums, p + 1, end)

def partition(nums: list, start: int, end: int) -> int:
    i = start
    p = start
    r = end

    m = find_median(nums, start, end)
    swap(nums, m, r)

    while i < r:
        if (nums[i] < nums[r]):
            swap(nums, p, i)
            p += 1
        i += 1
    
    swap(nums, p, r)

    return p

def find_median(nums, start, end):
    index1 = random.randint(start, end)
    num1 = nums[index1]
    index2 = random.randint(start, end)
    num2 = nums[index2]
    index3 = random.randint(start, end)
    num3 = nums[index3]

    if num1 > num2:
        if num2 > num3:
            return index2
        else:
            if num1 > num3:
                return index3
            else:
                return index1
    else:
        if num1 > num3:
            return index1
        else:
            if num2 > num3:
                return index3
            else:
                return index2

def swap(nums: list, a: int, b: int) -> None:
    tmp = nums[a]
    nums[a] = nums[b]
    nums[b] = tmp

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

quicksort(nums)
for i in range(len(nums)):
    print(nums[i])