file = open("kpolyakov/Task 26/26-69.txt")
N = 6000

data = []

for line in file:
    couple = list(map(int, line.split()))
    data.append(couple)

data.sort()

maximum = 0
counter = 1
row_number = 0

for i in range(N - 1):
    if data[i][0] == data[i + 1][0] and data[i][1] + 1 == data[i + 1][1]:
        counter += 1
    else:
        if maximum <= counter:
            row_number = data[i][0]
            maximum = counter
        counter = 1

print(row_number, maximum)
