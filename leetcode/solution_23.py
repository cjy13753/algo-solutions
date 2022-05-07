'''
Summary - Attempt #2 PASS

Your own answer? Yes
Time Complexity: O(nlogn) where n is the number of all nodes from lists. Visiting each node takes O(n) and heappush and heappop take O(nlogn).
Space Complexity: O(1)

Runtime: 104 ms, faster than 90.41% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18 MB, less than 44.93% of Python3 online submissions for Merge k Sorted Lists.
'''

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        minHeap = []
        for idx in range(len(lists)):
            if lists[idx] is not None:
                heapq.heappush(minHeap, (lists[idx].val, idx))

        while minHeap:
            _, idx = heapq.heappop(minHeap)
            tail.next = lists[idx]
            lists[idx] = lists[idx].next
            tail = tail.next
            tail.next = None
            
            if lists[idx] is not None:
                heapq.heappush(minHeap, (lists[idx].val, idx))

        return dummy.next

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