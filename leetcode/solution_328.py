# Summary:
    # your own answer?: yes
    # time spent: 1h20m
    # time complexity: O(n), Runtime: 44 ms, faster than 60.54% of Python3 online submissions for Odd Even Linked List.
    # space complexity: O(1), Memory Usage: 16.3 MB, less than 56.06% of Python3 online submissions for Odd Even Linked List.

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

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastOdd = head
        even = head

        if not head:
            return head

        while even.next and even.next.next:
            even = even.next
            evenAfterLastOdd = lastOdd.next
            nextOdd = even.next
            even.next = nextOdd.next
            nextOdd.next = evenAfterLastOdd
            lastOdd.next = nextOdd
            lastOdd = nextOdd

        return head

Solution()
