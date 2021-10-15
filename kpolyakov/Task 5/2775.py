mass = set()
for i in range(20, 601):
    num = bin(i)[2:-2]
    mass.add(num)
print(len(mass))
    