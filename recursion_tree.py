class Node:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None


"""
                 	4
        /      						\
        2                            6
       /   \
       1    3						/	\
								5         7
"""
#build tree

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

path_inorder = []
def inorder(root):
	if not root:
		return

	inorder(root.left)
	#print(root.val)
	path_inorder.append(root.val)
	inorder(root.right)

inorder(root)
#print(path_inorder)
assert path_inorder == [1,2,3,4,5,6,7]


path_preorder = []
def dfs_preorder(node):
	if node is None:
		return 
	#print(node.val)
	path_preorder.append(node.val)

	dfs_preorder(node.left)	
	dfs_preorder(node.right)	

dfs_preorder(root)
assert path_preorder == [4,2,1,3,6,5,7]

def get_height(node, height):
	if not node:
		return height
	#print("node:" + str(node.val) + " height: " + str(height))

	left = get_height(node.left, height+1)
	#print(f"node: {node.val}, left height: {left}")  # Include node information for clarity
	right = get_height(node.right, height + 1)
	return max(left, right)

height = get_height(root, 0)
assert height == 3

def get_max(node):
	if not node:
		return float('-inf')
	#stop recursion
	#else:
	left = get_max(node.left)
	right = get_max(node.right)
	return max(node.val, left, right)

def get_min(node):
	if not node:
		return float('inf')
	#stop recursion
	else:
		left = get_min(node.left)
		right = get_min(node.right)
		return min(node.val, left, right)

min_val = get_min(root)
assert min_val == 1

def find_path(node, target, path):
	if not node:
		return []

	path.append(node.val)
	if node.val == target:
		return path

	#path.copy() ensures that each recursive call works with a separate list. 
	left_path = find_path(node.left, target, path.copy())
	right_path = find_path(node.right, target, path.copy())

	if left_path:
		return left_path
	elif right_path:
		return right_path
	else:
		return None


target = 7
path_3 = find_path(root, target, [])
target = 1
path_1 = find_path(root, target, [])
#print(f"path_3: {path_3}")
#print(f"path_1: {path_1}")

assert path_3 == [4, 6, 7]

def get_lca(path1, path2):
	lca = -1
	i, j = 0, 0
	while i < len(path1) or j < len(path2):
		if path1[i] == path2[j]:
			lca = path1[i]	
		i+=1
		j+=1
	return lca

lca = get_lca(path_3, path_1)	
assert lca == 4

def find_lca(node, a , b):
	if not node:
		return None
	if node.val == a or node.val == b:
		return node

	left = find_lca(node.left, a, b)
	right = find_lca(node.right, a, b)

	if left and right:
		return node

	if not left:
		return right
	elif not right:
		return left
	else:
		return None

assert find_lca(root, 7, 1).val == 4
print("All assertions passed")


