
from cs115 import map, reduce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 1
' Study function questify(). Then implement questifyAlt() so that it gives
' the same results as questify(), using map and lambda but no helping function.
' Hint: adapt the body of addQuestmark().
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def questify(str_list):
    
    '''Assume str_list is a list of strings. Returns a list of
    the same strings but with ? suffixed to each.'''
    
    def addQuestmark(s):
        
        '''Adds a question mark to a string.'''
        
        return s + '?'

    return map(addQuestmark, str_list)

def questifyAlt(str_list):
    
    '''Same as questify'''
    
    return map(lambda x: x + '?', str_list)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 2
' Study functions leppard() and catenate(). Implement catenateLoop(), without
' using recursion or reduce or any built-in Python function. Instead, use a
' loop. In some ways your code will resemble the body of leppard().
' If you prefer, you can follow the style of leppardIndex(), but I suggest not.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def leppard(inputString):
    
    '''Mystery.'''
    
    outputString = ''
    
    for symbol in inputString:
        
        if symbol == 'o':
            outputString = outputString + 'ooo'
            
        else:
            outputString = outputString + symbol
            
    print(outputString)

def leppardIndex(inputString):
    
    '''Same as leppard(), but using an integer index rather than directly
    referring to elements of the input string.'''
    
    outputString = ''
    
    for i in range(len(inputString)):
        
        if inputString[i] == 'o':
            outputString = outputString + 'ooo'
            
        else:
            outputString = outputString + inputString[i]
            
    print(outputString)

def catenate(str_list):
    
    '''Assume str_list is a list of strings.
    Return a single string, their catenation.'''
    
    if str_list == []:
        return ''
    
    return reduce(lambda s, t: s + t, str_list)

def catenateLoop(str_list):
    
    '''Same as catenate'''
    
    outputString = ''
    
    for s in str_list:
        
        if str_list == []:
            return ''
        
        else:
            outputString = outputString + s
            
    
