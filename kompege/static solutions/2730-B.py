with open('kompege/files/27B-2730.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k12 = []
k = []

for element in data:
    if element % 12 == 0:
        k12 += [element]
    else:
        k += [element]

k12.sort(reverse=True)
k.sort(reverse=True)

ans = k12[:4] + k[:4]

maximum = 0

for a in range(len(ans)):
    for b in range(a + 1, len(ans)):
        for c in range(b + 1, len(ans)):
            for d in range(c + 1, len(ans)):
                if (ans[a] * ans[b] * ans[c] * ans[d]) % 12 == 0:
                    maximum = max(maximum, ans[a] + ans[b] + ans[c] + ans[d])

print(maximum)
