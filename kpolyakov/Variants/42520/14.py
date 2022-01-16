num = 100**2 + 625**25 + 5**100
counter = 0
while num > 0:
    if (num % 15) == 12:
        counter += 1
        num //= 15
        print(num)
print(counter)
    