def F(nums):
    a, b = nums
    a = str(a)
    b = str(b)
    ans = list([int(int(a[0]) + int(b[0])), int(int(a[1]) +
               int(b[1])), int(int(a[2]) + int(b[2]))])
    ans.sort()
    str1 = ''
    for element in ans:
        str1 += str(element)
    return str1


for i in range(100, 1000):
    if F((365, i)) == '51014':
        print(i)
