N=int(input())
v=[0]*(N+1)
for i in range(N-1):
    a,b=map(int,input().split())
    v[a]+=1
    v[b]+=1
for i in range(1,N+1):
    if v[i]==N-1:
        print("Yes")
        break
else:
    print("No")