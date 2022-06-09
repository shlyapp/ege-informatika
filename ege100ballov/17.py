with open('ege100ballov/17.txt') as file:
    data = [int(num) for num in file]
    counter = 0
    maximum = float('-inf')
    for i in range(len(data) - 1):
        couple = (data[i], data[i + 1])
        if any(num % 3 == 0 for num in couple):
            counter += 1
            maximum = max(maximum, sum(couple))

print(counter, maximum)
