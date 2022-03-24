line = '121212121212121212121212'

while '12' in line:
    line = line.replace('12', '4', 1)

print(sum(map(int, line)))
