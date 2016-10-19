import cat
'''
Gets a number from user input. Allows expressions.
Allows retries until valid input achived.
'''
def getnum(string=''):     
    while True:
        try: n = eval(raw_input(string))
        except (SyntaxError, NameError, ZeroDivisionError), e:
            cat.error.error(str(e))
            print('please try again')
            pass
        else: break
    return n

##'''
##checks an input for a set of values
##keeps asking until found
##special cases:
##input.num = any number
##If not case sensative, will return input.lower()
##For multiple special cases accepted together, use a tuple
##'''
##class LoopBreak(Exception): pass
##number = '1234567890.'
##letter = 'abcdefghijklmnopqrstuvwxyz'
##letter += letter.upper()
##special_cases = {id(num):
##'''for char in i:
##    if char in numbers:
##        raise LoopBreak''',
##                 id(letter):
##'''for char in i:
##    if char in letters:
##        raise LoopBreak'''}
###python does not change the id of b in a = b until be is modified
##def valid_input(inputs, string='', case_sensitive=True):
##    for i, option in enumerate(inputs):
##        if isinstance(option, tuple):
##            inputs[i] = ''
##            for e in option:
##                inputs[i] += e
##    while True:
##        i = raw_input(string)
##        if not case_sensative:
##            i = i.lower()
##        for option in inputs:
##            if i == option:
##                return i
##            elif option in special_cases:
##                exec special_cases[option]
##    return i
