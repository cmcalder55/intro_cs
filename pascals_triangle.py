

def pascal_row(n):
    
    '''Takes a single integer input representing the triangle's row
    number >= 0. Outputs a list of elements found in the indicated
    row of Pascal's Triangle.'''
    
    if n == 0:
        return [1]

    def pascal_helper(L):

        '''Outputs a list containing the sums of each pair of adjacent
        elements from the input list L.'''
        
        if len(L) <= 1:
            return []
        return[L[0] + L[1]] + pascal_helper(L[1:])
    
    return [1] + pascal_helper(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    
    '''Takes a single integer input and returns a list of lists representing
    the values of all the rows up to and including n in Pascals' Triangle.'''
    
    if n == 0:
        return [[1]]
    elif n == 1:
        return [[1], [1,1]]
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_triangle():

    '''Tests if the output of the pascal_triangle function at 0, 1, 3, and 5
    match the expected values.'''
    
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
def test_pascal_row():

    '''Tests if the output of the pascal_row function at 0, 1, 3, and 5
    match the expected values.'''
    
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
