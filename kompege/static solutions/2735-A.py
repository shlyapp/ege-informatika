import itertools

with open('kompege/files/27A-2735.txt') as file:
    N = int(file.readline())
    data = [list(map(int, points.split())) for points in file.readlines()]

counter = 0

for points in itertools.combinations(data, 3):
    if1 = list(map(lambda x: str(int(x[0] == 0)), points))
    if2 = list(map(lambda x: str(int(x[1] == 0)), points))
    if3 = list(map(lambda x: str(int(x[0] != 0 and x[1] != 0)), points))
    ans = list(map(lambda x: int(x[0]) +
               int(x[1]) + int(x[2]), [if1]+[if2]+[if3]))
    if ans == [1, 1, 1]:
        counter += 1

print(counter)
