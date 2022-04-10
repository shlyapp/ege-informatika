V = 30 * 1024 * 1024 * 8
u1 = 2**22
u2 = 2**19
time = V/u1 + V/u2
all_time = 18 * 60
print((all_time - time) / 60)
