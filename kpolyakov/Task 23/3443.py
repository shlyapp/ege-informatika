s=[]
def f(x, y,z): 
    if x>y:
        return 0
    elif x==y:
        s.append(z)
        return 1
    
    elif z<10: 
        f(x * 3, y,z+ 1)  
        f(x + 5, y,z+ 1) 
        f(x + 1, y, z+1) 
      
    

f(1, 227,0)
print(min(s))   
