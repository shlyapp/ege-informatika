x = 0
while True:
    num = str(oct(64**12-8**14+x))[2:]
    if (num.count('7')==12) and (num.count('1')==1):
        print(x)
        break
    x += 1 