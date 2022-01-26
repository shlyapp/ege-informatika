A = 0

while True:
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((5*x + 3*y != 60) or ((A > x) and (A > y))):
               break
        else:
            continue
        break
    else:
        print(A)
    A += 1