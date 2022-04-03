N=int(input())
B=1
while 2**B<N:
    B+=1
ans=N
for b in range(B):
    a=N//(2**b)
    c=N%(2**b)
    ans=min(ans,a+b+c)
print(ans)