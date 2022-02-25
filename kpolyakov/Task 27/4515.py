def is_prime(num):
    return all(num % d != 0 for d in range(2, round(num ** 0.5) + 1))

with open('kpolyakov/Task 27/27-82a.txt') as file:
    N = int(file.readline())
    data = [int(file.readline()) for i in range(N)]

K = 9
tail_sum = [0] + [None] * (K - 1)
total_sum = 0
sum_max = 0
prime_counter = 0

for i in range(0, N):
    num = data[i]
    total_sum += num
    if is_prime(num):
        prime_counter += 1
    r = prime_counter % K
    if tail_sum[r] is None:
        tail_sum[r] = total_sum
    if prime_counter >= K:
        sum_max = max(sum_max, total_sum - tail_sum[r])

print(sum_max)
    

