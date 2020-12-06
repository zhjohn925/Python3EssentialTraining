#!/usr/bin/python3

# module reference:
# http://docs.python.org/py3k/library/index.html 
# provides liable, efficient, and rich modules

# third party modules
# http://pypi.python.org/pypi
#     "Python 3 packages"
# As example, try to install "bitstring.py"

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)  #operating system
    
    #implement in different platform
    import os
    print(os.name)
    print(os.getenv('PATH')
    print(os.getcwd())  #current working directory
    print(os.urandom(25))
    
    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    type(page)  #this is iterable object
    for line in page: print(str(line, encoding = 'utf_8'), end='')
          
    import random
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
          
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    
# third party modules, use other people' works
# http://pypi.python.org/pypi
#     "Python 3 packages"
# As example, try to install "bitstring.py"      
     import bitstring
     a = bitstring.BitString(bin = '01010101')
     print(a.hex, a.bin, a.uint)

if __name__ == "__main__": main()
