# create a N x N grid with each inner "ring" being one
# greater than the next.
#
# general approach: create an "upside-down" triangle of 
# the same value, like the example below:
#
# 0, 0, 0, 0, 0, 0, 0, 0, 0
#    1, 1, 1, 1, 1, 1, 1
#       2, 2, 2, 2, 2
#          3, 3, 3,
#             4
#
# while constructing this triangle line-by-line, prepend
# and append the consecutive list of numbers leading up / 
# counting down from to the triangle value in the line, as
# follows:
#
# [0, 1, 2] + [3, 3, 3] + [2, 1, 0]
#
# this will result in the top half of the grid (example
# below):
#
# 0, 0, 0, 0, 0, 0, 0, 0, 0
# 0, 1, 1, 1, 1, 1, 1, 1, 0
# 0, 1, 2, 2, 2, 2, 2, 1, 0
# 0, 1, 2, 3, 3, 3, 2, 1, 0
# 0, 1, 2, 3, 4, 3, 2, 1, 0
#
# now just append copies of each row to the grid, starting
# from the last row. if N is odd, skip the last row as it
# does not need to be duplicated.

# you don't need to use the math library for this, but it
# is more readable with it. A non-`math` alternative will
# be commented out.
import math

def outside_in(N):
  # define the 2D grid ("big list")
  grid = []
  # how tall the triangle should be, also the same as half
  # the grid height rounded up.
  triangle_height = math.ceil(N / 2)
  # non-`math` alternative
  # triangle_height = (N // 2) + (N % 2)

  # create the top half of the grid
  for num in range(triangle_height):
    # creates a list of the same number representing the
    # triangle's row
    triangle_row = [num] * (N - (num * 2))
    # the side to prepend to the triangle row
    side = list(range(num))
    # prepend the side to the triangle row, the append the
    # same `side` but reversed. Assign to the `grid_row`.
    grid_row = side + triangle_row + side[::-1]
    # append the grid row to the grid
    grid.append(grid_row)
  
  # determine how many rows to duplicate. if N is odd, we
  # should not duplicate the last row (uses integer 
  # division).
  num_rows_to_duplicate = N // 2

  # # create the bottom half of the grid
  # for num in range(num_rows_to_duplicate):
  #   # make the bottom half of the grid mirror the top half
  #   # by appending the existing lists in the grid in
  #   # reverse order.
  #   grid.append(grid[num_rows_to_duplicate - num - 1])

  # FWIW, you could also just append a copied and reversed
  # version of `grid`, excluding the last row if N is odd. # See the code below (would replace lines 66 - 70):
  grid += grid[num_rows_to_duplicate - 1::-1]

  # you're done! return `grid`
  return grid

# used to help visualize the 2D output
def print_2D_list(list_of_lists):
  if (type(list_of_lists) == list):
    print("[")
  for l in list_of_lists:
    print("  " + str(l))
  if (type(list_of_lists) == list):
    print("]")

# even example
print_2D_list(outside_in(10))
# odd example
print_2D_list(outside_in(11))
