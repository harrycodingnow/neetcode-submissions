class ListNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
                
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev        


    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:            
            self.remove(self.dic[key])
        self.dic[key] = ListNode(key, value)
        self.insert(self.dic[key])

        if len(self.dic) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]

        

        
