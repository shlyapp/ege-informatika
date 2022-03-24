from collections import Counter

with open('udgu/24.txt') as file:
    line = file.readline()

letters = []

for i in range(1, len(line) - 1):
    a, b, c = line[i - 1], line[i], line[i + 1]
    if a == 'X' and c == 'Z':
        letters.append(b)

c = Counter(letters)
print(c)
