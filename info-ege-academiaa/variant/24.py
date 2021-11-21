data = open("info-ege-academiaa/variant/24.txt").readline()

char = ''
counter = 0
maximum = 0

for i in range(1, len(data)):
    if (data[i] == data[i-1]):
        counter += 1
    else:
        if (counter > maximum):
            maximum = counter + 1
            char = data[i - 1]
        counter = 0

print(char, maximum)