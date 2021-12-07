file = open("kpolyakov/Task 17/17-10.txt")
data = [int(x) for x in file]

counter = 0
minimum = 10000

for i in range(len(data) - 1):
    num = str(data[i] + data[i + 1])
    if len(num) == 3 and num[-1] > num[-2]:
        counter += 1
        minimum = min(minimum, int(num))

print(counter, minimum)