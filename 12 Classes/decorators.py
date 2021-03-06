#!/usr/bin/python3

#Use decorator in the object.  used  to access database

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)
    
    @property
    def color(slef) :
        return self.properties.get('color', None)
    
    @color.setter
    def color(self, c) :
        self.properties['color'] = c    #save to database
        
    @color.deleter
    def color(self):
        del self.properties['color']   #delete from database

def main():
    donald = Duck()
    donald.color = 'blue'
    print(donald.color)

if __name__ == "__main__": main()
