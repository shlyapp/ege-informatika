file = open("kpolyakov/Task 9/9-107.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    if (sum(a) == 180):
        a.sort()
        if (a[2] == 90):
            count +=1

print(count)