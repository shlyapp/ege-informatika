import itertools

a = list(itertools.product('01234', repeat=5))
counter = 0

for x in a:
    if (x[0]!='0'):
        count = 0
        for letter in x:
            if (int(letter)%2==0):
                count+=1
        if (count <= 3):
            counter+=1

print(counter)
