print("z w y x")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((y <= z) or ((not x) and w)) == (w == z)):
                    print(z, w, y, x)