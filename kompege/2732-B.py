with open('kompege/27B-2732.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = [ [] for i in range(80)]

for element in data:
    k[element % 80] += [element]

ans = []

for i in range(80):
    if len(k[i]) >= 2:
        ans += [max(k[i]) - min(k[i])]

print(max(ans))