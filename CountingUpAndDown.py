# Given: N
# Return: a list counting up and down by 1 that has length
# N
# Examples: N = 5
# Output: [1, 2, 3, 2, 1]
# N = 6
# Output: [1, 2, 3, 3, 2, 1]

# create a list of integers starting from 1, increasing by
# 1 each element until N // 2, adding the potential single
# middle digit of N is odd, then decreasing by 1 until the
# final element is 1.
def marching_in(N):
  # the midpoint of N, rounded down
  midpoint = N // 2
  # create a list to house the return values
  output = []
  # iterate through the range from 1 to (N // 2 + 1), appending # each value to the output
  for i in range(1, midpoint + 1):
    output.append(i)
  # if N is odd, add the next value
  if N % 2 == 1:
    output.append(midpoint + 1)  # same as math.ceil(N / 2)
  # iterate through the range from N // 2 to 1 (descending,
  # appending each value to the output
  for i in range(midpoint, 0, -1):
    output.append(i)
  return output

# use the `list()` function on the ranges described in the
# previous example along with the `+` operator for lists to
# condense the above function into one line.
def marching_in_but_cooler(N):
  midpoint = N // 2
  # creates a list representing the given range
  side = list(range(1, midpoint + 1))
  # if N is odd, create a list with a single element
  # containing the true midpoint. structured as a list to
  # be added to the other lists more easily.
  odd_midpoint = []
  if N % 2 == 1:
    odd_midpoint.append(midpoint + 1)
  # concatenate the lists together using `+`. reverse
  # `side` to reuse that list more effectively.
  return side + odd_midpoint + side[::-1]

print(marching_in(5))
print(marching_in_but_cooler(5))
print(marching_in(8))
print(marching_in_but_cooler(8))
