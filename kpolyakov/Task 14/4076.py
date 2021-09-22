num = 7**1003 + 6*(7**1104) - 3*(7**57) + 294
s = ''
while num > 0:
    s = str(num % 7) + s
    num = num // 7

print(sum(map(int, s)))