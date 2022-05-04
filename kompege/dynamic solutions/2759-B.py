file = open('kompege/files/27B-2759.txt')
N = int(file.readline())
counter = 0
m = [0] * 134

for i in range(N):
    num = int(file.readline())
    if num < 134:
        for j in range(num + 1, 134):
            if num + j <= 134: counter += m[j]
    
        m[num] += 1
        

print(counter)