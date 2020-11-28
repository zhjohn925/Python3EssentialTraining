#!/usr/bin/python3

# Classes are how you create your own objects
# A class is the blueprint for an object
# An object is an instance of a class

class Duck:
    def __init__(self, **kwargs) :  
        self._variables = kwargs  
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def setVariable(self, k, v) :
        self._variables[k] = v   
        
    def getVariable(self, k) :
        return self._variables.get(k, None)  #if key (k) is not found, return None

def main():
    donald = Duck(feet = 2)
    print(donald.getVariable('color'))
    print(donald.getVariable('feet'))
    donald.setVariable('color', 'blue')
    print(donald.getVariable('color'))

if __name__ == "__main__": main()
