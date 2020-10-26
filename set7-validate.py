class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def setAge(self,age):
        if age<60:
            self._age=age
    def getAge(self):
        return self._age
    age=property(getAge,setAge)

p1=Person("vinod",23)
print(p1.age)
p1.age=49
print(p1.age)
