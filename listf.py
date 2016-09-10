from copy import copy
#Returns a tuple of entry number, greatest value
def greatest(List):
    High = List[0]
    for i, v in enumerate(List):
        if v >= High:
            High = v
            HighNum = i
    return HighNum, High

#Returns a tuple of entry number, lowest value
def least(List):
    Low = List[0]
    for i, v in enumerate(List):
        if v <= Low:
            Low = v
            LowNum = i
    return LowNum, Low

#Returns a list of equavilent values in a two lists
def compare(List1, List2):
    a = 0
    Values = []
    for value in List1:
        if value in List2:
            Values.append(value)
    return Values

#Checks for duplicates in a list. Returns true if duplicates. 
def checkduplicate(List):
    from copy import copy
    Err = False
    Entry = 0
    for values in List:
        List2 = copy(List)
        del List2[Entry]
        if List[Entry] in List2:
            Err = True
        Entry = Entry + 1
    return Err

#Checks for duplicates in a list and returns a list with no duplicates
def delduplicate(list1):
    a = 0
    list3 = []
    for value in List:
        list2 = copy(list1)
        del list2[a]
        if value in list2:
            list3.append((a, value))
    return list3

'''
Cuts a list down to a specified lenth.
'''
def truncate(list1, lenth):
    for i in range(lenth, len(list1)):
        del list1[i]

'''
Picks a random value from the list
'''
def pick(l):
    import random
    return l[random.randint(0, len(l)-1)]

'''
searches a list for a value
Returns the index number
'''
def find(val, l):
    found = []
    for i, thing in enumerate(l):
        if val == thing:
            found.append(i)
    return found


'''
flattens a list of lists
List can be irregular ([[a, b, c], [e, f, g, h, i], j, k, l])
'''
def flatten(l):
    import collections
    newl = []
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            for item in genflatten(thing):
                newl.append(item)
        else:
            newl.append(thing)
    return newl

'''
like flatten, but a generator
'''
def genflatten(l):
    import collections
    for thing in l:
        if isinstance(thing, collections.Iterable) and not isinstance(thing, (str, bytes)):
            for item in genflatten(thing):
                yield item
        else:
            yield thing

'''
strips an entry from a list
'''
def strip(v, l):
    newl = []
    for i in l:
        if i != v:
            newl.append(i)
    return newl

'''
strips an entry from right
'''
def rstrip(v, l):
    strip = False
    for i, value in enumerate(reversed(l)):
        if value != v:
            break
    i = len(l) - i
    return l[:i]
'''
strips an entry from left
'''
def lstrip(v, l):
    strip = False
    for i, value in enumerate(l):
        if value != v:
            break
    i = len(l) - i
    return l[:i]
        
'''
class for dealing with strings in lists
'''
class string(object):
    @classmethod
    def __init__(self):
        None
        
    '''
    takes a list of strings and merges the strings between two charecters
    '''
    @classmethod
    def merge(self, l, start, end=None):
        if end is None:
            end = start
        newl = []
        startmerge = False
        for char in l:
            if char == end:
                newl.append(''.join([start]+newl2+[end]))
                startmerge = False
            elif char == start:
                newl2 = []
                startmerge = True
            if startmerge and char != start:
                newl2.append(char)
            elif char != end and char != start:
                newl.append(char)
        return newl

    '''
    splits a string into lists
    like string.split(), but will add the split charecter into the list
    Note: use str.partition() for single splits
    '''
    @classmethod
    def split(self, s, char):
        l = s.split(char)
        for i, thing in enumerate(l):
            l[i] = [thing, char]
        flatten(l)
        del l[len(l)-1]
        return l

    '''
    splits a string into lists with re
    '''
    @classmethod
    def resplit(self, s, char, supresserror=True):
        import re
        try: finds = re.search(s, char)
        except AttributeError:
            if supresserror:
                return s
            else:
                raise
        l = re.split(char, s)
        
