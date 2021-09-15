num = 7*(512**120) - 6*(64**100) + 8**210 - 255
s = ''
while num > 0:
    s += str(num%8)
    num = num // 8
print(s.count('0'))