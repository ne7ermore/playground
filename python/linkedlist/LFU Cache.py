"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:
    def __init__(self, v, k):
        self.v = v
        self.k = k
        self.c = 1
        self.prev = None
        self.next = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def hasNotNode(self):
        return (self.head.next == self.tail and self.tail.prev == self.head)

    def delLastOne(self):
        if not self.hasNotNode():
            self.tail.prev.delete()


class LFUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.cl = {}
        self.capacity = capacity
        self.invalid = capacity == 0

    def get(self, key: int) -> int:
        if self.invalid or key not in self.kv:
            return -1

        node = self.kv[key]
        node.delete()
        self.checkLc(node.c)
        node.c += 1
        self.updateLc(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if self.invalid:
            return

        if key in self.kv:
            node = self.kv[key]
            node.v = value
            node.delete()
            self.checkLc(node.c)
            node.c += 1
        else:
            node = Node(value, key)
            self.kv[key] = node
            if self.capacity < 1:
                idx = min(self.cl.keys())
                self.kv.pop(self.cl[idx].tail.prev.k)
                self.cl[idx].delLastOne()
                self.checkLc(idx)
            else:
                self.capacity -= 1

        self.updateLc(node)

    def updateLc(self, node):
        if node.c in self.cl:
            self.cl[node.c].insert(node)
        else:
            ll = LinkedList()
            ll.insert(node)
            self.cl[node.c] = ll

    def checkLc(self, k):
        if k in self.cl and self.cl[k].hasNotNode():
            self.cl.pop(k)
