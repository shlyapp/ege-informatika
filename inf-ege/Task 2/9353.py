print("x y z")

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (((not z) and x) or (x and y)):
                print(x, y, z)

# zyx