N,K=map(int,input().split())
a=list(map(int,input().split()))
div,mod=divmod(K,N)
A=set(sorted(a)[:mod])
for i in range(N):
    if a[i] in A:
        print(div+1)
    else:
        print(div)