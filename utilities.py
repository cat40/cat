#put home functions on first line. Subpackages should be handled in their files
##def __init__():
##    __all__ = ['copyf, ctype, makeList, ex, getvar']
#put home function shere
'''
Checks if variable is of given type
If not, raises error.
Silent allows for basic type checking, though you should use type() for this
'''
def ctype(var, exptype, fname='', silent=False):
    if type(var) is not exptype:
        if not silent:
            raise TypeError('%s %s argument expected, got %s' % (fname, exptype, type(var)))
        else:
            return False
    else:
        return True

'''
Copies using windows command prompt.
Faster than shutil.copy2()
Returns True if sucess
'''
def copyf(frompath, topath):
    import subprocess.call
    import os.path.abspath
    callThis = 'copy "'+os.path.abspath(frompath)+'" "'+os.path.abspath(topath)+'"'
    return not bool(subprocess.call(callThis, shell=True)) #true if worked, false if failed

'''
Makes a list out of a generator object
'''
def makeList(gen):
    l = []
    for thing in gen:
        l.append(thing)

'''
Executes code from a file
'''
def ex(path, warning=True): #Do not use to get variables
    if warning:
        print('WARNING: DO NOT USE TO OBTAIN VARIABLES. Use getvar instead.')
    lines = [line.rstrip('\n') for line in open(path)]
    code = ''
    for line in lines:
        code = code + '\n' + line
    exec(code)

'''
executes code from a file
Returns dictionary of variables
'''
def getvar(path): #returns a dictionary of variables. Call using getvar(path)['varname'].
    lines = [line.rstrip('\n') for line in open(path)]
    code = ''
    for line in lines:
        code = code + '\n' + line
    exec(code)
    del lines
    del code
    del line
    return locals()

'''
deletes all variables before exiting
Theoretically more secure than sys.exit()
'''
def delex():
    import sys
    this = sys.modules[__name__]
    for n in dir():
        if n[0]!='_': delattr(this, n)
    del n
    sys.exit()
    
def walk(path):
    import os
    return (os.path.join(root, filename) for root, _, filenames in os.walk(path) for filename in filenames)

def bitsfromfile(f):
    byte = (ord(b) for b in f.read())
    for b in byte:
        for i in range(8):
            #print b, i, b >> i, (b>>i)&1
            yield (b >> i) & 1
            
def bits(f):
    byte = (ord(b) for b in f)
    for b in byte:
        for i in range(8):
            #print b, i, b >> i, (b>>i)&1
            yield (b >> i) & 1

'''
assertion with customizable error type
'''
def assertf(phrase, error=AssertionError):
    if not phrase:
        raise error
