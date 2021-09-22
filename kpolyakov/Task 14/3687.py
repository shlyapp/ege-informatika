num = 123
for sys in range(3, 10):
    s = ''
    x = num
    while x > 0:
        s += str(x%sys)
        x = x//sys
    print(s[::-1], sys)

# answer 16 (146 - 9 sys and 234 - 7 sys)
