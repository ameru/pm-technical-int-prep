# Given an integer N, write a function that returns the Nth
# Fibonacci number. Example outputs:

# fibonacci(1) -> 0, since 0 is technically first
# fibonacci(4) -> 2
# fibonacci(9) -> 21
# fibonacci(15) -> 610

#UMPIRE

#Understand:
#Input: int, Output: int
#sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

#Match:
#Fibonacci sequence but iterative

#Plan:
#If n <= 1, return 0
#If n < 2, return 1
#else add the 2 inputs to create the next 2 sequence numbers



def fibonacci(n):
  # base cases (USUALLY easier to come up with)
  if n <= 1:
    return 0
  elif n == 2:
    return 1
  
  # recursive case
  else:
    return fibonacci(n-2) + fibonacci(n-1)

#print(fibonacci(1))
#print(fibonacci(10))


#### Stretch: ####
# Goal: to see how many recursive calls we can make before we get a "stack overflow exception" AKA maximmum depth for recursion

# Plan:
# make a recursive function call itself forever
# use an integer to keep track of the numbers of function calls we've made so far

def infinity(call_count):
  # base case: 
  if False: #never executed
    pass

  # recursive case:
  print(call_count)
  return infinity(call_count + 1)


print(infinity(1))

#I had to run it on my ide so that I can copy and paste the results


# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     infinity(1)
#   File "C:/Users/nelso/OneDrive/Desktop/CS-295/My exercises/maxdepth.py", line 8, in infinity
#     return infinity(call_count + 1)
#   File "C:/Users/nelso/OneDrive/Desktop/CS-295/My exercises/maxdepth.py", line 8, in infinity
#     return infinity(call_count + 1)
#   File "C:/Users/nelso/OneDrive/Desktop/CS-295/My exercises/maxdepth.py", line 8, in infinity
#     return infinity(call_count + 1)
#   [Previous line repeated 1009 more times]
#   File "C:/Users/nelso/OneDrive/Desktop/CS-295/My exercises/maxdepth.py", line 7, in infinity
#     print(call_count)
# RecursionError: maximum recursion depth exceeded while pickling an object
