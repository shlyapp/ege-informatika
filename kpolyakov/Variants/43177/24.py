from collections import Counter

with open('kpolyakov/Variants/43177/24.txt') as file:
    line = file.readline()

letters = []

for i in range(len(line)):
    if line[i] == 'A':
        letters.append(f'{line[i + 1]}')

c = Counter(letters)

print(c)
