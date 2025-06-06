"""
A satellite image of the Pacific Ocean consists of green and blue pixels, representing land and water. 
The Pacific ocean is large, and mostly blue; but contains islands, which are green. 
Islands themselves may contain blue pixels, which are lakes.
A frontend presents the image to a user, who can click on it. 
When the user clicks on a green pixel, 
a popup will appear that displays the number of lakes in that island. 
This UI code already exists: the problem of this question is to write the backend 
function that will return the value to display.
As an example, consider an image (20 pixels wide by 10 tall) 
that is mostly blue; but contains 3 green rectangles:
  
On the left of the image there is a horizontal line of three green pixels, 
                  x  y      x  y
from coordinates (2, 2) to (4, 2). This is an island with no lakes
In the middle is a 3x3 square of green pixels (coordinates (5, 4) to (7, 6)) 
where the center pixel (6, 5) is water. This is an island with 1 lake
On the right is a green rectangle (coordinates (11, 3) to (16, 5)) 
where three internal pixels are water: (12, 4), (14, 4), and (15, 4). 
This forms an island with two lakes.

Blue pixel = “.” | Green pixel = “x”

|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|x|x|x|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|x|x|x|x|x|x|.|.|.|
|.|.|.|.|.|x|x|x|.|.|.|x|.|x|.|.|x|.|.|.|
|.|.|.|.|.|x|.|x|.|.|.|x|x|x|x|x|x|.|.|.|
|.|.|.|.|.|x|x|x|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|



visited 5,6


count +1

count+1



1 visited

N-1


BFS

all land connected


if I see water
one more traversals DFS

visited 






diagonals also
all water pixels connected

when you find water DFS??? 


no diamon
go thorugh the land

|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|x|x|x|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|x|x|x|x|x|x|.|.|.|
|.|.|.|.|.|x|x|x|.|.|.|x|.|x|.|.|x|.|.|.|
|.|.|.|.|.|x|.|x|.|.|.|x|x|x|x|x|x|.|.|.|
|.|.|.|.|.|x|x|x|.|.|.|.|.|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|


image = [[.] for _ in 20]
|.|.|
|.|.|

[]



Assuming a function, count_lakes(image, coord) → integer:
CountLakes(image, (2,2)) → 0
CountLakes(image, (6,6)) → 1
CountLakes(image, (12,5)) → 2

Python:



def bfs_water(image, visited, new_row, new_col):
  queue = []
  queue.append((new_row,new_col))
  while queue:
    curr_row, curr_col = queue.pop()
      for off_row, off_col in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
        new_row, new_col = curr_row + off_row, curr_col + off_col
        if 0<= new_row < len(image) and 0 <= new_col < len(image[0]) and (new_row, new_col) not in visited and image[new_row][new_col] == '.':
          queue.append((new_row, new_col)) 
          visited.add((new_row, new_col))
            
            
            
def CountLakes(image: List[List[str], start_pixel: Tuple[int,int]) -> int:
  # code
                           
  if image[start_pixel[0]][start_pixel[1]] == '.':
    return 0
               
  #BFS on land
  queue = []
  queue.append((start_pixel[0],[start_pixel[1]))
  visited = set()
  visited.add((start_pixel[0],[start_pixel[1]))
  cont =0
  while queue:
   curr_row, curr_col = queue.pop()

   for off_row, off_col in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
      new_row, new_col = curr_row + off_row, curr_col + off_col
      if 0<= new_row < len(image) and 0 <= new_col < len(image[0]) and (new_row, new_col) not in visited:
           if image[new_row][new_col] == 'x':                    
             queue.append((new_row, new_col)) 
             visited.add((new_row, new_col))
           else: #water BFS
               bfs_water(image, visited, new_row, new_col)#'.'
                 cont+=1

   return cont-1                         
"""

from typing import List, Tuple


image2 = [["." for _ in range(20)] for _ in range(20)]
land_coordinates = [(2, 2), (2, 3), (2, 4), (5, 4), (6, 5), (12, 4), (14, 4), (15, 4)]
for r, c in land_coordinates:
    image2[r][c] = "x"
# Define the grid (20 pixels wide by 10 pixels tall)
#print(image2)
image = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "x", "x", "x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "x", "x", "x", "x", "x", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", ".", ".", ".", "x", ".", "x", ".", ".", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", "x", ".", ".", ".", "x", "x", "x", "x", "x", "x", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", "x", "x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

def bfs_water(image, visited, new_row, new_col):
  queue = []
  queue.append((new_row,new_col))
  visited.add((new_row, new_col))
  while queue:
    curr_row, curr_col = queue.pop(0)
    for off_row, off_col in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
        new_row, new_col = curr_row + off_row, curr_col + off_col
        if 0<= new_row < len(image) and 0 <= new_col < len(image[0]) and (new_row, new_col) not in visited and image[new_row][new_col] == '.':
            queue.append((new_row, new_col)) 
            visited.add((new_row, new_col))
          
def CountLakes(image: List[List[str]], start_pixel: Tuple[int,int]) -> int:
    # code
                           
    if image[start_pixel[0]][start_pixel[1]] == '.':
        return 0
                
    #BFS on land
    queue = []
    queue.append((start_pixel[0],start_pixel[1]))
    visited = set()
    visited.add((start_pixel[0],start_pixel[1]))
    cont =0
    while queue:
        curr_row, curr_col = queue.pop(0)

        for off_row, off_col in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
            new_row, new_col = curr_row + off_row, curr_col + off_col
            if 0<= new_row < len(image) and 0 <= new_col < len(image[0]) and (new_row, new_col) not in visited:
                if image[new_row][new_col] == 'x':                    
                    queue.append((new_row, new_col)) 
                    visited.add((new_row, new_col))
                else:
                    bfs_water(image, visited, new_row, new_col)#'.'
                    cont+=1

    return cont-1   
# Test the function with the given coordinates
assert CountLakes(image, (2,2)) == 0, "Test failed for (2,2)"
assert CountLakes(image, (6,6)) == 1, "Test failed for (6,6)"
assert CountLakes(image, (5,12)) == 2, "Test failed for (12,5)"
print("All assertions passed.")