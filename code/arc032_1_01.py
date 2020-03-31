N=int(input())
S=sum(n for n in range(N+1))
flag=0
for s in range(2,S):
    if S%s==0:
        flag=1
print("WANWAN" if flag==0 and N!=1 else "BOWWOW")