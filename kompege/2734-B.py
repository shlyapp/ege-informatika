from collections import Counter

with open('kompege/27B-2734.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

s = []

for element in data:
    summa = sum(map(lambda x: int(x), str(element)))
    s += [summa]

s = Counter(s)

print(s.most_common()[0][1])