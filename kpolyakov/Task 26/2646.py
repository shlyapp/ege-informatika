file = open('kpolyakov/Task 26/26-j4.txt')
data = sorted([int(x) for x in file])
v = sum(data)
maxi = data[0:1000]
mini = data[9000:10000]
print(v - sum(maxi) - sum(mini), data[8999])

