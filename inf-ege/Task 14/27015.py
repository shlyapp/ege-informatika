num = 49**7 + 7**20 - 28
s = ''
while num > 0:
    s += str(num%7)
    num = num//7
print(s.count('0'))