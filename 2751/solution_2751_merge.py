import sys

def mergesort(nums: list) -> None:
    merged = mergesort_core(nums)
    for num in merged:
        print(num)

def mergesort_core(nums: list) -> list:
    if len(nums) <= 1:
        return nums

    partition_index = len(nums) // 2
    arr_left = mergesort_core(nums[:partition_index])
    arr_right = mergesort_core(nums[partition_index:])
    
    return merge(arr_left, arr_right)


def merge(nums1: list, nums2: list) -> list:
    i = 0
    p = 0
    q = 0
    tmp = [0] * (len(nums1) + len(nums2))

    while p < len(nums1) and q < len(nums2):
        if nums1[p] <= nums2[q]:
            tmp[i] = nums1[p]
            p += 1
        else:
            tmp[i] = nums2[q]
            q += 1
        i += 1
    
    while p < len(nums1):
        tmp[i] = nums1[p]
        p += 1
        i += 1
    
    while q < len(nums2):
        tmp[i] = nums2[q]
        q += 1
        i += 1

    return tmp

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

mergesort(nums)