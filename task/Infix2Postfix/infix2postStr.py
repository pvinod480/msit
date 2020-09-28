for i in range(3):
    exp=input("Enter Your Expression :")
    pre={'*':2,'/':2,'+':1,'-':1}
    stack=[]
    p_num=' '
    out=''
    for ch in exp:
        if ch in pre:
            out+=p_num
            p_num=0
            while stack and pre[ch]<=pre[stack[-1]] :
                        out+=stack.pop()
            stack+=ch
        else:
            p_num=ch
    stack.append(p_num)
    while stack:
        out+=stack.pop()
    print(out)
