def Convert(num, base):
    num_convert = ''
    while num:
        num_convert = str(num % base) + num_convert
        num //= base
    return num_convert

file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]
counter = 0
minimum = max(data)

for element in data:
    if (Convert(element, 3)[-1] == Convert(element, 5)[-1]) and (element % 31 == 0 or element % 47 == 0 or element % 53 == 0):
        counter += 1
        minimum = min(minimum, element)

print(counter, minimum)