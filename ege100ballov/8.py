from itertools import product as pr

from numpy import iterable

words = ['0'] + list(pr('ЕЛМРУ', repeat=4))

for i in range(len(words)):
    word = ''.join(words[i])
    if word[0] == 'Л':
        print(i, word)
        break
