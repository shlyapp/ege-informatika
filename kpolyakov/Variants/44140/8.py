import itertools

a = list(itertools.product('МЕЧТА', repeat=6))
counter = 0

for word in a:
    word = ''.join(word)
    if word.count('А') >= 3:
        counter += 1
        print(word)

print(counter)
