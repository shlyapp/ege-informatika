P = [2, 4, 9, 10, 15]
Q = [3, 8, 9, 10, 20]

A = set(P+Q)
counter = 0

mass = []

for x in A:
    if (x in P) and (x in Q):
        mass.append(x)

print(*mass)