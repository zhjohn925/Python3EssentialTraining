#!/usr/bin/python3

#Regular expressions are a very powerful method of matching patterns in text


import re

def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):   # '|' like 'or'
            print(line, end='')
            
def main1():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)   # '|' like 'or'
        if match:  
            print(match.group())    
            
# sub - substitute            
def main2():
    fh = open('raven.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end='')   # '|' like 'or'

def main3():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)   # '|' like 'or'
        if match:  
            print(line.replace(match.group(), '###'), end='')           
    
#define pattern, then use it over and over again
#pre-compile pattern provides more efficient way since only compile it once
def main4():
    fh = open('raven.txt')
    #pattern = re.compile('(Len|Neverm)ore')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line): 
            print(line, end='')

def main5():
    fh = open('raven.txt')
    #pattern = re.compile('(Len|Neverm)ore')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line): 
            print(pattern.sub('###', line), end='')
            
if __name__ == "__main__": main()
