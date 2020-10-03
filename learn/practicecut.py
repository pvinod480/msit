import argparse
import re
parser=argparse.ArgumentParser()
parser.add_argument("-d",type=str,dest='delimt',required=True)
parser.add_argument("-f",type=str,dest='fields',default="all")

parser.add_argument('filename',nargs='?')

args=parser.parse_args()

delimt=args.delimt
fields=args.fields
filename=args.filename

#print("delimit={},fields={},filename={}".format(delimt,fields,filename))
if filename:
    fobj=open(filename,"r")
else:
    import sys
    fobj=sys.stdin.readlines()

def Isvalid(fields):
    pat='^\d+(,\d+)*$'
    if re.match(pat,fields):
        return True
    return False

def validIndexses(component,fields):
    indexes=[]
    fields=fields.split(",")
    for field in fields:
        if int(field)>0 and int(field)<=len(component):
            indexes.append(int(field)-1)
    indexes.sort()
    return indexes
            
            
if Isvalid(fields):
    for line in fobj:
        component=line.strip().split(delimt)
        indexes=validIndexses(component,fields)
        for index in indexes:
            print(component[index],end=" ")
        print()
else:
    for line in fobj:
        print(line)
        
    
    












