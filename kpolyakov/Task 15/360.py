P = [i for i in range(10, 26)]
Q = [i for i in range(15, 31)]
R = [i for i in range(25, 41)]
A = set(P+Q+R)
counter = 0

for x in range(10, 41):
    if not(((x in Q)<=(not(x in R))) and (x in A) and not(x in P)):
        counter+=1

print(counter-1)