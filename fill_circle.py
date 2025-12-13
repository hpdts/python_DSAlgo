"""
return a grid with a circle inside filled with True values
and the rest False values. 

[ 0 1 2 3 4 5
]
0 [false, false, false, false, false, false, false, false, false, false 
1 [false, false, false, true, false, false, false, false, false, false) 
2[false, false, true, true, true, false, false, false, false, false). 
3[false, true, true, true, true, true, false, false, false, false]. 
4[false, false, true, true, true, false, false, false, false, false], 
5[false, false, false, true, false, false, false, false, false, false] 
6[false, false, false, false, false, false, false, false, false, false] 
[false, false, false, false, false, false, false, false, false, false], 
[false, false, false, false, false, false, false, false, false, false). 
[false, false, false, false, false, false, false, false, false, false]
def fill_circle(grid, cx, cy, radius):

"""
import math
def print_grid(grid):
	for row in grid:
		print(" ". join(map(str, row)))

def distance(row, col, cx, cy):
	return math.sqrt((cx - row)**2 + (cy - col)**2)

def fill_circle_n2(rows, cols, cx, cy, radius):
	grid = [[False for _ in range(cols)] for _ in range(rows)]
	#print_grid(grid)

	for row in range(rows):
		for col in range(cols):
			#print(f"grid value: {grid[row][col]}, dist: {distance(row, col, cx, cy)}")
			if distance(row, col, cx, cy) <= radius:
				grid[row][col] = True
	return grid
print_grid(fill_circle_n2(3, 3, 1, 1, 1))
print_grid(fill_circle_n2(10, 10, 3, 3, 2))



