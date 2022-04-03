from itertools import accumulate
N=int(input())
A=list(map(int,input().split()))
A_add=list(accumulate(A))
A_max=list(accumulate(A,func=max))
A_total=[0]+list(accumulate(A_add))
for k in range(N):
    ans=A_add[k]+A_max[k]*(k+1)+A_total[k]
    print(ans)