# Given N  
# return a 2D array that represents the first N rows of Pascal's Triangle
# To get the Nth row of pascal's triangle,
# the first and last value are always 1
# the value of row[i] is the sum of the value of the previous row at i, and the the value of the previous row at i-1
## for example:
N = 3
# return:
[
  [1],
  [1,1],
  [1,2,1],
]

N = 7
# return:
[
  [1],
  [1,1],
  [1,2,1],
  [1,3,3,1],
  [1,4,6,4,1],
  [1,5,10,10,5,1],
  [1,6,15,20,15,6,1]
]

## (Scroll down for optional help , stretch questions, and useful links)

# Understand:
# every line has a number of integers
# iterate through every line, concatenating the values
# print the entries
# append 1 to first index and last index

# Matching:
# Variant of a right triangle problem

# Planning:
# create a 2D array, return an object
# Given a # = total # of rows
# Use a for loop to iterate through each row
# each list is representative of each row
# first one is single element list with value of 1
# list after that will have appending 1s
# use math to compute each row

# Implement:
def PascalTriangle(n):
  if n < 1:
    return []
  triangle = []
  current_row = [1]
  triangle.append(current_row)
  for i in range(n - 1):
    next_row = []
    next_row.append(1)
    for j in range(len(current_row)-1):
      next_element = current_row[j] + current_row[j + 1]
      next_row.append(next_element)
    next_row.append(1)
    triangle.append(next_row)
  return triangle

def print_grid(grid):
  print("----")
  for row in grid:
    printable_row = ""
    for column in row:
      printable_row += str(column) + ","
    print(printable_row)
  print("----")

print_grid(PascalTriangle(5))








# Optional Help 1-

## In the U (Understand) step of UMPIRE, make sure you understand
### - the input & output
### - how much longer will each row of the triangle be than the last?
### - which element (and at which index) do you need from the previous row to construct the current row?
### - how to access an element at grid[0][7] ?  Review 2D arrays guide if they're new or still surprising to you:
#### https://repl.it/@lizthedeveloper/2D-Arrays-Patterns#main.py


## Optional Help 2 - Your instructor Richard has identified 3 different approaches to solve this problem.  
### His 4 approaches (zero-indexed):
## Approach 0-
# initialize all places in the triangle, THEN fill their values appropriately

## Approach 1-
# incrementally appends elements and adds the previous
# parent's value to each child element.

## Approach 2-
# copies the entire previous line, adds those values to the
# copied version but shifted one place, then appends the final

## Approach 3 -
# the "math-y" solution: each element can be caluclated based
# on it's line, index, and previous element's value using the
# following formula:
#   element = prev_element * (line - index) / index 

### 1. Identify which one is your solution.
### 2. Try solving the problem is another way. (Hint: the hardest but maybe also the most educational is the "mathematical approach")

#########################################
## Helpful Links
# Week 5 SlideDeck (Liz Howard): https://docs.google.com/presentation/d/1URCVuKy7Jpqd9PzGmx7PdXU5xJ9gxAC_z3cH279Sa6k/edit#slide=id.g85c8f1be08_0_150
 
# Week 5 in Course Portal:
# https://courses.codepath.com/courses/intro_software_eng/unit/5#!overview

# Helpful tutorial for 2D Array:
# https://repl.it/@YuSu2/2DArrayTutorial

# Project Euler problems you might be interested in:
## Project Euler's problems are easiest solved if you have first solved Pascal's triangle the "mathy way". Read about the 4 approaches above if you're interested.
## 148 is "medium spicy" 203 is "quite spicy"

## 🌶️🌶️ 148: Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle
# https://projecteuler.net/problem=148

## 🌶️🌶🌶️  203: Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
#https://projecteuler.net/problem=203
