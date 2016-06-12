'''
Module for advanced math functions
Intended for use with user interface, rather than computer processing
For computer processesing, use oldmath (in progress)
'''
import cat
#import warnings

'''
Takes a number and the base to change it to and changes base
Returns a string
Default base is 2 if none provided
'''
def changebase(num, base=2):
    #if num is not evenly divisable by base
    #uses repeated subtraction instead of division
    num2 = num
    times = 0
    a = 0
    #gets highest power of the base (highest place) the number will reach
    while True:
        num2 -= base**a
        #print num2, base**a, a
        if num2 >= 0:
            num2 = num
            a += 1
        else:
            num2 = num
            #a -= 1
            break
    #gets the number
    #need to determine the value of each place using division and remanders
    numlist =  ['0']*a
    for index, dgt in enumerate(numlist):
        den = (base**(len(numlist)-1-index))
        char = int(float(num2)/den)
        numlist[index] = str(char)
        num2 -= den*char
    numstr = ''
    for char in numlist:
        numstr += char 
    return numstr

'''
retunrs the string of a number in base ten, transformed out of a given base
'''
def frombase(num, base=2):
    return str(int(num, base))

'''
Takes the root of a number
If the number is not a perfect square, returns simplifed radical
Using pad will pad the string returned with spaces on each side for flow.
'''
def root(num, base=2, pad=False):
    import cat
    cat.ctype(num, int, 'root()')
    num = float(num)
    exp = 1./base
    if int(num**exp) == num**exp:
        return str(num**exp)
    else:
        #gets perfect base powers possible, within range needed. Will then divide those out, checking remainder.
        #gets perfect powers in number
        perfs = []
        for i in range(1, int(num)+1):
            if not num % i**base:
                perfs.append(i)
        #divides out perfect sqaures, starting with largest
        perfs = sorted(perfs, reverse=True)
        num2 = num
        for i in perfs:
            if not num2 % (i**base):
                num2 = num2/(i**base)
        #gets the factor
        fact = (num/num2)**exp #remove +1 and add exception to make 0=1?
        #builds the return
        fact = '' if fact ==1 else str(int(fact))+'*'
        roottype = '' if base == 2 else str(int(base))
        expression = '%s%sroot(%s)' % (fact, roottype, int(num2))
        if pad:
            return ' '+expression+' '
        else:
            return expression

'''
class for factoring things
might move this to oldmath
'''
class factor(object):
    def __init__(self):
        import cat
       
    '''
    returns a list of factor tuples
    set one to False to exculde one from the factor list
    Setting both to False will return a single list of single factors
    Ignore ignores the number and one.
    '''
    @classmethod
    def factor(self, num, one=True, split=False):
        facts = []
        if one:
            a = 1
        else:
            a = 2
        for i in range(a, int(num**.5)+1):
            if not num % i:
                if not split:
                    facts.append((i, num/i))
                else:
                    facts.append(i)
                    facts.append(num/i)
        return facts

    '''
    checks if value is prime
    '''
    @classmethod
    def isPrime(self, num):
        import os
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Primes.txt'), 'r+') as f:
            primes = [int(line.rstrip('\n')) for line in f]
            if num not in primes:
                for i in range(int(num**.5) + 1, 1, -1):
                    if not num%i:
                        return False
                f.write('\n'+str(num))
                return True
        return True

    '''
    Used for writing primes to the list
    '''
    @classmethod
    def writePrimes(self, num):
        found = 0
        for i in range(num+1):
            found += int(factor.isPrime(i))
        print('%s primes found' % found)

    '''
    returns a list of prime factors.
    Should return a  list with multiple instances of factors occuring multiple times
    '''
    @classmethod
    def primeFactor(self, num):
        facts = []
        num2 = num
        for i in range(2, int((num**.5)+1)):
            print i
            if not num2%i and factor.isPrime(i):
                 facts.append(i)
                 num2 /= i
                 while not num2%i:
                     print i
                     num2 /= i
                     facts.append(i)
        return facts
    
'''
Class for fractions.
Contains methods for conversion to fractions, simplification of fractions
'''
class fraction(object):
    def __init__(self, n, d):
        import cat
        import warnings
        self.n = n
        self.d = d

    '''
    simplifies a fraction given as a tuple
    '''
    @classmethod
    def simplify(self, num):
      #  cat.ctype(num, cat.newmath.fraction, 'simplify()')
   #     if len(num) > 2:
   #         warnings.warn('Expected tuple of lenth 2. Tuple of lenth %s recived. This might still work' % len(num)) 
##        for i in num:
##            cat.ctype(i, int, 'simplify()')
        n = num.n
        d = num.d
        print factor.factor(n, one=False, split=True)
        for i in cat.listf.compare(factor.factor(n, one=False, split=True), factor.factor(d, one=False, split=True)):
            n /= i
            d /= i
            print n, d
        return n, d
    
    '''
    converts decimal to fraction
    returns tuple (numerator, denominator)
    '''
    @classmethod
    def tofrac(self, num):
        cat.ctype(num, float, 'tofrac()')
        num2 = num
        count = 0
        while not cat.oldmath.isint(num2):
            num2 *= 10
            count += 1
        n = num2
        d = 10**count
        print n, d
        return fraction.simplify((int(n), int(d)))

    '''
    Adds two fractions
    '''
    @classmethod
    def add(self, f1, f2):
        n1, d1 = totuple(f1)
        n2, d2 = totuple(f2)
        if n1 == n2:
            return (n1+n2, d2)
        else:
            #multiplies deominators and gets fraction
            nd = d1*d2
            n1 *= d2
            n2 *= d1
            

    '''
    gets a tuple of numerator, denominator from a fraciton object
    '''
    @classmethod
    def totuple(self, num):
        return num.n, num.d
    '''
    Returns a string of the fraction. Use for printing.
    '''
    @classmethod
    def tostring(frac):
        return frac[0]+'/'+frac(1)

'''
class for running regressions and giving the result
'''
class regression(object):
    @classmethod
    def __init__(self):
        None

    '''
    Standard regression
    '''
    def standard(self, xs, ys, retdeg=False):
        deg = len(xs)-1
        array = numpy.zeros((deg+1, deg+1))
        for i, x in enumerate(xs):
            for i2, __ in enumerate(array[i]):
                array[i][i2] = x**(deg-i2)
        A = numpy.matrix(array)
        array = numpy.zeros((deg+1, 1))
        for i, y in enumerate(ys):
            array[i][0] = y
        X = numpy.matrix(array)
        B = A.I*X
        coeffs = [float(i[0]) for i in B]
        eq = ''
        for i, c in enumerate(coeffs):
            #use for comparison; apparently floats are too imprecise
            cr = round(c, 2)
            if c < 10**-10 and c > -(10**-10):
                c = 0  
            if cr == 1:
                eq += 'x**%s+' % (deg-i)
            elif cr:
                eq += '%s*x**%s+' % (float(c), deg-i)
            #finds actual degree of equation
            if c == deg:
                deg -= 1
        #formats equation to make more readable
        eq = eq.rstrip('+')
        eq = eq.replace('+-', '-')
        if retdeg:
            return eq, deg, coeffs
        else:
            return eq

        '''
        root regression
        Only works in perfect cases: root(x)+c
        otherwise returns inverse function (x=y**5+y**2+5)
        '''
        @classmethod
        def root(self, xs, ys):
            eq, deg, coeffs = reg(ys, xs, True)
            eq = eq.replace('x', 'y')
            #perform limited 'algebra'
            if eq.count('y') == 1:
                c = str(coeffs[len(coeffs)-1-deg])
                c = '' if round(float(c), 2) == 1 else c
                eqt = eq.split('+')
                eql = eq.split('*')
                r = eqt[len(eqt)-1] if eqt[len(eqt)-1] == eql[len(eql)-1] else 0
                if r:
                    return str(c)+'x**(1/'+str(deg)+')+'+r
                else:
                    return str(c)+'x**(1/'+str(deg)+')'
            else:
                return eq
            
'''
class for taking irrational numbers out of equations
Only can do division for now
Exponents coming later
'''
class irrat(object):
    @classmethod
    def __init__(self):
        import math
        from math import pi, e
        
    '''
    pi
    '''
    def rempi(self, n, useunicode=True):
        pic = u'\u03c0'
        if not n%pi:
            n2 = n/pi
            if not cat.oldmath.isint(n2)
                n2 = fraction.tostring(fraction.tofrac(n2))
        #would need to determine if an even root can be taken here,
        #then take it if nessesary
        if useunicode:
            return u'\u03c0*'+n2
        else:
            return 'pi*'+n2

    '''
    e
    '''
    def reme(self, n):
        if not n%e:
            n2 = n/e
            if not cat.oldmath.isint(n2):
                n2 = fraction.tostring(fraction.tofrac(n2))
        return 'e*'+n2
        
        
    
#this stays at the bottom    
def newmath():
    print '''You can't take three from two,
Two is less than three,
So you look at the four in the tens place.
Now that's really four tens
So you make it three tens,
Regroup, and you change a ten to ten ones,
And you add 'em to the two and get twelve,
And you take away three, that's nine.
Is that clear?

Now instead of four in the tens place
You've got three,
'Cause you added one,
That is to say, ten, to the two,
But you can't take seven from three,
So you look in the hundreds place.

From the three you then use one
To make ten ones...
(And you know why four plus minus one
Plus ten is fourteen minus one?
'Cause addition is commutative, right!)...
And so you've got thirteen tens
And you take away seven,
And that leaves five...

Well, six actually...
But the idea is the important thing!

Now go back to the hundreds place,
You're left with two,
And you take away one from two,
And that leaves...?

Everybody get one?
Not bad for the first day!

Hooray for New Math,
New-hoo-hoo Math,
It won't do you a bit of good to review math.
It's so simple,
So very simple,
That only a child can do it!

Now, that actually is not the answer that I had in mind, because the book that I got this problem out of wants you to do it in base eight. But don't panic! Base eight is just like base ten really - if you're missing two fingers! Shall we have a go at it? Hang on...

You can't take three from two,
Two is less than three,
So you look at the four in the eights place.
Now that's really four eights,
So you make it three eights,
Regroup, and you change an eight to eight ones
And you add 'em to the two,
And you get one-two base eight,
Which is ten base ten,
And you take away three, that's seven.
Ok?

Now instead of four in the eights place
You've got three,
'Cause you added one,
That is to say, eight, to the two,
But you can't take seven from three,
So you look at the sixty-fours...

"Sixty-four? How did sixty-four get into it?" I hear you cry! Well, sixty-four is eight squared, don't you see? "Well, ya ask a silly question, ya get a silly answer!"

From the three, you then use one
To make eight ones,
You add those ones to the three,
And you get one-three base eight,
Or, in other words,
In base ten you have eleven,
And you take away seven,
And seven from eleven is four!
Now go back to the sixty-fours,
You're left with two,
And you take away one from two,
And that leaves...?

Now, let's not always see the same hands!
One, that's right.
Whoever got one can stay after the show and clean the erasers.

Hooray for New Math,
New-hoo-hoo Math!
It won't do you a bit of good to review math.
It's so simple,
So very simple,
That only a child can do it!
~Tom Lehrer'''
