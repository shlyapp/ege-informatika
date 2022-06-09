line = '3' + '6' * 120 + '3'

while '63' in line or '664' in line or '6665' in line:
    if '63' in line:
        line = line.replace('63', '4', 1)
    if '664' in line:
        line = line.replace('664', '5', 1)
    if '6665' in line:
        line = line.replace('6665', '3', 1)

print(line)
