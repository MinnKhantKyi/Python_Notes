# Dunder methods (Data model methods) examples
# x = [1,2,3]
# y = [4,5]
# x+y will output [1,2,3,4,5]#
# This is because list has dunder method to operate x + y 

# When it doesn't have dunder method
from typing import Any


class Person():
    def __init__(self, name):
        self.name = name

p = Person("Tom")
print(p)                # This will output memory address.

# When it has dunder method
class PersonD():
    def __init__(self, name):
        self.name = name

    # eg of one of the dunder methods
    def __repr__(self):
        return f"PersonD({self.name})"
    
    # eg of one of the dunder methods
    def __mul__(self,x):
        if( type(x)) is not int:
            raise Exception("Invalid argument, must be int")
        
        self.name = self.name * x

    # eg of one of the dunder methods
    def __call__(self, y):
        print("Called function ",y)
    
pd = PersonD("Tom")
print(pd)                # This will output -> PersonD(Tom).
pd * 3
print(pd)                # This will output -> PersonD(TomTomTom)
pd(4)
print(pd)               # This will output -> Called function  4