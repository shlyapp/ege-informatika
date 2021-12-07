file = open('kpolyakov/Task 17/17-3.txt')
data = [int(x) for x in file]

counter = 0
maximum = 0

for i in range(len(data) // 4 * 4 - 2):
    parity = (list(map(lambda x: str(x % 2), data[i:i+4])))
    if (parity == ['0', '1', '0', '1']) or (parity == ['1', '0', '1', '0']):
        maximum = max(maximum, sum(data[i:i+4]))
        counter += 1

print(counter, maximum)

