"""
  012345678
[
0[...c.....]
1[.........]
2[.....o...]
3[.........]
]


  012345678
[
0[...c.....]
1[.........]
2[...2.....]
3[o........]
]

[
0[...c.....]
1[.........]
2[...2.o...]
3[.........]
]

"""
from typing import List
def ride(desert:List[List[str]], gas:int) -> bool:
	coord_car = []
	coord_oasis = []
	coord_gas_station = []
	#print(desert)
	for row in range(rows):
		for col in range(cols):
			if desert[row][col] == 'c':
				#coord_car.append((row, col))
				coord_car = [(row, col)]
			elif desert[row][col] == 'o':
				coord_oasis.append((row, col))
			#elif desert[row][col].isnumeric(): does not work isnumber()BS
			elif isinstance(desert[row][col], int):
			#elif int(desert[row][col]) > 0: you need try catch
				coord_gas_station.append((row, col))
				gas_extra = int(desert[row][col])
	#print(f"coord_car: {coord_car}, coord_oasis: {coord_oasis}, coord_gas_station: {coord_gas_station}")
	car_row, car_col = coord_car[0]
	oasis_row, oasis_col = coord_oasis[0]
	gas_row, gas_col  = coord_gas_station[0]

	diff_row, diff_col = abs(car_row - oasis_row), abs(car_col - oasis_col)
	diff_gas_row, diff_gas_col = abs(car_row - gas_row), abs(car_col - gas_col)
	diff_gas_oasis_row, diff_gas_oasis_col = abs(oasis_row - gas_row), abs(oasis_col - gas_col)
	gas_remaining = gas - (diff_gas_row + diff_gas_col)
	#distance from gas to oasis
	#print(f"diff_row: {diff_row}, diff_col: {diff_col}")
	#print(f"diff_gas_row: {diff_gas_row}, diff_gas_col: {diff_gas_col}, gas_extra: {gas_extra}, gas_remaining after gas station: {gas_remaining}")
	if gas >= (diff_row + diff_col):
		return True
	elif gas >= (diff_gas_row + diff_gas_col) and (gas_extra + gas_remaining) >= (diff_gas_oasis_row + diff_gas_oasis_col):
		return True
	else:
		return False


rows, cols = 4, 9

desert = [['.' for _ in range(cols)] for _ in range(rows)]
desert[0][3] = 'c'
desert[2][5] = 'o'
desert[2][3] = 2

assert ride(desert, 4) == True, "4 gas should get to the oasis"
assert ride(desert, 5) == True, "5 gas should get to the oasis"
assert ride(desert, -5) == False, "-5 gas should not get to the oasis"
assert ride(desert, 0) == False, "0 gas should not get to the oasis"
assert ride(desert, 2) == True, "2 gas should get to the oasis"
assert ride(desert, 3) == True, "3 gas should get to the oasis"


desert[2][5] = '.'
desert[3][0] = 'o'
assert ride(desert, 3) == False, "3 gas should get to the second oasis"
assert ride(desert, 4) == True, "4 gas should get to the second oasis"
assert ride(desert, 5) == True, "5 gas should get to the second oasis"
assert ride(desert, 6) == True, "6 gas should get to the second oasis"
assert ride(desert, 60) == True, "60 gas should get to the second oasis"


"""
  012345678
[
0[...c.....]
1[rrrrrrr..]
2[...2.o...]
3[.........]
]

"""
desert[2][5] = 'o'
desert[3][0] = '.'
desert[2][3] = '.'
desert[1][0] = 'r'
desert[1][1] = 'r'
desert[1][2] = 'r'
desert[1][3] = 'r'
desert[1][4] = 'r'
desert[1][5] = 'r'
desert[1][6] = 'r'
desert[2][3] = '.'

"""
  012345678
[
0[---c-----]
1[rrrrrrrr_]
2[...2.----]
3[......___]
]


[
  012345678
0[...c.....]
1[rrrrrrrr.]
2[...2.o...]
3[.........]
]
"""
def ridebfs(desert:List[List[str]], gas:int) -> bool:
	rows, cols = len(desert), len(desert[0])
	coord_car = []
	visited = set()
	queue = []
	for row in range(rows):
		for col in range(cols):
			if desert[row][col] == 'c':
				coord_car.append((row, col))
				queue.append((row, col, gas))
				visited.add((row, col))
				#coord_car[(row, col)]

	#queue = [coord_car[0][0], coord_car[0][1]]
	#print(f"coord_car: {coord_car}, queue: {queue}")
	while queue:
		curr_row, curr_col, curr_gas = queue.pop(0)
		#print(f"curr_row: {curr_row}, curr_col: {curr_col}, curr_gas: {curr_gas}")

		if desert[curr_row][curr_col] == 'o':
			return True

		if curr_gas == 0:
			continue

		for offset_r, offset_c in [[1,0], [-1,0], [0,-1], [0,1]]:
			new_r, new_c = curr_row + offset_r, curr_col + offset_c
			if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and desert[new_r][new_c] in ['.', 'o']:
				queue.append((new_r, new_c, curr_gas-1))
				visited.add((new_r, new_c))


	return False

#print(desert)

assert ridebfs(desert, 4) == False, "4 gas should not get to the oasis"
assert ridebfs(desert, 8) == True, "8 gas should get to the oasis"
desert[1][7] = 'r'
assert ridebfs(desert, 6) == False, "6 gas should not get to the oasis"
assert ridebfs(desert, 8) == False, "8 gas should get to the oasis"
assert ridebfs(desert, 9) == False, "9 gas should get to the oasis"
assert ridebfs(desert, 10) == True, "10 gas should get to the oasis"
assert ridebfs(desert, 12) == True, "12 gas should get to the oasis"



print("All assertions passing")





