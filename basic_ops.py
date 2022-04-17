from math import e, factorial

def prime(n):
    
    '''checks if the input n is greater than 1, takes the range from 2 to the input applies the divides
    function to every list element, then sums the output list and checks if it is equal to zero;
    if the sum is equal to zero and the input is greater than 1 the input is prime and returns True.
    If either condition is not met it returns False.'''
    
    if n > 1 and sum(map(n), range(2,n)) == 0:

        return True

    return False

def inverse(n):
    
        '''returns inverse of n'''
        
        return (1/n)
    
def add(x,y):
    
        '''takes two numbers and returns sum'''
        
        return (x+y)
    
def mysum(inlist):
    
        '''takes a list, returns it's sum'''
        
        return reduce(add, inlist)
    
def e_val(n):
    
        '''returns approximate value of e'''
        
        value= map(factorial, range(0,n+1))
        
        return mysum(map(inverse, value))
    
def error(n):
    
        '''returns absolute value of difference between 'actual' and approximation of e'''
        
        return abs(e(n)-e) 
