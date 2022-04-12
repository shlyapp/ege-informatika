with open('kompege/27B-2726.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

even = []
odd = []

for element in data:
    if element % 2 == 0:
        even += [element]
    else:
        odd += [element]

even.sort()
odd.sort()

print(max([even[-1] + even[-2], even[-1] + odd[-1]]))
