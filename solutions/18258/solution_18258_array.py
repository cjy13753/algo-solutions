import sys

class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.start = 0

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if self.start < len(self.queue):
            print(self.queue[self.start])
            self.start += 1
        else:
            print(-1)
            
    def size(self):
        print(len(self.queue) - self.start)

    def empty(self):
        print(0) if self.start < len(self.queue) else print(1)

    def front(self):
        print(self.queue[self.start]) if self.start < len(self.queue) else print(-1)

    def back(self):
        print(self.queue[-1]) if self.start < len(self.queue) else print(-1)

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
