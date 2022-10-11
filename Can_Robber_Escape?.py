n=int(input())
s=list(map(int,input().split()))
ev,od=0,0
for i in s:
    if i%2==0:
        ev+=1
    else:
        od+=1
if od>2:
    print("NO")
else:
    print("YES")