#1000001

file = open('kpolyakov/Task 26/26-j2.txt')
data = sorted([int(x) for x in file])

median = data[len(data)//2]
sr = sum(data) / len(data)
counter = 0

for element in data:
    if sr <= element <= median:
        counter += 1

print(counter)

