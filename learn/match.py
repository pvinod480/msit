class Match:
    def __init__(self):
        self.females={}
        self.males={}
        fobj=open("records.txt","r")
        for line in fobj:
            fields=line.split()
            gender=fields[1]
            name=fields[0]
            age=int(fields[2])
            salary=int(fields[3])
            if gender =="f":
                self.females[name]={"age":age,"salary":salary}
            else:
                self.males[name]= {"age":age,"salary":salary}
                
                
    def distance(self,male,female):
        from math import sqrt
        ages= (self.males[male]["age"] - self.females[female]["age"])**2
        salarys=(self.males[male]["total_sal"] - self.females[female]["total_sal"])**2
        distance=sqrt(ages+salarys)
        return distance

    def recommendFemale(self,male):
             distances = []
             for female in self.females:
                         dist =self.distance(male,female)
                         distances.append((dist, female))
             distances.sort()
             return distances[0][1]
            
    def Normalize(self):
        total_sal=[]
        for male in self.males:
            sal=self.males[male]["salary"]
            total_sal.append(sal)
        for female in self.females:
            sal=self.females[female]["salary"]
            total_sal.append(sal)
            
        max_sal=max(total_sal)
        min_sal=min(total_sal)
        #print(max_sal,min_sal)
        avg=max_sal-min_sal
        
        for male in self.males:
            self.males[male]["total_sal"]=(self.males[male]["salary"]-min_sal)/avg
        for female in self.females:
            self.females[female]["total_sal"]=(self.females[female]["salary"]-min_sal)/avg
            
    def show(self):
        print("----------------------------------MALES--------------------------------------------")
        for name,details in self.males.items():
            print(name,end=" ")
            print(self.males[name]["age"],end=" ")
            print(self.males[name]["salary"],end=" ")
            print(self.males[name]["total_sal"])
           
            
            
        print("----------------------------------FEMALES--------------------------------------------")
        for name,details in self.females.items():
                print(name,end=" ")
                print(self.females[name]["age"],end=" ")
                print(self.females[name]["salary"],end=" ")
                print(self.females[name]["total_sal"])
        
c1=Match()
c1.Normalize()
print(c1.recommendFemale("murali"))
#print(c1.distance("murali","mary"))
#c1.show()



