num = 16**25 - 2**32 - 32
s = ''
while num > 0:
    s = str(num % 4) + s
    num = num // 4

print(s.count('3'))