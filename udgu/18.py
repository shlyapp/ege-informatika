with open('udgu/18.csv') as file:
    data = [float(num[:-1].replace(',', '.')) for num in file.readlines()]

summa = 0
maximum = 0

print(data)

for i in range(len(data) - 1):
    if data[i + 1] < data[i]:
        summa += data[i + 1]
    else:
        maximum = max(maximum, summa)
        summa = data[i + 1]

print(maximum)
