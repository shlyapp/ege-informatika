import itertools

a = list(itertools.product('ДКМО', repeat=5))

for index, word in enumerate(a):
    word = ''.join(word)
    if (word == 'ДОМОК' or word == 'КОМОД'):
        print(index, word)
