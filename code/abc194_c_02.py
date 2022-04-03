from collections import Counter
N=int(input())
A=list(map(int,input().split()))
count=Counter(A)
ans=0
for i in range(-200,201):
    for j in range(-200,201):
        ans+=count[i]*count[j]*(i-j)**2
print(ans//2)