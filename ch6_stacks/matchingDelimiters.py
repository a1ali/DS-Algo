'''
Can use stacks to see if an expression has proper delimeters placed
for example
([()]) is correct 
)[()]) is incorrect

uses the class established in arrayStack.py
'''


def is_matched(expr):
    '''return True if all the delimeters are properly match otherwize false'''
    lefty = '({[' #opening delimeters
    righty = ')}]' #closing delimeters
    S = ArrayStack()
    for c in expr:
        if c in lefty: #push left delimeter on stack
            S.push(c)
        elif c in righty:
            if S.is_empty(): #nothing to match
                return False 
            if righty.index(c) != lefty.index(S.pop()): #mismatched delimeters
                return False 
    
    return S.is_empty()