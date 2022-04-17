# Binary search - SOLUTION of binsearchEx.py

# This version is made to fit the search interface
# used in insertionExercise.py.
# The best way to do insertion sort is to use the insertV2
# function, with binary search instead of linear search.

#######################################################
# Search a sorted list segment.
# The idea is to use two variables, j and hi,
# narrowing the search range with j on the low
# side and hi on the high side.
# with invariant L[0:j] <= x and x < L[hi:i] and j<=hi
# Each iteration should decrease hi - j .
# 
# Note: as in the lab exercise on sorting, the notation
# L[0:j] <= x means all elements of L[0:j] are at most x.
# This isn't Python, it's just notation used in comments.
#######################################################

def binsearch(L, i, x):
    
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''
    
    j = 0  # now L[0:j] is []
    hi = i # now L[hi,i] is []
    
    # invariant: L[0:j] <= x < L[hi:i] and j <= hi

    while j != hi:
        
        # There's at least one element in L[j:hi]. 
        # Set mid to one of the indexes j,...,hi-1
        
        mid = (hi + j) // 2 
        
        if L[mid] <= x:
            j = mid + 1
            
        else:
            hi = mid
            
    # now j==hi and the invariant holds
    
    return j

def testBinSearch():
    # in middle
    assert binsearch([0,2,4,6,3,0,5], 3, 3) == 2
    # near start
    assert binsearch([1,2,3,4,1], 3, 1) == 1
    # at start 
    assert binsearch([1,2,3,0], 3, 2) == 2
    # at end
    assert binsearch([1,3,5,5], 3, 6) == 3
    assert binsearch([1,3,5,5], 4, 6) == 4
    # at end, short list 
    assert binsearch([0], 1, 5) == 1
    assert binsearch([3,4], 2, 5) == 2
    # at start, short list
    assert binsearch([5], 1, 2) == 0
    assert binsearch([3,4], 2, 1) == 0

#############################################
# Here's how to find an element of a list,
# using binary search.  Think carefully about
# why this is correct, based on the docstring
# that specifies binsearch.
#############################################

def find(L,x):
    
    '''For sorted L, return k such that L[k] == x,
       or -1 if x does not occur in L.'''
       
    j = binsearch(L, len(L), x) 
    
    if j == 0 or L[j-1] != x:
        return -1
    
    else:
        return j-1

def testFind():
    
    # at start
    assert find([3,6,20], 3) == 0
    # at end
    assert find([2,6,20], 20) == 2
    # in middle, odd position
    assert find([2,6,20,25,30], 25) == 3
    # in middle, even position
    assert find([2,6,20,25,30], 20) == 2
    # in middle, odd position, even list
    assert find([2,6,20,25], 25) == 3
    # in middle, even position, even list
    assert find([2,6,20,25], 20) == 2


##################################################
# Here's a version that prints a trace of the loop
##################################################

def binsearch_trace(L, i, x):
    
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''
    
    j = 0  
    hi = i 
    
    # invariant: L[0:j] <= x < L[hi:i] and j <= hi

    print("j hi \n-----")
    print(j, hi)

    while j != hi:
        mid = (hi + j) // 2 
        
        if L[mid] <= x:
            j = mid + 1
            
        else:
            
            hi = mid
            
        print(j, hi)
        
    return j


   
    
        
        
