file = open('kpolyakov/Task 27/27B-2673.txt')
N = int(file.readline())
buffer = [int(file.readline()) for i in range(6)]
counter = 0
k_2 = k_7 = k_14 = 0

for i in range(N - 6):
    num = int(file.readline())
    if num % 14 == 0:
        counter += i
    elif num % 7 == 0:
        counter += k_2
    elif num % 2 == 0:
        counter += k_7
    else:
        counter += k_14

    next = buffer[0]
    if next % 7 == 0:
        k_7 += 1
    if next % 2 == 0:
        k_2 += 1
    if next % 14 == 0:
        k_14 += 1
    buffer.append(num)
    buffer.pop(0)

print(counter)