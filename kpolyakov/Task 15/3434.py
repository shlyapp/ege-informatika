P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

A = set(P+Q)

counter = 0

for x in A:
    if (x in P) and ((x in Q) ):
        counter+=1

print(counter)