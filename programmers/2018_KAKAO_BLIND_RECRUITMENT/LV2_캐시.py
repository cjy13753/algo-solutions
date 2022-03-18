class DLLNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class Cache:
    def __init__(self, capa):
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.cnt = 0
        self.capa = capa
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key):
        node = None
        if key in self.map:
            node = self.map[key]
            self.deleteNode(node)
            self.addToHead(node)
        return node

    def set(self, key):
        node = DLLNode(key)
        if self.cnt < self.capa:
            self.map[key] = node
            self.addToHead(node)
            self.cnt += 1
        else:
            del self.map[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
            self.map[key] = node
            self.addToHead(node)

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    
    cache = Cache(cacheSize)

    for city in cities:
        city = city.upper()
        if cache.get(city):
            answer += 1
        else:
            cache.set(city)
            answer += 5
    
    return answer