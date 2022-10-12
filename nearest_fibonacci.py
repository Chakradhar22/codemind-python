n=int(input())
if n==0 or n==1:
    print(n)
l=[0,1]
if n>1:
    a=0
    while True:
        if a>n:
            break
        a=l[-1]+l[-2]
        l.append(a)
    if l[-1]-n > n-l[-2]:
        print(l[-2])
    elif l[-1]-n==n-l[-2]:
        print(l[-2],l[-1])
    else:
        print(l[-1])
