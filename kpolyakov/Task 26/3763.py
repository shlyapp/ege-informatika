from xmlrpc.client import MAXINT


file = open('kpolyakov/Task 26/26-47.txt')
N = 1000
data = [int(num) for num in file]

sr_couple = []

for i in range(N - 1):
    for j in range(i + 1, N):
        sr_couple.append((data[i]+data[j]) // 2)

K = []

for element in sr_couple:
    counter = 0
    for i in range(N):
        if element > data[i]:
            counter += 1
    K.append(counter)

counter = 0 
maximum = 0

for element in K:
    if element != 0 and element % 100 == 0:
        counter += 1
        maximum = max(maximum, element)

print(counter, maximum)
    