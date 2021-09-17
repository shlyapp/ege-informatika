p1, p2, q1, q2, r1, r2 = 10, 40, 5, 15, 35, 50
P = [i/10 for i in range(p1*10, p2*10+1)]
Q = [i/10 for i in range(q1*10, q2*10+1)]
R = [i/10 for i in range(r1*10, r2*10+1)]

def f(x, A):
    return (((x in A) or (x in P)) or ((x in Q) <= (x in R)))

A = set()

for x in [i/10 for i in range(40, 410)]:
    if not f(x, A):
        A.add(x)

print(*sorted(A))