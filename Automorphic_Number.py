n=int(input())
m=n**2
n=str(n)
m=str(m)
if m[-len(n):]==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
