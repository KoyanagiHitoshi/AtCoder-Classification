N=int(input())
ans=0
for A in range(1,N+1):
    if A*A*A>N:
        break
    for B in range(A,N+1):
        if A*B*B>N:
            break
        ans+=N//(A*B)-B+1
print(ans)