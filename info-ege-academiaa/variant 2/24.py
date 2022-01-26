s = open("info-ege-academiaa/variant 2/24.txt").read()

maximum = 0
counter = 0

for char in s:
    if (char == 'C'):
        counter += 1
    else:
        maximum = max(maximum, counter)
        counter = 0

print(maximum)