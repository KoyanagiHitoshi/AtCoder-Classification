N=int(input())
T=[0]*N
A=[[]]*N
for i in range(N):
    t,k,*a=list(map(int,input().split()))
    T[i]=t
    A[i]=a
flag=[False]*N
flag[-1]=True
for n in range(N-1,-1,-1):
    if not flag[n]:
        continue
    for a in A[n]:
        flag[a-1]=True
print(sum(T[i] for i in range(N) if flag[i]))