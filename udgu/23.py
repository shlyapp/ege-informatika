def find_simple_del(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return (list(filter(lambda x: x != 0, numbers)))


mass = find_simple_del(5_000_000)

MaxD = 0  # макс кол-во делителей
for i in range(20000, 1, -1):
    k = 0  # текущ счетчик делителей
    for j in range(len(mass)):
        if i % mass[j] == 0:
            k += 1
    if k >= MaxD:
        MaxD = k
        x = i
print(x, MaxD)
