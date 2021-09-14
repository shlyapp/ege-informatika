import itertools as it

# обратить внимание на алфавитный порядок
a = list(it.product("АВДПР", repeat = 4))
for i in range(len(a)):
    if (a[i].count("A") == 0 and a[i].count("П") == 1 and a[i].count("Р") == 1 and a[i].count("В") == 1 and a[i].count("Д") == 1):
        print(i+1)
        break