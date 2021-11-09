import sys

def mergesort(nums: list) -> None:
    if len(nums) > 1:
            
        partition_index = len(nums) // 2
        L = nums[:partition_index]
        R = nums[partition_index:]
        
        mergesort(L)
        mergesort(R)

        i = 0
        p = 0
        q = 0
        
        while p < len(L) and q < len(R):
            if L[p] <= R[q]:
                nums[i] = L[p]
                p += 1
            else:
                nums[i] = R[q]
                q += 1
            i += 1
        
        while p < len(L):
            nums[i] = L[p]
            p += 1
            i += 1
        
        while q < len(R):
            nums[i] = R[q]
            q += 1
            i += 1


n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

mergesort(nums)
for num in nums:
    print(num)