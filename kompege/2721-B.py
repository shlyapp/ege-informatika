with open('kompege/27B-2721.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = k65 = k5 = k13 = 0

for element in data:
    if element % 65 == 0:
        k65 += 1
    elif element % 13 == 0:
        k13 += 1
    elif element % 5 == 0:
        k5 += 1


print((k65*(k65 - 1) // 2) + k65*(N-k65) + (k13*k5))
