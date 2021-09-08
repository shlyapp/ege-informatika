for A in range(1, 100000):
    flag = True
    for x in range(1, 100000):
        if ( ( ( (x%A==0) and (x%45==0) ) <= (x%162==0) ) and (A > 200) ) == 0:
            flag = False
            break
    if (flag):
        print(A)
        break
        
        