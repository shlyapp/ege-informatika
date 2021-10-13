
def F(a):
    nums = list(map(int, str(a)))
    return max(nums) - min(nums)


counter = 0
for i in range(900, 999):
    if (F(i)==7): counter +=1

print(counter)