file = open("kpolyakov/Task 9/9-130.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    a.sort()
    if (a[1]-a[0] == a[2]-a[1] != 0):
        count+=1

print(count)