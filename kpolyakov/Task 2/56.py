print('a c b')

for a in range(2):
    for b in range(2):
        for c in range(2):
            if (a and c) or ((not a) and (b or (not c))):
                print(a, c, b)

# cab