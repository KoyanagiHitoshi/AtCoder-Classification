N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
counter=[0]*N
for i in range(N):
    counter[B[C[i]-1]-1]+=1
ans=0
for a in A:
    ans+=counter[a-1]
print(ans)