# Class without base class
class Base():
    # Constructor (called by "Base()" when creating an object)
    def __init__(self):
        self.a = "set in Base's constructor"

    def f(self):
        return self.a

    def g(self):
        return "returned from Base's g()"


class Derived(Base):
    # Function with the same name override the base class function.
    def f(self):
        return "returned from Derived's f()"


b = Base()  # Create an object of Base
print(b.f())  # Method call, as usual OO languages
print(b.g())

d = Derived()
print(d.f())
print(d.g())
