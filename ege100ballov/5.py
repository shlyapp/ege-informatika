def F(num):
    n = list(map(int, str(num)))
    sums = [n[0] + n[1], n[1] + n[2], n[2] + n[3]]
    sums.sort()
    return sums


def convert_to_6(num):
    n = ''
    while num > 0:
        n = str(num % 6) + n
        num //= 6
    return n


for num in range(1, 100000):
    n = convert_to_6(num)
    if len(n) == 4:
        if F(n) == [2, 5, 9]:
            print(num)
            break
