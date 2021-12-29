import math

def is_prime(x):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

for i in range(math.ceil((1000000 // 2) ** 0.5), math.ceil((101000000 // 2) ** 0.5) + 1):
    if is_prime(i):
        print(2*i**2, i)

