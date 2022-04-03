X,Y=map(int,input().split())
ans=0
if Y-X<=0:
    print(ans)
else:
    ans=(Y-X)//10
    if (Y-X)%10!=0:
        ans+=1
    print(ans)