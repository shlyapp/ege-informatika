def convert(num, base):
    answer = ''
    while num > 0:
        answer = str(num % base) + answer
        num //= base
    return answer


for i in range(10):
    num = int(f'1586{i}6')
    n = convert(num, 7)
    if n == n[::-1]:
        print(num, sum(map(int, str(n))))

for i in range(10000):
    for j in range(10):
        num = int(f'1{i}586{j}6')
        n = convert(num, 7)
        if n == n[::-1]:
            print(num, sum(map(int, str(n))))
