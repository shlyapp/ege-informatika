

def F(start, end, counter = 0):
    if (start > end or start < 0 or counter > 30):
        return 0
    elif (start == end and counter == 30):
        return 1
    return F(start + 5, end, counter + 1) + F(start - 3, end, counter + 1)

counter = 0
for i in range(-10000, 10000):
    if (F(4, i) != 0):
        counter += 1

print(counter)