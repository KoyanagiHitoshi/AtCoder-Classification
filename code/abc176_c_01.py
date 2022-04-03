N=int(input())
A=list(map(int,input().split()))
base=A[0]
ans=0
for a in A:
    if a<base:
        ans+=base-a
    else:
        base=a
print(ans)