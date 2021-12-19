'''
Summary

Your own answer?: Yes
Time spent: 55m
Runtime: 68 ms, faster than 77.25% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.9 MB, less than 34.13% of Python3 online submissions for Design Circular Queue.
Approach: Use array as an internal data structure and initialze head index and tail index to -1 to indicate that the queue is empty.

Problem link: https://leetcode.com/problems/design-circular-queue/
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.cQueue = [0] * k
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.head == -1 and self.tail == -1:
            self.head = 0
            self.tail = 0
            self.cQueue[0] = value
            return True

        if self.tail + 1 < self.size:
            if self.tail + 1 == self.head:
                return False
            else:
                self.cQueue[self.tail + 1] = value
                self.tail += 1
                return True
        else:
            if 0 == self.head:
                return False
            else:
                self.cQueue[0] = value
                self.tail = 0
                return True

    def deQueue(self) -> bool:
        if self.head == -1 and self.tail == -1:
            return False
        
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        else:
            if self.head + 1 < self.size:
                self.head += 1
                return True
            else:
                self.head = 0
                return True

    def Front(self) -> int:
        if self.head == -1 and self.tail == -1:
            return -1
        else:
            return self.cQueue[self.head]
        

    def Rear(self) -> int:
        if self.head == -1 and self.tail == -1:
            return -1
        else:
            return self.cQueue[self.tail]

    def isEmpty(self) -> bool:
        return True if self.head == -1 and self.tail == -1 else False
        

    def isFull(self) -> bool:
        if self.head == 0:
            return True if self.tail == self.size - 1 else False
        else:
            return True if self.head - 1 == self.tail else False

    # Helper function to display the current queue
    def printElements(self) -> None:
        if self.head == -1 and self.tail == -1:
            return
        if self.head <= self.tail:
            for i in range(self.head, self.tail + 1):
                print(self.cQueue[i])
        else:
            for i in range(self.head, self.size):
                print(self.cQueue[i])
            for i in range(self.tail + 1):
                print(self.cQueue[i])
        

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
obj.enQueue(3)
obj.enQueue(2)
obj.enQueue(4)
obj.deQueue()
print(obj.Front())
print(obj.Rear())
print(obj.isEmpty())
obj.deQueue()
obj.deQueue()
print(obj.isEmpty())
param_6 = obj.isFull()

print()
obj.printElements()