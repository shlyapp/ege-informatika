file = open("kpolyakov/Task 9/9-107.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    if (sum(a) == 180) and (a[0] == a[1] ==a [2] == 60):
        count +=1

print(count)