with open('udgu/2/24.txt') as file:
    line = file.readline()

counter = 0

for i in range(len(line)-4):
    word = line[i:i+5]
    if word == word[::-1]:
        counter += 1

print(counter)
