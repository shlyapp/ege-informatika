file = open("info-ege-academiaa/variant/18.csv")
data = []

for s in file:
    data.append(float(''.join(str(x) for x in map(str, s[:-1])).replace(',', '.')))

maximum = 0
var = []
a = set()
for i in range(1, len(data)):
    if (data[i] < data[i-1]):
        a.add(data[i])
        a.add(data[i-1])
    else:
        var.append(list(a))
        a.clear()

for element in var:
    maximum = max(sum(element), maximum)

print(maximum)

    
