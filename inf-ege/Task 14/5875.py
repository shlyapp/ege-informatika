for i in range(2, 100):
    num = 24
    s = ''
    while num > 0:
        s += str(num%i)
        num = num//i
    if (s[::-1] == '40'):
        print(i)