n = 20001
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0    
print(len(list(filter(lambda x: x != 0, numbers))))