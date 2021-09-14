import itertools

a = list(itertools.product("ТИМОФЕЙ", repeat = 5))
counter = 0
for x in a:
    if (x.count('Т') >= 1) and (x.count('Й') <= 1):
        counter += 1
print(counter)