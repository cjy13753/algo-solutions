import sys

class Solution():

    def __init__(self) -> None:
        self.histogram = []

    def largestRectangleArea(self, start: int, end: int) -> int:
        if len(self.histogram[start: end + 1]) == 1:
            return self.histogram[start]
            
        mid = start + (end - start) // 2
        leftArea = self.largestRectangleArea(start, mid)
        rightArea = self.largestRectangleArea(mid + 1, end)

        mArea = self.middleArea(start, mid, end)

        return max(leftArea, mArea, rightArea)

    def middleArea(self, start, mid, end) -> int:
        left = mid - 1
        right = mid + 1
        height = self.histogram[mid]
        maxArea = height

        while left >= start and right <= end:
            if self.histogram[left] > self.histogram[right]:
                height = min(height, self.histogram[left])
            else:
                height = min(height, self.histogram[right])

            maxArea = max(maxArea, height * (right - left))
            if self.histogram[left] > self.histogram[right]:
                left -= 1
            else:
                right += 1
        
        while left >= start:
            height = min(height, self.histogram[left])
            maxArea = max(maxArea, height * (right - left))
            left -= 1

        while right <= end:
            height = min(height, self.histogram[right])
            maxArea = max(maxArea, height * (right - left))
            right += 1
        
        return maxArea

solution = Solution()
while True:
    input = list(map(int, sys.stdin.readline().split()))
    if input[0] == 0:
        break
    solution.histogram = input[1:]
    print(solution.largestRectangleArea(0, len(solution.histogram) - 1))