class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
    def override(self):
        print("PARENT override()")
    def altered(self):
        print("parent altered()")

class Child(Parent):
    pass
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("child,before parent altered()")
        super(Child,self).altered()
        print("child,after parent altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

