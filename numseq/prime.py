def primes(n):
  """
    creates list of prime numbers
  """

  prime_list = []

  for val in range(n):
    if val >1:
      for i in range(2, val):
        if val%i == 0:
          break
      else:
        prime_list.append(val)

  return prime_list


def is_prime(n):
  """
    return true if number is prime
  """
  if n >1:
    for i in range(2,n):
      if n%i == 0:
        return False
  else:
    return False 
  
  return True
        

