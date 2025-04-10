from collections import deque, defaultdict
"""
--->      1
         / \\
--->    2   3   <---
       / \\ /
--->   6 5 4    <---

Answer: [6, 2, 1, 3, 4]
"""

class Node:
       def __init__(self, val):
              self.val = val
              self.left = None
              self.right = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

root = one
root.left = two
root.left.left = six
root.left.right = five 
root.right = three
root.right.left = four

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

#Map by level pointers tio get each side
def right_left_view(root):
    if not root:
        return []

    q = deque([(root, 0)])
    nodes_levels = defaultdict(list)
    max_level = 0
    while q:
            curr, level = q.popleft()
            nodes_levels[level].append(curr.val)
            max_level = max(max_level, level)
            if curr.left:
                    q.append((curr.left, level +1))  
            if curr.right:
                    q.append((curr.right, level +1))
    #print(f"mapLevel: {nodes_levels}")
    #[6, 2, 1, 3, 4]
    #mapLevel: defaultdict(<class 'list'>, {0: [1], 1: [2, 3], 2: [6, 5, 4]})
    # Extract the rightmost nodes from each level
    leftmost = []
    for level in range(max_level, -1, -1):
       #print(f"level: {level}")
       leftmost.append(nodes_levels[level][0])

    rightmost = []
    for level in range(1, max_level+1):
       #print(f"level: {level}, nodes_levels[level]: {nodes_levels[level]}")
       size = len(nodes_levels[level])
       rightmost.append(nodes_levels[level][size-1])

    #print(leftmost)
    #print(rightmost)

    return leftmost + rightmost
#inorder(root)
assert right_left_view(root) == [6, 2, 1, 3, 4]




"""
--->      1
         / \\
--->    2   3   <---
        \\
--->      5     <---

ans: [5, 2,1,3, 5]
"""

root2 = Node(1)
root2.left = Node(2)
root2.left.right = Node(5)
root2.right = Node(3)
#print("Example 2 heerere")
#print(right_left_view(root2))
#inorder(root2)
assert right_left_view(root2) == [5,2,1,3,5]

#inorder(root)

"""
--->      1
         /   \\
--->    2     3   <---
       / \\  /    
--->  4   5  6      <---

ans: [4, 2,1,3, 6]
"""
root3 = Node(1)
root3.left = Node(2)
root3.right = Node(3)
root3.left.left = Node(4)
root3.left.right = Node(5)
root3.right.left = Node(6)
#print(right_left_view(root3))
assert right_left_view(root3) == [4,2,1,3,6]
print("all assertions passed")


"""

Given two input strings representing arbitrary large (positive) integers, 
how to compute the result of their addition?

    Example:
            "12345678987654321" + "123456789123456789" = "135802468111111110"

            "12345678987654321"  [0,0,1,3,4,5]
            "123456789123456789"  [0,2,1,3,4,5]
"""

