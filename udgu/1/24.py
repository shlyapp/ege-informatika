F = open('udgu/26.txt')

N, S = map(int, F.readline().split())

a = []
b = []
for i in range(N):
    x = int(F.readline())
    if 180 <= x <= 200:
        a.append(x)
    else:
        b.append(x)

a.sort(reverse=True)
b.sort(reverse=True)

firstTotal = 0
firstCount = 0
for x in a:
    if firstTotal + x <= S:
        firstTotal += x
        firstCount += 1

extraS = S - firstTotal
extraTotal = 0
extraCount = 0
for x in b[::-1]:
    if extraTotal + x <= extraS:
        extraTotal += x
        extraCount += 1

remains = extraCount
extraTotal = 0
i = 0
while remains > 0:
    minPossible = extraTotal + b[i]
    if remains > 1:
        minPossible += sum(b[-(remains-1):])
    if minPossible <= extraS:
        remains -= 1
        extraTotal += b[i]
    i += 1

#print( firstCount, firstTotal )
#print( extraCount, extraTotal )

print(firstCount + extraCount, firstTotal + extraTotal)
