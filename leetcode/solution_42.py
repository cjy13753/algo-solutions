import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        height = [5,4,1,2]
        print(self.trap(height))

    # 기본적인 접근법은 각 층마다 빗물 카운트하면서 모든 높이까지 반복하기
    # 1 이상인 숫자가 나오면 그때부터 다음 1이상인 숫자가 나올 때까지 가로길이 구하기
    # 1 이상인 숫자가 실제로 나오면 가로길이 * 1 만큼을 최종 결과에 더해주고, 다시 초기화
    # 배열의 숫자를 1씩 차감해준다
    # 위의 과정을 높이가 1 이상인 배열의 요소가 2개 미만이 될 때까지 반복
    def trap(self, height: List[int]) -> int:
        maxWidth = len(height)
        ans = 0
        while max(height) > 0:
            i = 0
            switch = False
            tmp = 0
            while i <= maxWidth - 1:
                if switch == True:
                    if height[i] <= 0:
                        tmp += 1
                    else:
                        ans += tmp
                        tmp = 0
                else:
                    if height[i] > 0:
                        switch = True

                i += 1
            for j in range(maxWidth):
                height[j] -= 1

        return ans

Solution()