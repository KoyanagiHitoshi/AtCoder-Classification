N=int(input())
A=list(map(int,input().split()))
base=A[0]
ans=0
for a in A:
    base=max(base,a)
    ans+=base-a
print(ans)