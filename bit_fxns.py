'''
Created on Thursday March 24th 2020
@author:   ccalder
Pledge:    I pledge my honor I have abided by the Stevens Honor System. -Cameron Calder

CS115 - Hw 7
'''

def numToBaseB(N,B):
    
    '''Takes input of non-negative interger
    N and base B, where B is between 2 and
    10 inclusive,  and outputs a string
    representing number N in base B.'''

    if N == 0:
        return '0'
    
    return helpernumToBaseB(N,B)

def helpernumToBaseB(N,B):
    
    '''Helper function to do numToBaseB if N is not 0.'''
    
    if N == 0:
        return ''
    
    return helpernumToBaseB(N//B,B) + str(N%B)

print(numToBaseB(4,2)) #100
print(numToBaseB(0,2)) #0
print(numToBaseB(0,4)) #0
print(numToBaseB(4,3)) #11

def BaseBToNum(S,B):
    
    '''Takes input of string S and base B
    where S is a number in base B and B is
    between 2 and 10 inclusive and outputs
    the value of S in base B.'''
    
    if S == '':
        return 0
    
    return BaseBToNum(S[0:-1],B)*B + int(S[-1])

print(BaseBToNum('11',2)) #3
print(BaseBToNum('11',3)) #4
print(BaseBToNum('11',10)) #11
print(BaseBToNum('',10)) #0

def baseToBase(B1, B2, SinB1):
    
    '''Takes inputs base B1, base B2, both between
    2 and 10 inclusive, and string SinB1, representing
    a number in base B1. Outputs a string representing
    the same number in base B2.'''
    
    x = BaseBToNum(SinB1, B1)
    
    return numToBaseB(x, B2)

print(baseToBase(2,10,'11')) #3
print(baseToBase(10,2,'3')) #11
print(baseToBase(3,5,'11')) #4

def add(S,T):
    
    '''Takes input of two binary strings S and T
    and outputs their sum in binary.'''
    
    x = BaseBToNum(S,2)
    y = BaseBToNum(T,2)
    
    return numToBaseB(x+y,2)

print(add('11','01')) #100
print(add('011','100')) #111
print(add('110','011')) #1001

def addB(S,T):
    
    '''Takes two strings S and T as input
    representing binary numbers, with the rightmost
    bit of the string being least significant.
    Outputs a new string representing the sum
    of the input strings.'''
    
    if S == '':
        return T
    
    if T == '':
        return S

    if len(S) > len(T):
        
        T = lenAdjust(T,len(S))
        
    S = lenAdjust(S, len(T))

    def helperaddB(S,T,carryBit):
        
        '''Helper function for addB to check if carry is 1
        or 0 and carry it from one call to the next.'''
        
        sumBit, carryBit = FullAdder[S[-1],T[-1],carryIn(S[-1],T[-1])]
        
        if S == '':
          sumBit, carryBit = helperaddB(S[-1],T[-1],carryBit)
          
        if carryBit == '1':
            return carryBit + sumBit
        
        elif carryBit == '0':
            return sumBit
        
        return ''

    return helperaddB(S,T,'0')

def carryIn(A,B):
    
    '''Helper for addB. Takes input of two binary number
    strings A and B and outputs the carry of their addition.'''
    
    if A or B == '' or '0':
        
        return '0'
    
    return '1'

def lenAdjust(S,k):
    
    '''addB helper function to adjust string lengths to match.'''
    
    return '0'*(k-len(S))+S

#Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = {
('0','0','0'):('0','0'),
('0','0','1'):('1','0'),
('0','1','0'):('1','0'),
('0','1','1'):('0','1'),
('1','0','0'):('1','0'),
('1','0','1'):('0','1'),
('1','1','0'):('0','1'),
('1','1','1'):('1','1'),
}

#to get two elements out of a tuple,
#sumBit, carryBit = FullAdder[('0','0','1')]

print(addB('11','1')) #100
print(addB('011','100')) #111


'''
Created on Thursday March 12th 2020
@author:   ccalder
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 7
'''

# lab exercise: circuits in Python 

# Study the comments and code provided,
# before doing the exercises.


# Logic gates; should only be applied
# to "bits", i.e., either 0 and 1

def gnot(x):
    
    assert x in [0,1]
    
    return int(not(x)) 

def gand(x,y):
    
    assert x in [0,1] and y in [0,1]
    
    return x and y

def gor(x,y):
    
    assert x in [0,1] and y in [0,1]
    
    return x or y

# Example: XOR
# Definition x y | x xor y
#            0 0 | 0
#            0 1 | 1
#            1 0 | 1
#            1 1 | 0
# Here is an expression for the 1-rows, using ! for not
#   !xy + x!y 
# Here is code using only the logic gate functions:
    
def XOR(x,y):
    
    return gor( gand(gnot(x),y), gand(x,gnot(y)) )

def testXOR():
    
    assert XOR(0,0) == 0
    assert XOR(0,1) == 1
    assert XOR(1,0) == 1
    assert XOR(1,1) == 0
    
    print("testXOR success")


# EXERCISE
# Define this function as a single return using
# only the logic gate functions.

def gor3(x,y,z):
    
    '''Or of three inputs.'''

    assert x in [0,1] and y in [0,1] and z in [0,1]
    
    return x or y or z


# EXERCISE
# Full adder.  See Lecture 6 slide 10
# Implement this as a single return, using only
# the logical gate functions. 
# You may also use gor3 or similar helper functions
# that you write using just gates.
# And you may use assigned-once variables:
# think of those as named wires.

def FA(x,y,cin):
    
    '''Assume x, y, and cin are bits.
    Return the pair of bits (carry_out,sum) such that
    sum is the low bit of x+y+cin and carry_out is
    the high bit of x+y+carry_in.'''

    assert x in [0,1] and y in [0,1] and cin in [0,1]
    
    return (carry_out(x,y,cin), lowSum(x,y,cin))

def carry_out(x,y,cin):
    
    '''High bit of x+y+carry_in'''
    
    return gor(gand(x,y), gand(cin,gor(x,y)))

def lowSum(x,y,cin):
    
    '''Low bit of x+y+cin'''
    
    return XOR(XOR(x,y), cin)
            
def FAtest(x,y,c):
    
    '''Compute FA using integer arithmetic.'''
    
    s = (x+y+c) % 2
    d = 1 if x+y+c >= 2 else 0
    
    return (d,s)

def testFA():
    
    assert FA(0,0,0) == FAtest(0,0,0) 
    assert FA(0,1,0) == FAtest(0,1,0) 
    assert FA(1,1,1) == FAtest(1,1,1)
    
    print("testFA successful on 3 out of 8 cases")


# Review slide 12 of Lecture 6 ("A Circuit for Adding") before continuing.

def twoBitAdd(xx,yy):
    
    '''Assume xx and yy are pairs (xt,xo) and (yt,yo) of bits.
    Return (cout,(zt,zo)) where (zt,zo) is their two-bit sum
    is the carry bit. Note: xo is the one's place and xt is
    the two's place.  ALERT: use the notation xx[0] to refer to xt,
    and xx[1] to refer to xo.'''
    
    (c,zo) = FA(xx[1],yy[1],0)
    (d,zt) = FA(xx[0],yy[0],c)
    
    return (d,(zt,zo))

# Notice the assignments to two variables at once,
# which only works if the right-hand side evaluates to a pair.

def test_twoBitAdd():
    
    zero = (0,0)
    one = (0,1)
    two = (1,0)
    three = (1,1)
    
    c,ww = twoBitAdd(one,zero)
    assert( ww == one and c == 0 )
    
    c,ww = twoBitAdd(one,one)
    assert( ww == two and c == 0 )
    
    c,ww = twoBitAdd(three,three)
    assert( ww == two and c == 1 )
    
    print("test_twoBitAdd worked (but incomplete test)")


# EXERCISE: implement the following, using gates and/or FA.
# Hint: you might start by defining something like twoBitAdd
# but that also has a carry input.

def fourBitAdd(xxxx,yyyy):
    
    '''Assume xxxx is a quadruple (xe,xf,xt,xo) of four bits,
    with xe the high-order bit (i.e., eight's place).  Likewise
    yyyy.  Return (c,zzzz) where zzzz is their four-bit sum
    and c is the carry.'''

    (c, ze) = FA(xxxx[3], yyyy[3], 0)
    (c, zf) = FA(xxxx[2], yyyy[2], c)
    (c, zt) = FA(xxxx[1], yyyy[1], c)
    (c, z0) = FA(xxxx[0], yyyy[0], c)
    
    return (c, (z0, zt, zf, ze))

# EXERCISE: implement the following.

def test_fourBitAdd():
    
    '''at least four test cases'''
    
    zero = (0,0,0,0)
    one = (0,0,0,1)
    two = (0,0,1,0)
    ten = (1,0,1,0)
    
    c, ww = fourBitAdd(one, zero)
    assert(ww == (0,0,1,0) and c == 0)
    
    c, ww = fourBitAdd(one, one)
    assert(ww == (0,0,1,0) and c == 0)
    
    c, ww = fourBitAdd(two, two)
    assert(ww == (0,1,0,0) and c == 0)
    
    c, ww = fourBitAdd(ten, ten)
    assert(ww == (0,1,0,0) and c == 1)
    
    print("test_fourBitAdd worked (but incomplete test)")
    

    
