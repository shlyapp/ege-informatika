for m in range(1, 28, 2):
    for n in range(0, 9, 2):
        if 100000000 <= (2**m)*(7**n) <= 300000000:
            print((2**m)*(7**n), n+m)