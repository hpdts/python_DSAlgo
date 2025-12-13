"""
Knight Jump
You are given a two dimensional chess board of size N×N (1-based indexing). 
Some of the cells on this board are ‘.’ denoting an empty cell. 
Some of the cells on this board are ‘#’ denoting a blocked cell, 
which you are not allowed to visit. 


Exactly one of the cells on this board is ‘K’ denoting the initial position of the knight.

A knight at position (r,c) can move to any of the valid positions 
in set S = {(r+2,c+1), (r+2,c−1), (r−2,c+1), (r−2,c−1), (r+1,c+2), (r+1,c−2), (r−1,c+2), (r−1,c−2)}. 


Here valid position means that the resulting (r′,c′) 
should be within the bounds of the chess grid, i.e. 1≤r′≤N and 1≤c′≤N.

The question is you have to determine the minimum number of steps 
required for the Knight to reach cell (1,1) avoiding cells with ‘#’ in the path.

Note - There will be exactly one ‘K’ in the grid and cell (1,1) will NOT be a ‘#’.



Input
The first line contains an integer N (1≤N≤10^2) denoting the dimension of the chess board. 
Each of the next N lines contains a string denoting the itℎ row. The length of these strings will be N.
Output
Print the value of minimum number of steps. However, if (1,1) is not reachable, print the number -1.
 
Sample input 1:
4


k2...
..K1.
....
...K


Sample output 1: 2


Sample input 2:
3

..K
k1..
###

DFS
visited
backtracking

shortest path

dfs(visited, row, col)

     if row , col == 0,0
      //check the boundaries
S = {dfs(r+2,c+1), (r+2,c−1), (r−2,c+1), (r−2,c−1), (r+1,c+2), (r+1,c−2), (r−1,c+2), (r−1,c−2)}



Sample output 2: -1

BFS by level

....
....
....
...K

r,c
level =0
visited = set()


while q:




if r,c == 0,0
 return level

S = {(r+2,c+1), (r+2,c−1), (r−2,c+1), (r−2,c−1), (r+1,c+2), (r+1,c−2), (r−1,c+2), (r−1,c−2)}

rownew, colnew = r + r+2, c + c+1

if 1≤r′≤N and 1≤c′≤N and not in visted and grid[rownew][colnew] != '#'

q.push(rownew, colnew)
visited.add((r,c))



level++

return -1

//BFS with state visited new set and level keep going but save all that

"""

from collections import deque

def knight_min_steps(grid):
    N = len(grid)

    # Find the knight
    start_r = start_c = -1
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 'K':
                start_r, start_c = r, c

    # BFS queue
    q = deque()
    q.append((start_r, start_c, 0))
    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True

    # Knight moves
    moves = [
        (2,1), (2,-1), (-2,1), (-2,-1),
        (1,2), (1,-2), (-1,2), (-1,-2)
    ]

    target = (0, 0)  # 1-based (1,1) → 0-based (0,0)

    while q:
        r, c, dist = q.popleft()

        # Reached target
        if (r, c) == target:
            return dist

        # Explore knight moves
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))

    return -1

grid = [
"....",
"..K.",
"....",
"...."
]

print(knight_min_steps(grid))



