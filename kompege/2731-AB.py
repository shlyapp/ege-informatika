with open('kompege/27B-2731.txt') as file:
    N = int(file.readline())
    data = [list(map(int, points.split())) for points in file.readlines()]

x_p = []
ymax = 0

for x, y in data:
    if y == 0:
        x_p += [x]
    else:
        ymax = max(ymax, abs(y))

print(((max(x_p) - min(x_p)) * ymax) / 2)
