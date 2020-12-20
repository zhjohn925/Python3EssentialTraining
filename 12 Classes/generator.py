#!/usr/bin/python3

# iterable class / object

class Inclusive_range:
    def __init__(slef, *args) :
        numargs = len(args)
        if numargs < 1 : raise TypeError('requires at least one argument')
        elif numargs == 1 :
          self.stop = args[0]
          self.start = 0
          self.step = 1
        elif numargs == 2 :
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3 :
            (self.start, self.stop, self.step) = args
        else : raise TypeError('requires at most three arguments. got {} arguments'.format(numargs))    

     def __iter__(self) :
        i = self.start
        while i <= self.stop
           yield i     #like return , but return to next call starts from the beginning
           i += self.step    # yield to next call starts from the same point from last return
            
def main():
    o = Inclusive_range(0, 25, 1)   # constructor
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
