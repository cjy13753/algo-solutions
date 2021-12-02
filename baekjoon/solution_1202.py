import sys
INF = sys.maxsize
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numJewels, numSacks = map(int, input().split())
        jewels = []
        for _ in range(numJewels):
            weight, value = map(int, input().split())
            jewels.append([value, weight]) # jewels[i] = [value, weight]

        sacks = []
        for _ in range(numSacks):
            sacks.append(int(input()))
        
        self.maxValue(jewels, sacks, numSacks)

    # 보석들을 (1순위: 가치 내림차순, 2순위: 무게 내림차순) 정렬한 후, 견딜 수 있는 무게가 가장 낮은 가방부터 차례로 보석들을 넣어본다.
    # 가방의 경우 견딜 수 있는 무게가 낮은 것부터 오름차순으로 정렬한다.
    def maxValue(self, jewels: list, sacks: list, numSacks: int) -> None:
        jewels.sort(key=lambda x: (x[0], x[1]), reverse=True)
        sacks.sort()
        usedSacks = [False] * len(sacks)

        maxPrice = 0

        for value, weight in jewels:
            start = 0
            end = numSacks - 1

            minWeightIdx = INF
            while start <= end:
                mid = start + (end - start) // 2
                if weight <= sacks[mid]:
                    if usedSacks[mid] == False:
                        minWeightIdx = min(minWeightIdx, mid)
                    else:
                        left = mid - 1
                        right = mid + 1
                    end = mid - 1
                else:
                    start = mid + 1
            
            if minWeightIdx != INF:
                usedSacks[minWeightIdx] = True
                maxPrice += value

        print(maxPrice)

Solution()