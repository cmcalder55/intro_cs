
import sys, random

def createOneRow(width):
    
    ''' Returns one row of zeros of width "width". '''
    
    row = []
    
    for col in range(width):
        
        row += [0]
        
    return row

def createBoard(width, height):
    
    ''' Returns a 2d array with "height" rows and "width" columns. '''
    
    A = []
    
    for row in range(height):
        
        A += [createOneRow(width)]
        
    return A

#test 1

assert createBoard(5,3) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def printBoard(A):
    
    ''' Prints the 2d list-of-lists 'A' without spaces. '''
    
    for row in A:
        
        for col in row:
            
            sys.stdout.write( str(col) )
            
        sys.stdout.write( '\n' )

#test 2

assert createBoard(5,3) == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def diagonalize(width,height):
    
    ''' Creates an empty board and then modifies it so that it has a diagonal 
    strip of "on" cells. '''
    
    A = createBoard( width, height )
    
    for row in range(height):
        
        for col in range(width):
            
            if row == col:
                
                A[row][col] = 1
                
            else:
                
                A[row][col] = 0
                
    return A

#test 3

assert diagonalize(7,6) == [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]]

def innerCells(w,h):
    
    ''' Variation of diagonalize that returns a 2D array of 'live' cells with 
    value 1, except for a one cel border of empty cells with value 0 for the 
    edge of the array. '''

    A = createBoard(w,h)
    
    for row in range(h):
        
        for col in range(w):
            
            if row == 0 or row ==(h-1) or col == 0 or col == (w-1) : 
                
                A[row][col] = 0
                
            else:
                
                A[row][col] = 1
                
    return A

#test 4

assert innerCells(5,5) == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], \
                           [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]

def randomCells(w,h):
    
    ''' Variation of innerCells that returns and array of random 1s and 0s, 
    with the outer edge of the array still value 0. '''

    A = createBoard(w,h)
    
    for row in range(h):
        
        for col in range(w):
            
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                
                A[row][col] = 0
                
            else:
                
                A[row][col] = random.choice([0,1])
                
    return A

## test 5

## Expected output based on instructions.

#printBoard(randomCells(5,5))

## 00000 ##00000 ##00000
## 01110 ##01100 ##01010
## 00110 ##01100 ##00010
## 00000 ##01010 ##01110
## 00000 ##00000 ##00000

def copy(A):
    
    ''' Takes input of a 2D array and outputs a new 2D array with the same 
    pattern as the input. Peforms a deep copy of the second array. '''

    w = len(A[0])
    h = len(A)
    newA = createBoard(w,h)
    
    for row in range(h):
        
        for col in range(w):
            
            newA[row][col] = A[row][col]
            
    return newA

## test 6
## Expected output based on instructions.

#oldA = createBoard(2,2)

#print( printBoard(oldA))

##00
##00

#newA = oldA

#print( printBoard(newA))

##00
##00

#oldA[0][0] = 1

#print(printBoard(oldA))

##10
##00

#print(printBoard(newA))

##10
##00

def innerReverse(A):
    
    ''' Takes input of old 2D array (generation) and outputs a new generation/
    2D array of the same shape and size. '''

    newA = copy(A)
    w = len(A[0])
    h = len(A)
    
    for row in range(h):
        
        for col in range(w):
            
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                
                newA[row][col] = 0
                
            elif A[row][col] == 1:
                
                newA[row][col] = 0
                
            else:
                
                newA[row][col] = 1
                
    return newA

## test 7

## expected output based on instructions- same issue with making
## a test function as randomCells.

#A = randomCells(5,5)

#print( printBoard(A))

##00000
##00110
##00110
##01100
##00000

#A2 = innerReverse(A)

#print( printBoard(A2))

##00000
##01000
##01000
##00010
##00000

def countNeighbors(row,col,A):
    
    ''' Helper for next_life_generation that returns the number of live 
    neighbors in the board A at the given row and column. '''
    
    result = 0
    
    if A[row][col-1] == 1:
        result += 1
        
    if A[row][col+1] == 1: 
        result += 1
        
    if A[row-1][col] == 1:
        result += 1
        
    if A[row+1][col] == 1:
        result += 1
        
    if A[row+1][col+1] == 1:
        result += 1
        
    if A[row-1][col-1] == 1:
        result += 1
        
    if A[row+1][col-1] == 1:
        result += 1
        
    if A[row-1][col+1] == 1:
        result += 1
        
    return result


def next_life_generation(A):

    ''' Makes a copy of A and then advanced one generation of Conway's 
    Game of Life within the *inner cells* of that copy. The outer edge 
    always stays 0. '''

    newA = copy(A)
    w = len(A[0])
    h = len(A)
    
    for row in range(1, h-1):
        
        for col in range(1, w-1):
            
            if countNeighbors(row, col, A) <2 or countNeighbors(row, col, A) >3:
                
                newA[row][col] = 0
                
            elif countNeighbors(row, col, A) == 3 and A[row][col] == 0:
                
                newA[row][col] = 1
                
    return newA

# test 8

# Expected outcome based on instructions.

A = [[0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0]]

print("")
print(printBoard(A))
print("")

#00000
#00100
#00100
#00100
#00000

A2 = next_life_generation(A)

print("")
print(printBoard(A2))
print("")

#00000
#00000
#01110
#00000
#00000

A3 = next_life_generation(A2)

print("")
print(printBoard(A3))
print("")

#00000
#00100
#00100
#00100
#00000
