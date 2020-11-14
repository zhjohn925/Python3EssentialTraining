#!/usr/bin/python3

#########################################################################
# - Everything in Python is an object
#   Variables, functions, even code
#   Variables in Python are reference to objects
# - Every object has an ID, Type and Value
#   - ID uniquely identifies a particular instance of an object
#     Can not change for the life of the object
#   - Type identifies the class of an object
#     Can not change for the life of the object
# - Value is the contents of the object
#   Mutable objects can change value, immutable objects can not 
#########################################################################

# 1. All variables in Python are first class objects
#    What looks like a simple variable may be something more complex
#            v = some_object()
#            print(v)
#            v.attrib = 'string'
# 2. Objects in Python may be mutable or immutable
# 3. Mutable objects may change value, immutable objects may not
#     - May look like it's value changes
#     - Distinction is visible using id()
#     - Container objects (tuples, lists, etc) may appear to change value
# 4. Most fundamental types in Python are immutable:
#    - numbers, strings, tuples
# 5. Mutable objects include:
#    - lists, dictionaries, other objects depending upon implementation

def main():
    print("This is the variables.py file.")
    x = 42
    type(x)
    id(x)     #505409528
    x = 43
    id(x)     #505409544 (different)
    x = 42
    id(x)     #505409528 (back to same)
    num = 42 / 9    #float type
    num = 42 // 9   #int type (round down)
    num = round(42 / 9)  #int type (round up)
    num = round(42/9, 2) #float type
    num = 42 % 9   #remainder
    num = int(42.9)   #constructor to create int object
    num = float(42)   #constructor to create float object
    #Use string
    s = "This is a string!"
    s = "This is a\nstring!"   # new line
    s = r"This is a\nstring!"  # raw string. used in regular expression
    n = 42
    s = "This is a {} string!".format(n)
    s = '''\
    This is a string
    line after line
    of text and more
    text.
    '''
    s = """\
    This is a string
    line after line
    of text and more
    text.
    """
    #Use sequences
    x = (1, 2, 3) #immutable 
    x = [1, 2, 3] #mutable
    x.append(5)
    x.insert(0, 7)  # insert at the beginning
    x = 'string'
    x[2]
    x[2:4]   #slice
    for i in x:
        print(i)
    #Use dictionary, mutable    
    d = {'one':1, 'two':2, 'three':3, 'four':4}
    for k in d:
        print(k, d[k])
    for k in sorted(d.keys()): #alphbet order
        print(k, d[k])
    #same as above    
    d = dict(
        one=1, two=2, three=3, four=4
    )
    d['five'] = 5
    #identities
    #int is immutable. the below three have the same id
    x = 42
    id(x)
    id(42)
    y = 42
    id(y)
    x == y  # True
    x is y  # True (id is same)
    #dict is mutable, the below two have the different id
    x = dict(num = 42)
    y = dict(num = 42)
    x == y  # True
    x is y  # False (id is different). x and y point to different objects
    id(x)
    id(y)
    #bool is immutable. the below three have same id
    a = True
    b = True
    id(a)
    id(b)
    id(True)
    
    
    
    

if __name__ == "__main__": main()
