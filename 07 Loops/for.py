#!/usr/bin/python3

def main():
    fh = open('lines.txt')
    #readlines() is called iterator, which takes one object at a time from sequence objects
    #for loop works with iterator
    # line is a variable to hold object each time
    for line in fh.readlines():
        print(line)
        #print(line, end='')
    #str is container, containing characters     
    for s in 'string' :
        print(s)
    for n in [1, 2, 3, 4, 5]:
        print(n, end=' ')
        

if __name__ == "__main__": main()
