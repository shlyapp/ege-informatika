from functools import lru_cache

@lru_cache

def F(start, stop, counter = 0):
    if (start > stop):
        return 0
    elif (start == stop and counter <= 4):
        return 1
    return F(start + 1, stop, counter + 1) + F(start + 2, stop, counter + 1)

counter = 0
for i in range(2, 1000):
    if (F(2, i) == 0):
        break
    counter += 1

print(counter)