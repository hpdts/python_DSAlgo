"""
Knight Jump
You are given a two dimensional chess board of size N×N (1-based indexing). 
Some of the cells on this board are ‘.’ denoting an empty cell. Some of the cells on this board are ‘#’ denoting a blocked cell, which you are not allowed to visit. 
Exactly one of the cells on this board is ‘K’ denoting the initial position of the knight.
A knight at position (r,c) can move to any of the valid positions in 
set S = {(r+2,c+1), (r+2,c−1), (r−2,c+1), (r−2,c−1), (r+1,c+2), (r+1,c−2), (r−1,c+2), (r−1,c−2)}. 
Here valid position means that the resulting (r′,c′) should be within the bounds of the chess grid, i.e. 1≤r′≤N and 1≤c′≤N.
The question is you have to determine the minimum number of steps required for the Knight to reach cell (1,1) avoiding cells with ‘#’ in the path.
Note - There will be exactly one ‘K’ in the grid and cell (1,1) will NOT be a ‘#’.

Sample input 1:
4
....
....
.*..
...K

 0123
0....
1....
2....
3...K


....
....
.K..
....

8 branches



Sample output: 2


Sample input 2:
3
..K
...
###
Sample output 2: -1

for row 
 for col
S = {(r+2,c+1), (r+2,c−1), (r−2,c+1), (r−2,c−1), (r+1,c+2), (r+1,c−2), (r−1,c+2), (r−1,c−2)}.
[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
BFS optimal solution shorter paths
knight jump
"""
from collections import deque
def bfs(grid):
	rows = len(grid)
	cols = len(grid[0])
	visited = [[False] * cols for _ in range(rows)] 

	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == 'K':
				start = (row, col)
				break

	queue = deque([(start[0], start[1], 0)])
	visited[start[0]][start[1]] = True

	while queue:
		r, c, steps = queue.popleft()
		if (r,c) == (0,0):
			return steps
		for dr, dc in [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]:
			nr, nc = r+dr, c+dc
			if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != '#':
				visited[nr][nc] = True
				queue.append((nr, nc, steps+1))
	return -1 


"""
 0123 
0....
1....
2.*..
3...K

"""
n = 4
grid = [['.'] * n for _ in range(n)] 
grid[3][3] = 'K'

#print(f"grid: {grid}")
assert bfs(grid) == 2

"""
 012
0..K
1...
2###
"""
n=3
grid2 = [['.'] * n for _ in range(n)] 
grid2[0][2] = 'K'
grid2[2][0] = '#'
grid2[2][1] = '#'
grid2[2][2] = '#'

assert bfs(grid2) == -1
print("all assertions passed")




