class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.right = ListNode(0, 0)
        self.left = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        
    def insert(self, node):
        nxt = self.right 
        prev = self.right.prev 
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt
    
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

        if len(self.dic) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]
            
            

        

        
