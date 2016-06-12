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
