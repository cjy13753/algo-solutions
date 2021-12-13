# Summary:
    # refactored: edited variable names for better code readability with the logic intact 
    # your own answer?: yes
    # time spent: 30 minutes
    # time complexity: O(n), 28 ms, faster than 86.52% of Python3 online submissions for Swap Nodes in Pairs.
    # space complexity: O(1), 14.2 MB, less than 78.19% of Python3 online submissions for Swap Nodes in Pairs.

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
                head = ptr
                mid = ptr.next
                tail = mid.next

                head.next = tail
                mid.next = tail.next
                tail.next = mid

                ptr = mid
        
        return dummy.next

Solution()