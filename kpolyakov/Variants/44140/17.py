def convert(num, base):
    answer = ''
    while num > 0:
        answer = str(num % base) + answer
        num = num // 2
    return answer


file = open('kpolyakov/Variants/44140/17.txt')
data = [int(num) for num in file]
counter = 0
maximum = float('-inf')

for element in data:
    if sum(map(int, str(element))) % 5 == 0 and convert(element, 3)[-2:] != '00':
        counter += 1
        maximum = max(maximum, element)

print(counter, maximum)
