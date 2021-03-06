class Players:
    def __init__(self):
        self.players ={}

        try:
            fobj = open("players.txt","r")
            for line in fobj:
                fields = line.split()
                name = fields[0]
                players = fields[1:]

                for player in players:
                    self.addElement(name,player)
        except:
            pass
       
    def addElement(self,name,player):
        if name in self.players:
            if player  not in self.players[name]:
                self.players[name].append(player)
        else:
            self.players[name] = [player]

    def removePlayer(self,name,player):
        if name in self.players:
            if player in self.players[name]:
                self.players[name].remove(player)


    def save(self):
        fobj = open("players.txt","w")
        for name in self.players:
            fobj.write(name+" ")
            for player in self.players[name]:
                fobj.write(player+" ")
            fobj.write("\n")
        fobj.close()

    def show(self):
        for name in self.players:
            print(name,end = " ")
            for player in self.players[name]:
                print(player,end=" ")
            print()

    def mostPopularPlayer(self):
        populars = {}
        finals = []
        for players in self.players.values():
            for name in players:
                if name in populars:
                    populars[name] = populars[name]+1
                else:
                    populars[name] = 1
        for name,count in populars.items():
            finals.append((count,name))
        finals.sort()
        return finals[-1][-1]
   
    def __bool__(self):
        if len(self.players) == 0:
            return False
        else:
            return True

    def __eq__(self,obj):
        if self.players == obj.players:
            return True
        else:
            return False


    def __setitem__(self,name,player):
        if name in self.players:
            if player  not in self.players[name]:
                self.players[name].append(player)
        else:
            self.players[name] = [player]

    def __getitem__(self,name):
        return self.players[name]

    def __add__(self,obj):
        self.addElement(*obj)
        return Players(self)

               
           
       


p1= Players()
p1.show()
#print(dir(p1))
'''if p1:
    print("True")
else:
    print("false")'''
p2= Players()
p2.show()

'''p1["jade"]='amber'
p1["jade"] = "ravi"
print(p1["jade"])'''


#p1.show()

'''p2.players.clear()

print(p1.players)
print()
print(p2.players)
if p2:
    print("True")

else:
    print("False")'''



'''if p1==p2:
    print("Equal")
else:
    print("Not Equal")'''


print(p1+p2)



'''p1.addElement("raj","ambrose")
p1.addElement("milton","dravid")
p1.addElement("chirag","steve")
p1.addElement("veena","panting")
p1.addElement("jane","steve")


p1.addElement("raj","steve")
p1.addElement("sam","mark")
p1.addElement("sam","panting")
p1.addElement("sam","steve")
p1.addElement("sam","chris")
p1.addElement("raj","dravid")
p1.addElement("sam","richards")
p1.addElement("jane","ambrose")
p1.addElement("karthik","virat")

p1.removePlayer("sam","steve")'''
#p1.show()
#p1.save()
#print("Most popular player is "+p1.mostPopularPlayer())
'''
   r={}
        for name in self.players:
            for player in self.players[name]:
                if name in r:
                    if player  not in r[name]:
                        r[name].append(player)
                else:

                    r[name] = [player]
        for name in obj.players:
            for player in self.players[name]:
                if name in r:
                    if player  not in r[name]:
                        r[name].append(player)
            else:
                    r[name] = [player]
'''
