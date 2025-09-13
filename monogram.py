"""
A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and an instruction for each row and each column. The player has to color each row and column using the corresponding instruction. Each cell can be either black or white, which we will represent as 'B' for black and 'W' for white.

+------------+
| W  W  W  W |
| B  W  W  W |
| B  W  B  B |
| W  W  B  W |
| B  B  W  W |
+------------+

For each row and column, the corresponding instruction gives the lengths of contiguous runs of black ('B') cells. 
For example, the instruction [ 2, 1 ] for a specific row indicates that there must be a run of two black cells, 
followed later by another run of one black cell, and the rest of the row is filled with white cells.

These are valid solutions: [ W, B, B, W, B ] and [ B, B, W, W, B ] and also [ B, B, W, B, W ]
This is not valid: [ W, B, W, B, B ] since the runs are not in the correct order.
This is not valid: [ W, B, B, B, W ] since the two runs of Bs are not separated by Ws.

Your job is to write a function to validate a possible solution against a set of instructions. Given a 2D matrix representing a player's solution; and instructions for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

Example solution matrix:

validateNonogram(matrix1, rows1_1, columns1_1) => True

matrix1 ->
                                 rows1_1
                +------------+     
                | W  W  W  W | <-- []
                | B  W  W  W | <-- [1]
                | B  W  B  B | <-- [1,2]
                | W  W  B  W | <-- [1]
                | B  B  W  W | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
               [2,1] | [2] |
  columns1_1        [1]   [1]
       

Example instructions #2

(same matrix as above)
rows1_2    =  [], [], [1], [1], [1,1]
columns1_2 =  [2], [1], [2], [1]
validateNonogram(matrix1, rows1_2, columns1_2) => False

The second, third and last rows and the first column do not match their respective instructions.

All Test Cases:
validateNonogram(matrix1, rows1_1, columns1_1) => True
validateNonogram(matrix1, rows1_2, columns1_2) => False
validateNonogram(matrix1, rows1_3, columns1_3) => False
validateNonogram(matrix1, rows1_4, columns1_4) => False
validateNonogram(matrix1, rows1_5, columns1_5) => False
validateNonogram(matrix1, rows1_6, columns1_6) => False
validateNonogram(matrix1, rows1_7, columns1_7) => False
validateNonogram(matrix1, rows1_8, columns1_8) => False
validateNonogram(matrix2, rows2_1, columns2_1) => False
validateNonogram(matrix2, rows2_2, columns2_2) => False
validateNonogram(matrix2, rows2_3, columns2_3) => False
validateNonogram(matrix2, rows2_4, columns2_4) => False
validateNonogram(matrix2, rows2_5, columns2_5) => True
validateNonogram(matrix2, rows2_6, columns2_6) => False
validateNonogram(matrix3, rows3_1, columns3_1) => True
validateNonogram(matrix3, rows3_2, columns3_2) => False

n: number of rows in the matrix
m: number of columns in the matrix
"""

matrix1 = [
	['W','W','W','W'],
	['B','W','W','W'],
	['B','W','B','B'],
	['W','W','B','W'],
	['B','B','W','W']
]
rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]

rows1_2 = [[],[],[1],[1],[1,1]]
columns1_2 = [[2],[1],[2],[1]]

rows1_3 = [[],[1],[3],[1],[2]]
columns1_3 = [[3],[1],[2],[1]]

rows1_4 = [[],[1,1],[1,2],[1],[2]]
columns1_4 = [[2,1],[1],[2],[1]]

rows1_5 = [[],[1],[1],[1],[2]]
columns1_5 = [[2,1],[1],[2],[1]]

rows1_6 = [[],[1],[2,1],[1],[2]]
columns1_6 = [[2,1],[1],[2],[1]]

rows1_7 = [[],[1],[1,2],[1],[2,1]]
columns1_7 = [[2,1],[1],[2],[1]]

rows1_8 = [[1],[1],[1,2],[1],[2]]
columns1_8 = [[2,1],[1],[2],[1]]

matrix2 = [
	['W','W'],
	['B','B'],
	['B','B'],
	['W','B']
]

rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]

rows2_2 = [[],[2],[2],[1]]
columns2_2 = [[3],[3]]

rows2_3 = [[],[],[],[]]
columns2_3 = [[],[]]

rows2_4= [[],[2],[2],[1]]
columns2_4 = [[2,1],[3]]

rows2_5= [[],[2],[2],[1]]
columns2_5 = [[2],[3]]

rows2_6= [[],[2],[2],[1]]
columns2_6 = [[2],[1,1]]

matrix3 = [
  ['B', 'W', 'B', 'B', 'W', 'B']
]
rows3_1 = [[1, 2, 1]]
columns3_1 = [[1], [], [1], [1], [], [1]]

rows3_2 = [[1, 2, 2]]
columns3_2 = [[1], [], [1], [1], [], [1]]

"""
matrix1 = [
	['W','W','W','W'],
	['B','W','W','W'],
	['B','W','B','B'],
	['W','W','B','W'],
	['B','B','W','W']
]


matrix3 = [
    0.   1.  2.    3.  4.   5
  ['B', 'W', 'B', 'B', 'W', 'B']
              ^
]
"""


def validateMonogram(matrix, rows_check, columns_check):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows):
        col = 0
        contiguous_runs_black = []
        while col < cols:
            #print(f"row:{row}, col: {col}") 
            letter = matrix[row][col]
            cont = 0
            if letter == 'B':
                #print(f"row:{row}, col: {col} letter: {letter}") 
                while col < cols and matrix[row][col] == 'B' :
                    cont+=1
                    col+=1
                contiguous_runs_black.append(cont)
            else:
                col+=1
            #print(f"row:{row}, col: {col} letter: {letter}, cont: {cont}")
        if contiguous_runs_black != rows_check[row]:
            return False
    
    #cols
    #print("----columns----")
    for col in range(cols):
        row = 0
        contiguous_runs_black = []
        while row < rows:
            letter = matrix[row][col]
            cont = 0
            if letter == 'B':
                while row < rows and matrix[row][col] == 'B' :
                    cont+=1
                    row+=1
                contiguous_runs_black.append(cont)
            else:
                row+=1

            #print(f"row:{row}, col: {col} letter: {letter}, cont: {cont}")
        if contiguous_runs_black != columns_check[col]:
            return False

    return True
            


assert validateMonogram(matrix1, rows1_1, columns1_1) == True
assert validateMonogram(matrix1, rows1_2, columns1_2) == False
assert validateMonogram(matrix1, rows1_3, columns1_3) == False
assert validateMonogram(matrix1, rows1_4, columns1_4) == False
assert validateMonogram(matrix1, rows1_5, columns1_5) == False
assert validateMonogram(matrix1, rows1_6, columns1_6) == False
assert validateMonogram(matrix1, rows1_7, columns1_7) == False
assert validateMonogram(matrix1, rows1_8, columns1_8) == False
assert validateMonogram(matrix2, rows2_1, columns2_1) == False
assert validateMonogram(matrix2, rows2_2, columns2_2) == False
assert validateMonogram(matrix2, rows2_3, columns2_3) == False
assert validateMonogram(matrix2, rows2_4, columns2_4) == False
assert validateMonogram(matrix2, rows2_5, columns2_5) == True
assert validateMonogram(matrix2, rows2_6, columns2_6) == False
assert validateMonogram(matrix3, rows3_1, columns3_1) == True
assert validateMonogram(matrix3, rows3_2, columns3_2) == False
assert validateMonogram(matrix3, rows3_1, columns3_1) == True

print("All test cases pass")
    
    
