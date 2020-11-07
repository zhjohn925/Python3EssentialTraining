#!/usr/bin/python3

def main():
    #'r': read mode as default 
    #'rt': text mode; 'rb': binary mode
    #'w': write; 'a': append; 'r+': read and write
    #f is file object
    f = open('lines.txt')
    for line in f:
        print(line, end = '')
        
def main1():
    f = open('lines.txt', 'r')
    for line in f.readlines():
        print(line, end = '')
    print('Done.')
        
#copy file        
def main2():
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')
    for line in infile:
        print(line, file=outfile, end = '')
    print('Done.')    
        
#large file. do not want to read line by line to copy
#instead, use buffer I/O
#copy file        
def main3():
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer) :
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done.')
    
#copy binary file, Bad demo
def main4():
    f = open('olives.jpg')
    for line in f:
        print(line, end='')
        
#copy binary file ie. image files
def main5():        
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer) :
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done.')


if __name__ == "__main__": main()
    

