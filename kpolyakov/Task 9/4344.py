def is_trapecia(a):

    if (a[0]+a[1] == a[2]+a[3]):
        return True
    
    

file = open("kpolyakov/Task 9/9-123.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    if (sum(a)==360 and a[0]!=a[1]!=a[2]!=a[3] and is_trapecia(a)):
        count+=1
        print(*a)

print(count)