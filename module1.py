# This is a module that defines a function
def say_hello(self,name):
  print(f"Hello, {name}!")
  print("Hello,",name,"!")
  print("Hello,"+ name +"!")

# This is a module that defines a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
say_hello("kousik")