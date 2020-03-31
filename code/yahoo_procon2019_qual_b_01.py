l=[]
for i in range(3):
    a,b=map(int,input().split())
    l.append(a)
    l.append(b)
l.sort()
if l[0]!=l[1] and l[1]!=l[2] and l[2]==l[3] and l[3]!=l[4] and l[4]==l[5]:
    print("YES")
elif l[0]!=l[1] and l[1]==l[2] and l[2]!=l[3] and l[3]==l[4] and l[4]!=l[5]:
    print("YES")
elif l[0]==l[1] and l[1]!=l[2] and l[2]==l[3] and l[3]!=l[4] and l[4]!=l[5]:
    print("YES")
else:
    print("NO")