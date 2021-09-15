import itertools

a = set(list(itertools.product('КАНКАН', repeat=6)))
counter = 0

for x in a:
    s = ''.join(x)
    count = 0
    for letter in s:
        s1 = ''.join(letter)
        if (s1 != 'А'):
            count+=1
    if (count>=3):
        counter +=1

print(counter)