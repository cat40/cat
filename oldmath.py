'''
module for math computations
'''
import math
from math import sin, cos, atan

sqrt2 = 2**0.5


'''
Infinity. Includes the concept of multiple infinities
This will not say that oo + x > oo. Will be considered equal. Only considers multipliers and exponents
'''
class Infinity(object):
    def __init__(self, multiplier=1, exponent=1):
        self.multiplier = multiplier
        self.exponenet = exponenent
    def __add__(self, b):
        if isinstance(b, Infinity):
            if b.exponent == self.exponenet:
                return Infinity(self.multiplier+b.multiplier, self.exponent)
            else:
                diff = self.exponent - b.exponent
                return Infinity(self.multiplier**diff + b.multiplier, b.exponent)/Infinity(self.multiplier, self.exponent + diff)
        return self
    def __sub__(self, b):
        if isinstance(b, Infinity):
            if b.exponent == self.exponenet:
                return Infinity(self.multiplier-b.multiplier, self.exponent)
            else:
                diff = self.exponent - b.exponent
                return Infinity(self.multiplier**diff - b.multiplier, b.exponent)/Infinity(self.multiplier, self.exponent + diff)
        return self
    def __mul__(self, b):
        if isinstance(b, Infinity):
            return Infinity(self.multiplier*b.multiplier, self.exponent+b.exponenet)
        else:
            return Infinity(self.multiplier*b, self.exponent)
    def __div__(self, b):
        if isinstance(b, Infinity):
            return Infinity(self.multiplier/b.multiplier, self.exponent-b.exponent)
        else:
            return Infinity(self.multiplier-b, self.exponent)
    def __exp__(self, b):
        return Infinity(self.multiplier**b, self.exponent*b)
    def __mod__(self, b):
        if isinstance(b, Infinity):
            if self.exponent == b.exponent:
                return self.multiplier % b.multiplier
            else:
                return Infinity(self.multiplier % b.multiplier, self.exponenet % b.exponent)
        return Infinity(self.multiplier % b, self.exponent)
    def __lt__(self, b):
        if isinstance(b, Infinity):
            return self.exponent < b.exponent if self.exponent != b.exponent else self.multiplier < b.multiplier
        return False
    def __le__(self, b):
        if isinstance(b, Infinity):
            return self.exponent <= b.exponent if self.exponent != b.exponent else self.multiplier <= b.multiplier
        return False
    def __eq__(self, b):
        if isinstance(b, Infinity):
            return self.exponent == b.exponent and self.multipiier == b.multiplier
        return False
    def __ne__(self, b):
        return not self == b
    def __ge__(self, b):
        if isinstance(b, Infinity):
            return self.exponent >= b.exponent if self.exponent != b.exponent else self.multiplier >= b.multipier
        return True
    def __gt__(self, b):
        if isinstance(b, Infinity):
            return self.exponent > b.exponent if self.exponent != b.exponent else self.multiplier > b.multiplier
        return True
    
'''
bases
extend int/float?
add provisions for multiplying, adding, etc
Probably can't handle negative numbers right now
    Except on conversion from a base != 10?
Add floor/ceiling methods
ROUNDING, and probably some operators, will not work on bases > 10
'''
class Base(object):        
    def __init__(self, num, base=2, seperator='\\', isfloat=False, basesymbol=None):
        #this must be a string type!
        self.num = str(num)
        self.base = base
        self.seperator = seperator
        self.isfloat = isfloat
        self.whole = num.split('.')[0]
        self.float = num.split('.')[1] if isfloat else ''
        if basesymbol is None:
            basesymbol = str(base)
        self.basesymbol = basesymbol

    @classmethod
    def tobase(cls, num, base, precision=None):              
        if base == 10:
            #this might confuse the user
            return num
        elif str(num)[0] == '-':
            num = -num
            neg = '-'
        else:
            neg = ''
        if isinstance(base, int) and isinstance(num, int):
            string = ''
            while num > 0:
                rem = num % base
                string = cls.letters[rem] + string
                #num -= int(num/base)
                num = int(num/base)
            return cls(neg + string, base)
        #if base is float
        else:
            if precision is None:
                precision = len(str(base).split('.')[1])
            string = ''
            while num > 1:                    
                rem = int(num % base)
                string = cls.letters[rem] + string
                num = num/base
            #start going backwards
            power = 0
            string += '.'
            #subtraction of irrational numbers gets x.xxxxxxx*10**-100something
            while len(string.split('.')[1]) <= precision:
                power -= 1
                count = 0
                while num >= base**power:
                    num -= base**power
                    count += 1
                string += str(count)
            return cls(neg + string, base, isfloat=True)
        
    def decimal(self):
        if not self.isfloat:
            return int(self.num, self.base)
        else:
            power = 0
            value = 0
            for digit in self.num.split('.')[0][::-1]:
                value += self.numbers[digit] * self.base**power
                power += 1
            #part < 1
            power = -1
            for digit in self.num.split('.')[1]:
                value += int(digit) * self.base**power
                power -= 1
            return value            

    def round(self, num):
        if self.isint():
            return self
        b = self.base
        lessthan1 = self.split('.')[1]
        #check if empty string (might not need to do this
        if lessthan1:
            #this gets weird if b is not an integer
            #probably actually works that way
            threshold = b/2
            if int(lessthan1[num]) <= threshold:
                return Base(self.num.split('.')[0]+'.'+lessthan1[:num], self.base)
            return Base(self.num.split('.')[0]+'.'+lessthan1[:num-1]+str(int(lessthan1[num])+1), self.base)
    def floor(self):
        return Base(self.num.split('.')[0], base)
    
    def ceil(self):
        if self.isint():
            return self
        return Base(self.floor()+1, self.base)

    def isint(self):
        return '.' not in self.num or self.num[-1] == '.'\
               or int((self.num.split('.')+['0'])[1]) == 0

    #this is what will print with print(some_base_object):
    #not sure if seperator can be changed this way
    #might need a seperate attribute, maybe also a set_seperator function
    def __str__(self):
        return self.num + self.seperator + self.basesymbol

    #@staticmethod
    @classmethod
    def isbase(cls, a):
        return isinstance(a, cls)
    
    #defining operators for type:
    #just converts to base 10 for now
    #might come up with something more interesting later
    def __add__(a, b):
        #if b is a base number
        #if isinstance(b, type(a)):
        if Base.isbase(b):
            base = a.base if a.base == b.base else 10
            anum = a.decimal(); bnum = b.decimal()
            return a.tobase(anum+bnum, base)
        else:
            return a.decimal()+b
    def __radd__(b, a):
        return b + a

    def __sub__(a, b):
        if Base.isbase(b):
            base = a.base if a.base == b.base else 10
            return a.tobase(a.decimal() - b.decimal(), base)
        else:
            return a.decimal() - b

    def __rsub__(a, b):
        return -b + a

    def __neg__(a):
        a.num = '-'+a.num
        return a
    #this will do Regular, not floor, division
    #bases will soon be able to be floats
    def __div__(a, b):
        if Base.isbase(b):
            anum = a.decimal(); bnum = b.decimal()
            if a.base == b.base:
                return Base.tobase(float(anum) / bnum)
            else:
                return float(a.decimal())/b.decimal()
        return float(a.decimal())/b
    
    def __truediv__(a, b):
        return a/b
    
    def __floordiv__(a, b):
        if Base.isbase(b):
            return (a/b).floor()
        else:
            return int(a/b)

    def __rdiv__(a, b):
        return a/b
    def __rtruediv__(a, b):
        return a/b
    def __rfloordiv__(a, b):
        return a // b

    def __mul__(a, b):
        if Base.isbase(b):
            if a.base == b.base:
                return Base.tobase(a.decimal()*b.decimal(), a.base)
            else:
                return a.decimal()*b.decimal()
        return a.decimal()*b

    def __rumul__(a, b):
        return a*b

    def __mod__(a, b):
        if Base.isbase(b):
            if a.base == b.base:
                return Base.tobase(a.decimal()%b.decimal(), a.base)
            else:
                return a.decimal()%b.decimal()
        return a.decimal()%b
    def __rmod__(a, b):
        return a%b
Base.letters = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
           10:'a'}#, 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'g', 17:'h', 18:'i', 19:'j',
           #20:'k', 13:'l', 14:'m', 15:'n', 16:'o', 17:'p', 18:'q', 19:'r'}
for i in range(10, 36):
    Base.letters[i] = chr(i+87)
Base.numbers = dict((Base.letters[key], key) for key in Base.letters)
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
            theta = math.radians(theta)
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
