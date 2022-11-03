a=int(input())
b=int(str(a)[::-1])
c=a**2
d=int(str(b**2)[::-1])
if c==d:
    print(True)
else:
    print(False)
