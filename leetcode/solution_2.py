# Summary:
    # your own answer?: yes, with 1 preceding failed attempt with 'wrong answer' message
    # time spent: 45 minutes
    # time complexity: O(n), Runtime: 73 ms, faster than 39.78% of Python3 online submissions for Add Two Numbers.
    # space complexity: O(n), Memory Usage: 14.5 MB, less than 12.10% of Python3 online submissions for Add Two Numbers.

# approach sketch
    # Store numbers in singly-linked-lists in queues created for each list
    # while adding two numbers from each queue and storing the modulus of the sum in a different queue(tmpQueue), store a roundup number in a temporary variable    
    # after completing adding numbers, make a singly linked list out of the tmpQueue by popping left sequentially.

import sys
input = sys.stdin.readline
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        queue1 = deque()
        queue1.append(l1.val)
        queue2 = deque()
        queue2.append(l2.val)
        
        tmpQueue = deque()

        while l1.next != None:
            l1 = l1.next
            queue1.append(l1.val)
        
        while l2.next != None:
            l2 = l2.next
            queue2.append(l2.val)

        roundUp = 0
        while queue1 and queue2:
            e1 = queue1.popleft()
            e2 = queue2.popleft()

            if e1 + e2 + roundUp > 9:
                tmpQueue.append(e1 + e2 + roundUp - 10)
                roundUp = 1
            else:
                tmpQueue.append(e1 + e2 + roundUp)
                roundUp = 0

        while queue1:
            e1 = queue1.popleft()

            if e1 + roundUp > 9:
                tmpQueue.append(e1 + roundUp - 10)
                roundUp = 1
            else:
                tmpQueue.append(e1 + roundUp)
                roundUp = 0
        
        while queue2:
            e2 = queue2.popleft()

            if e2 + roundUp > 9:
                tmpQueue.append(e2 + roundUp - 10)
                roundUp = 1
            else:
                tmpQueue.append(e2 + roundUp)
                roundUp = 0

        if roundUp == 1:
            tmpQueue.append(1)

        ans = ListNode(tmpQueue.popleft())
        ptr = ans
        while tmpQueue:
            ptr.next = ListNode(tmpQueue.popleft())
            ptr = ptr.next

        return ans

Solution()