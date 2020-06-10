# break down n into all prime factors, then pick the largest 

def largest_prime_factor(n):
  if n < 2:
    return None

  potential_prime_factor = 2
  prime_factors = []
  while potential_prime_factor <= n:
    if n % potential_prime_factor == 0:
      n /= potential_prime_factor
      # n /= is short for n = n/potential_prime_factor
      prime_factors.append(potential_prime_factor)
    else:
      potential_prime_factor += 1

  return prime_factors[-1]
    # you can also return max(prime_factors), but will take longer

print(largest_prime_factor(5)) #should be 5
print(largest_prime_factor(26)) #should be 13
print(largest_prime_factor(13195)) #should be 5
print(largest_prime_factor(600851475143)) #should be 13
