import itertools

a = list(itertools.permutations("ГЕЛИЙ", r=5))
forbidden = 'ИЕЙ'
counter = 0

for x in a:
    s = ''.join(x)
    if (s[0]!='Й') and (forbidden not in s):
        counter += 1

print(counter)