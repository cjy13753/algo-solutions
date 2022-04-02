""" 
Attempt #1: PASS

My own answer: No
Reference: https://www.youtube.com/watch?v=fg2iGP4e2mc (동빈나 lecture in Korean)

Runtime: 1849 ms, faster than 83.88% of Python3 online submissions for Range Sum Query - Mutable.
Memory Usage: 31.2 MB, less than 64.62% of Python3 online submissions for Range Sum Query - Mutable.
"""


from typing import List

class BIT:
    def __init__(self, nums) -> None:
        self.nums = [0] * (len(nums) + 1)
        self.tree = [0] * (len(nums) + 1)
        self.size = len(nums)

        for i in range(1, len(nums) + 1):
            self.update(i, nums[i - 1])
            self.nums[i] = nums[i - 1]

    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        while index <= self.size:
            self.tree[index] += diff
            index += index & -index

class NumArray:
    def __init__(self, nums: List[int]):
        self.bit = BIT(nums)

    def update(self, index: int, val: int) -> None:
        index += 1
        self.bit.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        left += 1
        right += 1
        return self.bit.prefix_sum(right) - self.bit.prefix_sum(left - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)