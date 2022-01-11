def is_simple(num):
    return len([x for x in range(2, num) if num % x == 0]) == 0

for i in range(33333, 55556):
    if sum(map(int, str(i))) > 35 and is_simple(i):
        print(i, sum(map(int, str(i))))