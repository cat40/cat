'''
class for math computations
'''

'''
takes the root of a number with a given base
Returns numerical value
Use newmath.root() for display strings
'''
def root(n, base=2):
    p = 1.0/base
    return n**p

'''
Returns true if input is integer, false if not
'''
def isint(num):
    import math
    return int(num) == math.ceil(num)
