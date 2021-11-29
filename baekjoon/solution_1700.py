import sys
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        tabs, numItems = map(int, input().split())
        items = list(map(int, input().split()))

        self.minimumPlugouts(tabs, items)

    def minimumPlugouts(self, tabs:int, items: list) -> None:
        plugged = set()
        cnt = 0
        for i in range(len(items)):
            if len(plugged) < tabs:
                plugged.add(items[i])
            else:
                if items[i] in plugged:
                    continue
                else:
                    notToBeUsed = plugged - set(items[i + 1:])
                    if len(notToBeUsed) == 0:
                        plugged.pop()
                        cnt += 1
                        plugged.add(items[i])
                    else:
                        plugged.remove(notToBeUsed.pop())
                        cnt += 1
                        plugged.add(items[i])
        print(cnt)

Solution()