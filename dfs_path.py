class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_search(root, search):
    if root is None:
        return False
    if root.value == search:
        return True
    
    return dfs_search(root.left, search) or dfs_search(root.right, search)

def dfs_path(root, search, path):
    if root is None:
        return False
    path.append(root.value)
    if root.value == search:
        return True
    if dfs_path(root.left, search, path) or dfs_path(root.right, search, path):
        return True
    path.pop()
    return False

def bfs_search(root, search):
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.value == search:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return False

def bfs_path(root, search, path):
    print("BFS Path")
    queue = [root]
    parent_node_value = {root.value:None}
    while queue:
        curr = queue.pop(0)
        if curr.left:
            queue.append(curr.left)
            parent_node_value[curr.left.value] = curr.value
        if curr.right:
            queue.append(curr.right)
            parent_node_value[curr.right.value] = curr.value

    print(f"parent_node_value: {parent_node_value}")
    path.append(search)
    while search:
        search = parent_node_value[search]
        if search:
            path.append(search)
    path.reverse()
    return False

root = Node('A')
root.left = Node('B')
root.left.left = Node('D') 
root.right = Node('C')
root.right.left = Node('E')
root.right.right = Node('F')
root.right.left.right = Node('G')

path = []
print(dfs_search(root, 'G'))
print(dfs_search(root, 'B'))
print(dfs_search(root, 'A'))
print(dfs_search(root, 'R'))

path = []
print(dfs_path(root, 'G', path))
print(path)

print("BFS")
print(bfs_search(root, 'G'))
print(bfs_search(root, 'B'))
print(bfs_search(root, 'A'))
print(bfs_search(root, 'R'))
path = []
print(bfs_path(root, 'G', path))
print(path)


