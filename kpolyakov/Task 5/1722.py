k = 0

def F(a):
    global k
    a = list(map(int, a))
    if (a.count(0) == 1):
        a.sort()
        if (a[2] - a[1] == 3 and a[1] == 5):
            k += 1

for i in range(100, 1000):
    num = str(i)
    F(num)

print(k)
