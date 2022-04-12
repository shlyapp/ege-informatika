from numpy import maximum


with open('kompege/27B-2728.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k_0 = []
k_1 = []
k23_0 = []
k23_1 = []

for element in data:
    if element % 23 == 0 and element % 2 == 0:
        k23_0 += [element]
    if element % 23 == 0 and element % 2 != 0:
        k23_1 += [element]
    if element % 23 != 0 and element % 2 == 0:
        k_0 += [element]
    if element % 23 != 0 and element % 2 != 0:
        k_1 += [element]

k_0.sort()
k_1.sort()
k23_0.sort()
k23_1.sort()

ans = k_0[-2:] + k_1[-2:] + k23_0[-2:] + k23_1[-2:]

maximum = 0


for i in range(len(ans)):
    for j in range(i + 1, len(ans)):
        s = ans[i] + ans[j]
        if s % 2 == 0 and (ans[i] % 23 == 0 or ans[j] % 23 == 0):
            maximum = max(maximum, s)

print(maximum)
