for i in range(2, 30001):
    k = 0
    n = 0
    for x in range(1, i // 2 + 1):
        if i % x == 0:
            k += x
    for j in range(1, k // 2 + 1):
        if k % j == 0:
            n += j
    if i == n and i != k  and i == min(i, k):
        print(i, k)

    