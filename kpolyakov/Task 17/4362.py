file = open("kpolyakov/Task 17/17-9.txt")
data = [int(x) for x in file]

counter = 0
maximum = 0

for i in range(len(data) // 3 * 3):
    if list(map(lambda x: bin(x)[2:].count('1') >= 3 and bin(x)[2:].count('0') >= 1, [data[x] for x in range(i, i + 3)])).count(True) >= 2:
        counter += 1
        maximum = max(maximum, max([data[x] for x in range(i, i + 3)]))
    
print(counter, maximum)

