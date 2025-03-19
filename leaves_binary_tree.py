from typing import List, Optional
from collections import defaultdict
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node5.left = node6

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def remove_leaf(parent: Node, child: Node):
    if parent is not None:
        if parent.left is not None and parent.left.val == child.val:
            parent.left = None
        if parent.right is not None and parent.right.val == child.val:
            parent.right = None


#inorder(root)
remove_leaf(node5, node6)
#print("after removal")
#inorder(root)

levels = defaultdict(list)
def dfs(node):
        if not node:
            return -1
        
        # Get the height of left and right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Current node's height is max(left, right) + 1
        height = max(left_height, right_height) + 1

        # Append the node value to its height group
        levels[height].append(node.val)

        return height     

dfs(root)
print("Height Dictionary:", dict(levels))
ret_list = [levels[i] for i in sorted(levels.keys())]
assert ret_list == [[4, 5, 3], [2], [1]], f"Test failed: {ret_list}"
print("Test passed")

#[[3,5,4], [2], [1]]
#get all leaves on ret
def leaves_binary_tree(root: Node) -> List[int]:
    ret = []
    queue = [(root, None)]
    while queue:
        curr_node, parent = queue.pop(0)

        if curr_node.left is None and curr_node.right is None:
            ret.append(curr_node.val)
            if parent:
                #print(f"parentval: {parent.val}")
                remove_leaf(parent, curr_node)

        if curr_node.left is not None: 
            queue.append((curr_node.left, curr_node))  
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_node))

    return ret; 

def remove_leaves_level_by_level(root: Optional[Node]) -> List[List[int]]:
    all_leaves = []
    while root:
        leaves = leaves_binary_tree(root)
        if not leaves:
            break
        all_leaves.append(leaves)
        # Update the root reference if the root itself was a leaf
        if root.left is None and root.right is None:
            all_leaves.append([root.val])
            root = None
    return all_leaves

all_leaves = remove_leaves_level_by_level(root)
print(all_leaves)
assert all_leaves == [[3, 4, 5], [2], [1]], f"Test failed: {all_leaves}"
print("Test passed")


#dfs_post_order(root)
#print(ret)
#assert ret == [[3, 4, 5], [2], [1]], f"Test failed: {ret}"
#print("Test passed")
"""
print("Initial tree (inorder traversal):")
inorder(root)
print("\n")



print("\nTree after removing all leaves (inorder traversal):")
inorder(root)
print()
"""
