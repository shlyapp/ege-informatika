with open('kompege/27B-2727.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = []
k_31 = []

for element in data:
    if element % 31 == 0:
        k_31 += [element]
    else:
        k += [element]

k.sort()
k_31.sort()

print(min([k_31[0]*k_31[1], k[0]*k_31[0]]))
