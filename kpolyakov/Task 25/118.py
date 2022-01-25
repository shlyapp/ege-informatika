def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def div(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return sorted(d)

counter = 0
minim = 345293

for x in range(158_928, 345_293 + 1):
    d = [i for i in div(x) if is_simple(i)]
    if len(d) == 3 and d[0]*d[1]*d[2] == x:
        counter += 1
        minim = min(minim, x)

print(counter, minim)    
