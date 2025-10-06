from collections import defaultdict

#Hi
#LRU

#Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#The functions get and put must each run in O(1) average time complexity.

# Input
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]#
#
#

"""
1
h
t

2->1
 <-
   h
t
   
 3-> 2->1
  <-  <-
"""

class Node:
    def __init__(self, val):
        self.val = val  # An instance attribute
        self.next = None    # Another instance attribute
        self.prev = None    # Another instance attribute

    def __str__(self):
        return f"val: {self.val}"

    def __repr__(self):
        # dict printing uses __repr__, not __str__
        return f"Node(val={self.val})"

class DoubleLinkedList:
    def __init__(self):
        self.head = None  # The head of the list is initially None (empty list)
        self.tail = None  # The tail of the list is initially None
        self.length = 0   # Keeps track of the number of nodes i
    
    def add(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length+=1

    def delete(self, node):
        curr = node
        if curr == self.head:
            self.head = curr.next
            curr.next=None
        elif curr == self.tail:
            self.tail = curr.prev
            self.tail = None
        else:
            curr.prev.next = curr.next

    def print(self):
        curr = self.head
        while(curr):
            print(f"val: {curr.val}")
            curr = curr.next 
                    
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.doubleLinkedList = DoubleLinkedList()
        self.dictNode = defaultdict(Node)

    def print(self):
        print("Printing double linked list: ")
        self.doubleLinkedList.print()
        print(f"Printing dictNode: {self.dictNode}")

    def put(self, key, value):
        if self.doubleLinkedList.length < self.capacity:
            curr = Node(value)
            self.doubleLinkedList.add(curr)
            self.dictNode[key] = curr
        else:
            #remove LRU REVIEW THIS
            curr = self.dictNode[key]
            self.doubleLinkedList.delete(curr)
            del self.dictNode[key] 
            
            curr = Node(value)
            self.doubleLinkedList.add(curr)
            self.dictNode[key] = curr


lru = LRUCache(2)
lru.put(1,1)
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
lru.print()

"""
{} ->[] 

1->2->3
SingleList
list(3)
Key, value
1-2-3
LRU


map<key, Node>

#Sorry my internet went down

other data structure 

int size = 2

put (1,1)

2->....1->null
h      t
     <-

2->nill
h
t

remove from dict
map(1, Node1)
map(2, Node2)

map.size == capacity

get(1) go to dict and get Node.val

1->2-
h. t
put(3,3)

"""