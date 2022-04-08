import itertools

iterator = 1

for word in itertools.product('АПРСУ', repeat = 5):
    word = ''.join(word)
    if 'АА' not in word and word[0] == 'У':
        print(iterator)
        break
    iterator += 1