
def change(amount, coins):
    
    '''Takes input of a non negative amount of money
    and a list of coin types always containing a 1 coin and
    outputs a non negative integer indicating the minimum coins
    required to make up the given amount.'''
    
    if amount == 0:
        return 0
    
    if coins == []:
        return float('inf')
    
    if amount < 0:
        return 0
    
    if coins[0] > amount:
        return change(amount, coins[1:])
    
    useIt = 1 + change(amount - coins[0], coins)
    loseIt = change(amount, coins[1:])
    
    return min(useIt, loseIt)

def giveChange(amount, coins):
    '''Takes input of an amount of money and types of coin values.
    Returns output of minimum coins needed and the type of coins.'''
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    if coins[0] > amount:
        return giveChange(amount, coins[1:])
    useIt = giveChange(amount - coins[0], coins)
    loseIt = giveChange(amount, coins[1:])
    if useIt[0] < loseIt[0]:
        return[1+ useIt[0], useIt[1] + [coins[0]]]
    else:
        return loseIt

#test: giveChange(48, [1, 5, 10, 25, 50])

def fast_lucas(n):
    
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    
    def fast_lucas_helper(n, memo):
        
        '''Takes input of number n and uses memoization to
    take the sum of the two immediately previous terms, i.e the
    Lucas number.'''
    
        if n in memo:
            return memo[n]
        
        if n <= 0:
            result = 2
            
        elif n == 1:
            result = 1
            
        else:
            result = fast_lucas_helper(n-1, memo) + fast_lucas_helper(n-2, memo)
            
        memo[n] = result
        
        return result
    
    return fast_lucas_helper(n, {})

    pass  # TODO

def fast_change(amount, coins):
    
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    
    def fast_change_helper(amount, coins, memo):
        
        '''Helper function for fast change with input of coin type
        and amount with imporved performance using memoization and
        outputs the amount of coins needed to make desired change.'''
        
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        
        if amount == 0:
            result = 0
            
        elif len(coins) == 0 or amount < 0:
            
            result = float("inf")
            
        else:
            
            useIt = 1 + fast_change_helper(amount - coins[0], coins, memo)
            loseIt = fast_change_helper(amount, coins[1:], memo)
            result = min(useIt, float("inf") if loseIt == 0 else loseIt)
            memo[(amount, coins)] = result
            
        return result
    
        pass  # Write your code here

    # Call the helper. Note we converted the list to a tuple.
    
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

