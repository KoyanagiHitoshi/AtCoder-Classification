A=int(input())
for k in range(10,10**4+1):
    N=str(k)
    f=0
    for n in range(len(N)):
        f+=int(N[n:n+1])*(k**(len(N)-n-1))
    if f==A:
        print(k)
        break
else:
    print(-1)