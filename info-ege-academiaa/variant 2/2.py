print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not w) or (x or (not z)) and ((not x) or (not y) or z)):
                    print(z, w, y, x)