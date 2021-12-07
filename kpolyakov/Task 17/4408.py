def Convert(num, base):
    convert = ''
    while num:
        convert = str(num % base) + convert
        num //= base
    return convert

file = open("kpolyakov/Task 17/17-10.txt")
data = [int(x) for x in file]

counter = 0
maximum = 0

for i in range(len(data) - 1):
    if (Convert(data[i] + data[i + 1], 7) == Convert(data[i] + data[i + 1], 7)[::-1]):
        counter += 1
        maximum = max(maximum, data[i] + data[i + 1])

print(counter, Convert(maximum, 7))