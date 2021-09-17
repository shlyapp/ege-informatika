p1, p2, q1, q2 = 7, 14, 9, 11
P = [i/10 for i in range(p1*10, p2*10+1)]
Q = [i/10 for i in range(q1*10, q2*10+1)]

def f(x, A):
    return (((x in P) == (x in Q)) <= (x not in A))

A = set([i/10 for i in range(60, 150)])

for x in [i/10 for i in range(60, 150)]:
    if not f(x, A):
        A.remove(x)

print(*sorted(A))