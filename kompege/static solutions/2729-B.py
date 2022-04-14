with open('kompege/files/27B-2729.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = [[] for i in range(11)]

for element in data:
    k[element % 11] += [element]

ans = []

for i in range(11):
    k[i].sort()
    ans += k[i][:3]

a = []

for i in range(len(ans)):
    for j in range(i + 1, len(ans)):
        for k in range(j + 1, len(ans)):
            if (ans[i] + ans[j] + ans[k]) % 11 == 0:
                a += [ans[i] + ans[j] + ans[k]]

print(min(a))
