'''
Summary

Attempt #2
aggregated time spent: 1h50m
time complexity: O(n), Runtime: 39 ms, faster than 20.16% of Python3 online submissions for Reverse Linked List II.
space complexity: O(1), Memory Usage: 14.5 MB, less than 44.23% of Python3 online submissions for Reverse Linked List II.
'''

import sys
input = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
        pass

    def reverseBetween(self, head: Optional[ListNode], left_idx: int, right_idx: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        left_before_left = dummy
        left = left_before_left.next
        idx = 1
        while idx < left_idx:
            left_before_left = left
            left = left.next
            idx += 1
        
        left_first = left
        right = left.next
        while right and idx < right_idx:
            tmp = right.next
            right.next = left
            left = right
            right = tmp
            idx += 1
        
        left_before_left.next = left
        left_first.next = right

        return dummy.next

Solution()