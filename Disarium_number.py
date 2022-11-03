s=input()
c=1
su=0
for i in s:
    su+=int(i)**c
    c+=1
if su==int(s):
    print(True)
else:
    print(False)
