#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'mergeStreams' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST streamA
#  2. INTEGER_SINGLY_LINKED_LIST streamB
#  3. INTEGER x
#  4. INTEGER y
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
"""
x,y = 1???
x=2
y=2
px
1->2->3
   py
5->4


out:
1->5->4

      px
1->5->4->3

find node to be replaced px ends one before ,careful with 1
px.next = streamB
move px to the end next = None
px.next = py.next
py = None

x=2
y=3

px
2->3->4->5.   A
       py
       
6->7->->8->9.   B

            px
1->6->7->8->9->5

x=1,y=1
1->2

3

1->3

x=1
y = 1
2

1-2-3-4

1-2


3-4-5

"""
def findNodesXY(head, x, y):
    px, py = None, None
    current = head
    position = 1

    while current:
        if position == x - 1:  # Node before position x
            px = current
        if position == y:  # Node at position y
            py = current
        if px and py:  # Stop early if both nodes are found
            break
        current = current.next
        position += 1

    return px, py

def findNodesXY2(head, x, y):
    px,py = head, head
    if x == 1 and y == 1:
        return px, py
    cont = 1
    if x != 1:
        x-=1
        while px and cont != x:
            px=px.next
            cont+=1
    cont = 1
    if y != 1:
        while py and cont != y:
            py=py.next
            cont+=1
    
    return px,py

def mergeStreams(streamA, streamB, x, y):
    if x == 1:  # Special case: Replace the head of streamA
        if y == 1 or y == 2:
            return streamB
        # Find the node at position y
        _, py = findNodesXY(streamA, x, y)
        tailB = streamB
        while tailB.next:  # Move to the end of streamB
            tailB = tailB.next
        tailB.next = py.next  # Connect the tail of streamB to the rest of streamA
        return streamB

    # General case: Replace nodes between x and y
    px, py = findNodesXY(streamA, x, y)
    px.next = streamB  # Connect px to the head of streamB
    tailB = streamB
    while tailB.next:  # Move to the end of streamB
        tailB = tailB.next
    tailB.next = py.next  # Connect the tail of streamB to the rest of streamA
    return streamA

def mergeStreams2(streamA, streamB, x, y):
    if x == 1 and (y == 1 or y==2):
        return streamB
    # Write your code here
    #print(f"x: {x}, y: {y}")
    px, py = findNodesXY(streamA, x, y)
    if x == 1:
        streamA = streamB
   # print(f"px: {px.data}, py: {py.data}")
    px.next = streamB
    #move px to the end next = None
    #print(f"tailB: {streamB.tail.data}")
    while px.next:
        px=px.next
    #print(f"px tail: {px.data}")
    px.next = py.next
    py = None
    return streamA

def test_mergeStreams():
    def create_linked_list(values):
        linked_list = SinglyLinkedList()
        for value in values:
            linked_list.insert_node(value)
        return linked_list

    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.data)
            head = head.next
        return result

    # Test Case 1: x = 1, y = 1
    streamA = create_linked_list([1, 2, 3])
    #print_singly_linked_list(streamA.head, " -> ", sys.stdout)
    streamB = create_linked_list([4, 5, 6])
    x, y = 1, 1
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [4, 5, 6], f"Test Case 1 Failed: {linked_list_to_list(result)}"

    # Test Case 2: x = 2, y = 2
    streamA = create_linked_list([1, 2, 3])
    streamB = create_linked_list([4, 5, 6])
    x, y = 2, 2
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [1, 4, 5, 6, 3], f"Test Case 2 Failed: {linked_list_to_list(result)}"

    # Test Case 3: x = 1, y = 2
    streamA = create_linked_list([1, 2, 3])
    streamB = create_linked_list([4, 5, 6])
    x, y = 1, 2
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [4, 5, 6], f"Test Case 3 Failed: {linked_list_to_list(result)}"

    # Test Case 4: x = 2, y = 3
    streamA = create_linked_list([1, 2, 3, 4, 5])
    streamB = create_linked_list([6, 7, 8, 9])
    x, y = 2, 3
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [1, 6, 7, 8, 9, 4, 5], f"Test Case 4 Failed: {linked_list_to_list(result)}"

    # Test Case 5: x = 1, y = 1 (streamA is empty)
    streamA = create_linked_list([])
    streamB = create_linked_list([4, 5, 6])
    x, y = 1, 1
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [4, 5, 6], f"Test Case 5 Failed: {linked_list_to_list(result)}"

    """
    # Test Case 6: x = 1, y = 2 (streamB is empty)
    streamA = create_linked_list([1, 2, 3])
    streamB = create_linked_list([])
    x, y = 1, 2
    result = mergeStreams(streamA.head, streamB.head, x, y)
    assert linked_list_to_list(result) == [1, 2, 3], f"Test Case 6 Failed: {linked_list_to_list(result)}"
    """
    print("All test cases passed!")

# Run the tests
test_mergeStreams()

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    streamA_count = int(input().strip())

    streamA = SinglyLinkedList()

    for _ in range(streamA_count):
        streamA_item = int(input().strip())
        streamA.insert_node(streamA_item)

    streamB_count = int(input().strip())

    streamB = SinglyLinkedList()

    for _ in range(streamB_count):
        streamB_item = int(input().strip())
        streamB.insert_node(streamB_item)

    x = int(input().strip())

    y = int(input().strip())

    result = mergeStreams(streamA.head, streamB.head, x, y)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
"""