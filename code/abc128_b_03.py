n=int(input())
sp=[]
for i in range(n):
    s,p=input().split()
    sp.append([s,int(p),i+1])
sp.sort(key=lambda sp:(sp[0],-sp[1]))
for i in sp:print(i[2])