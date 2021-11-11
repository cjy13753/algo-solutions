import sys

def max_heapsort(arr: list) -> None:
    last_index = len(arr) - 1

    # build heap
    for i in range((last_index - 1) // 2, -1, -1):
        max_heapify(arr, i, last_index)

    # rearrange
    for i in range(last_index, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i - 1)

def max_heapify(arr:list, i: int, last_index: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left <= last_index and arr[left] > arr[largest]:
        largest = left
    
    if right <= last_index and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, last_index)

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

max_heapsort(nums)
for num in nums:
    print(num)