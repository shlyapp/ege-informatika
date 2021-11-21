file = open("info-ege-academiaa/variant/17.txt")
data = list(map(int, file.readlines()))

divisors = (7, 13, 17, 19)
counter = 0
suma = 0

for element in data:
    if sum(map(lambda x: element % x == 0, divisors)) == 2:
        counter += 1
        suma += element

print(counter, suma)
