counter = 0
maximum = 0

for i in range(1388, 63253):
    num = str(i)
    if i % 12 != 0 and (num.count('7') + num.count('4')) >= 1:
        counter += 1
        maximum = max(i, maximum)

print(counter, maximum)
