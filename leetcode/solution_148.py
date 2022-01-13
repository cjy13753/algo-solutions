'''
Summary - Ateempt #1

Your own answer?: Yes
Time Spent: 21m

Time Complexity: O(NlogN)
Runtime: 255 ms, faster than 84.47% of Python3 online submissions for Sort List.
Space Complexity: O(N)
Memory Usage: 38.1 MB, less than 11.97% of Python3 online submissions for Sort List.
'''

import sys
from typing import Optional
input = sys.stdin.readline

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        tempArr = []
        cur = head
        while cur:
            tempArr.append(cur.val)
            cur = cur.next
        tempArr.sort()

        dummyHead = ListNode(-1000)
        cur = dummyHead
        for i in tempArr:
            cur.next = ListNode(i)
            cur = cur.next

        return dummyHead.next

Solution()