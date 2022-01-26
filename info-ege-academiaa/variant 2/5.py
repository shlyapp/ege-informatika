def f(num):
    num = bin(num)[2:]
    if num.count('1') % 2 == 0:
        num = num + '0'
    else:
        num = num + '1'

    if num.count('1') % 2 == 0:
        num = num + '0'
    else:
        num = num + '1'
        
    return int(num, 2)

for N in range(0, 10000):
    if f(N) > 96:
        print(N)
        break

