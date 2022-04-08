with open("dosrok/17.txt") as file:
    data = [int(num) for num in file.readlines()]

minimum = 1_000_000
counter = 0

for element in data:
    if element % 17 == 0:
        minimum = min(minimum, element)

maximum = 0

for i in range(len(data) - 1):
    couple = (data[i], data[i + 1])
    if any(map(lambda x: x % minimum == 0, couple)):
        counter += 1
        maximum = max(maximum, sum(couple))

print(counter, maximum)