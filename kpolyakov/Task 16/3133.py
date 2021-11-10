nums = []

def F(n):
    nums.append(n + 1)
    if (n > 1):
        nums.append(n + 5)
        F(n - 1)
        F(n - 2)

for i in range(1, 10000):
    nums.clear()
    F(i)
    if (sum(nums) > 1000000):
        print(i, sum(nums))
        break
