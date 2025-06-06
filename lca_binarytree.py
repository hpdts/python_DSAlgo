class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)


root.left = two
root.right = three

root.left.left = four
root.left.right = five

root.right.left = six
root.right.right = seven

def inorder(root):
	if not root:
		return
	inorder(root.left)
	print(root.value)
	inorder(root.right)

inorder(root)

def dfs_path(root, node, path):
	if not root:
		return False
	path.append(root.value)
	if root.value == node.value:
		return True

	if dfs_path(root.left, node, path):
		return True
	if dfs_path(root.right, node, path):
		return True
	path.pop()  # Backtrack if not found
	return False

	

path_n1 = []
dfs_path(root, four, path_n1)
assert path_n1 == [1, 2, 4]

path_n2 = []
dfs_path(root, five, path_n2)
#print(f"path_n2: {path_n2}")

assert path_n2 == [1, 2, 5]


"""
[1, 2, 4]
 i
[1, 2, 5]
 j
"""
def get_lca(path_n1, path_n2):
	i = 0
	j = 0
	while i < len(path_n1) or j < len(path_n2):
		if path_n1[i] != path_n2[j]:
			break
		i+=1
		j+=1

	return path_n1[i-1]

assert get_lca(path_n1, path_n2) == 2

def lca(root, n1, n2):
	if not root:
		return None
	if root.value == n1.value or root.value == n2.value:
		return root
	left_search = lca(root.left, n1, n2)
	right_search = lca(root.right, n1, n2)

	if left_search and right_search:
		return root

	return left_search if left_search else right_search


#print(lca(root, four, five))
assert lca(root, four, five).value == 2


