A = 1

def Del(num, A):
    return num % A == 0

while True:
    for x in range(1, 1000000):
        if not ((not Del(x, A)) <= (Del(x, 6) <= (not Del(x, 4)))):
            break
    else:
        print(A)
    A += 1

