n=int(input())
m=int(n**0.5)
for i in range(0,n+1):
    if i*(i+1)==n or n==0:
        print('YES')
        break
else:
    print('NO')