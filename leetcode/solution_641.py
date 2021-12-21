'''
Summary (leetcode 641. Design Circular Deque)

Attempt #1
Your own answer?: Yes
Time spent: 30m
Runtime: 72 ms, faster than 63.57% of Python3 online submissions for Design Circular Deque.
Memory Usage: 15.2 MB, less than 19.35% of Python3 online submissions for Design Circular Deque.
Approach: similar to my solution to leetcode 622(designing circular queue). This time, I adopted the idea of keeping track of current size of the queue.

Problem link: https://leetcode.com/problems/design-circular-deque/
'''

import sys
input = sys.stdin.readline

class MyCircularDeque:

    def __init__(self, k: int):
        self.currSize = 0
        self.maxSize = k
        self.head = -1
        self.tail = -1
        self.arr = [0] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            self.arr[0] = value
            self.currSize += 1
            return True
        else:
            self.head = (self.head - 1) % self.maxSize
            self.arr[self.head] = value
            self.currSize += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            self.arr[0] = value
            self.currSize += 1
            return True
        else:
            self.tail = (self.tail + 1) % self.maxSize
            self.arr[self.tail] = value
            self.currSize += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.currSize == 1:
            self.head = -1
            self.tail = -1
            self.currSize = 0
            return True
        else:
            self.head = (self.head + 1) % self.maxSize
            self.currSize -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.currSize == 1:
            self.head = -1
            self.tail = -1
            self.currSize = 0
            return True
        else:
            self.tail = (self.tail - 1) % self.maxSize
            self.currSize -= 1
            return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.tail]

    def isEmpty(self) -> bool:
        return True if self.currSize == 0 else False

    def isFull(self) -> bool:
        return True if (self.head - 1) % self.maxSize == self.tail else False

        # Helper function to display the current queue
    def printElements(self) -> None:
        if self.head == -1 and self.tail == -1:
            return
        if self.head <= self.tail:
            for i in range(self.head, self.tail + 1):
                print(self.arr[i])
        else:
            for i in range(self.head, self.currSize):
                print(self.arr[i])
            for i in range(self.tail + 1):
                print(self.arr[i])
        
# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
obj.insertFront(1)
obj.insertFront(2)
obj.insertLast(3)
print(obj.deleteFront())
obj.printElements()
print(obj.deleteLast())
obj.printElements()