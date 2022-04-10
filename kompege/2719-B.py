with open('kompege/27B-2719.txt') as file:
    N = file.readline()
    data = (int(num) for num in file.readlines())

k0 = k1 = 0

for element in data:
    if element % 2 == 0:
        k0 += 1
    else:
        k1 += 1

print((k1*(k1 - 1) // 2) + k0*(k0 - 1) // 2)
