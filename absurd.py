'''
Joke module making a sort of data type that makes any value entered
absurdly large, messed up, and useless
'''
#class Absurd(object):
def Absurd(var):
    import random
##    types = {int:'return ((var*random.randint(100000000000000000, 50000000000000000000000000))+random.randint(9, 10))/random.random()',
##             long:'return var/float(random.randint(1000000000000000000000, 9000000000000000000000000000000000000000))',
##             float:'return random.randint(-int(var), int(var))',
##             complex:'''del var
##print "NumberTooComplexError: Number too complex to be read. We've been nice enough to delete it for you."
##return None''',
##             str:'return random.shuffle(var + chr(random.randint(32, 126))*(random.randint(1, 17)*len(var)))',
##             bool:'''exec("b="+"not"*random.randint(0, 250))
##return b''',
##             list:'''b = True
##d = dict()
##for i in list:
##if b:
##    c = i
##else:
##    if random.randint(0, 1):
##        d[c] = i
##    else:
##        d[i] = c
##b = not b''',
##             dict: '''l = []
##for key in var:
##if random.randint(0, 1):
##    l.append(key, var[key])
##else:
##    l.append(var[key], key)
##return random.shuffle(l)'''}
##    for key in types:
##        print key
##        if type(var) is key:
##            exec(types[key])
##    return 'problem'
    t = type(var)
    if t is int:
        return long(((var*random.randint(10*10**20, 50*10**50)**random.randint(17, 127))+random.randint(9, 10)))
    elif t is long:
        return var/float(random.randint(1000000000000000000000, 9000000000000000000000000000000000000000))
    elif t is float:
        return random.randint(-int(var), int(var))
    elif t is complex:
        del var
        print "NumberTooComplexError: Number too complex to be read. We've been nice enough to delete it for you."
        return None
    elif t is str:
        for i in range(random.randint(0, 12738)):
            var += chr(random.randint(32, 126))
        l = [c for c in var]
        random.shuffle(l)
        s = ''
        for c in l:
            s += c
        return s
    elif t is bool:
        exec("b="+"not "*random.randint(0, 251)+'var')
        return b
    elif t is list:
        b = True
        d = dict()
        random.shuffle(var)
        for i in var:
            if b:
                c = i
            else:
                if random.randint(0, 1):
                    d[c] = i
                else:
                    d[i] = c
            b = not b
        return d
    elif t is dict:
        l = []
        for key in var:
            if random.randint(0, 1):
                l.append(key, var[key])
            else:
                l.append(var[key], key)
        return random.shuffle(l)
    else:
        return 'problem'
        
