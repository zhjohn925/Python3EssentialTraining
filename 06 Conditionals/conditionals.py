#!/usr/bin/python3

# if statement: only one of statement is executed

def main():
    a, b = 0, 1
    if a > b:
        print('a is greater than b')
    else :
        print('a is less than or equal to b')
    if a > b:
        print('a is greater than b')
    elif a == b :   #can be multiple of elif
        print('a is equal to b')
    else :
        print('a is less than b')
    v = 'a is greater than b' if a > b else 'a is less than or equal to b'
    print(v)
    #switch
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    v = 'five'
    print(choices[v])   #no error handler
    print(choices.get(v, 'other'))
        
if __name__ == "__main__": main()
