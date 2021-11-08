str = open("kpolyakov/Task 24/k7.txt", 'r').read()
maximum = 0
counter = 0
for char in str:
    if (char == 'C'):
        counter += 1
    else:
        maximum = max(maximum, counter)
        counter = 0

print(maximum)