for i in range(10):
    for j in range(10):
        num = int(f'1245{i}6{j}8')
        if num % 17 == 0:
            print(num, num // 17)