p,r,t=map(int,input().split())
a=p*((1+r/100)**t)
print(format(a,'.2f'))