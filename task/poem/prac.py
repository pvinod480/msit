import re
class Poem:
    
    def __init__(self):
        self.poem = []
        fobj=open("poem.txt",'r')
        for  line in fobj:
               self.poem.append(line)
               
    def show(self):
        for line in self.poem:
            print(line.strip())
        print()
#---------------Clean---------------------------------------------
    def clean(self):
         pat='[^A-Za-z0-9]'
         self.poem=([re.sub(pat,"",line) for index,line in enumerate(self.poem)])
        
#-------------------------word frequncy-----------------------------
    def wordfre(self):
        words={}
      for line in self.poem:
            sp=line.split()
            for word in sp:
                if word in words:
                    words[word]=
          #------------------find Word in Lines ----------------------

    def getAllLines(self,word):
            result=[word]
            for index,line in enumerate(self.poem):
                if word in line:
                   result.append((index+1,line))
            return result


    def getAllLines(self,word):
           result= [(index+1,line) for index,line in enumerate(self.poem)  if word in line ]
           result.insert(0,word)
           return result
        
#---------------------------------------------
p1=Poem()
p1.clean()
p1.show()
