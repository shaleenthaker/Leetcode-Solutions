"""Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity."""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.previous = self.head
        self.head.next = self.tail

    def _remove(self, node):
        node.previous.next = node.next 
        node.next.previous = node.previous
        
    def _add_front(self, node):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.values:
            self._remove(self.values[key])
            self._add_front(self.values[key])
            return self.values[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            self.values[key] = Node(key, value)
            self._add_front(self.values[key])
            if len(self.values) > self.capacity:
                self.values.pop(self.tail.previous.key)
                self._remove(self.tail.previous)
        else:
            self.values[key].val = value
            self._remove(self.values[key])
            self._add_front(self.values[key])
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)