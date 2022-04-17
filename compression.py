'''
Created on Thursday March 12th 2020
@author:   ccalder
Pledge:    I pledge my honor I have abided by the Stevens Honor System. -Cameron Calder

CS115 - Hw 6

Comment 1: Despite being a 64 bit input the algorithm can go up to 2^8, or 128.

Comment 2: Professor Lai's functions can't exist because if there is no fixed input
the output will not always be shorter.

Comment 3: Three tests were done using a binary image of the letter C, a peace sign,
and a cat with the following compression ratios achieved:

Letter C- 1.875
Peace sign- 3.2142857142857144
Cat- 1.309523809238095
'''

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#Compress------------------------------------------------------------------

def compress(S):
    
    '''Takes a binary string of length 64 as input and outputs another
    binary string of the run-length encoding of the input string.'''
    
    def compressH(S, h):
        
        ''''First compress helper function takes an input of a binary
        string and outputs a list of the consecutive integers in S'''
        
        if S == '':
           return [h]
       
        if S[0] != h[0] and h[1] != 0:
            return [h] + compressH(S[1:], [S[0]] + [1])
        
        return compressH(S[1:], [S[0]] + [h[1] + 1])

    def compressHH(L):
        
        '''Second compression helper function adjusts the input list so
        it is not larger than the indicated maximum run length and
        outputs adjusted list.'''
        
        if L == []:
            return ''
        
        if len(L[0]) > MAX_RUN_LENGTH:
            L[0] = len(L[0]) - MAX_RUN_LENGTH
            
            return [MAX_RUN_LENGTH, 0] + compressHH(L)
        
        return lenAdjust(numToBinary(L[0][1])) + compressHH(L[1:])

    return ('0'*COMPRESSED_BLOCK_SIZE if S[0] == '1' else '') + compressHH(compressH(S, ['0', 0]))

#Uncompress----------------------------------------------------------------

def uncompress(C):
    
    '''Inverts/undoes compressing done by previous compress function.'''

    def uncompressH(C):
        
        '''Take the characters of the compressed number in compressed block size
        chunks.'''
        
        if C == '':
            return []
        
        return [binaryToNum(C[0:COMPRESSED_BLOCK_SIZE])] + uncompressH(C[COMPRESSED_BLOCK_SIZE:])

    def uncompressHH(L, zero):
        
        '''Takes input list and converts the list into that amount of 1's and 0's.'''
        
        if L == []:
            return ''
        
        return ('0' if zero else '1') * L[0] + uncompressHH(L[1:], not zero)
    
    return uncompressHH(uncompressH(C), True)

#Compression-----------------------------------------------------------------
            
def compression(S):
    
    '''Returns ratio of the compressed size to original size of image S.'''

    return len(compress(S)) / len(S)

#Helper Functions--------------------------------------------------------------

def lenAdjust(S):
    
    '''Adjusts length of binary string to be k=5.'''
    
    return '0' * (5- len(S)) + S

def numToBinary(n):
    
    '''Reused from lab 6. Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    
    if n == 0:
        return ''
    
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    
    return numToBinary(n//2) + '0'

def isOdd(n):
    
    '''Reused from lab 6. Returns whether or not the integer argument is odd.'''
    
    if n == '':
        return ''
    
    if n % 2 == 0:
        return False
    
    return True

def binaryToNum(S):
    
    '''Reused from lab 6. Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    
    if S == '':
        return 0
    
    return binaryToNum(S[:-1])*2 + int(S[-1])

#Tests----------------------------------------------------------------------------

#Letter C
print(compression('00011000'+'00100100'+'00100000'+'00100100'+'00011000'))

#Peace sign
print(compression('0011100'+'0101010'+'1001001'+'1010101'+'0110110'+'0011100'))

#Cat
print(compression('0100010'+'1100011'+'1111111'+'1111111'+'0111110'+'0000000'))





               

