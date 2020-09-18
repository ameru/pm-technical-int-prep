# here's a 2D array - it's 10x10
grid = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0]
]

## let's start by printing the whole array
def print_grid(grid):
  print("----")
  for row in grid:
    printable_row = "" 
    for column in row:
      printable_row += str(column)
    print(printable_row)
  print("----")

print_grid(grid)

## the above code helps us visualize each row
## let's try putting a 1 somewhere in the grid:

x = 3
y = 7

# what happens when we do this?
grid[x][y] = 1

print_grid(grid)

## Normally, we are used to the X variable referring to the horizontal (-) axis, while the Y variable refers to the vertical axis (|)
## Normally we write coordinates x,y

grid[x][y] = "wrong"
print_grid(grid)

## However, when we access a 2D array, the first bracket indicates the row, and the second bracket indicates the column

row = y 
column = x

grid[row][column] = "correct"
print_grid(grid)

## This is one of the most common pitfalls engineers make while in an interview, so we're hoping to spare you the trouble!

grid[x][y] = 0
grid[y][x] = 0
## let's reset the grid for the next section

## What if we want to access a particular section of the grid? We'll need to use offsets. 

## let's try to create a 3x3 square within the grid, given a center - try moving the box

box_center_row = 6
box_center_column = 6

grid[box_center_row][box_center_column] = 1 #center
grid[box_center_row+1][box_center_column] = 1 #down 
grid[box_center_row-1][box_center_column] = 1 #up
grid[box_center_row][box_center_column+1] = 1 #right
grid[box_center_row][box_center_column-1] = 1 #left
grid[box_center_row+1][box_center_column+1] = 1 #down, right
grid[box_center_row+1][box_center_column-1] = 1 #down, left
grid[box_center_row-1][box_center_column+1] = 1 #up, right
grid[box_center_row-1][box_center_column-1] = 1 #up, left

print_grid(grid)


# Python3 program to rotate an array by 
# d elements 
# Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
	for i in range(d): 
		leftRotatebyOne(arr, n) 

# Function to left Rotate arr[] of size n by 1*/ 
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
		

# utility function to print an array */ 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ") 


# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
