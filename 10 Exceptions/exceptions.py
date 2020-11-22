#!/usr/bin/python3
#Exceptions are the key method of handling errors in Python
#"try" something, then catch exception with "except"
#You may raise your own exceptions with "raise"

def main1() :
    try:
       f = open('filename')
    except IOError as e:
        print(e)
    else :
        for l in f: print(l)

def main2() :
    try :
        f = open('xlines.txt')
    except IOError as e:
        print('Could not open the file:', e)
    else :
        for line in f: print(line.strip())
            
def main2() :
    try :
        f = open('xlines.txt')
        for line in f: print(line.strip())
    except IOError as e:
        print('Could not open the file:', e)
        
def main3() :
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except ValueError as e:
        print('cannot read file:', e)

def readfile(filename) :
    if filename.endswith('.txt') :        
        f = open(filename)
        return f.readlines()
    else :
        raise ValueError('Filename must end with .txt')

def main():
    
            
def main():
    x = 0
    y = 3
    z = y/x

if __name__ == "__main__": main()
