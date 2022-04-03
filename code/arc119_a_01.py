N=int(input())
B=1
while 2**B<N:
    B+=1
ans=float("inf")
for b in range(B):
    a=N//(2**b)
    c=N-a*2**b
    ans=min(ans,a+b+c)
print(ans)