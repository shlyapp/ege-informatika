file = open('kpolyakov/Task 17/17-1.txt')
data = []
for elem in file:
    data.append(elem[:-1])

counter = 0
maximum = []
for i in range(0, len(data)-1):
    if (int(data[i])%7==0 and int(data[i+1])%17!=0) or (int(data[i])%17!=0 and int(data[i+1])%7==0):
        counter +=1
        maximum.append(int(data[i])+int(data[i+1]))

print(counter, min(maximum))