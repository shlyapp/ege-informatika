def convert(num, base):
    answer = ''
    while num > 0:
        answer = str(num % base) + answer
        num = num // 2
    return answer


for i in range(2, 10):
    for j in range(2, 10):
        if (convert(225, i) == convert(405, j)):
            print('i')
