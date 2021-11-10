k = 0

def F(n):
  global k
  k += 1
  if n > 0: 
    k += 1    
    G(n - 1)

def G(n):
  global k
  k += 1
  if n > 1: 
    k += 1    
    F(n - 2)

F(12)
print(k)