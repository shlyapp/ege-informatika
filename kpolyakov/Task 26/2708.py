N = 1000
file = open('kpolyakov/Task 26/26-j7.txt')
data = sorted([int(x) for x in file])[::-1]

vklad_rich = 0
vklad_bich = 0
summa_bich = 0

# сумма всех 0.6
# сумма богатых 0.8
# ставка бедных (все - богатые)
# сколько должны скинуть бедные на все

for i in range(200):
    vklad_rich += data[i] * 0.8

for i in range(200, 1000):
    vklad_bich += data[i] * 0.2
    summa_bich += data[i]

print(int(vklad_rich), int(summa_bich / vklad_bich))