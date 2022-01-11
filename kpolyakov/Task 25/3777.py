b = []
for x in range(3, 88):
    counter = 0
    for i in range(1, x + 1):
        if (x % i == 0):
            counter += 1
    if (counter == 2):
        b.append(x)

for i in b:
    x = i ** 4
    while x < 55000000:
        x = x * 2
    if  x <= 60000000:
        print(x, i**4)