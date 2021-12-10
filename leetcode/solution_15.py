import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        nums = [-2,0,1,1,2]
        print(self.threeSum(nums))

    # 정렬을 한다.(최종 결과값이 index의 모음이 아니기 때문에 정렬이 가능)
    # left, right idx pointer를 잡아두고, [left + 1, right - 1] inclusive 범위에서 이분탐색해서 -(nums[left] + nums[right])의 값과 일치하는 값이 있는지 확인
    # 값이 존재하면 그때의 값들의 조합을 set 자료구조에 넣어둔다.(duplicate triplet 방지 위함)
    # nums[left] + nums[right]의 값이 음수면 left++, 양수면 right--
    # 약간의 최적화를 위해서 left == prevLeft, right == prevRight이면 pass한다.
    # 시간 복잡도 O(nlogn), 공간 복잡도 O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        leftIdx = 0
        rightIdx = len(nums) - 1
        queue = deque()
        queue.append((leftIdx, rightIdx))
        ans = set()

        def binarySearch(leftIdx: int, rightIdx: int, twoSum: int) -> bool:
            if leftIdx > rightIdx:
                return False
            
            while leftIdx <= rightIdx:
                mid = leftIdx + (rightIdx - leftIdx) // 2
                if nums[mid] > twoSum:
                    rightIdx = mid - 1
                    continue
                if nums[mid] == twoSum:
                    return True
                else:
                    leftIdx = mid + 1
                    continue
            return False

        visited = set()
        while queue:
            leftIdx, rightIdx = queue.popleft()
            visited.add((leftIdx, rightIdx))
            
            twoSum = nums[leftIdx] + nums[rightIdx]
            if binarySearch(leftIdx + 1, rightIdx - 1, -twoSum):
                ans.add((nums[leftIdx], -twoSum, nums[rightIdx]))
            if twoSum > 0:
                if (leftIdx, rightIdx - 1) not in visited and leftIdx < rightIdx - 1:
                    queue.append((leftIdx, rightIdx - 1))
            elif twoSum == 0:
                if (leftIdx, rightIdx - 1) not in visited and leftIdx < rightIdx - 1:
                    queue.append((leftIdx, rightIdx - 1))
                if (leftIdx + 1, rightIdx) not in visited and leftIdx + 1 < rightIdx:
                    queue.append((leftIdx + 1, rightIdx))
            else:
                if (leftIdx + 1, rightIdx) not in visited and leftIdx + 1 < rightIdx:
                    queue.append((leftIdx + 1, rightIdx))

        return list(ans)

Solution()