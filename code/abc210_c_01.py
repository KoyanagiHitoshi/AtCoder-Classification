import collections
N,K=map(int,input().split())
c=list(map(int,input().split()))
kinds=collections.Counter(c[:K])
ans=len(kinds)
for i in range(N-K):
    kinds[c[i]]-=1
    kinds[c[i+K]]+=1
    if kinds[c[i]]==0:
        del kinds[c[i]]
    ans=max(ans,len(kinds))
print(ans)