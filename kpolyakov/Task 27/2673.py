with open('kpolyakov/Task 27/27-13b.txt') as file:
    N = int(file.readline())
    buffer = [int(file.readline()) for i in range(6)]
    counter = 0
    delim = [0] * 14

    for i in range(N - 6):
        num = int(file.readline())
        for j in range(14):
            if (num * j) % 14 == 0:
                counter += delim[j]

        delim[buffer[0] % 14] += 1
        buffer.append(num)
        buffer.pop(0)

print(counter)
