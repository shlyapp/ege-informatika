file = open('Testers/210913/17.txt')
data = []
for elem in file:
    data.append(elem[:-1])

counter = 0
maximum = []
for i in range(0, len(data)-1):
    if (int(data[i])%3==0 or int(data[i+1])%3==0):
        counter +=1
        maximum.append(int(data[i])+int(data[i+1]))

print(counter, maximum[-1])