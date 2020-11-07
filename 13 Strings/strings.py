#!/usr/bin/python3

#string is object
#string is immutable

def main():
    #string variable is a reference to the string
    s = 'this is a string'
    print(s.upper())
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

if __name__ == "__main__": main()
