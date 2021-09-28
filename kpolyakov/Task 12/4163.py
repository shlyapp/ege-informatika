s  = '3' + '1'*103  + '3'*97
while '12' in s or '13' in s:
    s = s.replace('12', '31', 1)
    s = s.replace('31', '23', 1)
    s = s.replace('13', '23', 1)

print(s)
print(sum(map(int, s)))
