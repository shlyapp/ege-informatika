with open('kpolyakov/Task 27/27-36a.txt') as file:
    N = int(file.readline())
    data = [list(map(int, file.readline().split())) for i in range(N)]
    
from itertools import *
from math import *

for i in range(N):
    NOD = []
    for x, y in combinations(data[i], 2):
        NOD.append(gcd(x, y))
    data[i].append(NOD)

counter = 0

for i in range(N)