file = open('kpolyakov/Task 26/26-44.txt')
data = sorted([int(num) for num in file])

data = [[element, (element - 1) // 500] for element in data]
maximum = max([element[1] for element in data])
category = [[] for i in range(maximum + 1)]

for element in data:
    category[element[1]].append(element[0])

sale = []

for element in category:
    new_element = []
    flag = 1
    for i in range(len(element)):
        num = max(element)
        if flag == -1: num = min(element) 
        new_element.append(num)
        del element[element.index(num)]
        flag = -flag
    for i in range(1, len(new_element), 2):
        sale.append(new_element[i] / 2)
        
print(int(sum(sale)), int(max(sale)))
        
