x=[1,2,3,4,1,2,3,1,2]
count={}
l=[]
li=[]
for num in x:
        if num in count :
            count[num]+=1
        else:
            count[num]=1
for key,value in count.items():
        l.append(value)
        li.append((value,key))

for v in li:
        if max(v)==
_size=len(l)
print(count)

repeated = []
for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if l[i] == l[j] and l[i] not in repeated: 
                repeated.append(l[i]) 
print(repeated)
