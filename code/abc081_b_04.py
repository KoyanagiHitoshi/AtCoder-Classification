input()
A=list(map(int,input().split()))
ans=0
while all(a%2==0 for a in A):
    A=[a/2 for a in A]
    ans+=1
print(ans)