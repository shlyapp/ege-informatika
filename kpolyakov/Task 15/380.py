
p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

A = set(p + q)

counter = 0

for x in A:
    if (x in p) and (x in q):
        counter+=1

print(counter)