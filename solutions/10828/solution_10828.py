import sys

class Node:
        def __init__(self, x: int) -> None:
            self.value = x
            self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    
    def push(self, x: int) -> None:
        if self.head == None:
            self.head = Node(x)
        else:
            newNode = Node(x)
            newNode.next = self.head
            self.head = newNode
        self.length += 1
    
    def pop(self) -> None:
        if self.head == None:
            print(-1)
        else:
            print(self.head.value)
            self.head = self.head.next
            self.length -= 1
    
    def size(self) -> None:
        print(self.length)

    def empty(self) -> None:
        if self.length > 0:
            print(0)
        else:
            print(1)

    def top(self) -> None:
        if self.length == 0:
            print(-1)
        else:
            print(self.head.value)

stack = Stack()
n = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for _ in range(n)]
for command in commands:
    command_verb = command[0]
    if command_verb == "push":
        stack.push(int(command[1]))
    elif command_verb == "pop":
        stack.pop()
    elif command_verb == "size":
        stack.size()
    elif command_verb == "empty":
        stack.empty()
    elif command_verb == "top":
        stack.top()