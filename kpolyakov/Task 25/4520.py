def search_divisors(n):
    q = round(n**0.5)
    divs = [q] if n % q == 0 else []
    for d in range(2,q):
        if n % d == 0:
            divs += [d, n//d]
    return sorted(divs)

min = 200000000
counter = 0 
num = min + 1

while counter < 5:
    div = search_divisors(num)
    if len(div) >= 5:
        num1 = div[0]*div[1]*div[2]*div[3]*div[4]
        if num1 < num and num1%10==1: 
            counter += 1
            print(num1, div[4])
    num += 1




