print("c a d b")

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a and b) == (not c)) and (b <= d):
                    print(c, a, d, b)

# удобно после нахождения одной буквы менять порядок вывода так, чтобы она стояла на своем месте
# cadb