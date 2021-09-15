num = 81**2017 + 9**5223 - 81
s = ''
while num > 0:
    s += str(num%9)
    num = num//9
print(s.count('8'))