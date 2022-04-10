line = '1' + '0'*33

while '1' in line or '100' in line:
    if '100' in line:
        line = line.replace('100', '0001', 1)
    else:
        line = line.replace('1', '00', 1)

print(line.count('0'))
