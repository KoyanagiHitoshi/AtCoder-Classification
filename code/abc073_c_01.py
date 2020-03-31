from collections import Counter
N=int(input())
A=Counter([int(input()) for i in range(N)])
ans=0
for count in A.values():
    if count%2:
        ans+=1
print(ans)