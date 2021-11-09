from functools import lru_cache
@lru_cache
def f(x, y,z): 
    
    if x>y:
        return 0
    elif x==y:
        print(z)
        return 1
    
    elif x<y: 
        f(x * 3, y,z+ 1)  
        f(x + 5, y,z+ 1) 
        f(x + 1, y, z+1) 
      
f(1, 227,0)
