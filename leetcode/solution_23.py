'''
Summary - Attempt #1 FAIL

Your own answer? Yes
Time spent: 50m
Fail reason: Time Limit Exceeded (passed only leetcode example testcases)
Time Complexity: O(n * m), where n is the number of list in lists and m is the length of a list with the most number of nodes.
Space Complexity: O(1)
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = None
        ansTail = None
        isFinished = False
        length = len(lists)

        while isFinished is False:
            minIdx = None
            minNode = None
            count = 0
            for i in range(length):
                if lists[i] is None:
                    continue
                count += 1
                if minIdx == None:
                    minIdx = i
                    minNode = lists[i]
                else:
                    if lists[i].val < minNode.val:
                        minIdx = i
                        minNode = lists[i]

            if count == 0:
                isFinished = True
            else:
                if ans is None:
                    ans = ListNode(lists[minIdx].val)
                    ansTail = ans
                else:
                    ansTail.next = ListNode(lists[minIdx].val)
                    ansTail = ansTail.next
                lists[minIdx] = lists[minIdx].next
                

        return ans

solution = Solution()

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

ans = solution.mergeKLists([list1, list2, list3])
while ans is not None:
    print(ans.val)
    ans = ans.next