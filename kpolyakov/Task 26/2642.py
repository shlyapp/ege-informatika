#100 30 10

file = open('kpolyakov/Task 26/26-k5.txt')
data = sorted([int(x) for x in file])

rich = data[90:100]
bich = data[0:30]

print(rich[0], sum(bich) // len(bich)) 
