#!/usr/bin/python3

def main():
    print("This is the ops.py file.")
    5 + 5
    5 * 5
    5 - 3
    5 / 3
    5 // 3 
    5 % 3
    divmod(5, 3)
    num = 3
    num += 1
    num -= 1
    num *= 2
    num /= 3
    num //= 5
    #bitwise binary
    0b0101   # 5 (print decimal)
    def b(n) : print('{:08b}'.format(n))    
    b(5)
    x, y = 0x55, 0xaa
    b(y)
    b(x | y)
    b(x & y)
    b(x ^ y)
    b(x << 4)
    b(x >> 4)
    b(~x)
    #Comparison
    5 < 6
    5 <= 6
    7 >= 6
    5 == 5
    5 != 6
    x, y = 5, 6
    id(x)
    id(y)
    x is y
    x is not y
    y = 5   #immutable variables have same id if they have same values
    id(y)
    x is y
    x, y = [5], [5]  #mutable variables have different id
    id(x)
    id(y)
    x == y   #test values of objects 
    x is y   #test identities of objects
    

if __name__ == "__main__": main()
