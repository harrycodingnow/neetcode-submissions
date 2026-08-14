class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None
            
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])

        if len(self.dic) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]
        
