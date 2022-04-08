with open("dosrok/24.txt") as file:
    line = file.readline()

line = line.replace('AC', '1')
line = line.replace('AB', '1')

counter = 1
maximum = 0

for i in range(len(line) - 1):
    if line[i + 1] == line[i] == '1':
        counter += 1
    else:
        maximum = max(counter, maximum)
        counter = 1

print(maximum)