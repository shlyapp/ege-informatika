P = [1, 3, 4, 9, 11, 13, 15, 17, 19, 21]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

A = set(P+Q)

counter = 0

for x in A:
    if ((x in P) and (x in Q)):
        counter += 1

print(counter)