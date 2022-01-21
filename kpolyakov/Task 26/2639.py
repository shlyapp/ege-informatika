#1000 50
k = 50
file = open('kpolyakov/Task 26/26-k2.txt')
data = sorted([int(x) for x in file])

new_data = data[k:950]

print(new_data[-1], sum(data) // len(data))