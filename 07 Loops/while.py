#!/usr/bin/python3

# while expression

def main():
    # simple fibonacci series
    # The sequence starts with F1=0, F2=1, and the recurrence Fn = Fn−1 + Fn−2 is valid for n > 2
    # 0,1,1,2,3,5,8,13,21,34,55,89,144,...
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 50:
        print(b, end=' ')
        a, b = b, a + b
    #Use 'else' in while loop. when expression is false, do else   
    s = 'this is a string'
    i = 0
    while (i < len(s)) :
        print(s[i], end='')
        i += 1
    else :
        print('else')

if __name__ == "__main__": main()
