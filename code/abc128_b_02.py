n=int(input())
SP=[]
for i in range(n):
    s,p=input().split()
    SP+=[[s,int(p),i+1]]
SP.sort(key=lambda A:(A[0],-A[1]))
for sp in SP:print(sp[2])