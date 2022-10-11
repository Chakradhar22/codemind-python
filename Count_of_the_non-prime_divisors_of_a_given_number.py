n=int(input())
count=0
for i in range(1,n+1,1):
    if n%i==0:
        c=0
        for j in range(2,n,1):
            if i%j==0:
                c+=1
        if c!=1:
            count+=1
print(count)