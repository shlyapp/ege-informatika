file = open('kompege/files/27B-2728.txt')
N = int(file.readline())
max_s = float('-inf')
max_k_23 = [float('-inf'), float('-inf')]
max_n = [float('-inf'), float('-inf')]

for i in range(N):
    num = int(file.readline())
    if num % 23 == 0:
        max_s = max(num + max_n[num % 2], max_s)
    max_s = max(num + max_k_23[num % 2], max_s)

    max_n[num % 2] = max(max_n[num % 2], num)
    if num % 23 == 0:
        max_k_23[num % 2] = max(max_k_23[num % 2], num)

print(max_s)
