counter = 0

def F(n):
    if (n > 0): G(n - 1)

def G(n):
    global counter
    counter += 1
    if (n > 1): F(n - 3)

F(11)
print(counter)