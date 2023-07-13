# Metaclass is class that can create claas.
# In Python, class is also an object.
# By using metaclass, we can create object on the fly(dynamically).
# Ref: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

# type() is aslo metaclass
# type(name, bases, attrs)
# name: name of the class
# bases: tuple of the parent class (for inheritance, can be empty)
# attrs: dictionary containing attributes names and values


Test = type("Test", (),{"x":5})
t = Test()
t.hello = "Hello from class on the fly..."      # Add attribute to a class
print(t)                # <__main__.Test object at 0x000002102E92E490>
print(t.x)              # 5
print(t.hello)          # Hello from class on the fly... 

class Foo():
    def show(self):
        print("Hi from base class...")

def add_attribute(self):
    self.y = 10

Test_Two = type("Test_two", (Foo,), {"x":5, "add_attribute": add_attribute})
t = Test_Two()
t.show()                    # Hi from base class...
t.add_attribute()
print(t.y)                  # 10
