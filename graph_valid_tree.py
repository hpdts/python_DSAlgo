"""
Docstring for graph_valid_tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

0-1---4
\\
2 3
Output: True


Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

0-1-2-3
  |___
  |
  4

  cycle

Output:
false
"""

def validTree(n, edges):
	if len(edges) > (n - 1):
		return False
	#create graph
	graph = {}
	for i in range(n):
		graph[i] = []

    #undirected graph
	for edge_from,edge_to in edges:
		graph[edge_from].append(edge_to)
		graph[edge_to].append(edge_from)

	#print(f"graph: {graph}")
	visited = set()
	
	def dfs(node, ancestor):
		if node in visited:
			return False
		visited.add(node)
		for neighbor in graph[node]:
			if neighbor == ancestor:
				continue
			if not dfs(neighbor, node):
				return False
		return True
	return dfs(0, -1) and len(visited) == n


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
#print(validTree(n, edges))
assert validTree(n, edges) == True
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
assert validTree(n, edges) == False
print("All the assertions have passed")


