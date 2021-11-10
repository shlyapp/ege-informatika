def F(n):
    if (n <= 18):
        return n + 3
    else:
        if (n % 3 == 0): return (n//3)*F(n//3)+n-12
        else: return F(n-1) + n*n + 5

#def is_good(n):
    #for element in str(n):
        #if (int(element) % 2 != 0):
            #return False
    #else:
        #return True



counter = 0
for i in range(1, 801):
    if (list(map(lambda x: int(x) % 2, str(F(i)))).count(0) == len(str(F(i)))):
        counter += 1

print(counter)

