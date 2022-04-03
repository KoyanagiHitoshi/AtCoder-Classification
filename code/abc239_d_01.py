prime=[True]*201
prime[0]=False
prime[1]=False
for p in range(15):
    if prime[p]:
        for i in range(p*p,201,p):
            prime[i]=False
A,B,C,D=map(int,input().split())
for x in range(A,B+1):
    if all(not prime[x+y] for y in range(C,D+1)):
        print("Takahashi")
        exit()
print("Aoki")