summa = 0
minim = 1178

for n in range(10, 1179):
    if (n % 10 != 0) and (n % 10 != 2) and (n % 10 != 6) and (n % 10 != 8) and (n % 100 != 14):
        summa += n
        minim = min(minim, n)

print(summa, minim)
