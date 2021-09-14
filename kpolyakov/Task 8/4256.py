import itertools

a = list(itertools.permutations("КУСАТЬ", r=5))
counter = 0

for x in a:
    s = ''.join(x)
    if (s[0]!='Ь') and ('СУК' not in s):
        counter+=1

print(counter)