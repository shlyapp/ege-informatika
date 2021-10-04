import itertools

file = open("kpolyakov/Task 9/9-130.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    a.sort()
    ls = list(itertools.permutations(a, r=3))
    for elem in ls:
        if (elem[1]/elem[0]==elem[2]/elem[1]!=1):
            count += 1
            break

print(count)