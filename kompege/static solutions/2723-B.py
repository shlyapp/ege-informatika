import math

with open('kompege/files/27B-2723.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k19 = 0

for element in data:
    if element % 19 == 0:
        k19 += 1

print(math.factorial(k19) // (math.factorial(3) * (math.factorial(k19 - 3))))
