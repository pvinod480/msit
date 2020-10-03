import os

def Directory_Size(lists):
    big=[]
    total_size = 0
    for l in lists:
        for path, dirs, files in os.walk(l):
                for f in files:
                    fp = os.path.join(path, f)
                    #total_size += os.path.getsize(fp)
                    st = os.stat(fp)
                    total_size+=st[6]
        big.append(total_size)
    print("Size of each Directory : ",big)
    return max(big)
entity=int(input("How many directory : "))
lists=[]
for inputs in range(1,entity+1):
    path=input("Enter path of directory {} : ".format(inputs))
    lists.append(path)
result = Directory_Size(lists)
print("Biggest Directory : {} KB ".format(result/1024))

