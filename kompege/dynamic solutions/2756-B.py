file = open('kompege/files/27A-2756.txt')
N = int(file.readline())
m_12 = [0] * 12
maximum = float('-inf')

for i in range(N):
    num = int(file.readline())
    ost = float('-inf')
    if num % 12 != 0 and num % 100 < 12:
        ost = 12 - num % 100
    if num % 100 == 12: ost = 0
    
    maximum = max(m_12[ost] + num, maximum)

    m_12[num % 100 if num % 100 < 12] = max(m[num % 100])
    

print(maximum)