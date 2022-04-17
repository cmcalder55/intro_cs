
def mult(c,n):
    
    '''Uses a loop and addition to return the product of c times n without
    multiplication.'''
    
    result = 0
    
    for x in range(n):
        
        result = result + c
        
    return result

def update(c,n):
    
    '''Starts with z=0 and repeatedly updates the value of z using the
    assignment z = z**2 + c, n times. Outputs final value of z.'''
    
    z = 0
    
    for x in range(n):
        
        z = z**2 + c
        
    return z

def inMSet(c,n):
    
    '''Takes input of complex number c and integer n and returns True
    if the complex number c is in the Mandelbrot set and False if not.'''

    z = 0
    
    for x in range(n):
        
        z = z**2 + c
        
        if abs(z) > 2:
            
            return False
        
    return True

if __name__ == '__main__':   
    
    '''Test cases'''
    
    # mult
    
    print(mult(6,7))        # 42
    print(mult(1.5,28))     # 42.0
    
    # update
    
    print(update(1,3))      # 5
    print(update(-1,3))     # -1
    print(update(1,10))     # 379186231026592608286823502802789327...325352026
                        
    print(update(-1,10))    # 0
    
    # inMset
    
    c = 0 + 0j
    print(inMSet(c,25))     # True
    
    c = 3 + 4j
    print(inMSet(c,25))     # False
    
    c = 0.3 + -0.5j
    print(inMSet(c,25))     # True
    
    c = -0.7 + 0.3j
    print(inMSet(c,25))     # False
    
    c = .42 + .2j
    print(inMSet(c,25))     # True
    print(inMSet(c,50))     # False
