import itertools

a = list(itertools.product('БЕЛКА', repeat = 4))
counter = 0

for element in a:
    element = ''.join(element)
    if (element.count('Б')==1):
        counter +=1

print(counter) 
