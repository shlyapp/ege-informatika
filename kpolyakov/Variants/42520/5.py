def func(num):
    num = bin(num)[2:]
    while len(num) < 8:
        num = '0' + num
    print(num)
    num = num[:2] + num[6:]
    return int(num, 2)

for num in range(131, 256):
    if func(num) == 10:
        print(num)
        break
