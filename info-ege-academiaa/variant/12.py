s = '8' * 156

while '77' in s or '888' in s:
    if ('77' in s):
        s = s.replace('77', '88', 1)
    else:
        s = s.replace('888', '7', 1)

print(s)