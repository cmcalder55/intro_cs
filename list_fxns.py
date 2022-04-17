
def ind(e,L):

    ''' Compares each element of L to e until the first instance is found and 
    returns its index. 'e' and 'L' must be strings. If 'e' does not occur in
    'L', length of the list is output.'''

    if L == [] or L == '':          # if the list is empty, return length '0'
        return 0
    
    elif e == L[0]:                 # if e is the same as the first element
        return 0                    # of L, return index '0'
    
    else:                           # compare e to each element in L and add 1 
        return ind(e,L[1:]) + 1     # to index count each time  
                                   

def removeAll(e,L):
    
    '''Takes input of an element e and list or string L and outputs the 
    input list L with all the instances of e removed; e must be a standalone
    element to be removed.'''

    if L == []:
        return []
    
    elif L[0] == e:
        return removeAll(e,L[1:])
    
    return [L[0]] + removeAll(e,L[1:])

def deepReverse(L):

    '''Takes input of a list of elements L and outputs the reversed list;
    if any of the list elements are lists, these are also reversed'''

    if L == []:
        return []
    
    elif isinstance(L[0],list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    
    return deepReverse(L[1:]) + ([L[0]])

if __name__ == '__main__':
    
    list_t = ['a','b','c','d']
    print(ind('c', list_t))
