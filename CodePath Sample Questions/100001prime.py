# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# Understand
  #input: we have no input
  #action: find the nth prime number, n = 10,001
  #output: 1 integer, 10 001st prime number

#Match

#Plan
  #7th prime, leave out 1
  #check if current number is prime (only divisible by 1 and itself)

  #how to check if a number is prime:
  #k = 3, start the loop, append k, start another loop dividing k by elements starting from index 0

#Implement

#Review

#Evaluate

#What is the 10001st prime number?

def nth_prime(n):
  # start with an empty list of primes
  primes = []
  # the first known prime is 2
  potential_prime = 2
  while len(primes) < n:
    if isPrime(potential_prime, primes):
      primes.append(potential_prime)
    potential_prime += 1

  return primes[-1]

def isPrime(n, list_of_known_primes):
  for val in list_of_known_primes:
    if n % val == 0:
      return False
  return True

# def isPrime(n):
#   for i in range(2, n):
#     if n % i == 0:
#       return False
#   return True

print(nth_prime(3))
print(nth_prime(6))
print(nth_prime(10001))

