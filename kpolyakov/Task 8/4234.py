import itertools

a = list(itertools.product("012345", repeat=5))
forbiddens = list(itertools.product('024', repeat=2)) + list(itertools.product('135', repeat=2))
counter = 0

for x in a:
    s = ''.join(x)
    if (s[0] != '0'):
        for forbidden in forbiddens:
            s1 = ''.join(forbidden)
            if s1 in s:
                break
        else:
            counter+=1

print(counter)