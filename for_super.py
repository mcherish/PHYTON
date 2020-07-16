class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A,self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")

class C(A,B):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")

test1 = A()
test1
print('#' * 10)
test2 = B()
test2 
print('#' * 10)
test3 = C()
test3