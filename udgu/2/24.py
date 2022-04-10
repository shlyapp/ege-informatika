with open('udgu/2/26.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

V = sum(data) * 0.9
v = []

data.sort(reverse=True)

for i in range(len(data)):
    if sum(data) <= V:
        v = data[i:]
        break
    else:
        data[i] = data[i] * 0.8

print(len(v), max(v))
