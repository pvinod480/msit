class Election:
    def __init__(self,year,fobj):
        self.w_name=w_name
        self.r_name=r_name
        self.party=party
        self.w_votes=w_votes
        self.r_votes=r_votes
        self.gender=gender
        self.year=year
        self.fobj=fobj
        
    def seatspartywon(self,fobj):
        parties={}
        for line in self.fobj:
            sp=line.split()
            party=sp[4]
            if party in parties:
                parties[party]+=1
            else:
                parties[party]=1
            print(parties)
import re
pat='[^0-9]'
files=["Elections2004.txt","Elections2009.txt","Elections2014.txt"]
for filename in files:
    year=re.sub(pat,'',filename)
    fobj=open(filename,'r')
    elec=Election(fobj)
    players.append(elec)
for pl in players:
    pl.seatspartywon()
    
