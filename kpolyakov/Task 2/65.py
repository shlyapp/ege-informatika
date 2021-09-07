print ("y x z")

for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not x) and y and z) or ((not x) and y and (not z)) or ((not x) and (not y) and (not z)):
                print(y, x, z)