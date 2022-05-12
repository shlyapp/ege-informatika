file = open('kpolyakov/Task 27/27A-2672.txt')
N = int(file.readline())
k_6 = k_2 = k_3 = 0
counter = 0

for i in range(N):
    num = int(file.readline())
    if num % 2 == 0:
        counter += k_3
    elif num % 3 == 0:
        counter += k_2
    elif num % 6 == 0:
        counter += i
    else:
        counter += k_6

    if num % 6 == 0:
        k_6 += 1
    if num % 2 == 0:
        k_2 += 1
    if num % 3 == 0:
        k_3 += 1

print(counter)