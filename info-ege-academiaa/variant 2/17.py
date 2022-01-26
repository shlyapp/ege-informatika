file = open("info-ege-academiaa/variant 2/17.txt")
data = list(map(int, file.readlines()))

counter = 0
summa = 0

def convert_to_7(num):
    ans = ''
    while num > 0:
        ans = str(num % 7) + ans
        num //= 7
    return ans

for element in data:
    if hex(element)[-1] == 'e' and oct(element)[-1] == convert_to_7(element)[-1]:
        summa += element
        counter += 1

print(summa, counter)