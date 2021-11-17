import sys

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail.next.prev= self.tail
            self.tail = self.tail.next
        self.count += 1

    def pop(self):
        if self.head == None:
            print(-1)
        else:
            popped = self.head.val
            print(popped)
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -= 1
            
    def size(self):
        print(self.count)

    def empty(self):
        if self.count == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head == None:
            print(-1)
        else:
            print(self.head.val)

    def back(self):
        if self.head == None:
            print(-1)
        else:
            print(self.tail.val)

q = Queue()
for _ in range(int(sys.stdin.readline())):
    commandLine = list(sys.stdin.readline().split())
    command = commandLine[0]
    if command == 'push':
        q.push(int(commandLine[1]))
    elif command == 'pop':
        q.pop()
    elif command == 'size':
        q.size()
    elif command == 'empty':
        q.empty()
    elif command == 'front':
        q.front()
    else:
        q.back()
