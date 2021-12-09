file = open("kpolyakov/Task 17/17-243.txt")
data = [int(x) for x in file]

summa = 0
counter = 0
minimum = 100000

for element in data:
    if (element % 35 == 0):
        summa += sum(map(int, str(element)))

for i in range(len(data) - 1):
    part = [data[i], data[i + 1]]
    a = list(map(lambda x: x > summa, part)) 
    b = list(map(lambda x: x % 16 == 15 and x // 16 % 16 == 14, part))
    if (a == [True, False] and b == [False, True]) or (b == [True, False] and a == [False, True]):
        counter += 1
        minimum = min(minimum, data[i + 1] + data[i])

print(counter, minimum)

