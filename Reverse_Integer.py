s=int(input())
c=str(s)
if s<0:
    c=c[1:]
    c=c[::-1]
    print(0-int(c))
else:
    print(int(c[::-1]))
