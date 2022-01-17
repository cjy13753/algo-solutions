'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 35m

Time Complexity: O(N^2) since the problem requires using insertion sorting algorithm.
Runtime: 2448 ms, faster than 15.81% of Python3 online submissions for Insertion Sort List.

Space Complexity: O(1) thanks to in-place sorting
Memory Usage: 16.4 MB, less than 31.09% of Python3 online submissions for Insertion Sort List.

Memo: I spent most of the time comming up with prev and now pointer. Other than that, fairly simple question.
'''

import sys
from typing import Optional
input = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        cur = head
        while cur:
            temp = cur
            cur = cur.next
            temp.next = None

            prev = dummy
            now = dummy.next
            while prev:
                if not now:
                    prev.next = temp
                    break
                if now.val > temp.val:
                    prev.next = temp
                    temp.next = now
                    break
                else:
                    prev = now
                    now = now.next
        
        return dummy.next

Solution()