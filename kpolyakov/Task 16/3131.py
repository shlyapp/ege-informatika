from typing import Counter
counter = 0

def F(n):
    global counter
    counter += 1
    if (n >= 1):
        counter += 1
        F(n - 1)
        F(n // 3)
        counter += 1

F(280)
print(counter)