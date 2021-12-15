'''
Summary

Attempt #1
time spent: 30 minutes
failed: Initial atttemp faield with "Error - Found cycle in the ListNode" with input head = [5]
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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_before_left = head
        left_node = head
        left_idx = 1
        while left_idx < left:
            left_before_left = left_node
            left_node = left_node.next
            left_idx += 1
        
        right_node = left_node.next
        right_idx = left_idx + 1
        while right_idx <= right:
            right_after_right = right_node.next
            right_node.next = left_node
            left_node = right_node
            right_node = right_after_right
            right_idx += 1
        
        if left_before_left.next:
            left_before_left.next.next = right_node
        left_before_left.next = left_node

        return head

Solution()