"""
Runtime: O(n) 
Space:O(n)
"""
def is_balanced(input):
    stack = []
    closed_open = {')':'(','}':'{',']':'['}
    for c in input:
        if c in closed_open.values():
            stack.append(c)
        else:
            if not stack:
                return False
            open_c = stack.pop()
            if closed_open[c] != open_c:
                return False
    return True if not stack else False

assert is_balanced("(]") == False
assert is_balanced("()") == True
assert is_balanced("()[]{}") == True
assert is_balanced("([(){[]}]{})") == True
assert is_balanced("{[]}") == True
assert is_balanced("([)]") == False
assert is_balanced("") == True
print("All assertions are passing")

"""
streaming

"()"	true	The pair () is balanced.
"()[]{}"	true	All pairs are balanced.
"(]"	false	( is closed by ], which is incorrect.
"{[]}"	true	Nested brackets are correctly balanced.
"([)]"

"""
#3 mistakes
def is_balanced_mine(input):
	stack=[]
	close_open = {}
	close_open[')'] = '('
	close_open['}'] = '{'
	close_open[']'] = '['
	close_open['>'] = '<'
	#print(f"close_open: {close_open}")
	for i in input:
		#c = input[i]
		c = i
		#print(f"i: {i}, c: {c}")
		if c in "({[>":
			stack.append(c)
		elif c in ")}]<":
			if not stack:
				return False
			par = stack.pop()
			if not close_open[c] == par:
				return False
		#print(f"stack: {stack}")
	if stack:
		return False
	else:
		return True
	

def is_balanced(input):
	stack=[]
	close_open = {')':'(','}':'{',']':'[','>':'<'}
	for i in input:
		if i in close_open.values():
			stack.append(i)
		elif i in close_open:
			if not stack or close_open[i] != stack.pop():
				return False
	return False if stack else True 


assert is_balanced("some string") == True
assert is_balanced("[abc(def)gh{i}j]") == True
assert is_balanced("[abcdef") == False
assert is_balanced("abcd(egf))") == False
assert is_balanced(")abcd((egf)") == False
assert is_balanced("(abcd[)]egfh") == False
print("All assertions passed")

"""
ret = 2,1 2,2 2,3
n =8
  x
y 01234567
0 ........
1 ..X.....
2 ..X.....
3 ..X.....
4 ........
5 ........
6 ........
7 ........


"""
# Battleship
n = 8
grid = [['.' for _ in range(n)] for _ in range(n)]
"""
grid[2][1] = 'X'
grid[2][2] = 'X'
grid[2][3] = 'X'
"""
grid[1][2] = 'X'
grid[2][2] = 'X'
grid[3][2] = 'X'
#for row in grid:
#	print(''.join(row))
def bomb_location(grid, x, y):
	return True if grid[x][y] == 'X' else False

#duplicated coordinates on output 1 mistake
def find_battleship_mine(n):
	grid = [['.' for _ in range(n)] for _ in range(n)]
	"""
	grid[2][1] = 'X'
	grid[2][2] = 'X'
	grid[2][3] = 'X'
	"""
	grid[1][2] = 'X'
	grid[2][2] = 'X'
	grid[3][2] = 'X'
	for row in grid:
		print(''.join(row))

	ret = []
	for x in range(n):
		for y in range(n):
			if bomb_location(grid,x,y):
				ret.append((x,y))
				if x+1 < n and x+2 < n and bomb_location(grid,x+1,y) and bomb_location(grid,x+2,y):
					ret.append((x+1,y))
					ret.append((x+2,y))
				if y+1 < n and y+2 < n and bomb_location(grid,x,y+1) and bomb_location(grid,x,y+2):
					ret.append((x,y+1))
					ret.append((x,y+2))

	return ret

def find_battleship(grid, n):
	ret = []
	for x in range(n):
		for y in range(n):
			if bomb_location(grid,x,y):
				if x + 2 < n and all(bomb_location(grid, x + i, y) for i in range(3)):
					return [(x + i, y) for i in range(3)]
				if y + 2 < n and all(bomb_location(grid, x, y + i) for i in range(3)):
					return [(x, y + i) for i in range(3)]
				#ret.append((x,y))
				#if x+2 < n and bomb_location(grid,x+1,y) and bomb_location(grid,x+2,y):
				#	ret.append((x+1,y))
				#	ret.append((x+2,y))
				#	return ret
				#if  y+2 < n and bomb_location(grid,x,y+1) and bomb_location(grid,x,y+2):
				#	ret.append((x,y+1))
				#	ret.append((x,y+2))
				#	return ret
	
	return ret

print(find_battleship(grid, n))
assert find_battleship(grid, n) == [(1, 2), (2, 2), (3, 2)]

grid2 = [['.' for _ in range(n)] for _ in range(n)]
grid2[2][2] = 'X'
grid2[2][3] = 'X'
grid2[2][4] = 'X'
print(find_battleship(grid2, n))
for row in grid2:
	print(''.join(row))
assert find_battleship(grid2,n) == [(2, 2), (2, 3), (2, 4)]


print("all assertions passed")
