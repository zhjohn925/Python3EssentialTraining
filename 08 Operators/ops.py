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
    True and False
    True and True
    False or True
    False or False
    True & True  #bitwise
    True & False #bitwise
    #slice operator
    list = [1,2,3,4,5,6,7,8,9]
    list[0]
    list[len(list)-1]
    list[-1]
    list[0:5]
    range(0, 10)
    for i in range(0,10): print(i)   #the last index is excluded
    list[:] = range(20)
    list[1:15:3]   #every other 3
    list[1:15:3] = (99, 99, 99, 99)
    
    

if __name__ == "__main__": main()
