'''
class for math computations
Add vector class
'''
import math
from math import sin, cos, atan
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

'''
compares to list of known fractions
returns true if in it
'''
def isfrac(num, fracs = [1./16, 2./16, 3./16, 4./16, 5./16, 6./16, 7./16, 8./16,
                         9./16, 10./16, 11./16, 12./16, 13./16, 14./16, 15./16,
                         1./9, 2./9, 3./9, 4./9, 5./9, 6./9, 7./9, 8./9]):
    for i, f in enumerate(fracs):
        fracs[i] = round(f, decimalplaces(num))
    return num in fracs

'''
Determines if number within given tolderance of being a fraction
denominator !> denominator limit, etc
'''
def isrational(num, denom_tol=10000, num_tol=10000):
    return num.as_integer_ratio()[1] < denom_tol and num.as_integer_ratio()[0] < num_tol

'''
finds quadrant of angle, given x and y and angle
uses radians
'''
def quadrant(x, y):
    if x >= 0 and y >= 0:
        return 1
    elif x >= 0 and y < 0:
        return 4
    elif x < 0 and y >= 0:
        return 2
    else:
        return 3

def angleInQuadrant(q, theta, neg=False):
    if q == 1:
        return theta
    elif q == 2:
        return theta + math.pi/2
    elif q == 3 and not neg:
        return theta + math.pi
    elif q == 3 and neg:
        return theta - math.pi
    elif q == 4 and not neg:
        return theta + 3*math.pi/2
    elif q == 4 and neg:
        return -theta
    else:
        raise ValueError('invalid quadrant: %s is not between 1 and 4' % q)
    
class Vector(object):
    #might be able to get rid of x and y if not much precision lost going from cartesian
    def __init__(self, r, theta, x, y):
        self.r = r
        self.radians = theta
        self.degrees = math.degrees(theta)
        self.x = x
        self.y = y
        self.quadrant = quadrant(self.x, self.y)
        
    @classmethod
    def from_polar(cls, r, theta, useDegrees=False):
        if useDegrees:
            theta = math.radians(theta))
        self.x = r*cos(self.radians)
        self.y = r*sin(self.radians)
        return cls(r, theta, x, y)

    @classmethod
    def from_cartesian(cls, x, y):
        r = math.sqrt(x**2 + y**2)
        theta = angleInQuadrant(quadrant(x, y), atan(float(y)/x))
        return cls(r, theta, x, y)

    def add(self, vector2):
        x = self.x + vectorlist.x
        y = self.y + vectorlist.y
        r = math.sqrt(x**2 + y**2)
        theta = angleInQuadrant(quadrant(x, y), atan(float(y)/x))
        return Vector(r, theta)

    @classmethod
    def sum(cls, *vectors):
        x = y = 0
        for v in vectors:
            x += v.x
            y += v.y
        r = math.sqrt(x**2 + y**2)
        theta = angleInQuadrant(quadrant(x, y), atan(float(y)/x))
        return Vector(r, theta)

    def multiply(self, num):
        return Vector(self.r*num, theta)
