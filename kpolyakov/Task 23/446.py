def F(start, end, acc=[],res=[]):
    if (start > end):
        return []
    elif (start == end):
        return res+[acc]
    return F(start + 1, end, acc+[1],res) + F(start * 2, end, acc+[3], res)

counter = 0

for element in F(4, 24):
    if (element[-2] == 1):
        counter += 1

print(counter)

