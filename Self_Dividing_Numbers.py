a=int(input())
b=int(input())
for i in range(a,b+1,1):
    if i%10!=0:
        i=str(i)
        for j in i:
            if int(i)%int(j)==0:
                r=True
            else:
                r=False
                break
        if r==True:
            print(int(i), end = ' ')