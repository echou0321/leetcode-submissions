class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.front = Node(0, 0)
        self.back = Node(0, 0)
        self.front.next = self.back
        self.back.prev = self.front

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.back.prev
            self.remove(lru)
            del self.cache[lru.key]

    
    def insert(self, node):
        temp = self.front.next
        self.front.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.front

    def remove(self, node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev









        
