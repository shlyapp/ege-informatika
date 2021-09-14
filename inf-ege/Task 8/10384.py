import itertools

a = list(itertools.product("ABCDX", repeat = 4))
counter = 0
for x in a:
    if ((x[0]=='X' and x.count('X')==1) or ('X' not in x)):
        counter += 1

print(counter)
