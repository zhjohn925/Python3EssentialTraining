#!/usr/bin/python3

#string is object
#string is immutable

def main():
    #string variable is a reference to the string
    s = 'this is a string'
    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())
    'This is a string'.upper()
    'This is a string {}'.format(42)
    'This is a string %d' % 42
    s3 = 'this is {}, that is {}'
    s3.format(a, b)
    s3 = 'this is {1}, that is {0}'   #specify positional order
    s3.format(a, b)
    'this is {bob} and that is {fred}'.format(bob=a, fred=b)
    d = dict(bob=a, fred=b)  #apply dictionary
    'this is {bob} and that is {fred}'.format(**d)
    s.find('is')
    s.replace('this', 'that')  #remember string is immutable
    id(s)
    newstring = s.upper()
    id(newstring)
    ' This is a string '.strip()  #remove white space, include new-line
    ' This is a string '.rstrip() #remove white space on the right
    s1 = 'This is a string \n'
    s1.rstrip('\n')
    s1.isalnum()  #False since there are space in s1
    'thisisastring'.isalnum() #True
    'thisisastring'.isalpha() #True
    '12345'.isdigit() #True
    s1.isprintable() #True  

if __name__ == "__main__": main()
