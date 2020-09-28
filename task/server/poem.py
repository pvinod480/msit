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
        for index,line in enumerate(self.poem):
            self.poem[index]=re.sub(pat," ",line)
            
    def clean(self):
        pat='[^A-Za-z0-9]'
        f=lambda line : re.sub(pat," ",line) 
        self.poem=list(map(f,self.poem))
        
    def clean(self):
        pat='[^A-Za-z0-9]'
        self.poem=[re.sub(pat," ",line) for index,line in enumerate(self.poem)]
        
#-------------------------word frequncy-----------------------------
    def wordfre(self):      
        word_fre = {}
        for line in self.poem :
            sp=line .split()
            for word in sp:
                     if word  in word_fre: 
                            word_fre[word]+=1
                     else:
                            word_fre[word]=1
#------------------find Word in Lines ----------------------

    def getLines(self,word):
            result=[word]
            for index,line in enumerate(self.poem):
                if word in line:
                   result.append((index+1,line))
                   
            return result


    def getLines(self,word):
           result= [(index+1,line) for index,line in enumerate(self.poem)  if word in line ]
           result.insert(0,word)
           return result
        
#---------------------------------------------
if __name__ == "__main__":
    p1=Poem()
    p1.clean()
    p1.show()
