n=int(input())
m=int(input())
n1,m1=0,0
for i in range(1,n):
    if n%i==0:
        n1+=i
for i in range(1,m):
    if m%i==0:
        m1+=i
if n==m1 and m==n1:
    print('Amicable')
else:
    print('Not Amicable')
