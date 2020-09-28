for i in range(3):
    exp=input("Enter Your Expression :")
    pre={'*':2,'/':2,'+':1,'-':1}
    stack=[]
    p_num=0
    out=[]
    for ch in exp:
        if ch in pre:
            out.append(p_num)
            p_num=0
            while stack and  pre[ch] <= pre[stack[-1]]:
                        out.append(stack.pop())
            stack.append(ch)
        else:
            p_num=(p_num*10)+int(ch)
    stack.append(p_num)
    while stack:
        out.append(stack.pop())
    print(out)
