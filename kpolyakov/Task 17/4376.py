def is_triangle(sides):
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    return hypotenuse**2 == sides[0]**2 + sides[1]**2


file = open("kpolyakov/Task 17/17-10.txt")
data = [int(x) for x in file]

counter = 0
summa = 0

for i in range(len(data) // 3 * 3 - 1):
    if (is_triangle([data[x] for x in range(i, i + 3)])):
        counter += 1
        summa += max([data[x] for x in range(i, i + 3)])

print(counter, summa)