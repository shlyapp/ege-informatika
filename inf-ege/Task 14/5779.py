num = 57
s = ''
while num > 0:
    s += str(num%4)
    num = num//4
print(s[::-1])