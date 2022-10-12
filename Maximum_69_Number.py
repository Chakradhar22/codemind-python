n=input()
for i in range(len(n)):
    if n[i]=='6':
        n=n[:i]+'9'+n[i+1:]
        break
print(int(n))