with open('kompege/files/27B-2735.txt') as file:
    N = int(file.readline())
    data = [list(map(int, points.split())) for points in file.readlines()]

x_p = y_p = p = 0

for point in data:
    if point[0] == 0:
        x_p += 1
    elif point[1] == 0:
        y_p += 1
    else:
        p += 1

print(x_p * y_p * p)
