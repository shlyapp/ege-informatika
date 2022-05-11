from collections import Counter
file = open('kpolyakov/Variants/44140/24.txt')
min_A = float('inf')
line_A = ''

for line in file.readlines():
    count = line.count('A')
    if count < min_A:
        min_A = count
        line_A = line

line_A = Counter(line_A)
letter = (line_A.most_common()[1][0])  # V

counter = 0
for line in file.readlines():
    counter += line.count('V')

print(counter)
