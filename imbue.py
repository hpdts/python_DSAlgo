"""
String
. pass
* checkpoint
# obstacle
4-connected tree

k of checkpoints

field = [
   01234
 0"*#..#",
   ^
 1".#*#.",
     
 2"*...*"]
       ^ 
 
 K = 2 () pick 2 checkpoints freom begin to end

 shortest path from (0,0) to (1,2) is 5
she chooses (0,0) and (1,2), one of the optimal sequences is (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2).
find all *


get all combinations from k 





"""


from typing import List
from itertools import combinations
def expected_length(field: List[str], K: int) -> float:
    return 0.0



field = [
 "*#..#",
 ".#*#.",
 "*...*"]
K = 2

def find_checkpoints(field: List[str]) -> List[tuple]:
    checkpoints = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '*':
                checkpoints.append((i, j))
    return checkpoints

checkpoints = find_checkpoints(field)
assert checkpoints == [(0, 0), (1, 2), (2, 0), (2, 4)], f"Test failed: {checkpoints}"

def bfs(field: List[str], start: tuple, end: tuple)->int:
    queue = [(start[0], start[1], 0)]
    visited = set()
    visited.add((start[0], start[1]))
    while queue:
        curr_row, curr_col, curr_steps = queue.pop(0)
        if curr_row == end[0] and curr_col == end[1]:
            return curr_steps

        for offr,offc in [[1,0], [-1,0], [0,-1], [0,1]]:
            nr, nc = curr_row + offr, curr_col + offc

            if 0 <= nr < len(field) and 0 <= nc < len(field[0]) and (nr, nc) not in visited and field[nr][nc] in '.*':
                queue.append((nr,nc, curr_steps+1))
                visited.add((nr, nc))

    return -1

assert bfs(field, checkpoints[0], checkpoints[1]) == 5, f"Test 1 failed bfs"
assert bfs(field, checkpoints[0], checkpoints[2]) == 2, f"Test 2 failed bfs"
assert bfs(field, checkpoints[0], checkpoints[3]) == 6, f"Test 3 failed bfs"
assert bfs(field, checkpoints[1], checkpoints[2]) == 3, f"Test 4 failed bfs"
assert bfs(field, checkpoints[1], checkpoints[3]) == 3, f"Test 5 failed bfs"
assert bfs(field, checkpoints[2], checkpoints[3]) == 4, f"Test 6 failed bfs"

ret = []
"""
[(0, 0), (1, 2), (2, 0), (2, 4)]
   
               0,0
               /     
            0,0-1,2   
"""

pairs = list(combinations(checkpoints, K))
#print(pairs)

length = 0
for pair in pairs:
    length+=bfs(field, pair[0], pair[1])

assert length/len(pairs) == 3.8333333333333335, f"Test length"

def get_all_combinations(build, level):

    if len(build) == K:
        ret.append(build[:])
        return

    for checkpoint in range(level, len(checkpoints)):
        build.append(checkpoints[checkpoint])
        get_all_combinations(build, checkpoint+1)
        build.pop()

get_all_combinations([], 0)
#print(pairs)
#print(ret)
#assert ret == pairs, f"Test combinations"




field = [
 "*#..#",
 ".#*#.",
 "*...*"]
K = 4

#I need to pass for all the checkpoints
checkpoints = find_checkpoints(field)
pairs = list(combinations(checkpoints, K))
#print(pairs)













