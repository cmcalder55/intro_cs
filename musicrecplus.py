'''
@author: ccalder
Pledge: I pledge my honor that I have abided by the Stevens
Honor System. - Cameron Calder

CS115 - Homework 10
'''

private = False
names = []
artists = []
FILE_NAME = 'musicrecplus.txt'

def printDB():
    
    '''Prints out user's name and their artists.'''
    
    print(names)
    print(artists)

# works

def loadDB():
    
    '''Reads the file musicrecplus.txt and formats the data.'''
    
    file = open(FILE_NAME, 'r+')

    for line in file:
        
        if line.find(':') != -1:
            
            name = line[0:line.index(':')]
            
            if name[-1] == '$':
                
                private = True
                
            names.append(name)
            a = line[line.index(':') + 1:]
            ab = a.split(',')
            artists.append(ab)
            
        else:
            
            break


def UpdateDB(names, new):
    
    '''Updatas database with new users.'''
    
    file = open(FILE_NAME, 'w')
    increment = 0
    
    for i in names:
        
        newLine = '{}: '.format(names[increment])
        
        for k in sorted(new[increment]):
            
            newLine += k + ', '
            
        newLine = newLine[:-2]
        print(newLine)
        file.write(newLine)
        increment += 1
        
    file.close()

def UpdatePref(name, userNumber):
    
    '''Updates user's preferences by writing strings to musicrecplus.txt'''
    
    new = []

    while True:
        
        a = input('Enter an artist that you like ( Enter to finish ):\n').strip()
        
        if a == '' or a == '\n':
            
            break

        artist = ''.join([' ' + word.capitalize() for word in a.split()])[1:]
        new.append(artist)

    if name not in names:
        
        names.append(name)
        artists.append(new)
        
    else:
        
        artists[userNumber] = new

    UpdateDB(names, artists)


def GetRec(users, current):
    
    '''Outputs user's recommendations based on which users have the most
    similar artists.'''
    
    # recs = []
    
    diffs = 100000
    twin = ''
    
    for name, u in users.items():
        
        if name == current or len(users[current].artists ^ u.artists) == 0:
            
            continue
        
        if len(users[current].artists ^ u.artists) < diffs:
            
            twin = name
            diffs = len(users[current].artists ^ u.artists)
            
    if twin == '':
        
        print('No recommendations available at this time .\n')
        
        return
    
    out = sorted([a for a in users[twin].artists - users[current].artists])
    
    for o in out:
        
        print(o)


def MostPop(artists):
    
    '''Prints most popular artist in the database.'''
    
    if len(artists) == 0:
        
        return ('Sorry , no artists found .\n')
    
    king = list(artists.keys())[0]
    
    for a, s in artists.items():
        
        if len(s) > len(artists[king]):
            
            king = a
            
    if king != '':
        
        return (king)
    
    else:
        
        return ('Sorry , no artists found .\n')


def HowPop(artists):
    
    '''Prints the number of likes of the most popular artists.'''
    
    king = MostPop(artists)
    
    if king != 'Sorry , no artists found .\n' and king != 'Sorry , no artists found .':
        
        print(len(artists[king]))


def MostUser(users):
    
    '''Prints which user likes the most artists.'''
    
    if len(users) == 0:
        
        print('Sorry , no user found .')
        
    queen = list(users.keys())[0]
    
    for name, u in users.items():
        
        if len(u.artists) > len(users[queen].artists):
            
            queen = name
            
    print(queen)


def main():
    
    '''Main function.'''

    # FILE_NAME = 'musicrecplus.txt'
    loadDB()
    # printDB()

    name = input('Enter your name ( put a $ symbol after your name if you '
                 'wish your preferences to remain private ): ')

    userNumber = 0;

    if name not in names:
        
        userNumber = len(names)
        UpdatePref(name, userNumber)
        
    else:
        
        for i in range(len(names)):
            
            if (name == names[i]):
                
                userNumber = i

    # current = name
    
    while True:
        
        res = input( 'Enter a letter to choose an option :\ne - Enter '
                    'preferences\nr - Get recommendations\np - Show most '
                   ' popular artists\nh - How popular is the most popular\nm '
                   '- Which user has the most likes\nq - Save and quit\n')
        
        if res == 'e':
            UpdatePref(name, userNumber)
            
        elif res == 'r':
            GetRec()
            
        elif res == 'p':
            MostPop()
            
        elif res == 'h':
            HowPop()
            
        elif res == 'm':
            MostUser()
            
        elif res == 'q':
            exit(1)
            
        else:
            print("Invalid Input Try Again")

if __name__ == '__main__':
    
    main()
