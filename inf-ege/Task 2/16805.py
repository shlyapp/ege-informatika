print("y x z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((not z) == x) <= (y == (w or x))):
                    print(y, x, z, w)

# yxwz