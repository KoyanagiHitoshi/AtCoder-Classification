s=int(input())
a=[]
while (s not in a):
    a.append(s)
    if s%2==0:
        s//=2
    else:
        s=3*s+1
print(len(a)+1)