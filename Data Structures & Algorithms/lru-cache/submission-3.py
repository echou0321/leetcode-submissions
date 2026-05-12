class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.front = Node(0, 0)
        self.back = Node(0, 0)
        self.front.next = self.back
        self.back.prev = self.front

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        temp = Node(key, value)
        self.cache[key] = temp
        self.insert(temp)
        if len(self.cache) > self.capacity:
            lru = self.back.prev
            self.remove(lru)
            del self.cache[lru.key]
    
    def insert(self, node):
        temp = self.front.next
        self.front.next = node
        node.next = temp
        node.prev = self.front
        temp.prev = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev





