f=int(input())
l=int(input())
for i in range(f,l+1,1):
    i=str(i)
    for j in range(len(i)//2):
        if i[j]!=i[-(j+1)]:
            break
    else:
        print(i,end=" ")