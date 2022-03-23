line = '1' + '0' * 75

while '10' in line or '1' in line:
    if '10' in line:
        line = line.replace('10', '001', 1)
    else:
        line = line.replace('1', '00', 1)

print(line.count('0'))
