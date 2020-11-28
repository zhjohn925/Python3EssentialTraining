#!/usr/bin/python3

# Classes are how you create your own objects
# A class is the blueprint for an object
# An object is an instance of a class

class Duck:
    def __init__(self, color='white') :   #constructor
        #name with "_", this attribute used in local, 
        #not access this variable outside the object
        #use getter and setter
        self._color = color   #_color attached to objects, not to the class
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def setColor(self, color) :
        self._color = color   
        
    def getColor(self) :
        return self._color

def main():
    donald = Duck()
    print(donald)
    donald.quack()   #self is donald,  'donald' is passed magically
    donald.walk()
    donald1 = Duck('blue')

if __name__ == "__main__": main()
