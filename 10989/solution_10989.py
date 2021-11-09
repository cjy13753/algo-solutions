# counting sort
def countingsort(nums: list) -> None:
    size = len(nums)
    max_elem = max(nums)

    count = [0] * (max_elem + 1)
    output = [0] * size

    for i in range(size):
        count[nums[i]] += 1

    for i in range(1, max_elem + 1):
        count[i] += count[i - 1]

    for i in range(size):
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1

    for i in range(size):
        nums[i] = output[i]

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

countingsort(nums)
print(nums)