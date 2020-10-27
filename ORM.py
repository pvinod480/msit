class Alpha:
    def fun(self):
        print("Class Alpha")


class Beta:
    def fun(self):
        print("Class Beta")



class B(Alpha):
    print("B")

class C(Beta):
    print("C")
   
class A(C,B):
    def Ram(self):
        print("Ram Dev")



    #Traceback (most recent call last):
    #File "C:/Users/ravi/OneDrive/Desktop/MSIT_Python/OOPS/Inheritance.py", line 30, in <module>
    #class C(A, B):
    #TypeError: Cannot create a consistent method resolution
    #order (MRO) for bases A, B


#------------------------------------------------------------------------
obA = A()
obA.fun()
