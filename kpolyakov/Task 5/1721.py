def F(a):
    nums = list(map(int, str(a)))
    return max(nums) - min(nums)

counter = 0
for i in range(100, 1000):
    if (F(i)==58): counter +=1

print(counter)