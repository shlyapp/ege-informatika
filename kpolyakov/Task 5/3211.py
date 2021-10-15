def F(x):
    num = bin(x)[2:]

    for i in range(3):
        if (num.count('0') == num.count('1')):
            num += num[-1]
        elif (num.count('0') > num.count('1')):
            num += '1'
        else:
            num += '0'

    z = int(num, 2)
    return z

for i in range(1, 80):
    if (F(i)%2==0 and F(i)%4!=0):
        print(i)