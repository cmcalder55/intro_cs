# exercise counting matches

def numMatches(L, M):
    
    ''' Assume L and M are lists without duplicates. Return the number
        of elements that are the same (using ==).'''
        
    count = 0
    
    for x in L:
        
        for y in M:
            
            if x==y:
                
                count += 1
                
    return count

L1 = ['Chance', 'Esperanza', 'Khaled', 'Morrisset', 'St. Vincent']
L2 = ['Alicia Keys', 'Esperanza', 'Lila Downs', 'Macklemore', 'Morrisset']

def numMatch(L,M):
    
    '''Assuming L and M are sorted lists without duplicates, return numMatches(L,M)'''
    
    count = 0
    i = 0
    j = 0
    
    # Invariant: count == number of matches between L[:i] and M[:j]
    
    while i < len(L) and j < len(M):
        
        if L[i]==M[j]:
            
            count += 1
            
        elif L[i] < M[j]:
            
            i += 1
            
        else:
            
            j += 1
            
    return count

assert numMatch(L1,L2) == numMatches(L1,L2)






