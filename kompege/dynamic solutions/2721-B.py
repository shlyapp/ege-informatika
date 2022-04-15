file = open('kompege/files/27B-2721.txt')
N = int(file.readline())
k5 = k13 = k65 = counter = 0

for i in range(N):
    num = int(file.readline())

    if num % 65 == 0: counter += i
    elif num % 5 == 0: counter += k13
    elif num % 13 == 0: counter += k5
    else: counter += k65

    if num % 65 == 0: k65 += 1
    if num % 5 == 0: k5 += 1
    if num % 13 == 0: k13 += 1

print(counter)