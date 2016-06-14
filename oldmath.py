'''
class for math computations
'''

'''
Determines number of decimal places a number has
'''
def decimalplaces(num):
    return len(str(num).split('.')[1])

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

'''
returns true of input is close to an integer (within defined range)
'''
def closeint(num, r=.05):
    p = decimalplaces(r)
    n = round(num, p)
    i = int(round(num, 0))
    return n <= i+r and num >= i-r
