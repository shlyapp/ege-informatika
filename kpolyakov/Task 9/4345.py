file = open("kpolyakov/Task 9/9-127.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    if (a[1]**2-4*a[0]*a[2] > 0):
        count +=1

print(count)