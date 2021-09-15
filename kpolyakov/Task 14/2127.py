x = 81**15 + 3**22 - 27
s = ''
while x > 0:
    s += str(x%9)
    x = x//9
print(s.count('8'))