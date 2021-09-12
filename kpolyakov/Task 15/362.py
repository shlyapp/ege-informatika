P = [i for i in range(37, 61)]
Q = [i for i in range(40, 78)]
A = set(P+Q)
counter = 0

for x in A:
    if (x in P) <= (((x in Q) or not(x in A)) <= (not(x in P))):
        counter+=1

print(counter)