
# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    
    while True:
        
        user_plays()
        display_piles()
        
        if sum(piles) == 0:

            print('You win!')

            break
        
        computer_plays()
        display_piles()
        
        if sum(piles) == 0:

            print('Computer wins!')

            break

def init_piles():
    
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
        
    global piles
    global num_piles
    
    print('Get ready to play Nim.')
    
    num_piles = int(input('How many piles do you want? '))

    while 1 > num_piles > 1001:
        num_piles = int(input('Input invalid. How many piles do you want?' ))
        
    piles = [0] * num_piles

    for x in range(num_piles):
        size = int(input('How many in pile ' + str(x) + '? '))

        while size < 0 or size > 1000:
            print('Pile size invalid. Please choose a positive integer \
less than 1000.')

            size = int(input('How many in pile ' + str(x) + '? '))
        piles[x] = size
        
def display_piles():
    
    """ display current amount in each pile """
    
    global piles
    global num_piles

    for x in range(num_piles):
        
        print('pile ' + str(x) + ' = ' + str(piles[x]))


def user_plays():
    
    """ get user's choices and update chosen pile """
    
    global piles
    
    print("Your turn! ")
    
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
        
    global piles
    global num_piles

    answer = int(input('Which pile do you want to choose? '))
    
    while answer < 0 or answer > num_piles - 1:
        answer = int(input('Pile number invalid. Which pile? '))
        
    return answer

def get_number(pnum):
    
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
        
    global piles
    
    remove = 0
    remove = int(input('How many do you wish to remove? '))

    while piles[pnum] < remove <= -1:
        remove = int(input('Input too large or negative, try again. How many? '))
        
    return remove

def game_nim_sum():
    
    """ return the nim-sum of the piles """
    
    global piles
    global num_piles
    nim_sum = 0

    for pile in piles:
        nim_sum = nim_sum ^ pile
        
    return nim_sum

def opt_play():
    
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
        
    global piles
    global num_piles 

    nim_sum = game_nim_sum()
    
    for pile in piles:
        
        if pile ^ nim_sum < pile:
            take = pile - (pile ^ nim_sum)
            
            return (piles.index(pile), take)

    for x in piles:
        
        if x != 0:
            take = 1
            
            return(piles.index(pile), take)

def computer_plays():
    
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
        
    global piles
    global num_piles

    print("")
    print('My turn! ')
    print("")
    
    comp = opt_play()
    
    print('I want to remove ' + str(comp[1]) + ' from pile ' + str(comp[0]) +'. ')
    
    piles[comp[0]] = piles[comp[0]] - comp[1]

#   start playing automatically
if __name__ == "__main__" : play_nim()
