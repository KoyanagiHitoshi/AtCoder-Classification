N,K=map(int,input().split())
a=list(map(int,input().split()))
div,mod=divmod(K,N)
A=set(sorted(a)[:mod])
for i in range(N):
    print(div+(a[i] in A))