class A:
    def show(self):
        print("ini show A")

class B(A):
    def show(self):
        print ("ini show B")

class C(A):
    def show(self):
        print("ini show C ")

class D(B,C):
    pass

objek = D()
objek.show()

objek2=C()
objek2.show()

objek3=B()
objek3.show()

objek4=A()
objek4.show()