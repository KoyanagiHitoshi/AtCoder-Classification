N=10**5
prime=[1]*(N+1)
prime[0]=prime[1]=0
for i in range(2,int(N**.5)+1):
    if not prime[i]:
        continue
    for j in range(i*2,N+1,i):
        prime[j]=0
 
check=[0]*(N+1)
for n in range(N+1):
    if n%2==1 and prime[n] and prime[(n+1)//2]:
        check[n]=1
 
accumulate=[0]*(N+1)
for n in range(1,N+1):
    accumulate[n]=accumulate[n-1]+check[n]
 
Q=int(input())
for q in range(Q):
    l,r=map(int,input().split())
    print(accumulate[r]-accumulate[l-1])