with open("kompege/files/27B-2722.txt") as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k5_0 = k5_1 = k_0 = k_1 = 0

for element in data:
    if element % 5 == 0 and element % 2 == 0:
        k5_0 += 1
    elif element % 5 == 0 and element % 2 == 1:
        k5_1 += 1
    elif element % 2 == 0:
        k_0 += 1
    else:
        k_1 += 1

print(k5_0*k_1 + k5_1 * k_0 + k5_0 * k5_1)
