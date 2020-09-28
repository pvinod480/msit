class Players:
    
    def __init__(self):
        self.players = {}
        try:
            fobj=open("player.txt",'r')
            for  line in fobj:
                sp=line.split()
                name=sp[0]
                fields=sp[1:]
                for player in fields:
                    self.addElement(name,player)
        except:
                pass

    def addElement(self,name,player):
        if name in self.players:
            if player not in self.players[name]:
                self.players[name].append(player)
        else:
            self.players[name]=[player]

    def mostpopular(self):
        populars={}
        li=[]
        for key,value in self.players.items():
            for fans in value:
                if fans  in populars:
                    populars[fans]+=1
                else:
                    populars[fans]=1
        for name,fans in populars.items():
                li.append((fans,name))
        li.sort()
        print(li[-1][-1])

    def remove_key():
        if name in slef.players:
            if player in self.players[name]:
                self.players[name].remove(player)

    def remove_value(self,name):
        
        if name in self.players:
            del self.players[name]
                        
    def save(self):
       fobj=open("player.txt",'w')
       for name in self.players:
            fobj.write(name+' ')
            for player in self.players[name]:
                 fobj.write(player+" ")
            fobj.write('\n')
            fobj.close
            
        
    def show(self):
        for name in self.players:
            print(name,end=" ")
            for player in self.players[name]:
                print(player,end=" ")
            print()

p1=Players()

'''
p1.addElement("raj","steve")
p1.addElement("sam","mark")
p1.addElement("vin","kum")
p1.addElement("vin","luv")
p1.addElement("kum","luv")
p1.addElement("akhil","vamsi")
p1.addElement("akhil","vinnu")
'''

p1.mostpopular()
p1.save()
#p1.show()

