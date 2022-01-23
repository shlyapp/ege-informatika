A = 1

while True:
    for x in range(1, 1000000):
        if not ((x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))):
            break
    else:
        print(A)
        break
    A += 1