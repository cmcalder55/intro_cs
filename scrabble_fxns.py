
import sys
from dict import *
from bigdict import *
from cs115 import map, filter

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scoreList):
    '''Takes input letter as a single letter string and outputs a list of two 
    element lists with the associated letters and their values.'''
    if scoreList == []:
        return 0
    if letter == scoreList[0][0]:
        return scoreList [0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    '''Recieves input string S and a list of lists of characters and their 
    values and returns the scrabble score value of S.'''
    if S == '':
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def remove(letter, Rack):
    '''Helper function that takes input of letter used and removes it from the 
    Rack list so they are not overused when creating a list of possible words 
    from the given Rack.'''
    
    if Rack == '':
        return ''
    elif Rack == letter:
        return remove(letter, Rack[1:])
    return Rack

def possible(letters, Rack):
    '''Helper function that takes lower case letters input and tests Rack list 
    for possible words.'''
    if letters == '':
        return True
    elif letters[0] in Rack:
        return possible(letters[1:], remove(letters[0], Rack))
    return False
    
def helperWordsList(letters, Rack):
    '''Helper list that takes lower case letters input and creates a list of 
    possible words within the Rack list.'''
    if letters == []:
        return []
    if possible(letters[0], Rack):
        return [letters[0]] + helperWordsList(letters[1:], Rack)
    return helperWordsList(letters[1:], Rack)

def scoreList(Rack):
    '''Takes single input of Rack, alist of lower case letters, and returns all
    the words in the defined Dictionary that the given letters can make.'''
    
    def helperList(scoreList, wordList):
        '''Helper list to create list of possible words in the defined Dictionary and their point values.'''
        if wordList == []:
            return []
        return [[wordList[0], wordScore(wordList[0], scoreList)]] + helperList(scoreList, wordList[1:])
    return helperList(scrabbleScores, helperWordsList(Dictionary, Rack))

def bestWord(Rack):
    '''Takes single input of list of lower case letters and returns the highest 
    scoring word and its scrabble points value.'''
    if scoreList(Rack) == []:
        return ['', 0]
    maxScore = max(map(lambda x: x[1], scoreList(Rack)))
    bestPlays = filter(lambda x: x[1] == maxScore, scoreList(Rack))
    return bestPlays[0]
            
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scoreList):
        '''Takes input of letters and outputs their score values.'''
        if scoreList == []:
            return 0
        if letter == scoreList[0][0]:
            return scoreList[0][1]
        return letterScore(letter, scoreList[1:])

    def wordScore(s, scoreList):
        '''Takes input of scrabble words and outputs their point values.'''
        if s == '':
            return 0
        return letterScore(s[0], scoreList) + wordScore(s[1:], scoreList)
    return map(lambda word: [word, wordScore(word, scores)], dct)

#test: wordsWithScore(Dictionary, scrabbleScores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 3
' Implement letterScoreLoop using --you guessed it-- a loop instead of
' recursion. Also, do not use map or reduce.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

scrabbleScores = [["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], \
                  ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], \
                  ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], \
                  ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], \
                  ["y", 4], ["z", 10]]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", \
               "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist):
    
    '''Assume scorelist is a list of lists [ltr, val] where ltr is a single
    letter and val is a natural number. Assume letter is a single letter string,
    that occurs in scorelist. Return the associated value.'''
    
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    
    return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scorelist):
    
    '''Same as letterScore'''
    
    for s in scorelist:
        
        if letter == s[0]:
            return s[1]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 4
' Implement wordScoreLoop using a loop instead of recursion. (And don't
' use map or reduce.)
' Use letterScore() or letterScoreLoop(); it shouldn't matter which one.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def wordScore(S, scorelist):
    
    '''Assume S is a string and scorelist is in the format above and
    includes every letter in S. Return the scrabble score of that string.'''
    
    if S == '':
        return 0
    
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scorelist):
    
    '''Same as wordScore'''
    
    scr = 0
    
    for i in range(len(S)):
        scr = scr + letterScoreLoop(S[i], scorelist)
        
    return scr

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 5
' Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def wordsWithScore(dct, scores):
    
    '''Assume dct is a list of words and scores is a list of [letter, number]
    pairs. Return a copy of the dictionary, annotated so each word is paired
    with its value. For example, wordsWithScore(scrabbleScores, aDictionary)
    should return [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    
    def scoreWord(wrd):
        
        return [ wrd, wordScore(wrd, scores) ]

    return map(scoreWord, dct)

def wordsWithScoreLambda(dct, scores):
    
    '''Same as wordsWithScore'''
    
    if len(dct) == 0:
        return []
    
    return map(lambda x: [x, wordScore(x, scores)], dct)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 6
' Implement wordsWithScoreLoop using a loop instead of map or recursion.
' Be careful NOT to change the dictionary.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def wordsWithScoreLoop(dct, scores):
    
    '''Same as wordsWithScore'''
    
    scr = []
    
    for x in dct:
        scr = scr + [[x, wordScore(x, scores)]]
        
    return scr








