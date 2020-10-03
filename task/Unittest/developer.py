def mean(x):
    return sum(x)/len(x)

def median(x):
    x.sort()
    if len(x)%2==0:
        t = int(len(x)/2)
        temp1 = x[t]
        temp2 = x[t-1]
        dif = (temp1+temp2)/2
        return dif
    else:
        t = int(len(x)/2)
        temp1 = x[t]
        return temp1

def mode(x):
    count={}
    for num in x:
        if num in count :
            count[num]+=1
        else:
            count[num]=1
    result =max(count,key=count.get)
    return result
