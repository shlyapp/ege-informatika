print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not w and ((x and (not z) or ((not x) and (not y)) and z)) ) == 1:
                    print(x, y, z, w)

# zwyx