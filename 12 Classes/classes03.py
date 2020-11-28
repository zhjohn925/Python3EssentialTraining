
#!/usr/bin/python3

# inherit

Class Animal :
  def talk(self) : print('I have something to say')
  def walk(self): print('Hey ! I am walking here!')
  def clothes(self) : print('I have nice clothes')


class Duck(Animal) :
    def __init__(self, color='white') :   #constructor
        #name with "_", this attribute used in local, 
        #not access this variable outside the object
        #use getter and setter
        self._color = color   #_color attached to objects, not to the class
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
        print('Walks like a duck.')
        
    def setColor(self, color) :
        self._color = color   
        
    def getColor(self) :
        return self._color
      
class Dog(Animal) :
  pass

def main():
    donald = Duck()
    print(donald)
    donald.quack()   #self is donald,  'donald' is passed magically
    donald.walk()
    donald1 = Duck('blue')
    
    fido = Dog()
    fido.clothes()

if __name__ == "__main__": main()
