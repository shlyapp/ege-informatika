k=0
for x in range(3,1000):
    num=bin(x)[2:]
    num=num+num[-2]+num[1]
    z=int(num,2)
    if 149<z<251:
        k+=1
print(k)