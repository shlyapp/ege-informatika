def is_simple(num):
    counter = 0
    for x in range(2, num):
        if num % x == 0:
            counter += 1
    if counter > 0:
        return False
    return True

def search_divisors(num):
    divisors = []
    for x in range(2, num):
        if num % x == 0:
            divisors.append(x)
    return divisors

def simple_divisors(num):
    div = []
    for x in search_divisors(num):
        if is_simple(x):
            div.append(x)
    return div

for i in range(33333, 55556):
    try:
        if i % sum(simple_divisors(i)) == 0 and sum(simple_divisors(i)) > 250:
            print(i, sum(simple_divisors(i)))
    except:
        pass
