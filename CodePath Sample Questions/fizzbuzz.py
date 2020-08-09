def fizzbuzz(n):
  for current_number in range(0,n+1):
    if current_number % 3 == 0 and current_number % 5 == 0:
      print("fizzbuzz")
    elif current_number % 3 == 0:
      print("fizz")
    elif current_number % 5 == 0:
      print("buzz")
    else:
      print(current_number)

fizzbuzz(15)

# for every number up to and including the input
  # is that number divisible by 3?
    # print fizz
  # is that number divisible by 5?
    # print buzz
  # is that number divisible by 3 and 5?
    # print fizzbuzz
