import math

def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

START = 525784203
END = 728943762

for x in range(math.ceil(START**0.25), math.ceil(END**0.25)):
    if is_simple(x):
        print(x**4, x**3)