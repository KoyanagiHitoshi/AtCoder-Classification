N,X=map(int,input().split())
total=0
for i in range(N):
    V,P=map(int,input().split())
    total+=V*P
    if total>X*100:
        print(i+1)
        break
else:
    print(-1)