# Given N, produce a right triangle of zeros N rows tall

def printPascal(n):
  # Iterate through every line and print entries in it
  for line in range(0, n):
    # every line has number of integers equal to line number
    for i in range(0, line + 1):
      print(binomialCoeff(line, i), " ", end = "")
     print()
     
 def binomialCoeff(n, k):
  res = 1
  if (k > n - k):
    k = n - k
  for i in range(0, k):
    res = res * (n - i)
    res = res // (i + 1)
  return res
  
# Driver program
n = 7
printPascal(n)

# Output:
>>>
1
1 1
1 2 1 
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
