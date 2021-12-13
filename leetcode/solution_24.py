# Summary:
    # your own answer?: yes
    # time spent: 30 minutes
    # time complexity: O(n), 32 ms, faster than 66.97% of Python3 online submissions for Swap Nodes in Pairs.
    # space complexity: O(1), 14.4 MB, less than 17.10% of Python3 online submissions for Swap Nodes in Pairs.

import sys
input = sys.stdin.readline

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
        pass

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = dummy

        while ptr.next != None:
            if ptr.next.next == None:
                break
            else:
                tmpPtrNext = ptr.next
                ptr.next = ptr.next.next
                tmpPtrNext.next = ptr.next.next
                ptr.next.next = tmpPtrNext
                ptr = tmpPtrNext
        
        return dummy.next

Solution()