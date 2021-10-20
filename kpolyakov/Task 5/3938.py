def F(n):
    num = bin(n)[2:]
    num += str(sum(map(int, num)) % 2)
    if (bin(n)[2:].count('1') > bin(n)[2:].count('0')):
        num += '0'
    else:
        num += '1'
    return int(num, 2)

counter = 0
for i in range(1, 10000):
    if (50 <= F(i) <= 80):
        counter += 1

print(counter)