P = [i for i in range(2, 11)]
Q = [i for i in range(6, 15)]
A = set(P+Q)
counter = 0

for x in A:
    if ((x in A) <= (x in P)) or (x in Q):
        counter+=1

print(counter-1)