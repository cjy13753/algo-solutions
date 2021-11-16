import sys

class HeapTree:
    def __init__(self) -> None:
        self.heap = [0] * 100_000
        self.tail = -1

    def insert(self, val):
        self.tail += 1
        self.heap[self.tail] = val
        childIdx = self.tail
        parentIdx = (childIdx - 1) // 2

        while parentIdx >= 0 and self.heap[childIdx] > self.heap[parentIdx]:
            self.heap[parentIdx], self.heap[childIdx] = self.heap[childIdx], self.heap[parentIdx]
            childIdx = parentIdx
            parentIdx = (childIdx - 1) // 2

    def popBig(self):
        if self.tail > -1:
            print(self.heap[0])
            self.heap[0], self.heap[self.tail] = self.heap[self.tail], self.heap[0]
            self.tail -= 1
            
            start = 0
            while start <= self.tail:
                biggest = start
                leftChild = biggest * 2 + 1
                rightChild = biggest * 2 + 2
                if leftChild <= self.tail and self.heap[leftChild] > self.heap[biggest]:
                    biggest = leftChild
                
                if rightChild <= self.tail and self.heap[rightChild] > self.heap[biggest]:
                    biggest = rightChild
                
                if biggest != start:
                    self.heap[biggest], self.heap[start] = self.heap[start], self.heap[biggest]
                    start = biggest
                else:
                    break
        else:
            print(0)

heaptree = HeapTree()

    
vals = []
for _ in range(int(sys.stdin.readline())):
    vals.append(int(sys.stdin.readline()))
for val in vals:
    if val == 0:
        heaptree.popBig()
    else:
        heaptree.insert(val)

# while True:
#     val = int(sys.stdin.readline())
#     if val == 0:
#         heaptree.popBig()
#     else:
#         heaptree.insert(val)
