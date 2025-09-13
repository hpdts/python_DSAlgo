"""
You are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is "sub-Sudoku", a game where the player has to position the numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix, returns true if  every row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters, so the matrix can contain any signed integer.

grid1 = [[2, 3, 1],
         [1, 2, 3],
         [3, 1, 2]]            -> True  (A grid of size 3: every row and column contains the numbers 1,2,3) 

grid2 = [[1, 2, 3],
         [3, 2, 1],
         [3, 1, 2]]            -> False (The first column is missing the value 2. It should contain the numbers 1,2 and 3. 
                                         Similarly, the second column is missing the value 3.)                                         

grid3 = [[2, 2, 3],
         [3, 1, 2],
         [2, 3, 1]]            -> False (The first row is missing the value 1. Same for the first column.)

grid4 = [[1]]                  -> True  (a grid of size one: it contains 1 as the single value) 

grid5 = [[-1, -2, -3],
         [-2, -3, -1],
         [-3, -1, -2]]         -> False (The rows and columns need to contain the values 1,2,3 and not -1, -2, and -3) 

grid6 = [[1, 3, 3],
         [3, 1, 2],
         [2, 3, 1]]            -> False

grid7 = [[1, 2, 3, 4],
         [4, 3, 2, 1],
         [1, 3, 2, 4],
         [4, 2, 3, 1]]         -> False

grid8 = [[0, 3],
         [3, 0]]               -> False (for a grid of size two, all the rows and columns should contain 1 and 2, not 0 and 3 )

grid9 = [[0, 1],
         [1, 0]]               -> False (same as above all rows and columns should contain 1 and 2, not 0 and 1 )

grid10 = [[1, 1, 6],
          [1, 6, 1],
          [6, 1, 1]]           -> False

grid11 = [[1, 2, 3, 4],
          [2, 3, 1, 4],
          [3, 1, 2, 4],
          [4, 2, 3, 1]]        -> False

grid12 = [[-1, -2, 12, 1],
          [12, -1, 1, -2],
          [-2, 1, -1, 12],
          [1, 12, -2, -1]]     -> False   (all the rows and columns should contain the values 1,2,3,4) 
                                          (the input could contain positive and negative numbers)

grid13 = [[2, 3, 3],
          [1, 2, 1],
          [3, 1, 2]]           -> False

grid14 = [[1, 3],              -> False
          [3, 1]]

grid15 = [[2, 3],              -> False
          [3, 2]]

grid16 = [[1, 2],              -> False
          [2, 2]]

grid17 = [[2, 3, 1],           -> False
          [1, 2, 3],
          [2, 3, 1]];


grid 18 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  -> True
          [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
          [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
          [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
          [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
          [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
          [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
          [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
          [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
          [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]];

validateSudoku(grid1)  => True
validateSudoku(grid2)  => False
validateSudoku(grid3)  => False
validateSudoku(grid4)  => True
validateSudoku(grid5)  => False
validateSudoku(grid6)  => False
validateSudoku(grid7)  => False
validateSudoku(grid8)  => False
validateSudoku(grid9)  => False
validateSudoku(grid10) => False
validateSudoku(grid11) => False
validateSudoku(grid12) => False
validateSudoku(grid13) => False
validateSudoku(grid14) => False
validateSudoku(grid15) => False
validateSudoku(grid16) => False
validateSudoku(grid17) => False
validateSudoku(grid18) => True
  
Complexity analysis variables:  
  
N = The number of rows/columns in the matrix
           c
grid7 = [r[1, 2, 3, 4],
         [4, 3, 2, 1],
         [1, 3, 2, 4],
         [4, 2, 3, 1]]
    set = 1..4  
         if set is empty the row is good 
         
"""

grid1 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2],
]
grid2 = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2],
]
grid3 = [
    [2, 2, 3],
    [3, 1, 2],
    [2, 3, 1],
]
grid4 = [
    [1],
]
grid5 = [
    [-1, -2, -3],
    [-2, -3, -1],
    [-3, -1, -2],
]
grid6 = [
    [1, 3, 3],
    [3, 1, 2],
    [2, 3, 1],
]
grid7 = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 3, 2, 4],
    [4, 2, 3, 1],
]
grid8 = [
    [0, 3],
    [3, 0],
]
grid9 = [
    [0, 1],
    [1, 0],
]
grid10 = [
    [1, 1, 6],
    [1, 6, 1],
    [6, 1, 1],
]
grid11 = [
    [1, 2, 3, 4],
    [2, 3, 1, 4],
    [3, 1, 2, 4],
    [4, 2, 3, 1],
]
grid12 = [
    [-1, -2, 12, 1],
    [12, -1, 1, -2],
    [-2, 1, -1, 12],
    [1, 12, -2, -1],
]
grid13 = [
    [2, 3, 3],
    [1, 2, 1],
    [3, 1, 2],
]
grid14 = [
    [1, 3],
    [3, 1],
]
grid15 = [
    [2, 3],
    [3, 2],
]
grid16 = [
    [1, 2],
    [2, 2],
]
grid17 = [
  [2, 3, 1],
  [1, 2, 3],
  [2, 3, 1],
]
grid18 = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
  [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
  [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
  [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
  [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
  [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
  [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
  [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]


"""
grid1 = [[2, 3, 1],
         [1, 2, 3],
         [3, 1, 2]]            -> True  (A grid of size 3: every row and column contains the numbers 1,2,3) 

grid9 = [
    [0, 1],
    [1, 0],
]

"""

def validateSudoku(grid):
    size = len(grid)
    
    rows = len(grid)
    cols = len(grid[0])
    
    #each row
    for row in range(rows):
        seen_numbers = set(list(range(1, size+1)))
        #print(seen_numbers)
        for col in range(cols):
            num = grid[row][col]
            #print(f"row:{row}, col: {col} num: {num}")
            if num in seen_numbers:
                seen_numbers.remove(num)
                
        if seen_numbers:
            return False
    ##print("cols")
    #each col
    for col in range(cols):
        seen_numbers = set(list(range(1, size+1)))
        for row in range(rows):
            num = grid[row][col]
            #print(f"row:{row}, col: {col} num: {num}")
            
            if num in seen_numbers:
                seen_numbers.remove(num)
                
        if seen_numbers:
            return False
    return True

assert validateSudoku(grid1)  == True
assert validateSudoku(grid2)  == False
assert validateSudoku(grid3)  == False
assert validateSudoku(grid4)  == True
assert validateSudoku(grid5)  == False
assert validateSudoku(grid6)  == False
assert validateSudoku(grid7)  == False
assert validateSudoku(grid8)  == False
assert validateSudoku(grid9)  == False
assert validateSudoku(grid10) == False
assert validateSudoku(grid11) == False
assert validateSudoku(grid12) == False
assert validateSudoku(grid13) == False
assert validateSudoku(grid14) == False
assert validateSudoku(grid15) == False
assert validateSudoku(grid16) == False
assert validateSudoku(grid17) == False
assert validateSudoku(grid18) == True

print("All test cases pass")

    
    
    
