counter = 0
maximum = 0
max_c = 0

def is_true(a, b, c):
    return a**2 + b**2 == c**2

for a in range(1, 5001):
    for b in range(a, 5001):
        c = (a**2 + b**2)**0.5
        if c == int(c) and c <= 5000:
            counter += 1
            if (a + b + c) > maximum:
                maximum =  a + b + c
                max_c = c

print(counter, max_c) 
