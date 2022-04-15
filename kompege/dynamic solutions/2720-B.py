file = open('kompege/files/27B-2720.txt')
N = int(file.readline())
k7 = counter = 0

for i in range(N):
    num = int(file.readline())
    
    if num % 7 == 0:
        counter += i
    if num % 7 != 0:
        counter += k7

    if num % 7 == 0:
        k7 += 1

print(counter)