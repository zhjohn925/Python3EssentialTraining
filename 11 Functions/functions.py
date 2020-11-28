#!/usr/bin/python3

#function needs to define first, before calling it
#function with no argument
#function with arguments
#arguments can have default values
#function can have optional arguments
#function with key word arguments
#function can return values
#generator function return iterable object

def main():
    testfunc()
    func_with_optional_arguments(1, 2, 33, 66, 88)
    func_with_key_word_arguments(1,2 3, 66, 77, one=1, two=2, four=4)
    for n in getRange() : print(n, end=' ')
    for i in inclusive_range(0, 25, 1) :
        print(i, end='')
    for i in my_range(25) :
        print(i, end='')
        
def testfunc():
    print('This is a test function')
    
def func_with_optional_arguments(first, second, *args) :
    print(first, second)
    print(args)   #in tuple
    for n in args: print(n, end='')
        
def func_with_key_word_arguments(this, that, other, *args, **kwargs) :
    print(this, that, other)
    print(args)
    print(kwargs['one'], kwargs['two'], kworgs['four'])
    for k in kwargs: print(k, kwargs[k])
        
def getRange() :
    return range(25)

#generator function return iterable object by yield
#work like range()
def inclusive_range(start, stop, step) :
    i = start
    while i <= stop :
        yield i
        i += step
        
def my_range(start=0, stop, step=1) :
    i = start
    while i <= stop :
        yield i
        i += step

def inclusive_range2(*args) :
    numargs = len(args)
    if numargs < 1 : raise TypeError('requires at least one argument')
    elif numargs == 1 :
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2 :
        (start, stop) = args
        step = 1
    elif numargs == 3 :
        (start, stop, step) = args
    else : raise TypeError('requires at most three arguments. got {} arguments'.format(numargs)) 
    i = start
    while i <= stop :
        yield i
        i += step
        

if __name__ == "__main__": main()
