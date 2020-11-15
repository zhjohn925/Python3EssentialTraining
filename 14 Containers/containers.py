#!/usr/bin/python3

#tuple - immutable 
#list - mutable
#dict - associate array

def main():
    t = (1,)
    t = (1,2,3)
    t = tuple(range(25))
    t[10] = 10 #bad
    10 in t
    50 in t
    50 not in t
    for i in t : print(t)
    l = [1]
    l = [1,2,3]
    l = list(range(25))
    l[10] = 100 #ok
    10 in l
    20 in l
    for i in l : print(i)
    l.count(5)
    l.index(5)
    l.append(101)
    len(l)
    l.extend(range(20)) #extend any iterable object
    len(l)
    l.insert(0, 25)
    l.remove(12)
    del l[12]
    x.pop()
    x.pop(0) #pop the beginning
    d = {'one' : 1, 'two': 2, 'three':3}
    d = dict(one=1, two=2, three=3)  #constructor, easier to create dict object

if __name__ == "__main__": main()
