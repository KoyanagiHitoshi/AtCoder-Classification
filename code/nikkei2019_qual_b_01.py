N=int(input())
A=list(input())
B=list(input())
C=list(input())
ans=0
for i in range(N):
    if A[i]==B[i] and B[i]==C[i]:
        ans+=0
    elif A[i]==B[i] or B[i]==C[i] or A[i]==C[i]:
        ans+=1
    else:
        ans+=2
print(ans)