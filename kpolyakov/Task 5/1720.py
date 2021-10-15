
def F(a):
    n = list(map(int, str(a)))
    n.sort()
    min = ''
    max = ''
    if (0 in n):
        return False
    max = int(str(n[2])+str(n[1]))
    min = int(str(n[0])+str(n[1]))
    if (max - min == 30):
        return True

counter = 0
for i in range(100, 199):
    if (F(i)):
        counter +=1

print(counter)
