import sys

def largestRectangleArea(tests: list) -> None:
    for heights in tests:
        stack = []
        max_area = 0
        
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (idx - prev_idx))
                start = prev_idx
            
            stack.append([start, height])

        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        print(max_area)

tests = []
while True:
    input = list(map(int, sys.stdin.readline().split()))
    if input[0] == 0:
        break
    tests.append(input[1:])

largestRectangleArea(tests)