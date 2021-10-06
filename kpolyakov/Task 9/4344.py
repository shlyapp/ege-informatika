def is_trapecia(a):

    #if (a[0]+a[1]==180 and a[2]+a[3]==180) or (a[0]+a[2]==180 and a[1]+a[3]==180):
        #if (a[0]<=90 and a[3]<=90) and (a[1]>=90 and a[2]>=90):
           #return True
    #else:
        #print(*a)
        
    #if ((a[0]+a[1]==180 and a[2]+a[3]==180) and (a[0]!=a[2] and a[1]!=a[3])) or ((a[0]+a[3]==180 and a[1]+a[2]==180) and (a[0]!=a[1] and a[2]!=a[3])):
        #return True
    #else:
        #print(*a)

    if (a[0]>=90 and a[1]<=90 and a[2]<=90 and a[3]>=90) or (a[0]<=90 and a[1]>=90 and a[2]>=90 and a[3]<=90):
        if (a[0]==90 or a[1]==90 or a[2]==90 or a[3]==90):
            print(*a)
        return True
   


    
file = open("kpolyakov/Task 9/9-123.csv")
count = 0
for s in file:
    a = list(map(int, s.split(';')))
    if (sum(a)==360 and is_trapecia(a) and a[0]!=a[1]!=a[2]!=a[3]):
        count+=1
        #print(*a)

print(count)