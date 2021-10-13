
def F(a):
    nums = list(map(int, str(a)))
    return max(nums) - min(nums)


counter = 0
for i in range(800, 901):
    if (F(i)==3): counter +=1

print(counter)