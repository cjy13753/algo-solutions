import sys
input = sys.stdin.readline
INF = sys.maxsize

class Solution:
    def __init__(self) -> None:
        tabs, numItems = map(int, input().split())
        items = list(map(int, input().split()))

        self.minimumPlugouts(tabs, items, numItems)

    def minimumPlugouts(self, tabs:int, items: list, numItems: int) -> None:
        pluggedIns = set()

        cnt = 0
        for i in range(len(items)):
            if len(pluggedIns) < tabs:
                pluggedIns.add(items[i])
            else:
                if items[i] in pluggedIns:
                    continue
                else:
                    maxIdx = -1
                    itemAtMaxIdx = -1
                    remainingList = items[i + 1:]
                    for item in pluggedIns:
                        idx = remainingList.index(item) if item in remainingList else INF
                        if idx == INF:
                            itemAtMaxIdx = item
                            break
                        else:
                            if idx > maxIdx:
                                maxIdx = idx
                                itemAtMaxIdx = item
                    pluggedIns.remove(itemAtMaxIdx)
                    cnt += 1
                    pluggedIns.add(items[i])

        print(cnt)

Solution()