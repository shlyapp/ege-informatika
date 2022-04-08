print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x <= z) or (y == w) or not(y)):
                    print(x, y, z, w)