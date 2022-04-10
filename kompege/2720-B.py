with open('kompege/27B-2720.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k7 = k = 0

for element in data:
    if element % 7 == 0:
        k7 += 1
    else:
        k += 1

print((k7*(k7-1)//2) + k*k7)
