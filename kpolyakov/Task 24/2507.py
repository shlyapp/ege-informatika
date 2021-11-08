str = open("kpolyakov/Task 24/k8.txt").read()
max_char = ''
maximum = 0
counter = 0
for i in range(1, len(str)):
    if (str[i] == str[i-1]):
        counter += 1
    else:
        if (counter > maximum):
            maximum = counter + 1
            max_char = str[i-1]
        counter = 0

print(max_char, maximum, sep='')