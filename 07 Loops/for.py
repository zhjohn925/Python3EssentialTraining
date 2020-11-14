#!/usr/bin/python3

def main():
    fh = open('lines.txt')
    #readlines() is called iterator, which takes one object at a time from sequence objects
    #for loop works with iterator
    # line is a variable to hold object each time
    for line in fh.readlines():
        print(line)
        #print(line, end='')
    #iterate by using enumerate to introduce index   
    for index, line in enumerate(fh.readlines()) :
        print(index, line, end="")
    s = 'this is a string'
    for i, c in enumerate(s) :
        if c == 's' :
            print('index {} is an s'.format(i))
    s = 'this is a string'
    for c in s:
        if c=='s' : break
        print(c, end='')
     s = 'this is a string'
    for c in s:
        if c=='s' : continue
        print(c, end='')   
    #Use 'else' with for loop
    s = 'this is a string'
    for c in s:
        print(c, end='')
    else :
        print('else')
    #str is container, containing characters     
    for s in 'string' :
        print(s)
    for n in [1, 2, 3, 4, 5]:
        print(n, end=' ')
        

if __name__ == "__main__": main()
