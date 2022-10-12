n=int(input())
a=str(n*n)
s=0
for i in a:
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")