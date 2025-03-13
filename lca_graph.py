class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

root.neighbors = [node1, node2, node3]
node1.neighbors = [node4, node5]
node3.neighbors = [node6, node7, node8]
node7.neighbors = [node9]

def print_tree(node, level=0):
    if not node:
        return
    print(" " * (level * 2) + str(node.value))
    for neighbor in node.neighbors:
        print_tree(neighbor, level + 1)

# Print the tree
#print_tree(root)


def bfs_path(root, search)->list:
    queue = [root]
    parent_node_value = {root.value:None}
    visited = set([root.value])
    while queue:
        curr = queue.pop(0)
        if curr.value == search:
            break
        for neighbor in curr.neighbors:
            if neighbor.value not in visited:
                queue.append(neighbor)
                visited.add(neighbor.value)
                parent_node_value[neighbor.value] = curr.value
    print(f"parent_node_value: {parent_node_value}")    
    path = [search]
    while search:
        search = parent_node_value[search]
        path.append(search)
    path.reverse()
    return path

path = bfs_path(root, 9)
print(path)

def lca(root, node1, node2):
    path1 = bfs_path(root, node1)
    path2 = bfs_path(root, node2)
    print(f"path1: {path1}")
    print(f"path2: {path2}")
    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1
    return path1[i-1]

print(lca(root, 4, 9))