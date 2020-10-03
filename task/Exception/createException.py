class NotAString(Exception):
    
    def __init__(self,element):
        
        self.element=element
        
    def __str__(self):
        return "String is {}".format(self.element)

    
class StringList(list):
    
    def append(self,element):
        if type(element)==str:
            list.append(self,element)
        else:
            #create obj
            #print Obj
            raise NotAString(element)
       
s1 = StringList()
s1.append("python")
print(s1)

#s1.append(75)
#print(s1)
