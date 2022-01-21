file = open('kpolyakov/Task 26/26-j1.txt')
data = [int(x) for x in file]
money = [data.count(i) for i in range(1, 100)]
couple = sum([min(money[i], money[98-i]) for i in range(99)])
print(couple // 2)
